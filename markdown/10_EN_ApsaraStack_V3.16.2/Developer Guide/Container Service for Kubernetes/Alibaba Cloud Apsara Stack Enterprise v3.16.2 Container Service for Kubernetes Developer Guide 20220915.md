---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Container Service for Kubernetes Developer Guide"
product_version: "V3.16.2"
doc_version: "20220915"
pdf_pages: 98
source_pdf: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Container Service for Kubernetes Developer Guide 20220915.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.16.2_intl_en/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97%2B%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Container%20Service%20for%20Kubernetes%20Developer%20Guide%2020220915.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Container Service for Kubernetes Developer Guide

## SDK reference

### Getting started

1.1.1. Usage notes on development documentation This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI). Prerequisites The Apsara Stack version is obtained from an O&M personnel or operations administrator. Procedure You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the Ent erprise, Agilit y, or All-in-one tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click View Det ails or Download PDF.
1.1.2. Make API calls You can use the Portable OpenAPI Proxy (POP) gateway or the Apsara Stack API (ASAPI) gateway to call Apsara Stack API operations. Starting from Apsara Stack Enterprise V3.16.0, POP Gateway is used by default to ensure a user experience same as Alibaba Cloud public cloud. This topic describes how to use the POP gateway to call Apsara Stack API operations. Not e You can still use the ASAPI gateway to call API operations. For more information, see Call API operations by using the ASAPI gateway, Obtain the endpoint of ASAPI, and Obtain ASAPI SDK. Flowchart Procedure
1. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for the API call. For more information, see Obtain an AccessKey pairor Obtain an AccessKey pair assigned by STS. Not e We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
2. Obtain the region ID.
For more information about how to obtain the value of the RegionID parameter, see Obtain the values of common headers.
3. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Co nsole Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Cons ole Developer Guide. Not e When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set. If you do not set the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is queried. If you do not set the `<x-acs-resourcegroupid>` parameter, this parameter is left empty by default. If you specify a resource set, you must also specify an organization ID.
4. Refer to the developer guide of the cloud service that you want to use to learn how to make an API call.
Refer to the developer guide of the cloud service that you want to use to learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
5. Obtain the endpoint of the cloud service.
6. Obtain the cloud service SDK and call an API operation.

### Preparations

1.2.1. Log on to the API Tool console You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, which include ! @ # $ %
3. Click Log On.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding operations in the following scenarios:
You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click Log On. c. Enter a six-digit MFA verification code and click Aut hent icat e. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click Aut hent icat e. Not e For more information, see the Bind a virtual MFA device to enable MFA topic in Apsara Uni-manager Management Console User Guide.
5. In the top navigation bar, choose Product s > Ot hers > API T ool.
1.2.2. View the information about an operation This topic describes how to view information about an API operation. The information includes service names, API operation names, and API versions. The information is required when you use an SDK to call API operations. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see the developer guide of the corresponding cloud service. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.
5. In the left-side navigation pane, click API Direct ory.
6. On the API Direct ory page, select the required cloud service from the Product Name drop-down list, enter a keyword of an operation name in the search box, and
then click Search.
7. In the search result, you can view the cloud service name, API operation name, and API version.
1.2.3. Obtain an AccessKey pair AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM. Context An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur. Warning The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
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
1.2.4. Obtain an STS AccessKey pair This topic describes how to use STS to make API calls. Background information Alibaba Cloud Security Token Service (STS) allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and an STS token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS?. Procedure
1. Obtain the `RAM role` that is assigned to the current user.
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click User Inf ormat ion. iii. Click View Current Role Policy. In the View Policies of Current Role dialog box, you can obtain information about the `RAM role` that is assigned to the current user.
2. Obtain an STS AccessKey 3-tuple.
Not e You must replace the following fields with the actual values. Delete the angle brackets (<>) before you submit the code. <yourRegionID>: Replace the field with the actual region ID. <yourAccessKeyID>: Replace the field with the AccessKey ID of the current user. <yourAccessKeySecret>: Replace the field with the AccessKey secret of the current user. <yourRoleSessionName>: Replace the field with the actual session name. <yourRoleArn>: Replace the field with the Alibaba Cloud Resource Name (ARN) of the RAM role that is assigned to the current user. <sts.aliyuns.com>: Replace the field with the actual endpoint of STS.

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the actual values.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
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
    // Replace "sts.aliyuns.com" with the actual endpoint of STS. The format of an endpoint of STS is sts-vpc.${global:region}.${global:internet-
domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // The business parameter. Replace <yourRoleSessionName> with the actual session name.
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

3. Use the STS AccessKey 3-tuple to call the `DescribeUserQuota` operation of Container Service. The following code provides an example:
Not e You must replace the following fields with the actual values. Delete the angle brackets (<>) before you submit the code. <yourRegionID>: Replace the field with the actual region ID. <yourAccessKeyID>: Replace the field with the AccessKey ID of the current user. <yourAccessKeySecret>: Replace the field with the AccessKey secret of the current user. <yourStsToken>: Replace the field with the STS token of the STS AccessKey 3-tuple. <yourResourceGroupID>: Replace the field with the actual resource set ID. <yourOrganizationID>: Replace the field with the actual organization ID.

```java
public class DescribeUserQuota {
    public static void main(String[] args) {
        /** use STS Token **/
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",           // The region ID
            "<your-access-key-id>",       // The AccessKey ID of the RAM account
            "<your-access-key-secret>",   // The AccessKey Secret of the RAM account
            "<your-sts-token>");          // STS Token
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        //request.setProtocol(ProtocolType.HTTPS);
        request.setMethod(MethodType.GET);
        request.setDomain("cs.cn-qingdao.aliyuncs.com");
        request.setVersion("2015-12-15");
        request.setUriPattern("/quota");
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

1.2.5. Obtain the values of common header parameters You must provide multiple header parameters when you call API operations. This topic describes the header parameters and how to obtain the values of the header parameters. This topic also describes the response parameters of specific header parameters after you call Apsara Stack API operations. Header parameters

| Paramet er | Descript ion |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-inst anceid | The ID of the Container Service cluster for which you want to call API operations. For more information about how to obtain cluster IDs, see Obtain a Container Service cluster ID. |

Query a region ID
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane, choose Resources > Regions.
4. Click the name of the organization that you want to view.
5. You can obtain the region ID in the Regions list.
Obtain an organization ID You can call the GetOrganizationList operation to obtain the organization ID. For more information, see the GetOrganizationList topic of the Apsara Uni-manager Management Console Developer Guide. Obtain a resource set ID You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see the ListResourceGroup topic of the Apsara Uni-manager Management Console Developer Guide. Obtain a Container Service cluster ID You can obtain a Container Service cluster ID on the Clusters page of the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose Product s > Elast ic Comput ing > Cont ainer Service f or Kubernet es.
3. In the left-side navigation pane, click Clust ers.
4. On the Clust ers page, click the name of the cluster that you want to manage.
5. On the Clust er Inf ormat ion page, click the Basic Inf ormat ion tab.
On the Basic Inf ormat ion tab, you can obtain the cluster ID. Response parameters The following response parameters are returned by default when you call list-type API operations for cloud product resource instances.

| Paramet er | Descript ion |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

1.2.6. Obtain the endpoint of Container Service for Kubernetes This topic describes how to obtain the endpoint of Container Service. Background information To use the Portable OpenAPI Proxy (POP) gateway to call API operations in Apsara Stack, you must specify the endpoint of the corresponding cloud service. You can obtain the endpoint from Alibaba Cloud onsite O&M engineers. You can also perform the following steps to obtain an endpoint. Procedure
1. On the top menu bar of the Apsara Uni-manager Operations Console, click Product s, and then click Apsara Inf rast ruct ure Management Framework.
2. On the left navigation bar of the Apsara Inf rast ruct ure Management Framework, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` .
4. On the Regist rat ion Vars of Services page, Click the
icon next to Service, enter `acs` and then click Apply Filt er.
5. In the Service Regist rat ion column of the `acs-acs_control` service, right-click and click Show More. On the details page, view the cs.openapi.endpoint value,
that is, Endpoint. On the Det ails page, view the csint ernal.openapi.endpoint value, which is the `endpoint` . 1.2.7. Obtain the Container Service SDK package When you call API operations in Apsara Stack by using the Portable OpenAPI Proxy (POP) gateway, you must use the SDK of the corresponding cloud service. This topic describes how to obtain Apsara Stack SDKs. An SDK includes code and examples. You can create cloud applications by using an SDK for the programming language that you require. The SDKs for Java, Python, and Go are provided. You can select the SDKs from Alibaba Cloud SDKs based on your business requirements. Not e We recommend that you use an SDK for Java, Python, or Go. If you use SDKs for other programming languages, the SDKs may be incompatible with your system. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack.

### Examples of using Container Service SDK for Java

1.3.1. Install Container Service SDK for Java This topic describes how to install Container Service SDK for Java. Environment requirements You must use Java 6 or later. To install the core library of Container Service SDK for Java, you can add the following dependencies to a Project Object Model (POM) file:

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.21</version>
</dependency>
```

Install Container Service SDK for Java To install Container Service SDK for Java by using Apache Maven, add the following dependencies to the project file:

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-cs</artifactId>
  <version>4.8.1</version>
</dependency>
```

1.3.2. Use Container Service SDK for Java This topic describes how to use Container Service SDK for Java. Procedure
1. Initialize the com.aliyuncs.profile.DefaultProfile object.

| The Profile object contains parameters such as | your-access-key-id , | your-access-key-secret | , and | your-region-id | . |
|---|---|---|---|---|---|
| IClientProfile profile = DefaultProfile.getProfile("<your-region-id>", "<your-access-key-id>", "<your-access-key-secret>"); |   |   |   |   |   |

2. Instantiate a client object from the com.aliyuncs.IAcsClient class.

```
IAcsClient client = new DefaultAcsClient(profile);
```

3. Create a request based on the required API operation.
The class is named after the API operation, followed by Request.

```
DescribeEventsRequest request = new DescribeEventsRequest();
```

4. Configure request parameters.
Call the setXxx method of the request class to set required parameters for the API operation.

```
request.setcluster_id("test"); // Specify the parameter based on your requirements. request.settype("test"); // Specify the parameter based on your requirements. request.setpage_size("1"); // Specify the parameter based on your requirements. request.setpage_number("1"); // Specify the parameter based on your requirements.
```

5. Obtain a response by using the client object.

```java
DescribeEventsResponse response = client.getAcsResponse(request); System.out.println(JSON.toJSONString(response));
```

6. Call the corresponding get method in the response to obtain the values of response parameters.

```java
System.out.println(response.getRequestId());
```

7. Call the catch() method to handle server and client errors.
Handle server errors

```
catch (ServerException e) {
    e.printStackTrace();
```

Handle client errors

```java
catch (ClientException e) {
    System.out.println("ErrCode:" + e.getErrCode());
    System.out.println("ErrMsg:" + e.getErrMsg());
    System.out.println("RequestId:" + e.getRequestId());
```

Sample code

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.alibaba.fastjson.JSON; import java.util.*; import com.aliyuncs.cs.model.v20151215.*; public class DescribeImages {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", "LTAjVUwKznS*****", "BNPO1zoNSi484oizGM9fzzwJJ*****");
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        DescribeEventsRequest request = new DescribeEventsRequest();
        request.setcluster_id("test"); // Specify the parameter based on your requirements.
        request.settype("test"); // Specify the parameter based on your requirements.
        request.setpage_size("1"); // Specify the parameter based on your requirements.
        request.setpage_number("1"); // Specify the parameter based on your requirements.
        try {
            DescribeEventsResponse response = client.getAcsResponse(request);
            System.out.println(JSON.toJSONString(response));
            // Print response parameters. In this example, the RequestId parameter is printed.
            System.out.println(response.getRequestId());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            // Print the error code.
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

### Examples of using Container Service SDK for Python

1.4.1. Install Container Service SDK for Python This topic describes how to install Container Service SDK for Python. Environment requirements You must use Python 2.7 or 3.x. Install Container Service SDK for Python by using the pip tool:

```
pip install alibabacloud_tea_openapi
```

Install Container Service SDK for Python PyPI PIP

```
pip install aliyun-python-sdk-cs==4.8.1
```

PyPI Anaconda

```
conde install aliyun-python-sdk-cs=4.8.1
```

1.4.2. Use Container Service SDK for Python This topic describes how to use Install Container Service SDK for Python. Procedure
1. Instantiate a client object from the AcsClient class of the aliyunsdkcore package.

| The client object contains the | your-access-key-id , | your-access-key-secret | , and | your-region-id | parameters. |
|---|---|---|---|---|---|
| from aliyunsdkcore.client import AcsClient client = AcsClient( ak="<your-access-key-id>", secret="<your-access-key-secret>", region_id='<region-id>' ) |   |   |   |   |   |

2. Create a request based on the required API operation.
The class is named after the API operation, followed by Request.

```
from aliyunsdkcs.request.v20151215.DescribeEventsRequest import DescribeEventsRequest request = DescribeEventsRequest()
```

3. Configure request parameters.
Use the set method of the request class to set the required parameters.

```
// Specify this parameter based on your requirements. request.set_cluster_id("test") // Specify this parameter based on your requirements. request.set_type("test") // Specify this parameter based on your requirements. request.set_page_size("1") // Specify this parameter based on your requirements. request.set_page_number("1")
```

4. Obtain a response by using the client object.

```python
response = client.do_action_with_exception(request) print(response)
```

5. You can use the try...except... method to handle exceptions that occur on clients and servers.
Handle server errors

```python
try:
    ...
except ServerException as e:
    print(e)
```

Handle client errors

```python
try:
    ...
except ClientException as e:
    print(e)
```

Sample code

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcs.request.v20151215.DescribeEventsRequest import DescribeEventsRequest client = AcsClient('<your-access-key-id>', '<your-access-key-secret>', 'cn-hangzhou') // Create an API request and configure the parameters. request = DescribeEventsRequest() // Specify this parameter based on your requirements. request.set_cluster_id("test") // Specify this parameter based on your requirements. request.set_type("test") // Specify this parameter based on your requirements. request.set_page_size("1") // Specify this parameter based on your requirements. request.set_page_number("1") response = client.do_action_with_exception(request) // Print response parameters as required.
# python2:  print response
print(str(response, encoding='utf-8'))
```

### Examples of using Container Service SDK for Go

1.5.1. Install Container Service SDK for Go This topic describes how to install Container Service SDK for Go. Environment requirements You must use Go 1.10.x or later. Install the core library of Container Service SDK for Go

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

Install Container Service SDK for Go Install Container Service SDK for Go by running the go get command:

```
go get github.com/aliyun/alibaba-cloud-sdk-go/services/CS
```

1.5.2. Use Container Service SDK for Go This topic describes how to use Container Service SDK for Go. Procedure
1. Add the following dependencies:

```java
import (
  cs "github.com/aliyun/alibaba-cloud-sdk-go/services/cs"
```

`)`
2. Instantiate a client object from the cs.NewClientWithAccessKey class.

| your-access-key-id , | your-access-key-secret |
|---|---|

```
client, err := cs.NewClientWithAccessKey("<your-region-id>", "<your-access-key-id>", "<your-access-key-secret>")
```

3. Create a request based on the required API operation.
The method is in the following format: Create<API operation>Request().

```
request := cs.CreateDescribeEventsRequest()
```

4. Set request parameters.
You must specify the parameters that are required to call the API operation.

```
// Specify this parameter based on your requirements. request.cluster_id = "test" // Specify this parameter based on your requirements. request.type = "test" // Specify this parameter based on your requirements. request.page_size = "1" // Specify this parameter based on your requirements. request.page_number = "1"
```

5. Obtain a response by using the client object.

```
response, err := client.DescribeEvents(request)
```

6. Use the err syntax to handle errors.

```
if err != nil {
  fmt.Println(err)
  return
```

7. Obtain a response parameter.
The following example shows how to obtain the RequestId parameter.

```
fmt.Println(response.RequestId)
```

Sample code

```java
package main import (
  "fmt"
  cs "github.com/aliyun/alibaba-cloud-sdk-go/services/cs"
```

`)`

```
func main() {
  client, err := cs.NewClientWithAccessKey("cn-hangzhou", "<yourAccessKeyID>", "<yourAccessKeySecret>")
  // Create an API request and configure the parameters.
  request := ecs.CreateDescribeEventsRequest()
  // Specify this parameter based on your requirements.
  request.cluster_id = "test"
  // Specify this parameter based on your requirements.
  request.type = "test"
  // Specify this parameter based on your requirements.
  request.page_size = "1"
  // Specify this parameter based on your requirements.
  request.page_number = "1"
  response, err := client.DescribeEvents(request)
  if err != nil {
    fmt.Println(err)
    return
  // Print response parameters as required. In this example, the RequestId parameter is printed.
  fmt.Println(response.RequestId)
```

## Cluster API list

### Container Service API invocation

2.1.1. Overview To use the APIs provided by Container Service, you can send HTTP requests to the endpoint of Container Service APIs and include specific parameters in the requests. The system returns a response after processing the request.
1. Common parameters
2. Request structure
3. Response parameters
4. Sign API requests
2.1.2. Common parameters This topic lists the common request headers, common response headers, and common parameters that are required in Apsara Stack API (ASAPI) requests when you make Container Service API requests. Common request parameters must be included in all Container Service API requests.

| Parameter | Description | Required |
|---|---|---|
| Authorization | The authentication information that is used to check the authenticity of a request. The string must follow the AccessKeyId:Signature format. | Yes |
| Content-Length | The length of the HTTP request content. This length is specified in RFC 2616. | Yes |
| Content-Type | The type of HTTP request content. This type must follow the format that is specified in RFC 2616. | Yes |
| Content-MD5 | The 128-bit MD5 hash value of the HTTP message body. The hash value is encoded in the Base64 format. We recommend that you set this parameter for all requests to prevent parameter tampering. | Yes |
| Date | The time when a request is created. The time must be in GMT. If the time between when the request is sent and when the request is received exceeds 15 minutes, the request is deemed invalid. | Yes |
| Host | The host to which the request is sent, for example, diku.aliyuncs.com. | Yes |
| Accept | The type of response that is required by the client. Valid values: application/json and application/xml. | Yes |
| x-acs-version | The version number of the API. Set the value to 2015-12- 15. | Yes |
| x-acs-region-id | The region where the Elastic Compute Service (ECS) instance is deployed. | Yes |
| x-acs-signature-nonce | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. | Yes |
| x-acs-signature-method | The encryption method of the signature string. Set the value to HMAC-SHA1. | Yes |

```
GET /clusters HTTP/1.1 Host: cs.aliyuncs.com Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: f63659d4-10ac-483b-99da-ea8fde61eae3 Authorization: acs <yourAccessKeyId>:<yourSignature> x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 11:18:47 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Content-Length: 0
```

Common parameters required in ASAPI requests Additional common parameters are required when you make ASAPI requests. The following table lists these common parameters.

| Parameter | Description | Required |
|---|---|---|
| x-ascm-product-ak | The AccessKey pair. You can check your AccessKey pair in the Alibaba Cloud Management Console. | Yes |
| x-ascm-product-name | The name of the service that supports the API. Set the value to cs for Container Service. | Yes |
| x-ascm-product-version | The version number of the API. Set the value to 2015-12- 15. | Yes |
| x-acs-regionid | The ID of the region where the Container Service cluster is deployed. | Yes |
| x-acs-organizationid | The ID of the organization to which the Container Service cluster belongs. | Yes |
| x-acs-resourceGroupId | The ID of the resource set of the Container Service cluster. | Yes |
| x-acs-roleid | The ID of the role. | Yes |

Common response parameters Every response returns a unique request ID regardless of whether the call is successful. XML format:

```json
<? xml version="1.0" encoding="UTF-8"? > <!—Result Root Node--> <Interface Name + Response>
 | <! -Returned Request Tag -->
 | <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
 | <! -Return Result Data -->
<Interface Name+Response>
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
    /* Return Result Data */
```

2.1.3. Request syntax This topic describes the syntax that you must follow when you make Container Service API requests. Endpoint The endpoints of the API operations are classified into the following types:

| cs.${global:internet-domain} |   |   |
|---|---|---|
| on: | cs.${global:region}.${global:internet-domain} |   |

You must add the /roa prefix to the endpoint that you use to make an Apsara Stack API (ASAPI) request. For example, if the /clusters endpoint is used to create a cluster, you must include /roa/clusters in your ASAPI request. Protocols HTTP and HTTPS are supported. We recommend that you send requests over HTTPS to enhance security. Request methods The following HTTP methods are supported: PUT, POST, GET, and DELETE. Each request must contain common request parameters and parameters unique to specific operations. Request encoding All requests and responses are encoded in the UTF-8 format. 2.1.4. Response parameters The response data is returned in a unified format. If status code `2xx` is returned, it indicates that the API call is successful. If status code `4xx` or `5xx` is returned, it indicates that the API call has failed. For successful API calls, response data is returned in XML or JSON format. You can pass a parameter to specify the format when you call the API. The default format is XML. The following example is formatted for readability. The actual result is not formatted with line feeds or indentation. 2.1.5. Sign API requests This topic describes how to sign API requests to protect Container Service from unauthorized access. Introduction Apsara Stack issues an AccessKey pair to each Apsara Stack tenant account. Each AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. You can obtain and manage the AccessKey pair in the Apsara Uni-manager Management Console. Container Service verifies every request it receives. All requests to Container Service must contain signature information. Container Service implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. Container Service accepts only requests that are validated by verification codes. Invalid requests are rejected and the HTTP status code 403 is returned. You can add the Authorization header to every HTTP request and include the signature in the header. You must add the signature to the Authorization header in the following format: `Authorization: acs [Access Key Id]:[Signature]` .

| The | Signature | is calculated based on the following rules: |
|---|---|---|
| Signature = base64(hmac-sha1(VERB + "\n" + ACCEPT + "\n" + Content-MD5 + "\n" + Content-Type + "\n" + Date + "\n" + CanonicalizedHeaders + "\n" + CanonicalizedResource)) |   |   |

`VERB` indicates the HTTP method. Example: `PUT` . `ACCEPT` specifies the type of response that is required by the client. Valid values: application/json and application/xml.

| Content-MD5 |   |
|---|---|
| Content-Type |   |
| Date | indicate |

`Content-MD5` indicates the MD5 hash value of the request content. `Content-Type` indicates the type of request content. `Date` indicates the time when the request was sent. This parameter is required. The time must be in GMT. If the time between when the request was sent and when the request was received exceeds 15 minutes, the request is deemed invalid and the HTTP status code 400 is returned. For example, `Thu, 17 Mar 2012 18:49:` `58 GMT` can be used.

| x-acs- |   |
|---|---|
|   | /clusters? name=my-clusters&resource=new |

`CanonicalizedHeaders` indicates the header fields that are prefixed with `x-acs-` in the request.

|   | CanonicalizedResource |   |
|---|---|---|
| CanonicalizedHeaders |   | (he |

`CanonicalizedResource` indicates the URI of the requested resource. For example, /clusters? name=my-clusters&resource=new can be used. `CanonicalizedHeaders` (headers that start with `x-acs-` ) must comply with the following specifications before the signature is verified:
1. Convert the names of all HTTP request headers prefixed with `x-acs-` to lowercase letters. For example, you must convert `X-ACS-Meta-Name: TaoBao` into `x-`
`acs-meta-name: TaoBao` . Header field names are case-insensitive. We recommend that you use lowercase letters.

| \t , | \n , | \r |
|---|---|---|

2. If a header field value is too long, replace specific delimiters with spaces. The delimiters include \t , \n , \r , and \f .
3. Sort all HTTP request headers that are obtained from the preceding step in alphabetical order.
4. Delete spaces from each side of a delimiter between the request header and its content. For example, convert `x-acs-meta-name: TaoBao,Alipay` into `x-acs-me`

```
ta-name:TaoBao,Alipay .
```

| 5. Separate all headers and content with delimiters ( | \n ) | to form the final canonicalized headers. |
|---|---|---|
| Not e CanonicalizedResource must follow this format: CanonicalizedResource specifies the URIs of the requested resources. You must sort sub- resources in alphabetical order and combine them with the & delimiter to form a string. In the following example, the string that follows the question mark ( ? ) indicates CanonicalizedResource. |   |   |

|   | CanonicalizedResource |
|---|---|
| & |   |

```
http://cs.aliyuncs.com/clusters?name=my-clusters&resource=new
```

| The value of | CanonicalizedResource | must be in the following format: |
|---|---|---|
| /clusters? name=my-clusters&resource=new |   |   |

Overview The following example shows how to sign an API request. The `access_key_id` and `access_key_secret` fields separately specify the AccessKey ID and AccessKey secret that are used in the example. We recommend that you use your own program to construct an API request. You can then calculate the signature that is used in the following example. Sample request:

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708****","size": 1,"network_mode": "vpc","data_disk_category": "c loud","data_disk_size": 10,"ecs_image_id": "m-253l****l"}
```

Const ruct t he request Calculate the values of `Content-Length` and `Content-MD5` .

| Content-Length | specifies the length of the content body. |
|---|---|
| Not e The body cannot start with a space or line feed. |   |

```
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708****","size": 1,"network_mode": "vpc","data_disk_categor y": "cloud","data_disk_size": 10,"ecs_image_id": "m-253ll****"} Content-Length: 210
```

| Content-MD5 | : The MD5 value is calculated based on the following rules: |
|---|---|
| body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708****","size": 1,"network_mode": "vpc","data_disk_categor y": "cloud","data_disk_size": 10,"ecs_image_id": "m-253ll****"} # Calculate the MD5 value of the body md5(body): e94e002cc90a4a3d0f61b790487aa098 # Convert the MD5 hash value into a byte array. Convert every two hexadecimal digits into one byte. # Example: e9 -> 11111111111111111111111111101001 -> -23 bytes(md5(body)): {[-23], [78], [0], [44], [-55], [10], [74], [61], [15], [97], [-73], [-112], [72], [122], [-96], [-104]} # Convert the byte array into a string that is encoded in the Base64 format. base64(bytes(md5(body))): 6U4ALMkKSj0PYbeQSHqgmA== Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== |   |

| Process | CanonicalizedHeaders |   |
|---|---|---|
| # List all header fields prefixed with 'x-acs-' x-acs-version: 2015-12-15 x-acs-signature-nonce: ca480402-7689-43ba-acc4-4d2013d9d8d4 x-acs-signature-version: 1.0 x-acs-signature-method: HMAC-SHA1 X-Acs-Region-Id: cn-beijing # Convert the header field name to lowercase, delete the spaces at the start and end of each line, and sort the header fields in lexicographical orde r. Delete spaces from each side of a delimiter between the request header and its content. # Note: No line feed in the last line. x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15 |   |   |

Calculate `CanonicalizedResource` In this example, the length of the `CanonicalizedResource` field value is 27 bytes. Not e A line feed \n exists at the end of the first line.

```
/clusters? param1=value1&param2=value2
```

| Signature |   |
|---|---|
| the value of | SignatureString |

Construct the value of `SignatureString` . In this example, the length of the signature string is 307 bytes. Apart from the last line, each line has a line feed \n at the end.

```
POST application/json 6U4ALMkKSj0PYbeQSHqgmA== application/json;charset=utf-8 Wed, 16 Dec 2015 12:20:18 GMT x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15 /clusters? param1=value1&param2=value2
```

| Calculate | Signature | base on the following rules: |
|---|---|---|
| # Use the AccessKey secret to encrypt the value of SignatureString. In this example, access_key_secret specifies the AccessKey secret. hmac-sha1(SignatureString): fee03d405e421ebaf514adec881038c4b313584d # Convert the encrypted string into a byte array, which is similar to calculating Content-MD5. # Convert the byte array into a string that is encoded in the Base64 format. The output is the signature string. base64(bytes(hmac-sha1(SignatureString))): ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEzNTg0ZA== Signature: ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEzNTg0ZA== |   |   |

The signature string is calculated. Add other header fields to your request and set the value of Signature to the calculated signature string. The following sample code shows the signed API request.

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708****","size": 1,"network_mode": "vpc","data_disk_category": "c loud","data_disk_size": 10,"ecs_image_id": "m-253ll****"}
```

### Clusters

2.2.1. Create a Container Service cluster You can call the CreateCluster operation to create a dedicated Kubernetes cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| cluster_type | String | Body | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster. |
| name | String |   | No | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| region_id | String | Body | No | cn-beijing | The ID of the region in which you want to deploy the cluster. |
| disable_rollback | Boolean | Body | No | true | Specifies whether to perform a rollback when the cluster fails to be created. Valid values: true : performs a rollback if the system fails to create the cluster false : does not perform a rollback if the system fails to create the cluster Default value: true |
| timeout_mins | Long | Body | No | 60 | Specifies the timeout period of cluster creation. Unit: minutes. Default value: 60 . |
| kubernetes_version | String | Body | No | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. The Kubernetes versions supported by Container Service are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not set this parameter, the latest Kubernetes version is used. You can create clusters of the latest two Kubernetes versions in the Container Service console. You can create clusters of earlier Kubernetes versions by calling API operations. |

| Parameter | Type | Position | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| snat_entry | Boolean | Body | No | true | Specifies whether to configure SNAT rules for the virtual private cloud (VPC) where your cluster is deployed. Valid values: true : automatically creates a NAT gateway and configures SNAT rules. Set this parameter to true if nodes and applications in the cluster need to access the Internet. false: does not create a NAT gateway or config |   |   |
|   |   |   |   |   |   | false: does not create a NAT gateway or config |   |
|   |   |   |   |   | ure SNAT rules. In this case, nodes and applications in the cluster cannot access the Internet. Default value: true |   |   |
| endpoint_public_access | Boolean | Body | No | true | Specifies whether to enable Internet access for the cluster. You can use an elastic IP address (EIP) to expose the API server. This way, you can access the cluster over the Internet. true : enables Internet access. false : disables Internet access. If you set this parameter to false, the API server cannot be accessed over the Internet. Default value: false |   |   |
| ssh_flags | Boolean | Body | No | true | Specifies whether to enable SSH logon over the Internet. true : enables SSH logon over the Internet. false : disables SSH logon over the Internet. Default value: false |   |   |
| cloud_monitor_flags | Boolean | Body | No | true | Specifies whether to install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent. false : does not install the CloudMonitor agent. Default value: false |   |   |
| deletion_protection | Boolean | Body | No | true | Specifies whether to enable deletion protection for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values: true : enables deletion protection for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations. false : disables deletion protection for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations. Default value: false |   |   |
| node_cidr_mask | String | Body | No | 26 | The maximum number of IP addresses that can be assigned to nodes. This number is determined by the node CIDR block. This parameter takes effect only if the cluster uses Flannel as the network plug-in. Default value: 26 |   |   |
| user_ca | String | Body | No | -----BEGIN CERTIFICATE----- **** | The custom Certificate Authority (CA) certificate used by the cluster. |   |   |
| proxy_mode | String | Body | No | ipvs | The kube-proxy mode. iptables is a kube-proxy mode. It uses iptables rules to conduct Service discovery and load balancing. The performance of this mode is limited by the size of the cluster. This mode is suitable for clusters that run a small number of Services. IPVS is a high-performance kube-proxy mode. It uses Linux IP Virtual Server (IPVS) to conduct Service discovery and load balancing. This mode is suitable for clusters that run a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required. Default value: ipvs . |   |   |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| tags.N.key | String | Body | No | key | The key of the label. |
| tags.N.value | String | Body | No | value | The value of the label. |
| addons.N.name | String | Body | No | nginx-ingress-controller | The name of the plug-in. |
| addons.N.config | String | Body | No | {\"IngressSlbNetworkType\ ":\"internet\"} | The component configurations. |
| addons.N.disabled | Boolean | Body | No | false | Specifies whether to disable automatic installation. true : disables automatic installation. false : enables automatic installation. |
| os_type | String | Body | No | Linux | The type of the node OS. Valid values: Windows Linux Default value: Linux |
| platform | String | Body | No | CentOS | The OS distribution that you want to use. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| user_data | String | Body | No | IyEvdXNyL2Jpbi9iYXNoCmVj aG8gIkhlbGxvIEFD**** | The user-defined data of the node. For more information, see the User-defined data chapter in the Elastic Compute Service (ECS) documentation. |
| node_port_range | String | Body | No | 30000~32767 | The node port range. Valid values: 30000 to 65535. Default value: 30000~32767 . |
| login_password | String | Body | No | Hello@1234 | The password for SSH logon. You must set this parameter or the key_pair parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
| cpu_policy | String | Body | No | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. Default value: none |
| taints.N.effect | String | Body | No | key | The key of a taint. |
| taints.N.key | String | Body | No | value | The value of a taint. |
| taints.N.value | String | Body | No | NoSchedule | The effect of the taint. |
| master_count | Long | Body | No | 3 | The number of master nodes. Set the value to 3 . Default value: 3 . |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| master_system_disk_categ ory | String | Body | No | cloud_ssd | The type of system disk that you want to use for the master nodes. Valid values: cloud_efficiency : ultra disk cloud_ssd : standard SSD cloud_essd : enhanced SSD (ESSD) |
| master_system_disk_size | Long | Body | No | 120 | The size of the system disk that you want to use for master nodes. Valid values: 40 to 500. Unit: GiB. Default value: 120 . |
| master_system_disk_snaps hot_policy_id | String | Body | No | sp-2zej1nogjvovnz4z**** | The automatic snapshot policy of master nodes. |
| master_system_disk_perfor mance_level | String | Body | No | PL1 | The performance level (PL) of the system disk that you want to use for master nodes. This parameter takes effect only for ESSDs. |
| num_of_nodes | Long | Body | No | 3 | The number of worker nodes. Valid values: 0 to 100. |
| worker_system_disk_catego ry | String | Body | No | cloud_efficiency | The type of system disk that is specified for worker nodes. Valid values: cloud_efficiency : ultra disk cloud_ssd : standard SSD Default value: cloud_ssd |
| worker_system_disk_size | Long | Body | No | 120 | The size of the system disk that is specified for worker nodes. Unit: GiB. Valid values: 40 to 500. The value of this parameter must be equal to or larger than the larger value between 40 and the size of the OS image. Default value: 120. |
| worker_system_disk_snapsh ot_policy_id | String | Body | No | sp-2zej1nogjvovnz4z**** | The automatic snapshot policy of worker nodes. |
| worker_system_disk_perfor mance_level | String | Body | No | PL1 | The PL of the system disk that you want to use for worker nodes. This parameter takes effect only for ESSDs. |
| worker_data_disks.N.auto_s napshot_policy_id | String | Body | No | sp-2zej1nogjvovnz4z**** | The ID of the automatic snapshot policy of worker nodes. |
| worker_data_disks.N.categ ory | String | Body | No | cloud_essd | The data disk type of worker nodes. |
| worker_data_disks.N.encryp ted | String | Body | No | true | Specifies whether to encrypt the data disks of worker nodes. |
| worker_data_disks.N.perfor mance_level | String | Body | No | PL1 | The PL of the system disk that you want to use for worker nodes. This parameter takes effect only for ESSDs. |
| worker_data_disks.N.size | Long | Body | No | 120 | The data disk size of worker nodes. |
| vpcid | String | Body | No | vpc-2zeik9h3ahvv2zz95**** | The virtual private cloud (VPC) in which you want to deploy the cluster. You must specify a VPC when you create the cluster. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| is_enterprise_security_grou p | Boolean | Body | No | true | Specifies whether to create an advanced security group. This parameter takes effect only if security_group_id is left empty. Not e To use a basic security group, make sure that the sum of the number of nodes in the cluster and the number of pods that use Terway does not exceed 2,000. Therefore, we recommend that you specify an advanced security group for a cluster that uses Terway as the network plug-in. true : creates an advanced security group false : does not create an advanced security group Default value: true |
| container_cidr | String | Body | No | 172.20.0.0/16 | The CIDR block of pods. This CIDR block cannot overlap with the CIDR block of the virtual private cloud (VPC) in which the cluster is deployed. If the VPC is automatically created by the system, the default CIDR block of pods is 172.16.0.0/16. Not e This parameter is required if the cluster uses Flannel as the network plug-in. This parameter is optional if the cluster uses Terway as the network plug-in. |
| service_cidr | String | Body | No | 172.21.0.0/20 | The CIDR block of Services. Valid values: 10.0.0.0/16-24, 172.16-31.0.0/16-24, and 192.168.0.0/16-24. The CIDR block of Services cannot overlap with the CIDR block of the VPC (10.1.0.0/21) or the CIDR blocks of existing clusters in the VPC. You cannot modify the CIDR block of Services after the cluster is created. By default, the CIDR block of Services is set to 172.19.0.0/20. |
| resource_group_id | String | Body | No | rg-acfm3mkrure**** | The ID of the resource group. |
| image_id | String | Body | No | m-bp16z7xko3vvv8gt**** | Specifies a custom image for nodes. By default, the system image is used. You can select a custom image to replace the default image. |
| cluster_domain | String | Body | No | cluster.local | The domain name of the cluster. The domain name can contain one or more parts that are separated by periods (.). Each part cannot exceed 63 characters in length, and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit. |
| profile | String | Body | No | Default | The profile of the cluster. Valid values: Default : dedicated Kubernetes cluster Edge : dedicated edge Kubernetes cluster |
| master_vswitch_ids | List<String> | Body | No | ["vsw- 2ze3ds0mdip0hdz8i****"] | The IDs of vSwitches. |
| master_instance_types | List<String> | Body | No | ["ecs.n4.xlarge"] | The ECS instance types of master nodes. For more information, see the Instance types chapter of ECS User Guide. |
| worker_vswitch_ids | List<String> | Body | No | ["vsw- 2ze3ds0mdip0hdz8i****"] | The IDs of vSwitches. You can specify 1 to 20 vSwitches. We recommend that you select vSwitches in different zones to ensure high availability. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| worker_instance_types | List<String> | Body | No | ["ecs.n4.large"] | The instance types of worker nodes. You must specify at least one instance type. For more information, see the Instance types chapter of ECS User Guide. Not e The instance types are listed in descending order of priority. If the system fails to create worker nodes based on the instance type of the highest priority, the system attempts to create worker nodes by using the instance type of the next highest priority. |
| pod_vswitch_ids | List<String> | Body | No | ["vsw- 2vc9mwkxbvudp25do****"] | The vSwitches that are used by pods. This parameter is required if you choose Terway as the network plug-in for the cluster. |
| runtime | Struct | Body | No | {"name": "docker", "version": "19.03.5"} | The container runtime of the cluster. The following runtimes are supported: containerd , Docker , and Sandboxed-Container . The default runtime is Docker . You must specify the name and version of the container runtime: name : the name of the container runtime. version : the version of the container runtime |
| name | String |   | No | docker | The name of the container runtime. |
| version | String |   | No | version 19.03.15 | The version of the container runtime. |

| containerd , | Docker |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster_id | String | cb95aa626a47740afbf6aa099b650* *** | The ID of the cluster. |
| request_id | String | 687C5BAA-D103-4993-884B- C35E4314A1E1 | The ID of the request. |
| task_id | String | T-5a54309c80282e39ea00002f | The ID of the export task. |

```json
POST /clusters HTTP/1.1 Common request header
    "cluster\_type": "Kubernetes",
    "container\_cidr": "172.20.0.0/16",
    "instances": i-2ze4zxnm36vq00xn****,
    "login\_password": "Hello@1234",
    "master\_instance\_types": ["ecs.n4.xlarge"],
    "master\_system\_disk\_category": "cloud_ssd",
    "master\_system\_disk\_size": "120",
    "master\_vswitch\_ids": vsw-2ze3ds0mdip0hdz8i****,
    "name": "cluster-demo",
    "num\_of\_nodes": "3",
    "region\_id": "cn-beijing",
    "service\_cidr": "172.21.0.0/20",
    "vpcid": "vpc-2zeik9h3ahvv2zz95****",
    "worker\_instance\_types": ["ecs.n4.large"],
    "worker\_system\_disk\_category": "cloud_efficiency",
    "worker\_system\_disk\_size": "120",
    "worker\_vswitch\_ids": vsw-2ze3ds0mdip0hdz8i****
```

| XML | format |
|---|---|
| <cluster_id>cb95aa626a47740afbf6aa099b650****</cluster_id> <task_id>T-5a54309c80282e39ea00002f</task_id> <request_id>687C5BAA-D103-4993-884B-C35E4314A1E1</request_id> |   |

```json
    "cluster_id": "cb95aa626a47740afbf6aa099b650****",
    "task_id": "T-5a54309c80282e39ea00002f",
    "request_id": "687C5BAA-D103-4993-884B-C35E4314A1E1"
```

2.2.2. Delete a cluster You can call the DeleteCluster operation to delete a cluster by ID and release all nodes in the cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /clusters/[ClusterId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c905d1364c2dd4b6284a3f4 1790c4**** | The ID of the cluster. |
| retain_all_resources | Boolean | Query | No | false | Specifies whether to retain all resources. If you set the parameter to true , the retain_resources parameter is ignored. true : retains all resources. false : does not retain all resources. Default value: false |
| keep_slb | Boolean | Query | No | false | Specifies whether to retain the Server Load Balancer (SLB) instances that are created by the cluster. true : retains the SLB instances that are created by the cluster. false : does not retain the SLB instances that are created by the cluster. Default value: false |
| retain_resources | List<String> | Query | No | ["sg- 2ze6ess9kho6fdn9****"] | The name of the resource. |

```json
DELETE /clusters/[ClusterId] HTTP/1.1
    "ClusterId": "c905d1364c2dd4b6284a3f41790c4****"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.2.3. Query the kubeconfig file of a cluster You can call the DescribeClusterUserKubeconfig operation to query the kubeconfig file of a cluster. The kubeconfig file contains the details of the current user and is used to configure access to the cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /k8s/[ClusterId]/user_config HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c5b5e80b0b64a4bf6939d2d 8fbbc5**** | The ID of the cluster. |
| PrivateIpAddress | Boolean | Query | No | true | Specifies whether to obtain the credential that is used to connect to the cluster over the internal network. Valid values: true : obtains the credential that is used to connect to the cluster over the internal network. false : obtains the credential that is used to connect to the cluster over the Internet. Default value: false |
| TemporaryDurationMinutes | Long | Query | No | 15 | The validity period of a temporary kubeconfig file. Unit: minutes. Valid values: 15 to 4320. If you specify this parameter, the returned kubeconfig file is valid within the specified time period and will expire at the time specified by expiration in the response. If you do not specify this parameter, the returned kubeconfig file is permanently valid. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| config | String | apiVersion: v1**** | The content of the kubeconfig file. |
| expiration | String | 2024-03-10T09:56:17Z | The expiration time of the kubeconfig file. The value is the UTC time displayed in RFC3339 format. |

```json
GET /k8s/[ClusterId]/user_config HTTP/1.1
    "ClusterId": "c5b5e80b0b64a4bf6939d2d8fbbc5****"
```

| XML | format |
|---|---|
| <expiration>2024-03-10T09:56:17Z</expiration> <config>apiVersion: v1****</config> |   |

| JSON | format |
|---|---|
| { "expiration": "2024-03-10T09:56:17Z", "config": "apiVersion: v1****" } |   |

2.2.4. Query 2.2.4.1. Query information about all clusters You can call the DescribeClustersV1 operation to query information about all clusters. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /api/v1/clusters HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| name | String | Query | No | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| cluster_type | String | Query | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster |
| page_size | Long | Query | No | 10 | The number of entries to return on each page. |
| page_number | Long | Query | No | 3 | The number of the page to return. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| clusters | Array of cluster |   | The details of clusters. |
| Department | Integer | 3 | The ID of the organization or department to which the cluster belongs. |
| DepartmentName | String | acs-test | The name of the organization or department to which the cluster belongs. |
| RMRegionId | String | cn-wl-env115-d01 | The ID of the region in which the cluster is deployed. |
| RegionId | String | cn-beijing | The ID of the region where the cluster is deployed. |
| ResourceGroup | Integer | 58 | The ID of the resource set. |
| ResourceGroupName | String | acr-test | The name of the resource set. |
| cluster_id | String | c3fb96524f9274b4495df0f12a6b5* *** | The ID of the cluster. |
| cluster_type | String | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster |
| created | String | 2020-08-20T10:51:29+08:00 | The time when the cluster was created. |
| current_version | String | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. |
| deletion_protection | Boolean | true | Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values: true : deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations. false : deletion protection is disabled for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations. |
| docker_version | String | 19.03.5 | The Docker version that is used by the cluster. |
| external_loadbalancer_id | String | lb-2vcrbmlevo6kjpgch**** | The ID of the Server Load Balancer (SLB) instance that is used for the Ingress of the cluster. The default SLB specification is slb.s1.small, which belongs to the high- performance instance type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| init_version | String | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. The Kubernetes versions supported by Container Service are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not set this parameter, the latest Kubernetes version is used. You can create clusters of the latest two Kubernetes versions in the Container Service console. You can create clusters of earlier Kubernetes versions by calling API operations. |
| maintenance_window | Struct |   | The maintenance window of the cluster. |
| duration | String | 3h | The duration of the cluster maintenance window. The duration ranges from 1 hour to 24 hours. Unit: hours. Default value: 3h. |
| enable | Boolean | false | Indicates whether the cluster maintenance window is enabled. Default value: false |
| maintenance_time | String | 03:00:00Z | The start time of the cluster maintenance window. The value must be in the standard Golang time format. Example: 15:04:05Z. |
| weekly_period | String | Monday,Thursday | The maintenance cycle. Valid values: Monday to Sunday. Separate multiple values with commas (,). Default value: Thursday. |
| master_url | String | {\"api_server_endpoint\":\"\",\"intr anet_api_server_endpoint\":\"http s://192.168.0.251:6443\"} | The endpoint of the cluster API server, including an internal endpoint and a public endpoint. |
| meta_data | String | {\"api_server_endpoint\":\"\",\"intr anet_api_server_endpoint\":\"http s://192.168.0.251:6443\"} | The metadata of the cluster. |
| name | String | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| network_mode | String | vpc | The network mode of the cluster. Valid values: classic : classic network vpc : virtual private cloud (VPC) overlay : overlay network calico : network powered by Calico |
| next_version | String | 1.18.8-aliyun.1 | The Kubernetes version to which the cluster can be updated. |
| private_zone | Boolean | false | Indicates whether Alibaba Cloud DNS PrivateZone is enabled. Valid values: true : Alibaba Cloud DNS PrivateZone is enabled. false : Alibaba Cloud DNS PrivateZone is disabled. |
| profile | String | Default | The identifier of the cluster. Valid values: Edge : The cluster is a managed edge Kubernetes cluster. Default : The cluster is not a managed edge Kubernetes cluster. |
| region_id | String | cn-beijing | The ID of the region where the cluster is deployed. |
| resource_group_id | String | rg-acfmyvw3wjm**** | The ID of the resource group to which the cluster belongs. |
| security_group_id | String | sg-2vcgwsrwgt5mp0yi**** | The ID of the security group to which the instances of the cluster belong. |
| size | Integer | 5 | The number of nodes in the cluster. Master nodes and worker nodes are included. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| state | String | running | The status of the cluster. Valid values: initial : The cluster is being created. failed : The cluster failed to be created. running : The cluster is running. updating : The cluster is being updated. updating_failed : The cluster failed to be updated. scaling : The cluster is being scaled. stopped : The cluster is stopped. deleting : The cluster is being deleted. deleted : The cluster is deleted. delete_failed : The cluster failed to be deleted. |
| subnet_cidr | String | 172.21.0.0/16 | The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets: 10.0.0.0/8 172.16-31.0.0/12-16 192.168.0.0/16 The CIDR block of pods cannot overlap with the CIDR block of the VPC in which the cluster is deployed and the CIDR blocks of existing clusters in the VPC. You cannot modify the pod CIDR block after the cluster is created. |
| tags | Array of tag |   | The labels of the cluster. |
| key | String | tier | The key of a label. |
| value | String | backend | The value of a label. |
| updated | String | 2020-09-16T11:09:55+08:00 | The time when the cluster was updated. |
| vpc_id | String | vpc-2vcg932hsxsxuqbgl**** | The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster. |
| vswitch_id | String | vsw-2vc41xuumx5z2rdma****,vsw- 2vc41xuumx5z2rdma**** | The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability. |
| worker_ram_role_name | String | KubernetesWorkerRole-ec87d15b- edca-4302-933f-c8a16bf0**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on Elastic Compute Service (ECS) instances. |
| zone_id | String | cn-beijing-b | The ID of the zone where the cluster is deployed. |
| page_info | Struct |   | The pagination details. |
| page_number | Integer | 3 | The page number of the returned page. |
| page_size | Integer | 20 | The number of entries returned per page. |
| total_count | Integer | 50 | The total number of entries returned. |

```
GET /api/v1/clusters HTTP/1.1
```

`XML` format

```xml
<page_info>
    <page_number>3</page_number>
    <total_count>50</total_count>
    <page_size>20</page_size>
</page_info> <clusters>
    <private_zone>false</private_zone>
    <resource_group_id>rg-acfmyvw3wjm****</resource_group_id>
    <vpc_id>vpc-2vcg932hsxsxuqbgl****</vpc_id>
    <network_mode>vpc</network_mode>
    <security_group_id>sg-2vcgwsrwgt5mp0yi****</security_group_id>
    <cluster_type>Kubernetes</cluster_type>
    <docker_version>19.03.5</docker_version>
    <next_version>1.18.8-aliyun.1</next_version>
    <zone_id>cn-beijing-b</zone_id>
    <Department>3</Department>
    <cluster_id>c3fb96524f9274b4495df0f12a6b5****</cluster_id>
    <external_loadbalancer_id>lb-2vcrbmlevo6kjpgch****</external_loadbalancer_id>
    <vswitch_id>vsw-2vc41xuumx5z2rdma****,vsw-2vc41xuumx5z2rdma****</vswitch_id>
    <meta_data>{\"api_server_endpoint\":\"\",\"intranet_api_server_endpoint\":\"https://192.168.0.251:6443\"}</meta_data>
    <RMRegionId>cn-wl-env115-d01</RMRegionId>
    <state>running</state>
    <ResourceGroup>58</ResourceGroup>
    <init_version>1.16.9-aliyun.1</init_version>
    <deletion_protection>true</deletion_protection>
    <created>2020-08-20T10:51:29+08:00</created>
    <profile>Default</profile>
    <subnet_cidr>172.21.0.0/16</subnet_cidr>
    <master_url>{\"api_server_endpoint\":\"\",\"intranet_api_server_endpoint\":\"https://192.168.0.251:6443\"}</master_url>
    <region_id>cn-beijing</region_id>
    <current_version>1.16.9-aliyun.1</current_version>
    <size>5</size>
    <name>cluster-demo</name>
    <DepartmentName>acs-test</DepartmentName>
    <RegionId>cn-beijing</RegionId>
    <worker_ram_role_name>KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****</worker_ram_role_name>
    <updated>2020-09-16T11:09:55+08:00</updated>
    <ResourceGroupName>acr-test</ResourceGroupName>
    <tags>
        <value>backend</value>
        <key>tier</key>
    </tags>
    <maintenance_window>
        <duration>3h</duration>
        <weekly_period>Monday,Thursday</weekly_period>
        <enable>false</enable>
        <maintenance_time>03:00:00Z</maintenance_time>
    </maintenance_window>
</clusters>
```

```json
    "page_info": {
        "page_number": 3,
        "total_count": 50,
        "page_size": 20
```

`},`

```json
    "clusters": {
        "private_zone": false,
        "resource_group_id": "rg-acfmyvw3wjm****",
        "vpc_id": "vpc-2vcg932hsxsxuqbgl****",
        "network_mode": "vpc",
        "security_group_id": "sg-2vcgwsrwgt5mp0yi****",
        "cluster_type": "Kubernetes",
        "docker_version": "19.03.5",
        "next_version": "1.18.8-aliyun.1",
        "zone_id": "cn-beijing-b",
        "Department": 3,
        "cluster_id": "c3fb96524f9274b4495df0f12a6b5****",
        "external_loadbalancer_id": "lb-2vcrbmlevo6kjpgch****",
        "vswitch_id": "vsw-2vc41xuumx5z2rdma****,vsw-2vc41xuumx5z2rdma****",
        "meta_data": "{\\\"api_server_endpoint\\\":\\\"\\\",\\\"intranet_api_server_endpoint\\\":\\\"https://192.168.0.251:6443\\\"}",
        "RMRegionId": "cn-wl-env115-d01",
        "state": "running",
        "ResourceGroup": 58,
        "init_version": "1.16.9-aliyun.1",
        "deletion_protection": true,
        "created": "2020-08-20T10:51:29+08:00",
        "profile": "Default",
        "subnet_cidr": "172.21.0.0/16",
        "master_url": "{\\\"api_server_endpoint\\\":\\\"\\\",\\\"intranet_api_server_endpoint\\\":\\\"https://192.168.0.251:6443\\\"}",
        "region_id": "cn-beijing",
        "current_version": "1.16.9-aliyun.1",
        "size": 5,
        "name": "cluster-demo",
        "DepartmentName": "acs-test",
        "RegionId": "cn-beijing",
        "worker_ram_role_name": "KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****",
        "updated": "2020-09-16T11:09:55+08:00",
        "ResourceGroupName": "acr-test",
        "tags": {
            "value": "backend",
            "key": "tier"
```

`},`

```json
        "maintenance_window": {
            "duration": "3h",
            "weekly_period": "Monday,Thursday",
            "enable": false,
            "maintenance_time": "03:00:00Z"
```

2.2.4.2. Query the information about a cluster You can call the DescribeClusterDetail operation to query the information about a cluster by the cluster ID. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cdde1f21ae22e483ebcb068 a6eb7f**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| asapiSuccess | Boolean | true | Indicates whether data is returned as expected from the Apsara Uni- manager Management Console. |
| cluster_id | String | c82e6987e2961451182edacd74faf* *** | The ID of the cluster. |

| Container Service f | or Kubernetes |   | Developer Guide·Cluster API list |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster_type | String | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster. |
| created | String | 2019-11-25T15:50:20+08:00 | The time when the cluster was created. |
| current_version | String | 1.16.6-aliyun.1 | The Kubernetes version of the cluster. |
| deletion_protection | Boolean | true | Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values: true : deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations. false : deletion protection is disabled for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations. |
| docker_version | String | 19.03.5 | The Docker version that is used by the cluster. |
| eagleEyeTraceId | String | 0a73095416412777494927508d004 e | The trace ID. |
| external_loadbalancer_id | String | lb-2zehc05z3b8dwiifh**** | The ID of the Server Load Balancer (SLB) instance that is created for the Ingress of the cluster. |
| init_version | String | 1.16.6-aliyun.1 | The Kubernetes version that is initially used by the cluster. |
| maintenance_window | Struct |   | The maintenance window of the cluster. |
| duration | String | 3h | The duration of the cluster maintenance window. The duration ranges from 1 hour to 24 hours. Unit: hours. Default value: 3h. |
| enable | Boolean | false | Indicates whether the cluster maintenance window is enabled. Default value: false. |
| maintenance_time | String | 03:00:00Z | The start time of the cluster maintenance window. The value must be in the standard Golang time format. Example: 15:04:05Z. |
| weekly_period | String | Monday,Thursday | The maintenance cycle. Valid values: Monday to Sunday. Separate multiple values with commas (,). Default value: Thursday. |
| master_url | String | {\"intranet_api_server_endpoint\":\ "https://192.168.0.251:6443\"***} | The endpoints of the cluster, including an internal endpoint and a public endpoint. |
| meta_data | String | \"Addons\":*** | The metadata of the cluster. |
| name | String | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| network_mode | String | vpc | The network mode of the cluster. Valid values: classic : classic network vpc : virtual private cloud (VPC) overlay : overlay network calico : network powered by Calico Default value: vpc . |
| next_version | String | 1.18.8-aliyun.1 | The Kubernetes version to which the cluster can be upgraded. |
| private_zone | Boolean | false | Indicates whether Alibaba Cloud DNS PrivateZone is enabled. true : Alibaba Cloud DNS PrivateZone is enabled. false : Alibaba Cloud DNS PrivateZone is disabled. |

| Developer Guide·Cl | uster API list |   | Container Service for Kubernetes |
|---|---|---|---|
| Parameter | Type | Example | Description |
| profile | String | Default | Indicates the scenario in which the cluster is used. Valid values: Default : dedicated Kubernetes cluster. Edge : dedicated edge Kubernetes cluster. |
| region_id | String | cn-beijing | The ID of the region in which the cluster is deployed. |
| resource_group_id | String | rg-acfmyvw3wjm**** | The ID of the resource group to which the cluster belongs. |
| security_group_id | String | sg-25yq**** | The ID of the security group to which the instances of the cluster belong. |
| size | Integer | 5 | The number of nodes in the cluster. Master nodes and worker nodes are included. |
| state | String | running | The status of the cluster. Valid values: initial : The cluster is being created. failed : The cluster failed to be created. running : The cluster is running. updating : The cluster is being upgraded. updating_failed : The cluster failed to be upgraded. scaling : The cluster is being scaled. stopped : The cluster is stopped. deleting : The cluster is being deleted. deleted : The cluster is deleted. delete_failed : The cluster failed to be deleted. |
| subnet_cidr | String | 172.20.0.0/16 | The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets: 10.0.0.0/8 172.16-31.0.0/12-16 192.168.0.0/16 The pod CIDR block cannot overlap with the CIDR block of the VPC or the CIDR blocks of the clusters in the VPC. |
| tags | Array of tag |   | The labels of the cluster. |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| updated | String | 2020-01-13T23:01:03+08:00 | The time when the cluster was updated. |
| vpc_id | String | vpc-2zecuu62b9zw7a7qn**** | The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster. |
| vswitch_id | String | vsw-2zete8s4qocqg0mf6****,vsw- 2zete8s4qocqg0mf6**** | The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability. |
| worker_ram_role_name | String | KubernetesWorkerRole-ec87d15b- edca-4302-933f-c8a16bf0**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on Elastic Compute Service (ECS) instances. |
| zone_id | String | cn-beijing-a | The ID of the zone where the cluster is deployed. |

```json
GET /clusters/[ClusterId] HTTP/1.1
    "ClusterId": "cdde1f21ae22e483ebcb068a6eb7f****"
```

| XML | format |
|---|---|
| <private_zone>false</private_zone> <resource_group_id>rg-acfmyvw3wjm****</resource_group_id> <vpc_id>vpc-2zecuu62b9zw7a7qn****</vpc_id> <network_mode>vpc</network_mode> <maintenance_window> <duration>3h</duration> <weekly_period>Monday,Thursday</weekly_period> <enable>false</enable> <maintenance_time>03:00:00Z</maintenance_time> </maintenance_window> <security_group_id>sg-25yq****</security_group_id> <cluster_type>Kubernetes</cluster_type> <docker_version>19.03.5</docker_version> <next_version>1.18.8-aliyun.1</next_version> <zone_id>cn-beijing-a</zone_id> <cluster_id>c82e6987e2961451182edacd74faf****</cluster_id> <external_loadbalancer_id>lb-2zehc05z3b8dwiifh****</external_loadbalancer_id> <vswitch_id>vsw-2zete8s4qocqg0mf6****,vsw-2zete8s4qocqg0mf6****</vswitch_id> <meta_data>\"Addons\":***</meta_data> <state>running</state> <eagleEyeTraceId>0a73095416412777494927508d004e</eagleEyeTraceId> <init_version>1.16.6-aliyun.1</init_version> <asapiSuccess>true</asapiSuccess> <deletion_protection>true</deletion_protection> <created>2019-11-25T15:50:20+08:00</created> <subnet_cidr>172.20.0.0/16</subnet_cidr> <profile>Default</profile> <master_url>{\"intranet_api_server_endpoint\":\"https://192.168.0.251:6443\"***}</master_url> <region_id>cn-beijing</region_id> <current_version>1.16.6-aliyun.1</current_version> <tags> <value>value</value> <key>key</key> </tags> <cluster_spec>ack.standard</cluster_spec> <size>5</size> <name>cluster-demo</name> <worker_ram_role_name>KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****</worker_ram_role_name> <updated>2020-01-13T23:01:03+08:00</updated> |   |

| JSON | format |
|---|---|
| { "private_zone": false, "resource_group_id": "rg-acfmyvw3wjm****", "vpc_id": "vpc-2zecuu62b9zw7a7qn****", "network_mode": "vpc", "maintenance_window": { "duration": "3h", "weekly_period": "Monday,Thursday", "enable": false, "maintenance_time": "03:00:00Z" }, "security_group_id": "sg-25yq****", "cluster_type": "Kubernetes", "docker_version": "19.03.5", "next_version": "1.18.8-aliyun.1", "zone_id": "cn-beijing-a", "cluster_id": "c82e6987e2961451182edacd74faf****", "external_loadbalancer_id": "lb-2zehc05z3b8dwiifh****", "vswitch_id": "vsw-2zete8s4qocqg0mf6****,vsw-2zete8s4qocqg0mf6****", "meta_data": "\\\"Addons\\\":***", "state": "running", "eagleEyeTraceId": "0a73095416412777494927508d004e", "init_version": "1.16.6-aliyun.1", "asapiSuccess": true, "deletion_protection": true, "created": "2019-11-25T15:50:20+08:00", "subnet_cidr": "172.20.0.0/16", "profile": "Default", "master_url": "{\\\"intranet_api_server_endpoint\\\":\\\"https://192.168.0.251:6443\\\"***}", "region_id": "cn-beijing", "current_version": "1.16.6-aliyun.1", "tags": { "value": "value", "key": "key" }, "cluster_spec": "ack.standard", "size": 5, "name": "cluster-demo", "worker_ram_role_name": "KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****", "updated": "2020-01-13T23:01:03+08:00" } |   |

2.2.4.3. Query resources in a cluster You can call the DescribeClusterResources operation to query all resources in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/resources HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cb95aa626a47740afbf6aa0 99b65**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| resources | Array of resource |   | The list of resources in the cluster. |
| auto_create | Integer | 0 | Indicates whether the resource is automatically created by the system. 0 : The resource is automatically created by the system. 1 : The resource is not automatically created by the system. |
| cluster_id | String | cb95aa626a47740afbf6aa099b65** ** | The ID of the cluster. |
| created | String | 2020-09-11T10:11:54+08:00 | The time when the resource was created. |
| dependencies | String | [] | The dependencies of the resource. |
| instance_id | String | lb-wz9poz4r0ymh8u0uf**** | The ID of the resource. |
| resource_info | String | {\"Id\":\"k8s_master_slb\",\"Name \":\"k8s_master_slb\",\"Type\":\" ALIYUN::SLB::LoadBalancer\",\"Sta tus\":\"CREATE_COMPLETE\",\"Stat usReason\":\"state changed\",\"Updated\":\"2020-05- 21T13:25:02\",\"PhysicalId\":\"lb- wz9poz4r0ymh8u0uf****\"} | The information about the resource. |
| resource_type | String | ALIYUN::SLB::LoadBalancer | The type of the resource. |
| state | String | CREATE_COMPLETE | The status of the resource. Valid values: CREATE_COMPLETE : The resource is created. CREATE_FAILED : The resource failed to be created. CREATE_IN_PROGRESS : The resource is being created. DELETE_FAILED : The resource failed to be deleted. DELETE_IN_PROGRESS : The resource is being deleted. ROLLBACK_COMPLETE : The resource is rolled back. ROLLBACK_FAILED : The resource failed to be rolled back. ROLLBACK_IN_PROGRESS : The resource is being rolled back. |

```json
GET /clusters/[ClusterId]/resources HTTP/1.1
    "ClusterId": "cb95aa626a47740afbf6aa099b65****"
```

`XML` format

```xml
<resources>
      <resource_info>{\"Id\":\"k8s_master_slb\",\"Name\":\"k8s_master_slb\",\"Type\":\"ALIYUN::SLB::LoadBalancer\",\"Status\":\"CREATE_COMPLETE\",\"S
tatusReason\":\"state changed\",\"Updated\":\"2020-05-21T13:25:02\",\"PhysicalId\":\"lb-wz9poz4r0ymh8u0uf****\"}</resource_info>
      <cluster_id>cb95aa626a47740afbf6aa099b65****</cluster_id>
      <instance_id>lb-wz9poz4r0ymh8u0uf****</instance_id>
      <created>2020-09-11T10:11:54+08:00</created>
      <resource_type>ALIYUN::SLB::LoadBalancer</resource_type>
      <state>CREATE_COMPLETE</state>
      <auto_create>0</auto_create>
      <dependencies>[]</dependencies>
</resources>
```

| JSON | format |
|---|---|
| { "resources": { "resource_info": "{\\\"Id\\\":\\\"k8s_master_slb\\\",\\\"Name\\\":\\\"k8s_master_slb\\\",\\\"Type\\\":\\\"ALIYUN::SLB::LoadBalancer\\\",\\\"S tatus\\\":\\\"CREATE_COMPLETE\\\",\\\"StatusReason\\\":\\\"state changed\\\",\\\"Updated\\\":\\\"2020-05-21T13:25:02\\\",\\\"PhysicalId\\\":\\\"lb-wz 9poz4r0ymh8u0uf****\\\"}", "cluster_id": "cb95aa626a47740afbf6aa099b65****", "instance_id": "lb-wz9poz4r0ymh8u0uf****", "created": "2020-09-11T10:11:54+08:00", "resource_type": "ALIYUN::SLB::LoadBalancer", "state": "CREATE_COMPLETE", "auto_create": 0, "dependencies": "[]" } } |   |

2.2.4.4. Query the namespaces of a cluster You can call the DescribeClusterNamespaces operation to query the namespaces of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /k8s/[ClusterId]/namespaces HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c68069cade53b4558924a92 4b415f**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| namespaces | List | [“kube-system”] | The name of the namespace. |

```json
GET /k8s/[ClusterId]/namespaces HTTP/1.1
    "ClusterId": "c68069cade53b4558924a924b415f****"
```

| XML | format |
|---|---|
| <namespaces>kube-system</namespaces> |   |

| JSON | format |
|---|---|
| { "namespaces": ["kube-system"] } |   |

2.2.4.5. Query the agent of a cluster You can call the DescribeExternalAgent operation to query the agent configurations of an external cluster that is registered in the Container Service console. You can deploy the agent configurations in an external cluster. This allows you to access the API server of the cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /k8s/[ClusterId]/external/agent/deployment HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f34eb1808d6b 9362c9**** | The ID of the cluster. |
| PrivateIpAddress | String | Query | No | true | Specifies whether to obtain the credential that is used to access the cluster over the internal network. true: obtains the credential that is used to access the cluster over the internal network. false: obtains the credential that is used to access the cluster over the Internet. Default value: false. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| config | String | apiVersion: v1**** | The agent configurations in the YAML format. |

```json
GET /k8s/[ClusterId]/external/agent/deployment HTTP/1.1
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

| XML | format |
|---|---|
| <config>apiVersion: v1****</config> |   |

| JSON | format |
|---|---|
| { "config": "apiVersion: v1****" } |   |

2.2.4.6. Query resource quotas You can call the DescribeUserQuota operation to query resource quotas. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /quota HTTP/1.1
```

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster_nodepool_quota | Long | 10 | The quota of node pools in a Container Service cluster. |
| cluster_quota | Long | 50 | The quota of Container Service clusters for all types. |
| node_quota | Long | 100 | The quota of nodes in a Container Service cluster. |

```
GET /quota HTTP/1.1
```

| XML | format |
|---|---|
| <amk_cluster_quota>20</amk_cluster_quota> <cluster_nodepool_quota>10</cluster_nodepool_quota> <cluster_quota>50</cluster_quota> <node_quota>100</node_quota> |   |

| JSON | format |
|---|---|
| { "amk_cluster_quota": 20, "cluster_nodepool_quota": 10, "cluster_quota": 50, "node_quota": 100 } |   |

2.2.4.7. Query the logs of a cluster You can call the DescribeClusterLogs operation to query the logs of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/logs HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f34eb1808d6b 9362c9**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The log list. |
| ID | Integer | 590749245 | The ID of the log. |
| cluster_id | String | c23421cfa74454bc8b37163fd19af** ** | The ID of the cluster. |
| cluster_log | String | start to update cluster status to CREATE_COMPLETE | The content of the log. |
| created | String | 2020-09-11T10:11:51+08:00 | The time when the log was generated. |
| log_level | String | 0004 | The level of the log. |
| updated | String | 2020-09-11T10:11:51+08:00 | The time when the log was updated. |

```json
GET /clusters/[ClusterId]/logs HTTP/1.1
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

`XML` format

```xml
<data>
      <cluster_id>c23421cfa74454bc8b37163fd19af***</cluster_id>
      <cluster_log>start to update cluster status to CREATE_COMPLETE</cluster_log>
      <created>2020-09-11T10:11:51+08:00</created>
      <log_level>0004</log_level>
      <ID>590749245</ID>
      <updated>2020-09-11T10:11:51+08:00</updated>
</data>
```

| JSON | format |
|---|---|
| { "data": { "cluster_id": "c23421cfa74454bc8b37163fd19af***", "cluster_log": "start to update cluster status to CREATE_COMPLETE", "created": "2020-09-11T10:11:51+08:00", "log_level": 4, "ID": 590749245, "updated": "2020-09-11T10:11:51+08:00" } } |   |

2.2.4.8. Query information about a Kubernetes version supported by Container Service You can call the DescribeKubernetesVersionMetadata operation to query a Kubernetes version supported by Container Service. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /api/v1/metadata/versions HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterType | String | Query | Yes | Kubernetes | The type of cluster. |
| Region | String | Query | Yes | cn-beijing | The region where the cluster is deployed. |
| KubernetesVersion | String | Query | No | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. Example: 1.16.9- aliyun.1. |
| Profile | String | Query | No | Default | The identifier of the cluster. Valid values: Default : dedicated Kubernetes cluster. Edge : dedicated edge Kubernetes cluster. |
| MultiAZ | Boolean | Query | No | false | Specifies whether to query a multi-zone cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The details of the queried Kubernetes version. |
| images | Array of image |   | The OS images of the Elastic Compute Service (ECS) instances. |
| image_category | String | system | The type of the image. Valid values: system : public image self : custom image others : shared image from other Alibaba Cloud accounts marketplace : image from the image market |
| image_id | String | centos_7_7_x64_20G_alibase_20200 426.vhd | The ID of the image. |
| image_name | String | CentOS 7.7 | The name of the image. |

| Container Service f | or Kubernetes |   | Developer Guide·Cluster API list |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| image_type | String | Centos_7_64 | The type of the image. |
| os_type | String | Linux | The type of the node OS. Valid values: Windows and Linux (Default). |
| os_version | String | 7.7 | The version of the OS distribution. |
| platform | String | CentOS | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| meta_data | Struct |   | The metadata of the Kubernetes version. |
| Architecture | String | amd64 | The OS architecture of the cluster. |
| AuditProjectName | String | k8s-log-c9bd1*** | The name of the Log Service project where the cluster audit log is stored. |
| DockerVersion | String | 19.03.15 | The version of the container runtime. |
| NodeNameMode | String | true | The name of the custom node. |
| Platform | String | "CentOS" | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| PodVswitchId | String | vsw-f8zubs2z9x1cjnzk2*** | The pod vSwitch, which is used to assign IP addresses to the pods in the cluster that uses Terway as the network plug-in. |
| ResourceGroupId | String | rg-aekzsmulow2wngq | The ID of the resource group. |
| multi_az | Boolean | false | Indicates whether the queried Kubernetes version supports cross-zone deployment. |
| runtimes | Array of runtime |   | Details of the supported container runtimes. |
| name | String | "docker" | The name of the container runtime. |
| version | String | "19.05.3" | The version of the container runtime. |
| version | String | "1.16.9-aliyun.1" | The Kubernetes version. |

```json
GET /api/v1/metadata/versions HTTP/1.1
    "ClusterType": "Kubernetes",
    "Region": "cn-beijing"
```

| XML | format |
|---|---|
| <data> <multi_az>false</multi_az> <version>"1.16.9-aliyun.1"</version> <images> <image_name>CentOS 7.7</image_name> <image_category>system</image_category> <os_version>7.7</os_version> <os_type>Linux</os_type> <image_id>centos_7_7_x64_20G_alibase_20200426.vhd</image_id> <platform>CentOS</platform> <image_type>Centos_7_64</image_type> </images> <runtimes> <name>"docker"</name> <version>"19.05.3"</version> </runtimes> <meta_data> <DockerVersion>19.03.15</DockerVersion> <Architecture>amd64</Architecture> <Platform>"CentOS"</Platform> <ResourceGroupId>rg-aekzsmulow2wngq </ResourceGroupId> <PodVswitchId>vsw-f8zubs2z9x1cjnzk2***</PodVswitchId> <NodeNameMode>true</NodeNameMode> <AuditProjectName>k8s-log-c9bd1***</AuditProjectName> </meta_data> </data> |   |

| JSON | format |
|---|---|
| { "data": { "multi_az": false, "version": "\"1.16.9-aliyun.1\"", "images": { "image_name": "CentOS 7.7", "image_category": "system", "os_version": 7.7, "os_type": "Linux", "image_id": "centos_7_7_x64_20G_alibase_20200426.vhd", "platform": "CentOS", "image_type": "Centos_7_64" }, "runtimes": { "name": "\"docker\"", "version": "\"19.05.3\"" }, "meta_data": { "DockerVersion": "19.03.15", "Architecture": "amd64", "Platform": "\"CentOS\"", "ResourceGroupId": "rg-aekzsmulow2wngq", "PodVswitchId": "vsw-f8zubs2z9x1cjnzk2***", "NodeNameMode": true, "AuditProjectName": "k8s-log-c9bd1***" } } } |   |

2.2.5. Modify 2.2.5.1. Modify cluster configurations You can call the ModifyCluster operation to modify the configurations of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /api/v2/clusters/[ClusterId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cb95aa626a47740afbf6aa0 99b65**** | The ID of the cluster. |

| Container Service fo | r Kubernete | s |   |   | Developer Guide·Cluster API list |
|---|---|---|---|---|---|

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| api_server_eip | Boolean | Body | No | true | Specifies whether to associate an elastic IP address (EIP) with the cluster API server. This enables Internet access for the cluster. Valid values: true : associates an EIP with the cluster API server. false : does not associate an EIP with the cluster API server. |
| api_server_eip_id | String | Body | No | eip-wz9fnasl6dsfhmvci**** | The ID of the EIP that you want to associate with the cluster API server. The parameter takes effect only if api_server_eip is set to true . |
| deletion_protection | Boolean | Body | No | true | Specifies whether to enable deletion protection for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values: true : enables deletion protection for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations. false : disables deletion protection for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations. Default value: false |
| instance_deletion_protectio n | Boolean | Body | No | true | Specifies whether to enable deletion protection for the instances in the cluster. If deletion protection is enabled, the instances in the cluster cannot be deleted in the console or by calling the API. Valid values: true : enables deletion protection for the instances in the cluster. You cannot delete the instances in the cluster in the console or by calling the API. false : disables deletion protection for the instances in the cluster. You can delete the instances in the cluster in the console or by calling the API. Default value: false |
| ingress_domain_rebinding | String | Body | No | true | Specifies whether to remap the test domain name of the cluster. Valid values: true : remaps the test domain name of the cluster. false : does not remap the test domain name of the cluster. Default value: false |
| ingress_loadbalancer_id | String | Body | No | lb-wz97kes8tnndkpodw**** | The ID of the Server Load Balancer (SLB) instance that is associated with the cluster. |
| resource_group_id | String | Body | No | rg-acfmyvw3wjm**** | The ID of the resource group to which the cluster belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster_id | String | cb95aa626a47740afbf6aa09**** | The ID of the cluster. |
| request_id | String | 687C5BAA-D103-4993-884B- C35E4314**** | The ID of the request. |
| task_id | String | T-5a54309c80282e39ea00**** | The ID of the task. |

```json
PUT /api/v2/clusters/[ClusterId] HTTP/1.1
    "ClusterId": "cb95aa626a47740afbf6aa099b65****"
```

`XML` format

```xml
<cluster_id>cb95aa626a47740afbf6aa09****</cluster_id> <task_id>T-5a54309c80282e39ea00****</task_id> <request_id>687C5BAA-D103-4993-884B-C35E4314****</request_id>
```

| JSON | format |
|---|---|
| { "cluster_id": "cb95aa626a47740afbf6aa09****", "task_id": "T-5a54309c80282e39ea00****", "request_id": "687C5BAA-D103-4993-884B-C35E4314****" } |   |

2.2.5.2. Modify the labels of a cluster You can call the ModifyClusterTags operation to modify the labels of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/tags HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f34eb1808d6b 9362c9**** | The ID of the cluster. |
| body | Array | Body | No |   |   |
| tag | Struct |   | No |   | The configurations of the label. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |

```json
POST /clusters/[ClusterId]/tags HTTP/1.1
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
    [ {
      "key" : "env",
      "value" : "prod"
    } ]
```

| XML | format |
|---|---|
| HTTP/1.1 200 OK |   |

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.2.6. Upgrade 2.2.6.1. Upgrade a cluster You can call the UpgradeCluster operation to upgrade a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /api/v2/clusters/[ClusterId]/upgrade HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961451182edac d74faf**** | The ID of the cluster. |
| body | Struct | body | No |   |   |
| component_name | String |   | No | k8s | The name of the component. Set the value to k8s . |
| version | String |   | No | 1.14.8-aliyun.1 | The Kubernetes version of the cluster. |
| next_version | String |   | No | 1.16.9-aliyun.1 | The Kubernetes version to which the cluster can be upgraded. |

```json
POST /api/v2/clusters/[ClusterId]/upgrade HTTP/1.1
    "ClusterId": ""
    "component_name" : "k8s",
    "next_version" : "1.16.9-aliyun.1",
    "version" : "1.14.8-aliyun.1"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.2.6.2. Query the upgrade status of a cluster You can call the GetUpgradeStatus operation to query the upgrade status of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /api/v2/clusters/[ClusterId]/upgrade/status HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f34eb1808d6b 9362c9**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| error_message | String | subject to actual return | The error message returned during the upgrade. |
| precheck_report_id | String | be4c8eb72de94d459ea7ace7c811d 119 | The ID of the precheck report. |
| status | String | running | The state of the upgrade. |
| upgrade_step | String | prechecking | The current phase of the upgrade. |
| upgrade_task | Struct |   | The details of the upgrade task. |
| message | String | subject to actual return | The description of the upgrade task. |
| status | String | running | The state of the upgrade task. |

```json
GET /api/v2/clusters/[ClusterId]/upgrade/status HTTP/1.1
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

| XML | format |
|---|---|
| <error_message>subject to actual return</error_message> <upgrade_task> <message>subject to actual return</message> <status>running</status> </upgrade_task> <precheck_report_id>be4c8eb72de94d459ea7ace7c811d119</precheck_report_id> <status>running</status> <upgrade_step>prechecking</upgrade_step> |   |

| JSON | format |
|---|---|
| { "error_message": "subject to actual return", "upgrade_task": { "message": "subject to actual return", "status": "running" }, "precheck_report_id": "be4c8eb72de94d459ea7ace7c811d119", "status": "running", "upgrade_step": "prechecking" } |   |

2.2.6.3. Suspend the upgrade of a cluster You can call the PauseClusterUpgrade operation to suspend the upgrade of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /api/v2/clusters/[ClusterId]/upgrade/pause HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961451182edac d74faf**** | The ID of the cluster. |

```json
POST /api/v2/clusters/[ClusterId]/upgrade/pause HTTP/1.1
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.2.6.4. Cancel the upgrade of a cluster You can call the CancelClusterUpgrade operation to cancel the upgrade of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /api/v2/clusters/[ClusterId]/upgrade/cancel HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f34eb1808d6b 9362c9**** | The ID of the cluster. |

```json
POST /api/v2/clusters/[ClusterId]/upgrade/cancel HTTP/1.1
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.2.6.5. Resume the upgrade of a cluster You can call the ResumeUpgradeCluster operation to resume the upgrade of a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /api/v2/clusters/[ClusterId]/upgrade/resume HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961451182edac d74faf**** | The ID of the cluster. |

```json
POST /api/v2/clusters/[ClusterId]/upgrade/resume HTTP/1.1
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

### Nodes

2.3.1. Query nodes in a cluster You can call the DescribeClusterNodes operation to query information about the nodes in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/nodes HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961451182edac d74faf**** | The ID of the cluster. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| instanceIds | String | Query | No | i-node1,i-node2 | The IDs of Elastic Compute Service (ECS) instances. Instances that match the IDs are returned. If nodepool_id is not empty, this parameter is ignored. Separate multiple nodes with commas (,). |
| nodepool_id | String | Query | No | np*** | The ID of the node pool. |
| state | String | Query | No | all | The state of the nodes in the cluster. You can filter the nodes by state. Valid values: all : Query all nodes in the cluster. running : Query nodes that are running in the cluster. removing : Query nodes that are being removed from the cluster. initial : Query nodes that are initializing in the cluster. failed : Query nodes that failed to be created in the cluster. |
| pageSize | String | Query | No | 3 | The number of entries to return on each page. |
| pageNumber | String | Query | No | 50 | The number of the page to return. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodes | Array of node |   | The details of the nodes in the cluster. |
| creation_time | String | "2020-08-25T11:25:35+08:00" | The time when the node was created. |
| error_message | String | "***" | The error message generated when the node was created. |
| expired_time | String | "2099-12-31T23:59:00+08:00" | The expiration date of the node. |
| host_name | String | "iZ2vcckdmxp7u0urj2k****" | The name of the host. |
| image_id | String | "aliyun_2_1903_x64_20G_alibase_20 200529.vhd" | The ID of the system image that is used by the node. |
| instance_charge_type | String | "PostPaid" | The billing method of the instance on which the node is deployed. |
| instance_id | String | "i-2vcckdmxp7u0urj2k2rw" | The ID of the instance on which the node is deployed. |
| instance_name | String | "worker-k8s-for-cs- c5cdf7e3938bc4f8eb0e44b21a80f* ***" | The name of the instance on which the node is deployed. |
| instance_role | String | "Worker" | The role of the node. Valid values: Master : master node Worker : worker node |
| instance_status | String | "Running" | The status of the node. |
| instance_type | String | "ecs.c5.xlarge" | The instance type of the node. |
| instance_type_family | String | "ecs.c5" | The ECS instance family of the node. |
| ip_address | List | ["192.168.44.247"] | The IP address of the node. |
| is_aliyun_node | Boolean | true | Indicates whether the instance is provided by Alibaba Cloud. |

| Container Service f | or Kubernetes |   | Developer Guide·Cluster API list |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| node_name | String | "cn-chengdu.192.168.0.36" | The name of the node. This name is the identifier of the node in the cluster. |
| node_status | String | "Ready" | Indicates whether the node is ready. |
| nodepool_id | String | "np0794239424a84eb7a95327369d 56****" | The ID of the node pool. |
| source | String | "ess_attach" | The source of the node. You can add a node to a cluster in the Container Service console or Resource Orchestration Service (ROS) console. |
| state | String | "running" | The status of the node. |
| page | Struct |   | The pagination details. |
| page_number | Integer | 1 | The number of the returned page. |
| page_size | Integer | 10 | The number of entries returned per page. |
| total_count | Integer | 5 | The total number of entries returned. |

```json
GET /clusters/[ClusterId]/nodes HTTP/1.1
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

| XML | format |
|---|---|
| <nodes> <creation_time>"2020-08-25T11:25:35+08:00"</creation_time> <error_message>"***"</error_message> <instance_name>"worker-k8s-for-cs-c5cdf7e3938bc4f8eb0e44b21a80f****"</instance_name> <node_status>"Ready"</node_status> <is_aliyun_node>true</is_aliyun_node> <node_name>"cn-chengdu.192.168.0.36"</node_name> <expired_time>"2099-12-31T23:59:00+08:00"</expired_time> <source>"ess_attach"</source> <instance_type_family>"ecs.c5"</instance_type_family> <instance_id>"i-2vcckdmxp7u0urj2k2rw"</instance_id> <instance_charge_type>"PostPaid"</instance_charge_type> <instance_role>"Worker"</instance_role> <instance_status>"Running"</instance_status> <state>"running"</state> <image_id>"aliyun_2_1903_x64_20G_alibase_20200529.vhd"</image_id> <instance_type>"ecs.c5.xlarge"</instance_type> <nodepool_id>"np0794239424a84eb7a95327369d56****"</nodepool_id> <host_name>"iZ2vcckdmxp7u0urj2k****"</host_name> <ip_address>["192.168.44.247"]</ip_address> </nodes> <page> <page_number>1</page_number> <total_count>5</total_count> <page_size>10</page_size> </page> |   |

```json
    "nodes": {
        "creation_time": "\"2020-08-25T11:25:35+08:00\"",
        "error_message": "\"***\"",
        "instance_name": "\"worker-k8s-for-cs-c5cdf7e3938bc4f8eb0e44b21a80f****\"",
        "node_status": "\"Ready\"",
        "is_aliyun_node": true,
        "node_name": "\"cn-chengdu.192.168.0.36\"",
        "expired_time": "\"2099-12-31T23:59:00+08:00\"",
        "source": "\"ess_attach\"",
        "instance_type_family": "\"ecs.c5\"",
        "instance_id": "\"i-2vcckdmxp7u0urj2k2rw\"",
        "instance_charge_type": "\"PostPaid\"",
        "instance_role": "\"Worker\"",
        "instance_status": "\"Running\"",
        "state": "\"running\"",
        "image_id": "\"aliyun_2_1903_x64_20G_alibase_20200529.vhd\"",
        "instance_type": "\"ecs.c5.xlarge\"",
        "nodepool_id": "\"np0794239424a84eb7a95327369d56****\"",
        "host_name": "\"iZ2vcckdmxp7u0urj2k****\"",
        "ip_address": "[\"192.168.44.247\"]"
```

`},`

```json
    "page": {
        "page_number": 1,
        "total_count": 5,
        "page_size": 10
```

2.3.2. Remove nodes from a cluster You can call the RemoveClusterNodes operation to remove nodes from a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /api/v2/clusters/[ClusterId]/nodes/remove HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Patj | Yes | c850429a2287b4d968e27e8 7a4921**** | The ID of the cluster. |
| body | Struct | Body | No |   |   |
| release_node | Boolean |   | No | true | Specifies whether to release the Elastic Compute Service (ECS) instances. Valid values: true : releases the ECS instances. false : does not release the ECS instances. Default value: false Not e You cannot release subscription ECS instances when you remove the nodes. |
| drain_node | Boolean |   | No | true | Specifies whether to remove all pods from the nodes that you want to remove. Valid values: true : removes all pods from the nodes that you want to remove. false : does not remove pods from the nodes that you want to remove. Default value: false |
| nodes | String |   | No | ["cn-chengdu.192.168.0.70"] | The name of the node. |

```json
POST /api/v2/clusters/[ClusterId]/nodes/remove HTTP/1.1
    "ClusterId": "c82e6987e2961451182edacd74faf****"
    "release_node": false,
    "nodes": [
        "cn-shenzhen.192.168.0.70"
```

`],`

```json
    "drain_node": false
HTTP/1.1 200 OK
```

2.3.3. Add existing ECS instances to a cluster You can call the AttachInstances operation to add existing Elastic Compute Service (ECS) instances to a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/attach HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f34eb1808d6b 9362c9**** | The ID of the cluster. |
| format_disk | Boolean | Body | No | false | Specifies whether to store container data and images on data disks. Valid values: true : mounts data disks to store container data and images. false : does not mount data disks to store container data or images. Default value: false How to mount a data disk: If the ECS instances are already mounted with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4 and mounts it to /var/lib/docker and /var/lib/kubelet. If no data disk is attached to the ECS instances, the system does not purchase a new data disk. Not e If you choose to store container data and images on data disks and a data disk is already mounted to the ECS instance, the original data on this data disk will be cleared. You can back up the disk to avoid data loss. |
| image_id | String | Body | No | aliyun_2_1903_x64_20G_alib ase_20200529.vhd | The ID of the custom image. If you do not set this parameter, the default system image is used. Not e If you specify a custom image, the custom image is used to deploy the operating systems on the system disks of the nodes. |
| keep_instance_name | Boolean | Body | No | true | Specifies whether to retain the instance name. Valid values: true : retains the instance name. false : does not retain the instance name. Default value: true |
| user_data | String | Body | No | IyEvdXNyL2Jpbi9iYXNoCmVj aG8gIkhlbGxvIEFDSyEi | The user-defined data on the node. For more information, see the User-defined data chapter in the ECS documentation. |

| Parameter | Type | Position | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| cpu_policy | String | Body | No | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. Default value: none |   |   |
| runtime | Json | Body | No | {"name": "docker", "version": "19.03.5"} | The container runtime. |   |   |
| platform | String | Body | No | CentOS | The OS distribution that you want to use. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |   |   |
| password | String | Body | No | Hello1234 | The SSH logon password that is used to log on to the ECS instances. You must set login_password or key_pair . The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It cannot contain backslashes (\) or double quotation marks ("). For security considerations, the password is encrypted during data transfer. |   |   |
| instances | String | Body | No | ["i-2zed0sswuau6o89b****"] | The IDs of the existing ECS instances that you want to add. |   |   |
| tags | Array | Body | No |   | The labels that you want to add to nodes. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs: , https:// , or http:// . |   |   |
| key | String |   | No | key | The key of the label. |   |   |
| value | String |   | No | value | The value of the label. |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| list | Array of list |   | The details of the added nodes. |
| code | String | 200 | The code that indicates the task result. |
| instanceId | String | i-2ze0lgm3y6iylcbt**** | The ID of the instance. |
| message | String | successful | Indicates whether the ECS instances are successfully added to the cluster. |
| task_id | String | T-5a544aff80282e39ea000039 | The ID of the task. |

```json
POST /clusters/[ClusterId]/attach HTTP/1.1
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

| XML | format |
|---|---|
| <task_id>T-5a544aff80282e39ea000039</task_id> <list> <code>200</code> <instanceId>i-2ze0lgm3y6iylcbt****</instanceId> <message>successful</message> </list> |   |

| JSON | format |
|---|---|
| { "task_id": "T-5a544aff80282e39ea000039", "list": { "code": 200, "instanceId": "i-2ze0lgm3y6iylcbt****", "message": "successful" } } |   |

2.3.4. Manually add existing instances to a cluster You can call the DescribeClusterAttachScripts operation to manually add an existing instance to a cluster. This operation returns a unique executable script. You can run this script on an existing instance to add the instance to the specified cluster as a node. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/attachscript HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | ca375a93a30474552ad2a0e be183e**** | The ID of the cluster. |   |   |
| body | Struct | body | No |   |   |   |   |
| keep_instance_name | Boolean |   | No | true | Specifies whether to retain the name of the existing instance when it is added to the cluster. If you do not retain the instance name, the instance is named in the worker- k8s-for-cs-<clusterid> format. Valid values: true : retains the instance name. false : does not retain the instance name. Default value: true |   |   |
|   |   |   |   |   |   | worker- |   |
| options | String |   | No | {\"enableIptables\": true,\"manageRuntime\": true,\"quiet\": true,\"allowedClusterAddo ns\": [\"kube- proxy\",\"flannel\",\"cored ns\"]} | The node configurations for the existing instance that you want to add as a node. |   |   |
| arch | String |   | No | amd64 | The CPU architecture of the node. |   |   |

|   | k8s-for-cs-<clusterid> |
|---|---|

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| format_disk | Boolean |   | No | false | Specifies whether to mount data disks to an existing instance when you add the instance to the cluster. You can add data disks to store the container data and images. Valid values: true : mounts data disks to the existing instance that you want to add. After a data disk is mounted, the original data that is stored on the disk is erased. Back up data before you mount a data disk. false : does not mount data disks to the existing instance. Default value: false How to mount a data disk: If the existing Elastic Compute Service (ECS) instance has data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet. If no data disk is attached to the ECS instances, the system does not purchase a new data disk. |
| nodepool_id | String |   | No | np1c9229d9be2d432c93f77 a88fca0**** | The ID of the node pool to which you want to add an existing node. This parameter allows you to add an existing node to a specified node pool. |
| rds_instances | String |   | No | ["rm-xxx"] | The names of the ApsaraDB RDS instances. |

```json
POST /clusters/[ClusterId]/attachscript HTTP/1.1
    "ClusterId": "ca375a93a30474552ad2a0ebe183e****"
    "nodepool_id": "np1c9229d9be2d432c93f77a88fca0****",
    "format_disk": false,
    "keep_instance_name": true,
    "rds_instances": ["rm-xxx"],
    "arch": "amd64",
    "options": "{\\\"enableIptables\\\": true,\\\"manageRuntime\\\": true,\\\"quiet\\\": true,\\\"allowedClusterA ddons\\\": [\\\"kube-proxy\\\",\\\"
flannel\\\",\\\"coredns\\\"]}"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.3.5. Node pools 2.3.5.1. Create a node pool You can call the CreateClusterNodePool operation to create a node pool for a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/nodepools HTTP/1.1
```

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | path | Yes | c61da77e8bfbc4c4c999a f2b51b65**** | The ID of the cluster. |
| body | Struct | body | No |   |   |
| count | Integer |   | No | 1 | The number of nodes in the node pool. |
| nodepool_info | Struct |   | No |   | The configuration of the node pool. |
| name | String |   | No | cluster-demo | The name of the node pool. |

| Container Service | for Kubern | etes |   |   | Developer Guide·Cluster API list |
|---|---|---|---|---|---|

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| scaling_group | Struct |   | No |   | The configuration of the scaling group that is used by the node pool. |
| system_disk_category | String |   | No | cloud_efficiency | The type of system disk. Valid values: cloud_efficiency : ultra disk cloud_ssd : standard SSD cloud_essd : enhanced SSD (ESSD) Default value: cloud_efficiency. |
| system_disk_size | Integer |   | No | 120 | The system disk size of a node. Unit: GiB. |
| system_disk_performanc e_level | String |   | No | PL1 | The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for ESSDs. |
| vpc_id | String |   | No | vpc- wz984yvbd6lck22z3**** | The ID of the virtual private cloud (VPC). |
| instance_charge_type | String |   | No | PrePaid | The billing method of nodes in the node pool. Valid values: PrePaid : subscription PostPaid : pay-as-you-go Default value: PostPaid |
| internet_max_bandwidth _out | Integer |   | No | 5 | The bandwidth of the public IP address. |
| login_password | String |   | No | Hello1234 | The logon password. |
| security_group_id | String |   | No | sg- wz9a8g2mt6x5llu0**** | The ID of the security group. |
| platform | String |   | No | Linux | The OS distribution. |
| image_id | String |   | No | aliyun_2_1903_x64_20G_a libase_20200529.vhd | The ID of a custom image. By default, the image provided by Container Service is used. |
| internet_charge_type | String |   | No | PayByTraffic | The billing method of the public IP address. |
| scaling_policy | String |   | No | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale- out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks. Default value: release . |
| vswitch_ids | String |   | No | vsw- wz9mfnhmssud6eicu**** | The IDs of vSwitches. |
| instance_types | String |   | No | ecs.d1ne.2xlarge | The type of instance. |
| tags | Array |   | No |   | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| data_disks | Array |   | No |   | The configuration of data disks. |
| category | String |   | No | cloud_ssd | The type of data disk. |
| size | Integer |   | No | 40 | The size of a data disk. Unit: GiB. |

| PostPaid |   |
|---|---|
|   | PostPaid |

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| encrypted | String |   | No | true | Specifies whether to encrypt data disks. Valid values: true : encrypts a data disk. false : does not encrypt a data disk. Default value: false |
| auto_snapshot_policy_id | String |   | No | sp-2zej1nogjvovnz4z**** | The ID of an automatic snapshot policy. Automatic backup is performed for a disk based on the specified automatic snapshot policy. By default, this parameter is empty. This indicates that automatic backup is disabled. |
| kubernetes_config | Struct |   | No |   | The configuration of the cluster. |
| cpu_policy | String |   | No | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : specifies that the default CPU affinity is used Default value: none |
| cms_enabled | Boolean |   | No | true | Specifies whether to install the CloudMonitor agent on ECS nodes. After the CloudMonitor agent is installed on ECS nodes, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes Default value: false |
| unschedulable | Boolean |   | No | false | Nodes that are newly added to the cluster are marked as unschedulable. If you specify this parameter, the nodes become unschedulable after they are added to the cluster. You can go to the Nodes page and set the nodes to schedulable. |
| user_data | String |   | No | dGhpcyBpcyBhIGV4YW1w bGU= | The user-defined data on the node. |
| runtime | String |   | No | docker | The container runtime. |
| runtime_version | String |   | No | 19.03.5 | The version of the container runtime. |
| node_name_mode | String |   | No | aliyun.com00055test | A custom node name consists of a prefix, an IP substring, and a suffix. The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). A custom node name must start and end with a digit or lowercase letter. The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the length of the IP address substring is 5, and the suffix is test, the node name will be aliyun.com00055test. |
| labels | Array |   | No |   | The labels that you want to add to the nodes in the cluster. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| taints | Array |   | No |   | The taints that you want to add to the nodes in the cluster. |

| Container Service | for Kubern | etes |   |   | Developer Guide·Cluster API list |
|---|---|---|---|---|---|

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| key | String |   | No | env | The key of a taint. |
| value | String |   | No | prod | The value of a taint. |
| effect | String |   | No | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| tee_config | Struct |   | No |   | The configuration about confidential computing for the cluster. |
| tee_enable | Boolean |   | No | true | Specifies whether to enable confidential computing for the cluster. |
| auto_scaling | Struct |   | No |   | The configuration about auto scaling. |
| enable | Boolean |   | No | true | Specifies whether to enable auto scaling. Valid values: true : enables auto scaling false : disables auto scaling. If you set this parameter to false, other parameters in the auto_scaling section do not take effect. Default value: false |
| max_instances | Integer |   | No | 10 | The maximum number of ECS instances that can be created in the node pool. |
| min_instances | Integer |   | No | 1 | The minimum number of ECS instances that must be kept in the node pool. |
| type | String |   | No | cpu | The minimum number of ECS instances that must be kept in the node pool. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepool_id | String | np5faa48fb31b6b8078d00**** | The ID of the node pool. |

```json
    "nodepool_info": {
        "name": "test"
```

`},`

```json
    "scaling_group": {
        "vswitch_ids": [
            "vsw-ow2maqt4wgnzsge7a****"
```

`],`

```json
        "system_disk_category": "cloud_efficiency",
        "system_disk_size": 120,
        "system_disk_performance_level": "",
        "data_disks": [],
        "instance_types": [
            "ecs.mn4.large"
```

`],`

```json
        "vpc_id": "vpc-ow2cm4rzhrclukhm6****",
        "tags": [],
        "instance_charge_type": "PostPaid",
        "internet_max_bandwidth_out": 0,
        "login_password": "Hello1234",
        "platform": "CentOS",
        "image_id": "centos_7_9_x64_20G_alibase_20210318.vhd",
        "rds_instances": []
```

`},`

```json
    "kubernetes_config": {
        "cpu_policy": "none",
        "cms_enabled": false,
        "unschedulable": false,
        "labels": [],
        "taints": [],
        "user_data": "",
        "runtime": "docker",
        "runtime_version": "19.03.15"
```

`},`

```json
    "auto_scaling": {
        "enable": false
```

`},`

```json
    "tee_config": {
        "tee_enable": false
```

`},`

```json
    "count": 1
```

| XML | format |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/xml <nodepool_id>np31da1b38983f4511b490fc62108a****</nodepool_id> |   |

| JSON | format |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "nodepool_id" : "np31da1b38983f4511b490fc62108a****" } |   |

2.3.5.2. Scale out a node pool You can call the ScaleClusterNodePool operation to scale out a node pool. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c23421cfa74454bc8b37163f d19af**** | The ID of the cluster. |
| NodepoolId | String | Path | Yes | np31da1b38983f4511b490f c62108a**** | The ID of the node pool. |
| body | Struct | body | No |   |   |

| Container Service fo | r Kubernete | s |   |   | Developer Guide·Cluster API list |
|---|---|---|---|---|---|

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| count | Long |   | No | 1 | The number of worker nodes that you want to add. You can add at most 500 nodes in one API call. The maximum number of nodes that can be added is limited by the quota of nodes in the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| task_id | String | T-5faa48fb31b6b8078d00**** | The ID of the task. |

```json
POST /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "NodepoolId": "np31da1b38983f4511b490fc62108a****"
    "count": 1
```

| XML | format |
|---|---|
| <task_id>T-5faa48fb31b6b8078d00****</task_id> |   |

| JSON | format |
|---|---|
| { "task_id": "T-5faa48fb31b6b8078d00****" } |   |

2.3.5.3. Modify the configuration of a node pool You can call the ModifyClusterNodePool operation to modify the configuration of a node pool. This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | path | Yes | c23421cfa74454bc8b371 63fd19af**** | The ID of the cluster. |
| NodepoolId | String | path | Yes | p31da1b38983f4511b49 0fc62108a**** | The ID of the node pool. |
| update_nodes | Boolean | Body | No | true | Specifies whether to update node information, such as labels and taints. |
| auto_scaling | Struct | Body | No |   | The configuration about auto scaling. |
| enable | Boolean |   | No | true | Specifies whether to enable auto scaling. true : enables auto scaling for the node pool false : disables auto scaling for the node pool. If you set this parameter to false , other parameters in the auto_scaling section do not take effect. Default value: false |
| max_instances | Long |   | No | 10 | The maximum number of Elastic Compute Service (ECS) instances supported by the node pool. |
| min_instances | Long |   | No | 2 | The minimum number of ECS instances. |

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| type | String |   | No | cpu | The minimum number of ECS instances that must be kept in the node pool. Valid values: cpu : regular instance gpu : GPU-accelerated instance gpushare : shared GPU-accelerated instance spot : preemptible instance Default value: cpu |
| kubernetes_config | Struct | Body | No |   | The configuration of the cluster. |
| labels | Array |   | No | [ { "key" : "String", "value" : "String" } ] | The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| taints | Array |   | No |   | The configurations of node taints. |
| key | String |   | No | env | The key of a taint. |
| value | String |   | No | prod | The value of a taint. |
| effect | String |   | No | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| cms_enabled | Boolean |   | No | true | Specifies whether to install the CloudMonitor agent on ECS nodes. After the CloudMonitor agent is installed on ECS nodes, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes Default value: false |
| runtime | String |   | No | docker | The name of the container runtime. |
| runtime_version | String |   | No | 19.03.5 | The version of the container runtime. |
| user_data | String |   | No | IyEvdXNyL2Jpbi9iYXNoCm VjaG8gIkhlbGxvIEFDSyEi | The user-defined data of the node pool. |
| unschedulable | Boolean |   | No | false | Nodes that are newly added to the cluster are marked as unschedulable. If you select this option, the nodes are unschedulable when they are added to the cluster. You can go to the Nodes page and set the nodes as schedulable. |
| scaling_group | Struct | Body | No |   | The configuration of the scaling group. |
| data_disks | Array |   | No |   | The configurations of the data disks that are mounted to the nodes in the node pool. You can mount 0 to 10 data disks. You can mount at most 10 data disks to the nodes in the node pool. |
| category | String |   | No | cloud_ssd | The size of a data disk. Unit: GiB. |

| Container Service | for Kubern | etes |   |   | Developer Guide·Cluster API list |
|---|---|---|---|---|---|

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| size | Integer |   | No | 40 | Specifies whether to encrypt data disks. Valid values: true : encrypts a data disk. false : does not encrypt a data disk. Default value: false |
| encrypted | String |   | No | true | The ID of an automatic snapshot policy. Automatic backup is performed for a disk based on the specified automatic snapshot policy. By default, this parameter is empty. This indicates that automatic backup is disabled. |
| tags | Array |   | No | testkey | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| instance_charge_type | String |   | No | PrePaid | The billing method of the instance on which the node is deployed. |
| platform | String |   | No | AliyunLinux | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| image_id | String |   | No | aliyun_2_1903_x64_20G_a libase_20200904.vhd | The ID of the custom image. You can call the DescribeKubernetesVersionMetadata operation to query the supported images. By default, the latest image is used. |
| login_password | String |   | No | Hello1234 | The password for SSH logon. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
| scaling_policy | String |   | No | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks. |
| system_disk_category | String |   | No | cloud_efficiency | The type of system disk. Valid values: cloud_efficiency : ultra disk cloud_ssd : standard SSD Default value: cloud_ssd |
| system_disk_size | String |   | No | 120 | The system disk size of a node. Unit: GiB. Valid values: 20 to 500 The value of this parameter must be at least 20 and greater than or equal to the image size. The default value is the greater one between 40 and the image size. |
| internet_max_bandwidth _out | Integer |   | No | 10 | The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100. |
| multi_az_policy | String |   | No | BALANCE | The ECS instance scaling policy for a multi-zone scaling group. |

| Developer Guide· | Cluster API | list |   |   | Container Service for Kubernetes |
|---|---|---|---|---|---|

| Field | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| internet_charge_type | String |   | No | PayByBandwidth | The billing method of the public IP address of the node. |
| instance_types | List<String> |   | No | ["ecs.c6.large"] | The type of instance. For more information, see the Instance types chapter in ECS User Guide. |
| vswitch_ids | List<String> |   | No | ["vsw- wz9uwxhawmtzg7u9h*** *"] | The IDs of vSwitches. |
| tee_config | Struct | Body | No |   | The configuration about confidential computing for the cluster. |
| tee_enable | Boolean |   | No | false | Specifies whether to enable confidential computing for the cluster. Valid values: true : enables confidential computing for the cluster false : disables confidential computing for the cluster Default value: false |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepool_id | String | np737c3ac1ac684703b9e10673aa2c **** | The ID of the node pool. |
| task_id | String | T-5fd211e924e1d00787000293 | The ID of the task. |

```json
PUT /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "NodepoolId": "p31da1b38983f4511b490fc62108a****"
```

| XML | format |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/xml <task_id>T-5fd211e924e1d00787000293</task_id> <nodepool_id>np737c3ac1ac684703b9e10673aa2c****</nodepool_id> |   |

| JSON | format |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "task_id": "T-5fd211e924e1d00787000293", "nodepool_id": "np737c3ac1ac684703b9e10673aa2c****" } |   |

2.3.5.4. Query node pools You can call the DescribeClusterNodePools operation to query node pools in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/nodepools HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cc0f87de0b8fb403f86e10e2 04f83**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepools | Array of nodepool |   | The list of the returned node pools. |
| auto_scaling | Struct |   | The configuration about auto scaling. |
| eip_bandwidth | Integer | 5 | The peak bandwidth of the elastic IP address (EIP). |
| enable | Boolean | true | Indicates whether auto scaling is enabled. true : Auto scaling is enabled for the node pool. false : Auto scaling is disabled for the node pool. If you set this parameter to false , other parameters in the auto_scaling section do not take effect. |
| max_instances | Integer | 10 | The maximum number of Elastic Compute Service (ECS) instances supported by the node pool. |
| min_instances | Integer | 2 | The minimum number of ECS instances. |
| type | String | cpu | The minimum number of ECS instances that must be kept in the node pool. Valid values: cpu : regular instance gpu : GPU-accelerated instance gpushare : shared GPU-accelerated instance spot : preemptible instance |
| kubernetes_config | Struct |   | The configuration of the cluster. |
| cms_enabled | Boolean | true | Indicates where the CloudMonitor agent is installed on ECS nodes of the cluster. After the CloudMonitor agent is installed, you can view monitoring information about the ECS instances in the CloudMonitor console. Installation is recommended. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes |
| cpu_policy | String | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. |
| labels | Array of label |   | The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs , https:// , or http:/ / . |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| node_name_mode | String | customized,test.,5,.com | The name of the custom node. |
| overwrite_hostname | Boolean | false | Indicates whether the host name is overwritten. |
| runtime | String | docker | The name of the container runtime. |
| runtime_version | String | 19.03.5 | The version of the container runtime. |
| taints | Array of taint |   | The taints that are added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. |

| aliyun , | acs , | https:// |
|---|---|---|

|   | / |
|---|---|

| Developer Guide·Cl | uster API list |   | Container Service for Kubernetes |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| effect | String | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| key | String | key | The key of a taint. |
| value | String | value | The value of a taint. |
| unschedulable | Boolean | false | Nodes that are newly added to the cluster are marked as unschedulable. If you select this option, the nodes are unschedulable when they are added to the cluster. You can go to the Nodes page and set the nodes as schedulable. |
| user_data | String | IyEvYmluL3NoCmVjaG8gIkhlbGxvIEF D****IyEvYmluL3NoCmVjaG8gIkhlbG xvIEFD**** | The user-defined data of the node pool. For more information, see the User-defined data chapter in the ECS documentation. |
| nodepool_info | Struct |   | The information about the node pool. |
| created | String | 2020-09- 27T19:14:09.156823496+08:00 | The time when the node pool was created. |
| is_default | Boolean | true | Indicates whether the node pool is a default node pool. A Container Service cluster usually has only one default node pool. Valid values: true : The node pool is a default node pool. false : The node pool is not a default node pool. |
| name | String | default-nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| nodepool_id | String | np615c0e0966124216a0412e10afe0 **** | The ID of the node pool. |
| region_id | String | cn-beijing | The region ID of the elastic container instance. |
| resource_group_id | String | rg-acfmyvw3wjm**** | The ID of the resource group. |
| type | String | ess | The type of the node pool. |
| updated | String | 2020-09-27T20:37:46+08:00 | The time when the node pool was last updated. |
| scaling_group | Struct |   | The configuration of the scaling group. |
| data_disks | String | [ { "category" : "String", "size" : Long, "encrypted" : "String", "auto_snapshot_policy_id" : "String" } ] | The configuration of data disks. |
| data_disks | Array of data_disk |   | The configurations of the data disks attached to the nodes in the node pool. The configurations include the disk type and disk size. |
| auto_snapshot_policy_id | String | sp-2zej1nogjvovnz4z**** | The automatic backup policy when disk backup is enabled. |
| category | String | cloud_ssd | The category of the data disk. |
| encrypted | String | true | Indicates whether the data disk is encrypted. |

| Container Service f | or Kubernetes |   | Developer Guide·Cluster API list |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| size | Long | 40 | The size of the data disk. Valid values: 40 to 32767. |
| image_id | String | aliyun_2_1903_x64_20G_alibase_20 200529.vhd | The ID of the custom image. You can call DescribeKubernetesVersionMetadata to query the images supported by ACK. |
| instance_charge_type | String | PostPaid | The billing method of the nodes in the node pool. Valid values: PrePaid : the subscription billing method PostPaid : the pay-as-you-go billing method. |
| instance_types | List | ["ecs.n4.large"] | The instance types of the nodes in the node pool. |
| internet_charge_type | String | PayByBandwidth | The billing method of the public IP address of the node. |
| internet_max_bandwidth_o ut | Integer | 10 | The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100. |
| login_password | String | ****** | The password for SSH logon. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. For security purposes, the returned password is encrypted. |
| multi_az_policy | String | BALANCE | The ECS instance scaling policy for a multi-zone scaling group. |
| platform | String | AliyunLinux | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| ram_policy | String | KubernetesWorkerRole-021dc54f- 929b-437a-8ae0-34c24d3e**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage ECS instances. |
| scaling_group_id | String | asg-2ze8n5qw4atggut8**** | The ID of the scaling group. |
| scaling_policy | String | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks. |
| security_group_id | String | sg-2ze1iuk12m2sb4c4**** | The ID of the security group. |
| system_disk_category | String | cloud_efficiency | The type of system disk. Valid values: cloud_efficiency : ultra disk cloud_ssd : standard SSD |
| system_disk_size | Integer | 120 | The system disk size of a node. Unit: GiB. Valid values: 20 to 500. |
| tags | Array of tag |   | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun or acs . Keys and values cannot contain https:// or http:// . |

| AliyunLinu |   |
|---|---|
| WindowsCor |   |
| CentOS 7.6 |   |
| ARM CentOS |   |
| NeoKylin : |   |
|   | AliyunLinux |

| Developer Guide·Cl | uster API list |   | Container Service for Kubernetes |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| vswitch_ids | List | ["vsw-2ze3ds0mdip0hdz8i****"] | The IDs of vSwitches. |
| status | Struct |   | The status details about the node pool. |
| failed_nodes | Integer | 0 | The number of failed nodes. |
| healthy_nodes | Integer | 3 | The number of healthy nodes. |
| initial_nodes | Integer | 0 | The number of nodes that are being created. |
| offline_nodes | Integer | 0 | The number of offline nodes. |
| removing_nodes | Integer | 0 | The number of nodes that are being removed. |
| serving_nodes | Integer | 3 | The number of running nodes. |
| state | String | active | The status of the node pool. Valid values: active : The node pool is active. scaling : The node pool is being scaled. removing : Nodes are being removed from the node pool. deleting : The node pool is being deleted. updating : The node pool is being updated. |
| total_nodes | Integer | 3 | The total number of nodes in the node pool. |
| tee_config | Struct |   | The configurations of confidential computing. |
| tee_enable | Boolean | false | Indicates whether confidential computing is enabled. Valid values: true : Confidential computing for the cluster is enabled. false : Confidential computing for the cluster is disabled. |

```json
GET /clusters/[ClusterId]/nodepools HTTP/1.1
    "ClusterId": "cc0f87de0b8fb403f86e10e204f83****"
```

`XML` format

```xml
<nodepools>
      <tee_config>
            <tee_enable>false</tee_enable>
      </tee_config>
      <scaling_group>
            <scaling_group_id>asg-2ze8n5qw4atggut8****</scaling_group_id>
            <internet_charge_type>PayByBandwidth</internet_charge_type>
            <internet_max_bandwidth_out>10</internet_max_bandwidth_out>
            <security_group_id>sg-2ze1iuk12m2sb4c4****</security_group_id>
            <multi_az_policy>BALANCE</multi_az_policy>
            <system_disk_size>120</system_disk_size>
            <platform>AliyunLinux</platform>
            <ram_policy>KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****</ram_policy>
            <data_disks>
                  <auto_snapshot_policy_id>sp-2zej1nogjvovnz4z****</auto_snapshot_policy_id>
                  <encrypted>true</encrypted>
                  <size>40</size>
                  <category>cloud_ssd</category>
            </data_disks>
            <instance_charge_type>PostPaid</instance_charge_type>
            <login_password>******</login_password>
            <system_disk_category>cloud_efficiency</system_disk_category>
            <image_id>aliyun_2_1903_x64_20G_alibase_20200529.vhd</image_id>
            <scaling_policy>release</scaling_policy>
            <tags>
                  <value>value</value>
                  <key>key</key>
            </tags>
            <instance_types>ecs.n4.large</instance_types>
            <vswitch_ids>vsw-2ze3ds0mdip0hdz8i****</vswitch_ids>
      </scaling_group>
      <kubernetes_config>
            <runtime_version>19.03.5</runtime_version>
            <cpu_policy>none</cpu_policy>
            <cms_enabled>true</cms_enabled>
            <overwrite_hostname>false</overwrite_hostname>
            <runtime>docker</runtime>
            <user_data>IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****</user_data>
            <unschedulable>false</unschedulable>
            <node_name_mode>customized,test.,5,.com</node_name_mode>
            <labels>
                  <value>value</value>
                  <key>key</key>
            </labels>
            <taints>
                  <effect>NoSchedule</effect>
                  <value>value</value>
                  <key>key</key>
            </taints>
      </kubernetes_config>
      <auto_scaling>
            <enable>true</enable>
            <min_instances>2</min_instances>
            <max_instances>10</max_instances>
            <eip_bandwidth>5</eip_bandwidth>
            <type>cpu</type>
      </auto_scaling>
      <nodepool_info>
            <resource_group_id>rg-acfmyvw3wjm****</resource_group_id>
            <created>2020-09-27T19:14:09.156823496+08:00</created>
            <name>default-nodepool</name>
            <region_id>cn-beijing</region_id>
            <type>ess</type>
            <is_default>true</is_default>
            <updated>2020-09-27T20:37:46+08:00</updated>
            <nodepool_id>np615c0e0966124216a0412e10afe0****</nodepool_id>
      </nodepool_info>
      <status>
            <serving_nodes>3</serving_nodes>
            <total_nodes>3</total_nodes>
            <state>active</state>
            <initial_nodes>0</initial_nodes>
            <removing_nodes>0</removing_nodes>
            <offline_nodes>0</offline_nodes>
            <failed_nodes>0</failed_nodes>
            <healthy_nodes>3</healthy_nodes>
      </status>
</nodepools>
```

```json
    "nodepools": {
        "tee_config": {
            "tee_enable": false
```

`},`

```json
        "scaling_group": {
            "scaling_group_id": "asg-2ze8n5qw4atggut8****",
            "internet_charge_type": "PayByBandwidth",
            "internet_max_bandwidth_out": 10,
            "security_group_id": "sg-2ze1iuk12m2sb4c4****",
            "multi_az_policy": "BALANCE",
            "system_disk_size": 120,
            "platform": "AliyunLinux",
            "ram_policy": "KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****",
            "data_disks": {
                "auto_snapshot_policy_id": "sp-2zej1nogjvovnz4z****",
                "encrypted": true,
                "size": 40,
                "category": "cloud_ssd"
```

`},`

```json
            "instance_charge_type": "PostPaid",
            "login_password": "******",
            "system_disk_category": "cloud_efficiency",
            "image_id": "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
            "scaling_policy": "release",
            "tags": {
                "value": "value",
                "key": "key"
```

`},`

```json
            "instance_types": ["ecs.n4.large"],
            "vswitch_ids": ["vsw-2ze3ds0mdip0hdz8i****"]
```

`},`

```json
        "kubernetes_config": {
            "runtime_version": "19.03.5",
            "cpu_policy": "none",
            "cms_enabled": true,
            "overwrite_hostname": false,
            "runtime": "docker",
            "user_data": "IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****",
            "unschedulable": false,
            "node_name_mode": "customized,test.,5,.com",
            "labels": {
                "value": "value",
                "key": "key"
```

`},`

```json
            "taints": {
                "effect": "NoSchedule",
                "value": "value",
                "key": "key"
```

`},`

```json
        "auto_scaling": {
            "enable": true,
            "min_instances": 2,
            "max_instances": 10,
            "eip_bandwidth": 5,
            "type": "cpu"
```

`},`

```json
        "nodepool_info": {
            "resource_group_id": "rg-acfmyvw3wjm****",
            "created": "2020-09-27T19:14:09.156823496+08:00",
            "name": "default-nodepool",
            "region_id": "cn-beijing",
            "type": "ess",
            "is_default": true,
            "updated": "2020-09-27T20:37:46+08:00",
            "nodepool_id": "np615c0e0966124216a0412e10afe0****"
```

`},`

```json
        "status": {
            "serving_nodes": 3,
            "total_nodes": 3,
            "state": "active",
            "initial_nodes": 0,
            "removing_nodes": 0,
            "offline_nodes": 0,
            "failed_nodes": 0,
            "healthy_nodes": 3
```

2.3.5.5. Query the details of a node pool You can call the DescribeClusterNodePoolDetail operation to query the details of a node pool. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c23421cfa74454bc8b37163f d19af**** | The ID of the cluster. |
| NodepoolId | String | Path | Yes | np31da1b38983f4511b490f c62108a**** | The ID of the node pool. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| auto_scaling | Struct |   | The auto scaling configurations of the queried node pool. |
| enable | Boolean | true | Indicates whether auto scaling is enabled. Valid values: true : Auto scaling is enabled for the node pool. false : Auto scaling is disabled for the node pool. If you set this parameter to false , other parameters in the auto_scaling section does not take effect. |
| max_instances | Integer | 10 | The maximum number of Elastic Compute Service (ECS) instances supported by the node pool. |
| min_instances | Integer | 1 | The minimum number of ECS instances. |
| type | String | cpu | The minimum number of ECS instances that must be kept in the node pool. Valid values: cpu : regular instance gpu : GPU-accelerated instance gpushare : shared GPU-accelerated instance spot : preemptible instance |
| kubernetes_config | Struct |   | The configuration of the cluster. |
| cms_enabled | Boolean | true | Indicates where the CloudMonitor agent is installed on ECS nodes of the cluster. After the CloudMonitor agent is installed, you can view monitoring information about the ECS instances in the CloudMonitor console. Installation is recommended. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes |
| cpu_policy | String | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. |
| labels | Array of label |   | The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs , https:// , or http:/ / . |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| node_name_mode | String | customized,test.,5,.com | The name of the custom node. |

| aliyun , | acs , | https:// |
|---|---|---|

|   | / |
|---|---|

| Developer Guide·Cl | uster API list |   | Container Service for Kubernetes |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| overwrite_hostname | Boolean | false | Indicates whether the host name is overwritten. |
| runtime | String | docker | The name of the container runtime. |
| runtime_version | String | 19.03.5 | The version of the container runtime. |
| taints | Array of taint |   | The taints that are added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. For more information, see taint-and-toleration. |
| effect | String | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| key | String | key | The key of a taint. |
| value | String | value | The value of a taint. |
| unschedulable | Boolean | false | Indicates whether the node is set to the unschedulable state. true : The node is set to the unschedulable state. false : The node is not set to the unschedulable state. |
| user_data | String | IyEvYmluL3NoCmVjaG8gIkhlbGxvIEF DSyEi | The user-defined data of the node pool. For more information, see the User-defined data chapter in the ECS documentation. |
| nodepool_info | Struct |   | The configuration of the node pool. |
| created | String | 2020-09- 27T19:14:09.156823496+08:00 | The time when the node pool was created. |
| is_default | Boolean | true | Indicates whether the node pool is a default node pool. A Container Service cluster usually has only one default node pool. Valid values: true : The node pool is a default node pool. false : The node pool is not a default node pool. |
| name | String | default-nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| nodepool_id | String | np615c0e0966124216a0412e10afe0 **** | The ID of the created node pool. |
| region_id | String | cn-beijing | The region ID of the elastic container instance. |
| resource_group_id | String | rg-acfmyvw3wjmb**** | The ID of the resource group. |
| type | String | ess | The type of the node pool. |
| updated | String | 2020-09-27T20:37:46+08:00 | The time when the node pool was last updated. |
| scaling_group | Struct |   | The configuration of the scaling group. |
| data_disks | Array of data_disk |   | The configurations of the data disks attached to the nodes in the node pool. The configurations include the disk type and disk size. |

| Container Service f | or Kubernetes |   | Developer Guide·Cluster API list |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| auto_snapshot_policy_id | String | sp-2zej1nogjvovnz4z**** | The automatic backup policy when disk backup is enabled. |
| category | String | cloud_ssd | The category of the data disk. |
| encrypted | String | true | Indicates whether the data disk is encrypted. |
| size | Long | 40 | The size of the data disk. Valid values: 40 to 32767. |
| image_id | String | aliyun_2_1903_x64_20G_alibase_20 200529.vhd | The ID of the custom image. You can call DescribeKubernetesVersionMetadata to query the images supported by ACK. |
| instance_charge_type | String | PayByBandwidth | The billing method of the public IP address of the node. |
| instance_types | List | ["ecs.n4.large"] | The instance types of the nodes in the node pool. |
| internet_charge_type | String | PayByTraffic | The billing method of the public IP address. |
| internet_max_bandwidth_o ut | Integer | 10 | The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100. |
| login_password | String | ******** | The password for SSH logon. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. For security purposes, the returned password is encrypted. |
| multi_az_policy | String | BALANCE | The ECS instance scaling policy for a multi-zone scaling group. |
| platform | String | AliyunLinux | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| ram_policy | String | KubernetesWorkerRole-021dc54f- 929b-437a-8ae0-34c24d3e**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage ECS instances. |
| scaling_group_id | String | asg-2zeieod8giqmov7z**** | The ID of the scaling group. |
| scaling_policy | String | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. Auto scaling is implemented by creating, stopping, and starting ECS instances. This mode accelerates scaling activities. When an ECS instance is stopped, you are charged only the storage fees. This does not apply to ECS instances that use local disks. |
| security_group_id | String | sg-2ze60ockeekspl3d**** | The ID of the security group. |
| system_disk_category | String | cloud_efficiency | The type of system disk. Valid values: cloud_efficiency : ultra disk cloud_ssd : standard SSD |
| system_disk_size | Integer | 120 | The system disk size of a node. Unit: GiB. Valid values: 20 to 500. |

| AliyunLinu |   |
|---|---|
| WindowsCor |   |
| CentOS 7.6 |   |
| ARM CentOS |   |
| NeoKylin : |   |
|   | AliyunLinux |

| Parameter | Type | Example | Description |
|---|---|---|---|
| tags | Array of tag |   | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun or acs: . Keys and values cannot contain https:// or http:// . |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| vswitch_ids | List | ["vsw-2ze3ds0mdip0hdz8i****"] | The IDs of vSwitches. |
| status | Struct |   | The status details about the nodes in the node pool. |
| failed_nodes | Integer | 0 | The number of failed nodes. |
| healthy_nodes | Integer | 3 | The number of healthy nodes. |
| initial_nodes | Integer | 0 | The number of nodes that are being created. |
| offline_nodes | Integer | 0 | The number of offline nodes. |
| removing_nodes | Integer | 0 | The number of nodes that are being removed. |
| serving_nodes | Integer | 3 | The number of running nodes. |
| state | String | active | The status of the node pool. Valid values: active : The node pool is active. scaling : The node pool is being scaled. removing : Nodes are being removed from the node pool. deleting : The node pool is being deleted. updating : The node pool is being updated. |
| total_nodes | Integer | 3 | The total number of nodes in the node pool. |
| tee_config | Struct |   | The configurations of confidential computing. |
| tee_enable | Boolean | false | Indicates whether confidential computing is enabled. Valid values: true : Confidential computing for the cluster is enabled. false : Confidential computing for the cluster is disabled. |

```json
GET /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "NodepoolId": "np31da1b38983f4511b490fc62108a****"
```

`XML` format

```xml
<tee_config>
    <tee_enable>false</tee_enable>
</tee_config> <scaling_group>
    <scaling_group_id>asg-2zeieod8giqmov7z****</scaling_group_id>
    <internet_charge_type>PayByTraffic</internet_charge_type>
    <ram_policy>KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****</ram_policy>
    <instance_charge_type>PayByBandwidth</instance_charge_type>
    <login_password>********</login_password>
    <system_disk_category>cloud_efficiency</system_disk_category>
    <internet_max_bandwidth_out>10</internet_max_bandwidth_out>
    <security_group_id>sg-2ze60ockeekspl3d****</security_group_id>
    <multi_az_policy>BALANCE</multi_az_policy>
    <image_id>aliyun_2_1903_x64_20G_alibase_20200529.vhd</image_id>
    <system_disk_size>120</system_disk_size>
    <platform>AliyunLinux</platform>
    <scaling_policy>release</scaling_policy>
    <data_disks>
        <auto_snapshot_policy_id>sp-2zej1nogjvovnz4z****</auto_snapshot_policy_id>
        <encrypted>true</encrypted>
        <size>40</size>
        <category>cloud_ssd</category>
    </data_disks>
    <tags>
        <value>value</value>
        <key>key</key>
    </tags>
    <instance_types>ecs.n4.large</instance_types>
    <vswitch_ids>vsw-2ze3ds0mdip0hdz8i****</vswitch_ids>
</scaling_group> <kubernetes_config>
    <runtime_version>19.03.5</runtime_version>
    <cpu_policy>none</cpu_policy>
    <cms_enabled>true</cms_enabled>
    <overwrite_hostname>false</overwrite_hostname>
    <runtime>docker</runtime>
    <user_data>IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFDSyEi</user_data>
    <unschedulable>false</unschedulable>
    <node_name_mode>customized,test.,5,.com</node_name_mode>
    <labels>
        <value>value</value>
        <key>key</key>
    </labels>
    <taints>
        <effect>NoSchedule</effect>
        <value>value</value>
        <key>key</key>
    </taints>
</kubernetes_config> <auto_scaling>
    <enable>true</enable>
    <min_instances>1</min_instances>
    <max_instances>10</max_instances>
    <type>cpu</type>
</auto_scaling> <nodepool_info>
    <resource_group_id>rg-acfmyvw3wjmb****</resource_group_id>
    <created>2020-09-27T19:14:09.156823496+08:00</created>
    <name>default-nodepool</name>
    <region_id>cn-beijing</region_id>
    <type>ess</type>
    <is_default>true</is_default>
    <updated>2020-09-27T20:37:46+08:00</updated>
    <nodepool_id>np615c0e0966124216a0412e10afe0****</nodepool_id>
</nodepool_info> <status>
    <serving_nodes>3</serving_nodes>
    <total_nodes>3</total_nodes>
    <state>active</state>
    <initial_nodes>0</initial_nodes>
    <removing_nodes>0</removing_nodes>
    <offline_nodes>0</offline_nodes>
    <failed_nodes>0</failed_nodes>
    <healthy_nodes>3</healthy_nodes>
</status>
```

```json
    "tee_config": {
        "tee_enable": false
```

`},`

```json
    "scaling_group": {
        "scaling_group_id": "asg-2zeieod8giqmov7z****",
        "internet_charge_type": "PayByTraffic",
        "ram_policy": "KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****",
        "instance_charge_type": "PayByBandwidth",
        "login_password": "********",
        "system_disk_category": "cloud_efficiency",
        "internet_max_bandwidth_out": 10,
        "security_group_id": "sg-2ze60ockeekspl3d****",
        "multi_az_policy": "BALANCE",
        "image_id": "aliyun_2_1903_x64_20G_alibase_20200529.vhd",
        "system_disk_size": 120,
        "platform": "AliyunLinux",
        "scaling_policy": "release",
        "data_disks": {
            "auto_snapshot_policy_id": "sp-2zej1nogjvovnz4z****",
            "encrypted": true,
            "size": 40,
            "category": "cloud_ssd"
```

`},`

```json
        "tags": {
            "value": "value",
            "key": "key"
```

`},`

```json
        "instance_types": ["ecs.n4.large"],
        "vswitch_ids": ["vsw-2ze3ds0mdip0hdz8i****"]
```

`},`

```json
    "kubernetes_config": {
        "runtime_version": "19.03.5",
        "cpu_policy": "none",
        "cms_enabled": true,
        "overwrite_hostname": false,
        "runtime": "docker",
        "user_data": "IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFDSyEi",
        "unschedulable": false,
        "node_name_mode": "customized,test.,5,.com",
        "labels": {
            "value": "value",
            "key": "key"
```

`},`

```json
        "taints": {
            "effect": "NoSchedule",
            "value": "value",
            "key": "key"
```

`},`

```json
    "auto_scaling": {
        "enable": true,
        "min_instances": 1,
        "max_instances": 10,
        "type": "cpu"
```

`},`

```json
    "nodepool_info": {
        "resource_group_id": "rg-acfmyvw3wjmb****",
        "created": "2020-09-27T19:14:09.156823496+08:00",
        "name": "default-nodepool",
        "region_id": "cn-beijing",
        "type": "ess",
        "is_default": true,
        "updated": "2020-09-27T20:37:46+08:00",
        "nodepool_id": "np615c0e0966124216a0412e10afe0****"
```

`},`

```json
    "status": {
        "serving_nodes": 3,
        "total_nodes": 3,
        "state": "active",
        "initial_nodes": 0,
        "removing_nodes": 0,
        "offline_nodes": 0,
        "failed_nodes": 0,
        "healthy_nodes": 3
```

2.3.5.6. Delete a node pool You can call the DeleteClusterNodepool operation to delete a node pool. This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c61da77e8bfbc4c4c999af2 b51b65**** | The ID of the cluster. |
| NodepoolId | String | Path | Yes | np30db56bcac7843dca90b9 99c8928**** | The ID of the node pool. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| request_id | String | 7263C978-3DBD-4E06-B319- 793B38A2**** | The ID of the request. |

```json
DELETE /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
    "ClusterId": "c61da77e8bfbc4c4c999af2b51b65****",
    "NodepoolId": "np30db56bcac7843dca90b999c8928****"
```

`XML` format

```xml
<request_id>7263C978-3DBD-4E06-B319-793B38A2****</request_id>
```

| JSON | format |
|---|---|
| { "request_id": "7263C978-3DBD-4E06-B319-793B38A2****" } |   |

### Templates

2.4.1. Create an orchestration template You can call the CreateTemplate operation to create an orchestration template. This operation uses only common request headers. For more information, see Common request parameters.

```
POST|PUT /templates HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| body | Struct | Body | No |   |   |
| template | String |   | Yes | service-account-template | The template content in the YAML format. |
| name | String |   | Yes | apiVersion: v1\nkind: ServiceAccount\nmetadata: \n name: test-sa | The template content in the YAML format. |
| description | String |   | No | this is test | The description of the template. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| template_type | String |   | No | kubernetes | The type of template. You can set the parameter to a custom value. If you set the parameter to kubernetes , the template is displayed on the Templates page in the console. If you set the parameter to compose , the template is not displayed in the console. We recommend that you set the parameter to kubernetes . Default value: compose . |
| tags | String |   | No | test | The label of the template. |

| kubernetes |   |
|---|---|
|   | compose |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| template_id | String | ba1fe77b-b01e-4640-b77e- 8f1b80e3**** | The ID of the template. |

```json
POST /templates HTTP/1.1
    "name": "service-account-template",
    "template": "apiVersion:v1\\nkind:ServiceAccount\\nmetadata:\\n name:test-sa",
    "tags": "test",
    "description": "this is test",
    "template_type": "kubernetes"
```

| XML | format |
|---|---|
| <template_id>ba1fe77b-b01e-4640-b77e-8f1b80e3****</template_id> |   |

| JSON | format |
|---|---|
| { "template_id": "ba1fe77b-b01e-4640-b77e-8f1b80e3****" } |   |

2.4.2. Delete an orchestration template You can call the DeleteTemplate operation to delete an orchestration template. This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /templates/[TemplateId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| TemplateId | String | Path | Yes | 20663627-81ee-4cfe-9b69- c96fcb84**** | The ID of the template. |

```json
DELETE /templates/[TemplateId] HTTP/1.1
    "TemplateId": "20663627-81ee-4cfe-9b69-c96fcb84****"
```

`XML` format

```
HTTP/1.1 200 OK
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.4.3. Query all orchestration templates You can call the DescribeTemplates operation to query all orchestration templates. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /templates HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| template_type | String | Query | Yes | kubernetes | The type of template. You can set this parameter to a custom value. If you set the parameter to kubernetes , the template is displayed on the Templates page in the console. If you set the parameter to compose , the template is not displayed on the Templates page in the console. Default value: kubernetes . |
| page_num | Long | Query | No | 1 | The number of the page to return. Default value: 1. |
| page_size | Long | Query | No | 10 | The number of entries to return on each page. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| page_info | Struct |   | The pagination details. |
| page_number | Long | 20 | The page number of the returned page. |
| page_size | Long | 3 | The maximum number of entries returned per page. |
| total_count | Long | 50 | The total number of entries returned. |
| templates | Array of template |   | The list of returned templates. |
| acl | String | private | The access control policy of the template. Valid values: private : The template is private. public : The template is public. shared : The template can be shared. Default value: private . |
| created | String | 2020-06-10T16:30:16+08:00 | The time when the template was created. |
| description | String | a web server | The description of the template. |
| id | String | 874ec485-e7e6-4373-8a3b- 47bde8ae**** | The ID of the template. |
| name | String | webserver | The name of the template. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| tags | String | kubernetes | The label of the template. By default, the value is the name of the template. |
| template | String | apiVersion: apps/v1\nkind: Deployment\nmetadata:\n name: nginx-deployment-basic\n labels:\n app: nginx\nspec:\n replicas: 2\n selector:\n matchLabels:\n app: nginx\n template:\n metadata:\n labels:\n app: nginx\n spec:\n containers:\n - name: nginx\n image: busybox:latest\n ports:\n - containerPort: 80 | The template content in the YAML format. |
| template_type | String | kubernetes | The type of template. This parameter can be set to a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If the parameter is set to compose , the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated. |
| template_with_hist_id | String | ad81d115-7c8b-47e7-a222- 9c28d7f6e588 | The ID of the parent template. The value of template_with_hist_id is the same for each template version. This allows you to manage different template versions. |
| updated | String | 2020-06-10T16:30:16+08:00 | The time when the template was updated. |

```
GET /templates HTTP/1.1
    "template\_type": "kubernetes"
```

| XML | format |
|---|---|
| <templates> <template>apiVersion: apps/v1\nkind: Deployment\nmetadata:\n name: nginx-deployment-basic\n labels:\n app: nginx\nspec:\n replicas: 2\n selector: \n matchLabels:\n app: nginx\n template:\n metadata:\n labels:\n app: nginx\n spec:\n containers:\n - name: nginx\n image: busybox:latest\n ports:\n - containerPort: 80</template> <template_with_hist_id>ad81d115-7c8b-47e7-a222-9c28d7f6e588</template_with_hist_id> <created>2020-06-10T16:30:16+08:00</created> <name>webserver</name> <description>a web server</description> <template_type>kubernetes</template_type> <acl>private</acl> <id>874ec485-e7e6-4373-8a3b-47bde8ae****</id> <updated>2020-06-10T16:30:16+08:00</updated> <tags>kubernetes</tags> </templates> <page_info> <page_number>20</page_number> <total_count>50</total_count> <page_size>3</page_size> </page_info> |   |

```json
    "templates": {
        "template": "apiVersion: apps/v1\\nkind: Deployment\\nmetadata:\\n name: nginx-deployment-basic\\n labels:\\n app: nginx\\nspec:\\n replicas:
2\\n selector:\\n matchLabels:\\n app: nginx\\n template:\\n metadata:\\n labels:\\n app: nginx\\n spec:\\n containers:\\n - name: nginx\\n image: bu sybox:latest\\n ports:\\n - containerPort: 80",
        "template_with_hist_id": "ad81d115-7c8b-47e7-a222-9c28d7f6e588",
        "created": "2020-06-10T16:30:16+08:00",
        "name": "webserver",
        "description": "a web server",
        "template_type": "kubernetes",
        "acl": "private",
        "id": "874ec485-e7e6-4373-8a3b-47bde8ae****",
        "updated": "2020-06-10T16:30:16+08:00",
        "tags": "kubernetes"
```

`},`

```json
    "page_info": {
        "page_number": 20,
        "total_count": 50,
        "page_size": 3
```

2.4.4. Query an orchestration template You can call the DescribeTemplateAttributeoperation to query the details of an orchestration template. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /templates/[TemplateId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| TemplateId | String | Path | Yes | 874ec485-e7e6-4373-8a3b- 47bde8a**** | The ID of the template. |
| template_type | String | Query | No | kubernetes | The type of template. The value can be a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If the value of the parameter is not kubernetes , the template is not displayed on the Templates page in the console. We recommend that you set the parameter to kubernetes . Default value: kubernetes . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| body | Array of body |   | The details of the template. |
| acl | String | private | The access control policy of the template. |
| created | String | 2020-09-16T19:21:29+08:00 | The time when the template was created. |
| description | String | test template | The description of the template. |
| id | String | 72d20cf8-a533-4ea9-a10d- e7630d3d**** | The ID of the template. When you update a template, a new template ID is generated. |
| name | String | web | The name of the template. |
| tags | String | sa | The label of the template. |
| template | String | apiVersion: V1\n*** | The template content in the YAML format. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| template_type | String | kubernetes | The type of template. The value can be a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If the value of the parameter is not kubernetes , the template is not displayed on the Templates page in the console. We recommend that you set the parameter to kubernetes . Default value: kubernetes . |
| template_with_hist_id | String | 874ec485-e7e6-4373-8a3b- 47bde8ae**** | The unique ID of the template. The value remains unchanged after the template is updated. |
| updated | String | 2020-09-16T19:21:29+08:00 | The time when the template was updated. |

```json
GET /templates/[TemplateId] HTTP/1.1
    "TemplateId": "874ec485-e7e6-4373-8a3b-47bde8a****"
```

| XML | format |
|---|---|
| <body> <template>apiVersion: V1\n***</template> <template_with_hist_id>874ec485-e7e6-4373-8a3b-47bde8ae****</template_with_hist_id> <created>2020-09-16T19:21:29+08:00</created> <name>web</name> <description>test template</description> <template_type>kubernetes</template_type> <acl>private</acl> <id>72d20cf8-a533-4ea9-a10d-e7630d3d****</id> <updated>2020-09-16T19:21:29+08:00</updated> <tags>sa</tags> </body> |   |

| JSON | format |
|---|---|
| { "body": { "template": "apiVersion: V1\\n***", "template_with_hist_id": "874ec485-e7e6-4373-8a3b-47bde8ae****", "created": "2020-09-16T19:21:29+08:00", "name": "web", "description": "test template", "template_type": "kubernetes", "acl": "private", "id": "72d20cf8-a533-4ea9-a10d-e7630d3d****", "updated": "2020-09-16T19:21:29+08:00", "tags": "sa" } } |   |

2.4.5. Update an orchestration template You can call the UpdateTemplate operation to update an orchestration template. This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /templates/[TemplateId] HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| TemplateId | String | Path | Yes | 72d20cf8-a533-4ea9-a10d- e7630d3d2708 | The ID of the template. |
| body | Struct | Body | No |   |   |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| template | String |   | No | service-account-template | The template content in the YAML format. |
| name | String |   | No | apiVersion: v1\nkind: ServiceAccount\nmetadata: \n name: test-sa | The template content in the YAML format. |
| description | String |   | No | this is test | The description of the template. |
| template_type | String |   | No | kubernetes | The type of template. You can set the parameter to a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If you set the parameter to compose , the template is not displayed in the console. We recommend that you set the parameter to kubernetes . Default value: compose . |
| tags | String |   | No | test | The label of the template. |

| kubernetes |   |
|---|---|
|   | compose . |

```json
PUT /templates/[TemplateId] HTTP/1.1
    "name": "service-account-template",
    "template": "apiVersion:v1\\nkind:ServiceAccount\\nmetadata:\\n name:test-sa",
    "tags": "test",
    "description": "this is test",
    "template_type": "kubernetes"
HTTP/1.1 200 OK
```

### Add-ons

2.5.1. Install a component in a cluster You can call the InstallClusterAddons to install a component in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/components/install HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961451182edac d74faf**** | The ID of the cluster. |
| body | Array | Body | No |   | The request body parameters. |
| config | String |   | No | {\"IngressDashboardEnable d\":\"true\",\"sls_project_n ame\":\"your_sls_project_n ame\"}"} | The component configurations. |
| name | String |   | Yes | ags-metrics-collector | The name of the component. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| version | String |   | Yes | v1.0.0.2-cc3b2d6-aliyun | The version of the component. Not e You can call the DescribeClusterAddonsVersion operation to query the version of the component. For more information, see Query the details of the components in a cluster. |

```json
POST /clusters/[ClusterId]/components/install HTTP/1.1
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

| XML | format |
|---|---|
| HTTP/1.1 200 OK |   |

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.5.2. Query the details of the components in a cluster You can call the DescribeAddons operation to query the details of the components that are installed in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/components/metadata HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| region | String | Query | Yes | cn-beijing | The ID of the region where the cluster is deployed. |
| cluster_type | String | Query | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ComponentGroups | Array of ComponentGroup |   | The list of the returned components. |
| group_name | String | storage | The name of the component group. |
| items | Array of item |   | The names of the components in the component group. |
| name | String | flexvolume | The name of the component. |
| StandardComponents | Struct |   | Standard components. |
| key | Struct |   | The details of the standard components. |
| description | String | test | The description of the component. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| disabled | Boolean | false | Indicates whether the automatic installation of the component is disabled. By default, some optional components, such as components for logging and Ingresses, are installed when a cluster is created. You can set this parameter to disable the automatic installation of a component. Valid values: true : disables the automatic installation of a component. false : allows the automatic installation of the component. |
| name | String | ack-arena | The name of the component. |
| required | String | false | Indicates whether the component is required in a Container Service cluster. Valid values: true : The component is required and must be installed when a cluster is created. false : The component is optional. After a cluster is created, you can go to the Add-ons page to install the component. |
| version | String | 0.5.0 | The version of the component. |

```json
GET /clusters/components/metadata HTTP/1.1
    "region": "cn-beijing"
```

| XML | format |
|---|---|
| <StandardComponents> <key> <name>ack-arena</name> <description>test</description> <disabled>false</disabled> <version>0.5.0</version> <required>false</required> </key> </StandardComponents> <ComponentGroups> <group_name>storage</group_name> <items> <name>flexvolume</name> </items> </ComponentGroups> |   |

| JSON | format |
|---|---|
| { "StandardComponents": { "key": { "name": "ack-arena", "description": "test", "disabled": false, "version": "0.5.0", "required": false } }, "ComponentGroups": { "group_name": "storage", "items": { "name": "flexvolume" } } } |   |

2.5.3. Query components You can call the DescribeClusterAddonsVersion operation to query the components that are installed in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/components/version HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e2961451182edac d74faf**** | The ID of the cluster. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| key | Struct |   | The details of the component. |
| can_upgrade | Boolean | false | Indicates whether the component is upgradable. Valid values: true : The component is upgradable. false : The component is not upgradable. |
| changed | String | false | Indicates whether the component is upgraded. Valid values: true : The component is upgraded. false : The component is not upgraded. |
| component_name | String | ack-node-problem-detector | The name of the component. |
| exist | Boolean | true | Indicates whether the component was installed. Valid values: true : The component was installed. false : The component was not installed. |
| message | String | A plug-in that detects exceptions and reports them to the Kubernetes event center. | Additional information about whether the component is upgradable. |
| next_version | String | 1.2.1 | The version to which the component can be upgraded. |
| policy | String | overwrite | The upgrade policy of the component. overwrite : The component configurations of the later version overwrite those of the current version. Default value: overwrite . |
| ready_to_upgrade | String | false | Indicates whether the component meets the upgrade conditions. Valid values: true : The component meets the upgrade conditions. false : The component does not meet the upgrade conditions. |
| required | Boolean | false | Indicates whether the component is required in the cluster. Valid values: true : The component is required in the cluster. false : The component is not required in the cluster. |
| value | String | npd:\n # Custom monitor definitions to add to Node Problem Detector **** | The custom parameter setting. When you install a component, you can customize parameter settings for the component. |
| version | String | 1.2.1 | The current version of the component. |

```json
GET /clusters/[ClusterId]/components/version HTTP/1.1
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

`XML` format

```xml
<key>
      <exist>true</exist>
      <component_name>ack-node-problem-detector</component_name>
      <can_upgrade>false</can_upgrade>
      <ready_to_upgrade>false</ready_to_upgrade>
      <message>A plug-in that detects node exceptions and reports them to the Kubernetes event center.</message>
      <value>npd:\n # Custom monitor definitions to add to Node Problem Detector ****</value>
      <version>1.2.1</version>
      <required>false</required>
      <policy>overwrite</policy>
      <changed>false</changed>
      <next_version>1.2.1</next_version>
</key>
```

| JSON | format |
|---|---|
| { "key": { "exist": true, "component_name": "ack-node-problem-detector", "can_upgrade": false, "ready_to_upgrade": false, "message": "A plug-in that detects node exceptions and reports them to the Kubernetes event center.", "value": "npd:\\n # Custom monitor definitions to add to Node Problem Detector ****", "version": "1.2.1", "required": false, "policy": "overwrite", "changed": false, "next_version": "1.2.1" } } |   |

2.5.4. Query the upgrade status of components in a cluster You can call the DescribeClusterAddonsUpgradeStatus operation to query the upgrade status of the specified components in a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
GET /clusters/[ClusterId]/components/upgradestatus HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c23421cfa74454bc8b37163f d19af**** | The ID of the cluster. |
| componentIds | List<String> | Query | Yes | ["metric-server"] | The name of the component. |

```json
GET /clusters/[ClusterId]/components/upgradestatus HTTP/1.1
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "componentIds": "[metric-server"]
```

| XML | format |
|---|---|
| HTTP/1.1 200 OK |   |

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.5.5. Upgrade a component in a cluster You can call the UpgradeClusterAddons operation to upgrade a specified component in a cluster to the required version. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/components/upgrade HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cf4299b79b3e34226abfdc8 0a4bda**** | The ID of the cluster. |
| body | Array | Body | No |   | The request parameters for the operation. |
| component_name | String |   | Yes | coredns | The name of the component. |
| next_version | String |   | Yes | 1.6.7 | The required version. You can call the DescribeClusterAddonsVersion operation to query the version to which the component can be upgraded. |
| version | String |   | No | v1.6.2 | The current version of the component. |

```json
POST /clusters/[ClusterId]/components/upgrade HTTP/1.1
    "ClusterId": "cf4299b79b3e34226abfdc80a4bda****"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

2.5.6. Uninstall components from a cluster You can call the UnInstallClusterAddons operation to uninstall components from a cluster. This operation uses only common request headers. For more information, see Common request parameters.

```
POST /clusters/[ClusterId]/components/uninstall HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c5b5e80b0b64a4bf6939d2d 8fbbc5**** | The ID of the cluster. |
| addons | Array | Body | No |   | The list of components that you want to uninstall. The list is an array. |
| name | String |   | No | ack-node-problem- detector | The name of the component. |

```json
POST /clusters/[ClusterId]/components/uninstall HTTP/1.1
    "ClusterId": "c5b5e80b0b64a4bf6939d2d8fbbc5****"
```

| JSON | format |
|---|---|
| HTTP/1.1 200 OK |   |

## Appendixes

### Use the ASAPI gateway to call API operations

You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references. Procedure
1. Obtain the ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain the ASAPI SDK. For more information, see Obtain the ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI.
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for calling an API operation. Not e We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.
4. Obtain the region ID.
Obtain the region ID that is required for calling an API operation.
5. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Co nsole Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Cons ole Developer Guide. Not e When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs-resourcegroupid> parameters. This allows you to query specified resources. If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default. If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.
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
    parameters.put("Product", "Ecs");// Specify the POP code, which is the same as the POP code in the corresponding API directory.
    parameters.put("Action", "DescribeInstances"); // Specify the name of the API operation. Use the same letter case as the corresponding API di
rectory.
    parameters.put("Version", "2014-05-26"); // Specify the API version.
    // Specify the region ID that you obtained.
    parameters.put("RegionId", "xxx");
    // Specify your AccessKey ID and AccessKey secret.
    parameters.put("AccessKeyId", "xxx");
    parameters.put("AccessKeySecret", "xxx");
    // Add the parameters based on the API reference. Take note that the parameters are case-sensitive.
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
    System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), SerializerFeature.PrettyFormat));
```

### Use the ASAPI gateway to make API calls

3.2.1. Obtain the endpoint of ASAPI This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI). This topic also describes how to verify the endpoint. Methods Method 1: Use Registration Vars of Services to obtain an endpoint
1. Log on to the Apsara Infrastructure Management Console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click Product s. iii. Choose Plat f orms > Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` . In the report list that appears, click the name of the report.
4. On the Regist rat ion Vars of Services page, click the
icon to the right of Service and enter `asapi` in the search box.
5. Find the asapi service, right-click the service in the Service Regist rat ion column, and then select Show More from the shortcut menu.
In the Det ails dialog box, obtain the value of asapi.public.endpoint .
6. Generate an endpoint for ASAPI in the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

Method 2: Use cluster resources to generate an endpoint
1. Log on to the Apsara Infrastructure Management Console.
2. Go to the cluster operations page.
i. In the left-side navigation pane, choose Operat ions > Clust er Operat ions. ii. In the Clust er search box, enter `ascm` . iii. In the Act ions column, click Operat ions.
3. Obtain the domain value.
i. Click the Clust er Resources tab. ii. In the Name field, search for `asapi_dns_public` . iii. In the Applicat ion Paramet er column, click Det ails. In the Applicat ion Paramet er message, obtain the value of the domain parameter.
4. Generate an endpoint for ASAPI in the following format:

```
https://<domain>/asapi/v3
```

Method 3: Concatenate strings to generate an endpoint You can concatenate strings to generate an endpoint in the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

Not e
1. Replace <region> with your actual region ID.
2. Replace <internet-
domain> with the root domain of your Apsara Stack service. To obtain the root domain, contact Apsara Stack O&M engineers. Make sure that you use the internetdomain parameter instead of the intranet-domain parameter. Example: if the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint is used as a reference:

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

Verify the endpoint Enter the following code. If you cannot access the endpoint, the endpoint is unavailable. You can use the historical endpoint.

```bash
 curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k
```

Not e ${global:region} and ${global:internet-domain} are variables. You must replace these variables with the actual values that you obtained. Available endpoint example: Unavailable endpoint example: Historical endpoint Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-domain` and is in the following format:

```
 http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3
```

Not e ${global:region} and ${global:intranet-domain} are variables. You must replace these variables with the actual values that you obtained. Procedure To obtain the actual values of the ${global:region}, ${global:internet-domain}, and ${global:intranet-domain} variables, perform the following steps:
1. In the address bar, enter region-id.aso.intranet-domain-id.com URL and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the current page.
2. Enter your username and password.
Not e Obtain the username and password that are used to log on to the Apsara Unimanager Operations Console from the deployment personnel or an administrator. The first time that you log on to the Apsara Uni-manager Operations Console, change the password of your username as prompted. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters, such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password must be 10 to 20 characters in length.
3. Click Log On to log on to the Apsara Uni-manager Operat ions Console.
4. In the top navigation bar, choose Product s > Plat f orms > Apsara Inf rast ruct ure Management Framework to go to the Apsara Infrastructure Management pag
5. In the left-side navigation pane, choose Operat ions > Clust er Operat ions.
6. On the Clust er Operat ions page, enter ascm-A in the Cluster field and click the search icon. Click the cluster name in the Clust er column.
7. Click the Clust er Conf igurat ion tab.
8. On the File Inf o tab of Clust er Conf igurat ion, click kv.conf .
9. In the right window of the displayed page, press Ctrl+F to search for the values of the region, internet-domain, and intranet-domain parameters.

| Replace | ${global:region} | w |
|---|---|---|
| ${global:intranet-domain} |   |   |

Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internet-domain value, and ${global:intranet-domain} with the obtained intranet-domain value. Not e Do not include ${global:} in the endpoint of ASAPI that you want to use. 3.2.2. Obtain the ASAPI SDK Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. Public environment If you use the public environment, you can go to the Apsara Stack documentation page and download the ASAPI SDK in the Ot her Resources section at the lower part of the page. Private environment If you use the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the ASAPI SDK in the Ot her Resources section. ASAPI SDK for Java

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

ASAPI SDK for Python

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

3.3.1. What is STS? Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token. Use an STS token to assume a RAM role An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources. Benefits STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization. 3.3.2. AssumeRole Obtains a Security Token Service (STS) token to assume a RAM role. In this operation, an Alibaba Cloud account is used as the trusted entity of the Resource Access Management (RAM) role.

| Paramet er | T ype | Required | Example | Descript ion |
|---|---|---|---|---|
| Act ion | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456789012****:rol e/adminrole | The Alibaba Cloud Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Alibaba Cloud account. |
| RoleSessionName | String | Yes | alice | The custom name of the role session. You can specify the value of this parameter based on your business requirements. In most cases, this parameter is set to the identity of the user who calls the operation, such as the username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user- specific auditing. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | The policy that specifies the permissions of the returned STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The value of the parameter must be 1 to 1,024 characters in length. |

Response parameters

| Paramet er | T ype | Example | Descript ion |
|---|---|---|---|
| Request Id | String | 6894B13B-6D71-4EF5-88FA- F32781734A7F | The ID of the request. |
| Credent ials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ***************************************** | The AccessKey secret. |
| Securit yT oken | String | ******** | The STS token. |
| Expirat ion | String | 2015-04-09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789012****:role/ad minrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495****:alice | The ID of the temporary identity that you use to assume the RAM role. |

Add Project Object Model (POM) dependencies The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

Call an API operation to obtain the STS AccessKey triplet. In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the triplet.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of the STS token. In most cases, the STS token is in the following format: sts-vpc.${gl
obal:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify in this API operation for the role session. It is a business parameter.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtain in the preceding step for the RAM role.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS triplet.
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
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and secret in the STS triplet that you obtain in the pre
ceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "<yourStsAccessKeySecret>");
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
        // Replace "<yourStsToken>" with the STS token in the STS triplet that you obtain in the preceding step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Specify the resource set ID. It is optional.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Specify the organization ID. It is required.
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

| HT T P st at us code | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the format of the RoleSessionName parameter is invalid. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_). |
| 400 | InvalidParameter.DurationSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the Durat ionSeconds parameter is invalid. The value must be greater than or equal to 900 and less than or equal to the MaxSessionDurat ion value. |
| 400 | InvalidParameter.PolicyGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the specified policy is invalid. |

| Container Service for Kubern | etes | D | eveloper Guide·Appendixes |   |
|---|---|---|---|---|

| HT T P st at us code | Error code | Error message | Descript ion |
|---|---|---|---|
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |
