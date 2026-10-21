---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Uni-manager Management Console Developer Guide 20251105"
product_version: "V3.14.0"
doc_version: "20251105"
pdf_pages: 321
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Uni-manager Management Console Developer Guide 20251105.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.14.0/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Apsara%20Uni-manager%20Management%20Console%20Developer%20Guide%2020251105.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Apsara Uni-manager Management Console Developer Guide 20251105

## Table of Contents

- 1 Preparations
  - 1.1 View the information about API operations
  - 1.2 Obtain AccessKey credentials
  - 1.3 Obtain the values of common request headers
- 2 Use SDKs
  - 2.1 Use POP to make API calls
    - 2.1.1 Obtain service endpoints
    - 2.1.2 Obtain an SDK
    - 2.1.3 Call examples for SDK for Java
      - 2.1.3.1 Getting started
      - 2.1.3.2 Use SDK
        - 2.1.3.2.1 Install an SDK for Java
        - 2.1.3.2.2 Configure authentication credentials
        - 2.1.3.2.3 Configure connection requests
        - 2.1.3.2.4 Initiate a request
        - 2.1.3.2.5 Handle errors
        - 2.1.3.2.6 Use CommonRequest to call API operations
    - 2.1.4 Call examples for SDK for Python
      - 2.1.4.1 Getting started
      - 2.1.4.2 Use SDK
        - 2.1.4.2.1 Install the SDK for Python
        - 2.1.4.2.2 Configure authentication credentials
        - 2.1.4.2.3 Set HTTPS requests
        - 2.1.4.2.4 Initiate a request
        - 2.1.4.2.5 Handle errors
        - 2.1.4.2.6 Use CommonRequest to call API operations
    - 2.1.5 Call examples for SDK for Go
      - 2.1.5.1 Getting started
      - 2.1.5.2 Use SDK
        - 2.1.5.2.1 Install Go SDK
        - 2.1.5.2.2 Configure authentication credentials
        - 2.1.5.2.3 Initiate a request
        - 2.1.5.2.4 Handle errors
        - 2.1.5.2.5 Use CommonRequest to call API operations
  - 2.2 Use ASAPI to call API operations
    - 2.2.1 ASAPI overview
    - 2.2.2 Obtain the endpoint of ASAPI
    - 2.2.3 Obtain Apsara Stack SDKs
    - 2.2.4 SDK for Java
    - 2.2.5 SDK for Python
    - 2.2.6 SDK for Node.js
- 3 HTTP requests
  - 3.1 Overview
  - 3.2 Request structure
  - 3.3 Request signatures
  - 3.4 Responses
- 4 API reference
  - 4.1 Common parameters
  - 4.2 Apsara Uni-manager Management Console authentication
  - 4.3 List of operations by function
    - 4.3.1 Enterprise
      - 4.3.1.1 Organizations
        - 4.3.1.1.1 UpdateOrganization
        - 4.3.1.1.2 UpdateSupportRegionsForOrg
        - 4.3.1.1.3 GetOrganization
        - 4.3.1.1.4 GetOrganizationList
        - 4.3.1.1.5 RemoveOrganization
        - 4.3.1.1.6 ListResourceGroupByOrgId
        - 4.3.1.1.7 CreateOrganization
        - 4.3.1.1.8 GetPrivateCloudAccountByOrganizationId
      - 4.3.1.2 Resource sets
        - 4.3.1.2.1 CreateResourceGroup
        - 4.3.1.2.2 UnbindAscmUserAndResourceGroup
        - 4.3.1.2.3 UpdateResourceGroup
        - 4.3.1.2.4 RemoveResourceGroup
        - 4.3.1.2.5 ListResourceGroup
        - 4.3.1.2.6 BindAscmUserAndResourceGroup
        - 4.3.1.2.7 ListAscmUsersInsideResourceGroup
      - 4.3.1.3 Roles
        - 4.3.1.3.1 SetDefaultRole
        - 4.3.1.3.2 ListRoles
        - 4.3.1.3.3 ListActiveRoles
      - 4.3.1.4 Users
        - 4.3.1.4.1 AddUser
        - 4.3.1.4.2 AddRoleToUser
        - 4.3.1.4.3 ResetPasswordByLoginName
        - 4.3.1.4.4 GetLoginPolicyByLoginName
        - 4.3.1.4.5 UpdatePassword
        - 4.3.1.4.6 RemoveUserByLoginName
        - 4.3.1.4.7 GetUserInfo
        - 4.3.1.4.8 ListUsers
        - 4.3.1.4.9 ActivateUser
        - 4.3.1.4.10 ListDeletedUsers
        - 4.3.1.4.11 ListResourceGroupByAscmUserId
        - 4.3.1.4.12 ModifyUserInformation
        - 4.3.1.4.13 RecoverUserByLoginName
        - 4.3.1.4.14 DeactivateUser
      - 4.3.1.5 User groups
        - 4.3.1.5.1 ListUserGroups
        - 4.3.1.5.2 CreateUserGroup
        - 4.3.1.5.3 ListUsersInUserGroup
        - 4.3.1.5.4 AddUsersToUserGroup
        - 4.3.1.5.5 AddRoleToUserGroup
        - 4.3.1.5.6 AddResourceSetToUserGroup
        - 4.3.1.5.7 RemoveUsersFromUserGroup
        - 4.3.1.5.8 RemoveRoleFromUserGroup
        - 4.3.1.5.9 RemoveResourceSetFromUserGroup
        - 4.3.1.5.10 DeleteUserGroup
      - 4.3.1.6 Logon policies
        - 4.3.1.6.1 AddLoginPolicy
        - 4.3.1.6.2 CheckLoginPolicy
        - 4.3.1.6.3 ListLoginPolicies
        - 4.3.1.6.4 ModifyLoginPolicy
        - 4.3.1.6.5 GetLoginPolicyById
    - 4.3.2 Operations
      - 4.3.2.1 CreateQuota
      - 4.3.2.2 DescribeGpdbModifiableInstanceType
      - 4.3.2.3 UpdateQuota
      - 4.3.2.4 DeleteQuota
      - 4.3.2.5 GetQuota
      - 4.3.2.6 MeteringQuery
      - 4.3.2.7 SelectCommonSpec
      - 4.3.2.8 AddCommonSpec
      - 4.3.2.9 UpdateCommonSpecStatus
    - 4.3.3 Cloud services
      - 4.3.3.1 DescribeModifiableInstanceType
      - 4.3.3.2 DescribeSeriesIdFamilies
      - 4.3.3.3 GroupCommonSpec
      - 4.3.3.4 DescribeInstanceTypeFamilies
      - 4.3.3.5 GetRegionsByProduct
      - 4.3.3.6 BindBucketPolicy
      - 4.3.3.7 UnBindBucketPolicy
    - 4.3.4 Configurations
      - 4.3.4.1 RemoveLoginPolicyById
      - 4.3.4.2 GetPasswordPolicy
      - 4.3.4.3 ResetPasswordPolicy
      - 4.3.4.4 SetPasswordPolicy
      - 4.3.4.5 ListRAMServiceRoles
      - 4.3.4.6 ListRAMPolicies
      - 4.3.4.7 ListRAMPoliciesForUser
      - 4.3.4.8 RemoveLoginPolicyByName
    - 4.3.5 Parameters related to the MeteringQuery operation
      - 4.3.5.1 ECS
      - 4.3.5.2 SLB
      - 4.3.5.3 OSS
      - 4.3.5.4 EIP
      - 4.3.5.5 VPC
      - 4.3.5.6 ApsaraDB RDS for MySQL
      - 4.3.5.7 Tablestore
      - 4.3.5.8 PolarDB-X
      - 4.3.5.9 What is KVStore for Redis?
      - 4.3.5.10 AnalyticDB for PostgreSQL
      - 4.3.5.11 ApsaraDB for MongoDB
      - 4.3.5.12 Message Queue for Apache RocketMQ
      - 4.3.5.13 ApsaraDB RDS for PostgreSQL
      - 4.3.5.14 ApsaraDB RDS for SQL Server
      - 4.3.5.15 Log Service
      - 4.3.5.16 EBS
      - 4.3.5.17 Snapshots
      - 4.3.5.18 Auto Scaling
      - 4.3.5.19 KMS
      - 4.3.5.20 API Gateway
- 5 Monitoring
  - 5.1 Common parameters
  - 5.2 Major metrics for Apsara Stack services
  - 5.3 API Reference
    - 5.3.1 Cloud Products
      - 5.3.1.1 DescribeProjectMeta
      - 5.3.1.2 DescribeMetricLast
      - 5.3.1.3 DescribeMetricList
      - 5.3.1.4 DescribeMetricMetaList
    - 5.3.2 Alert rules for time series metrics
      - 5.3.2.1 DescribeMetricRuleList
      - 5.3.2.2 PutResourceMetricRule
      - 5.3.2.3 DescribeMetricRuleCount
      - 5.3.2.4 DeleteMetricRules
      - 5.3.2.5 EnableMetricRules
      - 5.3.2.6 DisableMetricRules
      - 5.3.2.7 DescribeAlertingMetricRuleResources
      - 5.3.2.8 DeleteMetricRuleResources

rations

## 1 Preparations

### 1.1 View the information about API operations

You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs.

**Procedure**

1. Log on to the API Tool console.
2. In the left-side navigation pane, click **API fold**.
3. On the **API Directory** page, select the target service from the drop-down list, enter the API operation name in the search box, and then click the
search icon.
4. View and remember the service name, API operation name, and API version.

### 1.2 Obtain AccessKey credentials

AccessKey credentials are assigned by Resource Access Management (RAM) .

**Background information**

An AccessKey ID and an AccessKey secret are used to implement symmetric encryption and verify the identity of a request sender. The AccessKey ID is used to identify a user. The AccessKey secret is a string that is used to encrypt a signature.

**Obtain an AccessKey pair**

The Apsara Uni-manager Management Console provides two types of AccessKey pairs: those for personal accounts and those for organization accounts. We recommend that you use an AccessKey pair for personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services.

> **Note:** Only operations administrators and level-1 organization administrators can obtain AccessKey pairs for organization accounts.

**Obtain an AccessKey pair for personal accounts**

To use an AccessKey pair for personal accounts, you must configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region to which the instance that you want to access belongs. Example: cn-qingdao-****-****. |
| x-acs-organizationid | The ID of the organization to which the instance that you want to access belongs. For information about how to obtain the ID, see Obtain common header parameters. |
| x-acs-resourcegroupid | The ID of the resource set to which the instance that you want to access belongs. For information about how to obtain the ID, see Obtain common header parameters. |
| x-acs-instanceid | The ID of the instance that you want to access. For example, you can view the ID of an Elastic Compute Service (ECS) instance in the ECS instance list. |

1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
rations
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain an AccessKey pair for organizations**

> **Warning:** An AccessKey pair for personal accounts is managed and controlled by the permission system of the Apsara Uni-manager Management Console. An AccessKey pair for organization accounts provides more permissions than an AccessKey pair for personal accounts. If you need to obtain an AccessKey pair for organizations, make sure that your operation is allowed by your administrator. This ensures security.

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization navigation tree, click the name of the level-1 organization for which you want to obtain AccessKey pairs.
5. Click **Management AccessKey** on the right side of the page.
6. In the Management AccessKey dialog box, view the AccessKey pair of the organization.

### 1.3 Obtain the values of common request headers

In Apsara Stack, you must specify multiple common request headers to call API operations. Then, common response parameters are returned in the results.

**Common request parameters**

You must specify the values of the common request parameters in the code to call API operations in Apsara Stack. For example, you need to replace the `<Your resource group ID>` with the actual resource set ID in `request.putHeadParameter("x-acs-` `resourcegroupid", "<Your resource group ID>")` when you use the SDK for Java to call API operations.

| Name | Description |
|---|---|
| x-acs-regionid | The region ID of the instance resource on which you want to perform operations. For more information, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization to which the instance resource belongs. For more information, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set to which the instance resource belongs. For more information, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance to which the resource belongs. For more information, see Obtain an instance ID. |

> **Note:** When you call API operations in Apsara Stack, you must use `<x-acs-organizationid>` to add the organization ID to the request header. Otherwise, the call fails and an error message indicating that you do not have permissions to initiate calls is returned.
> When you call API operations in Apsara Stack, we recommend that you use `<x-acs-resourcegroupid>` to add the resource set ID to the request header. After you specify the organization ID and the resource set ID, you can narrow down the query scope when you query instance resources. If you do not use `<x-acs-resourcegroupid>` to specify the resource set ID, the default resource set of the organization to which the user belongs is obtained.

**Obtain a region ID**

You can view the region IDs of resources in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization that you want to view.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

rations You must call a specific API operation to obtain the organization ID. You can obtain the organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Others** > **API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. On the **API Directory** page, enter `GetOrgnizationList` in the **Search by operation name** field and click **Search**.
5. Click **Online Debug** in the Actions column. For more information about the `GetOrgnizationList` operation, see the GetOrgnizationList topic in
the Apsara Uni-manager Management Console Developer Guide.
6. Obtain the organization ID from the **id** parameter in the **returned results**.

**Obtain a resource set ID**

You can view the IDs of resource sets in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Resource Sets**.
4. On the **Resource Sets** page, view the **Resource Set/ID**.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, you can view instance IDs in the ECS console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Elastic Compute Service**.
3. In the left-side navigation pane, choose **Instances & Images > Instances**.
4. In the instance list that appears, view the instance IDs in the **Instance ID/Name** column.

**Common response parameters**

The following table describes the common response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Name | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

DKs

## 2 Use SDKs

### 2.1 Use POP to make API calls

#### 2.1.1 Obtain service endpoints

This topic describes how to obtain service endpoints.

**Background information**

To call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must specify the endpoint of your cloud service. You can obtain an endpoint from onsite Apsara Stack O&M engineers. You can also perform the following steps to obtain an endpoint.

**Procedure**

The following example procedure shows how to obtain the endpoint of ECS.
1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. In the **Base/Platforms** section, click **Apsara Infrastructure Management Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` . In the report list that appears, click the name of the report.
4. On the **Registration Vars of Services** page, click the
icon next to **Service**. Specify the Contains operator, enter `ECS` in the filter text filed, and then click Apply Filter.
5. Find the `ecs-yaochi` service, right-click the value in the **Service Registration** column, and then select **Show More** from the shortcut menu.
On the **Details** page, view the **internal.openapi.endpoint** value, which is the `endpoint` .

#### 2.1.2 Obtain an SDK

To call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK of your cloud service. This topic describes how to obtain an SDK of your cloud service. An SDK includes code and examples. You can create cloud applications by using an SDK for the programming language that you require. SDKs for Java, Python, and Go are perfectly supported. You can select the SDKs from Alibaba Cloud SDKs based on your business requirements.

> **Note:** We recommend that you use an SDK for Java, Python, or Go. If you use SDKs for other programming languages, the SDKs may be incompatible with your system.

We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack.

#### 2.1.3 Call examples for SDK for Java

##### 2.1.3.1 Getting started

This topic describes how to obtain and use an SDK for Java.

**Prerequisites**

An authorized Apsara Stack tenant account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain AccessKey credentials. The endpoint of the cloud service is obtained. For more information, see Obtain service endpoints. Java Development Kit (JDK) 1.8 or later is installed. SDKs for Java provided by Apsara Stack require JDK 1.8 or later.

**Install the SDK for Java**

To use Apache Maven for Java project management, include the JAR file in `pom.xml` . DKs To use an SDK of a service, you must install both the SDK core library and the SDK. We recommend that you use the latest SDK core library.

**Use the SDK for Java**

To use an Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in your code.
> Parameters:
> <yourRegionID>: Replace it with the region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <Product>: Replace it with the name of the service.
> <Endpoint>: Replace it with the endpoint of the service.
> <readTimeout>: Replace it with a read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Replace it with a connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Replace it with the maximum number of requests that are supported by each host.
> <maxRequests>: Replace it with the maximum number of requests.
> <http://192.168.XX.XX:33XX>: Replace it with the IP address and port of the proxy.

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
            "<yourRegionID>",          // Replace it with the region ID.
            "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
        // Specify the endpoint of the current service.
        profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
        // Configure the request parameters.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// Ignore the certificate.
        clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the read timeout period. Unit: milliseconds.
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Specify the connection timeout period. Unit: milliseconds.
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify the maximum number of requests per host.
        clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum number of requests.
        clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Specify the request protocol. Default value: HTTP.
        /* Optional. Specify the IP address and port of the proxy.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```java
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        DescribeInstancesRequest request = new DescribeInstancesRequest();
        // Set service-related parameters.
        request.setPageSize(10);
        request.setPageNumber(1);
        // Specify the organization ID and resource set ID to query specified resources.
        request.putHeaderParameter("x-acs-organizationid", "1");
        request.putHeaderParameter("x-acs-resourcegroupid", "11");
        // Send the request and handle the response or exception.
        DescribeInstancesResponse response;
        try {
            response = client.getAcsResponse(request);
            for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
                System.out.println(instance.getPublicIpAddress());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
```

##### 2.1.3.2 Use SDK

###### 2.1.3.2.1 Install an SDK for Java

DKs This topic describes how to install and use the SDK for Java of your cloud service. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK package. For more information, visit Alibaba Cloud SDKs. To use the development tool kit for a cloud service, you must install the core library of Apsara Stack SDK for Java and the SDK for Java of your cloud service. We recommend that you use the latest version of the core library of Apsara Stack SDK for Java. For example, to use ECS SDK for Java, you must install the core library of Apsara Stack SDK for Java and ECS SDK for Java, and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDKs.

```xml
<!-- https://mvnrepository.com/artifact/com.aliyun/aliyun-java-sdk-core --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.30</version>
</dependency> <!-- ecs java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-ecs</artifactId>
    <version>4.23.2</version>
</dependency>
```

###### 2.1.3.2.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. Apsara Stack SDK for Java supports authentication based on an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain AccessKey credentials. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

> **Note:** Do not disclose code containing your AccessKey pair (for example, do not commit AccessKey pair-related code to public GitHub projects). Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace it with the region ID.
    "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
```

> **Note:** Replace the parameters in the preceding sample code with your actual information. Delete the angle brackets (<>) in your code.

###### 2.1.3.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

> **Note:** You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER.
> <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER.
> <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

DKs

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

###### 2.1.3.2.4 Initiate a request

This topic describes how to use the SDK for Java of a cloud service to initiate a request.

**Procedure**

1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request , where **${apiName}** indicates the name of an API operation, such as DescribeInstances. When multiple service SDKs are used, different requests may have the same name. Differentiate the requests by using package names.

```
DescribeInstancesRequest request = new DescribeInstancesRequest(); // Specify service-related parameters. request.setPageSize(10); request.setPageNumber(1); // Specify the organization ID and resource set ID to query specified resources. request.putHeaderParameter("x-acs-organizationid", "1"); request.putHeaderParameter("x-acs-resourcegroupid", "");
```

3. Initiate the request and handle the response.

| DescribeInstancesResponse response; try { response = client.getAcsResponse(request); for (DescribeInstancesResponse.Instance instance:response.getInstances()) { System.out.println(instance.getPublicIpAddress()); } } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { e.printStackTrace(); } |   |   |   |   |
|---|---|---|---|---|
| In normal cases, all returned fields are deserialized into the response. You can directly use |   |   | response.getXXX() | to obtain the response fields. |
| Boolean status = response.getStatus(); |   |   |   |   |
| If an exception occurs or you need the original HTTP response, use | doAction() | to obtain the original response. |   |   |
| HttpResponse response = client.doAction(request); |   |   |   |   |

###### 2.1.3.2.5 Handle errors

If the server or SDK encounters an error when you use the SDK for Java, the SDK returns an error response. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by the SDK for Java. You only need to handle server errors based on error messages generated on the server side. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code: DKs

```java
try {
    AcsResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // You can add your error handling logic here.
    // For example, display the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If you are unable to fix the error, submit a ticket and provide RequestId to Alibaba Cloud technical support.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your error handling logic here.
    // For example, display the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

###### 2.1.3.2.6 Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight: You need to only download the core package. You do not need to download and install SDKs of services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters from the API document of a service. product: the service name of the operation. domain: the endpoint of the service. version: the version of the API. The version is in the YYYY-MM-DD format. You can obtain the API version from the common parameters chapter in the API document. Operation information: the name of the API operation that you want to call. For Remote Procedure Call (RPC) APIs, which are used by services such as Elastic Compute Service (ECS) and Relational Database Service RDS):

| request.setSysAction("<Action>") |   | format. |
|---|---|---|
| tion in | request.setSysAction("RunInstances") |   |

You must obtain the value of the **Action** parameter and specify an API operation in `request.setSysAction("<Action>")` format. For example, to call the RunInstances operation of ECS, you must specify the operation in `request.setSysAction("RunInstances")` . For Representational State Transfer (RESTful) APIs, which are used by services such as Container Service (CS): You must obtain the value of the **PathPattern** parameter and specify a RESTful path in `request.setSysUriPattern("<PathPattern>")` format. For example, if the **PathPattern** value in an API operation that is used to query all cluster instances in CS is `/api/v1/clusters` , you must specify the RESTful path in the `request.setSysUriPattern("/api/v1/clusters")` format.

**Example: Call an RPC API operation**

The following code shows an example on how to use CommonRequest to call the DescribeInstanceStatus operation of ECS.

> **Note:** Replace `<yourRegionID>` , `<yourAccessKeyID>` , `<yourAccessKeySecret>` , `<yourSecurityToken>` , `<yourResourceGroupID>` ,
> `<yourOrganizationID>` , `<yourInstanceID>` , and `<http://192.168.XX.XX:33XX>` with the actual values. Delete the angle brackets (<>) in your code.

DKs

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with your region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTP);// Determine whether to configure an HTTP proxy based on your business requirements.
        // Configure the HTTP proxy in the following method:
        // clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Replace the parameter with the actual proxy IP address and port.
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        CommonRequest request = new CommonRequest();
        // Replace the parameter with the actual service endpoint.
        request.setSysMethod(MethodType.POST);
        request.setSysDomain("ecs.aliyuncs.com");
        request.setSysProduct("Ecs");
        request.setSysLocationProduct("ecs");
        request.setSysVersion("2014-05-26");
        request.setSysAction("DescribeInstanceStatus");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Replace the parameter with the actual resource
set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Replace the parameter with the actual
organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required. Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional. Replace the parameter with the actual region ID.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional. Replace the parameter with the actual instance ID.
This parameter is required when you want to delete, modify, or query an instance.
        // When you use an STS AccessKey 3-tuple to call an API operation, you must add the SecurityToken field in the request parameters.
        // Format:
        //request.putQueryParameter("SecurityToken", "<yourSecurityToken>"); Replace the parameter with the actual security token.
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

DKs

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with your region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTP);// Determine whether to configure an HTTP proxy based on your business requirements.
        // Configure the HTTP proxy in the following method:
        // clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Replace the parameter with the actual proxy IP address and port.
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // Specify the endpoint of the service.
        request.setSysMethod(MethodType.POST);
        request.setSysDomain("ecs.aliyuncs.com");
        request.setSysProduct("Ecs");
        request.setSysLocationProduct("ecs");
        request.setSysVersion("2014-05-26");
        request.setSysAction("DescribeInstanceStatus");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Replace the parameter with the actual resource
set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Replace the parameter with the actual
organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required. Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Required. Replace the parameter with the actual region ID.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional. Replace the parameter with the actual instance ID.
This parameter is required when you want to delete, modify, or query an instance.
        // When you use an STS AccessKey 3-tuple to call an API operation, you must add the SecurityToken field in the request parameters.
        // Format:
        //request.putQueryParameter("SecurityToken", "<yourSecurityToken>"); Replace the parameter with the actual token.
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

**Example: Call a RESTful API operation**

You must pass parameters in two methods depending on the request method and ContentType value. If the request method is `GET` or `DELETE` , or the ContentType value is `application/x-www-form-urlencoded` , use the following method to pass parameters: Place the request parameters in the Query parameter, for example, request.putQueryParameter("page_number", "1"); . If the request method is `POST` or `PUT` and the ContentType value is `application/json` , use the following method to pass parameters: Place the request parameters in the body, for example:

```
String requestBody = "{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \"<yourSecurityToken>\"}"; request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
```

The following code shows an example on how to use CommonRequest to call the DescribeClusterV1 operation of CS.

> **Note:** Replace `<yourRegionID>` , `<yourAccessKeyID>` , `<yourAccessKeySecret>` , `<yourResourceGroupID>` , `<yourOrganizationID>` ,
> `<yourInstanceID>` , `<http://192.168.XX.XX:33XX>` , and `<yourSecurityToken>` with the actual values. Delete the angle brackets (<>) in your code.

DKs

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    //DemoAPI: DescribeClusterV1
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with your region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTP);// Determine whether to configure an HTTP proxy based on your business requirements.
        // Configure the HTTP proxy in the following method:
        // clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Replace the parameter with the actual proxy IP address and port.
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the parameters.
        CommonRequest request = new CommonRequest();
        // The request method of the operation. For details, see API documents.
        request.setSysMethod(MethodType.GET);
        request.setSysDomain("cs.aliyuncs.com");
        request.setSysProduct("CS");
        request.setSysLocationProduct("cs");
        request.setSysVersion("2015-12-15");
        request.setSysUriPattern("/api/v1/clusters");
        request.putHeadParameter("Content-Type", "application/json");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Replace the parameter with the actual resource
set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Replace the parameter with the actual
organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required. Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional. Replace the parameter with the actual region ID. If you use
Apsara Stack Enterprise V3.15.0 or earlier versions, this parameter is required.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional. Replace the parameter with the actual instance ID.
This parameter is required when you want to delete, modify, or query an instance.
        // Business parameters. If the request method is GET or DELETE, or the ContentType value is application/x-www-form-urlencoded, use the
following method to pass parameters:
        request.putQueryParameter("page_number", "1");
        request.putQueryParameter("page_size", "5");
        // When you use an STS AccessKey 3-tuple to call an API operation, you must add the SecurityToken field in the request parameters.
        // Format:
        // String requestBody = "{\"SecurityToken\": \"<yourSecurityToken>\"}"; Replace the parameter with the actual token.
        If the request method is POST or PUT and the ContentType value is application/json, use the following method to pass parameters:
        //String requestBody = "{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \"<your-SecurityToken>\"}";
        //request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
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

#### 2.1.4 Call examples for SDK for Python

##### 2.1.4.1 Getting started

This topic describes how to obtain and use an SDK for Python.

**Prerequisites**

An authorized Apsara Stack tenant account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain AccessKey credentials. The endpoint of the cloud service is obtained. For more information, see Obtain service endpoints.
1. Install the SDK core library.
If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK: DKs

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install the SDK of the cloud service.
The following sample code shows how to install ECS SDK for Python: If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-ecs
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-ecs
```

**Use the SDK for Python**

For example, to use ECS SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must obtain a region ID, AccessKey ID, and AccessKey secret.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in your code.
> Parameters:
> <yourRegionID>: Replace it with the region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <ecs.aliyuns.com>: Replace it with the endpoint of the actual service.

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
region_id = '<yourRegionID>' # Specify the region ID. access_key = '<yourAccessKeyID>' # Specify your AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Specify your AccessKey secret.
# product config
product_name = 'ECS' # Specify the name of the required service. endpoint = '<ecs.aliyuns.com>' # The endpoint of the required service. Replace ecs.aliyuns.com with the endpoint of the actual service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print response # The print statement in Python 2.x. If you use Python 3.x, use print(response).
```

##### 2.1.4.2 Use SDK

###### 2.1.4.2.1 Install the SDK for Python

This topic describes how to install and use the SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK for Python of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python. For example, if you want to use ECS SDK for Python, you must install the SDK core library for Python and ECS SDK for Python.

If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

The following examples describe how to install ECS SDK for Python: If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-ecs
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-ecs
```

###### 2.1.4.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for authentication. The SDKs for Python support AccessKey pair-based authentication. For more information about how to obtain an AccessKey pair, see Obtain AccessKey credentials. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client. DKs

> **Important:** Do not disclose any code containing your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
clt = AcsClient(access_key, access_secret, region_id)
```

###### 2.1.4.2.3 Set HTTPS requests

The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use.

> **Note:** The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set.

**Add OpenSSL dependency**

HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python. Run the `python -c "import ssl"` command to check if the Python environment supports OpenSSL. If the `ImportError: No module named ssl` error message does not appear, OpenSSL is supported in Python. If Python does not support OpenSSL, run the following command to install OpenSSL:

```
pip install pyopenssl
```

**Set HTTP/HTTPS for a request**

See the following code example for reference to set the HTTPS call for an API:

```bash
request = CreateInstanceRequest.CreateInstanceRequest() request.set_protocol_type("https")
# Value: "https" or "http"
```

**Set global default protocol for all requests**

See the following code example for reference to set the global default protocol for all requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

###### 2.1.4.2.4 Initiate a request

This topic describes how to use the SDK for Python of a cloud service to initiate a request.

**Procedure**

1. Import the SDK for Python of the cloud service.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
```

2. Create an AcsClient instance.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = AcsClient(access_key, access_secret, region_id)
```

3. Create a request.

```
request = DescribeInstancesRequest() request.set_accept_format('json')
```

4. Initiate the request and process the response.

```
response = clt.do_action_with_exception(request) print response
```

###### 2.1.4.2.5 Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

To handle the errors returned by the Python SDK, see the following code example for reference: DKs

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

###### 2.1.4.2.6 Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight design: You need to only download the core package. You do not need to download and install SDKs of services. Ease of use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration: CommonRequest enables fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters from the API document of a service. product: the name of the service whose API operation you want to call. domain: the endpoint of the service. version: the version of the API in the YYYY-MM-DD format. You can obtain the API version from the common parameters in the API documents. action_name: the name of the API operation that you want to call. For Remote Procedure Call (RPC) APIs, which are used by services such as Elastic Compute Service (ECS) and Relational Database Service (RDS): You must obtain the value of the **Action** parameter and use `request.set_action_name('Action')` to specify the API operation. For example, to use CommonRequest to call the RunInstances operation of ECS, specify the operation in

```
 request.set_action_name('RunInstances') .
```

For Representational State Transfer (RESTful) APIs, which are used by services such as Container Service (CS): You must obtain the value of the **PathPattern** parameter and use `request.set_uri_pattern('Pattern')` to specify the RESTful path. For example, if the **PathPattern** value in an API operation that is used to query all cluster instances in CS is `/api/v1/clusters` , you must specify the RESTful path in the `request.set_uri_pattern ('/api/v1/clusters')` format.

**Example: Call an RPC API operation**

The following code provides an example on how to use CommonRequest to call the DescribeInstanceStatus operation of ECS.

> **Note:** Replace `<yourRegionID>` , `<yourAccessKeyID>` , `<yourAccessKeySecret>` , `<yourSecurityToken>` , `<yourResourceGroupID>` ,
> `<yourOrganizationID>` , `<yourInstanceID>` , and `<ecs.aliyuncs.com>` with the actual values. Delete the angle brackets (<>) in your code.

DKs

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Ecs') request.set_action_name('DescribeInstanceStatus') request.set_version('2014-05-26') request.set_domain('<ecs.aliyuncs.com>') # Replace <ecs.aliyuncs.com> with the endpoint of the actual service.
# or:
# request = = CommonRequest(product='Ecs', action_name='DescribeInstanceStatus',version='2014-05-26',domain='ecs.aliyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# You can specify HTTPS as the protocol in the following manner:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
# If you use the access credentials assigned by STS to call an API operation, you must specify the SecurityToken parameter in the request.
# Specify your security token in the following format:
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
# Specify your security token.
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

**Example: Call a RESTful API operation**

You must pass parameters by using one of the following two methods, depending on the request method and ContentType value. If the request method is `GET` or `DELETE` , or the ContentType value is `application/x-www-form-urlencoded` , use the following method to pass parameters: Place the request parameters in the Query parameter, for example, `request.add_query_param("page_number", "1")` . If the request method is `POST` or `PUT` and the ContentType value is `application/json` , use the following method to pass parameters: Place the request parameters in the body, for example:

```
body = '{"page_number":"1",page_size"5":"SecurityToken","":"<yourSecurityToken>"}' request.set_content(body.encode('utf-8'))
```

The following code provides an example on how to use CommonRequest to call the DescribeClusterV1 operation of CS.

> **Note:** Replace `<yourRegionID>` , `<yourAccessKeyID>` , `<yourAccessKeySecret>` , `<yourSecurityToken>` , `<yourResourceGroupID>` ,
> `<yourOrganizationID>` , `<yourInstanceID>` , and `<cs.aliyuncs.com>` with the actual values. Delete the angle brackets (<>) in your code.

DKs

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
######
# API:CS-DescribeClusterV1
######
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CS') request.set_version('2015-12-15') request.set_uri_pattern('/api/v1/clusters') # Pattern request.set_domain('<cs.aliyuncs.com>') # Replace <cs.aliyuncs.com> with the endpoint of the actual service.
# or:
# request = CommonRequest(product='CS', version='2015-12-15', uri_pattern='/api/v1/clusters', domain='cs.aliyuns.com')
######
# Specify the request protocol. Valid values: http and https. Default value: http.
# You can specify HTTPS as the protocol in the following manner:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('GET') request.add_header('Content-Type', 'application/json')
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack Enterprise V3.15.0 or earlier.
request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
// Pass parameters. If the request method is GET or DELETE, or the ContentType value is application/x-www-form-urlencoded, use the following m ethod to pass parameters: request.add_query_param("page_number", "1") request.add_query_param("page_size", "5")
######
# If you use the access credentials assigned by STS to call an API operation, you must specify the SecurityToken parameter in the request.
# Specify your security token in the following format:
# body = '''{\"SecurityToken\", \"<yourSecurityToken>\"}'''
# Specify your security token.
######
######
If the request method is POST or PUT and the ContentType value is application/json, use the following method to pass parameters:
# body = '{"page_number":"1",page_size"5":"SecurityToken","":"<your-SecurityToken>"}'
# request.set_content(body.encode('utf-8'))
######
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

#### 2.1.5 Call examples for SDK for Go

##### 2.1.5.1 Getting started

This topic describes how to obtain and use an SDK for Go.

**Prerequisites**

An authorized Apsara Stack tenant account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain AccessKey credentials. The endpoint of the cloud service is obtained. For more information, see Obtain service endpoints.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use the SDK for Go**

To use the SDK for Go, perform the following steps:
1. Initialize a client instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in your code.
> Parameters:
> <yourRegionID>: Replace it with the region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <Endpoint>: Replace it with the actual endpoint.

DKs

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

`)`

```
func main() {
    // Create an ecsClient instance.
    ecsClient, err := ecs.NewClientWithAccessKey(
        "<yourRegionID>",             // Replace it with the region ID.
        "<yourAccessKeyID>",         // Replace it with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace it with your AccessKey secret.
    if err != nil {
        // Handle exceptions.
        panic(err)
    // Create an API request and configure the required parameters.
    request := ecs.CreateDescribeInstancesRequest()
    // Specify the endpoint of the service.
    request.Domain = "<Endpoint>"
    // Set request.PageSize to 10.
    request.PageSize = requests.NewInteger(10)
    // Initiate the request and handle exceptions.
    response, err := ecsClient.DescribeInstances(request)
    if err != nil {
        // Handle exceptions.
        panic(err)
    fmt.Println(response)
```

4. (Optional) Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

##### 2.1.5.2 Use SDK

###### 2.1.5.2.1 Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
2. Extract the package to the directory where the GO_PATH file of the current user resides.

###### 2.1.5.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDKs for Go support AccessKey pair-based authentication. For more information, see Obtain AccessKey credentials. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

> **Important:** Do not disclose any code containing your AccessKey pair. For example, do not commit AccessKey-related code to public GitHub projects. Otherwise, your account may be compromised.

The following code provides an example on how to initialize an ecsClient instance.

```
// Initialize the ecsClient instance. ecsClient, err := ecs.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace it with the region ID.
        "<yourAccessKeyID>",             // Replace it with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace it with your AccessKey secret.
```

> **Note:** Replace the parameters in the preceding sample code with your actual information. Delete the angle brackets (<>) in your code.

###### 2.1.5.2.3 Initiate a request

This topic uses Elastic Compute Service (ECS) SDK for Go as an example to show how to initiate a request by using the SDK for Go of a specific cloud service.
1. Import ECS SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. Create an ECS client. The client includes all API operations of ECS.

| Note In the following code, replace the parameters with actual values. Delete the angle brackets <> in your code. |   |   |
|---|---|---|
| ecsClient,err := <ecs>.NewClientWithAccessKey( // Replace ecs with the name of the actual service. "<yourRegionID>", // Replace it with the region ID. "<yourAccessKeyID>", // Replace it with your AccessKey ID. "<yourAccessKeySecret>") // Replace it with your AccessKey secret. ecsClient.Domain = "ecs.aliyuns.com" // Specify the endpoint of the service. |   |   |
| Use | xxx.CreateXXXRequest | to create a request. |

DKs The naming convention for this method is ${service}.Create${apiName}Request , where:
**${service}** specifies the service name in lowercase. In this example, ecs is used.
**${apiName}** specifies the API operation, such as DescribeInstances.

```
request := ecs.CreateDescribeInstancesRequest()
```

4. Initiate the request.

```
response, err := ecsClient.DescribeInstances(request)
```

###### 2.1.5.2.4 Handle errors

When you use Apsara Stack SDK for Go, a `ClientError` or a `ServerError` is returned if an error occurs on the SDK side or on the server side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors.

**Error handling**

You can use the following code to handle errors:

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
    // Obtain the error information.
   err.Error()
```

**ClientError**

When you send a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a `ClientError` .

| The following sample code shows how to determine and obtain the error message in a | ClientError | returned by ECS SDK for Go: |
|---|---|---|
| Important When you use a specific error struct, you must add the error package github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors by using the following code: package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the name of the actual service. "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // The error package that you want to add. "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |   |   |

```
response, err := ecsClient.DescribeInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

**ServerError**

When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following sample code shows how to determine and obtain the error message in a ServerError and Response returned by ECS SDK for Go:

> **Important:** When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the name of the actual service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := ecsClient.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

DKs

###### 2.1.5.2.5 Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Call an RPC API operation**

The following code shows an example on how to use CommonRequest to call the DescribeInstanceStatus operation of ECS.

> **Note:** Replace `<yourRegionID>` , `<yourAccessKeyID>` , `<yourAccessKeySecret>` , `<yourSecurityToken>` , `<yourResourceGroupID>` ,
> `<yourOrganizationID>` , `<yourInstanceID>` , and `<ecs.aliyuncs.com>` with the actual values. Delete the angle brackets (<>) in your code.

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
        "<yourRegionID>",        // Replace the variable parameter with your region ID.
        "<yourAccessKeyID>",     // Replace the variable parameter with your AccessKey ID.
        "<yourAccessKeySecret>") // Replace the variable parameter with your AccessKey secret.
    if err != nil {
        panic(err)
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ecs.aliyuncs.com>" // Replace the variable parameter with the endpoint of your service.
    request.Product = "Ecs"
    request.Version = "2014-05-26"
    // This is an RPC API operation. Therefore, the ApiName(Action) parameter must be configured.
    request.ApiName = "DescribeInstanceStatus"
    // Specify service-related parameters.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*`

```
     When you use STS AccessKey credentials to call an RPC API operation, you must add the SecurityToken field to the request parameters.
     Request example:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Replace the variable parameter with your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. Specify the source of the call.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify your region ID. If you use Apsara Stack Enterprise V3.15.0 or ea
rlier, you must configure this parameter.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Specify the resource set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Specify the organization ID.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Specify the instance ID. If you want to modify, delete, or query
an instance, you must configure this parameter.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

**Call a RESTful API operation**

You must use one of the following methods to pass parameters based on the request method and the value of ContentType.

| application/x-www-form-urlencoded |   | , use th |
|---|---|---|
| request.QueryParams["page_number"] = "1" |   |   |
| application/json | , use the following method |   |

Place the request parameters in the Query parameter, such as `request.QueryParams["page_number"] = "1"` . Place the request parameters in the body. For example:

```
body := "{\"page_number\":\"1\",page_size:\"5\"}" request.SetContent([]byte(body)) request.SetContentType("application/json")
```

The following code provides an example on how to use CommonRequest to call the DescribeClusterV1 operation of CS.

> **Note:** Replace `<yourRegionID>` , `<yourAccessKeyID>` , `<yourAccessKeySecret>` , `<yourResourceGroupID>` , `<yourOrganizationID>` ,
> `<yourInstanceID>` , `<cs.aliyuncs.com>` , and `<yourSecurityToken>` with the actual values. Delete the angle brackets (<>) in your code.

DKs

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
        "<yourRegionID>",         // Replace the variable parameter with the actual region ID.
        "<yourAccessKeyID>",      // Replace the variable parameter with your AccessKey ID.
        "<yourAccessKeySecret>")  // Replace the variable parameter with your AccessKey secret.
    if err != nil {
        panic(err)
    request := requests.NewCommonRequest()
    request.Method = "GET"
    request.Domain = "cs.aliyuncs.com" // The endpoint of the service. Replace the sample value with the actual service endpoint.
    request.Product = "CS"
    request.Version = "2015-12-15"
    // This is a RESTful API. You must specify the PathPattern field.
    request.PathPattern = "/api/v1/clusters"
    // When you use an STS AccessKey pair to call the ROA operation, you must specify the x-acs-security-token header.
    // request.Headers["x-acs-security-token"] = "<yourSecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. This parameter is required for the Enterprise Edition V3.15.0 and earlier versions.
    request.Headers["x-acs-regionid"] = "<yourRegionID>"
    // Optional. Replace the variable parameter with your resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>"
    // Required. Replace the variable parameter with your organization ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"
    // Optional. Specify the instance ID. If you want to modify, delete, or query an instance, this parameter is required.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>"
    // Business parameters. If the request method is GET or DELETE, or ContentType is application/x-www-form-urlencoded, use the following met
hod to pass parameters:
    // request.QueryParams["page_number"] =  "1"
    // request.QueryParams["page_size"] = "5"
    If the request method is POST or PUT and ContentType is application/json, use the following method to pass parameters:
    // body := "{\"page_number\":\"1\",page_size:\"5\"}"
    // request.SetContent([]byte(body))
    // request.SetContentType("application/json")
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

### 2.2 Use ASAPI to call API operations

#### 2.2.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). DKs The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide.

> **Note:** If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 2.2.2 Obtain the endpoint of ASAPI

You can obtain the endpoint of ASAPI by replacing the variables. The actual values of the variables can be obtained in the Apsara Unimanager Operations Console. The endpoint can be a new one or a historical one. You can use one of them based on actual situations. We recommend that you use the new endpoint. If New endpoint Only the HTTPS protocol is supported. The new endpoint is suffixed with `internet-domain` and in the following format:

```
 https://public.asapi.${global:region}.${global:internet-domain}/asapi/v3
```

> **Note:** ${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained.

DKs Verify that the new endpoint is available Enter the following code. If you cannot access the endpoint, the new endpoint is unavailable. You can use the historical endpoint.

```bash
 curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k
```

> **Note:** ${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained.

Example of an available endpoint: Example of an unavailable endpoint: Historical endpoint

| Only the HTTP protocol is supported. The historical endpoint is suffixed with | intranet-domain |
|---|---|
| http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3 |   |
| Note ${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained. |   |

To obtain the actual values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranetdomain}, perform the following operations.
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

2. Enter your username and password.

> **Note:** Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator.

When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
3. Click **Log On** to go to the **ASO** console.
4. In the left-
side navigation pane, choose **Product Management > Products > Apsara Infrastructure Management Framework** to go to the Apsara Infrastru
5. In the top navigation bar, choose **Operations > Cluster Operations**.
6. On the **Clusters Operations** page, enter **ascm-A** in the Cluster search box to find the cluster. Click the cluster name.
DKs
7. On the **Cluster Dashboard** page, click **Operations Menu > Configuration Files**.
8. In the **File List** window on the left side of the **Cluster Configuration** page, click **kv.conf**, click the file content in the right window, and then press Ctr
domain, and intranet-domain. Replace ${global:region} with the obtained region value, ${global:internet-domain} with the obtained internetdomain value, and ${global:intranet-domain} with the obtained intranet-domain value.

> **Note:** ${global:} is not included in the endpoint of ASAPI that you can use.

#### 2.2.3 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. You can go to Apsara Stack documentation and download the Apsara Stack SDKs in the **Other Resources** section at the lower part of the page. DKs

#### 2.2.4 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java to call API operations.

**Prerequisites**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. You can obtain and view your AccessKey pair in the Apsara Uni-manager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of the ASAPI is obtained. For more information, see Generate an endpoint for ASAPI. Apsara Stack SDK for Java 1.8 or later is installed.

**Background information**

The help center of Apsara Stack provides Maven dependencies and JAR files for Apsara Stack SDK for Java. You can write code to use Apsara Stack SDK for Java to call API operations. In this example, the Windows 10 64-bit OS and IntelliJ IDEA are used.

**Procedure**

1. Use one of the following methods to configure Maven in IntelliJ IDEA. Maven is a tool used for project management.
Use Maven that is integrated in IntelliJ IDEA. Download Maven based on the OS that you are using from the official website and configure Maven. For more information, see Download Maven.
2. Obtain the Maven dependencies for Apsara Stack SDK for Java from the official website.
3. Use one of the following methods to create a Maven project:
Method 1: Create a Maven project in IntelliJ IDEA. Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select **Add Framework Support...**. b. Select **Maven** and click **OK**.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara Stack SDK for Java to the libs folder, as shown in the
following figure. DKs
5. Add the dependencies of Apsara Stack SDK for Java to the pom.xml file in the project directory.

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>asapi</artifactId>
        <version>1.0.6.4-RELEASE</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/asapi-1.0.6.4-RELEASE.jar</systemPath>
    </dependency>
  <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>alicrypto-java-aliyun</artifactId>
    <version>1.0.4</version>
    <systemPath>${project.basedir}/libs/alicrypto-java-aliyun-1.0.4.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>gmsse</artifactId>
    <version>1.1.0</version>
    <systemPath>${project.basedir}/libs/gmsse-1.1.0.jar</systemPath>
  </dependency>
    <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.7</version>
    <systemPath>${project.basedir}/libs/httpclient-4.5.7.jar</systemPath>
  </dependency>
</dependencies>
```

> **Note:** Replace `1.0.6.4-RELEASE` with the actual version of Apsara Stack SDK for Java.

6. On the right side of IntelliJ IDEA, view information in the Maven section.
If the information in the following figure appears, the dependencies are added.

**Use Apsara Stack SDK for Java**

You can use the GET or POST method to call API operations provided by ASAPI. The following sample code shows how to call API operations: DKs

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only for identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your environment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Version parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // When you use the STS AccessKey ID to call RPC API operations, you must add the SecurityToken parameter to the header. // parameters.put("SecurityToken", "<your-securitytoken>"); // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-security-token parameter to the header. // headers.put("x-acs-security-token", "<your-securitytoken>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operation-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid values of the SignatureMethod parameter: HMAC-SHA1 a nd HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

**Configure proxies**

If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. |
| x-acs-instanceid | The ID of the instance to which you make API calls. |

#### 2.2.5 SDK for Python

This topic describes how to obtain and use Apsara Stack SDK for Python to call API operations. An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of ASAPI is obtained. For more information, see Generate an endpoint for ASAPI.

**Install Apsara Stack SDK for Python**

1. Download the required version of Apsara Stack SDK for Python. For more information, see Obtain Apsara Stack SDKs.
2. Upload the compressed file of Apsara Stack SDK for Python to the host from which you want to send API requests and extract the file. Then, run the
following code in the directory of the extracted files to install Apsara Stack SDK for Python:

```bash
# Install Apsara Stack SDK for Python 2.x.
pip install aliyun-python2-sdk-asapi-2.4.7.tar.gz
# Install Apsara Stack SDK for Python 3.x.
pip3 install aliyun-python3-sdk-asapi-2.4.7.tar.gz
```

DKs

> **Note:** Replace `2.4.7` with the actual version of Apsara Stack SDK for Python.

**Sample requests**

You can use the GET or POST method to call API operations provided by ASAPI.

```python
# 1. Import dependencies.
   from aliyunsdkasapi.ASClient import ASClient
   from aliyunsdkasapi.AsapiRequest import AsapiRequest
   if __name__ == '__main__':
    # 2. Create a request. The Product parameter specifies the name of the service. The Version parameter specifies the version of the API ope
ration. The Action parameter specifies the operation that you want to perform. The asapi-endpoint parameter specifies the endpoint of ASAPI.
    req = AsapiRequest("<Product>", "<Version>", "<Action>", "<asapi-endpoint>")
    # 3. Configure operation-specific parameters.
    req.add_body_params("<key>", "<value>")
 # When you use the STS AccessKey ID to call RPC API operations, you must add the SecurityToken parameter to the header.
 # req.add_body_params("SecurityToken", "<your-securitytoken>");
 # When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-security-token parameter to the header.
 # req.add_header("x-acs-security-token", "<your-securitytoken>");
    # 4. Configure request headers.
    req.add_header("x-acs-resourcegroupid", "<your-resourcegroupid>");
    req.add_header("x-acs-organizationid", "<your-organizationid>");
    req.add_header("x-acs-regionid", "<your-regionid>");
    req.add_header("x-acs-instanceid", "<your-instanceid>");
    # 5. Configure a request method.
    req.set_method("POST")
    # 6. Configure initialization parameters for an ASClient object. The parameter values vary based on your environment. The timeout
parameter specifies the time-out period for a request. The cert_file parameter specifies the certificate. The verify parameter specifies wheth er to verify the certificate.
    as_client = ASClient("<accesskeyid>", "<accesskeysecret>", "<regionid>",timeout=1000,
            cert_file=None,
            verify=False)
    # Configure the identifier of the requester. This parameter is required and used only for identification. You can set this parameter to a
random value.
    as_client.setSdkSource("<The identifier of the requester>")
    response = as_client.do_request(req)
    print(response)
```

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. |
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |

**Configure proxies**

Perform the following steps to configure a proxy:
1. Import OS dependencies.

```java
import os
```

2. Configure one or more proxies.

```bash
# Before you make an API call, configure one or more proxies.
os.environ['http_proxy'] = "http://x.x.x.x:xxxx" os.environ['https_proxy'] = "https://x.x.x.x:xxxx"
```

#### 2.2.6 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js to call API operations. An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for the ASAPI. For more information about how to obtain the region ID, see Obtain the endpoint of ASAPI.

**Add dependencies**

Run the following command to install Apsara Stack SDK for Node.js: DKs

```
 tnpm i @ali/asapi-nodejs-sdk@0.0.33 --save
```

**Use Apsara Stack SDK for Node.js**

The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls:

```
// 1. Import the dependencies of Apsara Stack SDK for Node.js. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // 2. Configure the parameters. const cnofig = {
    API_GATEWAY: '<The endpoint of ASAPI>',
    regionId: '<The ID of the region in which the Apsara Stack service is deployed>',
    accessKeyId: '<The AccessKey ID of your Apsara Stack tenant account>',
    accessKeySecret: '<The AccessKey secret of your Apsara Stack tenant account>'
```

};

```json
// 3. Initialize a client for API calls. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // 4. Configure request parameters. const params = {
    "Action": "<The name of the API operation>",
    "Product": "<The name of the service that provides the API operation>",
    "Version": "<The version of the API operation>",
    "regionId": '<The ID of the region in which the Apsara Stack service is deployed>',
    // When you use the STS AccessKey ID to call RPC API operations, you must add the SecurityToken parameter to the header.
    // "SecurityToken": "<your-securitytoken>",
      "<The name of the operation-specific parameter required by the API operation>": "<The value of the operation-specific parameter>"
// 5. Configure request headers. // When you use the STS AccessKey ID to call ROA API operations, you must add the x-acs-security-token parameter to the header. // AsapiClient.addHeader("x-acs-security-token", "<your-securitytoken>") AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') AsapiClient.addHeader('x-acs-roleid', '<The ID of the role>') AsapiClient.addHeader('x-acs-userid', '<The ID of the user>') AsapiClient.addHeader('x-acs-organizationid', '<your-organizationid>') AsapiClient.addHeadert("x-acs-regionid", "<your-regionid>"); AsapiClient.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); AsapiClient.addHeader("x-acs-instanceid", "<your-instanceid>"); // 6. Make an API call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // The request method.
    formatParams: false, // Specifies whether to format parameters and capitalize the first letter of each parameter.
    enableProxy: true, // Specifies whether to configure a proxy.
    proxy: 'http://x.x.x.x:xxxx',
    timeout: 10000, // The time-out period.
  // ca: , // The certificate issued by a certificate authority (CA). For more information, visit
https://nodejs.org/api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

**Disable certificate validation**

The following sample code shows how to disable certificate validation:

```
Configure the environment variable. NODE_TLS_REJECT_UNAUTHORIZED=0
```

**Request headers**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. |
| x-acs-caller-sdk-source | The custom name of the requester or the system. This parameter is used to identify the source of the API request. |
| x-acs-roleid | The ID of the role. |
| x-acs-userid | The ID of the user. |

requests

## 3 HTTP requests

### 3.1 Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

### 3.2 Request structure

You can use API URLs to initiate HTTP GET requests. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of ASAPI.

**Sample request**

GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation. `Id` : the ID of the organization. `<Common request parameters>` : common parameters specified in the system.

**Protocols**

ASAPI supports only the HTTP request protocol.

**Endpoints**

For more information about how to obtain the endpoint of ASAPI, see Generate an endpoint for ASAPI. You must use the `Action, Product, and Version` parameters to specify an API operation. For example, you can set `Action to GetOrganizationList,` `Product to ascm, and Version to 2019-05-10` . You must also specify other operation-specific request parameters and common request parameters. For more information, see Common request parameters.

### 3.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni- manager Management Console.
> The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential.

ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI.

**Step 1: Create a canonicalized query string**

| Arrange the request parameters in alphabetical order, including all common and operation-specific parameters except the | Signature | parameter. |
|---|---|---|
| Note If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?). |   |   |

2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules apply in the encoding process:

| hyphens ( - ), the %XY forma ncoded as %22 %XY%ZA… form |   | - |   |   |   |   |
|---|---|---|---|---|---|---|
|   | %XY |   |   |   |   |   |
|   |   | %22 |   |   |   |   |
|   |   | form |   |   |   |   |
|   |   | s as plus signs ( + ). application/x-www-form-urlencoded library, use percentEncode to encod %20 , asterisks ( * ) with %2A , an | + | ). |   |   |
|   |   | %20 |   |   |   |   |

example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ).

| * | ) with | %2A |
|---|---|---|

an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException {
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null;
```

requests
3. Use equal signs ( `=` ) to connect the encoded request parameters and their values.
4. Use ampersands ( `&` ) to connect the encoded request parameters. These parameters must be arranged in the same order as those in Step 1.
Then, a canonicalized query string that follows the request structure is obtained. For more information, see Request structure.

**Step 2: Create a string-to-sign**

1. Create a `string-to-sign` . You can also use `percentEncode` to encode the canonicalized query string created in Step 1 based on the following
rules:

| StringToSign= HTTPMethod + "&" + //HTTPMethod: the HTTP method that is used to send a request, such as GET. percentEncode("/") + "&" + //percentEncode("/"): Encode the forward slash (/) in UTF-8 as %2F. percentEncode(CanonicalizedQueryString) // Encode the canonicalized query string created in Step 1. |   |   |   |   |
|---|---|---|---|---|
| Calculate the RFC 2104-compliant HMAC-SHA1 or HMAC-256 value of |   |   | StringToSign | . In the following example, Java Base64 is used: |
| String signature = Base64.getEncoder().encodeToString(signData); |   |   |   |   |
| Note When you calculate the signature, the key value specified by RFC 2104 is your AccessKey secret plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair. |   |   |   |   |
| Encode the | Signature | parameter based on RFC 3986 and add it to the canonicalized query string. |   |   |

**Example 1: Concatenate parameters**

`GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret. Perform the following operations:
1. Construct a canonicalized query string.

| https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-te st&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09- 15T08%3A50%3A40Z&Version=2019-05-10 |   |   |
|---|---|---|
| Create a | string-to-sign | . |
| GET&%2F&AccessKeyId%3Dtestid%26Action%3DGetOrganizationList%26Format%3DJSON%26Id%3D1%26Product%3Dascm%26RegionId%3Dcn-region- test%26SignatureMethod%3DHMAC-SHA1%26SignatureNonce%3D43967c6e-e3ad-44fa-b06b-fcf3db5f39d2%26SignatureVersion%3D1.0%26Timestamp%3D2020-09-15 T08%253A50%253A40Z%26Version%3D2019-05-10 |   |   |

3. Calculate the signature.
Calculate the signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is set to testsecret. The calculated

| signature is | OLeaidS1JvxuMvnyHOwuJ+uX5qY= . | Java Base64 is used in t |
|---|---|---|
| String signature = Base64.getEncoder().encodeToString(signData); |   |   |

String signature = Base64.getEncoder().encodeToString(signData); Encode `Signature=hvqv9Ll5RE6kQ4YsQXFAf9VuRIY=` based on RFC 3986 and add it to the canonicalized query string.

| https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-te st&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09- 15T08%3A50%3A40Z&Version=2019-05-10 |   |   |
|---|---|---|
| u can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the | DescribeRegions | operation to query the Alibaba |

Cloud region list.

**Example 2: Use the standard library of the programming language**

`GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
1. Predefine an encoding method.

| private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; } |   |   |   |   |
|---|---|---|---|---|
| Predefine the time format for the | Timestamp | parameter. Specify the | Timestamp | parameter in the ISO 8601 format. The time must be in UTC+0. |
| private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) { SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT); df.setTimeZone(new SimpleTimeZone(0, "GMT")); return df.format(date); } |   |   |   |   |

3. Create a request string.
requests

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Specify request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Arrange request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
//Encode the canonicalized query string. stringToSign.append(percentEncode( canonicalizedQueryString.toString().substring(1)));
```

4. The signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is set to testsecret. The calculated signature is

```
 OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D .
// The following sample code shows how to calculate the signature: final String ALGORITHM = "HmacSHA1"; final String ENCODING = "UTF-8"; key = "testsecret&"; Mac mac = Mac.getInstance(ALGORITHM); mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM)); byte[] signData = mac.doFinal(stringToSign.getBytes(ENCODING)); String signature = Base64.getEncoder().encodeToString(signData);
```

Encode the Signature parameter based on RFC 3986 and add it to the canonicalized query string. The following URL is obtained:

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-te st&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09- 15T08%3A50%3A40Z&Version=2019-05-10
```

5. Use browsers or tools such as cURL and Wget to initiate an HTTP request.

### 3.4 Responses

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned.

**Sample success responses**

If a request is successful, the request ID and operation-specific parameter values are returned. For more information, see the developer guide of the corresponding Apsara Stack service. requests

```json
   "successResponse":true,
  "eagleEyeTraceId":"xxxxxxxxxxxxxx",
  "asapiSuccess":true,
  "code":"200",
  "cost":12,
  "asapiRequestId":"xxxxxxxxxxxxxx",
  "data":[
```

`{`

```json
      "muserId":"aliyuntest",
      "internal":false,
      "level":"0",
      "supportRegions":"cn-*",
      "personNum":100,
      "mtime":1553247962000,
      "uuid":"1",
      "parentId":0,
      "supportRegionList":[
        "cn-*"
```

`],`

```json
      "name":"root",
      "alias":"root",
      "ctime":1553247962000,
      "id":1,
      "resourceGroupNum":100,
      "cuserId":"aliyuntest"
```

`],`

```json
  "requestId":"xxxxxxxxxxxxxx",
  "success":true,
  "message":"success"
```

**Sample error responses**

If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service. `{`

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by ASAPI.
```

## 4 API reference

### 4.1 Common parameters

**Common request parameters**

Common request parameters must be included in the request of each API. Table 1. Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API, in YYYY-MM-DD format. Set the value to 2019-05-10. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| AccessKeySecret | String | Yes | The AccessKey secret provided to you by Apsara Stack. |
| RegionID | String | Yes | The region ID provided to you by Apsara Stack. |
| Product | String | Yes | The name of the service to which the API operation belongs. |

You must obtain the values of the `Product` and `Version` parameters in the Apsara Uni-manager Management Console. Perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Others > API Tool**.
3. In the left-side navigation pane of the API Tool page, click **API Directory**.
4. In the **Operation Name** search box, enter the name of an operation to query its information.

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

### 4.2 Apsara Uni-manager Management Console authentication

**authentication**

Before you can make ASAPI requests, you must obtain the AccessKey pair (AccessKey ID and AccessKey secret) of an organization account in the Apsara Uni-manager Management Console. The organization account grants access permissions on available resources. Then, the resources can be accessed by using the AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair.

> **Important:** If you use the AccessKey pair of a personal account to call an API operation, you must configure header parameters for access control. Otherwise, a message is prompted to indicate that you have insufficient permissions.

Header parameters

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For information about how to obtain the ID of an organization, see GetOrganizationList. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For information about how to obtain the ID of a resource set, see ListResourceGroup. |
| x-acs-instanceid | The ID of the instance on which you perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

### 4.3 List of operations by function

#### 4.3.1 Enterprise

##### 4.3.1.1 Organizations

###### 4.3.1.1.1 UpdateOrganization

Updates an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/update HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| id | String | Body | No | 23 | The ID of the organization. Note This parameter is required. |
| name | String | Body | No | org-test | The name of the organization that you want to update. Note This parameter is required. |
| orgUuid | String | Body | No | org- 101****e53b40ae6086*** *m | The UUID of the organization. Note The organization UUID cannot be updated by using API operations. |
| parentId | String | Body | No | 1 | The ID of the parent organization. Note The ID of the root organization is 1. |
| level | String | Body | No | 0.1.3 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
| personNum | String | Body | No | 10 | The maximum number of users. The value must be a positive integer. |
| resourceGroupNum | String | Body | No | 10 | The maximum number of resource sets. The value must be a positive integer. |
| alias | String | Body | No | org-test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
| multiCloudStatus | String | Body | No | null | The multi-cloud status of the organization. Default value: null. master: The organization is a primary-cloud organization. slaver: The organization is a secondary-cloud organization. null: The organization is not a multi-cloud organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The organization ID is empty. The organization name is duplicated. One or more parameters are invalid. One or more request parameters are not specified in the operation. 403: You do not have permissions. 404: The user does not exist. 500: An internal error occurred. |
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Struct |   | The response data. |

| alias | String | org-test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
|---|---|---|---|
| ctime | Long | 1607512443989 | The time when the organization was created. |
| cuserId | String | 5003 | The username of the user who created the organization. |
| id | Integer | 1 | The ID of the organization. Note The ID of the root organization is 1. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. Note The system automatically generates a preset organization, which is also named the default organization. |
| level | String | 0.1 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
| mtime | Long | 1606791494471 | The time when the organization was last updated. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary-cloud organization. slave: The organization is a secondary-cloud organization. Note This parameter is returned only in multi-cloud scenarios. |
| muserId | String | admin | The username of the user who last updated the organization. |
| name | String | org-test | The name of the updated organization. The name is the same as the value that is specified for the name request parameter. |
| parentId | Integer | 0 | The ID of the parent organization. Note The ID of the root organization is 1. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of zones. |
| supportRegions | String | cn-qingdao-****-d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |
| message | String | 200 | The message. Examples: OrgNameExist: The organization name is duplicated. missing uuid or id: The UUID or ID of the organization is not contained in request parameters. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | false | Indicates whether the request is redirected. true false |
| requestId | String | 1 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateOrganization &Id=23 &Name=org-test &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>cn-qingdao-****-d01</supportRegions> <mtime>1606791494471</mtime> <uuid>1231</uuid> <parentId>0</parentId> <multiCloudStatus>master</multiCloudStatus> <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList> <name>org-test</name> <ctime>1607512443989</ctime> <alias>org-test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>1</requestId> <pureListData>true</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "data": { "muserId": "admin", "internal": true, "level": 0.1, "supportRegions": "cn-qingdao-****-d01", "mtime": 1606791494471, "uuid": 1231, "parentId": 0, "multiCloudStatus": "master", "supportRegionList": "[\"cn-qingdao-****-d01\"]", "name": "org-test", "ctime": 1607512443989, "alias": "org-test", "id": 1, "cuserId": "admin" }, "success": true, "requestId": 1, "pureListData": true, "message": 200 } |   |

###### 4.3.1.1.2 UpdateSupportRegionsForOrg

You can call this operation to update supported regions for an organization.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateSupportRegionsForOr g | The operation that you want to perform. Set the value to UpdateSupportRegionsForOrg. |
| OrganizationId | Integer | Yes | 5 | The ID of the organization. |
| SupportRegions | String | Yes | RegionId1,RegionId2 | The list of region IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |

| cost | Integer | 32 | The time consumed by the operation. |
|---|---|---|---|
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=UpdateSupportRegionsForOrg &OrganizationId=5 &SupportRegions=RegionId1,RegionId2 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>32</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "32", "code": "200", "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.1.3 GetOrganization

Queries the information about an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/query HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| id | Integer | Body | No | 32 | The ID of the organization. Note The ID of the root organization is 1. |
| orgUuid | String | Body | No | org- 101****0b6a70ae6086*** ** | The UUID of the organization. Note If you specify the id and orgUuid parameters, the value of the id parameter is used. If you leave the parameters empty, the response is empty. |
| requestId | String | Body | No | 0a1a****1655458030688 2970d**** | The ID of the request. Note In most cases, you do not need to specify this parameter. The system automatically generates a value for this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: One or more parameters are invalid or required request parameters are not specified for the operation. 403: You do not have permissions. 404: The user does not exist. 500: An internal error occurred. |
|---|---|---|---|
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Struct |   | The response data. |
| alias | String | test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The username of the user who created the organization. |
| extraInfo | String | null | This parameter is deprecated. |
| id | Integer | 1 | The ID of the organization. Note The ID of the root organization is 1. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. Note The system automatically generates a preset organization, which is also named the default organization. |
| level | String | 0.1 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
| mtime | Long | 1607512443989 | The time when the organization was last modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary-cloud organization. slave: The organization is a secondary-cloud organization. Note This parameter is returned only in multi-cloud scenarios. |
| muserId | String | admin | The username of the user who last modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. Note The ID of the root organization is 1. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of zones. |
| supportRegions | String | cn-qingdao-****-d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |
| message | String | success | The message. Examples: success: The call is successful. MissingParams: Required request parameters are not specified. |

| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
|---|---|---|---|
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetOrganization &Id=32 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>cn-qingdao-****-d01</supportRegions> <mtime>1607512443989</mtime> <uuid>1231</uuid> <parentId>1</parentId> <multiCloudStatus>master</multiCloudStatus> <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList> <name>test</name> <ctime>1606791494471</ctime> <alias>test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "data": { "muserId": "admin", "internal": "true", "level": "0.1", "supportRegions": "cn-qingdao-****-d01", "mtime": "1607512443989", "uuid": "1231", "parentId": "1", "multiCloudStatus": "master", "supportRegionList": "[\"cn-qingdao-****-d01\"]", "name": "test", "ctime": "1606791494471", "alias": "test", "id": "1", "cuserId": "admin" }, "success": "true", "requestId": "16d09b14-8a59-****-****-7536fe897b66", "pureListData": "true", "message": "success" } |   |

###### 4.3.1.1.4 GetOrganizationList

Queries the list of organizations.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetOrganizationList | The operation that you want to perform. Set the value to GetOrganizationList. |
| RequestId | String | No | sdfasdfafsdf | The ID of the request. |
| Id | String | No | 1 | The ID of the organization. |
| Name | String | No | test | The name of the organization. If both the organization ID and the organization name are specified, the organization ID prevails. If both the organization ID and the organization name are not specified, no data is returned. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1607512443989 | The time when the organization was created. |
| cuserId | String | admin | The creator of the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | cn-qingdao-env17-d01 | The list of regions. |
| supportRegions | String | ["cn-qingdao-env17-d01"] | The list of regions. |
| uuid | String | 1231 | The UUID of the organization. |
| message | String | success | The error message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| requestId | String | 1 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetOrganizationList &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>["cn-qingdao-env17-d01"]</supportRegions> <mtime>1606791494471</mtime> <uuid>1231</uuid> <parentId>0</parentId> <multiCloudStatus>master</multiCloudStatus> <name>test</name> <ctime>1607512443989</ctime> <alias>test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <data> <supportRegionList>cn-qingdao-env17-d01</supportRegionList> </data> <success>true</success> <requestId>1</requestId> <pureListData>true</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "data": [ { "muserId": "admin", "internal": "true", "level": "0.1", "supportRegions": "[\"cn-qingdao-env17-d01\"]", "mtime": "1606791494471", "uuid": "1231", "parentId": "0", "multiCloudStatus": "master", "name": "test", "ctime": "1607512443989", "alias": "test", "id": "1", "cuserId": "admin" }, { "supportRegionList": "cn-qingdao-env17-d01" } ], "success": "true", "requestId": "1", "pureListData": "true", "message": "200" } |   |

###### 4.3.1.1.5 RemoveOrganization

You can call this operation to delete an organization.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveOrganization | The operation that you want to perform. Set the value to RemoveOrganization. |
| Id | String | Yes | 10 | The ID of the organization. |
| RequestId | String | No | retertertet | The ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The time consumed by the operation. |
| message | String | 200 | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 1 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=RemoveOrganization &Id=10 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <requestId>1</requestId> <pureListData>true</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "10000", "code": "200", "success": "true", "requestId": "1", "pureListData": "true", "message": "200" } |   |

###### 4.3.1.1.6 ListResourceGroupByOrgId

You can call this operation to query the list of resource sets in an organization.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceGroupByOrgId | The operation that you want to perform. Set the value to ListResourceGroupByOrgId. |
| Id | String | Yes | 3 | The ID of the organization. |
| resourcegroupname _ _ | String | No | testrs | The name of the resource set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The time consumed by the operation. |
| data | Array of dataItem |   | The response. |
| creator | String | admin | The creator. |

| gmtCreated | Float | 1607512443989 | The creation time. |
|---|---|---|---|
| gmtModified | Float | 1607512443989 | The modification time. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| organizationName | String | admin | The name of the organization. |
| resourceGroupName | String | test | The name of the resource set. |
| resourceGroupType | Integer | 1 | The type of the resource set. |
| message | String | 200 | The message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The number of the page returned. |
| pageSize | Integer | 10 | The number of entries returned per page. |
| total | Integer | 10 | The total number of entries returned. |
| totalPage | Integer | 10 | The total number of pages returned. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=ListResourceGroupByOrgId &Id=3 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <organizationID>1</organizationID> <gmtModified>1607512443989</gmtModified> <creator>admin</creator> <resourceGroupName>test</resourceGroupName> <organizationName>admin</organizationName> <gmtCreated>1607512443989</gmtCreated> <resourceGroupType>1</resourceGroupType> <id>1</id> </data> <success>true</success> <pageInfo> <total>10</total> <totalPage>10</totalPage> <pageSize>10</pageSize> <currentPage>1</currentPage> </pageInfo> <pureListData>true</pureListData> <message> 200</message> |   |

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "data": [
```

`{`

```json
            "organizationID": "1",
            "gmtModified": "1607512443989",
            "creator": "admin",
            "resourceGroupName": "test",
            "organizationName": "admin",
            "gmtCreated": "1607512443989",
            "resourceGroupType": "1",
            "id": "1"
```

`],`

```json
    "success": "true",
    "pageInfo": {
        "total": "10",
        "totalPage": "10",
        "pageSize": "10",
        "currentPage": "1"
```

`},`

```json
    "pureListData": "true",
    "message": " 200"
```

###### 4.3.1.1.7 CreateOrganization

You can call this operation to create an organization.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateOrganization | The operation that you want to perform. Set the value to CreateOrganization. |
| Name | String | Yes | hellowolrd | The name of the organization. |
| ParentId | String | Yes | 1 | The ID of the parent organization. |
| RequestId | String | No | 100000000 | The ID of the request. |
| PersonNum | String | No | 1 | A reserved parameter. |
| ResourceGroupNum | String | No | 1 | A reserved parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The time consumed by the operation. |
| data | Struct |   | The response. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1607512443989 | The creation time. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The modification time. |

| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. |
|---|---|---|---|
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegionList | List | cn-qingdao-env17-d01 | The list of regions. |
| supportRegions | String | ["cn-qingdao-env17-d01"] | The list of regions. |
| uuid | String | 1231 | The universally unique identifier (UUID) of the organization. |
| message | String | 200 | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| requestId | String | 1234 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=CreateOrganization &Name=hellowolrd &ParentId=1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>["cn-qingdao-env17-d01"]</supportRegions> <mtime>1606791494471</mtime> <uuid>1231</uuid> <parentId>1</parentId> <multiCloudStatus>master</multiCloudStatus> <supportRegionList>cn-qingdao-env17-d01</supportRegionList> <name>test</name> <ctime>1607512443989</ctime> <alias>test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>1234</requestId> <pureListData>true</pureListData> <message>200</message> |   |

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "data": {
        "muserId": "admin",
        "internal": "true",
        "level": "0.1",
        "supportRegions": "[\"cn-qingdao-env17-d01\"]",
        "mtime": "1606791494471",
        "uuid": "1231",
        "parentId": "1",
        "multiCloudStatus": "master",
        "supportRegionList": "cn-qingdao-env17-d01",
        "name": "test",
        "ctime": "1607512443989",
        "alias": "test",
        "id": "1",
        "cuserId": "admin"
```

`},`

```json
    "success": "true",
    "requestId": "1234",
    "pureListData": "true",
    "message": "200"
```

###### 4.3.1.1.8 GetPrivateCloudAccountByOrganizationId

Queries an Apsara Stack tenant account with which a level-1 organization is associated.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/getPrivateCloudAccountByOrganizationId HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| OrganizationId | Integer | Body | Yes | 1 | The ID of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Struct |   | The response data. |
| aliyunid | String | 1 | The ID of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| message | String | success | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/getPrivateCloudAccountByOrganizationId HTTP/1.1 Common request headers
```

`{`

```json
"OrganizationId": "1"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <aliyunid>1</aliyunid> <primaryKey>212530506704030466</primaryKey> </data> <success>true</success> <pureListData>true</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": {"aliyunid":"1","primaryKey":"212530506704030466"},"success":"true","pureListData":"true","message":"success"} |   |

##### 4.3.1.2 Resource sets

###### 4.3.1.2.1 CreateResourceGroup

You can call this operation to create a resource set.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateResourceGroup | The operation that you want to perform. Set the value to CreateResourceGroup. |
| organizationid _ | Integer | Yes | 3 | The ID of the organization. |
| resourcegroupname _ _ | String | Yes | testrs | The name of the resource set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The time consumed by the operation. |
| data | Struct |   | The response. |
| gmtCreated | Long | 1607512443989 | The creation time. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | String | 1 | The ID of the organization. |
| resourceGroupName | String | test | The name of the resource set. |
| rsId | String | rs-1010e71e5e520aab483b000f | The unique ID of the registry. |
| message | String | 200 | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| requestId | String | 1234 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=CreateResourceGroup &organization_id=3 &resource_group_name=testrs &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <organizationID>1</organizationID> <resourceGroupName>test</resourceGroupName> <gmtCreated>1607512443989</gmtCreated> <rsId>rs-1010e71e5e520aab483b000f</rsId> <id>1</id> </data> <success>true</success> <requestId>1234</requestId> <pureListData>true</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "data": { "organizationID": "1", "resourceGroupName": "test", "gmtCreated": "1607512443989", "rsId": "rs-1010e71e5e520aab483b000f", "id": "1" }, "success": "true", "requestId": "1234", "pureListData": "true", "message": "200" } |   |

###### 4.3.1.2.2 UnbindAscmUserAndResourceGroup

You can call this operation to unbind a user from a resource set.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnbindAscmUserAndResourc eGroup | The operation that you want to perform. Set the value to UnbindAscmUserAndResourceGroup. |
| AscmUserIds | String | Yes | 1 | The list of user IDs. |
| ResourceGroupId | Integer | Yes | 1 | The ID of the resource set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The time consumed by the operation. |
| message | String | 200 | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=UnbindAscmUserAndResourceGroup &AscmUserIds=1 &ResourceGroupId=1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <pureListData>true</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "pureListData": "true", "message": "200" } |   |

###### 4.3.1.2.3 UpdateResourceGroup

Modifies the information of a resource set.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateResourceGroup | The operation that you want to perform. Set the value to UpdateResourceGroup. |
| id | String | Yes | 16 | The ID of the resource set to be modified. |
| resourcegroupname _ _ | String | Yes | oldres _ | The current name of the resource set to be modified. |
| resourceGroupName | String | Yes | newres _ | The new name of the resource set to be modified. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The amount of time taken to perform the operation. |
| message | String | 200 | The message. |
| pageInfo | Struct |   | The data information. |
| gmtModified | Float | 1606791494471 | The time when the resource set was modified. |
| id | Integer | 1 | The ID of the resource set. |
| resourceGroupName | String | test | The name of the resource set. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateResourceGroup &id=16 &resource_group_name=DefaultRewwww &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <pageInfo> <gmtModified>1606791494471</gmtModified> <resourceGroupName>test</resourceGroupName> <id>1</id> </pageInfo> <pureListData>true</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "pageInfo": { "gmtModified": "1606791494471", "resourceGroupName": "test", "id": "1" }, "pureListData": "true", "message": "200" } |   |

###### 4.3.1.2.4 RemoveResourceGroup

Deletes a resource set.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /ascm/auth/resource_group/delete_resource_group HTTP/1.1
```

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| resourcegroupid _ _ | Integer | Body | No | 5 | The ID of the resource set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The time consumed by the operation. |
| message | String | 200 | The message. |
| pureListData | Integer | 0 | Indicates whether only data is returned and other parameters are not returned. 0 indicates that only data is returned. 1 indicates that other parameters are returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| requestId | String | 1234 | The ID of the request. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveResourceGroup &resource_group_id=5 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <requestId>1234</requestId> <pureListData>0</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "requestId": "1234", "pureListData": "0", "message": "200" } |   |

###### 4.3.1.2.5 ListResourceGroup

Queries the list of available resource sets of a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceGroup | The operation that you want to perform. Set the value to ListResourceGroup. |
| resourceGroupName | String | No | test | The name of the resource set to be queried. |
| organizationId | Integer | No | 1 | The ID of the organization. After this parameter is specified, you can obtain the list of resource sets in the current organization, excluding its subordinate organizations. If this parameter is not specified or is set to 1, the list of all resource sets visible to the user is obtained. |
| pageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| pageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The page information. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| Total | Integer | 10 | The total number of entries returned. |
| TotalPage | Integer | 1 | The total number of pages. |
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| creator | String | admin | The creator of the resource set. |

| gmtCreated | Float | 1606719003858 | The time when the resource set was created. |
|---|---|---|---|
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| organizationName | String | test | The name of the organization. |
| resourceGroupName | String | test | The name of the resource set. |
| rsId | String | rs-1010e71e5e520aab483b000f | The ID of the resource set. |
| message | String | 200 | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListResourceGroup &<Common request parameters>
```

Sample success response

| XML | format |
|---|---|
| <redirect>true</redirect> <PageInfo> <TotalPage>1</TotalPage> <PageSize>10</PageSize> <CurrentPage>1</CurrentPage> <Total>10</Total> </PageInfo> <cost>10000</cost> <code>200</code> <data> <organizationID>1</organizationID> <creator>admin</creator> <resourceGroupName>test</resourceGroupName> <organizationName>test</organizationName> <gmtCreated>1606719003858</gmtCreated> <rsId>rs-1010e71e5e520aab483b000f</rsId> <id>1</id> </data> <success>true</success> <pureListData>true</pureListData> <message>200</message> |   |

`JSON` format `{`

```json
    "redirect": "true",
    "PageInfo": {
        "TotalPage": "1",
        "PageSize": "10",
        "CurrentPage": "1",
        "Total": "10"
```

`},`

```json
    "cost": "10000",
    "code": "200",
    "data": [
```

`{`

```json
            "organizationID": "1",
            "creator": "admin",
            "resourceGroupName": "test",
            "organizationName": "test",
            "gmtCreated": "1606719003858",
            "rsId": "rs-1010e71e5e520aab483b000f",
            "id": "1"
```

`],`

```json
    "success": "true",
    "pureListData": "true",
    "message": "200"
```

###### 4.3.1.2.6 BindAscmUserAndResourceGroup

Binds a user to a resource set.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request syntax**

```
POST /ascm/auth/resource_group/add_ascm_users HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| resourcegroupid _ _ | Integer | Body | No | 7 | The ID of the resource set. |
| ascmuserids _ _ | String | Body | No | "[\"5017\",\"5023 \"]" | The user IDs to be bound. Separate multiple user IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 10000 | The amount of time taken to perform the operation. |
| message | String | 200 | The message. |
| pureListData | Integer | 0 | Indicates whether only data is returned and other parameters are not returned. 0 indicates that only data is returned. 1 indicates that other parameters are returned. |
| redirect | Boolean | true | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/resource_group/add_ascm_users HTTP/1.1 http(s)://[Endpoint]/?Action=BindAscmUserAndResourceGroup &ascm_user_ids="[\"5017\",\"5023 \"]" &resource_group_id=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <pureListData>0</pureListData> <message>200</message>
```

| JSON | format |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "pureListData": "0", "message": "200" } |   |

###### 4.3.1.2.7 ListAscmUsersInsideResourceGroup

You can call this operation to query the list of users within a resource set.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListAscmUsersInsideResource Group | The operation that you want to perform. Set the value to ListAscmUsersInsideResourceGroup. |
| ResourceGroupId | Integer | Yes | 7 | The ID of the resource set. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| cost | Integer | 1000 | The time consumed by the operation. |
| data | Array of dataItem |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdg******** | The AccessKey ID. |
| ctime | Long | 1606675230000 | The creation time. |
| cuserId | String | 1 | The ID of the creator. |
| id | Integer | 1 | The ID of the AccessKey pair. |
| region | String | cn-qingdao-env17-d01 | The region. |
| status | String | ACTIVE | The status. |
| cellphoneNum | String | 00000000000 | The phone number. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| defaultRole | Struct |   | The list of roles. |

| active | Boolean | true | Indicates whether the operation is active. |
|---|---|---|---|
| arId | String | 111 | The unique code. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description. |
| enable | Boolean | true | Indicates whether the operation is enabled. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The creator. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the organization. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name. |
| email | String | t***@163.com | The email address. |
| enableDingTalk | Boolean | false | Indicates whether notifications are sent by DingTalk. |
| enableEmail | Boolean | false | Indicates whether notifications are sent by email. |
| enableShortMessage | Boolean | false | Indicates whether notifications are sent by SMS. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The username. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The creator. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the operation is enabled. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |

| protocol | String | IPV4 | The protocol. |
|---|---|---|---|
| lpId | String | 111 | The unique code. |
| muserId | String | admin | The creator. |
| name | String | deafult.loginpolicy | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the organization. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The creation time. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The modification time. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-env17-d01 | The list of regions. |
| uuid | String | 1231 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the operation is active. |

| arId | String | 111 | The unique code. |
|---|---|---|---|
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description. |
| enable | Boolean | true | Indicates whether the operation is enabled. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The creator. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the organization. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. |
| status | String | ACTIVE | The status. |
| userGroupRoles | List | admin | The list of roles of the user group. |
| userGroups | List | admin | The list of user groups. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the operation is active. |
| arId | String | 1121 | The unique code. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description. |
| enable | Boolean | true | Indicates whether the operation is enabled. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the organization. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1123 | The level of the role. |

| roleName | String | defaultRole.resourceUser.name | The name of the role. |
|---|---|---|---|
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. |
| message | String | 200 | The message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 10 | The number of entries returned per page. |
| total | Integer | 10 | The total number of entries returned. |
| totalPage | Integer | 10 | The total number of pages returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=ListAscmUsersInsideResourceGroup &ResourceGroupId=7 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <code>200</code> <cost>49</cost> <data> <cellphoneNum>13813800138</cellphoneNum> <defaultRole> <roleRange>roleRange.resourceSet</roleRange> <muserId/> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_SET_ADMIN</code> <active>true</active> <description>defaultRole.resourceSetAdmin.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceSetAdmin.name</roleName> <id>5</id> <roleLevel>2147483647</roleLevel> <cuserId/> <organizationVisibility>organizationVisibility.global</organizationVisibility> </defaultRole> <displayName>asapibaixue1</displayName> <enableDingTalk>true</enableDingTalk> <roles> <roleRange>roleRange.resourceSet</roleRange> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_SET_ADMIN</code> <active>true</active> <description>defaultRole.resourceSetAdmin.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceSetAdmin.name</roleName> <id>5</id> <roleLevel>2147483647</roleLevel> <organizationVisibility>organizationVisibility.global</organizationVisibility> </roles> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> |   |

```xml
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_USER</code>
        <active>true</active>
        <description>defaultRole.resourceUser.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <id>2</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1824191931284921</parentPk>
    <lastLoginTime>1592232390657</lastLoginTime>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_USER</code>
        <active>true</active>
        <description>defaultRole.resourceUser.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <id>2</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
```

`d/`

```xml
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_SET_ADMIN</code>
        <active>true</active>
        <description>defaultRole.resourceSetAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceSetAdmin.name</roleName>
        <id>5</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1591931519000</ctime>
        <id>609</id>
        <region>cn-qingdao-env17-d01</region>
        <accesskeyId>1KAj********</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>asapibaixue1</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-env17-d01</supportRegionList>
        <level>0.1</level>
        <name>asapi_test</name>
        <alias>asapi_test</alias>
        <supportRegions>cn-qingdao-env17-d01</supportRegions>
        <id>353</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5617</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>mail@example.com</email>
    <enableShortMessage>true</enableShortMessage>
    <primaryKey>261424091942319265</primaryKey>
    <status>ACTIVE</status>
</data> <data>
    <cellphoneNum>13813813800</cellphoneNum>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <displayName>asapitest</displayName>
    <enableDingTalk>true</enableDingTalk>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
```

```xml
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1824191931284921</parentPk>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1591930977000</ctime>
        <id>607</id>
        <region>cn-qingdao-env17-d01</region>
        <cuserId>admin</cuserId>
        <accesskeyId>o4LE********</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>asapitest</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-env17-d01</supportRegionList>
        <level>0.1</level>
        <name>asapi_test</name>
        <alias>asapi_test</alias>
        <supportRegions>cn-qingdao-env17-d01</supportRegions>
        <id>353</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5615</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>mail@example.com</email>
    <enableShortMessage>true</enableShortMessage>
    <primaryKey>250944791941776838</primaryKey>
    <status>ACTIVE</status>
</data> <data>
    <cellphoneNum>13813813800</cellphoneNum>
    <displayName>asapibaixue</displayName>
    <enableDingTalk>false</enableDingTalk>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
```

```xml
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1824191931284921</parentPk>
    <accessKeys>
        <ctime>1591931388000</ctime>
        <id>608</id>
        <region>cn-qingdao-env17-d01</region>
        <accesskeyId>cNae********</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>asapibaixue</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-env17-d01</supportRegionList>
        <level>0.1</level>
        <name>asapi_test</name>
        <alias>asapi_test</alias>
        <supportRegions>cn-qingdao-env17-d01</supportRegions>
        <id>353</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5616</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>false</enableEmail>
    <email>mail@example.com</email>
    <enableShortMessage>false</enableShortMessage>
    <primaryKey>221543391942188032</primaryKey>
    <status>ACTIVE</status>
</data> <success>true</success> <pageInfo>
    <total>3</total>
    <totalPage>1</totalPage>
    <pageSize>10</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": false, "code": "200", "cost": 49, "data": [ { "cellphoneNum": "13813800138", "defaultRole": { "roleRange": "roleRange.resourceSet", "muserId": "", "rAMRole": false, "code": "ROLE_RESOURCE_SET_ADMIN", "active": true, "description": "defaultRole.resourceSetAdmin.description", "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.resourceSetAdmin.name", "id": 5, "roleLevel": 2147483647, "cuserId": "", "organizationVisibility": "organizationVisibility.global" }, "displayName": "asapibaixue1", "enableDingTalk": true, "roles": [ { "roleRange": "roleRange.resourceSet", "rAMRole": false, "code": "ROLE_RESOURCE_SET_ADMIN", "active": true, "description": "defaultRole.resourceSetAdmin.description", "roleType": "ROLETYPE_ASCM", "default": true, |   |

```json
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceSetAdmin.name",
            "id": 5,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "code": "ROLE_ORGANIZATION_ADMIN",
            "active": true,
            "description": "defaultRole.organizationAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "id": 4,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
            "roleRange": "roleRange.resourceSet",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_USER",
            "active": true,
            "description": "defaultRole.resourceUser.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "id": 2,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
```

`],`

```json
        "loginPolicy": {
          "ipRanges": [
```

`{`

```json
              "protocol": "IPV4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
```

`],`

```json
          "muserId": "",
          "default": true,
          "ownerOrganizationId": 1,
          "timeRanges": [
```

`{`

```json
              "loginPolicyId": 1,
              "startTime": "00:00",
              "endTime": "24:00"
```

`],`

```json
          "enable": true,
          "name": "defaultLoginPolicy.name",
          "rule": "ALLOW",
          "id": 1,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
        "parentPk": "1824191931284921",
        "lastLoginTime": 1592232390657,
        "userGroups": [],
        "userRoles": [
```

`{`

```json
            "roleRange": "roleRange.resourceSet",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_USER",
            "active": true,
            "description": "defaultRole.resourceUser.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "id": 2,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
            "roleRange": "roleRange.orgAndSubOrgs",
            "muserId": "",
```

```json
            "rAMRole": false,
            "code": "ROLE_ORGANIZATION_ADMIN",
            "active": true,
            "description": "defaultRole.organizationAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "id": 4,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
            "roleRange": "roleRange.resourceSet",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_SET_ADMIN",
            "active": true,
            "description": "defaultRole.resourceSetAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceSetAdmin.name",
            "id": 5,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
```

`],`

```json
        "accessKeys": [
```

`{`

```json
            "ctime": 1591931519000,
            "id": 609,
            "region": "cn-qingdao-env17-d01",
            "accesskeyId": "1KAj********",
            "status": "ACTIVE"
```

`],`

```json
        "default": false,
        "deleted": false,
        "loginName": "asapibaixue1",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-env17-d01"
```

`],`

```json
          "level": "0.1",
          "name": "asapi_test",
          "alias": "asapi_test",
          "supportRegions": "cn-qingdao-env17-d01",
          "id": 353,
          "cuserId": "",
          "uuid": "null",
          "parentId": 1
```

`},`

```json
        "userGroupRoles": [],
        "id": 5617,
        "mobileNationCode": "86",
        "enableEmail": true,
        "email": "mail@example.com",
        "enableShortMessage": true,
        "primaryKey": "261424091942319265",
        "status": "ACTIVE"
```

`},` `{`

```json
        "cellphoneNum": "13813813800",
        "defaultRole": {
          "roleRange": "roleRange.orgAndSubOrgs",
          "muserId": "",
          "rAMRole": false,
          "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
          "active": true,
          "description": "defaultRole.yundunOrgSecAdmin.description",
          "roleType": "ROLETYPE_ASCM",
          "default": true,
          "ownerOrganizationId": 1,
          "enable": true,
          "roleName": "defaultRole.yundunOrgSecAdmin.name",
          "id": 8,
          "roleLevel": 2147483647,
          "cuserId": "",
"organizationVisibility":"organizationVisibility.global"
```

```
          organizationVisibility: organizationVisibility.global
```

`},`

```json
        "displayName": "asapitest",
        "enableDingTalk": true,
        "roles": [
```

`{`

```json
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
            "active": true,
            "description": "defaultRole.yundunOrgSecAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.yundunOrgSecAdmin.name",
            "id": 8,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
```

`],`

```json
        "loginPolicy": {
          "ipRanges": [
```

`{`

```json
              "protocol": "IPV4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
```

`],`

```json
          "muserId": "",
          "default": true,
          "ownerOrganizationId": 1,
          "timeRanges": [
```

`{`

```json
              "loginPolicyId": 1,
              "startTime": "00:00",
              "endTime": "24:00"
```

`],`

```json
          "enable": true,
          "name": "defaultLoginPolicy.name",
          "rule": "ALLOW",
          "id": 1,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
        "parentPk": "1824191931284921",
        "userGroups": [],
        "userRoles": [
```

`{`

```json
            "roleRange": "roleRange.orgAndSubOrgs",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
            "active": true,
            "description": "defaultRole.yundunOrgSecAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.yundunOrgSecAdmin.name",
            "id": 8,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
```

`],`

```json
        "accessKeys": [
```

`{`

```json
            "ctime": 1591930977000,
            "id": 607,
            "region": "cn-qingdao-env17-d01",
            "cuserId": "admin",
            "accesskeyId": "o4LE********",
            "status": "ACTIVE"
```

`],`

```json
        "default": false,
        "deleted": false,
        "loginName": "asapitest",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-env17-d01"
```

`],`

```
"leel" "01"
```

```json
          "level": "0.1",
          "name": "asapi_test",
          "alias": "asapi_test",
          "supportRegions": "cn-qingdao-env17-d01",
          "id": 353,
          "cuserId": "",
          "uuid": "null",
          "parentId": 1
```

`},`

```json
        "userGroupRoles": [],
        "id": 5615,
        "mobileNationCode": "86",
        "enableEmail": true,
        "email": "mail@example.com",
        "enableShortMessage": true,
        "primaryKey": "250944791941776838",
        "status": "ACTIVE"
```

`},` `{`

```json
        "cellphoneNum": "13813813800",
        "displayName": "asapibaixue",
        "enableDingTalk": false,
        "loginPolicy": {
          "ipRanges": [
```

`{`

```json
              "protocol": "IPV4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
```

`],`

```json
          "muserId": "",
          "default": true,
          "ownerOrganizationId": 1,
          "timeRanges": [
```

`{`

```json
              "loginPolicyId": 1,
              "startTime": "00:00",
              "endTime": "24:00"
```

`],`

```json
          "enable": true,
          "name": "defaultLoginPolicy.name",
          "rule": "ALLOW",
          "id": 1,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
        "parentPk": "1824191931284921",
        "userGroups": [],
        "userRoles": [],
        "accessKeys": [
```

`{`

```json
            "ctime": 1591931388000,
            "id": 608,
            "region": "cn-qingdao-env17-d01",
            "accesskeyId": "cNae********",
            "status": "ACTIVE"
```

`],`

```json
        "default": false,
        "deleted": false,
        "loginName": "asapibaixue",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-env17-d01"
```

`],`

```json
          "level": "0.1",
          "name": "asapi_test",
          "alias": "asapi_test",
          "supportRegions": "cn-qingdao-env17-d01",
          "id": 353,
          "cuserId": "",
          "uuid": "null",
          "parentId": 1
```

`},`

```json
        "userGroupRoles": [],
        "id": 5616,
        "mobileNationCode": "86",
        "enableEmail": false,
        "email": "mail@example.com",
        "enableShortMessage": false,
        "primaryKey": "221543391942188032",
        "status": "ACTIVE"
```

`],`

```json
    "success": true,
    "pageInfo": {
      "total": 3,
      "totalPage": 1,
      "pageSize": 10,
      "currentPage": 1
```

`},`

```json
    "pureListData": false,
    "message": "success"
```

##### 4.3.1.3 Roles

###### 4.3.1.3.1 SetDefaultRole

Sets a default role.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetDefaultRole | The operation that you want to perform. Set the value to SetDefaultRole. |
| RoleId | Integer | Yes | 5 | The ID of the role. |
| LoginName | String | No | testu | The logon name of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetDefaultRole &RoleId=5 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect":"false", "cost":"1000", "code":"200", "success":"true", "pureListData":"false", "message":"success" } |   |

###### 4.3.1.3.2 ListRoles

Queries the list of available roles of a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListRoles | The operation that you want to perform. Set the value to ListRoles. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| IsDefault | Boolean | No | true | Specifies whether the role is a built-in role. |
| RoleType | String | No | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM: the Resource Access Management (RAM) _ role ROLETYPEASCM: the custom role _ |
| RoleName | String | No | defaultRole.organizationAdmi n.name | The name of the role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-9999999902 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | defaultRole.resourceUser.descript ion | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The organization to which the role belongs. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2147483647 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |

| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM: the RAM role _ ROLETYPEASCM: the custom role _ |
| userCount | Integer | 12 | The number of users. |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 2 | The total number of entries returned. |
| totalPage | Integer | 39 | The total number of pages. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListRoles &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>ar-9999999902</arId> <code>ROLE_RESOURCE_USER</code> <description>defaultRole.resourceUser.description</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <userCount>12</userCount> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <roleLevel>2147483647</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> </data> <success>true</success> <pageInfo> <total>2</total> <totalPage>39</totalPage> <pageSize>20</pageSize> <currentPage>1</currentPage> </pageInfo> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": false, "cost": 1000, "code": 200, "data": { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": false, "muserId": "admin", "arId": "ar-9999999902", "code": "ROLE_RESOURCE_USER", "description": "defaultRole.resourceUser.description", "active": true, "roleType": "ROLETYPE_ASCM", "default": true, "userCount": 12, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.resourceUser.name", "roleLevel": 2147483647, "id": 1, "organizationVisibility": "organizationVisibility.global" }, "success": true, "pageInfo": { "total": 2, "totalPage": 39, "pageSize": 20, "currentPage": 1 }, "pureListData": false, "message": "success" } |   |

###### 4.3.1.3.3 ListActiveRoles

Queries the list of roles that can be bound.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListActiveRoles | The operation that you want to perform. Set the value to ListActiveRoles. |
| IncludeRAMRoles | Boolean | No | false | Specifies whether to include Resource Access Management (RAM) roles. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-9999999902 | The ID of the role. |
| code | String | 200 ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | defaultRole.resourceUser.descript ion | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The organization to which the role belongs. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2147483647 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| userCount | Integer | 12 | The number of users. |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 2 | The total number of entries returned. |
| totalPage | Integer | 39 | The total number of pages. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListActiveRoles &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <roleRange>roleRange.orgAndSubOrgs</roleRange>
    <rAMRole>false</rAMRole>
    <arId>ar-9999999902</arId>
    <code>200 ROLE_RESOURCE_USER</code>
    <description>defaultRole.resourceUser.description</description>
    <active>true</active>
    <roleType>ROLETYPE_ASCM</roleType>
    <default>true</default>
    <userCount>12</userCount>
    <ownerOrganizationId>1</ownerOrganizationId>
    <enable>true</enable>
    <roleName>defaultRole.resourceUser.name</roleName>
    <roleLevel>2147483647</roleLevel>
    <id>1</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
</data> <success>true</success> <pageInfo>
    <total>2</total>
    <totalPage>39</totalPage>
    <pageSize>20</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": [ { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "arId": "ar-9999999902", "code": "200 ROLE_RESOURCE_USER", "description": "defaultRole.resourceUser.description", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "userCount": "12", "ownerOrganizationId": "1", "enable": "true", "roleName": "defaultRole.resourceUser.name", "roleLevel": "2147483647", "id": "1", "organizationVisibility": "organizationVisibility.global" } ], "success": "true", "pageInfo": { "total": "2", "totalPage": "39", "pageSize": "20", "currentPage": "1" }, "pureListData": "false", "message": "success" } |   |

##### 4.3.1.4 Users

###### 4.3.1.4.1 AddUser

Creates a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddUser | The operation that you want to perform. Set the value to AddUser. |
| CellphoneNum | String | Yes | 10000000000 | The mobile number of the user. |

| DisplayName | String | Yes | testuser | The display name of the user. |
|---|---|---|---|---|
| Email | String | Yes | a***@a.com | The email address of the user. |
| LoginName | String | Yes | testu | The logon name of the user. |
| LoginPolicyId | Integer | Yes | 1 | The ID of the logon policy. |
| MobileNationCode | String | Yes | 86 | The country code. |
| OrganizationId | Integer | Yes | 5 | The ID of the organization. |
| roleIdList | Json | No | {"RoleIdList": [ "5", "6", "8" ]} | The list of role IDs. |
| OrganizationUuid | String | No | 1223 | The UUID of the organization. |
| TelephoneNum | String | No | 00000000 | The telephone number. |
| DingTalkToken | String | No | 12345abc | The DingTalk token. |
| EnableDingTalk | Boolean | No | false | Specifies whether to use DingTalk to send notifications. |
| EnableShortMessage | Boolean | No | false | Specifies whether to use SMS to send notifications. |
| EnableEmail | Boolean | No | false | Specifies whether to use emails to send notifications. |
| MultiCloudStatus | String | No | master | Specifies whether the user is a multi-cloud user. Valid values: master and slave. master indicates a primary-cloud user. slave indicates a secondary-cloud user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID of the user. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| id | Integer | 1 | The ID of the AccessKey pair. |
| region | String | cn-qingdao-****-d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |

| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
|---|---|---|---|
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who created the logon policy. |
| name | String | deafult.loginpolicy | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range for the query. |
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the Resource Access Management (RAM) user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |

| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
|---|---|---|---|
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRoles | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 11213 | The ID of the user group. |
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | ack-user-old | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |

| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
|---|---|---|---|
| uuid | String | 1231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | restest _ | The name of the resource set. |
| rsId | String | 12312a | The ID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1231 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
|---|---|---|---|
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | RamUser | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8**** | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |

| arId | String | 1121 | The ID of the role. |
|---|---|---|---|
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1123 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddUser &CellphoneNum=10000000000 &DisplayName=testuser &Email=a***@a.com &LoginName=testu &LoginPolicyId=1 &MobileNationCode=86 &OrganizationId=5 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> / |   |

```xml
<code>200</code> <cost>5542</cost> <data>
    <cellphoneNum>13269752565</cellphoneNum>
    <displayName>csblcl</displayName>
    <enableDingTalk>true</enableDingTalk>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_GLOBAL_RESOURCE_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.globalResourceAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.globalResourceAuditor.name</roleName>
        <id>6</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_PLATSECCONF_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunPlatSecConfAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunPlatSecConfAdmin.name</roleName>
        <id>15</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_SET_ADMIN</code>
        <active>true</active>
        <description>defaultRole.resourceSetAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceSetAdmin.name</roleName>
        <id>5</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_GLOBALORG_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunGlobalOrgAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunGlobalOrgAdmin.name</roleName>
        <id>11</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_PLATSEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunPlatSecAdmin.description</description>
```

```xml
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunPlatSecAdmin.name</roleName>
        <id>12</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_SECSYSCONF_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunSecSysConfAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunSecSysConfAdmin.name</roleName>
        <id>10</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_SEC_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.yundunSecAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunSecAuditor.name</roleName>
        <id>9</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_PLATSEC_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.yundunPlatSecAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunPlatSecAuditor.name</roleName>
        <id>14</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORG_RESOURCE_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.orgResourceAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.orgResourceAuditor.name</roleName>
        <id>16</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
```

```xml
        <code>ROLE_RESOURCE_USER</code>
        <active>true</active>
        <description>defaultRole.resourceUser.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <id>2</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_GLOBALORGSEC_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.yundunGlobalOrgSecAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunGlobalOrgSecAuditor.name</roleName>
        <id>13</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1925689189671814</parentPk>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_USER</code>
        <active>true</active>
        <description>defaultRole.resourceUser.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <id>2</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <muserId/>
<rAMRole>false</rAMRole>
```

```xml
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_SET_ADMIN</code>
        <active>true</active>
        <description>defaultRole.resourceSetAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceSetAdmin.name</roleName>
        <id>5</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_GLOBAL_RESOURCE_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.globalResourceAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.globalResourceAuditor.name</roleName>
        <id>6</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_SEC_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.yundunSecAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunSecAuditor.name</roleName>
        <id>9</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_SECSYSCONF_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunSecSysConfAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunSecSysConfAdmin.name</roleName>
        <id>10</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_GLOBALORG_ADMIN</code>
```

`i` `/` `i`

```xml
        <active>true</active>
        <description>defaultRole.yundunGlobalOrgAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunGlobalOrgAdmin.name</roleName>
        <id>11</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_PLATSEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunPlatSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunPlatSecAdmin.name</roleName>
        <id>12</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_GLOBALORGSEC_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.yundunGlobalOrgSecAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunGlobalOrgSecAuditor.name</roleName>
        <id>13</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_PLATSEC_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.yundunPlatSecAuditor.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunPlatSecAuditor.name</roleName>
        <id>14</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_PLATSECCONF_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunPlatSecConfAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunPlatSecConfAdmin.name</roleName>
        <id>15</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORG_RESOURCE_AUDITOR</code>
        <active>true</active>
        <description>defaultRole.orgResourceAuditor.description</description>
```

```xml
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.orgResourceAuditor.name</roleName>
        <id>16</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1592439877000</ctime>
        <id>664</id>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <accesskeyId>mX7fKY******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>csbuser</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
        <name>dataworks_test</name>
        <alias>dataworks_test</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <id>41</id>
        <cuserId/>
        <uuid>41</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5671</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>w***@alibaba-inc.com</email>
    <enableShortMessage>false</enableShortMessage>
    <primaryKey>269837392450677029</primaryKey>
    <status>ACTIVE</status>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": false, "code": "200", "cost": 5542, "data": { "cellphoneNum": "13269752565", "displayName": "csblcl", "enableDingTalk": true, "roles": [ { "roleRange": "roleRange.allOrganizations", "rAMRole": false, "code": "ROLE_GLOBAL_RESOURCE_AUDITOR", "active": true, "description": "defaultRole.globalResourceAuditor.description", "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.globalResourceAuditor.name", "id": 6, "roleLevel": 2147483647, "organizationVisibility": "organizationVisibility.global" }, { "roleRange": "roleRange.allOrganizations", "rAMRole": false, "code": "ROLE_YUNDUN_PLATSECCONF_ADMIN", "active": true, "description": "defaultRole.yundunPlatSecConfAdmin.description", "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.yundunPlatSecConfAdmin.name", "id": 15, "roleLevel": 2147483647, "organizationVisibility": "organizationVisibility.global" } |   |

`},` `{`

```json
        "roleRange": "roleRange.resourceSet",
        "rAMRole": false,
        "code": "ROLE_RESOURCE_SET_ADMIN",
        "active": true,
        "description": "defaultRole.resourceSetAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.resourceSetAdmin.name",
        "id": 5,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
        "active": true,
        "description": "defaultRole.yundunOrgSecAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunOrgSecAdmin.name",
        "id": 8,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_GLOBALORG_ADMIN",
        "active": true,
        "description": "defaultRole.yundunGlobalOrgAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunGlobalOrgAdmin.name",
        "id": 11,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_PLATSEC_ADMIN",
        "active": true,
        "description": "defaultRole.yundunPlatSecAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunPlatSecAdmin.name",
        "id": 12,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_SECSYSCONF_ADMIN",
        "active": true,
        "description": "defaultRole.yundunSecSysConfAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunSecSysConfAdmin.name",
        "id": 10,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_SEC_AUDITOR",
        "active": true,
        "description": "defaultRole.yundunSecAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunSecAuditor.name",
```

```json
        "id": 9,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_PLATSEC_AUDITOR",
        "active": true,
        "description": "defaultRole.yundunPlatSecAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunPlatSecAuditor.name",
        "id": 14,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "rAMRole": false,
        "code": "ROLE_ORG_RESOURCE_AUDITOR",
        "active": true,
        "description": "defaultRole.orgResourceAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.orgResourceAuditor.name",
        "id": 16,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "rAMRole": false,
        "code": "ROLE_ORGANIZATION_ADMIN",
        "active": true,
        "description": "defaultRole.organizationAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.organizationAdmin.name",
        "id": 4,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.resourceSet",
        "rAMRole": false,
        "code": "ROLE_RESOURCE_USER",
        "active": true,
        "description": "defaultRole.resourceUser.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.resourceUser.name",
        "id": 2,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_GLOBALORGSEC_AUDITOR",
        "active": true,
        "description": "defaultRole.yundunGlobalOrgSecAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunGlobalOrgSecAuditor.name",
        "id": 13,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`],`

```json
    "loginPolicy": {
      "ipRanges": [
```

`{`

```json
          "protocol": "IPV4",
          "ipRange": "0.0.0.0/0",
          "loginPolicyId": 1
```

`],`

```json
      "muserId": "",
      "default": true,
      "ownerOrganizationId": 1,
      "timeRanges": [
```

`{`

```json
          "loginPolicyId": 1,
          "startTime": "00:00",
          "endTime": "24:00"
```

`],`

```json
      "enable": true,
      "name": "defaultLoginPolicy.name",
      "rule": "ALLOW",
      "id": 1,
      "cuserId": "",
      "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
    "parentPk": "1925689189671814",
    "userGroups": [],
    "userRoles": [
```

`{`

```json
        "roleRange": "roleRange.resourceSet",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_RESOURCE_USER",
        "active": true,
        "description": "defaultRole.resourceUser.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.resourceUser.name",
        "id": 2,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_ORGANIZATION_ADMIN",
        "active": true,
        "description": "defaultRole.organizationAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.organizationAdmin.name",
        "id": 4,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.resourceSet",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_RESOURCE_SET_ADMIN",
        "active": true,
        "description": "defaultRole.resourceSetAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.resourceSetAdmin.name",
        "id": 5,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_GLOBAL_RESOURCE_AUDITOR",
        "active": true,
        "description": "defaultRole.globalResourceAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.globalResourceAuditor.name",
        "id": 6,
        "roleLevel": 2147483647,
"cuserId":"",
```

```
        cuserId:
```

`,`

```json
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
        "active": true,
        "description": "defaultRole.yundunOrgSecAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunOrgSecAdmin.name",
        "id": 8,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_SEC_AUDITOR",
        "active": true,
        "description": "defaultRole.yundunSecAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunSecAuditor.name",
        "id": 9,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_SECSYSCONF_ADMIN",
        "active": true,
        "description": "defaultRole.yundunSecSysConfAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunSecSysConfAdmin.name",
        "id": 10,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_GLOBALORG_ADMIN",
        "active": true,
        "description": "defaultRole.yundunGlobalOrgAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunGlobalOrgAdmin.name",
        "id": 11,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_PLATSEC_ADMIN",
        "active": true,
        "description": "defaultRole.yundunPlatSecAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunPlatSecAdmin.name",
        "id": 12,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_GLOBALORGSEC_AUDITOR",
        "active": true,
        "description": "defaultRole.yundunGlobalOrgSecAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunGlobalOrgSecAuditor.name",
        "id": 13,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_PLATSEC_AUDITOR",
        "active": true,
        "description": "defaultRole.yundunPlatSecAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunPlatSecAuditor.name",
        "id": 14,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_PLATSECCONF_ADMIN",
        "active": true,
        "description": "defaultRole.yundunPlatSecConfAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunPlatSecConfAdmin.name",
        "id": 15,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "muserId": "",
        "rAMRole": false,
        "code": "ROLE_ORG_RESOURCE_AUDITOR",
        "active": true,
        "description": "defaultRole.orgResourceAuditor.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.orgResourceAuditor.name",
        "id": 16,
        "roleLevel": 2147483647,
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`],`

```json
    "accessKeys": [
```

`{`

```json
        "ctime": 1592439877000,
        "id": 664,
        "region": "cn-qingdao-****-d01",
        "cuserId": "admin",
        "accesskeyId": "mX7fKY******",
        "status": "ACTIVE"
```

`],`

```json
    "default": false,
    "deleted": false,
    "loginName": "csbuser",
    "organization": {
      "muserId": "",
      "internal": false,
      "supportRegionList": [
```

```
        "cn-qingdao-****-d01"
```

`],`

```json
      "level": "0.1",
      "name": "dataworks_test",
      "alias": "dataworks_test",
      "supportRegions": "cn-qingdao-****-d01",
      "id": 41,
      "cuserId": "",
      "uuid": "41",
      "parentId": 1
```

`},`

```json
    "userGroupRoles": [],
    "id": 5671,
    "mobileNationCode": "86",
    "enableEmail": true,
    "email": "w***@alibaba-inc.com",
    "enableShortMessage": false,
    "primaryKey": "269837392450677029",
    "status": "ACTIVE"
```

`},`

```json
  "success": true,
  "pureListData": false,
  "message": "success"
```

###### 4.3.1.4.2 AddRoleToUser

Binds a role to a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddRoleToUser | The operation that you want to perform. Set the value to AddRoleToUser. |
| LoginName | String | Yes | test | The logon name of the user. |
| RoleId | Integer | Yes | 3 | The ID of the role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddRoleToUser &LoginName=test &RoleId=3 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

###### 4.3.1.4.3 ResetPasswordByLoginName

Resets the password of a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetPasswordByLoginName | The operation that you want to perform. Set the value to ResetPasswordByLoginName. |
| LoginName | String | Yes | testu | The logon name of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | sucess | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ResetPasswordByLoginName &LoginName=testu &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>sucess</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "success": "true", "pureListData": "false", "message": "sucess" } |   |

###### 4.3.1.4.4 GetLoginPolicyByLoginName

Queries the logon policy that is bound to a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | GetLoginPolicyByLoginName | The operation that you want to perform. Set the value to GetLoginPolicyByLoginName. |
|---|---|---|---|---|
| LoginName | String | Yes | testu | The logon name of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| cuserId | String | admin | The creator of the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | defaultLoginPolicy.name | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range for query. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetLoginPolicyByLoginName &LoginName=testu &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <ipRanges> <ipRange>0.0.0.0/0</ipRange> <protocol>IPV4</protocol> <loginPolicyId>1</loginPolicyId> </ipRanges> <muserId>admin</muserId> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1</loginPolicyId> <endTime>24:00</endTime> </timeRanges> <enable>true</enable> <name>defaultLoginPolicy.name</name> <rule>ALLOW</rule> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <lpId>111</lpId> <cuserId>admin</cuserId> </data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "ipRanges": [ { "ipRange": "0.0.0.0/0", "protocol": "IPV4", "loginPolicyId": "1" } ], "muserId": "admin", "default": "true", "ownerOrganizationId": "1", "timeRanges": [ { "startTime": "00:00", "loginPolicyId": "1", "endTime": "24:00" } ], "enable": "true", "name": "defaultLoginPolicy.name", "rule": "ALLOW", "id": "1", "organizationVisibility": "organizationVisibility.global", "lpId": "111", "cuserId": "admin" }, "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.4.5 UpdatePassword

Modifies a password.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | UpdatePassword | The operation that you want to perform. Set the value to UpdatePassword. |
|---|---|---|---|---|
| NewPassword | String | Yes | QAZ2wsx | The new password. The password must comply with the password policy specified by the administrator in the Apsara Uni-manager Operations Console. |
| OldPassword | String | Yes | #EDC4rfv | The current password. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdatePassword &NewPassword=QAZ2wsx &OldPassword=#EDC4rfv &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.4.6 RemoveUserByLoginName

Deletes a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveUserByLoginName | The operation that you want to perform. Set the value to RemoveUserByLoginName. |
| LoginName | String | Yes | testu | The logon name of the user. |
| MultiCloudStatus | String | No | master | Specifies whether the user is a multi-cloud user. Valid values: master and slave. master indicates a primary-cloud user. slave indicates a secondary-cloud user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveUserByLoginName &LoginName=testu &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.4.7 GetUserInfo

Queries the information of a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetUserInfo | The operation that you want to perform. Set the value to GetUserInfo. |
| LoginName | String | No | testu | The logon name of the user. |
| UserAccessKeyId | String | No | test | The AccessKey ID of the user. |
| Pk | String | No | 279319888999990000 | The primary key of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |

| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
|---|---|---|---|
| accesskeySecret | String | ************** | The AccessKey secret. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | 1 | The user who created the AccessKey pair. |
| id | Integer | 1 | The ID of the AccessKey pair. |
| region | String | cn-qingdao-****-d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 11123 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
|---|---|---|---|
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications are sent by DingTalk. |
| enableEmail | Boolean | false | Indicates whether notifications are sent by email. |
| enableShortMessage | Boolean | false | Indicates whether notifications are sent by SMS. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1132111 | The most recent logon time. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | default.loginpolicy | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |

| startTime | String | 00:00 | The start of the time range for the query. |
|---|---|---|---|
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1622311 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 15123222 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
| uuid | String | 123331 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRoles | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |

| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 11213 | The ID of the user group. |
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | group-test | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
| uuid | String | 1231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the storage set was created. |
| id | Integer | 1 | The ID of the resource set. |

| organizationID | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| resourceGroupName | String | restest _ | The name of the resource set. |
| rsId | String | 123121a | The ID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |

| backendAccountType | String | RamUser | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
|---|---|---|---|
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications are sent by DingTalk. |
| enableEmail | Boolean | false | Indicates whether notifications are sent by email. |
| enableShortMessage | Boolean | false | Indicates whether notifications are sent by SMS. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWN****** | The password of the cluster user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1121 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |

| id | Integer | 1 | The ID of the role. |
|---|---|---|---|
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1123 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other fields are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetUserInfo &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <cellphoneNum>00000000000</cellphoneNum> <defaultRole> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>111</arId> <code>ROLE_RESOURCE_USER</code> <description>test</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>role_test</roleName> <roleLevel>11123</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </defaultRole> <enableDingTalk>false</enableDingTalk> <displayName>test</displayName> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>111</arId> <code>ROLE_RESOURCE_USER</code> <description>test</description> <active>true</active> |   |

`/`

```xml
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11321</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
    <loginPolicy>
        <ipRanges>
            <ipRange>0.0.0.0/0</ipRange>
            <protocol>IPV4</protocol>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId>admin</muserId>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <startTime>00:00</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>default.loginpolicy</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>111</lpId>
        <cuserId>admin</cuserId>
    </loginPolicy>
    <parentPk>1689406703302188</parentPk>
    <lastLoginTime>1132111</lastLoginTime>
    <userGroups>
        <organizationId>1</organizationId>
        <createTimeStamp>1606791494471</createTimeStamp>
        <groupName>group-test</groupName>
        <augId>11213</augId>
        <id>1</id>
    </userGroups>
    <userGroups>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>res_test</resourceGroupName>
            <gmtCreated>1606791494471</gmtCreated>
            <rsId>123121a</rsId>
            <id>1</id>
        </resourceSets>
        <users>
            <muserId>admin</muserId>
            <backendAccountType>RamUser</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <mtime>1606791494471</mtime>
            <organizationId>1</organizationId>
            <password>H2xW******</password>
            <default>false</default>
            <loginTime>1606791494471</loginTime>
            <userLoginCtrlId>34</userLoginCtrlId>
            <loginName>test</loginName>
            <ctime>1606791494471</ctime>
            <id>1</id>
            <enableShortMessage>false</enableShortMessage>
            <email>t***@163.com</email>
            <defaultRoleId>1</defaultRoleId>
            <cellphoneNum>00000000000</cellphoneNum>
            <aliyunUser>false</aliyunUser>
            <accountType>1</accountType>
            <active>true</active>
            <deleted>false</deleted>
            <mobileNationCode>86</mobileNationCode>
            <ramUser>true</ramUser>
            <enableEmail>false</enableEmail>
            <username>test</username>
        </users>
        <roles>
            <roleRange>roleRange.orgAndSubOrgs</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>1231</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>role_test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>true</default>
<ownerOrganizationId>1</ownerOrganizationId>
```

```xml
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>role_test</roleName>
            <roleLevel>1231</roleLevel>
            <id>1</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
    </userGroups>
    <userGroups>
        <organization>
            <muserId>admin</muserId>
            <internal>false</internal>
            <level>0.1</level>
            <supportRegions>cn-qingdao-****-d01</supportRegions>
            <mtime>1606791494471</mtime>
            <uuid>1231</uuid>
            <parentId>0</parentId>
            <multiCloudStatus>master</multiCloudStatus>
            <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
            <name>test</name>
            <ctime>1606791494471</ctime>
            <alias>test</alias>
            <id>1</id>
            <cuserId>admin</cuserId>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>1121</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>1123</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <default>false</default>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-qingdao-****-d01</region>
        <accesskeySecret>**************</accesskeySecret>
        <cuserId>1</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>JGdgSN2p******</accesskeyId>
    </accessKeys>
    <deleted>false</deleted>
    <loginName>test</loginName>
    <organization>
        <muserId>admin</muserId>
        <internal>false</internal>
        <level>0.1</level>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <mtime>15123222</mtime>
        <uuid>123331</uuid>
        <parentId>0</parentId>
        <multiCloudStatus>master</multiCloudStatus>
        <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
        <name>test</name>
        <ctime>1622311</ctime>
        <alias>test</alias>
        <id>1</id>
        <cuserId>admin</cuserId>
    </organization>
    <userGroupRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11321</roleLevel>
```

`/`

```xml
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>false</enableEmail>
    <enableShortMessage>false</enableShortMessage>
    <email>t***@163.com</email>
    <status>ACTIVE</status>
    <primaryKey>212530506704030466</primaryKey>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "cellphoneNum": "00000000000", "defaultRole": { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "muserId": "admin", "arId": "111", "code": "ROLE_RESOURCE_USER", "description": "test", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "ownerOrganizationId": "1", "enable": "true", "roleName": "role_test", "roleLevel": "11123", "id": "1", "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" }, "enableDingTalk": "false", "displayName": "test", "roles": [ { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "muserId": "admin", "arId": "111", "code": "ROLE_RESOURCE_USER", "description": "test", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "ownerOrganizationId": "1", "enable": "true", "roleName": "role_test", "roleLevel": "11321", "id": "1", "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" } ], "loginPolicy": { "ipRanges": [ { "ipRange": "0.0.0.0/0", "protocol": "IPV4", "loginPolicyId": "1" } ], "muserId": "admin", "default": "true", "ownerOrganizationId": "1", "timeRanges": [ { "startTime": "00:00", "loginPolicyId": "1", "endTime": "24:00" } ], "enable": "true", "name": "default.loginpolicy", "rule": "ALLOW", "id": "1", "organizationVisibility": "organizationVisibility global" |   |

```json
            organizationVisibility: organizationVisibility.global,
            "lpId": "111",
            "cuserId": "admin"
```

`},`

```json
        "parentPk": "1689406703302188",
        "lastLoginTime": "1132111",
        "userGroups": [
```

`{`

```json
                "organizationId": "1",
                "createTimeStamp": "1606791494471",
                "groupName": "group-test",
                "augId": "11213",
                "id": "1"
```

`},` `{`

```json
                "resourceSets": [
```

`{`

```json
                        "organizationID": "1",
                        "creator": "admin",
                        "resourceGroupName": "res_test",
                        "gmtCreated": "1606791494471",
                        "rsId": "123121a",
                        "id": "1"
```

`],`

```json
                "users": [
```

`{`

```json
                        "muserId": "admin",
                        "backendAccountType": "RamUser",
                        "enableDingTalk": "false",
                        "mtime": "1606791494471",
                        "organizationId": "1",
                        "password": "H2xW******",
                        "default": "false",
                        "loginTime": "1606791494471",
                        "userLoginCtrlId": "34",
                        "loginName": "test",
                        "ctime": "1606791494471",
                        "id": "1",
                        "enableShortMessage": "false",
                        "email": "t***@163.com",
                        "defaultRoleId": "1",
                        "cellphoneNum": "00000000000",
                        "aliyunUser": "false",
                        "accountType": "1",
                        "active": "true",
                        "deleted": "false",
                        "mobileNationCode": "86",
                        "ramUser": "true",
                        "enableEmail": "false",
                        "username": "test"
```

`],`

```json
                "roles": [
```

`{`

```json
                        "roleRange": "roleRange.orgAndSubOrgs",
                        "rAMRole": "false",
                        "muserId": "admin",
                        "arId": "1231",
                        "code": "ROLE_RESOURCE_USER",
                        "description": "role_test",
                        "active": "true",
                        "roleType": "ROLETYPE_ASCM",
                        "default": "true",
                        "ownerOrganizationId": "1",
                        "enable": "true",
                        "roleName": "role_test",
                        "roleLevel": "1231",
                        "id": "1",
                        "organizationVisibility": "organizationVisibility.global",
                        "cuserId": "admin"
```

`]` `},` `{`

```json
                "organization": {
                    "muserId": "admin",
                    "internal": "false",
                    "level": "0.1",
                    "supportRegions": "cn-qingdao-****-d01",
                    "mtime": "1606791494471",
                    "uuid": "1231",
                    "parentId": "0",
                    "multiCloudStatus": "master",
                    "supportRegionList": "[\"cn-qingdao-****-d01\"]",
                    "name": "test",
                    "ctime": "1606791494471",
"li
```

`"` `"` `"`

```json
                    "alias": "test",
                    "id": "1",
                    "cuserId": "admin"
```

`],`

```json
        "userRoles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "1121",
                "code": "ROLE_RESOURCE_USER",
                "description": "role_test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "defaultRole.resourceUser.name",
                "roleLevel": "1123",
                "id": "1",
                "organizationVisibility": "defaultRole.resourceUser.description",
                "cuserId": "admin"
```

`],`

```json
        "default": "false",
        "accessKeys": [
```

`{`

```json
                "ctime": "1606675230000",
                "id": "1",
                "region": "cn-qingdao-****-d01",
                "accesskeySecret": "**************",
                "cuserId": "1",
                "status": "ACTIVE",
                "accesskeyId": "JGdgSN2p******"
```

`],`

```json
        "deleted": "false",
        "loginName": "test",
        "organization": {
            "muserId": "admin",
            "internal": "false",
            "level": "0.1",
            "supportRegions": "cn-qingdao-****-d01",
            "mtime": "15123222",
            "uuid": "123331",
            "parentId": "0",
            "multiCloudStatus": "master",
            "supportRegionList": "[\"cn-qingdao-****-d01\"]",
            "name": "test",
            "ctime": "1622311",
            "alias": "test",
            "id": "1",
            "cuserId": "admin"
```

`},`

```json
        "userGroupRoles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "111",
                "code": "ROLE_RESOURCE_USER",
                "description": "role_test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11321",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`],`

```json
        "mobileNationCode": "86",
        "id": "1",
        "enableEmail": "false",
        "enableShortMessage": "false",
        "email": "t***@163.com",
        "status": "ACTIVE",
        "primaryKey": "212530506704030466"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

###### 4.3.1.4.8 ListUsers

Queries the list of available users.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUsers | The operation that you want to perform. Set the value to ListUsers. |
| LoginName | String | No | test | The logon name of the user. |
| RoleId | Integer | No | 2 | The ID of the role. |
| LoginPolicyId | Integer | No | 1 | The ID of the logon policy. |
| OrganizationId | Integer | No | 3 | The ID of the organization. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 188 | The amount of time taken to perform the operation. Unit: ms. |
| data | Array of dataItem |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | 5013 | The user who created the AccessKey pair. |
| id | Integer | 1 | The AccessKey ID. |
| region | String | cn-**-d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 188*****188 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |

| enable | Boolean | true | Indicates whether the role is valid. |
|---|---|---|---|
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | usertest _ | The display name of the user. |
| email | String | xxx@alibaba-inc.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1606675230000 | The most recent logon time. |
| loginName | String | usertest _ | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | false | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0 | The CIDR block. |

| ference |   |   |   |
|---|---|---|---|

| loginPolicyId | Integer | 1 | The ID of the logon policy. |
|---|---|---|---|
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | policytest _ | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00.00 | The start of the time range for the query. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1607512443989 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegionList | List | cn-***-d01 | The list of regions. |
| supportRegions | String | ["cn-***-d01"] | The list of regions. |

| uuid | String | 123456 | The universally unique identifier (UUID) of the organization. |
|---|---|---|---|
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 111 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRoles | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |

| default | Boolean | true | Indicates whether the role is a preset role. |
|---|---|---|---|
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 111 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 1111 | The ID of the user group. |
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | ack-user-old | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 123 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |

| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
|---|---|---|---|
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegionList | List | cn-**-d01 | The list of regions. |
| supportRegions | String | ["cn-**-d01"] | The list of regions. |
| uuid | String | 123456 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | resourcetest _ | The name of the resource set. |
| rsId | String | 123456 | The ID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123456 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1231 | The level of the role. |

| roleName | String | defaultRole.resourceUser.name | The name of the role. |
|---|---|---|---|
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | RamUser | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | true | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | xxx@alibaba-inc.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xW****** | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |

| userLoginCtrlId | Integer | 34 | The ID of the logon control. |
|---|---|---|---|
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 123 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 39 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |

| ference |   |   |   |
|---|---|---|---|

| redirect | Boolean | false | Indicates whether redirections are performed. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListUsers &<Common request parameters>
```

Sample success response

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>188</cost> <code>200</code> <data> <cellphoneNum>188*****188</cellphoneNum> <enableDingTalk>false</enableDingTalk> <displayName>user_test</displayName> <parentPk>1689406703302188</parentPk> <lastLoginTime>1606675230000</lastLoginTime> <default>false</default> <deleted>false</deleted> <loginName>user_test</loginName> <mobileNationCode>86</mobileNationCode> <id>1</id> <enableEmail>false</enableEmail> <enableShortMessage>false</enableShortMessage> <email>xxx@alibaba-inc.com</email> <status>ACTIVE</status> <primaryKey>212530506704030466</primaryKey> </data> <data> <userGroupRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>111</arId> <code>ROLE_RESOURCE_USER</code> <description>test</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>role_test</roleName> <roleLevel>111</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </userGroupRoles> <userGroups> <organizationId>1</organizationId> <createTimeStamp>1606791494471</createTimeStamp> <groupName>ack-user-old</groupName> <augId>1111</augId> <id>1</id> </userGroups> <userGroups> <resourceSets> <organizationID>1</organizationID> <creator>admin</creator> <resourceGroupName>resource_test</resourceGroupName> <gmtCreated>1606791494471</gmtCreated> <rsId>123456</rsId> <id>1</id> </resourceSets> <users> <muserId>admin</muserId> <backendAccountType>RamUser</backendAccountType> <enableDingTalk>false</enableDingTalk> <mtime>1606791494471</mtime> <organizationId>1</organizationId> <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password> <default>true</default> <loginTime>1606791494471</loginTime> <userLoginCtrlId>34</userLoginCtrlId> <loginName>test</loginName> <ctime>1606791494471</ctime> |   |

```xml
            <ctime>1606791494471</ctime>
            <id>1</id>
            <enableShortMessage>false</enableShortMessage>
            <email>xxx@alibaba-inc.com</email>
            <defaultRoleId>1</defaultRoleId>
            <cellphoneNum>00000000000</cellphoneNum>
            <aliyunUser>false</aliyunUser>
            <accountType>1</accountType>
            <active>true</active>
            <deleted>false</deleted>
            <mobileNationCode>86</mobileNationCode>
            <ramUser>true</ramUser>
            <enableEmail>false</enableEmail>
            <username>test</username>
        </users>
        <roles>
            <roleRange>roleRange.orgAndSubOrgs</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>123456</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>true</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>defaultRole.resourceUser.name</roleName>
            <roleLevel>1231</roleLevel>
            <id>1</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
    </userGroups>
    <userGroups>
        <organization>
            <muserId>admin</muserId>
            <internal>true</internal>
            <level>123</level>
            <supportRegions>["cn-**-d01"]</supportRegions>
            <mtime>1606791494471</mtime>
            <uuid>123456</uuid>
            <parentId>1</parentId>
            <multiCloudStatus>master</multiCloudStatus>
            <supportRegionList>cn-**-d01</supportRegionList>
            <name>test</name>
            <ctime>1606791494471</ctime>
            <alias>test</alias>
            <id>1</id>
            <cuserId>admin</cuserId>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>1111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>123</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-**-d01</region>
        <cuserId>5013</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>JGdgSN2p******</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
<df lt>t </df lt>
```

```xml
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>111</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
</data> <data>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <ipRanges>
            <ipRange>0.0.0.0</ipRange>
            <protocol>IPV4</protocol>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId>admin</muserId>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <startTime>00.00</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>policy_test</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>111</lpId>
        <cuserId>admin</cuserId>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>true</internal>
        <level>0.1</level>
        <supportRegions>["cn-***-d01"]</supportRegions>
        <mtime>1606791494471</mtime>
        <uuid>123456</uuid>
        <parentId>1</parentId>
        <multiCloudStatus>master</multiCloudStatus>
        <supportRegionList>cn-***-d01</supportRegionList>
        <name>test</name>
        <ctime>1607512443989</ctime>
        <alias>test</alias>
        <id>1</id>
        <cuserId>admin</cuserId>
    </organization>
</data> <success>true</success> <pageInfo>
    <total>39</total>
    <totalPage>2</totalPage>
    <pageSize>20</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "188", "code": "200", "data": [ { "cellphoneNum": "188*****188", "enableDingTalk": "false", |   |

```json
            enableDingTalk: false,
            "displayName": "user_test",
            "parentPk": "1689406703302188",
            "lastLoginTime": "1606675230000",
            "default": "false",
            "deleted": "false",
            "loginName": "user_test",
            "mobileNationCode": "86",
            "id": "1",
            "enableEmail": "false",
            "enableShortMessage": "false",
            "email": "xxx@alibaba-inc.com",
            "status": "ACTIVE",
            "primaryKey": "212530506704030466"
```

`},` `{`

```json
            "userGroupRoles": [
```

`{`

```json
                    "roleRange": "roleRange.orgAndSubOrgs",
                    "rAMRole": "false",
                    "muserId": "admin",
                    "arId": "111",
                    "code": "ROLE_RESOURCE_USER",
                    "description": "test",
                    "active": "true",
                    "roleType": "ROLETYPE_ASCM",
                    "default": "true",
                    "ownerOrganizationId": "1",
                    "enable": "true",
                    "roleName": "role_test",
                    "roleLevel": "111",
                    "id": "1",
                    "organizationVisibility": "organizationVisibility.global",
                    "cuserId": "admin"
```

`],`

```json
            "userGroups": [
```

`{`

```json
                    "organizationId": "1",
                    "createTimeStamp": "1606791494471",
                    "groupName": "ack-user-old",
                    "augId": "1111",
                    "id": "1"
```

`},` `{`

```json
                    "resourceSets": [
```

`{`

```json
                            "organizationID": "1",
                            "creator": "admin",
                            "resourceGroupName": "resource_test",
                            "gmtCreated": "1606791494471",
                            "rsId": "123456",
                            "id": "1"
```

`],`

```json
                    "users": [
```

`{`

```json
                            "muserId": "admin",
                            "backendAccountType": "RamUser",
                            "enableDingTalk": "false",
                            "mtime": "1606791494471",
                            "organizationId": "1",
                            "password": "H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS",
                            "default": "true",
                            "loginTime": "1606791494471",
                            "userLoginCtrlId": "34",
                            "loginName": "test",
                            "ctime": "1606791494471",
                            "id": "1",
                            "enableShortMessage": "false",
                            "email": "xxx@alibaba-inc.com",
                            "defaultRoleId": "1",
                            "cellphoneNum": "00000000000",
                            "aliyunUser": "false",
                            "accountType": "1",
                            "active": "true",
                            "deleted": "false",
                            "mobileNationCode": "86",
                            "ramUser": "true",
                            "enableEmail": "false",
                            "username": "test"
```

`],`

```json
                    "roles": [
```

`{`

```json
                            "roleRange": "roleRange.orgAndSubOrgs",
                            "rAMRole": "false",
"mserId" "admin"
```

```json
                            "muserId": "admin",
                            "arId": "123456",
                            "code": "ROLE_RESOURCE_USER",
                            "description": "test",
                            "active": "true",
                            "roleType": "ROLETYPE_ASCM",
                            "default": "true",
                            "ownerOrganizationId": "1",
                            "enable": "true",
                            "roleName": "defaultRole.resourceUser.name",
                            "roleLevel": "1231",
                            "id": "1",
                            "organizationVisibility": "organizationVisibility.global",
                            "cuserId": "admin"
```

`]` `},` `{`

```json
                    "organization": {
                        "muserId": "admin",
                        "internal": "true",
                        "level": "123",
                        "supportRegions": "[\"cn-**-d01\"]",
                        "mtime": "1606791494471",
                        "uuid": "123456",
                        "parentId": "1",
                        "multiCloudStatus": "master",
                        "supportRegionList": "cn-**-d01",
                        "name": "test",
                        "ctime": "1606791494471",
                        "alias": "test",
                        "id": "1",
                        "cuserId": "admin"
```

`],`

```json
            "userRoles": [
```

`{`

```json
                    "roleRange": "roleRange.orgAndSubOrgs",
                    "rAMRole": "false",
                    "muserId": "admin",
                    "arId": "1111",
                    "code": "ROLE_RESOURCE_USER",
                    "description": "test",
                    "active": "true",
                    "roleType": "ROLETYPE_ASCM",
                    "default": "true",
                    "ownerOrganizationId": "1",
                    "enable": "true",
                    "roleName": "defaultRole.resourceUser.name",
                    "roleLevel": "123",
                    "id": "1",
                    "organizationVisibility": "defaultRole.resourceUser.description",
                    "cuserId": "admin"
```

`],`

```json
            "accessKeys": [
```

`{`

```json
                    "ctime": "1606675230000",
                    "id": "1",
                    "region": "cn-**-d01",
                    "cuserId": "5013",
                    "status": "ACTIVE",
                    "accesskeyId": "JGdgSN2p******"
```

`],`

```json
            "roles": [
```

`{`

```json
                    "roleRange": "roleRange.orgAndSubOrgs",
                    "rAMRole": "false",
                    "muserId": "admin",
                    "arId": "111",
                    "code": "ROLE_RESOURCE_USER",
                    "description": "test",
                    "active": "true",
                    "roleType": "ROLETYPE_ASCM",
                    "default": "true",
                    "ownerOrganizationId": "1",
                    "enable": "true",
                    "roleName": "role_test",
                    "roleLevel": "111",
                    "id": "1",
                    "organizationVisibility": "organizationVisibility.global",
                    "cuserId": "admin"
```

`]` `},` `{`

```json
            "defaultRole": {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "111",
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "1",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
            "loginPolicy": {
                "ipRanges": [
```

`{`

```json
                        "ipRange": "0.0.0.0",
                        "protocol": "IPV4",
                        "loginPolicyId": "1"
```

`],`

```json
                "muserId": "admin",
                "default": "false",
                "ownerOrganizationId": "1",
                "timeRanges": [
```

`{`

```json
                        "startTime": "00.00",
                        "loginPolicyId": "1",
                        "endTime": "24:00"
```

`],`

```json
                "enable": "true",
                "name": "policy_test",
                "rule": "ALLOW",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "lpId": "111",
                "cuserId": "admin"
```

`},`

```json
            "organization": {
                "muserId": "admin",
                "internal": "true",
                "level": "0.1",
                "supportRegions": "[\"cn-***-d01\"]",
                "mtime": "1606791494471",
                "uuid": "123456",
                "parentId": "1",
                "multiCloudStatus": "master",
                "supportRegionList": "cn-***-d01",
                "name": "test",
                "ctime": "1607512443989",
                "alias": "test",
                "id": "1",
                "cuserId": "admin"
```

`],`

```json
    "success": "true",
    "pageInfo": {
        "total": "39",
        "totalPage": "2",
        "pageSize": "20",
        "currentPage": "1"
```

`},`

```json
    "pureListData": "false",
    "message": "success"
```

###### 4.3.1.4.9 ActivateUser

Activates a user. When a user is activated, all AccessKey pairs of the user are activated. This operation is supported by Apsara Stack Enterprise Edition V3.12.0 SP016 or later. This operation is supported by Apsara Stack Enterprise Edition V3.14.0 SP013 or later.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/activateUser HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | test | The logon name of the user. |
| multiCloudStatus | String | Body | No | master | The multi-cloud status of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| data | Struct |   | The response data. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | 1 | The AccessKey ID. |
| ctime | Long | 123141313 | The time when the AccssKey pair of the user was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID. |
| region | String | cn-qingdao-env17-d01 | The zone. |
| status | String | ACTIVE | The state. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11 | The level of the role. |
| roleName | String | name | The name of the role. |

| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
|---|---|---|---|
| roleType | String | ROLETYPEASCM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | xx@xx.com | The email address of the user. |
| enableDingTalk | Boolean | true | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | true | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | true | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 16341341514 | The time when the user last logged on. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The creator. |
| default | Boolean | false | Indicates whether the policy is a preset policy. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks that are used to log on to the Apsara Uni- manager Management Console. |
| ipRange | String | 0.0.0.0/0 | The CIDR block that is used to log on to the Apsara Uni-manager Management Console. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 123 | The UUID of the logon policy. |
| muserId | String | admin | The modifier. |
| name | String | testpolicy _ | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The type of the logon policy. Allow: whitelist Deny: blacklist |

| timeRanges | Array of timeRange |   | The list of time ranges. |
|---|---|---|---|
| endTime | String | 24:00 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range queried. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1231244123123 | The time when the organization to which the user belongs was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 23124231234123 | The time when the organization to which the user belongs was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | [cn-qingdao-env17-d01] | The list of zones. |
| supportRegions | String | cn-qingdao-env17-d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-111 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | desc | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |

| muserId | String | admin | The modifier. |
|---|---|---|---|
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| status | String | ACTIVE | The state of the user. active inactive |
| userGroupRoles | Array of userGroupRole |   | The list of roles for the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-12323 | The UUID of the role. |
| code | String | test | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | desc | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM, ROLETYPEASCM, _ _ and ROLETYPERAMROLEAUTHORIZATION. ROLETYPERAM specifies a _ _ RAM role. ROLETYPEASCM specifies a preset or custom role. _ ROLETYPERAMROLEAUTHORIZATION specifies a RAM role-based batch _ authorization role. |
| userGroups | Array of userGroup |   | The list of user groups. |

| augId | String | 123 | The UUID of the user group. |
|---|---|---|---|
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | test | The name of the user group. |
| id | Integer | 2 | The ID of the user group. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization to which the user group belongs was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 2 | The ID. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization to which the user group belongs was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | The list of zones. |
| supportRegions | String | cn-qingdao-env17-d01 | The list of zones. |
| uuid | String | 23123 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 2 | The ID. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | test | The name of the resource set. |
| rsId | String | 123 | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |

| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
|---|---|---|---|
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 123 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPERAM _ | The type of the role. |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the logon policy is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | RamUser | The type of the account that is mapped in the backend. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1011 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | xx@xx.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 2 | The ID of the user. |
| loginName | String | aaa | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |

| mobileNationCode | String | 86 | The country code. |
|---|---|---|---|
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The modifier. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxMWLhtyjsO1fRkY oCRcErAgP9Hd0IXp2f5rRSmArS | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 12 | This parameter is deprecated. |
| username | String | aaa | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles for the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | desctest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |

| success | Boolean | true | Indicates whether the call is successful. |
|---|---|---|---|

**Examples**

Sample requests

```
POST /ascm/auth/user/activateUser HTTP/1.1 Common request headers
```

`{`

```json
"LoginName": "test"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <cellphoneNum>18888888888</cellphoneNum> <enableDingTalk>true</enableDingTalk> <displayName>test</displayName> <parentPk>1689406703302188</parentPk> <lastLoginTime>16341341514</lastLoginTime> <default>false</default> <deleted>false</deleted> <loginName>test</loginName> <mobileNationCode>86</mobileNationCode> <id>1</id> <enableEmail>true</enableEmail> <enableShortMessage>true</enableShortMessage> <email>xx@xx.com</email> <status>ACTIVE</status> <primaryKey>212530506704030466</primaryKey> <userGroupRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>true</rAMRole> <muserId>admin</muserId> <arId>ar-12323</arId> <code>test</code> <description>desc</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>false</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>test</roleName> <roleLevel>1</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </userGroupRoles> <userGroups> <organizationId>1</organizationId> <groupName>test</groupName> <augId>123</augId> <createTimeStamp>1606791494471</createTimeStamp> <id>2</id> <resourceSets> <organizationID>1</organizationID> <creator>admin</creator> <resourceGroupName>test</resourceGroupName> <gmtCreated>1606791494471</gmtCreated> <rsId>123</rsId> <id>2</id> </resourceSets> <users> <cellphoneNum>18888888888</cellphoneNum> <muserId>admin</muserId> <aliyunUser>false</aliyunUser> <backendAccountType>RamUser</backendAccountType> <enableDingTalk>false</enableDingTalk> <accountType>1</accountType> <active>true</active> <mtime>1606791494471</mtime> <organizationId>1</organizationId> <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password> <default>false</default> <loginTime>1606791494471</loginTime> <deleted>false</deleted> <userLoginCtrlId>12</userLoginCtrlId> <loginName>aaa</loginName> <ctime>1606791494471</ctime> <mobileNationCode>86</mobileNationCode> <id>2</id> |   |

```xml
            <ramUser>true</ramUser>
            <enableEmail>false</enableEmail>
            <enableShortMessage>false</enableShortMessage>
            <email>xx@xx.com</email>
            <defaultRoleId>1011</defaultRoleId>
            <username>aaa</username>
        </users>
        <roles>
            <roleRange>roleRange.orgAndSubOrgs</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>123</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>test</description>
            <active>true</active>
            <roleType>ROLETYPE_RAM</roleType>
            <default>false</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>test</roleName>
            <roleLevel>123</roleLevel>
            <id>1</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
        <organization>
            <muserId>admin</muserId>
            <internal>true</internal>
            <multiCloudStatus>master</multiCloudStatus>
            <level>0.1</level>
            <name>test</name>
            <supportRegions>cn-qingdao-env17-d01</supportRegions>
            <ctime>1606791494471</ctime>
            <alias>test</alias>
            <id>2</id>
            <mtime>1606791494471</mtime>
            <uuid>23123</uuid>
            <cuserId>admin</cuserId>
            <parentId>1</parentId>
            <supportRegionList>["cn-qingdao-env17-d01"]</supportRegionList>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>true</rAMRole>
        <muserId>admin</muserId>
        <arId>123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>desc_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>name</roleName>
        <roleLevel>2</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>123141313</ctime>
        <id>1</id>
        <region>cn-qingdao-env17-d01</region>
        <cuserId>admin</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>1</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>true</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>desc</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>name</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
<defaultRole>
```

```xml
deautoe
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>name</roleName>
        <roleLevel>11</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <muserId>admin</muserId>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <name>test_policy</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>123</lpId>
        <cuserId>admin</cuserId>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <timeRanges>
            <startTime>00:00</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>24:00</endTime>
        </timeRanges>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>true</internal>
        <multiCloudStatus>master</multiCloudStatus>
        <level>0.1</level>
        <name>test</name>
        <supportRegions>cn-qingdao-env17-d01</supportRegions>
        <ctime>1231244123123</ctime>
        <alias>test</alias>
        <id>1</id>
        <mtime>23124231234123</mtime>
        <uuid>1231</uuid>
        <cuserId>admin</cuserId>
        <parentId>0</parentId>
        <supportRegionList>[cn-qingdao-env17-d01]</supportRegionList>
    </organization>
</data> <success>true</success> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"cellphoneNum":"18888888888","enableDingTalk":"true","displayName":"test","parentPk":"1689406703302188","lastLoginTime":"16341341514","default" se","deleted":"false","loginName":"test","mobileNationCode":"86","id":"1","enableEmail":"true","enableShortMessage":"true","email":"xx@xx.com","s s":"ACTIVE","primaryKey":"212530506704030466","userGroupRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar- 12323","code":"test","description":"desc","active":"true","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"true" eName":"test","roleLevel":"1","id":"1","organizationVisibility":"organizationVisibility.global","cuserId":"admin"}],"userGroups": [{"organizationId":"1","groupName":"test","augId":"123","createTimeStamp":"1606791494471","id":"2","resourceSets": [{"organizationID":"1","creator":"admin","resourceGroupName":"test","gmtCreated":"1606791494471","rsId":"123","id":"2"}],"users": [{"cellphoneNum":"18888888888","muserId":"admin","aliyunUser":"false","backendAccountType":"RamUser","enableDingTalk":"false","accountType":"1", ve":"true","mtime":"1606791494471","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS","default":"false","log me":"1606791494471","deleted":"false","userLoginCtrlId":"12","loginName":"aaa","ctime":"1606791494471","mobileNationCode":"86","id":"2","ramUser ue","enableEmail":"false","enableShortMessage":"false","email":"xx@xx.com","defaultRoleId":"1011","username":"aaa"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123","code":"ROLE_RESOURCE_USER","description":"test","active rue","roleType":"ROLETYPE_RAM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":"123","id":"1","organiza Visibility":"organizationVisibility.global","cuserId":"admin"}],"organization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"0.1","name":"test","supportRegions":"cn-qingdao-env17d01","ctime":"1606791494471","alias":"test","id":"2","mtime":"1606791494471","uuid":"23123","cuserId":"admin","parentId":"1","supportRegionList" [\"cn-qingdao-env17-d01\"]"}}],"userRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"123","code":"ROLE_RESOURCE_USER","description":"desc_test","ac ":"true","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"name","roleLevel":"2","id":"1","organ ionVisibility":"defaultRole.resourceUser.description","cuserId":"admin"}],"accessKeys":[{"ctime":"123141313","id":"1","region":"cn-qingdaoenv17-d01","cuserId":"admin","status":"ACTIVE","accesskeyId":"1"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar- 111","code":"ROLE_RESOURCE_USER","description":"desc","active":"true","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","ena :"true","roleName":"name","roleLevel":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cuserId":"admin"}],"defaultRo {"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"ar- 123","code":"ROLE_RESOURCE_USER","description":"role_test","active":"true","roleType":"ROLETYPE_ASCM","default":"true","ownerOrganizationId":"1" ble":"true","roleName":"name","roleLevel":"11","id":"1","organizationVisibility":"defaultRole.resourceUser.description"},"loginPolicy": {"muserId":"admin","default":"false","ownerOrganizationId":"1","enable":"true","name":"test_policy","rule":"ALLOW","id":"1","organizationVisibili "organizationVisibility.global","lpId":"123","cuserId":"admin","ipRanges": [{"protocol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"}],"timeRanges": [{"startTime":"00:00","loginPolicyId":"1","endTime":"24:00"}]},"organization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"0.1","name":"test","supportRegions":"cn-qingdao-env17d01","ctime":"1231244123123","alias":"test","id":"1","mtime":"23124231234123","uuid":"1231","cuserId":"admin","parentId":"0","supportRegionList" [cn-qingdao-env17-d01]"}},"success":"true","pureListData":"true","message":"success"}
```

###### 4.3.1.4.10 ListDeletedUsers

Queries the list of deleted users.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDeletedUsers | The operation that you want to perform. Set the value to ListDeletedUsers. |
| LoginName | String | No | testu | The logon name of the user. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| dataItem |   |   |   |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| deleted | Boolean | true | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |

| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
|---|---|---|---|
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1231212 | The most recent logon time. |
| loginName | String | test | The logon name of the user. |
| mobileNationCode | String | 86 | The country code. |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 2 | The total number of entries returned. |
| totalPage | Integer | 39 | The total number of pages. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListDeletedUsers &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <cellphoneNum>00000000000</cellphoneNum> <enableDingTalk>false</enableDingTalk> <displayName>test</displayName> <lastLoginTime>1231212</lastLoginTime> <default>false</default> <deleted>true</deleted> <loginName>test</loginName> <mobileNationCode>86</mobileNationCode> <id>1</id> <enableEmail>false</enableEmail> <enableShortMessage>false</enableShortMessage> <email>t***@163.com</email> <status>ACTIVE</status> </data> <success>true</success> <pageInfo> <total>2</total> <totalPage>39</totalPage> <pageSize>20</pageSize> <currentPage>1</currentPage> </pageInfo> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": [ { "cellphoneNum": "00000000000", "enableDingTalk": "false", "displayName": "test", "lastLoginTime": "1231212", "default": "false", "deleted": "true", "loginName": "test", "mobileNationCode": "86", "id": "1", "enableEmail": "false", "enableShortMessage": "false", "email": "t***@163.com", "status": "ACTIVE" } ], "success": "true", "pageInfo": { "total": "2", "totalPage": "39", "pageSize": "20", "currentPage": "1" }, "pureListData": "false", "message": "success" } |   |

###### 4.3.1.4.11 ListResourceGroupByAscmUserId

Queries the list of resource sets of a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceGroupByAscmUs erId | The operation that you want to perform. Set the value to ListResourceGroupByAscmUserId. |
| ascmuserid _ | Integer | Yes | 5 | The ID of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 12314 | The time when the resource set was created. |
| gmtModified | Long | 12314 | The time when the resource set was modified. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | test | The name of the resource set. |
| resourceGroupType | Integer | 1 | The type of the resource set. 1 indicates the default resource set. If you leave this parameter empty, all the resource sets other than the default one are specified. |
| rsId | String | rs-123144 | The ID of the resource set. |

| message | String | success | The error message. |
|---|---|---|---|
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListResourceGroupByAscmUserId &ascmuser_id=5 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <organizationID>1</organizationID> <gmtModified>12314</gmtModified> <creator>admin</creator> <resourceGroupName>test</resourceGroupName> <gmtCreated>12314</gmtCreated> <rsId>rs-123144</rsId> <resourceGroupType>1</resourceGroupType> <id>1</id> </data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": [ { "organizationID": "1", "gmtModified": "12314", "creator": "admin", "resourceGroupName": "test", "gmtCreated": "12314", "rsId": "rs-123144", "resourceGroupType": "1", "id": "1" } ], "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.4.12 ModifyUserInformation

Modifies the information of a user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyUserInformation | The operation that you want to perform. Set the value to ModifyUserInformation. |
| Id | Integer | No | 100 | The ID of the user. |
| LoginName | String | No | test | The logon name of the user. |
| DisplayName | String | No | test | The display name of the user. |

| LoginPolicyId | Integer | No | 100 | The ID of the logon policy. |
|---|---|---|---|---|
| MobileNationCode | String | No | test | The country code. |
| CellphoneNum | String | No | 12345678 | The mobile number of the user. |
| TelephoneNum | String | No | 12345678 | The landline number of the user. |
| Email | String | No | e***@test.com | The email address of the user. |
| Description | String | No | test | The description of the user. |
| DingTalkToken | String | No | abc123 | The DingTalk token. |
| EnableDingTalk | Boolean | No | false | Specifies whether to use DingTalk to send notifications. |
| EnableShortMessage | Boolean | No | false | Specifies whether to use SMS to send notifications. |
| EnableEmail | Boolean | No | false | Specifies whether to use emails to send notifications. |
| MultiCloudStatus | String | No | master | Specifies whether the user is a multi-cloud user. Valid values: master and slave. master indicates a primary-cloud user. slave indicates a secondary-cloud user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | admin | The user who created the AccessKey pair. |
| id | Integer | 1 | The ID of the AccessKey pair. |
| region | String | cn-qingdao-****-d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | The status of the AccessKey pair. Valid values: active and inactive. |
| cellphoneNum | String | 0000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |

| enable | Boolean | true | Indicates whether the role is valid. |
|---|---|---|---|
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates RAM roles. _ _ ROLETYPEASCM indicates custom roles. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1606675230000 | The most recent logon time. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |

| ference |   |   |   |
|---|---|---|---|

| loginPolicyId | Integer | 1 | The ID of the logon policy. |
|---|---|---|---|
| protocol | String | IPV4 | The protocol. |
| lpId | String | 11213 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | default.loginpolicy | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the organization. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
| uuid | String | 11231 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |

| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
|---|---|---|---|
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admmin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates RAM roles. _ _ ROLETYPEASCM indicates custom roles. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRoles | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |

| enable | Boolean | true | Indicates whether the role is valid. |
|---|---|---|---|
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates RAM roles. _ _ ROLETYPEASCM indicates custom roles. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 11231 | The ID of the user group. |
| createTimeStamp | Long | 1606675230000 | The time when the user group was created. |
| groupName | String | grouptest _ | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606675230000 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606675230000 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |

| name | String | test | The name of the organization. |
|---|---|---|---|
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
| uuid | String | 11231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606675230000 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | restest _ | The name of the resource set. |
| rsId | String | 11231a | The unique code. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |

| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates RAM roles. _ _ ROLETYPEASCM indicates custom roles. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | 1 | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606675230000 | The time when the user was created. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606675230000 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 1606675230000 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xW****** | The password of the user. |
| ramUser | Boolean | false | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 34 | The ID of the logon control. |

| username | String | test | The display name of the user. |
|---|---|---|---|
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates RAM roles. _ _ ROLETYPEASCM indicates custom roles. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyUserInformation &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>0000000000</cellphoneNum>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11231</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <enableDingTalk>false</enableDingTalk>
    <displayName>test</displayName>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admmin</muserId>
        <arId>11231</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11231</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
    <loginPolicy>
        <ipRanges>
            <ipRange>0.0.0.0/0</ipRange>
            <protocol>IPV4</protocol>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId>admin</muserId>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <startTime>00:00</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>default.loginpolicy</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>11213</lpId>
        <cuserId>admin</cuserId>
    </loginPolicy>
    <parentPk>1689406703302188</parentPk>
    <lastLoginTime>1606675230000</lastLoginTime>
    <userGroups>
        <organizationId>1</organizationId>
        <createTimeStamp>1606675230000</createTimeStamp>
        <groupName>group_test</groupName>
        <augId>11231</augId>
        <id>1</id>
    </userGroups>
    <userGroups>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>res_test</resourceGroupName>
            <gmtCreated>1606675230000</gmtCreated>
            <rsId>11231a</rsId>
            <id>1</id>
        </resourceSets>
        <users>
            <muserId>admin</muserId>
            <backendAccountType>1</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <mtime>1606675230000</mtime>
```

`/`

```xml
            <organizationId>1</organizationId>
            <password>H2xW******</password>
            <default>false</default>
            <loginTime>1606675230000</loginTime>
            <userLoginCtrlId>34</userLoginCtrlId>
            <loginName>test</loginName>
            <ctime>1606675230000</ctime>
            <id>1</id>
            <enableShortMessage>false</enableShortMessage>
            <email>t***@163.com</email>
            <defaultRoleId>1</defaultRoleId>
            <cellphoneNum>00000000000</cellphoneNum>
            <aliyunUser>false</aliyunUser>
            <accountType>1</accountType>
            <active>true</active>
            <deleted>false</deleted>
            <mobileNationCode>86</mobileNationCode>
            <ramUser>false</ramUser>
            <enableEmail>false</enableEmail>
            <username>test</username>
        </users>
        <roles>
            <roleRange>roleRange.orgAndSubOrgs</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>11231</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>role_test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>false</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>role_test</roleName>
            <roleLevel>11231</roleLevel>
            <id>1</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
    </userGroups>
    <userGroups>
        <organization>
            <muserId>admin</muserId>
            <internal>false</internal>
            <level>0.1</level>
            <supportRegions>cn-qingdao-****-d01</supportRegions>
            <mtime>1606675230000</mtime>
            <uuid>11231</uuid>
            <parentId>0</parentId>
            <multiCloudStatus>master</multiCloudStatus>
            <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
            <name>test</name>
            <ctime>1606675230000</ctime>
            <alias>test</alias>
            <id>1</id>
            <cuserId>admin</cuserId>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>11231</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11231</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <default>false</default>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>JGdgSN2p******</accesskeyId>
    </accessKeys>
    <deleted>false</deleted>
<loginName>test</loginName>
```

```xml
    <loginName>test</loginName>
    <organization>
        <muserId>admin</muserId>
        <internal>false</internal>
        <level>0.1</level>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <mtime>1606791494471</mtime>
        <uuid>11231</uuid>
        <parentId>0</parentId>
        <multiCloudStatus>master</multiCloudStatus>
        <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
        <name>test</name>
        <ctime>1606791494471</ctime>
        <alias>test</alias>
        <id>1</id>
        <cuserId>admin</cuserId>
    </organization>
    <userGroupRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>11231</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11231</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>false</enableEmail>
    <enableShortMessage>false</enableShortMessage>
    <email>t***@163.com</email>
    <status>ACTIVE</status>
    <primaryKey>212530506704030466</primaryKey>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "cellphoneNum": "0000000000", "defaultRole": { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "muserId": "admin", "arId": "111", "code": "ROLE_RESOURCE_USER", "description": "test", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "ownerOrganizationId": "1", "enable": "true", "roleName": "role_test", "roleLevel": "11231", "id": "1", "organizationVisibility": "organizationVisibility.global" }, "enableDingTalk": "false", "displayName": "test", "roles": [ { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "muserId": "admmin", "arId": "11231", "code": "ROLE_RESOURCE_USER", "description": "role_test", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "ownerOrganizationId": "1", "enable": "true", |   |

`,`

```json
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`],`

```json
        "loginPolicy": {
            "ipRanges": [
```

`{`

```json
                    "ipRange": "0.0.0.0/0",
                    "protocol": "IPV4",
                    "loginPolicyId": "1"
```

`],`

```json
            "muserId": "admin",
            "default": "true",
            "ownerOrganizationId": "1",
            "timeRanges": [
```

`{`

```json
                    "startTime": "00:00",
                    "loginPolicyId": "1",
                    "endTime": "24:00"
```

`],`

```json
            "enable": "true",
            "name": "default.loginpolicy",
            "rule": "ALLOW",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "11213",
            "cuserId": "admin"
```

`},`

```json
        "parentPk": "1689406703302188",
        "lastLoginTime": "1606675230000",
        "userGroups": [
```

`{`

```json
                "organizationId": "1",
                "createTimeStamp": "1606675230000",
                "groupName": "group_test",
                "augId": "11231",
                "id": "1"
```

`},` `{`

```json
                "resourceSets": [
```

`{`

```json
                        "organizationID": "1",
                        "creator": "admin",
                        "resourceGroupName": "res_test",
                        "gmtCreated": "1606675230000",
                        "rsId": "11231a",
                        "id": "1"
```

`],`

```json
                "users": [
```

`{`

```json
                        "muserId": "admin",
                        "backendAccountType": "1",
                        "enableDingTalk": "false",
                        "mtime": "1606675230000",
                        "organizationId": "1",
                        "password": "H2xW******",
                        "default": "false",
                        "loginTime": "1606675230000",
                        "userLoginCtrlId": "34",
                        "loginName": "test",
                        "ctime": "1606675230000",
                        "id": "1",
                        "enableShortMessage": "false",
                        "email": "t***@163.com",
                        "defaultRoleId": "1",
                        "cellphoneNum": "00000000000",
                        "aliyunUser": "false",
                        "accountType": "1",
                        "active": "true",
                        "deleted": "false",
                        "mobileNationCode": "86",
                        "ramUser": "false",
                        "enableEmail": "false",
                        "username": "test"
```

`],`

```json
                "roles": [
```

`{`

```json
                        "roleRange": "roleRange.orgAndSubOrgs",
                        "rAMRole": "false",
"muserId":"admin"
```

```json
                        muserId: admin,
                        "arId": "11231",
                        "code": "ROLE_RESOURCE_USER",
                        "description": "role_test",
                        "active": "true",
                        "roleType": "ROLETYPE_ASCM",
                        "default": "false",
                        "ownerOrganizationId": "1",
                        "enable": "true",
                        "roleName": "role_test",
                        "roleLevel": "11231",
                        "id": "1",
                        "organizationVisibility": "organizationVisibility.global",
                        "cuserId": "admin"
```

`]` `},` `{`

```json
                "organization": {
                    "muserId": "admin",
                    "internal": "false",
                    "level": "0.1",
                    "supportRegions": "cn-qingdao-****-d01",
                    "mtime": "1606675230000",
                    "uuid": "11231",
                    "parentId": "0",
                    "multiCloudStatus": "master",
                    "supportRegionList": "[\"cn-qingdao-****-d01\"]",
                    "name": "test",
                    "ctime": "1606675230000",
                    "alias": "test",
                    "id": "1",
                    "cuserId": "admin"
```

`],`

```json
        "userRoles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "11231",
                "code": "ROLE_RESOURCE_USER",
                "description": "role_test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`],`

```json
        "default": "false",
        "accessKeys": [
```

`{`

```json
                "ctime": "1606675230000",
                "id": "1",
                "region": "cn-qingdao-****-d01",
                "cuserId": "admin",
                "status": "ACTIVE",
                "accesskeyId": "JGdgSN2p******"
```

`],`

```json
        "deleted": "false",
        "loginName": "test",
        "organization": {
            "muserId": "admin",
            "internal": "false",
            "level": "0.1",
            "supportRegions": "cn-qingdao-****-d01",
            "mtime": "1606791494471",
            "uuid": "11231",
            "parentId": "0",
            "multiCloudStatus": "master",
            "supportRegionList": "[\"cn-qingdao-****-d01\"]",
            "name": "test",
            "ctime": "1606791494471",
            "alias": "test",
            "id": "1",
            "cuserId": "admin"
```

`},`

```json
        "userGroupRoles": [
```

`{` `"` `l` `"` `"` `l`

```
dSbO
```

`"`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "11231",
                "code": "ROLE_RESOURCE_USER",
                "description": "role_test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`],`

```json
        "mobileNationCode": "86",
        "id": "1",
        "enableEmail": "false",
        "enableShortMessage": "false",
        "email": "t***@163.com",
        "status": "ACTIVE",
        "primaryKey": "212530506704030466"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

###### 4.3.1.4.13 RecoverUserByLoginName

Restores a deleted user.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RecoverUserByLoginName | The operation that you want to perform. Set the value to RecoverUserByLoginName. |
| LoginName | String | Yes | testtest | The logon name of the user. |
| OrganizationId | Integer | Yes | 5 | The ID of the organization. |
| roleIdList | Json | No | {"RoleIdList": [ "5", "6", "8" ]} | The list of roles. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | admin | The user who created the AccessKey pair. |
| id | Integer | 1 | The AccessKey ID. |
| region | String | cn-qingdao-****-d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |

| default | Boolean | false | Indicates whether the role is a preset role. |
|---|---|---|---|
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates RAM roles. _ _ ROLETYPEASCM indicates custom roles. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1606675230000 | The most recent logon time. |
| loginName | String | test | The logon name of the user. |

| loginPolicy | Struct |   | The logon policy. |
|---|---|---|---|
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRang |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 11231 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | default.loginpolicy | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the logon policy is globally shared. organizationVisibility.organization indicates that the logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |

| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
|---|---|---|---|
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
| uuid | String | 11231 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 112311 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |

| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
|---|---|---|---|
| userGroupRoles | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| userGroups | Array of userGroups |   | The list of user groups. |
| augId | String | 11231 | The ID of the user group. |
| createTimeStamp | Long | 1606675230000 | The time when the user group was created. |
| groupName | String | grouptest _ | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606675230000 | The time when the organization was created. |

| cuserId | String | admin | The user who created the organization. |
|---|---|---|---|
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606675230000 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of regions. |
| supportRegions | String | cn-qingdao-****-d01 | The list of regions. |
| uuid | String | 11231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606675230000 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | restest _ | The name of the resource set. |
| rsId | String | 11231 | The ID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | 1 | The type of the account. Valid values: AscmUser, AliyunUser, and RamUser. AscmUser indicates a user who is visible to customers in the Apsara Uni-manager Management Console. AliyunUser indicates an Apsara Stack tenant account. RamUser indicates a RAM user. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606675230000 | The time when the user was created. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortMessage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606675230000 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |

| mtime | Long | 1606675230000 | The time when the user was modified. |
|---|---|---|---|
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxMWLhtyjsO1fRkY oCRcErAgP9Hd0IXp2f5rRSmArS | The password of the cluster user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11321 | The ID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM indicates a RAM role. _ _ ROLETYPEASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |

| redirect | Boolean | false | Indicates whether redirections are performed. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RecoverUserByLoginName &LoginName=testtest &OrganizationId=5 &<Common request parameters>
```

Sample success response

| XML | format |
|---|---|
| <redirect>false</redirect> <code>200</code> <cost>746</cost> <data> <cellphoneNum>13311111111</cellphoneNum> <displayName>fengyueSubOrgAdmin2</displayName> <enableDingTalk>true</enableDingTalk> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <code>ROLE_ORGANIZATION_ADMIN</code> <active>true</active> <description>defaultRole.organizationAdmin.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.organizationAdmin.name</roleName> <id>4</id> <roleLevel>2147483647</roleLevel> <organizationVisibility>organizationVisibility.global</organizationVisibility> </roles> <loginPolicy> <ipRanges> <protocol>IPV4</protocol> <ipRange>0.0.0.0/0</ipRange> <loginPolicyId>1</loginPolicyId> </ipRanges> <muserId/> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <timeRanges> <loginPolicyId>1</loginPolicyId> <startTime>00:00</startTime> <endTime>24:00</endTime> </timeRanges> <enable>true</enable> <name>defaultLoginPolicy.name</name> <rule>ALLOW</rule> <id>1</id> <cuserId/> <organizationVisibility>organizationVisibility.global</organizationVisibility> </loginPolicy> <parentPk>1809392454221726</parentPk> <lastLoginTime>1592465207953</lastLoginTime> <userRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <muserId/> <rAMRole>false</rAMRole> <code>ROLE_ORGANIZATION_ADMIN</code> <active>true</active> <description>defaultRole.organizationAdmin.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.organizationAdmin.name</roleName> <id>4</id> <roleLevel>2147483647</roleLevel> <cuserId/> <organizationVisibility>organizationVisibility.global</organizationVisibility> </userRoles> <accessKeys> <ctime>1592454572000</ctime> <id>673</id> <region>cn-qingdao-****-d01</region> <cuserId>admin</cuserId> <accesskeyId>0qZ6FB******</accesskeyId> |   |

```xml
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>admin</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <level>0.1.377</level>
        <name>suborg</name>
        <alias>suborg</alias>
        <id>379</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>377</parentId>
    </organization>
    <id>5679</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>1@1.com</email>
    <enableShortMessage>true</enableShortMessage>
    <primaryKey>228648192465372091</primaryKey>
    <status>ACTIVE</status>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "cellphoneNum": "00000000000", "defaultRole": { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "muserId": "admin", "arId": "111", "code": "ROLE_RESOURCE_USER", "description": "test", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "ownerOrganizationId": "1", "enable": "true", "roleName": "role_test", "roleLevel": "11321", "id": "1", "organizationVisibility": "organizationVisibility.global" }, "enableDingTalk": "false", "displayName": "test", "roles": [ { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": "false", "muserId": "admin", "arId": "112311", "code": "ROLE_RESOURCE_USER", "description": "role_test", "active": "true", "roleType": "ROLETYPE_ASCM", "default": "true", "ownerOrganizationId": "1", "enable": "true", "roleName": "role_test", "roleLevel": "11231", "id": "1", "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" } ], "loginPolicy": { "ipRanges": [ { "ipRange": "0.0.0.0/0", "protocol": "IPV4", "loginPolicyId": "1" } ], "muserId": "admin", "default": "true", "ownerOrganizationId": "1" |   |

```json
            "ownerOrganizationId": "1",
            "timeRanges": [
```

`{`

```json
                    "startTime": "00:00",
                    "loginPolicyId": "1",
                    "endTime": "24:00"
```

`],`

```json
            "enable": "true",
            "name": "default.loginpolicy",
            "rule": "ALLOW",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "11231",
            "cuserId": "admin"
```

`},`

```json
        "parentPk": "1689406703302188",
        "lastLoginTime": "1606675230000",
        "userGroups": [
```

`{`

```json
                "organizationId": "1",
                "createTimeStamp": "1606675230000",
                "groupName": "group_test",
                "augId": "11231",
                "id": "1"
```

`},` `{`

```json
                "resourceSets": [
```

`{`

```json
                        "organizationID": "1",
                        "creator": "admin",
                        "resourceGroupName": "res_test",
                        "gmtCreated": "1606675230000",
                        "rsId": "11231",
                        "id": "1"
```

`],`

```json
                "users": [
```

`{`

```json
                        "muserId": "admin",
                        "backendAccountType": "1",
                        "enableDingTalk": "false",
                        "mtime": "1606675230000",
                        "organizationId": "1",
                        "password": "H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS",
                        "default": "false",
                        "loginTime": "1606675230000",
                        "userLoginCtrlId": "34",
                        "loginName": "test",
                        "ctime": "1606675230000",
                        "id": "1",
                        "enableShortMessage": "false",
                        "email": "t***@163.com",
                        "defaultRoleId": "1",
                        "cellphoneNum": "00000000000",
                        "aliyunUser": "false",
                        "accountType": "1",
                        "active": "true",
                        "deleted": "false",
                        "mobileNationCode": "86",
                        "ramUser": "true",
                        "enableEmail": "false",
                        "username": "test"
```

`],`

```json
                "roles": [
```

`{`

```json
                        "roleRange": "roleRange.orgAndSubOrgs",
                        "rAMRole": "false",
                        "muserId": "admin",
                        "arId": "11231",
                        "code": "ROLE_RESOURCE_USER",
                        "description": "test",
                        "active": "true",
                        "roleType": "ROLETYPE_ASCM",
                        "default": "true",
                        "ownerOrganizationId": "1",
                        "enable": "true",
                        "roleName": "role_test",
                        "roleLevel": "11231",
                        "id": "1",
                        "organizationVisibility": "organizationVisibility.global",
                        "cuserId": "admin"
```

`]` `},` `{`

```json
                "organization": {
                    "muserId": "admin",
                    "internal": "false",
                    "level": "0.1",
                    "supportRegions": "cn-qingdao-****-d01",
                    "mtime": "1606675230000",
                    "uuid": "11231",
                    "parentId": "0",
                    "multiCloudStatus": "master",
                    "supportRegionList": "[\"cn-qingdao-****-d01\"]",
                    "name": "test",
                    "ctime": "1606675230000",
                    "alias": "test",
                    "id": "1",
                    "cuserId": "admin"
```

`],`

```json
        "userRoles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "11321",
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`],`

```json
        "default": "false",
        "accessKeys": [
```

`{`

```json
                "ctime": "1606675230000",
                "id": "1",
                "region": "cn-qingdao-****-d01",
                "cuserId": "admin",
                "status": "ACTIVE",
                "accesskeyId": "JGdgSN2p******"
```

`],`

```json
        "deleted": "false",
        "loginName": "test",
        "organization": {
            "muserId": "admin",
            "internal": "false",
            "level": "0.1",
            "supportRegions": "cn-qingdao-****-d01",
            "mtime": "1606791494471",
            "uuid": "11231",
            "parentId": "0",
            "multiCloudStatus": "master",
            "supportRegionList": "[\"cn-qingdao-****-d01\"]",
            "name": "test",
            "ctime": "1606791494471",
            "alias": "test",
            "id": "1",
            "cuserId": "admin"
```

`},`

```json
        "userGroupRoles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "11231",
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`],`

```json
        "mobileNationCode": "86",
        "id": "1",
        "enableEmail": "false",
        "enableShortMessage": "false",
        "email": "t***@163.com",
        "status": "ACTIVE",
        "primaryKey": "212530506704030466"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

###### 4.3.1.4.14 DeactivateUser

Deactivates a user. When a user is deactivated, all AccessKey pairs of the user are deactivated. This operation is supported by Apsara Stack Enterprise Edition V3.12.0 SP016 or later. This operation is supported by Apsara Stack Enterprise Edition V3.14.0 SP013 or later.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/deactivateUser HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | test | The logon name of the user. |
| multiCloudStatus | String | Body | No | master | The multi-cloud status of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Struct |   | The response data. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | 1 | The ID of the AccessKey. |
| ctime | Long | 12314123123123 | The time when the AccessKey pair of the user was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID. |
| region | String | abc | The zone. |
| status | String | ACTIVE | The state. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |

| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
|---|---|---|---|
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | testdesc _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1234 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | test | The management permissions of the role. |
| roleType | String | ROLETYPERAM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | xx@xx.com | The email address of the user. |
| enableDingTalk | Boolean | true | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | true | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | true | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 16071312412314 | The time when the user last logged on. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The creator. |
| default | Boolean | true | Indicates whether the policy is a preset policy. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks that are used to log on to the Apsara Uni- manager Management Console. |
| ipRange | String | 0.0.0.0/0 | The CIDR block that is used to log on to the Apsara Uni-manager Management Console. |

| loginPolicyId | Integer | 1 | The ID of the logon policy. |
|---|---|---|---|
| protocol | String | IPV4 | The protocol. |
| lpId | String | 123 | The UUID of the logon policy. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The type of the logon policy. Allow: whitelist Deny: blacklist |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range queried. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 18635345234 | The time when the organization to which the user belongs was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 18239237283 | The time when the organization to which the user belongs was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | [cn-qingdao-env17-d01] | The list of zones. |
| supportRegions | String | cn-qingdao-env17-d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |

| parentPk | String | 1689406703302188 | The primary key of the Apsara Stack tenant account. |
|---|---|---|---|
| primaryKey | String | 212530506704030466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | roledesc _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| status | String | ACTIVE | The state of the user. active inactive |
| userGroupRoles | Array of userGroupRole |   | The list of roles for the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | 123 | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | false | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |

| muserId | String | admin | The modifier of the role. |
|---|---|---|---|
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPERAM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 1 | The UUID of the user group. |
| createTimeStamp | Long | 123123123 | The time when the user group was created. |
| groupName | String | test | The name of the user group. |
| id | Integer | 1 | The ID. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 123124123 | The time when the organization to which the user group belongs was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 1 | The level of the organization. |
| mtime | Long | 15134123123 | The time when the organization to which the user group belongs was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | TEST | The name of the organization. |
| parentId | Integer | 2 | The ID of the parent organization. |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | The list of zones. |
| supportRegions | String | cn-qingdao-env17-d01 | The list of zones. |
| uuid | String | 123123 | The UUID of the organization. |

| organizationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator. |
| gmtCreated | Long | 12312423123 | The time when the resource set was created. |
| id | Integer | 1 | The ID. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | test | The name of the resource set. |
| rsId | String | 123 | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1 | The UUID of the role. |
| code | String | 1 | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | 1test | The description of the role. |
| enable | Boolean | false | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | defaultRole.resourceUser.name | The management permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM, ROLETYPEASCM, _ _ and ROLETYPERAMROLEAUTHORIZATION. ROLETYPERAM specifies a _ _ RAM role. ROLETYPEASCM specifies a preset or custom role. _ ROLETYPERAMROLEAUTHORIZATION specifies a RAM role-based batch _ authorization role. |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. |
| active | Boolean | false | Indicates whether the role is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | 1 | The type of the account that is mapped in the backend. |

| cellphoneNum | String | 18888888888 | The mobile number of the user. |
|---|---|---|---|
| ctime | Long | 1234132123 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | xx@xx.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID. |
| loginName | String | admin | The logon name of the user. |
| loginTime | Long | 1231232323 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 12312312312 | The time when the user was modified. |
| muserId | String | admin | The modifier of the role. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxMWLhtyjsO1fRkY oCRcErAgP9Hd0IXp2f5rRSmArS | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 23 | This parameter is deprecated. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles for the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | desc | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. |

| ownerOrganizationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. ROLETYPERAM: a RAM role _ ROLETYPEASCM: a preset or custom role _ ROLETYPERAMROLEAUTHORIZATION: a RAM role-based batch _ authorization role |
| message | String | success | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/deactivateUser HTTP/1.1 Common request headers
```

`{`

```json
"loginName": "test"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <cellphoneNum>18888888888</cellphoneNum> <enableDingTalk>true</enableDingTalk> <displayName>test</displayName> <parentPk>1689406703302188</parentPk> <lastLoginTime>16071312412314</lastLoginTime> <default>false</default> <deleted>false</deleted> <loginName>test</loginName> <mobileNationCode>86</mobileNationCode> <id>1</id> <enableEmail>true</enableEmail> <enableShortMessage>true</enableShortMessage> <email>xx@xx.com</email> <status>ACTIVE</status> <primaryKey>212530506704030466</primaryKey> <userGroupRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>123</arId> <code>123</code> <description>test</description> <active>true</active> <roleType>ROLETYPE_RAM</roleType> <default>false</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>false</enable> <roleName>test</roleName> <roleLevel>1</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </userGroupRoles> <userGroups> <organizationId>1</organizationId> <groupName>test</groupName> |   |

```xml
        <augId>1</augId>
        <createTimeStamp>123123123</createTimeStamp>
        <id>1</id>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>test</resourceGroupName>
            <gmtCreated>12312423123</gmtCreated>
            <rsId>123</rsId>
            <id>1</id>
        </resourceSets>
        <users>
            <cellphoneNum>18888888888</cellphoneNum>
            <muserId>admin</muserId>
            <aliyunUser>false</aliyunUser>
            <backendAccountType>1</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <accountType>1</accountType>
            <active>false</active>
            <mtime>12312312312</mtime>
            <organizationId>1</organizationId>
            <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password>
            <default>false</default>
            <loginTime>1231232323</loginTime>
            <deleted>false</deleted>
            <userLoginCtrlId>23</userLoginCtrlId>
            <loginName>admin</loginName>
            <ctime>1234132123</ctime>
            <mobileNationCode>86</mobileNationCode>
            <id>1</id>
            <ramUser>true</ramUser>
            <enableEmail>false</enableEmail>
            <enableShortMessage>false</enableShortMessage>
            <email>xx@xx.com</email>
            <defaultRoleId>1</defaultRoleId>
            <username>test</username>
        </users>
        <roles>
            <roleRange>defaultRole.resourceUser.name</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>1</arId>
            <code>1</code>
            <description>1test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>false</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>false</enable>
            <roleName>test</roleName>
            <roleLevel>2</roleLevel>
            <id>1</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
        <organization>
            <muserId>admin</muserId>
            <internal>true</internal>
            <multiCloudStatus>master</multiCloudStatus>
            <level>1</level>
            <name>TEST</name>
            <supportRegions>cn-qingdao-env17-d01</supportRegions>
            <ctime>123124123</ctime>
            <alias>test</alias>
            <id>1</id>
            <mtime>15134123123</mtime>
            <uuid>123123</uuid>
            <cuserId>admin</cuserId>
            <parentId>2</parentId>
            <supportRegionList>["cn-qingdao-env17-d01"]</supportRegionList>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>true</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>desc</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>name</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
```

```xml
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>12314123123123</ctime>
        <id>1</id>
        <region>abc</region>
        <cuserId>admin</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>1</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>true</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_desc</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>name</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
    <defaultRole>
        <roleRange>test</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test_desc</description>
        <active>true</active>
        <roleType>ROLETYPE_RAM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>test</roleName>
        <roleLevel>1234</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <muserId>admin</muserId>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <name>test</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>123</lpId>
        <cuserId>admin</cuserId>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <timeRanges>
            <startTime>00:00</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>24:00</endTime>
        </timeRanges>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>true</internal>
        <multiCloudStatus>master</multiCloudStatus>
        <level>0.1</level>
        <name>test</name>
        <supportRegions>cn-qingdao-env17-d01</supportRegions>
        <ctime>18635345234</ctime>
        <alias>test</alias>
        <id>1</id>
        <mtime>18239237283</mtime>
        <uuid>1231</uuid>
        <cuserId>admin</cuserId>
        <parentId>0</parentId>
        <supportRegionList>[cn-qingdao-env17-d01]</supportRegionList>
    </organization>
</data> <success>true</success> <pureListData>true</pureListData>
```

```xml
pue statatue/pue stata <message>success</message>
```

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": {"cellphoneNum":"18888888888","enableDingTalk":"true","displayName":"test","parentPk":"1689406703302188","lastLoginTime":"16071312412314","defau false","deleted":"false","loginName":"test","mobileNationCode":"86","id":"1","enableEmail":"true","enableShortMessage":"true","email":"xx@xx.com atus":"ACTIVE","primaryKey":"212530506704030466","userGroupRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123","code":"123","description":"test","active":"true","role :"ROLETYPE_RAM","default":"false","ownerOrganizationId":"1","enable":"false","roleName":"test","roleLevel":"1","id":"1","organizationVisibility" anizationVisibility.global","cuserId":"admin"}],"userGroups": [{"organizationId":"1","groupName":"test","augId":"1","createTimeStamp":"123123123","id":"1","resourceSets": [{"organizationID":"1","creator":"admin","resourceGroupName":"test","gmtCreated":"12312423123","rsId":"123","id":"1"}],"users": [{"cellphoneNum":"18888888888","muserId":"admin","aliyunUser":"false","backendAccountType":"1","enableDingTalk":"false","accountType":"1","activ alse","mtime":"12312312312","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS","default":"false","loginTime 31232323","deleted":"false","userLoginCtrlId":"23","loginName":"admin","ctime":"1234132123","mobileNationCode":"86","id":"1","ramUser":"true","e Email":"false","enableShortMessage":"false","email":"xx@xx.com","defaultRoleId":"1","username":"test"}],"roles": [{"roleRange":"defaultRole.resourceUser.name","rAMRole":"false","muserId":"admin","arId":"1","code":"1","description":"1test","active":"true","r pe":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"false","roleName":"test","roleLevel":"2","id":"1","organizationVisibil "organizationVisibility.global","cuserId":"admin"}],"organization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"1","name":"TEST","supportRegions":"cn-qingdao-env17- d01","ctime":"123124123","alias":"test","id":"1","mtime":"15134123123","uuid":"123123","cuserId":"admin","parentId":"2","supportRegionList":"[ \"cn-qingdao-env17-d01\"]"}}],"userRoles":[{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar- 123","code":"ROLE_RESOURCE_USER","description":"desc","active":"true","roleType":"ROLETYPE_ASCM","default":"true","ownerOrganizationId":"1","ena "true","roleName":"name","roleLevel":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cuserId":"admin"}],"accessKey [{"ctime":"12314123123123","id":"1","region":"abc","cuserId":"admin","status":"ACTIVE","accesskeyId":"1"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar- 123","code":"ROLE_RESOURCE_USER","description":"role_desc","active":"true","roleType":"ROLETYPE_ASCM","default":"true","ownerOrganizationId":"1" ble":"true","roleName":"name","roleLevel":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cuserId":"admin"}],"defa le":{"roleRange":"test","rAMRole":"false","muserId":"admin","arId":"ar- 123","code":"ROLE_RESOURCE_USER","description":"test_desc","active":"true","roleType":"ROLETYPE_RAM","default":"false","ownerOrganizationId":"1" ble":"true","roleName":"test","roleLevel":"1234","id":"1","organizationVisibility":"organizationVisibility.global"},"loginPolicy": {"muserId":"admin","default":"true","ownerOrganizationId":"1","enable":"true","name":"test","rule":"ALLOW","id":"1","organizationVisibility":"or ationVisibility.global","lpId":"123","cuserId":"admin","ipRanges": [{"protocol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"}],"timeRanges": [{"startTime":"00:00","loginPolicyId":"1","endTime":"24:00"}]},"organization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"0.1","name":"test","supportRegions":"cn-qingdao-env17- d01","ctime":"18635345234","alias":"test","id":"1","mtime":"18239237283","uuid":"1231","cuserId":"admin","parentId":"0","supportRegionList":"[ cn-qingdao-env17-d01]"}},"success":"true","pureListData":"true","message":"success"} |   |

##### 4.3.1.5 User groups

###### 4.3.1.5.1 ListUserGroups

Queries a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/listUserGroups HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | test | The logon name of the user. |
| userGroupName | String | Body | No | groupname | The name of the user group. |
| roleId | Integer | Body | No | 1 | The ID of the role. |
| resourceSetId | Integer | Body | No | 123 | The ID of the resource set. |
| organizationId | Integer | Body | No | 123 | The ID of the organization. |
| currentPage | Integer | Body | No | 1 | The number of the page to return. |
| pageSize | Integer | Body | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Array of itemData |   | The response data. |
| augId | String | 1122 | The UUID of the user group. |
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | test | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | 123 | The creator of the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier of the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegionList | List | cn-qingdao-env17-d01 | The list of zones. |
| supportRegions | String | ["cn-qingdao-env17-d01"] | The list of zones. |
| uuid | String | 1323 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | restest _ | The name of the resource set. |
| rsId | String | 123a | The UUID of the resource set. |

| roles | Array of role |   | The list of roles. |
|---|---|---|---|
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123a | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | aa | The description of the role. |
| enable | Boolean | false | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | RamUser | The type of the account that is mapped in the backend. AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 12345678911 | The mobile number of the user. |

| ctime | Long | 1606791494471 | The time when the user was created. |
|---|---|---|---|
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | 1***@123.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The modifier of the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxMWLhtyjsO1fRkY oCRcErAgP9Hd0IXp2f5rRSmArS | The password of the user. |
| ramUser | Boolean | false | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 123 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| message | String | success | The message. |
| pageInfo | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The number of the returned page. |
| pageSize | Integer | 5 | The number of entries returned per page. |
| total | Integer | 10 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/listUserGroups HTTP/1.1 Common request headers
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <organizationId>1</organizationId> <groupName>test</groupName> <augId>1122</augId> <createTimeStamp>1606791494471</createTimeStamp> <description>a</description> <id>1</id> <resourceSets> <organizationId>1</organizationId> <creator>admin</creator> <resourceGroupName>res_test</resourceGroupName> <gmtCreated>1606791494471</gmtCreated> <rsId>123a</rsId> <id>1</id> </resourceSets> <users> <cellphoneNum>12345678911</cellphoneNum> <muserId>admin</muserId> <aliyunUser>false</aliyunUser> <backendAccountType>RamUser</backendAccountType> <enableDingTalk>false</enableDingTalk> <accountType>1</accountType> <active>true</active> <mtime>1606791494471</mtime> <organizationId>1</organizationId> <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password> <default>false</default> <loginTime>1606791494471</loginTime> <deleted>false</deleted> <userLoginCtrlId>123</userLoginCtrlId> <loginName>test</loginName> <ctime>1606791494471</ctime> <mobileNationCode>86</mobileNationCode> <id>1</id> <ramUser>false</ramUser> <enableEmail>false</enableEmail> <enableShortMessage>false</enableShortMessage> <email>1***@123.com</email> <defaultRoleId>1</defaultRoleId> <username>test</username> </users> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>123a</arId> <code>ROLE_RESOURCE_USER</code> <description>aa</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>false</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>false</enable> <roleName>role_test</roleName> <roleLevel>0.1</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </roles> <organization> <muserId>admin</muserId> <internal>false</internal> <multiCloudStatus>master</multiCloudStatus> <level>0.1</level> <name>test</name> <supportRegions>["cn-qingdao-env17-d01"]</supportRegions> <ctime>1606791494471</ctime> <alias>test</alias> <id>1</id> <mtime>1606791494471</mtime> <uuid>1323</uuid> <cuserId>123</cuserId> <parentId>0</parentId> <supportRegionList>cn-qingdao-env17-d01</supportRegionList> </organization> </data> <success>true</success> <pageInfo> <total>10</total> <totalPage>2</totalPage> <pageSize>5</pageSize> |   |
| > Document Version: 20251105 187 |   |

```xml
    <pageSize>5</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": [{"organizationId":"1","groupName":"test","augId":"1122","createTimeStamp":"1606791494471","description":"a","id":"1","resourceSets": [{"organizationId":"1","creator":"admin","resourceGroupName":"res_test","gmtCreated":"1606791494471","rsId":"123a","id":"1"}],"users": [{"cellphoneNum":"12345678911","muserId":"admin","aliyunUser":"false","backendAccountType":"RamUser","enableDingTalk":"false","accountType":"1", ve":"true","mtime":"1606791494471","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS","default":"false","lo me":"1606791494471","deleted":"false","userLoginCtrlId":"123","loginName":"test","ctime":"1606791494471","mobileNationCode":"86","id":"1","ramUs false","enableEmail":"false","enableShortMessage":"false","email":"1***@123.com","defaultRoleId":"1","username":"test"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123a","code":"ROLE_RESOURCE_USER","description":"aa","active ue","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"false","roleName":"role_test","roleLevel":"0.1","id":"1","o zationVisibility":"organizationVisibility.global","cuserId":"admin"}],"organization": {"muserId":"admin","internal":"false","multiCloudStatus":"master","level":"0.1","name":"test","supportRegions":"[\"cn-qingdao-env17- d01\"]","ctime":"1606791494471","alias":"test","id":"1","mtime":"1606791494471","uuid":"1323","cuserId":"123","parentId":"0","supportRegionList" qingdao-env17-d01"}}],"success":"true","pageInfo": {"total":"10","totalPage":"2","pageSize":"5","currentPage":"1"},"pureListData":"false","message":"success"} |   |

###### 4.3.1.5.2 CreateUserGroup

Creates a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/createUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| GroupName | String | Body | Yes | test | The name of the user group. |
| OrganizationId | Integer | Body | Yes | 1 | The ID of the organization. |
| Description | String | Body | No | test | The description of the user group. |
| RoleIdList | Json | Body | No | ["12"] | The list of roles. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| code | String | 200 | The HTTP status code. |
| data | Struct |   | The response data. |
| augId | String | 12312 | The UUID of the user group. |
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| description | String | grouptest _ | The description of the user group. |
| groupName | String | grouptest _ | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1638345831 | The time when the organization was created. |

| cuserId | String | admin | The creator of the organization. |
|---|---|---|---|
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1638345831 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegionList | List | cn-qingdao-env17-d01 | The list of zones. |
| supportRegions | String | ["cn-qingdao-env17-d01"] | The list of zones. |
| uuid | String | e2469ed4-527d-11ec-85ab- 0a80ff2603de | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 12 | The ID of the resource set. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceGroupName | String | restest _ | The name of the resource set. |
| rsId | String | 123121a | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123123 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccountType | String | RamUser | The type of the account that is mapped in the backend. AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 16067914944 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | 1***@123.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |

| loginTime | Long | 1606791494471 | The time when the user logged on. |
|---|---|---|---|
| mobileNationCode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The modifier of the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxMWLhtyjsO1fRkY oCRcErAgP9Hd0IXp2f5rRSmArS | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlId | Integer | 12 | This parameter is deprecated. |
| username | String | test | The display name of the user. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/createUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"GroupName": "", "OrganizationId": ""
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <organizationId>1</organizationId>
    <groupName>group_test</groupName>
    <augId>12312</augId>
    <createTimeStamp>1606791494471</createTimeStamp>
    <description>group_test</description>
    <id>1</id>
    <resourceSets>
        <organizationId>1</organizationId>
        <creator>admin</creator>
        <resourceGroupName>res_test</resourceGroupName>
        <gmtCreated>1606791494471</gmtCreated>
        <rsId>123121a</rsId>
        <id>12</id>
    </resourceSets>
    <users>
        <cellphoneNum>16067914944</cellphoneNum>
        <muserId>admin</muserId>
        <aliyunUser>false</aliyunUser>
        <backendAccountType>RamUser</backendAccountType>
        <enableDingTalk>false</enableDingTalk>
        <accountType>1</accountType>
        <active>true</active>
        <mtime>1606791494471</mtime>
        <organizationId>1</organizationId>
        <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password>
        <default>true</default>
        <loginTime>1606791494471</loginTime>
        <deleted>false</deleted>
        <userLoginCtrlId>12</userLoginCtrlId>
        <loginName>test</loginName>
        <ctime>1606791494471</ctime>
        <mobileNationCode>86</mobileNationCode>
        <id>1</id>
        <ramUser>true</ramUser>
        <enableEmail>false</enableEmail>
        <enableShortMessage>false</enableShortMessage>
        <email>1***@123.com</email>
        <defaultRoleId>1</defaultRoleId>
        <username>test</username>
    </users>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>123123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
    <organization>
        <muserId>admin</muserId>
        <internal>false</internal>
        <multiCloudStatus>master</multiCloudStatus>
        <level>0.1</level>
        <name>test</name>
        <supportRegions>["cn-qingdao-env17-d01"]</supportRegions>
        <ctime>1638345831</ctime>
        <alias>test</alias>
        <id>1</id>
        <mtime>1638345831</mtime>
        <uuid>e2469ed4-527d-11ec-85ab-0a80ff2603de</uuid>
        <cuserId>admin</cuserId>
        <parentId>1</parentId>
        <supportRegionList>cn-qingdao-env17-d01</supportRegionList>
    </organization>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"organizationId":"1","groupName":"group_test","augId":"12312","createTimeStamp":"1606791494471","description":"group_test","id":"1","resourceSet [{"organizationId":"1","creator":"admin","resourceGroupName":"res_test","gmtCreated":"1606791494471","rsId":"123121a","id":"12"}],"users": [{"cellphoneNum":"16067914944","muserId":"admin","aliyunUser":"false","backendAccountType":"RamUser","enableDingTalk":"false","accountType":"1", ve":"true","mtime":"1606791494471","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS","default":"true","logi e":"1606791494471","deleted":"false","userLoginCtrlId":"12","loginName":"test","ctime":"1606791494471","mobileNationCode":"86","id":"1","ramUser ue","enableEmail":"false","enableShortMessage":"false","email":"1***@123.com","defaultRoleId":"1","username":"test"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123123","code":"ROLE_RESOURCE_USER","description":"test","act :"true","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"role_test","roleLevel":"1","id":"1","o izationVisibility":"organizationVisibility.global","cuserId":"admin"}],"organization": {"muserId":"admin","internal":"false","multiCloudStatus":"master","level":"0.1","name":"test","supportRegions":"[\"cn-qingdao-env17d01\"]","ctime":"1638345831","alias":"test","id":"1","mtime":"1638345831","uuid":"e2469ed4-527d-11ec-85ab- 0a80ff2603de","cuserId":"admin","parentId":"1","supportRegionList":"cn-qingdao-env17d01"}},"success":"true","pureListData":"false","message":"success"}
```

###### 4.3.1.5.3 ListUsersInUserGroup

Queries users in a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/listUsersInUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| UserGroupId | Integer | Body | Yes | 123 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Struct |   | The response data. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| CreateTime | String | 1606675230000 | The time when the AccessKey pair was created. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
| accesskeySecret | String | ************** | The AccessKey secret. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | admin | The user who created the AccessKey pair. |
| dtUserId | Integer | 1 | This parameter is deprecated. |
| id | Integer | 1 | The primary key of the AccessKey pair. |
| mtime | Long | 1606675230000 | The time when the AccessKey was modified. |
| muserId | String | admin | The user who modified the AccessKey pair. |
| region | String | cn-qingdao-****-d01 | The zone in which the AccessKey pair is available. |
| status | String | active | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| type | String | 1 | The type of the AccessKey pair. |

| cellphoneNum | String | 18888888888 | The mobile number of the user. |
|---|---|---|---|
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | as | The description of the role. |
| enable | Boolean | true | Indicates whether the role is enabled. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| description | String | description | The description of the user. |
| displayName | String | test | The display name. |
| email | String | 1***@122.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |

| enableShortMessage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
|---|---|---|---|
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 162314151313 | The time when the user logged on. |
| loginName | String | 123 | The logon name of the user. |
| loginPolicy | Struct |   | The information about the logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | false | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Struct |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The UUID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | default.loginpolicy | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | allow | The type of the logon policy. Valid values: Allow and Deny. Allow specifies a whitelist. Deny specifies a blacklist. |
| timeRanges | Struct |   | The list of time ranges. |
| endTime | String | 11:20 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 10:20 | The beginning of the time range queried. |
| mobileNationCode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| childrenOrder | String | 343,44,33 | The sorted organization IDs. |
| ctime | Long | 1622311 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |

| description | String | aa | The description of the organization. |
|---|---|---|---|
| dtOrgId | Integer | 1 | This parameter is deprecated. |
| extraInfo | String | aaa | This parameter is deprecated. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 1 | The level of the organization. |
| mtime | Long | 15123222 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| personNum | Integer | 12 | The maximum number of users. |
| resourceGroupNum | Integer | 10 | The maximum number of resource sets. |
| status | String | active | Indicates whether the organization is valid. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of zones. |
| supportRegions | String | cn-qingdao-****-d01 | The list of zones. |
| uuid | String | 1231231 | The UUID of the organization. |
| parentPk | String | 1689406703302180 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030000 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | String | true | Indicates whether the role is valid. |
| arId | String | 1231 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| privilegeCodes | List | ["123"] | The list of permission codes. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | roletest _ | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| systemPrivilegeCodes | List | ["123"] | The list of system permission codes. |
| status | String | active | The state of the user. Valid values: active and inactive. |
| telephoneNum | String | 12345678 | The landline number of the user. |
| userGroupRoles | Array of userGroupRole |   | The list of roles for the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | 1 | The code of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | roletest _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganizationId | Integer | 2 | The ID of the organization. |
| rAMRole | String | false | Indicates whether the role is a RAM role. |

| roleLevel | Integer | 1 | The level of the role. |
|---|---|---|---|
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| userGroups | Struct |   | The list of user groups. |
| augId | String | 1231 | The UUID of the user group. |
| createTimeStamp | Long | 1606791494471 | The time when the user group was created. |
| description | String | test | The description of the user group. |
| groupName | String | grouptest _ | The name of the user group. |
| id | Integer | 123 | The ID of the user group. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| childrenOrder | String | 343,44,33 | The sorted organization IDs. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| description | String | test | The description of the organization. |
| dtOrgId | Integer | 1 | This parameter is deprecated. |
| extraInfo | String | 123 | This parameter is deprecated. |
| id | Integer | 2 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| personNum | Integer | 12 | The maximum number of users. |

| resourceGroupNum | Integer | 10 | The maximum number of resource sets. |
|---|---|---|---|
| status | String | active | Indicates whether the organization is valid. |
| supportRegionList | List | ["cn-qingdao-****-d01"] | The list of zones. |
| supportRegions | String | cn-qingdao-****-d01 | The list of zones. |
| uuid | String | asd123 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The user who created the resource set. |
| description | String | test | The description of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| gmtModified | Long | 1606791494471 | The time when the resource set was modified. |
| id | Integer | 1 | The ID of the resource set. |
| modifier | String | admin | The user who modified the resource set. |
| organizationId | Integer | 1 | The ID of the organization. |
| organizationName | String | testz | The name of the organization. |
| resourceGroupName | String | restest _ | The name of the resource set. |
| resourceGroupType | Integer | 1 | The type of the resource set. |
| rsId | String | 123a | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | String | true | Indicates whether the role is valid. |
| arId | String | 123a | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | 132 | The user who modified the role. |

| organizationVisibility | String | organizationVisibility.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| privilegeCodes | List | ["123"] | The list of permission codes. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| systemPrivilegeCodes | List | ["123"] | The list of system permission codes. |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| backendAccountType | String | RamUser | The type of the account that is mapped in the backend. AscmUser: the user who is visible to customers in the Apsara Uni- manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 123412341231 | The mobile number of the user. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role for the user. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| description | String | test | The description of the user. |
| dtUserId | Integer | 1 | This parameter is deprecated. |
| email | String | 1***@123.com | The email address of the user. |
| enableDingTalk | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortMessage | Boolean | false | Indicates whether notifications by using text messages are enabled. |

| extraInfo | String | 1 | This parameter is deprecated. |
|---|---|---|---|
| id | Integer | 1 | The ID of the user. |
| loginName | String | admin | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationCode | String | 86 | The country code. |
| multiCloudStatus | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| parentPk | String | 1234123 | The primary key of the Apsara Stack tenant account. |
| password | String | afarqwedf | The password of the user. |
| pk | String | 123 | The primary key. |
| telephoneNum | String | 123123123 | The landline number of the user. |
| userLoginCtrlId | Integer | 1 | The ID of the logon control. |
| username | String | admin | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles for the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | ROLERESOURCEUSER _ _ | The code of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | 123 | The user who modified the role. |
| organizationVisibility | String | defaultRole.resourceUser.descript ion | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganizationId | String | 123 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndSubOrgs | The management permissions. |

| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
|---|---|---|---|
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | String | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/listUsersInUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"UserGroupId": "123"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <cellphoneNum>18888888888</cellphoneNum> <telephoneNum>12345678</telephoneNum> <enableDingTalk>false</enableDingTalk> <displayName>test</displayName> <description>description</description> <parentPk>1689406703302180</parentPk> <lastLoginTime>162314151313</lastLoginTime> <default>false</default> <deleted>false</deleted> <loginName>123</loginName> <mobileNationCode>86</mobileNationCode> <id>1</id> <enableEmail>false</enableEmail> <enableShortMessage>false</enableShortMessage> <email>1***@122.com</email> <status>active</status> <primaryKey>212530506704030000</primaryKey> <userGroupRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>123</arId> <code>1</code> <description>role_test</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>false</default> <ownerOrganizationId>2</ownerOrganizationId> <enable>true</enable> <roleName>test</roleName> <roleLevel>1</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> </userGroupRoles> <userRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>123</muserId> <arId>123</arId> <code>ROLE_RESOURCE_USER</code> <description>test</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>false</default> <ownerOrganizationId>123</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <roleLevel>1</roleLevel> <id>1</id> <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility> </userRoles> <accessKeys> <muserId>admin</muserId> |   |

```xml
        <muserId>admin</muserId>
        <CreateTime>1606675230000</CreateTime>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <mtime>1606675230000</mtime>
        <type>1</type>
        <accesskeySecret>**************</accesskeySecret>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <dtUserId>1</dtUserId>
        <status>active</status>
        <accesskeyId>JGdgSN2p******</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>1231</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <cuserId>admin</cuserId>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <privilegeCodes>["123"]</privilegeCodes>
        <systemPrivilegeCodes>["123"]</systemPrivilegeCodes>
    </roles>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>as</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>test</roleName>
        <roleLevel>2</roleLevel>
        <id>1</id>
        <cuserId>admin</cuserId>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <muserId>admin</muserId>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <name>default.loginpolicy</name>
        <rule>allow</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>111</lpId>
        <cuserId>admin</cuserId>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <timeRanges>
            <startTime>10:20</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>11:20</endTime>
        </timeRanges>
    </loginPolicy>
    <organization>
        <dtOrgId>1</dtOrgId>
        <muserId>admin</muserId>
        <internal>false</internal>
        <level>1</level>
        <description>aa</description>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <personNum>12</personNum>
        <mtime>15123222</mtime>
        <uuid>1231231</uuid>
        <parentId>1</parentId>
        <multiCloudStatus>master</multiCloudStatus>
        <childrenOrder>343,44,33</childrenOrder>
        <name>test</name>
```

```xml
        <ctime>1622311</ctime>
        <alias>test</alias>
        <resourceGroupNum>10</resourceGroupNum>
        <id>1</id>
        <cuserId>admin</cuserId>
        <status>active</status>
        <extraInfo>aaa</extraInfo>
        <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
    </organization>
    <userGroups>
        <organizationId>1</organizationId>
        <groupName>group_test</groupName>
        <augId>1231</augId>
        <createTimeStamp>1606791494471</createTimeStamp>
        <description>test</description>
        <id>123</id>
        <resourceSets>
            <organizationId>1</organizationId>
            <creator>admin</creator>
            <gmtModified>1606791494471</gmtModified>
            <resourceGroupName>res_test</resourceGroupName>
            <organizationName>testz</organizationName>
            <gmtCreated>1606791494471</gmtCreated>
            <modifier>admin</modifier>
            <rsId>123a</rsId>
            <description>test</description>
            <resourceGroupType>1</resourceGroupType>
            <id>1</id>
        </resourceSets>
        <users>
            <backendAccountType>RamUser</backendAccountType>
            <telephoneNum>123123123</telephoneNum>
            <enableDingTalk>false</enableDingTalk>
            <description>test</description>
            <parentPk>1234123</parentPk>
            <organizationId>1</organizationId>
            <default>true</default>
            <password>afarqwedf</password>
            <loginTime>1606791494471</loginTime>
            <userLoginCtrlId>1</userLoginCtrlId>
            <loginName>admin</loginName>
            <id>1</id>
            <enableShortMessage>false</enableShortMessage>
            <defaultRoleId>1</defaultRoleId>
            <email>1***@123.com</email>
            <cellphoneNum>123412341231</cellphoneNum>
            <accountType>1</accountType>
            <active>true</active>
            <dtUserId>1</dtUserId>
            <multiCloudStatus>master</multiCloudStatus>
            <deleted>false</deleted>
            <pk>123</pk>
            <mobileNationCode>86</mobileNationCode>
            <enableEmail>false</enableEmail>
            <extraInfo>1</extraInfo>
            <username>admin</username>
        </users>
        <roles>
            <roleRange>roleRange.orgAndSubOrgs</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>132</muserId>
            <arId>123a</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>false</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>test</roleName>
            <roleLevel>1</roleLevel>
            <id>1</id>
            <cuserId>admin</cuserId>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <privilegeCodes>["123"]</privilegeCodes>
            <systemPrivilegeCodes>["123"]</systemPrivilegeCodes>
        </roles>
        <organization>
            <dtOrgId>1</dtOrgId>
            <muserId>admin</muserId>
            <internal>false</internal>
            <level>1</level>
            <description>test</description>
            <supportRegions>cn-qingdao-****-d01</supportRegions>
            <personNum>12</personNum>
            <mtime>1606791494471</mtime>
            <uuid>asd123</uuid>
```

```xml
            <parentId>1</parentId>
            <multiCloudStatus>master</multiCloudStatus>
            <childrenOrder>343,44,33</childrenOrder>
            <name>test</name>
            <ctime>1606791494471</ctime>
            <alias>test</alias>
            <resourceGroupNum>10</resourceGroupNum>
            <id>2</id>
            <cuserId>admin</cuserId>
            <status>active</status>
            <extraInfo>123</extraInfo>
            <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
        </organization>
    </userGroups>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": {"cellphoneNum":"18888888888","telephoneNum":"12345678","enableDingTalk":"false","displayName":"test","description":"description","parentPk":"16 703302180","lastLoginTime":"162314151313","default":"false","deleted":"false","loginName":"123","mobileNationCode":"86","id":"1","enableEmail":" ","enableShortMessage":"false","email":"1***@122.com","status":"active","primaryKey":"212530506704030000","userGroupRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123","code":"1","description":"role_test","active":"true","r pe":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"2","enable":"true","roleName":"test","roleLevel":"1","id":"1","organizationVisibili organizationVisibility.global"}],"userRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"123","arId":"123","code":"ROLE_RESOURCE_USER","description":"test","active" e","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"123","enable":"true","roleName":"defaultRole.resourceUser.name","roleLeve ","id":"1","organizationVisibility":"defaultRole.resourceUser.description"}],"accessKeys": [{"muserId":"admin","CreateTime":"1606675230000","ctime":"1606675230000","id":"1","mtime":"1606675230000","type":"1","accesskeySecret":"JGdgSN2p *","region":"cn-qingdao-env17-d01","cuserId":"admin","dtUserId":"1","status":"active","accesskeyId":"**************"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"1231","code":"ROLE_RESOURCE_USER","description":"role_test", ve":"true","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"role_test","roleLevel":"1","id":"1 serId":"admin","organizationVisibility":"organizationVisibility.global","privilegeCodes":"[\"123\"]","systemPrivilegeCodes":" [\"123\"]"}],"defaultRole": {"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"111","code":"ROLE_RESOURCE_USER","description":"as","active": ","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":"2","id":"1","cuserId":"a ,"organizationVisibility":"organizationVisibility.global"},"loginPolicy": {"muserId":"admin","default":"false","ownerOrganizationId":"1","enable":"true","name":"default.loginpolicy","rule":"allow","id":"1","organizatio bility":"organizationVisibility.global","lpId":"111","cuserId":"admin","ipRanges": {"protocol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"},"timeRanges": {"startTime":"10:20","loginPolicyId":"1","endTime":"11:20"}},"organization": {"dtOrgId":"1","muserId":"admin","internal":"false","level":"1","description":"aa","supportRegions":"cn-qingdao-****- d01","personNum":"12","mtime":"15123222","uuid":"1231231","parentId":"1","multiCloudStatus":"master","childrenOrder":"343,44,33","name":"test"," ":"1622311","alias":"test","resourceGroupNum":"10","id":"1","cuserId":"admin","status":"active","extraInfo":"aaa","supportRegionList":"[\"cn-q ingdao-****-d01\"]"},"userGroups": {"organizationId":"1","groupName":"group_test","augId":"1231","createTimeStamp":"1606791494471","description":"test","id":"123","resourceSets": [{"organizationId":"1","creator":"admin","gmtModified":"1606791494471","resourceGroupName":"res_test","organizationName":"testz","gmtCreated":"1 1494471","modifier":"admin","rsId":"123a","description":"test","resourceGroupType":"1","id":"1"}],"users": [{"backendAccountType":"RamUser","telephoneNum":"123123123","enableDingTalk":"false","description":"test","parentPk":"1234123","organizationId": default":"true","password":"afarqwedf","loginTime":"1606791494471","userLoginCtrlId":"1","loginName":"admin","id":"1","enableShortMessage":"fals efaultRoleId":"1","email":"1***@123.com","cellphoneNum":"123412341231","accountType":"1","active":"true","dtUserId":"1","multiCloudStatus":"maste eleted":"false","pk":"123","mobileNationCode":"86","enableEmail":"false","extraInfo":"1","username":"admin"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"132","arId":"123a","code":"ROLE_RESOURCE_USER","description":"test","active ue","roleType":"ROLETYPE_ASCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":"1","id":"1","cuserId": n","organizationVisibility":"organizationVisibility.global","privilegeCodes":"[\"123\"]","systemPrivilegeCodes":"[\"123\"]"}],"organization":{ "dtOrgId":"1","muserId":"admin","internal":"false","level":"1","description":"test","supportRegions":"cn-qingdao-****- d01","personNum":"12","mtime":"1606791494471","uuid":"asd123","parentId":"1","multiCloudStatus":"master","childrenOrder":"343,44,33","name":"tes time":"1606791494471","alias":"test","resourceGroupNum":"10","id":"2","cuserId":"admin","status":"active","extraInfo":"123","supportRegionList": [\"cn-qingdao-****-d01\"]"}}},"success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.4 AddUsersToUserGroup

Adds users to a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/addUsersToUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| LoginNameList | Json | Body | Yes | ["test"] | The list of users. |
| UserGroupId | Integer | Body | Yes | 1 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/addUsersToUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"LoginNameList": "["test"]", "UserGroupId": "1"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.5 AddRoleToUserGroup

Adds a role to one or more user groups.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/addRoleToUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| UserGroupId | Integer | Body | Yes | 1 | The ID of the user group. |
| UserGroupIdList | Json | Body | Yes | ["1","2"] | The IDs of the user groups. |
| RoleId | Integer | Body | No | 1 | The ID of the role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |

| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
|---|---|---|---|
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/addRoleToUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"UserGroupId": "1", "UserGroupIdList": "["1","2"]"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.6 AddResourceSetToUserGroup

Binds a resource set to a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/addResourceSetToUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AscmRoleId | String | Body | Yes | 1 | The ID of the role in the Apsara Uni-manager Management Console. |
| ResourceSetId | Integer | Body | Yes | 1 | The ID of the resource set. |
| UserGroupId | Integer | Body | No | 1 | The ID of the user group. |
| UserGroupIdList | Json | Body | No | ["1","2"] | The list of user groups. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/addResourceSetToUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"AscmRoleId": "1", "ResourceSetId": "1"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.7 RemoveUsersFromUserGroup

Removes users from a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/removeUsersFromUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| LoginNameList | Json | Body | Yes | ["admin"] | The logon names of the users. |
| UserGroupId | Integer | Body | Yes | 12 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/removeUsersFromUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"LoginNameList": "", "UserGroupId": ""
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.8 RemoveRoleFromUserGroup

Removes a role from a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/removeRoleFromUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RoleId | Integer | Body | Yes | 1 | The ID of the role. |
| UserGroupId | Integer | Body | Yes | 2 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/removeRoleFromUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"RoleId": "1", "UserGroupId": "2"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.9 RemoveResourceSetFromUserGroup

Deletes a resource set from a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/removeResourceSetFromUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ResourceSetId | Integer | Body | Yes | 1 | The ID of the resource set. |
| UserGroupId | Integer | Body | Yes | 1 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/removeResourceSetFromUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"ResourceSetId": "1", "UserGroupId": "1"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

###### 4.3.1.5.10 DeleteUserGroup

Deletes a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/deleteUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|

| UserGroupId | Integer | Body | Yes | 123 | The ID of the user group. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/deleteUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"UserGroupId": "123"
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

##### 4.3.1.6 Logon policies

###### 4.3.1.6.1 AddLoginPolicy

Creates a logon policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddLoginPolicy | The operation that you want to perform. Set the value to AddLoginPolicy. |
| Name | String | Yes | testlp | The name of the logon policy. |
| Description | String | No | just for test | The description of the logon policy. |
| Rule | String | No | deny | The rule of the logon policy. Valid values: Allow and Deny. |
| ipRanges | Json | No | {"IpRanges": [ { " ipRange": "1.1.1.0/24" }, { " ipRange": "2.2.2.5/24" } ]} | The list of CIDR blocks. |
| timeRanges | Json | No | {"TimeRanges ": [ { "startTime ": "11:00", " endTime": " 13:35" }, { " startTime": "12: 00", "endTime": "12:30" } ]} | The list of time ranges. |
| Enable | Boolean | No | true | Specifies whether the logon policy is valid. |

| OrganizationVisibility | String | No | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| ipRanges | Array of ipRang |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | Integer | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | defaultLoginPolicy.name | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| message | String | success | The error message. |
| pureListData | Boolean | true | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddLoginPolicy &Name=testlp &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <ipRanges> <ipRange>0.0.0.0/0</ipRange> <protocol>IPV4</protocol> <loginPolicyId>1</loginPolicyId> </ipRanges> <muserId>admin</muserId> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1</loginPolicyId> <endTime>24:00</endTime> </timeRanges> <enable>true</enable> <name>defaultLoginPolicy.name</name> <rule>ALLOW</rule> <organizationVisibility>organizationVisibility.global</organizationVisibility> <lpId>111</lpId> <cuserId>admin</cuserId> </data> <success>true</success> <pureListData>true</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "ipRanges": [ { "ipRange": "0.0.0.0/0", "protocol": "IPV4", "loginPolicyId": "1" } ], "muserId": "admin", "default": "true", "ownerOrganizationId": "1", "timeRanges": [ { "startTime": "00:00", "loginPolicyId": "1", "endTime": "24:00" } ], "enable": "true", "name": "defaultLoginPolicy.name", "rule": "ALLOW", "organizationVisibility": "organizationVisibility.global", "lpId": "111", "cuserId": "admin" }, "success": "true", "pureListData": "true", "message": "success" } |   |

###### 4.3.1.6.2 CheckLoginPolicy

Checks a logon policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CheckLoginPolicy | The operation that you want to perform. Set the value to CheckLoginPolicy. |

| Ip | String | Yes | 1.1.1.1 | The IP address to be checked. Logon policies include whitelist and blacklist policies. A whitelist policy is used to check the IP addresses from which you can log on. A blacklist policy is used to check the IP addresses from which you cannot log on. |
|---|---|---|---|---|
| LoginName | String | Yes | testu | The logon name to be checked. |
| Time | Long | No | 1575889112 | The timestamp to be checked. By default, the current system timestamp is used. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Boolean | true | The response. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CheckLoginPolicy &Ip=1.1.1.1 &LoginName=testu &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>true</data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": "true", "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.6.3 ListLoginPolicies

Queries the list of logon policies.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListLoginPolicies | The operation that you want to perform. Set the value to ListLoginPolicies. |

| Name | String | No | test | The name of the logon policy. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRang |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 1111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | deaultLogin | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| userCount | Integer | 12 | The number of users who use the logon policy. |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |

| currentPage | Integer | 1 | The page number of the returned page. |
|---|---|---|---|
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 39 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListLoginPolicies &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <muserId>admin</muserId> <default>true</default> <userCount>12</userCount> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <name>Indicates whether only data is returned and other parameters are not returned.</name> <rule>ALLOW</rule> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <lpId>1111</lpId> <cuserId>admin</cuserId> </data> <data> <ipRanges> <ipRange>0.0.0.0/0</ipRange> <protocol>IPV4</protocol> <loginPolicyId>1</loginPolicyId> </ipRanges> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1</loginPolicyId> <endTime>24:00</endTime> </timeRanges> </data> <success>true</success> <pageInfo> <total>39</total> <totalPage>2</totalPage> <pageSize>20</pageSize> <currentPage>1</currentPage> </pageInfo> <pureListData>false</pureListData> <message>success</message> |   |

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": [
```

`{`

```json
            "muserId": "admin",
            "default": "true",
            "userCount": "12",
            "ownerOrganizationId": "1",
            "enable": "true",
            "name": Indicates whether only data is returned and other parameters are not returned.
            "rule": "ALLOW",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "1111",
            "cuserId": "admin"
```

`},` `{`

```json
            "ipRanges": [
```

`{`

```json
                    "ipRange": "0.0.0.0/0",
                    "protocol": "IPV4",
                    "loginPolicyId": "1"
```

`],`

```json
            "timeRanges": [
```

`{`

```json
                    "startTime": "00:00",
                    "loginPolicyId": "1",
                    "endTime": "24:00"
```

`]` `],`

```json
    "success": "true",
    "pageInfo": {
        "total": "39",
        "totalPage": "2",
        "pageSize": "20",
        "currentPage": "1"
```

`},`

```json
    "pureListData": "false",
    "message": "success"
```

###### 4.3.1.6.4 ModifyLoginPolicy

Modifies a logon policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoginPolicy | The operation that you want to perform. Set the value to ModifyLoginPolicy. |
| Id | Integer | Yes | 2 | The ID of the logon policy. |
| Name | String | No | testtttt | The new name of the logon policy. |
| Description | String | No | tttt | The new description of the logon policy. |
| Rule | String | No | allow | The rule of the logon policy. Valid values: Allow and Deny. |
| ipRanges | Json | No | { "ipRanges": [ { "ipRange": "0.0.0.0/0", "loginPolicyId": 1, "protocol": "IPV4" } ]} | The list of new CIDR blocks. |
| timeRanges | Json | No | {"timeRanges": [ { "endTime": "24:00", "loginPolicyId": 1, "startTime": "00:00" } ]} | The list of new time ranges. |
| Enable | Boolean | No | true | Specifies whether to enable the logon policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| cuserId | String | admin | The creator of the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRang |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | lp-1010e681dc790aab5041000y | The ID of the logon policy. |
| mtime | Long | 1608175299345 | The time when the logon policy was modified. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | testNew | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range for the query. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoginPolicy &Id=2 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <muserId>admin</muserId> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1</loginPolicyId> <endTime>24:00</endTime> </timeRanges> <rule>ALLOW</rule> <mtime>1608175299345</mtime> <lpId>lp-1010e681dc790aab5041000y</lpId> <ipRanges> <ipRange>0.0.0.0/0</ipRange> <protocol>IPV4</protocol> <loginPolicyId>1</loginPolicyId> </ipRanges> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <name>testNew</name> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "muserId": "admin", "timeRanges": [ { "startTime": "00:00", "loginPolicyId": "1", "endTime": "24:00" } ], "rule": "ALLOW", "mtime": "1608175299345", "lpId": "lp-1010e681dc790aab5041000y", "ipRanges": [ { "ipRange": "0.0.0.0/0", "protocol": "IPV4", "loginPolicyId": "1" } ], "default": "true", "ownerOrganizationId": "1", "enable": "true", "name": "testNew", "id": "1", "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" }, "success": "true", "pureListData": "false", "message": "success" } |   |

###### 4.3.1.6.5 GetLoginPolicyById

Queries the information of a logon policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetLoginPolicyById | The operation that you want to perform. Set the value to GetLoginPolicyById. |
| Id | Integer | Yes | 1 | The ID of the logon policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | defaultLoginPolicy.name | The name of the logon policy. |
| organizationVisibility | String | organizationVisibility.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganizationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range for the query. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetLoginPolicyById &Id=1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <ipRanges> <ipRange>0.0.0.0/0</ipRange> <protocol>IPV4</protocol> <loginPolicyId>1</loginPolicyId> </ipRanges> <muserId>admin</muserId> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1</loginPolicyId> <endTime>24:00</endTime> </timeRanges> <enable>true</enable> <name>defaultLoginPolicy.name</name> <rule>ALLOW</rule> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <lpId>111</lpId> <cuserId>admin</cuserId> </data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "ipRanges": [ { "ipRange": "0.0.0.0/0", "protocol": "IPV4", "loginPolicyId": "1" } ], "muserId": "admin", "default": "true", "ownerOrganizationId": "1", "timeRanges": [ { "startTime": "00:00", "loginPolicyId": "1", "endTime": "24:00" } ], "enable": "true", "name": "defaultLoginPolicy.name", "rule": "ALLOW", "id": "1", "organizationVisibility": "organizationVisibility.global", "lpId": "111", "cuserId": "admin" }, "success": "true", "pureListData": "false", "message": "success" } |   |

#### 4.3.2 Operations

##### 4.3.2.1 CreateQuota

You can call this operation to create a quota.

```json
    {"productName":"ECS",
    "quotaBody":{"totalCpu":100,"totalMem":100,"totalGpu":100,
    "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100}}
```

```json
{"productName":"OSS",
    "quotaBody":{"totalAmount":100}}
 {"productName":"VPC",
    "quotaBody":{"totalVPC":100}}
```

ApsaraDB RDS

```json
 {"productName":"RDS",
    "quotaBody":{"totalCpu":100,"totalMem":100,"totalDisk":100}}
{"productName":"SLB",
    "quotaBody":{"totalVipInternal":100,"totalVipPublic":100}}
```

MaxCompute (ODPS)

```json
{"productName":"ODPS",
    "quotaBody":{"totalCu":100,"totalDisk":100}}
{"productName":"EIP",
    "quotaBody":{"totalEIP":100}}
```

AnalyticDB for MySQL (ADB)

```json
  {"productName": "ADB",
       "quotaBody":{"totalCpu": 100, "totalMem": 100, "totalDisk":100}}
```

AnalyticDB for PostgreSQL (GPDB)

```json
{"productName": "GPDB",
  "quotaBody":{"totalCpu": 100, "totalMem": 100, "totalDisk":100}}
```

KVStore for Redis (R-kvstore)

```json
 {"productName": "R-kvstore",       "quotaBody":{"totalMem": 100}}
```

PolarDB-X (DRDS)

```json
 {"productName": "DRDS",
       "quotaBody":{"totalCpu": 100}}
```

Tablestore (OTS)

```json
   {"productName": "OTS",
      "quotaBody":{"totalDisk": 100}}
```

Apsara File Storage NAS

```json
 {"productName": "NAS",
       "quotaBody":{"totalDisk": 100}}
```

ApsaraDB for MongoDB (DDS)

```json
 {"productName": "DDS",
        "quotaBody":{"totalCpu": 100, "totalMem": 100, "totalDisk":100}}
```

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateQuota | The operation that you want to perform. Set the value to CreateQuota. |
| ProductName | String | Yes | ECS | The name of the service. Valid values: ECS, OSS, VPC, RDS, SLB, ODPS, EIP, ADB, GPDB, R-kvstore, DRDS, OTS, NAS, and DDS. |
| QuotaBody | Json | Yes | {"totalCpu":100,"totalMem": 100,"totalGpu":100, "totalDiskcloudssd":100,"to _ _ talDiskcloudefficiency":100 _ _ } | The parameters of the quota to update. The parameters vary with the specific service. ECS: {"totalCpu":100,"totalMem":100,"totalGpu":100,"total Disk_cloud_ssd":100,"totalDisk_cloud_efficiency":100 } OSS: {"totalAmount":100} VPC: {"totalVPC":100} RDS: {"totalCpu":100,"totalMem":100,"totalDisk":100} SLB: {"totalVipInternal":100,"totalVipPublic":100} ODPS: {"totalCu":100,"totalDisk":100} EIP: {"totalEIP":100} |
| QuotaType | String | Yes | organization | Valid values: organization and resourceGroup. |
| QuotaTypeId | Integer | Yes | 1 | The ID of the quota type. Specify an organization ID when the QuotaType parameter is set to organization. Specify a resource set ID when the QuotaType parameter is set to resourceGroup. |
| RegionName | String | Yes | cn-******-****-d01 | The region name. |
| RequestId | String | No | d0c6ed24-45af-4703-866f- 5103302b9a72 | The ID of the request. |
| ClusterName | String | No | "" | The name of the cluster. This reserved parameter is optional and can be left empty. |
| TargetType | String | No | MySQL | To create a quota for ApsaraDB RDS, specify the name of the engine. Valid values: MySQL and SQLServer. This parameter is optional and can be left empty for other services. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| data | Struct |   | The response. |
| allocateVPC | Integer | 1 | The number of allocated virtual private clouds (VPCs). |
| cluster | String | cn-qingdao-env17-d01 | The cluster. |
| ctime | Float | 1608519825999 | The creation time. |
| dtFlag | Boolean | false | The DTCenter flag. |
| id | Integer | 1 | The ID of the primary key. |
| quotaType | String | organization | The type of the quota. |
| quotaTypeId | Integer | 1 | The ID of the quota. |
| region | String | cn-qingdao-env17-d01 | The region. |

| targetType | String | mysql | The type of the cluster. |
|---|---|---|---|
| totalVPC | Integer | 10 | The total number of VPCs. |
| usedVPC | Integer | 1 | The number of used VPCs. |
| message | String | 200 | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=CreateQuota &ProductName=ECS &QuotaBody={"totalCpu":100,"totalMem":100,"totalGpu":100, "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100} &QuotaType=organization &QuotaTypeId=1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <quotaType>organization</quotaType> <cluster>cn-qingdao-env17-d01</cluster> <totalVPC>10</totalVPC> <dtFlag>false</dtFlag> <quotaTypeId>1</quotaTypeId> <usedVPC>1</usedVPC> <ctime>1608519825999</ctime> <allocateVPC>1</allocateVPC> <targetType>mysql</targetType> <id>1</id> <region>cn-qingdao-env17-d01</region> </data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "quotaType": "organization", "cluster": "cn-qingdao-env17-d01", "totalVPC": "10", "dtFlag": "false", "quotaTypeId": "1", "usedVPC": "1", "ctime": "1608519825999", "allocateVPC": "1", "targetType": "mysql", "id": "1", "region": "cn-qingdao-env17-d01" }, "success": "true", "requestId": "111", "pureListData": "false", "message": "200" } |   |

##### 4.3.2.2 DescribeGpdbModifiableInstanceType

You can call this operation to query the AnalyticDB for PostgreSQL instance types that can be upgraded or downgraded.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGpdbModifiableInsta nceType | The operation that you want to perform. Set the value to DescribeGpdbModifiableInstanceType. |
| instanceId | String | Yes | sdfsdfsdfsfdsdf | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |
| result | Array of dataItem |   | The collection of results. |
| baseVersion | String | 3.13 | The version of the instance type. |
| cpu | String | 1 | The number of vCPUs. |
| engineVersion | String | 5.6 | The engine version of the instance. |
| gmtCreate | String | 2020-12-23 19:08:15 | The creation time. |
| gmtModified | String | 2020-12-23 19:08:15 | The modification time. |
| label | String | "" | Indicates whether the field is internationalized. Valid values: true and false. |
| memory | String | 4 | The memory size. |
| node | String | "" | The node. |
| regionId | String | cn-qingdao-env66-d01 | The ID of the region. |
| resourceType | String | GDB | The resource type. |
| specFrom | String | system | The source of the instance type. |
| specification | String | gdb.r.13xlarge | The instance type. |
| status | String | Available | Indicates whether the instance type is available. |
| storage | String | 20 | The storage. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeGpdbModifiableInstanceType &instanceId=sdfsdfsdfsfdsdf &<Common request parameters>
```

Sample success responses `XML` format

```xml
<data>
    <result>
        <engineVersion>5.6</engineVersion>
        <gmtModified>2020-12-23 19:08:15</gmtModified>
        <memory>4</memory>
        <baseVersion>3.13</baseVersion>
        <cpu>1</cpu>
        <specification>gdb.r.13xlarge</specification>
        <specFrom>system</specFrom>
        <storage>20</storage>
        <label>""</label>
        <gmtCreate>2020-12-23 19:08:15</gmtCreate>
        <node>""</node>
        <regionId>cn-qingdao-env66-d01</regionId>
        <status>Available</status>
        <resourceType>GDB</resourceType>
    </result>
    <success>true</success>
    <status>200</status>
</data> <host>""</host> <status>200</status>
```

| JSON | format |
|---|---|
| { "data": { "result": [ { "engineVersion": "5.6", "gmtModified": "2020-12-23 19:08:15", "memory": "4", "baseVersion": "3.13", "cpu": "1", "specification": "gdb.r.13xlarge", "specFrom": "system", "storage": "20", "label": """", "gmtCreate": "2020-12-23 19:08:15", "node": """", "regionId": "cn-qingdao-env66-d01", "status": "Available", "resourceType": "GDB" } ], "success": "true", "status": "200" }, "host": """", "status": "200" } |   |

##### 4.3.2.3 UpdateQuota

You can call this operation to update a quota.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateQuota | The operation that you want to perform. Set the value to UpdateQuota. |
| ProductName | String | Yes | ECS | The name of the service. Valid values: ECS, OSS, VPC, RDS, SLB, ODPS, and EIP. |

| QuotaBody | Json | Yes | {"totalCpu":100,"totalMem": 100,"totalGpu":100, "totalDiskcloudssd":100,"to _ _ talDiskcloudefficiency":100 _ _ } | The parameters of the quota to update. The parameters vary with the specific service. ECS: {"totalCpu":100,"totalMem":100,"totalGpu":100,"total Disk_cloud_ssd":100,"totalDisk_cloud_efficiency":100 } OSS: {"totalAmount":100} VPC: {"totalVPC":100} RDS: {"totalCpu":100,"totalMem":100,"totalDisk":100} SLB: {"totalVipInternal":100,"totalVipPublic":100} ODPS: {"totalCu":100,"totalDisk":100} EIP: {"totalEIP":100} |
|---|---|---|---|---|
| QuotaType | String | Yes | organization | The type of the quota. Valid values: organization and resourceGroup. |
| QuotaTypeId | Integer | Yes | 1 | The ID of the quota type. Specify an organization ID when the QuotaType parameter is set to organization. Specify a resource set ID when the QuotaType parameter is set to resourceGroup. |
| RegionName | String | Yes | cn-*******-****-d01 | The region name. |
| RequestId | String | No | 84319b92-835e-4aeb-9190- 0c12c9****** | The ID of the request. |
| ClusterName | String | No | TEST | The name of the cluster. This reserved parameter is optional and can be left empty. |
| TargetType | String | No | MySQL |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| data | Struct |   | The response. |
| allocateVPC | Integer | 1 | The number of allocated virtual private clouds (VPCs). |
| cluster | String | cn-qingdao-env17-d01 | The cluster. |
| ctime | Float | 1608519825999 | The creation time. |
| dtFlag | Boolean | false | The DTCenter flag. |
| id | Integer | 1 | The ID of the primary key. |
| quotaType | String | organization | The type of the quota. |
| quotaTypeId | Integer | 1 | The ID of the quota. |
| region | String | cn-qingdao-env17-d01 | The region. |
| targetType | String | mysql | The type of the cluster. |
| totalVPC | Integer | 10 | The total number of VPCs. |
| usedVPC | Integer | 1 | The number of used VPCs. |

| message | String | 200 | The message. |
|---|---|---|---|
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=UpdateQuota &ProductName=ECS &QuotaBody={"totalCpu":100,"totalMem":100,"totalGpu":100, "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100} &QuotaType=organization &QuotaTypeId=1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <quotaType>organization</quotaType> <cluster>cn-qingdao-env17-d01</cluster> <totalVPC>10</totalVPC> <dtFlag>false</dtFlag> <quotaTypeId>1</quotaTypeId> <usedVPC>1</usedVPC> <ctime>1608519825999</ctime> <allocateVPC>1</allocateVPC> <targetType>mysql</targetType> <id>1</id> <region>cn-qingdao-env17-d01</region> </data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "quotaType": "organization", "cluster": "cn-qingdao-env17-d01", "totalVPC": "10", "dtFlag": "false", "quotaTypeId": "1", "usedVPC": "1", "ctime": "1608519825999", "allocateVPC": "1", "targetType": "mysql", "id": "1", "region": "cn-qingdao-env17-d01" }, "success": "true", "requestId": "111", "pureListData": "false", "message": "200" } |   |

##### 4.3.2.4 DeleteQuota

You can call this operation to delete a quota.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DeleteQuota | The operation that you want to perform. Set the value to DeleteQuota. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| message | String | 200 | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteQuota &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "success": "true", "requestId": "111", "pureListData": "false", "message": "200" } |   |

##### 4.3.2.5 GetQuota

You can call this operation to query a quota.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetQuota | The operation that you want to perform. Set the value to GetQuota. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| data | Struct |   | The response. |

| allocateAmount | Integer | 1 | The number of allocated quotas. |
|---|---|---|---|
| cluster | String | cn-qingdao-env17-d01 | The cluster. |
| ctime | Float | 1608519825999 | The creation time. |
| cuserId | String | admin | The creator. |
| dtFlag | Boolean | false | The DTCenter flag. |
| id | Integer | 1 | The ID of the primary key. |
| muserId | String | admin | The modifier. |
| quotaType | String | organization | The type of the quota. |
| quotaTypeId | Integer | 1 | The ID of the quota. |
| region | String | cn-qingdao-env17-d01 | The region. |
| targetType | String | mysql | The type of the cluster. |
| totalAmount | Integer | 10 | The total number of quotas. |
| usedAmount | Integer | 1 | The number of used quotas. |
| message | String | 200 | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=GetQuota &ProductName=ECS &QuotaType=organization &QuotaTypeId=1 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <muserId>admin</muserId> <cluster>cn-qingdao-env17-d01</cluster> <quotaTypeId>1</quotaTypeId> <usedAmount>1</usedAmount> <allocateAmount>1</allocateAmount> <targetType>mysql</targetType> <totalAmount>10</totalAmount> <quotaType>organization</quotaType> <dtFlag>false</dtFlag> <ctime>1608519825999</ctime> <id>1</id> <region>cn-qingdao-env17-d01</region> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "muserId": "admin", "cluster": "cn-qingdao-env17-d01", "quotaTypeId": "1", "usedAmount": "1", "allocateAmount": "1", "targetType": "mysql", "totalAmount": "10", "quotaType": "organization", "dtFlag": "false", "ctime": "1608519825999", "id": "1", "region": "cn-qingdao-env17-d01", "cuserId": "admin" }, "success": "true", "requestId": "111", "pureListData": "false", "message": "200" } |   |

##### 4.3.2.6 MeteringQuery

You can call this operation to query the metering data.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MeteringQuery | The operation that you want to perform. Set the value to MeteringQuery. |
| startTime | String | Yes | 2019-10-10T00:00:00Z | The start of the time range for the query. The time must be in UTC. |
| endTime | String | Yes | 2019-10-10T01:00:00Z | The end of the time range for the query. The time must be in UTC. |
| orgId | String | Yes | 1 | The ID of the organization. |
| pageSize | Integer | No | 500 | The number of entries to return on each page. Maximum value: 1000. |
| productName | String | Yes | ECS | The name of the service. Valid values: ECS, OSS, RDS, SLB, EIP, and VPC. |
| isParentId | Integer | Yes | 0 | A value of 1 specifies that the metering data of subordinate organizations under this organization is returned. If you do not specify this parameter or set the parameter to a value other than 1, only the metering data of this organization is returned. |
| resourceGId | String | No | test | The metering data of the specified resource set. By fault, if this parameter is empty or not specified, the metering data of all the resource sets in the specified organization is queried. Note If refined query is not required, we recommend that you do not specify the resourceGId, region, and insId parameters. You can query all the metering data of the specified organization to improve efficiency. |
| region | String | No | test | The metering data of the specified cluster. Note If refined query is not required, we recommend that you do not specify the resourceGId, region, and insId parameters. You can query all the metering data of the specified organization to improve efficiency. |

| insId | String | No | test | The metering data of the specified instance. Note If refined query is not required, we recommend that you do not specify the resourceGId, region, and insId parameters. You can query all the metering data of the specified organization to improve efficiency. |
|---|---|---|---|---|
| token | String | No | test | The token returned as an offset when the data volume to be queried is greater than the value of the pageSize parameter. You can query the data of the next page after you enter the token for the next request. You can ignore this parameter or enter an empty string for the first query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| message | String | success | The returned information. |
| requestId | String | sddsdsd | The ID of the request. |
| success | Normal | true | Indicates whether the call was successful. |
| token | String | {"InsId":"i- 9fx013f0ueoh5fzc8yww","Pos":"E CS00000000032000-01- _ _ 01T01:00:00Z","ResourceGId":"2" ,"RegionId":"cn-qingdao-env- d01"} | The token used to query data by page. You can query the data of the next page after you enter the token for the next request. |
| total | Integer | 100 | The amount of data returned for this query. |
| data | String |   | The response. |
| Pos | String | ECS00000000032000-01- _ _ 01T01:00:00Z | The primary key of the metering data. The primary key consists of the service name, organization ID, and start time. |
| OrgName | String | test | The name of the organization. |
| ResourceGId | Integer | test | The ID of the resource set. |
| ResourceGName | String | test | The name of the resource set. |
| InsId | String | i-h5i05vhigf256qxqmg4h | The ID of the instance. |
| RegionId | String | cn-qingdao-env3b-d02 | The ID of the region. |
| StartTime | String | 2019-12-16 06:00:00 | The start time of the metering data. |
| EndTime | String | 2019-12-16 07:00:00 | The end time of the metering data. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=MeteringQuery &startTime=2019-10-10T00:00:00Z &endTime=2019-10-10T01:00:00Z &orgId=1 &pageSize=500 &productName=ECS &isParentId=0 &<Common request parameters>
```

Sample success responses in JSON format `{`

```json
 "code": "200",
 "cost": 1104,
 "data": [
```

`{`

```json
     "Status": "Pending",
     "EndTime": "2019-12-16T07:00:00Z",
     "Memory": 8192,
     "StartTime": "2019-12-16T06:00:00Z",
     "Cpu": 4,
     "ResourceGId": "2",
     "OrgName": "katy",
     "GPUAmount": 0,
     "InstanceNetworkType": "vpc",
     "InstanceName": "",
     "InsId": "i-h5i05vhigf256qxqmg4h",
     "Pos": "ECS_0000000003_2019-12-16T06:00:00Z",
     "RegionId": "cn-qingdao-env3b-d02",
     "ResourceGName": "Default resource group",
     "InstanceType": "ecs.sn1ne.xlarge"
```

`},` `{`

```json
     "Status": "Stopped",
     "EndTime": "2019-12-16T07:00:00Z",
     "Memory": 65536,
     "StartTime": "2019-12-16T06:00:00Z",
     "Cpu": 8,
     "ResourceGId": "2",
     "OrgName": "katy",
     "GPUAmount": 0,
     "InstanceNetworkType": "vpc",
     "InstanceName": "master-02-k8s-for-cs-c7bf8128e65b84e1e95e650cb56dd****",
     "InsId": "i-h5i05vhigf27annjmgbz",
     "Pos": "ECS_0000000003_2019-12-16T06:00:00Z",
     "RegionId": "cn-qingdao-env3b-d02",
     "ResourceGName": "Default resource group",
     "InstanceType": "ecs.se1.2xlarge"
```

`},` `{`

```json
     "Status": "Running",
     "EndTime": "2019-12-16T07:00:00Z",
     "Memory": 65536,
     "StartTime": "2019-12-16T06:00:00Z",
     "Cpu": 8,
     "ResourceGId": "2",
     "OrgName": "katy",
     "GPUAmount": 0,
     "InstanceNetworkType": "vpc",
     "InstanceName": "worker-k8s-for-cs-c7bf8128e65b84e1e95e650cb56dd****",
     "InsId": "i-h5i05vhigf27atkmym9f",
     "Pos": "ECS_0000000003_2019-12-16T06:00:00Z",
     "RegionId": "cn-qingdao-env3b-d02",
     "ResourceGName": "Default resource group",
     "InstanceType": "ecs.se1.2xlarge"
```

`],`

```json
 "message": "success",
 "pageNumber": 1,
 "redirect": false,
 "requestId": "0a04160015765602607441591d0217",
 "size": 10,
 "success": true,
 "token": "xxxx",
 "total": 1000,
 "asapiRequestId": "47b3e68f-a87d-4222-8263-e8f6a7801e09"
```

##### 4.3.2.7 SelectCommonSpec

You can call this operation to query the specifications of a service by condition.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SelectCommonSpec | The operation that you want to perform. Set the value to SelectCommonSpec. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The dataset. |

| result | Array of dataItem |   | The collection of results. |
|---|---|---|---|
| baseVersion | String | 3.13 | The version of the specifications. |
| gmtCreate | String | 2019-10-27 17:47:27 | The creation time of the specifications. |
| gmtModified | String | 2019-10-27 17:47:27 | The modification time of the specifications. |
| pageOrder | String | 1 | The page order. |
| pageSize | Integer | 5 | The number of entries returned per page. |
| pageSort | String | null | The sorting of pages. |
| pageStart | Integer | 1 | The number of the page to query. Start from page 1. |
| regionId | String | cn-qingdao-env66-d01 | The ID of the region. |
| resourceType | String | RDS | The resource type. |
| specFrom | String | system | The source of the specifications. |
| status | String | Available | Indicates whether the specifications are available. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=SelectCommonSpec &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <data> <result> <gmtModified>2019-10-27 17:47:27</gmtModified> <pageOrder>1</pageOrder> <pageSort>null</pageSort> <regionId>cn-qingdao-env66-d01</regionId> <baseVersion>3.13</baseVersion> <pageStart>1</pageStart> <pageSize>5</pageSize> <specFrom>system</specFrom> <gmtCreate>2019-10-27 17:47:27</gmtCreate> <status>Available</status> <resourceType>RDS</resourceType> </result> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |   |

`JSON` format `{`

```json
    "data": {
        "result": [
```

`{`

```json
                "gmtModified": "2019-10-27 17:47:27",
                "pageOrder": "1",
                "pageSort": "null",
                "regionId": "cn-qingdao-env66-d01",
                "baseVersion": "3.13",
                "pageStart": "1",
                "pageSize": "5",
                "specFrom": "system",
                "gmtCreate": "2019-10-27 17:47:27",
                "status": "Available",
                "resourceType": "RDS"
```

`],`

```json
        "success": "true",
        "status": "200"
```

`},`

```json
    "host": "\"\"",
    "status": "200"
```

##### 4.3.2.8 AddCommonSpec

You can call this operation to add custom specifications of a service.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddCommonSpec | The operation that you want to perform. Set the value to AddCommonSpec. |
| specName | String | Yes | Enhanced Enterprise Edition | The Chinese name of the specifications. |
| status | String | Yes | Available | The status. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The returned dataset. |
| success | Boolean | true | The success code. |
| validationInfo | String | "" | The verification code. |
| code | String | 200 | The HTTP status code. |
| httpOk | Boolean | true | The returned status code. |
| ip | String | "" | The IP address. |
| message | String | success | The error message. |
| requestId | String | 0a1ec3c216087759426241251d0 2bd | The ID of the request. |
| success | Boolean | true | The success code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=AddCommonSpec &resourceType=RDS &specName=Enhanced Enterprise Edition &status=Available &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <success>true</success>
    <validationInfo>""</validationInfo>
</data> <httpOk>true</httpOk> <requestId>0a1ec3c216087759426241251d02bd</requestId> <success>true</success> <ip>""</ip> <message>success</message>
```

| JSON | format |
|---|---|
| { "code": "200", "data": { "success": "true", "validationInfo": """" }, "httpOk": "true", "requestId": "0a1ec3c216087759426241251d02bd", "success": "true", "ip": """", "message": "success" } |   |

##### 4.3.2.9 UpdateCommonSpecStatus

You can call this operation to enable or disable specifications.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateCommonSpecStatus | The operation that you want to perform. Set the value to UpdateCommonSpecStatus. |
| ids | String | Yes | 1 | The IDs of the specifications. |
| status | String | Yes | Unavailable | The status. Valid values: Available and Unavailable. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| data | Integer | 200 | The collection of data. |
| message | String | success | The message. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=UpdateCommonSpecStatus &ids=1 &status=Unavailable &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <code>200</code> <data>200</data> <success>true</success> <message>success</message> |   |

| JSON | format |
|---|---|
| { "code": "200", "data": "200", "success": "true", "message": "success" } |   |

#### 4.3.3 Cloud services

##### 4.3.3.1 DescribeModifiableInstanceType

You can call this operation to query the Elastic Compute Service (ECS) instance types that can be upgraded or downgraded.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeModifiableInstanceT ype | The operation that you want to perform. Set the value to DescribeModifiableInstanceType. |
| destinationResource | String | Yes | sfdsf | Set the value to instanceType. |
| instanceId | String | Yes | sfdsfsfdsfsfdsf | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |
| result | Array of dataItem |   | The collection of data. |
| baselineCredit | Integer | 1 | The baseline vCPU computing performance (overall computing performance of all vCPUs) of the t5 or t6 burstable instance family. |
| cpuCoreCount | Integer | 1 | The number of vCPUs. |
| eniPrivateIpAddressQuanti ty | Integer | 2 | The maximum number of private IP addresses per elastic network interface (ENI). |
| eniQuantity | Integer | 2 | The maximum number of ENIs that can be bound to an instance. |
| gPUAmount | Integer | 0 | The number of GPUs. |
| gPUSpec | String | "" | The GPU specifications. |
| initialCredit | Integer | 1 | The initial vCPU credits of the t5 or t6 burstable instance family. |
| instanceBandwidthRx | Integer | 1 | The maximum inbound internal bandwidth. Unit: Kbit/s. |
| instanceBandwidthTx | Integer | 1 | The maximum outbound internal bandwidth. Unit: Kbit/s. |
| instanceFamilyLevel | String | EnterpriseLevel | The level of the instance family. |
| instancePpsRx | Long | 1 | The inbound packet forwarding rate over the internal network. Unit: pps. |
| instancePpsTx | Long | 1 | The outbound packet forwarding rate over the internal network. Unit: pps. |
| instanceTypeFamily | String | ecs.sn2.large | The instance family. |
| instanceTypeId | String | ecs.sn2.large | The ID of the instance type. |
| localStorageAmount | Integer | 1 | The number of local disks attached per instance. |
| localStorageCapacity | Long | 2000 | The capacity of each local disk attached per instance. Unit: GiB. |
| localStorageCategory | String | 2000 | The capacity of each local disk attached per instance. Unit: GiB. |
| memorySize | Integer | 4 | The amount of memory. Unit: GiB. |
| status | Integer | 200 | The returned status code. |

| success | String | true | The success code. |
|---|---|---|---|
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeModifiableInstanceType &destinationResource=sfdsf &instanceId=sfdsfsfdsfsfdsf &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <data> <result> <instancePpsTx>1</instancePpsTx> <instanceTypeFamily>ecs.sn2.large</instanceTypeFamily> <localStorageCapacity>2000</localStorageCapacity> <instanceTypeId>ecs.sn2.large</instanceTypeId> <instancePpsRx>1</instancePpsRx> <cpuCoreCount>1</cpuCoreCount> <initialCredit>1</initialCredit> <localStorageAmount>1</localStorageAmount> <gPUAmount>0</gPUAmount> <memorySize>4</memorySize> <instanceFamilyLevel>EnterpriseLevel</instanceFamilyLevel> <eniQuantity>2</eniQuantity> <instanceBandwidthRx>1</instanceBandwidthRx> <eniPrivateIpAddressQuantity>2</eniPrivateIpAddressQuantity> <localStorageCategory>2000</localStorageCategory> <instanceBandwidthTx>1</instanceBandwidthTx> <baselineCredit>1</baselineCredit> <gPUSpec>""</gPUSpec> </result> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |   |

| JSON | format |
|---|---|
| { "data": { "result": [ { "instancePpsTx": "1", "instanceTypeFamily": "ecs.sn2.large", "localStorageCapacity": "2000", "instanceTypeId": "ecs.sn2.large", "instancePpsRx": "1", "cpuCoreCount": "1", "initialCredit": "1", "localStorageAmount": "1", "gPUAmount": "0", "memorySize": "4", "instanceFamilyLevel": "EnterpriseLevel", "eniQuantity": "2", "instanceBandwidthRx": "1", "eniPrivateIpAddressQuantity": "2", "localStorageCategory": "2000", "instanceBandwidthTx": "1", "baselineCredit": "1", "gPUSpec": """" } ], "success": "true", "status": "200" }, "host": "\"\"", "status": "200" } |   |

##### 4.3.3.2 DescribeSeriesIdFamilies

You can call this operation to query instance families.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSeriesIdFamilies | The operation that you want to perform. Set the value to DescribeSeriesIdFamilies. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |
| result | Array of dataItem |   | The collection of data. |
| baseVersion | String | 3.13 | The version of the instance type. |
| gmtCreate | String | 2019-10-15 17:47:27 | The creation time of the instance type. |
| gmtModified | String | 2019-10-15 17:47:27 | The modification time of the instance type. |
| pageOrder | String | null | The order of instance types. |
| pageSize | Integer | 5 | The number of entries returned per page. |
| pageSort | String | null | The sorting of pages. |
| pageStart | Integer | 1 | The number of the page to query. Start from page 1. |
| regionId | String | cn-qingdao-env66-d01 | The region ID. |
| resourceType | String | RDS | The resource type. |
| seriesId | String | drds.sn2.8c32g | The ID of the edition. |
| seriesName | String | Standard Edition | The name of the edition. |
| seriesNameLabel | String | Standard Edition | The display name of the edition. |
| specFrom | String | systen | The source of the instance type. |
| status | String | Available | The status. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeSeriesIdFamilies &<Common request parameters>
```

Sample success responses `XML` format

```xml
<data>
    <result>
        <gmtModified>2019-10-15 17:47:27</gmtModified>
        <baseVersion>3.13</baseVersion>
        <seriesName>Standard Edition</seriesName>
        <pageSize>5</pageSize>
        <specFrom>systen</specFrom>
        <gmtCreate>2019-10-15 17:47:27</gmtCreate>
        <seriesId>drds.sn2.8c32g</seriesId>
        <pageOrder>null</pageOrder>
        <pageSort>null</pageSort>
        <regionId>cn-qingdao-env66-d01</regionId>
        <pageStart>1</pageStart>
        <seriesNameLabel>Standard Edition</seriesNameLabel>
        <status>Available</status>
        <resourceType>RDS</resourceType>
    </result>
    <success>true</success>
    <status>200</status>
</data> <host>""</host> <status>200</status>
```

| JSON | format |
|---|---|
| { "data": { "result": [ { "gmtModified": "2019-10-15 17:47:27", "baseVersion": "3.13", "seriesName": "Standard Edition", "pageSize": "5", "specFrom": "systen", "gmtCreate": "2019-10-15 17:47:27", "seriesId": "drds.sn2.8c32g", "pageOrder": "null", "pageSort": "null", "regionId": "cn-qingdao-env66-d01", "pageStart": "1", "seriesNameLabel": "Standard Edition", "status": "Available", "resourceType": "RDS" } ], "success": "true", "status": "200" }, "host": """", "status": "200" } |   |

##### 4.3.3.3 GroupCommonSpec

You can call this operation to query the valid values of the specifications-specific fields.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GroupCommonSpec | The operation that you want to perform. Set the value to GroupCommonSpec. |
| groupFiled | String | Yes | storageType | The field for which to query valid values. |
| resourceType | String | Yes | RDS | The resource type. |
| label | String | No | "" | The tag. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The dataset. |

| data | List | [ { "storageType":"AutoTestWn4MR _ xEkKK" }, { "storageType":"AutoTestUZOBA _ EDvil" }, { "storageType":"AutoTest8WqAc _ 6rtpp" }, { "storageType":"AutoTestaCPiv2n _ Ih3" }, { "storageType":"Standard" }, { "storageType":"1" } ] | The collection of results. |
|---|---|---|---|
| status | Integer | 200 | The returned status code. |
| success | String | true | The success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=GroupCommonSpec &groupFiled=storageType &resourceType=RDS &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <data> <data>[ { "storageType":"AutoTest_Wn4MRxEkKK" }, { "storageType":"AutoTest_UZOBAEDvil" }, { "storageType":"AutoTest_8WqAc6rtpp" }, { "storageType":"AutoTest_aCPiv2nIh3" }, { "storageType":"Standard" }, { "storageType":"1" } ]</data> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |   |

| JSON | format |
|---|---|
| { "data": { "data": "[ { \"storageType\":\"AutoTest_Wn4MRxEkKK\" }, { \"storageType\":\"AutoTest_UZOBAEDvil\" }, { \"storageType\":\"AutoTest_8WqAc6rtpp\" }, { \"storageType\":\"AutoTest_aCPiv2nIh3\" }, { \"storageType\":\"Standard\" }, { \"storageType\":\"1\" } ]", "success": "true", "status": "200" }, "host": "\"\"", "status": "200" } |   |

##### 4.3.3.4 DescribeInstanceTypeFamilies

You can call this operation to query Elastic Compute Service (ECS) instance families.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanceTypeFamilie s | The operation that you want to perform. Set the value to DescribeInstanceTypeFamilies. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |
| result | Struct |   | The collection of data. |
| instanceTypeFamilies | Array of instanceTypeFamilie |   | The ECS instance families. |

| generation | String | "" | The code of the instance family. |
|---|---|---|---|
| instanceTypeFamilyId | String | ecs.se1ne | The ID of the instance family. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The returned success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeInstanceTypeFamilies &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <data> <result> <instanceTypeFamilies> <generation>""</generation> <instanceTypeFamilyId>ecs.se1ne</instanceTypeFamilyId> </instanceTypeFamilies> </result> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |   |

| JSON | format |
|---|---|
| { "data": { "result": { "instanceTypeFamilies": [ { "generation": "\"\"", "instanceTypeFamilyId": "ecs.se1ne" } ] }, "success": "true", "status": "200" }, "host": "\"\"", "status": "200" } |   |

##### 4.3.3.5 GetRegionsByProduct

Queries the region list of a service.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRegionsByProduct | The operation that you want to perform. Set the value to GetRegionsByProduct. |
| ProductName | String | Yes | ecs | The name of the service. |
| Organization | String | No | 1 | The ID of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| body | Struct |   | The response body. |

| RegionList | Array of Region |   | The list of regions. |
|---|---|---|---|
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region. |
| RegionType | String | center | The type of the region. center cell |
| code | Integer | 200 | The HTTP status code. |
| successResponse | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetRegionsByProduct &ProductName=ecs &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <successResponse>true</successResponse> <code>200</code> <body> <RegionList> <RegionType>center</RegionType> <RegionId>cn-qingdao-env17-d01</RegionId> </RegionList> </body> |   |

| JSON | format |
|---|---|
| { "successResponse": "true", "code": "200", "body": { "RegionList": [ { "RegionType": "center", "RegionId": "cn-qingdao-env17-d01" } ] } } |   |

##### 4.3.3.6 BindBucketPolicy

Associates a policy with an OSS bucket.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/ossIsolationVpc/bind HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| vpcName | String | Body | No | vpcName | The name of the VPC. |
| vLan | String | Body | No | vLan | The IP address of the VLAN. |
| bucketName | String | Body | No | testName | The name of the bucket. |
| vpcId | String | Body | No | vpcId | The ID of the VPC. |
| endpoint | String | Body | No | endpoint | The endpoint of the OSS bucket. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | Integer | 200 | The HTTP status code. |
| data | String | "" | The data returned. |
| message | String | "" | The message returned. |
| success | String | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/manage/saleconf/ossIsolationVpc/bind HTTP/1.1 Common request headers
```

Sample success responses

| XML | format |
|---|---|
| <code>200</code> <success>true</success> <data/> |   |

| JSON | format |
|---|---|
| { "code": 200, "success": true, "data": "" } |   |

##### 4.3.3.7 UnBindBucketPolicy

Disassociates a policy from an OSS bucket.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/ossIsolationVpc/unBind HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| bucketName | String | Body | No | bucketName | The name of the bucket. |
| vpcId | String | Body | No | vpcId | The ID of the VPC. |
| endpoint | String | Body | No | endpoint | The endpoint of the OSS bucket. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Data | String | "" | The data returned. |
| Message | String | "" | The message returned. |
| Success | String | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/manage/saleconf/ossIsolationVpc/unBind HTTP/1.1 Common request headers
```

Sample success responses

| XML | format |
|---|---|
| <Code>200</Code> <Success>true</Success> <Data/> |   |

| JSON | format |
|---|---|
| { "Code": 200, "Success": true, "Data": "" } |   |

#### 4.3.4 Configurations

##### 4.3.4.1 RemoveLoginPolicyById

Deletes a logon policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveLoginPolicyById | The operation that you want to perform. Set the value to RemoveLoginPolicyById. |
| Id | Integer | Yes | 2 | The ID of the logon policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveLoginPolicyById &Id=2 &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "success": "true", "pureListData": "false", "message": "success" } |   |

##### 4.3.4.2 GetPasswordPolicy

Queries a password policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetPasswordPolicy | The operation that you want to perform. Set the value to GetPasswordPolicy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| hardExpiry | Boolean | true | Indicates whether the password expires. |
| maxLoginAttemps | Integer | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| maxPasswordAge | Integer | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| minimumPasswordLength | Integer | 10 | The minimum number of characters in the password. |
| passwordErrorLockPeriod | Integer | 30 | The locking period of the password. |
| passwordErrorToleranceP eriod | Integer | 5 | The tolerance period of the password when a password error occurs. |
| passwordReusePrevention | Integer | 5 | The number of previous passwords that the user is disallowed to reuse. Default value: 0. The default value indicates that the user can reuse previous passwords. |
| requireLowercaseCharact ers | Boolean | true | Indicates whether lowercase letters are required. |
| requireNumbers | Boolean | true | Indicates whether digits are required. |
| requireSymbols | Boolean | true | Indicates whether special characters are required. |
| requireUppercaseCharact ers | Boolean | true | Indicates whether uppercase letters are required. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPasswordPolicy &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <passwordErrorTolerancePeriod>5</passwordErrorTolerancePeriod>
    <minimumPasswordLength>10</minimumPasswordLength>
    <requireSymbols>true</requireSymbols>
    <passwordErrorLockPeriod>30</passwordErrorLockPeriod>
    <passwordReusePrevention>5</passwordReusePrevention>
    <maxLoginAttemps>5</maxLoginAttemps>
    <requireLowercaseCharacters>true</requireLowercaseCharacters>
    <hardExpiry>true</hardExpiry>
    <requireNumbers>true</requireNumbers>
    <requireUppercaseCharacters>true</requireUppercaseCharacters>
    <maxPasswordAge>90</maxPasswordAge>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "passwordErrorTolerancePeriod": "5", "minimumPasswordLength": "10", "requireSymbols": "true", "passwordErrorLockPeriod": "30", "passwordReusePrevention": "5", "maxLoginAttemps": "5", "requireLowercaseCharacters": "true", "hardExpiry": "true", "requireNumbers": "true", "requireUppercaseCharacters": "true", "maxPasswordAge": "90" }, "success": "true", "pureListData": "false", "message": "success" } |   |

##### 4.3.4.3 ResetPasswordPolicy

Resets a password policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetPasswordPolicy | The operation that you want to perform. Set the value to ResetPasswordPolicy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| hardExpiry | Boolean | true | Indicates whether the password expires. |
| maxLoginAttemps | Integer | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| maxPasswordAge | Integer | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| minimumPasswordLength | Integer | 10 | The minimum number of characters in the password. |
| passwordErrorLockPeriod | Integer | 30 | The locking period of the password. |

| passwordErrorToleranceP eriod | Integer | 5 | The tolerance period of the password when a password error occurs. |
|---|---|---|---|
| passwordReusePrevention | Integer | 5 | The number of previous passwords that the user is disallowed to reuse. The default value is 0, which indicates that the users can reuse previous passwords. |
| requireLowercaseCharact ers | Boolean | true | Indicates whether lowercase letters are required. |
| requireNumbers | Boolean | true | Indicates whether digits are required. |
| requireSymbols | Boolean | true | Indicates whether special characters are required. |
| requireUppercaseCharact ers | Boolean | true | Indicates whether uppercase letters are required. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ResetPasswordPolicy &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <passwordErrorTolerancePeriod>5</passwordErrorTolerancePeriod> <minimumPasswordLength>10</minimumPasswordLength> <requireSymbols>true</requireSymbols> <passwordErrorLockPeriod>30</passwordErrorLockPeriod> <passwordReusePrevention>5</passwordReusePrevention> <maxLoginAttemps>5</maxLoginAttemps> <requireLowercaseCharacters>true</requireLowercaseCharacters> <hardExpiry>true</hardExpiry> <requireNumbers>true</requireNumbers> <requireUppercaseCharacters>true</requireUppercaseCharacters> <maxPasswordAge>90</maxPasswordAge> </data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "passwordErrorTolerancePeriod": "5", "minimumPasswordLength": "10", "requireSymbols": "true", "passwordErrorLockPeriod": "30", "passwordReusePrevention": "5", "maxLoginAttemps": "5", "requireLowercaseCharacters": "true", "hardExpiry": "true", "requireNumbers": "true", "requireUppercaseCharacters": "true", "maxPasswordAge": "90" }, "success": "true", "pureListData": "false", "message": "success" } |   |

##### 4.3.4.4 SetPasswordPolicy

Modifies a password policy.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetPasswordPolicy | The operation that you want to perform. Set the value to SetPasswordPolicy. |
| HardExpiry | Boolean | No | true | Specifies whether the password expires. |
| RequireNumbers | Boolean | No | true | Specifies whether digits are required. |
| RequireSymbols | Boolean | No | true | Specifies whether special characters are required. |
| RequireLowercaseCharacters | Boolean | No | true | Specifies whether lowercase letters are required. |
| RequireUppercaseCharacters | Boolean | No | true | Specifies whether uppercase letters are required. |
| MaxLoginAttemps | Integer | No | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| MaxPasswordAge | Integer | No | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| MinimumPasswordLength | Integer | No | 10 | The minimum required number of characters in the password. |
| PasswordReusePrevention | Integer | No | 5 | The number of previous passwords that the user is disallowed to reuse. Default value: 0. The default value indicates that the user can reuse previous passwords. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| hardExpiry | Boolean | true | Indicates whether the password expires. |
| maxLoginAttemps | Integer | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| maxPasswordAge | Integer | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| minimumPasswordLength | Integer | 10 | The minimum number of characters in the password. |
| passwordErrorLockPeriod | Integer | 30 | The locking period of the password. |
| passwordErrorToleranceP eriod | Integer | 5 | The tolerance period of the password when a password error occurs. |
| passwordReusePrevention | Integer | 5 | The number of previous passwords that the user is disallowed to reuse. Default value: 0. The default value indicates that the user can reuse previous passwords. |
| requireLowercaseCharact ers | Boolean | true | Indicates whether lowercase letters are required. |
| requireNumbers | Boolean | true | Indicates whether digits are required. |
| requireSymbols | Boolean | true | Indicates whether special characters are required. |
| requireUppercaseCharact ers | Boolean | true | Indicates whether uppercase letters are required. |

| message | String | success | The error message. |
|---|---|---|---|
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetPasswordPolicy &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <passwordErrorTolerancePeriod>5</passwordErrorTolerancePeriod> <minimumPasswordLength>10</minimumPasswordLength> <requireSymbols>true</requireSymbols> <passwordErrorLockPeriod>30</passwordErrorLockPeriod> <passwordReusePrevention>5</passwordReusePrevention> <maxLoginAttemps>5</maxLoginAttemps> <requireLowercaseCharacters>true</requireLowercaseCharacters> <hardExpiry>true</hardExpiry> <requireNumbers>true</requireNumbers> <requireUppercaseCharacters>true</requireUppercaseCharacters> <maxPasswordAge>90</maxPasswordAge> </data> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "passwordErrorTolerancePeriod": "5", "minimumPasswordLength": "10", "requireSymbols": "true", "passwordErrorLockPeriod": "30", "passwordReusePrevention": "5", "maxLoginAttemps": "5", "requireLowercaseCharacters": "true", "hardExpiry": "true", "requireNumbers": "true", "requireUppercaseCharacters": "true", "maxPasswordAge": "90" }, "success": "true", "pureListData": "false", "message": "success" } |   |

##### 4.3.4.5 ListRAMServiceRoles

Queries the list of RAM roles.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/role/listRAMServiceRoles HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|

| regionName | String | Body | No | testregion _ | The ID of the zone. |
|---|---|---|---|---|---|
| productName | String | Body | No | protest _ | The name of the service. |
| roleName | String | Body | No | roletest _ | The name of the role. |
| organizationId | Integer | Body | No | 1 | The ID of the organization. |
| currentPage | Integer | Body | No | 1 | The number of the page to return. |
| pageSize | Integer | Body | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Array of itemData |   | The response data. |
| aliyunUserId | Integer | 12 | The ID of the Apsara Stack tenant account. |
| arn | String | 123 | The ARN. |
| assumeRolePolicyDocume nt | String | 123 | The file of the policy based on which the role is assumed. |
| description | String | test | The description. |
| id | Integer | 1 | The ID. |
| organizationId | Integer | 1 | The ID of the organization. |
| organizationName | String | organizationtest _ | The name of the organization. |
| policies | Array of itemPolicy |   | The list of policies. |
| aliyunUserId | Integer | 1 | The ID of the Apsara Stack tenant account. |
| ascmRamPolicyId | Integer | 1 | The ID of the RAM policy in the Apsara Uni-manager Management Console. |
| attachDate | Long | 1645234235 | This parameter is deprecated. |
| defaultVersion | String | 1 | The default version. |
| description | String | testdescription | The description. |
| id | Integer | 1 | The ID. |
| policyDocument | String | 123 | The file of the policy. |
| policyName | String | test | The name of the policy. |
| policyType | String | test | The type of the policy. |
| privilegeId | Integer | 1 | This parameter is deprecated. |
| ramGroupId | Integer | 1 | The ID of the RAM user group. |
| ramRoleId | Integer | 1 | The ID of the RAM role. |

| region | String | cn-qingdao-env17-d01 | The zone. |
|---|---|---|---|
| resourceSetId | Integer | 1 | The ID of the resource set. |
| product | String | 123 | The ID of the service. |
| region | String | cn-qingdao-env17-d01 | The ID of the zone. |
| roleId | String | 1 | The ID of the role. |
| roleName | String | defaultRole.resourceUser.name | The name of the role. |
| roleType | String | ROLETYPEASCM _ | The type of the role. Valid values: ROLETYPERAM and _ ROLETYPEASCM. ROLETYPERAM specifies a RAM role. _ _ ROLETYPEASCM specifies a custom role. _ |
| message | String | success | The message. |
| pageInfo | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 5 | The number of entries returned per page. |
| total | Integer | 10 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/role/listRAMServiceRoles HTTP/1.1 Common request headers
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <organizationId/>
    <aliyunUserId/>
    <product/>
    <organizationName/>
    <assumeRolePolicyDocument/>
    <roleId>1</roleId>
    <roleName>defaultRole.resourceUser.name</roleName>
    <description/>
    <id/>
    <roleType>ROLETYPE_ASCM</roleType>
    <region>cn-qingdao-env17-d01</region>
    <arn/>
    <policies>
        <policyDocument/>
        <ramRoleId/>
        <ramGroupId/>
        <policyName/>
        <description/>
        <ascmRamPolicyId/>
        <aliyunUserId/>
        <privilegeId/>
        <attachDate/>
        <policyType/>
        <id/>
        <resourceSetId/>
        <region/>
        <defaultVersion/>
    </policies>
</data> <success>true</success> <pageInfo>
    <total>10</total>
    <totalPage>2</totalPage>
    <pageSize>5</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": [{"organizationId":"","aliyunUserId":"","product":"","organizationName":"","assumeRolePolicyDocument":"","roleId":"1","roleName":"defaultRole.re eUser.name","description":"","id":"","roleType":"ROLETYPE_ASCM","region":"cn-qingdao-env17-d01","arn":"","policies": [{"policyDocument":"","ramRoleId":"","ramGroupId":"","policyName":"","description":"","ascmRamPolicyId":"","aliyunUserId":"","privilegeId":"","a Date":"","policyType":"","id":"","resourceSetId":"","region":"","defaultVersion":""}]}],"success":"true","pageInfo": {"total":"10","totalPage":"2","pageSize":"5","currentPage":"1"},"pureListData":"false","message":"success"} |   |

##### 4.3.4.6 ListRAMPolicies

Queries the list of RAM policies.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/role/listRAMPolicies HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| PolicyName | String | Body | No | testpolicy _ | The name of the policy. |
| Description | String | Body | No | test | The description of the policy. |
| RoleId | Integer | Body | No | 1 | The ID of the role. |
| CurrentPage | Integer | Body | No | 1 | The number of the page to return. |
| PageSize | Integer | Body | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Array of itemData |   | The response data. |
| ctime | Long | 16223113123 | The time when the policy was created. |
| id | Integer | 1 | The ID of the policy. |
| mtime | Long | 16223113123 | The time when the policy was modified. |
| muserId | String | admin | The modifier. |
| policyDocument | String | a | The file of the policy. |
| policyName | String | testpolicy _ | The name of the policy. |
| region | String | cn-qingdao-env17-d01 | The zone. |
| message | String | success | The message. |
| pageInfo | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 5 | The number of entries returned per page. |
| total | Integer | 10 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/role/listRAMPolicies HTTP/1.1 Common request headers
```

Sample success responses `XML` format

```xml
<redirect/> <cost/> <code/> <data>
    <policyDocument/>
    <muserId/>
    <policyName/>
    <ctime/>
    <id/>
    <region/>
    <mtime/>
</data> <success/> <pageInfo>
    <total/>
    <totalPage/>
    <pageSize/>
    <currentPage/>
</pageInfo> <pureListData/> <message/>
```

| JSON | format |
|---|---|
| { "redirect": "", "cost": "", "code": "", "data": [ { "policyDocument": "", "muserId": "", "policyName": "", "ctime": "", "id": "", "region": "", "mtime": "" } ], "success": "", "pageInfo": { "total": "", "totalPage": "", "pageSize": "", "currentPage": "" }, "pureListData": "", "message": "" } |   |

##### 4.3.4.7 ListRAMPoliciesForUser

Queries the list of RAM policies that are attached to a role.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/dataPrivilege/listRAMPoliciesForUser HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | admin | The logon user. |

**Examples**

Sample requests

```
POST /ascm/auth/dataPrivilege/listRAMPoliciesForUser HTTP/1.1 Common request headers
```

`{`

```json
"loginName": ""
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <ascmRamPolicyId>1</ascmRamPolicyId>
    <aliyunUserId>123</aliyunUserId>
    <policyDocument>ccc</policyDocument>
    <ramGroupId>1</ramGroupId>
    <policyName>test</policyName>
    <attachDate>1638414294</attachDate>
    <policyType>1</policyType>
    <description>test</description>
    <id>1</id>
    <region>cn-qingdao-env17-d01</region>
    <defaultVersion>3</defaultVersion>
</data> <success>true</success> <pageInfo>
    <total>10</total>
    <totalPage>2</totalPage>
    <pageSize>5</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": [{"ascmRamPolicyId":"1","aliyunUserId":"123","policyDocument":"ccc","ramGroupId":"1","policyName":"test","attachDate":"1638414294","policyType": description":"test","id":"1","region":"cn-qingdao-env17-d01","defaultVersion":"3"}],"success":"true","pageInfo": {"total":"10","totalPage":"2","pageSize":"5","currentPage":"1"},"pureListData":"false","message":"success"} |   |

##### 4.3.4.8 RemoveLoginPolicyByName

Deletes a logon policy.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/loginPolicy/removeLoginPolicyByName HTTP/1.1
```

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| name | String | Body | No | test | The name of the logon policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/loginPolicy/removeLoginPolicyByName HTTP/1.1 Common request headers
```

`{`

```json
"Name": ""
```

Sample success responses

| XML | format |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |   |

| JSON | format |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","message":"success"} |   |

#### 4.3.5 Parameters related to the MeteringQuery operation

##### 4.3.5.1 ECS

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Elastic Compute Service (ECS).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| ZoneId | Zone | The ID of the zone where the instance resides. |
| InstanceType | Instance type | The ECS instance type defines the basic properties of the ECS instance, such as CPU (including CPU model and clock speed) and memory. |
| InstanceTypeFamily | Instance family | ECS instances are categorized into different instance families based on the business scenarios to which they can be applied. Each instance family is divided into different instance types based on their CPU and memory specifications. |
| SerialNumber | Serial number | The serial number of the ECS instance. |
| InstanceNetworkType | Network type | The network type of the instance. Valid values: Classic VPC |
| ExpiredTime | Expiration time | The time when the instance expires. |
| HostName | Hostname | The hostname of the ECS instance. |
| Status | Instance status | The status of the instance. Valid values: Pending: The instance is being created. Running: The instance is running. Starting: The instance is being started. Stopping: The instance is being stopped. Stopped: The instance is stopped. |

| Parameter | Name | Description |
|---|---|---|
| InstanceName | Instance name | The name of the ECS instance. |
| PrivateIpAddress | Internal IP address | The private IP address of the instance in a virtual private cloud (VPC). When InstanceNetworkType is set to vpc, this parameter value can consist of multiple IP addresses. |
| OSName | Operating system name | The name of the operating system installed on the instance. |
| EipAddress | Elastic IP address (EIP) | The EIPs of the instance. |
| NatIpAddress | Network translation address | The public or private IP address of the ECS instance. |
| VpcId | VPC ID | The ID of the VPC. |
| EipBandwidth | EIP bandwidth | The bandwidth of the EIP associated with the ECS instance. |
| IoOptimized | Whether I/O optimization is enabled | Indicates whether the instance is I/O optimized. |
| InternetMaxBandwidthIn | Maximum inbound public bandwidth | Valid values: 1 to 200. Unit: Mbit/s. |
| GPUAmount | Number of GPUs | The number of GPUs that the GPU-accelerated instance has. |
| GPUSpec | GPU model | The model of GPUs used by the GPU-accelerated instance. |
| InstanceBandwidthTx | Maximum outbound internal bandwidth | Unit: KB/s. |
| Memory | Memory | The amount of memory. Unit: MB. |
| Cpu | Processor | The number of processors. |
| SysDiskSize | System disk | The size of the system disk. Unit: GB. |
| DataDiskSize | Data disk size | The size of the data disk. Unit: GB. |

##### 4.3.5.2 SLB

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Server Load Balancer (SLB).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |

|   |   | t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| CreateTime | Instance creation time | The time when the instance was created. |
| ChargeType | Billing method | Valid values: PayByBandwidth PayByTraffic |
| StoreSpace | Capacity threshold | The capacity threshold set for the bucket. After the threshold value is exceeded, write operations cannot be performed on the bucket. Unit: GB. |
| CdnOut | CDN back-to-origin traffic | The traffic sent from OSS to Alibaba Cloud CDN (CDN). Unit: byte. |
| IntranetIn | Inbound traffic to the internal network | Unit: byte. |
| ChargedDatasize | Actually billed storage space | The actually billed Infrequent Access (IA) locally redundant storage (LRS) or OSS Archive LRS space. Unit: byte. |
| GetRequest | Number of GET requests | The number of GET requests that occurred between the specified start time and the specified end time. |
| RetrievalData | Volume of retrieved data | The volume of retrieved IA or Archive data. Unit: byte. |
| PutRequest | Number of PUT requests | The number of PUT requests that occurred between the specified start time and the specified end time. |
| IntranetOut | Outbound traffic from the internal network | Unit: byte. |
| ProcessI | Number of video snapshots | The number of video snapshots. |
| ProcessImgSize | Volume of processed images | The volume of processed images. Unit: byte. |
| SelectScanSize | Volume of scanned data | The volume of scanned data that is queried by using the SELECT statement. |
| NetworkOut | Outbound traffic | The traffic sent from OSS to external networks, which occurred between the specified start time and the specified end time. Unit: byte. |
| Storage | Volume of stored data | The amount of used Standard LRS storage space. Unit: byte. |
| NetworkIn | Inbound traffic | The traffic sent from external networks to OSS, which occurred between the specified start time and the specified end time. Unit: byte. |
| AvailabilityAverage _ | Average availability value | The average availability obtained from CloudMonitor at the specified end time. |
| AvailabilityMaximum _ | Maximum availability value | The maximum availability value obtained from CloudMonitor at the specified end time. |
| AvailabilityMinimum _ | Minimum availability value | The minimum availability value obtained from CloudMonitor at the specified end time. |
| MeteringStorageUtilizationAverage _ | Average capacity value | The average capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |
| MeteringStorageUtilizationMaximum _ | Maximum capacity value | The maximum capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |

| Apsara Uni-manager Man t Console Developer Guid | agemen e·API re |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| MeteringStorageUtilizationMinimum _ | Minimum capacity value | The minimum capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |

##### 4.3.5.3 OSS

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Object Storage Service (OSS).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the bucket belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the bucket belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the bucket belongs. |
| InsId | Bucket ID | The ID of the bucket. |
| RegionId | Region | The ID of the region where the bucket resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Bucket creation time | The time when the bucket was created. |
| ChargeType | Billing method | Valid values: PayByBandwidth PayByTraffic |
| StoreSpace | Capacity threshold | The capacity threshold set for the bucket. After the threshold value is exceeded, write operations cannot be performed on the bucket. Unit: GB. |
| CdnOut | CDN back-to-origin traffic | The traffic sent from OSS to Alibaba Cloud CDN (CDN). Unit: byte. |
| IntranetIn | Inbound traffic to the internal network | Unit: byte. |
| ChargedDatasize | Actually billed storage space | The actually billed Infrequent Access (IA) locally redundant storage (LRS) or OSS Archive LRS space. Unit: byte. |
| GetRequest | The number of GET requests. | The number of GET requests that occurred between the specified start time and the specified end time. |
| RetrievalData | Volume of retrieved data | The volume of retrieved IA or Archive data. Unit: byte. |
| PutRequest | The number of PUT requests. | The number of PUT requests that occurred between the specified start time and the specified end time. |
| IntranetOut | Outbound traffic from the internal network | Unit: byte. |
| ProcessI | Number of video snapshots | The number of video snapshots. |
| ProcessImgSize | Volume of processed images | The volume of processed images. Unit: byte. |

|   |   | Apsara Uni-manager Managemen t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| SelectScanSize | Volume of scanned data | The volume of scanned data that is queried by using the SELECT statement. |
| NetworkOut | Outbound traffic | The traffic sent from OSS to external networks, which occurred between the specified start time and the specified end time. Unit: byte. |
| Storage | Volume of stored data | The amount of used Standard LRS storage space. Unit: byte. |
| NetworkIn | Inbound traffic | The traffic sent from external networks to OSS, which occurred between the specified start time and the specified end time. Unit: byte. |
| AvailabilityAverage _ | Average availability value | The average availability obtained from CloudMonitor at the specified end time. |
| AvailabilityMaximum _ | Maximum availability value | The maximum availability value obtained from CloudMonitor at the specified end time. |
| AvailabilityMinimum _ | Minimum availability value | The minimum availability value obtained from CloudMonitor at the specified end time. |
| MeteringStorageUtilizationAverage _ | Average capacity value | The average capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |
| MeteringStorageUtilizationMaximum _ | Maximum capacity value | The maximum capacity value obtained from CloudMonitor at the end time. Unit: byte. |
| MeteringStorageUtilizationMinimum _ | Minimum capacity value | The minimum capacity value obtained from CloudMonitor at the end time. Unit: byte. |

##### 4.3.5.4 EIP

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Elastic IP Address (EIP).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the elastic IP address (EIP) belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the EIP belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the EIP belongs. |
| InsId | EIP ID | The ID of the EIP. |
| RegionId | Region | The ID of the region where the EIP resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | EIP creation time | The time when the EIP was created. |
| PrivateIpAddress | Internal IP address | The IP address that belongs to the CIDR block of the vSwitch. |
| Name | EIP name | The name of the EIP. |
| ExpiredTime | Expiration time | The time when the EIP expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |

| Apsara Uni-manager Man t Console Developer Guid ference | agemen e·API re |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| BandwidthPackageId | ID of the EIP bandwidth plan | The ID of the EIP bandwidth plan. |
| Status | EIP status | The status of the EIP. Valid values: Associating: The EIP is being associated with an instance. Unassociating: The EIP is being disassociated from an instance. InUse: The EIP is associated with an instance. Available: The EIP is available. |
| ISP | Line type | The line type. Valid values: BGP: BGP (Multi-ISP) lines BGPPRO: BGP (Multi-ISP) Pro lines _ |
| Mode | Association mode | The mode in which you associate the EIP. Valid values: NAT: the standard NAT mode MULTIBINDED: the Multi-EIP to ENI mode _ BINDED: the cut-through mode This parameter is required only when InstanceType is set to NetworkInterface. |
| BandwidthPackageType | Bandwidth type | The type of the bandwidth. Only CommonBandwidthPackage (an EIP bandwidth plan) is returned. |
| ChargeType | Billing method | The billing method of the EIP. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| IpAddress | IP address | The IP address of the EIP. |
| BindInstanceId | ID of the associated instance | The ID of the instance with which the EIP is associated. |
| BindInstanceType | The type of the associated instance. | The type of the instance with which the EIP is associated. Valid values: EcsInstance: an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC) SlbInstance: a Server Load Balancer (SLB) instance in a VPC Nat: a NAT gateway. HaVip: a high-availability virtual IP address (HAVIP) NetworkInterface: a secondary elastic network interface (ENI). |
| BindInstanceName | Name of the associated instance | The name of the associated instance. |
| Bandwidth | Maximum bandwidth value | The maximum bandwidth value of the EIP. Unit: Mbit/s. |

##### 4.3.5.5 VPC

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Virtual Private Cloud (VPC).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the virtual private cloud (VPC) belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the VPC belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the VPC belongs. |
| InsId | VPC ID | The ID of the VPC. |
| RegionId | Region | The ID of the region where the VPC resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |

|   |   | t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | VPC creation time | The time when the VPC was created. |
| Status | VPC status | The status of the VPC. Valid values: Pending: The VPC is being configured. Available: The VPC is available. |
| CidrBlock | IPv4 CIDR block | The IPv4 CIDR block of the VPC. |
| VRouterId | Router ID | The ID of the vRouter. |
| VpcName | VPC name | The name of the VPC. |
| Ipv6CidrBlock | IPv6 CIDR block | The IPv6 CIDR block of the VPC. |
| Description | Description | The description of the VPC. |
| IsDefault | Default VPC | Indicates whether the VPC is the default VPC in the region. Valid values: true: The VPC is the default VPC in the region. false: The VPC is not the default VPC in the region. |

##### 4.3.5.6 ApsaraDB RDS for MySQL

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB RDS for MySQL.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| DBInstanceDescription | Instance description | The description of the instance. |
| Category | Instance edition | The edition of the instance. Valid values: Basic: Basic Edition HighAvailability: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
| ClassCode | Instance type | The instance type of the instance. Example: rds.mysql.t1.small. |
| DBType | Engine type | The type of the database. Example: MySQL. |
| DBVersion | Engine version | The database version. Example: 8.0. |

| t Console Developer Guid ference | e·API re |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| Zone | Zone ID | The zone ID of the instance. |
| DBInstanceStatus | Instance status | The status of the RDS instance. |
| DBInstanceType | Instance architecture | The architecture of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| LockMode | Lock mode | The lock mode of the instance. Valid values: Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked because it has expired. LockByRestoration: The instance is automatically locked for a rollback. LockByDiskQuota: The instance is automatically locked because its disk space is used up. LockReadInstanceByDiskQuota: The instance is a read-only instance and is automatically locked when the disk space is full. |
| Port | Port number | The internal port of the instance. |
| DBInstanceClassType | Instance family | The instance family of the instance. Valid values: s: shared instance family x: general purpose instance family d: dedicated instance family h: dedicated host instance family |
| DBInstanceStorageType | Storage type | The type of storage media that is used by the instance. Valid values: localssd or ephemeralssd: local SSD _ _ cloudssd: standard SSD _ cloudessd: enhanced SSD _ |
| AvailabilityValue | Availability | The availability status of the instance. Unit: %. |
| IpAddress | IP address | The IP address. |
| VPCId | VPC ID | The ID of the virtual private cloud (VPC). |
| BackupStorage | Backup storage | The backup storage. Unit: byte. |
| NetworkIn | Inbound traffic | The traffic sent from external networks to RDS, which occurred between the specified start time and the specified end time. |
| NetworkOut | Outbound traffic | The traffic sent from RDS to external networks, which occurred between the specified start time and the specified end time. |
| Storage | Volume of stored data | The total storage capacity. Unit: byte. |
| UsedStorage | Used storage | The amount of used storage. Unit: byte. |
| AccountMaxQuantity | Maximum number of accounts that can be created | The maximum number of accounts that can be created. |
| DBInstanceCPU | Number of CPUs | The number of CPUs that are configured for the instance. |
| MaxConnections | Maximum number of connections | The maximum number of concurrent connections that are allowed by the instance. |
| DBInstanceMemory | Memory | The memory capacity of the instance. Unit: MB. |
| MaxIOPS | Maximum IOPS | The maximum number of I/O requests that the instance can process per second. |

|   |   | Apsara Uni-manager Managemen t Console Developer Guide·API re |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| DBMaxQuantity | Maximum number of databases that can be created | The maximum number of databases that can be created. |
| CpuUsageMaximum _ | Maximum CPU utilization | The maximum CPU utilization obtained from CloudMonitor at the specified end time. |
| CpuUsageMinimum _ | Minimum CPU utilization | The minimum CPU utilization obtained from CloudMonitor at the specified end time. |
| DiskUsageAverage _ | Average disk usage | The average disk usage obtained from CloudMonitor at the specified end time. |
| DiskUsageMaximum _ | Maximum disk usage | The maximum disk usage obtained from CloudMonitor at the specified end time. |
| DiskUsageMinimum _ | Minimum disk usage | The minimum disk usage obtained from CloudMonitor at the specified end time. |
| IOPSUsageAverage _ | Average IOPS usage | The average IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUsageMaximum _ | Maximum IOPS usage | The maximum IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUsageMinimum _ | Minimum IOPS usage | The minimum IOPS usage obtained from CloudMonitor at the specified end time. |
| MemoryUsageAverage _ | Average memory usage | The average memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsageMaximum _ | Maximum memory usage | The maximum memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsageMinimum _ | Minimum memory usage | The minimum memory usage obtained from CloudMonitor at the specified end time. |

##### 4.3.5.7 Tablestore

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Tablestore.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| InstanceType | Instance type | The instance type of the instance. Example: ssd. |
| TableName | Table name | The name of the table. |
| InstanceName | Instance name | The name of the instance. |
| Description | Instance description | The description of the instance. |

| Apsara Uni-manager Man t Console Developer Guid | agemen e·API re |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| Status | Instance status | The status of the instance. |
| Version | Engine version | The database engine version. |

##### 4.3.5.8 PolarDB-X

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to PolarDB-X.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the cluster belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the cluster belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the cluster belongs. |
| InsId | Cluster ID | The ID of the cluster. |
| RegionId | Region | The ID of the region where the cluster resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Cluster creation time | The time when the cluster was created. |
| Status | Cluster status | The status of the cluster. |
| Description | Description | The description of the database. |
| InstanceSpec | Instance type | The instance type of the cluster. Example: drds.sn2.4c16g.8C32G. |
| ZoneId | Zone ID | The zone ID of the cluster. |
| MachineType | Cluster machine type | The type of the machine where the cluster is deployed. The value is set to ECS. |
| Label | Instance label | The label of the cluster. Valid values: NORMAL: the normal cluster HAVPC: the high-availability cluster VPC: the cluster of the VPC type |
| InstanceSeries | Instance family | The instance family of the cluster. Example: drds.sn2.4c16g/. |
| VersionAction | Available action for the cluster version | The available actions for the cluster version. |
| Type | Instance architecture | The architecture of the cluster. Valid values: PRIVATE: the dedicated cluster PUBLIC: the shared cluster |
| VpcId | VPC ID | The ID of the virtual private cloud (VPC). |
| OrderInstanceId | ID of the purchased cluster | The ID of the purchased cluster. |
| InstRole | Cluster role | The role of the cluster. MASTER: the primary cluster SLAVE: the analytic read-only cluster SLAVEFLOW: the concurrent read-only cluster _ |

|   |   | Apsara Uni-manager Managemen t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| NetworkType | Network type | The network type of the cluster. Valid values: CLASSIC VPC |
| CommodityCode | Commodity code | The commodity code. |
| IpAddress | IP address | The IP address. |

##### 4.3.5.9 What is KVStore for Redis?

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to KVStore for Redis.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| ConnectionDomain | Private IP address | The private IP address of the instance. |
| NetworkType | Network type | The network type. Valid values: CLASSIC VPC |
| InstanceStatus | Instance status | The status of the instance. |
| PackageType | Service plan | The plan type. Valid values: standard: the standard plan customized: the custom plan |
| InstanceType | Instance type | The instance type of the instance. |
| ArchitectureType | Instance architecture | The architecture of the instance. Valid values: cluster: the cluster architecture standard: the standard architecture rwsplit: the read/write splitting architecture |
| EngineVersion | The engine version. | The database engine version. |
| ZoneId | Zone ID | The zone ID of the instance. |
| InstanceClass | Instance type | The instance type of the instance. |
| InstanceName | Instance name | The name of the instance. |

| Apsara Uni-manager Man t Console Developer Guid | agemen e·API re |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| ChargeType | Billing method | The billing method of the instance. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| NodeType | Node type | The type of the node. Valid values: double: master and replica nodes single: the single replica node |
| HasRenewChangeOrder | Whether an order for renewal and configuration change that has not taken effect exists | Indicates whether an order for renewal and configuration change that has not taken effect exists. Valid values: true: yes false: no |
| IsRds | Whether the instance is managed by ApsaraDB RDS | Indicates whether the instance is managed by RDS. Valid values: true: yes false: no |
| Connections | Connections | The maximum number of connections supported by the instance. |
| Port | Port number | The service port of the KVStore for Redis instance. |
| QPS | QPS | The estimated maximum queries per second (QPS). |
| Capacity | Capacity | The storage capacity of the instance. Unit: MB. |
| Bandwidth | Bandwidth | The bandwidth of the instance. Unit: MB/s. |
| ConnectionUsageAverage _ | Average connection usage | The average connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUsageMaximum _ | Maximum connection usage | The maximum connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUsageMinimum _ | Minimum connection usage | The minimum connection usage obtained from CloudMonitor at the specified end time. |
| FailedCountAverage _ | Average number of failures | The average number of failures obtained from CloudMonitor at the specified end time. |
| FailedCountMaximum _ | Maximum number of failures | The maximum number of failures obtained from CloudMonitor at the specified end time. |
| FailedCountMinimum _ | Minimum number of failures | The minimum number of failures obtained from CloudMonitor at the specified end time. |
| IntranetInAverage _ | Average write bandwidth | The average write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetInMaximum _ | Maximum write bandwidth | The maximum write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetInMinimum _ | Minimum write bandwidth | The minimum write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetInRatioAverage _ | Average write bandwidth usage | The average write bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetInRatioMaximum _ | Maximum write bandwidth usage | The maximum write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetInRatioMinimum _ | Minimum write bandwidth usage | The minimum write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetOutAverage _ | Average read bandwidth | The average read bandwidth obtained from CloudMonitor at the specified end time. |

|   |   | t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| IntranetOutMaximum _ | Maximum read bandwidth | The maximum read bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetOutMinimum _ | Minimum read bandwidth | The minimum read bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetOutRatioAverage _ | Average read bandwidth usage | The average read bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetOutRatioMaximum _ | Maximum read bandwidth usage | The maximum read bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetOutRatioMinimum _ | Minimum read bandwidth usage | The minimum read bandwidth usage obtained from CloudMonitor at the specified end time. |
| MemoryUsageAverage _ | Average memory usage | The average memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsageMaximum _ | Maximum memory usage | The maximum memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsageMinimum _ | Minimum memory usage | The minimum memory usage obtained from CloudMonitor at the specified end time. |

##### 4.3.5.10 AnalyticDB for PostgreSQL

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parametersGPDBspecific to AnalyticDB for PostgreSQL.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| EngineVersion | Engine version | The database engine version that is run on the instance. |
| ZoneId | Zone ID | The zone ID of the instance. |
| DBInstanceNetType | NIC type | The type of the network interface card (NIC) that is used by the instance. |
| PayType | Billing method | The billing method. Valid values: PostPaid: pay-as-you-go PrePaid: subscription |
| InstanceNetworkType | Network type | The network type of the instance. Valid values: Classic VPC |
| DBInstanceDescription | Instance description | The description of the instance. |

| ference |   |   |
|---|---|---|
| Parameter | Name | Description |
| Engine | Database engine | The engine of the database. |
| DBInstanceStatus | Instance status | The status of the instance. |
| LockMode | Lock mode | The lock mode. Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked because it has expired. LockByRestoration: The instance is automatically locked for a rollback. LockByDiskQuota: The instance is automatically locked because its disk space is used up. |
| LockReason | Lock reason | The reason why the cluster is locked. |
| ConnectionMode | Access mode | The access mode of the instance. Performance: the standard mode Safety: the safe mode |
| HostType | Disk type of compute nodes | The disk type of compute nodes. Valid values: 0: SSD 1: HDD |
| DBInstanceClass | Instance type | The instance type of the instance. |
| DBInstanceClassType | Instance family | The instance family. Valid values: s: shared instance family x: general purpose instance family d: dedicated instance family h: dedicated host instance family |
| AvailabilityValue | Availability status | The availability status of the instance. Unit: %. |
| VpcId | VPC ID | The ID of the virtual private cloud (VPC). |
| Port | Port number | The port number. |
| DBInstanceDiskMBPS | Disk throughput | The maximum disk throughput of a compute node. Unit: Mbit/s. |
| MaxConnections | Maximum number of connections | The maximum number of concurrent connections to an instance. |
| DBInstanceGroupCount | Number of compute nodes | The number of compute nodes. |
| DBInstanceMemory | Memory | The memory capacity of the instance. Unit: MB. |
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |
| DBInstanceCpuCores | CPU | The number of CPU cores. |

##### 4.3.5.11 ApsaraDB for MongoDB

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB for MongoDB.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |

|   |   | t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| EngineVersion | Engine version | The database engine version. |
| ZoneId | Zone ID | The zone ID of the instance. |
| DBInstanceStatus | Instance status | The status of the instance. |
| DBInstanceClass | Instance type | The instance type. Example: dds.mongo.mid. |
| DBInstanceType | Instance architecture | The architecture of the instance. Valid values: replicate: the replica set instance sharding: the sharded cluster instance |
| LockMode | Lock status | The lock status of the instance. Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked because it has expired. LockByRestoration: The instance is automatically locked for a rollback. LockByDiskQuota: The instance is automatically locked because its disk space is used up. Released: The instance is released. When the instance is in the Released state, it cannot be unlocked. You must use backup data to create a new instance. It may take an extended period of time to create another instance. |
| ChargeType | Billing method | The billing method of the instance. Valid values: PrePaid: subscription Postpaid: pay-as-you-go |
| NetworkType | Network type | The network type of the instance. Valid values: Classic VPC |
| DBInstanceDescription | Instance name | The name of the instance. |
| Engine | Database engine | The engine of the database. |
| VpcId | VPC ID | The ID of the virtual private cloud (VPC). |
| VSwitchId | vSwitch ID | The ID of the vSwitch to which the instance is connected. |
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |
| Storage | Volume of stored data | The volume of stored data. Unit: byte. |
| CpuNum | Number of CPUs | The number of CPUs. |
| MemoryNum | Memory size | The memory size. Unit: GiB. |
| CPUUtilizationAverage _ | Average CPU utilization | The average CPU utilization obtained from CloudMonitor at the specified end time. |

| t Console Developer Guid ference | e·API re |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| CPUUtilizationMaximum _ | Maximum CPU utilization | The maximum CPU utilization obtained from CloudMonitor at the specified end time. |
| CPUUtilizationMinimum _ | Minimum CPU utilization | The minimum CPU utilization obtained from CloudMonitor at the specified end time. |
| ConnectionAmountAverage _ | Average number of connections | The average number of connections obtained from CloudMonitor at the specified end time. |
| ConnectionAmountMaximum _ | Maximum number of connections | The maximum number of connections obtained from CloudMonitor at the specified end time. |
| ConnectionAmountMinimum _ | Minimum number of connections | The minimum number of connections obtained from CloudMonitor at the specified end time. |
| ConnectionUtilizationAverage _ | Average connection usage | The average connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUtilizationMaximum _ | Maximum connection usage | The maximum connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUtilizationMinimum _ | Minimum connection usage | The minimum connection usage obtained from CloudMonitor at the specified end time. |
| DiskUtilizationAverage _ | Average disk usage | The average disk usage obtained from CloudMonitor at the specified end time. |
| DiskUtilizationMaximum _ | Maximum disk usage | The maximum disk usage obtained from CloudMonitor at the specified end time. |
| DiskUtilizationMinimum _ | Minimum disk usage | The minimum disk usage obtained from CloudMonitor at the specified end time. |
| IOPSUtilizationAverage _ | Average IOPS usage | The average IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUtilizationMaximum _ | Maximum IOPS usage | The maximum IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUtilizationMinimum _ | Minimum IOPS usage | The minimum IOPS usage obtained from CloudMonitor at the specified end time. |
| MemoryUtilizationAverage _ | Average memory usage | The average memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUtilizationMaximum _ | Minimum memory usage | The minimum memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUtilizationMinimum _ | Maximum memory usage | The maximum memory usage obtained from CloudMonitor at the specified end time. |
| QPSAverage _ | Average QPS | The average queries per second (QPS) obtained from CloudMonitor at the specified end time. |
| QPSMaximum _ | Maximum QPS | The maximum QPS obtained from CloudMonitor at the specified end time. |
| QPSMinimum _ | Minimum QPS | The minimum QPS obtained from CloudMonitor at the specified end time. |

##### 4.3.5.12 Message Queue for Apache RocketMQ

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Message Queue for Apache RocketMQ.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | It consists of the product ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |

|   |   | t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| cluster | Cluster ID | The ID of the cluster. |
| instanceName | Instance name | The name of the instance. |
| spInstanceId | Instance ID | The ID of the instance. |
| independentNaming | Whether a separate namespace is configured | Indicates whether a separate namespace is configured. |
| instanceType | Instance type | The instance type of the instance. |
| instanceStatus | Instance status | The status of the instance. |
| topicCapacity | Topic capacity | The number of topics. |

##### 4.3.5.13 ApsaraDB RDS for PostgreSQL

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB RDS for PostgreSQL.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| Port | Port number | The internal port number of the instance. |
| DBInstanceClassType | Instance family | The instance family of the instance. Valid values: s: shared instance family. x: general purpose instance family. d: dedicated instance family. h: dedicated host instance family. |

| Parameter | Name | Description |
|---|---|---|
| DBInstanceClass | Instance type | The instance type of the instance. Example: rds.mys2.small. |
| DBInstanceNetType | Internet and internal networks | Indicates whether the instance is connected over the Internet or an internal network. Valid values: Internet: the Internet. Intranet: internal networks. |
| DBInstanceType | Instance role | The role of the instance. Valid values: Primary: primary instance. Readonly: read-only instance. Guard: disaster recovery instance. Temp: temporary instance. |
| InstanceNetworkType | Network type | The network type of the instance. Valid values: Classic VPC |
| DBInstanceDescription | Instance description | The description of the instance. |
| DBType | Database type | The type of the database. |
| DBVersion | Engine version | The database engine version that is available. |
| ZoneId | Zone ID | The zone ID of the instance. |
| LockMode | Lock mode | The lock mode of the instance. Valid values: Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked because it has expired. LockByRestoration: The instance is automatically locked for a rollback. LockByDiskQuota: The instance is automatically locked because its disk space is used up. LockReadInstanceByDiskQuota: The instance is a read-only instance and is automatically locked when the disk space is full. |
| PayType | Billing method | The billing method of the instance. Valid values: PostPaid: pay-as-you-go PrePaid: subscription |
| ConnectionMode | Access mode | The access mode of the instance. Valid values: Standard: the standard mode Safe: the proxy mode |
| DBInstanceStorageType | Storage type | The type of storage media that is used by the instance. Valid values: localssd or ephemeralssd: local SSD _ _ cloudssd: standard SSD. _ cloudessd: enhanced SSD _ |
| DBInstanceStatus | Instance status | The status of the instance. |
| AvailabilityValue | Availability status | The availability status of the instance. Unit: %. |
| IpAddress | IP address | The IP address. |
| VPCId | VPC ID | The ID of the virtual private cloud (VPC). |
| AccountMaxQuantity | Maximum number of accounts that can be created | The maximum number of accounts that can be created. |
| DBInstanceCPU | Number of CPUs that are configured for the instance | The number of CPUs that are configured for the instance. |

|   |   | Apsara Uni-manager Managemen t Console Developer Guide·API re |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| MaxConnections | Maximum number of concurrent connections | The maximum number of concurrent connections that are allowed by the instance. |
| DBInstanceMemory | Memory | The memory capacity of the instance. Unit: MB. |
| DBInstanceDiskUsed | Used storage | The used storage. Unit: byte. |
| MaxIOPS | Maximum IOPS | The maximum number of I/O requests that the instance can process per second. |
| DBMaxQuantity | Maximum number of databases that can be created | The maximum number of databases that can be created on the instance. |
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |

##### 4.3.5.14 ApsaraDB RDS for SQL Server

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB RDS for SQL Server.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| DBInstanceDescription | Instance description | The description of the instance. |
| Category | Instance edition | The edition of the instance. Valid values: Basic: Basic Edition HighAvailability: High-availability Edition AlwaysOn: Cluster Edition Finance: Enterprise Edition |
| ClassCode | Instance type | The instance type. Example: mssql.x4.medium.s2. |
| DBType | Database type | The type of the database. |
| DBVersion | Engine version | The database engine version. |
| Zone | Zone | The ID of the zone. |

| Parameter | Name | Description |
|---|---|---|
| LockMode | Lock mode | The lock mode of the instance. Valid values: Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked because it has expired. LockByRestoration: The instance is automatically locked for a rollback. LockByDiskQuota: The instance is automatically locked because its disk space is used up. LockReadInstanceByDiskQuota: The instance is a read-only instance and is automatically locked when the disk space is full. |
| DBInstanceStatus | Instance status | The status of the instance. |
| DBInstanceType | Instance role | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| Port | Port number | The internal port number of the instance. |
| DBInstanceClassType | Instance family | The instance family. Valid values: s: shared instance family x: general purpose instance family d: dedicated instance family h: dedicated host instance family |
| DBInstanceStorageType | Storage type | The type of storage media that is used by the instance. Valid values: localssd or ephemeralssd: local SSD _ _ cloudssd: standard SSD. _ cloudessd: enhanced SSD _ |
| AvailabilityValue | Availability status | The availability status of the instance. Unit: %. |
| IpAddress | IP address | The IP address. |
| VPCId | VPC ID | The ID of the virtual private cloud (VPC). |
| BackupStorage | Backup storage | The amount of backup storage. Unit: byte. |
| IORequest | Number of I/O requests | The number of I/O requests. |
| NetworkIn | Inbound traffic | The traffic sent from external networks, which occurred between the specified start time and the specified end time. |
| NetworkOut | Outbound traffic | The traffic sent to external networks, which occurred between the specified start time and the specified end time. |
| Storage | Volume of stored data | The amount of stored data. Unit: byte. |
| UsedStorage | Used storage | The amount of used storage space. Unit: byte. |
| AccountMaxQuantity | Maximum number of accounts that can be created | The maximum number of accounts that can be created. |
| DBInstanceCPU | Number of CPUs | The number of CPUs that are configured for the instance. |
| MaxConnections | Maximum number of concurrent connections | The maximum number of concurrent connections. |
| DBInstanceMemory | Memory | The memory capacity of the instance. Unit: MB. |
| DBInstanceDiskUsed | Used storage | The used storage. Unit: byte. |

|   |   | t Console Developer Guide·API re ference |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| MaxIOPS | Maximum IOPS | The maximum number of I/O requests that the instance can process per second. |
| DBMaxQuantity | Maximum number of databases that can be created | The maximum number of databases that can be created on the instance. |
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |

##### 4.3.5.15 Log Service

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Log Service.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | It consists of the product ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the logstore belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the logstore belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the logstore belongs. |
| InsId | Logstore ID | The ID of the logstore. |
| RegionId | Region | The ID of the region where the logstore resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Logstore creation time | The time when the logstore was created. |
| description | Description | The description of the logstore. |
| status | Status | The status of the logstore. |
| ShardSize | Number of active shards | The number of active shards. The number can include decimal places. |
| OutflowSize | Read traffic | The volume of compressed read traffic of Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| InflowSize | Write traffic | The volume of compressed write traffic of Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| WriteCount | Number of writes | The number of writes to Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| ReadCount | Number of reads | The number of reads from Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| IndexSum | Total index volume | The total volume of indexes occupied by Log Service. Unit: byte. |
| RawSum | Total data size | The total size of data occupied by Log Service. Unit: byte. |
| IndexSize | Volume of index data | The volume of index data between the specified start time and the specified end time, and also at the specified start time. Unit byte. |

##### 4.3.5.16 EBS

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Elastic Block Storage (EBS).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the EBS device belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the EBS device belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the EBS device belongs. |
| InsId | Instance ID | The ID of the EBS device. |
| RegionId | Region | The ID of the region where the EBS device resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the EBS device was created. |
| Description | Description | The description of the cloud disk or local disk. |
| DiskCategory | Disk category | The category of the cloud disk or local disk. Valid values: all: all disk categories cloud: basic disk cloudefficiency: ultra disk _ cloudssd: standard SSD _ cloudessd: enhanced SSD (ESSD) _ localssdpro: I/O-intensive local disk _ _ localhddpro: throughput-intensive local disk _ _ ephemeral: retired local disk ephemeralssd: retired local SSD _ Default value: all. |
| DiskChargeType | Billing method | The billing method of the cloud disk or local disk. Valid values: PrePaid: subscription PostPaid: pay-as-you-go |
| ExpiredTime | Expiration time | The time when the cloud desktop expires. |
| ImageId | Image ID | The ID of the image used to create the Elastic Compute Service (ECS) instance. This parameter is empty unless the disk was created from an image. This parameter value remains unchanged throughout the lifecycle of the disk. |
| Status | Disk status | The status of the disk. Valid values: Inuse _ Available Attaching Detaching Creating ReIniting All Default value: All. |
| AttachedTime | Attach time | The time when the disk was attached. The time follows the ISO 8601 standard and is displayed in UTC. This parameter is valid only when Status is set to Available. |
| BindInstanceId | ID of the instance to which the disk was attached | The ID of the instance to which the cloud disk or local disk was attached. This parameter has a value only when Status is set to Inuse. Otherwise, the parameter _ is empty. |
| Device | Mount point | The mount point of the cloud disk or local disk. |
| DiskName | Name of the cloud disk or local disk. | The name of the cloud disk or local disk. |

|   |   | ference |
|---|---|---|
| Parameter | Name | Description |
| Type | Disk type | The type of the cloud disk or local disk. Valid values: system: system disk data: data disk |
| KMSKeyId | ID of the KMS key | The ID of the Key Management Service (KMS) key used by the disk. |
| DiskSize | Disk size | The size of the cloud disk or local disk. Unit: GiB. |

##### 4.3.5.17 Snapshots

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to the snapshot feature.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the snapshot belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the snapshot belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the snapshot belongs. |
| InsId | Snapshot ID | The ID of the snapshot. |
| RegionId | Region | The region ID of the snapshot. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Snapshot creation time | The time when the snapshot was created. |
| Status | Snapshot status | The status of the snapshot. Default value: all. Valid values: progressing: The snapshot is being created. accomplished: The snapshot is created. failed: The snapshot fails to be created. all: This parameter indicates all snapshot states. |
| Progress | Creation progress | The progress of snapshot creation. Example: 100%. |
| Usage | Whether the snapshot has been used | Indicates whether the snapshot has been used to create images or disks. Valid values: image: The snapshot has been used to create custom images. disk: The snapshot has been used to create disks. imagedisk: The snapshot has been used to create custom images and data _ disks. none: The snapshot has not been used to create custom images or disks. |
| Description | Snapshot description | The description of the snapshot. |
| SnapshotCategory | Snapshot type | The type of the snapshot. Valid values: standard: normal snapshot flash: local snapshot |
| SnapshotName | Snapshot name | The name of the snapshot. |
| SourceDiskId | Source disk ID | The ID of the source disk. |
| SourceStorageType | Source disk type | The type of the source disk. |
| SnapshotSN | Snapshot serial number | The serial number of the snapshot. |

| ference |   |   |
|---|---|---|
| Parameter | Name | Description |
| LastModifiedTime | Time when the snapshot was last changed | The time when the snapshot was last changed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| SnapshotType | Type of snapshot creation | The type of snapshot creation. Valid values: auto or timer: automatically created snapshot user: manually created snapshot all: all snapshot types |
| SourceDiskType | Source disk attribute | The attribute of the source disk. The value is set to systemdata. |
| SourceDiskSize | Source disk size | The size of the system disk. Unit: GB. |
| RetentionDays | Retention period of the automatic snapshot | The retention period of the automatic snapshot. |

##### 4.3.5.18 Auto Scaling

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Auto Scaling.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the scaling group belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the scaling group belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the scaling group belongs. |
| InsId | Scaling group ID | The ID of the scaling group. |
| RegionId | Region | The ID of the region where the scaling group resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Scaling group creation time | The time when the scaling group was created. |
| LifecycleState | Status | The status of the scaling group. Valid values: Active: The scaling group is active. Active scaling groups can receive requests to execute scaling rules and trigger scaling activities. Inactive: The scaling group is inactive. Inactive scaling groups cannot receive requests to execute scaling rules. Deleting: The scaling group is being deleted. Scaling groups that are being deleted cannot receive requests to execute scaling rules and their parameters cannot be modified. |
| ScalingPolicy | Reclaim mode | Indicates the reclaim mode of the scaling group. Valid values: recycle: The reclaim mode of the scaling group is set to Shutdown and Reclaim Mode. release: The reclaim mode of the scaling group is set to Release Mode. |
| VSwitchId | vSwitch ID | The ID of the vSwitch that is associated with the scaling group. |
| ScalingGroupName | ScalinggGroup name | The name of the scaling group. |
| VpcId | VPC ID | The ID of the virtual private cloud (VPC) to which the scaling group belongs. |

|   |   | Apsara Uni-manager Managemen |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| MultiAZPolicy | Multi-zone scaling policy | The Elastic Compute Service (ECS) instance scaling policy for the multi-zone scaling group. Valid values: PRIORITY: ECS instances are scaled based on the specified vSwitch. When an ECS instance cannot be created in the zone where the vSwitch that has the highest priority resides, the system uses the vSwitch that has the next highest priority to create the instance. COSTOPTIMIZED: ECS instances are created based on the unit price of vCPU in _ ascending order. Preemptible instances are preferentially created when preemptible instance types are specified in the active scaling configuration. BALANCE: ECS instances are evenly distributed in multiple zones specified for the scaling group. |
| PendingWaitCapacity | Number of instances in the Pending state | The number of ECS instances that are in the Pending state in the scaling group. |
| TotalCapacity | Total capacity | Indicates the total weighted capacity of all ECS instances in the scaling group if the instance type weight is specified for the scaling group. If the instance type weight is not specified, this parameter indicates the total number of ECS instances in the scaling group. |
| RemovingWaitCapacity | Number of instances in the Suspending state | The number of ECS instances that are in the Suspending state in the scaling group. |
| ProtectedCapacity | Number of instances in the Protected state | The number of ECS instances that are in the Protected state in the scaling group. |
| StandbyCapacity | Number of instances in the Standby state | The number of instances that are in the Standby state in the scaling group. |
| RemovingCapacity | Number of instances in the Removing state | The number of ECS instances that are in the Removing state in the scaling group. |
| PendingCapacity | Number of instances in the Adding state | The number of ECS instances that are being added to the scaling group and are still being configured. |
| ActiveCapacity | Number of instances in the In Service state | The number of ECS instances that have been added to the scaling group and are running normally. |
| StoppedCapacity | Number of stopped instances | The number of instances that are in the Stopped state in the scaling group. |
| MaxSize | Maximum number of instances | The maximum number of ECS instances in the scaling group. |
| MinSize | Minimum number of instances | The minimum number of ECS instances in the scaling group. |
| DefaultCooldown | Default cooldown time | The default cooldown time of the scaling group. Unit: seconds. During the cooldown time, Auto Scaling executes only scaling activities that are triggered by CloudMonitor event-triggered tasks. |

##### 4.3.5.19 KMS

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Key Management Service (KMS).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the key belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the key belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the key belongs. |
| InsId | Instance ID | The ID of the key. |
| RegionId | Region | The ID of the region where the key resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |

| ference |   |   |
|---|---|---|
| Parameter | Name | Description |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Key creation time | The time when the key was created. |
| Description | Description | The description of the key. |
| KeySpec | Key type | The type of the key. |
| KeyState | Key status | The status of the key. |
| KeyUsage | Key purpose | The purpose of the key. |
| PrimaryKeyVersion | Primary key version | The primary version of the key. |
| DeleteDate | Estimated deletion time | The estimated time when the key is deleted. |
| Creator | Creator | The creator. |
| KeyArn | ARN of the key | The Alibaba Cloud Resource Name (ARN) of the key. |
| Origin | Key material source | The source of the key material. |
| MaterialExpireTime | Expiration time of the key material | The time when the key material expires. The time is displayed in UTC. If this parameter value is empty, the key material does not expire. |
| ProtectionLevel | Protection level | The protection level of the key. |
| AutomaticRotation | Automatic rotation status | Indicates whether automatic key rotation is enabled. Valid values: Enabled: Automatic key rotation is enabled. Disabled: Automatic key rotation is disabled. Suspended: Automatic key rotation is suspended. This parameter is suitable only for symmetric customer master keys (CMKs). |
| LastRotationDate | Last rotation time | The time when the last rotation was performed. The time is displayed in UTC. For a new CMK, this parameter value is the time when the initial version of the CMK was generated. |

##### 4.3.5.20 API Gateway

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to API Gateway.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | It consists of the product ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |

|   |   | t Console Developer Guide·API re ference |   |
|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| ApiName | API name | The name of the API. |
| GroupId | API group ID | The ID of the specified API group. |
| GroupName | API group name | The name of the specified API group. |
| Visibility | Type | The type of the API. |

oring

## 5 Monitoring

### 5.1 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack API requests. Table 1. Table of common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. For more information, seeV iew information about API operations. |
| Product | String | Yes | The name of the service to which the API operation belongs. Valid value: cms |
| Version | String | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Example value: 2019-01-01. |
| RegionId | String | Yes | The ID of the region. For more information, see Obtain the values of common header parameters. |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access the service. For more information, seeO btain AccessKey credentials. |
| Signature | String | Yes | The signature string. For more information, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC-SHA1 and HMAC-SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01-01T12:00:00Z. |
| Format | String | No | The format of the response. Set the value to JSON. |

| Note The Signature, SignatureMethod, SignatureVersion, SignatureNonce, Timestamp, and Format parameters are encapsulated into the SDK. You do not need to specify these parameters. |   |   |   |   |
|---|---|---|---|---|
| You can obtain the values of the | Product | and | Version | parameters in the Apsara Uni-manager Management Console by performing the following |

steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Others > API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. In the **Search by operation name** search box, enter the name of an operation to query its information.

**Common header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see Obtain the values of common header parameters. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see Obtain the values of common header parameters. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. For more information about how to obtain an instance ID, see Obtain the values of common header parameters. |

> **Note:** When you call the API operations of cloud services, you must specify the **x-acs-organizationid**, **x-acs-resourcegroupid**, and **x-acs-** **instanceid** parameters to identify the instance on which you want to perform the operation, and the organization and resource set to which the instance belongs. If you call an API operation to create an instance or query the information about one or more instances, you do not need to specify the x-acs-instanceid header. If you do not specify the headers when you call an API operation, the organization and resource set at the root level are used by default.

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

### 5.2 Major metrics for Apsara Stack services

**Precautions**

The **Sum** function is used to measure the total amount of an object during a specific time period. For example, you can measure the total amount of Internet traffic (KB/minute) that goes through an Elastic Compute Service (ECS) instance within a period of 5 minutes. You can use API operations to query monitoring data of the last 31 days. The **Dimensions** value is a JSON string. Example: `{"instanceId":"i-23gyb3kkd"}` .

**Metrics for ECS whose namespace is acs_ecs_dashboard**

oring Basic metrics The following metrics are used to monitor basic ECS properties. You can query monitoring data of these metrics without installing the CloudMonitor agent. Set **Project** to acs_ecs_dashboard and the statistical period to 60 seconds. Set Period to an integer multiple of 60. Assign the actual instance ID to **instanceId** in the **Dimensions** parameter.

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| InternetInRate | The inbound bandwidth to the Internet. | Bit/s | instanceId | Average, Minimum, and Maximum |
| IntranetInRate | The inbound bandwidth to the internal network. | Bit/s | instanceId | Average, Minimum, and Maximum |
| IntranetOutRate | The outbound bandwidth from the internal network. | Bit/s | instanceId | Average, Minimum, and Maximum |
| DiskReadBPS | The number of bytes read from the system disk per second. | Bit/s | instanceId | Average, Minimum, and Maximum |
| DiskWriteBPS | The number of bytes written to the system disk per second. | Bit/s | instanceId | Average, Minimum, and Maximum |
| DiskReadIOPS | The number of read operations performed on the system disk per second. | Count/s | instanceId | Average, Minimum, and Maximum |
| DiskWriteIOPS | The number of write operations performed on the system disk per second. | Count/s | instanceId | Average, Minimum, and Maximum |

Operating system metrics The minimum **period** value is 15 seconds.

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| cputotal _ | The total CPU utilization. | % | instanceId | Average, Minimum, and Maximum |
| memoryusedutilization _ | The memory usage. | % | instanceId | Average, Minimum, and Maximum |
| load1m _ | The average system load in the last 1 minute. Windows operating systems do not support this metric. | N/A | instanceId | Average, Minimum, and Maximum |
| load5m _ | The average system load in the last 5 minutes. Windows operating systems do not support this metric. | N/A | instanceId | Average, Minimum, and Maximum |
| load15m _ | The average system load in the last 15 minutes. Windows operating systems do not support this metric. | N/A | instanceId | Average, Minimum, and Maximum |
| diskusageutilization _ | The disk usage. | % | instanceId and device | Average, Minimum, and Maximum |
| diskreadbytes _ | The number of bytes that are read from the specified disk per second. | Byte/s | instanceId and device | Average, Minimum, and Maximum |
| diskwritebytes _ | The number of bytes that are written to the specified disk per second. | Byte/s | instanceId and device | Average, Minimum, and Maximum |
| diskreadiops _ | The number of read requests received by the specified disk per second. | Count/s | instanceId and device | Average, Minimum, and Maximum |
| diskwriteiops _ | The number of write requests received by the specified disk per second. | Count/s | instanceId and device | Average, Minimum, and Maximum |
| fsinodeutilization _ | The inode usage. | % | instanceId and device | Average, Minimum, and Maximum |

**Metrics for ApsaraDB RDS whose namespace is acs_rds_dashboard**

Set **Project** to acs_rds_dashboard and the statistical period to 300 seconds. Set **Period** to an integer multiple of 300. If you have set the monitoring period to 1 minute in the ApsaraDB RDS console, you must set the statistical period to 60 seconds or more. Assign the actual instance ID to **instanceId** in the **Dimensions** parameter. Metrics for ApsaraDB RDS for PostgreSQL

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| CpuUsage | The CPU utilization. | % | instanceId | Average, Minimum, and Maximum |
| DiskUsage | The disk usage. | % | instanceId | Average, Minimum, and Maximum |

oring

| IOPSUsage | The IOPS usage. | % | instanceId | Average, Minimum, and Maximum |
|---|---|---|---|---|
| ConnectionUsage | The connection usage. | % | instanceId | Average, Minimum, and Maximum |
| MemoryUsage | The memory usage. | % | instanceId | Average, Minimum, and Maximum |

Metrics for ApsaraDB RDS for MySQL

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| MySQLNetworkInNew _ | The amount of data sent to an ApsaraDB RDS for MySQL instance per second. | Bit/s | instanceId | Average, Minimum, and Maximum |
| MySQLNetworkOutNew _ | The amount of data sent from an ApsaraDB RDS for MySQL instance per second. | Bit/s | instanceId | Average, Minimum, and Maximum |
| CpuUsage | The CPU utilization. | % | instanceId | Average, Minimum, and Maximum |
| DiskUsage | The disk usage. | % | instanceId | Average, Minimum, and Maximum |
| IOPSUsage | The IOPS usage. | % | instanceId | Average, Minimum, and Maximum |
| ConnectionUsage | The connection usage. | % | instanceId | Average, Minimum, and Maximum |
| MemoryUsage | The memory usage. | % | instanceId | Average, Minimum, and Maximum |

Metrics for ApsaraDB RDS for SQL Server

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| SQLServerNetworkInNew _ | The amount of data sent to an ApsaraDB RDS for SQL Server instance per second. | Bit/s | instanceId | Average, Minimum, and Maximum |
| SQLServerNetworkOutNew _ | The amount of data sent from an ApsaraDB RDS for SQL Server instance per second. | Bit/s | instanceId | Average, Minimum, and Maximum |
| CpuUsage | The CPU utilization. | % | instanceId | Average, Minimum, and Maximum |
| DiskUsage | The disk usage. | % | instanceId | Average, Minimum, and Maximum |
| IOPSUsage | The IOPS usage. | % | instanceId | Average, Minimum, and Maximum |
| ConnectionUsage | The connection usage. | % | instanceId | Average, Minimum, and Maximum |
| MemoryUsage | The memory usage. | % | instanceId | Average, Minimum, and Maximum |

**Metrics for Server Load Balancer (SLB) whose namespace is acs_slb_dashboard**

Set **Project** to acs_slb_dashboard and the statistical period to 60 seconds. Set **Period** to an integer multiple of 60. Assign the actual instance ID to **instanceId** in the **Dimensions** parameter. Assign the actual port used by the SLB instance to **port** in the **Dimensions** parameter. Assign the actual endpoint of the SLB instance to **vip** in the **Dimensions** parameter.

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| UnhealthyServerCount | The number of faulty backend ECS instances. | Count | instanceId | Average, Minimum, and Maximum |
| PacketTX | The number of packets sent over the specified port per second. | Count/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| PacketRX | The number of packets received over the specified port per second. | Count/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| TrafficRXNew | The amount of data received over the specified port per second. | Bit/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| TrafficTXNew | The amount of data sent over the specified port per second. | Bit/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| ActiveConnection | The number of active connections to SLB on the specified port. | Count | instanceId, port, and vip | Average, Minimum, and Maximum |

oring

| InactiveConnection | The number of idle connections to SLB on the specified port. | Count | instanceId, port, and vip | Average, Minimum, and Maximum |
|---|---|---|---|---|
| NewConnection | The number of new connections on the specified port. | Count | instanceId, port, and vip | Average, Minimum, and Maximum |
| MaxConnection | The number of concurrent connections on the specified port. | Count | instanceId, port, and vip | Average, Minimum, and Maximum |
| DropConnection | The number of connections that are dropped per second. | Count/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| DropPacketRX | The number of inbound packets that are lost per second. | Count/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| DropPacketTX | The number of outbound packets that are lost per second. | Count/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| DropTrafficRX | The amount of inbound data that is lost per second. | Bit/s | instanceId, port, and vip | Average, Minimum, and Maximum |
| DropTrafficTX | The amount of outbound data that is lost per second. | Bit/s | instanceId, port, and vip | Average, Minimum, and Maximum |

**Metrics for KVStore for Redis whose namespace is acs_kvstore**

Set **Project** to acs_kvstore and the statistical period to 60 seconds. Set **Period** to an integer multiple of 60. Assign the actual instance ID to **instanceId** in the **Dimensions** parameter.

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| ConnectionUsage | The connection usage on the specified node. | % | instanceId and nodeId | Average and Maximum |
| FailedCount | The number of failed commands. | Count/s | instanceId | Average and Maximum |
| IntranetIn | The inbound bandwidth of the specified node. | Bit/s | instanceId and nodeId | Average and Maximum |
| IntranetInRatio | The inbound bandwidth usage of the specified node. | % | instanceId and nodeId | Average and Maximum |
| IntranetOut | The outbound bandwidth of the specified node. | Bit/s | instanceId and nodeId | Average and Maximum |
| IntranetOutRatio | The outbound bandwidth usage of the specified node. | % | instanceId and nodeId | Average and Maximum |
| MemoryUsage | The memory usage of the specified node. | % | instanceId and nodeId | Average and Maximum |
| UsedQPS | The average queries on the specified node per second. | Count | instanceId and nodeId | Average and Maximum |

**Metrics for Object Storage Service (OSS) whose namespace is acs_oss_dashboard**

| Metric | Metric name | Unit | Level |
|---|---|---|---|
| Availability | Availability | % | Bucket level |
| RequestValidRate | Valid request rate | % | Bucket level |
| TotalRequestCount | Total requests | N/A | Bucket level |
| ValidRequestCount | Valid requests | N/A | Bucket level |
| InternetSend | Internet outbound traffic | Byte | Bucket level |
| InternetRecv | Internet inbound traffic | Byte | Bucket level |
| IntranetSend | Intranet outbound traffic | Byte | Bucket level |
| IntranetRecv | Intranet inbound traffic | Byte | Bucket level |
| CdnSend | CDN Outbound Traffic by User | Byte | Bucket level |
| CdnRecv | CDN Inbound Traffic by User | Byte | Bucket level |
| SyncSend | Cross-region replication (CRR) outbound traffic | Byte | Bucket level |
| SyncRecv | CRR inbound traffic | Byte | Bucket level |
| ServerErrorCount | Server-side error requests | N/A | Bucket level |
| ServerErrorRate | Server-side error request rate | % | Bucket level |
| NetworkErrorCount | Network-side error requests | N/A | Bucket level |

oring

| NetworkErrorRate | Network-side error request rate | % | Bucket level |
|---|---|---|---|
| AuthorizationErrorCount | Client-side authorization error requests | N/A | Bucket level |
| AuthorizationErrorRate | Client-side authorization error request rate | % | Bucket level |
| ResourceNotFoundErrorCount | Client-side error requests indicating resources not found | N/A | Bucket level |
| ResourceNotFoundErrorRate | Rate of client-side error requests indicating resources not found | % | Bucket level |
| ClientTimeoutErrorCount | Client-side timeout error requests | N/A | Bucket level |
| ClientTimeoutErrorRate | Client-side timeout error request rate | % | Bucket level |
| ClientOtherErrorCount | Other client-side error requests | N/A | Bucket level |
| ClientOtherErrorRate | Rate of other client-side error requests | % | Bucket level |
| SuccessCount | Successful requests | N/A | Bucket level |
| SuccessRate | Successful request rate | % | Bucket level |
| RedirectCount | Redirect requests | N/A | Bucket level |
| RedirectRate | Redirect request rate | % | Bucket level |
| MaxGetObjectE2eLatency | Maximum E2E latency of GetObject requests | Millisecond | Bucket level |
| MaxGetObjectServerLatency | GetObject Request Maximum Server Latency | Millisecond | Bucket level |
| MaxHeadObjectE2eLatency | Maximum E2E latency of HeadObject requests | Millisecond | Bucket level |
| MaxHeadObjectServerLatency | Maximum server latency of HeadObject requests | Millisecond | Bucket level |
| MaxPutObjectE2eLatency | Maximum E2E latency of PutObject requests | Millisecond | Bucket level |
| MaxPutObjectServerLatency | Maximum server latency of PutObject requests | Millisecond | Bucket level |
| MaxPostObjectE2eLatency | Maximum E2E latency of PostObject requests | Millisecond | Bucket level |
| MaxPostObjectServerLatency | Maximum server latency of PostObject requests | Millisecond | Bucket level |
| MaxAppendObjectE2eLatency | Maximum E2E latency of AppendObject requests | Millisecond | Bucket level |
| MaxAppendObjectServerLatency | Maximum server latency of AppendObject requests | Millisecond | Bucket level |
| MaxUploadPartE2eLatency | Maximum E2E latency of UploadPart requests | Millisecond | Bucket level |
| MaxUploadPartServerLatency | Maximum server latency of UploadPart requests | Millisecond | Bucket level |
| MaxUploadPartCopyE2eLatency | Maximum E2E latency of UploadPartCopy requests | Millisecond | Bucket level |
| MaxUploadPartCopyServerLatency | UploadPartCopy Request Maximum Server Latency | Millisecond | Bucket level |
| GetObjectCount | Successful GetObject requests | N/A | Bucket level |
| HeadObjectCount | Successful HeadObject requests | N/A | Bucket level |
| PostObjectCount | Successful PostObject requests | N/A | Bucket level |
| AppendObjectCount | Successful AppendObject requests | N/A | Bucket level |
| UploadPartCount | Successful UploadPart requests | N/A | Bucket level |
| DeleteObjectCount | Successful DeleteObject requests | N/A | Bucket level |
| DeleteObjectsCount | Successful DeleteObjects requests | N/A | Bucket level |

**Metrics for VPN Gateway**

Set **Project** to acs_vpn and the statistical period to 60 seconds. Set **Period** to an integer multiple of 60.

| Metric | Description | Unit | Dimensions |
|---|---|---|---|
| sslclient.count _ | The number of SSL connections. | Count | instanceId |
| ipsec.rxPkgs | The number of inbound packets of a connection per second. | Packet/s | VpnConnectionId |

oring

| ipsec.txPkgs | The number of outbound packets of a connection per second. | Packet/s | VpnConnectionId |
|---|---|---|---|
| ipsecrx.rate _ | The inbound bandwidth of a connection. | Bit/s | VpnConnectionId |
| ipsectx.rate _ | The outbound bandwidth of a connection. | Bit/s | VpnConnectionId |

**Metrics for API Gateway**

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| Latency | The response time. | Millisecond | userId, region, and apiUid | Average |
| SumQPS | The overall queries per second (QPS). | Count | userId, region, and apiUid | Count |
| TrafficRX | The inbound bandwidth. | KBytes | userId, region, and apiUid | Sum |
| TrafficTX | The outbound bandwidth. | KBytes | userId, region, and apiUid | Sum |
| code2XX | code2XX | Count | userId, region, and apiUid | Value |
| code4XX | code4XX | Count | userId, region, and apiUid | Value |
| code5XX | code5XX | Count | userId, region, and apiUid | Value |

**Metrics for EIP**

Set **Project** to acs_vpc_eip and the statistical period to 60 seconds. Set **Period** to an integer multiple of 60. Assign the actual instance ID to **instanceId** in the **Dimensions** parameter. Assign the actual elastic IP address (EIP) to **ip** in the **Dimensions** parameter.

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| netrx.rate _ | The inbound bandwidth. | Bit/s | userld and instanceld | Value |
| netrxPkgs.rate _ | The number of inbound packets per second. | Packet/s | userld and instanceld | Value |
| netrx.rate _ | The outbound bandwidth. | Bit/s | userld and instanceld | Value |
| nettxPkgs.rate _ | The number of outbound packets per second. | Packet/s | userld and instanceld | Value |
| outratelimitdropspeed _ _ _ | The packet loss rate when the data transfer rate is limited. | Packet/s | userld and instanceld | Average |

**Metrics for AnalyticDB for PostgreSQL**

| Metric | Description | Unit | Dimensions | Statistics |
|---|---|---|---|---|
| ConnectionUsage | The connection usage. | % | userId, instanceId, and role | Average |
| CpuUsage | The CPU utilization. | % | userId, instanceId, and role | Average |
| DiskUsage | The disk usage. | % | userId, instanceId, and role | Average |
| IOPSUsage | The IOPS usage. | % | userId, instanceId, and role | Average |
| MemoryUsage | The memory usage. | % | userId, instanceId, and role | Average |

### 5.3 API Reference

#### 5.3.1 Cloud Products

##### 5.3.1.1 DescribeProjectMeta

You can call this operation to query information of monitored services in Cloud Monitor. The information obtained by this operation includes the service description, namespace, and tags.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProjectMeta | The operation that you want to perform. Set the value to DescribeProjectMeta. |
| callerType | String | No | "" | The type of the caller. |

oring

| Labels | String |   |   |   |   | The tags of metrics. You can specify tags of metrics to filter services. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag |   |
|   |   |   |   |   |   | name","value":"Tag value"},{"name":"Tag |   |   |
|   |   |   |   |   |   | name","value":"Tag value"}] |   |   |
|   |   |   | No | [{"name":"product","value":" ECS"}] |   |   |   |   |
| PageNumber | Integer |   | No | 1 |   | The number of the page to return. Default value: 1. |   |   |
| PageSize | Integer |   | No | 30 |   | The number of entries to return on each page. Default value: 30. Note Apsara Stack does not limit the value of this parameter. If you want to view all desired entries on a small number of pages, set this parameter to a greater value. |   |   |
| RequestId | string |   | No | sdsdsdd |   | The ID of the request. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RequestId | String | 4C2061B2-3B1B-43BF-A4A4- C53426F479C0 | The ID of the request. |
| Resources | Array | N/A | The information of services found. |
| Resource | N/A | N/A | The information of a service found. |
| Description | String | CDN | The description of the service. |

oring

| Labels | String |   |   | The tags of metrics. Services were filtered based on the specified tags. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag name","value":"Tag value"}, |   |
|---|---|---|---|---|---|
|   |   |   |   |   | [{"name":"Tag name","value":"Tag value"}, |
|   |   |   |   | {"name":"Tag name","value":"Tag value"}] |   |
|   |   |   | [{"groupFlag":true}] |   |   |
| Namespace | String |   | acscdn _ | The namespace of the service, which is used to distinguish between services. Typically, the value of the format is acs_Abbreviation of the service name . |   |
| Success | Boolean |   | true | Indicates whether the call was successful. |   |
| Total | String |   | 12 | The total number of entries returned. |   |

| acs_Abbreviation of |   |
|---|---|

|   | the service name |
|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeProjectMeta &<Common request parameters>
```

Sample success responses

| Note The response content varies with the services that are actually monitored. |   |
|---|---|
| JSON | format |
| { "PageNumber":1, "PageSize":5, "RequestId":"4C2061B2-3B1B-43BF-A4A4-C53426F479C0", "Success":true, "Code":200, "Total":62, "Resources":{ "Resource":[{ "Description": "ECS", "Labels": "[{\"name\":\"product\",\"value\":\"ECS\"}, {\"name\":\"productCategory\",\"value\":\"ecs,ecs_net_interface,hpc_node,hpc_cluster\"},{\"name\":\"groupFlag\",\"value\":\"true\"}, {\"name\":\"cnName\",\"value\":\"ECS\"},{\"name\":\"enName\",\"value\":\"ECS\"}]", "Namespace": "acs_ecs_dashboard" }, ] } } |   |

##### 5.3.1.2 DescribeMetricLast

You can call this operation to query the latest monitoring data of a monitored object.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

oring

| Action | String | Yes | DescribeMetricLast | The operation that you want to perform. Set the value to DescribeMetricLast. |
|---|---|---|---|---|
| MetricName | String | Yes | CPUUtilization | The name of the metric. |
| Namespace | String | Yes | acsecsdashboard _ _ | The namespace of the service. Specify the value in the format of acsService name. _ |
| Dimensions | String | No | [{"instanceId":"XXXXXX"}] | The dimension map of the monitored resources. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores (), forward slashes (/), and _ backslashes (\). Note If you hope to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |
| EndTime | String | No | 2019-01-31 10:10:00 | The end of the time range for the query. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Note Only a time range within the last 270 days can be specified to query. |
| Express | String | No | {"groupby": ["userId","instanceId"]} | The expression for real-time computation on the query results. |
| Length | String | No | 1000 | The number of entries to return on each page. Default value: 1000. |
| NextToken | String | No | 15761432850009dd70bb64cf f1f0fff6c0b08ffff073be5fb1e7 85e2b020f7fed9b5e137bd81 0a6d6cff5ae**** | The pagination cursor. If the number of entries that match the search criteria exceeds the maximum number allowed on a single page, a pagination cursor is returned. This pagination cursor can be used as an input parameter to obtain entries on the next page. If a response does not contain pagination cursors, all query results are returned. |
| Period | String | No | 60 | The time interval at which to query monitoring data. Typically, the time interval is the same as the interval for reporting metric data. Unit: seconds. If you do not specify this parameter, raw data is queried at the reporting interval specified when the corresponding metric was created. If a statistical period was specified for the corresponding alert rule, raw data is queried based on the statistical period. |
| StartTime | String | No | 2019-01-31 10:00:00 | The start of the time range for the query. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Note Only a time range that covers a maximum of 31 days within the last 270 days can be specified to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 021472A6-25E3-4094-8D00- BA4B6A5486C3 | The ID of the request. |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Period | String | 60 | The time interval at which monitoring data was queried. Unit: seconds. |

oring

| NextToken | String | xxxxxx | The pagination cursor. |
|---|---|---|---|
| Datapoints | String | [{"timestamp":1548777660000," userId":"123","instanceId":"i- abc","Minimum":9.92,"Average": 9.92,"Maximum":9.92}] | The list of monitoring data. |
| Message | String | Success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMetricLast &MetricName=CPUUtilization &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <QueryMetricListResponse> <Period>60</Period> <Datapoints> <Datapoints> <timestamp>1490152860000</timestamp> <Maximum>100</Maximum> <userId> 123456789876****</userId> <Minimum>93.1</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.52</Average> </Datapoints> <Datapoints> <timestamp>1490152920000</timestamp> <Maximum>100</Maximum> <userId> 123456789876**** </userId> <Minimum>92.59</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.49</Average> </Datapoints> <Datapoints> <timestamp>1490152980000</timestamp> <Maximum>100</Maximum> <userId>123456789876****</userId> <Minimum>92.86</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.44</Average> </Datapoints> <Datapoints> <timestamp>1490153040000</timestamp> <Maximum>100</Maximum> <userId>123456789876****</userId> <Minimum>91.43</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.36</Average> </Datapoints> <Datapoints> <timestamp>1490153100000</timestamp> <Maximum>100</Maximum> <userId>123456789876****</userId> <Minimum>93.55</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.51</Average> </Datapoints> <Datapoints> <timestamp>1490153160000</timestamp> <Maximum>100</Maximum> <userId>123456789876****</userId> <Minimum>93.1</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.52</Average> </Datapoints> <Datapoints> <timestamp>1490153220000</timestamp> <Maximum>100</Maximum> <userId>123456789876****</userId> <Minimum>92.59</Minimum> <instanceId>i-abcdefgh12****</instanceId> <Average>99.42</Average> </Datapoints> <Datapoints> <timestamp>1490153280000</timestamp> <Maximum>100</Maximum> <userId>123456789876****</userId> |   |

oring

```xml
            <Minimum>91.18</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.34</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153340000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.86</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.46</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153400000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.18</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.35</Average>
        </Datapoints>
    </Datapoints>
    <RequestId>6661EC50-8625-4161-B349-E0DD59002AB7</RequestId>
    <Success>true</Success>
    <Code>200</Code>
</QueryMetricListResponse>
```

| JSON | format |
|---|---|
| { "Period":"60", "Datapoints":[ { "timestamp":1490152860000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":93.1, "Average":99.52 }, { "timestamp":1490152920000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.59, "Average":99.49 }, { "timestamp":1490152980000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.86, "Average":99.44 }, { "timestamp":1490153040000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":91.43, "Average":99.36 }, { "timestamp":1490153100000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":93.55, "Average":99.51 }, { "timestamp":1490153160000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":93.1, "Average":99.52 }, { "timestamp":1490153220000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.59, "Average":99.42 |   |

oring `},` `{`

```json
   "timestamp":1490153280000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.34
```

`},` `{`

```json
   "timestamp":1490153340000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.46
```

`},` `{`

```json
   "timestamp":1490153400000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.18,
   "Average":99.35
```

`],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

##### 5.3.1.3 DescribeMetricList

You can call this operation to query the monitoring data of time series metrics of Apsara Stack services in a specified period. For more information about how to assign values to the Namespace, Project, Metric, Period, and Dimensions parameters for Apsara Stack services, see Major metrics for Apsara Stack services.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricList | The operation that you want to perform. Set the value to DescribeMetricList. |
| MetricName | String | Yes | cpuidle _ | The name of the metric that you want to query. |
| Namespace | String | Yes | acsecsdashboard _ _ | The namespace of the service. Specify the value in the format of acsService name. _ |
| Dimensions | String | No | [{"instanceId": "i- abcdefgh12****"}] | The dimension map of the monitored resources. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores (), forward slashes (/), and _ backslashes (\). Note If you want to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |
| EndTime | String | No | 2019-01-30 00:10:00 | The end of the time range for the query. Supported formats: UNIX timestamp: The value can be a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Time format: The value can be in the YYYY-MM- DDThh:mm:ssZ format. |
| Express | String | No | {"groupby": ["userId","instanceId"]} | The expression for real-time computation on the query results. Only the groupby expression is supported, which is similar to the groupby statement used in databases. |
| Length | String | No | 1000 | The number of entries to return on each page. Default value: 1000. |

oring

| NextToken | String | No | 15761485350009dd70bb64cf f1f0fff750b08ffff073be5fb1e 785e2b020f1a949d5ea14aea 7fed82f01dd87311 | The pagination cursor. Note You do not need to specify this parameter if you only want to obtain entries on the first page. The pagination cursor returned in a response can be used as an input parameter for obtaining entries on the next page. If a response contains no pagination cursors, all the query result has been returned. |
|---|---|---|---|---|
| Period | String | No | 60 | The time interval at which monitoring data is queried. Unit: seconds. Valid values: 60, 300, and 900, which represent 1 minute, 5 minutes, and 15 minutes. Note Set this parameter to suit your needs. For example, if you set this parameter to 60, only 1,000 records are returned, though a total of 1,440 records are generated. This is because the maximum number of records that can be returned for each query is 1,000. If you set this parameter to 300, 288 records are returned. |
| StartTime | String | No | 2019-01-30 00:00:00 | The start of the time range for the query. Supported formats: UNIX timestamp: The value can be a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Time format: The value can be in the YYYY-MM- DDThh:mm:ssZ format. Note The period specified by StartTime and EndTime includes the time point specified by EndTime but does not include the time point specified by StartTime. StartTime must be earlier than EndTime. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3121AE7D-4AFF-4C25-8F1D- C8226EBB1F42 | The ID of the request. |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Success | Boolean | true | Indicates whether the call was successful. |
| NextToken | String | 15761441850009dd70bb64cff1f0 fff6d0b08ffff073be5fb1e785e2b0 20f7fed9b5e137bd810a6d6cff5a ee816 | The pagination cursor. Note If this parameter was not specified, only entries on the first page were returned. If a response contains a pagination cursor, more entries are to be returned. If a response contains no pagination cursors, all the query result has been returned. |
| Period | String | 60 | The time interval at which monitoring data was queried. Unit: seconds. Valid values: 60, 300, and 900. |
| Datapoints | String | [{"timestamp":1548777660000," userId":"123","instanceId":"i- abc","Minimum":9.92,"Average": 9.92,"Maximum":9.92}] | The list of monitoring data. |
| Message | String | Success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMetricList &MetricName=cpu_idle &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format oring

```xml
<Period>60</Period> <Datapoints>
    <timestamp>1490152860000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.1</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.52</Average>
</Datapoints> <Datapoints>
    <timestamp>1490152920000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.59</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.49</Average>
</Datapoints> <Datapoints>
    <timestamp>1490152980000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.86</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.44</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153040000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.43</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.36</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153100000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.55</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.51</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153160000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>93.1</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.52</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153220000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.59</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.42</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153280000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.18</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.34</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153340000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>92.86</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.46</Average>
</Datapoints> <Datapoints>
    <timestamp>1490153400000</timestamp>
    <Maximum>100</Maximum>
    <userId>123456789876****</userId>
    <Minimum>91.18</Minimum>
    <instanceId>i-abcdefgh12****</instanceId>
    <Average>99.35</Average>
</Datapoints> <RequestId>6A5F022D-AC7C-460E-94AE-B9E75083D027</RequestId> <Success>true</Success> <Code>200</Code>
```

oring

| JSON | format |
|---|---|
| { "Period":"60", "Datapoints":[ { "timestamp":1490152860000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":93.1, "Average":99.52 }, { "timestamp":1490152920000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.59, "Average":99.49 }, { "timestamp":1490152980000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.86, "Average":99.44 }, { "timestamp":1490153040000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":91.43, "Average":99.36 }, { "timestamp":1490153100000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":93.55, "Average":99.51 }, { "timestamp":1490153160000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":93.1, "Average":99.52 }, { "timestamp":1490153220000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.59, "Average":99.42 }, { "timestamp":1490153280000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":91.18, "Average":99.34 }, { "timestamp":1490153340000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":92.86, "Average":99.46 }, { "timestamp":1490153400000, "Maximum":100, "userId":"123456789876****", "instanceId":"i-abcdefgh12****", "Minimum":91.18, "Average":99.35 } ], "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027", |   |
| 298 > Document Version: 20251105 |   |

oring

```json
 "Success":true,
 "Code":"200"
```

##### 5.3.1.4 DescribeMetricMetaList

Queries the descriptions of time series metrics that are supported in CloudMonitor. This operation is used with DescribeMetricList and DescribeMetricLast.

**Request parameters**

|   | Parameter |   | Type | Required | Example | Description |   |
|---|---|---|---|---|---|---|---|
|   | Action |   | String | Yes | DescribeMetricMetaList | The operation that you want to perform. Set the value to DescribeMetricMetaList. |   |
|   | Namespace |   | String | Yes | acskvstore _ | The namespace of the service. You can call the DescribeProjectMeta operation to query the namespace of each service. |   |
|   |   |   |   |   |   | The tags of the metric. You must specify the tags in the following format: [{&quot;name&quot;:&quot;Tag |   |
|   |   |   |   |   |   |   | [{&quot;name&quot;:&quot;Tag |
|   |   |   |   |   |   | key&quot;,&quot;value&quot;:&quot;Tag value&quot;}, |   |
|   |   |   |   |   |   | {&quot;name&quot;:&quot;Tag |   |
|   |   |   |   |   |   | key&quot;,&quot;value&quot;:&quot;Tag |   |
|   |   |   |   |   |   | value&quot;}] |   |
|   | Labels |   | String | No | [{&quot;name&quot;:&quot; productCategory&quot;,&quo t;value&quot;:&quot;kvstore _ old&quot;}] |   |   |
|   | MetricName |   | String | No | CPUUtilization | The name of the metric. The metric with the specified name is matched. |   |
|   | PageNumber |   | Integer | No | 1 | The number of the page to return. Default value: 1. |   |
|   | PageSize |   | Integer | No | 30 | The number of entries to return on each page. Default value: 30. |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. |
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| RequestId | String | 0CCE0AF0-053C-4B13-A583- DC9A85785D49 | The request ID for troubleshooting. |
| Message | String | success | The error message returned. |
| Resources |   |   | The information of metrics found. |
| Resource |   |   | The information of a metric found. |
| Description | String | CPUUtilization | The description of the metric. |
| Dimensions | String | instanceId | The dimensions of the metric. Separate multiple dimensions with commas (,). |

oring

| Labels | String | [{&quot;name&quot;:&quot;alert Unit&quot;,&quot;value&quot;:&q uot;Bytes&quot;}, {&quot;name&quot;:&quot;minAl ertPeriod&quot;,&quot;value&qu ot;:&quot;60&quot;}, {&quot;name&quot;:&quot;metri cCategory&quot;,&quot;value&qu ot;:&quot;instanceId&quot;}, {&quot;name&quot;:&quot;instan ceType&quot;,&quot;value&quot; :&quot;disaster&quot;}, {&quot;name&quot;:&quot;isala _ rm&quot;,&quot;value&quot;:&qu ot;true&quot;}, {&quot;name&quot;:&quot;produ ctCategory&quot;,&quot;value&q uot;:&quot;kvstoreold&quot;}] _ |   | The tags of the metric. The value is a JSON array string in the format of [{&quot;name&quot;:&quot;Tag |   |
|---|---|---|---|---|---|
|   |   |   |   |   | [{&quot;name&quot;:&quot;Tag |
|   |   |   | &quot;name&quot;:&quot;minAl | name&quot;,&quot;value&quot;:&quot;Tag value&quot;}] |   |
| MetricName | String | CPUUtilization |   | The name of the metric that you want to query. |   |
| Namespace | String | acskvstore _ |   | The namespace of the service. The namespace is in the format of acsService name. _ |   |
| Periods | String | 60,300 |   | The statistical period of the metric. Separate multiple periods with commas (,). Example: 15,60,900. |   |
| Statistics | String | Average,Minimum,Maximum |   | The statistical method of the metric. Separate multiple statistical methods with commas (,). Example: Average,Minimum,Maximum. |   |
| Unit | String | % |   | The unit of the metric. |   |
| TotalCount | String | 12 |   | The total number of records. |   |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricMetaList &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses

| Note The response content varies with the services that are actually monitored. |   |
|---|---|
| XML | format |
| <DescribeMetricMetaListResponse> <TotalCount>120</TotalCount> <RequestId>EA94B362-973C-4D6B-BE94-6774E18915C2</RequestId> <Success>true</Success> <Code>200</Code> <Resources> <Resource> <Description>ECS.CPUUtilization</Description> <Statistics>Average,Minimum,Maximum</Statistics> <MetricName>CPUUtilization</MetricName> <Labels>[{"name":"alertUnit","value":"%"},{"name":"alertDefault","value":"80"},{"name":"minAlertPeriod","value":"60"}, {"name":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels> <Dimensions>userId,instanceId</Dimensions> <Namespace>acs_ecs_dashboard</Namespace> <Periods>60,300</Periods> <Unit>%</Unit> </Resource> <Resource> <Description></Description> <Statistics>Average,Maximum,Minimum</Statistics> <MetricName>DiskReadBPS</MetricName> <Labels>[{"name":"alertUnit","value":"Mbytes/s"},{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"n ame":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels> <Dimensions>userId,instanceId</Dimensions> <Namespace>acs_ecs_dashboard</Namespace> <Periods>60,300</Periods> <Unit>bytes/s</Unit> </Resource> <Resource> <Description>The number of read operations performed on the system disk per second.</Description> <Statistics>Average,Minimum,Maximum</Statistics> <MetricName>DiskReadIOPS</MetricName> <Labels>[{"name":"alertUnit","value":"Count/Second"},{"name":"minAlertPeriod","value":"60"}, {"name":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels> <Dimensions>userId,instanceId</Dimensions> <Namespace>acs_ecs_dashboard</Namespace> |   |

oring

```json
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"n
ame":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The number of write operations performed on the system disk per second.</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},{"name":"minAlertPeriod","value":"60"},
{"name":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupCPUUtilization</MetricName>
            <Labels>[{"name":"alertUnit","value":"%"},{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</Labe
ls>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"n
ame":"metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},{"name":"minAlertPeriod","value":"60"},
{"name":"metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"n
ame":"metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},{"name":"minAlertPeriod","value":"60"},
{"name":"metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
    </Resources>
</DescribeMetricMetaListResponse>
```

| JSON | format |
|---|---|
| { |   |

oring

```json
 "TotalCount":1853,
 "RequestId":"CDE9EAFF-D54E-4024-BBFC-B0AAC883143B",
 "Success":true,
 "Code":200,
 "Resources":{
  "Resource":[
```

`{`

```json
    "Description":"The rated capacity of the disk",
    "MetricName":"ads.diskSize",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"300\"},{\"name\":\"alertDefault\",\"value\":\"\"},
{\"name\":\"unitFactor\",\"value\":\"1\"},{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},{\"name\":\"productCategory\",\"value\":\"ads\"}, {\"name\":\"is_alarm\",\"value\":\"true\"},{\"name\":\"metricCategory\",\"value\":\"workerId\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"Mbytes"
```

`},` `{`

```json
    "Description":"The used space of the disk",
    "MetricName":"ads.diskUsed",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},{\"name\":\"minAlertPeriod\",\"value\":\"300\"},
{\"name\":\"metricCategory\",\"value\":\"workerId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"Mbytes"
```

`},` `{`

```json
    "Description":"The disk usage",
    "MetricName":"ads.diskUsedPercent",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},{\"name\":\"minAlertPeriod\",\"value\":\"300\"},
{\"name\":\"metricCategory\",\"value\":\"workerId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The number of unconsumed messages in the queue",
    "MetricName":"QueueMessageAccumulation",
    "Statistics":"Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},{\"name\":\"alertDefault\",\"value\":\"\"},
{\"name\":\"unitFactor\",\"value\":\"1\"},{\"name\":\"alertUnit\",\"value\":\"count/min\"},{\"name\":\"productCategory\",\"value\":\"amqp\"},{ \"name\":\"is_alarm\",\"value\":\"true\"},{\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of new messages in the queue per minute",
    "MetricName":"QueueMessageInput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},{\"name\":\"alertDefault\",\"value\":\"\"},{\"n
ame\":\"unitFactor\",\"value\":\"1\"},{\"name\":\"alertUnit\",\"value\":\"count/min\"},{\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"},{\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of unconsumed messages in the queue",
    "MetricName":"QueueMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},{\"name\":\"alertDefault\",\"value\":\"\"},
{\"name\":\"unitFactor\",\"value\":\"1\"},{\"name\":\"alertUnit\",\"value\":\"count/min\"},{\"name\":\"productCategory\",\"value\":\"amqp\"},{ \"name\":\"is_alarm\",\"value\":\"true\"},{\"name\":\"metricCategory\",\"value\":\"queue\"}]",
    "Dimensions":"userId,regionId,vhostName,queueName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages generated by the instance per minute",
    "MetricName":"VhostMessageInput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},{\"name\":\"alertDefault\",\"value\":\"\"},
{\"name\":\"unitFactor\",\"value\":\"1\"},{\"name\":\"alertUnit\",\"value\":\"count/min\"},{\"name\":\"productCategory\",\"value\":\"amqp\"},{ \"name\":\"is_alarm\",\"value\":\"true\"},{\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

oring `},` `{`

```json
    "Description":"The number of messages consumed by the instance per minute",
    "MetricName":"VhostMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},{\"name\":\"alertDefault\",\"value\":\"\"},
{\"name\":\"unitFactor\",\"value\":\"1\"},{\"name\":\"alertUnit\",\"value\":\"count/min\"},{\"name\":\"productCategory\",\"value\":\"amqp\"},{ \"name\":\"is_alarm\",\"value\":\"true\"},{\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Latency",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"ms\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"ms"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"SumQPS",
    "Statistics":"Count",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"TrafficRX",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"KBytes"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"TrafficTX",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300,900",
    "Unit":"KBytes"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code2XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code4XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"tru\"}]",
    "Dimensions":"userId,region,apiUid",
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"code5XX",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,region,apiUid",
"Namespace":"acsapigatewaydashboard",
```

oring

```json
aespace:acs_apgateway_dasboad,
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"pps"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.rate",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"unitFactor\",\"value\":\"1048576\"},{\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"pps"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.rate",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"unitFactor\",\"value\":\"1048576\"},{\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.ratePercent",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"Maximum network traffic per unit time",
    "MetricName":"BPS",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"unitFactor\",\"value\":\"1000000\"},{\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"GroupBPS",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"unitFactor\",\"value\":\"1000000\"},{\"name\":\"metricCategory\",\"value\":\"groupId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
"MetricName":"GroupInternetOut"
```

oring

```json
    "MetricName":"GroupInternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"unitFactor\",\"value\":\"1000000\"},{\"name\":\"metricCategory\",\"value\":\"groupId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bytes"
```

`},` `{`

```json
    "Description":"The downstream traffic",
    "MetricName":"InternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"unitFactor\",\"value\":\"1000000\"},{\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bytes"
```

`},` `{`

```json
    "Description":"The average number of accesses in the specified time range",
    "MetricName":"QPS",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"UserQPS",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},{\"name\":\"alertDefault\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"},{\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":""
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Usercode4xx",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"Usercode5xx",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"Count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"UserhitRate",
    "Statistics":"Average",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The percentage of 4XX HTTP status codes over total status codes in the specified time range",
    "MetricName":"code4xx",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"metricCategory\",\"value\":\"instanceId\"},{\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"%"
```

oring `]`

#### 5.3.2 Alert rules for time series metrics

##### 5.3.2.1 DescribeMetricRuleList

You can call this operation to query alert rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricRuleList | The operation that you want to perform. Set the value to DescribeMetricRuleList. |
| Namespace | String | No | acsecsdashboard _ _ | The namespace of the service. Note For more information, see Major metrics for Apsara Stack services. |
| MetricName | String | No | cputotal _ | The name of the metric. Note For more information, see Major metrics for Apsara Stack services. |
| EnableState | Boolean | No | true | Specifies whether to query enabled or disabled alert rules. Valid values: true: indicates that enabled alert rules are queried. false: indicates that disabled alert rules are queried. This parameter is empty by default, which indicates that both enabled and disabled rules are queried. |
| Page | String | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | String | No | 10 | The number of entries to return on each page. Default value: 10. |
| AlertState | String | No | ALARM | The status of the alert rule. Valid values: OK: No active alerts are triggered based on the alert rule. ALARM: At least one alert is triggered based on the alert rule. INSUFFICIENTDATA: No data is available. _ |
| Dimensions | String | No | {"instanceId":"i-xy123****"} | The dimension map of the monitored resources. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores (), forward slashes (/), and _ backslashes (\). Note If you hope to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |
| RuleName | String | No | ECS CPU alert rule | The name of the alert rule. Note This parameter supports fuzzy match. |
| GroupId | String | No | 123456 | The ID of the application group. |
| RuleIds | String | No | a151cd6023eacee2f0978e03 863cc1697c8950812**** | The ID of the alert rule. Note You can specify a maximum of 20 alert rule IDs. Separate multiple IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

oring

| RequestId | String | 0E657631-CD6C-4C24-9637- 98D000B9272C | The ID of the request. |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Total | String | 21 | The total number of entries returned. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Alarms | Array | None | The list of alert rules. |
| Alarm | None | None | The information of an alert rule. |
| AlertState | String | OK | The status of the alert rule. Valid values: OK: No active alerts are triggered based on the alert rule. ALARM: At least one alert is triggered based on the alert rule. INSUFFICIENTDATA: No data is available. _ |
| ContactGroups | String | Default alert contacts | The information of the alert contacts. |
| Dimensions | String | {"userId":"4342","instanceId":"21 2312"} | The dimension map of the monitored resources. The value is a collection of key-value pairs. A typical key- value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores (), forward slashes (/), and backslashes (\). _ Note If you set Dimensions to ordered strings in the request, the value of this parameter is a key-value map expressed by JSON strings. |
| EffectiveInterval | String | 00:00-23:59 | The time period during which the alert rule is effective. |
| EnableState | Boolean | true | Indicates whether enabled or disabled alert rules are queried. Valid values: true: indicates that enabled alert rules are queried. false: indicates that disabled alert rules are queried. This parameter is empty by default, which indicates that both enabled and disabled rules are queried. |
| Escalations | None | None | The conditions that trigger different levels of alerts. |
| Critical | None | None | The conditions for triggering critical-level alerts. |
| ComparisonOperator | String | GreaterThanOrEqualToThreshold | The comparison operator of the threshold for critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical method for critical-level alerts. |
| Threshold | String | 90 | The threshold for critical-level alerts. |

|   | value |
|---|---|

oring

| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for critical-level alerts before a critical-level alert is triggered. |
|---|---|---|---|
| Info | None | None | The conditions for triggering info-level alerts. |
| ComparisonOperator | String | GreaterThanOrEqualToThreshold | The comparison operator of the threshold for info-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical method for info-level alerts. |
| Threshold | String | 90 | The threshold for info-level alerts. |
| Times | String | 1 | The consecutive number of times for which the metric value exceeds the threshold for info-level alerts before an alert is triggered. |
| Warn | None | None | The conditions for triggering warn-level alerts. |
| ComparisonOperator | String | GreaterThanOrEqualToThreshold | The comparison operator of the threshold for warn-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical method for warn-level alerts. |
| Threshold | String | 90 | The threshold for warn-level alerts. |
| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for warn-level alerts before a warn-level alert is triggered. |
| GroupId | String | 123456 | The ID of the application group. |
| GroupName | String | My application group | The name of the application group. Note If the alert rule is associated with an application group, the name of the application group is returned in this parameter. |
| MailSubject | String | An alert occurs | The subject of the alert notification email. |
| MetricName | String | cputotal _ | The name of the metric. |

oring

| Namespace | String | acsecsdashboard _ _ | The namespace of the service. |
|---|---|---|---|
| NoEffectiveInterval | String | 00:00-23:59 | The time period during which the alert rule is ineffective. |
| Period | String | 60 | The statistical period. |
| Resources | String | [{\"instanceId\":\"i- a2d5q7pm3f9yr29e****\"}, {\"instanceId\":\"i- a2d5q7pm3f9yr29e****\"} | The resources that are associated with the alert rule. |
| RuleId | String | a151cd6023eacee2f0978e03863 cc1697c895012**** | The ID of the alert rule. |
| RuleName | String | My alert rule | The name of the alert rule. |
| SilenceTime | String | 86400 | The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: 86400. Minimum value: 3600. Only one alert is reported during each mute period even if the metric value consecutively exceeds the alert rule threshold several times. |
| SourceType | String | METRIC | The type of the alert rule. Valid values: METRIC: the alert rule for time series metrics. EVENT: the alert rule for event-type metrics. This type was used in earlier versions and has been discarded. |
| Webhook | String | http://www.aliyun.com | The callback URL. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMetricRuleList &<Common request parameters>
```

Sample success responses `XML` format oring

```xml
<Alarms>
    <Alarm>
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>Group name</GroupName>
        <Webhook/>
        <Subject>aaabbb</Subject>
        <EffectiveInterval>00:00-23:59</EffectiveInterval>
        <RuleName>My alert rule</RuleName>
        <NoEffectiveInterval/>
        <GroupId>3596360</GroupId>
        <EvaluationCount>3</EvaluationCount>
        <MetricName>cpu_total</MetricName>
        <Threshold>92</Threshold>
        <State>OK</State>
        <Enable>true</Enable>
        <SilenceTime>86400</SilenceTime>
        <Dimensions>[{}]</Dimensions>
        <RuleId>a151cd6023eacee2f0978e03863cc1697c89508e2b61****</RuleId>
        <Namespace>acs_ecs_dashboard</Namespace>
        <ContactGroups>Test</ContactGroups>
        <Escalations>
            <Critical>
                <Statistics>Average</Statistics>
                <Threshold>92</Threshold>
                <Times>3</Times>
                <ComparisonOperator>GreaterThanOrEqualToThreshold</ComparisonOperator>
            </Critical>
            <Info/>
            <Warn/>
        </Escalations>
        <ComparisonOperator>&gt;=</ComparisonOperator>
        <Resources>[{"instanceId":"i-a2d5q7pm3f12****"}]</Resources>
    </Alarm>
    <Alarm>
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>demo</GroupName>
        <Webhook/>
        <Subject>${serviceType}-${metricName}-${levelDescription}Notification(${dimensions})</Subject>
        <EffectiveInterval>00:00-23:59</EffectiveInterval>
        <RuleName>xxxxxxxxxxxxxxx</RuleName>
        <NoEffectiveInterval/>
        <GroupId>12345</GroupId>
        <EvaluationCount>3</EvaluationCount>
        <MetricName>cpu_total</MetricName>
        <Threshold>90</Threshold>
        <State>OK</State>
        <Enable>true</Enable>
        <SilenceTime>86400</SilenceTime>
        <Dimensions>[{}]</Dimensions>
        <RuleId>alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****</RuleId>
        <Namespace>acs_ecs_dashboard</Namespace>
        <ContactGroups>rongfei</ContactGroups>
        <Escalations>
            <Critical>
                <Statistics>Average</Statistics>
                <Threshold>6666</Threshold>
                <Times>3</Times>
                <ComparisonOperator>GreaterThanOrEqualToThreshold</ComparisonOperator>
            </Critical>
            <Info/>
            <Warn/>
        </Escalations>
        <ComparisonOperator>&gt;=</ComparisonOperator>
        <Resources>[{"instanceId":"host-fTcUci7****"}</Resources>
    </Alarm>
</Alarms> <RequestId>0F05309F-8863-4B2A-8F52-C6AA00E701B4</RequestId> <Success>true</Success> <Code>200</Code> <Total>102</Total>
```

`JSON` format oring `{`

```json
 "RequestId":"0F05309F-8863-4B2A-8F52-C6AA00E701B4",
 "Alarms":{
  "Alarm":[
```

`{`

```json
    "Period":60,
    "Statistics":"Average",
    "GroupName":"Group name",
    "Webhook":"",
    "Subject":"aaabbb",
    "EffectiveInterval":"00:00-23:59",
    "RuleName":"My alert rule",
    "NoEffectiveInterval":"",
    "GroupId":"3596360",
    "EvaluationCount":3,
    "MetricName":"cpu_total",
    "State":"OK",
    "Threshold":"92",
    "Enable":true,
    "SilenceTime":86400,
    "Dimensions":"[{}]",
    "RuleId":"a151cd6023eacee2f0978e03863cc1697c89508e2b61****",
    "Namespace":"acs_ecs_dashboard",
    "ContactGroups":"Test",
    "ComparisonOperator":">=",
    "Escalations":{
     "Critical":{
      "Statistics":"Average",
      "Threshold":"92",
      "Times":3,
      "ComparisonOperator":"GreaterThanOrEqualToThreshold"
```

`},`

```json
     "Info":{},
     "Warn":{}
```

`},`

```json
    "Resources":"[{\"instanceId\":\"i-a2d5q7pm3f12****\"}]"
```

`},` `{`

```json
    "Period":60,
    "Statistics":"Average",
    "GroupName":"demo",
    "Webhook":"",
    "Subject":"${serviceType}-${metricName}-${levelDescription}Notification(${dimensions})",
    "EffectiveInterval":"00:00-23:59",
    "RuleName":"xxxxxxxxxxxxxxx",
    "NoEffectiveInterval":"",
    "GroupId":"12345",
    "EvaluationCount":3,
    "MetricName":"cpu_total",
    "State":"OK",
    "Threshold":"90",
    "Enable":true,
    "SilenceTime":86400,
    "Dimensions":"[{}]",
    "RuleId":"alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****",
    "Namespace":"acs_ecs_dashboard",
    "ContactGroups":"rongfei",
    "ComparisonOperator":">=",
    "Escalations":{
     "Critical":{
      "Statistics":"Average",
      "Threshold":"6666",
      "Times":3,
      "ComparisonOperator":"GreaterThanOrEqualToThreshold"
```

`},`

```json
     "Info":{},
     "Warn":{}
```

`},`

```json
    "Resources":"[{\"instanceId\":\"host-fTcUci7****\"}"
```

`]` `},`

```json
 "Success":true,
 "Code":"200",
 "Total":102
```

##### 5.3.2.2 PutResourceMetricRule

You can call this operation to configure an alert rule for a performance metric of a resource. For more information about example values of the cloud service parameters, such as `Namespace` , `MetricName` , and `Dimensions` , that you must set when you configure an alert rule, see Major metrics for Apsara Stack services. oring

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PutResourceMetricRule | The operation that you want to perform. Set the value to PutResourceMetricRule. |
| ContactGroups | String | Yes | Default contact group | The alert contact group. Note Separate multiple groups with commas (,). |
| MetricName | String | Yes | cputotal _ | The name of the metric. Note For more information, see Major metrics for Apsara Stack services. |
| Namespace | String | Yes | acsecsdashboard _ _ | The namespace of the service. Note For more information, see Major metrics for Apsara Stack services. |
| Resources | String | Yes | [{"instanceId":"xxxxxxx"}] | The resource for which the alert rule is to be configured. Note For more information, see Dimensions in Major metrics for Apsara Stack services. |
| RuleId | String | Yes | a151cd6023eacee2f0978e03 863cc1697c89508**** | The ID of the alert rule. Note The ID is generated by the caller. You can specify an existing ID to modify the corresponding alert rule or specify a new ID to create an alert rule. |
| RuleName | String | Yes | My alert rule | The name of the alert rule. |
| Webhook | String | No | http://ww.aliyun.com | The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. |
| EffectiveInterval | String | No | 00:00-23:59 | The time period during which the alert rule is effective. |
| NoEffectiveInterval | String | No | 00:00-06:00 | The time period during which the alert rule is ineffective. |
| SilenceTime | Integer | No | 86400 | The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: 86400. Note Only one alert is reported during each mute period even if the metric value consecutively exceeds the alert rule threshold several times. |
| Interval | String | No | 60 | The interval at which Cloud Monitor checks whether the alert rule is triggered. The default value is the lowest frequency at which the metric is polled. Unit: seconds. Note For more information about the frequency at which monitoring data is collected, see DescribeMetricMetaList. |
| EmailSubject | String | No | An alert occurs | The subject of the alert notification email. |
| Period | String | No | 60 | The aggregation cycle of monitoring data. The value is an integer multiple of 60. Unit: seconds. The default value is the frequency at which monitoring data is collected. |
| Escalations.Critical.Statist ics | String | No | Average | The statistical method for critical-level alerts. |

oring

| Escalations.Critical.Comp arisonOperator | String | No | GreaterThanOrEqualToThres hold | The comparison operator of the threshold for critical-level alerts. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to GreaterThanThreshold : greater than LessThanOrEqualToThreshold : less than or equal to LessThanThreshold : less than NotEqualToThreshold : not equal to GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in the last monitoring cycle LessThanLastPeriod : less than the metric value in the last monitoring cycle |
|---|---|---|---|---|
| Escalations.Critical.Thres hold | String | No | 90 | The threshold for triggering critical-level alerts. |
| Escalations.Critical.Times | Integer | No | 3 | The consecutive number of times for which the metric value exceeds the threshold for critical-level alerts before a critical- level alert is triggered. |
| Escalations.Warn.Statistic s | String | No | Average | The statistical method for warn-level alerts. |
| Escalations.Warn.Compari sonOperator | String | No | GreaterThanOrEqualToThres hold | The comparison operator of the threshold for warn-level alerts. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to GreaterThanThreshold : greater than LessThanOrEqualToThreshold : less than or equal to LessThanThreshold : less than NotEqualToThreshold : not equal to GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in the last monitoring cycle LessThanLastPeriod : less than the metric value in the last monitoring cycle |
| Escalations.Warn.Thresho ld | String | No | 90 | The threshold for triggering warn-level alerts. |
| Escalations.Warn.Times | Integer | No | 3 | The consecutive number of times for which the metric value exceeds the threshold for warn-level alerts before a warn-level alert is triggered. |
| Escalations.Info.Statistics | String | No | Average | The statistical method for info-level alerts. |

oring

| Escalations.Info.Comparis onOperator | String | No | GreaterThanOrEqualToThres hold | The comparison operator of the threshold for Info alerts. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to GreaterThanThreshold : greater than LessThanOrEqualToThreshold : less than or equal to LessThanThreshold : less than NotEqualToThreshold : not equal to GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in the last monitoring cycle LessThanLastPeriod : less than the metric value in the last monitoring cycle |
|---|---|---|---|---|
| Escalations.Info.Threshol d | String | No | 90 | The threshold for info-level alerts. |
| Escalations.Info.Times | Integer | No | 3 | The consecutive number of times for which the metric value exceeds the threshold for info-level alerts before an info-level alert is triggered. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| RequestId | String | 65D50468-ECEF-48F1-A6E1- D952E89D9436 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=PutResourceMetricRule &ContactGroups=Default alert group &MetricName=cpu_total &Namespace=acs_ecs_dashboard &Resources=[{"instanceId":"xxxxxxx"}] &RuleId=a151cd6023eacee2f0978e03863cc1697c89508**** &RuleName=My alert rule &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <Code>200</Code> <Message>success</Message> <RequestId>65D50468-ECEF-48F1-A6E1-D952E89D9436</RequestId> <Success>true</Success> |   |

| JSON | format |
|---|---|
| { "Message":"success", "RequestId":"65D50468-ECEF-48F1-A6E1-D952E89D9436", "Success":true, "Code":"200" } |   |

##### 5.3.2.3 DescribeMetricRuleCount

Queries the number of alert rules in each state. oring

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | No | DescribeMetricRuleCount | The operation that you want to perform. Set the value to DescribeMetricRuleCount. |
| MetricName | String | No | cputotal _ | The name of the metric . |
| Namespace | String | No | acsecsdashboard _ _ | The namespace of the service. You can call the DescribeMetricMetaList operation to query namespaces. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call is successful. |
| Message | String | The Request is not authorization. | The returned message. |
| MetricRuleCount | N/A | N/A | The number of alert rules in each state. |
| Alarm | Integer | 5 | The number of alert rules based on which alerts were triggered and not cleared. |
| Disable | Integer | 0 | The number of disabled alert rules. |
| Nodata | Integer | 0 | The number of alert rules for which status data is unavailable. |
| Ok | Integer | 40 | The number of alert rules that do not have active alerts triggered. |
| Total | Integer | 45 | The total number of alert rules. |
| RequestId | String | FF38D33A-67C1-40EB-AB65- FAEE51EDB644 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleCount &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DescribeMetricRuleCountResponse> <Success>true</Success> <Code>200</Code> <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId> <MetricRuleCount> <Ok>40</Ok> <Disable>0</Disable> <Total>45</Total> <Nodata>0</Nodata> <Alarm>5</Alarm> </MetricRuleCount> </DescribeMetricRuleCountResponse> |   |

`JSON` format oring `{`

```json
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":"200",
 "MetricRuleCount":{
  "Ok":40,
  "Disable":0,
  "Nodata":0,
  "Total":45,
  "Alarm":5
```

##### 5.3.2.4 DeleteMetricRules

You can call this operation to delete one or more alert rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Id.N | RepeatList | Yes | ab05733c97b7ce239fb1b533 93dc1697c7e12**** | The ID of the alert rule. |
| Action | String | No | DeleteMetricRules | The operation that you want to perform. Set the value to DeleteMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| RequestId | String | E5599964-8D0D-40DC-8E90- 27A619384B81 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteMetricRules &Id.1=ab05733c97b7ce239fb1b53393dc1697c7e12**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DeleteMetricRulesResponse> <Code>200</Code> <Message>success</Message> <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId> <Success>true</Success> </DeleteMetricRulesResponse> |   |

| JSON | format |
|---|---|
| { "Message":"success", "RequestId":"E5599964-8D0D-40DC-8E90-27A619384B81", "Success":true, "Code":"200" } |   |

##### 5.3.2.5 EnableMetricRules

Enables one or more alert rules.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

oring

| RuleId.N | RepeatList | Yes | ab05733c97b7ce239fb1b533 93dc1697c123**** | The ID of the alert rule. |
|---|---|---|---|---|
| Action | String | No | EnableMetricRules | The operation that you want to perform. Set the value to EnableMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| RequestId | String | FF38D33A-67C1-40EB-AB65- FAEE51EDB644 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c123**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <EnableMetricRulesResponse> <Code>200</Code> <Message>success</Message> <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId> <Success>true</Success> </EnableMetricRulesResponse> |   |

| JSON | format |
|---|---|
| { "Message":"success", "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644", "Success":true, "Code":200 } |   |

**Error codes**

For a list of error codes, visit the API Error Center.

##### 5.3.2.6 DisableMetricRules

You can call this operation to disable one or more alert rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableMetricRules | The operation that you want to perform. Set the value to DisableMetricRules. |
| RuleId.N | RepeatList | Yes | ab05733c97b7ce239fb1b533 93dc1697c7e012**** | The ID of the alert rule. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| RequestId | String | FF38D33A-67C1-40EB-AB65- FAEE51EDB644 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the call was successful. |

oring

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DisableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c7e012**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <DisableMetricRulesResponse> <Code>200</Code> <Message>success</Message> <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId> <Success>true</Success> </DisableMetricRulesResponse> |   |

| JSON | format |
|---|---|
| { "Message":"success", "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644", "Success":true, "Code":"200" } |   |

##### 5.3.2.7 DescribeAlertingMetricRuleResources

You can call this operation to query the resources that have active alerts triggered based on an alert rule.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlertingMetricRuleR esources | The operation that you want to perform. Set the value to DescribeAlertingMetricRuleResources. |
| GroupId | String | No | 123456 | The ID of the application group. |
| Page | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |
| RuleId | String | No | alerRuleId**** | The ID of the alert rule. Note You must specify at least one of the GroupId and RuleId parameters. If you specify both parameters, only entries that meet both conditions are returned. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B868619-77B4-4623-AD64- 6181EA7CF8FA | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Total | Integer | 1 | The total number of entries returned. |
| Resources | Array | None | The list of resources to which the alert rule applies. |
| Resource | None | None | The information of a resource to which the alert rule applies. |
| Enable | String | true | Indicates whether the alert rule is enabled for the resource. |

oring

| GroupId | String | 123456 | The ID of the application group. Note If the alert rule is associated with an application group, the ID of the application group is returned in this parameter. |
|---|---|---|---|
| LastAlertTime | String | 1554718182000 | The last time when an alert was triggered for the resource based on the alert rule. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| LastModifyTime | String | 1554723762000 | The time when the resource was last modified. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| MetricValues | String | {"timestamp":1554723720000,"V alue":631} | The metric value that triggered the alert based on the alert rule. The value is a JSON string. |
| Resource | String | userId=177541323192****,taskId =3****,instanceId=i- bp1a0v6yzqrms01k**** | The resource for which an alert was triggered based on the alert rule. |
| RetryTimes | String | 3 | The consecutive number of times for which the metric value was measured before an alert was triggered. |
| RuleId | String | alerRuleId**** | The ID of the alert rule. |
| RuleName | String | cpuAlert | The name of the alert rule. |
| StartTime | String | 1545901080000 | The time when the resource was associated with the alert rule. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| Threshold | String | 400 | The alert threshold. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeAlertingMetricRuleResources &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <Total>1</Total> <Resources> <Resource> <Enable>true</Enable> <Resource>userId=12****,instanceId=i-bp1a012****</Resource> <RuleId>alerRuleId****</RuleId> <RetryTimes>3</RetryTimes> <LastAlertTime>1554718182000</LastAlertTime> <MetricValues>{"timestamp":1554723720000,"Value":631}</MetricValues> <LastModifyTime>1554723762000</LastModifyTime> <StartTime>1545901080000</StartTime> <RuleName>cpuAlert</RuleName> <Threshold>400</Threshold> <GroupId>123456</GroupId> </Resource> </Resources> <Success>true</Success> |   |

`JSON` format oring `{`

```json
 "Success":true,
 "Total":1,
 "Resources":{
  "Resource":[
```

`{`

```json
    "LastAlertTime":1554718182000,
    "Resource":"userId=12****,instanceId=i-bp1a012****",
    "Threshold":"400",
    "Enable":true,
    "LastModifyTime":1554723762000,
    "RuleId":"alerRuleId****",
    "MetricValues":"{\"timestamp\":1554723720000,\"Value\":631}",
    "RetryTimes":3,
    "StartTime":1545901080000,
    "RuleName":"cpuAlert",
    "GroupId":"123456"
```

`]`

##### 5.3.2.8 DeleteMetricRuleResources

You can call this operation to delete resources associated with an alert rule.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMetricRuleResources | The operation that you want to perform. Set the value to DeleteMetricRuleResources. |
| Resources | String | Yes | [{"instanceId":"*****ixxxId1" }] | The resources to be disassociated from the alert rule. The value is a JSON array. |
| RuleId | String | Yes | rr-bp18017n6iolv**** | The ID of the alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8A35882-90C6-4F03-BBEB- 153C180398EA | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteMetricRuleResources &Resources=[{"instanceId":"*****ixxxId1"}] &RuleId=rr-bp18017n6iolv**** &<Common request parameters>
```

Sample success responses

| XML | format |
|---|---|
| <RequestId>0671A721-0D7A-4F11-BB77-2416325D65AB</RequestId> <Success>true</Success> <Message>success</Message> <Code>200</Code> |   |

`JSON` format oring `{`

```json
    "Message":"success",
    "RequestId":"0671A721-0D7A-4F11-BB77-2416325D65AB",
    "Success":true,
    "Code":"200"
```
