---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 185
source_pdf: "b6812a23b5cab52a_Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Developer Guide 20260828.pd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20ACK/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Container%20Service%20for%20Kubernetes%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Container Service for Kubernetes Developer Guide 20260828

## Table of Contents

- 1 SDK reference
  - 1.1 Preparations
    - 1.1.1 Log on to OpenAPI Explorer
    - 1.1.2 View the information about an operation
    - 1.1.3 Obtain an AccessKey pair
    - 1.1.4 Obtain an STS AccessKey pair
    - 1.1.5 Obtain the values of common header parameters
    - 1.1.6 Obtain the information and the endpoint of an API operation
    - 1.1.7 Obtain the Container Service SDK package
  - 1.2 Examples of using Container Service SDK for Java
    - 1.2.1 Install Container Service SDK for Java
    - 1.2.2 Use Container Service SDK for Java
    - 1.2.3 Use CommonRequest
  - 1.3 Examples of using Container Service SDK for Python
    - 1.3.1 Install Container Service SDK for Python
    - 1.3.2 Use Container Service SDK for Python
    - 1.3.3 Use CommonRequest
  - 1.4 Examples of using Container Service SDK for Go
    - 1.4.1 Install Container Service SDK for Go
    - 1.4.2 Use Container Service SDK for Go
    - 1.4.3 Use CommonRequest
- 2 Cluster API list
  - 2.1 Container Service API invocation
    - 2.1.1 Overview
    - 2.1.2 Common parameters
    - 2.1.3 Request syntax
    - 2.1.4 Response parameters
    - 2.1.5 Sign API requests
  - 2.2 Clusters
    - 2.2.1 Create an ACK cluster
    - 2.2.2 Delete a cluster
    - 2.2.3 Query the kubeconfig file of a cluster
    - 2.2.4 Query
      - 2.2.4.1 Query information about all clusters
      - 2.2.4.2 DescribeClusterDetail
      - 2.2.4.3 Query resources in a cluster
      - 2.2.4.4 Query the namespaces of a cluster
      - 2.2.4.5 Query the agent of a cluster
      - 2.2.4.6 Query resource quotas
      - 2.2.4.7 Query the logs of a cluster
      - 2.2.4.8 Query information about a Kubernetes version supported by Container Service
    - 2.2.5 Modify
      - 2.2.5.1 Modify cluster configurations
      - 2.2.5.2 Modify the labels of a cluster
    - 2.2.6 Upgrade
      - 2.2.6.1 Upgrade a cluster
      - 2.2.6.2 Query the upgrade status of a cluster
      - 2.2.6.3 Suspend the upgrade of a cluster
      - 2.2.6.4 Cancel the upgrade of a cluster
      - 2.2.6.5 Resume the upgrade of a cluster
  - 2.3 Nodes
    - 2.3.1 Query nodes in a cluster
    - 2.3.2 Remove nodes from a cluster
    - 2.3.3 Add existing ECS instances to a cluster
    - 2.3.4 Manually add existing instances to a cluster
    - 2.3.5 Node pools
      - 2.3.5.1 Create a node pool
      - 2.3.5.2 Synchronize node pool information
      - 2.3.5.3 Scale out a node pool
      - 2.3.5.4 Modify the configuration of a node pool
      - 2.3.5.5 Query node pools
      - 2.3.5.6 Query the details of a node pool
      - 2.3.5.7 Delete a node pool
  - 2.4 Templates
    - 2.4.1 Create an orchestration template
    - 2.4.2 Delete an orchestration template
    - 2.4.3 Query all orchestration templates
    - 2.4.4 Query an orchestration template
    - 2.4.5 Update an orchestration template
  - 2.5 Add-ons
    - 2.5.1 Install a component in a cluster
    - 2.5.2 Query the details of the components in a cluster
    - 2.5.3 Query components
    - 2.5.4 Query the upgrade status of components in a cluster
    - 2.5.5 Upgrade a component in a cluster
    - 2.5.6 Uninstall components from a cluster
  - 2.6 Policies
    - 2.6.1 Deploy a policy instance in an ACK cluster
    - 2.6.2 DescribePolicyInstancesStatus
    - 2.6.3 Update a policy instance in an ACK cluster
    - 2.6.4 Query policy instances that are deployed in an ACK cluster
    - 2.6.5 Query information about policies in an ACK cluster
    - 2.6.6 Query information about a policy
    - 2.6.7 DescribePolicies
    - 2.6.8 Delete policy instances from an ACK cluster
- 3 Appendixes
  - 3.1 STS overview
    - 3.1.1 What is STS?
    - 3.1.2 Obtain an STS token

## 1 SDK reference

### 1.1 Preparations

#### 1.1.1 Log on to OpenAPI Explorer

You can log on to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of a
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password from an administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Re-enter the username and password as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Application Services > OpenAPI**
**Explorer**.

#### 1.1.2 View the information about an operation

**operation**

This topic describes how to view information about an API operation. The information includes service names, API operation names, and API versions. The information is required when you use an SDK to call API operations.

**Background information**

The API operations on the API Directory page are only for reference. For information about how to call API operations, see the developer guide of the corresponding cloud service. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press the Enter key.
2. On the login page, enter your username and password.
You can obtain the username and password that are used to log in to the Apsara Unimanager Management Console from the operations administrator.

> **Note:** **First login**
> The first time that you log on to the Apsara Uni-manager Management Console, you need to change the password of your account. The password must be 10 to 32 characters in length. It must contain all of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include: ! @ # $ %
> **Forgotten password**
> If you have forgotten your password, click Forgot Password. On the page that appears, enter the username of your account, the email address that was used to create the account, and the CAPTCHA code. Then, the system sends a link for resetting the password to the specified email address.

3. Click **Log In**.
4. In the top navigation bar, choose **Products > Application Services > OpenAPl**
**Explorer**.
5. In the **OpenAPI Explorer** page, choose **API Integration > API Debugging**.
6. In the left navigation bar, select the required cloud service.
7. In the **Version** drop-down list, select the required API version.
8. Below the API list, you can view all API interfaces for the current version.

#### 1.1.3 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

#### 1.1.4 Obtain an STS AccessKey pair

This topic describes how to use STS to make API calls.

**Background information**

Alibaba Cloud Security Token Service (STS) allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and an STS token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS?.

**Procedure**

1. Obtain the `RAM role` that is assigned to the current user.
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click
**User Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, you can obtain information about the `RAM role` that is assigned to the current user.
2. Obtain an STS AccessKey 3-tuple.

> **Note:** You must replace the following fields with the actual values. Delete the angle brackets (<>) before you submit the code.
> <yourRegionID>: Replace the field with the actual region ID.
> <yourAccessKeyID>: Replace the field with the AccessKey ID of the current user.
> <yourAccessKeySecret>: Replace the field with the AccessKey secret of the current user.
> <yourRoleSessionName>: Replace the field with the actual session name.
> <yourRoleArn>: Replace the field with the Alibaba Cloud Resource Name (ARN) of the RAM role that is assigned to the current user.
> <sts.aliyuns.com>: Replace the field with the actual endpoint of STS.

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the act
ual values.
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
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the actual endpoint of STS. The format of an en
dpoint of STS is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // The business parameter. Replace <yourRoleSessionName> with the actual session
name.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the RAM role ARN that is obtained in the previous
step.
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

3. Use the STS AccessKey 3-tuple to call the `DescribeUserQuota` operation of Container
Service. The following code provides an example:

> **Note:** You must replace the following fields with the actual values. Delete the angle brackets (<>) before you submit the code.
> <yourRegionID>: Replace the field with the actual region ID.
> <yourAccessKeyID>: Replace the field with the AccessKey ID of the current user.
> <yourAccessKeySecret>: Replace the field with the AccessKey secret of the current user.
> <yourStsToken>: Replace the field with the STS token of the STS AccessKey 3- tuple.
> <yourResourceGroupID>: Replace the field with the actual resource set ID.
> <yourOrganizationID>: Replace the field with the actual organization ID.

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

#### 1.1.5 Obtain the values of common header parameters

**parameters**

You must provide multiple header parameters when you call API operations. This topic describes the header parameters and how to obtain the values of the header parameters. This topic also describes the response parameters of specific header parameters after you call Apsara Stack API operations.

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the Container Service cluster for which you want to call API operations. For more information about how to obtain cluster IDs, see Obtain a Container Service cluster ID. |

**Query a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization that you want to view.
5. You can obtain the region ID in the **Regions** list.

**Obtain an organization ID**

You can call the GetOrganizationList operation to obtain the organization ID. For more information, see the GetOrganizationList topic of the Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see the ListResourceGroup topic of the Apsara Uni-manager Management Console Developer Guide.

**Obtain a Container Service cluster ID**

You can obtain a Container Service cluster ID on the Clusters page of the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Container Service**
**for Kubernetes**.
3. In the left-side navigation pane, click **Clusters**.
4. On the **Clusters** page, click the name of the cluster that you want to manage.
5. On the **Cluster Information** page, click the **Basic Information** tab.
On the **Basic Information** tab, you can obtain the cluster ID.

**Response parameters**

The following response parameters are returned by default when you call list-type API operations for cloud product resource instances.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

#### 1.1.6 Obtain the information and the endpoint of an API operation

**endpoint of an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

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

#### 1.1.7 Obtain the Container Service SDK package

**package**

When you call API operations in Apsara Stack by using the Portable OpenAPI Proxy (POP) gateway, you must use the SDK of the corresponding cloud service. This topic describes how to obtain Apsara Stack SDKs. An SDK includes code and examples. You can create cloud applications by using an SDK for the programming language that you require. The SDKs for Java, Python, and Go are provided. You can select the SDKs from Alibaba Cloud SDKs based on your business requirements.

> **Note:** We recommend that you use an SDK for Java, Python, or Go. If you use SDKs for other programming languages, the SDKs may be incompatible with your system.

We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack.

### 1.2 Examples of using Container Service SDK for Java

**Service SDK for Java**

#### 1.2.1 Install Container Service SDK for Java

This topic describes how to install Container Service SDK for Java.

**Environment requirements**

You must use Java 6 or later. To install the core library of Container Service SDK for Java, you can add the following dependencies to a Project Object Model (POM) file:

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.21</version>
</dependency>
```

**Install Container Service SDK for Java**

To install Container Service SDK for Java by using Apache Maven, add the following dependencies to the project file:

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-cs</artifactId>
  <version>4.8.1</version>
</dependency>
```

#### 1.2.2 Use Container Service SDK for Java

This topic describes how to use Container Service SDK for Java.

**Procedure**

1. Initialize the com.aliyuncs.profile.DefaultProfile object.
The Profile object contains parameters such as `your-access-key-id` , `your-access-key-` `secret` , and `your-region-id` .

```
IClientProfile profile = DefaultProfile.getProfile("<your-region-id>", "<your-accesskey-id>", "<your-access-key-secret>");
```

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

6. Call the corresponding get method in the response to obtain the values of response
parameters.

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

**Sample code**

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.alibaba.fastjson.JSON; import java.util.*; import com.aliyuncs.cs.model.v20151215.*; public class DescribeImages {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
"LTAjVUwKznS*****", "BNPO1zoNSi484oizGM9fzzwJJ*****");
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        DescribeEventsRequest request = new DescribeEventsRequest();
        request.setcluster_id("test"); // Specify the parameter based on your
requirements.
        request.settype("test"); // Specify the parameter based on your requirements.
        request.setpage_size("1"); // Specify the parameter based on your requirements.
        request.setpage_number("1"); // Specify the parameter based on your
requirements.
        try {
            DescribeEventsResponse response = client.getAcsResponse(request);
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

#### 1.2.3 Use CommonRequest

To use an SDK for POP Java to call the API of an Apsara Stack service, you must first learn the remote procedure call (RPC) or resource-oriented architecture (ROA) API style.

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample RPC call contains the service (ACK), API operation (CreateCluster), and version (2015-12-15) information.

```java
package com.aliyun.sample; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    /**
     * The sample API call listed in this topic is for reference only. For more informa
tion, refer to the Getting started topic.
```

`*/`

```
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("cn-qingdao-env8e-d01", "<yo
ur-access-key-id>", "<your-access-key-secret>");
        /** Use a Security Token Service (STS) token.
        DefaultProfile profile = DefaultProfile.getProfile(
            "cn-qingdao-env8e-d01",           // The region ID.
            "<your-access-key-id>",       // The AccessKey ID of the RAM user.
            "<your-access-key-secret>",   // The AccessKey Secret of the RAM user.
            "<your-sts-token>");          // STS Token
        **/
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        You can configure the HTTP proxy based on your business requirements.
        You can configure the HTTP proxy in the following way:
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
Specif theIPaddressandportofthepro
```

```
        Specify the IP address and port of the proxy.
```

`*/`

```
        // Configure the connection timeout period. Unit: milliseconds.
        // clientConfig.setConnectionTimeoutMillis(1000L);
        // Configure the read request timeout period. Unit: milliseconds.
        // clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request.
        CommonRequest request = new CommonRequest();
        // Configure the API parameters.
        request.setSysProduct("CS");
        request.setSysVersion("2015-12-15");
        request.setSysUriPattern("/clusters");
        // Specify the endpoint of the API.
        request.setSysDomain("cs.env8e-b.com");
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        /**
        When you initiate an API request based on the core library of Alibaba Cloud SDK
, you can configure the Path, Query, Body, and Header parameters.
        The Path parameters are used to replace variables in the UriPattern of the requ
est.
        The Query parameters are used to set the URL of the request (GET request in mos
t cases).
        The Body parameters are used to configure the HTTP content of the request (POST
or PUT request in most cases). You must set the Body parameters together with the HTTP Content-Type parameter. You can set the HTTP Content-Type parameter to JSON or FORM.
        The Header parameter is used to set the HTTP headers of the request.
```

`*/`

```java
        // Configure headers.
        // Configure the identifier. This parameter is required and used only for ident
ification. You can set this parameter based on your business requirements.
        request.putHeadParameter("x-acs-caller-sdk-source","<your-sdk-source>");
        // When you call an API operation in Apsara Stack, you must configure multiple
common Header parameters, such as x-acs-regionid, x-acs-organizationid, x-acs-resourceg roupid, and x-acs-instanceid. For more information, see Obtain the value of common head er parameters.
        // Configure operation-specific parameters.
        request.setHttpContentType(FormatType.FORM);
        try {
            // Initiate the request and obtain the response.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

> **Important:** By default, if you send HTTPS requests, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is thrown.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following setting:
> Java

### 1.3 Examples of using Container Service SDK for Python

**Service SDK for Python**

#### 1.3.1 Install Container Service SDK for Python

**Python**

This topic describes how to install Container Service SDK for Python.

**Environment requirements**

You must use Python 2.7 or 3.x. Install Container Service SDK for Python by using the pip tool:

```
pip install alibabacloud_tea_openapi
```

**Install Container Service SDK for Python**

PyPI PIP

```
pip install aliyun-python-sdk-cs==4.8.1
```

PyPI Anaconda

```
conde install aliyun-python-sdk-cs=4.8.1
```

#### 1.3.2 Use Container Service SDK for Python

This topic describes how to use Install Container Service SDK for Python.

**Procedure**

1. Instantiate a client object from the AcsClient class of the aliyunsdkcore package.
The client object contains the `your-access-key-id` , `your-access-key-secret` , and `your-region-id` parameters.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    ak="<your-access-key-id>",
    secret="<your-access-key-secret>",
    region_id='<region-id>'
```

`)`
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

5. You can use the try...except... method to handle exceptions that occur on clients and
servers. Handle server errors

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

**Sample code**

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcs.request.v20151215.DescribeEventsRequest import DescribeEventsRequest client = AcsClient('<your-access-key-id>', '<your-access-key-secret>', 'cn-hangzhou') // Create an API request and configure the parameters. request = DescribeEventsRequest() // Specify this parameter based on your requirements. request.set_cluster_id("test") // Specify this parameter based on your requirements. request.set_type("test") // Specify this parameter based on your requirements. request.set_page_size("1") // Specify this parameter based on your requirements. request.set_page_number("1") response = client.do_action_with_exception(request) // Print response parameters as required.
# python2:  print response
print(str(response, encoding='utf-8'))
```

#### 1.3.3 Use CommonRequest

To use an SDK for POP Python to call the API of an Apsara Stack service, you must first learn the remote procedure call (RPC) or resource-oriented architecture (ROA) API style.

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample RPC call contains the service (ACK), API operation (CreateCluster), and version (2015-12-15) information.

```bash
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential
# The sample API call listed in this topic is for reference only. For more information,
refer to the Getting started topic. credentials = AccessKeyCredential('<your-access-key-id>', '<your-access-key-secret>')
# Use a Security Token Service (STS) token.
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>',
'<your-sts-token>')
# Configure the timeout period of AcsClient connection requests. Unit: milliseconds.
client = AcsClient(region_id='cn-qingdao-env8e-d01', credential=credentials, timeout=10000)
# Create an API request.
request = CommonRequest()
# Configure the API parameters.
request.set_product("CS") request.set_version('2015-12-15') request.set_uri_pattern("/clusters")
# Specify the endpoint of the API.
request.set_domain('cs.env8e-b.com')
# Specify the request method.
request.set_method('POST')
# Specify the request protocol.
request.set_protocol_type('http')
# When you initiate an API request based on the core library of Alibaba Cloud SDK, you
can configure the Path, Query, Body, and Header parameters.
# The Path parameters are used to replace variables in the UriPattern of the request.
# The Query parameters are used to set the URL of the request (GET request in most case
s).
# The Body parameters are used to configure the HTTP content of the request (POST or PU
T request in most cases). You must set the Body parameters together with the HTTP Conte nt-Type parameter. You can set the HTTP Content-Type parameter to JSON or FORM.
# The Header parameter is used to set the HTTP headers of the request.
# Configure headers.
Configure the identifier. This parameter is required and used only for identification. You can set this parameter based on your business requirements. request.add_header("x-acs-caller-sdk-source","<your-sdk-source>")
# When you call an API operation in Apsara Stack, you must configure multiple common He
ader parameters, such as x-acs-regionid, x-acs-organizationid, x-acs-resourcegroupid, a nd x-acs-instanceid. For more information, see Obtain the value of common header parame ters.
# Configure operation-specific parameters.
request.set_content_type('application/x-www-form-urlencoded')
# Initiate the request and obtain the response.
response = client.do_action_with_exception(request)
```

```python
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

**Configure a proxy**

You can configure the HTTP_PROXY and HTTPS_PROXY environment variables when you call API operations. Sample code:

```bash
# HTTPS proxy
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# HTTP proxy
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS**

This section describes related configurations for sending HTTP requests.

**Enable HTTPS**

By default, the SDKs use HTTPS as the request protocol.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Set the protocol to HTTPS. client.do_action_with_exception(request)
```

**Disable certificate verification**

> **Important:** By default, if you send an HTTPS request, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is thrown.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can set the `verify` parameter to false.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify=False  # Disable SSL certificate verification.
```

`)`

**Enable certificate verification**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

`)`

### 1.4 Examples of using Container Service SDK for Go

**Service SDK for Go**

#### 1.4.1 Install Container Service SDK for Go

This topic describes how to install Container Service SDK for Go.

**Environment requirements**

You must use Go 1.10.x or later. Install the core library of Container Service SDK for Go

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Install Container Service SDK for Go**

Install Container Service SDK for Go by running the go get command:

```
go get github.com/aliyun/alibaba-cloud-sdk-go/services/CS
```

#### 1.4.2 Use Container Service SDK for Go

This topic describes how to use Container Service SDK for Go.

**Procedure**

1. Add the following dependencies:

```java
import (
  cs "github.com/aliyun/alibaba-cloud-sdk-go/services/cs"
```

`)`
2. Instantiate a client object from the cs.NewClientWithAccessKey class.
NewClientWithAccessKey contains the `your-access-key-id` , `your-access-key-secret` , and `your-region-id` parameters.

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

**Sample code**

```java
package main import (
  "fmt"
  cs "github.com/aliyun/alibaba-cloud-sdk-go/services/cs"
```

`)`

```
func main() {
  client, err := cs.NewClientWithAccessKey("cn-hangzhou", "<yourAccessKeyID>", "<yourAc
cessKeySecret>")
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
  // Print response parameters as required. In this example, the RequestId parameter is
printed.
  fmt.Println(response.RequestId)
```

#### 1.4.3 Use CommonRequest

This topic describes how to work with the SDK for POP Go.

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample RPC call contains the service (ACK), API operation (CreateCluster), and version (2015-12-15) information.

```java
package main import (
 "encoding/json"
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
/**
 * The sample API call listed in this topic is for reference only. For more information
, refer to the Getting started topic.
```

`*/`

```
func main() {
 config := sdk.NewConfig()
 credential := credentials.NewAccessKeyCredential("<your-access-key-id>", "<your-access
-key-secret>")
    /* Use a Security Token Service (STS) token.
    credential := credentials.NewStsTokenCredential("<your-access-key-id>", "<your-acce
ss-key-secret>", "<your-sts-token>")
```

`*/`

```
 client, err := sdk.NewClientWithOptions("cn-qingdao-env8e-d01", config, credential)
 if err != nil {
  panic(err)
 /**
  * Configure an HTTP proxy in the following way based on your business requirements:
  * client.SetHttpProxy("<http://192.168.XX.XX:33XX>")
  * Specify the IP address and port of the proxy.
```

`*/`

```
 // Create an API request.
 request := requests.NewCommonRequest()
 // Specify the timeout period of connections.
 // request.SetConnectTimeout(1 * time.Second)
 // Specify the read request timeout period.
 // request.SetReadTimeout(10 * time.Second)
 // Specify the request protocol.
 request.SetScheme(requests.HTTP)
 // Configure the API parameters.
 request.Product = "CS"
 request.Version = "2015-12-15"
 request.PathPattern = "/clusters"
 // Specify the endpoint of the API.
 request.Domain = "cs.env8e-b.com"
 // Specify the request method.
 request.Method = "POST"
```

```
 /**
  * When you initiate an API request based on the core library of Alibaba Cloud SDK, yo
u can configure the Path, Query, Body, and Header parameters.
  * The Path parameters are used to replace variables in the UriPattern of the request.
  * The Query parameters are used to set the URL of the request (GET request in most ca
ses).
  * The Body parameters are used to configure the HTTP content of the request (POST or
PUT request in most cases). You must set the Body parameters together with the HTTP Con tent-Type parameter. You can set the HTTP Content-Type parameter to JSON or FORM.
  * The Header parameter is used to set the HTTP headers of the request.
```

`*/`

```
 // Configure headers.
 // Configure the identifier. This parameter is required and used only for identificati
on. You can set this parameter based on your business requirements.
 request.Headers["x-acs-caller-sdk-source"] = "<your-sdk-source>"
 // When you call an API operation in Apsara Stack, you must configure multiple common
Header parameters, such as x-acs-regionid, x-acs-organizationid, x-acs-resourcegroupid, and x-acs-instanceid. For more information, see Obtain the value of common header param eters.
 // Configure operation-specific parameters.
 request.SetContentType(requests.Form)
 // Initiate the request and obtain the response.
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  fmt.Print(err.Error())
 fmt.Printf(response.GetHttpContentString())
```

**Configure a proxy**

You can configure a proxy in one of the following ways when you call API operations: Configure a proxy by using environment variables. Specify the HTTP_PROXY and HTTPS_PROXY environment variables, or specify the NO_PROXY environment variable. Sample code:

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

Configure a proxy on the client. Sample code:

```
// The proxy that is configured on the client take precedence over the proxy that is configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL encryption**

**Digest**

You can configure SSL authentication for requests. If you set the HTTPSInsecure parameter to `true` , certificate verification is disabled. To ensure connection security, we recommend that you enable certificate verification. If you set the HTTPSInsecure parameter to `false` , certificate verification is enabled. By default, certificate authority (CA) certificates on the operating systems are used.

**Default**

Default value: `false` .

**Settings**

> **Important:** By default, if you send HTTPS requests, the SDK enables certificate verification to verify the validity of SSL certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is thrown. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following settings:

```
// If you configure HTTPSInsecure for the request, the setting takes effect only on the current request. request.SetHTTPSInsecure(true) // Set HTTPSInsecure to true fo r the request. isInsecure := request.GetHTTPSInsecure() // Query the setting of HTTPSIn secure for the request.
```

If you do not configure HTTPSInsecure for the request, the HTTPSInsecure setting for the client takes effect.

```
// If you configure HTTPSInsecure for the client, the setting takes effect on all reque sts that are initiated by the client. client.SetHTTPSInsecure(true) // Set HTTPSInsecure to true for t he client. isInsecure := client.GetHTTPSInsecure() // Query the setting of HTTPSInsec ure for the client.
```

> **Important:** By default, if you send HTTPS requests, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is thrown.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be disabled in the test environment, you can specify the following setting:

Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate verification. clientConfig.setIgnoreSSLCerts(true)
```

## 2 Cluster API list

### 2.1 Container Service API invocation

**invocation**

#### 2.1.1 Overview

To use the APIs provided by Container Service, you can send HTTP requests to the endpoint of Container Service APIs and include specific parameters in the requests. The system returns a response after processing the request.

#### 2.1.2 Common parameters

This topic lists the common request headers, common response headers when you make Container Service API requests.

**Common request headers**

Common request parameters must be included in all Container Service API requests.

| Parameter | Description | Required |
|---|---|---|
| Authorization | The authentication information that is used to check the authenticity of a request. The string must follow the AccessKeyId:Signature format. | Yes |
| Content-Length | The length of the HTTP request content. This length is specified in RFC 2616. | Yes |
| Content-Type | The type of HTTP request content. This type must follow the format that is specified in RFC 2616. | Yes |
| Content-MD5 | The 128-bit MD5 hash value of the HTTP message body. The hash value is encoded in the Base64 format. We recommend that you set this parameter for all requests to prevent parameter tampering. | Yes |

| Date | The time when a request is created. The time must be in GMT. If the time between when the request is sent and when the request is received exceeds 15 minutes, the request is deemed invalid. | Yes |
|---|---|---|
| Host | The host to which the request is sent, for example, diku.aliyuncs.com. | Yes |
| Accept | The type of response that is required by the client. Valid values: application/json and application/xml. | Yes |
| x-acs-version | The version number of the API. Set the value to 2015-12-15. | Yes |
| x-acs-region-id | The region where the Elastic Compute Service (ECS) instance is deployed. | Yes |
| x-acs-signature-nonce | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. | Yes |
| x-acs-signature-method | The encryption method of the signature string. Set the value to HMAC-SHA1. | Yes |

**Examples**

```
GET /clusters HTTP/1.1 Host: cs.aliyuncs.com Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: f63659d4-10ac-483b-99da-ea8fde61eae3 Authorization: acs <yourAccessKeyId>:<yourSignature> x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 11:18:47 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Content-Length: 0
```

**Common response parameters**

Every response returns a unique request ID regardless of whether the call is successful.

**Examples**

XML format:

```
<? xml version="1.0" encoding="UTF-8"? > <!—Result Root Node--> <Interface Name + Response>
 | <! -Returned Request Tag -->
 | <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
 | <! -Return Result Data -->
<Interface Name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
    /* Return Result Data */
```

#### 2.1.3 Request syntax

This topic describes the syntax that you must follow when you make Container Service API requests.

**Endpoint**

The endpoints of the API operations are classified into the following types: Primary region: cs.${global:internet-domain} Secondary region: cs.${global:region}.${global:internet-domain}

**Protocols**

HTTP and HTTPS are supported. We recommend that you send requests over HTTPS to enhance security.

**Request methods**

The following HTTP methods are supported: PUT, POST, GET, and DELETE.

**Request parameters**

Each request must contain common request parameters and parameters unique to specific operations.

**Request encoding**

All requests and responses are encoded in the UTF-8 format.

#### 2.1.4 Response parameters

|   | 2xx |
|---|---|
| 5xx |   |

The response data is returned in a unified format. If status code `2xx` is returned, it indicates that the API call is successful. If status code `4xx` or `5xx` is returned, it indicates that the API call has failed. For successful API calls, response data is returned in XML or JSON format. You can pass a parameter to specify the format when you call the API. The default format is XML. The following example is formatted for readability. The actual result is not formatted with line feeds or indentation.

#### 2.1.5 Sign API requests

This topic describes how to sign API requests to protect Container Service from unauthorized access.

**Introduction**

Apsara Stack issues an AccessKey pair to each Apsara Stack tenant account. Each AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. You can obtain and manage the AccessKey pair in the Apsara Uni-manager Management Console. Container Service verifies every request it receives. All requests to Container Service must contain signature information. Container Service implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. Container Service accepts only requests that are validated by verification codes. Invalid requests are rejected and the HTTP status code 403 is returned. You can add the Authorization header to every HTTP request and include the signature in the header. You must add the signature to the Authorization header in the following format:

```
 Authorization: acs [Access Key Id]:[Signature] .
```

The `Signature` is calculated based on the following rules:

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
| ACCEPT |   |

`VERB` indicates the HTTP method. Example: `PUT` . `ACCEPT` specifies the type of response that is required by the client. Valid values: application/json and application/xml.

| Content-MD5 |   | i |
|---|---|---|
| Content-Type |   |   |
| Date | indicate |   |

`Content-MD5` indicates the MD5 hash value of the request content. `Content-Type` indicates the type of request content. `Date` indicates the time when the request was sent. This parameter is required. The time must be in GMT. If the time between when the request was sent and when the request was received exceeds 15 minutes, the request is deemed invalid and the HTTP status code 400 is returned. For example, `Thu, 17 Mar 2012 18:49:58 GMT` can be used. `CanonicalizedHeaders` indicates the header fields that are prefixed with `x-acs-` in the request.

| CanonicalizedResource | indicates the URI of |
|---|---|

/clusters? name=my-clusters&resource=new can be used. `CanonicalizedHeaders` (headers that start with `x-acs-` ) must comply with the following specifications before the signature is verified:
1. Convert the names of all HTTP request headers prefixed with `x-acs-` to lowercase letters.
For example, you must convert `X-ACS-Meta-Name: TaoBao` into `x-acs-meta-name:` `TaoBao` . Header field names are case-insensitive. We recommend that you use lowercase letters.
2. If a header field value is too long, replace specific delimiters with spaces. The delimiters
include \t , \n , \r , and \f .
3. Sort all HTTP request headers that are obtained from the preceding step in alphabetical
order.
4. Delete spaces from each side of a delimiter between the request header and its content.
For example, convert `x-acs-meta-name: TaoBao,Alipay` into `x-acs-meta-`

```
name:TaoBao,Alipay .
```

5. Separate all headers and content with delimiters ( \n ) to form the final canonicalized
headers.

> **Note:** `CanonicalizedResource` must follow this format: `CanonicalizedResource` specifies the URIs of the requested resources. You must sort sub-resources in alphabetical order and combine them with the `&` delimiter to form a string. In the following example, the string that follows the question mark ( ? ) indicates CanonicalizedResource.

```
http://cs.aliyuncs.com/clusters?name=my-clusters&resource=new
```

The value of `CanonicalizedResource` must be in the following format:

```
/clusters? name=my-clusters&resource=new
```

**Example**

The following example shows how to sign an API request. The `access_key_id` and `access_key_secret` fields separately specify the AccessKey ID and AccessKey secret that are used in the example. We recommend that you use your own program to construct an API request. You can then calculate the signature that is used in the following example. Sample request:

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708
****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 1
0,"ecs_image_id": "m-253l****l"}
```

**Construct the request**

Calculate the values of `Content-Length` and `Content-MD5` . `Content-Length` specifies the length of the content body.

> **Note:** The body cannot start with a space or line feed.

```
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluste r-9708****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10,"ecs_image_id": "m-253ll****"} Content-Length: 210
```

`Content-MD5` : The MD5 value is calculated based on the following rules:

```bash
body: {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluste r-9708****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 10,"ecs_image_id": "m-253ll****"}
# Calculate the MD5 value of the body
md5(body): e94e002cc90a4a3d0f61b790487aa098
# Convert the MD5 hash value into a byte array. Convert every two hexadecimal digits in
to one byte.
# Example: e9 -> 11111111111111111111111111101001 -> -23
bytes(md5(body)): {[-23], [78], [0], [44], [-55], [10], [74], [61], [15], [97], [-73], [-112], [72], [122], [-96], [-104]}
# Convert the byte array into a string that is encoded in the Base64 format.
base64(bytes(md5(body))): 6U4ALMkKSj0PYbeQSHqgmA== Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA==
```

Process `CanonicalizedHeaders`

```bash
# List all header fields prefixed with 'x-acs-'
x-acs-version: 2015-12-15 x-acs-signature-nonce: ca480402-7689-43ba-acc4-4d2013d9d8d4 x-acs-signature-version: 1.0 x-acs-signature-method: HMAC-SHA1 X-Acs-Region-Id: cn-beijing
# Convert the header field name to lowercase, delete the spaces at the start and end of
each line, and sort the header fields in lexicographical order. Delete spaces from each side of a delimiter between the request header and its content.
# Note: No line feed in the last line.
x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15
```

Calculate `CanonicalizedResource` In this example, the length of the `CanonicalizedResource` field value is 27 bytes.

> **Note:** A line feed \n exists at the end of the first line.

```
/clusters? param1=value1&param2=value2
```

Calculate `Signature` Construct the value of `SignatureString` . In this example, the length of the signature string is 307 bytes. Apart from the last line, each line has a line feed \n at the end.

```
POST application/json 6U4ALMkKSj0PYbeQSHqgmA== application/json;charset=utf-8 Wed, 16 Dec 2015 12:20:18 GMT x-acs-region-id:cn-beijing x-acs-signature-method:HMAC-SHA1 x-acs-signature-nonce:fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version:1.0 x-acs-version:2015-12-15 /clusters? param1=value1&param2=value2
```

Calculate `Signature` base on the following rules:

```bash
# Use the AccessKey secret to encrypt the value of SignatureString. In this example, ac
cess_key_secret specifies the AccessKey secret. hmac-sha1(SignatureString): fee03d405e421ebaf514adec881038c4b313584d
#  Convert the encrypted string into a byte array, which is similar to calculating Cont
ent-MD5.
# Convert the byte array into a string that is encoded in the Base64 format. The output
is the signature string. base64(bytes(hmac-sha1(SignatureString))): ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEzNTg0ZA== Signature: ZmVlMDNkNDA1ZTQyMWViYWY1MTRhZGVjODgxMDM4YzRiMzEzNTg0ZA==
```

The signature string is calculated. Add other header fields to your request and set the value of Signature to the calculated signature string. The following sample code shows the signed API request.

```json
POST http://cs.aliyuncs.com/clusters?param1=value1&param2=value2 HTTP/1.1 Accept-Encoding: identity Content-Length: 210 Content-MD5: 6U4ALMkKSj0PYbeQSHqgmA== x-acs-version: 2015-12-15 Accept: application/json User-Agent: cs-sdk-python/0.0.1 (Darwin/15.2.0/x86_64;2.7.10) x-acs-signature-nonce: fbf6909a-93a5-45d3-8b1c-3e03a7916799 x-acs-signature-version: 1.0 Date: Wed, 16 Dec 2015 12:20:18 GMT x-acs-signature-method: HMAC-SHA1 Content-Type: application/json;charset=utf-8 X-Acs-Region-Id: cn-beijing Authorization: acs <yourAccessKeyId>:<yourSignature> {"password": "Just$****","instance_type": "ecs.m2.medium","name": "my-test-cluster-9708
****","size": 1,"network_mode": "vpc","data_disk_category": "cloud","data_disk_size": 1
0,"ecs_image_id": "m-253ll****"}
```

### 2.2 Clusters

#### 2.2.1 Create an ACK cluster

You can call the CreateCluster operation to create a Container Service for Kubernetes (ACK) dedicated cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| cluster type _ | String | Body | No | Kubernetes | The type of cluster. Set the value to Kubernetes to create an ACK dedicated cluster. |
| name | String |   | No | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| region id _ | String | Body | No | cn-beijing | The ID of the region in which you want to deploy the cluster. |
| disable rollbac _ k | Boolea n | Body | No | true | Specifies whether to perform a rollback if the cluster fails to be created. Valid values: true : performs a rollback if the system fails to create the cluster false : does not perform a rollback if the system fails to create the cluster Default value: true . |
| timeout mins _ | Long | Body | No | 60 | Specifies the timeout period of cluster creation. Unit: minutes. Default value: 60 . |
| kubernetes ve _ rsion | String | Body | No | 1.16.9- aliyun.1 | The Kubernetes version of the cluster. The Kubernetes versions supported by ACK are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not set this parameter, the latest Kubernetes version is used. You can create clusters of the latest two Kubernetes versions in the ACK console. You can create clusters of earlier Kubernetes versions by calling API operations. |

| snat entry _ | Boolea n | Body | No | true | Specifies whether to configure SNAT rules for the virtual private cloud (VPC) where your cluster is deployed. Valid values: true : automatically creates a NAT gateway and configures SNAT rules. Set this parameter to true if nodes and applications in the cluster need to access the Internet. false : does not create a NAT gateway or configure SNAT rules. In this case, nodes and applications in the cluster cannot access the Internet. Default value: true . |
|---|---|---|---|---|---|
| endpoint publi _ c access _ | Boolea n | Body | No | true | Specifies whether to enable Internet access for the cluster. You can use an elastic IP address (EIP) to expose the API server. This way, you can access the cluster over the Internet. true : enables Internet access. false : disables Internet access. If you set this parameter to false, the API server cannot be accessed over the Internet. Default value: false . |
| ssh flags _ | Boolea n | Body | No | true | Specifies whether to enable SSH logon over the Internet. true : enables SSH logon over the Internet. false : disables SSH logon over the Internet. Default value: false . |
| cloud monitor _ flags _ | Boolea n | Body | No | true | Specifies whether to install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent. false : does not install the CloudMonitor agent. Default value: false . |

| deletion prote _ ction | Boolea n | Body | No | true | Specifies whether to enable deletion protection for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the ACK console or by calling API operations. Valid values: true : enables deletion protection for the cluster. This way, the cluster cannot be deleted in the ACK console or by calling API operations. false : disables deletion protection for the cluster. This way, the cluster can be deleted in the ACK console or by calling API operations. Default value: false . |
|---|---|---|---|---|---|
| node cidr mas _ _ k | String | Body | No | 26 | The maximum number of IP addresses that can be assigned to nodes. This number is determined by the node CIDR block. This parameter takes effect only if the cluster uses Flannel as the network plug-in. Default value: 26 . |
| user ca _ | String | Body | No | -----BEGIN CERTIFICATE--- --**** | The custom certificate authority (CA) certificate used by the cluster. |

| proxy mode _ | String | Body | No | ipvs | The kube-proxy mode. Valid values: iptables : a mature and stable kube-proxy mode. It uses iptables rules to conduct Service discovery and load balancing. The performance of this mode is limited by the size of the cluster. This mode is suitable for clusters that run a small number of Services. ipvs : a high-performance kube-proxy mode. It uses Linux IP Virtual Server (IPVS) to conduct Service discovery and load balancing. This mode is suitable for clusters that run a large number of Services. We recommend that you use this mode in scenarios where high- performance load balancing is required. Default value: ipvs . |
|---|---|---|---|---|---|
| tags.N.key | String | Body | No | key | The key of a label. |
| tags.N.value | String | Body | No | value | The value of a label. |
| addons.N.nam e | String | Body | No | nginx-ingress- controller | The name of a component. |
| addons.N.confi g | String | Body | No | {\"IngressSlbN etworkType\":\ "internet\"} | The configuration of a component. |
| addons.N.disa bled | Boolea n | Body | No | false | Specifies whether to disable automatic installation. Valid values: true : disables automatic installation. false : enables automatic installation. |
| os type _ | String | Body | No | Linux | The type of OS. Valid values: Windows Linux Default value: Linux . |

| platform | String | Body | No | CentOS | The OS distribution that you want to use. Valid values: CentOS : CentOS. AliyunLinux : Alibaba Cloud Linux. WindowsCore : Windows. CentOS 7.6 : CentOS 7.6. ARM CentOS : CentOS 7.7. NeoKylin : Kylin. Default value: AliyunLinux . |
|---|---|---|---|---|---|
| image type _ | String | Body | No | AliyunLinux | The type of OS distribution that you want to use. To specify the node OS, we recommend that you use this parameter. Valid values: AliyunLinux CentOSArm64 KylinV10 KylinV10Arm64 UOSAnolis UOSAnolisArm64 Default value: AliyunLinux . |
| node port ran _ _ ge | String | Body | No | 30000~32767 | The node port range. Valid values: 30000 to 65535. Default value: 30000~32767 . |
| login passwor _ d | String | Body | No | Hello@1234 | The password for SSH logon. You must set this parameter or the key pair parameter. The _ password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |

| cpu policy _ | String | Body | No | none | The CPU management policy of nodes. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity. none : specifies that the default CPU affinity is used. Default value: none . |
|---|---|---|---|---|---|
| taints.N.effect | String | Body | No | key | The key of a taint. |
| taints.N.key | String | Body | No | value | The value of a taint. |
| taints.N.value | String | Body | No | NoSchedule | The effect of a taint. |
| master count _ | Long | Body | No | 3 | The number of master nodes. Set the value to 3 . Default value: 3 . |
| master syste _ m disk catego _ _ ry | String | Body | No | cloud ssd _ | The type of system disk that you want to use for master nodes. Valid values: cloud efficiency : ultra _ disk. cloud ssd : standard SSD. _ cloud essd : enhanced SSD _ (ESSD). |
| master syste _ m disk size _ _ | Long | Body | No | 120 | The size of the system disk that you want to use for master nodes. Valid values: 40 to 500. Unit: GiB. Default value: 120 . |
| master syste _ m disk snapsh _ _ ot policy id _ _ | String | Body | No | sp- 2zej1nogjvovn z4z**** | The ID of the automatic snapshot policy that you want to use for the system disks of master nodes. |

| master syste _ m disk perfor _ _ mance level _ | String | Body | No | PL1 | The performance level (PL) of the system disk that you want to use for master nodes. This parameter takes effect only for ESSDs. |
|---|---|---|---|---|---|
| num of nodes _ _ | Long | Body | No | 3 | The number of worker nodes. Valid values: 0 to 100. |
| worker system _ disk category _ _ | String | Body | No | cloud efficienc _ y | The type of system disk that you want to use for worker nodes. Valid values: cloud efficiency : ultra _ disk. cloud ssd : standard SSD. _ Default value: cloud ssd . _ |
| worker system _ disk size _ _ | Long | Body | No | 120 | The size of the system disk that you want to use for worker nodes. Unit: GiB. Valid values: 40 to 500. The value of this parameter must be equal to or larger than the larger value between 40 and the size of the OS image. Default value: 120. |
| worker system _ disk snapshot _ _ policy id _ _ | String | Body | No | sp- 2zej1nogjvovn z4z**** | The ID of the automatic snapshot policy that you want to use for the system disks of worker nodes. |
| worker system _ disk perform _ _ ance level _ | String | Body | No | PL1 | The PL of the system disk that you want to use for worker nodes. This parameter takes effect only for ESSDs. |
| worker data di _ _ sks.N.auto sna _ pshot policy i _ _ d | String | Body | No | sp- 2zej1nogjvovn z4z**** | The ID of the automatic snapshot policy that you want to use for the data disks of worker nodes. |
| worker data di _ _ sks.N.category | String | Body | No | cloud essd _ | The data disk type of worker nodes. |
| worker data di _ _ sks.N.encrypte d | String | Body | No | true | Specifies whether to encrypt the data disks of worker nodes. |

| worker data di _ _ sks.N.perform ance level _ | String | Body | No | PL1 | The PL of the data disk that you want to use for worker nodes. This parameter takes effect only for ESSDs. |
|---|---|---|---|---|---|
| worker data di _ _ sks.N.size | Long | Body | No | 120 | The size of the data disk that you want to use for worker nodes. |
| vpcid | String | Body | No | vpc- 2zeik9h3ahvv 2zz95**** | The VPC in which you want to deploy the cluster. This parameter is required. |
| is enterprise s _ _ ecurity group _ | Boolea n | Body | No | true | Specifies whether to create an advanced security group. This parameter takes effect only if security group id is left _ _ empty. Note To use a basic security group, make sure that the sum of the number of nodes in the cluster and the number of pods that use Terway does not exceed 2,000. Therefore, we recommend that you specify an advanced security group for a cluster that uses Terway as the network plug- in. true : creates an advanced security group. false : does not create an advanced security group. Default value: true . |

| container cidr _ | String | Body | No | 172.20.0.0/16 | The CIDR block of pods. This CIDR block cannot overlap with the CIDR block of the VPC in which you want to deploy the cluster. If the VPC is automatically created by the system, the default CIDR block of pods is 172.16.0.0/16. Note This parameter is required if the cluster uses Flannel as the network plug-in. This parameter is optional if the cluster uses Terway as the network plug-in. |
|---|---|---|---|---|---|
| service cidr _ | String | Body | No | 172.21.0.0/20 | The CIDR block of Services. Valid values: 10.0.0.0/16-24, 172.16- 31.0.0/16-24, and 192.168.0.0/16-24. The CIDR block of Services cannot overlap with the CIDR block of the VPC (10.1.0.0/21) or the CIDR blocks of existing clusters in the VPC. You cannot modify the CIDR block of Services after the cluster is created. By default, the CIDR block of Services is set to 172.19.0.0/20. |
| resource grou _ p id _ | String | Body | No | rg- acfm3mkrure* *** | The ID of the resource group to which the cluster belongs. |
| image id _ | String | Body | No | m- bp16z7xko3vv v8gt**** | Specifies a custom image for nodes. By default, the image provided by ACK is used. You can select a custom image to replace the default image. |
| cluster domai _ n | String | Body | No | cluster.local | The domain name of the cluster. The domain name can contain one or more parts that are separated by periods (.). Each part cannot exceed 63 characters in length, and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit. |

| profile | String | Body | No | Default | The identifier of the cluster. Valid values: Default : ACK dedicated cluster. Edge : ACK edge cluster. |
|---|---|---|---|---|---|
| master vswitc _ h ids _ | List<St ring> | Body | No | ["vsw- 2ze3ds0mdip0 hdz8i****"] | The IDs of vSwitches for master nodes. |
| master instan _ ce types _ | List<St ring> | Body | No | ["ecs.n4.xlarg e"] | The Elastic Compute Service (ECS) instance types of master nodes. For more information about ECS instance types, see the Instance types chapter of the ECS User Guide. |
| worker vswitc _ h ids _ | List<St ring> | Body | No | ["vsw- 2ze3ds0mdip0 hdz8i****"] | The IDs of vSwitches for worker nodes. You can specify 1 to 20 vSwitches. We recommend that you select vSwitches in different zones to ensure high availability. |
| worker instanc _ e types _ | List<St ring> | Body | No | ["ecs.n4.large" ] | The ECS instance types of worker nodes. You must specify at least one instance type. For more information, see the Instance types chapter of ECS User Guide. Note The instance types are listed in descending order of priority. If the system fails to create worker nodes with the instance type of the highest priority, the system attempts to create worker nodes with the instance type of the next highest priority. |
| pod vswitch id _ _ s | List<St ring> | Body | No | ["vsw- 2vc9mwkxbvu dp25do****"] | The vSwitches that are used by pods. This parameter is required if you choose Terway as the network plug-in for the cluster. |

| runtime | Struct | Body | No | {"name": "docker", "version": "19.03.5"} | The container runtime used by the cluster. The following runtimes are supported: containerd , Docker , and Sandboxed-Container.runv . The default container runtime is Docker . You must specify the following parameters for a container runtime: name : the name of the container runtime. version : the version of the container runtime. |
|---|---|---|---|---|---|
| name | String |   | No | docker | The name of the container runtime. |
| version | String |   | No | version19.03.1 5 | The version of the container runtime. |
| user data _ | String | Body | No | IyEvdXNyL2Jpb i9iYXNoCmVja G8gIkhlbGxvIE FD**** | The user data of nodes. For more information, see the ECS instance user data chapter in the ECS documentation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | cb95aa626a47740 afbf6aa099b650*** * | The cluster ID. |
| request id _ | String | 687C5BAA-D103- 4993-884B- C35E4314A1E1 | The request ID. |
| task id _ | String | T- 5a54309c80282e3 9ea00002f | The task ID. |

**Examples**

Sample requests

```
POST /clusters HTTP/1.1 Common request headers
```

`{`

```json
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

Sample success responses `XML` format

```xml
<cluster_id>cb95aa626a47740afbf6aa099b650****</cluster_id> <task_id>T-5a54309c80282e39ea00002f</task_id> <request_id>687C5BAA-D103-4993-884B-C35E4314A1E1</request_id>
```

`JSON` format `{`

```json
    "cluster_id": "cb95aa626a47740afbf6aa099b650****",
    "task_id": "T-5a54309c80282e39ea00002f",
    "request_id": "687C5BAA-D103-4993-884B-C35E4314A1E1"
```

#### 2.2.2 Delete a cluster

You can call the DeleteCluster operation to delete a cluster by ID and release all nodes in the cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
DELETE /clusters/[ClusterId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c905d1364c2d d4b6284a3f41 790c4**** | The ID of the cluster. |
| retain all reso _ _ urces | Boolea n | Quer y | No | false | Specifies whether to retain all resources. If you set the parameter to true , the retain resources parameter _ is ignored. true : retains all resources. false : does not retain all resources. Default value: false |
| keep slb _ | Boolea n | Quer y | No | false | Specifies whether to retain the Server Load Balancer (SLB) instances that are created by the cluster. true : retains the SLB instances that are created by the cluster. false : does not retain the SLB instances that are created by the cluster. Default value: false |
| retain resourc _ es | List<St ring> | Quer y | No | ["sg- 2ze6ess9kho6f dn9****"] | The name of the resource. |

**Examples**

Sample requests

```
DELETE /clusters/[ClusterId] HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c905d1364c2dd4b6284a3f41790c4****"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

#### 2.2.3 Query the kubeconfig file of a cluster

You can call the DescribeClusterUserKubeconfig operation to query the kubeconfig file of a cluster. The kubeconfig file contains the details of the current user and is used to configure access to the cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /k8s/[ClusterId]/user_config HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c5b5e80b0b64 a4bf6939d2d8 fbbc5**** | The ID of the cluster. |
| PrivateIpAddre ss | Boolea n | Quer y | No | true | Specifies whether to obtain the credential that is used to connect to the cluster over the internal network. Valid values: true : obtains the credential that is used to connect to the cluster over the internal network. false : obtains the credential that is used to connect to the cluster over the Internet. Default value: false |
| TemporaryDur ationMinutes | Long | Quer y | No | 15 | The validity period of a temporary kubeconfig file. Unit: minutes. Valid values: 15 to 4320. If you specify this parameter, the returned kubeconfig file is valid within the specified time period and will expire at the time specified by expiration in the response. If you do not specify this parameter, the returned kubeconfig file is permanently valid. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| config | String | apiVersion: v1**** | The content of the kubeconfig file. |
| expiration | String | 2024-03- 10T09:56:17Z | The expiration time of the kubeconfig file. The value is the UTC time displayed in RFC3339 format. |

**Examples**

Sample requests

```
GET /k8s/[ClusterId]/user_config HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c5b5e80b0b64a4bf6939d2d8fbbc5****"
```

Sample success responses `XML` format

```xml
<expiration>2024-03-10T09:56:17Z</expiration> <config>apiVersion: v1****</config>
```

`JSON` format `{`

```json
    "expiration": "2024-03-10T09:56:17Z",
    "config": "apiVersion: v1****"
```

#### 2.2.4 Query

##### 2.2.4.1 Query information about all clusters

You can call the DescribeClustersV1 operation to query information about all clusters.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /api/v1/clusters HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| name | String | Quer y | No | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| cluster type _ | String | Quer y | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster |
| page size _ | Long | Quer y | No | 10 | The number of entries to return on each page. |
| page number _ | Long | Quer y | No | 3 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| clusters | Array of cluster |   | The details of clusters. |
| Department | Integer | 3 | The ID of the organization or department to which the cluster belongs. |
| DepartmentNa me | String | acs-test | The name of the organization or department to which the cluster belongs. |
| RMRegionId | String | cn-wl-env115-d01 | The ID of the region in which the cluster is deployed. |
| RegionId | String | cn-beijing | The ID of the region where the cluster is deployed. |
| ResourceGrou p | Integer | 58 | The ID of the resource set. |
| ResourceGrou pName | String | acr-test | The name of the resource set. |
| cluster id _ | String | c3fb96524f9274b4 495df0f12a6b5**** | The ID of the cluster. |

| cluster type _ | String | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster |
|---|---|---|---|
| created | String | 2020-08- 20T10:51:29+08:0 0 | The time when the cluster was created. |
| current versio _ n | String | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. |
| deletion prote _ ction | Boolean | true | Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values: true : deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations. false : deletion protection is disabled for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations. |
| docker versio _ n | String | 19.03.5 | The Docker version that is used by the cluster. |
| external loadb _ alancer id _ | String | lb- 2vcrbmlevo6kjpgc h**** | The ID of the Server Load Balancer (SLB) instance that is used for the Ingress of the cluster. The default SLB specification is slb.s1.small, which belongs to the high- performance instance type. |
| init version _ | String | 1.16.9-aliyun.1 | The Kubernetes version of the cluster. The Kubernetes versions supported by Container Service are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not set this parameter, the latest Kubernetes version is used. You can create clusters of the latest two Kubernetes versions in the Container Service console. You can create clusters of earlier Kubernetes versions by calling API operations. |

| maintenance _ window | Struct |   | The maintenance window of the cluster. |
|---|---|---|---|
| duration | String | 3h | The duration of the cluster maintenance window. The duration ranges from 1 hour to 24 hours. Unit: hours. Default value: 3h. |
| enable | Boolean | false | Indicates whether the cluster maintenance window is enabled. Default value: false |
| maintenance t _ ime | String | 03:00:00Z | The start time of the cluster maintenance window. The value must be in the standard Golang time format. Example: 15:04:05Z. |
| weekly period _ | String | Monday,Thursday | The maintenance cycle. Valid values: Monday to Sunday. Separate multiple values with commas (,). Default value: Thursday. |
| master url _ | String | {\"api server endp _ _ oint\":\"\",\"intranet api server endpoi _ _ _ nt\":\"https://192.1 68.0.251:6443\"} | The endpoint of the cluster API server, including an internal endpoint and a public endpoint. |
| meta data _ | String | {\"api server endp _ _ oint\":\"\",\"intranet api server endpoi _ _ _ nt\":\"https://192.1 68.0.251:6443\"} | The metadata of the cluster. |
| name | String | cluster-demo | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| network mode _ | String | vpc | The network mode of the cluster. Valid values: classic : classic network vpc : virtual private cloud (VPC) overlay : overlay network calico : network powered by Calico |
| next version _ | String | 1.18.8-aliyun.1 | The Kubernetes version to which the cluster can be updated. |

| private zone _ | Boolean | false | Indicates whether Alibaba Cloud DNS PrivateZone is enabled. Valid values: true : Alibaba Cloud DNS PrivateZone is enabled. false : Alibaba Cloud DNS PrivateZone is disabled. |
|---|---|---|---|
| profile | String | Default | The identifier of the cluster. Valid values: Edge : The cluster is a managed edge Kubernetes cluster. Default : The cluster is not a managed edge Kubernetes cluster. |
| region id _ | String | cn-beijing | The ID of the region where the cluster is deployed. |
| resource grou _ p id _ | String | rg- acfmyvw3wjm**** | The ID of the resource group to which the cluster belongs. |
| security group _ id _ | String | sg- 2vcgwsrwgt5mp0yi **** | The ID of the security group to which the instances of the cluster belong. |
| size | Integer | 5 | The number of nodes in the cluster. Master nodes and worker nodes are included. |
| state | String | running | The status of the cluster. Valid values: initial : The cluster is being created. failed : The cluster failed to be created. running : The cluster is running. updating : The cluster is being updated. updating failed : The cluster failed _ to be updated. scaling : The cluster is being scaled. stopped : The cluster is stopped. deleting : The cluster is being deleted. deleted : The cluster is deleted. delete failed : The cluster failed to _ be deleted. |

| subnet cidr _ | String | 172.21.0.0/16 | The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets: 10.0.0.0/8 172.16-31.0.0/12-16 192.168.0.0/16 The CIDR block of pods cannot overlap with the CIDR block of the VPC in which the cluster is deployed and the CIDR blocks of existing clusters in the VPC. You cannot modify the pod CIDR block after the cluster is created. |
|---|---|---|---|
| tags | Array of tag |   | The labels of the cluster. |
| key | String | tier | The key of a label. |
| value | String | backend | The value of a label. |
| updated | String | 2020-09- 16T11:09:55+08:0 0 | The time when the cluster was updated. |
| vpc id _ | String | vpc- 2vcg932hsxsxuqbg l**** | The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster. |
| vswitch id _ | String | vsw- 2vc41xuumx5z2rd ma****,vsw- 2vc41xuumx5z2rd ma**** | The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability. |
| worker ram ro _ _ le name _ | String | KubernetesWorker Role-ec87d15b- edca-4302-933f- c8a16bf0**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on Elastic Compute Service (ECS) instances. |
| zone id _ | String | cn-beijing-b | The ID of the zone where the cluster is deployed. |
| page info _ | Struct |   | The pagination details. |
| page number _ | Integer | 3 | The page number of the returned page. |
| page size _ | Integer | 20 | The number of entries returned per page. |

| total count _ | Integer | 50 | The total number of entries returned. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /api/v1/clusters HTTP/1.1 Common request headers
```

Sample success responses `XML` format

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
    <meta_data>
{\"api_server_endpoint\":\"\",\"intranet_api_server_endpoint\":\"https://192.168.0.251:64 \"}</meta_data>
    <RMRegionId>cn-wl-env115-d01</RMRegionId>
    <state>running</state>
    <ResourceGroup>58</ResourceGroup>
    <init_version>1.16.9-aliyun.1</init_version>
    <deletion_protection>true</deletion_protection>
    <created>2020-08-20T10:51:29+08:00</created>
    <profile>Default</profile>
    <subnet_cidr>172.21.0.0/16</subnet_cidr>
    <master_url>
{\"api_server_endpoint\":\"\",\"intranet_api_server_endpoint\":\"https://192.168.0.251:64 \"}</master_url>
    <region_id>cn-beijing</region_id>
    <current_version>1.16.9-aliyun.1</current_version>
    <size>5</size>
    <name>cluster-demo</name>
    <DepartmentName>acs-test</DepartmentName>
    <RegionId>cn-beijing</RegionId>
    <worker_ram_role_name>KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****</wo
```

`k` `l` `>`

```xml
rker_ram_role_name>
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

`JSON` format `{`

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
        "meta_data": "
{\\\"api_server_endpoint\\\":\\\"\\\",\\\"intranet_api_server_endpoint\\\":\\\"https://19 168.0.251:6443\\\"}",
        "RMRegionId": "cn-wl-env115-d01",
        "state": "running",
        "ResourceGroup": 58,
        "init_version": "1.16.9-aliyun.1",
        "deletion_protection": true,
        "created": "2020-08-20T10:51:29+08:00",
        "profile": "Default",
        "subnet_cidr": "172.21.0.0/16",
        "master_url": "
{\\\"api_server_endpoint\\\":\\\"\\\",\\\"intranet_api_server_endpoint\\\":\\\"https://19 168.0.251:6443\\\"}",
        "region_id": "cn-beijing",
        "current_version": "1.16.9-aliyun.1",
        "size": 5,
```

```json
        "name": "cluster-demo",
        "DepartmentName": "acs-test",
        "RegionId": "cn-beijing",
        "worker_ram_role_name": "KubernetesWorkerRole-ec87d15b-edca-4302-933f-
c8a16bf0****",
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

##### 2.2.4.2 DescribeClusterDetail

You can call the DescribeClusterDetail operation to query the information about a cluster by the cluster ID.

**Request headers**

The DescribePolicies operation does not have operation-specific request headers and uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId] HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Path | Yes | cdde1f21ae22e483ebcb 068a6eb7f**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28D**** | The request ID. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId] HTTP/1.1 &ClusterId=cdde1f21ae22e483ebcb068a6eb7f**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"0ED8D006-F706-4D23-88ED-E11ED28D****"
```

##### 2.2.4.3 Query resources in a cluster

You can call the DescribeClusterResources operation to query all resources in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/resources HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cb95aa626a47 740afbf6aa09 9b65**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| resources | Array of resource |   | The list of resources in the cluster. |
| auto create _ | Integer | 0 | Indicates whether the resource is automatically created by the system. 0 : The resource is automatically created by the system. 1 : The resource is not automatically created by the system. |
| cluster id _ | String | cb95aa626a47740 afbf6aa099b65**** | The ID of the cluster. |

| created | String | 2020-09- 11T10:11:54+08:0 0 | The time when the resource was created. |
|---|---|---|---|
| dependencies | String | [] | The dependencies of the resource. |
| instance id _ | String | lb- wz9poz4r0ymh8u0 uf**** | The ID of the resource. |
| resource info _ | String | {\"Id\":\"k8s maste _ r slb\",\"Name\":\"k _ 8s master slb\",\"T _ _ ype\":\"ALIYUN::SL B::LoadBalancer\",\ "Status\":\"CREATE COMPLETE\",\"Stat _ usReason\":\"state changed\",\"Updat ed\":\"2020-05- 21T13:25:02\",\"Ph ysicalId\":\"lb- wz9poz4r0ymh8u0 uf****\"} | The information about the resource. |
| resource type _ | String | ALIYUN::SLB::Load Balancer | The type of the resource. |
| state | String | CREATE COMPLET _ E | The status of the resource. Valid values: CREATE COMPLETE : The resource is _ created. CREATE FAILED : The resource failed _ to be created. CREATE IN PROGRESS : The resource _ _ is being created. DELETE FAILED : The resource failed _ to be deleted. DELETE IN PROGRESS : The resource _ _ is being deleted. ROLLBACK COMPLETE : The resource _ is rolled back. ROLLBACK FAILED : The resource _ failed to be rolled back. ROLLBACK IN PROGRESS : The _ _ resource is being rolled back. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/resources HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "cb95aa626a47740afbf6aa099b65****"
```

Sample success responses `XML` format

```xml
<resources>
      <resource_info>
{\"Id\":\"k8s_master_slb\",\"Name\":\"k8s_master_slb\",\"Type\":\"ALIYUN::SLB::LoadBalanc \",\"Status\":\"CREATE_COMPLETE\",\"StatusReason\":\"state changed\",\"Updated\":\"2020-05-21T13:25:02\",\"PhysicalId\":\"lbwz9poz4r0ymh8u0uf****\"}</resource_info>
      <cluster_id>cb95aa626a47740afbf6aa099b65****</cluster_id>
      <instance_id>lb-wz9poz4r0ymh8u0uf****</instance_id>
      <created>2020-09-11T10:11:54+08:00</created>
      <resource_type>ALIYUN::SLB::LoadBalancer</resource_type>
      <state>CREATE_COMPLETE</state>
      <auto_create>0</auto_create>
      <dependencies>[]</dependencies>
</resources>
```

`JSON` format `{`

```json
    "resources": {
        "resource_info": "
{\\\"Id\\\":\\\"k8s_master_slb\\\",\\\"Name\\\":\\\"k8s_master_slb\\\",\\\"Type\\\":\\\"A YUN::SLB::LoadBalancer\\\",\\\"Status\\\":\\\"CREATE_COMPLETE\\\",\\\"StatusReason\\\":\\ state changed\\\",\\\"Updated\\\":\\\"2020-05- 21T13:25:02\\\",\\\"PhysicalId\\\":\\\"lb-wz9poz4r0ymh8u0uf****\\\"}",
        "cluster_id": "cb95aa626a47740afbf6aa099b65****",
        "instance_id": "lb-wz9poz4r0ymh8u0uf****",
        "created": "2020-09-11T10:11:54+08:00",
        "resource_type": "ALIYUN::SLB::LoadBalancer",
        "state": "CREATE_COMPLETE",
        "auto_create": 0,
        "dependencies": "[]"
```

##### 2.2.4.4 Query the namespaces of a cluster

You can call the DescribeClusterNamespaces operation to query the namespaces of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /k8s/[ClusterId]/namespaces HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c68069cade53 b4558924a92 4b415f**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| namespaces | List | [“kube-system”] | The name of the namespace. |

**Examples**

Sample requests

```
GET /k8s/[ClusterId]/namespaces HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c68069cade53b4558924a924b415f****"
```

Sample success responses `XML` format

```xml
<namespaces>kube-system</namespaces>
```

`JSON` format `{`

```json
    "namespaces": ["kube-system"]
```

##### 2.2.4.5 Query the agent of a cluster

You can call the DescribeExternalAgent operation to query the agent configurations of an external cluster that is registered in the Container Service console. You can deploy the agent configurations in an external cluster. This allows you to access the API server of the cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /k8s/[ClusterId]/external/agent/deployment HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f 34eb1808d6b 9362c9**** | The ID of the cluster. |
| PrivateIpAddre ss | String | Quer y | No | true | Specifies whether to obtain the credential that is used to access the cluster over the internal network. true: obtains the credential that is used to access the cluster over the internal network. false: obtains the credential that is used to access the cluster over the Internet. Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| config | String | apiVersion: v1**** | The agent configurations in the YAML format. |

**Examples**

Sample requests

```
GET /k8s/[ClusterId]/external/agent/deployment HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

Sample success responses `XML` format

```xml
<config>apiVersion: v1****</config>
```

`JSON` format `{`

```json
    "config": "apiVersion: v1****"
```

##### 2.2.4.6 Query resource quotas

You can call the DescribeUserQuota operation to query resource quotas.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /quota HTTP/1.1
```

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster nodep _ ool quota _ | Long | 10 | The quota of node pools in a Container Service cluster. |
| cluster quota _ | Long | 50 | The quota of Container Service clusters for all types. |
| node quota _ | Long | 100 | The quota of nodes in a Container Service cluster. |

**Examples**

Sample requests

```
GET /quota HTTP/1.1 Common request headers
```

Sample success responses `XML` format

```xml
<amk_cluster_quota>20</amk_cluster_quota> <cluster_nodepool_quota>10</cluster_nodepool_quota> <cluster_quota>50</cluster_quota> <node_quota>100</node_quota>
```

`JSON` format `{`

```json
    "amk_cluster_quota": 20,
    "cluster_nodepool_quota": 10,
    "cluster_quota": 50,
    "node_quota": 100
```

##### 2.2.4.7 Query the logs of a cluster

You can call the DescribeClusterLogs operation to query the logs of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/logs HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f 34eb1808d6b 9362c9**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The log list. |
| ID | Integer | 590749245 | The ID of the log. |
| cluster id _ | String | c23421cfa74454bc 8b37163fd19af**** | The ID of the cluster. |
| cluster log _ | String | start to update cluster status to CREATE COMPLET _ E | The content of the log. |
| created | String | 2020-09- 11T10:11:51+08:0 0 | The time when the log was generated. |
| log level _ | String | 0004 | The level of the log. |

| updated | String | 2020-09- 11T10:11:51+08:0 0 | The time when the log was updated. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/logs HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

Sample success responses `XML` format

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

`JSON` format `{`

```json
    "data": {
        "cluster_id": "c23421cfa74454bc8b37163fd19af***",
        "cluster_log": "start to update cluster status to CREATE_COMPLETE",
        "created": "2020-09-11T10:11:51+08:00",
        "log_level": 4,
        "ID": 590749245,
        "updated": "2020-09-11T10:11:51+08:00"
```

##### 2.2.4.8 Query information about a Kubernetes version supported by Container Service

**version supported by Container Service**

You can call the DescribeKubernetesVersionMetadata operation to query a Kubernetes version supported by Container Service.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /api/v1/metadata/versions HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterType | String | Quer y | Yes | Kubernetes | The type of cluster. |
| Region | String | Quer y | Yes | cn-beijing | The region where the cluster is deployed. |
| KubernetesVer sion | String | Quer y | No | 1.16.9- aliyun.1 | The Kubernetes version of the cluster. Example: 1.16.9-aliyun.1. |
| Profile | String | Quer y | No | Default | The identifier of the cluster. Valid values: Default : dedicated Kubernetes cluster. Edge : dedicated edge Kubernetes cluster. |
| MultiAZ | Boolea n | Quer y | No | false | Specifies whether to query a multi-zone cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The details of the queried Kubernetes version. |
| images | Array of image |   | The OS images of the Elastic Compute Service (ECS) instances. |
| image categor _ y | String | system | The type of the image. Valid values: system : public image self : custom image others : shared image from other Alibaba Cloud accounts marketplace : image from the image market |
| image id _ | String | centos 7 7 x64 20 _ _ _ _ G alibase 2020042 _ _ 6.vhd | The ID of the image. |

| image name _ | String | CentOS 7.7 | The name of the image. |
|---|---|---|---|
| image type _ | String | Centos 7 64 _ _ | The type of the image. |
| os type _ | String | Linux | The type of the node OS. Valid values: Windows and Linux (Default). |
| os version _ | String | 7.7 | The version of the OS distribution. |
| platform | String | CentOS | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| meta data _ | Struct |   | The metadata of the Kubernetes version. |
| Architecture | String | amd64 | The OS architecture of the cluster. |
| AuditProjectNa me | String | k8s-log-c9bd1*** | The name of the Log Service project where the cluster audit log is stored. |
| DockerVersion | String | 19.03.15 | The version of the container runtime. |
| NodeNameMo de | String | true | The name of the custom node. |
| Platform | String | "CentOS" | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |

| PodVswitchId | String | vsw- f8zubs2z9x1cjnzk2 *** | The pod vSwitch, which is used to assign IP addresses to the pods in the cluster that uses Terway as the network plug-in. |
|---|---|---|---|
| ResourceGrou pId | String | rg- aekzsmulow2wngq | The ID of the resource group. |
| multi az _ | Boolean | false | Indicates whether the queried Kubernetes version supports cross-zone deployment. |
| runtimes | Array of runtime |   | Details of the supported container runtimes. |
| name | String | "docker" | The name of the container runtime. |
| version | String | "19.05.3" | The version of the container runtime. |
| version | String | "1.16.9-aliyun.1" | The Kubernetes version. |

**Examples**

Sample requests

```
GET /api/v1/metadata/versions HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterType": "Kubernetes",
    "Region": "cn-beijing"
```

Sample success responses `XML` format

```xml
<data>
      <multi_az>false</multi_az>
      <version>"1.16.9-aliyun.1"</version>
      <images>
            <image_name>CentOS 7.7</image_name>
            <image_category>system</image_category>
            <os_version>7.7</os_version>
            <os_type>Linux</os_type>
            <image_id>centos_7_7_x64_20G_alibase_20200426.vhd</image_id>
            <platform>CentOS</platform>
            <image_type>Centos_7_64</image_type>
      </images>
      <runtimes>
            <name>"docker"</name>
            <version>"19.05.3"</version>
      </runtimes>
      <meta_data>
            <DockerVersion>19.03.15</DockerVersion>
            <Architecture>amd64</Architecture>
            <Platform>"CentOS"</Platform>
            <ResourceGroupId>rg-aekzsmulow2wngq </ResourceGroupId>
            <PodVswitchId>vsw-f8zubs2z9x1cjnzk2***</PodVswitchId>
            <NodeNameMode>true</NodeNameMode>
            <AuditProjectName>k8s-log-c9bd1***</AuditProjectName>
      </meta_data>
</data>
```

`JSON` format `{`

```json
    "data": {
        "multi_az": false,
        "version": "\"1.16.9-aliyun.1\"",
        "images": {
            "image_name": "CentOS 7.7",
            "image_category": "system",
            "os_version": 7.7,
            "os_type": "Linux",
            "image_id": "centos_7_7_x64_20G_alibase_20200426.vhd",
            "platform": "CentOS",
            "image_type": "Centos_7_64"
```

`},`

```json
        "runtimes": {
            "name": "\"docker\"",
            "version": "\"19.05.3\""
```

`},`

```json
        "meta_data": {
            "DockerVersion": "19.03.15",
            "Architecture": "amd64",
            "Platform": "\"CentOS\"",
            "ResourceGroupId": "rg-aekzsmulow2wngq",
            "PodVswitchId": "vsw-f8zubs2z9x1cjnzk2***",
            "NodeNameMode": true,
            "AuditProjectName": "k8s-log-c9bd1***"
```

#### 2.2.5 Modify

##### 2.2.5.1 Modify cluster configurations

You can call the ModifyCluster operation to modify the configurations of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
PUT /api/v2/clusters/[ClusterId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | cb95aa626a47 740afbf6aa09 9b65**** | The ID of the cluster. |

| api server eip _ _ | Boolea n | Body | No | true | Specifies whether to associate an elastic IP address (EIP) with the cluster API server. This enables Internet access for the cluster. Valid values: true : associates an EIP with the cluster API server. false : does not associate an EIP with the cluster API server. |
|---|---|---|---|---|---|
| api server eip _ _ id _ | String | Body | No | eip- wz9fnasl6dsfh mvci**** | The ID of the EIP that you want to associate with the cluster API server. The parameter takes effect only if api server eip _ _ is set to true . |
| deletion prote _ ction | Boolea n | Body | No | true | Specifies whether to enable deletion protection for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values: true : enables deletion protection for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations. false : disables deletion protection for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations. Default value: false |

|   | api server eip _ _ |
|---|---|
| true |   |

| instance deleti _ on protection _ | Boolea n | Body | No | true | Specifies whether to enable deletion protection for the instances in the cluster. If deletion protection is enabled, the instances in the cluster cannot be deleted in the console or by calling the API. Valid values: true : enables deletion protection for the instances in the cluster. You cannot delete the instances in the cluster in the console or by calling the API. false : disables deletion protection for the instances in the cluster. You can delete the instances in the cluster in the console or by calling the API. Default value: false |
|---|---|---|---|---|---|
| ingress domai _ n rebinding _ | String | Body | No | true | Specifies whether to remap the test domain name of the cluster. Valid values: true : remaps the test domain name of the cluster. false : does not remap the test domain name of the cluster. Default value: false |
| ingress loadba _ lancer id _ | String | Body | No | lb- wz97kes8tnnd kpodw**** | The ID of the Server Load Balancer (SLB) instance that is associated with the cluster. |
| resource grou _ p id _ | String | Body | No | rg- acfmyvw3wjm **** | The ID of the resource group to which the cluster belongs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| cluster id _ | String | cb95aa626a47740 afbf6aa09**** | The ID of the cluster. |
| request id _ | String | 687C5BAA-D103- 4993-884B- C35E4314**** | The ID of the request. |

| task id _ | String | T- 5a54309c80282e3 9ea00**** | The ID of the task. |
|---|---|---|---|

**Examples**

Sample requests

```
PUT /api/v2/clusters/[ClusterId] HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "cb95aa626a47740afbf6aa099b65****"
```

Sample success responses `XML` format

```xml
<cluster_id>cb95aa626a47740afbf6aa09****</cluster_id> <task_id>T-5a54309c80282e39ea00****</task_id> <request_id>687C5BAA-D103-4993-884B-C35E4314****</request_id>
```

`JSON` format `{`

```json
    "cluster_id": "cb95aa626a47740afbf6aa09****",
    "task_id": "T-5a54309c80282e39ea00****",
    "request_id": "687C5BAA-D103-4993-884B-C35E4314****"
```

##### 2.2.5.2 Modify the labels of a cluster

You can call the ModifyClusterTags operation to modify the labels of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/tags HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f 34eb1808d6b 9362c9**** | The ID of the cluster. |
| body | Array | Body | No |   |   |

| tag | Struct |   | No |   | The configurations of the label. |
|---|---|---|---|---|---|
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/tags HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
    [ {
      "key" : "env",
      "value" : "prod"
    } ]
```

Sample success responses `XML` format

```
HTTP/1.1 200 OK
```

`JSON` format

```
HTTP/1.1 200 OK
```

#### 2.2.6 Upgrade

##### 2.2.6.1 Upgrade a cluster

You can call the UpgradeCluster operation to upgrade a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /api/v2/clusters/[ClusterId]/upgrade HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| ClusterId | String | Path | Yes | c82e6987e296 1451182edacd 74faf**** | The ID of the cluster. |
|---|---|---|---|---|---|
| body | Struct | body | No |   |   |
| component na _ me | String |   | No | k8s | The name of the component. Set the value to k8s . |
| version | String |   | No | 1.14.8- aliyun.1 | The Kubernetes version of the cluster. |
| next version _ | String |   | No | 1.16.9- aliyun.1 | The Kubernetes version to which the cluster can be upgraded. |

**Examples**

Sample requests

```
POST /api/v2/clusters/[ClusterId]/upgrade HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": ""
    "component_name" : "k8s",
    "next_version" : "1.16.9-aliyun.1",
    "version" : "1.14.8-aliyun.1"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

##### 2.2.6.2 Query the upgrade status of a cluster

You can call the GetUpgradeStatus operation to query the upgrade status of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /api/v2/clusters/[ClusterId]/upgrade/status HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f 34eb1808d6b 9362c9**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| error message _ | String | subject to actual return | The error message returned during the upgrade. |
| precheck repo _ rt id _ | String | be4c8eb72de94d4 59ea7ace7c811d1 19 | The ID of the precheck report. |
| status | String | running | The state of the upgrade. |
| upgrade step _ | String | prechecking | The current phase of the upgrade. |
| upgrade task _ | Struct |   | The details of the upgrade task. |
| message | String | subject to actual return | The description of the upgrade task. |
| status | String | running | The state of the upgrade task. |

**Examples**

Sample requests

```
GET /api/v2/clusters/[ClusterId]/upgrade/status HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

Sample success responses `XML` format

```xml
<error_message>subject to actual return</error_message> <upgrade_task>
    <message>subject to actual return</message>
    <status>running</status>
</upgrade_task> <precheck_report_id>be4c8eb72de94d459ea7ace7c811d119</precheck_report_id> <status>running</status> <upgrade_step>prechecking</upgrade_step>
```

`JSON` format `{`

```json
    "error_message": "subject to actual return",
    "upgrade_task": {
        "message": "subject to actual return",
        "status": "running"
```

`},`

```json
    "precheck_report_id": "be4c8eb72de94d459ea7ace7c811d119",
    "status": "running",
    "upgrade_step": "prechecking"
```

##### 2.2.6.3 Suspend the upgrade of a cluster

You can call the PauseClusterUpgrade operation to suspend the upgrade of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /api/v2/clusters/[ClusterId]/upgrade/pause HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e296 1451182edacd 74faf**** | The ID of the cluster. |

**Examples**

Sample requests

```
POST /api/v2/clusters/[ClusterId]/upgrade/pause HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

##### 2.2.6.4 Cancel the upgrade of a cluster

You can call the CancelClusterUpgrade operation to cancel the upgrade of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /api/v2/clusters/[ClusterId]/upgrade/cancel HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f 34eb1808d6b 9362c9**** | The ID of the cluster. |

**Examples**

Sample requests

```
POST /api/v2/clusters/[ClusterId]/upgrade/cancel HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

##### 2.2.6.5 Resume the upgrade of a cluster

You can call the ResumeUpgradeCluster operation to resume the upgrade of a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /api/v2/clusters/[ClusterId]/upgrade/resume HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| ClusterId | String | Path | Yes | c82e6987e296 1451182edacd 74faf**** | The ID of the cluster. |
|---|---|---|---|---|---|

**Examples**

Sample requests

```
POST /api/v2/clusters/[ClusterId]/upgrade/resume HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

### 2.3 Nodes

#### 2.3.1 Query nodes in a cluster

You can call the DescribeClusterNodes operation to query information about the nodes in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/nodes HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e296 1451182edacd 74faf**** | The ID of the cluster. |
| instanceIds | String | Quer y | No | i-node1,i- node2 | The IDs of Elastic Compute Service (ECS) instances. Instances that match the IDs are returned. If nodepool id is not _ empty, this parameter is ignored. Separate multiple nodes with commas (,). |

| nodepool id _ | String | Quer y | No | np*** | The ID of the node pool. |
|---|---|---|---|---|---|
| state | String | Quer y | No | all | The state of the nodes in the cluster. You can filter the nodes by state. Valid values: all : Query all nodes in the cluster. running : Query nodes that are running in the cluster. removing : Query nodes that are being removed from the cluster. initial : Query nodes that are initializing in the cluster. failed : Query nodes that failed to be created in the cluster. |
| pageSize | String | Quer y | No | 3 | The number of entries to return on each page. |
| pageNumber | String | Quer y | No | 50 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodes | Array of node |   | The details of the nodes in the cluster. |
| creation time _ | String | "2020-08- 25T11:25:35+08:0 0" | The time when the node was created. |
| error message _ | String | "***" | The error message generated when the node was created. |
| expired time _ | String | "2099-12- 31T23:59:00+08:0 0" | The expiration date of the node. |
| host name _ | String | "iZ2vcckdmxp7u0u rj2k****" | The name of the host. |
| image id _ | String | "aliyun 2 1903 x6 _ _ _ 4 20G alibase 202 _ _ _ 00529.vhd" | The ID of the system image that is used by the node. |
| instance char _ ge type _ | String | "PostPaid" | The billing method of the instance on which the node is deployed. |

| instance id _ | String | "i- 2vcckdmxp7u0urj2 k2rw" | The ID of the instance on which the node is deployed. |
|---|---|---|---|
| instance nam _ e | String | "worker-k8s-for-cs- c5cdf7e3938bc4f8 eb0e44b21a80f*** *" | The name of the instance on which the node is deployed. |
| instance role _ | String | "Worker" | The role of the node. Valid values: Master : master node Worker : worker node |
| instance statu _ s | String | "Running" | The status of the node. |
| instance type _ | String | "ecs.c5.xlarge" | The instance type of the node. |
| instance type _ _ family | String | "ecs.c5" | The ECS instance family of the node. |
| ip address _ | List | ["192.168.44.247"] | The IP address of the node. |
| is aliyun node _ _ | Boolean | true | Indicates whether the instance is provided by Alibaba Cloud. |
| node name _ | String | "cn- chengdu.192.168.0 .36" | The name of the node. This name is the identifier of the node in the cluster. |
| node status _ | String | "Ready" | Indicates whether the node is ready. |
| nodepool id _ | String | "np0794239424a8 4eb7a95327369d5 6****" | The ID of the node pool. |
| source | String | "ess attach" _ | The source of the node. You can add a node to a cluster in the Container Service console or Resource Orchestration Service (ROS) console. |
| state | String | "running" | The status of the node. |
| page | Struct |   | The pagination details. |
| page number _ | Integer | 1 | The number of the returned page. |
| page size _ | Integer | 10 | The number of entries returned per page. |

| total count _ | Integer | 5 | The total number of entries returned. |
|---|---|---|---|

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/nodes HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

Sample success responses `XML` format

```xml
<nodes>
    <creation_time>"2020-08-25T11:25:35+08:00"</creation_time>
    <error_message>"***"</error_message>
    <instance_name>"worker-k8s-for-cs-c5cdf7e3938bc4f8eb0e44b21a80f****"
</instance_name>
    <node_status>"Ready"</node_status>
    <is_aliyun_node>true</is_aliyun_node>
    <node_name>"cn-chengdu.192.168.0.36"</node_name>
    <expired_time>"2099-12-31T23:59:00+08:00"</expired_time>
    <source>"ess_attach"</source>
    <instance_type_family>"ecs.c5"</instance_type_family>
    <instance_id>"i-2vcckdmxp7u0urj2k2rw"</instance_id>
    <instance_charge_type>"PostPaid"</instance_charge_type>
    <instance_role>"Worker"</instance_role>
    <instance_status>"Running"</instance_status>
    <state>"running"</state>
    <image_id>"aliyun_2_1903_x64_20G_alibase_20200529.vhd"</image_id>
    <instance_type>"ecs.c5.xlarge"</instance_type>
    <nodepool_id>"np0794239424a84eb7a95327369d56****"</nodepool_id>
    <host_name>"iZ2vcckdmxp7u0urj2k****"</host_name>
    <ip_address>["192.168.44.247"]</ip_address>
</nodes> <page>
    <page_number>1</page_number>
    <total_count>5</total_count>
    <page_size>10</page_size>
</page>
```

`JSON` format `{`

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

#### 2.3.2 Remove nodes from a cluster

You can call the RemoveClusterNodes operation to remove nodes from a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /api/v2/clusters/[ClusterId]/nodes/remove HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Patj | Yes | c850429a2287 b4d968e27e8 7a4921**** | The ID of the cluster. |
| body | Struct | Body | No |   |   |

| release node _ | Boolea n |   | No | true | Specifies whether to release the Elastic Compute Service (ECS) instances. Valid values: true : releases the ECS instances. false : does not release the ECS instances. Default value: false Note You cannot release subscription ECS instances when you remove the nodes. |
|---|---|---|---|---|---|
| drain node _ | Boolea n |   | No | true | Specifies whether to remove all pods from the nodes that you want to remove. Valid values: true : removes all pods from the nodes that you want to remove. false : does not remove pods from the nodes that you want to remove. Default value: false |
| nodes | String |   | No | ["cn- chengdu.192.1 68.0.70"] | The name of the node. |

**Examples**

Sample requests

```
POST /api/v2/clusters/[ClusterId]/nodes/remove HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c82e6987e2961451182edacd74faf****"
    "release_node": false,
    "nodes": [
        "cn-shenzhen.192.168.0.70"
```

`],`

```json
    "drain_node": false
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

#### 2.3.3 Add existing ECS instances to a cluster

You can call the AttachInstances operation to add existing Elastic Compute Service (ECS) instances to a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/attach HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c106f377e16f 34eb1808d6b 9362c9**** | The ID of the cluster. |
| format disk _ | Boolea n | Body | No | false | Specifies whether to store container data and images on data disks. Valid values: true : mounts data disks to store container data and images. false : does not mount data disks to store container data or images. Default value: false How to mount a data disk: If the ECS instances are already mounted with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4 and mounts it to /var/lib/docker and /var/lib/kubelet. If no data disk is attached to the ECS instances, the system does not purchase a new data disk. Note If you choose to store container data and images on data disks and a data disk is already mounted to the ECS instance, the original data on this data disk will be cleared. You can back up the disk to avoid data loss. |

| image id _ | String | Body | No | aliyun 2 1903 _ _ x64 20G alib _ _ _ ase 20200529 _ .vhd | The ID of the custom image. If you do not set this parameter, the default system image is used. Note If you specify a custom image, the custom image is used to deploy the operating systems on the system disks of the nodes. |
|---|---|---|---|---|---|
| keep instance _ name _ | Boolea n | Body | No | true | Specifies whether to retain the instance name. Valid values: true : retains the instance name. false : does not retain the instance name. Default value: true |
| user data _ | String | Body | No | IyEvdXNyL2Jpb i9iYXNoCmVja G8gIkhlbGxvIE FDSyEi | The user-defined data on the node. For more information, see the User-defined data chapter in the ECS documentation. |
| cpu policy _ | String | Body | No | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. Default value: none |
| runtime | Json | Body | No | {"name": "docker", "version": "19.03.5"} | The container runtime. |

| platform | String | Body | No | CentOS | The OS distribution that you want to use. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
|---|---|---|---|---|---|
| password | String | Body | No | Hello1234 | The SSH logon password that is used to log on to the ECS instances. You must set login password or key pair . _ _ The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It cannot contain backslashes (\) or double quotation marks ("). For security considerations, the password is encrypted during data transfer. |
| instances | String | Body | No | ["i- 2zed0sswuau6 o89b****"] | The IDs of the existing ECS instances that you want to add. |
| tags | Array | Body | No |   | The labels that you want to add to nodes. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs: , https:// , or http:// . |
| key | String |   | No | key | The key of the label. |
| value | String |   | No | value | The value of the label. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| list | Array of list |   | The details of the added nodes. |
| code | String | 200 | The code that indicates the task result. |
| instanceId | String | i- 2ze0lgm3y6iylcbt* *** | The ID of the instance. |
| message | String | successful | Indicates whether the ECS instances are successfully added to the cluster. |
| task id _ | String | T- 5a544aff80282e39 ea000039 | The ID of the task. |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/attach HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c106f377e16f34eb1808d6b9362c9****"
```

Sample success responses `XML` format

```xml
<task_id>T-5a544aff80282e39ea000039</task_id> <list>
    <code>200</code>
    <instanceId>i-2ze0lgm3y6iylcbt****</instanceId>
    <message>successful</message>
</list>
```

`JSON` format `{`

```json
    "task_id": "T-5a544aff80282e39ea000039",
    "list": {
        "code": 200,
        "instanceId": "i-2ze0lgm3y6iylcbt****",
        "message": "successful"
```

#### 2.3.4 Manually add existing instances to a cluster

**cluster**

You can call the DescribeClusterAttachScripts operation to manually add an existing instance to a cluster. This operation returns a unique executable script. You can run this script on an existing instance to add the instance to the specified cluster as a node.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/attachscript HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| ClusterId | String | Path | Yes |   | ca375a93a304 74552ad2a0e be183e**** | The ID of the cluster. |   |   |
| body | Struct | body | No |   |   |   |   |   |
| keep instance _ name _ | Boolea n |   | No |   |   | Specifies whether to retain the name of the existing instance when it is added to the cluster. If you do not retain the instance name, the instance is named in the worker-k8s-for-cs- <clusterid> format. Valid values: true : retains the instance name. false : does not retain the instance name. Default value: true |   |   |
|   |   |   |   |   |   |   | worker-k8s-for-cs- |   |
|   |   |   |   |   | true | <clusterid> |   |   |
| options | String |   | No |   | {\"enableIptab les\": true,\"manage Runtime\": true,\"quiet\": true,\"allowed ClusterAddons \": [\"kube- proxy\",\"flann el\",\"coredns\ "]} | The node configurations for the existing instance that you want to add as a node. |   |   |
| arch | String |   | No |   | amd64 | The CPU architecture of the node. |   |   |

| format disk _ | Boolea n |   | No | false | Specifies whether to mount data disks to an existing instance when you add the instance to the cluster. You can add data disks to store the container data and images. Valid values: true : mounts data disks to the existing instance that you want to add. After a data disk is mounted, the original data that is stored on the disk is erased. Back up data before you mount a data disk. false : does not mount data disks to the existing instance. Default value: false How to mount a data disk: If the existing Elastic Compute Service (ECS) instance has data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet. If no data disk is attached to the ECS instances, the system does not purchase a new data disk. |
|---|---|---|---|---|---|
| nodepool id _ | String |   | No | np1c9229d9be 2d432c93f77a 88fca0**** | The ID of the node pool to which you want to add an existing node. This parameter allows you to add an existing node to a specified node pool. |
| rds instances _ | String |   | No | ["rm-xxx"] | The names of the ApsaraDB RDS instances. |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/attachscript HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "ca375a93a30474552ad2a0ebe183e****"
    "nodepool_id": "np1c9229d9be2d432c93f77a88fca0****",
    "format_disk": false,
    "keep_instance_name": true,
    "rds_instances": ["rm-xxx"],
    "arch": "amd64",
    "options": "{\\\"enableIptables\\\": true,\\\"manageRuntime\\\":
true,\\\"quiet\\\": true,\\\"allowedClusterA ddons\\\": [\\\"kubeproxy\\\",\\\"flannel\\\",\\\"coredns\\\"]}"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

#### 2.3.5 Node pools

##### 2.3.5.1 Create a node pool

You can call the CreateClusterNodePool operation to create a node pool for a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/nodepools HTTP/1.1
```

**Request parameters**

| Field | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | path | Yes | c61da77e8bf bc4c4c999af 2b51b65**** | The ID of the cluster. |
| body | Struct | body | No |   |   |
| count | Intege r |   | No | 1 | The number of nodes in the node pool. |
| nodepool inf _ o | Struct |   | No |   | The configuration of the node pool. |
| name | String |   | No | cluster-demo | The name of the node pool. |

| scaling grou _ p | Struct |   | No |   | The configuration of the scaling group that is used by the node pool. |
|---|---|---|---|---|---|
| system disk _ _ category | String |   | No | cloud efficie _ ncy | The type of system disk. Valid values: cloud efficiency : _ ultra disk cloud ssd : standard _ SSD cloud essd : enhanced _ SSD (ESSD) Default value: cloud efficiency. _ |
| system disk _ _ size | Intege r |   | No | 120 | The system disk size of a node. Unit: GiB. |
| system disk _ _ performance level _ | String |   | No | PL1 | The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for ESSDs. |
| vpc id _ | String |   | No | vpc- wz984yvbd6l ck22z3**** | The ID of the virtual private cloud (VPC). |
| instance cha _ rge type _ | String |   | No | PrePaid | The billing method of nodes in the node pool. Valid values: PrePaid : subscription PostPaid : pay-as-you- go Default value: PostPaid |
| internet max _ bandwidth _ _ out | Intege r |   | No | 5 | The bandwidth of the public IP address. |
| login passwo _ rd | String |   | No | Hello1234 | The logon password. |
| security grou _ p id _ | String |   | No | sg- wz9a8g2mt6 x5llu0**** | The ID of the security group. |
| platform | String |   | No | Linux | The OS distribution. |
| image id _ | String |   | No | aliyun 2 190 _ _ 3 x64 20G a _ _ _ libase 20200 _ 529.vhd | The ID of a custom image. By default, the image provided by Container Service is used. |
| internet char _ ge type _ | String |   | No | PayByTraffic | The billing method of the public IP address. |

| scaling polic _ y | String |   | No | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks. Default value: release . |
|---|---|---|---|---|---|
| vswitch ids _ | String |   | No | vsw- wz9mfnhmss ud6eicu**** | The IDs of vSwitches. |
| instance typ _ es | String |   | No | ecs.d1ne.2xl arge | The type of instance. |
| tags | Array |   | No |   | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| data disks _ | Array |   | No |   | The configuration of data disks. |
| category | String |   | No | cloud ssd _ | The type of data disk. |
| size | Intege r |   | No | 40 | The size of a data disk. Unit: GiB. |

| encrypted | String |   | No | true | Specifies whether to encrypt data disks. Valid values: true : encrypts a data disk. false : does not encrypt a data disk. Default value: false |
|---|---|---|---|---|---|
| auto snapsh _ ot policy id _ _ | String |   | No | sp- 2zej1nogjvov nz4z**** | The ID of an automatic snapshot policy. Automatic backup is performed for a disk based on the specified automatic snapshot policy. By default, this parameter is empty. This indicates that automatic backup is disabled. |
| kubernetes c _ onfig | Struct |   | No |   | The configuration of the cluster. |
| cpu policy _ | String |   | No | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : specifies that the default CPU affinity is used Default value: none |
| cms enabled _ | Boole an |   | No | true | Specifies whether to install the CloudMonitor agent on ECS nodes. After the CloudMonitor agent is installed on ECS nodes, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes Default value: false |

| unschedulabl e | Boole an |   | No | false | Nodes that are newly added to the cluster are marked as unschedulable. If you specify this parameter, the nodes become unschedulable after they are added to the cluster. You can go to the Nodes page and set the nodes to schedulable. |
|---|---|---|---|---|---|
| user data _ | String |   | No | dGhpcyBpcy BhIGV4YW1 wbGU= | The user-defined data on the node. |
| runtime | String |   | No | docker | The container runtime. |
| runtime vers _ ion | String |   | No | 19.03.5 | The version of the container runtime. |
| node name _ _ mode | String |   | No | aliyun.com00 055test | A custom node name consists of a prefix, an IP substring, and a suffix. The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). A custom node name must start and end with a digit or lowercase letter. The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the length of the IP address substring is 5, and the suffix is test, the node name will be aliyun.com00055test. |
| labels | Array |   | No |   | The labels that you want to add to the nodes in the cluster. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| taints | Array |   | No |   | The taints that you want to add to the nodes in the cluster. |

| key | String |   | No | env | The key of a taint. |
|---|---|---|---|---|---|
| value | String |   | No | prod | The value of a taint. |
| effect | String |   | No | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| tee config _ | Struct |   | No |   | The configuration about confidential computing for the cluster. |
| tee enable _ | Boole an |   | No | true | Specifies whether to enable confidential computing for the cluster. |
| auto scaling _ | Struct |   | No |   | The configuration about auto scaling. |
| enable | Boole an |   | No | true | Specifies whether to enable auto scaling. Valid values: true : enables auto scaling false : disables auto scaling. If you set this parameter to false, other parameters in the auto scaling section do not _ take effect. Default value: false |
| max instanc _ es | Intege r |   | No | 10 | The maximum number of ECS instances that can be created in the node pool. |
| min instance _ s | Intege r |   | No | 1 | The minimum number of ECS instances that must be kept in the node pool. |

| type | String |   | No | cpu | The minimum number of ECS instances that must be kept in the node pool. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepool id _ | String | np5faa48fb31b6b8 078d00**** | The ID of the node pool. |

**Example**

Sample requests `{`

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

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <nodepool_id>np31da1b38983f4511b490fc62108a****</nodepool_id>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
  "nodepool_id" : "np31da1b38983f4511b490fc62108a****"
```

##### 2.3.5.2 Synchronize node pool information

You can synchronize node pool information, including metadata and node information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request syntax**

```
POST /clusters/[ClusterId]/sync_nodepools HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Path | Yes | c905d1364c2dd4b6284a 3f41790c4**** | The cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2D69A58F-345C- 4FDE-88E4- BF51894XXXXX | The request ID. |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/sync_nodepools HTTP/1.1
```

`{`

```json
"ClusterId":"c905d1364c2dd4b6284a3f41790c4****"
```

Sample success responses `JSON` format `{`

```json
 "RequestId":"2D69A58F-345C-4FDE-88E4-BF51894XXXXX"
```

##### 2.3.5.3 Scale out a node pool

You can call the ScaleClusterNodePool operation to scale out a node pool.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c23421cfa744 54bc8b37163f d19af**** | The ID of the cluster. |
| NodepoolId | String | Path | Yes | np31da1b389 83f4511b490f c62108a**** | The ID of the node pool. |
| body | Struct | body | No |   |   |
| count | Long |   | No | 1 | The number of worker nodes that you want to add. You can add at most 500 nodes in one API call. The maximum number of nodes that can be added is limited by the quota of nodes in the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| task id _ | String | T- 5faa48fb31b6b807 8d00**** | The ID of the task. |

**Example**

Sample requests

```
POST /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "NodepoolId": "np31da1b38983f4511b490fc62108a****"
    "count": 1
```

Sample success responses `XML` format

```xml
<task_id>T-5faa48fb31b6b8078d00****</task_id>
```

`JSON` format `{`

```json
    "task_id": "T-5faa48fb31b6b8078d00****"
```

##### 2.3.5.4 Modify the configuration of a node pool

You can call the ModifyClusterNodePool operation to modify the configuration of a node pool.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
PUT /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

**Request parameters**

| Field | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | path | Yes | c23421cfa74 454bc8b371 63fd19af**** | The ID of the cluster. |
| NodepoolId | String | path | Yes | p31da1b389 83f4511b490 fc62108a**** | The ID of the node pool. |
| update node _ s | Boole an | Body | No | true | Specifies whether to update node information, such as labels and taints. |
| auto scaling _ | Struct | Body | No |   | The configuration about auto scaling. |
| enable | Boole an |   | No | true | Specifies whether to enable auto scaling. true : enables auto scaling for the node pool false : disables auto scaling for the node pool. If you set this parameter to false , other parameters in the auto scaling section _ do not take effect. Default value: false |

| max instanc _ es | Long |   | No | 10 | The maximum number of Elastic Compute Service (ECS) instances supported by the node pool. |
|---|---|---|---|---|---|
| min instance _ s | Long |   | No | 2 | The minimum number of ECS instances. |
| type | String |   | No | cpu | The minimum number of ECS instances that must be kept in the node pool. Valid values: cpu : regular instance gpu : GPU-accelerated instance gpushare : shared GPU- accelerated instance spot : preemptible instance Default value: cpu |
| kubernetes c _ onfig | Struct | Body | No |   | The configuration of the cluster. |
| labels | Array |   | No | [ { "key" : "String", "value" : "String" } ] | The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules: Each label is a case- sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| taints | Array |   | No |   | The configurations of node taints. |
| key | String |   | No | env | The key of a taint. |
| value | String |   | No | prod | The value of a taint. |

| effect | String |   | No | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
|---|---|---|---|---|---|
| cms enabled _ | Boole an |   | No | true | Specifies whether to install the CloudMonitor agent on ECS nodes. After the CloudMonitor agent is installed on ECS nodes, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes Default value: false |
| runtime | String |   | No | docker | The name of the container runtime. |
| runtime vers _ ion | String |   | No | 19.03.5 | The version of the container runtime. |
| user data _ | String |   | No | IyEvdXNyL2J pbi9iYXNoC mVjaG8gIkhl bGxvIEFDSyE i | The user-defined data of the node pool. |

| unschedulabl e | Boole an |   | No | false | Nodes that are newly added to the cluster are marked as unschedulable. If you select this option, the nodes are unschedulable when they are added to the cluster. You can go to the Nodes page and set the nodes as schedulable. |
|---|---|---|---|---|---|
| scaling grou _ p | Struct | Body | No |   | The configuration of the scaling group. |
| data disks _ | Array |   | No |   | The configurations of the data disks that are mounted to the nodes in the node pool. You can mount 0 to 10 data disks. You can mount at most 10 data disks to the nodes in the node pool. |
| category | String |   | No | cloud ssd _ | The size of a data disk. Unit: GiB. |
| size | Intege r |   | No | 40 | Specifies whether to encrypt data disks. Valid values: true : encrypts a data disk. false : does not encrypt a data disk. Default value: false |
| encrypted | String |   | No | true | The ID of an automatic snapshot policy. Automatic backup is performed for a disk based on the specified automatic snapshot policy. By default, this parameter is empty. This indicates that automatic backup is disabled. |
| tags | Array |   | No | testkey | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://. |
| key | String |   | No | env | The key of a label. |
| value | String |   | No | prod | The value of a label. |
| instance cha _ rge type _ | String |   | No | PrePaid | The billing method of the instance on which the node is deployed. |

| platform | String |   | No | AliyunLinux | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
|---|---|---|---|---|---|
| image id _ | String |   | No | aliyun 2 190 _ _ 3 x64 20G a _ _ _ libase 20200 _ 904.vhd | The ID of the custom image. You can call the DescribeKubernetesVersionMe tadata operation to query the supported images. By default, the latest image is used. |
| login passwo _ rd | String |   | No | Hello1234 | The password for SSH logon. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. |
| scaling polic _ y | String |   | No | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks. |
| system disk _ _ category | String |   | No | cloud efficie _ ncy | The type of system disk. Valid values: cloud efficiency : _ ultra disk cloud ssd : standard _ SSD Default value: cloud ssd _ |

| system disk _ _ size | String |   | No | 120 | The system disk size of a node. Unit: GiB. Valid values: 20 to 500 The value of this parameter must be at least 20 and greater than or equal to the image size. The default value is the greater one between 40 and the image size. |
|---|---|---|---|---|---|
| internet max _ bandwidth _ _ out | Intege r |   | No | 10 | The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100. |
| multi az poli _ _ cy | String |   | No | BALANCE | The ECS instance scaling policy for a multi-zone scaling group. |
| internet char _ ge type _ | String |   | No | PayByBandwi dth | The billing method of the public IP address of the node. |
| instance typ _ es | List<S tring> |   | No | ["ecs.c6.larg e"] | The type of instance. For more information, see the Instance types chapter in ECS User Guide. |
| vswitch ids _ | List<S tring> |   | No | ["vsw- wz9uwxhaw mtzg7u9h*** *"] | The IDs of vSwitches. |
| tee config _ | Struct | Body | No |   | The configuration about confidential computing for the cluster. |
| tee enable _ | Boole an |   | No | false | Specifies whether to enable confidential computing for the cluster. Valid values: true : enables confidential computing for the cluster false : disables confidential computing for the cluster Default value: false |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepool id _ | String | np737c3ac1ac684 703b9e10673aa2c **** | The ID of the node pool. |

| task id _ | String | T- 5fd211e924e1d00 787000293 | The ID of the task. |
|---|---|---|---|

**Example**

Sample requests

```
PUT /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "NodepoolId": "p31da1b38983f4511b490fc62108a****"
```

Sample success responses `XML` format

```xml
HTTP/1.1 200 OK Content-Type:application/xml <task_id>T-5fd211e924e1d00787000293</task_id> <nodepool_id>np737c3ac1ac684703b9e10673aa2c****</nodepool_id>
```

`JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
    "task_id": "T-5fd211e924e1d00787000293",
    "nodepool_id": "np737c3ac1ac684703b9e10673aa2c****"
```

##### 2.3.5.5 Query node pools

You can call the DescribeClusterNodePools operation to query node pools in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/nodepools HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| ClusterId | String | Path | Yes | cc0f87de0b8fb 403f86e10e20 4f83**** | The ID of the cluster. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| nodepools | Array of nodepool |   | The list of the returned node pools. |
| auto scaling _ | Struct |   | The configuration about auto scaling. |
| eip bandwidth _ | Integer | 5 | The peak bandwidth of the elastic IP address (EIP). |
| enable | Boolean | true | Indicates whether auto scaling is enabled. true : Auto scaling is enabled for the node pool. false : Auto scaling is disabled for the node pool. If you set this parameter to false , other parameters in the auto scaling section do not take _ effect. |
| max instances _ | Integer | 10 | The maximum number of Elastic Compute Service (ECS) instances supported by the node pool. |
| min instances _ | Integer | 2 | The minimum number of ECS instances. |
| type | String | cpu | The minimum number of ECS instances that must be kept in the node pool. Valid values: cpu : regular instance gpu : GPU-accelerated instance gpushare : shared GPU-accelerated instance spot : preemptible instance |
| kubernetes co _ nfig | Struct |   | The configuration of the cluster. |

| cms enabled _ | Boolean | true | Indicates where the CloudMonitor agent is installed on ECS nodes of the cluster. After the CloudMonitor agent is installed, you can view monitoring information about the ECS instances in the CloudMonitor console. Installation is recommended. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes |
|---|---|---|---|
| cpu policy _ | String | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. |
| labels | Array of label |   | The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs , https:// , or http:// . |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| node name m _ _ ode | String | customized,test.,5,. com | The name of the custom node. |
| overwrite host _ name | Boolean | false | Indicates whether the host name is overwritten. |
| runtime | String | docker | The name of the container runtime. |
| runtime versio _ n | String | 19.03.5 | The version of the container runtime. |

| taints | Array of taint |   | The taints that are added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. |
|---|---|---|---|
| effect | String | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| key | String | key | The key of a taint. |
| value | String | value | The value of a taint. |
| unschedulable | Boolean | false | Nodes that are newly added to the cluster are marked as unschedulable. If you select this option, the nodes are unschedulable when they are added to the cluster. You can go to the Nodes page and set the nodes as schedulable. |
| user data _ | String | IyEvYmluL3NoCmVj aG8gIkhlbGxvIEFD* ***IyEvYmluL3NoC mVjaG8gIkhlbGxvI EFD**** | The user-defined data of the node pool. For more information, see the User- defined data chapter in the ECS documentation. |
| nodepool info _ | Struct |   | The information about the node pool. |
| created | String | 2020-09- 27T19:14:09.1568 23496+08:00 | The time when the node pool was created. |

| is default _ | Boolean | true | Indicates whether the node pool is a default node pool. A Container Service cluster usually has only one default node pool. Valid values: true : The node pool is a default node pool. false : The node pool is not a default node pool. |
|---|---|---|---|
| name | String | default-nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| nodepool id _ | String | np615c0e0966124 216a0412e10afe0* *** | The ID of the node pool. |
| region id _ | String | cn-beijing | The region ID of the elastic container instance. |
| resource grou _ p id _ | String | rg- acfmyvw3wjm**** | The ID of the resource group. |
| type | String | ess | The type of the node pool. |
| updated | String | 2020-09- 27T20:37:46+08:0 0 | The time when the node pool was last updated. |
| scaling group _ | Struct |   | The configuration of the scaling group. |
| data disks _ | String | [ { "category" : "String", "size" : Long, "encrypted" : "String", "auto snapshot pol _ _ icy id" : "String" } ] _ | The configuration of data disks. |
| data disks _ | Array of data disk _ |   | The configurations of the data disks attached to the nodes in the node pool. The configurations include the disk type and disk size. |
| auto snapshot _ policy id _ _ | String | sp- 2zej1nogjvovnz4z* *** | The automatic backup policy when disk backup is enabled. |

| category | String |   | cloud ssd _ | The category of the data disk. |
|---|---|---|---|---|
| encrypted | String |   | true | Indicates whether the data disk is encrypted. |
| size | Long |   | 40 | The size of the data disk. Valid values: 40 to 32767. |
| image id _ | String |   | aliyun 2 1903 x64 _ _ _ 20G alibase 2020 | The ID of the custom image. You can call DescribeKubernetesVersionMetadata to query the images supported by ACK. |
|   |   |   | _ _ _ 0529.vhd |   |
| instance char _ ge type _ | String |   | PostPaid | The billing method of the nodes in the node pool. Valid values: PrePaid : the subscription billing method PostPaid : the pay-as-you-go billing method. |
| instance types _ | List |   | ["ecs.n4.large"] | The instance types of the nodes in the node pool. |
| internet charg _ e type _ | String |   | PayByBandwidth | The billing method of the public IP address of the node. |
| internet max _ _ bandwidth out _ | Integer |   | 10 | The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100. |
| login passwor _ d | String |   | ****** | The password for SSH logon. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. For security purposes, the returned password is encrypted. |
| multi az polic _ _ y | String |   | BALANCE | The ECS instance scaling policy for a multi-zone scaling group. |

| platform | String | AliyunLinux | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
|---|---|---|---|
| ram policy _ | String | KubernetesWorker Role-021dc54f- 929b-437a-8ae0- 34c24d3e**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage ECS instances. |
| scaling group _ _ id | String | asg- 2ze8n5qw4atggut8 **** | The ID of the scaling group. |
| scaling policy _ | String | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks. |
| security group _ id _ | String | sg- 2ze1iuk12m2sb4c4 **** | The ID of the security group. |
| system disk c _ _ ategory | String | cloud efficiency _ | The type of system disk. Valid values: cloud efficiency : ultra disk _ cloud ssd : standard SSD _ |
| system disk si _ _ ze | Integer | 120 | The system disk size of a node. Unit: GiB. Valid values: 20 to 500. |

| tags | Array of tag |   | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun or acs . Keys and values cannot contain https:// or http:// . |
|---|---|---|---|
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| vswitch ids _ | List | ["vsw- 2ze3ds0mdip0hdz8 i****"] | The IDs of vSwitches. |
| status | Struct |   | The status details about the node pool. |
| failed nodes _ | Integer | 0 | The number of failed nodes. |
| healthy nodes _ | Integer | 3 | The number of healthy nodes. |
| initial nodes _ | Integer | 0 | The number of nodes that are being created. |
| offline nodes _ | Integer | 0 | The number of offline nodes. |
| removing nod _ es | Integer | 0 | The number of nodes that are being removed. |
| serving nodes _ | Integer | 3 | The number of running nodes. |
| state | String | active | The status of the node pool. Valid values: active : The node pool is active. scaling : The node pool is being scaled. removing : Nodes are being removed from the node pool. deleting : The node pool is being deleted. updating : The node pool is being updated. |

| total nodes _ | Integer | 3 | The total number of nodes in the node pool. |
|---|---|---|---|
| tee config _ | Struct |   | The configurations of confidential computing. |
| tee enable _ | Boolean | false | Indicates whether confidential computing is enabled. Valid values: true : Confidential computing for the cluster is enabled. false : Confidential computing for the cluster is disabled. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/nodepools HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "cc0f87de0b8fb403f86e10e204f83****"
```

Sample success responses `XML` format

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
            <ram_policy>KubernetesWorkerRole-021dc54f-929b-437a-8ae0-34c24d3e****
</ram_policy>
            <data_disks>
                  <auto_snapshot_policy_id>sp-2zej1nogjvovnz4z****
</auto_snapshot_policy_id>
                  <encrypted>true</encrypted>
                  <size>40</size>
                  <category>cloud_ssd</category>
            </data_disks>
            <instance_charge_type>PostPaid</instance_charge_type>
            <login_password>******</login_password>
            <system_disk_category>cloud_efficiency</system_disk_category>
            <image_id>aliyun_2_1903_x64_20G_alibase_20200529.vhd</image_id>
```

```xml
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
<user_data>IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****</us er_data>
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
<health nodes>3</health nodes>
```

```xml
            <healthy_nodes>3</healthy_nodes>
      </status>
</nodepools>
```

`JSON` format `{`

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
            "user_data":
"IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****IyEvYmluL3NoCmVjaG8gIkhlbGxvIEFD****",
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
```

```json
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

##### 2.3.5.6 Query the details of a node pool

You can call the DescribeClusterNodePoolDetail operation to query the details of a node pool.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| ClusterId | String | Path | Yes | c23421cfa744 54bc8b37163f d19af**** | The ID of the cluster. |
|---|---|---|---|---|---|
| NodepoolId | String | Path | Yes | np31da1b389 83f4511b490f c62108a**** | The ID of the node pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| auto scaling _ | Struct |   | The auto scaling configurations of the queried node pool. |
| enable | Boolean | true | Indicates whether auto scaling is enabled. Valid values: true : Auto scaling is enabled for the node pool. false : Auto scaling is disabled for the node pool. If you set this parameter to false , other parameters in the auto scaling section does not take _ effect. |
| max instances _ | Integer | 10 | The maximum number of Elastic Compute Service (ECS) instances supported by the node pool. |
| min instances _ | Integer | 1 | The minimum number of ECS instances. |
| type | String | cpu | The minimum number of ECS instances that must be kept in the node pool. Valid values: cpu : regular instance gpu : GPU-accelerated instance gpushare : shared GPU-accelerated instance spot : preemptible instance |
| kubernetes co _ nfig | Struct |   | The configuration of the cluster. |

| cms enabled _ | Boolean | true | Indicates where the CloudMonitor agent is installed on ECS nodes of the cluster. After the CloudMonitor agent is installed, you can view monitoring information about the ECS instances in the CloudMonitor console. Installation is recommended. Valid values: true : installs the CloudMonitor agent on ECS nodes false : does not install the CloudMonitor agent on ECS nodes |
|---|---|---|---|
| cpu policy _ | String | none | The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later. static : allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity none : indicates that the default CPU affinity is used. |
| labels | Array of label |   | The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules: Each label is a case-sensitive key-value pair. You can add up to 20 labels. A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun , acs , https:// , or http:// . |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| node name m _ _ ode | String | customized,test.,5,. com | The name of the custom node. |
| overwrite host _ name | Boolean | false | Indicates whether the host name is overwritten. |
| runtime | String | docker | The name of the container runtime. |
| runtime versio _ n | String | 19.03.5 | The version of the container runtime. |

| taints | Array of taint |   | The taints that are added to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, toleration rules allow pods to be scheduled to nodes with matching taints. For more information, see taint-and- toleration. |
|---|---|---|---|
| effect | String | NoSchedule | The scheduling policy. Valid values: NoSchedule : Pods that do not tolerate this taint are not scheduled to nodes with this taint. This policy affects only the scheduling process and takes effect only for pods to be scheduled. Scheduled pods are not subject to this policy. NoExecute : Pods that do not tolerate this taint are evicted after this taint is added to the node. PreferNoSchedule : a preference policy on pods. Scheduled pods are not subject to this policy. If this taint is added to a node, the system tries to not schedule pods that do not tolerate this taint to the node. Default value: NoSchedule . |
| key | String | key | The key of a taint. |
| value | String | value | The value of a taint. |
| unschedulable | Boolean | false | Indicates whether the node is set to the unschedulable state. true : The node is set to the unschedulable state. false : The node is not set to the unschedulable state. |
| user data _ | String | IyEvYmluL3NoCmVj aG8gIkhlbGxvIEFD SyEi | The user-defined data of the node pool. For more information, see the User- defined data chapter in the ECS documentation. |
| nodepool info _ | Struct |   | The configuration of the node pool. |
| created | String | 2020-09- 27T19:14:09.1568 23496+08:00 | The time when the node pool was created. |

| is default _ | Boolean | true | Indicates whether the node pool is a default node pool. A Container Service cluster usually has only one default node pool. Valid values: true : The node pool is a default node pool. false : The node pool is not a default node pool. |
|---|---|---|---|
| name | String | default-nodepool | The name of the node pool. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-). |
| nodepool id _ | String | np615c0e0966124 216a0412e10afe0* *** | The ID of the created node pool. |
| region id _ | String | cn-beijing | The region ID of the elastic container instance. |
| resource grou _ p id _ | String | rg- acfmyvw3wjmb*** * | The ID of the resource group. |
| type | String | ess | The type of the node pool. |
| updated | String | 2020-09- 27T20:37:46+08:0 0 | The time when the node pool was last updated. |
| scaling group _ | Struct |   | The configuration of the scaling group. |
| data disks _ | Array of data disk _ |   | The configurations of the data disks attached to the nodes in the node pool. The configurations include the disk type and disk size. |
| auto snapshot _ policy id _ _ | String | sp- 2zej1nogjvovnz4z* *** | The automatic backup policy when disk backup is enabled. |
| category | String | cloud ssd _ | The category of the data disk. |
| encrypted | String | true | Indicates whether the data disk is encrypted. |

| size | Long |   | 40 | The size of the data disk. Valid values: 40 to 32767. |
|---|---|---|---|---|
| image id _ | String |   | aliyun 2 1903 x64 _ _ _ 20G alibase 2020 | The ID of the custom image. You can call DescribeKubernetesVersionMetadata to query the images supported by ACK. |
|   |   |   | _ _ _ 0529.vhd |   |
| instance char _ ge type _ | String |   | PayByBandwidth | The billing method of the public IP address of the node. |
| instance types _ | List |   | ["ecs.n4.large"] | The instance types of the nodes in the node pool. |
| internet charg _ e type _ | String |   | PayByTraffic | The billing method of the public IP address. |
| internet max _ _ bandwidth out _ | Integer |   | 10 | The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100. |
| login passwor _ d | String |   | ******** | The password for SSH logon. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. For security purposes, the returned password is encrypted. |
| multi az polic _ _ y | String |   | BALANCE | The ECS instance scaling policy for a multi-zone scaling group. |
| platform | String |   | AliyunLinux | The OS distribution. Valid values: CentOS : CentOS AliyunLinux : Alibaba Cloud Linux WindowsCore : Windows CentOS 7.6 : CentOS 7.6 ARM CentOS : CentOS 7.7 NeoKylin : Kylin Default value: AliyunLinux |
| ram policy _ | String |   | KubernetesWorker Role-021dc54f- 929b-437a-8ae0- 34c24d3e**** | The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage ECS instances. |

| ontainer Service | for Kubernetes |   | Developer Guide·Cluster API lis |
|---|---|---|---|

| scaling group _ _ id | String | asg- 2zeieod8giqmov7z **** | The ID of the scaling group. |
|---|---|---|---|
| scaling policy _ | String | release | The scaling mode of the scaling group. Valid values: release : the standard mode. ECS instances are created and released based on the resource usage. recycle : the swift mode. Auto scaling is implemented by creating, stopping, and starting ECS instances. This mode accelerates scaling activities. When an ECS instance is stopped, you are charged only the storage fees. This does not apply to ECS instances that use local disks. |
| security group _ id _ | String | sg- 2ze60ockeekspl3d* *** | The ID of the security group. |
| system disk c _ _ ategory | String | cloud efficiency _ | The type of system disk. Valid values: cloud efficiency : ultra disk _ cloud ssd : standard SSD _ |
| system disk si _ _ ze | Integer | 120 | The system disk size of a node. Unit: GiB. Valid values: 20 to 500. |
| tags | Array of tag |   | The labels that you want to add to the ECS instances. A key must be unique and cannot exceed 128 characters in length. Keys and values cannot start with aliyun or acs: . Keys and values cannot contain https:// or http:// . |
| key | String | key | The key of the label. |
| value | String | value | The value of the label. |
| vswitch ids _ | List | ["vsw- 2ze3ds0mdip0hdz8 i****"] | The IDs of vSwitches. |

| status | Struct |   | The status details about the nodes in the node pool. |
|---|---|---|---|
| failed nodes _ | Integer | 0 | The number of failed nodes. |
| healthy nodes _ | Integer | 3 | The number of healthy nodes. |
| initial nodes _ | Integer | 0 | The number of nodes that are being created. |
| offline nodes _ | Integer | 0 | The number of offline nodes. |
| removing nod _ es | Integer | 0 | The number of nodes that are being removed. |
| serving nodes _ | Integer | 3 | The number of running nodes. |
| state | String | active | The status of the node pool. Valid values: active : The node pool is active. scaling : The node pool is being scaled. removing : Nodes are being removed from the node pool. deleting : The node pool is being deleted. updating : The node pool is being updated. |
| total nodes _ | Integer | 3 | The total number of nodes in the node pool. |
| tee config _ | Struct |   | The configurations of confidential computing. |
| tee enable _ | Boolean | false | Indicates whether confidential computing is enabled. Valid values: true : Confidential computing for the cluster is enabled. false : Confidential computing for the cluster is disabled. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "NodepoolId": "np31da1b38983f4511b490fc62108a****"
```

Sample success responses `XML` format

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
```

```xml
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

`JSON` format `{`

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
        "datadisks": {
```

```json
data_dss:{
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
```

```json
        "failed_nodes": 0,
        "healthy_nodes": 3
```

##### 2.3.5.7 Delete a node pool

You can call the DeleteClusterNodepool operation to delete a node pool.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
DELETE /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c61da77e8bfb c4c4c999af2b 51b65**** | The ID of the cluster. |
| NodepoolId | String | Path | Yes | np30db56bcac 7843dca90b99 9c8928**** | The ID of the node pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| request id _ | String | 7263C978-3DBD- 4E06-B319- 793B38A2**** | The ID of the request. |

**Examples**

Sample requests

```
DELETE /clusters/[ClusterId]/nodepools/[NodepoolId] HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c61da77e8bfbc4c4c999af2b51b65****",
    "NodepoolId": "np30db56bcac7843dca90b999c8928****"
```

Sample success responses `XML` format

```xml
<request_id>7263C978-3DBD-4E06-B319-793B38A2****</request_id>
```

`JSON` format `{`

```json
    "request_id": "7263C978-3DBD-4E06-B319-793B38A2****"
```

### 2.4 Templates

#### 2.4.1 Create an orchestration template

You can call the CreateTemplate operation to create an orchestration template.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST|PUT /templates HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posi tion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| body | Struct | Body | No |   |   |
| template | String |   | Yes | service- account- template | The template content in the YAML format. |
| name | String |   | Yes | apiVersion: v1\nkind: ServiceAccoun t\nmetadata:\n name: test-sa | The template content in the YAML format. |
| description | String |   | No | this is test | The description of the template. |

| template type _ | String |   | No | kubernetes | The type of template. You can set the parameter to a custom value. If you set the parameter to kubernetes , the template is displayed on the Templates page in the console. If you set the parameter to compose , the template is not displayed in the console. We recommend that you set the parameter to kubernetes . Default value: compose . |
|---|---|---|---|---|---|
| tags | String |   | No | test | The label of the template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| template id _ | String | ba1fe77b-b01e- 4640-b77e- 8f1b80e3**** | The ID of the template. |

**Examples**

Sample requests

```
POST /templates HTTP/1.1 Common request headers
```

`{`

```json
    "name": "service-account-template",
    "template": "apiVersion:v1\\nkind:ServiceAccount\\nmetadata:\\n name:test-sa",
    "tags": "test",
    "description": "this is test",
    "template_type": "kubernetes"
```

Sample success responses `XML` format

```xml
<template_id>ba1fe77b-b01e-4640-b77e-8f1b80e3****</template_id>
```

`JSON` format `{`

```json
    "template_id": "ba1fe77b-b01e-4640-b77e-8f1b80e3****"
```

#### 2.4.2 Delete an orchestration template

You can call the DeleteTemplate operation to delete an orchestration template.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
DELETE /templates/[TemplateId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| TemplateId | String | Path | Yes | 20663627- 81ee-4cfe- 9b69- c96fcb84**** | The ID of the template. |

**Examples**

Sample requests

```
DELETE /templates/[TemplateId] HTTP/1.1 Common request headers
```

`{`

```json
    "TemplateId": "20663627-81ee-4cfe-9b69-c96fcb84****"
```

Sample success responses `XML` format

```
HTTP/1.1 200 OK
```

`JSON` format

```
HTTP/1.1 200 OK
```

#### 2.4.3 Query all orchestration templates

You can call the DescribeTemplates operation to query all orchestration templates.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /templates HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| template type _ | String | Quer y | Yes | kubernetes | The type of template. You can set this parameter to a custom value. If you set the parameter to kubernetes , the template is displayed on the Templates page in the console. If you set the parameter to compose , the template is not displayed on the Templates page in the console. Default value: kubernetes . |
| page num _ | Long | Quer y | No | 1 | The number of the page to return. Default value: 1. |
| page size _ | Long | Quer y | No | 10 | The number of entries to return on each page. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| page info _ | Struct |   | The pagination details. |
| page number _ | Long | 20 | The page number of the returned page. |
| page size _ | Long | 3 | The maximum number of entries returned per page. |
| total count _ | Long | 50 | The total number of entries returned. |
| templates | Array of template |   | The list of returned templates. |

| acl | String | private | The access control policy of the template. Valid values: private : The template is private. public : The template is public. shared : The template can be shared. Default value: private . |
|---|---|---|---|
| created | String | 2020-06- 10T16:30:16+08:0 0 | The time when the template was created. |
| description | String | a web server | The description of the template. |
| id | String | 874ec485-e7e6- 4373-8a3b- 47bde8ae**** | The ID of the template. |
| name | String | webserver | The name of the template. |
| tags | String | kubernetes | The label of the template. By default, the value is the name of the template. |
| template | String | apiVersion: apps/v1\nkind: Deployment\nmeta data:\n name: nginx-deployment- basic\n labels:\n app: nginx\nspec:\n replicas: 2\n selector:\n matchLabels:\n app: nginx\n template:\n metadata:\n labels:\n app: nginx\n spec:\n containers:\n - name: nginx\n image: busybox:latest\n ports:\n - containerPort: 80 | The template content in the YAML format. |

| template type _ | String | kubernetes | The type of template. This parameter can be set to a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If the parameter is set to compose , the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated. |
|---|---|---|---|
| template with _ hist id _ _ | String | ad81d115-7c8b- 47e7-a222- 9c28d7f6e588 | The ID of the parent template. The value of template with hist id is the _ _ _ same for each template version. This allows you to manage different template versions. |
| updated | String | 2020-06- 10T16:30:16+08:0 0 | The time when the template was updated. |

**Examples**

Sample requests

```
GET /templates HTTP/1.1 Common request headers
```

`{`

```
    "template\_type": "kubernetes"
```

Sample success responses `XML` format

```xml
<templates>
    <template>apiVersion: apps/v1\nkind: Deployment\nmetadata:\n name: nginx-
deployment-basic\n labels:\n app: nginx\nspec:\n replicas: 2\n selector:\n matchLabels: \n app: nginx\n template:\n metadata:\n labels:\n app: nginx\n spec:\n containers:\n name: nginx\n image: busybox:latest\n ports:\n - containerPort: 80</template>
    <template_with_hist_id>ad81d115-7c8b-47e7-a222-9c28d7f6e588</template_with_hist_id>
    <created>2020-06-10T16:30:16+08:00</created>
    <name>webserver</name>
    <description>a web server</description>
    <template_type>kubernetes</template_type>
    <acl>private</acl>
    <id>874ec485-e7e6-4373-8a3b-47bde8ae****</id>
    <updated>2020-06-10T16:30:16+08:00</updated>
    <tags>kubernetes</tags>
</templates> <page_info>
    <page_number>20</page_number>
    <total_count>50</total_count>
    <page_size>3</page_size>
</page_info>
```

`JSON` format `{`

```json
    "templates": {
        "template": "apiVersion: apps/v1\\nkind: Deployment\\nmetadata:\\n name: nginx-
deployment-basic\\n labels:\\n app: nginx\\nspec:\\n replicas: 2\\n selector:\\n matchL abels:\\n app: nginx\\n template:\\n metadata:\\n labels:\\n app: nginx\\n spec:\\n con tainers:\\n - name: nginx\\n image: busybox:latest\\n ports:\\n - containerPort: 80",
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

#### 2.4.4 Query an orchestration template

You can call the DescribeTemplateAttributeoperation to query the details of an orchestration template.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /templates/[TemplateId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| TemplateId | String | Path | Yes | 874ec485- e7e6-4373- 8a3b- 47bde8a**** | The ID of the template. |
| template type _ | String | Quer y | No | kubernetes | The type of template. The value can be a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If the value of the parameter is not kubernetes , the template is not displayed on the Templates page in the console. We recommend that you set the parameter to kubernetes . Default value: kubernetes . |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| body | Array of body |   | The details of the template. |
| acl | String | private | The access control policy of the template. |
| created | String | 2020-09- 16T19:21:29+08:0 0 | The time when the template was created. |
| description | String | test template | The description of the template. |
| id | String | 72d20cf8-a533- 4ea9-a10d- e7630d3d**** | The ID of the template. When you update a template, a new template ID is generated. |

| name | String | web | The name of the template. |
|---|---|---|---|
| tags | String | sa | The label of the template. |
| template | String | apiVersion: V1\n*** | The template content in the YAML format. |
| template type _ | String | kubernetes | The type of template. The value can be a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If the value of the parameter is not kubernetes , the template is not displayed on the Templates page in the console. We recommend that you set the parameter to kubernetes . Default value: kubernetes . |
| template with _ hist id _ _ | String | 874ec485-e7e6- 4373-8a3b- 47bde8ae**** | The unique ID of the template. The value remains unchanged after the template is updated. |
| updated | String | 2020-09- 16T19:21:29+08:0 0 | The time when the template was updated. |

**Examples**

Sample requests

```
GET /templates/[TemplateId] HTTP/1.1 Common request headers
```

`{`

```json
    "TemplateId": "874ec485-e7e6-4373-8a3b-47bde8a****"
```

Sample success responses `XML` format

```xml
<body>
      <template>apiVersion: V1\n***</template>
      <template_with_hist_id>874ec485-e7e6-4373-8a3b-47bde8ae****
</template_with_hist_id>
      <created>2020-09-16T19:21:29+08:00</created>
      <name>web</name>
      <description>test template</description>
      <template_type>kubernetes</template_type>
      <acl>private</acl>
      <id>72d20cf8-a533-4ea9-a10d-e7630d3d****</id>
      <updated>2020-09-16T19:21:29+08:00</updated>
      <tags>sa</tags>
</body>
```

`JSON` format `{`

```json
    "body": {
        "template": "apiVersion: V1\\n***",
        "template_with_hist_id": "874ec485-e7e6-4373-8a3b-47bde8ae****",
        "created": "2020-09-16T19:21:29+08:00",
        "name": "web",
        "description": "test template",
        "template_type": "kubernetes",
        "acl": "private",
        "id": "72d20cf8-a533-4ea9-a10d-e7630d3d****",
        "updated": "2020-09-16T19:21:29+08:00",
        "tags": "sa"
```

#### 2.4.5 Update an orchestration template

You can call the UpdateTemplate operation to update an orchestration template.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
PUT /templates/[TemplateId] HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| TemplateId | String | Path | Yes | 72d20cf8- a533-4ea9- a10d- e7630d3d270 8 | The ID of the template. |
|---|---|---|---|---|---|
| body | Struct | Body | No |   |   |
| template | String |   | No | service- account- template | The template content in the YAML format. |
| name | String |   | No | apiVersion: v1\nkind: ServiceAccoun t\nmetadata:\n name: test-sa | The template content in the YAML format. |
| description | String |   | No | this is test | The description of the template. |
| template type _ | String |   | No | kubernetes | The type of template. You can set the parameter to a custom value. If the parameter is set to kubernetes , the template is displayed on the Templates page in the console. If you set the parameter to compose , the template is not displayed in the console. We recommend that you set the parameter to kubernetes . Default value: compose . |
| tags | String |   | No | test | The label of the template. |

**Examples**

Sample requests

```
PUT /templates/[TemplateId] HTTP/1.1 Common request headers
```

`{`

```json
    "name": "service-account-template",
    "template": "apiVersion:v1\\nkind:ServiceAccount\\nmetadata:\\n name:test-sa",
    "tags": "test",
    "description": "this is test",
    "template_type": "kubernetes"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

### 2.5 Add-ons

#### 2.5.1 Install a component in a cluster

You can call the InstallClusterAddons to install a component in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/components/install HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posi tion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e296 1451182edacd 74faf**** | The ID of the cluster. |
| body | Array | Body | No |   | The request body parameters. |
| config | String |   | No | {\"IngressDas hboardEnable d\":\"true\",\"sl s project nam _ _ e\":\"your sls _ _ project name\ _ "}"} | The component configurations. |
| name | String |   | Yes | ags-metrics- collector | The name of the component. |
| version | String |   | Yes | v1.0.0.2- cc3b2d6- aliyun | The version of the component. Note You can call the DescribeClusterAddonsVersio n operation to query the version of the component. For more information, see Query the details of the components in a cluster. |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/components/install HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

Sample success responses `XML` format

```
HTTP/1.1 200 OK
```

`JSON` format

```
HTTP/1.1 200 OK
```

#### 2.5.2 Query the details of the components in a cluster

**a cluster**

You can call the DescribeAddons operation to query the details of the components that are installed in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/components/metadata HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| region | String | Quer y | Yes | cn-beijing | The ID of the region where the cluster is deployed. |
| cluster type _ | String | Quer y | No | Kubernetes | The type of cluster. Valid values: Kubernetes : dedicated Kubernetes cluster or dedicated edge Kubernetes cluster |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| ComponentGr oups | Array of ComponentGr oup |   | The list of the returned components. |
|---|---|---|---|
| group name _ | String | storage | The name of the component group. |
| items | Array of item |   | The names of the components in the component group. |
| name | String | flexvolume | The name of the component. |
| StandardComp onents | Struct |   | Standard components. |
| key | Struct |   | The details of the standard components. |
| description | String | test | The description of the component. |
| disabled | Boolean | false | Indicates whether the automatic installation of the component is disabled. By default, some optional components, such as components for logging and Ingresses, are installed when a cluster is created. You can set this parameter to disable the automatic installation of a component. Valid values: true : disables the automatic installation of a component. false : allows the automatic installation of the component. |
| name | String | ack-arena | The name of the component. |
| required | String | false | Indicates whether the component is required in a Container Service cluster. Valid values: true : The component is required and must be installed when a cluster is created. false : The component is optional. After a cluster is created, you can go to the Add-ons page to install the component. |
| version | String | 0.5.0 | The version of the component. |

**Examples**

Sample requests

```
GET /clusters/components/metadata HTTP/1.1 Common request headers
```

`{`

```json
    "region": "cn-beijing"
```

Sample success responses `XML` format

```xml
<StandardComponents>
    <key>
        <name>ack-arena</name>
        <description>test</description>
        <disabled>false</disabled>
        <version>0.5.0</version>
        <required>false</required>
    </key>
</StandardComponents> <ComponentGroups>
    <group_name>storage</group_name>
    <items>
        <name>flexvolume</name>
    </items>
</ComponentGroups>
```

`JSON` format `{`

```json
    "StandardComponents": {
        "key": {
            "name": "ack-arena",
            "description": "test",
            "disabled": false,
            "version": "0.5.0",
            "required": false
```

`},`

```json
    "ComponentGroups": {
        "group_name": "storage",
        "items": {
            "name": "flexvolume"
```

#### 2.5.3 Query components

You can call the DescribeClusterAddonsVersion operation to query the components that are installed in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/components/version HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c82e6987e296 1451182edacd 74faf**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| key | Struct |   | The details of the component. |
| can upgrade _ | Boolean | false | Indicates whether the component is upgradable. Valid values: true : The component is upgradable. false : The component is not upgradable. |
| changed | String | false | Indicates whether the component is upgraded. Valid values: true : The component is upgraded. false : The component is not upgraded. |
| component na _ me | String | ack-node-problem- detector | The name of the component. |
| exist | Boolean | true | Indicates whether the component was installed. Valid values: true : The component was installed. false : The component was not installed. |
| message | String | A plug-in that detects exceptions and reports them to the Kubernetes event center. | Additional information about whether the component is upgradable. |

| next version _ | String | 1.2.1 | The version to which the component can be upgraded. |
|---|---|---|---|
| policy | String | overwrite | The upgrade policy of the component. overwrite : The component configurations of the later version overwrite those of the current version. Default value: overwrite . |
| ready to upgr _ _ ade | String | false | Indicates whether the component meets the upgrade conditions. Valid values: true : The component meets the upgrade conditions. false : The component does not meet the upgrade conditions. |
| required | Boolean | false | Indicates whether the component is required in the cluster. Valid values: true : The component is required in the cluster. false : The component is not required in the cluster. |
| value | String | npd:\n # Custom monitor definitions to add to Node Problem Detector **** | The custom parameter setting. When you install a component, you can customize parameter settings for the component. |
| version | String | 1.2.1 | The current version of the component. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/components/version HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c82e6987e2961451182edacd74faf****"
```

Sample success responses `XML` format

```xml
<key>
      <exist>true</exist>
      <component_name>ack-node-problem-detector</component_name>
      <can_upgrade>false</can_upgrade>
      <ready_to_upgrade>false</ready_to_upgrade>
      <message>A plug-in that detects node exceptions and reports them to the
Kubernetes event center.</message>
      <value>npd:\n # Custom monitor definitions to add to Node Problem Detector ****</
value>
      <version>1.2.1</version>
      <required>false</required>
      <policy>overwrite</policy>
      <changed>false</changed>
      <next_version>1.2.1</next_version>
</key>
```

`JSON` format `{`

```json
    "key": {
        "exist": true,
        "component_name": "ack-node-problem-detector",
        "can_upgrade": false,
        "ready_to_upgrade": false,
        "message": "A plug-in that detects node exceptions and reports them to the
Kubernetes event center.",
        "value": "npd:\\n # Custom monitor definitions to add to Node Problem Detector
****",
        "version": "1.2.1",
        "required": false,
        "policy": "overwrite",
        "changed": false,
        "next_version": "1.2.1"
```

#### 2.5.4 Query the upgrade status of components in a cluster

**components in a cluster**

You can call the DescribeClusterAddonsUpgradeStatus operation to query the upgrade status of the specified components in a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
GET /clusters/[ClusterId]/components/upgradestatus HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c23421cfa744 54bc8b37163f d19af**** | The ID of the cluster. |
| componentIds | List<St ring> | Quer y | Yes | ["metric- server"] | The name of the component. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/components/upgradestatus HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c23421cfa74454bc8b37163fd19af****",
    "componentIds": "[metric-server"]
```

Sample success responses `XML` format

```
HTTP/1.1 200 OK
```

`JSON` format

```
HTTP/1.1 200 OK
```

#### 2.5.5 Upgrade a component in a cluster

You can call the UpgradeClusterAddons operation to upgrade a specified component in a cluster to the required version.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/components/upgrade HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| ClusterId | String | Path |   | Yes | cf4299b79b3e 34226abfdc80 a4bda**** | The ID of the cluster. |   |   |
|---|---|---|---|---|---|---|---|---|
| body | Array | Body |   | No |   | The request parameters for the operation. |   |   |
| component na _ me | String |   |   | Yes | coredns | The name of the component. |   |   |
| next version _ | String |   |   |   |   | The required version. You can call the DescribeClusterAddonsVersion operation to query the version to which the component can be upgraded. |   |   |
|   |   |   |   |   |   |   | DescribeClusterAddonsVersion |   |
|   |   |   |   | Yes | 1.6.7 |   |   |   |
| version | String |   |   | No | v1.6.2 | The current version of the component. |   |   |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/components/upgrade HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "cf4299b79b3e34226abfdc80a4bda****"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

#### 2.5.6 Uninstall components from a cluster

You can call the UnInstallClusterAddons operation to uninstall components from a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /clusters/[ClusterId]/components/uninstall HTTP/1.1
```

**Request parameters**

| 57 |   |   |   |   | > Document Version: 2026082 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Path | Yes | c5b5e80b0b64 a4bf6939d2d8 fbbc5**** | The ID of the cluster. |
| addons | Array | Body | No |   | The list of components that you want to uninstall. The list is an array. |
| name | String |   | No | ack-node- problem- detector | The name of the component. |

**Examples**

Sample requests

```
POST /clusters/[ClusterId]/components/uninstall HTTP/1.1 Common request headers
```

`{`

```json
    "ClusterId": "c5b5e80b0b64a4bf6939d2d8fbbc5****"
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK
```

### 2.6 Policies

#### 2.6.1 Deploy a policy instance in an ACK cluster

**cluster**

You can call the DeployPolicyInstance operation to deploy a policy instance in a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
POST /clusters/{cluster_id}/policies/{policy_name} HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| cluster id _ | strin g |   | Yes | c8155823d057948c69a** ** | The cluster ID. |
| policy nam _ e | strin g |   | Yes | ACKAllowedRepos | The name of the policy. |
| body | obje ct |   | No | { "action" : "deny", "namespaces" : [ "default" ], "parameters": { "repos": [ "registry-vpc.cn- hangzhou.aliyuncs.com/a cs/", "registry.cn- hangzhou.aliyuncs.com/a cs/" ] } } | action: the action of the policy. Valid values: deny and warn. namespaces: the applicable scope of the policy instance. If you leave the parameter empty, the policy instance applies to all namespaces in the cluster. parameters: the parameters of the policy instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

**Examples**

Sample requests

```
POST /clusters/c8155823d057948c69a****/policies/ACKAllowedRepos HTTP/1.1
```

`{`

```json
  "action" : "deny",
  "namespaces" : [ "default" ],
  "parameters": {
     "repos": [
          "registry-vpc.cn-hangzhou.aliyuncs.com/acs/",
          "registry.cn-hangzhou.aliyuncs.com/acs/"
```

`]` Sample success responses `JSON` format `{`

```json
  "instances" : [ "allowed-repos-kqxnc" ]
```

`XML` format

```xml
<DeployPolicyInstanceResponse>
    <instances>allowed-repos-kqxnc</instances>
</DeployPolicyInstanceResponse>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

#### 2.6.2 DescribePolicyInstancesStatus

You can call the DescribePolicyInstancesStatus operation to query information about policy instances in a Container Service for Kubernetes (ACK) cluster. The information includes the number of instances deployed from each policy and the number of policy instances of each severity level.

**Request headers**

The DescribePolicyInstancesStatus operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request syntax**

```
GET /clusters/ClusterId/policies/status HTTP/1.1
```

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Path | Yes | c8155823d057948c69a* *** | The cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0B26C1D0-*** | The request ID. |

**Examples**

Sample requests

```
GET /clusters/[ClusterId]/policies/status HTTP/1.1 &ClusterId=c8155823d057948c69a**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "policy_instances" : [ {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKBlockNodePort",
    "policy_description" : "Disallows all Services with type NodePort.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKExternalIPs",
    "policy_description" : "Restricts Services from containing externalIPs except those
in a provided allowlist.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPHostNamespace",
    "policy_description" : "Controls usage of host namespaces.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPReadOnlyRootFilesystem",
    "policy_description" : "Requires the use of a read only root file system.",
    "policy_severity" : "medium"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPVolumeTypes",
    "policy_description" : "Controls usage of volume types.",
    "policy_severity" : "medium"
  }, {
    "policy_category" : "infra",
    "policy_name" : "ACKOSSStorageLocationConstraint",
    "policy_description" : "Restricts location of oss storage in cluster.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKBlockAutoinjectServiceEnv",
    "policy_description" : "Disable autoinjecting information about services into pod's
environment variables.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKImageDigests",
    "policy_description" : "Requires container images to contain a digest.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPAllowedUsers",
```

```json
    "policy_description" : "Controls the user and group IDs of the container.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPHostFilesystem",
    "policy_description" : "Controls usage of the host filesystem.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "infra",
    "policy_name" : "ACKBlockProcessNamespaceSharing",
    "policy_description" : "Restricts shareProcessNamespace used in pod.",
    "policy_severity" : "high",
    "policy_instances_count" : 2
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPCapabilities",
    "policy_description" : "Controls Linux capabilities.",
    "policy_severity" : "high",
    "policy_instances_count" : 5
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPForbiddenSysctls",
    "policy_description" : "Controls the `sysctl` profile used by containers.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPSeccomp",
    "policy_description" : "Controls the seccomp profile used by containers.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKBlockLoadBalancer",
    "policy_description" : "Disallows all Services with type LoadBalancer.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPAppArmor",
    "policy_description" : "Controls the AppArmor profile used by containers.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPPrivilegedContainer",
    "policy_description" : "Controls running of privileged containers.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPProcMount",
    "policy_description" : "Controls the allowed `procMount` types for the container.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPSELinuxV2",
    "policy_description" : "Controls the SELinux context of the container.",
    "policy_severity" : "low"
```

```json
  }, {
    "policy_category" : "infra",
    "policy_name" : "ACKEmptyDirHasSizeLimit",
    "policy_description" : "Requires that emptydir volume must have a `sizelimit` defin
ed.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPAllowPrivilegeEscalationContainer",
    "policy_description" : "Controls restricting escalation to root privileges.",
    "policy_severity" : "medium"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPFSGroup",
    "policy_description" : "Controls allocating an FSGroup that owns the Pod's
volumes.",
    "policy_severity" : "medium"
  }, {
    "policy_category" : "compliance",
    "policy_name" : "ACKPodsRequireSecurityContext",
    "policy_description" : "Requires that Pods must have a `securityContext` defined.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "compliance",
    "policy_name" : "ACKRestrictNamespaces",
    "policy_description" : "Restricts resources from using the `default` namespace.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKContainerLimits",
    "policy_description" : "Requires containers to have memory and CPU limits set and w
ithin a specified maximum amount.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPHostNetworkingPorts",
    "policy_description" : "Controls usage of host networking and ports.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKBlockAutomountToken",
    "policy_description" : "Disable automounting API credentials.",
    "policy_severity" : "high"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKRequiredLabels",
    "policy_description" : "Requires all resources to contain a specified label with a
value matching a provided regular expression.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "psp",
    "policy_name" : "ACKPSPFlexVolumes",
    "policy_description" : "Controls the allowlist of Flexvolume drivers.",
    "policy_severity" : "medium"
```

`{`

```json
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKAllowedRepos",
    "policy_description" : "Requires container images to begin with a repo string from
a specified list.",
    "policy_severity" : "high",
    "policy_instances_count" : 4
  }, {
    "policy_category" : "compliance",
    "policy_name" : "ACKNoEnvVarSecrets",
    "policy_description" : "Restricts secrets used in pod envs.",
    "policy_severity" : "medium",
    "policy_instances_count" : 1
  }, {
    "policy_category" : "compliance",
    "policy_name" : "ACKRestrictRoleBindings",
    "policy_description" : "Restricts use of the cluster-admin role.",
    "policy_severity" : "medium"
  }, {
    "policy_category" : "infra",
    "policy_name" : "ACKLocalStorageRequireSafeToEvict",
    "policy_description" : "Restricts safe to evict annotation existing in pod with loc
al storage.",
    "policy_severity" : "low"
  }, {
    "policy_category" : "k8s-general",
    "policy_name" : "ACKRequiredProbes",
    "policy_description" : "Requires Pods to have readiness and/or liveness probes.",
    "policy_severity" : "medium"
  } ],
  "instances_severity_count" : {
    "high" : 11,
    "medium" : 1
```

`XML` format

```xml
<policy_instances><policy_category>k8s-general</policy_category> <policy_name>ACKBlockNodePort</policy_name><policy_description>Disallows all Services w ith type NodePort.</policy_description><policy_severity>high</policy_severity></policy_ instances><policy_instances><policy_category>k8s-general</policy_category> <policy_name>ACKExternalIPs</policy_name><policy_description>Restricts Services from co ntaining externalIPs except those in a provided allowlist.</policy_description><policy_ severity>high</policy_severity></policy_instances><policy_instances> <policy_category>psp</policy_category><policy_name>ACKPSPHostNamespace</policy_name><po licy_description>Controls usage of host namespaces.</policy_description> <policy_severity>high</policy_severity></policy_instances><policy_instances> <policy_category>psp</policy_category> <policy_name>ACKPSPReadOnlyRootFilesystem</policy_name><policy_description>Requires the use of a read only root file system.</policy_description> <policy_severity>medium</policy_severity></policy_instances><policy_instances><policy_c ategory>psp</policy_category><policy_name>ACKPSPVolumeTypes</policy_name> <policy_description>Controls usage of volume types.</policy_description>
```

```xml
<policy_severity>medium</policy_severity></policy_instances><policy_instances><policy_c ategory>infra</policy_category> <policy_name>ACKOSSStorageLocationConstraint</policy_name><policy_description>Restricts location of oss storage in cluster.</policy_description> <policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>k8s-general</policy_category> <policy_name>ACKBlockAutoinjectServiceEnv</policy_name><policy_description>Disable auto injecting information about services into pod&#x27;s environment variables.</policy_des cription><policy_severity>low</policy_severity></policy_instances><policy_instances><po licy_category>k8s-general</policy_category><policy_name>ACKImageDigests</policy_name><p olicy_description>Requires container images to contain a digest.</policy_description><p olicy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>psp</policy_category><policy_name>ACKPSPAllowedUsers</policy_name><pol icy_description>Controls the user and group IDs of the container.</policy_description>< policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>psp</policy_category><policy_name>ACKPSPHostFilesystem</policy_name><p olicy_description>Controls usage of the host filesystem.</policy_description><policy_se verity>high</policy_severity></policy_instances><policy_instances> <policy_category>infra</policy_category> <policy_name>ACKBlockProcessNamespaceSharing</policy_name><policy_description>Restricts shareProcessNamespace used in pod.</policy_description> <policy_severity>high</policy_severity> <policy_instances_count>2</policy_instances_count></policy_instances><policy_instances> <policy_category>psp</policy_category><policy_name>ACKPSPCapabilities</policy_name><pol icy_description>Controls Linux capabilities.</policy_description> <policy_severity>high</policy_severity> <policy_instances_count>5</policy_instances_count></policy_instances><policy_instances> <policy_category>psp</policy_category><policy_name>ACKPSPForbiddenSysctls</policy_name> <policy_description>Controls the `sysctl` profile used by containers. </policy_description><policy_severity>high</policy_severity></policy_instances><policy_ instances><policy_category>psp</policy_category> <policy_name>ACKPSPSeccomp</policy_name><policy_description>Controls the seccomp profil e used by containers.</policy_description><policy_severity>low</policy_severity></polic y_instances><policy_instances><policy_category>k8s-general</policy_category><policy_nam e>ACKBlockLoadBalancer</policy_name><policy_description>Disallows all Services with typ e LoadBalancer.</policy_description><policy_severity>high</policy_severity> </policy_instances><policy_instances><policy_category>psp</policy_category> <policy_name>ACKPSPAppArmor</policy_name><policy_description>Controls the AppArmor prof ile used by containers.</policy_description><policy_severity>low</policy_severity></pol icy_instances><policy_instances><policy_category>psp</policy_category> <policy_name>ACKPSPPrivilegedContainer</policy_name><policy_description>Controls runnin g of privileged containers.</policy_description><policy_severity>high</policy_severity> </policy_instances><policy_instances><policy_category>psp</policy_category> <policy_name>ACKPSPProcMount</policy_name><policy_description>Controls the allowed `pro cMount` types for the container.</policy_description> <policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>psp</policy_category><policy_name>ACKPSPSELinuxV2</policy_name><policy _description>Controls the SELinux context of the container.</policy_description><policy _severity>low</policy_severity></policy_instances><policy_instances> <policy_category>infra</policy_category> <policy_name>ACKEmptyDirHasSizeLimit</policy_name><policy_description>Requires that emp tydir volume must have a `sizelimit` defined.</policy_description> <policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>psp</policy_category>
```

`/`

```xml
<policy_name>ACKPSPAllowPrivilegeEscalationContainer</policy_name> <policy_description>Controls restricting escalation to root privileges. </policy_description><policy_severity>medium</policy_severity></policy_instances><polic y_instances><policy_category>psp</policy_category> <policy_name>ACKPSPFSGroup</policy_name><policy_description>Controls allocating an FSGr oup that owns the Pod&#x27;s volumes.</policy_description> <policy_severity>medium</policy_severity></policy_instances><policy_instances><policy_c ategory>compliance</policy_category> <policy_name>ACKPodsRequireSecurityContext</policy_name><policy_description>Requires th at Pods must have a `securityContext` defined.</policy_description> <policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>compliance</policy_category> <policy_name>ACKRestrictNamespaces</policy_name><policy_description>Restricts resources from using the `default` namespace.</policy_description> <policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>k8s-general</policy_category> <policy_name>ACKContainerLimits</policy_name><policy_description>Requires containers to have memory and CPU limits set and within a specified maximum amount.</policy_descripti on><policy_severity>low</policy_severity></policy_instances><policy_instances><policy_c ategory>psp</policy_category><policy_name>ACKPSPHostNetworkingPorts</policy_name><polic y_description>Controls usage of host networking and ports.</policy_description><policy_ severity>high</policy_severity></policy_instances><policy_instances> <policy_category>k8s-general</policy_category> <policy_name>ACKBlockAutomountToken</policy_name><policy_description>Disable automounti ng API credentials.</policy_description><policy_severity>high</policy_severity></policy _instances><policy_instances><policy_category>k8s-general</policy_category> <policy_name>ACKRequiredLabels</policy_name><policy_description>Requires all resources to contain a specified label with a value matching a provided regular expression.</poli cy_description><policy_severity>low</policy_severity></policy_instances> <policy_instances><policy_category>psp</policy_category> <policy_name>ACKPSPFlexVolumes</policy_name><policy_description>Controls the allowlist of Flexvolume drivers.</policy_description><policy_severity>medium</policy_severity></p olicy_instances><policy_instances><policy_category>k8s-general</policy_category><policy _name>ACKAllowedRepos</policy_name><policy_description>Requires container images to beg in with a repo string from a specified list.</policy_description> <policy_severity>high</policy_severity> <policy_instances_count>4</policy_instances_count></policy_instances><policy_instances> <policy_category>compliance</policy_category> <policy_name>ACKNoEnvVarSecrets</policy_name><policy_description>Restricts secrets used in pod envs.</policy_description><policy_severity>medium</policy_severity> <policy_instances_count>1</policy_instances_count></policy_instances><policy_instances> <policy_category>compliance</policy_category> <policy_name>ACKRestrictRoleBindings</policy_name><policy_description>Restricts use of the cluster-admin role.</policy_description><policy_severity>medium</policy_severity></ policy_instances><policy_instances><policy_category>infra</policy_category><policy_name >ACKLocalStorageRequireSafeToEvict</policy_name><policy_description>Restricts safe to e vict annotation existing in pod with local storage.</policy_description> <policy_severity>low</policy_severity></policy_instances><policy_instances> <policy_category>k8s-general</policy_category> <policy_name>ACKRequiredProbes</policy_name><policy_description>Requires Pods to have r eadiness and/or liveness probes.</policy_description> <policy_severity>medium</policy_severity></policy_instances><instances_severity_count>< high>11</high><medium>1</medium></instances_severity_count>
```

#### 2.6.3 Update a policy instance in an ACK cluster

**cluster**

You can call the ModifyPolicyInstance operation to update a policy instance in a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
PUT /clusters/ClusterId/policies/PolicyName HTTP/1.1
```

`{`

```json
  "action" : "String",
  "instance_name" : "String",
  "namespaces" : [ "String" ]
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Path | Yes | c8155823d057948c69a** ** | The cluster ID. |
| PolicyNam e | Strin g | Path | Yes | ACKAllowedRepos | The name of the policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0B26C1D0-*** | The request ID. |

**Examples**

Sample requests

```
PUT /clusters/c8155823d057948c69a****/policies/ACKAllowedRepos HTTP/1.1
```

`{`

```json
  "action" : "deny",
  "instance_name" : "allowed-repos-cbhhb",
  "namespaces" : [ ["test3","test4" ]
```

Sample success responses `JSON` format `{`

```json
  "instances" : [ "allowed-repos-kqxnc" ]
```

`XML` format

```xml
<instances>allowed-repos-kqxnc</instances>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

#### 2.6.4 Query policy instances that are deployed in an ACK cluster

**deployed in an ACK cluster**

You can call the DescribePolicyInstances operation to query policy instances that are deployed in a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
GET /clusters/ClusterId/policies HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Path | true | c8155823d057948c69a** ** | The cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 312F4BC4-*** | The request ID. |

**Examples**

Sample requests

```
GET /clusters/c8155823d057948c69a****/policies? policy_name=ACKPSPCapabilities&instance_name=allowed-repos-cz4s2 HTTP/1.1
```

Sample success responses `JSON` format

```json
[ {
  "ali_uid" : "16298168****",
  "cluster_id" : "c8155823d057948c69a****",
  "instance_name" : "no-env-var-secrets-****",
  "policy_name" : "ACKPSPCapabilities",
  "policy_category" : "k8s-general",
  "policy_description" : "Restricts secrets used in pod envs",
  "policy_parameters" : "\"restrictedNamespaces\": [ \"test\" ]",
  "policy_severity" : "low",
  "policy_scope" : "*",
  "policy_action" : "deny"
} ]
```

`XML` format

```xml
<DescribePolicyInstancesResponse>
    <ali_uid>16298168****</ali_uid>
    <cluster_id>c8155823d057948c69a****</cluster_id>
    <instance_name>no-env-var-secrets-****</instance_name>
    <policy_name>ACKPSPCapabilities</policy_name>
    <policy_category>k8s-general</policy_category>
    <policy_description>Restricts secrets used in pod envs</policy_description>
    <policy_parameters>"restrictedNamespaces": [ "test" ]</policy_parameters>
    <policy_severity>low</policy_severity>
    <policy_scope>*</policy_scope>
    <policy_action>deny</policy_action>
</DescribePolicyInstancesResponse>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

#### 2.6.5 Query information about policies in an ACK cluster

**ACK cluster**

You can call the DescribePolicyGovernanceInCluster operation to query information about policies in a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
GET /clusters/cluster_id/policygovernance HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Path | true | c8155823d057948c69a** ** | The cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0B26C1D0-*** | The request ID. |

**Examples**

Sample requests

```
GET /clusters/cluster_id/policygovernance HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "on_state" : [ {
    "enabled_count" : 0,
    "total" : 14,
    "severity" : "low"
  }, {
    "enabled_count" : 2,
    "total" : 13,
    "severity" : "high"
  }, {
    "enabled_count" : 1,
    "total" : 8,
    "severity" : "medium"
  } ],
  "admit_log" : {
    "progress" : "Complete",
    "count" : 75,
    "log" : [ {
      "__source__" : "192.168.0.188",
      "__tag__:__hostname__" : "iZwz98e621h0kvki3ja****",
      "__tag__:__pack_id__" : "63DE8FD17599E86****",
      "__tag__:__path__" : "/policy_admit_logs/gatekeeper_admit.log",
      "__tag__:__receive_time__" : "1631168040",
      "__tag__:__user_defined_id__" : "k8s-group-cb36d98a701ef4742b50603866809****",
      "__tag__:_container_ip_" : "10.102.0.89",
      "__tag__:_container_name_" : "manager",
      "__tag__:_image_name_" : "registry-vpc.cn-
shenzhen.aliyuncs.com/acs/gatekeeper:v3.6.0.60-g72c4896-aliyun",
      "__tag__:_namespace_" : "kube-system",
      "__tag__:_node_ip_" : "192.168.0.188",
      "__tag__:_node_name_" : "cn-shenzhen.192.168.XX.XX",
      "__tag__:_pod_name_" : "gatekeeper-7648f64cc8-27nd4",
```

`"`

```
tag :poduid":"11083b05-eecd-454c-8d22-81c83ce1****",
```

```
      __tag__:_pod_uid_ : 11083b05eecd454c8d2281c83ce1
```

`,`

```json
      "__time__" : "1631168037",
      "__topic__" : "",
      "cluster_id" : "cb36d98a701ef4742b50603866809****",
      "constraint_action" : "deny",
      "constraint_api_version" : "v1beta1",
      "constraint_group" : "constraints.gatekeeper.sh",
      "constraint_kind" : "ACKAllowedRepos",
      "constraint_name" : "allowed-repos-80970511-c93d-4c40-b692-be18c077****",
      "event_msg" : "Admission webhook \"validation.gatekeeper.sh\" denied request, Res
ource Namespace: default, Constraint: allowed-repos-80970511-c93d-4c40-b692-be18c077038 2, Message: container <nginx> has an invalid image repo <nginx:1.7.9>, allowed repos ar e [\"registry.cn-shanghai.aliyuncs.com/acs/\", \"registry.cnhangzhou.aliyuncs.com/acs/\"]",
      "event_reason" : "GatekeeperFailedAdmission",
      "event_type" : "violation",
      "level" : "info",
      "logger" : "ack_policy_admit_log_for_sls",
      "msg" : "container <nginx> has an invalid image repo <nginx:1.7.9>, allowed repos
are [\"registry.cn-shanghai.aliyuncs.com/acs/\", \"registry.cnhangzhou.aliyuncs.com/acs/\"]",
      "process" : "admission",
      "request_uid" : "9db8f008-c2e8-4723-a380-18ef358c2827",
      "request_username" : "system:serviceaccount:kube-system:replicaset-controller",
      "resource_api_version" : "v1",
      "resource_group" : "",
      "resource_kind" : "Pod",
      "resource_name" : "nginx-deployment-basic2-84ccb74bfc-df22p",
      "resource_namespace" : "default",
      "time" : "2021-09-09T06:13:57Z",
      "ts" : "1631168037.444757"
    }, {
      "__source__" : "192.168.XX.XX"
    } ]
```

`},`

```json
  "Violation" : {
    "totalViolations" : {
      "deny" : [ {
        "severity" : "high",
        "violations" : 75
      }, {
        "severity" : "medium",
        "violations" : 0
      } ],
      "warn" : [ {
        "severity" : "high",
        "violations" : 0
      }, {
        "severity" : "medium",
        "violations" : 0
      } ]
```

`},`

```json
    "violations" : {
      "deny" : [ {
        "policyName" : "policy-gatekeeper-ackallowedrepos",
```

```json
        "policyDescription" : "Requires container images to begin with a repo string fr
om a specified list.",
        "severity" : "high",
        "violations" : 11
      }, {
        "policyName" : "policy-gatekeeper-ackpspcapabilities",
        "policyDescription" : "Controls Linux capabilities.",
        "severity" : "high",
        "violations" : 81
      } ]
```

`XML` format

```xml
<DescribePolicyGovernanceInClusterResponse>
    <on_state>
        <enabled_count>0</enabled_count>
        <total>14</total>
        <severity>low</severity>
    </on_state>
    <on_state>
        <enabled_count>2</enabled_count>
        <total>13</total>
        <severity>high</severity>
    </on_state>
    <on_state>
        <enabled_count>1</enabled_count>
        <total>8</total>
        <severity>medium</severity>
    </on_state>
    <admit_log>
        <progress>Complete</progress>
        <count>75</count>
        <log>
            <__source__>192.168.0.188</__source__>
            <__tag__:__hostname__>iZwz98e621h0kvki3ja****</__tag__:__hostname__>
            <__tag__:__pack_id__>63DE8FD17599E86****</__tag__:__pack_id__>
<__tag__:__path__>/policy_admit_logs/gatekeeper_admit.log</__tag__:__path__>
            <__tag__:__receive_time__>1631168040</__tag__:__receive_time__>
            <__tag__:__user_defined_id__>k8s-group-cb36d98a701ef4742b50603866809****
</__tag__:__user_defined_id__>
            <__tag__:_container_ip_>10.102.0.89</__tag__:_container_ip_>
            <__tag__:_container_name_>manager</__tag__:_container_name_>
            <__tag__:_image_name_>registry-vpc.cn-
shenzhen.aliyuncs.com/acs/gatekeeper:v3.6.0.60-g72c4896-aliyun</__tag__:_image_name_>
            <__tag__:_namespace_>kube-system</__tag__:_namespace_>
            <__tag__:_node_ip_>192.168.0.188</__tag__:_node_ip_>
            <__tag__:_node_name_>cn-shenzhen.192.168.XX.XX</__tag__:_node_name_>
            <__tag__:_pod_name_>gatekeeper-7648f64cc8-27nd4</__tag__:_pod_name_>
            <__tag__:_pod_uid_>11083b05-eecd-454c-8d22-81c83ce1****</__tag__:_pod_uid_>
```

`<`

```
time >1631168037</ time
```

`>`

```xml
            <__time__>1631168037</__time__>
            <__topic__/>
            <cluster_id>cb36d98a701ef4742b50603866809****</cluster_id>
            <constraint_action>deny</constraint_action>
            <constraint_api_version>v1beta1</constraint_api_version>
            <constraint_group>constraints.gatekeeper.sh</constraint_group>
            <constraint_kind>ACKAllowedRepos</constraint_kind>
            <constraint_name>allowed-repos-80970511-c93d-4c40-b692-be18c077****
</constraint_name>
            <event_msg>Admission webhook "validation.gatekeeper.sh" denied request,
Resource Namespace: default, Constraint: allowed-repos-80970511-c93d-4c40-b692-be18c077 0382, Message: container &lt;nginx&gt; has an invalid image repo &lt;nginx:1.7.9&gt;, a llowed repos are ["registry.cn-shanghai.aliyuncs.com/acs/", "registry.cnhangzhou.aliyuncs.com/acs/"]</event_msg>
            <event_reason>GatekeeperFailedAdmission</event_reason>
            <event_type>violation</event_type>
            <level>info</level>
            <logger>ack_policy_admit_log_for_sls</logger>
            <msg>container &lt;nginx&gt; has an invalid image repo &lt;nginx:1.7.9&gt;,
allowed repos are ["registry.cn-shanghai.aliyuncs.com/acs/", "registry.cnhangzhou.aliyuncs.com/acs/"]</msg>
            <process>admission</process>
            <request_uid>9db8f008-c2e8-4723-a380-18ef358c2827</request_uid>
            <request_username>system:serviceaccount:kube-system:replicaset-
controller</request_username>
            <resource_api_version>v1</resource_api_version>
            <resource_group/>
            <resource_kind>Pod</resource_kind>
            <resource_name>nginx-deployment-basic2-84ccb74bfc-df22p</resource_name>
            <resource_namespace>default</resource_namespace>
            <time>2021-09-09T06:13:57Z</time>
            <ts>1631168037.444757</ts>
        </log>
        <log>
            <__source__>192.168.XX.XX</__source__>
        </log>
    </admit_log>
    <Violation>
        <totalViolations>
            <deny>
                <severity>high</severity>
                <violations>75</violations>
            </deny>
            <deny>
                <severity>medium</severity>
                <violations>0</violations>
            </deny>
            <warn>
                <severity>high</severity>
                <violations>0</violations>
            </warn>
            <warn>
                <severity>medium</severity>
                <violations>0</violations>
            </warn>
```

`/`

```xml
        </totalViolations>
        <violations>
            <deny>
                <policyName>policy-gatekeeper-ackallowedrepos</policyName>
                <policyDescription>Requires container images to begin with a repo string
from a specified list.</policyDescription>
                <severity>high</severity>
                <violations>11</violations>
            </deny>
            <deny>
                <policyName>policy-gatekeeper-ackpspcapabilities</policyName>
                <policyDescription>Controls Linux capabilities.</policyDescription>
                <severity>high</severity>
                <violations>81</violations>
            </deny>
        </violations>
    </Violation>
</DescribePolicyGovernanceInClusterResponse>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

#### 2.6.6 Query information about a policy

You can call the DescribePolicyDetails operation to query information about a policy.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
GET /policies/policy_name HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| PolicyNam e | Strin g | Path | true | ACKAllowedRepos | The name of the policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0B26C1D0-*** | The request ID. |

**Examples**

Sample requests

```
GET /policies/ACKAllowedRepos HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "name" : "ACKAllowedRepos",
  "category" : "k8s-general",
  "description" : "Requires container images to begin with a repo string from a specifi
ed list",
  "action" : "enforce",
  "severity" : "high",
  "template" : "",
  "no_config" : 0,
  "is_deleted" : 0
```

`XML` format

```xml
<DescribePolicyDetailsResponse>
    <name>ACKAllowedRepos</name>
    <category>k8s-general</category>
    <description>Requires container images to begin with a repo string from a specified
list</description>
    <action>enforce</action>
    <severity>high</severity>
    <template></template>
    <no_config>0</no_config>
    <is_deleted>0</is_deleted>
</DescribePolicyDetailsResponse>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

#### 2.6.7 DescribePolicies

You can call the DescribePolicies operation to query a list of policies.

**Request headers**

The DescribePolicies operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0B26C1D0-*** | The request ID. |

**Examples**

Sample requests

```
GET /policies HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "compliance" : [ "ACKNoEnvVarSecrets", "ACKPodsRequireSecurityContext",
"ACKRestrictNamespaces", "ACKRestrictRoleBindings" ],
  "infra" : [ "ACKBlockProcessNamespaceSharing", "ACKEmptyDirHasSizeLimit", "ACKLocalSt
orageRequireSafeToEvict", "ACKOSSStorageLocationConstraint" ],
  "k8s-general" : [ "ACKBlockAutoinjectServiceEnv", "ACKBlockAutomountToken", "ACKBlock
LoadBalancer", "ACKBlockNodePort", "ACKContainerLimits", "ACKExternalIPs", "ACKImageDigests", "ACKRequiredLabels", "ACKRequiredProbes", "ACKAllowedRepos" ],
  "psp" : [ "ACKPSPAllowPrivilegeEscalationContainer", "ACKPSPAllowedUsers", "ACKPSPApp
Armor", "ACKPSPCapabilities", "ACKPSPFSGroup", "ACKPSPFlexVolumes", "ACKPSPForbiddenSysctls", "ACKPSPHostFilesystem", "ACKPSPHostNamespace", "ACKPSPHostNetworkingPorts", "ACKPSPPrivilegedContainer", "ACKPSPProcMount", "ACKPSPReadOnlyRootFilesystem", "ACKPSPSELinuxV2", "ACKPSPSeccomp", "ACKPSPVolumeTypes"
```

`]` `XML` format

```xml
<DescribePoliciesResponse>
    <compliance>ACKNoEnvVarSecrets</compliance>
    <compliance>ACKPodsRequireSecurityContext</compliance>
    <compliance>ACKRestrictNamespaces</compliance>
    <compliance>ACKRestrictRoleBindings</compliance>
    <infra>ACKBlockProcessNamespaceSharing</infra>
    <infra>ACKEmptyDirHasSizeLimit</infra>
    <infra>ACKLocalStorageRequireSafeToEvict</infra>
    <infra>ACKOSSStorageLocationConstraint</infra>
    <k8s-general>ACKBlockAutoinjectServiceEnv</k8s-general>
    <k8s-general>ACKBlockAutomountToken</k8s-general>
    <k8s-general>ACKBlockLoadBalancer</k8s-general>
    <k8s-general>ACKBlockNodePort</k8s-general>
    <k8s-general>ACKContainerLimits</k8s-general>
    <k8s-general>ACKExternalIPs</k8s-general>
    <k8s-general>ACKImageDigests</k8s-general>
    <k8s-general>ACKRequiredLabels</k8s-general>
    <k8s-general>ACKRequiredProbes</k8s-general>
    <k8s-general>ACKAllowedRepos</k8s-general>
    <psp>ACKPSPAllowPrivilegeEscalationContainer</psp>
    <psp>ACKPSPAllowedUsers</psp>
    <psp>ACKPSPAppArmor</psp>
    <psp>ACKPSPCapabilities</psp>
    <psp>ACKPSPFSGroup</psp>
    <psp>ACKPSPFlexVolumes</psp>
    <psp>ACKPSPForbiddenSysctls</psp>
    <psp>ACKPSPHostFilesystem</psp>
    <psp>ACKPSPHostNamespace</psp>
    <psp>ACKPSPHostNetworkingPorts</psp>
    <psp>ACKPSPPrivilegedContainer</psp>
    <psp>ACKPSPProcMount</psp>
    <psp>ACKPSPReadOnlyRootFilesystem</psp>
    <psp>ACKPSPSELinuxV2</psp>
    <psp>ACKPSPSeccomp</psp>
    <psp>ACKPSPVolumeTypes</psp>
</DescribePoliciesResponse>
```

#### 2.6.8 Delete policy instances from an ACK cluster

**cluster**

You can call the DeletePolicyInstance operation to delete policy instances from a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation of common request parameters.

**Request syntax**

```
DELETE /clusters/cluster_id/policies/policy_name?instance_name=String HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| cluster id _ | strin g |   | true | c8155823d057948c69a** ** | The cluster ID. |
| policy nam _ e | strin g |   | true | ACKAllowedRepos | The name of the policy. |
| instance n _ ame | strin g |   | false | allowed-repos-mqdsf | The name of the policy instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

**Example**

Sample requests

```
DELETE /clusters/c8155823d057948c69a****/policies/ACKAllowedRepos? instance_name=allowed-repos-mqdsf HTTP/1.1
```

Sample success responses `JSON` format `{`

```json
  "instances" : [ "allowed-repos-kqxnc" ]
```

`XML` format

```xml
<instances>allowed-repos-kqxnc</instances>
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

## 3 Appendixes

### 3.1 STS overview

#### 3.1.1 What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 3.1.2 Obtain an STS token

You can call the AssumeRole operation to obtain a Security Token Service (STS) token. A Resource Access Management (RAM) user can use the STS token to assume a RAM role whose trusted entity is an Alibaba Cloud account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | Obtain an STS token | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456 789012****:role/ adminrole | The Alibaba Cloud Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Alibaba Cloud account. |

| RoleSessionNa me | String | Yes | alice | The custom name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the API caller. For example, you can specify a username. You can specify RoleSessionName to identify API callers that assume the same RAM role in ActionTrail logs. This allows you to track the users that perform the operations. The value must be 2 to 64 characters in length, and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
|---|---|---|---|---|
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | The policy that specifies the permissions of the returned STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. Details: If you specify this parameter, the permissions of the returned STS token are the permissions that are included in the value of this parameter and owned by the RAM role. If you do not specify this parameter, the returned STS token has all the permissions of the RAM role. The value of the parameter must be 1 to 1,024 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The request ID. |
| Credentials | N/A | None | The STS credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | The AccessKey ID. |
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |

| SecurityToken | String | ******** | The STS token. |
|---|---|---|---|
| Expiration | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | N/A | None | The temporary identity that you use to assume the RAM role. |
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

**Call an API operation to obtain the STS 3-tuple.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the 3-tuple.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
//CreateandinitializeaDefaultAcsClientinstance
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
            // Obtain the STS 3-tuple.
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

**Sample requests**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; importcom.aliyuncs.CommonResponse;
```

```java
import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the
AccessKey ID and AccessKey secret in the 3-tuple that you obtained in the preceding ste
```

`p.`

```java
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
        // Specify the resource set ID. This parameter is optional.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Specify the organization ID. This parameter is required.
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
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length, and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |

| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
|---|---|---|---|
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |
