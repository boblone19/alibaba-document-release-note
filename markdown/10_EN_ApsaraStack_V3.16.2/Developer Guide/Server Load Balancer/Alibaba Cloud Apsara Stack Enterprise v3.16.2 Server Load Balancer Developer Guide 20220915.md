---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Load Balancer Developer Guide"
product_version: "V3.16.2"
doc_version: "20220915"
pdf_pages: 283
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Load Balancer Developer Guide 20220915.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Server%20Load%20Balancer%20Developer%20Guide%2020220915.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Server Load Balancer Developer Guide

## Getting Started

### Apsara Stack documentation

This topic describes how to view the references of an Apsara Stack service when you call Apsara Stack API. Workflow The following figure shows how to find your desired information in the Apsara Stack documentation. Prerequisites The Apsara Stack version is obtained from O&M personnel or an operations administrator. Procedure You can go to the Apsara Stack documentation center to view the documentation of an Apsara Stack service.
1. Go to the Apsara Stack documentation center.
2. Click the Ent erprise, Agilit y, or All-in-one tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service.
5. In the upper-right corner of the documentation section, click View Det ails or Download PDF.

### Call an API operation

Apsara Stack allows you to call API operations by using the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway. To ensure that Apsara Stack provides the same user experience as the public cloud, API operations in Apsara Stack are called by using the POP gateway by default starting Apsara Stack Enterprise V3.16.0. This topic describes how to call API operations in Apsara Stack by using the POP gateway. Not e You can still use the ASAPI gateway to call API operations. For more information, see Call API operations by using the ASAPI gateway, Obtain the endpoint of ASAPI, and Obtain ASAPI SDK. Procedure
1. Obtain AccessKey credentials.
Obtain the AccessKey credentials that are required for calling an API operation. For more information, see Obtain an AccessKey pairor Obtain an STS AccessKey 3-tuple. Not e We recommend that you use an AccessKey pair or an STS AccessKey 3-tuple of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information, see Obtain the values of common header parameters.
3. Obtain the organization ID and resource set ID.
You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management C onsole Developer Guide. You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Con sole Developer Guide. Not e When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is queried. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is left empty by default. If you specify a resource set ID, you must also specify an organization ID.
4. Obtain the API reference.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
5. Obtain the endpoint of the cloud service.
6. Obtain an SDK of the cloud service and call an API operation.

## Preparations

### Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your browser
and press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations
in the following scenarios: This is your first time logging on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click Aut hent icat e. Not e For more information, see the Bind a virtual MFA device to enable MFA topic in A psara Uni-manager Management Console User Guide.
5. In the top navigation bar, choose Product s > Ot hers > API T ool.

### View information about an API

operation This topic describes how to view information about an API operation. The information includes service names, API operation names, and API versions. The information is required when you use an SDK to call API operations. Context The API operations on the API Directory page are for reference only. For information about how to call API operations, see the developer guide of the corresponding cloud service. If the information on the API Directory page is different from that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select a cloud service from the Product Name drop-down list, enter a
keyword of an operation name in the search box, and then click Search.
4. View and record the service name, API operation name, and API version.

### Obtain an AccessKey pair

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You only need to provide one type of AccessKey credential for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Context An AccessKey pair is used to verify the identity of request senders. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur. Warning The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion.
3. In the AccessKey Pair section, view the AccessKey pair of the personal account.
Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Organizat ions.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want
to obtain.
5. Click Management AccessKey on the right side of the page.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### Obtain STS credentials

This topic describes how to use Security Token Service (STS) credentials to make API calls. Background information Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. You can use STS credentials to make API calls. To call Apsara Stack APIs, you must obtain an AccessKey ID, an AccessKey secret, and a security token assigned by STS. For more information, see STS. Procedure
1. Obtain the `Resource Access Management (RAM) role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click User Inf ormat ion. iii. Click View Current Role Policy. In the View Policies of Current Role dialog box, you can obtain information about the `RAM role` that is assigned to the current user.
2. Obtain the STS credentials.
Not e In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) before you submit the code. The following section describes the parameters: <yourRegionID>: Replace it with the region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <yourRoleSessionName>: Replace it with the name of the current session. <yourRoleArn>: Replace it with your RAM role. "sts.aliyuns.com": Replace it with the endpoint of STS.

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
    // Obtain the AccessKey ID, AccessKey secret, and security token assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the actual endpoint of the STS. In most cases, en
dpoint is in the following format: sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the ARN that you obtain in the preceding step.
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
        } catch (com.aliyuncs.exceptions.ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
```

`}`

```
    return null;
```

`}`
3. The following sample code shows how to use STS credentials to call the DescribeLoadBalancers
operation of the Server Load Balancer (SLB) API: Not e In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) before you submit the code. The following section describes the parameters: <yourRegionID>: Replace it with the region ID. <yourStsAccesskeyID>: Replace it with your STS AccessKey ID. <yourAccessKeySecret>: Replace it with your STS AccessKey secret. <yourStsToken>. Replace it with your STS security token. <yourRegionID>: Replace it with the actual resource set ID. <yourRegionID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey
ID and AccessKey secret assigned by STS.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAcces
skey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("ecs.aliyuns.com");
    request.setSysProduct("Slb");
    request.setSysAction("DescribeLoadBalancers");
    request.setSysVersion("2014-05-15");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRegionID>" with the region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token assigned by STS.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace it with your resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace it with your organization ID.
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

header parameters You must set header parameters when you call API operations. This topic describes the header parameters and how to obtain the values of the parameters. This topic also describes the values of some response parameters after you call API operations. Header parameters

| Paramet er | Descript ion |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-inst anceid | The ID of the instance on which you want to perform operations. For more information about how to obtain instance IDs, see Obtain an instance ID. |

Obtain a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the organization that you want to view.
5. View the region ID in the Regions section on the right.
Obtain an organization ID You must call an operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You must call an operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. Obtain an instance ID You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an elastic IP address (EIP), perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product sNet workingServer Load Balancer.
3. In the left-side navigation pane, choose Inst ances & Images > Inst ances.
4. View the inst ance ID in the instance list.
Response parameters The following response parameters are returned by default when you call operations to query the instances of cloud services.

| Paramet er | Descript ion |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### Obtain the endpoint of the SLB

API This topic describes how to obtain the endpoint of the Server Load Balancer (SLB) API. Background information To use the POP gateway to call Apsara Stack API (ASAPI) operations, you must obtain a service endpoint. You can obtain a service endpoint from Apsara Stack onsite O&M engineers. You can also perform the following operations to obtain the endpoint: Procedure
1. Log on to Apsara Infrastructure Management.
i. Log on to the Apsara Uni-manager Operations Console. ii.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `SLB` .
5. Find the `slb-yaochi` service, right-click the Service Regist rat ion column, and then select Show
More from the shortcut menu. On the Det ails page, view the slb.openapi.endpoint value, which is the `endpoint` .

### Obtain the SLB SDK

When you call API operations of a cloud service in Apsara Stack by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK. This topic describes how to obtain Alibaba Cloud SDK. Background information To use Server Load Balancer (SLB) features, you must install both the SLB SDK and the Alibaba Cloud core library. For example, to use SLB SDK for Java, you must download `aliyun-java-sdk-sl` and

```
 aliyun-java-sdk-core .
```

The SLB SDK encapsulates the API released on May 15, 2014. The SDK identifies callers based on their AccessKey pairs and provides features such as automatic signing to allow you to create and manage resources by calling API operations. Alibaba Cloud SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. We recommend that you use the SDK core library that is provided on the Alibaba Cloud website. The SDK core library is ideal for all cloud services and is compatible with Apsara Stack. Instructions Alibaba Cloud SDK supports Java, Python, and Go. You can select an SDK from Alibaba Cloud SDK based on your business requirements. Not e We recommend that you use an SDK for Java, Python, or Go. If you use SDKs in other programming languages, the SDKs may be incompatible with your system. SDK for Java

## Call examples for SDK for Java

### Quick start

This topic describes how to obtain and use the Server Load Balancer (SLB) SDK for Java. Prerequisites An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of the SLB API, see Obtain the endpoint of the SLB API. Java Development Kit (JDK) 1.8 or later is installed. SDKs for Java provided by Alibaba Cloudrequire JDK 1.8or later. Install Alibaba Cloud SDK for Java If you use Apache Maven to manage a Java project, import the JAR file to the pom.xml file of the project. To use the SLB SDK, you must install the SDK core library and the SLB SDK. We recommend that you use version 4.5.17 or later for the SDK core library. In this example, the SLB SDK uses version 3.3.8. Procedure To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
Not e In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code. The following list describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.alibaba.fastjson.JSON; import java.util.*;
```

SDK for Java

```java
import com.aliyuncs.slb.model.v20140515.*; public class DescribeImages {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",
            "<yourAccessKeyID>",
            "<yourAccessKeySecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the required parameters.
        DescribeLoadBalancersRequest request = new DescribeLoadBalancersRequest();
        request.setResourceOwnerAccount("test"); // This value is for reference only. E
nter a value based on your business requirements.
        request.setResourceOwnerId("1"); // This value is for reference only. Enter a v
alue based on your business requirements.
        request.setRegionId("test"); // This value is for reference only. Enter a value
based on your business requirements.
        request.setServerId("test"); // This value is for reference only. Enter a value
based on your business requirements.
        request.setAddressIPVersion("test"); // This value is for reference only. Enter
a value based on your business requirements.
        request.setLoadBalancerStatus("test"); // This value is for reference only. Ent
er a value based on your business requirements.
        request.setLoadBalancerId("test"); // This value is for reference only. Enter a
value based on your business requirements.
        request.setLoadBalancerName("test"); // This value is for reference only. Enter
a value based on your business requirements.
        request.setServerIntranetAddress("test"); // This value is for reference only.
Enter a value based on your business requirements.
        request.setAddressType("test"); // This value is for reference only. Enter a va
lue based on your business requirements.
        request.setInternetChargeType("test"); // This value is for reference only. Ent
er a value based on your business requirements.
        request.setVpcId("test"); // This value is for reference only. Enter a value ba
sed on your business requirements.
        request.setVSwitchId("test"); // This value is for reference only. Enter a valu
e based on your business requirements.
        request.setNetworkType("test"); // This value is for reference only. Enter a va
lue based on your business requirements.
```

SDK for Java

```java
        request.setAddress("test"); // This value is for reference only. Enter a value
based on your business requirements.
        request.setMasterZoneId("test"); // This value is for reference only. Enter a v
alue based on your business requirements.
        request.setSlaveZoneId("test"); // This value is for reference only. Enter a va
lue based on your business requirements.
        request.setOwnerAccount("test"); // This value is for reference only. Enter a v
alue based on your business requirements.
        request.setTags("test"); // This value is for reference only. Enter a value bas
ed on your business requirements.
        request.setPayType("test"); // This value is for reference only. Enter a value
based on your business requirements.
        request.setResourceGroupId("test"); // This value is for reference only. Enter
a value based on your business requirements.
        try {
            DescribeLoadBalancersResponse response = client.getAcsResponse(request);
            System.out.println(JSON.toJSONString(response));
            // Print response parameters. In this example, the RequestId parameter is p
rinted.
            System.out.println(response.getRequestId());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            // Print the error code.
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}`

### Work with SLB SDK for Java

#### Install SLB SDK for Java

This topic describes how to install Server Load Balancer (SLB) SDK for Java and how to use the SDK to make API calls. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. SDK for Java Before you start, you must install the core library of Apsara Stack SDK for Java and SLB SDK for Java. We recommend that you use the core library version 4.5.17 or later, and use the SDK for Java 3.3.9. To use SLB SDK for Java, you must install the core library of Apsara Stack SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Apsara Stack SDK.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-slb</artifactId>
            <version>3.3.9</version>
        </dependency>
</dependencies>
```

#### Configure authentication credentials

When you use Apsara Stack SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. SDK for Java supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client. Not e Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace it with your region ID.
    "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
```

Not e Replace the preceding variables with your actual information. Remove the angle brackets (<>) when you specify the parameters.

#### Call SLB SDK for Java

This topic describes how to call SLB SDK for Java. SDK for Java Procedure
1. Create an AcsClient.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request , where ${apiName} is the API name such as DescribeLoadBalancers. When the SDKs of multiple services are used, different requests may have the same name. Differentiate the requests by SDK package. SDK for Java

```
DescribeLoadBalancersRequest request = new DescribeLoadBalancersRequest(); // Set service-specific parameters. request.setResourceOwnerAccount("test"); // This value is for reference only. Enter a v alue based on your business requirements. request.setResourceOwnerId("1"); // This value is for reference only. Enter a value bas ed on your business requirements. request.setRegionId("test"); // This value is for reference only. Enter a value based o n your business requirements. request.setServerId("test"); // This value is for reference only. Enter a value based o n your business requirements. request.setAddressIPVersion("test"); // This value is for reference only. Enter a value based on your business requirements. request.setLoadBalancerStatus("test"); // This value is for reference only. Enter a val ue based on your business requirements. request.setLoadBalancerId("test"); // This value is for reference only. Enter a value b ased on your business requirements. request.setLoadBalancerName("test"); // This value is for reference only. Enter a value based on your business requirements. request.setServerIntranetAddress("test"); // This value is for reference only. Enter a value based on your business requirements. request.setAddressType("test"); // This value is for reference only. Enter a value base d on your business requirements. request.setInternetChargeType("test"); // This value is for reference only. Enter a val ue based on your business requirements. request.setVpcId("test"); // This value is for reference only. Enter a value based on y our business requirements. request.setVSwitchId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setNetworkType("test"); // This value is for reference only. Enter a value base d on your business requirements. request.setAddress("test"); // This value is for reference only. Enter a value based on your business requirements. request.setMasterZoneId("test"); // This value is for reference only. Enter a value bas ed on your business requirements. request.setSlaveZoneId("test"); // This value is for reference only. Enter a value base d on your business requirements. request.setOwnerAccount("test"); // This value is for reference only. Enter a value bas ed on your business requirements. request.setTags("test"); // This value is for reference only. Enter a value based on yo ur business requirements. request.setPayType("test"); // This value is for reference only. Enter a value based on your business requirements. request.setResourceGroupId("test"); // This value is for reference only. Enter a value based on your business requirements.
```

3. Initiate the request and handle the response.

```java
DescribeLoadBalancersResponse response = client.getAcsResponse(request); System.out.println(JSON.toJSONString(response));
```

#### Handle errors

SDK for Java Server Load Balancer (SLB) SDK for Java returns error codes and messages when errors occur on the server side or the SDK side. You do not need to handle the errors returned by the SDK. You need to only handle the errors on the server side. `ServerException` indicates a server error. `ClientException` indicates an error returned by the SDK. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

The following code provides an example on how to handle errors returned by the SDK:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // Add a computing logic for handling errors.
    // For example, you can obtain the error information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, you can submit a ticket with the request ID included.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add a computing logic for handling errors.
    // For example, you can obtain the error information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}` thon to make API calls

## Use SLB SDK for Python to

make API calls

### Quick start

This topic describes how to obtain and use Server Load Balancer (SLB) SDK for Python. Prerequisites An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. The endpoint of the SLB API is obtained. For more information, see Obtain the endpoint of the SLB API. Install SLB SDK for Python
1. Install the SDK core library.
If you use Python 2.x, run the following command to install the core library of Alibaba Cloud SDK:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install the SDK.
The following example shows how to install SLB SDK for Python: If you use Python 2.x, run the following command to install the SLB SDK:

```
pip install aliyun-python-sdk-slb==3.3.8
```

If you use Python 3.x, run the following command to install the SLB SDK:

```
pip3 install aliyun-python-sdk-slb==3.3.8
```

Call SLB SDK for Python To call SLB SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must obtain a region ID, your
AccessKey ID, and your AccessKey secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.
thon to make API calls Not e In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code. The following section describes the parameters: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <your-endpoint>: Replace the value of this parameter with the endpoint of the service.

```
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBal ancersRequest client = AcsClient('<yourAccessKeyID>', '<yourAccessKeySecret>', '<yourRegionID>') // Create an API request and set the required parameters. request = DescribeLoadBalancersRequest() // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerId("1") // This value is for reference only. Enter a value based on your business requirements. request.set_RegionId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressIPVersion("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerStatus("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerName("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerIntranetAddress("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_InternetChargeType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VpcId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VSwitchId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_NetworkType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Address("test") // This value is for reference only. Enter a value based on your business requirements. request.set_MasterZoneId("test")
```

thon to make API calls

```python
// This value is for reference only. Enter a value based on your business requirements. request.set_SlaveZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_OwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Tags("test") // This value is for reference only. Enter a value based on your business requirements. request.set_PayType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceGroupId("test") response = client.do_action_with_exception(request) // Print the required return values.
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### Work with SLB SDK for Python

#### Install SDK for Python

This topic describes how to install and use Server Load Balancer (SLB) SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip. Not e To use the SDK of an Apsara Stack service, you must install the core library of Alibaba Cloud SDK for Python. For example, if you want to use SLB SDK for Python, you must install the SDK core library for Python and SLB SDK for Python. If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

The following example describes how to install the SLB SDK. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-slb==3.3.8
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-slb==3.3.8
```

#### Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. SDK for Python supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. thon to make API calls If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client. Not ice Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### Set HTTPS requests

SDK for Python allows you to send API requests by using HTTP and HTTPS. You can specify a protocol (HTTP or HTTPS) for a specific request, or set a global default protocol. Not e The default protocol of the service takes precedence over the global default protocol. Add OpenSSL support OpenSSL support in Python is required for sending HTTPS requests by using SDK for Python. To use Alibaba Cloud SDK for Python to send requests over HTTPS, you need to add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later. Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the error message `ImportError: No module named ssl` does not appear, OpenSSL is supported. If OpenSSL is not supported, run the following command to install it:

```
pip install pyopenssl
```

Set the protocol to HTTP or HTTPS for a request The following code shows how to set HTTPS as the protocol for a request:

```bash
request = DescribeLoadBalancersRequest() request.set_protocol_type("https")
# Set the value to https or http.
```

Set a global protocol for all service requests The following code shows how to set a global protocol for all service requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### Call SLB SDK for Python

This topic describes how to call Server Load Balancer (SLB) SDK for Python. thon to make API calls Procedure
1. Import SLB SDK for Python.

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBal ancersRequest
```

2. Create an AcsClient instance.

```
client = AcsClient('<yourAccessKeyId>', '<yourAccessKeySecret>', '<yourRegionID>')
```

3. Create a Request object.
thon to make API calls

```
request = DescribeLoadBalancersRequest() // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerId("1") // This value is for reference only. Enter a value based on your business requirements. request.set_RegionId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressIPVersion("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerStatus("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerName("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerIntranetAddress("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_InternetChargeType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VpcId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VSwitchId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_NetworkType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Address("test") // This value is for reference only. Enter a value based on your business requirements. request.set_MasterZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_SlaveZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_OwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Tags("test") // This value is for reference only. Enter a value based on your business requirements. request.set_PayType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceGroupId("test")
```

4. Initiate a call and handle the response.

```python
response = client.do_action_with_exception(request) // Print the required return values.
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

#### Troubleshooting

thon to make API calls The Python SDK returns error messages when errors occur on the server side or the SDK side. These errors contain detailed error information, including the error code and the error message. You do not need to handle the errors returned by the SDK. You only need to handle server errors based on the error messages generated on the server side. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAcce ssKeyId.NotFound Specified access key is not found.
```

The following code provides an example on how to handle errors returned by SDK for Python:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your own computing logic for handling errors here.
    # For example, you can obtain the error information.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

to make API calls

## Use SLB SDK for Go to make

API calls

### Quick start

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Server Load Balancer (SLB) SDK for Go. Prerequisites An Apsara Stack tenant account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are obtained. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of the SLB API is obtained. For more information, see Obtain the endpoint of the SLB API. Install the core package of Apsara Stack SDK for Go Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

Call SLB SDK for Go To call SLB SDK for Go, perform the following steps:
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and manage the response or exceptions.
Not e In the following code, replace the parameters with your actual information. Delete the angle brackets <> in the final code. The following list describes the parameters: <yourRegionID>: Replace the variable with the region ID. <yourAccessKeyID>: Replace the variable with your AccessKey ID. <yourAccessKeySecret>: Replace the variable with your AccessKey secret. <Endpoint>: Replace the variable with the endpoint.

```java
package main import (
  "fmt"
  slb "github.com/aliyun/alibaba-cloud-sdk-go/services/slb"
```

`)`

```
func main() {
  client, err := slb.NewClientWithAccessKey("cn-hangzhou", "<yourAccessKeyID>", "<yourA
ccessKeySecret>")
```

to make API calls

```
ccesseySecet
```

`)`

```
  // Create an API request and set the required parameters.
  request := ecs.CreateDescribeLoadBalancersRequest()
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ResourceOwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ResourceOwnerId = "1"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.RegionId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ServerId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.AddressIPVersion = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.LoadBalancerStatus = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.LoadBalancerId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.LoadBalancerName = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ServerIntranetAddress = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.AddressType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.InternetChargeType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.VpcId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.VSwitchId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.NetworkType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.Address = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.MasterZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.SlaveZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

to make API calls `s.`

```
  request.OwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.Tags = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.PayType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ResourceGroupId = "test"
  response, err := client.DescribeLoadBalancers(request)
  if err != nil {
    fmt.Println(err)
    return
```

`}`

```
  // Print response parameters. In this example, the RequestId parameter is printed.
  fmt.Println(response.RequestId)
```

`}`
4. Optional. Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### Work with SLB SDK for Go

#### Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. SDK for Go supports authentication based on an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client. Not ice Do not disclose any code containing your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
client, err := slb.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAcce ssKeySecret>")
```

to make API calls Not e In the preceding code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code.

#### Call SLB SDK for Go

This topic describes how to call Server Load Balancer (SLB) SDK for Go.
1. Import SLB SDK for Go.

```java
import (
  "fmt"
  slb "github.com/aliyun/alibaba-cloud-sdk-go/services/slb"
```

`)`
2. Create a client that includes all of the API operations.
Not e In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code.

```
client, err := slb.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<your AccessKeySecret>")
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request . ${service} specifies the service name in lowercase, such as slb. ${apiName} is an API name such as DescribeLoadBalancers.

```
request := slb.CreateDescribeLoadBalancersRequest()
 // This value is for reference only. Enter a value based on your business requirements
```

`.`

```
  request.ResourceOwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ResourceOwnerId = "1"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.RegionId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ServerId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.AddressIPVersion = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.LoadBalancerStatus = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.LoadBalancerId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.` to make API calls

```
  request.LoadBalancerName = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ServerIntranetAddress = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.AddressType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.InternetChargeType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.VpcId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.VSwitchId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.NetworkType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.Address = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.MasterZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.SlaveZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.OwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.Tags = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.PayType = "test"
  // This value is for reference only. Enter a value based on your business requirement
```

`s.`

```
  request.ResourceGroupId = "test"
```

4. Initiate the call.

```
response, err := client.DescribeLoadBalancers(request)
```

#### Troubleshooting

When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned if an error occurs on the server side or on the SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors. Troubleshooting to make API calls You can use the following code to handle errors:

```
  response, err := client.DescribeLoadBalancers(request)
  if err != nil {
    fmt.Println(err)
    return
```

`}` ClientError When you make a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a `ClientError` . The following code shows how to identify and obtain the error message in the `ClientError` : Not ice When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
  "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
  "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := client.DescribeLoadBalancers(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

`}` ServerError When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following code shows how to identify and obtain the error message in ServerError and Response: to make API calls Not ice When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
  "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
  "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := client.DescribeLoadBalancers(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

`}`

## API Reference

### Make API requests

To call a Server Load Balancer (SLB) API operation, you must send an HTTP GET request to the endpoint of the SLB API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8. Request syntax SLB API operations use the RPC protocol. You can call SLB API operations by sending HTTP GET requests. The request syntax is:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the SLB API is `slb.example.com` . Not e `example.com` is a custom domain name. To obtain the domain name, contact an administrator. For more information, see Generate the Apsara Stack API (ASAPI) endpoint. Action: the name of the operation being performed. For example, to query SLB instances, you must set the Action parameter to DescribeLoadBalancers. Version: is the version of the API that you want to use. The current SLB API version is 2014-05-15. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information, see Common parameters. The following example demonstrates how to call the DescribeLoadBalancers operation in SLB. Not e The sample requests are formatted to improve readability.

```
https://slb.example.com/?Action=DescribeLoadBalancers &Format=xml &Version=2014-05-15 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &TimeStamp=2016-02-23T12:46:24Z ...
```

API authorization To ensure the security of your account, we recommend that you call APIs as a Resource Access Management (RAM) user. To call the SLB API as a RAM user, you must create and add a permission policy to the RAM user. For more information about the resources and operations that can be authorized to a RAM user, see RAM authentication. Request signatures You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. SLB implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users. An AccessKey pair is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information, see Obtain an AccessKey pair. You must add the signature to the SLB API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
```

SHA1`&Signature=`xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take the DescribeLoadBalancers operation as an example. If the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the pre-signed request URL is:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-26 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a query string for the signature.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeLoadBalancers&Format%3DXML&SignatureMetho d%3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D 1.0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the hash-based message authentication code (HMAC) value of the string-to-sign.
Append an ampersand (&) to the AccessKey secret as the key for calculating the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YG****E=
```

3. Add the signature to the request parameters:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-15 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### RAM authentication

Before calling an SLB API as a RAM user, you must use an Alibaba Cloud account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, you must use an Alibaba Cloud Resource Name (ARN) as the unique identifier of the resource. Available SLB resources The following table describes the ARN format for different types of SLB resources.

| Resource type | ARN format |
|---|---|
| LoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:slb:$regionid:$accountid:loadbalancer/* |
|   | acs:slb:*:$accountid:loadbalancer/* |
|   | acs:slb:*:*:loadbalancer/* |
| Certificate | acs:slb:$regionid:$accountid:certificate/$servercertificateId |
|   | acs:slb:$regionid:$accountid:certificate/* |

$regionid/accoutid/servercertificateId is the resource ID. `*` indicates the corresponding resources. SLB APIs The following table lists the APIs that can be authorized and their corresponding ARN formats.

| API | ARN format |   |   |
|---|---|---|---|
| CreateLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ModifyLoadBalancerInternetSpec | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteLoadBalancer | rid |   |   |

| API | ARN format |   |   |
|---|---|---|---|
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerStatus | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerName | rid |   |   |
| DescribeLoadBalancers | acs:slb:$regionid:$accountid:loadbalancer/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeLoadBalancerAttribute | rid |   |   |
| DescribeRegions | acs:slb:*:$accountid:* |   |   |
| UploadServerCertificate | acs:slb:%s:%s:certificate/* |   |   |
| DeleteServerCertificate | acs:slb:%s:%s:certificate/% |   |   |
| DescribeServerCertificate | acs:slb:%s:%s:certificate/% |   |   |
| SetServerCertificateName | acs:slb:%s:%s:certificate/% |   |   |
| DescribeServerCertificates | acs:slb:%s:%s:certificate/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerHTTPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerHTTPSListener | rid |   |   |
|   | acs:slb:%s:%s:certificate/% |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerTCPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerUDPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteLoadBalancerListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| StartLoadBalancerListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| StopLoadBalancerListener | rid |   |   |
| SetLoadBalancerHTTPListenerAttribut | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| e | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
|   | rid |   |   |
| SetLoadBalancerHTTPSListenerAttrib |   |   |   |
| 6 |   |   |   |

| erver Load Balancer | Developer Guide·API Referenc |   |   |
|---|---|---|---|
| SetLoadBalancerHTTPSListenerAttrib |   |   |   |
| uAtPeI | ARN format |   |   |
|   | acs:slb:%s:%s:certificate/% |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerTCPListenerAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerUDPListenerAttribute | rid |   |   |
| DescribeLoadBalancerHTTPListenerAt | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| tribute | rid |   |   |
| DescribeLoadBalancerHTTPSListenerA | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ttribute | rid |   |   |
| DescribeLoadBalancerTCPListenerAttr | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ibute | rid |   |   |
| DescribeLoadBalancerUDPListenerAttr | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ibute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| AddBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| RemoveBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeHealthStatus | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateVServerGroup | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetVServerGroupAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteVServerGroup | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeVServerGroups | rid |   |   |

| eveloper Guide·API Reference | Server Load Balance |
|---|---|

| API | ARN format |   |   |
|---|---|---|---|
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeVServerGroupAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| AddVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| RemoveVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ModifyVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |

### Common parameters

Common request parameters Common request parameters are request parameters that you must use when you call any API. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | String | Yes | The API version in the format of YYYY-MM-DD . Valid values: 2014-05-15 |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access a service. |
| Signature | String | Yes | The signature result string. |
| SignatureMethod | String | Yes | The algorithm used to create the request signature. Valid values: HMAC-SHA1 |

| Name | Type | Required | Description |
|---|---|---|---|
| Timestamp | String | Yes | The request timestamp. The timestamp uses UTC and it complies with the ISO 8601 standard. The timestamp format is YYYY-MM-DDThh:mm:ssZ . For example, 20:00:00 on January 1st, 2013 in China Standard Time (UTC +8) would be written as 2013-01- 10T12:00:00Z. |
| SignatureVersion | String | Yes | The signature algorithm version. Valid value: 1.0 |
| SignatureNonce | String | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2014-05-19T10%3A33%3A56Z &Format=xml &AccessKeyId=testid &Action=DescribeLoadBalancerAttribute &SignatureMethod=Hmac-SHA1 &LoadBalancerId=loadBalancerID &SignatureNonce=NwDAxvLU6tFE0DVb &Version=2014-05-15 &SignatureVersion=1.0 &Signature=Signature
```

Common response parameters API responses use a unified format. The 2xx HTTP status code indicates a successful invocation. The 4xx or 5xx HTTP status code indicates a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time a request is sent to call an API, the system returns a unique identifier RequestId, regardless of whether the invocation is successful. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
    <!—Result root node-->
    <API name+Response>
        <!—Returned request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Returned result-->
    </API name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /*Returned result*/
```

`}`

### SLB instance

#### CreateLoadBalancer

Creates a Server Load Balancer (SLB) instance. Before you call this operation, take note of the following items: Before you create an SLB instance, call the DescribeAvailableResource operation to query the resources available for purchase in the zone where you want to create the SLB instance. You are charged for the SLB instances that you create. For more information, see Create an SLB instance. If you do not set LoadBalancerSpec, a shared-resource SLB instance is created. We recommend that you set the LoadBalancerSpec parameter to specify the specification of the SLB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cer | The operation that you want to perform. Set the value to Creat eLoadBalancer. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where you want to create the SLB instance. You can call the DescribeRegions operation to query region IDs. |
| AddressType | String | No | internet | The network type of the SLB instance. Valid values: int ernet and int ranet . int ernet : After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. int ranet : After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InternetChargeTy pe | String | No | paybytraffic | The billing method of the Internet- facing SLB instance. Set the value to paybytraffic. |
| Bandwidth | Integer | No | 10 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit for each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. For more information, see Bandwidth of a shared-resource SLB instance. |
| ClientToken | String | No | 5A2CFF0E-5718- 45B5-9D4D- 70B3FF3898 | This parameter is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LoadBalancerNa me | String | No | abc | The name of the SLB instance. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. If this parameter is not set, the system automatically creates a name for the SLB instance. |
| VpcId | String | No | vpc- bp1aevy8sofi8mh 1***** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- bp12mw1f8k3jgy ***** | The ID of the vSwitch to which the internal-facing SLB instance belongs. The vSwitch must be deployed in a VPC. To create an internal-facing SLB instance that is deployed in a VPC, you must set this parameter. If this parameter is set, the value of the AddessT ype parameter is set to int ranet by default. |
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| access key id _ _ | String | No | 111 | The AccessKey ID. |
| Tags | String | No | test | The tags that you want to add to the SLB instance. |
| EnableVpcVipFlo w | String | No | 1 | The flow log. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerSpe c | String | No | slb.s2.small | Apsara Stack provides two types of SLB instance: shared-resource SLB instances and high-performance SLB instances. You can create high-performance SLB instances of different specifications. Valid values: slb.s1.small slb.s2.small slb.s3.small slb.s2.medium For more information about the specifications of high-performance SLB instances, see High-performance SLB instances. |
| AddressIPVersion | String | No | ipv4 | The IP version that is used by the SLB instance. Valid values: ipv4 and ipv6. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-hddhfjg******* | The ID of the SLB instance. |
| Address | String | 42.250.**.** | The IP address that is allocated to the SLB instance. |
| VpcId | String | vpc-25dvzy9***** | The ID of the VPC to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecr*** | The ID of the vSwitch to which the SLB instance belongs. |
| LoadBalancerN ame | String | abc | The name of the SLB instance. |
| AddressIPVersi on | String | ipv4 | The IP version that is used by the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkType | String | classic | The type of network where the SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancer &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerResponse>
    <NetworkType>vpc</NetworkType>
      <LoadBalancerName>abc</LoadBalancerName>
      <Address>192.168.0.**</Address>
      <ResourceGroupId>rg-acfmxazb***</ResourceGroupId>
      <RequestId>AB197CF0-D9E9-4475-A89D-35DBCCF13BBE</RequestId>
      <AddressIPVersion>ipv4</AddressIPVersion>
      <LoadBalancerId>lb-bp1b6c719dfa0***</LoadBalancerId>
      <VSwitchId>vsw-bp12mw1f8k3jgygk9****</VSwitchId>
      <VpcId>vpc-bp1aevy8sofi8mh1q***</VpcId>
</CreateLoadBalancerResponse>
```

`JSON` format

```json
{"LoadBalancerName":"abc", "VpcId":"vpc-25dvzy9*****", "Address":"42.250.**.**", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "NetworkType":"classic", "AddressIPVersion":"ipv4", "VSwitchId":"vsw-255ecr***", "LoadBalancerId":"lb-hddhfjg*******"}
```

#### DeleteLoadBalancer

Deletes a pay-as-you-go Server Load Balancer (SLB) instance. Not e After you delete an SLB instance, the listeners configured for the SLB instance and the tags added to the SLB instance are deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalan cer | The operation that you want to perform. Set the value to Delet eLoadBalancer. |
| LoadBalancerId | String | Yes | lb- bp1h66tp5uat8** ** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

If the SLB instance that you want to delete has deletion protection enabled, the system reports an error in the following formats: JSON format `{`

```json
 "RequestId": "7B7AB375-1EA6-4A18-9D1C-F258F2D57638",
 "HostId": "slb.aliyuncs.com",
 "Code": "OperationDenied.DeleteProtectionIsOn",
 "Message": "The loadbalancer can't be deleted due to DeleteProtection is enabled."
```

`}` XML format

```xml
   <?xml version="1.0" encoding="UTF-8" ?>
        <DeleteLoadBabalancerResponse>
 <RequestId>7B7AB375-1EA6-4A18-9D1C-F258F2D57638</RequestId>
 <HostId>slb.aliyuncs.com</HostId>
 <Code>OperationDenied.DeleteProtectionIsOn</Code>
 <Message>The loadbalancer can't be deleted due to DeleteProtection is enabled.</Message>
       </DeleteLoadBabalancerResponse>
```

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancer &LoadBalancerId=lb-bp1h66tp5uat8******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteLoadBabalancerResponse>
   <RequestId>E3F602B8-A162-4683-A7EC-49364E597259</RequestId>
</DeleteLoadBabalancerResponse>
```

`JSON` format `{`

```json
    "RequestId": "0D9B7343-AC1F-498C-A18A-78FE14A7C3A3"
```

`}`

#### ModifyLoadBalancerInstanceSpec

Modifies the specification of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalan cerInstanceSpec | The operation that you want to perform. Set the value to Modif yLoadBalancerInst anceSpec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719df**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerSpe c | String | Yes | slb.s1.small | The specification of the SLB instance. Valid values: slb.s1.small slb.s2.small slb.s2.medium slb.s3.small slb.s3.medium slb.s3.large The supported specifications vary by region. For more information, see Instance types . Not e When you change a shared-resource SLB instance to a high-performance SLB instance, your service may be temporarily interrupted for 10 to 30 seconds. Therefore, we recommend that you modify the specification during off-peak hours. In addition, you can use Alibaba Cloud DNS (DNS) to schedule your workloads to another SLB instance before you modify the specification. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInstanceSpec &LoadBalancerId=lb-bp1b6c719df**** &LoadBalancerSpec=slb.s2.small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyLoadBalancerInstanceSpecResponse>
     <RequestId>D456A34A-6E40-4379-8DAF-9175760FE215</RequestId>
  </ModifyLoadBalancerInstanceSpecResponse>
```

`JSON` format `{`

```json
    "ModifyLoadBalancerInstanceSpecResponse": {
        "RequestId": "D456A34A-6E40-4379-8DAF-9175760FE215"
```

`}` `}`

#### ModifyLoadBalancerInternetSpec

Modifies the billing method of an Internet-facing Server Load Balancer (SLB) instance. You can modify the billing method of an Internet-facing SLB instance in the following ways: Change the bandwidth limit of a pay-by-bandwidth SLB instance. The new bandwidth limit immediately takes effect. Change the billing method of an SLB instance from pay-by-data-transfer to pay-by-bandwidth. The new billing method takes effect at 00:00 the following day. Change the billing method of an SLB instance from pay-by-bandwidth to pay-by-data-transfer. The new billing method takes effect at 00:00 the following day. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalan cerInternetSpec | The operation that you want to perform. Set the value to Modif yLoadBalancerInt ernet Spec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | 10 | The bandwidth limit of the Internet- facing SLB instance that is billed on a pay-by-bandwidth basis. Unit: Mbit/s. Valid values: 1 t o 5000. The bandwidth limit varies based on the region where the SLB instance is created. Not e You do not need to set this parameter for pay-by- data-transfer SLB instances. In this case, the value of Int ernet ChargeT ype is paybyt raf f ic. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInternetSpec &LoadBalancerId=lb-bp1b6c719dfa08ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyLoadBalancerInternetSpecResponse>
      <RequestId>E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED</RequestId>
</ModifyLoadBalancerInternetSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED"
```

`}`

#### SetLoadBalancerName

Modifies the name of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer Name | The operation that you want to perform. Set the value to Set LoadBalancerName. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 e**** | The ID of the SLB instance. |
| LoadBalancerNa me | String | Yes | lb-instance-test | The name of the SLB instance. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerName &LoadBalancerId=lb-bp1b6c719dfa08e**** &LoadBalancerName=abc1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerStatusResponse>
   <RequestId>3C7F675E-9F82-4806-BA47-FF57E3ACC850</RequestId>
</SetLoadBalancerStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "3C7F675E-9F82-4806-BA47-FF57E3ACC850"
```

`}`

#### SetLoadBalancerStatus

Sets the state of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer Status | The operation that you want to perform. Set the value to Set LoadBalancerSt at us. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 e**** | The ID of the SLB instance. |
| LoadBalancerStat us | String | Yes | active | The state of the SLB instance. Valid values: act ive and inact ive. act ive (default) When an SLB instance is in the Active state, listeners of the SLB instance can forward inbound traffic based on forwarding rules. inact ive When an SLB instance is in the inact ive state, listeners of the SLB instance do not forward inbound traffic. Not e If all listeners of an SLB instance are deleted, the SLB instance automatically switches to the inact ive state. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerStatus &LoadBalancerId=lb-bp1b6c719dfa08e****** &LoadBalancerStatus=active &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerStatusResponse>
     <RequestId>E6DDFE22-F019-4F34-B8DD-FD14973450A6</RequestId>
  </SetLoadBalancerStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "E6DDFE22-F019-4F34-B8DD-FD14973450A6"
```

`}`

#### DescribeLoadBalancerAttribute

Queries detailed information about a specified Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerAt t ribut e. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-dhhd**** | The ID of the SLB instance. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the SLB instance is deployed. |
| RegionIdAlias | String | cn-qingdao-env17- d01 | The alias of the region where the SLB instance is deployed. |
| LoadBalancerN ame | String | abc | The name of the SLB instance. |
| LoadBalancerSt atus | String | active | The state of the SLB instance. Valid values: inact ive: The SLB instance is stopped. SLB instances in the inactive state do not forward traffic. act ive: The SLB instance runs as expected. Newly created SLB instances are in the act ive state by default. locked: The SLB instance is locked. SLB instances may be locked due to overdue payments or other reasons. |
| Address | String | 42.XX.XX.6 | The IP address that the SLB instance uses to provide services. |
| AddressType | String | internet | The type of IP address that the SLB instance uses to provide services. |
| NetworkType | String | vpc | The type of network where the SLB instance is deployed. |

| eveloper Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | Description |
| VpcId | String | vpc-25dvzy9f8**** | The ID of the virtual private cloud (VPC) where the internal-facing SLB instance is deployed. |
| Bandwidth | Integer | 5 | The bandwidth limit of the Internet-facing SLB instance that is billed on a pay-by- bandwidth basis. |
| CreateTime | String | 2017-08- 31T02:49:05Z | The time when the SLB instance was created. |
| ListenerPorts | List | 80 | The list of frontend ports that are used by the SLB instance. |
| ListenerPortsAn dProtocol | Array of ListenerPortAn dProtocol |   | The list of frontend ports and protocols that are used by the SLB instance. |
| ListenerPortAn dProtocol |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtoco l | String | https | The frontend protocol that is used by the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers that are added to the SLB instance. |
| BackendServer |   |   |   |
| ServerId | String | i-djghr2**** | The ID of the backend server. |
| Weight | Integer | 90 | The weight of the backend server. |
| ServerIp | String | 192.168.0.1 | The IP address of the backend server. |
| Type | String | ecs | The type of the backend server. |
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AutoReleaseTi me | Long | 1513947075 | The timestamp that indicates when the SLB instance was released. |
| CreateTimeSta mp | Long | 1504147745000 | The timestamp that indicates when the SLB instance was created. |
| EndTime | String | 2999-09- 08T16:00:00Z | The time when the SLB instance was suspended. |
| EndTimeStamp | Long | 32493801600000 | The timestamp that indicates when the SLB instance was suspended. |
| InternetCharge Type | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Valid values: paybybandwidt h and paybyt raf f ic. paybybandwidt h: pay-by-bandwidth paybyt raf f ic (default): pay-by-data- transfer |
| ListenerPortsAn dProtocal | Array of ListenerPortAn dProtocal |   | The port and protocol of the listener. |
| ListenerPortAn dProtocal |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtoca l | String | http | The frontend protocol that is used by the SLB instance. |
| LoadBalancerS pec | String | slb.s2.small | The specification of the SLB instance. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecrwq5**** | The ID of the vSwitch to which the internal- facing SLB instance belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerAttribute &LoadBalancerId=lb-bp1b6c719dfa08ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerAttributeResponse>
      <CreateTimeStamp>1541679713000</CreateTimeStamp>
   <RegionIdAlias>cn-hangzhou</RegionIdAlias>
   <BackendServers>
      <BackendServer>
         <ServerId>i-bp1c3zrr37ablp8ujo7v</ServerId>
         <Weight>100</Weight>
         <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
   <HasReservedInfo>false</HasReservedInfo>
   <ListenerPorts></ListenerPorts>
   <InternetChargeType>paybytraffic</InternetChargeType>
   <VSwitchId>vsw-bp12mw1f8k3*********</VSwitchId>
   <VpcId>vpc-bp1aevy8sofi8mh*****</VpcId>
   <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
   <LoadBalancerSpec>slb.s2.small</LoadBalancerSpec>
   <NetworkType>vpc</NetworkType>
   <ListenerPortsAndProtocol></ListenerPortsAndProtocol>
   <PayType>PayOnDemand</PayType>
   <Bandwidth>5120</Bandwidth>
   <LoadBalancerName>abc1</LoadBalancerName>
   <ResourceGroupId>rg-acfmxazb4p*****</ResourceGroupId>
   <AddressIPVersion>ipv4</AddressIPVersion>
   <LoadBalancerId>lb-bp1b6c719dfa08e*****</LoadBalancerId>
   <EndTimeStamp>32493801600000</EndTimeStamp>
   <MasterZoneId>cn-hangzhou-b</MasterZoneId>
   <ListenerPortsAndProtocal></ListenerPortsAndProtocal>
   <Address>192.168.0.1</Address>
   <RegionId>cn-hangzhou</RegionId>
   <RequestId>35D745B3-1567-4855-9EF1-F5CED3C1670C</RequestId>
   <CreateTime>2018-11-08T12:21:53Z</CreateTime>
   <AddressType>intranet</AddressType>
   <EndTime>2999-09-08T16:00:00Z</EndTime>
   <LoadBalancerStatus>active</LoadBalancerStatus>
</DescribeLoadBalancerAttributeResponse>
```

`JSON` format `{`

```json
    "CreateTimeStamp": 1541679713000,
    "RegionIdAlias": "cn-hangzhou",
    "BackendServers": {
        "BackendServer": [
```

`{`

```json
                "ServerId": "i-bp1c3zrr37ab*****",
                "Weight": 100,
                "Type": "ecs"
```

`}` `]` `},`

```json
    "HasReservedInfo": "false",
    "ListenerPorts": {
        "ListenerPort": [ ]
```

`},`

```json
    "InternetChargeType": "paybytraffic",
    "VSwitchId": "vsw-bp12mw1f8k******",
    "VpcId": "vpc-bp1aevy8sofi8mh******",
    "SlaveZoneId": "cn-hangzhou-d",
    "LoadBalancerSpec": "slb.s2.small",
    "NetworkType": "vpc",
    "ListenerPortsAndProtocol": {
        "ListenerPortAndProtocol": [ ]
```

`},`

```json
    "PayType": "PayOnDemand",
    "Bandwidth": 5120,
    "LoadBalancerName": "abc1",
    "ResourceGroupId": "rg-acfmxazb*****",
    "AddressIPVersion": "ipv4",
    "LoadBalancerId": "lb-bp1b6c719dfa08*****",
    "EndTimeStamp": 32493801600000,
    "MasterZoneId": "cn-hangzhou-b",
    "ListenerPortsAndProtocal": {
        "ListenerPortAndProtocal": [ ]
```

`},`

```json
    "Address": "192.168.0.1",
    "RegionId": "cn-hangzhou",
    "RequestId": "35D745B3-1567-4855-9EF1-F5CED3C1670C",
    "CreateTime": "2018-11-08T12:21:53Z",
    "AddressType": "intranet",
    "EndTime": "2999-09-08T16:00:00Z",
    "LoadBalancerStatus": "active"
```

`}`

#### DescribeLoadBalancers

Queries Server Load Balancer (SLB) instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncers | The operation that you want to perform. Set the value to DescribeLoadBalancers. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. You can query the region ID from the Regions and zones list or by calling the DescribeRegions operation. |
| ServerId | String | No | vm-23**** | The ID of the backend server that is added to the SLB instance. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa*** * | The ID of the SLB instance. You can specify at most 10 IDs in each request. Separate multiple IDs with commas (,). |
| LoadBalancerNa me | String | No | abc1 | The name of the SLB instance. You can specify at most 10 names in each request. Separate multiple names with commas (,). |
| ServerIntranetAd dress | String | No | 10.XX.XX.6 | The private IP address of the backend server that is added to the SLB instance. You can specify multiple IP addresses to query SLB instances. Separate multiple IP addresses with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AddressType | String | No | intranet | The type of network where the SLB instance is deployed. Valid values: int ranet and int ernet . int ernet : After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. int ranet : After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |
| InternetChargeTy pe | String | No | paybybandwidth | The billing method of the Internet- facing SLB instance. Valid values: paybybandwidt h and paybyt raf f ic. paybybandwidt h: pay-by- bandwidth paybyt raf f ic: pay-by-data- transfer. Not e If you do not specify this parameter, the billing method of the SLB instance remains unchanged. |
| VpcId | String | No | vpc- bp1aevy8sof**** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |
| VSwitchId | String | No | vsw- bp12mw1f8k3*** * | The ID of the vSwitch to which the SLB instance belongs. |
| NetworkType | String | No | vpc | The type of network where the internal-facing SLB instance is deployed. Valid values: vpc and classic. vpc: a VPC classic: a classic network |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Address | String | No | 192.168.0.1 | The IP address that the SLB instance uses to provide services. |
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. Multiple zones are not supported for users whose workloads are deployed on Alibaba Finance Cloud. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The list of tags that are added to the SLB instances. The tags must be key- value pairs in a JSON dictionary. You can specify at most 10 tags in each request. |
| PayType | String | No | PayOnDemand | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. PayOnDemand: pay-as-you-go PrePay: subscription |
| AddressIPVersion | String | No | ipv4 | The IP version. Valid values: ipv4 and ipv6. Not e You can create high- performance IPv6 SLB instances only in the following zones: Hangzhou Zone E and Hangzhou Zone F in the China (Hangzhou) region, Beijing Zone F and Beijing Zone G in the China (Beijing) region, Nantong Zone D and Nantong Zone E in the China (Nantong) region, Zhangjiakou Zone A and Zhangjiakou Zone B in the China (Zhangjiakou) region, and Shenzhen Zone D and Shenzhen Zone E in the China (Shenzhen) region. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancers | Array of LoadBalancer |   | The list of SLB instances. |
| LoadBalancer |   |   |   |
| LoadBalancerId | String | lb-hjfng**** | The ID of the SLB instance. |
| LoadBalancerN ame | String | def | The name of the SLB instance. |
| LoadBalancerSt atus | String | active | The state of the SLB instance. Valid values: inact ive: Listeners do not forward requests. act ive: Newly created SLB instances are in the active state by default. locked: The SLB instance is locked. |
| Address | String | 100.XX.XX.28 | The IP address of the SLB instance. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the SLB instance is deployed. |
| RegionIdAlias | String | cn-qingdao-env17- d01 | The name of the region where the SLB instance is deployed. |
| AddressType | String | intranet | The type of network where the SLB instance is deployed. |
| VSwitchId | String | vsw-255ecr**** | The ID of the vSwitch to which the internal- facing SLB instance belongs. |
| VpcId | String | vpc-25dvzy9f8**** | The ID of the VPC to which the internal- facing SLB instance belongs. |
| NetworkType | String | vpc | The type of network where the internal- facing SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| CreateTime | String | 2017-08- 31T02:49:05Z | The time when the SLB instance was created. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone where the SLB instance is deployed. |
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone where the SLB instance is deployed. |
| AddressIPVersi on | String | ipv4 | The IP version. Valid values: ipv4 and ipv6. |
| CreateTimeSta mp | Long | 1504147745000 | The timestamp generated when the SLB instance was created. |
| InternetCharge Type | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Set the value to paybytraffic. paybyt raf f ic (default): pay-by-data- transfer Not e If the value of the PayType parameter is set to PrePay, only pay-by- bandwidth is supported. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancers &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>50</PageSize>
      <LoadBalancers>
            <LoadBalancer>
                  <CreateTimeStamp>1541679713000</CreateTimeStamp>
                  <LoadBalancerName>abc1</LoadBalancerName>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxaz*******y</ResourceGroupId>
                  <AddressIPVersion>ipv4</AddressIPVersion>
                  <LoadBalancerId>lb-bp1b6c********fuca5</LoadBalancerId>
                  <VSwitchId>vsw-bp12mw1f********bmlj</VSwitchId>
                  <InternetChargeType>4</InternetChargeType>
                  <VpcId>vpc-bp1aevy8*********5cm</VpcId>
                  <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
                  <NetworkType>vpc</NetworkType>
                  <MasterZoneId>cn-hangzhou-b</MasterZoneId>
                  <CreateTime>2018-11-08T20:21Z</CreateTime>
                  <Address>192.168.0.**</Address>
                  <RegionId>cn-hangzhou</RegionId>
                  <AddressType>intranet</AddressType>
                  <PayType>PayOnDemand</PayType>
                  <LoadBalancerStatus>active</LoadBalancerStatus>
            </LoadBalancer>
      </LoadBalancers>
      <RequestId>1C7445CB-C21C-4C19-9A3C-65C3190D1944</RequestId>
</DescribeLoadBalancersResponse>
```

`JSON` format `{`

```json
    "DescribeLoadBalancersResponse": {
        "PageNumber": 1,
        "TotalCount": 1,
        "PageSize": 50,
        "LoadBalancers": {
            "LoadBalancer": {
                "CreateTimeStamp": 1541679713000,
                "LoadBalancerName": "abc1",
                "RegionIdAlias": "cn-hangzhou",
                "ResourceGroupId": "rg-acfmxaz*******y",
                "AddressIPVersion": "ipv4",
                "LoadBalancerId": "lb-bp1b6c********fuca5",
                "VSwitchId": "vsw-bp12mw1f********bmlj",
                "InternetChargeType": 4,
                "VpcId": "vpc-bp1aevy8*********5cm",
                "SlaveZoneId": "cn-hangzhou-d",
                "NetworkType": "vpc",
                "MasterZoneId": "cn-hangzhou-b",
                "CreateTime": "2018-11-08T20:21Z",
                "Address": "192.168.0.**",
                "RegionId": "cn-hangzhou",
                "AddressType": "intranet",
                "PayType": "PayOnDemand",
                "LoadBalancerStatus": "active"
```

`}` `},`

```json
        "RequestId": "1C7445CB-C21C-4C19-9A3C-65C3190D1944"
```

`}` `}`

#### DescribeRegions

Queries regions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | The list of regions. |

|   | Developer Guide·AP | I Reference |   | Server Load Balance | r |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Region |   |   |   |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region. |
| LocalName | String | China (Qingdao) | The name of the region. |
| RequestId | String | 1651FBB6-4FBF- 49FF-A9F5- DF5D696C7EC6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6</RequestId> <Regions>
    <Region>
        <RegionId>cn-beijing</RegionId>
        <LocalName>China (Beijing)</LocalName>
    </Region>
</Regions>
```

`JSON` format `{`

```json
    "RequestId": "1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6",
    "Regions": {
        "Region": {
            "RegionId": "cn-beijing",
            "LocalName": "China (Beijing)"
```

`}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Acquire the permissions and try again. |

#### DescribeZones

Queries zones in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array of Zone |   | The list of zones. |
| Zone |   |   |   |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| LocalName | String | Hangzhou Zone | The name of the zone. |
| SlaveZones | Array of SlaveZone |   | The list of secondary zones. |
| SlaveZone |   |   |   |
| ZoneId | String | cn-hangzhou-g | The ID of the secondary zone. |
| LocalName | String | Hangzhou Zone G | The name of the secondary zone. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A48D35FF-440A- 4BC0-A4A2- A9BF69B7E43A | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeZones &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeZonesResponse>
  <RequestId>3FF183FF-F4AA-40E8-8B5D-90788C6799C2</RequestId>
   <Zones>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
               <LocalName>Hangzhou Zone D</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <LocalName>Hangzhou Zone B</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
               <LocalName>Hangzhou Zone E</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-d</ZoneId>
         <LocalName>Hangzhou Zone D</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-f</ZoneId>
               <LocalName>Hangzhou Zone F</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
               <LocalName>Hangzhou Zone D</LocalName>
```

`g` `/`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <LocalName>Hangzhou Zone E</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
               <LocalName>Hangzhou Zone E</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <LocalName>Hangzhou Zone F</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-h</ZoneId>
               <LocalName>Hangzhou Zone H</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-b</ZoneId>
               <LocalName>Hangzhou Zone B</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-g</ZoneId>
         <LocalName>Hangzhou Zone G</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-h</ZoneId>
         <LocalName>Hangzhou Zone H</LocalName>
      </Zone>
   </Zones>
</DescribeZonesResponse>
```

`JSON` format `{`

```json
    "DescribeZonesResponse": {
        "RequestId": "3FF183FF-F4AA-40E8-8B5D-90788C6799C2",
        "Zones": {
            "Zone": [
```

`{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{` `"Z`

```
Id"
```

`"` `h` `h` `"`

```json
                                "ZoneId": "cn-hangzhou-g",
                                "LocalName": "Hangzhou Zone G"
```

`},` `{`

```json
                                "ZoneId": "cn-hangzhou-d",
                                "LocalName": "Hangzhou Zone D"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-b",
                    "LocalName": "Hangzhou Zone B"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
                            "LocalName": "Hangzhou Zone E"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-d",
                    "LocalName": "Hangzhou Zone D"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{`

```json
                                "ZoneId": "cn-hangzhou-f",
                                "LocalName": "Hangzhou Zone F"
```

`},` `{`

```json
                                "ZoneId": "cn-hangzhou-d",
                                "LocalName": "Hangzhou Zone D"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-e",
                    "LocalName": "Hangzhou Zone E"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
                            "LocalName": "Hangzhou Zone E"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-f",
                    "LocalName": "Hangzhou Zone F"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{`

```json
                                "ZoneId": "cn-hangzhou-h",
                                "LocalName": "Hangzhou Zone H"
```

`}` `},` `{`

```json
                                "ZoneId": "cn-hangzhou-b",
                                "LocalName": "Hangzhou Zone B"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-g",
                    "LocalName": "Hangzhou Zone G"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-g",
                            "LocalName": "Hangzhou Zone G"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-h",
                    "LocalName": "Hangzhou Zone H"
```

`}` `]` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Request the permissions and try again. |

### Listeners

#### TCP listeners

##### CreateLoadBalancerTCPListener

Creates a TCP listener. Not e Newly created listeners are in the Stopped state. After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerTCPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerT CPList ener. |
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit of each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. Not e Only high- performance SLB instances support the sch and tch consistent hashing algorithms. |
| PersistenceTimeo ut | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 t o 3600. Unit: seconds. Default value: 0. By default, session persistence is disabled. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. |
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period of a health check response. Valid values: 1 t o 300. Unit: seconds. Default value: 5. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 t o 65535. If you do not set this parameter, the port of the backend server is used for health checks. |
| healthCheckInterv al | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.),and hyphens (-). |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter to enable HTTP health checks for the TCP listener. If this parameter is not set, TCP health checks are performed. |
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. Default _ _ value: http 2xx. _ |
| HealthCheckType | String | No | tcp | The type of health checks. Valid values: t cp and ht t p. Default value: tcp. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterSlaveServe rGroupId | String | No | rsp-0bfucw**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| EstablishedTimeo ut | Integer | No | 500 | The timeout period of a connection. Valid values: 10 t o 900. Unit: seconds. |
| Description | String | No | CreateListeners. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain Chinese _ characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerTCPListener &Bandwidth=-1 &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerTCPListenerResponse>
     <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</CreateLoadBalancerTCPListenerResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.VServerGroupId AndMasterSlaveServ erGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the VServerGroupId parameter or the MasterSlaveServerGroupId parameter does not match. |

##### SetLoadBalancerTCPListenerAttribute

Modifes the configurations of a TCP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer TCPListenerAttrib ute | The operation that you want to perform. Set the value to Set LoadBalancerT CPList enerAt t rib ut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | 43 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1 and 1 t o 5120. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 t o 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit of each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. Not e Only high- performance SLB instances support the sch and tch consistent hashing algorithms. |
| PersistenceTimeo ut | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 to 3600. Unit: seconds. Default value: 0. If you set the value to 0, session persistence is disabled. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 to 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 to 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the health check fails. Valid values: 1 to 300. Unit: seconds. Not e If the value of the Healt hCheckConnect T imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the HCT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. If this parameter is not set, the port specified in BackendServerPort is used for health checks. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. $ ip: The private IP address of the _ backend server. If you do not set this parameter or set the parameter to $ ip, the SLB _ instance uses the private IP address of each backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. ) |
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ |
| HealthCheckType | String | No | tcp | The type of health checks. Valid values: t cp and ht t p. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SynProxy | String | No | enable | Specifies whether to enable SynProxy to protect backend servers against attacks. We recommend that you use the default value for this parameter. Valid values: enable and disable. |
| MaxConnection | Integer | No | 20 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| VServerGroupId | String | No | rsp-cige6j5**** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-cige**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| MasterSlaveServe rGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and of f . You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| EstablishedTimeo ut | Integer | No | 500 | The timeout period of connections. Valid values: 10 to 900. Unit: seconds. |
| Description | String | No | test | The description of the TCP listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerTCPListenerAttributeResponse>
     <RequestId>59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1</RequestId>
</SetLoadBalancerTCPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1"
```

`}`

##### DescribeLoadBalancerTCPListenerAttribute

Queries the configurations of a TCP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerTCPListenerA ttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerT CPList enerA t t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| eveloper Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y**** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. Not e When the SLB instance uses a vServer group, this parameter is not displayed. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet- facing SLB instance, this value is set to -1. This indicates that the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, a bandwidth limit is set for each listener. The sum of bandwidth limit values that are set for all listeners of an SLB instance does not exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: indicates that the listener runs as expected. st opped: indicates that the listener is stopped. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SynProxy | String | enable | Indicates whether SynProxy is enabled. SynProxy is a feature that protects SLB from attacks. We recommend that you use the default value for this parameter. Valid values: Enable: SynProxy is enabled. Disable: SynProxy is disabled. |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| PersistenceTim eout | Integer | 0 | Indicates whether session persistence is enabled. If the value is set to 0, it indicates that session persistence is disabled. |
| HealthCheckTy pe | String | tcp | The health check method that is used by the TCP listener. Valid values: t cp and ht t p. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. |

|   | Parameter | Type |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | HealthCheckInt erval | Integer |   | 5 | The interval between two consecutive health checks. Unit: seconds. |   |   |
|   | HealthCheckDo main | String |   | www.domain.com | The domain name that is used for health checks. |   |   |
|   | HealthCheckURI | String |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), |   |   |
|   |   |   |   |   |   | hyphens (-), forward slashes (/), |   |
|   |   |   | ing | /test/index.html | periods (.),%?number signs (#), and |   |   |
|   |   |   |   |   | ampersands (&) |   |   |
|   | HealthCheckHtt pCode | String |   | http 2xx _ | The HTTP status code that indicates a successful health check. Valid values: ht t p 2xx, ht t p 3xx, ht t p 4xx, and _ _ _ ht t p 5xx. Default value: http 2xx. _ _ |   |   |
|   | VServerGroupId | String |   | rsp-cige6******8 | The ID of the associated vServer group. |   |   |
|   | Description | String |   | Description. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain _ Chinese characters. |   |   |
|   | EstablishedTim eout | Integer |   | 500 | The timeout period of connections. Valid values: 10 t o 900. Unit: seconds. |   |   |
|   | HealthCheckCo nnectTimeout | Integer |   | 100 | The timeout period of a health check response. |   |   |
|   | MasterSlaveSer verGroupId | String |   | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |   |   |
|   | MaxConnection | Integer |   | 10 | The maximum number of connections. |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerTCPListenerAttributeResponse>
     <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
   <PersistenceTimeout>0</PersistenceTimeout>
   <HealthCheckType>tcp</HealthCheckType>
   <HealthyThreshold>3</HealthyThreshold>
   <Scheduler>wrr</Scheduler>
   <UnhealthyThreshold>3</UnhealthyThreshold>
   <Bandwidth>-1</Bandwidth>
   <Description>tcp_80</Description>
   <AclStatus>off</AclStatus>
   <HealthCheckURI>/</HealthCheckURI>
   <HealthCheck>on</HealthCheck>
   <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout>
   <ListenerPort>80</ListenerPort>
   <Status>running</Status>
   <EstablishedTimeout>900</EstablishedTimeout>
   <HealthCheckDomain></HealthCheckDomain>
   <HealthCheckInterval>2</HealthCheckInterval>
   <RequestId>9A113A8C-BB8F-475E-9533-7819ECA2FFC1</RequestId>
   <BackendServerPort>80</BackendServerPort>
    </DescribeLoadBalancerTCPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "PersistenceTimeout": 0,
    "HealthCheckType": "tcp",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "UnhealthyThreshold": 3,
    "Bandwidth": -1,
    "Description": "tcp_80",
    "AclStatus": "off",
    "HealthCheckURI": "/",
    "HealthCheck": "on",
    "HealthCheckConnectTimeout": 5,
    "ListenerPort": 80,
    "Status": "running",
    "EstablishedTimeout": 900,
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "RequestId": "9A113A8C-BB8F-475E-9533-7819ECA2FFC1",
    "BackendServerPort": 80
```

`}`

#### UDP listeners

##### CreateLoadBalancerUDPListener

Creates a UDP listener. Not e You cannot view the source IP addresses of network traffic if you create UDP listeners for a Server Load Balancer (SLB) instance that is deployed in a classic network. In addition, newly created listeners are in the st opped state. After a listener is created, you must call the StartLoadBalancerListener operation to enable the listener. This way, the listener can forward network traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerUDPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerUDPList ener. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 34 | The bandwidth limit of the listener. Unit: Mbit/s. Set the value to -1.For a pay-by-data- transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y7**** | The ID of the SLB instance. |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. qch: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Not e Only high- performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 t o 300. Unit: seconds. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 t o 65535. If you do not specify this parameter, the backend port is used to send health check probes. |
| healthCheckInterv al | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. |
| healthCheckReq | String | No | hello | Specifies the request string for UDP listener health checks. The request string must be 1 to 500 characters in length, and can contain only letters and digits. |
| healthCheckExp | String | No | ok | Specifies the response string for UDP listener health checks. The response string must be 1 to 500 characters in length, and can contain only letters and digits. |
| VServerGroupId | String | No | rsp-cige6j****8 | The ID of the vServer group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterSlaveServe rGroupId | String | No | rsp-0bfucwu**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| Description | String | No | test | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain Chinese _ characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerUDPListener &Bandwidth=34 &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y7****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerUDPListenerResponse>
      <RequestId>06F00FBB-3D9E-4CCE-9D43-1A6946A75456</RequestId>
</CreateLoadBalancerUDPListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "06F00FBB-3D9E-4CCE-9D43-1A6946A75456"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.VServerGroupId AndMasterSlaveServ erGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the VServerGroupId parameter or the MasterSlaveServerGroupId parameter does not match. |

##### SetLoadBalancerUDPListenerAttribute

Modifies the configurations of a UDP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer UDPListenerAttrib ute | The operation that you want to perform. Set the value to Set LoadBalancerUDPList enerAt t rib ut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb4 3ecu4sf-c**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 t o 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify a value as the bandwidth limit for each listener. The sum of maximum bandwidth values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. For more information, see Bandwidth limit of a shared- resource SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. qch: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Not e Only high- performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 to 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 to 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 to 300. Not e If the value of the Healt hCheckConnect T imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCheckConnect T imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 to 65535. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| healthCheckReq | String | No | hello | The request string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| healthCheckExp | String | No | ok | The response string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . Not e You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| VServerGroupId | String | No | rsp-cige6**** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-0bfuc**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| MasterSlaveServe rGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and of f . You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| Description | String | No | test | The description of the listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43ecu4sf-c**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerUDPListenerAttributeResponse>
     <RequestId>A0F0643E-D653-4F6F-A67F-205B2A92BE18</RequestId>
</SetLoadBalancerUDPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "A0F0643E-D653-4F6F-A67F-205B2A92BE18"
```

`}`

##### DescribeLoadBalancerUDPListenerAttribute

Queries the configurations of a UDP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerUDPListenerA ttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerUDPList ener At t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb4 3e**** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 53 | The backend port that is used by the SLB instance. Not e If the listener is associated with a vServer group, this parameter is not returned. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet- facing SLB instance, this value is set to -1. This indicates that the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, each listener has a bandwidth limit. The sum of bandwidth limit values that are set for all listeners of an SLB instance does not exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: indicates that the listener runs as expected. st opped: indicates that the listener is stopped. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckCo nnectTimeout | Integer | 100 | The timeout period for a health check response. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the listener. |
| Description | String | AccessControlDescri ption. | The description of access control. |
| HealthCheckExp | String | ok | The response string for UDP listener health checks. |

| S | erver Load Balanc | er |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckRe q | String | hello | The request string for UDP listener health checks. |
| MasterSlaveSer verGroupId | String | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |
| MaxConnection | Integer | 10 | The maximum number of connections. |
| PersistenceTim eout | Integer | 0 | The timeout period of session persistence. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43e**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerUDPListenerAttributeResponse>
    <AclStatus>off</AclStatus>
    <HealthCheck>on</HealthCheck>
    <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout>
    <PersistenceTimeout>0</PersistenceTimeout>
    <ListenerPort>80</ListenerPort>
    <Status>stopped</Status>
    <Scheduler>wrr</Scheduler>
    <HealthyThreshold>3</HealthyThreshold>
    <HealthCheckInterval>2</HealthCheckInterval>
    <RequestId>9C103591-2533-432B-9E6B-6DB098C0E65C</RequestId>
    <UnhealthyThreshold>3</UnhealthyThreshold>
    <BackendServerPort>34</BackendServerPort>
    <Bandwidth>67</Bandwidth>
</DescribeLoadBalancerUDPListenerAttributeResponse>
```

`JSON` format `{`

```json
 "AclStatus":"off",
 "HealthCheck":"on",
 "HealthCheckConnectTimeout":5,
 "PersistenceTimeout":0,
 "ListenerPort":80,
 "Status":"stopped",
 "Scheduler":"wrr",
 "HealthyThreshold":3,
 "HealthCheckInterval":2,
 "RequestId":"9C103591-2533-432B-9E6B-6DB098C0E65C",
 "UnhealthyThreshold":3,
 "BackendServerPort":34,
 "Bandwidth":67
```

`}`

#### HTTP listeners

##### CreateLoadBalancerHTTPListener

Creates an HTTP listener. Not e Newly created listeners are in the st opped state. After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerHTTPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerHT T PList ener. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: If you set the value to -1, the bandwidth of the listener is unlimited. 1 t o 5120: If you set a value from 1 to 5120, the value that you specify equals the bandwidth limit of the listener. The sum of bandwidth limit values that you specify for all listeners of the Server Load Balancer (SLB) instance cannot exceed the bandwidth limit of the SLB instance. Not e This parameter applies only to mainland China. |
| HealthCheck | String | Yes | on | Specifies whether to enable health checks. Valid values: on and of f . |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1c9vixxjh92q83 tw**** | The ID of the SLB instance. |
| StickySession | String | Yes | off | Specifies whether to enable session persistence. Valid values: on and of f . |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. Not e If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |

| X- |   |
|---|---|

|   | Forwarded-For |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will forward the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

|   | Parameter | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes |   |
|   |   |   |   |   |   |   | hyphens (-), forward slashes |
|   |   |   |   |   |   | (/), periods (.),%?number signs |   |
|   |   |   |   |   |   | (#), and ampersands (&) |   |
|   | HealthCheckURI | String | No |   | /test/index.html |   |   |
|   | HealthyThreshold | Integer | No |   | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 t o 300. Unit: seconds. Not e If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is invalid and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 80 | The backend port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Default value: ht t p 2xx. _ Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . Default value: off. |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . Default value: off. |

|   | IP |
|---|---|

|   | ID |
|---|---|

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
|   |   |   |   |   | X- |   |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Default value: on. Valid values: on and of f . Default value: off. |   |   |
| IdleTimeout | Integer | No | 3 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |   |   |
| RequestTimeout | Integer | No | 6 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
| ListenerForward | String | No | off | Specifies whether to enable HTTP-to- HTTPS redirection. Valid values: on and of f . |   |   |
| ForwardPort | Integer | No | 443 | The listening port that is used to redirect HTTP requests to HTTPS. |   |   |

|   | Forwarded-Proto |
|---|---|

|   | 504 |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | ListenerDescriptio n | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain Chinese _ characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPListener &HealthCheck=off &ListenerPort=80 &LoadBalancerId=lb-bp1c9vixxjh92q83tw***** &StickySession=off &BackendServerPort=80 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerHTTPListenerResponse>
   <RequestId>1FF504CB-BFFF-4508-A51A-58A416604FC8</RequestId>
</CreateLoadBalancerHTTPListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "1FF504CB-BFFF-4508-A51A-58A416604FC8"
```

`}`

##### SetLoadBalancerHTTPListenerAttribute

Modifies the configurations of an HTTP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer HTTPListenerAttri bute | The operation that you want to perform. Set the value to Set LoadBalancerHT T PList enerAt t ri but e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a h**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and of f . |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will forward the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 to 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and of f . |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is specified or the HealthCheckDomain parameter is not specified, the SLB instance uses the private IP address of the backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 to 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 to 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the health check fails. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 to 300. Unit: seconds. Not e If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is invalid and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the server group. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . |

|   | IP |
|---|---|

|   | ID |
|---|---|

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . |   |   |
|   |   |   |   |   | X- |   |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and of f . |   |   |
| IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |   |   |
| RequestTimeout | Integer | No | 3 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
| Description | String | No | test | The description of the listener. |   |   |

|   | Forwarded-Proto |
|---|---|

|   | 504 |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1qjwo61pqz3ah**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerHTTPListenerAttributeResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPListenerAttributeResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### DescribeLoadBalancerHTTPListenerAttribute

Queries the configurations of an HTTP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerHTTPListener Attribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHT T PList ene rAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is deployed. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1: If -1 is returned, it indicates that the bandwidth of the listener is unlimited. 1 t o 5120: the maximum bandwidth of the listener. The sum of the maximum bandwidth of all listeners added to an SLB instance cannot exceed the maximum bandwidth of the SLB instance. Not e This parameter is available only in the Chinese mainland. |
| Status | String | stopped | The status of the listener. Valid values: running st opped |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to retrieve client IP addresses. Valid values: on and of f . |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections to a backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and of f . Default value: off. |
| StickySessionTy pe | String | insert | The method that is used to handle a cookie. Valid values: insert and server. insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user- defined cookie. The next request from the client carries the user-defined cookie, and the listener will distribute this request to the recorded backend server. Not e This parameter is required if the St ickySession parameter is set to on. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. Unit: seconds. Valid values: 1 t o 86400. |
| Cookie | String | B490B5EBF6F3CD402 E515D22BCDA1598 | The cookie that is configured on the backend server. The cookie is 1 to 200 characters in length, and can contain only ASCII characters and digits. It does not contain commas (,), semicolons (;), or space characters. It does not start with a dollar sign ($). |
| HealthCheck | String | on | Indicates whether the health check feature is enabled. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckDo main | String | www.example.com | The domain name that is used for health checks. |
| HealthCheckURI | String | /test/index.html | The URL path that is used for health checks. It is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL path is not a single forward slash (/) but it starts with a forward slash (/). ) |
| HealthyThresho ld | Integer | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from f ail to success. Valid values: 2 to 10. |
| UnhealthyThres hold | Integer | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from success to f ail. Valid values: 2 to 10. |
| HealthCheckTi meout | Integer | 3 | The timeout period of a health check response. Unit: seconds. Valid values: 1 to 300. |
| HealthCheckInt erval | Integer | 5 | The interval at which health checks are performed. Unit: seconds. Valid values: 1 to 50. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckHtt pCode | String | http 2xx _ | The HTTP status code for a successful health check. Multiple HTTP status codes are separated by commas (,). Valid values: ht t p 2xx (default), ht t p 3xx, ht t p 4xx, _ _ _ and ht t p 5xx. _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only if the Healt hCheck parameter is set to on. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the forwarding rule. |
| Gzip | String | on | Indicates whether Gzip compression is enabled to compress specific types of files. Valid values: on and of f . |
| AclId | String | acl- bp1l0kk4gxce43kz** **** | The ID of the network access control list (ACL) that is associated with the listener. If AclSt at us is set to on, this parameter is required. |
| AclStatus | String | off | Indicates whether access control is enabled. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclType | String | white | The type of the network ACL. Valid values: whit e: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application. After a whitelist is configured, only IP addresses in the whitelist can access the SLB listener. Risks may arise if the whitelist is improperly set. If a whitelist is configured but no IP address is added to the whitelist, the listener forwards all requests. black: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are blocked. Blacklists apply to scenarios in which you want to deny access from specific IP addresses to an application. If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests. Not e This parameter takes effect if AclSt at us is set to on. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. |
| Description | String | test | The description of the HTTP listener. The description is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| ForwardPort | Integer | 80 | The listening port that is used to redirect HTTP requests to HTTPS. Not e If the List enerForward parameter is set to of f , this parameter is not returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IdleTimeout | Integer | 2 | The timeout period of an idle connection. Unit: seconds. Valid values: 1~60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| ListenerForwar d | String | on | Indicates whether HTTP-to-HTTPS redirection is enabled. Valid values: on: enabled of f : disabled |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeou t | Integer | 34 | The request timeout period. Unit: seconds. Valid values: 1 t o 180. Unit: seconds. Default value: 60. If no response is received from a backend server within the specified timeout period, SLB returns the HTTP 504 error code to the client. |
| Rules | Array of Rule |   | The list of forwarding rules. |
| Rule |   |   |   |
| Domain | String | www.example.com | The domain name. |
| RuleId | String | rule-xjsq****** | The ID of the forwarding rule. |
| RuleName | String | example | The name of the forwarding rule. |
| Url | String | /example | The request path. |
| VServerGroupId | String | rsp-bp****** | The ID of the vServer group that is associated with the forwarding rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SecurityStatus | String | on | Indicates whether the listener is in the Secure state. Valid values: on and of f . |
| XForwardedFor SLBID _ | String | on | Indicates whether the SLB-ID header is used to retrieve the ID of the SLB instance. |
| XForwardedFor SLBIP _ | String | on | Indicates whether the SLB-IP header is used to retrieve the IP address of the SLB instance. |
| XForwardedFor proto _ | String | on | Indicates whether the X-Forwarded- Proto header is used to retrieve the listening protocol. |

|   | Proto |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5********* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerHTTPListenerAttributeResponse>
    <ForwardPort>443</ForwardPort>
    <ListenerPort>80</ListenerPort>
    <Status>stopped</Status>
    <RequestId>99439CEF-192C-4B01-A45A-2D5BD5BCDA62</RequestId>
    <ListenerForward>on</ListenerForward>
</DescribeLoadBalancerHTTPListenerAttributeResponse>
```

`JSON` format

```json
{"CookieTimeout":"500","VServerGroupId":"rsp-cige6j****","Description":"test","UnhealthyThr eshold":"4","HealthCheckURI":"/test/index.html","Scheduler":"wrr","HealthCheck":"on","IdleT imeout":"2","BackendServerPort":"80","XForwardedFor_SLBID":"on","HealthCheckConnectPort":"8 080","SecurityStatus":"on","Bandwidth":"-1","Gzip":"on","StickySessionType":"insert ","XFor wardedFor_SLBIP":"on","HealthCheckHttpCode":"http_2xx","Cookie":"B490B5EBF6F3CD402E515D22BC DA1598","Status":"stopped","RequestTimeout":"34","ListenerPort":"80","HealthCheckInterval": "5","RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","AclId":"acl-bp1l0kk4gxce43kz******" ,"HealthCheckTimeout":"3","Rules":[{"VServerGroupId":"rsp-bp******","RuleId":"rule-xjsq****
**","Domain":"www.example.com","Url":"/example","RuleName":"example"}],"ListenerForward":"o
n","StickySession":"on","ForwardPort":"80","AclStatus":"off","HealthyThreshold":"4","XForwa rdedFor":"on","HealthCheckDomain":"www.example.com","AclType":"white","XForwardedFor_proto" :"on"}
```

#### HTTPS listeners

##### CreateLoadBalancerHTTPSListener

Creates an HTTPS listener. Not e Newly created listeners are in the stopped state. After a listener is created, call the `StartLoadBalancerListener` operation to enable the listener to forward network traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerHTTPSListener | The operation that you want to perform. Set the value to Creat eLoadBalancerHT T PSList ener. |
| Bandwidth | Integer | Yes | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set this parameter to -1. This way, the bandwidth of the listener is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the maximum bandwidth of each listener. The sum of the maximum bandwidth of all listeners cannot exceed the maximum bandwidth of the SLB instance. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheck | String | Yes | on | Specifies whether to enable the health check feature. Valid values: on and of f . |   |   |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |   |   |
| LoadBalancerId | String | Yes | lb- bp1o94dp5i6earr **** | The ID of the SLB instance. |   |   |
| StickySession | String | Yes | on | Specifies whether to enable session persistence. Valid values: on and of f . |   |   |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |   |   |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to retrieve client IP addresses. Set the value to on. |   |   |
|   |   |   |   |   | X- |   |
| Scheduler | String | No | wrr | The routing algorithm. Valid values: wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections to a backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |   |   |

|   | Forwarded-For |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Default value: Insert. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will distribute the request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, SLB rewrites the original cookie with the user-defined cookie. The next request from the client carries the user-defined cookie, and the listener distributes the request to the recorded backend server. Not e This parameter is required when the StickySession parameter is set to on. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Unit: seconds. Valid values: 1 t o 86400. Not e If St ickySession is set to on and St ickySessionT ype is set to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie that is configured on the backend server. It must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Not e This parameter is required if the St ickySession parameter is set to on and the St ickySessionT ype parameter is set to server. |
| HealthCheckMeth od | String | No | get | The health check method used in HTTP health checks. Valid values: head and get . Not e This parameter takes effect only if the HealthCheck parameter is set to on. |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: the private IP addresses of the _ backend servers. If you do not set this parameter or set the parameter to $ ip, SLB uses the private IP _ address of each backend server for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.), and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URI that is used for health checks. It must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & . The URL path is not a single forward slash (/) but it starts with a forward slash (/). Not e This parameter takes effect when the Healt hCheck parameter is set to on. |   |   |
|   |   |   |   |   | - / |   |
| HealthyThreshold | Integer | No | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from f ail to success. Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| UnhealthyThresh old | Integer | No | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from success to f ail. Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |

|   | . % ? # & |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check. If a backend server, such as an Elastic Compute Service (ECS) instance, does not return a health check response within the specified timeout period, the server fails the health check. Unit: seconds. Valid values: 1 t o 300. If the value of the Healt hCheckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the timeout period specified by the Healt hCheckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is used as the timeout period. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only if the Healt hCheck parameter is set to on. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Unit: seconds. Valid values: 1 t o 50. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that is returned when a health check is successful. Separate multiple HTTP status codes with commas (,). Default value: ht t p 2xx. _ Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificateI d | String | No | idkp-123-cn-test- **** | The ID of the server certificate. |
| VServerGroupId | String | No | rsp- cige6j5e7p**** | The ID of the server group. |
| CACertificateId | String | No | 139a00604ad-cn- east-hangzh**** | The ID of the certification authority (CA) certificate. To enable mutual authentication, upload a CA certificate and a server certificate. To enable one-way authentication, upload only a server certificate. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to retrieve client IP addresses. Valid values: on and of f . Default value: off. |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to retrieve the ID of the SLB instance. Valid values: on and of f . Default value: off. |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to retrieve the listener protocol. Valid values: on and of f . Default value: off. |   |   |
|   |   |   |   |   |   | X- |   |
|   | Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and of f . Default value: off. |   |   |
|   | IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 t o 60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When a request is received, SLB establishes a new connection. |   |   |
|   | RequestTimeout | Integer | No | 23 | The timeout period of a request. Unit: seconds. Valid values: 1 t o 180. Default value: 60. If no response is received from the backend server within the request timeout period, SLB returns the HTTP 504 error code to the client. |   |   |
|   |   |   |   |   | You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes TLS protocol versions and cipher suites that are available for HTTPS. The following security policies are supported. For more information about the differences, see Differences in TLS security policies. t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLS 1.0, TLS 1.1, and TLS 1.2 |   |   |

|   | Forwarded-Proto |
|---|---|

| Parameter | Type | Required | Example | Supported cipher suites: ECDHE- Description RSA-AES128-GCM-SHA256, ECDHE- |
|---|---|---|---|---|
|   |   |   |   | RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, |
| TLSCipherPolicy | String | No | tls cipher policy _ _ _ 1 1 _ | AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLS 1.1 and TLS 1.2 Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLS 1.2 Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLS 1.2 Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA- AES256-SHA |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | CreateListeners | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores ( ). _ |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where the SLB instance is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| AclId | String | No | acl- bp1l0kk4gxce43k z****** | The ID of the network ACL that is associated with the listener. If AclSt at us is set to on, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AclType | String | No | white | The type of the ACL. Valid values: whit e: an allowlist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Allowlists apply to scenarios in which you want to allow only specified IP addresses to access an application. After an allowlist is configured, only IP addresses in the allowlist can access the SLB listener. Risks may arise if the allowlist is improperly set. If an allowlist is configured but no IP address is added to the allowlist, the listener forwards all requests. black: a denylist. All requests from the IP addresses or CIDR blocks in the network ACL are blocked. Denylists apply to scenarios in which you want to deny access from specific IP addresses or CIDR blocks to an application. If a denylist is configured for a listener but no IP address is added to the denylist, the listener forwards all requests. Not e If AclSt at us is set to on, this parameter is required. |
| AclStatus | String | No | off | Specifies whether to enable access control. Valid values: Valid values: on and of f . Default value: off. |
| EnableHttp2 | String | No | off | Specifies whether to enable HTTP/2. Valid values: on and of f . Default value: off. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPSListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5i6earr***** &StickySession=on &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateLoadBalancerHTTPSListenerResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</CreateLoadBalancerHTTPSListenerResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ParamDuplicateError | The specified parameter value of XForwardedFor ClientCertSubjec _ tDNAlias is duplicate. Please change to a different one. | The error message returned because the value of XForwardedFor ClientCertSubjec _ tDNAlias is duplicate. |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedFor ClientCertIssuer _ DNAlias is duplicate. Please change to a different one. | The error message returned because the value of XForwardedFor ClientCertIssuer _ DNAlias is duplicate. |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedFor ClientCertFinger _ printAlias is duplicate. Please change to a different one. | The error message returned because the value of XForwardedFor ClientCertFinger _ printAlias is duplicate. |

| erver Load Ba | lancer |   | Developer Guide·API Referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ParamDuplicateError | The specified parameter value of XForwardedFor ClientCertClientV _ erifyAlias is duplicate. Please change to a different one. | The error message returned because the value of XForwardedFor ClientCertClientV _ erifyAlias is duplicate. |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | The error message returned because the specified IP version is not supported by the network ACL. |
| 400 | InvalidParameter.Idl eTimeout | The specified IdleTimeout exceeds the limit. | The error message returned because the specified timeout period of idle connections is invalid. Specify a valid value and try again. |
| 400 | InvalidParameter.Re questTimeout | The specified RequestTimeout exceeds the limit. | The error message returned because the specified timeout period of requests is invalid. Specify a valid value and try again. |
| 400 | ListenerForwardNot Support | X-Forward-For is not supported to a ipv6 instance. | The error message returned because SLB instances that have IPv6 enabled do not support the X-Forward-For header. |
| 400 | InvalidParameter.Re gionNotSupport | The region does not support the parameter: %s. | The error message returned because the parameter is not supported in the region. |
| 400 | InvalidParameter.Sp ecNotSupport | The loadBalancer of shared spec does not support the parameter: %s. | The error message returned because the parameter is not supported by shared-resource SLB instances. |
| 400 | ListenerProcessing | A previous configuration of the listener is pending,please try again later. | The error message returned because the specified listener is being configured. Try again later. |
| 400 | Certkey.Forbidden | The specified certkey is not owned by the current user. | The error message returned because the specified certificate key does not belong to the current account. |
| 400 | InvalidParameter.List enerPortConflict | There is conflict listener port exists. | The error message returned because the specified listening port already exists. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ResourceNotAvailibl e.HttpsListener | The specified Zone did not have enough resource. | The error message returned because resources are insufficient in the specified zone. |
| 400 | OperationUnsupport ed.CreateLoadBalan cerLayer7Listener | The slb instance does not support create HTTP or HTTPS listener. | The error message returned because the specified SLB instance does not support HTTP or HTTPS listeners. |
| 400 | InvalidParameter.VS erverGroupId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. | The error message returned because HTTP and HTTPS listeners do not support primary/secondary server groups. |
| 400 | MissingParam.Health CheckDomain | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. | The error message returned because the HealthCheckDomain parameter is not set. |
| 400 | InvalidParameter.He althCheckHttpVersio n | The param HealthCheckHttpVersion is invalid. | The error message returned because the specified HTTP version for health checks is invalid. Specify a valid value and try again. |
| 400 | QuotaLimitExceeds. AclAttachedToListen er | %s. | The error message returned because the number of listeners associated with the network ACL has reached the upper limit. |
| 400 | QuotaLimitExceeds. TotalAclEntry | %s. | The error message returned because the number of network ACL rules has reached the upper limit. |
| 400 | Duplicated.AclEntry | %s. | The error message returned because the specified ACL rule already exists. |
| 400 | CertificateNotExist | The specified CertificateId does not exist. | The error message returned because the specified certificate does not exist. |
| 400 | OperationFailed.Insu fficientResources | The loadbalancer does not support this operation because of insufficient resources. | The error message returned because the operation failed due to insufficient resources. |
| 400 | InvalidTLSPolicyId.N otExist | The specified TLS cipher policy does not exist. | The error message returned because the specified TLS policy does not exist. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | TLSPolicyConfiguring | The specified TLS cipher policy is configuring. | The error message returned because the specified TLS policy is being modified. |
| 400 | TLSCipherPolicyVipR elationOverLimit | The number of listeners associated with a policy has exceeded. | The error message returned because the number of TLS policies has reached the upper limit. |
| 400 | CertificateTypeMism atched | The certificate type does not match. | The error message returned because the specified certificate type is invalid. |
| 400 | MissingParam.Server Certificates | Server certificates are required. | The error message returned because the ServerCertificates parameter is not set. |
| 400 | TooManyCertificates | The number of certificates must not be greater than one. | The error message returned because the number of certificates cannot exceed 1. |
| 400 | CnCertificateNotSup port | The cn certificate is not support. | The error message returned because ShangMi (SM) cipher suites are not supported. |
| 400 | InvalidParam.Certific ateBindingType | The param CertificateBindingType is invalid. | The error message returned because the CertificateBindingType parameter is set to an invalid value. Specify a valid value and try again. |
| 400 | InvalidParamSize.Ser verCertificates | The size of param ServerCertificates is invalid. | The error message returned because the value of the ServerCertificates parameter is in an invalid length. Specify a valid value and try again. |
| 400 | TooManyCertificates .ServerCertificates | The number of certificates must not be greater than one. | The error message returned because the number of certificates cannot exceed 1. |
| 400 | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. | The error message returned because the specified instance does not allow you to create TCP SSL listeners. |
| 400 | LbSupportTcpsslOnl y | The specified load balancer supports TCP SSL type listener only. | The error message returned because the specified instance allows you to create only TCP SSL listeners. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ListenerNotSupport Rule | You cannot create a rule for the specified listener. | The error message returned because the specified listener does not allow you to create forwarding rules. |
| 400 | Mismatch.SlbSpecTy peAndListenerProto col | The SlbSpecType and ListenerProtocol are mismatched. | The error message returned because the specified instance type and listener type do not match. |

##### SetLoadBalancerHTTPSListenerAttribute

Modifies the configurations of an HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer HTTPSListenerAtt ribute | The operation that you want to perform. Set the value to Set LoadBalancerHT T PSList enerAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb-sjhfdji**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | Specify the bandwidth limit of the listener. Valid values: 1 t o 5120 and -1. -1: If you set the value to -1, the bandwidth is unlimited. 1 t o 5120: If you set a value from 1 to 5120, the value that you specify equals the bandwidth limit of the listener. The sum of bandwidth limit values that you specify for all listeners of the SLB instance cannot exceed the bandwidth limit of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Valid values: on and of f . |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and of f . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie that is configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and of f . |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 t o 300. Unit: seconds. Not e If the value of the Healt hCheckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCheckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is used as the timeout period. This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificateI d | String | No | idkp-123-cn- te**** | The ID of the server certificate. |
| CACertificateId | String | No | 139a00604ad-cn- east-**** | The ID of the CA certificate. If both the CA certificate and the server certificate are uploaded, two- factor authentication is used. If you upload only the server certificate, single-factor authentication is used. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| Tags | String | No | loadbalancerhttp s**** | The tags. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . |   |   |
|   |   |   |   |   |   | X- |   |
|   | Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and of f . |   |   |
|   | IdleTimeout | Integer | No | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 t o 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |   |   |
|   | RequestTimeout | Integer | No | 223 | The timeout period of a request. Unit: seconds. Valid values: 1 t o 180. Default value: 60. If no response is received from the backend server during the specified timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
|   |   |   |   |   | You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes TLS protocol versions and cipher suites that are available for HTTPS. You can select a security policy based on your requirements. The following security policies are supported: t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. |   |   |

|   | Forwarded-Proto |
|---|---|

|   | Parameter | Type | Required |   | Example | Supported cipher suites: ECDHE- Description RSA-AES128-GCM-SHA256, ECDHE- |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- |   |   |
|   | TLSCipherPolicy | String | No |   | tls cipher policy _ _ _ 1 2 _ | SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA- AES256-SHA. |   |   |
|   | Description | String | No |   | ListenerDescriptio n | The description of the listener. The description must be 2 to 256 characters in length. It can contain only characters in the following string: ^([^\x00-\xff]\|[\w.,;/@-]) {2,256}$ . |   |   |
|   |   |   |   |   |   |   | ^([^\x00-\xff]\|[\w.,;/@-]) |   |
|   |   |   |   |   |   | {2,256}$ |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-sjhfdji**************** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerHTTPSListenerAttributeResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPSListenerAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### DescribeLoadBalancerHTTPSListenerAttribute

Queries the configurations of an HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerHTTPSListene rAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHT T PSList en erAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| eveloper Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| LoadBalancerId | String | Yes | lb- bp1mxu5r8lau*** * | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to obtain the real IP address of the client. Valid values: on and of f . |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StickySessionTy pe | String | insert | The method that is used to handle a cookie. If you set the StickySession parameter to on, this parameter is required. Valid values: insert and server. insert : inserts a cookie into the response. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user- defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. |
| Cookie | String | B490B5EBF6F3CD402 E515D22BCDA1598 | The cookie configured on the backend server. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthCheckDo main | String | www.test.com | The domain name that is used for health checks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckURI | String | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must start with a forward slash (/) but cannot contain only a forward slash (/). |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckTi meout | Integer | 3 | The timeout period of a health check response. Unit: seconds. |
| HealthCheckInt erval | Integer | 5 | The time interval between two consecutive health checks. Unit: seconds. Valid values: 1 t o 50. |
| HealthCheckHtt pCode | String | http 2xx _ | The HTTP status code that indicates a successful health check. Multiple status codes are separated with commas (,). Valid values: ht t p 2xx (default), ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificat eId | String | idkp-123-cn-test- **** | The ID of the server certificate. |
| CACertificateId | String | idkp-234-cn-test- **** | The ID of the CA certificate. |
| VServerGroupId | String | rsp-cige6j5e**** | The ID of the associated vServer group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Gzip | String | on | Indicates whether gzip compression is enabled. Valid values: on and of f . |
| Description | String | ListenerDescription | The description of the listener. The description must be 2 to 256 characters in length. It can contain only Chinese characters and characters in the following string: /^([^\x00-\xff]\|[\w.,;/@-]){2,256}$/. |
| IdleTimeout | Integer | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| MaxConnection | Integer | 10 |   |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeou t | Integer | 43 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If the backend server does not respond within the specified timeout period, SLB returns the HTTP 504 error code to the client. |
| SecurityStatus | String | on | The security status. Valid values: on and of f . |
|   |   |   | The security policy. You can specify the TLSCipherPolicy parameter only for a high- performance SLB instance. Each security policy includes different TLS protocol versions and cipher suites for HTTPS. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | The following security policies are Description supported. For more information about the |
| TLSCipherPolicy | String | tls cipher policy 1 _ _ _ _ 0 | differences, see Differences in TLS security policies. You can specify a security policy based on your requirements. Valid values: t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA-AES256-SHA. |

| Parameter | Type | Example | Description Indicates whether the SLB-ID header is |
|---|---|---|---|
| XForwardedFor SLBID _ | String | on | used to obtain the ID of the SLB instance. Valid values: on and of f . |
| XForwardedFor SLBIP _ | String | on | Indicates whether the SLB-IP header is used to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor proto _ | String | on | Indicates whether the X-Forwarded- Proto header is used to obtain the listener protocol of the SLB instance. Valid values: on and of f . |

|   | Proto |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1mxu5r8lau******* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerHTTPSListenerAttributeResponse>
   <RequestId>11F52428-64ED-40F7-98C2-DBB6D0BB0AD7</RequestId>
      <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
      <HealthCheckTimeout>5</HealthCheckTimeout>
      <ServerCertificateId>1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746</ServerCertifi
cateId>
      <XForwardedFor_SLBID>off</XForwardedFor_SLBID>
      <Gzip>on</Gzip>
      <HealthyThreshold>3</HealthyThreshold>
      <Scheduler>wrr</Scheduler>
      <StickySession>off</StickySession>
      <UnhealthyThreshold>3</UnhealthyThreshold>
      <XForwardedFor_SLBIP>off</XForwardedFor_SLBIP>
      <XForwardedFor_proto>off</XForwardedFor_proto>
      <Bandwidth>-1</Bandwidth>
      <HealthCheckURI>/</HealthCheckURI>
      <VServerGroupId>rsp-0xiju72x******</VServerGroupId>
      <HealthCheck>on</HealthCheck>
      <ListenerPort>443</ListenerPort>
      <Status>running</Status>
      <XForwardedFor>on</XForwardedFor>
      <HealthCheckDomain></HealthCheckDomain>
      <HealthCheckInterval>2</HealthCheckInterval>
      <BackendServerPort>443</BackendServerPort>
</DescribeLoadBalancerHTTPSListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "11F52428-64ED-40F7-98C2-DBB6D0BB0AD7",
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "HealthCheckTimeout": 5,
    "ServerCertificateId": "1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746",
    "XForwardedFor_SLBID": "off",
    "Gzip": "on",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "StickySession": "off",
    "UnhealthyThreshold": 3,
    "XForwardedFor_SLBIP": "off",
    "XForwardedFor_proto": "off",
    "Bandwidth": -1,
    "HealthCheckURI": "/",
    "VServerGroupId": "rsp-0xiju72x******",
    "HealthCheck": "on",
    "ListenerPort": 443,
    "Status": "running",
    "XForwardedFor": "on",
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "BackendServerPort": 443
```

`}`

##### DescribeHealthStatus

Queries the health status of backend servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHealthSt atus | The operation that you want to perform. Set the value to DescribeHealt hSt at us. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a h**** | The ID of the Server Load Balancer (SLB) instance. |
| ListenerPort | Integer | No | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. Not e If you do not specify this parameter, the health status of all ports is returned. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i- bp1h5u3fv54ytf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerHealthSt atus | String | abnormal | The health status of the backend server: normal: The backend server is healthy. abnormal: The backend server is unhealthy. unavailable: The health check is not completed. |
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| port | Integer | 80 |   |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHealthStatus &LoadBalancerId=lb-bp1qjwo61pqz3ah**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHealthStatusResponse>
  <RequestId>E69BA4CE-2B55-45EC-94CA-E47B16759459</RequestId>
  <BackendServers>
        <BackendServer>
              <ListenerPort>80</ListenerPort>
              <ServerId>i-bp1h5u3fv54ytf0******</ServerId>
              <Port>80</Port>
              <ServerIp>192.168.0.**</ServerIp>
              <ServerHealthStatus>abnormal</ServerHealthStatus>
              <Protocol>http</Protocol>
        </BackendServer>
        <BackendServer>
              <ListenerPort>8080</ListenerPort>
              <ServerId>i-bp1h5u3fv54ytf0******</ServerId>
              <Port>80</Port>
              <ServerIp>192.168.0.**</ServerIp>
              <ServerHealthStatus>abnormal</ServerHealthStatus>
              <Protocol>tcp</Protocol>
        </BackendServer>
  </BackendServers>
</DescribeHealthStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "E69BA4CE-2B55-45EC-94CA-E47B16759459",
    "BackendServers": {
        "BackendServer": [
```

`{`

```json
                "ListenerPort": 80,
                "ServerId": "i-bp1h5u3fv54ytf*****",
                "Port": 80,
                "ServerIp": "192.168.**.**",
                "ServerHealthStatus": "abnormal",
                "Protocol": "http"
```

`},` `{`

```json
                "ListenerPort": 8080,
                "ServerId": "i-bp1h5u3fv54ytf0******",
                "Port": 80,
                "ServerIp": "192.168.**.**",
                "ServerHealthStatus": "abnormal",
                "Protocol": "tcp"
```

`}` `]` `}` `}`

#### Access control

##### SetListenerAccessControlStatus

Enables or disables the whitelist of a specified listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetListenerAcces sControlStatus | The operation that you want to perform. Set the value to Set List enerAccessCont rolSt at us. |
| AccessControlSta tus | String | Yes | open white list _ _ | Specifies whether to enable the whitelist. Valid values: open whit e list : enables the _ _ whitelist. close: disables the whitelist. Not e After the whitelist is enabled, if no IP address is added to the whitelist, the Server Load Balancer (SLB) instance does not distribute network traffic. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetListenerAccessControlStatus &AccessControlStatus=open_white_list &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetListenerAccessControlStatusResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetListenerAccessControlStatusResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

##### DescribeListenerAccessControlAttribute

Queries the whitelist configurations of a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeListenerA ccessControlAttri bute | The operation that you want to perform. Set the value to DescribeList enerAccessCont rolAt t r ibut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerId | String | Yes | lb- 8vb86hxixo8****** *6jaz | The ID of the SLB instance. |
| Tags | String | No | listeneraccesscon trolslb**** | The tags. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessControlS tatus | String | open white list _ _ | Indicates whether the whitelist is enabled. Valid values: open whit e list : the whitelist is _ _ enabled. close: the whitelist is disabled. |
| SourceItems | String | 192.168.0.1 | The IP addresses or CIDR blocks that are added to the whitelist. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeListenerAccessControlAttribute &ListenerPort=80 &LoadBalancerId=lb-8vb86hxixo8*******6jaz &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeListenerAccessControlAttributeResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
   <AccessControlStatus>open_white_list</AccessControlStatus>
   <SourceItems>192.168.0.1</SourceItems>
</DescribeListenerAccessControlAttributeResponse>
```

`JSON` format

```json
{"AccessControlStatus":"open_white_list", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "SourceItems":"192.168.0.1"}
```

##### AddListenerWhiteListItem

Adds IP addresses to the whitelist of a listener. Request parameters

| Parameter | Type |   | Required | Example | Description |   |
|---|---|---|---|---|---|---|
| Action | String |   | Yes | AddListenerWhite ListItem | The operation that you want to perform. Set the value to AddList enerWhit eList It em. |   |
| ListenerPort | Integer |   | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |   |
| LoadBalancerId | String |   | Yes | 139a00604ad-cn- east-hangzhou- 01 | The ID of the SLB instance. |   |
| SourceItems | String |   | Yes | 1.XX.XX.1,1.XX.X X.0/21 | The IP addresses or CIDR blocks that you want to add to the whitelist. This parameter takes effect only when AccessCont rolSt at us of the listener is set to open whit e list . _ _ Separate multiple IP addresses or CIDR blocks with commas (,). You cannot enter 0.0.0.0 or 0.0.0.0/0. You can call the SetListenerAccessControlStatus operation to set the value of the AccessCont rolSt at us parameter to close. This indicates that access control is disabled. |   |
|   |   |   |   |   |   | SetListenerAccessControlStatus |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=139a00604ad-cn-east-hangzhou-01 &SourceItems=1.XX.XX.1,XX.XX.1.0/21 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddListenerWhiteListItemResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</AddListenerWhiteListItemResponse>
```

`JSON` format `{`

```json
    "AddListenerWhiteListItemResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` `}`

##### RemoveListenerWhiteListItem

Removes IP addresses from the whitelist of a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveListenerW hiteListItem | The operation that you want to perform. Set the value to RemoveList enerWhit eList It em. |
| ListenerPort | Integer | Yes | 80 | The listener port. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the Server Load Balancer (SLB) instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceItems | String | Yes | 192.168.0.1/24 | The IP addresses or CIDR blocks to be removed. Separate multiple IP addresses or CIDR blocks with commas (,). Not e If all IP addresses are removed from the whitelist, the listener does not forward requests. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex**** &SourceItems=192.168.0.1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveListenerWhiteListItemResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</RemoveListenerWhiteListItemResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

##### CreateAccessControlList

Creates an access control list (ACL). You can create multiple ACLs. Each ACL can contain one or more IP addresses or CIDR blocks. Before you create an ACL, take note of the following limits: Each Apsara Stack tenant account can create at most 50 ACLs in a region. The maximum number of IP addresses that an Apsara Stack tenant account can add to an ACL is 50. The maximum number of IP addresses or CIDR blocks that can be added to an ACL is 300. The maximum number of ACLs that can be associated with a listener is 50. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccessCon trolList | The operation that you want to perform. Set the value to Creat eAccessCont rolList . |
| AclName | String | Yes | rule1 | The name of the ACL. ACL names must be unique within the region. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where you want to create the ACL. |
| AddressIPVersion | String | No | ipv4 | The IP version. Valid values: ipv4 and ipv6. Not e You can create high- performance IPv6 Server Load Balancer (SLB) instances only in the following zones: Hangzhou Zone E and Hangzhou Zone F, Beijing Zone F and Beijing Zone G, Shenzhen Zone D and Shenzhen Zone E, and all zones in the China (Shanghai) region. |
| ResourceGroupId | String | No | rg-atstuj3rt**** | The ID of the resource group to which the ACL belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclId | String | acl- rj9xpxzcwxrukois**** | The ID of the ACL. |
| RequestId | String | 988CB45E-1643- 48C0-87B4- 928DDF77EA49 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateAccessControlList &AclName=rule1 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateAccessControlListResponse>
    <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId>
    <AclId>acl-rj9xpxzcwxrukois******</AclId>
</CreateAccessControlListResponse>
```

`JSON` format

```json
{"RequestId":"988CB45E-1643-48C0-87B4-928DDF77EA49","AclId":"acl-rj9xpxzcwxrukois****"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAction.Region NotSupport | The region does not support this action. | The error message returned because the parameter is not supported in the current region. |
| 400 | AclNumberOverLimit | The Acl number has reached to the max quota limit. | The error message returned because the number of ACLs has reached the upper limit. |
| 400 | InvalidResourceGrou pId.NotFound | The specified ResourceGroupId is not found. | The error message returned because the specified resource group does not exist. |
| 400 | ResourceInConfigurin g.Acl | The specified resource is configuring, please try again later. | The error message returned because the specified ACL is being configured. Try again later. |

##### DeleteAccessControlList

Deletes an access control list (ACL). You can delete an ACL only if it is not associated with a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccessCon trolList | The operation that you want to perform. Set the value to Delet eAccessCont rolList . |
| AclId | String | Yes | acl- bp1l0kk4gxce43k z**** | The ID of the ACL. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the ACL is created. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 988CB45E-1643- 48C0-87B4- 928DDF77EA49 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteAccessControlList &AclId=acl-bp1l0kk4gxce43kz****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteAccessControlListResponse>
    <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId>
</DeleteAccessControlListResponse>
```

`JSON` format `{`

```json
    "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationFailed.AclB indedWithVip | The ACL has binded with vip. | The error message returned because the ACL is associated with a listener and the operation failed. |

##### DescribeAccessControlLists

Queries network access control lists (ACLs). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessCo ntrolLists | The operation that you want to perform. Set the value to DescribeAccessCont rolList s. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the network ACL is created. You can call the DescribeRegions operation to query the most recent region list. |
| AclName | String | No | acl | The name of the network ACL. The name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), hyphens (-), forward slashes (/), and underscores ( ). The _ name of the network ACL must be unique within the region. |
| AddressIPVersion | String | No | ipv4 | The IP version of the Server Load Balancer (SLB) instance with which the network ACL is associated. Valid values: ipv4: IPv4 ipv6: IPv6 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| eveloper Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ResourceGroupId | String | No | rg- atstuj3rtop**** | The ID of the resource group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Acls | Array of Acl |   | A list of network ACLs. |
| Acl |   |   |   |
| AclId | String | acl- bp1l0kk4gxce43k*** ** | The ID of the network ACL. |
| AclName | String | rule1 | The name of the network ACL. |
| AddressIPVersi on | String | ipv4 | The IP version that is used by the associated SLB instance. |
| ResourceGroupI d | String | rg-jfenf*********** | The ID of the resource group. |
| Count | Integer | 5 | The number of network ACLs on the current page. |
| PageNumber | Integer | 2 | The number of the returned page. Minimum value: 1. Default value: 1. |
| PageSize | Integer | 3 | The number of entries returned per page. Default value: 10. |
| RequestId | String | 3CB646EF-6147- 4566-A9D9- CE8FBE86F971 | The ID of the request. |
| TotalCount | Integer | 3 | The number of network ACLs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAccessControlLists &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeAccessControlListsResponse>
   <RequestId>3CB646EF-6147-4566-A9D9-CE8FBE86F971</RequestId>
   <Acls>
      <Acl>
         <AclId>acl-bp1j9vn2g7wm9wn0*****</AclId>
         <AclName>test</AclName>
         <AddressIPVersion>ipv4</AddressIPVersion>
      </Acl>
      <Acl>
         <AclId>acl-bp1l0kk4gxce43*****</AclId>
         <AclName>doctest</AclName>
         <AddressIPVersion>ipv4</AddressIPVersion>
      </Acl>
   </Acls>
</DescribeAccessControlListsResponse>
```

`JSON` format `{`

```json
    "RequestId": "3CB646EF-6147-4566-A9D9-CE8FBE86F971",
    "Acls": {
        "Acl": [
```

`{`

```json
                "AclId": "acl-bp1j9vn2g7wm9wn0****",
                "AclName": "test",
                "AddressIPVersion": "ipv4"
```

`},` `{`

```json
                "AclId": "acl-bp1l0kk4gxce43*****",
                "AclName": "doctest",
                "AddressIPVersion": "ipv4"
```

`}` `]` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidResourceGrou pId.NotFound | The specified ResourceGroupId is not found. | The error message returned because the specified resource group does not exist. |

##### DescribeAccessControlListAttribute

Queries the configurations of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessCo ntrolListAttribute | The operation that you want to perform. Set the value to DescribeAccessCont rolList At t ribut e. |
| AclId | String | Yes | acl- bp1l0kk4gxce43k zet04s | The ID of the network ACL that you want to query. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the network ACL is created. You can call the DescribeRegions operation to query the most recent region list. |
| AclEntryComment | String | No | test | The description of the network ACL entry. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclEntrys | Array of AclEntry |   | A list of ACL entries. |
| AclEntry |   |   |   |
| AclEntryComme nt | String | The network ACL entry. | The description of the ACL entry. |
| AclEntryIP | String | 192.168.0.1 | The IP address specified in the network ACL entry. |
| AclId | String | acl- bp1l0kk4gxce43kzet 04s | The ID of the network ACL. |
| AclName | String | doctest | The name of the network ACL. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AddressIPVersi on | String | ipv4 | The IP version of the instance with which the network ACL is associated. |
| RelatedListener s | Array of RelatedListener |   | A list of listeners with which the network ACL is associated. |
| RelatedListener |   |   |   |
| AclType | String | white | The type of the network ACL. Valid values: black: a denylist. whit e: an allowlist. |
| ListenerPort | Integer | 443 | The frontend port of the listener with which the network ACL is associated. |
| LoadBalancerId | String | lb- bp13jaf5qli5xmgl1m iup | The ID of the SLB instance. |
| Protocol | String | https | The type of protocol that the associated listener uses. Valid values: t cp udp ht t p ht t ps |
| RequestId | String | C9906A1D-86F7- 4C9C-A369- 54DA42EF206A | The ID of the request. |
| ResourceGroupI d | String | rg-atstuj3rtop**** | The ID of the resource group. |

Examples Sample requests

```
/?Action=DescribeAccessControlListAttribute &AclId=acl-bp1l0kk4gxce43kzet04s &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeAccessControlListAttributeResponse>
   <AclId>acl-bp1l0kk4gxce43kzet04s</AclId>
   <RelatedListeners>
      <RelatedListener>
         <AclType>white</AclType>
         <LoadBalancerId>lb-bp13jaf5qli5xmgl1miup</LoadBalancerId>
         <Protocol>https</Protocol>
         <ListenerPort>443</ListenerPort>
      </RelatedListener>
   </RelatedListeners>
   <AclName>doctest</AclName>
   <RequestId>C9906A1D-86F7-4C9C-A369-54DA42EF206A</RequestId>
   <AddressIPVersion>ipv4</AddressIPVersion>
</DescribeAccessControlListAttributeResponse>
```

`JSON` format

```
clEntrys":{"AclEntry":[{"AclEntryComment":"Network ACL entry","AclEntryIP":"192.168.0.1"}]} ,"ResourceGroupId":"rg-******************","RequestId":"C9906A1D-86F7-4C9C-A369-54DA42EF206 A","AddressIPVersion":"ipv4","AclId":"acl-bp1l0kk4gxce43kzet04s","RelatedListeners":{"Relat edListener":[{"ListenerPort":"443","AclType":"white","LoadBalancerId":"lb-bp13jaf5qli5xmgl1 miup","Protocol":"https"}]},"AclName":"doctest"}{"A
```

##### SetAccessControlListAttribute

Changes the name of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetAccessControl ListAttribute | The operation that you want to perform. Set the value to Set AccessCont rolList At t ribut e. |
| AclId | String | Yes | acl- bp1l0kk4gxce43k zet04s | The ID of the network ACL. |
| AclName | String | Yes | test1 | The name of the network ACL. The name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), hyphens (-), forward slashes (/), and underscores ( ). The _ name of the network ACL must be unique within the region. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the network ACL is created. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclId | String | acl- bp1l0kk4gxce43kzet 04s | The ID of the network ACL. |
| RequestId | String | 988CB45E-1643- 48C0-87B4- 928DDF77EA49 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetAccessControlListAttribute &AclId=acl-bp1l0kk4gxce43kzet04s &AclName=test1 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<SetAccessControlListAttributeResponse>
    <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId>
</SetAccessControlListAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49"
```

`}`

##### AddAccessControlListEntry

Adds IP addresses to an access control list (ACL). Each ACL can contain one or more IP addresses or CIDR blocks. The limits on ACLs are: The maximum number of IP addresses that an Apsara Stack tenant account can add to an ACL in each call is 50. The maximum number of IP addresses or CIDR blocks that can be added to an ACL is 300. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddAccessContro lListEntry | The operation that you want to perform. Set the value to AddAccessCont rolList Ent ry. |
| AclId | String | Yes | acl- bp1l0kk4gxce43k ze***** | The ID of the ACL. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the ACL is created. |
| AclEntrys | String | No | [{"entry":"10.0.**. **/24","comment ":"privaterule1"}, {"entry":"192.168. **.**/16","comme nt":"privaterule2" }] | The IP addresses that you want to add to the ACL. ent ry: the IP addresses or CIDR blocks that you want to add to the ACL. Separate multiple IP addresses or CIDR blocks with commas (,). comment : the comment on the ACL. Not e You can add at most 50 IP addresses or CIDR blocks to an ACL in each call. If the IP address or CIDR block that you want to add to an ACL already exists, the IP address or CIDR block is not added. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 988CB45E-1643- 48C0-87B4- 928DDF77EA4 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddAccessControlListEntry &AclId=acl-bp1l0kk4gxce43kze***** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<AddAccessControlListEntryResponse>
    <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId>
</AddAccessControlListEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParam.AclEntr yExists | The specified aclEntry already exists in the acl. | The error message returned because the IP address or CIDR block is already in the ACL. |
| 400 | IllegalEntry | Entry version is conflict to the acl version. | The error message returned because the version of the IP address or CIDR block conflicts with the version of the ACL. |
| 400 | InvalidEntry | %s. | The error message returned because the value of a parameter is invalid. Specify a valid value and try again. |
| 400 | InvalidParam.Comm ent | The specified comment is invalid. | The error message returned because Comment is set to an invalid value. |
| 503 | ServiceUnavailable | Service is unavailable now. | The error message returned because the service is unavailable. |
| 400 | AclEntryExceedLimit | The maximum number of ACL entries is exceeded. | The error message returned because the number of specified IP addresses or CIDR blocks exceeds the upper limit. |

##### RemoveAccessControlListEntry

Removes IP addresses from an access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveAccessCo ntrolListEntry | The operation that you want to perform. Set the value to RemoveAccessCont rolList Ent ry. |
| AclId | String | Yes | acl- bp1l0kk4gxce43k ****** | The ID of the ACL. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the ACL is created. You can call the DescribeRegions operation to query the most recent region list. |
| AclEntrys | String | No | [{"entry":"10.0.**. **/24","comment ":"privaterule1"}] | The IP addresses that you want to remove from the ACL. ent ry: the IP address or CIDR block that you want to remove from the ACL. Separate multiple IP addresses or CIDR blocks with commas (,). comment : the comment of the ACL. Not e If the ACL is associated with a listener, you cannot remove all IP addresses from the ACL. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 988CB45E-1643- 48C0-87B4- 928DDF77EA49 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveAccessControlListEntry &AclId=acl-bp1l0kk4gxce43k****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<RemoveAccessControlListEntryResponse>
    <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId>
</RemoveAccessControlListEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49"
```

`}`

#### DeleteLoadBalancerListener

Deletes a listener. Not e You can delete only listeners that are in the st opped or running state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalan cerListener | The operation that you want to perform. Set the value to Delet eLoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5xm** ** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xm**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteLoadBalancerListenerResponse>
     <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId>
  </DeleteLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54"
```

`}`

#### StopLoadBalancerListener

Disables a listener. When you call this operation, take note of the following items: If the operation is successful, the listener switches to the Stopped state. You cannot perform the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state. Not e After a listener is disabled, it stops forwarding requests to the associated backend servers. This may cause service interruptions. Proceed with caution. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopLoadBalance rListener | The operation that you want to perform. Set the value to St opLoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5xmgl **** | The ID of the SLB instance. |
| Tags | String | No | null | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=StopLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xmgl**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StopLoadBalancerListenerResponse>
     <RequestId>21D2B318-650E-4B0B-A3B5-693D462247B3</RequestId>
  </StopLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "21D2B318-650E-4B0B-A3B5-693D462247B3"
```

`}`

#### StartLoadBalancerListener

Enables a listener. When you call this operation, take note of the following items: You can call the operation only when the listener is in the Stopped state. If the operation is successful, the state of the listener changes to Starting. You cannot call the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartLoadBalance rListener | The operation that you want to perform. Set the value to St art LoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5**** | The ID of the SLB instance. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=StartLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StartLoadBalancerListenerResponse>
     <RequestId>CC000321-00F2-49B8-9BCA-60D822414960</RequestId>
  </StartLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "CC000321-00F2-49B8-9BCA-60D822414960"
```

`}`

### Server certificates

#### UploadServerCertificate

Uploads a server certificate. You can upload only one server certificate and its private key in each request. The request is successful only when the server certificate and its private key are both uploaded. If the server certificate or its private key is not uploaded, the request fails. After a server certificate and its private key are uploaded, the fingerprints of all server certificates that belong to your account are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadServerCert ificate | The operation that you want to perform. Set the value to UploadServerCert if icat e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the server certificate is created. You can call the DescribeRegions operation to query region IDs. |
| AliCloudCertificat eId | String | No | 730912673****** _ 15d97e7709a 71 _ 445759hr 7892*** _ *** | The ID of the server certificate that is provided by Apsara Stack SSL Certificates Service. This parameter is required if you use a server certificate that is provided by Apsara Stack SSL Certificates Service. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AliCloudCertificat eName | String | No | testcertkey | The name of the server certificate that is provided by Apsara Stack SSL Certificates Service. |
| ServerCertificate | String | No | test | The public key certificate that you want to upload. Not e This parameter is required if you use a server certificate that is provided by a third party. |
| PrivateKey | String | No | wmsa**** | The private key that you want to upload. Not e This parameter is required if you use a server certificate that provided by a third party. |
| ServerCertificateN ame | String | No | mycert01 | The name of the server certificate that you want to upload. The name must be 1 to 80 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. |
| Tags | String | No | ServerCertificate* *** | The tag that you want to add to the server certificate. |
| StandardType | String | No | ServerCertificate | The type of the server certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerCertificat eId | String | xxxxidkp-123-cn- test**** | The ID of the server certificate. |
| ServerCertificat eName | String | mycert01 | The name of the server certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Fingerprint | String | 01:DF:AB:** | The fingerprint of the server certificate. |
| AliCloudCertific ateId | String | 730912xxxxx 15d97 _ e7709a 71445759hr _ 7**** _ | The ID of the server certificate if the server certificate is provided by Apsara Stack SSL Certificates Service. |
| AliCloudCertific ateName | String | testcert**** | The name of the server certificate if the server certificate is provided by Apsara Stack SSL Certificates Service. |
| IsAliCloudCertifi cate | Integer | 0 | Indicates whether the server certificate is provided by Apsara Stack SSL Certificates Service. Valid values: 0: The server certificate is provided by a third-party CA. 1: The server certificate is provided by Apsara Stack SSL Certificates Service. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the server certificate is created. |
| RegionIdAlias | String | hangzhou | The name of the region where the server certificate is created. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UploadServerCertificate &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UploadServerCertificateResponse>
      <RegionIdAlias>cn-east-hangzhou-01</RegionIdAlias>
      <Fingerprint>01:DF:AB:**</Fingerprint>
      <AliCloudCertificateName>testcert***</AliCloudCertificateName>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <IsAliCloudCertificate>0</IsAliCloudCertificate>
      <ServerCertificateId>xxxxidkp-123-cn-test******</ServerCertificateId>
      <ServerCertificateName>mycert01</ServerCertificateName>
      <RegionId>cn-hangzhou</RegionId>
      <AliCloudCertificateId>730912xxxxx_15d97e7709a_71445759hr_7*******</AliCloudCertifica
teId> </UploadServerCertificateResponse>
```

`JSON` format `{`

```json
    "UploadServerCertificateResponse": {
        "RegionIdAlias": "cn-east-hangzhou-01",
        "Fingerprint": "01:DF:AB:**",
        "AliCloudCertificateName": "testcert***",
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "IsAliCloudCertificate": 0,
        "ServerCertificateId": "xxxxidkp-123-cn-test******",
        "ServerCertificateName": "mycert01",
        "RegionId": "cn-hangzhou",
        "AliCloudCertificateId": "730912xxxxx_15d97e7709a_71445759hr_7*******"
```

`}` `}`

#### DeleteServerCertificate

Deletes a server certificate. Not e You cannot delete a server certificate that is in use. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteServerCerti ficate | The operation that you want to perform. Set the value to Delet eServerCert if icat e. |
| ServerCertificateI d | String | Yes | 123157**** 166f8 _ 204689 1714763 _ 408 7099**** _ | The ID of the server certificate. |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteServerCertificate &ServerCertificateId=123157****_166f8204689_1714763408_7099**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteServerCertificateResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</DeleteServerCertificateResponse>
```

`JSON` format `{`

```json
    "DeleteServerCertificateResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` `}`

#### DescribeServerCertificates

Queries server certificates in a specified region. Not e For security reasons, only fingerprints and names of the server certificates are returned. The content of the server certificates and private keys is not returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeServerCer tificates | The operation that you want to perform. Set the value to DescribeServerCert if icat es. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateI d | String | No | 12315790xxxxxxx 166f8204689 17 _ _ 14763408 709*** _ ** | The ID of the server certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerCertificat es | Array of ServerCertificat e |   | The list of server certificates. |
| ServerCertificat e |   |   |   |
| ServerCertificat eId | String | 123157xxxxxxxx 166 _ f8204689 17147634 _ 08 709981430-cn- _ east-hangz****** | The ID of the server certificate. |
| ServerCertificat eName | String | slb | The name of the server certificate. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the server certificate is created. |
| Fingerprint | String | 68:08:1a:f8:2c:97:6 9:a3:a1:e6:16:41:4 b:ca:4f:5d:ee:a5:ef :0d | The fingerprint of the server certificate. |
| AliCloudCertific ateId | String | 7309xxxxxxxx 15d97 _ e7709a 71445759hr _ 78928***** _ | The ID of the server certificate from Apsara Stack SSL Certificates Service. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AliCloudCertific ateName | String | testcertkey | The name of the server certificate from Apsara Stack SSL Certificates Service. |
| IsAliCloudCertifi cate | Integer | 0 | Indicates whether the server certificate is from Apsara Stack SSL Certificates Service. Valid values: 1: yes 0: no |
| RegionIdAlias | String | cn-qingdao-env17- d01 | The name of the region where the SLB instance is deployed. |
| StandardType | String | ServerCertificate | The type of the server certificate. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeServerCertificates &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeServerCertificatesResponse>
      <RequestId>9FFF450B-CC09-4FFB-900F-E347EB7AA2CC</RequestId>
      <ServerCertificates>
            <ServerCertificate>
                  <CreateTimeStamp>1541761156000</CreateTimeStamp>
                  <CommonName>*.example1.com</CommonName>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:ef:0d<
/Fingerprint>
                  <ServerCertificateId>1231579xxxxxx_166f8204689_1714763408_709981430</Serv
erCertificateId>
                  <ExpireTimeStamp>1558161264000</ExpireTimeStamp>
                  <AliCloudCertificateId>1501739</AliCloudCertificateId>
                  <ExpireTime>2019-05-18T06:34:24Z</ExpireTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <CreateTime>2018-11-09T10:59:16Z</CreateTime>
                  <ServerCertificateName>*.example1.com</ServerCertificateName>
                  <IsAliCloudCertificate>1</IsAliCloudCertificate>
                  <AliCloudCertificateName>slb</AliCloudCertificateName>
            </ServerCertificate>
            <ServerCertificate>
                  <CreateTimeStamp>1481623069000</CreateTimeStamp>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:84:8d<
/Fingerprint>
                  <ServerCertificateId>1231579085xxxx_158f79de306</ServerCertificateId>
                  <ExpireTimeStamp>1732169065000</ExpireTimeStamp>
                  <AliCloudCertificateId>0</AliCloudCertificateId>
                  <ExpireTime>2024-11-21T06:04:25Z</ExpireTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <CreateTime>2016-12-13T09:57:49Z</CreateTime>
                  <ServerCertificateName>test_certificate</ServerCertificateName>
                  <IsAliCloudCertificate>0</IsAliCloudCertificate>
                  <AliCloudCertificateName></AliCloudCertificateName>
            </ServerCertificate>
      </ServerCertificates>
</DescribeServerCertificatesResponse>
```

`JSON` format `{`

```json
    "DescribeServerCertificatesResponse": {
        "RequestId": "9FFF450B-CC09-4FFB-900F-E347EB7AA2CC",
        "ServerCertificates": {
            "ServerCertificate": [
```

`{`

```json
                    "CreateTimeStamp": 1541761156000,
                    "CommonName": "*.example1.com",
                    "RegionIdAlias": "cn-hangzhou",
                    "ResourceGroupId": "rg-acfmxazb4ph6aiy",
                    "Fingerprint": "68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:e
f:0d",
                    "ServerCertificateId": "1231579xxxxxx_166f8204689_1714763408_709981430"
```

`,`

```json
                    "ExpireTimeStamp": 1558161264000,
                    "AliCloudCertificateId": 1501739,
                    "ExpireTime": "2019-05-18T06:34:24Z",
                    "RegionId": "cn-hangzhou",
                    "CreateTime": "2018-11-09T10:59:16Z",
                    "ServerCertificateName": "*.example1.com",
                    "IsAliCloudCertificate": 1,
                    "AliCloudCertificateName": "slb"
```

`},` `{`

```json
                    "CreateTimeStamp": 1481623069000,
                    "RegionIdAlias": "cn-hangzhou",
                    "ResourceGroupId": "rg-acfmxazb4ph6aiy",
                    "Fingerprint": "cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:8
4:8d",
                    "ServerCertificateId": "1231579085xxxx_158f79de306",
                    "ExpireTimeStamp": 1732169065000,
                    "AliCloudCertificateId": 0,
                    "ExpireTime": "2024-11-21T06:04:25Z",
                    "RegionId": "cn-hangzhou",
                    "CreateTime": "2016-12-13T09:57:49Z",
                    "ServerCertificateName": "test_certificate",
                    "IsAliCloudCertificate": 0,
                    "AliCloudCertificateName": ""
```

`}` `]` `}` `}` `}`

#### SetServerCertificateName

Sets the name of a server certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetServerCertifica teName | The operation that you want to perform. Set the value to Set ServerCert if icat eName. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateI d | String | Yes | 139a****-cn- qingdao-env17- d01 | The ID of the server certificate. |
| ServerCertificateN ame | String | Yes | slb- servercertificate- cn-east- hangzhou**** | The name of the server certificate. The name must be 1 to 80 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FE7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetServerCertificateName &RegionId=cn-east-hangzhou-01 &ServerCertificateId=139a****-cn-east-hangzhou-01 &ServerCertificateName=slb-servercertificate-cn-east-hangzhou**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetServerCertificateNameResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId>
</SetServerCertificateNameResponse>
```

`JSON` format `{`

```json
    "SetServerCertificateNameResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984"
```

`}` `}`

#### UploadCACertificate

Uploads a CA certificate. You can upload only one CA certificate in each call. After a CA certificate is uploaded, the ID, name, and fingerprint of the certificate are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadCACertific ate | The operation that you want to perform. Set the value to UploadCACert if icat e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| CACertificate | String | Yes | test | The content of the CA certificate that you want to upload. |
| CACertificateNam e | String | No | mycacert01 | The name of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificateId | String | 139a00604ad-cn- east-hangzh**** | The ID of the CA certificate. |
| CACertificateNa me | String | mycacert01 | The name of the CA certificate. |
| Fingerprint | String | 02:DF:AB:ED | The fingerprint of the CA certificate. |

|   | Developer Guide·AP | I Reference |   | Server Load Balance | r |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UploadCACertificate &RegionId=cn-qingdao-env17-d01 &CACertificate=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UploadCACertificateResponse>
      <Fingerprint>02:DF:AB:ED</Fingerprint>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <CACertificateId>139a00604ad-cn-east-hangzh*****</CACertificateId>
      <CACertificateName>mycacert01</CACertificateName>
</UploadCACertificateResponse>
```

`JSON` format `{`

```json
    "UploadCACertificateResponse": {
        "Fingerprint": "02:DF:AB:ED",
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "CACertificateId": "139a00604ad-cn-east-hangzh*****",
        "CACertificateName": "mycacert01"
```

`}` `}`

#### DeleteCACertificate

Deletes a CA certificate. Not e You cannot delete a CA certificate that is in use. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCACertifica te | The operation that you want to perform. Set the value to Delet eCACert if icat e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 123157908**** 1 _ 5c73d77203 - _ 986300114 - _ 2110544**** | The ID of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteCACertificate &RegionId=cn-east-hangzhou-01 &CACertificateId=123157908****_15c73d77203_-986300114_-211054**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteCACertificateResponse>
      <RequestId>CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</DeleteCACertificateResponse>
```

`JSON` format `{`

```json
    "DeleteCACertificateResponse": {
        "RequestId": "CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` `}`

#### DescribeCACertificates

Queries CA certificates. Not e For security reasons, only fingerprints and names of the CA certificates are returned, the content of the CA certificates is not returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCACertifi cates | The operation that you want to perform. Set the value to DescribeCACert if icat es. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the CA certificate is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | No | 139a006****-cn- qingdao-env17- d01 | The ID of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificates | Array of CACertificate |   | Information about the CA certificate. |
| CACertificate |   |   |   |
| CACertificateId | String | 139a006****-cn- qingdao-env17-d01 | The ID of the CA certificate. |
| CACertificateNa me | String | test | The name of the CA certificate. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the CA certificate is created. |
| Fingerprint | String | AC:BE:FD | The fingerprint of the CA certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCACertificates &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCACertificateResponse>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <CACertificates>
            <CACertificateName>test</CACertificateName>
            <Fingerprint>AC:BE:FD</Fingerprint>
            <RegionId>cn-east-hangzhou-01</RegionId>
            <CACertificateId>139a006****-cn-east-hangzhou-02</CACertificateId>
      </CACertificates>
</DescribeCACertificateResponse>
```

`JSON` format `{`

```json
    "DescribeCACertificateResponse": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "CACertificates": {
            "CACertificateName": "test",
            "Fingerprint": "AC:BE:FD",
            "RegionId": "cn-east-hangzhou-01",
            "CACertificateId": "139a006****-cn-east-hangzhou-02"
```

`}` `}` `}`

#### SetCACertificateName

Sets the name of a CA certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetCACertificateN ame | The operation that you want to perform. Set the value to Set CACert if icat eName. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 139a0****-cn- qingdao-env17- d01 | The ID of the CA certificate. |
| CACertificateNam e | String | Yes | mycacert02 | The name of the CA certificate. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FE7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetCACertificateName &RegionId=cn-qingdao-env17-d01 &CACertificateId=139a0****-cn-qingdao-env17-d01 &CACertificateName=mycacert02 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetCACertificateNameResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId>
</SetCACertificateNameResponse>
```

`JSON` format `{`

```json
    "SetCACertificateNameResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984"
```

`}` `}`

### Backend servers

#### AddBackendServers

Adds backend servers. Not e If multiple identical Elastic Compute Service (ECS) instances are specified in a request, only the first ECS instance is added. The other ECS instances are ignored. If the backend server that you add is the same as one of the existing backend servers that are already associated with the listener, an error message is returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBackendServe rs | The operation that you want to perform. Set the value to AddBackendServers. |
| LoadBalancerId | String | Yes | lb- 2ze7o5h52g02kk zz**** | The ID of the Server Load Balancer (SLB) instance. |
|   |   |   |   | The list of backend servers that you want to add to the SLB instance. The following parameters are used to specify the backend servers: ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. You can specify the ID of an ECS instance or an elastic network interface (ENI). If ServerId is set to the ID of an ENI, the T ype parameter is required. Weight : The weight of the backend |

|   | Parameter |   | Type |   | Required |   | Example |   | server. Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | Valid values: 0 t o 100. |   |   |   |
|   | BackendServers |   | String |   | Yes |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", |   | Default value: 100. Not e If the weight is set to 0, no requests are forwarded to the backend server. Descript ion: Optional. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain _ Chinese characters. T ype: Specify the type of backend server. Valid values: ecs (default): an ECS instance. eni: an ENI. ServerIp: Specify the IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   | "Port":"80","Desc |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   | ription":"test- |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   | 113" }] |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |
|   | 12 |   |   |   |   |   |   |   | > Document Version: 2022091 |   |   |   |

| Parameter | Type | Required | Example |   | Description Not e Only backend servers |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | that are in the Running state can be added to an SLB instance. You can add at most 20 backend |   |
| Response parameters |   |   |   |   | servers in each call. |   |

| Parameter | Type | Example | You can specify ENIs as backend Descriptisoenrvers only for high-performance |
|---|---|---|---|
| LoadBalancerId | String | lb- 2ze7o5h52g02kkzz* *** | SLB instances. The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-2zej4lxhjoq1icu**** | The ID of the ECS instance or ENI. |
| Weight | String | 100 | The weight of the backend server. Valid values: 0 t o 100. Default value: 100. If the value is set to 0, the SLB instance does not forward requests to the backend server. |
| Description | String | BackendServer | The description of the backend server. |
| RequestId | String | 34B82C81-F13B- 4EEB-99F6- A048C67CC830 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddBackendServers &LoadBalancerId=lb-2ze7o5h52g02kkzz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBackendServersResponse>
    <BackendServers>
        <BackendServer>
            <ServerId>i-2zej4lxhjoq1icu*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
        <BackendServer>
            <ServerId>i-2ze1u9ywulp5pbv*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
    </BackendServers>
    <RequestId>34B82C81-F13B-4EEB-99F6-A048C67CC830</RequestId>
    <LoadBalancerId>lb-2ze7o5h52g02kkzz*****</LoadBalancerId>
</AddBackendServersResponse>
```

`JSON` format `{`

```json
    "AddBackendServersResponse": {
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "i-2zej4lxhjoq1icu*****",
                    "Weight": 100,
                    "Type": "ecs"
```

`},` `{`

```json
                    "ServerId": "i-2ze1u9ywulp5pbv*****",
                    "Weight": 100,
                    "Type": "ecs"
```

`}` `]` `},`

```json
        "RequestId": "34B82C81-F13B-4EEB-99F6-A048C67CC830",
        "LoadBalancerId": "lb-2ze7o5h52g02kkzz*****"
```

`}` `}`

#### RemoveBackendServers

Removes backend servers. Not e If the backend server that you want to remove does not belong to the specified Server Load Balancer (SLB) instance, the request fails. However, the system does not report an error. Request parameters

| Parameter |   | Type | Required |   | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| Action |   | String | Yes |   | RemoveBackendS ervers | The operation that you want to perform. Set the value to RemoveBackendServers. |   |   |   |
| BackendServers |   | String | Yes |   | [{"ServerId":"i- 2zej4lxhjoq****", "Type": "ecs","Weight":"1 00"}] | The backend servers to be removed. Valid values: ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. T ype: Specify the type of the backend server. Valid values: ecs: an Elastic Compute Service (ECS) instance. This is the default value. eni: an elastic network interface (ENI). Not e You can remove up to 20 backend servers in each call. Examples: ECS: [{"ServerId":"i- 2zej 4lx |   |   |   |
|   |   |   |   |   |   |   | [{"ServerId":"i- 2zej 4lx |   |   |
|   |   |   |   |   |   | hjoq ***", "Type": "ecs","Weig |   |   |   |
|   |   |   |   |   |   | ht":"100"}] |   |   |   |
|   |   |   |   |   |   | ENI: | [{"ServerId":"eni- 2ze 1s |   |   |
|   |   |   |   |   |   | dp 5***","Type": "eni","Weight |   |   |   |
|   |   |   |   |   |   | ":"100"}] |   |   |   |
| LoadBalancerId |   | String | Yes |   | lb- bp1qjwo61pqz3a hl**** | The ID of the SLB instance. |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb- bp1vjkb671z53**** | The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServer |   |   |   |
| ServerId | String | i-jjgjgjgggd**** | The ID of the backend server. |
| Weight | Integer | 100 | The weight of the backend server. Valid values: 0 t o 100. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveBackendServers &BackendServers=[{"ServerId":"i-2zej4lxhjoq****", "Type": "ecs","Weight":"100"}] &LoadBalancerId=lb-bp1qjwo61pqz3ahl**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveBackendServersResponse>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <LoadBalancerId>lb-bp1vjkb671z53cy******</LoadBalancerId>
  <BackendServers>
        <BackendServer>
              <ServerId>i-jjgjgjg*****</ServerId>
              <Weight>100</Weight>
        </BackendServer>
        <BackendServer>
              <ServerId>i-jjgjgituitu****</ServerId>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
</RemoveBackendServersResponse>
```

`JSON` format `{`

```json
    "RemoveBackendServers": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "LoadBalancerId": "lb-bp1vjkb671z53cy******",
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "i-jjgjgjg*****",
                    "Weight": 100
```

`},` `{`

```json
                    "ServerId": "i-jjgjgituitu****",
                    "Weight": 100
```

`}` `]` `}` `}` `}`

#### SetBackendServers

Sets the weights of backend servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetBackendServer s | The operation that you want to perform. Set the value to Set BackendServers. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a **** | The ID of the Server Load Balancer (SLB) instance. |
|   |   |   |   | The list of backend servers that you want to add to the SLB instance. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. |

|   | Parameter |   | Type |   | Required |   | Example |   | Weight : Required. Specify the Description weight of the backend server. This |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | parameter must be of the INTEGER type. Valid values: 0 to 100. |   |   |   |
|   | BackendServers |   | String |   | Yes |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Desc ription":"test- 112" }] |   | Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: Specify the IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |

| Parameter |   | Type | Required |   | Example |   |   | Description Not e The backend servers |   |
|---|---|---|---|---|---|---|---|---|---|
| Response parameters |   |   |   |   |   |   |   | that you add to an SLB instance must be in the Running state. You can add at most 20 backend |   |
| Parameter | Type |   |   | Example |   | Descri |   | ptsioenrvers to an SLB instance in each call. In addition, you can specify |   |
| LoadBalancerId | String |   |   | lb- bp1qjwo61pqz3a*** * |   | ENIs as backend servers only for The ID ohf igthhe- pSeLrBf oinrsmtaannccee. SLB instances. |   | ENIs as backend servers only for ohf igthhe- pSeLrBf oinrsmtaannccee. SLB instances. |   |
| BackendServers | Array of BackendServer |   |   |   |   | The list of backend servers. |   |   |   |
| BackendServer |   |   |   |   |   |   |   |   |   |
| ServerId | String |   |   | eni-hg231**** |   | The ID of the ECS instance. |   |   |   |
| Weight | String |   |   | 100 |   | The weight of the backend server. |   |   |   |
| Description | String |   |   | BackendServer |   | The description of the backend server. |   |   |   |
| Type | String |   |   | ecs |   | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |   |   |   |
| RequestId | String |   |   | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 |   | The ID of the request. |   |   |   |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetBackendServers &LoadBalancerId=lb-bp1qjwo61pqz3a**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetBackendServersResponse>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <LoadBalancerId>lb-dhf13*******</LoadBalancerId>
      <BackendServers>
            <BackendServer>
                  <ServerId>eni-hg231**</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
            <BackendServer>
                  <ServerId>eni-hfhf***</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
      </BackendServers>
</SetBackendServersResponse>
```

`JSON` format `{`

```json
    "SetBackendServersResponse": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "LoadBalancerId": "lb-dhf13*******",
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "eni-hg231**",
                    "Weight": 100,
                    "Type": "eni"
```

`},` `{`

```json
                    "ServerId": "eni-hfhf***",
                    "Weight": 100,
                    "Type": "eni"
```

`}` `]` `}` `}` `}`

### vServer groups

#### CreateVServerGroup

Creates a vServer group and adds backend servers to the vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVServerGro up | The operation that you want to perform. Set the value to Creat eVServerGroup. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a hl**** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |
| VServerGroupNa me | String | No | Group1 | The name of the vServer group. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
|   |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- | The list of backend servers to be added. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements in a list for each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. |

|   |   |   |   |   |   |   | pt o : test |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | BPaacrakmenedtSeerrvers |   | STtyrpineg |   | NReoquired |   | 112" }, { Example "ServerId": "eni- |   | T ype: Required. Specify the type of Description the backend server. This parameter |   |   |   |
|   |   |   |   |   |   |   | xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" }] |   | must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-2**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | vServerGroup | The description of the vServer group. |
| ServerType | String | ECS |   |
| Type | String | Type | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVServerGroup &LoadBalancerId=lb-bp1qjwo61pqz3ahl**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVServerGroupResponse>
  <VServerGroupId>rsp-bp1i4c******</VServerGroupId>
  <RequestId>3EBBDBAE-8E8B-438F-A109-95C2FDB2C333</RequestId>
  <BackendServers>
        <BackendServer>
              <Type>ecs</Type>
              <ServerId>i-bp1ds2yjlk66********</ServerId>
              <Description>test-11244</Description>
              <Port>80</Port>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
</CreateVServerGroupResponse>
```

`JSON` format `{`

```json
  "VServerGroupId": "rsp-bp1i4c3******",
  "RequestId": "3EBBDBAE-8E8B-438F-A109-95C2FDB2C333",
  "BackendServers": {
    "BackendServer": [
```

`{`

```json
        "Type": "ecs",
        "ServerId": "i-bp1ds2yjlk666******",
        "Description": "test-11244",
        "Port": 80,
        "Weight": 100
```

`}` `]` `}` `}`

#### SetVServerGroupAttribute

Modifies the configurations of a vServer group. You can call the operation to modify only configurations such as the weight and port of a backend server. If you want to modify backend servers in a specified vServer group, call the `ModifyVServerGroupBack` `endServers` operation. If you want to add backend servers, call the `AddVServerGroupBackendServers` operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetVServerGroup Attribute | The operation that you want to perform. Set the value to Set VServerGroupAt t ribut e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupNa me | String | No | vserver-group- test | The name of the vServer group. |
|   |   |   |   | The backend servers in the vServer group. |

|   | erver Load Balancer |   |   |   |   |   |   |   | Developer Guide·API Referenc |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   | Type |   | Required |   | Example |   | You can add up to 20 backend servers Description in each call. |   |   |   |
|   | BackendServers |   | String |   | No |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Desc ription":"test- 113" }] |   | ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |

|   |   |   |   | 6.**.**", "Port":"80","Descrip Description |   |
|---|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |   |
|   |   |   |   | tion":"test-113" }] |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupN ame | String | Group1 | The name of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-bp1ek6yd7jvkx**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescrip tion. | The description of the vServer group. |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetVServerGroupAttributeResponse>
  <BackendServers>
        <BackendServer>
              <ServerId>i-bp1ek6yd7jvkx*****</ServerId>
              <Port>80</Port>
              <Weight>100</Weight>
              <Type>ecs</Type>
        </BackendServer>
  </BackendServers>
  <RequestId>A4FDF333-F904-4540-88FC-ED6F87AEFFCB</RequestId>
  <VServerGroupId>rsp-bp1d2e3*****</VServerGroupId>
  <VServerGroupName>test1</VServerGroupName>
</SetVServerGroupAttributeResponse>
```

`JSON` format `{`

```json
    "SetVServerGroupAttributeResponse": {
        "BackendServers": {
            "BackendServer": {
                "ServerId": "i-bp1ek6yd7jvkx*****",
                "Port": 80,
                "Weight": 100,
                "Type": "ecs"
```

`}` `},`

```json
        "RequestId": "A4FDF333-F904-4540-88FC-ED6F87AEFFCB",
        "VServerGroupId": "rsp-bp1d2e3*****",
        "VServerGroupName": "test1"
```

`}` `}`

#### AddVServerGroupBackendServers

Adds backend servers to a specified vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddVServerGroup BackendServers | The operation that you want to perform. Set the value to AddVServerGroupBackendServers. |
|   |   |   |   | The list of backend servers that you want to add to the vServer group. You can specify up to 20 backend servers in each request. |

|   | eveloper Guide·API |   | Reference |   |   |   |   |   | Server Load Balance |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   | Type |   | Required |   | Example |   | The following parameters are used to Description specify the backend servers: |   |   |   |
|   | BackendServers |   | String |   | Yes |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6*", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Desc ription":"test- 113" }] |   | ServerId: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). Port : Required. The port that is used by the backend server. Valid values: 1 t o 65535. Weight : The weight of the backend server. Valid values: 0 t o 100. Default value: 100. If the value is set to 0, no requests are forwarded to the backend server. T ype: The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |

|   |   |   |   | tion":"test-113" }] |   |   |
|---|---|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |   |   |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-231 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | test | The description of the vServer group. |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weigh t": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }
```

`]`

```
&RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddVServerGroupBackendServersResponse>
  <VServerGroupId>rsp-cige6j******</VServerGroupId>
  <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
  <BackendServers>
        <Type>ecs</Type>
        <Description>test</Description>
        <ServerId>vm-231</ServerId>
        <Weight>100</Weight>
        <Port>70</Port>
  </BackendServers>
</AddVServerGroupBackendServersResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6j******", "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "BackendServers":[
    {"Type":"ecs","Description":"test","ServerId":"vm-231","Weight":"100","Port":"70"}
```

`]` `}`

#### RemoveVServerGroupBackendServers

Removes a backend server from a specified vServer group. Not e If one or more backend servers specified by BackendServers do not exist in the vServer group, the backend servers are ignored and no error message is returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveVServerGr oupBackendServe rs | The operation that you want to perform. Set the value to RemoveVServerGroupBackendServ ers. |
| BackendServers | String | Yes | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Desc ription":"test- 113" }] | The list of backend servers that you want to remove from the vServer group. You can specify at most 20 backend servers for a vServer group in each call. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. ServerIp: Specify the IP address of the ECS instance or ENI. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-230 | The ID of the ECS instance or ENI. |
| Port | Integer | 80 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weigh t": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }
```

`]`

```
&RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveVServerGroupBackendServersResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
   <VServerGroupId>rsp-cige6******</VServerGroupId>
   <BackendServers>
      <BackendServer>
         <ServerId>vm-231</ServerId>
         <Port>70</Port>
         <Weight>100</Weight>
                              <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
</RemoveVServerGroupBackendServersResponse>
```

`JSON` format `{`

```json
  "RemoveVServerGroupBackendServersResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "VServerGroupId": "rsp-cige6******",
    "BackendServers": {
      "BackendServer": {
        "ServerId": "vm-231",
        "Port": "70",
        "Weight": "100",
        "Type": "ecs"
```

`}` `}` `}` `}`

#### ModifyVServerGroupBackendServers

Replaces backend servers in a specified vServer group. You can call this operation to replace the backend servers in a specified vServer group. To modify the configurations of the backend servers, such as their weights, you can call the `SetVServerGroupAttribute` operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVServerGro upBackendServer s | The operation that you want to perform. Set the value to Modif yVServerGroupBackendServer s. |

| Parameter |   | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|---|
| RegionId |   | String | Yes |   | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |   |
| VServerGroupId |   | String | Yes |   | rsp-cige6j**** | The ID of the vServer group. |   |
| OldBackendServer s |   | String | No |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Desc ription":"test- 112" }] | The list of backend servers to be replaced. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. Specify the description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an ENI ServerIp: Specify the IP address of the ECS instance or ENI Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |
|   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |
|   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |
|   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |
|   |   |   |   |   |   | n":"test-112" }] |   |

|   | Parameter |   | Type |   | Required |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | red | Example |   | Description xxxx", "Weight": "100", "Type" | tion |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |
|   |   |   |   |   |   |   |   |   | The list of backend servers to be added. You can specify at most 20 backend servers for a vServer group in each call. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. |   |   |
|   | NewBackendServ ers |   | String |   | No |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80" "Desc |   | This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. It can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It _ can also contain Chinese characters. T ype: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI ServerIp: the IP address of the ECS |   |   |

|   |   |   |   |   |   |   | Port : 80 , Desc |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   | Type |   | Required |   | rEixpatmionp"le:"test- 113" }] |   | instance or ENI Description |   |   |   |
|   |   |   |   |   |   |   |   |   | Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-236 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVServerGroupBackendServers &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVServerGroupBackendServersResponse>
      <VServerGroupId>rsp-cige6j******</VServerGroupId>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
      <BackendServers>
            <ServerId>vm-236</ServerId>
            <Weight>100</Weight>
            <Port>70</Port>
      </BackendServers>
</ModifyVServerGroupBackendServersResponse>
```

`JSON` format `{`

```json
    "ModifyVServerGroupBackendServersResponse": {
        "VServerGroupId": "rsp-cige6j******",
        "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
        "BackendServers": {
            "ServerId": "vm-236",
            "Weight": 100,
            "Port": 70
```

`}` `}` `}`

#### DeleteVServerGroup

Deletes a vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVServerGro up | The operation that you want to perform. Set the value to Delet eVServerGroup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6j**** | The ID of the vServer group. Not e You cannot delete a vServer group that is in use. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVServerGroup &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVServerGroupResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteVServerGroupResponse>
```

`JSON` format `{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

`}`

#### DescribeVServerGroups

Queries the vServer groups of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerG roups | The operation that you want to perform. Set the value to DescribeVServerGroups. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5i6ea** ** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroups | Array of VServerGroup |   | The list of backend servers. |
| VServerGroup |   |   |   |
| VServerGroupId | String | rsp-bp1oygn**** | The ID of the vServer group. |
| VServerGroupN ame | String | k8s/31065/nginx- ingress-lb/kube- system/clust****" | The name of the vServer group. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVServerGroups &LoadBalancerId=lb-bp1o94dp5i6ea**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVServerGroupsResponse>
  <VServerGroups>
        <VServerGroup>
              <VServerGroupId>rsp-bp1oygn******</VServerGroupId>
              <VServerGroupName>k8s/31065/nginx-ingress-lb/kube-system/clust****</VServerGr
oupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1i6sn******</VServerGroupId>
              <VServerGroupName>k8s/31605/nginx-ingress-lb/kube-system/clusterid</VServerGr
oupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1f85n******</VServerGroupId>
              <VServerGroupName>VSG1</VServerGroupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
  </VServerGroups>
  <RequestId>31ADDBCD-275F-4C37-B0A3-5DFC8564E686</RequestId>
</DescribeVServerGroupsResponse>
```

`JSON` format `{`

```json
 "VServerGroups": {
  "VServerGroup": [
```

`{`

```json
    "VServerGroupId": "rsp-bp1oygn******",
    "VServerGroupName": "k8s/31065/nginx-ingress-lb/kube-system/clust****",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `},` `{`

```json
    "VServerGroupId": "rsp-bp1i6sn******",
    "VServerGroupName": "k8s/31605/nginx-ingress-lb/kube-system/clusterid",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `},` `{`

```json
    "VServerGroupId": "rsp-bp1f85n******",
    "VServerGroupName": "VSG1",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `}` `]` `},`

```json
 "RequestId": "31ADDBCD-275F-4C37-B0A3-5DFC8564E686"
```

`}`

#### DescribeVServerGroupAttribute

Queries detailed information about a vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerG roupAttribute | The operation that you want to perform. Set the value to DescribeVServerGroupAt t ribut e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupN ame | String | Group1 | The name of the vServer group. The name is 1 to 80 characters in length, and can contain Chinese characters, letters, digits, hyphens (- ), forward slashes (/), periods (.),and underscores ( ). _ |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-233 | The ID of the Elastic Compute Service (ECS) instance. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescrip tion. | The description of the vServer group. |
| ServerType | String | ecs |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVServerGroupAttributeResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
   <VServerGroupId>rsp-cige6******</VServerGroupId>
   <VServerGroupName>Group1</VServerGroupName>
   <BackendServers>
      <BackendServer>
         <ServerId>vm-232</ServerId>
         <Port>80</Port>
         <Weight>100</Weight>
      </BackendServer>
      <BackendServer>
         <ServerId>vm-233</ServerId>
         <Port>90</Port>
         <Weight>100</Weight>
      </BackendServer>
   </BackendServers>
</DescribeVServerGroupAttributeResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6*****","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","VSer verGroupName":"Group1","BackendServers":[{"ServerType":"ecs","Type":"ecs","ServerId":"vm-23 3","Description":"vServerGroupDescription.","VpcId":"vpc-**","Port":"90","ServerIp":"192.16 8.*.*","Weight":"100"}]}
```

### Primary/secondary server groups

#### CreateMasterSlaveServerGroup

Creates a primary/secondary server group. A primary/secondary server group contains only two Elastic Compute Service (ECS) instances. One of the ECS instances serves as the primary server. The other ECS instance serves as the secondary server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMasterSlav eServerGroup | The operation that you want to perform. Set the value to Creat eMast erSlaveServerGroup. |
| LoadBalancerId | String | Yes | lb- bp1hv944r69al4j* *** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |
| MasterSlaveServe rGroupName | String | No | sg- atstuj3rtopty**** | The name of the primary/secondary server group. |
|   |   |   |   | The list of backend servers in the primary/secondary server group. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each call. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter must be of the |

| Parameter |   | Type | Required |   | Example |   | STRING type. The description must Description be 1 to 80 characters in length and |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). The _ description can contain Chinese characters. ServerT ype: Specify the type of the backend server. This parameter must be of the STRING type. Valid values: |   |   |   |   |
| MasterSlaveBacke ndServers |   | String | No |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Serv erType":"Master" ,"Description":"te st-112" }, { "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Serv erType":"Slave"," Description":"tes t-112" }] |   | Mast er: primary server Slave: secondary server T ype: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an elastic network interface (ENI) ServerIp: the IP address of the ECS instance or ENI. A primary/secondary server group can contain at most two backend servers. If you do not set this parameter, an empty primary/secondary server group is created. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |   |
|   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   | "ecs", "Port":"80","ServerType |   |   |   |   |
|   |   |   |   |   |   |   | ":"Master","Description":"test |   |   |   |   |
|   |   |   |   |   |   |   | -112" }, { "ServerId": "i-xxxx |   |   |   |   |
|   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |
|   |   |   |   |   |   |   | ": "ecs", "Port":"80","ServerT |   |   |   |   |
|   |   |   |   |   |   |   | ype":"Slave","Description":"te |   |   |   |   |
|   |   |   |   |   |   |   | st-112" }] |   |   |   |   |
|   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |   |
|   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |   |
|   |   |   |   |   |   |   | : "eni", "Port":"80","ServerTy |   |   |   |   |
|   |   |   |   |   |   |   | pe":"Master","Description":"te |   |   |   |   |
|   |   |   |   |   |   |   | st-112" }, { "ServerId": "eni- |   |   |   |   |
|   |   |   |   |   |   |   | xxxxxxxxx", "Weight": "100", " |   |   |   |   |
|   |   |   |   |   |   |   | Type": "eni", "ServerIp": "192 |   |   |   |   |
|   |   |   |   |   |   |   | .168.**.**", "Port":"80","Serv |   |   |   |   |
|   |   |   |   |   |   |   | erType":"Slave","Description": |   |   |   |   |
|   |   |   |   |   |   |   | "test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |

|   | Parameter | Type |   | Required | Example | Weight": "100", "Type": "eni", Description |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |
|   |   |   |   |   |   | Port":"80","ServerType":"Maste |   |
|   |   |   |   |   |   | r","Description":"test-112" }, |   |
|   |   |   |   |   |   | { "ServerId": "eni-xxxxxxxxx", |   |
|   |   |   |   |   |   | "Weight": "100", "Type": "eni" |   |
|   |   |   |   |   |   | ,"ServerIp": "192.168.**.**", |   |
|   |   |   |   |   |   | "Port":"80","ServerType":"Slav |   |
|   |   |   |   |   |   | e","Description":"test-112" }] |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupId | String | rsp-cige6j**** | The ID of the primary/secondary server group. |
| MasterSlaveBac kendServers | Array of MasterSlaveBac kendServer |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveBac kendServer |   |   |   |
| ServerId | String | vm-2h**** | The ID of the ECS instance or ENI that is added. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| ServerType | String | Slave | Indicates whether the backend server is a primary or secondary server. Valid values: Mast er and Slave. Default value: Master. |
| Description | String | Primary/SecondaryS erverGroupDescripti on. | The description of the primary/secondary server group. The description is 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateMasterSlaveServerGroup &LoadBalancerId=lb-bp1hv944r69al4j**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateMasterSlaveServerGroupResponse>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
      <MasterSlaveServerGroupId>rsp-cige******</MasterSlaveServerGroupId>
      <MasterSlaveBackendServers>
            <MasterSlaveBackendServers>
                  <ServerId>vm-gtgt***</ServerId>
                  <Port>80</Port>
                  <Weight>100</Weight>
                  <ServerType>Master</ServerType>
            </MasterSlaveBackendServers>
            <MasterSlaveBackendServers>
                  <ServerId>vm-tygtyg****</ServerId>
                  <Port>90</Port>
                  <Weight>100</Weight>
                  <ServerType>Slave</ServerType>
            </MasterSlaveBackendServers>
      </MasterSlaveBackendServers>
</CreateMasterSlaveServerGroupResponse>
```

`JSON` format `{`

```json
    "CreateMasterSlaveServerGroupResponse": {
        "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
        "MasterSlaveServerGroupId": "rsp-cige******",
        "MasterSlaveBackendServers": {
            "MasterSlaveBackendServers": [
```

`{`

```json
                    "ServerId": "vm-gtgt***",
                    "Port": 80,
                    "Weight": 100,
                    "ServerType": "Master"
```

`},` `{`

```json
                    "ServerId": "vm-tygtyg****",
                    "Port": 90,
                    "Weight": 100,
                    "ServerType": "Slave"
```

`}` `]` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | BACKEND SERVERS N _ _ UM MUST BE TWO _ _ _ | Backend servers num must be 2. | The error message returned because two backend servers must be specified. |
| 400 | BACKEND SERVERS H _ _ AVE SAME PORT AN _ _ _ D SERVERID _ | Backend servers have same port and serverId. | The error message returned because a backend server with the same port and ID is already specified in the server group. |
| 400 | BACKEND SERVERS C _ _ AN ONLY CONTAIN _ _ _ ONE MASTER AND O _ _ _ NE SLAVE _ | Backend servers can only contain one master and one slave. | The error message returned because a primary/secondary server group can contain only one primary server and one secondary server. |
| 400 | BACKEND SERVER ID _ _ CAN NOT EMPTY _ _ _ | Backend server id can not empty. | The error message returned because the ID of the backend server is not specified. |
| 400 | INVALID SERVER TYP _ _ E | Invalid server type. | The error message returned because the specified type of backend server is invalid. |
| 400 | BACKEND SERVER PO _ _ RT CAN NOT EMPTY _ _ _ | Backend server port can not empty. | The error message returned because the port of the backend server is not specified. |

| erver Load Ba | lancer |   | Developer Guide·API Referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | RealServerPortNotSu pport | Real server port not support. | The error message returned because the specified port of the backend server is invalid. |

#### DeleteMasterSlaveServerGroup

Deletes a specified primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMasterSlav eServerGroup | The operation that you want to perform. Set the value to Delet eMast erSlaveServerGroup. |
| MasterSlaveServe rGroupId | String | Yes | rsp-cige6**** | The ID of the primary/secondary server group. Not e You cannot delete a primary/secondary server group that is in use. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMasterSlaveServerGroup &MasterSlaveServerGroupId=rsp-cige6**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteMasterSlaveServerGroupResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteMasterSlaveServerGroupResponse>
```

`JSON` format `{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

`}`

#### DescribeMasterSlaveServerGroups

Queries backend servers in a primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSl aveServerGroups | The operation that you want to perform. Set the value to DescribeMast erSlaveServerGroups. |
| LoadBalancerId | String | Yes | lb- bp14zi0n66zpg6 o**** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroups | Array of MasterSlaveSer verGroup |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveSer verGroup |   |   |   |
| MasterSlaveSer verGroupId | String | rsp-0bfuc**** | The ID of the primary/secondary server group. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupName | String | Group3 | The name of the primary/secondary server group. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroups &LoadBalancerId=lb-bp14zi0n66zpg6o**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMasterSlaveServerGroupsResponse>
      <RequestId>2631BB5E-B576-4925-BDED-07A66D23E5DE</RequestId>
      <MasterSlaveServerGroups>
     <MasterSlaveServerGroup>
        <MasterSlaveServerGroupId>rsp-bp1ro3mw******</MasterSlaveServerGroupId>
        <MasterSlaveServerGroupName>test</MasterSlaveServerGroupName>
     </MasterSlaveServerGroup>
      </MasterSlaveServerGroups>
</DescribeMasterSlaveServerGroupsResponse>
```

`JSON` format `{`

```json
    "RequestId": "265989FE-136B-4D6A-B549-FD40E7",
    "MasterSlaveServerGroups": {
        "MasterSlaveServerGroup": [
```

`{`

```json
                "MasterSlaveServerGroupId": "rsp-bp1nly******",
                "MasterSlaveServerGroupName": "primary/secondary1",
                "AssociatedObjects": {
                    "Listeners": {
                        "Listener": [ ]
```

`}` `}` `}` `]` `}` `}`

#### DescribeMasterSlaveServerGroupAttribute

Queries detailed information about a primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSl aveServerGroupA ttribute | The operation that you want to perform. Set the value to DescribeMast erSlaveServerGroupA t t ribut e. |
| MasterSlaveServe rGroupId | String | Yes | rsp-cige6j**** | The ID of the primary/secondary server group. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupId | String | rsp-cige6**** | The ID of the primary/secondary server group. |
| MasterSlaveSer verGroupName | String | Group1 | The name of the primary/secondary server group. |
| MasterSlaveBac kendServers | Array of MasterSlaveBac kendServer |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveBac kendServer |   |   |   |
| ServerId | String | vm-hrf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerType | String | Slave | The type of backend server. Valid values: Mast er and Slave. Default value: Master. |
| Description | String | Primary/SecondaryS erverGroupDescripti on. | The description of the primary/secondary server group. |
| Type | String | ecs | The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroupAttribute &MasterSlaveServerGroupId=rsp-cige6j**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMasterSlaveServerGroupAttributeResponse>
    <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
    <MasterSlaveServerGroupId>rsp-cige6******</MasterSlaveServerGroupId>
    <MasterSlaveBackendServers>
          <MasterSlaveBackendServers>
                <ServerId>vm-sshssh****</ServerId>
                <Port>80</Port>
                <Weight>100</Weight>
                <ServerType>Master</ServerType>
          </MasterSlaveBackendServers>
          <MasterSlaveBackendServers>
                <ServerId>vm-ffff*****</ServerId>
                <Port>90</Port>
                <Weight>100</Weight>
                <ServerType>Slave</ServerType>
          </MasterSlaveBackendServers>
    </MasterSlaveBackendServers>
</DescribeMasterSlaveServerGroupAttributeResponse>
```

`JSON` format `{`

```json
  "DescribeMasterSlaveServerGroupAttributeResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "MasterSlaveServerGroupId": "rsp-cige6******",
    "MasterSlaveBackendServers": {
      "MasterSlaveBackendServers": [
```

`{`

```json
          "ServerId": "vm-sshssh****",
          "Port": "80",
          "Weight": "100",
          "ServerType": "Master"
```

`},` `{`

```json
          "ServerId": "vm-ffff*****",
          "Port": "90",
          "Weight": "100",
          "ServerType": "Slave"
```

`}` `]` `}` `}` `}`

### Tags

#### AddTags

Adds tags to a Server Load Balancer (SLB) instance. When you call this operation, take note of the following items: You can add at most 10 tags to an SLB instance. You can specify at most five tags in each request. All tags and keys added to an SLB instance must be unique. If you add a tag that has the same key as an existing tag but with a different value, the new tag overwrites the existing tag. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddTags | The operation that you want to perform. Set the value to AddT ags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |
| Tags | String | Yes | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags to be added. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddTags &LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</AddTagsResponse>
```

`JSON` format `{`

```json
  "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710"
```

`}`

#### DescribeTags

Queries a list of tags. When you call this operation, take note of the following items: You can query tags by instance ID, tag key, and tag value. If the operation is successful, the system returns all tags that match the specified conditions. If the logical relationship among the specified conditions is `AND` , only tags that match all of the specified conditions are returned. If the Tagkey parameter is specified and the Tagvalue parameter is not specified, all tags that contain the specified tag key are returned. If you have specified the Tagvalue parameter in a request, you must also specify the Tagkey parameter in this request. If you specify both the Tagkey and Tagvalue parameters, tags with the specified key-value pair are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTags | The operation that you want to perform. Set the value to DescribeT ags. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| Tags | String | No | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags to be queried. |
| DistinctKey | Boolean | No | false | Specifies whether the tag is DistinctKey. Valid values: t rue and f alse. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | No | 1 | The number of the page to return. Minimum value: 1. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TagSets | Array of TagSet |   | The list of tags. |
| TagSet |   |   |   |
| TagKey | String | test | The key of the tag. |
| TagValue | String | api | The value of the tag. |
| InstanceCount | Integer | 10 | The number of instances to which the tag is added. |
| PageSize | Integer | 50 | The number of entries returned on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | 1 | The number of the returned page. Minimum value: 1. Default value: 1. |
| TotalCount | Integer | 1 | The total number of instances that are returned after the tags are matched against the specified conditions. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTags &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
    <TagSets>
            <TagSet>
                  <TagKey>test</TagKey>
                  <TagValue>api</TagValue>
            </TagSet>
      </TagSets>
   <PageSize>50</PageSize>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
</DescribeTagsResponse>
```

`JSON` format `{`

```json
    "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
    "TagSets": {
        "TagSet": [
```

`{`

```json
                "TagKey": "test",
                "TagValue": "api"
```

`}` `],`

```json
        "PageNumber": 1,
        "PageSize": 50,
        "TotalCount": 1
```

`}` `}`

#### RemoveTags

Removes tags from a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveTags | The operation that you want to perform. Set the value to RemoveT ags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tags | String | Yes | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags that you want to remove. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveTags &LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</RemoveTagsResponse>
```

`JSON` format

```json
{ "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710" }
```

### Error codes

|   | Error code |   |   |   | Error message |   |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|
|   | CertificateAndPriv |   |   |   | Certificate and |   |   |   | The error message returned because the certificate is used by other resources. |
|   |   |   |   |   |   | Certificate and |   |   | The |
|   |   | CertificateAndPriv |   |   |   | Certificate |   |   |   |
|   |   |   | ficateAndPriv |   | PrivateKey I |   |   |   |   |
|   |   |   |   |   |   |   |   | 40 |   |
|   | ateKeyIsRefered |   | sRefered |   |   |   |   |   |   |
|   |   |   |   |   | Refered. |   |   |   |   |

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code |   | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | CertificateNotMatc |   |   |   |   |   |   |   |   |   |   |   | Certificate and |   |   |   |   |   |   | The error message returned because the certificate and the private key do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Certificate and |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | CertificateNotMatc |   |   |   |   |   |   |   |   |   |   |   | Certifi |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ficateNotMatc |   |   |   |   |   |   | key does |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |   |
|   |   |   |   |   |   | hPrivateKey |   |   |   |   | eKey |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health- |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health- |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ch |   |   | ecked Listener |   |   |   | The error message returne |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | enerNot |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | to |   |   | the specified |   | 404 |   | health c |   |
|   |   |   |   |   |   | Found |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | authorized to |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the |   |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified |   |   |   |   |   |   | you are unauthorized to per |   |
|   |   |   |   |   |   |   | Forbbiden.SubUser |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 403 |   | you are unauthori |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource as your |   |   |   |   |   |   | operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | account is |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | created by |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | another user. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   | The error message returned because you are unauthorized to perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | authorized to |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the |   |   |   |   | 403 |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | IncorrectListenerA |   |   |   |   |   |   |   |   |   |   |   | Current |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Current |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   | IncorrectList |   |   |   |   |   |   |   | enerA |   |   | listener access |   |   |   |   |   |   | The error message returned be |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the access control configuratio |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the access c |   |
|   |   |   |   |   |   |   | ccessControlStatusSt |   |   |   |   |   |   |   |   |   |   | co |   | ntrol status |   |   | 500 |   | the listener i |   |
|   |   |   |   |   |   | atus |   |   |   |   |   |   |   |   |   |   |   | does not support |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   | The error message returned because an internal error occurred. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing has |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message re |   |
|   |   |   |   |   |   |   | InternalError |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failed due to |   |   |   |   | 400 |   | an in |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backend service |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exception. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing has |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InternalInvokeErro |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failed due to |   |   |   |   |   |   | The error message re |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 500 |   |   |   |
|   |   |   |   |   |   | r |   |   |   |   |   |   |   |   |   |   |   | some unknown |   |   |   |   |   |   | an int |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | error, exception |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or failure. |   |   |   |   |   |   |   |   |

|   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancer |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance's |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | addresstype is |   |   |   |   | the network types of the Elastic |   |
|   |   |   |   |   | InvalidBackendServ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | private, so it |   |   |   | 400 | Compute Service (ECS) instances |   |
|   |   |   |   | ers.Inconsistent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | forbidden to add |   |   |   |   | that of the S |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ecs vpc |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backendservers |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | for now. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BackendServers on |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned because you cannot specify both ECS |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | you cannot specify both ECS |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | one Specified |   |   |   |   | instances in a classic network and |   |
|   |   |   |   |   |   |   | InvalidBackendServ |   |   |   |   |   |   |   |   |   |   |   |   | instances in a classi |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancer h |   |   | ave | 400 | ECS instances in a vi |   |
|   |   |   |   | ers.Inconsistent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | to be in the same |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc or all |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | classic |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   | The error message returned because you are unauthorized to perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | identity was not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   | InvalidIdentity | InvalidIdentity |   |   |   |   | entity |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | allowed |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operated. |   |   |   |   |   |   |
|   |   |   |   | InvalidLoadBalance |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The error message returned because the specified SLB instance is invalid. |   |
|   |   |   |   |   | InvalidLoadBalance |   |   |   |   |   |   |   |   |   |   | LoadBala | ncerId |   | 404 |   |   |
|   |   |   |   | rId.NotF |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ound |   |   |   |   |   |   | does not exist. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the specified certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | format is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | error. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the certificate is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The |   |
|   |   |   |   |   | InvalidParameter |   |   |   | Parameter |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id is empty. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the ID of the server certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id is not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | support. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the certificate and the private key are not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or Key is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | empty. |   |   |   |   |   |   |

|   |   |   |   |   | Error code |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified private key is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter key |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   | InvalidParameter | InvalidParameter | Parameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | format is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | error. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned because the specified region does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   | Specified |   | T |   |
|   |   |   |   |   |   | InvalidPara |   | meter |   | region does not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Port is not Integer. |   | 400 | The error message returned because the specified port is invalid. Valid values: 1 to 65535. |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   | 400 | The error message returned because the specified port is invalid. Valid values: 1 to 65535. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   | Invalid | Parameter |   |   | port is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified bandwidth limit is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | Th |   |
|   |   |   |   |   |   | Invalid | Parameter |   |   | bandwidth is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned because a specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | Specified |   | The |   |
|   |   |   |   |   |   | InvalidPara |   | meter |   | parameter Check |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of HealthCheckHttpCode is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | HealthCheckHttpCo |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | de is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth is not |   |   | the specified value of Band |   |
|   |   |   |   |   | InvalidParameter | InvalidParameter |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | valid, out of the |   |   | exceeds |   |
|   |   |   |   |   |   |   |   |   |   | instance total |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of Bandwidth is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified health check configuration is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error messa |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | HealthCheck is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |

|   | Port is not | 40 |
|---|---|---|
| Integer. |   |   |

|   |   |   |   | Error code |   |   |   |   | Error message |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error mess |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | SourceItem is not |   |   |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified protocol type is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | T |
|   |   |   |   |   | Invalid | Parameter |   |   | protocol is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 40 |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | RS Pool is empty. |   | 400 | The error message returned because no backend server is available. |
|   |   |   |   | InvalidParameter |   |   |   |   | RS Pool doesn't exist. |   | 400 | The error message returned because no backend server is available. |
|   |   |   |   | InvalidParameter |   |   |   |   | Illegal user ID. |   | 400 | The error message returned because the user ID is invalid. |
|   |   |   |   | InvalidParameter |   |   |   |   | User ID is null |   | 400 | The error message returned because the user ID is not specified. |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified type of SLB instance is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error m |
|   |   |   |   |   | Invalid | Parameter |   |   | parameter lb type _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of Mode is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error |
|   |   |   |   |   | Invalid | Parameter |   |   | parameter mode is |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | not valid.. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of AccessControlStatus is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   |   |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The erro |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | AccessControlStat |   | 400 |   |
|   |   |   |   |   |   |   |   |   | us is not |   |   |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error messa |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | SourceItems is |   |   |   |
|   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of BackendServers is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error message |
|   |   |   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   |   |   | 404 | th |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 404 |   |
|   |   |   |   |   |   |   |   |   | BackendServers is |   |   |   |
|   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned because a specified parameter is invalid. |
|   |   |   |   |   |   |   |   |   |   | Specified |   |   |
|   |   |   |   |   | InvalidPara |   | meter |   | parameter is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |

|   | RS Pool is |
|---|---|
| empty. |   |

|   | RS Pool doesn't | 400 |
|---|---|---|
| exist. |   |   |

|   | Illegal user |
|---|---|
| ID. |   |

|   | User ID is |
|---|---|
| null |   |

|   |   |   | Error code |   |   |   | Error message |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of Domain is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error m |
|   |   |   |   | Invalid | Parameter |   | parameter Domain |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of URI is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The err |
|   |   |   |   | Invalid | Parameter |   | parameter URI is |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of Scheduler is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error me |
|   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | Scheduler is not |   |   |   |
|   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of ListenerStatus is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message |
|   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   | 400 | th |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ListenerStatus is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of PersistenceTimeout is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message return |
|   |   |   |   |   |   |   | parameter |   |   | The err |
|   |   |   |   |   |   |   |   |   | 400 | the spe |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | PersistenceTimeou |   |   |   |
|   |   |   |   |   |   |   | t is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of ConnectPort is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error messa |
|   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ConnectPort is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of ConnectTimeout is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error messag |
|   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   | 400 | t |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ConnectTimeou is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of StickySessionType is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message retu |
|   |   |   |   |   |   |   | parameter |   |   | The e |
|   |   |   |   |   |   |   |   |   | 400 | the s |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | StickySessionType |   |   |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of HealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message ret |
|   |   |   |   |   |   |   | parameter |   |   | The |
|   |   |   |   |   |   |   |   |   | 400 | the |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | HealthyThreshold |   |   |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of UnhealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message return |
|   |   |   |   |   |   |   | parameter |   |   | The err |
|   |   |   |   |   |   |   |   |   | 400 | the spe |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | UnhealthyThreshol |   |   |   |
|   |   |   |   |   |   |   | d is not valid. |   |   |   |

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of Interval is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error m |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 40 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Interval is not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of XForwardedFor is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error messag |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | t |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | XForwardedFor is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of IsPublicAddress is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message r |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   | Th |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | the |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | IsPublicAddress |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidRegionId.No tFound |   |   |   |   |   |   |   |   | Specified region does not exist. |   |   |   |   | 404 | The error message returned because the specified region is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   | The error message returned because the ID of the backend server is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | serv |   |   |   | er ID is not |   | The error messag |   |
|   |   |   |   |   |   |   |   |   |   |   | rverId.Ma |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vali |   |   |   | d, flush | 400 |   |   |
|   |   |   |   |   |   | lformed |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | control ip chain |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | fail. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidServerId.No |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified backend server is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InvalidServerId.No |   |   |   |   |   |   |   |   | Th |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ServerId.No |   |   |   |   | ser |   |   |   |   |   |   |   |
|   |   |   |   |   |   | tFound |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | found. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidWeight.Malf |   |   |   |   |   |   |   |   | A specified |   |   |   |   | 400 | The error message returned because the specified value of weight is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InvalidWeight.Malf |   |   |   |   |   |   |   |   | A |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ight.Malf |   |   |   | we |   |   |   |   |   |   |   |
|   |   |   |   |   |   | ormed |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | IpNotAvailable |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of Address is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error m |   |
|   |   |   |   |   |   |   | IpNotAv |   |   | ailable |   |   |   |   | parameter Address |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | ListenerAlreadyExi |   |   |   |   |   |   |   |   | There is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | There is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | already a |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | Lis | tenerAlreadyExi |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener bound to |   |   |   |   | The error message retur |   |
|   |   |   |   |   |   | sts |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the port on the |   |   |   |   |   | the |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified load |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | balancer. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to |   |   |   |   |   | The error message returned because the specified listener is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the specified |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The |   |
|   |   |   |   |   |   | ListenerNotFound | ListenerNotFound |   |   | rNotFound |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |

| InvalidRegionId.No | Spe |
|---|---|

|   |   |   |   | Error code |   |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter Cookie |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned b |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   |   | the Cookie parameter is not |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   | 400 | the Cook |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | specified |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | BackendServerPort |   |   | The error message returned because |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   | 400 | the BackendServerPort param |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | not speci |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | LoadBalancerId |   |   | The error message returned because |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   | 400 | the LoadBalancerId paramete |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | specified |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | RegionId that is |   |   | The error message returned because |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | mandatory for |   | 400 | the RegionId param |   |
|   |   |   |   |   |   |   |   |   |   | processing this |   |   | spec |   |
|   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | supplied. |   |   |   |   |
|   |   |   |   | MissingParameter |   |   |   |   |   | The combination |   |   | The error message returned because a required parameter is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   | The combination |   |   |   |
|   |   |   |   |   |   |   |   |   |   | of some |   |   |   |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameters |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | violates the |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | spec. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | OwnerId,OwnerAcco |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned beca |   |
|   |   |   |   |   |   |   |   |   |   | unt that is |   |   | OwnerAccount and OwnerId are n |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   | 403 | OwnerAccount and |   |
|   |   |   |   |   |   |   |   |   |   | mandatory for |   |   | specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | spec |   |
|   |   |   |   |   |   |   |   |   |   | processing this |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | supplied. |   |   |   |   |
|   |   |   |   | PrivateKeyEncrypti on |   |   |   |   |   | Key has Encrypted . |   | 400 | The error message returned because the private key is encrypted. |   |

| PrivateKeyEncrypti |   |   | Key has | 4 |
|---|---|---|---|---|

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | ProcessingSameRequ |   |   |   |   |   |   |   |   |   |   |   |   | The same |   |   |   |   | The error message returned because the same request is being processed. Try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The same |   |   |   | The error message ret |   |
|   |   |   |   |   |   |   |   | ProcessingSa |   |   |   |   |   |   |   | meRequ |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request is being |   |   | 400 | the same |   |
|   |   |   |   |   |   | est |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processed. Please |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | try later. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServerCertificateI |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   | The error message returned because the specified certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ServerCerti |   |   |   |   |   |   | ficateI |   |   |   | ServerCe |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | rtificate | 404 |   |   |
|   |   |   |   |   |   | d.NotFound |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id does not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exist. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The request has |   |   |   |   | The error message returned because the service is unavailable. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request has |   |   |   |   |   |
|   |   |   |   |   |   |   |   | Servic |   |   |   | eUnavailable |   |   |   |   |   |   | failed due to a |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 | The error mes |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | temporary failure |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | of the server. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the specified name already exists. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The error mes |   |
|   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   | loadbalancer name |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has been used. |   |   |   |   |   |   |
|   |   |   |   |   |   | TcpNotSupportForHy |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   | The error message returned because you cannot create TCP listeners. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loa |   | dbalancer |   |   | The error m |   |
|   |   |   |   |   |   |   |   | TcpNotSupportForHy |   |   |   |   |   | ortForHy |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doe |   |   |   | 400 |   |   |
|   |   |   |   |   |   | bridLb | bridLb |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TCP type |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number of input |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned |   |
|   |   |   |   |   |   |   |   | TooManyBackendServ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | real servers |   |   | 400 | you canno |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | ers |   |   |   |   |   |   |   |   |   |   |   |   | exceeds max |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported number: |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 20. |   |   |   |   |   |   |
|   |   |   |   |   |   | TooManyBackendServ |   |   |   |   |   |   |   |   |   |   |   |   | The backend |   |   |   |   | The error message returned because the number of backend servers exceeds the limit. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The backend |   |   |   | The error messag |   |
|   |   |   |   |   |   |   |   | TooManyBac |   |   |   |   |   | kendServ |   |   |   |   |   |   |   |   |   | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | server parameter |   |   | 400 | th |   |
|   |   |   |   |   |   | ers |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 4 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has too many |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | entries. |   |   |   |   |   |   |
|   |   |   |   |   |   | UnsupportedOperati on |   |   |   |   |   |   |   |   |   |   |   |   | The |   |   |   |   | The error message returned because the specified type of SLB instance does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The |   |   |   | The error mes |   |
|   |   |   |   |   |   |   |   | UnsupportedOperat |   |   |   |   |   |   |   |   | i |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Loadbalancer |   |   | 400 | the spe |   |
|   |   |   |   |   |   | on |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doesn't support |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this function. |   |   |   |   |   |   |
|   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because you cannot perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The |   |
|   |   |   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | rtedOperati |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | on |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |   |   |

|   |   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port has been |   |   |   |   |
|   |   |   |   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | assigned one type |   |   | The error message returned because |   |
|   |   |   |   |   |   |   | ononfixedprotocalpor |   |   |   |   |   |   |   |   |   |   |   |   | of protocal, and |   | 400 | the protocol of the specified |   |
|   |   |   |   |   |   |   | t |   |   |   |   |   |   |   |   |   |   |   |   | this protocal |   |   | does not s |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doesn't support |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |
|   |   |   |   |   |   |   | UnsupportedParamet |   |   |   |   |   |   |   |   |   |   |   |   | The input |   |   | The error message returned because a specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input |   | The e |   |
|   |   |   |   |   |   |   |   |   | UnsupportedParamet |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Paramet |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | er |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | unsupported. |   |   |   |   |
|   |   |   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   |   |   |   |   |   |   |   | The vip |   |   | The error message returned because the protocol type of the listener and the protocol type of the backend server do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The vip |   | The err |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | protocol is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   |   | pool |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match with |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Rspool. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   | The error message returned because you cannot add more than 50 listeners in each call. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number of input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message return |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | istener |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listeners exceeds |   | 400 | you can |   |
|   |   |   |   |   |   |   | s |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | max supported |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number: 50. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified resource does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | The |   |
|   |   |   |   |   |   |   |   |   | Invalid |   |   |   |   | Parameter |   |   |   |   |   | resource does not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exist. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified instance is being configured. Try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loadbalancer is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | configuring, |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | please retry |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | later. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | please make sure |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the system fails to obtai |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | ceUnavailable |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the ECS exists |   | 503 | addr |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | and the status is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | running. |   |   |   |   |
|   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified region does not support VPCs. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | Th |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   | region not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | support VPC. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified VPC is deleted. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc cloud |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   | InvalidParameter |   |   |   |   | Parameter |   |   |   |   |   |   |   | 4 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance has |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | deleted. |   |   |   |   |

## Appendix

### Call the ASAPI gateway

You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to the relevant references. Procedure
1. Obtain ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain ASAPI SDK. For more information, see Obtain ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPIObtain the
endpoint of ASAPI.
3. Obtain your AccessKey pair. @
Obtain the AccessKey pair that is required for calling an API operation. Not e We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
4. Obtain the region ID.
Obtain the region ID that is required for calling an API operation.
5. Obtain the organization ID and resource set ID.
You can call an API operation to obtain the organization ID. For more information about how to obtain the organization ID, see GetOrganizationList in Apsara Uni-manager Management Console De veloper Guide. You can call an API operation to obtain the resource set. For more information about how to obtain the resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Dev eloper Guide. Not e When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs-resourcegroupid> parameters. This allows you to query specified resources. If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default. If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.
6. Refer to the API reference.
Obtain the developer guide of the cloud service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
7. Use ASAPI SDK to call API operations.
After you complete the preceding steps, you can use ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java:

```
public static void main(String[] args) {
    ASClient client = new ASClient();
    // Specify the caller. The caller is recorded in logs.
    client.setSdkSource("autoTest");
    // Set request parameters.
    Map<String, Object> parameters = new HashMap<String, Object>();;
    parameters.put("Product", "Slb");// Specify the POP code, which is the same as the
POP code in the corresponding API directory.
    parameters.put("Action", "DescribeLoadBalancers"); // Specify the name of the API o
peration. Use the same letter case as the letter case in the corresponding API director
```

`y.`

```java
    parameters.put("Version", "2014-05-15"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify your AccessKey ID and AccessKey secret.
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

### Use ASAPI to make API calls

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

#### Obtain the endpoint of the ASAPI

This topic describes three methods that can be used to generate an endpoint for the Apsara Stack API (ASAPI).
1. Log on to the OPS1 server.
2. Run the following commands to generate three different domain names:

```bash
kubectl get ingress -n ascm |grep asapiserver
```

3. Use the domain name that starts with `public` as the value of the `domain` parameter.
4. Generate an endpoint for ASAPI based on the following format:

```
https://<domain>/asapi/v3
```

#### Obtain Apsara Stack SDKs

Apsara Stack API is a unified portal provided by Apsara Stack. You can use Apsara Stack API to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. Public environment If you are using the public environment, you can go to the Apsara Stack documentation page and download Apsara Stack SDKs in the Ot her Resources section at the lower part of the page. Private environment If you are using the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download Apsara Stack SDKs in the Ot her Resources section. Apsara Stack SDK for Java

| greopId | artifactId | version |
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
| idna | 3.2 |
| jmespath | 0.10.0 |

| erver Load Balancer | Developer Guide·Appendi |
|---|---|
| Package | Version |
| pycparser | 2.20 |
| requests | 2.26.0 |
| urllib3 | 1.26.6 |

Not e You can use the version for each package listed in the preceding table or a later version.

### STS overview

#### What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token. Use an STS token to assume a RAM role An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources. Benefits STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. You do not need to rotate STS tokens when they expire. You can attach policies to STS tokens to create fine-grained permissions on cloud resources based on your business requirements.

#### AssumeRole

Obtains a Security Token Service (STS) token to assume a Resource Access Management (RAM) role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role. Request parameters

| Paramet er | T ype | Requi red | Example | Descript ion |
|---|---|---|---|---|
| Act ion | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |

| Developer Guide·Appe | ndix |   |   | Server Load Balance |
|---|---|---|---|---|
| Paramet er | T ype | Requi red | Example | Descript ion |
| RoleArn | String | Yes | acs:ram::1234567 89012****:role/ad minrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |
| RoleSessionNam e | String | Yes | alice | The custom name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the API caller. For example, you can specify a username. You can specify RoleSessionName to identify API callers that assume the same RAM role in ActionTrail logs. This allows you to track the users that perform the operations. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource ": ["*"]}],"Version":"1 "} | The policy that specifies the permissions of the returned STS token. This allows you to implement more fine-grained access control. Limits: The policy must be 1 to 1,024 characters in length. |

Response parameters

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Request Id | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credent ials | N/A | N/A | The STS credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5 U1**** | The AccessKey ID. |

| erver Load Balancer |   |   | Developer Guide·Appendi |
|---|---|---|---|
| Paramet er | T ype | Example | Descript ion |

| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
|---|---|---|---|
| Securit yT oken | String | ******** | The STS token. |
| Expirat ion | String | 2015-04- 09T11:52:19Z | The expiration time. |
| AssumedRoleUser | N/A | N/A | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789 012****:role/adminr ole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495**** :alice | The ID of the temporary identity that you use to assume the RAM role. |

Add Project Object Model (POM) dependencies The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

Call an API operation to obtain the STS credentials. In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the credentials.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest;
```

`p` `y` `q`

```java
import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
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
        // Replace "sts.aliyuns.com" with the actual endpoint of the STS API. In most cases
, endpoint is in the following format: sts-vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the name of the role session.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the ARN that you obtain in the preceding step.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS credentials.
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

`}` `}` `}` Sample code In this example, the `DescribeZones` operation is called to query the zones of Elastic Compute Service (ECS).

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey I
D and the AccessKey secret obtained in the preceding step. The AccessKey ID and the AccessK ey secret are assigned by STS.
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
        // Replace "<yourStsToken>" with the STS token that you obtained in the preceding s
tep.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Optional. Specify the resource set ID.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");
        try {
            CommonResponse response = client.getCommonResponse(request);
```

```java
            System.out.println(response.getData());
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

`}` `}` `}` Error codes

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleAr n | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSe ssionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the format of the RoleSessionName parameter is invalid. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |

| Ht t pCode | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter.Durati onSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the Durat ionSeconds parameter is invalid. The value must be greater than or equal to 900 and less than or equal to the MaxSessionDurat ion value. |
| 400 | InvalidParameter.PolicyG rammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the specified policy is invalid. |
| 400 | InvalidParameter.PolicyS ize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |
