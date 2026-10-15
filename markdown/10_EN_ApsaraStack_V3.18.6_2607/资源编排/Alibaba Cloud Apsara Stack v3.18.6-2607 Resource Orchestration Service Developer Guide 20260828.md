---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 172
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%B5%84%E6%BA%90%E7%BC%96%E6%8E%92/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Resource%20Orchestration%20Service%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Resource Orchestration Service Developer Guide 20260828

## Getting started

### Usage notes on development

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

### Call an API operation

Apsara Stack allows you to call API operations by using the point of presence (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterprise V3.16.0. This topic describes how to call API operations in Apsara Stack by using the POP gateway.

**Note**

You can still call API operations by using the ASAPI gateway if you are using an earlier version of Apsara Stack Enterprise. For more information, see Call API operations by using the ASAPI gateway, Obtain the endpoint of ASAPI, and Obtain the ASAPI SDK.

**Flowchart**

**Procedure**

1. Obtain AccessKey credentials.
Obtain the AccessKey credentials that are required when you call an API operation. For more information, see Obtain an AccessKey pair or Obtain an STS AccessKey 3-tuple.

**Note**

We recommend that you use the AccessKey pair of a personal account or a Security Token Service (STS) AccessKey 3-tuple to call the API operations of the Apsara Unimanager Management Console and cloud services.
2. Obtain a region ID.
Obtain a region ID that is required when you call an API operation. For more information, see Obtain the values of common header parameters.
3. Obtain an organization ID and a resource set ID.
You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Mana gement Console Developer Guide.

**Note**

When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained and the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is used by default. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is empty by default. If you specify a resource set ID, you must also specify an organization ID.
4. Obtain the API references.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
5. Obtain the endpoint of the cloud service.
6. Obtain an SDK of the cloud service and call an API operation.

## Preparations

### Go to OpenAPI Explorer

You can go to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

**Note**

The first time you log on to the Apsara Uni-manager Management Console, you must follow instructions to change the password of your account. For security purposes, your password must be 10 to 32 characters in length and must contain at least two of the following character types: Letters Digits Special characters, including ! @ # $ %
3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform operations based
on your logon scenarios: Scenario 1: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, follow the on-screen instructions to bind an MFA device. b. Re-enter the username and password as described in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. Scenario 2: You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable MFA** topic in
**Apsara Uni-manager Management Console User Guide** .
5. In the top navigation bar, choose **Products > Application Services > OpenAPI**
**Explorer**.

### Obtain the information and

**the endpoint of an API operation**

To call an API operation of a cloud service, you must familiarize yourself with the information about the operation, including the service code, operation name, and API version.

**Background information**

The information about the API operation provided on the right of the API operation list in the Apsara Uni-manager Management Console is for call reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the Apsara Uni-manager Management Console is different from the information in the developer guide of a cloud service, the information in the developer guide shall prevail.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging**.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, view all API operations of the current version.
7. Click the API operation that you want to call. Obtain the endpoint from the Endpoint
parameter on the Parameter tab. image

### Obtain an AccessKey pair

An AccessKey credential can be assigned by Resource Access Management (RAM) or STS. You can use one of the services to obtain an AccessKey credential for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

The AccessKey ID and AccessKey secret contained in an AccessKey credential are used to implement symmetric encryption and verify the identity of request senders. The AccessKey ID is used to identify a user. The AccessKey secret is a string that is used to encrypt the signature. An AccessKey credential can be assigned by RAM or STS: An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, set the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

**Warning**

The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
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
5. Click **Management AccessKey** on the right side of the page.
6. In the **Management AccessKey** dialog box, view the AccessKey pair of the organization.

### Obtain an STS AccessKey 3-

**tuple**

This topic describes how to use STS to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call API operations in Apsara Stack. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. All the three elements are required when you use STS to call API operations in Apsara Stack. For more information, see What is STS?

**Procedure**

1. Obtain the Alibaba Cloud Resource Name (ARN) of the **RAM role** that is assumed by the
organization that you want to use. i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. iv. In the **View Policies of Current Role** dialog box, select an organization and view the
**RAM Role**.
2. Obtain an STS AccessKey 3-tuple

**Note**

In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourRoleSessionName>: Replace the parameter with the name of the current session. <yourRoleArn>: Replace the parameter with the obtained ARN of the RAM role. <sts.aliyuns.com>: Replace the parameter with the STS endpoint.

```xml
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
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
    // Obtain the STS AccessKey 3-tuple.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace <sts.aliyuns.com> with the STS endpoint in the sts-
vpc.${global:region}.${global:internet-domain} format.
    request.setSysDomain("<sts.aliyuncs.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace <yourRoleArn> with the ARN of the RAM role that is obtained in the pre
vious step.
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
3. Use the AccessKey 3-tuple assigned by STS to call an operation of a service. The following
sample code provides an example on how to use the AccessKey 3-tuple assigned by STS to call the DescribeRegions operation of Resource Orchestration Service (ROS):

**Note**

In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourStsAccesskeyID>: Replace the parameter with your STS AccessKey ID. <yourStsAccessKeySecret>: Replace the parameter with your STS AccessKey secret. <yourStsToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID.

```java
public static void main(String[] args) {
    // Replace <yourRegionID> with the region ID.
    // Replace <yourStsAccessKeyID> and <yourStsAccessKeySecret> with the AccessKey I
D and AccessKey secret obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
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

**header parameters**

You must set header parameters when you call API operations in Apsara Stack. This topic describes the header parameters and how to obtain the values of the parameters. This topic also describes the return values of some parameters after you call API operations.

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization that you want to use.
5. In the **Regions** section, view the region ID.

**Obtain an organization ID**

You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide.

**Response parameters**

The following table describes the response parameters that are returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### Obtain an ROS SDK

To call API operations of ROS in Apsara Stack by using the POP gateway, you must use an ROS SDK. The following table provides links for you to download Alibaba Cloud SDKs and ROS SDKs.

| Alibaba Cloud SDK | ROS SDK |
|---|---|
| Alibaba Cloud SDK for Java | ROS SDK for Java |
| Alibaba Cloud SDK for Python | ROS SDK for Python |
| Alibaba Cloud SDK for Go | ROS SDK for Go |

r Java

## Use ROS SDK for Java

### Get started with ROS SDK for

**Java**

This topic describes how to get started with ROS SDK for Java.

**Prerequisites**

An Apsara Stack tenant account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are obtained. For more information, see Obtain an AccessKey pair. The endpoint of ROS is obtained. For more information, see Obtain the endpoint of ROS. Java Development Kit (JDK)1.8or later is installed.

**Install the SDK**

If you use Apache Maven to manage a Java project, you need to only import the JAR file to the pom.xml file of the project. To use ROS SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and ROS SDK for Java. We recommend that you use the SDK core library of V4.5.17 or later and ROS SDK for Java of V1.0.1 or later.

**Use ROS SDK for Java**

1. Create and initialize a com.aliyun.ros20190910.Client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionId>: Replace the parameter with the region ID. <yourAccessKeyId>: Replace the parameter with your AccessKey ID. <yourAccessKeySecrect>: Replace the parameter with your AccessKey secret. <Endpoint>: Replace the parameter with the endpoint of ROS.

```java
package com.aliyun.sample; import com.aliyun.ros20190910.Client; import com.aliyun.tea.*; import com.aliyun.ros20190910.*; import com.aliyun.ros20190910.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
```

r Java

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
        DescribeRegionsResponse resp =
client.describeRegions(describeRegionsRequest);
```

`}`

```
    public static void getStack(Client client, String stackId, String regionId) throw
s Exception {
        GetStackRequest getStackRequest = new GetStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
        // Run the following code to obtain the response of the API request.
        GetStackResponse resp = client.getStack(getStackRequest);
com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM (resp)));
```

`}`

```
    public static void deleteStack(Client client, String stackId, String regionId) th
rows Exception {
        DeleteStackRequest deleteStackRequest = new DeleteStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
        // Run the following code to obtain the response of the API request.
        DeleteStackResponse resp = client.deleteStack(deleteStackRequest);
com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM (resp)));
```

`}` r Java

```
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.ros20190910.Client client = Sample.createClient();
        CreateStackRequest.CreateStackRequestParameters parameters0 = new
CreateStackRequest.CreateStackRequestParameters()
                .setParameterKey("VpcName")
                .setParameterValue("TestVpc");
        CreateStackRequest.CreateStackRequestParameters parameters1 = new
CreateStackRequest.CreateStackRequestParameters()
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

`}` `}` r Java

### Use SDK

#### Install ROS SDK for Java

This topic describes the two steps that are required to install ROS SDK for Java: obtain ROS SDK for Java and add Maven dependencies.

**Step 1: Obtain ROS SDK for Java**

A JDK of 1.8 or later is required for Alibaba Cloud SDK for Java. To use ROS SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and ROS SDK for Java. The version of the SDK core library must be V4.5.17 or later. The version of ROS SDK for Java must be V1.0.1 or later. For more information, see ROS SDK for Java.

**Step 2: Add Maven dependencies**

When you install ROS SDK for Java, you must add the following dependencies to the pom.xml file:

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

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. ROS SDK for Java allows you to complete the authentication process by using an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access ROS, you must configure the AccessKey pair as the credentials when you initialize a client instance.

**Warning**

Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised. r Java

```java
private static String ACCESSKEYID = "<yourAccessKeyId>"; // Specify your AccessKey ID
```

`.`

```java
private static String SECRET = "<yourAccessKeySecrect>"; // Specify your AccessKey s ecret. private static String REGIONID = "<yourRegionId>"; // Specify the region ID.
```

**Note**

In the preceding code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code.

#### Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

**Note**

You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy. r Java

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

#### Use ROS SDK for Java

This topic describes how to use ROS SDK for Java.

**Procedure**

1. Create an AcsClient instance.

```
new com.aliyun.ros20190910.Client(config)
```

2. Create a request.
Name the request in the ${apiName}Request format. **${apiName}** indicates the name of the API operation that you want to call. Example: GetStack. If multiple client instances are used, different requests may have the same name. You can differentiate the requests based on package names.

```
GetStackRequest getStackRequest = new GetStackRequest()
        .setStackId(stackId)
        .setRegionId(regionId);
```

3. Initiate the request and process the response.

```
GetStackResponse resp = client.getStack(getStackRequest); com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM (resp)));
```

#### Handle errors

r Java When you use ROS SDK for Java, errors may occur. If an error occurs on the ROS server, the SDK returns a `ServerException` error response. If an error occurs on a client instance, the SDK returns a `ClientException` error response. An error response is composed of an error code and an error message. In general, you do not need to handle client instance errors. You need to only handle server errors. If you want to handle client instance errors, you can use the following sample code:

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

`}` r Python

## Use ROS SDK for Python

### Get started with ROS SDK for

**Python**

This topic describes how to get started with ROS SDK for Python.

**Prerequisites**

An Apsara Stack tenant account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are obtained. For more information, see Obtain an AccessKey pair. The endpoint of ROS is obtained. For more information, see Obtain the endpoint of ROS.

**Step 1: Install ROS SDK for Python**

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

**Step 2: Use ROS SDK for Python**

1. Create a client instance. When you create a client instance, you must specify a region ID,
an AccessKey ID, and an AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

In the following code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <ros.aliyuncs.com>: Replace the parameter with the endpoint of ROS. r Python

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkros.request.v20190910.ListResourceTypesRequest import ListResourceTypesRequest
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

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. ROS SDK for Python allows you to complete the authentication process by using an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access ROS, you must configure the AccessKey pair r Python as the credentials when you initialize a client instance.

**Warning**

Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```python
from aliyunsdkcore import client clt = client.AcsClient(secret_id, secret_key, region_id, endpoint=endpoint)
```

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

#### Use ROS SDK for Python

This topic describes how to use ROS SDK for Python.

**Procedure**

r Python
1. Import ROS SDK for Python.

```python
from aliyunsdkcore import client from aliyunsdkros.request.v20190910.ListResourceTypesRequest import ListResourceTypesRequest
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

When you use ROS SDK for Python, errors may occur. If an error occurs on the ROS server, the SDK returns a `ServerException` error response. If an error occurs on a client instance, the SDK returns a `ClientException` error response. An error response is composed of an error code and an error message. In general, you do not need to handle client instance errors. You need to only handle server errors. If you want to handle client instance errors, you can use the following sample code:

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

r Go

## Use ROS SDK for Go

### Get started with ROS SDK for

**Go**

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to use ROS SDK for Go.

**Prerequisites**

An Apsara Stack tenant account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair. An endpoint of ROS is obtained. For more information, see Obtain the endpoint of ROS.

**Step 1: Install the core package of Alibaba Cloud SDK for Go**

Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Step 2: Use ROS SDK for Go**

1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

In the following sample code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <Endpoint>: Replace the parameter with your ROS endpoint. r Go

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
    client, err := sdk.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>",
"<yourAccessKeySecret>")
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

#### Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. ROS SDK for Go allows you to complete the authentication process by using an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access ROS, you must configure the AccessKey pair as the credentials when you initialize a client instance. r Go

**Warning**

Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
// Initialize a client instance. client, err := sdk.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<your AccessKeySecret>")
```

**Note**

In the preceding sample code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code.

#### Handle errors

When you use ROS SDK for Go, errors may occur. If an error occurs on the ROS server, the

| ns a | ServerError |   |
|---|---|---|
| ClientError |   |   |
|   |   | erro |

SDK returns a `ServerError` error response. If an error occurs on a client instance, the SDK returns a `ClientError` error response. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface and can be handled in a similar way as standard Go errors.

**Handle errors**

You can use the following code to handle errors:

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
    // Obtain the error response.
   err.Error()
```

`}`

**ClientError**

When you send a request, if an error occurs on the client instance and cannot be automatically handled, the SDK returns a `ClientError` error response. The following sample code provides an example on how to determine and obtain the error

| message in the | ClientError | error response: |
|---|---|---|
| client, err := sdk.NewClientWithAccessKey("cn-hangzhou-ste4-d01", "<accessKeyId>", "<ac cessSecret>") if clientError, ok := err.(*errors.ClientError); ok{ // Obtain the error code. clientError.ErrorCode() // Obtain the error message. clientError.Message() // Obtain the original error. clientError.OriginError() } |   |   |

r Go

**Note**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Add an error package.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

**ServerError**

When the server returns an error message, the SDK wraps the message into a `ServerError` error response and returns it to the client instance. In this case, you can still obtain the original HTTP response from the error response. The following sample code provides an example on how to determine and obtain the error message in ServerError and Response:

```
response, err := client.ProcessCommonRequest(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

`}`

**Note**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Add an error package.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

#### Use CommonRequest to call API

**operations**

r Go If you want to call the API operations of an Apsara Stack service that does not provide SDKs, or the requests and responses of the API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations. The following sample code provides an example on how to query details of a stack by calling the GetStack operation of ROS.

**Note**

In the following sample code, replace the variable parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the variable parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <ros.aliyuncs.com>: Replace the parameter with the endpoint of the service. <yourSecurityToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID. r Go

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
    request.Domain = "<ros.aliyuncs.com>" // The endpoint of the service. Replace the s
ample value with the actual endpoint of the service.
    request.Version = "2019-09-10"
    // The name of the API operation. This parameter is required because the operation
is to be called by using the Remote Procedure Call (RPC) style.
    request.ApiName = "GetStack"
    // The business parameters.
    request.QueryParams["RegionId"] = "<yourRegionID>"
```

`/*`

```
     When you use STS AccessKey credentials to call an RPC API operation, you must add
the SecurityToken field in the request parameters.
     You can use the following syntax to specify this field:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Replace the field value with your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. The source
of the call.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify the regio
n ID.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Spe
cify the resource set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Speci
fy the organization ID.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` e API calls

## Use POP to make API calls

### Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

To enable you to call API operations in the same way as that in Alibaba Cloud public cloud and have a more convenient and consistent experience, we recommend that you use the POP gateway to call API operations in Apsara Stack.

**Obtain service endpoints**

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

e API calls To use the POP gateway to call API operations in Apsara Stack, you must obtain the required service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers You can also obtain service endpoints by yourself. In this example, API Gateway is used.
1. Log on to the Apsara Uni-manager Operations Console.
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

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain the values of common request headers.

### SDK for Java

Before you call the SDK for Java to access the endpoint of a cloud service by using the Point of Presence (POP) gateway, you must familiarize yourself with the call style of the cloud service. The following call styles are supported: remote procedure call (RPC) and resource-oriented architecture (ROA).

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack API operations. To view the recommended SDK version and sample code, perform the following operations: Log on to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Products** >
**Application Services** > **OpenAPI Explorer**. In the top navigation bar of the page that
appears, choose **API Integration** > **SDK Sample Code**.

**Important**

We recommend that you do not download SDKs fromSDK Centerand use them in Apsara Stack. The SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues. Proceed with caution.

**Call example of CommonRequest**

This section provides an example on how to call an API operation by using CommonRequest. In this example, the Resource Orchestration Service (ROS) service, the ListStacks operation, and the 2019-09-10 version are used. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient;
```

e API calls

```java
import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
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
        request.setSysDomain("<ROSEndpoint>");
        // Specify the API version.
        request.setSysVersion("2019-09-10");
        // Specify the service name.
        request.setSysProduct("ROS");
        // Specify the name of the API operation.
        request.setSysAction("ListStacks");
        // If you use the Security Token Service (STS) AccessKey pair to call RPC API o
perations, you must specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // (Required) Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // (Optional) You must specify this parameter for Apsara Stack V3.15.0 or
earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // (Optional) Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // (Required) Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // (Optional) You must specify this parameter when you modify or delete
resources.
```

e API calls

```java
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
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

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can configure the following setting: Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable certificate verification for the client. clientConfig.setIgnoreSSLCerts(true)
```

### SDK for Go

This topic describes how to use the Point of Presence (POP) gateway to call the SDK for Go.

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack API operations. To view the recommended SDK version and sample code, perform the following operations: Log on to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Products** >
**Application Services** > **OpenAPI Explorer**. In the top navigation bar of the page that
appears, choose **API Integration** > **SDK Sample Code**.

**Important**

We recommend that you do not download SDKs fromSDK Centerand use them in Apsara Stack. The SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues. Proceed with caution. e API calls

**Background information**

Remote procedure call (RPC) and resource-oriented architecture (ROA) styles are supported for API calls.

**Call example of CommonRequest**

This section provides an example on how to call an API operation by using CommonRequest. In this example, the Resource Orchestration Service (ROS) service, the ListStacks operation, and the 2019-09-10 version are used. Sample code: e API calls

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
cessKey Secret>")
    request := requests.NewCommonRequest()
    // Configure the parameters for the API operation of ROS.
    request.Product = "ROS"
    request.Version = "2019-09-10"
    request.ApiName = "ListStacks"
    // Specify the endpoint of ROS.
    request.Domain = "ros.inter.env230.shuguang.com"
    // Specify the request method.
    request.Method = "POST"
    request.Domain = "<ROSEndpoint>"
    // If you use the Security Token Service (STS) AccessKey pair to call RPC API opera
tions, you must specify the SecurityToken parameter.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // (Required) Specify the call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // (Optional) You must specify this parameter for Apsara Stack V3.15.0 or earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // (Optional) Specify the ID of the resource set.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // (Required) Specify the organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // (Optional) You must specify this parameter when you modify or delete resources.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
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

You can configure a proxy by using one of the following methods when you call API operations: Method 1: Configure a proxy by using environment variables. Specify the HTTP_PROXY and HTTPS_PROXY environment variables, or specify the NO_PROXY environment variable. e API calls Sample code:

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
// The proxy that is configured on the client takes precedence over the proxy that is configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL verification**

**Digest**

You can configure SSL certificate verification for requests. If you set the HTTPSInsecure parameter to `true` , SSL certificate verification is disabled. To ensure security, we recommend that you enable SSL certificate verification. If you set the HTTPSInsecure parameter to `false` , SSL certificate verification is enabled. By default, certificate authority (CA) certificates on the OSs are used.

**Default value**

The default value is `false` .

**Settings**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can configure the following settings: e API calls

```
// If you specify the HTTPSInsecure parameter for the request, the setting takes effect only for the current request. request.SetHTTPSInsecure(true) // Set the HTTPSInsecure parame ter for the request to true. isInsecure := request.GetHTTPSInsecure() // Query the setting of the HTT PSInsecure parameter for the request.
```

The HTTPSInsecure setting takes effect for the client only when you do not specify the HTTPSInsecure parameter for the request.

```
// If you specify the HTTPSInsecure parameter for the client, the setting takes effect for all requests that are initiated by the client. client.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter for the client to true. isInsecure := client.GetHTTPSInsecure() // Query the setting of the HTTPSI nsecure parameter for the client.
```

### SDK for Python

This topic describes how to use the SDK for Python to call the API of a cloud service by using the Point of Presence (POP) gateway.

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack API operations. To view the recommended SDK version and sample code, perform the following operations: Log on to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Products** >
**Application Services** > **OpenAPI Explorer**. In the top navigation bar of the page that
appears, choose **API Integration** > **SDK Sample Code**.

**Important**

We recommend that you do not download SDKs fromSDK Centerand use them in Apsara Stack. The SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues. Proceed with caution.

**Background information**

Only the remote procedure call (RPC) style is supported for API calls.

**Call example of CommonRequest**

This section provides an example on how to call an API operation by using CommonRequest. In this example, the Resource Orchestration Service (ROS) service, the ListStacks operation, and the 2019-09-10 version are used. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
"<A
```

`K` `S`

```
t>"
```

e API calls

|   | "<AccessKey Secret>", "<your-RegionID>", timeout=1000, # Specify the timeout period. verify=False, # Disable SSL certificate verification. If you want to enable SSL cer tificate verification, set the verify parameter to '<Path of the certificate>'. ); # Use the client setting together with the HTTPS or HTTP request protocol. # client.set verify(False) _ # os.environ["HTTPS PROXY"] = "http://127.0.0.1:8080" _ # os.environ["HTTP PROXY"] = "http://127.0.0.1:8080" _ def describe api groups(): _ _ # Create a request and configure the request parameters. request = CommonRequest() # If you use the Security Token Service (STS) AccessKey pair to call RPC API operat ions, you must specify the SecurityToken parameter. # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your- SecurityToken>"}; params = {"PageSize":"10","PageNumber":"1"}; request.set query params(params) _ _ headers = { # (Required) Specify the call source. "x-acs-caller-sdk-source":"ApiTestDemo", # (Optional) Specify the region ID. You must specify this parameter for Apsara Stack V3.15.0 or earlier. "x-acs-regionid":"<your-RegionID>", # (Optional) Specify the ID of the resource set. "x-acs-resourcegroupid":"<your-ResourceGroupID>", # (Required) Specify the organization ID. "x-acs-organizationid":"<your-OrganizationID>" # (Optional) You must specify this parameter when you modify or delete resources. # "x-acs-instanceid":"<your-InstanceID>" } request.set headers(headers) _ request.set version("2019-09-10") _ request.set action name("ListStacks") _ _ request.set endpoint("<ROSEndpoint>") // Replace the ROSEndpoint part with the ac _ tual endpoint. request.set product("ROS") _ request.set method("POST") _ # Specify the request protocol. request.set protocol type('http') _ _ # Initiate the API request and obtain the response. response = client.do action with exception(request) _ _ _ print(response) if name == ' main ': __ __ __ __ print("Hello Aliyun OpenApi!") describe api groups() |   |
|---|---|---|

e API calls

```
    describe_api_groups()
```

**Proxy settings**

You can configure a proxy for an API call by specifying the HTTP_PROXY or HTTPS_PROXY environment variable. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS settings**

This section describes how to send an API request over HTTPS.

**Use HTTPS**

By default, the SDK uses HTTPS as the request protocol.

```
from aliyunsdkros.request.v20190910.ListStacksRequest import ListStacksRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Specify the region ID.
```

`)`

```
request = ListStacksRequest() request.set_protocol_type('https') # Use the HTTPS protocol. client.do_action_with_exception(request)
```

**Disable certificate verification**

**Important**

By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can set the `verify` parameter to false.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Specify the region ID.
    verify=False  # Disable SSL certificate verification.
```

`)`

**Enable certificate verification**

e API calls

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Specify the region ID.
    verify='./cacert.pem'  # Specify the path of the certificate authority (CA) certifi
cate.
```

`)`

## API Reference

### List of operations by function

The following tables list the API operations available for use in ROS.

**Stack operations**

| Operation | Description |
|---|---|
| CreateStack | Creates a stack. |
| ContinueCreateStack | Creates another stack based on the template of the previous stack that failed to be created. |
| UpdateStack | Updates a stack. |
| CancelUpdateStack | Cancels the update of a stack. |
| GetStack | Queries the information about a stack. |
| DeleteStack | Deletes a stack. |
| ListStacks | Queries the information about stacks. |
| PreviewStack | Previews the information about a stack that you want to create by using a specific template. |
| ListStackEvents | Queries a stack and its resource events. |

**Resource operations**

| Operation | Description |
|---|---|
| GetResourceTypeTemplate | Queries the template of a resource by resource type. |
| ListStackResources | Queries the resources of a specific stack. |
| GetStackResource | Queries the information about a resource in a specific stack. |

| GetResourceType | Queries the details of a resource type. |
|---|---|

**Template operations**

| Operation | Description |
|---|---|
| ValidateTemplate | Validates the template that is used to create a stack. |
| GetTemplate | Queries the details of a template. |
| DeleteTemplate | Deletes a template. |
| ListTemplates | Queries templates. |
| CreateTemplate | Creates a custom template. |
| UpdateTemplate | Updates a template. |
| GetTemplateSummary | Queries the information about a new or existing template. |

**Other operations**

| Operation | Description |
|---|---|
| DescribeRegions | Queries available regions. |
| SignalResource | Sends signals. |
| ListStackOperationRisks | Detects resources that may face high risks caused by a stack deletion operation, and queries the reason for each risk. |

### Request method

To send a Resource Orchestration Service (ROS) API request, you must send an HTTPS GET or POST request to the ROS endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8.

**Request syntax**

ROS API operations use the Remote Procedure Call (RPC) protocol. You can call ROS API operations by sending HTTPS GET or POST requests. The following example describes the request syntax of an ROS API request:

```
https://Endpoint/?Action=xx&Parameters
```

The following table describes the parameters in the request syntax.

| Parameter | Description |
|---|---|
| Endpoint | The endpoint of the ROS API. Set the value to ros.aliyuncs.com. |
| Action | The name of the operation being performed. For example, to query the list of stacks, you must set the Action parameter to ListStacks. |
| Parameter s | The request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common request parameters and operation-specific parameters. Common parameters include information such as the API version number and authentication information. For more information, see Common parameters. |

**Sample request**

The following example demonstrates how to call the ListStacks operation to query the list of stacks:

```
https://ros.aliyuncs.com/?Action=ListStacks &RegionId=cn-hangzhou-180e-d01 &Format=JSON &Version=2019-09-10 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dg**** &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI******************** &Timestamp=2020-06-01T12:00:00Z ...
```

### Request signatures

You must sign all API requests to ensure security. Alibaba Cloud uses the request signature to verify the identity of the API caller. Each API request must contain the signature, regardless of whether the request is sent over HTTP or HTTPS.

**Overview**

You must add the signature to the ROS API request in the following format:

```
https://Endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=CT9X0VtwR86fNWSnsc6v8YGOjuE%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e 0ad82fd6cf
```

A signature contains the following parameters:
**SignatureMethod**: the encryption method of the signature string. Set the value to HMAC-
SHA1.
**SignatureVersion**: the version of the signature encryption algorithm. Set the value to 1.0.
**SignatureNonce**: a unique, random number used to prevent replay attacks. You must use
different random numbers for different requests. We recommend that you use universally unique identifiers (UUIDs).
**Signature**: the signature generated after the request has been symmetrically encrypted by
using the AccessKey secret. The signature encryption algorithm complies with RFC 2104 HMAC-SHA1 specifications. The AccessKey secret is used to calculate the hash-based message authentication code (HMAC) value of the encoded and sorted query string, and the HMAC value is used as the signature string. Request signatures include operation-specific parameters. Therefore, the signature of a request varies based on the request parameters. To calculate a signature, follow the steps in this topic.

```
Signature = Base64( HMAC-SHA1( AccessKey Secret, UTF-8-Encoding-Of(StringToSign)) )
```

**Step 1: Compose and encode a string-to-sign**

1. Create a canonicalized query string by using the request parameters.
i. Create a canonicalized query string by arranging the request parameters (including all common and operation-specific parameters except Signature) in alphabetical order.

**Note**

If you use the GET method to submit the request, these parameters are the part located after the question mark (?) and connected by the ampersands (&) in the request uniform resource identifier (URI). ii. Encode the names and values of the arranged request parameters in the request URL by using the unicode transformation format (UTF)-8 character set. The following table describes the encoding rules.

| Character | Encoding rule |
|---|---|
| Uppercase letters, lowercase letters, digits, hyphens (-), underscores ( ), periods (.), _ and tildes (~) | These characters do not need to be encoded. |
| Other characters | These characters must be percent encoded in %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22 . |
| Extended ASCII characters (UTF-8) | These characters are encoded in %XY%ZA... format. |
| Spaces | Spaces must be encoded as %20 . Do not encode spaces as plus signs (+). This encoding method is different from the application/x- www-form-urlencoded MIME encoding algorithm (such as the java.net.URLEncoder class provided by the Java standard library). However, you can apply the encoding algorithm and replace the plus sign (+) in the encoded string with %20 , the asterisk (*) with %2A , and the tilde (~) with %7E . You can use the following percentEncode method to implement this algorithm: private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value ! = null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; } |

|   | www-form-urlencoded |   |
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

A string-to-sign contains the following parameters:
**HTTPMethod**: the HTTP method used to submit a request, such as GET.
**percentEncode("/")**: specifies the encoded value (%2F) of a forward slash (/). The
encoding follows the URL encoding rules.
**percentEncode(CanonicalizedQueryString)**: specifies the encoded canonicalized
query string based on the URL encoding rules.

**Step 2: Calculate the signature string**

1. Calculate the HMAC value of the string-to-sign based on RFC 2104.

**Note**

Use the SHA1 algorithm to calculate the HMAC value of the string-to-sign. The combination of your AccessKey secret and an ampersand (&) (ASCII code 38) that follows the secret is used as the key for the HMAC calculation.
2. Encode the HMAC value in Base64 to obtain the signature string.
3. Add the signature string to the request as the **Signature** parameter.

**Note**

When the obtained signature value is submitted as the final request parameter value, the value must be URL-encoded that is similar to other parameters based on rules defined in RFC 3986.

**Example**

| DescribeRegions |   | oper |
|---|---|---|
| ess when |   |   |

The `DescribeRegions` operation is used in this example. This example shows the signature process when `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret:
1. Create a canonicalized query string.

```
http://ros.aliyuncs.com/?Timestamp=2019-08- 23T12%3A46%3A24Z&Format=XML&AccessKeyId=testid&Action=DescribeRegions&SignatureMethod=H C-SHA1&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&Version=2019-09-10&Signatu reVersion=1.0
```

2. Create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3DXML%26SignatureMetho 3DHMAC-SHA1%26SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf%26SignatureVersion%3D1.0%26Timestamp%3D2019-08- 23T12%253A46%253A24Z%26Version%3D2019-09-10
```

3. Calculate the signature. Because `AccessKeySecret` is set to testsecret, the key value used

| for calculation is | testsecret& | . |
|---|---|---|
| OLeaidS1JvxuMvnyHOwuJ+uX5qY= |   |   |

`OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . The Java Base64 encoding method is used in this example.

```
Signature = Base64( HMAC-SHA1( AccessSecret, UTF-8-Encoding-Of(StringToSign) ) )
```

4. Add the Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D string that has been encoded based
on RFC 3986 to the URL in Step 1.

```
http://ros.aliyuncs.com/? SignatureVersion=1.0&Action=DescribeRegions&Format=XML&SignatureNonce=3ee8c1b8-83d3-4 4af-a94f-4e0ad82fd6cf&Version=2019-09- 10&AccessKeyId=testid&Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D&SignatureMethod=HMAC- SHA1&Timestamp=2019-08-23T12%253A46%253A24Z
```

You can use browsers or tools such as cURL and Wget to initiate an HTTP request by using the new URL. The HTTP request calls the `DescribeRegions` operation to query the Alibaba Cloud region list.

### Common parameters

This topic describes the common request and response parameters.

**Common request parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Default value: JSON. Valid values: JSON XML |
| Version | String | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Set the value to 2019- 09-10. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Set the value to HMAC- SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. Example: 2020-01- 10T12:00:00Z. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

Sample requests:

```
https://ros.aliyuncs.com/?Action=XXXXXX &Format=xml &Version=2019-09-10 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dg**** &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI******************** &Timestamp=2020-06-01T12:00:00Z
```

**Common response parameters**

Responses can be returned in the JSON or XML format. You can specify the response format in the request. The default response format is JSON. Every response returns a unique
**RequestId** value regardless of whether the call is successful.
A `2xx` HTTP status code indicates a successful call. A `4xx` or `5xx` HTTP status code indicates a failed call. Sample responses XML format

```xml
<?xml version="1.0" encoding="utf-8"?>
    ><!--Result root node-->
    <Operation name + Response>
        <!--Response request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!--Returned data-->
    </Operation name + Response>
```

JSON format `{`

```json
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216"
    /*Returned data*/
```

`}`

### Common error codes

This topic describes the common client and server error codes.

**Client error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| UnknownError | The request processing has failed due to some unknown error. | 400 | The error message returned because an unknown error that is not caused by a server-side issue has occurred on the client. |
|   | The input parameter {name} should be specified. | 400 | The error message returned because the input parameter is missing. name indicates the parameter name. |

| Developer Guide·API R | eference Resource Orchestration Servic |   |   |
|---|---|---|---|
| MissingParameter |   |   |   |
|   | One of the input parameters {names} should be specified. | 400 | The error message returned because the input parameter is missing. You must specify one of the input parameters. names indicates the names of all the related parameters. |
|   | The input parameter {name} should be specified, {reason}. | 400 | The error message returned because the input parameter is missing. name indicates the parameter name, and reason indicates the specific reason. |
| InvalidParameter | The specified parameter {name} is invalid. | 400 | The error message returned because the specified parameter is invalid. name indicates the parameter name. |
|   | The specified parameter {name} is invalid, {reason}. | 400 | The error message returned because the specified parameter is invalid. name indicates the parameter name, and reason indicates the specific reason. |
| MultipleParameter | Only one of the input parameters {names} can be specified. | 400 | The error message returned because the number of specified parameters exceeds the limit. You can specify only one of the parameters. names indicates the names of all the related parameters. |
| InvalidIdempotence Parameter | The specified parameters are different from before. | 400 | The error message returned because the idempotent token is the same, but the specified parameters are different from before. |
| LastTokenProcessin g | The last token request is processing. | 400 | The error message returned because the previous token request is being processed. Try again later. |
| Invalid | Data supplied was not valid: {reason}. | 400 | The error message returned because the value is invalid. reason indicates the specific reason. |
| InvalidValue | {reason}. | 400 | The error message returned because the value is invalid. reason indicates the specific reason. |

| RequestLimitExcee ded | Request limit exceeded: {reason}. | 400 | The error message returned because the request contains content that exceeds the limit. reason indicates the specific reason. You can change the part of content that exceeds the limit by adjusting the quota. |
|---|---|---|---|
| NotSupported | {feature} is not supported. | 400 | The error message returned because a specified feature is not supported. feature indicates the specific feature or operation. |
| MismatchNextToke n | {name} mismatches next token. | 400 | The error message returned because the specified parameter does not match the next token. name indicates the parameter name. |
| AssumeRoleFailure | Fail to assume role {name}: {reason} | 400 | The error message returned because ROS has failed to obtain a temporary identity to assume the specified RAM role. name indicates the RAM role name, and reason indicates the specific reason for the failure. |
| Forbidden | You are not authorized to complete this action. | 403 | The error message returned because you are not authorized to complete this action. |
|   | A required authorization for the specified action {api} is not supplied. Code: {code} RequestId: {request id} _ | 403 | The error message returned because you have not authorized ROS to call the operation. api indicates the name of the operation. code indicates the error code. request id indicates the ID of _ the request. |
| AccountTypeNotSu pported | Account type not supported. | 403 | The error message returned because the specified account type is not supported. |
| NotFound | {reason}. | 404 | The error message returned because the request contains content that does not exist. reason indicates the specific reason. |

**Server error codes**

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|

| InternalError | Server error. | 500 | The error message returned because an internal error has occurred. |
|---|---|---|---|
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 | The error message returned because a server error has occurred. Try again later. If the problem persists, submit a ticket. |

### Stack operations

#### CreateStack

You can call this operation to create a stack.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateStack | The operation that you want to perform. Set the value to CreateStack. |
| Parameters.N.Pa rameterKey | String | Yes | InstanceId | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Note Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.Parameter Key and Parameters.N.Parameter Value. |

| Parameters.N.Pa rameterValue | String | Yes | i-xxxxxx | The value of parameter N. Maximum value of N: 200. Note Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.Parameter Key and Parameters.N.Parameter Value. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackName | String | Yes | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a _ digit or letter. |
| DisableRollback | Boolean | No | false | Specifies whether to disable rollback on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |
| TemplateBody | String | No | { "ROSTemplateF ormatVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| TimeoutInMinute s | Long | No | 10 | The timeout period that is specified for the stack creation request. Default value: 60. Unit: minutes. |
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| NotificationURLs .N | RepeatL ist | No | http://my- site.com/ros- event | The callback URL for receiving stack event N. Only HTTP POST is supported. Maximum value of N: 5. Each URL can be up to 1,024 bytes in length. ROS sends a notification to the specified URL when the stack state changes. If rollback is enabled on the stack, notifications are sent if the stack is in the CREATE ROLLBACK or _ ROLLBACK state, but are not sent when the stack is in the CREATE FAILED or UPDATE FAILED _ _ state. Note ROS does not send notifications when the stack is in the IN PROGRESS state. _ Notifications are sent regardless of whether the Outputs parameter is specified. The following code is an example of a notification: |

|   |   |   |   | { "Outputs": [ { "Description": "No description given", "OutputKey": "InstanceId", "OutputValue": "i-xxx" } ], "StackId": "80bd6b6c- e888-4573-ae3b- 93d29113****", "StackName": "test- notification-url", "Status": "CREATE COMPLETE" _ } |
|---|---|---|---|---|
|   |   |   |   | The name of the RAM role. ROS |
| RamRoleName | String | No | test-role | assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

| DeletionProtecti on | String | No | Enabled | Specifies whether to enable deletion protection on the stack. Default value: Disabled. Valid values: Enabled: enables deletion protection on the stack. Disabled: disables deletion protection on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Note The deletion protection property of a nested stack is the same as that of its root stack. |
|---|---|---|---|---|
| CreateOption | String | No | KeepStackOnCre ationComplete | Specifies whether to delete the stack after it is created. Default value: KeepStackOnCreationComplete. Valid values: KeepStackOnCreationComplete: retains the stack and all its resources after the stack is created. AbandonStackOnCreationComplet e: deletes the stack but retains all its resources after the stack is created. This helps you ensure that the maximum number of stacks allowed to be created is not reached. If the stack fails to be created, the stack is retained. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

**Examples**

Sample requests

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
| InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |

| InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |
|---|---|---|---|
| InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| InvalidTemplateSectio n | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
| InvalidTemplateVersio n | The template version is invalid: {reason}. | 400 | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| StackValidationFailed | {reason}. | 400 | The error message returned because the stack validation failed. reason indicates the specific reason. |
| UnknownUserParamet er | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |

| UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
|---|---|---|---|
| ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |
| StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack with the same name already exists. name indicates the stack name. |

#### ContinueCreateStack

Creates a stack based on the template of the previous stack that fails to be created.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ContinueCreate Stack | The operation that you want to perform. Set the value to ContinueCreateStack. |
| Parameters.N.Pa rameterKey | String | Yes | Amount | The key of template parameter N to be overridden. If the key and value of the parameter are not specified, the key and value are set to those in the template of the stack that fails to be created. Maximum value of N: 200. Note This parameter takes effect only when the Mode parameter is set to Recreate. |

| Parameters.N.Pa rameterValue | String | Yes | 12 | The value of template parameter N to be overridden. Maximum value of N: 200. This parameter takes effect only when the Mode parameter is set to Recreate. Take note of the following limits on the template parameter to be overridden: This parameter cannot change values in the Conditions section of the template from true to false or from false to true. This parameter can be referenced only by resources that are recreated. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RecreatingResou rces.N | RepeatL ist | No | WebServer | The resource N to be recreated upon creation failure. ROS recreates the resources you list in this parameter and all resources that depend on the resources. |
| RamRoleName | String | No | test-role | The name of the Resource Access Management (RAM) role. Resource Orchestration Service (ROS) assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permissions to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

| Mode | String | No | Recreate | The stack recreation mode. Default value: Recreate. Valid values: Recreate Only the following types of resources are recreated: Resources that fail to be created Resources specified in the RecreatingResources.N parameter Resources that depend on the resources specified in the RecreatingResources.N parameter Resources for which creation operations are not initiated The RecreatingResources.N, TemplateBody, TemplateURL, and Parameters parameters take effect only when the Mode parameter is set to Recreate. Ignore: ROS ignores and discards all resources that fail to be recreated and the resources for which creation operations are not initiated. Then, the stack creation operation is marked as successful. Content of the template is changed. |
|---|---|---|---|---|

| TemplateBody | String | No | { "ROSTemplateF ormatVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. This parameter takes effect only when the Mode parameter is set to Recreate. Take note of the following limits on the template: Only the Description, Metadata, Resources, and Outputs sections in the template can be modified. No sections can be added to or removed from the outermost layer of the template. Take note of the following limits on the Resources section of the template: The resources not to be recreated cannot be deleted, and their template content cannot be modified. The resources to be recreated can be deleted, and their template content can be modified. New resources can be added. |
|---|---|---|---|---|

| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Object Storage Service (OSS) bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou.The template can be up to 524,288 bytes in length. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. This parameter takes effect only when the Mode parameter is set to Recreate. For information about the limits on the template specified in this parameter, see the description of the TemplateBody parameter. |
|---|---|---|---|---|
| DryRun | Boolean | No | false | Specifies whether to check the validity of the request without actually making the request. Default value: false. Valid values: true: checks the validity of the request without actually making the request. false: makes the request to recreate the stack. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/?Action=ContinueCreateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
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
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is invalid. reason indicates the specific reason. |
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |

| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
|---|---|---|---|
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | The error message returned because the template contains an invalid section. section indicates the section name. |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |
| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
| 400 | UnknownUserParamet er | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 400 | ContinueCreateStackV alidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |

| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the specified stack. name indicates the resource name, and stack indicates the stack name or ID. |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### UpdateStack

You can call this operation to update a stack. The values of Parameters and UsePreviousParameters in the request are related. If parameters defined in the template are not specified by Parameters, take note of the following items: When UsePreviousParameters is set to false, if the parameter has a default value in the template, the default value is used. If the parameter does not have a default value in the template, you must specify the parameter in the Parameters section. When UsePreviousParameters is set to true, if the parameter is specified when the stack is created, the specified value is used. If the parameter is not specified and it has a default value in the template, the default value is used.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateStack | The operation that you want to perform. Set the value to UpdateStack. |

| Parameters.N.Pa rameterKey | String | Yes | Amount | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Note Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.Parameter Key and Parameters.N.Parameter Value. |
|---|---|---|---|---|
| Parameters.N.Pa rameterValue | String | Yes | 12 | The value of parameter N. Maximum value of N: 200. Note Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.Parameter Key and Parameters.N.Parameter Value. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

| StackPolicyDurin gUpdateBody | String | No | {"Statement": [{"Effect": "Allow", "Action": "Update:*", "Principal": "*", "Resource": "*"}]} | The structure that contains the body of the temporary overriding stack policy. The stack policy body must be 1 to 16,384 bytes in length. To update protected resources, specify a temporary overriding stack policy during the update. If you do not specify a stack policy, the current policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters: StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
|---|---|---|---|---|
| TimeoutInMinute s | Long | No | 10 | The timeout period that is specified for the stack update request. Default value: 60. Unit: minutes. |
| TemplateBody | String | No | {"ROSTemplate FormatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| StackPolicyDurin gUpdateURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the temporary overriding stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. To update protected resources, specify a temporary overriding stack policy during the update. If you do not specify a stack policy, the current policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters: StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |

| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| UsePreviousPara meters | Boolean | No | true | Specifies whether to use the values that were passed last time for the parameters that you do not specify in the current request. Valid values: true false |
| DisableRollback | Boolean | No | false | This parameter cannot take effect when the stack is being updated. If the update fails, a rollback is performed regardless of the value of this parameter. |
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
|---|---|---|---|---|
| ReplacementOpt ion | String | No | Disabled | Specifies whether to enable replacement update after a resource attribute that does not support modification update is changed. Modification update keeps the physical ID of the resource unchanged. However, the resource is deleted and then recreated, and its physical ID is changed if replacement update is enabled. Default value: Disabled. Valid values: Enable: enables replacement update. Disabled: disables replacement update. Note Modification update takes precedence over replacement update. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

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
| 400 | InvalidSchema | {reason}. | The error message returned because the specified template format is incorrect. reason indicates the specific reason. |

| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
|---|---|---|---|
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | The error message returned because the template contains an invalid section. section indicates the section name. |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |
| 400 | StackPolicyValidationF ailed | Action denied by stack policy: {reason}. | The error message returned because the stack policy validation failed. reason indicates the specific reason. |

| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
|---|---|---|---|
| 400 | UnknownUserParamet er | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### CancelUpdateStack

Cancels the update of a stack.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelUpdateSt ack | The operation that you want to perform. Set the value to CancelUpdateStack. |

| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
|---|---|---|---|---|
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| CancelType | String | No | Safe | The method to cancel the update operation. Valid values: Quick: cancels the update of a stack as soon as possible. Safe: cancels the update of a stack as safely as possible. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/?Action=CancelUpdateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelUpdateStackResponse>
         <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
         <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
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

| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
|---|---|---|---|
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### GetStack

You can call this operation to query information about a stack.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStack | The operation that you want to perform. Set the value to GetStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| CreateTime | String | 2019-08- 01T04:07:39 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
|---|---|---|---|
| Description | String | my stack description | The description of the stack. |
| DisableRollbac k | Boolean | false | Indicates whether rollback is disabled on stack creation failure. Default value: false. Valid values: true: The rollback on stack creation failure is disabled. false: The rollback on stack creation failure is enabled. |
| NotificationUR Ls | List | ["http://127.XX.XX. 1:8080/x", "http://127.0.XX.XX :8080/y"] | The callback URLs for receiving stack events. |
| Outputs | List | [{"Description": "Instance ID","OutputKey": "InstanceId","Outp utValue": "i- a****"}] | The output parameters of the stack. |
| Parameters | Array of Parameter |   | The list of input parameters of the stack. |
| ParameterKey | String | InstanceType | The key of the parameter. |
| ParameterValu e | String | ecs.cm4.6xlarge | The value of the parameter. |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the parent stack. |
| RegionId | String | cn-beijing | The region ID of the stack. |

| Status | String | CREATE COMPLET _ E | The state of the stack. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |
| UpdateTime | String | 2019-08- 01T04:07:39 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |

| StatusReason | String | Stack successfully created | The reason why the stack is in its current state. |
|---|---|---|---|
| TemplateDesc ription | String | Some description | The description of the stack. |
| TimeoutInMinu tes | Integer | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
| DeletionProtec tion | String | Enabled | Indicates whether deletion protection is enabled on the stack. Valid values: Enabled: Deletion protection is enabled on the stack. Disabled: Deletion protection is disabled on the stack. You can release the stack by using the ROS console or by calling the DeleteStack operation. Note The deletion protection property of a nested stack is the same as that of its root stack. |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| RamRoleName | String | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS uses the role previously associated with the stack. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |
| RootStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the root stack. This parameter is returned if the specified stack is a nested stack. |

| StackDriftStat us | String | IN SYNC _ | The drift state of the stack in the last successful drift detection. Valid values: DRIFTED: The stack has drifted. NOT CHECKED: No drift detection has _ been successful on the stack group. IN SYNC: The stack is being _ synchronized. |
|---|---|---|---|
| StackType | String | ROS | The type of the stack. Valid values: ROS: The stack was created based on an ROS template. Terraform: The stack was created based on a Terraform template. |

**Examples**

Sample requests

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

You can call this operation to delete a stack and all of its resources.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteStack | The operation that you want to perform. Set the value to DeleteStack. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| RetainAllResourc es | Boolean | No | false | Specifies whether to retain the resources in the stack. |
| RetainResources .N | RepeatL ist | No | WebServer | The list of resources to retain. |
| RamRoleName | String | No | test-role | The name of the RAM role. ROS assumes the specified RAM role to create the stack and call API operations by using the credentials of the role. All operations are performed under this role. If a RAM user is authorized to perform operations on the stack but does not have the permission to use the role, ROS still uses the role and grants the role the least privilege. If you do not specify this parameter, ROS does not use the role previously associated with the stack. If you want to use a role, you must specify it in this parameter. If no roles are available, ROS uses the temporary credentials generated from the credentials of your account. The RAM role name can be up to 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

**Examples**

Sample requests

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
| 400 | InvalidOperation.Deleti onProtection | Fail to delete stack {ID}, as deletion protection is enabled. | The error message returned because deletion protection prevented the stack from being deleted. ID indicates the stack ID. |
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | The error message returned because the specified stack has a change operation in progress. name indicates the name or ID of the stack, and action indicates the change operation. |

#### ListStacks

Queries the list of stacks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStacks | The operation that you want to perform. Set the value to ListStacks. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| Status.N | RepeatL ist | No | CREATE COMPL _ ETE | The status of stack N. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PR _ _ _ _ OGRESS IMPORT CREATE ROLLBACK FAILE _ _ _ D IMPORT CREATE ROLLBACK COMP _ _ _ LETE IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PR _ _ _ _ OGRESS IMPORT UPDATE ROLLBACK FAILE _ _ _ D IMPORT UPDATE ROLLBACK COM _ _ _ PLETE Valid values of N: 1 to 5. |

| PageSize | Long | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
|---|---|---|---|---|
| ParentStackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the parent stack. |
| StackName.N | RepeatL ist | No | MyStack | The name of stack N. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a _ digit or letter. Fuzzy search with an asterisk (*) is supported. Valid values of N: 1 to 5. |
| PageNumber | Long | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| ShowNestedStac k | Boolean | No | true | Specifies whether to display nested stacks. Default value: false. Valid values: true false Note This parameter is set to true if the ParentStackId parameter is specified. |
| Tag.N.Key | String | No | usage | The key of tag N of the stack. Valid values of N: 1 to 20. |
| Tag.N.Value | String | No | test | The value of tag N of the stack. Valid values of N: 1 to 20. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. If detailed information about the stack is not required, you can use this parameter to replace the GetStack operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Stacks | Array of Stack |   | The list of stacks. |
|---|---|---|---|
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| DisableRollbac k | Boolean | false | Indicates whether rollback is disabled when the stack fails to be created. Default value: false. Valid values: true: Rollback is disabled when the stack fails to be created. false: Rollback is enabled when the stack fails to be created. |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | The time when the latest successful drift detection operation was initiated. |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | The ID of the parent stack. |
| RegionId | String | cn-hangzhou | The region ID of the stack. |
| StackDriftStat us | String | IN SYNC _ | The drift status of the stack in the latest successful drift detection. Valid values: DRIFTED: The stack has drifted. NOT CHECKED: No drift detection has _ been performed on the stack. IN SYNC: The stack is being _ synchronized. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | MyStack | The name of the stack. |
| StackType | String | ROS | The type of the stack. Set the value to ROS, which indicates that the stack was created based on an ROS template. |

| Status | String | CREATE COMPLET _ E | The status of the stack. Valid values: CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |
|---|---|---|---|
| StatusReason | String | Stack successfully created | The reason why the stack is in its current state. |
| TimeoutInMinu tes | Integer | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. |
| UpdateTime | String | 2019-08- 01T04:07:39 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |

| PageSize | Integer | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 1 | The total number of stacks. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/?Action=ListStacks &RegionId=cn-hangzhou &<Common request parameters>
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

You can call this operation to preview the stack to be created by using a specified template.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PreviewStack | The operation that you want to perform. Set the value to PreviewStack. |

| Parameters.N.Pa rameterKey | String | Yes | InstanceType | The key of parameter N. If the key and value of the parameter are not specified, the key and value in the template are used. Maximum value of N: 200. Note Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.Parameter Key and Parameters.N.Parameter Value. |
|---|---|---|---|---|
| Parameters.N.Pa rameterValue | String | Yes | ecs.cm4.6xlarge | The value of parameter N. Maximum value of N: 200. Note Parameters is an optional parameter. If you need to specify Parameters, you must specify both Parameters.N.Parameter Key and Parameters.N.Parameter Value. |
| RegionId | String | Yes | cn-beijing | The region ID of the stack. |
| StackName | String | Yes | MyStack | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a _ digit or letter. |
| DisableRollback | Boolean | No | false | Specifies whether to disable rollback on stack creation failure. Default value: false. Valid values: true: disables rollback on stack creation failure. false: enables rollback on stack creation failure. |

| TimeoutInMinute s | Long | No | 10 | The timeout period that is specified for the stack creation request. Unit: minutes. Default value: 60. |
|---|---|---|---|---|
| TemplateBody | String | No | {"ROSTemplate FormatVersion": "2015-09-01" } | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| StackPolicyURL | String | No | oss://ros-stack- policy/demo | The URL of the file that contains the stack policy. The URL must point to a policy located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/stack- policy/demo and oss://ros/stack- policy/demo?RegionId=cn-hangzhou. The policy can be up to 16,384 bytes in length and the URL can be up to 1,350 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |
| StackPolicyBody | String | No | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length. Note You must specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them. |

| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
|---|---|---|---|---|
| TemplateURL | String | No | oss://ros- template/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template must be 1 to 524,288 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | The ID of the request. |
| Stack | Struct |   | Details about the stack. |
| Description | String | One ECS instance. | The description of the stack. |
| DisableRollbac k | Boolean | false | Indicates whether rollback is disabled. |
| Parameters | Array of Parameter |   | The parameters of the stack. |
| ParameterKey | String | SystemDiskCatego ry | The key of the parameter. |
| ParameterValu e | String | cloud ssd _ | The value of the parameter. |
| RegionId | String | cn-beijing | The region ID of the stack. |

| Resources | Array of Resource |   | The list of resources in the stack. |
|---|---|---|---|
| Description | String | ECS instance. | The description of the resource. |
| LogicalResour ceId | String | WebServer | The logical resource ID. |
| Properties | Map | { "DiskMappings": [ { "Category": "cloud ssd", "Size": _ "20" } ], "SystemDisk Categ _ ory": "cloud ssd", _ "InstanceChargeTy pe": "PostPaid", "AutoRenew": "False", "WillReplace": true, "ImageId": "centos 7", _ "InstanceType": "ecs.g6.large", "AllocatePublicIP": true, "AutoRenewPeriod" : 1, "IoOptimized": "optimized", "ZoneId": "cn- beijing-g", "VSwitchId": "", "SecurityGroupId": "", "Period": 1, "InternetChargeTy pe": "PayByTraffic", "SystemDiskCateg ory": "cloud efficiency", _ "InternetMaxBand widthOut": 1, "VpcId": "", "InternetMaxBand widthIn": 200, "PeriodUnit": "Month" } | The properties of the resource. |
| RequiredBy | List | ["Resource1", "Resource2"] | The list of one or more resources that are dependent on the stack. |
| ResourceType | String | ALIYUN::ECS::Insta nce | The type of the resource. |
| Stack | Map | {} | Details about the nested stacks. The data structure of this parameter is the same as that of the entire responses. |
| StackName | String | MyStack | The name of the stack. |

| StackPolicyBo dy | Map | { "Statement": [ { "Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*" }, { "Action": "Update:*", "Resource": "LogicalResourceId /apple1", "Effect": "Deny", "Principal": "*" } ] } | The stack policy. |
|---|---|---|---|
| TemplateDesc ription | String | One ECS instance. | The description of the template. |
| TimeoutInMinu tes | Integer | 10 | The timeout period. Unit: minutes. |

**Examples**

Sample requests

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
```

```xml
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
                                  <ParameterValue>test-preview-stack-complex-
nested</ParameterValue>
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
                            <StackName>test-preview-stack-complex-nested</StackName>
                            <StackPolicyBody>
                                  <Statement>
                                        <Action>Update:*</Action>
                                        <Effect>Allow</Effect>
                                        <Principal>*</Principal>
                                        <Resource>*</Resource>
                                  </Statement>
                                  <Statement>
```

```xml
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
```

```json
equ edBy:[],
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
|---|---|---|---|
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |

| 400 | StackValidationFailed | {reason}. | The error message returned because the stack validation failed. reason indicates the specific reason. |
|---|---|---|---|
| 400 | UnknownUserParamet er | The Parameter ({name}) was not defined in template. | The error message returned because the specified parameter is not defined in the template. name indicates the parameter key. |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | The error message returned because no value is passed into the specified parameter defined in the template. name indicates the parameter key. |
| 409 | StackExists | The Stack ({name}) already exists. | The error message returned because a stack with the same name already exists. name indicates the stack name. |

#### ListStackEvents

You can call this operation to query stacks and their resource events.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackEvents | The operation that you want to perform. Set the value to ListStackEvents. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |

| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
|---|---|---|---|---|
| Status.N | RepeatL ist | No | CREATE IN PRO _ _ GRESS | The state of resource N. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ UPDATE SKIPPED _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| ResourceType.N | RepeatL ist | No | ALIYUN::ECS::Ins tance | The type of resource N. Maximum value of N: 200. |
| LogicalResourceI d.N | RepeatL ist | No | WebServer | The logical ID of the resource as defined in the template. |
| PageNumber | Long | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Long | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Events | Array of Event |   | The list of events. |
| CreateTime | String | 2019-08- 01T04:07:39 | The time when the task was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |

| EventId | String | 0086612d-77cf- 4056-b0b5- ff8e94ad**** | The ID of the event. |
|---|---|---|---|
| LogicalResour ceId | String | WebServer | The logical ID of the resource as defined in the template. |
| PhysicalResou rceId | String | i- m5e3tfdbinchnexh **** | The physical ID of the resource. |
| ResourceType | String | ALIYUN::ECS::Insta nce | The type of the resource. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | StackName | The name of the stack. |
| Status | String | CREATE COMPLET _ E | The state of the resource. |
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| PageNumber | Integer | 1 | The page number of the returned page. Pages start from page 1. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| TotalCount | Integer | 20 | The total number of returned events. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ListStackEvents &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListStackEventsResponse>
       <Events class="array">
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:56</CreationTime>
                     <EventId type="string">0086612d-77cf-4056-b0b5-ff8e94ad****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">test-describe-
events</LogicalResourceId>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">Stack successfully
updated</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">2b900d01-959b-49a8-8cfe-f7de87aa****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">30f721d4-8124-4fd4-8afd-7b21471f****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:54</CreationTime>
                     <EventId type="string">b5ecc0ac-f855-4503-945c-82d398a2****</EventI
```

`d>`

```
                     <LogicalResourceId
type="string">WaitConditionHandle</LogicalResourceId>
                     <ResourceType
type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
```

`St`

```
kIdt "ti "57d0946 7f44f4 0d43012****/St
```

`kI`

```
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">a01e5730-7244-414e-b9ff-f97e3885****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">262b2f54-7ae7-4cf6-9c8a-eb4d0801****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">163c3965-1617-4787-ba08-1eed0e3a****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">71f7c25c-2ac7-4336-9934-85482111****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>` `d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">a5a0eb9e-7abe-44a1-a376-70955211****</EventI
```

`d>`

```
                     <LogicalResourceId
type="string">WaitConditionHandle</LogicalResourceId>
                     <ResourceType
type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">250f5003-f59d-46f9-8471-65d0c630****</EventI
```

`d>`

```
                     <LogicalResourceId type="string">test-describe-
events</LogicalResourceId>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```
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
```

```json
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

`}` `},` `{`

```json
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "163c3965-1617-4787-ba08-1eed0e3a****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
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

| > Document Version: 202 | 60828 |   | 11 |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

### Resource operations

#### GetResourceTypeTemplate

You can call this operation to query the template of a resource by resource type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetResourceTyp eTemplate | The operation that you want to perform. Set the value to GetResourceTypeTemplate. |
| ResourceType | String | Yes | ALIYUN::ECS::VP C | The type of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 87F54B2B-AEF0- 4C33-A72A- 3F8856A575E9 | The ID of the request. |
| TemplateBody | Map | {"ROSTemplateFor matVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 51,200 bytes in length. |

**Examples**

Sample requests

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
              <ROSTemplateFormatVersion type="string">2015-09-
01</ROSTemplateFormatVersion>
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
| 404 | ResourceTypeNotFoun d | The Resource Type ({name}) could not be found. | The error message returned because the specified resource type does not exist. name indicates the name of the resource type. |

#### ListStackResources

You can call this operation to query the resource list of a specific stack.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListStackResour ces | The operation that you want to perform. Set the value to ListStackResources. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| Resources | Array of Resource |   | The list of resources. |
| CreateTime | String | 2019-08- 01T06:01:23 | The time when the resource was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |
| LogicalResour ceId | String | dummy | The logical resource ID defined in the template. |
| PhysicalResou rceId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | The physical ID of the resource. |

| ResourceDriftS tatus | String | IN SYNC _ | The drift state of the resource in the last successful drift detection. Valid values: DELETED: The actual configuration of the resource differs from its expected template configuration because the resource has been deleted. MODIFIED: The actual configuration of the resource differs from its expected template configuration. NOT CHECKED: ROS has not checked _ whether the actual configuration of the resource differs from its expected template configuration. IN SYNC: The actual configuration of the _ resource matches its expected template configuration. |
|---|---|---|---|
| ResourceType | String | ALIYUN::ROS::Stac k | The type of the resource. |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| StackName | String | test-describe- resource | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |
| Status | String | UPDATE COMPLET _ E | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| StatusReason | String | state changed | The reason why the resource is in its current state. |

| UpdateTime | String | 2019-08- 01T06:01:29 | The time when the resource was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
|---|---|---|---|

**Examples**

Sample requests

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
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
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
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId
type="string">WaitConditionHandle</LogicalResourceId>
                     <PhysicalResourceId type="string"></PhysicalResourceId>
```

```
                     <ResourceType
type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
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
                     <PhysicalResourceId type="string">d04af923-e6b7-4272-aeaa-47ec9777*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
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
"StackName":"test-describe-resource",
```

```json
           StackName: testdescriberesource,
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
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
```

`}` `]` `}`

| Error code | Error message | HTTP status code | Description |
|---|---|---|---|
| StackNotFound | The Stack ({name}) could not be found. | 404 | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### GetStackResource

You can call this operation to query information about a resource in a specific stack.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetStackResour ce | The operation that you want to perform. Set the value to GetStackResource. |
| LogicalResourceI d | String | Yes | WebServer | The logical ID of the resource as defined in the template. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| ShowResourceAt tributes | Boolean | No | true | Specifies whether to query resource attributes. Valid values: true false |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Status | String | CREATE COMPLET _ E | The state of the resource. Valid values: CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
|---|---|---|---|
| Description | String | no description | The description of the resource. |
| LogicalResour ceId | String | WebServer | The logical ID of the resource as defined in the template. |
| StackId | String | efdf5c10-96a5- 4fd7-ab89- 68e7baa2**** | The ID of the stack. |
| StackName | String | test-describe- resource | The name of the stack. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |
| StatusReason | String | state changed | The reason why the resource is in its current state. |
| PhysicalResou rceId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | The physical ID of the resource. |
| ResourceType | String | ALIYUN::ROS::Wait ConditionHandle | The type of the resource. |
| CreateTime | String | 2019-08- 01T06:01:23 | The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
| Metadata | Map | {"key": "value"} | The metadata. |

| UpdateTime | String | 2019-08- 01T06:01:29 | The time when the stack was last updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC. |
|---|---|---|---|
| ResourceAttrib utes | List | [ { "ResourceAttribute Value":"curl -Uri \"http://100.100.XX .XX/waitcondition? stackname=test- describe- resource&stackid= efdf5c10-96a5- 4fd7-ab89- 68e7baa2****&res ource=WaitConditi onHandle&expire= 156468****&signat ure=991d910a901 a89db6580d74233 119960c004****\" - Method Post - Headers @{\"Content- Type\"=\"applicatio n/json\"; \"Accept\"=\"applic ation/json\"; \"x- acs-region- id\"=\"cn- beijing\"}", "ResourceAttribute Key":"PowerShellC urlCli" } ] | The list of resource attributes. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | The time when the last successful drift detection operation was initiated. |

| ResourceDriftS tatus | String | IN SYNC _ | The drift state of the resource in the last successful drift detection. Valid values: DELETED: The actual configuration of the resource differs from its expected template configuration because the resource had been deleted. MODIFIED: The actual configuration of the resource differs from its expected template configuration. NOT CHECKED: ROS has not checked _ whether the actual configuration of the resource differs from its expected template configuration. IN SYNC: The actual configuration of the _ resource matches its expected template configuration. |
|---|---|---|---|

**Examples**

Sample requests

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
                <ResourceAttributeValue>curl -i -X POST -H 'Content-Type: application/js
on' -H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcondition?stackname=test-describeresource\&amp;stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****\&amp;resource=WaitConditionHandle\&amp;expire=156468****\&amp;signature=991d 0a901a89db6580d74233119960c004****</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceAttributes>
                <ResourceAttributeKey>WindowsCurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -i -X POST -H "Content-Type: application/js
on" -H "Accept: application/json" -H "x-acs-region-id: cn-beijing" "http://100.100.XX.XX/waitcondition?stackname=test-describeresource&amp;stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****&amp;resource=WaitConditionHandle&amp;expire=156468****&amp;signature=991d910 01a89db6580d74233119960c004****"</ResourceAttributeValue>
          </ResourceAttributes>
          <ResourceAttributes>
                <ResourceAttributeKey>PowerShellCurlCli</ResourceAttributeKey>
                <ResourceAttributeValue>curl -Uri "http://100.100.XX.XX/waitcondition?st
ackname=test-describe-resource&amp;stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****&amp;resource=WaitConditionHandle&amp;expire=156468****&amp;signature=991d910 01a89db6580d74233119960c004****" -Method Post -Headers @{"Content- Type"="application/json"; "Accept"="application/json"; "x-acs-region-id"="cn-beijing"}< /ResourceAttributeValue>
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
            "ResourceAttributeValue": "curl -i -X POST -H 'Content-Type: application/jso
n' -H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcondition?stackname=test-describe-resource\\&stackid=efdf5c10- 96a5-4fd7-ab89- 68e7baa2****\\&resource=WaitConditionHandle\\&expire=156468****\\&signature=991d910a901a8 b6580d74233119960c004****"
```

`},` `{`

```json
            "ResourceAttributeKey": "WindowsCurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H \"Content-Type: application/js
on\" -H \"Accept: application/json\" -H \"x-acs-region-id: cn-beijing\" \"http://100.100.XX.XX/waitcondition?stackname=test-describe-resource&stackid=efdf5c10- 96a5-4fd7-ab89- 68e7baa2****&resource=WaitConditionHandle&expire=156468****&signature=991d910a901a89db658 74233119960c004****\""
```

`},` `{`

```json
            "ResourceAttributeKey": "PowerShellCurlCli",
            "ResourceAttributeValue": "curl -Uri \"http://100.100.XX.XX/waitcondition?
stackname=test-describe-resource&stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****&resource=WaitConditionHandle&expire=156468****&signature=991d910a901a89db658 74233119960c004****\" -Method Post -Headers @{\"Content-Type\"=\"application/json\"; \" Accept\"=\"application/json\"; \"x-acs-region-id\"=\"cn-beijing\"}"
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

| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name, and stack indicates the name or ID of the stack. |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |

#### GetResourceType

You can call this operation to query details about resource types.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetResourceTyp e | The operation that you want to perform. Set the value to GetResourceType. |
| ResourceType | String | Yes | ALIYUN::ROS::W aitConditionHan dle | The type of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Attributes | Map | {"CurlCli": {},"PowerShellCurl Cli": {},"WindowsCurlCli ": {}} | The attributes of the resource. |
| Properties | Map | {"Count": {},"Mode": {"Constraints": []}} | The properties of the resource. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceType | String | ALIYUN::ROS::Wait ConditionHandle | The type of the resource. |

| SupportDriftDe tection | Boolean | false | Indicates whether the resource supports drift detection. Valid values: true: The resource supports drift detection. false: The resource does not support drift detection. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetResourceType &ResourceType=ALIYUN::SLB::LoadBalancer &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetResourceTypeResponse>
       <Attributes class="object">
              <CurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI
command prefix, which can be used for signalling handle completion or failure. You can signal success by adding --data-binary '{"status": "SUCCESS"}' , or signal failure by a dding --data-binary '{"status": "FAILURE"}'</Description>
              </CurlCli>
              <PowerShellCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI
command prefix for PowerShell, which can be used for signalling handle completion or fa ilure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShel l satisfies the constraint. (Show the version via $PSVersionTable.PSVersion.) You can s ignal success by adding -Body '{"status": "SUCCESS"}' , or signal failure by adding -Bo dy '{"status": "FAILURE"}' </Description>
              </PowerShellCurlCli>
              <WindowsCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI
command prefix for Windows, which can be used for signalling handle completion or failu re. As Windows does not support curl command, you need to install curl.exe and add it t o PATH first. You can signal success by adding --data-binary "{\"status\": \"SUCCESS\"} " , or signal failure by adding --data-binary "{\"status\": \"FAILURE\"}" </Description>
              </WindowsCurlCli>
       </Attributes>
       <Properties class="object">
              <Count class="object">
                     <Default type="number">-1</Default>
                     <Description type="string">There are 3 preconditions that make Coun
t taking effect: 1.Mode is set to Full. 2.Count &gt;= 0. 3.The id of signal is not specified. If so, it will be a self-increasing integer starte d from 1. For example, the id of the first signal is 1, the id of the second signal is 2, and so on.
```

`,`

```
If Count takes effect, signals with id &gt; Count will be deleted before update. The default value is -1, which means no effect. It is recommended to quote the same value with WaitCondition.Count. </Description>
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
                     <Description type="string">If set to Increment, all old signals wil
l be deleted before update. In this mode, WaitCondition.Count should reference an incre mental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances. If set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCo ndition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mode with Count. Default to Full. </Description>
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
            "Description": "Convenience attribute, provides curl CLI command prefix,
which can be used for signalling handle completion or failure. You can signal success by adding --data-binary '{\"status\": \"SUCCESS\"}' , or signal failure by adding --dat a-binary '{\"status\": \"FAILURE\"}'"
```

`},`

```json
        "PowerShellCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for
PowerShell, which can be used for signalling handle completion or failure. As this cmdl etwasintroducedinPowerShell30 ensuretheversionofPowerShellsatisfiesthecon
```

```
et was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the con straint. (Show the version via $PSVersionTable.PSVersion.) You can signal success by ad ding -Body '{\"status\": \"SUCCESS\"}' , or signal failure by adding -Body '{\"status\" : \"FAILURE\"}' "
```

`},`

```json
        "WindowsCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for
Windows, which can be used for signalling handle completion or failure. As Windows does not support curl command, you need to install curl.exe and add it to PATH first. You ca n signal success by adding --data-binary \"{\\\"status\\\": \\\"SUCCESS\\\"}\" , or sig nal failure by adding --data-binary \"{\\\"status\\\": \\\"FAILURE\\\"}\" "
```

`}` `},`

```json
    "Properties": {
        "Count": {
            "Default": -1,
            "Description": "There are 3 preconditions that make Count taking
effect:\n1.Mode is set to Full.\n2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing integer started from 1. For example, the id of the fir st signal is 1, the id of the second signal is 2, and so on.\n\nIf Count takes effect, signals with id > Count will be deleted before update.\nThe default value is -1, which means no effect.\nIt is recommended to quote the same value with WaitCondition.Count.",
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
            "Description": "If set to Increment, all old signals will be deleted before
update. In this mode, WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n\nIf set to Ful l, no old signal will be deleted unless Count is set. In this mode, WaitCondition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mode with Count.\n\nDefault to Full.",
            "Immutable": false,
            "Required": false,
            "Type": "string",
            "UpdateAllowed": true
```

`}` `},`

```json
    "RequestId": "BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0",
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "SupportDriftDetection": false
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceTypeNotFoun d | The Resource Type ({name}) could not be found. | The error message returned because the specified resource type does not exist. name indicates the name of the resource type. |

### Template operations

#### ValidateTemplate

You can call this operation to validate the template that is used to create stacks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ValidateTemplat e | The operation that you want to perform. Set the value to ValidateTemplate. |
| TemplateURL | String | No | oss://ros/templat e/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| RegionId | String | No | cn-hangzhou | The region ID of the stack template. |

| TemplateBody | String | No | {"ROSTemplate FormatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | No description | The description of the stack template. |
| Parameters | List | [{"Description": "", "Label": "param integer", _ "NoEcho": "false", "ParameterKey": "param integer", _ "Type": "Number"},{ "Description": "", "Label": "param float", _ "NoEcho": "false", "ParameterKey": "param float", _ "Type": "Number"}] | The input parameters of the stack template. The input parameters define the parameters that you must specify to create stacks based on the template. These parameters specify information about a stack, such as the username, password, and environment-related ECS instance type. |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=ValidateTemplate &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ValidateTemplateResponse>
       <Description type="string">No description</Description>
       <Parameters class="array">
```

`P` `t` `l`

```
"bj
```

`t"`

```
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
                     <Description type="string"></Description>
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
<Labeltype="string">paramlist</Label>
```

```
                     <Label type=string>param_list</Label>
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
```

```json
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

You can call this operation to query details about a template.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplate | The operation that you want to perform. Set the value to GetTemplate. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ChangeSetId | String | No | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | The ID of the change set. |
| TemplateId | String | No | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| TemplateBody | String | {\"ROSTemplateFo rmatVersion\": \"2015-09-01\"} | The structure that contains the template body. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplate &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```json
<GetTemplateResponse>
        <TemplateBody>{"ROSTemplateFormatVersion": "2015-09-01", "Resources":
{"dummy2": {"Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {"Ref": "param_has_default"}, "List": {"Ref": "param_list"}}}, "dummy": {"Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {"Ref": "param_json_dict"}, "String": {"R ef": "param_str"}, "List": {"Ref": "param_json_list"}, "Number": {"Ref": "param_float"}, "Bool": {"Ref": "param_bool"}, "Integer": {"Ref": "param_integer"}}}, " nested": {"Type": "ALIYUN::ROS::Stack", "Properties": {"TemplateURL": "oss://nested-sta ck/simple/nested_demo", "TimeoutMins": 16}}, "WaitConditionHandle": {"Type": "ALIYUN::R OS::WaitConditionHandle", "Properties": {"UpdateVersion": {"Ref": "UpdateVersion"}}}}, "Parameters": {"param_integer": {"Type": "Number"}, "param_float": {"Type": "Number"}, "param_bool": {"Type": "Boolean"}, "param_json_list": {"Type": "Json"}, "param_has_default": {"Default": "{\"c\": []}", "Type": "Json"}, "UpdateVersion": {"Typ e": "Number"}, "param_str": {"Type": "String"}, "param_list": {"Type": "CommaDelimitedList"}, "param_json_dict": {"Type": "Json"}}, "Outputs": {"param_integer": {"Value": {"Ref": "param_integer"}}, "param_float": {"Value": {"Ref": "param_float"}}, "param_bool": {"Value": {"Ref": "param_bool"}}, "param_json_list": {"V alue": {"Ref": "param_json_list"}}, "param_has_default": {"Value": {"Ref": "param_has_default"}}, "param_str": {"Value": {"Ref": "param_str"}}, "CurlCli": {"Value ": {"Fn::GetAtt": ["WaitConditionHandle", "CurlCli"]}}, "param_list": {"Value": {"Ref": "param_list"}}, "param_json_dict": {"Value": {"Ref": "param_json_dict"}}}} </TemplateBody>
        <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
</GetTemplateResponse>
```

`JSON` format `{`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TemplateBody": "{\"ROSTemplateFormatVersion\": \"2015-09-01\", \"Resources\": {\"du
mmy2\": {\"Type\": \"ALIYUN::DEBUG::Dummy\", \"Properties\": {\"Map\": {\"Ref\": \"para m_has_default\"}, \"List\": {\"Ref\": \"param_list\"}}}, \"dummy\": {\"Type\": \"ALIYUN ::DEBUG::Dummy\", \"Properties\": {\"Map\": {\"Ref\": \"param_json_dict\"}, \"String\": {\"Ref\": \"param_str\"}, \"List\": {\"Ref\": \"param_json_list\"}, \"Number\": {\"Ref\ ": \"param_float\"}, \"Bool\": {\"Ref\": \"param_bool\"}, \"Integer\": {\"Ref\": \"para m_integer\"}}}, \"nested\": {\"Type\": \"ALIYUN::ROS::Stack\", \"Properties\": {\"Templ ateURL\": \"oss://nested-stack/simple/nested_demo\", \"TimeoutMins\": 16}}, \"WaitCondi tionHandle\": {\"Type\": \"ALIYUN::ROS::WaitConditionHandle\", \"Properties\": {\"Updat eVersion\": {\"Ref\": \"UpdateVersion\"}}}}, \"Parameters\": {\"param_integer\": {\"Typ e\": \"Number\"}, \"param_float\": {\"Type\": \"Number\"}, \"param_bool\": {\"Type\": \ "Boolean\"}, \"param_json_list\": {\"Type\": \"Json\"}, \"param_has_default\": {\"Defau lt\": \"{\\\"c\\\": []}\", \"Type\": \"Json\"}, \"UpdateVersion\": {\"Type\": \"Number\"}, \"param_str\": {\"Type\": \"String\"}, \"param_list\": {\"Type\": \"CommaD elimitedList\"}, \"param_json_dict\": {\"Type\": \"Json\"}}, \"Outputs\": {\"param_integer\": {\"Value\": {\"Ref\": \"param_integer\"}}, \"param_float\": {\"Valu e\": {\"Ref\": \"param_float\"}}, \"param_bool\": {\"Value\": {\"Ref\": \"param_bool\"}}, \"param_json_list\": {\"Value\": {\"Ref\": \"param_json_list\"}}, \"p aram_has_default\": {\"Value\": {\"Ref\": \"param_has_default\"}}, \"param_str\": {\"Va lue\": {\"Ref\": \"param_str\"}}, \"CurlCli\": {\"Value\": {\"Fn::GetAtt\": [\"WaitCond itionHandle\", \"CurlCli\"]}}, \"param_list\": {\"Value\": {\"Ref\": \"param_list\"}}, \"param_json_dict\": {\"Value\": {\"Ref\": \"param_json_dict\"}}}}"
```

`}`

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the specified stack does not exist. name indicates the name or ID of the stack. |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | The error message returned because the specified template does not exist. ID indicates the template ID. |

#### DeleteTemplate

You can call this operation to delete a stack and all of its resources.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteTemplate | The operation that you want to perform. Set the value to DeleteTemplate. |
| TemplateId | String | Yes | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the stack. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |

**Examples**

Sample requests

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

You can call this operation to query the list of one or more templates.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTemplates | The operation that you want to perform. Set the value to ListTemplates. |
| TemplateName | String | No | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a _ digit or letter. |
| PageNumber | Long | No | 10 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Long | No | 1 | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |

| Tag.N.Key | String | No | TestKey | The key of tag N. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |
|---|---|---|---|---|
| Tag.N.Value | String | No | TestValue | The value of tag N. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://. It cannot start with acs: or aliyun. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C3A8413B-1F16- 4DED-AC3E- 61A00718DE8A | The ID of the request. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| PageNumber | Integer | 1 | The page number of the returned page. Pages start from page 1. |
| TotalCount | Integer | 3 | The total number of templates. |
| Templates | Array of Template |   | Details about the templates. |
| CreateTime | String | 2019-10- 15T08:17:14.0000 00 | The time when the template was created. |
| Description | String | test-description | The description of the template. |
| TemplateId | String | 4d4f5aa2-3260- 4e47-863b- 763fbb12**** | The ID of the template. |
| TemplateNam e | String | test-list-templates | The name of the template. |
| UpdateTime | String | 2019-10- 15T08:17:14.0000 00 | The time when the template was created. |

**Examples**

Sample requests

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

You can call this operation to create a template.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateTemplate | The operation that you want to perform. Set the value to CreateTemplate. |
| TemplateName | String | Yes | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a _ digit or letter. |

| TemplateURL | String | No | oss://ros/templat e/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You can specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| Description | String | No | It is a demo. | The description of the template. The description can be up to 256 characters in length. |
| TemplateBody | String | No | {"ROSTemplate FormatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

**Examples**

Sample requests

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
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is incorrect. resource indicates the resource name, and name indicates the attribute name. |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is incorrect. resource indicates the resource name, and section indicates the section name. |

| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
|---|---|---|---|
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | The error message returned because the template version is incorrect. reason indicates the specific reason. |

#### UpdateTemplate

You can call this operation to update a template.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateTemplate | The operation that you want to perform. Set the value to UpdateTemplate. |
| TemplateId | String | Yes | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |

| TemplateURL | String | No | oss://ros/templat e/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| TemplateName | String | No | MyTemplate | The name of the template. The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must start with a _ digit or letter. |
| Description | String | No | It is a demo. | The description of the template. The description can be up to 256 characters in length. |
| TemplateBody | String | No | {"ROSTemplate FormatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | The ID of the request. |

| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |
|---|---|---|---|

**Examples**

Sample requests

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
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | The error message returned because the resource attribute referenced in the template is invalid. resource indicates the resource name, and name indicates the attribute name. |

| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | The error message returned because the type of the specified resource section defined in the template is invalid. resource indicates the resource name, and section indicates the section name. |
|---|---|---|---|
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | The error message returned because the template contains an invalid reference. name indicates the reference name, and referencer indicates the referencer name. |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | The error message returned because the template contains an invalid property. section indicates the section name. |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | The error message returned because the template version is invalid. reason indicates the specific reason. |

#### GetTemplateSummary

You can call this operation to query information about a new or existing template. To specify the query object, you must specify one of the StackId, ChangeSetId, TemplateId, TemplateBody, and TemplateURL parameters.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetTemplateSu mmary | The operation that you want to perform. Set the value to GetTemplateSummary. |
| StackId | String | No | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |

| TemplateBody | String | No | {"ROSTemplate FormatVersion": "2015-09-01"} | The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
|---|---|---|---|---|
| RegionId | String | No | cn-hangzhou | The region ID of the stack. |
| TemplateId | String | No | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | The ID of the template. |
| TemplateURL | String | No | oss://ros/templat e/demo | The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo? RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length. If the region of the OSS bucket is not specified, the RegionId value is used. Note You must specify one of the TemplateBody and TemplateURL parameters, but you cannot specify both of them. |
| ChangeSetId | String | No | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | The ID of the change set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | No description | The description of the stack template. |
| Metadata | Map | {"key": "value"} | The metadata that is specified in the template. |

| Parameters | List | [{"Description":"", "Label":"Name", "NoEcho":"false", "ParameterKey":"N ame", "Type":"String"}] | Details about the parameter declarations that describe the attributes of parameters. |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |
| ResourceIdenti fierSummaries | Array of ResourceIdenti fierSummary |   | Details about the resource identifier summaries. A summary describes the resource into which you want to import other resources and the attributes that can be used to identify the resource. For example, VpcId is the identifier of the ALIYUN::ECS::VPC resource. |
| LogicalResour ceIds | List | ["Vpc"] | The logical IDs of all resources that are of the type that is specified by the ResourceType parameter. |
| ResourceIdenti fiers | List | ["VpcId"] | The attributes of the resource. The attributes are used to identify the resource into which you want to import other resources. For example, VpcId is the identifier of the ALIYUN::ECS::VPC resource. |
| ResourceType | String | ALIYUN::ECS::VPC | The type of the resource. Note You can import resources into the ALIYUN::ECS::VPC resource type. |
| ResourceType s | List | ["ALIYUN::ECS::VPC "] | All the resource types that are used in the template. |
| Version | String | 2015-09-01 | The version of the template. |

**Examples**

Sample requests

```
http(s)://ros.aliyuncs.com/? Action=GetTemplateSummary &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &RegionId=cn-hangzhou &TemplateURL=oss://ros/template/demo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<GetTemplateSummary>
          <Description>No description</Description>
          <Metadata></Metadata>
          <Parameters>
                <Description>Description of the vpc, [2, 256] characters. Do not fill
or empty, the default is empty. </Description>
                <Label>Description</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>Description</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>Tags to attach to vpc. Max support 20 tags to add during cr
eate vpc. Each tag with two properties Key and Value, and Key is required. </Descriptio
```

`n>`

```xml
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
                <Description>Whether to enable an IPv6 network cidr, the value is:False
(default): not turned on.True: On. </Description>
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
                <Description>Display name of the vpc instance, [2, 128] English or Chine
se characters, must start with a letter or Chinese in size, can contain numbers, '_' or
```

```xml
'.', '-'</Description>
                <Label>VpcName</Label>
                <NoEcho>false</NoEcho>
                <ParameterKey>VpcName</ParameterKey>
                <Type>String</Type>
          </Parameters>
          <Parameters>
                <Description>
                The IP address range of the VPC in the CIDR block form. You can use the
following IP address ranges and their subnets:
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
            "Description": "Description of the vpc, [2, 256] characters. Do not fill or
empty, the default is empty.",
            "Label": "Description",
            "NoEcho": "false",
            "ParameterKey": "Description",
            "Type": "String"
```

`},` `{`

```json
            "Description": "Tags to attach to vpc. Max support 20 tags to add during
create vpc. Each tag with two properties Key and Value, and Key is required.",
            "Label": "Tags",
            "MaxLength": 20,
            "NoEcho": "false",
            "ParameterKey": "Tags",
            "Type": "Json"
```

`},` `{`

```json
            "Description": "IPv6 network cidr of the VPC.",
            "Label": "Ipv6CidrBlock",
```

```json
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
            "Description": "Whether to enable an IPv6 network cidr, the value is:False
(default): not turned on.True: On.",
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
            "Description": "Display name of the vpc instance, [2, 128] English or
Chinese characters, must start with a letter or Chinese in size, can contain numbers, ' _' or '.', '-'",
            "Label": "VpcName",
            "NoEcho": "false",
            "ParameterKey": "VpcName",
            "Type": "String"
```

`},` `{`

```json
            "Description": "The IP address range of the VPC in the CIDR block form. You
can use the following IP address ranges and their subnets:\n10.0.0.0/8\n172.16.0.0/12 ( Default)\n192.168.0.0/16",
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

You can call this operation to query available regions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| AcceptLanguage | String | No | zh-CN | The natural language that is used to filter responses. Default value: zh-CN. Valid values: zh-CN en-US ja |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | Details about the regions. |
| LocalName | String | China (Hangzhou) | The name of the region in the local language. |
| RegionEndpoin t | String | ros.aliyuncs.com | The endpoint of the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | 59F0F0A0-A637- 4292-9B91- 251EF5010913 | The ID of the request. |

**Examples**

Sample requests

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
            <LocalName>China (Beijing)</LocalName>
        </Region>
        <Region>
            <RegionId>cn-zhangjiakou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>China (Zhangjiakou)</LocalName>
```

```xml
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
            <LocalName>Indonesia (Jakarta)</LocalName>
        </Region>
        <Region>
            <RegionId>ap-south-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

```xml
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
            "RegionId": "cn-zhangjiakou"
```

`},` `{`

```json
            "localName": "China (Hohhot)",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-huhehaote"
```

`g` `},` `{`

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
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-south-1"
```

`},` `{`

```json
            "localName": "US (Virginia)",
            "RegionEndpoint": "ros.aliyuncs.com",
```

```json
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

You can call this operation to send signals.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SignalResource | The operation that you want to perform. Set the value to SignalResource. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| LogicalResourceI d | String | Yes | WebServer | The logical ID of the resource as defined in the template. |

| Status | String | Yes | SUCCESS | The state of the signal. Failure signals can cause stack creation or update to fail. If all signals are warnings, the stack cannot be created or updated. Valid values: SUCCESS FAILURE WARNING |
|---|---|---|---|---|
| UniqueId | String | Yes | 27c7347b-352a- 4377-accf- 63d361c1**** | The unique ID of the signal. The ID must be 1 to 64 characters in length. If multiple signals are sent to a single resource, each signal must have a unique ID. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-) and underscores ( ). _ |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | The ID of the request. |

**Examples**

Sample requests

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

You can call this operation to detect the resources that may face high risks caused by a stack deletion operation, and query the reason for each risk.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ListStackOperati onRisks | The operation that you want to perform. Set the value to ListStackOperationRisks. |
|---|---|---|---|---|
| OperationType | String | Yes | DeleteStack | The operation type to be detected. The DeleteStack value specifies to detect resources that may face high risks caused by a stack deletion operation. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the stack. |
| StackId | String | Yes | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | The ID of the stack. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| RamRoleName | String | No | test-role | The name of the RAM role. If you specify a RAM role, ROS creates stacks based on the permissions granted to the RAM role and uses the credentials of the RAM role to call API operations. If you do not specify a RAM role, ROS creates stacks based on the permissions of the current account. The RAM role name can be up to 64 characters in length. |
| RetainAllResourc es | Boolean | No | false | Specifies whether to retain all resources in the stack. Default value: false. Valid values: true: The resources in the stack are retained. false: The resources in the stack are not retained. Note This parameter is valid only when the OperationType parameter is set to DeleteStack. |

| RetainResources .N | RepeatL ist | No | WebServer | The list of resources to retain. Note This parameter is valid only when the OperationType parameter is set to DeleteStack. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 72108E7A-E874- 4A5E-B22C- A61E94AD12CD | The ID of the request. |
| RiskResources | Array of Resource |   | The resources that face high risks caused by the stack deletion operation. |
| Code | String | NoPermission | The error code that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| LogicalResour ceId | String | MySG | The logical ID of the resource. It is the resource name defined in the template. |
| Message | String | You are not authorized to complete this action. | The error message that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| PhysicalResou rceId | String | sg- bp1dpioafqphedg9 **** | The physical ID of the resource. |
| Reason | String | There are some ECS instances (i- bp18el96s4wq635 e****) depending on the security group. | The reason for the risk. |
| RequestId | String | DF4296CF-F45F- 4845-A72B- BE617601DB25 | The request ID that is returned when the risk detection fails. This parameter is not returned when the risk detection succeeds. |
| ResourceType | String | ALIYUN::ECS::Secur ityGroup | The type of the resource. |

| RiskType | String | Referenced | The type of the risk. Valid values: Referenced: The current resource is referenced by other resources. MaybeReferenced: The current resource may be referenced by other resources. AdditionalRiskCheckRequired: An additional risk detection is required for nested stacks. |
|---|---|---|---|

**Examples**

Sample requests

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
       <Reason>There are some ECS instances (i-bp18el96s4wq635e****) depending on the s
ecurity group. </Reason>
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
      "Reason": "There are some ECS instances (i-bp18el96s4wq635e****) depending on the
security group.",
      "RiskType": "Referenced"
```

`}` `]` `}`

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
