---
title: "Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Management Console Developer Guide"
product_version: "V3.16.2"
doc_version: "20251106"
pdf_pages: 607
source_pdf: "469e7d0de43f2a54_Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Management Console Developer Guide 20251106.pd"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.16.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E7%BB%9F%E4%B8%80%E4%BA%91%E7%AE%A1/Alibaba%20Cloud%20Apsara%20Stack%20v3.16.2%20Apsara%20Uni-manager%20Management%20Console%20Developer%20Guide%2020251106.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.16.2 Apsara Uni-manager Management Console Developer Guide

## Table of Contents

- 1 Preparations
  - 1.1 Obtain API information
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
        - 2.1.5.2.1 Install the core package of SDK for Go
        - 2.1.5.2.2 Configure authentication credentials
        - 2.1.5.2.3 Initiate a request
        - 2.1.5.2.4 Handle errors
        - 2.1.5.2.5 Use CommonRequest to call API operations
  - 2.2 Use ASAPI to call API operations
    - 2.2.1 ASAPI overview
    - 2.2.2 Obtain the endpoint of ASAPI
    - 2.2.3 Obtain ASAPI SDKs
    - 2.2.4 SDK for Java
    - 2.2.5 SDK for Python
    - 2.2.6 Use SDK for Node.js to call API operations
- 3 HTTP requests
  - 3.1 Overview
  - 3.2 Request syntax
  - 3.3 Signature method
  - 3.4 Responses
- 4 Apsara Uni-manager Management Console API Reference
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
      - 4.3.2.10 BillQuery
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
      - 4.3.5.8 ApsaraDB for Redis
      - 4.3.5.9 AnalyticDB for PostgreSQL
      - 4.3.5.10 ApsaraDB for MongoDB
      - 4.3.5.11 Message Queue for Apache RocketMQ
      - 4.3.5.12 ApsaraDB RDS for PostgreSQL
      - 4.3.5.13 ApsaraDB RDS for SQL Server
      - 4.3.5.14 Log Service
      - 4.3.5.15 EBS
      - 4.3.5.16 Snapshots
      - 4.3.5.17 Auto Scaling
      - 4.3.5.18 API Gateway
- 5 CloudMonitor API Reference
  - 5.1 Common parameters
  - 5.2 Metrics for Apsara Stack services
  - 5.3 API Reference
    - 5.3.1 Cloud Products
      - 5.3.1.1 DescribeProjectMeta
      - 5.3.1.2 DescribeMetricLast
      - 5.3.1.3 DescribeMetricList
      - 5.3.1.4 DescribeMetricMetaList
    - 5.3.2 Threshold-triggered alert rules
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

### 1.1 Obtain API information

To call API operations by using an SDK, you must first obtain information about the service name, API operation name, and API version.

**Background information**

The information on the API Directory page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the API Directory page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, click **Products** and choose **Others** > **API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. On the **API Directory** page, select the required cloud service from the Product Name drop-
down list, enter a keyword of an operation name in the search box, and then click Search.
5. In the search result, you can view the **cloud service name**, **API operation name**, and
**API version**.

### 1.2 Obtain AccessKey credentials

AccessKey credentials are assigned by Resource Access Management (RAM) .

**Background information**

An AccessKey ID and an AccessKey secret are used to implement symmetric encryption and verify the identity of a request sender. The AccessKey ID is used to identify a user. The AccessKey secret is a string that is used to encrypt a signature.

**Obtain an AccessKey pair**

The Apsara Uni-manager Management Console provides two types of AccessKey pairs: those for personal accounts and those for organization accounts. We recommend that you use an AccessKey pair for personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services.

**Note**

Only operations administrators and level-1 organization administrators can obtain AccessKey pairs for organization accounts.

**Obtain an AccessKey pair for personal accounts**

To use an AccessKey pair for personal accounts, you must configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

| Parameter | Description |
|---|---|

rations

| x-acs-regionid | The ID of the region to which the instance that you want to access belongs. Example: cn- qingdao-****-****. |
|---|---|
| x-acs-organizationid | The ID of the organization to which the instance that you want to access belongs. For information about how to obtain the ID, see Obtain common header parameters. |
| x-acs-resourcegroupid | The ID of the resource set to which the instance that you want to access belongs. For information about how to obtain the ID, see Obtain common header parameters. |
| x-acs-instanceid | The ID of the instance that you want to access. For example, you can view the ID of an Elastic Compute Service (ECS) instance in the ECS instance list. |

1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain an AccessKey pair for organizations**

**Warning**

An AccessKey pair for personal accounts is managed and controlled by the permission system of the Apsara Uni-manager Management Console. An AccessKey pair for organization accounts provides more permissions than an AccessKey pair for personal accounts. If you need to obtain an AccessKey pair for organizations, make sure that your operation is allowed by your administrator. This ensures security.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
rations
4. In the organization navigation tree, click the name of the level-1 organization for which you
want to obtain AccessKey pairs.
5. Click **Management AccessKey** on the right side of the page.
6. In the Management AccessKey dialog box, view the AccessKey pair of the organization.

### 1.3 Obtain the values of common request headers

**request headers**

In Apsara Stack, you must specify multiple common request headers to call API operations. Then, common response parameters are returned in the results.

**Common request parameters**

You must specify the values of the common request parameters in the code to call API operations in Apsara Stack. For example, you need to replace the `<Your resource group ID>` with the actual resource

```
set ID in request.putHeadParameter("x-acs-resourcegroupid", "<Your resource group ID>")
```

when you use the SDK for Java to call API operations.

| Name | Description |
|---|---|
| x-acs-regionid | The region ID of the instance resource on which you want to perform operations. For more information, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization to which the instance resource belongs. For more information, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set to which the instance resource belongs. For more information, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance to which the resource belongs. For more information, see Obtain an instance ID. |

rations

**Note**

| <x-acs- |   |
|---|---|

When you call API operations in Apsara Stack, you must use `<x-acs-` `organizationid>` to add the organization ID to the request header. Otherwise, the call fails and an error message indicating that you do not have permissions to initiate calls is returned. When you call API operations in Apsara Stack, we recommend that you use `<x-` `acs-resourcegroupid>` to add the resource set ID to the request header. After you specify the organization ID and the resource set ID, you can narrow down the query

| <x-acs- |   |
|---|---|

scope when you query instance resources. If you do not use `<x-acs-` `resourcegroupid>` to specify the resource set ID, the default resource set of the organization to which the user belongs is obtained.

**Obtain a region ID**

You can view the region IDs of resources in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization that you want to view.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call a specific API operation to obtain the organization ID. You can obtain the organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Others** > **API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. On the **API Directory** page, enter `GetOrgnizationList` in the **Search by operation**
**name** field and click **Search**.
5. Click **Online Debug** in the Actions column. For more information about the
`GetOrgnizationList` operation, see the GetOrgnizationList topic in the Apsara Uni-manag er Management Console Developer Guide.
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
rations
2. In the top navigation bar, choose **Products** > **Elastic Computing** > **Elastic Compute**
**Service**.
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
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. In the **Base/Platforms** section, click **Apsara Infrastructure Management**
**Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` . In the report list
that appears, click the name of the report.
4. On the **Registration Vars of Services** page, click the
icon next to **Service**. Specify the Contains operator, enter `ECS` in the filter text filed, and then click Apply Filter.
5. Find the `ecs-yaochi` service, right-click the value in the **Service Registration** column,
and then select **Show More** from the shortcut menu. On the **Details** page, view the **internal.openapi.endpoint** value, which is the

```
 endpoint .
```

DKs

#### 2.1.2 Obtain an SDK

To call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK of your cloud service. This topic describes how to obtain an SDK of your cloud service. An SDK includes code and examples. You can create cloud applications by using an SDK for the programming language that you require. SDKs for Java, Python, and Go are perfectly supported. You can select the SDKs from Alibaba Cloud SDKs based on your business requirements.

**Note**

We recommend that you use an SDK for Java, Python, or Go. If you use SDKs for other programming languages, the SDKs may be incompatible with your system. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack.

#### 2.1.3 Call examples for SDK for Java

##### 2.1.3.1 Getting started

This topic describes how to obtain and use an SDK for Java.

**Prerequisites**

An authorized Apsara Stack tenant account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain AccessKey credentials. The endpoint of the cloud service is obtained. For more information, see Obtain service endpoints. Java Development Kit (JDK) 1.8 or later is installed. SDKs for Java provided by Apsara Stack require JDK 1.8 or later.

**Install the SDK for Java**

To use Apache Maven for Java project management, include the JAR file in `pom.xml` . To use an SDK of a service, you must install both the SDK core library and the SDK. We recommend that you use the latest SDK core library.

**Use the SDK for Java**

To use an Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.
DKs

**Note**

In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in your code. Parameters: <yourRegionID>: Replace it with the region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <Product>: Replace it with the name of the service. <Endpoint>: Replace it with the endpoint of the service. <readTimeout>: Replace it with a read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Replace it with a connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Replace it with the maximum number of requests that are supported by each host. <maxRequests>: Replace it with the maximum number of requests. <http://192.168.XX.XX:33XX>: Replace it with the IP address and port of the proxy.

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
        clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the rea
d timeout period. Unit: milliseconds.
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Spe
cify the connection timeout period. Unit: milliseconds.
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify
the maximum number of requests per host.
        clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum n
umber of requests.
        clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Specify the req
uest protocol. Default value: HTTP.
        /* Optional. Specify the IP address and port of the proxy.
clientConfigsetHttpProxy("<http://192168XXXX:33XX>");
```

DKs

```
        clientConfig.setHttpProxy(<http://192.168.XX.XX:33XX>);
```

`Or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        DescribeInstancesRequest request = new DescribeInstancesRequest();
        // Set service-related parameters.
        request.setPageSize(10);
        request.setPageNumber(1);
        // Specify the organization ID and resource set ID to query specified
resources.
        request.putHeaderParameter("x-acs-organizationid", "1");
        request.putHeaderParameter("x-acs-resourcegroupid", "11");
        // Send the request and handle the response or exception.
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

##### 2.1.3.2 Use SDK

###### 2.1.3.2.1 Install an SDK for Java

This topic describes how to install and use the SDK for Java of your cloud service. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK package. For more information, visit Alibaba Cloud SDKs. To use the development tool kit for a cloud service, you must install the core library of Apsara Stack SDK for Java and the SDK for Java of your cloud service. We recommend that you use the latest version of the core library of Apsara Stack SDK for Java. For example, to use ECS SDK for Java, you must install the core library of Apsara Stack SDK for Java and ECS SDK for Java, and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDKs. DKs

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

**Note**

Do not disclose code containing your AccessKey pair (for example, do not commit AccessKey pair-related code to public GitHub projects). Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace it with the region ID.
    "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
```

**Note**

Replace the parameters in the preceding sample code with your actual information. Delete the angle brackets (<>) in your code.

###### 2.1.3.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. DKs

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

###### 2.1.3.2.4 Initiate a request

This topic describes how to use the SDK for Java of a cloud service to initiate a request.

**Procedure**

1. Create an AcsClient instance.
DKs

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request , where **${apiName}** indicates the name of an API operation, such as DescribeInstances. When multiple service SDKs are used, different requests may have the same name. Differentiate the requests by using package names.

```
DescribeInstancesRequest request = new DescribeInstancesRequest(); // Specify service-related parameters. request.setPageSize(10); request.setPageNumber(1); // Specify the organization ID and resource set ID to query specified resources. request.putHeaderParameter("x-acs-organizationid", "1"); request.putHeaderParameter("x-acs-resourcegroupid", "");
```

3. Initiate the request and handle the response.

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

`}` In normal cases, all returned fields are deserialized into the response. You can directly use `response.getXXX()` to obtain the response fields.

```
Boolean status = response.getStatus();
```

If an exception occurs or you need the original HTTP response, use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

###### 2.1.3.2.5 Handle errors

If the server or SDK encounters an error when you use the SDK for Java, the SDK returns an error response. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by the SDK for Java. You only need to handle server errors based on error messages generated on the server side. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

DKs If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code:

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
    // If you are unable to fix the error, submit a ticket and provide RequestId to Ali
baba Cloud technical support.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your error handling logic here.
    // For example, display the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}`

###### 2.1.3.2.6 Use CommonRequest to call API operations

#### operations

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight: You need to only download the core package. You do not need to download and install SDKs of services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters from the API document of a service. product: the service name of the operation. domain: the endpoint of the service. version: the version of the API. The version is in the YYYY-MM-DD format. You can obtain the API version from the common parameters chapter in the API document. Operation information: the name of the API operation that you want to call. DKs For Remote Procedure Call (RPC) APIs, which are used by services such as Elastic Compute Service (ECS) and Relational Database Service RDS): You must obtain the value of the **Action** parameter and specify an API operation in `request.setSysAction("<Action>")` format. For example, to call the RunInstances operation of ECS, you must specify the operation in

```
 request.setSysAction("RunInstances") .
```

For Representational State Transfer (RESTful) APIs, which are used by services such as Container Service (CS): You must obtain the value of the **PathPattern** parameter and specify a RESTful path in

```
 request.setSysUriPattern("<PathPattern>")  format.
```

For example, if the **PathPattern** value in an API operation that is used to query all

| cluster instances in CS is | /api/v1/clusters | , you |
|---|---|---|
| request.setSysUriPattern("/api/v1/clusters") |   |   |

**Example: Call an RPC API operation**

The following code shows an example on how to use CommonRequest to call the DescribeInstanceStatus operation of ECS.

|   | <yourRegionID> |   |
|---|---|---|
| <yourSecurityToken> |   |   |
| <yourInstanceID> |   |   |

|   | <yourAccessKeyID> |   |   |
|---|---|---|---|
|   |   | , |   |

`<yourInstanceID>` , and `<http://192.168.XX.XX:33XX>` with the actual values. Delete the angle brackets (<>) in your code.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with your region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey
secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTP);// Determine whether to
configure an HTTP proxy based on your business requirements.
        // Configure the HTTP proxy in the following method:
        // clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Replace the
parameter with the actual proxy IP address and port.
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        CommonRequest request = new CommonRequest();
        // Replace the parameter with the actual service endpoint.
        request.setSysMethod(MethodType.POST);
```

`t` `tS` `D`

```
i("
```

`li` `")` DKs

```java
        request.setSysDomain("ecs.aliyuncs.com");
        request.setSysProduct("Ecs");
        request.setSysLocationProduct("ecs");
        request.setSysVersion("2014-05-26");
        request.setSysAction("DescribeInstanceStatus");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// O
ptional. Replace the parameter with the actual resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Req
uired. Replace the parameter with the actual organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional.
Replace the parameter with the actual region ID.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");//
Optional. Replace the parameter with the actual instance ID. This parameter is required when you want to delete, modify, or query an instance.
        // When you use an STS AccessKey 3-tuple to call an API operation, you must add
the SecurityToken field in the request parameters.
        // Format:
        //request.putQueryParameter("SecurityToken", "<yourSecurityToken>"); Replace th
e parameter with the actual security token.
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

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with your region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey
secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
clientConfigsetProtocolType(ProtocolTypeHTTP);//Determinewhetherto
```

DKs

```java
        clientConfig.setProtocolType(ProtocolType.HTTP);// Determine whether to
configure an HTTP proxy based on your business requirements.
        // Configure the HTTP proxy in the following method:
        // clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Replace the
parameter with the actual proxy IP address and port.
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
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// O
ptional. Replace the parameter with the actual resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Req
uired. Replace the parameter with the actual organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Required.
Replace the parameter with the actual region ID.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");//
Optional. Replace the parameter with the actual instance ID. This parameter is required when you want to delete, modify, or query an instance.
        // When you use an STS AccessKey 3-tuple to call an API operation, you must add
the SecurityToken field in the request parameters.
        // Format:
        //request.putQueryParameter("SecurityToken", "<yourSecurityToken>"); Replace th
e parameter with the actual token.
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

You must pass parameters in two methods depending on the request method and ContentType value. If the request method is `GET` or `DELETE` , or the ContentType value is `application/x-` `www-form-urlencoded` , use the following method to pass parameters: DKs Place the request parameters in the Query parameter, for example,

```
 request.putQueryParameter("page_number", "1"); .
```

If the request method is `POST` or `PUT` and the ContentType value is `application/json` , use the following method to pass parameters: Place the request parameters in the body, for example:

```
String requestBody = "{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \ "<yourSecurityToken>\"}"; request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
```

The following code shows an example on how to use CommonRequest to call the DescribeClusterV1 operation of CS.

|   | <yourRegionID> |   |   |
|---|---|---|---|
| <yourResourceGroupID> |   |   |   |
|   |   | , |   |

|   | <yourAccessKeyID> |   |
|---|---|---|
|   |   | , |

`<http://192.168.XX.XX:33XX>` , and `<yourSecurityToken>` with the actual values. Delete the angle brackets (<>) in your code.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    //DemoAPI: DescribeClusterV1
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace the parameter with your region ID.
            "<yourAccessKeyID>",      // Replace the parameter with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey
secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTP);// Determine whether to
configure an HTTP proxy based on your business requirements.
        // Configure the HTTP proxy in the following method:
        // clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Replace the
parameter with the actual proxy IP address and port.
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
requestputHeadParameter("x-acs-resourcegroupid" "<yourResourceGroupID>");//O
```

DKs

```java
        request.putHeadParameter(xacsresourcegroupid, <yourResourceGroupID>);// O
ptional. Replace the parameter with the actual resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Req
uired. Replace the parameter with the actual organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional.
Replace the parameter with the actual region ID. If you use Apsara Stack Enterprise V3. 15.0 or earlier versions, this parameter is required.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");//
Optional. Replace the parameter with the actual instance ID. This parameter is required when you want to delete, modify, or query an instance.
        // Business parameters. If the request method is GET or DELETE, or the
ContentType value is application/x-www-form-urlencoded, use the following method to pas s parameters:
        request.putQueryParameter("page_number", "1");
        request.putQueryParameter("page_size", "5");
        // When you use an STS AccessKey 3-tuple to call an API operation, you must add
the SecurityToken field in the request parameters.
        // Format:
        // String requestBody = "{\"SecurityToken\": \"<yourSecurityToken>\"}"; Replace
the parameter with the actual token.
        If the request method is POST or PUT and the ContentType value is
application/json, use the following method to pass parameters:
        //String requestBody = "
{\"page_number\":\"1\",\"page_size\":\"5\",\"SecurityToken\", \"<your- SecurityToken>\"}";
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

`}` `}` `}`

#### 2.1.4 Call examples for SDK for Python

##### 2.1.4.1 Getting started

This topic describes how to obtain and use an SDK for Python.

**Prerequisites**

An authorized Apsara Stack tenant account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain AccessKey credentials. The endpoint of the cloud service is obtained. For more information, see Obtain service DKs endpoints.

**Install the SDK for Python**

1. Install the SDK core library.
If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK:

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
1. Create a client instance. When you create a client instance, you must obtain a region ID,
AccessKey ID, and AccessKey secret.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

**Note**

In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in your code. Parameters: <yourRegionID>: Replace it with the region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <ecs.aliyuns.com>: Replace it with the endpoint of the actual service. DKs

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
region_id = '<yourRegionID>' # Specify the region ID. access_key = '<yourAccessKeyID>' # Specify your AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Specify your AccessKey secret.
# product config
product_name = 'ECS' # Specify the name of the required service. endpoint = '<ecs.aliyuns.com>' # The endpoint of the required service. Replace ecs.al iyuns.com with the endpoint of the actual service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print response # The print statement in Python 2.x. If you use Python 3.x, use print( response).
```

##### 2.1.4.2 Use SDK

###### 2.1.4.2.1 Install the SDK for Python

This topic describes how to install and use the SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

**Note**

To use the SDK for Python of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python. For example, if you want to use ECS SDK for Python, you must install the SDK core library for Python and ECS SDK for Python. If you use Python 2.x, run the following command to install the core library:

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

DKs

###### 2.1.4.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for authentication. The SDKs for Python support AccessKey pair-based authentication. For more information about how to obtain an AccessKey pair, see Obtain AccessKey credentials. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

**Important**

Do not disclose any code containing your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
clt = AcsClient(access_key, access_secret, region_id)
```

###### 2.1.4.2.3 Set HTTPS requests

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

The following sample code provides an example on how to set a global default protocol: DKs

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

#### operations

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight design: You need to only download the core package. You do not need to download and install SDKs of services. Ease of use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration: CommonRequest enables fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters from the API document of a service. product: the name of the service whose API operation you want to call. domain: the endpoint of the service. version: the version of the API in the YYYY-MM-DD format. You can obtain the API version from the common parameters in the API documents. action_name: the name of the API operation that you want to call. For Remote Procedure Call (RPC) APIs, which are used by services such as Elastic Compute Service (ECS) and Relational Database Service (RDS): You must obtain the value of the **Action** parameter and use `request.set_action_name('Action')` to specify the API operation. For example, to use CommonRequest to call the RunInstances operation of ECS, specify the operation in `request.set_action_name('RunInstances')` . For Representational State Transfer (RESTful) APIs, which are used by services such as Container Service (CS): You must obtain the value of the **PathPattern** parameter and use `request.set_uri_pattern('Pattern')` to specify the RESTful path. For example, if the **PathPattern** value in an API operation that is used to query all

| cluster instances in CS is | /api/v1/clusters | , yo |
|---|---|---|
| request.set uri pattern ('/api/v1/clusters') _ _ |   |   |

DKs

**Example: Call an RPC API operation**

The following code provides an example on how to use CommonRequest to call the DescribeInstanceStatus operation of ECS.

|   | <yourRegionID> |   |
|---|---|---|
| <yourSecurityToken> |   |   |
| <yourInstanceID> |   |   |

| <yourAccessKeyID> |   |
|---|---|

`<yourInstanceID>` , and `<ecs.aliyuncs.com>` with the actual values. Delete the angle brackets (<>) in your code. DKs

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Ecs') request.set_action_name('DescribeInstanceStatus') request.set_version('2014-05-26') request.set_domain('<ecs.aliyuncs.com>') # Replace <ecs.aliyuncs.com> with the endpoint of the actual service.
# or:
# request = = CommonRequest(product='Ecs',
action_name='DescribeInstanceStatus',version='2014-05-26',domain='ecs.aliyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# You can specify HTTPS as the protocol in the following manner:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
# If you use the access credentials assigned by STS to call an API operation, you must
specify the SecurityToken parameter in the request.
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
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack E
nterprise V3.15.0 or earlier. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify,
delete, or query an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

**Example: Call a RESTful API operation**

You must pass parameters by using one of the following two methods, depending on the request method and ContentType value. If the request method is `GET` or `DELETE` , or the ContentType value is `application/x-` `www-form-urlencoded` , use the following method to pass parameters: DKs Place the request parameters in the Query parameter, for example,

```
 request.add_query_param("page_number", "1") .
```

If the request method is `POST` or `PUT` and the ContentType value is `application/json` , use the following method to pass parameters: Place the request parameters in the body, for example:

```
body = '{"page_number":"1",page_size"5":"SecurityToken","":"<yourSecurityToken>"}' request.set_content(body.encode('utf-8'))
```

The following code provides an example on how to use CommonRequest to call the DescribeClusterV1 operation of CS.

|   | <yourRegionID> |   |
|---|---|---|
| <yourSecurityToken> |   |   |
| <yourInstanceID> |   |   |

| <yourAccessKeyID> |   |
|---|---|

`<yourInstanceID>` , and `<cs.aliyuncs.com>` with the actual values. Delete the angle brackets (<>) in your code.

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
######
# API:CS-DescribeClusterV1
######
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CS') request.set_version('2015-12-15') request.set_uri_pattern('/api/v1/clusters') # Pattern request.set_domain('<cs.aliyuncs.com>') # Replace <cs.aliyuncs.com> with the endpoint o f the actual service.
# or:
# request = CommonRequest(product='CS', version='2015-12-15',
uri_pattern='/api/v1/clusters', domain='cs.aliyuns.com')
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
# Optional. Specify the region ID. This parameter is required if you use Apsara Stack E
nterprise V3.15.0 or earlier. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify,
delete, or query an instance.
#requestaddheader("x-acs-instanceid"
"<yourInstanceID>")
```

DKs

```python
# request.add_header(xacsinstanceid, <yourInstanceID>)
// Pass parameters. If the request method is GET or DELETE, or the ContentType value is application/x-www-form-urlencoded, use the following method to pass parameters: request.add_query_param("page_number", "1") request.add_query_param("page_size", "5")
######
# If you use the access credentials assigned by STS to call an API operation, you must
specify the SecurityToken parameter in the request.
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
DKs

**Note**

In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in your code. Parameters: <yourRegionID>: Replace it with the region ID. <yourAccessKeyID>: Replace it with your AccessKey ID. <yourAccessKeySecret>: Replace it with your AccessKey secret. <Endpoint>: Replace it with the actual endpoint.

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
```

`}`

```
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

##### 2.1.5.2 Use SDK

###### 2.1.5.2.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package: DKs

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

###### 2.1.5.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDKs for Go support AccessKey pair-based authentication. For more information, see Obtain AccessKey credentials. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

**Important**

Do not disclose any code containing your AccessKey pair. For example, do not commit AccessKey-related code to public GitHub projects. Otherwise, your account may be compromised. The following code provides an example on how to initialize an ecsClient instance.

```
// Initialize the ecsClient instance. ecsClient, err := ecs.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace it with the region ID.
        "<yourAccessKeyID>",             // Replace it with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace it with your AccessKey secret.
```

**Note**

Replace the parameters in the preceding sample code with your actual information. Delete the angle brackets (<>) in your code.

###### 2.1.5.2.3 Initiate a request

This topic uses Elastic Compute Service (ECS) SDK for Go as an example to show how to initiate a request by using the SDK for Go of a specific cloud service.
1. Import ECS SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. Create an ECS client. The client includes all API operations of ECS.

**Note**

In the following code, replace the parameters with actual values. Delete the angle brackets <> in your code.

```
ecsClient,err := <ecs>.NewClientWithAccessKey( // Replace ecs with the name of the a ctual service.
    "<yourRegionID>",  // Replace it with the region ID.
    "<yourAccessKeyID>",  // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>")  // Replace it with your AccessKey secret.
ecsClient.Domain = "ecs.aliyuns.com" // Specify the endpoint of the service.
```

3. Use `xxx.CreateXXXRequest` to create a request.
The naming convention for this method is ${service}.Create${apiName}Request , where:
**${service}** specifies the service name in lowercase. In this example, ecs is used.
DKs
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

`}`

**ClientError**

When you send a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a `ClientError` . The following sample code shows how to determine and obtain the error message in a `ClientError` returned by ECS SDK for Go:

**Important**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the n
ame of the actual service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)` DKs

```
response, err := ecsClient.DescribeInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

`}`

**ServerError**

When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following sample code shows how to determine and obtain the error message in a ServerError and Response returned by ECS SDK for Go:

**Important**

When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the n
ame of the actual service.
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

`}`

###### 2.1.5.2.5 Use CommonRequest to call API operations

#### operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations. DKs

**Call an RPC API operation**

The following code shows an example on how to use CommonRequest to call the DescribeInstanceStatus operation of ECS.

|   | <yourRegionID> |   |
|---|---|---|
| <yourSecurityToken> |   |   |
| <yourInstanceID> |   |   |

| <yourAccessKeyID> |   |
|---|---|

`<yourInstanceID>` , and `<ecs.aliyuncs.com>` with the actual values. Delete the angle brackets (<>) in your code. DKs

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
        "<yourAccessKeyID>",     // Replace the variable parameter with your AccessKey
ID.
        "<yourAccessKeySecret>") // Replace the variable parameter with your AccessKey
secret.
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ecs.aliyuncs.com>" // Replace the variable parameter with the en
dpoint of your service.
    request.Product = "Ecs"
    request.Version = "2014-05-26"
    // This is an RPC API operation. Therefore, the ApiName(Action) parameter must be c
onfigured.
    request.ApiName = "DescribeInstanceStatus"
    // Specify service-related parameters.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*`

```
     When you use STS AccessKey credentials to call an RPC API operation, you must add
the SecurityToken field to the request parameters.
     Request example:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Replace the variable parameter with your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. Specify the
source of the call.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify your regi
on ID. If you use Apsara Stack Enterprise V3.15.0 or earlier, you must configure this p arameter.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Spe
cify the resource set ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Speci
fy the organization ID.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Specify th
e instance ID. If you want to modify, delete, or query an instance, you must configure this parameter.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` DKs

**Call a RESTful API operation**

You must use one of the following methods to pass parameters based on the request method and the value of ContentType. If the request method is `GET` or `DELETE` , or ContentType is `application/x-www-form-` `urlencoded` , use the following method to pass parameters: Place the request parameters in the Query parameter, such as

```
 request.QueryParams["page_number"] = "1" .
```

If the request method is `POST` or `PUT` and ContentType is `application/json` , use the following method to pass parameters: Place the request parameters in the body. For example:

```
body := "{\"page_number\":\"1\",page_size:\"5\"}" request.SetContent([]byte(body)) request.SetContentType("application/json")
```

The following code provides an example on how to use CommonRequest to call the DescribeClusterV1 operation of CS.

|   | <yourRegionID> |   |
|---|---|---|
| <yourResourceGroupID> |   |   |
| <cs.aliyuncs.com> |   |   |

| <yourAccessKeyID> |   |
|---|---|

`<cs.aliyuncs.com>` , and `<yourSecurityToken>` with the actual values. Delete the angle brackets (<>) in your code.

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
        "<yourRegionID>",         // Replace the variable parameter with the actual
region ID.
        "<yourAccessKeyID>",      // Replace the variable parameter with your AccessKey
ID.
        "<yourAccessKeySecret>")  // Replace the variable parameter with your AccessKey
secret.
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Method = "GET"
    request.Domain = "cs.aliyuncs.com" // The endpoint of the service. Replace the samp
le value with the actual service endpoint.
    request.Product = "CS"
    request.Version = "2015-12-15"
    // This is a RESTful API. You must specify the PathPattern field.
    request.PathPattern = "/api/v1/clusters"
    // When you use an STS AccessKey pair to call the ROA operation, you must specify t
he x-acs-security-token header.
    // request.Headers["x-acs-security-token"] = "<yourSecurityToken>"
    // Required. The call source.
```

`t``H` `d` `["` `ll` `dk` `"]`

```
"AiT
```

`tD` `"` DKs

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. This parameter is required for the Enterprise Edition V3.15.0 and earl
ier versions.
    request.Headers["x-acs-regionid"] = "<yourRegionID>"
    // Optional. Replace the variable parameter with your resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>"
    // Required. Replace the variable parameter with your organization ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"
    // Optional. Specify the instance ID. If you want to modify, delete, or query an in
stance, this parameter is required.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>"
    // Business parameters. If the request method is GET or DELETE, or ContentType is a
pplication/x-www-form-urlencoded, use the following method to pass parameters:
    // request.QueryParams["page_number"] =  "1"
    // request.QueryParams["page_size"] = "5"
    If the request method is POST or PUT and ContentType is application/json, use the f
ollowing method to pass parameters:
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

### 2.2 Use ASAPI to call API operations

#### operations

#### 2.2.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). DKs The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Unimanager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Unimanager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. DKs

**Note**

If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 2.2.2 Obtain the endpoint of ASAPI

You can obtain the endpoint of ASAPI by replacing the variables. The actual values of the variables can be obtained in the Apsara Uni-manager Operations Console.

**Method 1: Use Registration Vars of Services to obtain an**

**endpoint**

**Procedure**

1. Log on to Apsara Infrastructure Management.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. In the **Base/Platforms** section, click **Apsara**
**Infrastructure Management Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` . In the report list
that appears, click the name of the report. DKs
4. On the **Registration Vars of Services** page, click the icon next to
**Service** and search
for `asapi` .
5. Find the asapi service, right-click the value in the **Service Registration** column, and then
select **Show More** from the shortcut menu. In the **Details** dialog box, obtain the **asapi.public.endpoint** value.
6. Generate an endpoint in the following format for ASAPI:

```
https://<asapi.public.endpoint>/asapi/v3
```

**Method 2: Concatenate strings to generate an endpoint**

The endpoint can be a new one or a historical one. You can use one of them based on actual situations. We recommend that you use the new endpoint. If you discover that the certificate is not updated, you can contact the administrator to update the certificate or use the historical endpoint.

**New endpoint**

Only the HTTPS protocol is supported. The new endpoint is suffixed with `internet-domain` and in the following format:

```
 https://public.asapi.${global:region}.${global:internet-domain}/asapi/v3
```

**Note**

${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained.

**Verify that the new endpoint is available**

You can use the following code to verify whether the new endpoint is available. If you cannot access the endpoint, the new endpoint is unavailable, and you need to use the historical endpoint.

```bash
 curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k
```

DKs

**Note**

${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained. Example of an available endpoint: Example of an unavailable endpoint:

**Historical endpoint**

Only the HTTP protocol is supported. The historical endpoint is suffixed with `intranet-` `domain` and in the following format:

```
 http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3
```

**Note**

${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained.

**Obtain the values of variables**

To obtain the values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranet-domain}, perform the following steps: DKs
1. Log on to the Apsara Uni-manager Operations Console.

**Note**

You can select a language from the drop-down list in the upper-right corner of the logon page. Obtain the username and password for logging on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator. When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password as prompted. To ensure security, your password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
2. In the top navigation bar, choose **Products** > **Base/Platforms** > **Apsara Infrastructure**
**Management Framework**.
3. In the left-side navigation pane, choose **Operations** > **Cluster Operations**.
DKs
4. On the **Clusters** page, enter **ascm-A** in the Cluster search box to find the cluster. Click the
cluster name.
5. On the **Cluster Details** page, click the **Cluster Configuration** tab.
6. In the file list of the **Cluster Configuration** tab, click **kv.conf**, click the file content in the
right window, and then press Ctrl+F. Search for region, internet-domain, and intranetdomain.Replace

|   | ${global:internet-domain} |
|---|---|
| ${global:intranet-domain} |   |

intranet-domain value.

**Note**

Do not include ${global:} in the endpoint of ASAPI that you use.

#### 2.2.3 Obtain ASAPI SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. You can download the general package of ASAPI SDKs by using one of the following methods: Go to the **Other Resources** section at the lower part of the Apsara Stack documentation page. Click ASAPI SDK package. After the package is downloaded, select a language and version based on your local environment. DKs

**Note**

The general package of ASAPI SDKs includes ASAPI SDKs for Java, Python, and Node.js. ASAPI SDK for Java version 1.0.6.7-RELEASE supports Apsara Stack Agility v3.6 and later, Apsara Stack Enterprise v3.14.0 and later, Apsara Stack Enterprise v3.13.0 SP002+, and Apsara Stack Enterprise v3.12.0 SP006+. ASAPI SDK for Java version 1.0.2.5-RELEASE supports Apsara Stack Enterprise v3.12.0, Apsara Stack Enterprise v3.13.0, and Apsara Stack Agility v3.5. ASAPI SDK for Python version 2.4.7.1-RELEASE supports Apsara Stack Agility v3.6 and later, Apsara Stack Enterprise v3.14.0 and later, Apsara Stack Enterprise v3.13.0 SP002+, and Apsara Stack Enterprise v3.12.0 SP006+. ASAPI SDK for Python version 2.2.1.1-RELEASE supports Apsara Stack Enterprise v3.12.0, Apsara Stack Enterprise v3.13.0, and Apsara Stack Agility v3.5. ASAPI SDK for Node.js provides full version support for each edition.

#### 2.2.4 SDK for Java

After you install Apsara Stack API (ASAPI) SDK for Java, you can write code to call Apsara Stack API operations by using ASAPI.

**Prerequisites**

You have obtained an AccessKey pair or an STS AccessKey 3-tuple. We recommend that you use an AccessKey pair or an STS AccessKey 3-tuple for personal accounts to call API operations of Apsara Uni-manager Operations Console and cloud services. For more information, see Obtain AccessKey credentials. You have obtained the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI. You have obtained the ASAPI SDK package that supports the current edition. For more information, seeObtain ASAPI SDKs. Java Development Kit (JDK) 1.8 or later is installed.

**Background information**

ASAPI SDK for Java contains Maven project dependencies and JAR packages. After you install the SDK dependencies, you can write code to call Apsara Stack API operations by using ASAPI.

**Note**

In this example, the Windows 10 64-bit OS and IntelliJ IDEA are used.

**Install dependencies**

1. Use one of the following methods to configure Maven in IntelliJ IDEA. Maven is a tool used
for project management. Use Maven that is integrated in IntelliJ IDEA. Download Maven based on your OS from the official website and configure Maven. For more information, see Downloading Apache Maven 3.8.6.
2. From the general ASAPI SDK package, obtain the Maven project dependencies for ASAPI
SDK for Java. For more information, see Obtain ASAPI SDKs.
3. Use one of the following methods to create a Maven project:
Method 1: Create a Maven project in IntelliJ IDEA. DKs Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select **Add Framework**
**Support...**.
b. Select **Maven** and click **OK**.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of
ASAPI SDK for Java to the libs folder, as shown in the following figure. DKs
5. Add the dependencies of ASAPI SDK for Java to the pom.xml file in the project directory.
DKs

```xml
<dependencies>
  <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>1.0.6.7-RELEASE</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/asapi-1.0.6.7-RELEASE.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>alicrypto-java-aliyun</artifactId>
    <version>1.0.4</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/alicrypto-java-aliyun-1.0.4.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcpkix-jdk15on</artifactId>
    <version>1.65</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/bcpkix-jdk15on-1.65.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>gmsse</artifactId>
    <version>1.1.0</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/gmsse-1.1.0.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.7</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/httpclient-4.5.7.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.83</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/fastjson-1.2.83.jar</systemPath>
  </dependency>
</dependencies>
```

**Note**

Replace `1.0.6.7-RELEASE` with the actual version of ASAPI SDK for Java.
6. On the right side of IntelliJ IDEA, view information in the Maven section.
If the information in the following figure appears, the dependencies are added. DKs

**Common templates**

The following code is a common method for using ASAPI SDK for Java to call API operations.

```java
import com.aliyun.asapi.ASClient; import java.util.HashMap; import java.util.Map; public class Demo {
    public static void main(String[] args) {
        // Create a connection to an ASClient object.
        ASClient client = new ASClient();
        // Configure the identifier of the requester to identify the source of the call
. This parameter is required and used only for identification. You can set this paramet er to a random value.
        client.setSdkSource("<The identifier of the requester>");
        // Specify whether to convert the first letter of the parameter from lowercase
to uppercase.
        client.setIsFormat(false);
        // The endpoint of ASAPI.
        String endpoint = "<The endpoint of ASAPI>";
        // Configure request parameters.
        Map<String, Object> parameters = new HashMap<String, Object>();
        // Authorization parameters.
        parameters.put(ASClient.ACCESSKEY_ID, "<yourAccessKeyId>");
        parameters.put(ASClient.ACCESSKEY_SECRET, "<yourAccessKeySecret>");
        parameters.put(ASClient.REGIONID, "<yourRegionId>");
        // API parameters of the cloud service.
        parameters.put(ASClient.PRODUCT, "<Service name>");
        parameters.put(ASClient.ACTION, "<API name>");
        parameters.put(ASClient.PRODUCT, "<API version>");
        // If you use an STS AcessKey 3-tuple to call the operation, enter the
SecurityToken information in the following format:
        // parameters.put(ASClient.SECURITY_TOKEN, "<yourSecurityToken>");
        // Configure business parameters for the API.
        parameters.put("<Parameter name>", "<Parameter value>");
        // Set the headers. The API of a cloud service requires multiple common header
parameters, including x-acs-regionid, x-acs-organizationid, x-acs-resourcegroupid, and x-acs-instanceid. For more information, see Obtain common header parameters.
        Map<String, String> headers = new HashMap<String, String>();
```

DKs

```java
        headers.put("x-acs-regionid", "<yourRegionId>");
        headers.put("x-acs-resourcegroupid", "<yourResourceGroupId>");
        headers.put("x-acs-organizationid", "<yourOrganizationId>");
        headers.put("x-acs-instanceid", "<your-instanceid>");
        // Configure the connection timeout period.
        // client.setConnectTimeout(10000);
        // Configure the request timeout period.
        // client.setSocketTimeout(10000);
        try {
            // Initiate the request and obtain the response.
            String result = client.doPost(endpoint, headers, parameters);
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
```

`}` `}` `}`

**Note**

1.0.6.7-RELEASE: uses HMAC-SHA256 as the default signature algorithm, and also supports HMAC-SHA1. 1.0.2.5-RELEASE: uses HMAC-SHA1 as the default signature algorithm, and also supports HMAC-SHA256. Use Parameter to set the signature algorithm that you want to use, for example,

```
 parameters.put("SignatureMethod","HMAC-SHA256"); .
```

**Call examples**

The following example shows how to call the GetOrganizationList operation. DKs

```java
import com.aliyun.asapi.ASClient; import java.util.HashMap; import java.util.Map; public class Demo {
    public static void main(String[] args) {
        // Create a connection to an ASClient object.
        ASClient client = new ASClient();
        // Configure the identifier of the requester to identify the source of the call
. This parameter is required and used only for identification. You can set this paramet er to a random value.
        client.setSdkSource("<The identifier of the requester>");
        // Specify whether to convert the first letter of the parameter from lowercase
to uppercase.
        client.setIsFormat(false);
        // The endpoint of ASAPI.
        String endpoint = "<The endpoint of ASAPI>";
        // Configure request parameters.
        Map<String, Object> parameters = new HashMap<String, Object>();
        // Authorization parameters.
        parameters.put(ASClient.ACCESSKEY_ID, "<yourAccessKeyId>");
        parameters.put(ASClient.ACCESSKEY_SECRET, "<yourAccessKeySecret>");
        parameters.put(ASClient.REGIONID, "<yourRegionId>");
        // API parameters of the cloud service.
        parameters.put(ASClient.PRODUCT, "ascm");
        parameters.put(ASClient.ACTION, "GetOrganizationList");
        parameters.put(ASClient.VERSION, "2019-05-10");
        // Configure business parameters for the API.
        parameters.put("id",3);
        // Set the headers.
        Map<String, String> headers = new HashMap<String, String>();
        // Configure the connection timeout period.
        // client.setConnectTimeout(10000);
        // Configure the request timeout period.
        // client.setSocketTimeout(10000);
        try {
            // Initiate the request and obtain the response.
            String result = client.doPost(endpoint, headers, parameters);
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
```

`}` `}` `}`

**Configure a proxy**

If a network proxy exists between your environment and the ASAPI network, you need to replace ASClient client = new ASClient(); in the calling code with the following code to set the proxy. DKs

```
Cloud cloud = new Cloud(); // Set the IP address. cloud.setConfig("proxy_host", "<IP>"); // Set the port. cloud.setConfig("proxy_port", "<Port>"); // Create an ASClient connection to use a network proxy. ASClient client = new ASClient(cloud);
```

#### 2.2.5 SDK for Python

After you install Apsara Stack SDK for Python, you can write code to call API operations by using Apsara Stack API (ASAPI).

**Prerequisites**

An AccessKey pair or an STS AccessKey 3-tuple is obtained. We recommend that you use an AccessKey pair or an STS AccessKey 3-tuple for personal accounts to call API operations of the Apsara Uni-manager Management Console and cloud services. For more information, see Obtain AccessKey credentials. The endpoint of ASAPI is obtained. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of ASAPI. The package of Apsara Stack SDK for Python is obtained. For more information, see Obtain Apsara Stack SDKs.

**Add dependencies**

**Install the SDK for Python over the Internet**

After you download and decompress the package of Apsara Stack SDK for Python, run the following code in the directory where the package is stored to install the applicable version of SDK for Python.

**Note**

We recommend that you install Python 3.x. Install Apsara Stack SDK for Python 3.x.

```bash
# Install the core library of Apsara Stack SDK.
pip3 install aliyun-python-sdk-core-v3
# Install the SDK for Python.
pip3 install aliyun-python3-sdk-asapi-<The version number of the SDK for Python>.tar.
```

`gz` Install Apsara Stack SDK for Python 2.x.

```bash
# Install the core library of Apsara Stack SDK.
pip install aliyun-python-sdk-core
# Install the SDK for Python.
pip install aliyun-python2-sdk-asapi-<The version number of the SDK for Python>.tar.g
```

`z` DKs

**Note**

When you install the SDK for Python, the required resource packages are automatically downloaded. If you cannot connect to the Internet, follow the operations described in the Install the SDK for Python without Internet access section to install the SDK for Python.

**Install the SDK for Python without Internet access**

If you cannot connect to the Internet, perform the following operations to install the SDK.

**Step 1: Export the resource packages for the SDK for Python.**

**Note**

Only the resource packages for the X86-based SDK for Python are provided. For more information, obtain the **downloadPackage.tgz** of the SDK for Python from the Apsara Stack SDK package. If the provided resource packages cannot meet your needs, perform Step 1 to export the resource packages you need.
1. If you can connect to the Internet, see the Install the SDK for Python over the Internet
section to install the SDK.
2. Run the following command to export the resource packages to the **downloadPackage**
folder:

```
pip freeze > requirements.txt & pip download -d downloadPackage -r requirements.txt
```

3. Compress the **downloadPackage** folder into a `.tgz` package.

**Step 2: Install Apsara Stack SDK for Python.**

1. Upload the **downloadPackage.tgz** package to your environment and decompress it.

**Important**

Decompress the **downloadPackage.tgz** package and store the **downloadPackage** folder in the directory in which the SDK for Python is stored.
2. Run the following command to install the Apsara Stack SDK for Python:
Replace `<The version number of the SDK for Python>` with the actual version number of the SDK for Python. Install Apsara Stack SDK for Python 3.x.

```
pip install --no-index --find-links=./downloadPackage aliyun-python-sdk-asapi-<The version number of the SDK for Python>-py3.tar.gz
```

Install Apsara Stack SDK for Python 2.x.

```
pip install --no-index --find-links=./downloadPackage aliyun-python-sdk-asapi-<The version number of the SDK for Python>-py2.tar.gz
```

**Common templates**

The following code is a common method for using ASAPI SDK for Python to call API operations. DKs

```python
#coding=utf-8
from aliyunsdkasapi.ASClient import ASClient from aliyunsdkasapi.AsapiRequest import AsapiRequest
# Create a connection to an ASClient object. The timeout parameter specifies the timeou
t period for a request. The cert_file parameter specifies the certificate. The verify p arameter specifies whether to verify the certificate. client = ASClient("<yourAccessKeyId>", "<yourAccessKeySecret>", "<yourRegionId>",
                  timeout=10000,
                  cert_file=None,
                  verify=False)
# Configure the identifier of the requester to identify the source of the call. This pa
rameter is required and used only for identification. You can set this parameter to a r andom value. client.setSdkSource("<The identifier of the requester>")
# The ASAPI endpoint. For more information, see Obtain the endpoint of ASAPI.
endpoint = "<The ASAPI endpoint>"
# Create a request.
request = AsapiRequest("<Product name>", "<API version>", "<API name>", endpoint)
# Specify the request method.
request.set_method("POST")
# Configure business parameters for the API.
request.add_body_params("<Business parameter name>", "<Parameter value>")
# If you use an STS AcessKey 3-tuple to call the operation, enter the SecurityToken inf
ormation in the following format:
# request.add_body_params("SecurityToken", "<Your security token>");
# Set the headers.
# The API of a cloud service requires multiple common header parameters, including x-ac
s-regionid, x-acs-organizationid, x-acs-resourcegroupid, and x-acs-instanceid. For more information, see Obtain the value of common header parameters. request.add_header("x-acs-resourcegroupid", "<yourResourceGroupId>"); request.add_header("x-acs-organizationid", "<yourOrganizationId>"); request.add_header("x-acs-regionid", "<yourRegionId>"); request.add_header("x-acs-instanceid", "<yourInstanceId>");
# Initiate the request and obtain the response.
response = client.do_request(request)
# Print the response. python2: print(response)
print(str(response, encoding='utf-8'))
```

DKs

**Note**

2.4.7.1-RELEASE: HMAC-SHA256 is used as the default signature algorithm. HMAC- SHA1 is also supported. 2.2.1.1-RELEASE: HMAC-SHA1 is used as the default signature algorithm. HMAC- SHA256 is also supported. Run a command in the following format to specify the signature algorithm:

```
 request.add_body_params("SignatureMethod", "<Your signature algorithm>") . For
example, request.add_body_params("SignatureMethod","HMAC-SHA256"); .
```

**Call example**

The following code provides an example on how to call the `GetOrganizationList` operation by using SDK for Python:

```python
#coding=utf-8
from aliyunsdkasapi.ASClient import ASClient from aliyunsdkasapi.AsapiRequest import AsapiRequest
# Create a connection to an ASClient object. The timeout parameter specifies the timeou
t period for a request. The cert_file parameter specifies the certificate. The verify p arameter specifies whether to verify the certificate. client = ASClient("<yourAccessKeyId>", "<yourAccessKeySecret>", "<yourRegionId>",
                  timeout=10000,
                  cert_file=None,
                  verify=False)
# Configure the identifier of the requester to identify the source of the call. This pa
rameter is required and used only for identification. You can set this parameter to a r andom value. client.setSdkSource("<The identifier of the requester>")
# The ASAPI endpoint. For more information, see Obtain the endpoint of ASAPI.
endpoint = "<The ASAPI endpoint>"
# Create a request.
request = AsapiRequest("ascm", "2019-05-10", "GetOrganizationList", endpoint)
# Specify the request method.
request.set_method("POST")
# Configure business parameters for the API.
request.add_body_params("id", 3)
# Set the headers.
# Initiate the request and obtain the response.
response = client.do_request(request)
# Print the response. python2: print(response)
print(str(response, encoding='utf-8'))
```

**Configure proxies**

If a network proxy exists between your environment and ASAPI, you must add the following code before `client = ASClient(...)` when you call the API operation to import OS dependencies and set the proxy. DKs

```java
# Import OS dependencies.
import os
# Set the proxy. Replace x.x.x.x:xxxx with the IP address and port number of the proxy.
os.environ['http_proxy'] = "http://x.x.x.x:xxxx" os.environ['https_proxy'] = "https://x.x.x.x:xxxx"
```

#### 2.2.6 Use SDK for Node.js to call API operations

#### operations

After you install ASAPI SDK for Node.js, you can create programmatic access to Apsara Stack services by using the SDK to call ASAPI operations.

**Prerequisites**

You have obtained an AccessKey pair or access credentials assigned by STS. We recommend that you use an AccessKey pair or access credentials assigned by STS for personal accounts to call API operations for the Apsara Uni-manager Management Console and cloud services. For more information, see Obtain AccessKey credentials. The endpoint of ASAPI is obtained. For more information, see Obtain the endpoint of ASAPI. If the endpoint of ASAPI uses HTTPS, you can ignore the certificate by using the `NODE_TLS_REJECT_UNAUTHORIZED=0` environment variable configuration. The Node.js ASAPI SDK package is obtained. For more information, see Obtain the ASAPI SDK package.

**Install dependencies**

The **asapi-nodejs-sdk.tgz** package included in the general ASAPI SDK package contains ASAPI SDK for Node.js and related dependencies. You can perform the following steps to install ASAPI SDK for Node.js, regardless of whether you have access to the Internet:
1. Locate the **asapi-nodejs-sdk.tgz** package from the general ASAPI SDK package.
2. Run the following command to decompress the **asapi-nodejs-sdk.tgz** package. After the
decompression, place the **asapi-nodejs-sdk** folder under the root directory of the Node.js project. We recommend that you use an LTS version of Node.js.

```
tar -zxf asapi-nodejs-sdk.tgz
```

3. Under the root directory of the Node.js project, run the following command to install ASAPI
SDK for Node.js:

```
npm i ./asapi-nodejs-sdk --save
```

**Common template**

The following code shows a common method for using ASAPI SDK for Node.js to call API operations.

```
// Import the SDK dependencies. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // Set the endpoint of ASAPI and authenticate the API operation. const cnofig = {
  API_GATEWAY: '<ASAPI endpoint>',
```

DKs

```
  regionId: '<yourRegionId>',
  accessKeyId: '<yourAccessKeyId>',
  accessKeySecret: '"<yourAccessKeySecret>'
```

};

```json
// Initialize the ASAPI client. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // Specify the request parameters. const params = {
  "Action": "<apiOperation>",
  "Product": "<serviceName>",
  "Version": "<apiVersion>",
  "regionId": "<yourRegionId>",
  // When you use access credentials assigned by STS to call an API operation, you must
add the SecurityToken field in the request parameters.
  // "SecurityToken": "<yourSecurityToken>"
  // Configure parameters for the API operation.
  "<Operation-specific parameter>": "<parameterValue>"
```

`}`

```
// Set the headers. // Configure the identifier of the requester to identify the source of the call. This p arameter is required and used only for identification. You can set this parameter to a random value. AsapiClient.addHeader('x-acs-caller-sdk-source', '<requesterIdentifier>') // Set the headers. The API of a cloud service requires multiple common header parameters, including x-acs-regionid, x-acs-organizationid, x-acs-resourcegroupid, and x-acs-instanceid. For more information, see the "Obtain the value of common header para meters" topic. AsapiClient.addHeader("x-acs-resourcegroupid", "<yourResourceGroupId>"); AsapiClient.addHeader("x-acs-organizationid", "<yourOrganizationId>"); AsapiClient.addHeader("x-acs-regionid", "<yourRegionId>"); AsapiClient.addHeader("x-acs-instanceid", "<yourInstanceId>"); // Initiate the call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // Specify the request method.
    formatParams: false, // Specify whether to format parameters and capitalize the fir
st letter of each parameter.
    enableProxy: false, // Specify whether to configure a proxy. If you want to configu
re a proxy, set this parameter to true. If you do not want to configure a proxy, set th is parameter to false.
    proxy: 'http://x.x.x.x:xxxx', // Specify the URL of the proxy.
    timeout: 10000 // Specify the timeout period.
    //ca: fs.readFileSync(path.resolve(__dirname, keys_dir,'ca.crt'), 'utf8')
    // You can optionally specify a CA certificate. For more information, visit https:/
/nodejs.org/api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

`}`

**Call example**

DKs The following sample code shows how to call the `GetOrganizationList` operation for the Apsara Uni-manager Management Console:

```
// Import the SDK dependencies. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // Specify the endpoint and authentication configuration. const cnofig = {
  API_GATEWAY: '<ASAPI endpoint>',
  regionId: '<yourRegionId>',
  accessKeyId: '<yourAccessKeyId>',
  accessKeySecret: '"<yourAccessKeySecret>'
```

};

```json
// Initiate the ASAPI client. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // Specify the request parameters. const params = {
  "Action": "GetOrganizationList",
  "Product": "ascm",
  "Version": "2019-05-10",
  "regionId": "<yourRegionId>",
  // Configure parameters for the API operation.
  "id": 3
```

`}`

```
// Set the headers. AsapiClient.addHeader('x-acs-caller-sdk-source', '<requesterIdentifier>') // Initiate the call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // Specify the request method.
    formatParams: false, // Specify whether to format parameters and capitalize the fir
st letter of each parameter.
    enableProxy: false, // Specify whether to configure a proxy. If you want to configu
re a proxy, set this parameter to true. If you do not want to configure a proxy, set th is parameter to false.
    proxy: 'http://x.x.x.x:xxxx', // Specify the URL of the proxy.
    timeout: 10000 // Specify the timeout period.
    //ca: fs.readFileSync(path.resolve(__dirname, keys_dir,'ca.crt'), 'utf8')
    // You can optionally specify a CA certificate. For more information, visit https:/
/nodejs.org/api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

`}`

**Configure a proxy**

You can optionally configure a proxy between your environment and the network for ASAPI: DKs

```
enableProxy: true, // Specify whether to configure a proxy. If you want to configure a proxy, set this parameter to true. If you do not want to configure a proxy, set this pa rameter to false. proxy: 'http://x.x.x.x:xxxx', // Specify the URL of the proxy. Replace x.x.x.x.x:xxxx w ith the actual network proxy IP address and proxy port. timeout: 10000 // Specify the timeout period.
```

requests

## 3 HTTP requests

### 3.1 Overview

This topic describes how to call Apsara Stack APIs registered with ASAPI by sending HTTP requests.

**Note**

We recommend that you use SDKs to call API operations instead of using HTTP requests. Currently, ASAPI provides SDKs for Node.js, Python, and Java, which save you from the signing process. If you use an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters but has a fixed request structure. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded, which makes them easy to read. Before you initiate a request, you must encode the request URL. After the request is verified, the results are returned. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

### 3.2 Request syntax

ASAPI allows you to initiate HTTP GET requests based on URLs. Each URL must contain request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of ASAPI.

**Sample request**

The following example shows an unencoded URL that is used to call the GetOrganizationList operation:

```
https://public.asapi.aliyuns.com/asapi/v3? Action=GetOrganizationList&Product=ascm&Version=2019-05-10&Id=<Organization ID>&<Common request parameters>
```

`https` specifies the protocol that is used to send the request. `public.asapi.aliyuns.com/asapi/v3` specifies the endpoint of ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` specifies the API operation. `Id` specifies the ID of the organization. For more information, see Obtain the values of common header parameters. `<Common request parameters>` specifies common parameters. For more information, see Common parameters.

**Communications protocol**

ASAPI supports only HTTPS.

**Endpoint**

For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of ASAPI. requests You must use the Action, Product, and Version parameters to specify an API operation. For example, you can set Action to GetOrganizationList, Product to ascm, and Version to 2019-05-
10. You also need to specify other parameters and common request parameters in an
API operation. For more information, see the related API reference documentation and Common parameters.

### 3.3 Signature method

This topic describes how to sign HTTP API requests. Apsara Stack uses the request signature to verify the identity of the requester. Specifically, Apsara Stack uses an AccessKey pair to perform symmetric encryption and verify the identity of the requester.

**Note**

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify the identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must store the AccessKey secret in a secure location.

**Step 1: Create a canonicalized query string**

1. Sort the request parameters in alphabetical order, including all common and operation-
specific parameters except for `Signature` .

**Note**

If you use the GET method to send a request, the request parameters are included as part of the request URL. The parameters follow the question mark (?) and are connected by ampersands (&) in the URL.
2. Encode the names and values of the request parameters in UTF-8 based on RFC 3986. The
following rules apply in the encoding process: Letters, digits, hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Other characters must be percent-encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). The preceding encoding method is similar to but slightly different from the `application/x-www-form-urlencoded` MIME-type encoding algorithm. If you use `java.net.URLEncoder` in the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules. requests

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException {
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").r
eplace("*", "%2A").replace("%7E", "~") : null;
```

`}`
3. Use equal signs ( `=` ) to connect the name and value of an encoded parameter.
4. Use ampersands ( `&` ) to connect the encoded request parameters. These parameters
must be arranged in the same order as those in Step 1. Then, a canonicalized query string that follows the request structure is obtained. For more information, see Request syntax.

**Step 2: Create a string-to-sign**

1. Create a string-to-sign ( `StringToSign` ). You can also use `percentEncode` to encode the
canonicalized query string that is generated in Step 1. When you create a string-to-sign, take note of the following rules:

```
StringToSign=
    HTTPMethod + "&" + //HTTPMethod: the HTTP method that is used to send the request
, such as GET.
    percentEncode("/") + "&" + // percentEncode("/"): Encode the forward slash (/) in
UTF-8 as %2F.
    percentEncode(CanonicalizedQueryString) // Encode the canonicalized query string
created in Step 1.
```

2. Calculate the HMAC-SHA1 or HMAC-256 value of `StringToSign` based on RFC 2104. In this
example, the Java Base64 encoding method is used.

```
String signature = Base64.getEncoder().encodeToString(signData);
```

**Note**

When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
3. Encode the `Signature` parameter based on RFC 3986 and add the parameter to the
canonicalized query string.

**Example 1: Concatenate parameters**

| GetOrganizationList |   | is used in this |
|---|---|---|
| is set to testid and |   |   |

`GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret. Perform the following operations:
1. Create a canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/? AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn region-test&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f 39d2&SignatureVersion=1.0&Timestamp=2020-09-15T08%3A50%3A40Z&Version=2019-05-10
```

2. Create a string-to-sign ( `StringToSign` ).
requests

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DGetOrganizationList%26Format%3DJSON%26Id%3D1%26 oduct%3Dascm%26RegionId%3Dcn-region-test%26SignatureMethod%3DHMAC- SHA1%26SignatureNonce%3D43967c6e-e3ad-44fa-b06bfcf3db5f39d2%26SignatureVersion%3D1.0%26Timestamp%3D2020-09- 15T08%253A50%253A40Z%26Version%3D2019-05-10
```

3. Calculate the signature.
Calculate the signature. If `AccessKeySecret` is set to testsecret, `testsecret&` is used as the key value to calculate the signature. The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . In this example, the Java Base64 encoding method is used.

| String signature = Base64.getEncoder().encodeToString(signData); |   |
|---|---|
| Signature=hvqv9Ll5RE6kQ4YsQXFAf9VuRIY= | based on RFC 3986 and ad |

canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/? AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn region-test&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f 39d2&SignatureVersion=1.0&Timestamp=2020-09-15T08%3A50%3A40Z&Version=2019-05-10
```

The new URL allows you to send an HTTP request from a browser or a tool such as cURL and Wget to call the `DescribeRegions` operation, which is used to query Alibaba Cloud regions.

**Example 2: Use the standard library of the programming language**

| GetOrganizationList |   | is used in t |
|---|---|---|

`GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored

| Map<String, String> |   |   |
|---|---|---|
|   |   | o |

1. Predefine the encoding method.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
```

`{`

```
        return value != null ? URLEncoder.encode(value, ENCODING).replace("+",
"%20").replace("*", "%2A").replace("%7E", "~") : null;
```

`}`
2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp`
parameter in the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

`}`
3. Create a query string.
requests

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Configure request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Sort the request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
```

`}`

```
// Encode the canonicalized query string. stringToSign.append(percentEncode( canonicalizedQueryString.toString().substring(1)));
```

4. Calculate the signature. If `AccessKeySecret` is set to testsecret, `testsecret&` is used as
the key value to calculate the signature. The calculated signature is

```
 OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D .
// The following sample code shows how to calculate the signature: final String ALGORITHM = "HmacSHA1"; final String ENCODING = "UTF-8"; key = "testsecret&"; Mac mac = Mac.getInstance(ALGORITHM); mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM)); byte[] signData = mac.doFinal(stringToSign.getBytes(ENCODING)); String signature = Base64.getEncoder().encodeToString(signData);
```

Encode the Signature parameter based on RFC 3986 and add the result to the canonicalized query string. The following URL is obtained:

```
https://public.asapi.aliyuns.com/asapi/v3/? AccessKeyId=testid&Action=GetOrganizationList&Format=JSON&Id=1&Product=ascm&RegionId=cn region-test&SignatureMethod=HMAC-SHA1&SignatureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f 39d2&SignatureVersion=1.0&Timestamp=2020-09-15T08%3A50%3A40Z&Version=2019-05-10
```

requests
5. Use a browser or a tool such as cURL or Wget to send an HTTP request.

### 3.4 Responses

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned.

**Sample success responses**

If a request is successful, the request ID and operation-specific parameter values are returned. `{`

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

`}` `],`

```json
  "requestId":"xxxxxxxxxxxxxx",
  "success":true,
  "message":"success"
```

`}`

**Sample error responses**

If a request fails, the following information is returned: requests `{`

```json
    "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by ASAPI.
```

`}`

## 4 Apsara Uni-manager Management Console API Reference

**Management Console API**

**Reference**

### 4.1 Common parameters

Common parameters are classified into common request parameters, common request headers, and common response parameters.

**Common request parameters**

Common request parameters must be included in all API requests of the Apsara Uni-manager Management Console. Table 1. Table of common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. For more information, see Obtain API information. |
| Product | Strin g | Yes | The name of the service to which the operation belongs. Set the value to ascm. |
| Version | Strin g | Yes | The version number of the API. The value is in the YYYY-MM-DD format. Set the value to 2019-05-10. |
| RegionId | Strin g | Yes | The ID of the region. For more information, see Obtain a region ID. |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided to you by the Apsara Uni-manager Management Console. For more information, see Obtain AccessKey credentials. |
| Signature | Strin g | Yes | The signature string of the current request. For more information about how signatures are calculated, see the "Request signatures" topic. |
| SignatureMe thod | Strin g | Yes | The encryption algorithm of the signature string. Valid values: HMAC-SHA1 and HMAC-SHA256. |
| SignatureVer sion | Strin g | Yes | The version of the signature encryption algorithm. Valid values: 1.0, 2.0, and 2.1. |
| SignatureNo nce | Strin g | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | Strin g | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, 2018-01-01T12:00:00Z specifies 20:00:00 on January 1, 2018 in UTC+8. |
| Format | Strin g | No | The format in which to return the response. Set the value to JSON. |

**Note**

The Signature, SignatureMethod, SignatureVersion, SignatureNonce, Timestamp, and Format parameters are encapsulated into SDK of the Apsara Unimanager Management Console. You do not need to specify these parameters. You can obtain the values of the `Product` and `Version` parameters in the Apsara Unimanager Management Console. Perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products > Others > API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. In the **operation name** search box, enter the name of an operation to query its
information.

**Common request headers**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. For more information about how to obtain an instance ID, see Obtain an instance ID. |

**Note**

When you call an operation of a cloud service, you must specify common request headers, such as **x-acs-organizationid**, **x-acs-resourcegroupid**, and **x-acs-**
**instanceid**, in the request. x-acs-instanceid specifies the ID of the instance on which you
want to perform the operation. x-acs-organizationid specifies the ID of the organization to which the instance belongs. x-acs-resourcegroupid specifies the ID of the resource group to which the instance belongs. If you call an operation to create an instance or query the list of instances, you do not need to specify x-acs-instanceid. If you do not specify specific request headers when you call an operation, the relevant data in the root organization and root resource set is used.

**Common response parameters**

| Parameter | Returned in a successful call | Description |
|---|---|---|
| asapiRequestId | Yes Note This parameter is returned regardless of whether the call is successful. | The ID of the request. |

| asapiSuccess | Yes Note This parameter is returned regardless of whether the call is successful. If this parameter is not contained in the response parameters of specific operations, you can check whether the calls are successful based on the return values in the documentation. | Indicates whether the call is successful. true false |
|---|---|---|
| eagleEyeTraceId | Yes Note This parameter is returned regardless of whether the call is successful. | The EagleEye ID of a trace. |
| asapiErrorCode | No | The error code. |
| asapiErrorMessage | No | The error message. |
| product | No | The code of the service to which the operation belongs. |
| api | No | The information about the operation. |
| serverRole | No | The name of the service that is accessed. |
| domain | No | The domain name of the service that is accessed. |

**Sample code of a successful call:**

`{`

```json
    "asapiRequestId": "6ff2f841-949c-4328-ab40-1e527f1d8dea",
    "asapiSuccess": true,
    "eagleEyeTraceId": "0a8008a116540922323935472e0022"
```

`}`

**Sample code of a failed call:**

`{`

```json
    "asapiRequestId": "0aa9394d16145818029452621d0054",
    "asapiSuccess": false,
    "eagleEyeTraceId": "0aa9394d16145818029452621d0054",
    "asapiErrorCode": "ascm.auth.account.notLoggedIn",
    "asapiErrorMessage": "Load ascm ticket failed, try to clear cookies and relogin.",
    "product": "ascm",
    "api": "ascm:LoadByAscmTicket:2019-05-10",
    "serverRole": "ascm-brm.Auth#",
    "domain": "ascm-auth.res.ali.hgpoc.ctax.govcn"
```

`}`

### 4.2 Apsara Uni-manager Management Console authentication

**Management Console**

**authentication**

Before you make ASAPI requests, you must obtain the AccessKey pair (an AccessKey ID and an AccessKey secret) of an organization account in the Apsara Uni-manager Management Console. The organization account grants access permissions on available resources. Then, you can use the AccessKey pair to access the resources and manage the resources. For more information about how to obtain an AccessKey pair, see Obtain AccessKey credentials.

**Important**

If you use the AccessKey pair of a personal account to call an API operation, you must configure header parameters for access control. Otherwise, a message is prompted to indicate that you have insufficient permissions. Header parameters

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain the ID of an organization, see GetOrganizationList. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain the ID of a resource set, see ListResourceGroup. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an ECS instance, you can obtain the ID from the ECS instance list. |

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

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| id | String | Body | No | 23 | The ID of the organization. Note This parameter is required. |
| name | String | Body | No | org-test | The name of the organization that you want to update. Note This parameter is required. |
| orgUuid | String | Body | No | org- 101****e53b4 0ae6086****m | The UUID of the organization. Note The organization UUID cannot be updated by using API operations. |
| parentId | String | Body | No | 1 | The ID of the parent organization. Note The ID of the root organization is 1. |

| level | String | Body | No | 0.1.3 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
|---|---|---|---|---|---|
| personNum | String | Body | No | 10 | The maximum number of users. The value must be a positive integer. |
| resourceGroup Num | String | Body | No | 10 | The maximum number of resource sets. The value must be a positive integer. |
| alias | String | Body | No | org-test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
| multiCloudStat us | String | Body | No | null | The multi-cloud status of the organization. Default value: null. master: The organization is a primary-cloud organization. slaver: The organization is a secondary-cloud organization. null: The organization is not a multi-cloud organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The organization ID is empty. The organization name is duplicated. One or more parameters are invalid. One or more request parameters are not specified in the operation. 403: You do not have permissions. 404: The user does not exist. 500: An internal error occurred. |
|---|---|---|---|
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Struct |   | The response data. |
| alias | String | org-test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
| ctime | Long | 1607512443989 | The time when the organization was created. |
| cuserId | String | 5003 | The username of the user who created the organization. |
| id | Integer | 1 | The ID of the organization. Note The ID of the root organization is 1. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. Note The system automatically generates a preset organization, which is also named the default organization. |

| level | String | 0.1 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
|---|---|---|---|
| mtime | Long | 1606791494471 | The time when the organization was last updated. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary- cloud organization. slave: The organization is a secondary- cloud organization. Note This parameter is returned only in multi-cloud scenarios. |
| muserId | String | admin | The username of the user who last updated the organization. |
| name | String | org-test | The name of the updated organization. The name is the same as the value that is specified for the name request parameter. |
| parentId | Integer | 0 | The ID of the parent organization. Note The ID of the root organization is 1. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |

| message | String | 200 | The message. Examples: OrgNameExist: The organization name is duplicated. missing uuid or id: The UUID or ID of the organization is not contained in request parameters. |
|---|---|---|---|
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | false | Indicates whether the request is redirected. true false |
| requestId | String | 1 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateOrganization &Id=23 &Name=org-test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>10000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <internal>true</internal>
    <level>0.1</level>
    <supportRegions>cn-qingdao-****-d01</supportRegions>
    <mtime>1606791494471</mtime>
    <uuid>1231</uuid>
    <parentId>0</parentId>
    <multiCloudStatus>master</multiCloudStatus>
    <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
    <name>org-test</name>
    <ctime>1607512443989</ctime>
    <alias>org-test</alias>
    <id>1</id>
    <cuserId>admin</cuserId>
</data> <success>true</success> <requestId>1</requestId> <pureListData>true</pureListData> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": false,
    "cost": 10000,
    "code": 200,
    "data": {
        "muserId": "admin",
        "internal": true,
        "level": 0.1,
        "supportRegions": "cn-qingdao-****-d01",
        "mtime": 1606791494471,
        "uuid": 1231,
        "parentId": 0,
        "multiCloudStatus": "master",
        "supportRegionList": "[\"cn-qingdao-****-d01\"]",
        "name": "org-test",
        "ctime": 1607512443989,
        "alias": "org-test",
        "id": 1,
        "cuserId": "admin"
```

`},`

```json
    "success": true,
    "requestId": 1,
    "pureListData": true,
    "message": 200
```

`}`

###### 4.3.1.1.2 UpdateSupportRegionsForOrg

Updates the list of zones in an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/updateSupportRegionsForOrg HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| supportRegion s | String | Body | No | RegionId1,Reg ionId2 | The list of zones that you want to update. Separate multiple zone IDs with commas (,). |
| organizationId | Integer | Body | No | 5 | The ID of the organization. Note The ID of the root organization is 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 400: One or more parameters are invalid or the AccessKey pair is disabled. 403: You do not have permissions. 404: The RAM policy mapping, user, or AccessKey does not exist. |
| cost | Integer | 32 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |

| message | String | success | The message. Examples Empty securityToken: The security token is empty. The ram role mapping is not exist: The RAM role mapping does not exist. Can't find user by specified ascm user id: xxx: No user is found by using the user ID. |
|---|---|---|---|
| pureListData | Boolean | false | Indicates whether only data is returned. false: Only data is returned. ture: Other parameters are returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST null HTTP/1.1 Common request headers
```

`{`

```json
"OrganizationId": "5", "SupportRegions": "RegionId1,RegionId2"
```

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>32</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "32",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.1.3 GetOrganization

Queries the information about an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/query HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| id | Integer | Body | No | 32 | The ID of the organization. Note The ID of the root organization is 1. |
| orgUuid | String | Body | No | org- 101****0b6a7 0ae6086***** | The UUID of the organization. Note If you specify the id and orgUuid parameters, the value of the id parameter is used. If you leave the parameters empty, the response is empty. |
| requestId | String | Body | No | 0a1a****1655 45803068829 70d**** | The ID of the request. Note In most cases, you do not need to specify this parameter. The system automatically generates a value for this parameter. |

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
|---|---|---|---|
| mtime | Long | 1607512443989 | The time when the organization was last modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary- cloud organization. slave: The organization is a secondary- cloud organization. Note This parameter is returned only in multi-cloud scenarios. |
| muserId | String | admin | The username of the user who last modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. Note The ID of the root organization is 1. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |
| message | String | success | The message. Examples: success: The call is successful. MissingParams: Required request parameters are not specified. |

| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
|---|---|---|---|
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59- ****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetOrganization &Id=32 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <internal>true</internal>
    <level>0.1</level>
    <supportRegions>cn-qingdao-****-d01</supportRegions>
    <mtime>1607512443989</mtime>
    <uuid>1231</uuid>
    <parentId>1</parentId>
    <multiCloudStatus>master</multiCloudStatus>
    <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
    <name>test</name>
    <ctime>1606791494471</ctime>
    <alias>test</alias>
    <id>1</id>
    <cuserId>admin</cuserId>
</data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "data": {
        "muserId": "admin",
        "internal": "true",
        "level": "0.1",
        "supportRegions": "cn-qingdao-****-d01",
        "mtime": "1607512443989",
        "uuid": "1231",
        "parentId": "1",
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
    "success": "true",
    "requestId": "16d09b14-8a59-****-****-7536fe897b66",
    "pureListData": "true",
    "message": "success"
```

`}`

###### 4.3.1.1.4 GetOrganizationList

Queries the list of organizations.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/queryList HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| id | Integer | Body | No | 1 | The ID of the organization. Note The ID of the root organization is 1. |
| name | String | Body | No | test | The name of the organization. Note If you specify the id and name request parameters, the system returns the IDs of subordinate organizations of the organization whose ID is specified by using the id request parameter. If you specify only the name request parameter, the system returns the IDs of subordinate organizations of the organization whose name is specified by using the name request parameter. If you do not specify the id and name request parameters, the response is empty. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 403: You do not have permissions. |
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Array of dataItem |   | The response data. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The username of the user who created the organization. |
| extraInfo | String | null | This parameter is deprecated. |
| id | Integer | 1 | The ID of the organization. Note If only the id or name request parameter is specified, the IDs of subordinate organizations of the organization whose ID is specified by using the id request parameter or of the organization whose name is specified by using the name request parameter are returned. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. Note The system automatically generates a preset organization, which is also named the default organization. |

| level | String | 0.1 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
|---|---|---|---|
| mtime | Long | 1607512443989 | The time when the organization was last modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary- cloud organization. master: The organization is a secondary-cloud organization. Note This parameter is returned only in multi-cloud scenarios. |
| muserId | String | admin | The username of the user who last modified the organization. |
| name | String | test | The name of the organization. Note If only the id request parameter is specified, the name of the organization whose ID is specified by using the id request parameter is returned. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |

| message | String | success | The message. The value success specifies that the call is successful. The call fails in the following scenarios: The signature fails to be verified. The AccessKey pair is invalid. |
|---|---|---|---|
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59- ****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
POST /ascm/auth/organization/queryList HTTP/1.1 Common request headers
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <internal>true</internal>
    <level>0.1</level>
    <supportRegions>cn-qingdao-****-d01</supportRegions>
    <mtime>1607512443989</mtime>
    <uuid>1231</uuid>
    <parentId>0</parentId>
    <multiCloudStatus>master</multiCloudStatus>
    <name>test</name>
    <ctime>1606791494471</ctime>
    <alias>test</alias>
    <id>1</id>
    <cuserId>admin</cuserId>
</data> <data>
    <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
</data> <success>true</success> <requestId>1</requestId> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": true,
    "cost": 10000,
    "code": 200,
    "data": [
```

`{`

```json
            "muserId": "admin",
            "internal": true,
            "level": 0.1,
            "supportRegions": "cn-qingdao-****-d01",
            "mtime": 1607512443989,
            "uuid": 1231,
            "parentId": 0,
            "multiCloudStatus": "master",
            "name": "test",
            "ctime": 1606791494471,
            "alias": "test",
            "id": 1,
            "cuserId": "admin"
```

`},` `{`

```json
            "supportRegionList": "[\"cn-qingdao-****-d01\"]"
```

`}` `],`

```json
    "success": true,
    "requestId": 1,
    "message": 200
```

`}`

###### 4.3.1.1.5 RemoveOrganization

Deletes an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/delete HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| orgUuid | String | Body | No | org- 101bbf866a93 0ae6******** | The UUID of the organization. Note When you call the RemoveOrganization operation, you must specify at least one request parameter. You can call the GetOrganization or GetOrganizationList operation to query the UUID of the organization. |
|---|---|---|---|---|---|
| id | String | Body | No | 39 | The ID of the organization that you want to delete. Note When you call the RemoveOrganization operation, you must specify at least one request parameter. You can call the GetOrganizationList operation to query the ID of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The organization ID is left empty. The organization does not exist. The AccessKey pair is invalid. One or more parameters are invalid. The operation is not supported by the Apsara Stack account. 403: You do not have permissions. 404: The AccessKey pair does not exist. The role does not exist. The user does not exist. The role does not belong to you. 500: An internal error occurred. Before you delete a resource set, you must delete all cloud resources in the resource set. The organization fails to be deleted. Before you delete the organization, you must delete users in the organization. The organization fails to be deleted. Before you delete the organization, you must delete user groups in the organization. The organization fails to be deleted. Before you delete the organization, you must delete roles in the organization. The organization fails to be deleted. Before you delete the organization, you must delete permission policies associated with the organization. The organization fails to be deleted. Before you delete the organization, you must delete logon policies associated with the organization. |
|---|---|---|---|
| cost | Integer | 10000 | The time consumed by the operation. Unit: milliseconds. Note If the time consumed between the request and the response of an operation called by using the ASAPI gateway exceeds 10 seconds, the operation times out. |

| message | String | success | The message. success: The call is successful. Calling manage returns empty body: No results are returned for the call. CheckResourceEmpty throws exception: One or more resource sets exist in the organization. |
|---|---|---|---|
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | false | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59- ****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveOrganization &Id=39 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "10000",
    "code": "200",
    "success": "true",
    "requestId": "16d09b14-8a59-****-****-7536fe897b66",
    "pureListData": "true",
    "message": "success"
```

`}`

###### 4.3.1.1.6 ListResourceGroupByOrgId

Queries the list of resource sets in an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/resourceGroupList HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| id | String | Body | No | 34 | The ID of the organization. Note This parameter is required when you call the operation. Otherwise, the response is empty. |
| resource grou _ p name _ | String | Body | No | testrs | The name of the resource set. Note This parameter is deprecated. |
| default | String | Body | No | 1 | The type of the resource set. 1: The resource set is the default one. 0: The resource set is not the default one. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The organization ID is empty. The organization does not exist. The AccessKey pair is invalid. One or more parameters are invalid. The operation is not supported by the Apsara Stack tenant account. 403: You do not have permissions. The operation fails to be called because the role of your account is disabled. Try again after the administrator enables the role. 404: The AccessKey pair does not exist. The role does not exist. The user does not exist. The role does not belong to your account. 500: A remote call error occurred. An internal error occurred. |
|---|---|---|---|
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Array of dataItem |   | The response data. |
| creator | String | admin | The username of the user who created the organiozation. |
| gmtCreated | Float | 1607512443989 | The time when the resource set was created. |
| gmtModified | Float | 1607512443999 | The time when the resource set was last modified. |
| id | Integer | 1 | The ID of the resource set. |

| organizationID | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| organizationN ame | String | admin-org | The name of the organization. |
| resourceGroup Name | String | resg-test | The name of the resource set. |
| resourceGroup Type | Integer | 1 | The type of the resource set. 1: The resource set is the default one. 0: The resource set is not the default one. |
| message | String | 200 | The message. Examples: The caller is not organization account: You do not have the permissions to view the organization that is specified in the request. User and access-key not matched: Your account does not match the AccessKey pair. |
| pageInfo | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 10 | The number of entries returned per page. |
| total | Integer | 100 | The total number of entries returned. |
| totalPage | Integer | 10 | The total number of pages returned. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListResourceGroupByOrgId &Id=34 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <data>
    <organizationID>1</organizationID>
    <gmtModified>1607512443999</gmtModified>
    <creator>admin</creator>
    <resourceGroupName>test</resourceGroupName>
    <organizationName>admin</organizationName>
    <gmtCreated>1607512443989</gmtCreated>
    <resourceGroupType>1</resourceGroupType>
    <id>1</id>
</data> <success>true</success> <pageInfo>
    <total>100</total>
    <totalPage>10</totalPage>
    <pageSize>10</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>true</pureListData> <message> 200</message>
```

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
            "gmtModified": "1607512443999",
            "creator": "admin",
            "resourceGroupName": "test",
            "organizationName": "admin",
            "gmtCreated": "1607512443989",
            "resourceGroupType": "1",
            "id": "1"
```

`}` `],`

```json
    "success": "true",
    "pageInfo": {
        "total": "100",
        "totalPage": "10",
        "pageSize": "10",
        "currentPage": "1"
```

`},`

```json
    "pureListData": "true",
    "message": " 200"
```

`}`

###### 4.3.1.1.7 CreateOrganization

Creates an organization.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/organization/add HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| name | String | Body | No | ascm-test | The name of the organization. Note This parameter is required. |

| parentId | Integer | Body | No | 1 | The ID of the parent organization. Note The ID of the root organization is 1. This parameter is required. |
|---|---|---|---|---|---|
| orgParentUuid | String | Body | No | org- 101bbf866a93 0ae6******** | The UUID of the parent organization. |
| orgUuid | String | Body | No | org- 101bbf866a93 0ae6******** | The UUID of the organization. The system automatically generates a value for this parameter. |
| multiCloudStat us | String | Body | No | null | The multi-cloud status of the organization. Default value: null. master: The organization is a primary-cloud organization. slave: The organization is a secondary-cloud organization. null. |
| extraInfo | String | Body | No | null | The additional information. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The organization name is left empty. The ID of the parent organization is left empty. The parent organization does not exist. The AccessKey pair is invalid. One or more parameters are invalid. 403: You do not have permissions. 500: A remote call error occurred. An internal error occurred. |
|---|---|---|---|
| cost | Integer | 10000 | The time consumed by the operation. Unit: milliseconds. Note If the time consumed between the request and the response of an operation called by using the ASAPI gateway exceeds 10 seconds, the operation times out. |
| data | Struct |   | The response data. |
| alias | String | test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The username of the user who created the organization. |
| extraInfo | String | null | The additional information. |
| id | Integer | 1 | The ID of the organization. |

| internal | Boolean | false | Indicates whether the organization is a preset organization. Note The system automatically generates a preset organization, which is also named the default organization. |
|---|---|---|---|
| level | String | 0.1 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the parent organization ID (root organization ID) of the organization is 1. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
| mtime | Long | 1606791494471 | The time when the organization was last modified. Note In the scenario in which you create an organization, the system returns the same value for the mtime and ctime parameters. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary- cloud organization. slave: The organization is a secondary- cloud organization. This parameter is returned only in multi- cloud scenarios. |
| muserId | String | admin | The username of the user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. Note The ID of the root organization is 1. |

| supportRegion List | List | ["cn-qingdao- env17-d01"] | The list of zones. Note This parameter takes effect only for level-1 organizations. If a level-1 organization is created, the ID of the central region is returned for this parameter. If a level-2 organization or its subordinate organization is created, no value is returned for this parameter. |
|---|---|---|---|
| supportRegion s | String | cn-qingdao-env17- d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |
| message | String | success | The message. Examples: success: The call is successful. Can't find user by specified accessKey: No users are found by using the AccessKey pair. Caller is not the parent of user: xxx: You do not have sufficient permissions. Calling manage returns empty body: No results are returned for the call. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59- ****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateOrganization &Name=ascm-test &ParentId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <internal>true</internal>
    <level>0.1</level>
    <supportRegions>cn-qingdao-****-d01</supportRegions>
    <mtime>1606791494471</mtime>
    <uuid>1231</uuid>
    <parentId>1</parentId>
    <multiCloudStatus>master</multiCloudStatus>
    <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
    <name>test</name>
    <ctime>1606791494471</ctime>
    <alias>test</alias>
    <id>1</id>
    <cuserId>admin</cuserId>
</data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "data": {
        "muserId": "admin",
        "internal": "true",
        "level": "0.1",
        "supportRegions": "cn-qingdao-****-d01",
        "mtime": "1606791494471",
        "uuid": "1231",
        "parentId": "1",
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
    "success": "true",
    "requestId": "16d09b14-8a59-****-****-7536fe897b66",
    "pureListData": "true",
    "message": "success"
```

`}`

**4.3.1.1.8.**

###### GetPrivateCloudAccountByOrganizationId

Queries an Apsara Stack tenant account with which a level-1 organization is associated.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/getPrivateCloudAccountByOrganizationId HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| OrganizationId | Integer | Body | Yes | 1 | The ID of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Struct |   | The response data. |
| aliyunid | String | 1 | The ID of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <aliyunid>1</aliyunid>
    <primaryKey>212530506704030466</primaryKey>
</data> <success>true</success> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"aliyunid":"1","primaryKey":"212530506704030466"},"success":"true","pureListData":"true" message":"success"}
```

##### 4.3.1.2 Resource sets

###### 4.3.1.2.1 CreateResourceGroup

Creates a resource set.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/create_resource_group HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| organization i _ d | Integer | Body | No | 3 | The ID of the organization. Note This parameter is required. |
| resource grou _ p name _ | String | Body | No | testrs | The name of the resource set. The name must be 2 to 50 characters in length. Note This parameter is required. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The name of the resource set is empty. The ID of the organization is empty. The resource set cannot be created in a root organization. The organization does not exist. The AccessKey pair is invalid. One or more parameters are invalid. 403: You do not have permissions. 404: The AccessKey pair does not exist. The organization does not exist. The user does not exist. The AccessKey pair of the organization does not exist. 500: A remote call error occurred. An internal error occurred. |
|---|---|---|---|
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Struct |   | The response data. |
| creator | String | admin | The username of the user who created the resource set. |
| gmtCreated | Long | 1607512443989 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization to which the resource set belongs. Note The ID of the root organization is 1. |

| resourceGroup Name | String | test | The name of the resource set. The value is the same as the value of the resource group name request parameter. _ _ |
|---|---|---|---|
| rsId | String | rs- 1010e71e5e520aa b******** | The UUID of the resource set. |
| message | String | 200 | The message. Examples: Can't find user by specified accessKey: The AccessKey pair does not exist. Caller is not the parent of user: xxx: You do not have sufficient permissions. Calling manage returns empty body: No results are returned for the call. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59- ****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateResourceGroup &organization_id=3 &resource_group_name=testrs &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <data>
    <organizationID>1</organizationID>
    <resourceGroupName>test</resourceGroupName>
    <gmtCreated>1607512443989</gmtCreated>
    <rsId>rs-1010e71e5e520aab********</rsId>
    <id>1</id>
</data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "data": {
        "organizationID": "1",
        "resourceGroupName": "test",
        "gmtCreated": "1607512443989",
        "rsId": "rs-1010e71e5e520aab********",
        "id": "1"
```

`},`

```json
    "success": "true",
    "requestId": "16d09b14-8a59-****-****-7536fe897b66",
    "message": "200"
```

`}`

###### 4.3.1.2.2 UnbindAscmUserAndResourceGroup

Unbinds one or more users from a resource set.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/remove_ascm_users HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|

| resource grou _ p id _ | Integer | Body | No | 7 | The ID of the resource set. Note This parameter is required. |
|---|---|---|---|---|---|
| ascm user ids _ _ | String | Body | No | "[5017,5023]" | The IDs of the users that you want to unbind from the resource set. Separate multiple user IDs with commas (,). Note This parameter is required. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 400: One or more parameters are invalid. The operation is not supported by a RAM user. 403: You do not have permissions. You do not have the permissions to manage the resoure set. You cannot call the operation to unbind your account from the resource set. 404: The resource set does not exist. The AccessKey pair does not exist. The role does not belong to your account. The user does not exist. The role does not exist. 500: An internal error occurred. 511: The maximum number of users that can be bound to a resource set is exceeded. |

| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
|---|---|---|---|
| message | String | 200 | The message. Examples: An internal error occurred. User and resource set must be in the same top organization: The user and the resource set are not in the same level-1 organization. Invalid ascmRoleId or ascmUserId: The ID of the role or user is invalid. The role is not exist: xxx: The role does not exist. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UnbindAscmUserAndResourceGroup &AscmUserIds="[5017,5023]" &ResourceGroupId=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "success": "true",
    "message": "200"
```

`}`

###### 4.3.1.2.3 UpdateResourceGroup

Updates a resource set.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/update_resource_group HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| id | String | Body | No | 16 | The ID of the resource set that you want to update. Note This parameter is required. |
| resourceGroup Name | String | Body | No | new res _ | The new name of the resource set that you want to update. The name must be 2 to 50 characters in length. Note This parameter is required. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The AccessKey pair is invalid. You cannot call the operation for the default resource set. Before you delete a resource set, you must unbind all user groups from the resource set. Before you delete a resource set, you must delete all cloud resources from the resource set. Before you delete a resource set, you must unbind all users from the resource set. One or more parameters are invalid. 403: You do not have permissions. 404: The AccessKey pair does not exist. The organization does not exist. The user does not exist. The AccessKey pair of the organization does not exist. 500: A remote call error occurred. An internal error occurred. |
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Struct |   | The response data. |
| creator | String | admin | The username of the user who created the resource set. |
| gmtCreated | Float | 1653485365361 | The time when the resource set was created. |
| gmtModified | Float | 1653485365362 | The time when the resource set was last updated. |

| id | Integer | 3 | The ID of the resource set. The ID is the same as the value that is specified for the id request parameter. |
|---|---|---|---|
| organizationID | Integer | 2 | The ID of the organization to which the resource set belongs. |
| organizationN ame | String | ascm-test | The name of the organization to which the resource set belongs. |
| resourceGroup Name | String | new res _ | The new name of the resource set that is updated. The name is the same as the value that is specified for the resourceGroupName request parameter. |
| resourceGroup Type | Integer | 1 | The type of the resource set. 0: The resource set is not the default resource set. 1: The resource set is the default resource set. |
| message | String | success | The message. Examples: success: The call is successful. Can't find user by specified accessKey: No user is found by using the AccessKey pair. Caller is not the parent of user: xxx: You do not have sufficient permissions. Calling manage returns empty body: No results are returned for the call. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateResourceGroup &id=16 &resource_group_name=new_res &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <pageInfo>
    <gmtModified>1606791494471</gmtModified>
    <resourceGroupName>new_res</resourceGroupName>
    <id>1</id>
</pageInfo> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "success": "true",
    "pageInfo": {
        "gmtModified": "1606791494471",
        "resourceGroupName": "new_res",
        "id": "1"
```

`},`

```json
    "message": "success"
```

`}`

###### 4.3.1.2.4 RemoveResourceGroup

Deletes a resource set.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/delete_resource_group HTTP/1.1
```

**Request parameters**

| > Document Versi | on: 20251 | 106 |   |   | 12 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| resource grou _ p id _ | Integer | Body | No | 5 | The ID of the resource set that you want to delete. If you leave this parameter empty, the response is empty. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The AccessKey pair is invalid. You cannot call the operation for the default resource set. Before you delete a resource set, you must unbind all user groups from the resource set. Before you delete a resource set, you must delete all cloud resources from the resource set. Before you delete a resource set, you must unbind all users from the resource set. One or more parameters are invalid. 403: You do not have permissions. 404: The AccessKey pair does not exist. The organization does not exist. The user does not exist. The AccessKey pair of the organization does not exist. 500: A remote call error occurred. An internal error occurred. |
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |

| message | String | success | The message. Examples: success: The call is successful. Can't find user by specified accessKey: No user is found by using the AccessKey pair. Caller is not the parent of user: xxx: You do not have sufficient permissions. Calling manage returns empty body: No results are returned for the call. |
|---|---|---|---|
| pureListData | Integer | 0 | Indicates whether only data is returned and other parameters are not returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| requestId | String | 16d09b14-8a59- ****-****- 7536fe897b66 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveResourceGroup &resource_group_id=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "success": "true",
    "requestId": "16d09b14-8a59-****-****-7536fe897b66",
    "message": "success"
```

`}`

###### 4.3.1.2.5 ListResourceGroup

Queries the list of resource sets that are visible to your account.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/list_resource_group HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| resourceGroup Name | String | Body | No | test | The name of the resource set that you want to query. If you specify only the organizationId parameter, the system returns resource sets that belong to the relevant organization and are visible to your account. If you specify only the resourceGroupName parameter, the system returns resource sets whose names contain the specified resource set name and that are visible to your account. |

| organizationId | Integer | Body | No | 1 | The ID of the organization. Note You can use this parameter to query the list of resource sets in the specified organization, excluding its subordinate organizations. If you leave this parameter empty or set this parameter to 1, the system returns the list of all resource sets that are visible to your account. |
|---|---|---|---|---|---|
| pageNumber | Integer | Body | No | 1 | The number of the page to return. Default value: 1. |
| pageSize | Integer | Body | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| Total | Integer | 10 | The total number of entries returned. |
| TotalPage | Integer | 1 | The total number of pages returned. |
| code | String | 200 | The HTTP status code. 200: The call is successful. 403: You do not have permissions. |

| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
|---|---|---|---|
| data | Array of dataItem |   | The response data. |
| creator | String | admin | The username of the user who created the resource set. |
| gmtCreated | Float | 1606719003858 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization to which the resource set belongs. |
| organizationN ame | String | test | The name of the organization to which the resource set belongs. |
| resourceGroup Name | String | test | The name of the resource set. |
| rsId | String | rs- 1010e71e5e520aa b******** | The UUID of the resource set. |
| message | String | success | The message. success: The call is successful. The caller is not organization account: You do not have permissions. |
| pureListData | Boolean | true | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |

| success | Boolean | true | Indicates whether the call is successful. true false |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListResourceGroup &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <PageInfo>
    <TotalPage>1</TotalPage>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <Total>10</Total>
</PageInfo> <cost>10000</cost> <code>200</code> <data>
    <organizationID>1</organizationID>
    <creator>admin</creator>
    <resourceGroupName>test</resourceGroupName>
    <organizationName>test</organizationName>
    <gmtCreated>1606719003858</gmtCreated>
    <rsId>rs-1010e71e5e520aab********</rsId>
    <id>1</id>
</data> <success>true</success> <message>success</message>
```

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
            "rsId": "rs-1010e71e5e520aab********",
            "id": "1"
```

`}` `],`

```json
    "success": "true",
    "message": "success"
```

`}`

###### 4.3.1.2.6 BindAscmUserAndResourceGroup

Binds users to a resource set.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/add_ascm_users HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| resource grou _ p id _ | Integer | Body | No | 7 | The ID of the resource set. Note If you leave the resource group id and _ _ ascm role id parameters _ _ empty or specify only one of the parameters, an error is reported. |

| ascm user ids _ _ | String | Body | No | "[5017,5023]" | The IDs of the users that you want to bind. Separate multiple user IDs with commas (,). |
|---|---|---|---|---|---|
| ascm role id _ _ | Integer | Body | No | 1 | The ID of the role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. 200: The call is successful. 400: The maximum number of users that can be bound to the resource set at a time is exceeded. The maximum number of resource sets to which a user can be bound is exceeded. One or more parameters are invalid. The operation is not supported by RAM roles. 403: You do not have permissions. You do not have the permissions to manage the resource set. You cannot call the operation for your account. 404: The resource set does not exist. The AccessKey pair does not exist. The role does not belong to you. The user does not exist. The role does not exist. 500: An internal error occurred. 511: The maximum number of users that can be bound to a resource set is exceeded. |
| cost | Integer | 10000 | The time consumed by the operation. Unit: milliseconds. Note If the time consumed between the request and the response of an operation called by using the ASAPI gateway exceeds 10 seconds, the operation times out. |

| message | String | success | The message. Examples: success: The call is successful. An internal error occurred. User and resource set must be in the same top organization: The user and the resource set are not in the same level-1 organization. invalid ascmRoleId or ascmUserId: The ID of the role or user is invalid. the role is not exist: xxx: The role does not exist. |
|---|---|---|---|
| pureListData | Integer | 0 | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | true | Indicates whether the request is redirected. true false |
| success | Boolean | true | Indicates whether the call is successful. true false |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=BindAscmUserAndResourceGroup &ascm_user_ids="[5017,5023]" &resource_group_id=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "success": "true",
    "message": "success"
```

`}`

###### 4.3.1.2.7 ListAscmUsersInsideResourceGroup

Queries the list of users in a resource set.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/resource_group/list_ascm_users HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| resourceGroup Id | Integer | Body | No | 7 | The ID of the resource set. If you leave this parameter empty, the response is empty. |
| currentPage | Integer | Body | No | 1 | The number of the page to return. Default value: 1. |
| pageSize | Integer | Body | No | 10 | The number of entries to return on each page. |
| loginName | String | Body | No | admin | The logon name of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. 200: The call is successful. 400: One or more parameters are invalid. 403: You do not have permissions. 404: The AccessKey pair does not exist. The user does not exist. 500: An internal error occurred. |
|---|---|---|---|
| cost | Integer | 10000 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Array of dataItem |   | The response data. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p******** | The AccessKey ID of the user. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | 1 | The ID of the user who created the AccessKey pair. |
| id | Integer | 1 | The primary key of the AccessKey pair. |
| region | String | cn-qingdao-****- d01 | The zone in which the AccessKey pair available. |
| status | String | ACTIVE | The state of the AccessKey pair. active: The AccessKey pair is active. deactive: The AccessKey pair is inactive. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |

| default | Boolean | false | Indicates whether the user is a preset user. true false Note Preset users are automatically created by the system. |
|---|---|---|---|
| defaultRole | Struct |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. Note This parameter is deprecated. |
| arId | String | 111 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | defaultRole.operati onAdmin.descriptio n | The description of the role. |
| enable | Boolean | true | Indicates whether the role is disabled. true false |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The username of the user who created the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. The value organizationVisibility.global specifies that the role is globally shared. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |

| roleLevel | Integer | 11321 | The level of the role. Note This parameter is deprecated. |
|---|---|---|---|
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.allOrganizations: The role has management permissions on all organizations. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The name of the user. |
| loginPolicy | Struct |   | The logon policy. |

| cuserId | String | admin | The username of the user who created the logon policy. |
|---|---|---|---|
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The CIDR blocks that are defined in the logon policy. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPv4 | The protocol that is defined in the logon policy. Note Only IPv4 is supported. |
| lpId | String | 111 | The UUID of the logon policy. |
| muserId | String | admin | The username of the user who created the logon policy. |
| name | String | deafult.loginpolicy | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |

| rule | String | ALLOW | The type of the logon policy. Allow: whitelist Deny: blacklist |
|---|---|---|---|
| timeRanges | Array of timeRange |   | The logon time ranges that are defined in the logon policy. |
| endTime | String | 24:00 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range queried. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. The system automatically generates an alias that is the same name as the organization name. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The username of the user who created the organization. |
| id | Integer | 1 | The ID of the organization to which the user belongs. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. Note The system automatically generates a preset organization, which is also named the default organization. |

| level | String | 0.1 | The level of the organization. Note The level of the root organization is 0, and the levels of level-1 organizations are 0.1. 1 in 0.1 indicates that the ID of the parent organization of level-1 organizations is 1. In this case, the parent organization is the root organization. All levels follow the same rule. For example, if the ID of a level-1 organization is 3, the level of its subordinate organization is 0.1.3. |
|---|---|---|---|
| mtime | Long | 1606791494472 | The time when the organization was last modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. master: The organization is a primary- cloud organization. slave: The organization is a secondary- cloud organization. Note This parameter is returned only in multi-cloud scenarios. |
| muserId | String | admin | The username of the user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao- env17-d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-env17- d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |

| parentPk | String | 1689406703****** | The primary key of the Apsara Stack tenant account. The primary key is used as the UID of the account. Note The primary key is the same as the UID of the Apsara Stack tenant account on the Users page in the Apsara Uni-manager Management Console. |
|---|---|---|---|
| primaryKey | String | 212530506704**** ** | The primary key of the RAM user. The primary key is used as the UID of the RAM user. Note The primary key is the same as the RAM user on the Users page in the Apsara Uni-manager Management Console. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. Note This parameter is deprecated. |
| arId | String | 111 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. Preset roles are automatically created by the system. true false |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is disabled. true false |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The username of the user who created the role. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. The value organizationVisibility.global specifies that the role is globally shared. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. Note This parameter is deprecated. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.allOrganizations: The role has management permissions on all organizations. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| status | String | active | The state of the AccessKey pair. active: The AccessKey pair is active. deactive: The AccessKey pair is inactive. |
| userGroupRole s | List | admin | The list of roles for the user group. |
| userGroups | List | admin | The list of user groups. |
| userRoles | Array of userRole |   | The list of roles for the user. |

| active | Boolean | true | Indicates whether the role is valid. Note This parameter is deprecated. |
|---|---|---|---|
| arId | String | 1121 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The username of the user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The username of the user who last modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. The value organizationVisibility.global specifies that the role is globally shared. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization to which the role belongs. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1123 | The level of the role. Note This parameter is deprecated. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. The name can be up to 64 characters in length. |

| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.allOrganizations: The role has management permissions on all organizations. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| message | String | success | The message. success: The call is successful. User has no permission to access the resource set: The user does not have permissions to access the resource set. |
| pageInfo | Struct |   | The pagination information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 10 | The number of entries returned per page. |
| total | Integer | 10 | The total number of entries returned. |
| totalPage | Integer | 10 | The total number of pages returned. |
| pureListData | Integer | 0 | Indicates whether only data is returned. Note This parameter is deprecated. |
| redirect | Boolean | false | Indicates whether the request is redirected. true false |
| requestId | String | 0ba87292-fd63- ****-****- c4f975b84cd0 | The ID of the request. |

| success | Boolean | true | Indicates whether the call is successful. true false |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListAscmUsersInsideResourceGroup &ResourceGroupId=7 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <code>200</code> <cost>49</cost> <data>
    <cellphoneNum>13813800138</cellphoneNum>
    <defaultRole>
        <roleRange>roleRange.resourceSet</roleRange>
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
    </defaultRole>
    <displayName>asapibaixue1</displayName>
    <enableDingTalk>true</enableDingTalk>
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
```

```xml
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
            <protocol>IPv4</protocol>
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
    <parentPk>1824191931******</parentPk>
```

`<l` `tL`

```
iTi >1592232390657</l
```

`tL`

```
iTi
```

`>`

```xml
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
```

```xml
        <id>609</id>
        <region>cn-qingdao-****-d01</region>
        <accesskeyId>1KAjDIqCGM******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>asapibaixue1</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
        <name>asapi_test</name>
        <alias>asapi_test</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
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
    <primaryKey>261424091942******</primaryKey>
    <status>ACTIVE</status>
</data> <data>
    <cellphoneNum>18999999999</cellphoneNum>
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
        <code>ROLEYUNDUNORGSECADMIN</code>
```

`_` `_` `_` `_` `/`

```xml
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
    <parentPk>1824191931******</parentPk>
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
        <region>cn-qingdao-****-d01</region>
```

```xml
        <cuserId>admin</cuserId>
        <accesskeyId>o4LEJ8SoW******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>asapitest</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
        <name>asapi_test</name>
        <alias>asapi_test</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
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
    <primaryKey>250944791941*****</primaryKey>
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
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
```

```xml
    <parentPk>1824191931******</parentPk>
    <accessKeys>
        <ctime>1591931388000</ctime>
        <id>608</id>
        <region>cn-qingdao-****-d01</region>
        <accesskeyId>cNaeitV1RB******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>asapibaixue</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
        <name>asapi_test</name>
        <alias>asapi_test</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
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
    <primaryKey>221543391942******</primaryKey>
    <status>ACTIVE</status>
</data> <success>true</success> <pageInfo>
    <total>3</total>
    <totalPage>1</totalPage>
    <pageSize>10</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": false,
    "code": "200",
    "cost": 49,
    "data": [
```

`{`

```json
        "cellphoneNum": "13813800138",
        "defaultRole": {
          "roleRange": "roleRange.resourceSet",
```

```json
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

`},`

```json
        "displayName": "asapibaixue1",
        "enableDingTalk": true,
        "roles": [
```

`{`

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
```

```json
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "id": 2,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
```

`}` `],`

```json
        "loginPolicy": {
          "ipRanges": [
```

`{`

```json
              "protocol": "IPv4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
```

`}` `],`

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

`}` `],`

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
        "parentPk": "1824191931******",
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
```

```json
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

`}` `],`

```json
        "accessKeys": [
```

`{`

```json
            "ctime": 1591931519000,
            "id": 609,
            "region": "cn-qingdao-****-d01",
            "accesskeyId": "1KAjDIqCGM******",
            "status": "ACTIVE"
```

`}` `],`

```json
        "default": false,
        "deleted": false,
        "loginName": "asapibaixue1",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
"cnqingdao****d01"
```

```
            "cn-qingdao-****-d01"
```

`],`

```json
          "level": "0.1",
          "name": "asapi_test",
          "alias": "asapi_test",
          "supportRegions": "cn-qingdao-****-d01",
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
        "primaryKey": "261424091942******",
        "status": "ACTIVE"
```

`},` `{`

```json
        "cellphoneNum": "18999999999",
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
          "organizationVisibility": "organizationVisibility.global"
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
"roleLevel":2147483647,
```

```json
            roleLevel: 2147483647,
            "organizationVisibility": "organizationVisibility.global"
```

`}` `],`

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

`}` `],`

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

`}` `],`

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
        "parentPk": "1824191931******",
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

`}` `],`

```json
        "accessKeys": [
```

`{`

```json
            "ctime": 1591930977000,
            "id": 607,
            "region": "cn-qingdao-****-d01",
```

`g` `q` `g` `,`

```json
            "cuserId": "admin",
            "accesskeyId": "o4LEJ8SoW******",
            "status": "ACTIVE"
```

`}` `],`

```json
        "default": false,
        "deleted": false,
        "loginName": "asapitest",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-****-d01"
```

`],`

```json
          "level": "0.1",
          "name": "asapi_test",
          "alias": "asapi_test",
          "supportRegions": "cn-qingdao-****-d01",
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
        "primaryKey": "250944791941*****",
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

`}` `],`

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

`}` `],`

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
        "parentPk": "1824191931******",
        "userGroups": [],
        "userRoles": [],
        "accessKeys": [
```

`{`

```json
            "ctime": 1591931388000,
            "id": 608,
            "region": "cn-qingdao-****-d01",
            "accesskeyId": "cNaeitV1RB******",
            "status": "ACTIVE"
```

`}` `],`

```json
        "default": false,
        "deleted": false,
        "loginName": "asapibaixue",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-****-d01"
```

`],`

```json
          "level": "0.1",
          "name": "asapi_test",
          "alias": "asapi_test",
          "supportRegions": "cn-qingdao-****-d01",
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
        "primaryKey": "221543391942******",
        "status": "ACTIVE"
```

`}` `],`

```json
    "success": true,
    "pageInfo": {
      "total": 3,
      "totalPage": 1,
      "pageSize": 10,
```

```json
      "currentPage": 1
```

`},`

```json
    "pureListData": false,
    "message": "success"
```

`}`

##### 4.3.1.3 Roles

###### 4.3.1.3.1 SetDefaultRole

Sets a default role.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect":"false",
    "cost":"1000",
    "code":"200",
    "success":"true",
    "pureListData":"false",
    "message":"success"
```

`}`

###### 4.3.1.3.2 ListRoles

Queries the list of available roles of a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListRoles | The operation that you want to perform. Set the value to ListRoles. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| IsDefault | Boolean | No | true | Specifies whether the role is a built- in role. |

| RoleType | String | No | ROLETYPE ASC _ M | The type of the role. Valid values: ROLETYPE RAM: the Resource _ Access Management (RAM) role ROLETYPE ASCM: the custom role _ |
|---|---|---|---|---|
| RoleName | String | No | defaultRole.orga nizationAdmin.n ame | The name of the role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-9999999902 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | defaultRole.resourc eUser.description | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The organization to which the role belongs. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2147483647 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM: the RAM role _ ROLETYPE ASCM: the custom role _ |
| userCount | Integer | 12 | The number of users. |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |

| total | Integer | 2 | The total number of entries returned. |
|---|---|---|---|
| totalPage | Integer | 39 | The total number of pages. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListRoles &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <roleRange>roleRange.orgAndSubOrgs</roleRange>
    <rAMRole>false</rAMRole>
    <muserId>admin</muserId>
    <arId>ar-9999999902</arId>
    <code>ROLE_RESOURCE_USER</code>
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

`JSON` format `{`

```json
    "redirect": false,
    "cost": 1000,
    "code": 200,
    "data": {
        "roleRange": "roleRange.orgAndSubOrgs",
        "rAMRole": false,
        "muserId": "admin",
        "arId": "ar-9999999902",
        "code": "ROLE_RESOURCE_USER",
        "description": "defaultRole.resourceUser.description",
        "active": true,
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "userCount": 12,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.resourceUser.name",
        "roleLevel": 2147483647,
        "id": 1,
        "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
    "success": true,
    "pageInfo": {
        "total": 2,
        "totalPage": 39,
        "pageSize": 20,
        "currentPage": 1
```

`},`

```json
    "pureListData": false,
    "message": "success"
```

`}`

###### 4.3.1.3.3 ListActiveRoles

Queries the list of roles that can be bound.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListActiveRoles | The operation that you want to perform. Set the value to ListActiveRoles. |
| IncludeRAMRole s | Boolean | No | false | Specifies whether to include Resource Access Management (RAM) roles. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-9999999902 | The ID of the role. |
| code | String | 200 ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | defaultRole.resourc eUser.description | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The organization to which the role belongs. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2147483647 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": [
```

`{`

```json
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": "false",
            "arId": "ar-9999999902",
            "code": "200 ROLE_RESOURCE_USER",
            "description": "defaultRole.resourceUser.description",
            "active": "true",
            "roleType": "ROLETYPE_ASCM",
            "default": "true",
            "userCount": "12",
            "ownerOrganizationId": "1",
            "enable": "true",
            "roleName": "defaultRole.resourceUser.name",
            "roleLevel": "2147483647",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global"
```

`}` `],`

```json
    "success": "true",
    "pageInfo": {
        "total": "2",
        "totalPage": "39",
        "pageSize": "20",
        "currentPage": "1"
```

`},`

```json
    "pureListData": "false",
    "message": "success"
```

`}`

##### 4.3.1.4 Users

###### 4.3.1.4.1 AddUser

Creates a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddUser | The operation that you want to perform. Set the value to AddUser. |
| CellphoneNum | String | Yes | 10000000000 | The mobile number of the user. |

| DisplayName | String | Yes | testuser | The display name of the user. |
|---|---|---|---|---|
| Email | String | Yes | a***@a.com | The email address of the user. |
| LoginName | String | Yes | testu | The logon name of the user. |
| LoginPolicyId | Integer | Yes | 1 | The ID of the logon policy. |
| MobileNationCod e | String | Yes | 86 | The country code. |
| OrganizationId | Integer | Yes | 5 | The ID of the organization. |
| roleIdList | Json | No | {"RoleIdList": [ "5", "6", "8" ]} | The list of role IDs. |
| OrganizationUui d | String | No | 1223 | The UUID of the organization. |
| TelephoneNum | String | No | 00000000 | The telephone number. |
| DingTalkToken | String | No | 12345abc | The DingTalk token. |
| EnableDingTalk | Boolean | No | false | Specifies whether to use DingTalk to send notifications. |
| EnableShortMes sage | Boolean | No | false | Specifies whether to use SMS to send notifications. |
| EnableEmail | Boolean | No | false | Specifies whether to use emails to send notifications. |
| MultiCloudStatus | String | No | master | Specifies whether the user is a multi- cloud user. Valid values: master and slave. master indicates a primary- cloud user. slave indicates a secondary-cloud user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |

| cost | Integer | 1000 | The amount of time taken to perform the operation. |
|---|---|---|---|
| data | Struct |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID of the user. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| id | Integer | 1 | The ID of the AccessKey pair. |
| region | String | cn-qingdao-****- d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |

| loginName | String | test | The logon name of the user. |
|---|---|---|---|
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
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |

| timeRanges | Array of timeRange |   | The list of time ranges. |
|---|---|---|---|
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range for the query. |
| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the Resource Access Management (RAM) user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRole s | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |

| cuserId | String | admin | The user who created the role. |
|---|---|---|---|
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
|---|---|---|---|
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 11213 | The ID of the user group. |
| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
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
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |

| muserId | String | admin | The user who modified the organization. |
|---|---|---|---|
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 1231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| rsId | String | 12312a | The ID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1231 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |

| default | Boolean | true | Indicates whether the role is a preset role. |
|---|---|---|---|
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1231 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |

| users | Array of user |   | The list of users. |
|---|---|---|---|
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | RamUser | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |

|   |   |   | a Uni-manager Management Co sole API Referenc |
|---|---|---|---|

| loginName | String | test | The logon name of the user. |
|---|---|---|---|
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8**** | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1121 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |

| id | Integer | 1 | The ID of the role. |
|---|---|---|---|
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1123 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |

| redirect | Boolean | false | Indicates whether redirections are performed. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddUser &CellphoneNum=10000000000 &DisplayName=testuser &Email=a***@a.com &LoginName=testu &LoginPolicyId=1 &MobileNationCode=86 &OrganizationId=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <code>200</code> <cost>5542</cost> <data>
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
```

```xml
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
```

```xml
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
```

```xml
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
```

`<d`

```
iti >df ltRl
```

`d`

```
GlblO
```

`S`

```
Adit
```

`d`

```
iti </d iti
```

`>`

```xml
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
```

```xml
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
```

`/`

```xml
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
        <active>true</active>
        <description>defaultRole.yundunGlobalOrgAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunGlobalOrgAdmin.name</roleName>
```

```xml
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
```

```xml
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
```

`tR` `i` `i` `d`

```
****d01/
```

`tR` `i`

```xml
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

`JSON` format `{`

```json
  "redirect": false,
  "code": "200",
  "cost": 5542,
  "data": {
    "cellphoneNum": "13269752565",
    "displayName": "csblcl",
    "enableDingTalk": true,
    "roles": [
```

`{`

```json
        "roleRange": "roleRange.allOrganizations",
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
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.allOrganizations",
        "rAMRole": false,
        "code": "ROLE_YUNDUN_PLATSECCONF_ADMIN",
        "active": true,
        "description": "defaultRole.yundunPlatSecConfAdmin.description",
        "roleType": "ROLETYPE_ASCM",
        "default": true,
        "ownerOrganizationId": 1,
        "enable": true,
```

```json
        "roleName": "defaultRole.yundunPlatSecConfAdmin.name",
        "id": 15,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

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
```

```json
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
"organiationVisibilit" "organiationVisibilit global"
```

```json
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
"default":true,
```

```json
        default: true,
        "ownerOrganizationId": 1,
        "enable": true,
        "roleName": "defaultRole.yundunGlobalOrgSecAuditor.name",
        "id": 13,
        "roleLevel": 2147483647,
        "organizationVisibility": "organizationVisibility.global"
```

`}` `],`

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

`}` `],`

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

`}` `],`

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
        "cuserId": "",
        "organizationVisibility": "organizationVisibility.global"
```

`},` `{`

```json
        "roleRange": "roleRange.orgAndSubOrgs",
        "muserId": "",
        "rAMRole": false,
```

```json
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
```

```json
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
```

`"`

```
bl"
```

`t`

```json
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

`}` `],`

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

`}` `],`

```json
    "default": false,
    "deleted": false,
"loginName":"csbuser"
```

```json
    loginName: csbuser,
    "organization": {
      "muserId": "",
      "internal": false,
      "supportRegionList": [
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

`}`

###### 4.3.1.4.2 AddRoleToUser

Binds a role to a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddRoleToUser | The operation that you want to perform. Set the value to AddRoleToUser. |
| LoginName | String | Yes | test | The logon name of the user. |
| RoleId | Integer | Yes | 3 | The ID of the role. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.3 ResetPasswordByLoginName

Resets the password of a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetPasswordB yLoginName | The operation that you want to perform. Set the value to ResetPasswordByLoginName. |
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>sucess</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "sucess"
```

`}`

###### 4.3.1.4.4 GetLoginPolicyByLoginName

Queries the logon policy that is bound to a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetLoginPolicyB yLoginName | The operation that you want to perform. Set the value to GetLoginPolicyByLoginName. |
| LoginName | String | Yes | testu | The logon name of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| cuserId | String | admin | The creator of the logon policy. |

| default | Boolean | true | Indicates whether the logon policy is the default one. |
|---|---|---|---|
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | defaultLoginPolicy. name | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |

| loginPolicyId | Integer | 1 | The ID of the logon policy. |
|---|---|---|---|
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
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
    <name>defaultLoginPolicy.name</name>
    <rule>ALLOW</rule>
    <id>1</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
    <lpId>111</lpId>
    <cuserId>admin</cuserId>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "ipRanges": [
```

`{`

```json
                "ipRange": "0.0.0.0/0",
                "protocol": "IPV4",
                "loginPolicyId": "1"
```

`}` `],`

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

`}` `],`

```json
        "enable": "true",
        "name": "defaultLoginPolicy.name",
        "rule": "ALLOW",
        "id": "1",
        "organizationVisibility": "organizationVisibility.global",
        "lpId": "111",
        "cuserId": "admin"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.5 UpdatePassword

Modifies a password.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdatePassword | The operation that you want to perform. Set the value to UpdatePassword. |

| NewPassword | String | Yes | QAZ2wsx | The new password. The password must comply with the password policy specified by the administrator in the Apsara Uni-manager Operations Console. |
|---|---|---|---|---|
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.6 RemoveUserByLoginName

Deletes a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveUserByL oginName | The operation that you want to perform. Set the value to RemoveUserByLoginName. |
| LoginName | String | Yes | testu | The logon name of the user. |
| MultiCloudStatus | String | No | master | Specifies whether the user is a multi- cloud user. Valid values: master and slave. master indicates a primary- cloud user. slave indicates a secondary-cloud user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |

| success | Boolean | true | Indicates whether the call is successful. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveUserByLoginName &LoginName=testu &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.7 GetUserInfo

Queries the information of a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetUserInfo | The operation that you want to perform. Set the value to GetUserInfo. |
| LoginName | String | No | testu | The logon name of the user. |
| UserAccessKeyId | String | No | test | The AccessKey ID of the user. |

| Pk | String | No | 2793198889999 90000 | The primary key of the user. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
| accesskeySecr et | String | ************** | The AccessKey secret. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | 1 | The user who created the AccessKey pair. |
| id | Integer | 1 | The ID of the AccessKey pair. |
| region | String | cn-qingdao-****- d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |

| arId | String | 111 | The ID of the role. |
|---|---|---|---|
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 11123 | The level of the role. |
| roleName | String | role test _ | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications are sent by DingTalk. |
| enableEmail | Boolean | false | Indicates whether notifications are sent by email. |
| enableShortM essage | Boolean | false | Indicates whether notifications are sent by SMS. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1132111 | The most recent logon time. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |

| enable | Boolean | true | Indicates whether the logon policy is valid. |
|---|---|---|---|
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | default.loginpolicy | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |

| mobileNationC ode | String | 86 | The country code. |
|---|---|---|---|
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1622311 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 15123222 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 123331 | The universally unique identifier (UUID) of the organization. |

| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
|---|---|---|---|
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |

| roleName | String | role test _ | The name of the role. |
|---|---|---|---|
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRole s | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 11213 | The ID of the user group. |
| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | group-test | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |

| organization | Struct |   | The information of the organization. |
|---|---|---|---|
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 1231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |

| creator | String | admin | The creator of the resource set. |
|---|---|---|---|
| gmtCreated | Long | 1606791494471 | The time when the storage set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| rsId | String | 123121a | The ID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1231 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |

| backendAccou ntType | String | RamUser | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
|---|---|---|---|
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications are sent by DingTalk. |
| enableEmail | Boolean | false | Indicates whether notifications are sent by email. |
| enableShortM essage | Boolean | false | Indicates whether notifications are sent by SMS. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |

| organizationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| password | String | H2xWN****** | The password of the cluster user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1121 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |

| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1123 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other fields are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetUserInfo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>00000000000</cellphoneNum>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
<code>ROLERESOURCEUSER</code>
```

```xml
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>11123</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </defaultRole>
    <enableDingTalk>false</enableDingTalk>
    <displayName>test</displayName>
    <roles>
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
```

```xml
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
```

```xml
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "cellphoneNum": "00000000000",
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
            "roleLevel": "11123",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
```

`},`

```json
        "enableDingTalk": "false",
        "displayName": "test",
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
                "roleLevel": "11321",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
```

`}` `],`

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

`}` `],`

```json
            "muserId": "admin",
```

```json
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

`}` `],`

```json
            "enable": "true",
            "name": "default.loginpolicy",
            "rule": "ALLOW",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
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

`}` `],`

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
"df ltRlId" "1"
```

```json
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

`}` `],`

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

`}` `]` `},` `{`

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
                    "alias": "test",
                    "id": "1",
                    "cuserId": "admin"
```

`}` `}` `],`

```json
        "userRoles": [
```

`{`

```json
"roleRange":"roleRangeorgAndSubOrgs"
```

```json
                roleRange: roleRange.orgAndSubOrgs,
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

`}` `],`

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

`}` `],`

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
                "code": "ROLERESOURCEUSER",
```

```
code:
```

`O` `_`

```
SOUC_US
```

`,`

```json
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

`}` `],`

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

`}`

###### 4.3.1.4.8 ListUsers

Queries the list of available users.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListUsers | The operation that you want to perform. Set the value to ListUsers. |
| LoginName | String | No | test | The logon name of the user. |
| RoleId | Integer | No | 2 | The ID of the role. |
| LoginPolicyId | Integer | No | 1 | The ID of the logon policy. |
| OrganizationId | Integer | No | 3 | The ID of the organization. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| PageSize | Integer | No | 10 | The number of entries to return on each page. |
|---|---|---|---|---|

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

| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
|---|---|---|---|
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
|---|---|---|---|
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | user test _ | The display name of the user. |
| email | String | xxx@alibaba- inc.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1606675230000 | The most recent logon time. |
| loginName | String | user test _ | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | false | Indicates whether the logon policy is the default one. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0 | The CIDR block. |

| loginPolicyId | Integer | 1 | The ID of the logon policy. |
|---|---|---|---|
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The ID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | policy test _ | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00.00 | The start of the time range for the query. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1607512443989 | The time when the organization was created. |

| cuserId | String | admin | The user who created the organization. |
|---|---|---|---|
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegion List | List | cn-***-d01 | The list of regions. |
| supportRegion s | String | ["cn-***-d01"] | The list of regions. |
| uuid | String | 123456 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |

| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
|---|---|---|---|
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 111 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
|---|---|---|---|
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRole s | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |

| roleLevel | Integer | 111 | The level of the role. |
|---|---|---|---|
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 1111 | The ID of the user group. |
| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
| groupName | String | ack-user-old | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |

| internal | Boolean | true | Indicates whether the organization is a preset organization. |
|---|---|---|---|
| level | String | 123 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegion List | List | cn-**-d01 | The list of regions. |
| supportRegion s | String | ["cn-**-d01"] | The list of regions. |
| uuid | String | 123456 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | resource test _ | The name of the resource set. |

| rsId | String | 123456 | The ID of the resource set. |
|---|---|---|---|
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123456 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1231 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | RamUser | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | true | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |

| email | String | xxx@alibaba- inc.com | The email address of the user. |
|---|---|---|---|
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xW****** | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1111 | The ID of the role. |

| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
|---|---|---|---|
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 123 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
|---|---|---|---|
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 39 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListUsers &<Common request parameters>
```

Sample success response `XML` format

```xml
<redirect>false</redirect> <cost>188</cost> <code>200</code> <data>
    <cellphoneNum>188*****188</cellphoneNum>
    <enableDingTalk>false</enableDingTalk>
    <displayName>user_test</displayName>
    <parentPk>1689406703302188</parentPk>
    <lastLoginTime>1606675230000</lastLoginTime>
    <default>false</default>
    <deleted>false</deleted>
<loginName>usertest</loginName>
```

```xml
    <loginName>user_test</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>false</enableEmail>
    <enableShortMessage>false</enableShortMessage>
    <email>xxx@alibaba-inc.com</email>
    <status>ACTIVE</status>
    <primaryKey>212530506704030466</primaryKey>
</data> <data>
    <userGroupRoles>
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
        <roleLevel>111</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <userGroups>
        <organizationId>1</organizationId>
        <createTimeStamp>1606791494471</createTimeStamp>
        <groupName>ack-user-old</groupName>
        <augId>1111</augId>
        <id>1</id>
    </userGroups>
    <userGroups>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>resource_test</resourceGroupName>
            <gmtCreated>1606791494471</gmtCreated>
            <rsId>123456</rsId>
            <id>1</id>
        </resourceSets>
        <users>
            <muserId>admin</muserId>
            <backendAccountType>RamUser</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <mtime>1606791494471</mtime>
            <organizationId>1</organizationId>
            <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password>
            <default>true</default>
            <loginTime>1606791494471</loginTime>
            <userLoginCtrlId>34</userLoginCtrlId>
<loginName>test</loginName>
```

```xml
            <loginName>test</loginName>
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
```

```xml
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
```

```xml
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
```

```xml
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "188",
    "code": "200",
    "data": [
```

`{`

```json
            "cellphoneNum": "188*****188",
            "enableDingTalk": "false",
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

`}` `],`

```json
            "userGroups": [
```

`{`

```json
                    "organizationId": "1",
                    "createTimeStamp": "1606791494471",
                    "groupName": "ack-user-old",
```

```json
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

`}` `],`

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
                            "password":
"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS",
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

`}` `],`

```json
                    "roles": [
```

`{`

```json
                            "roleRange": "roleRange.orgAndSubOrgs",
                            "rAMRole": "false",
                            "muserId": "admin",
                            "arId": "123456",
                            "code": "ROLE_RESOURCE_USER",
                            "description": "test",
                            "active": "true",
                            "roleType": "ROLETYPE_ASCM",
                            "default": "true",
```

```json
                            "ownerOrganizationId": "1",
                            "enable": "true",
                            "roleName": "defaultRole.resourceUser.name",
                            "roleLevel": "1231",
                            "id": "1",
                            "organizationVisibility": "organizationVisibility.global",
                            "cuserId": "admin"
```

`}` `]` `},` `{`

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

`}` `}` `],`

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

`}` `],`

```json
            "accessKeys": [
```

`{`

```json
                    "ctime": "1606675230000",
                    "id": "1",
                    "region": "cn-**-d01",
```

`"`

```
Id" "5013"
```

```json
                    "cuserId": "5013",
                    "status": "ACTIVE",
                    "accesskeyId": "JGdgSN2p******"
```

`}` `],`

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

`}` `]` `},` `{`

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

`}` `],`

```json
                "muserId": "admin",
                "default": "false",
"ownerOrganizationId":"1"
```

```json
                ownerOrganizationId: 1,
                "timeRanges": [
```

`{`

```json
                        "startTime": "00.00",
                        "loginPolicyId": "1",
                        "endTime": "24:00"
```

`}` `],`

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

`}` `}` `],`

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

`}`

###### 4.3.1.4.9 ActivateUser

Activates a user. When a user is activated, all AccessKey pairs of the user are activated. This operation is supported by Apsara Stack Enterprise Edition V3.12.0 SP016 or later. This operation is supported by Apsara Stack Enterprise Edition V3.14.0 SP013 or later.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/activateUser HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | test | The logon name of the user. |
| multiCloudStat us | String | Body | No | master | The multi-cloud status of the organization. |

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
| region | String | cn-qingdao-env17- d01 | The zone. |
| status | String | ACTIVE | The state. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |

| defaultRole | Struct |   | The default role. |
|---|---|---|---|
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| deleted | Boolean | false | Indicates whether the user is deleted. |

| displayName | String | test | The display name of the user. |
|---|---|---|---|
| email | String | xx@xx.com | The email address of the user. |
| enableDingTal k | Boolean | true | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | true | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | true | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 16341341514 | The time when the user last logged on. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
| cuserId | String | admin | The creator. |
| default | Boolean | false | Indicates whether the policy is a preset policy. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks that are used to log on to the Apsara Uni-manager Management Console. |
| ipRange | String | 0.0.0.0/0 | The CIDR block that is used to log on to the Apsara Uni-manager Management Console. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |

| lpId | String | 123 | The UUID of the logon policy. |
|---|---|---|---|
| muserId | String | admin | The modifier. |
| name | String | test policy _ | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The type of the logon policy. Allow: whitelist Deny: blacklist |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range queried. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1231244123123 | The time when the organization to which the user belongs was created. |
| cuserId | String | admin | The creator. |

| id | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 23124231234123 | The time when the organization to which the user belongs was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | [cn-qingdao- env17-d01] | The list of zones. |
| supportRegion s | String | cn-qingdao-env17- d01 | The list of zones. |
| uuid | String | 1231 | The UUID of the organization. |
| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-111 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator. |

| default | Boolean | false | Indicates whether the role is a preset role. |
|---|---|---|---|
| description | String | desc | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| status | String | ACTIVE | The state of the user. active inactive |
| userGroupRole s | Array of userGroupRole |   | The list of roles for the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-12323 | The UUID of the role. |
| code | String | test | The code of the role. |

| cuserId | String | admin | The creator of the role. |
|---|---|---|---|
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | desc | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM, ROLETYPE ASCM, and _ _ ROLETYPE RAMROLEAUTHORIZATION. _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a preset or _ custom role. ROLETYPE RAMROLEAUTHORIZATION _ specifies a RAM role-based batch authorization role. |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 123 | The UUID of the user group. |

| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
|---|---|---|---|
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
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao- env17-d01"] | The list of zones. |

| supportRegion s | String | cn-qingdao-env17- d01 | The list of zones. |
|---|---|---|---|
| uuid | String | 23123 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 2 | The ID. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | test | The name of the resource set. |
| rsId | String | 123 | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |

| muserId | String | admin | The modifier of the role. |
|---|---|---|---|
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 123 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE RAM _ | The type of the role. |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the logon policy is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | RamUser | The type of the account that is mapped in the backend. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1011 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |

| email | String | xx@xx.com | The email address of the user. |
|---|---|---|---|
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 2 | The ID of the user. |
| loginName | String | aaa | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The modifier. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxM WLhtyjsO1fRkYoCR cErAgP9Hd0IXp2f5r RSmArS | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 12 | This parameter is deprecated. |
| username | String | aaa | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles for the user. |
| active | Boolean | true | Indicates whether the role is valid. |

| arId | String | 123 | The UUID of the role. |
|---|---|---|---|
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | desc test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2 | The level of the role. |
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |

| pureListData | Boolean | true | Indicates whether only data is returned and other parameters are not returned. |
|---|---|---|---|
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/user/activateUser HTTP/1.1 Common request headers
```

`{`

```json
"LoginName": "test"
```

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>18888888888</cellphoneNum>
    <enableDingTalk>true</enableDingTalk>
    <displayName>test</displayName>
    <parentPk>1689406703302188</parentPk>
    <lastLoginTime>16341341514</lastLoginTime>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>test</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>true</enableEmail>
    <enableShortMessage>true</enableShortMessage>
    <email>xx@xx.com</email>
    <status>ACTIVE</status>
    <primaryKey>212530506704030466</primaryKey>
    <userGroupRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>true</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-12323</arId>
        <code>test</code>
        <description>desc</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
```

```xml
        <enable>true</enable>
        <roleName>test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <userGroups>
        <organizationId>1</organizationId>
        <groupName>test</groupName>
        <augId>123</augId>
        <createTimeStamp>1606791494471</createTimeStamp>
        <id>2</id>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>test</resourceGroupName>
            <gmtCreated>1606791494471</gmtCreated>
            <rsId>123</rsId>
            <id>2</id>
        </resourceSets>
        <users>
            <cellphoneNum>18888888888</cellphoneNum>
            <muserId>admin</muserId>
            <aliyunUser>false</aliyunUser>
            <backendAccountType>RamUser</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <accountType>1</accountType>
            <active>true</active>
            <mtime>1606791494471</mtime>
            <organizationId>1</organizationId>
            <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password>
            <default>false</default>
            <loginTime>1606791494471</loginTime>
            <deleted>false</deleted>
            <userLoginCtrlId>12</userLoginCtrlId>
            <loginName>aaa</loginName>
            <ctime>1606791494471</ctime>
            <mobileNationCode>86</mobileNationCode>
            <id>2</id>
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
<actie>tre</actie>
```

```xml
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
```

```xml
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
```

`p` `g`

```xml
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
{"redirect":"false","cost":"1000","code":"200","data": {"cellphoneNum":"18888888888","enableDingTalk":"true","displayName":"test","parentPk":"16 406703302188","lastLoginTime":"16341341514","default":"false","deleted":"false","loginNam :"test","mobileNationCode":"86","id":"1","enableEmail":"true","enableShortMessage":"true" email":"xx@xx.com","status":"ACTIVE","primaryKey":"212530506704030466","userGroupRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar-1 2323","code":"test","description":"desc","active":"true","roleType":"ROLETYPE_ASCM","defa t":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":"1","i :"1","organizationVisibility":"organizationVisibility.global","cuserId":"admin"}],"userGr ps": [{"organizationId":"1","groupName":"test","augId":"123","createTimeStamp":"1606791494471" id":"2","resourceSets": [{"organizationID":"1","creator":"admin","resourceGroupName":"test","gmtCreated":"1606791 4471","rsId":"123","id":"2"}],"users": [{"cellphoneNum":"18888888888","muserId":"admin","aliyunUser":"false","backendAccountType "RamUser","enableDingTalk":"false","accountType":"1","active":"true","mtime":"16067914944 ","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS" default":"false","loginTime":"1606791494471","deleted":"false","userLoginCtrlId":"12","lo nName":"aaa","ctime":"1606791494471","mobileNationCode":"86","id":"2","ramUser":"true","e bleEmail":"false","enableShortMessage":"false","email":"xx@xx.com","defaultRoleId":"1011" username":"aaa"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123", ode":"ROLE_RESOURCE_USER","description":"test","active":"true","roleType":"ROLETYPE_RAM", efault":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":" 3""id":"1""organizationVisibility":"organizationVisibilityglobal""cuserId":"admin"}]
```

```json
3,id:1,organizationVisibility:organizationVisibility.global,cuserId:admin}], rganization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"0.1","name":"te ","supportRegions":"cn-qingdao-env17d01","ctime":"1606791494471","alias":"test","id":"2","mtime":"1606791494471","uuid":"2312 ,"cuserId":"admin","parentId":"1","supportRegionList":"[\"cn-qingdao-env17d01\"]"}}],"userRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"123"," de":"ROLE_RESOURCE_USER","description":"desc_test","active":"true","roleType":"ROLETYPE_A M","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"name","roleLev ":"2","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cuserId": dmin"}],"accessKeys":[{"ctime":"123141313","id":"1","region":"cn-qingdao-env17-d01","cu serId":"admin","status":"ACTIVE","accesskeyId":"1"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar-1 11","code":"ROLE_RESOURCE_USER","description":"desc","active":"true","roleType":"ROLETYPE SCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"name","roleL el":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cuserId "admin"}],"defaultRole": {"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"ar-1 23","code":"ROLE_RESOURCE_USER","description":"role_test","active":"true","roleType":"ROL YPE_ASCM","default":"true","ownerOrganizationId":"1","enable":"true","roleName":"name","r eLevel":"11","id":"1","organizationVisibility":"defaultRole.resourceUser.description"},"l inPolicy": {"muserId":"admin","default":"false","ownerOrganizationId":"1","enable":"true","name":"te _policy","rule":"ALLOW","id":"1","organizationVisibility":"organizationVisibility.global" lpId":"123","cuserId":"admin","ipRanges": [{"protocol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"}],"timeRanges":[{"startTi me":"00:00","loginPolicyId":"1","endTime":"24:00"}]},"organization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"0.1","name":"te ","supportRegions":"cn-qingdao-env17d01","ctime":"1231244123123","alias":"test","id":"1","mtime":"23124231234123","uuid":"123 ,"cuserId":"admin","parentId":"0","supportRegionList":"[cn-qingdao-env17d01]"}},"success":"true","pureListData":"true","message":"success"}
```

###### 4.3.1.4.10 ListDeletedUsers

Queries the list of deleted users.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDeletedUsers | The operation that you want to perform. Set the value to ListDeletedUsers. |
| LoginName | String | No | testu | The logon name of the user. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| PageSize | Integer | No | 10 | The number of entries to return on each page. |
|---|---|---|---|---|

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
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 1231212 | The most recent logon time. |
| loginName | String | test | The logon name of the user. |

| mobileNationC ode | String | 86 | The country code. |
|---|---|---|---|
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>00000000000</cellphoneNum>
    <enableDingTalk>false</enableDingTalk>
    <displayName>test</displayName>
    <lastLoginTime>1231212</lastLoginTime>
    <default>false</default>
    <deleted>true</deleted>
    <loginName>test</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>false</enableEmail>
    <enableShortMessage>false</enableShortMessage>
    <email>t***@163.com</email>
    <status>ACTIVE</status>
</data> <success>true</success> <pageInfo>
    <total>2</total>
    <totalPage>39</totalPage>
    <pageSize>20</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": [
```

`{`

```json
            "cellphoneNum": "00000000000",
            "enableDingTalk": "false",
            "displayName": "test",
            "lastLoginTime": "1231212",
            "default": "false",
            "deleted": "true",
            "loginName": "test",
            "mobileNationCode": "86",
            "id": "1",
            "enableEmail": "false",
            "enableShortMessage": "false",
            "email": "t***@163.com",
            "status": "ACTIVE"
```

`}` `],`

```json
    "success": "true",
    "pageInfo": {
        "total": "2",
        "totalPage": "39",
        "pageSize": "20",
        "currentPage": "1"
```

`},`

```json
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.11 ListResourceGroupByAscmUserId

Queries the list of resource sets of a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListResourceGro upByAscmUserI d | The operation that you want to perform. Set the value to ListResourceGroupByAscmUserId. |
| ascmuser id _ | Integer | Yes | 5 | The ID of the user. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Array of dataItem |   | The response. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 12314 | The time when the resource set was created. |
| gmtModified | Long | 12314 | The time when the resource set was modified. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | test | The name of the resource set. |
| resourceGroup Type | Integer | 1 | The type of the resource set. 1 indicates the default resource set. If you leave this parameter empty, all the resource sets other than the default one are specified. |
| rsId | String | rs-123144 | The ID of the resource set. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListResourceGroupByAscmUserId &ascmuser_id=5 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <organizationID>1</organizationID>
    <gmtModified>12314</gmtModified>
    <creator>admin</creator>
    <resourceGroupName>test</resourceGroupName>
    <gmtCreated>12314</gmtCreated>
    <rsId>rs-123144</rsId>
    <resourceGroupType>1</resourceGroupType>
    <id>1</id>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": [
```

`{`

```json
            "organizationID": "1",
            "gmtModified": "12314",
            "creator": "admin",
            "resourceGroupName": "test",
            "gmtCreated": "12314",
            "rsId": "rs-123144",
            "resourceGroupType": "1",
            "id": "1"
```

`}` `],`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.12 ModifyUserInformation

Modifies the information of a user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyUserInfor mation | The operation that you want to perform. Set the value to ModifyUserInformation. |
| Id | Integer | No | 100 | The ID of the user. |
| LoginName | String | No | test | The logon name of the user. |
| DisplayName | String | No | test | The display name of the user. |
| LoginPolicyId | Integer | No | 100 | The ID of the logon policy. |
| MobileNationCod e | String | No | test | The country code. |
| CellphoneNum | String | No | 12345678 | The mobile number of the user. |
| TelephoneNum | String | No | 12345678 | The landline number of the user. |
| Email | String | No | e***@test.com | The email address of the user. |
| Description | String | No | test | The description of the user. |
| DingTalkToken | String | No | abc123 | The DingTalk token. |
| EnableDingTalk | Boolean | No | false | Specifies whether to use DingTalk to send notifications. |
| EnableShortMes sage | Boolean | No | false | Specifies whether to use SMS to send notifications. |
| EnableEmail | Boolean | No | false | Specifies whether to use emails to send notifications. |
| MultiCloudStatus | String | No | master | Specifies whether the user is a multi- cloud user. Valid values: master and slave. master indicates a primary- cloud user. slave indicates a secondary-cloud user. |

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
| region | String | cn-qingdao-****- d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | The status of the AccessKey pair. Valid values: active and inactive. |
| cellphoneNum | String | 0000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |

| description | String | test | The description of the role. |
|---|---|---|---|
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates RAM roles. _ ROLETYPE ASCM indicates custom roles. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |

| displayName | String | test | The display name of the user. |
|---|---|---|---|
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
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
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 11213 | The ID of the logon policy. |

| muserId | String | admin | The user who modified the logon policy. |
|---|---|---|---|
| name | String | default.loginpolicy | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the organization. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRange |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |

| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
|---|---|---|---|
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 11231 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |

| id | Integer | 1 | The ID of the role. |
|---|---|---|---|
| muserId | String | admmin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates RAM roles. _ ROLETYPE ASCM indicates custom roles. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRole s | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |

| arId | String | 11231 | The ID of the role. |
|---|---|---|---|
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates RAM roles. _ ROLETYPE ASCM indicates custom roles. _ |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 11231 | The ID of the user group. |
| createTimeSta mp | Long | 1606675230000 | The time when the user group was created. |
| groupName | String | group test _ | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606675230000 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |

| mtime | Long | 1606675230000 | The time when the organization was modified. |
|---|---|---|---|
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 11231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606675230000 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| rsId | String | 11231a | The unique code. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |

| arId | String | 11231 | The ID of the role. |
|---|---|---|---|
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates RAM roles. _ ROLETYPE ASCM indicates custom roles. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | 1 | The type of the account. Valid values: AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606675230000 | The time when the user was created. |
| default | Boolean | false | Indicates whether the user is a preset user. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |

| email | String | t***@163.com | The email address of the user. |
|---|---|---|---|
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606675230000 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606675230000 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xW****** | The password of the user. |
| ramUser | Boolean | false | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 34 | The ID of the logon control. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |

| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
|---|---|---|---|
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations: The role has permissions on all organizations. roleRange.orgAndSubOrgs: The role has permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has permissions on the resource set. roleRange.userGroup: The role has permissions on the user group to which the RAM role belongs. |

| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates RAM roles. _ ROLETYPE ASCM indicates custom roles. _ |
|---|---|---|---|
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyUserInformation &<Common request parameters>
```

Sample success responses `XML` format

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
```

`/`

```xml
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
```

```xml
            <rsId>11231a</rsId>
            <id>1</id>
        </resourceSets>
        <users>
            <muserId>admin</muserId>
            <backendAccountType>1</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <mtime>1606675230000</mtime>
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
```

```xml
            <supportRegions>cnqingdao
d01</supportRegions>
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
```

```xml
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "cellphoneNum": "0000000000",
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
"roleName":"roletest"
```

```json
            roleName: role_test,
            "roleLevel": "11231",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
        "enableDingTalk": "false",
        "displayName": "test",
        "roles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admmin",
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

`}` `],`

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

`}` `],`

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

`}` `],`

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
```

`g` `,`

```json
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

`}` `],`

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

`}` `],`

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
```

```json
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

`}` `]` `},` `{`

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

`}` `}` `],`

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

`}` `],`

```json
        "default": "false",
```

```json
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

`}` `],`

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

`}` `],`

```json
        "mobileNationCode": "86",
        "id": "1",
        "enableEmail": "false",
        "enableShortMessage": "false",
        "email": "t***@163.com",
        "status": "ACTIVE",
```

`"` `i` `K` `"`

```
"212530506704030466"
```

```json
        "primaryKey": "212530506704030466"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.4.13 RecoverUserByLoginName

Restores a deleted user.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RecoverUserByL oginName | The operation that you want to perform. Set the value to RecoverUserByLoginName. |
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
|---|---|---|---|
| region | String | cn-qingdao-****- d01 | The region where the AccessKey pair is available. |
| status | String | ACTIVE | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |

| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| rAMRole | Boolean | false | Indicates whether the role is a Resource Access Management (RAM) role. |
| roleLevel | Integer | 11321 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates RAM roles. _ ROLETYPE ASCM indicates custom roles. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |

| lastLoginTime | Long | 1606675230000 | The most recent logon time. |
|---|---|---|---|
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |
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
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the logon policy is globally shared. organizationVisibility.organization indicates that the logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the logon policy is shared to subordinate organizations. |

| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606791494471 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |

| name | String | test | The name of the organization. |
|---|---|---|---|
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 11231 | The universally unique identifier (UUID) of the organization. |
| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 112311 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| status | String | ACTIVE | The status of the user. Valid values: active and inactive. |
| userGroupRole s | Array of userGroupRole |   | The list of roles of the user group. |
| active | Boolean | true | Indicates whether the role is valid. |

| arId | String | 11231 | The ID of the role. |
|---|---|---|---|
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| userGroups | Array of userGroups |   | The list of user groups. |
| augId | String | 11231 | The ID of the user group. |
| createTimeSta mp | Long | 1606675230000 | The time when the user group was created. |
| groupName | String | group test _ | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information of the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1606675230000 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |

| level | String | 0.1 | The level of the organization. |
|---|---|---|---|
| mtime | Long | 1606675230000 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master indicates a primary-cloud organization. slave indicates a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of regions. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of regions. |
| uuid | String | 11231 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606675230000 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| rsId | String | 11231 | The ID of the resource set. |

| roles | Array of role |   | The list of roles. |
|---|---|---|---|
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11231 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global, organizationVisibility.organization, and organizationVisibility.orgAndSubOrgs. organizationVisibility.global indicates that the role is globally shared. organizationVisibility.organization indicates that the role is shared within the same organization. organizationVisibility.orgAndSubOrgs indicates that the role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |

| roleLevel | Integer | 11231 | The level of the role. |
|---|---|---|---|
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is discarded and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | 1 | The type of the account. Valid values: AscmUser, AliyunUser, and RamUser. AscmUser indicates a user who is visible to customers in the Apsara Uni-manager Management Console. AliyunUser indicates an Apsara Stack tenant account. RamUser indicates a RAM user. |
| cellphoneNum | String | 00000000000 | The mobile number of the user. |
| ctime | Long | 1606675230000 | The time when the user was created. |

| default | Boolean | false | Indicates whether the user is a preset user. |
|---|---|---|---|
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | t***@163.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether to use DingTalk to send notifications. |
| enableEmail | Boolean | false | Indicates whether to use emails to send notifications. |
| enableShortM essage | Boolean | false | Indicates whether to use SMS to send notifications. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606675230000 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606675230000 | The time when the user was modified. |
| muserId | String | admin | The one who calls the operation to modify the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxM WLhtyjsO1fRkYoCR cErAgP9Hd0IXp2f5r RSmArS | The password of the cluster user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 34 | The ID of the logon control. |

| username | String | test | The display name of the user. |
|---|---|---|---|
| userRoles | Array of userRole |   | The list of roles of the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 11321 | The ID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. Valid values: organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 11231 | The level of the role. |
| roleName | String | role test _ | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The permissions of the role. Valid values: roleRange.allOrganizations, roleRange.orgAndSubOrgs, roleRange.resourceSet, and roleRange.userGroup. roleRange.allOrganizations indicates that the role has permissions on all organizations. roleRange.orgAndSubOrgs indicates that the role has permissions on the organization and its subordinate organizations. roleRange.resourceSet indicates that the role has permissions on the resource set. roleRange.userGroup indicates that the role has permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM indicates a RAM role. _ ROLETYPE ASCM indicates a custom role. _ |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RecoverUserByLoginName &LoginName=testtest &OrganizationId=5 &<Common request parameters>
```

Sample success response `XML` format

```xml
<redirect>false</redirect> <code>200</code> <cost>746</cost> <data>
    <cellphoneNum>13311111111</cellphoneNum>
    <displayName>fengyueSubOrgAdmin2</displayName>
```

```xml
    <enableDingTalk>true</enableDingTalk>
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
    <parentPk>1809392454221726</parentPk>
    <lastLoginTime>1592465207953</lastLoginTime>
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
```

```xml
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1592454572000</ctime>
        <id>673</id>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <accesskeyId>0qZ6FB******</accesskeyId>
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "cellphoneNum": "00000000000",
        "defaultRole": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": "false",
            "muserId": "admin",
            "arId": "111",
            "code": "ROLE_RESOURCE_USER",
            "description": "test",
            "active": "true",
            "roleType": "ROLETYPE_ASCM",
```

```json
            "default": "true",
            "ownerOrganizationId": "1",
            "enable": "true",
            "roleName": "role_test",
            "roleLevel": "11321",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global"
```

`},`

```json
        "enableDingTalk": "false",
        "displayName": "test",
        "roles": [
```

`{`

```json
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "112311",
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

`}` `],`

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

`}` `],`

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

`}` `],`

```json
            "enable": "true",
            "name": "default.loginpolicy",
            "rule": "ALLOW",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "11231",
```

```json
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

`}` `],`

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
                        "password":
"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS",
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

`}` `],`

```json
                "roles": [
```

`{` `"` `l``R` `"` `"` `l``R`

```
AdSbO
```

`"`

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

`}` `]` `},` `{`

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

`}` `}` `],`

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
"organizationVisibility":"organizationVisibilityglobal"
```

```json
                organizationVisibility: organizationVisibility.global,
                "cuserId": "admin"
```

`}` `],`

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

`}` `],`

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

`}` `],`

```json
        "mobileNationCode": "86",
"id":"1",
```

```json
        id: 1,
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

`}`

###### 4.3.1.4.14 DeactivateUser

Deactivates a user. When a user is deactivated, all AccessKey pairs of the user are deactivated. This operation is supported by Apsara Stack Enterprise Edition V3.12.0 SP016 or later. This operation is supported by Apsara Stack Enterprise Edition V3.14.0 SP013 or later.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/deactivateUser HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | test | The logon name of the user. |
| multiCloudStat us | String | Body | No | master | The multi-cloud status of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Struct |   | The response data. |

| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
|---|---|---|---|
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
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test desc _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. |

| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1234 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | test | The management permissions of the role. |
| roleType | String | ROLETYPE RAM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| displayName | String | test | The display name of the user. |
| email | String | xx@xx.com | The email address of the user. |
| enableDingTal k | Boolean | true | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | true | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | true | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 16071312412314 | The time when the user last logged on. |
| loginName | String | test | The logon name of the user. |
| loginPolicy | Struct |   | The logon policy. |

| cuserId | String | admin | The creator. |
|---|---|---|---|
| default | Boolean | true | Indicates whether the policy is a preset policy. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRange |   | The list of CIDR blocks that are used to log on to the Apsara Uni-manager Management Console. |
| ipRange | String | 0.0.0.0/0 | The CIDR block that is used to log on to the Apsara Uni-manager Management Console. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 123 | The UUID of the logon policy. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The type of the logon policy. Allow: whitelist Deny: blacklist |

| timeRanges | Array of timeRange |   | The list of time ranges. |
|---|---|---|---|
| endTime | String | 24:00 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range queried. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 18635345234 | The time when the organization to which the user belongs was created. |
| cuserId | String | admin | The creator. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | true | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |
| mtime | Long | 18239237283 | The time when the organization to which the user belongs was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | [cn-qingdao- env17-d01] | The list of zones. |

| supportRegion s | String | cn-qingdao-env17- d01 | The list of zones. |
|---|---|---|---|
| uuid | String | 1231 | The UUID of the organization. |
| parentPk | String | 168940670330218 8 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 466 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | role desc _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | name | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| status | String | ACTIVE | The state of the user. active inactive |
| userGroupRole s | Array of userGroupRole |   | The list of roles for the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | 123 | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | false | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |

| roleName | String | test | The name of the role. |
|---|---|---|---|
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE RAM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
| userGroups | Array of userGroup |   | The list of user groups. |
| augId | String | 1 | The UUID of the user group. |
| createTimeSta mp | Long | 123123123 | The time when the user group was created. |
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

| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
|---|---|---|---|
| muserId | String | admin | The modifier. |
| name | String | TEST | The name of the organization. |
| parentId | Integer | 2 | The ID of the parent organization. |
| supportRegion List | List | ["cn-qingdao- env17-d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-env17- d01 | The list of zones. |
| uuid | String | 123123 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator. |
| gmtCreated | Long | 12312423123 | The time when the resource set was created. |
| id | Integer | 1 | The ID. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | test | The name of the resource set. |
| rsId | String | 123 | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 1 | The UUID of the role. |

| code | String | 1 | The code of the role. |
|---|---|---|---|
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | 1test | The description of the role. |
| enable | Boolean | false | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2 | The level of the role. |
| roleName | String | test | The name of the role. |
| roleRange | String | defaultRole.resourc eUser.name | The management permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM, ROLETYPE ASCM, and _ _ ROLETYPE RAMROLEAUTHORIZATION. _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a preset or _ custom role. ROLETYPE RAMROLEAUTHORIZATION _ specifies a RAM role-based batch authorization role. |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. |

| active | Boolean | false | Indicates whether the role is valid. |
|---|---|---|---|
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | 1 | The type of the account that is mapped in the backend. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |
| ctime | Long | 1234132123 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | xx@xx.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID. |
| loginName | String | admin | The logon name of the user. |
| loginTime | Long | 1231232323 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 12312312312 | The time when the user was modified. |
| muserId | String | admin | The modifier of the role. |

| organizationId | Integer | 1 | The ID of the organization. |
|---|---|---|---|
| password | String | H2xWNY8oitAhxM WLhtyjsO1fRkYoCR cErAgP9Hd0IXp2f5r RSmArS | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 23 | This parameter is deprecated. |
| username | String | test | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles for the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | ar-123 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| description | String | desc | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | true | Indicates whether the role is a RAM role. |

| roleLevel | Integer | 1 | The level of the role. |
|---|---|---|---|
| roleName | String | name | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. ROLETYPE RAM: a RAM role _ ROLETYPE ASCM: a preset or custom _ role ROLETYPE RAMROLEAUTHORIZATION: a _ RAM role-based batch authorization role |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>18888888888</cellphoneNum>
    <enableDingTalk>true</enableDingTalk>
    <displayName>test</displayName>
    <parentPk>1689406703302188</parentPk>
    <lastLoginTime>16071312412314</lastLoginTime>
    <default>false</default>
    <deleted>false</deleted>
<loginName>test</loginName>
```

```xml
    <loginName>test</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>true</enableEmail>
    <enableShortMessage>true</enableShortMessage>
    <email>xx@xx.com</email>
    <status>ACTIVE</status>
    <primaryKey>212530506704030466</primaryKey>
    <userGroupRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>123</arId>
        <code>123</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_RAM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>false</enable>
        <roleName>test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <userGroups>
        <organizationId>1</organizationId>
        <groupName>test</groupName>
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
```

```
use
```

`og` `Ct` `d`

```
3/use
```

`og` `Ct` `d`

```xml
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
```

```xml
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
```

```xml
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
</data> <success>true</success> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"cellphoneNum":"18888888888","enableDingTalk":"true","displayName":"test","parentPk":"16 406703302188","lastLoginTime":"16071312412314","default":"false","deleted":"false","login me":"test","mobileNationCode":"86","id":"1","enableEmail":"true","enableShortMessage":"tr ","email":"xx@xx.com","status":"ACTIVE","primaryKey":"212530506704030466","userGroupRoles [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123", ode":"123","description":"test","active":"true","roleType":"ROLETYPERAM","default":"fals
```

`,` `p` `,` `,` `yp` `_` `,`

```json
,"ownerOrganizationId":"1","enable":"false","roleName":"test","roleLevel":"1","id":"1","o anizationVisibility":"organizationVisibility.global","cuserId":"admin"}],"userGroups":[ {"organizationId":"1","groupName":"test","augId":"1","createTimeStamp":"123123123","id":" ,"resourceSets": [{"organizationID":"1","creator":"admin","resourceGroupName":"test","gmtCreated":"1231242 23","rsId":"123","id":"1"}],"users": [{"cellphoneNum":"18888888888","muserId":"admin","aliyunUser":"false","backendAccountType "1","enableDingTalk":"false","accountType":"1","active":"false","mtime":"12312312312","or nizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS","defau ":"false","loginTime":"1231232323","deleted":"false","userLoginCtrlId":"23","loginName":" min","ctime":"1234132123","mobileNationCode":"86","id":"1","ramUser":"true","enableEmail" false","enableShortMessage":"false","email":"xx@xx.com","defaultRoleId":"1","username":"t t"}],"roles": [{"roleRange":"defaultRole.resourceUser.name","rAMRole":"false","muserId":"admin","arId": ","code":"1","description":"1test","active":"true","roleType":"ROLETYPE_ASCM","default":" lse","ownerOrganizationId":"1","enable":"false","roleName":"test","roleLevel":"2","id":"1 "organizationVisibility":"organizationVisibility.global","cuserId":"admin"}],"organizatio
```

`:`

```json
{"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"1","name":"TEST "supportRegions":"cn-qingdao-env17d01","ctime":"123124123","alias":"test","id":"1","mtime":"15134123123","uuid":"123123","c erId":"admin","parentId":"2","supportRegionList":"[\"cn-qingdao-env17d01\"]"}}],"userRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar-1 23","code":"ROLE_RESOURCE_USER","description":"desc","active":"true","roleType":"ROLETYPE SCM","default":"true","ownerOrganizationId":"1","enable":"true","roleName":"name","roleLe l":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cuserId" admin"}],"accessKeys": [{"ctime":"12314123123123","id":"1","region":"abc","cuserId":"admin","status":"ACTIVE","a esskeyId":"1"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"true","muserId":"admin","arId":"ar-1 23","code":"ROLE_RESOURCE_USER","description":"role_desc","active":"true","roleType":"ROL YPE_ASCM","default":"true","ownerOrganizationId":"1","enable":"true","roleName":"name","r eLevel":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.description","cus Id":"admin"}],"defaultRole": {"roleRange":"test","rAMRole":"false","muserId":"admin","arId":"ar- 123","code":"ROLE_RESOURCE_USER","description":"test_desc","active":"true","roleType":"RO TYPE_RAM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"test"," leLevel":"1234","id":"1","organizationVisibility":"organizationVisibility.global"},"login licy": {"muserId":"admin","default":"true","ownerOrganizationId":"1","enable":"true","name":"tes ,"rule":"ALLOW","id":"1","organizationVisibility":"organizationVisibility.global","lpId": 23","cuserId":"admin","ipRanges": [{"protocol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"}],"timeRanges":[{"startTi me":"00:00","loginPolicyId":"1","endTime":"24:00"}]},"organization": {"muserId":"admin","internal":"true","multiCloudStatus":"master","level":"0.1","name":"te ","supportRegions":"cn-qingdao-env17d01","ctime":"18635345234","alias":"test","id":"1","mtime":"18239237283","uuid":"1231","c erId":"admin","parentId":"0","supportRegionList":"[cn-qingdao-env17d01]"}},"success":"true","pureListData":"true","message":"success"}
```

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

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| loginName | String | Body | No | test | The logon name of the user. |
| userGroupNam e | String | Body | No | groupname | The name of the user group. |
| roleId | Integer | Body | No | 1 | The ID of the role. |
| resourceSetId | Integer | Body | No | 123 | The ID of the resource set. |
| organizationId | Integer | Body | No | 123 | The ID of the organization. |
| currentPage | Integer | Body | No | 1 | The number of the page to return. |
| pageSize | Integer | Body | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Array of itemData |   | The response data. |

| augId | String | 1122 | The UUID of the user group. |
|---|---|---|---|
| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
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
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier of the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 0 | The ID of the parent organization. |
| supportRegion List | List | cn-qingdao-env17- d01 | The list of zones. |

| supportRegion s | String | ["cn-qingdao- env17-d01"] | The list of zones. |
|---|---|---|---|
| uuid | String | 1323 | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 1 | The ID of the resource set. |
| organizationID | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| rsId | String | 123a | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123a | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | aa | The description of the role. |
| enable | Boolean | false | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |

| muserId | String | admin | The modifier of the role. |
|---|---|---|---|
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |

| active | Boolean | true | Indicates whether the user is valid. |
|---|---|---|---|
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | RamUser | The type of the account that is mapped in the backend. AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 12345678911 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role. |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | 1***@123.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |

| mobileNationC ode | String | 86 | The country code. |
|---|---|---|---|
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The modifier of the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxM WLhtyjsO1fRkYoCR cErAgP9Hd0IXp2f5r RSmArS | The password of the user. |
| ramUser | Boolean | false | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 123 | The ID of the logon control. |
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <organizationId>1</organizationId>
    <groupName>test</groupName>
    <augId>1122</augId>
    <createTimeStamp>1606791494471</createTimeStamp>
    <description>a</description>
    <id>1</id>
    <resourceSets>
        <organizationId>1</organizationId>
        <creator>admin</creator>
        <resourceGroupName>res_test</resourceGroupName>
        <gmtCreated>1606791494471</gmtCreated>
        <rsId>123a</rsId>
        <id>1</id>
    </resourceSets>
    <users>
        <cellphoneNum>12345678911</cellphoneNum>
        <muserId>admin</muserId>
        <aliyunUser>false</aliyunUser>
        <backendAccountType>RamUser</backendAccountType>
        <enableDingTalk>false</enableDingTalk>
        <accountType>1</accountType>
        <active>true</active>
        <mtime>1606791494471</mtime>
        <organizationId>1</organizationId>
        <password>H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS</password>
        <default>false</default>
        <loginTime>1606791494471</loginTime>
        <deleted>false</deleted>
        <userLoginCtrlId>123</userLoginCtrlId>
        <loginName>test</loginName>
        <ctime>1606791494471</ctime>
        <mobileNationCode>86</mobileNationCode>
        <id>1</id>
        <ramUser>false</ramUser>
        <enableEmail>false</enableEmail>
        <enableShortMessage>false</enableShortMessage>
        <email>1***@123.com</email>
        <defaultRoleId>1</defaultRoleId>
        <username>test</username>
    </users>
    <roles>
<roleRange>roleRangeorgAndSubOrgs</roleRange>
```

```xml
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>123a</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>aa</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>false</enable>
        <roleName>role_test</roleName>
        <roleLevel>0.1</roleLevel>
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
        <ctime>1606791494471</ctime>
        <alias>test</alias>
        <id>1</id>
        <mtime>1606791494471</mtime>
        <uuid>1323</uuid>
        <cuserId>123</cuserId>
        <parentId>0</parentId>
        <supportRegionList>cn-qingdao-env17-d01</supportRegionList>
    </organization>
</data> <success>true</success> <pageInfo>
    <total>10</total>
    <totalPage>2</totalPage>
    <pageSize>5</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": [{"organizationId":"1","groupName":"test","augId":"1122","createTimeStamp":"1606791494471 "description":"a","id":"1","resourceSets": [{"organizationId":"1","creator":"admin","resourceGroupName":"res_test","gmtCreated":"160 91494471","rsId":"123a","id":"1"}],"users": [{"cellphoneNum":"12345678911","muserId":"admin","aliyunUser":"false","backendAccountType "RamUser","enableDingTalk":"false","accountType":"1","active":"true","mtime":"16067914944 ","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS" default":"false","loginTime":"1606791494471","deleted":"false","userLoginCtrlId":"123","l inName":"test","ctime":"1606791494471","mobileNationCode":"86","id":"1","ramUser":"false" enableEmail":"false","enableShortMessage":"false","email":"1***@123.com","defaultRoleId":" ,"username":"test"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123a" code":"ROLE_RESOURCE_USER","description":"aa","active":"true","roleType":"ROLETYPE_ASCM", efault":"false","ownerOrganizationId":"1","enable":"false","roleName":"role_test","roleLe l":"0.1","id":"1","organizationVisibility":"organizationVisibility.global","cuserId":"adm "}],"organization": {"muserId":"admin","internal":"false","multiCloudStatus":"master","level":"0.1","name":"t t","supportRegions":"[\"cn-qingdao-env17d01\"]","ctime":"1606791494471","alias":"test","id":"1","mtime":"1606791494471","uuid":"1 3","cuserId":"123","parentId":"0","supportRegionList":"cn-qingdao-env17d01"}}],"success":"true","pageInfo": {"total":"10","totalPage":"2","pageSize":"5","currentPage":"1"},"pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.2 CreateUserGroup

Creates a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/createUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| GroupName | String | Body | Yes | test | The name of the user group. |
| OrganizationId | Integer | Body | Yes | 1 | The ID of the organization. |
| Description | String | Body | No | test | The description of the user group. |

| RoleIdList | Json | Body | No | ["12"] | The list of roles. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| code | String | 200 | The HTTP status code. |
| data | Struct |   | The response data. |
| augId | String | 12312 | The UUID of the user group. |
| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
| description | String | group test _ | The description of the user group. |
| groupName | String | group test _ | The name of the user group. |
| id | Integer | 1 | The ID of the user group. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| ctime | Long | 1638345831 | The time when the organization was created. |
| cuserId | String | admin | The creator of the organization. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 0.1 | The level of the organization. |

| mtime | Long | 1638345831 | The time when the organization was modified. |
|---|---|---|---|
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The modifier. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| supportRegion List | List | cn-qingdao-env17- d01 | The list of zones. |
| supportRegion s | String | ["cn-qingdao- env17-d01"] | The list of zones. |
| uuid | String | e2469ed4-527d- 11ec-85ab- 0a80ff2603de | The UUID of the organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The creator of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| id | Integer | 12 | The ID of the resource set. |
| organizationId | Integer | 1 | The ID of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| rsId | String | 123121a | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |

| active | Boolean | true | Indicates whether the role is valid. |
|---|---|---|---|
| arId | String | 123123 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The creator of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The modifier of the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | role test _ | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| aliyunUser | Boolean | false | Indicates whether the account is an Apsara Stack tenant account. |
| backendAccou ntType | String | RamUser | The type of the account that is mapped in the backend. AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 16067914944 | The mobile number of the user. |
| ctime | Long | 1606791494471 | The time when the user was created. |
| default | Boolean | true | Indicates whether the role is a preset role. |

| defaultRoleId | Integer | 1 | The ID of the default role. |
|---|---|---|---|
| deleted | Boolean | false | Indicates whether the user is deleted. |
| email | String | 1***@123.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | test | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| mtime | Long | 1606791494471 | The time when the user was modified. |
| muserId | String | admin | The modifier of the user. |
| organizationId | Integer | 1 | The ID of the organization. |
| password | String | H2xWNY8oitAhxM WLhtyjsO1fRkYoCR cErAgP9Hd0IXp2f5r RSmArS | The password of the user. |
| ramUser | Boolean | true | Indicates whether the account is a RAM user. |
| userLoginCtrlI d | Integer | 12 | This parameter is deprecated. |
| username | String | test | The display name of the user. |

| message | String | success | The message. |
|---|---|---|---|
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

`}` Sample success responses `XML` format

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
```

```xml
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
</data> <success>true</success> <pureListData>false</pureListData>
```

```xml
<pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"organizationId":"1","groupName":"group_test","augId":"12312","createTimeStamp":"1606791 4471","description":"group_test","id":"1","resourceSets": [{"organizationId":"1","creator":"admin","resourceGroupName":"res_test","gmtCreated":"160 91494471","rsId":"123121a","id":"12"}],"users": [{"cellphoneNum":"16067914944","muserId":"admin","aliyunUser":"false","backendAccountType "RamUser","enableDingTalk":"false","accountType":"1","active":"true","mtime":"16067914944 ","organizationId":"1","password":"H2xWNY8oitAhxMWLhtyjsO1fRkYoCRcErAgP9Hd0IXp2f5rRSmArS" default":"true","loginTime":"1606791494471","deleted":"false","userLoginCtrlId":"12","log Name":"test","ctime":"1606791494471","mobileNationCode":"86","id":"1","ramUser":"true","e bleEmail":"false","enableShortMessage":"false","email":"1***@123.com","defaultRoleId":"1", sername":"test"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"12312 ,"code":"ROLE_RESOURCE_USER","description":"test","active":"true","roleType":"ROLETYPE_AS ","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"role_test","rol evel":"1","id":"1","organizationVisibility":"organizationVisibility.global","cuserId":"ad n"}],"organization": {"muserId":"admin","internal":"false","multiCloudStatus":"master","level":"0.1","name":"t t","supportRegions":"[\"cn-qingdao-env17d01\"]","ctime":"1638345831","alias":"test","id":"1","mtime":"1638345831","uuid":"e2469ed 527d-11ec-85ab-0a80ff2603de","cuserId":"admin","parentId":"1","supportRegionList":"cn-q ingdao-env17-d01"}},"success":"true","pureListData":"false","message":"success"}
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

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| UserGroupId | Integer | Body | Yes | 123 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Struct |   | The response data. |
| accessKeys | Array of accessKey |   | The list of AccessKey pairs. |
| CreateTime | String | 1606675230000 | The time when the AccessKey pair was created. |
| accesskeyId | String | JGdgSN2p****** | The AccessKey ID. |
| accesskeySecr et | String | ************** | The AccessKey secret. |
| ctime | Long | 1606675230000 | The time when the AccessKey pair was created. |
| cuserId | String | admin | The user who created the AccessKey pair. |
| dtUserId | Integer | 1 | This parameter is deprecated. |
| id | Integer | 1 | The primary key of the AccessKey pair. |
| mtime | Long | 1606675230000 | The time when the AccessKey was modified. |
| muserId | String | admin | The user who modified the AccessKey pair. |
| region | String | cn-qingdao-****- d01 | The zone in which the AccessKey pair is available. |
| status | String | active | Indicates whether the AccessKey pair is valid. Valid values: active and inactive. |
| type | String | 1 | The type of the AccessKey pair. |
| cellphoneNum | String | 18888888888 | The mobile number of the user. |

| default | Boolean | false | Indicates whether the role is a preset role. |
|---|---|---|---|
| defaultRole | Struct |   | The default role. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 111 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | as | The description of the role. |
| enable | Boolean | true | Indicates whether the role is enabled. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 2 | The level of the role. |
| roleName | String | test | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
| deleted | Boolean | false | Indicates whether the user is deleted. |
| description | String | description | The description of the user. |
| displayName | String | test | The display name. |
| email | String | 1***@122.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| id | Integer | 1 | The ID of the user. |
| lastLoginTime | Long | 162314151313 | The time when the user logged on. |
| loginName | String | 123 | The logon name of the user. |
| loginPolicy | Struct |   | The information about the logon policy. |

| cuserId | String | admin | The user who created the logon policy. |
|---|---|---|---|
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
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | allow | The type of the logon policy. Valid values: Allow and Deny. Allow specifies a whitelist. Deny specifies a blacklist. |
| timeRanges | Struct |   | The list of time ranges. |

| endTime | String | 11:20 | The end of the time range queried. |
|---|---|---|---|
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 10:20 | The beginning of the time range queried. |
| mobileNationC ode | String | 86 | The country code. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| childrenOrder | String | 343,44,33 | The sorted organization IDs. |
| ctime | Long | 1622311 | The time when the organization was created. |
| cuserId | String | admin | The user who created the organization. |
| description | String | aa | The description of the organization. |
| dtOrgId | Integer | 1 | This parameter is deprecated. |
| extraInfo | String | aaa | This parameter is deprecated. |
| id | Integer | 1 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 1 | The level of the organization. |
| mtime | Long | 15123222 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |

| muserId | String | admin | The modifier. |
|---|---|---|---|
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| personNum | Integer | 12 | The maximum number of users. |
| resourceGroup Num | Integer | 10 | The maximum number of resource sets. |
| status | String | active | Indicates whether the organization is valid. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of zones. |
| uuid | String | 1231231 | The UUID of the organization. |
| parentPk | String | 168940670330218 0 | The primary key of the Apsara Stack tenant account. |
| primaryKey | String | 212530506704030 000 | The primary key of the RAM user. |
| roles | Array of role |   | The list of roles. |
| active | String | true | Indicates whether the role is valid. |
| arId | String | 1231 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| cuserId | String | admin | The user who created the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |

| enable | Boolean | true | Indicates whether the role is valid. |
|---|---|---|---|
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| privilegeCodes | List | ["123"] | The list of permission codes. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | role test _ | The name of the role. |
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |

| systemPrivileg eCodes | List | ["123"] | The list of system permission codes. |
|---|---|---|---|
| status | String | active | The state of the user. Valid values: active and inactive. |
| telephoneNum | String | 12345678 | The landline number of the user. |
| userGroupRole s | Array of userGroupRole |   | The list of roles for the user group. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | 1 | The code of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | role test _ | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | admin | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 2 | The ID of the organization. |
| rAMRole | String | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |

| roleName | String | test | The name of the role. |
|---|---|---|---|
| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
| userGroups | Struct |   | The list of user groups. |
| augId | String | 1231 | The UUID of the user group. |
| createTimeSta mp | Long | 1606791494471 | The time when the user group was created. |
| description | String | test | The description of the user group. |
| groupName | String | group test _ | The name of the user group. |
| id | Integer | 123 | The ID of the user group. |
| organization | Struct |   | The information about the organization. |
| alias | String | test | The alias of the organization. |
| childrenOrder | String | 343,44,33 | The sorted organization IDs. |
| ctime | Long | 1606791494471 | The time when the organization was created. |

| cuserId | String | admin | The user who created the organization. |
|---|---|---|---|
| description | String | test | The description of the organization. |
| dtOrgId | Integer | 1 | This parameter is deprecated. |
| extraInfo | String | 123 | This parameter is deprecated. |
| id | Integer | 2 | The ID of the organization. |
| internal | Boolean | false | Indicates whether the organization is a preset organization. |
| level | String | 1 | The level of the organization. |
| mtime | Long | 1606791494471 | The time when the organization was modified. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| muserId | String | admin | The user who modified the organization. |
| name | String | test | The name of the organization. |
| parentId | Integer | 1 | The ID of the parent organization. |
| personNum | Integer | 12 | The maximum number of users. |
| resourceGroup Num | Integer | 10 | The maximum number of resource sets. |
| status | String | active | Indicates whether the organization is valid. |
| supportRegion List | List | ["cn-qingdao-****- d01"] | The list of zones. |
| supportRegion s | String | cn-qingdao-****- d01 | The list of zones. |

| uuid | String | asd123 | The UUID of the organization. |
|---|---|---|---|
| organizationId | Integer | 1 | The ID of the organization. |
| resourceSets | Array of resourceSet |   | The list of resource sets. |
| creator | String | admin | The user who created the resource set. |
| description | String | test | The description of the resource set. |
| gmtCreated | Long | 1606791494471 | The time when the resource set was created. |
| gmtModified | Long | 1606791494471 | The time when the resource set was modified. |
| id | Integer | 1 | The ID of the resource set. |
| modifier | String | admin | The user who modified the resource set. |
| organizationId | Integer | 1 | The ID of the organization. |
| organizationN ame | String | testz | The name of the organization. |
| resourceGroup Name | String | res test _ | The name of the resource set. |
| resourceGroup Type | Integer | 1 | The type of the resource set. |
| rsId | String | 123a | The UUID of the resource set. |
| roles | Array of role |   | The list of roles. |
| active | String | true | Indicates whether the role is valid. |
| arId | String | 123a | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |

| cuserId | String | admin | The user who created the role. |
|---|---|---|---|
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | 132 | The user who modified the role. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| privilegeCodes | List | ["123"] | The list of permission codes. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | test | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions of the role. roleRange.allOrganizations: The role has management permissions on all organizations. roleRange.orgAndSubOrgs: The role has management permissions on the organization and its subordinate organizations. roleRange.resourceSet: The role has management permissions on the resource set. roleRange.userGroup: The role has management permissions on the user group to which the RAM role belongs. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
| systemPrivileg eCodes | List | ["123"] | The list of system permission codes. |
| users | Array of user |   | The list of users. |
| accountType | Integer | 1 | The type of the account. This parameter is deprecated and is not processed in the code. The default value is used. |
| active | Boolean | true | Indicates whether the user is valid. |
| backendAccou ntType | String | RamUser | The type of the account that is mapped in the backend. AscmUser: the user who is visible to customers in the Apsara Uni-manager Management Console AliyunUser: the Apsara Stack tenant account RamUser: the RAM user |
| cellphoneNum | String | 123412341231 | The mobile number of the user. |
| default | Boolean | true | Indicates whether the role is a preset role. |
| defaultRoleId | Integer | 1 | The ID of the default role for the user. |
| deleted | Boolean | false | Indicates whether the user is deleted. |

| description | String | test | The description of the user. |
|---|---|---|---|
| dtUserId | Integer | 1 | This parameter is deprecated. |
| email | String | 1***@123.com | The email address of the user. |
| enableDingTal k | Boolean | false | Indicates whether notifications by using DingTalk are enabled. |
| enableEmail | Boolean | false | Indicates whether notifications by using emails are enabled. |
| enableShortM essage | Boolean | false | Indicates whether notifications by using text messages are enabled. |
| extraInfo | String | 1 | This parameter is deprecated. |
| id | Integer | 1 | The ID of the user. |
| loginName | String | admin | The logon name of the user. |
| loginTime | Long | 1606791494471 | The time when the user logged on. |
| mobileNationC ode | String | 86 | The country code. |
| multiCloudStat us | String | master | Indicates whether the organization is a multi-cloud organization. Valid values: master and slave. master specifies a primary-cloud organization. slave specifies a secondary-cloud organization. |
| organizationId | Integer | 1 | The ID of the organization. |
| parentPk | String | 1234123 | The primary key of the Apsara Stack tenant account. |
| password | String | afarqwedf | The password of the user. |
| pk | String | 123 | The primary key. |
| telephoneNum | String | 123123123 | The landline number of the user. |

| userLoginCtrlI d | Integer | 1 | The ID of the logon control. |
|---|---|---|---|
| username | String | admin | The display name of the user. |
| userRoles | Array of userRole |   | The list of roles for the user. |
| active | Boolean | true | Indicates whether the role is valid. |
| arId | String | 123 | The UUID of the role. |
| code | String | ROLE RESOURCE _ _ USER | The code of the role. |
| default | Boolean | false | Indicates whether the role is a preset role. |
| description | String | test | The description of the role. |
| enable | Boolean | true | Indicates whether the role is valid. |
| id | Integer | 1 | The ID of the role. |
| muserId | String | 123 | The user who modified the role. |
| organizationVi sibility | String | defaultRole.resourc eUser.description | The sharing scope of the role. organizationVisibility.global: The role is globally shared. organizationVisibility.organization: The role is shared within the same organization. organizationVisibility.orgAndSubOrgs: The role is shared with subordinate organizations. |
| ownerOrganiz ationId | String | 123 | The ID of the organization. |
| rAMRole | Boolean | false | Indicates whether the role is a RAM role. |
| roleLevel | Integer | 1 | The level of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |

| roleRange | String | roleRange.orgAndS ubOrgs | The management permissions. |
|---|---|---|---|
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>18888888888</cellphoneNum>
    <telephoneNum>12345678</telephoneNum>
    <enableDingTalk>false</enableDingTalk>
    <displayName>test</displayName>
    <description>description</description>
    <parentPk>1689406703302180</parentPk>
    <lastLoginTime>162314151313</lastLoginTime>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>123</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>false</enableEmail>
    <enableShortMessage>false</enableShortMessage>
    <email>1***@122.com</email>
<status>active</status>
```

```xml
    <status>active</status>
    <primaryKey>212530506704030000</primaryKey>
    <userGroupRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>123</arId>
        <code>1</code>
        <description>role_test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>2</ownerOrganizationId>
        <enable>true</enable>
        <roleName>test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userGroupRoles>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>123</muserId>
        <arId>123</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>123</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
<organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
    </userRoles>
    <accessKeys>
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
```

```
use dad /use
```

`d`

```xml
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
```

```xml
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
```

```xml
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
            <parentId>1</parentId>
            <multiCloudStatus>master</multiCloudStatus>
            <childrenOrder>343,44,33</childrenOrder>
            <name>test</name>
```

`/`

```xml
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

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"cellphoneNum":"18888888888","telephoneNum":"12345678","enableDingTalk":"false","display me":"test","description":"description","parentPk":"1689406703302180","lastLoginTime":"162 4151313","default":"false","deleted":"false","loginName":"123","mobileNationCode":"86","i :"1","enableEmail":"false","enableShortMessage":"false","email":"1***@122.com","status":"a ive","primaryKey":"212530506704030000","userGroupRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"123", ode":"1","description":"role_test","active":"true","roleType":"ROLETYPE_ASCM","default":" lse","ownerOrganizationId":"2","enable":"true","roleName":"test","roleLevel":"1","id":"1" organizationVisibility":"organizationVisibility.global"}],"userRoles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"123","arId":"123","c e":"ROLE_RESOURCE_USER","description":"test","active":"true","roleType":"ROLETYPE_ASCM"," fault":"false","ownerOrganizationId":"123","enable":"true","roleName":"defaultRole.resour User.name","roleLevel":"1","id":"1","organizationVisibility":"defaultRole.resourceUser.de ription"}],"accessKeys": [{"muserId":"admin","CreateTime":"1606675230000","ctime":"1606675230000","id":"1","mtime" 1606675230000","type":"1","accesskeySecret":"**************","region":"cn-qingdao-env17
```

`-`

```json
d01","cuserId":"admin","dtUserId":"1","status":"active","accesskeyId":"JGdgSN2p******"}], oles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"1231" code":"ROLE_RESOURCE_USER","description":"role_test","active":"true","roleType":"ROLETYPE SCM","default":"false","ownerOrganizationId":"1","enable":"true","roleName":"role_test"," leLevel":"1","id":"1","cuserId":"admin","organizationVisibility":"organizationVisibility. obal","privilegeCodes":"[\"123\"]","systemPrivilegeCodes":"[\"123\"]"}],"defaultRole":{ "roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"admin","arId":"111","c e":"ROLE_RESOURCE_USER","description":"as","active":"true","roleType":"ROLETYPE_ASCM","de ult":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":"2", d":"1","cuserId":"admin","organizationVisibility":"organizationVisibility.global"},"login licy": {"muserId":"admin","default":"false","ownerOrganizationId":"1","enable":"true","name":"de ult.loginpolicy","rule":"allow","id":"1","organizationVisibility":"organizationVisibility lobal","lpId":"111","cuserId":"admin","ipRanges": {"protocol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"},"timeRanges": {"startTime":"10:20","loginPolicyId":"1","endTime":"11:20"}},"organization":{"dtOrgId": "1","muserId":"admin","internal":"false","level":"1","description":"aa","supportRegions": n-qingdao-****-
```

```json
d01","personNum":"12","mtime":"15123222","uuid":"1231231","parentId":"1","multiCloudStatu :"master","childrenOrder":"343,44,33","name":"test","ctime":"1622311","alias":"test","res rceGroupNum":"10","id":"1","cuserId":"admin","status":"active","extraInfo":"aaa","support gionList":"[\"cn-qingdao-****-d01\"]"},"userGroups": {"organizationId":"1","groupName":"group_test","augId":"1231","createTimeStamp":"16067914 471","description":"test","id":"123","resourceSets": [{"organizationId":"1","creator":"admin","gmtModified":"1606791494471","resourceGroupName "res_test","organizationName":"testz","gmtCreated":"1606791494471","modifier":"admin","rs ":"123a","description":"test","resourceGroupType":"1","id":"1"}],"users": [{"backendAccountType":"RamUser","telephoneNum":"123123123","enableDingTalk":"false","des iption":"test","parentPk":"1234123","organizationId":"1","default":"true","password":"afa wedf","loginTime":"1606791494471","userLoginCtrlId":"1","loginName":"admin","id":"1","ena eShortMessage":"false","defaultRoleId":"1","email":"1***@123.com","cellphoneNum":"12341234 31","accountType":"1","active":"true","dtUserId":"1","multiCloudStatus":"master","deleted "false","pk":"123","mobileNationCode":"86","enableEmail":"false","extraInfo":"1","usernam :"admin"}],"roles": [{"roleRange":"roleRange.orgAndSubOrgs","rAMRole":"false","muserId":"132","arId":"123a"," de":"ROLE_RESOURCE_USER","description":"test","active":"true","roleType":"ROLETYPE_ASCM", efault":"false","ownerOrganizationId":"1","enable":"true","roleName":"test","roleLevel":" ,"id":"1","cuserId":"admin","organizationVisibility":"organizationVisibility.global","pri legeCodes":"[\"123\"]","systemPrivilegeCodes":"[\"123\"]"}],"organization":{"dtOrgId":" 1","muserId":"admin","internal":"false","level":"1","description":"test","supportRegions" cn-qingdao-****d01","personNum":"12","mtime":"1606791494471","uuid":"asd123","parentId":"1","multiCloudS tus":"master","childrenOrder":"343,44,33","name":"test","ctime":"1606791494471","alias":" st","resourceGroupNum":"10","id":"2","cuserId":"admin","status":"active","extraInfo":"123 "supportRegionList":"[\"cn-qingdao-****d01\"]"}}},"success":"true","pureListData":"false","message":"success"}
```

###### 4.3.1.5.4 AddUsersToUserGroup

Adds users to a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/addUsersToUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.5 AddRoleToUserGroup

Adds a role to one or more user groups.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/addRoleToUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| UserGroupId | Integer | Body | Yes | 1 | The ID of the user group. |
| UserGroupIdLi st | Json | Body | Yes | ["1","2"] | The IDs of the user groups. |
| RoleId | Integer | Body | No | 1 | The ID of the role. |

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
POST /ascm/auth/user/addRoleToUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"UserGroupId": "1", "UserGroupIdList": "["1","2"]"
```

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.6 AddResourceSetToUserGroup

Binds a resource set to a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/addResourceSetToUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| AscmRoleId | String | Body | Yes | 1 | The ID of the role in the Apsara Uni-manager Management Console. |
| ResourceSetId | Integer | Body | Yes | 1 | The ID of the resource set. |
| UserGroupId | Integer | Body | No | 1 | The ID of the user group. |

| UserGroupIdLi st | Json | Body | No | ["1","2"] | The list of user groups. |
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
POST /ascm/auth/user/addResourceSetToUserGroup HTTP/1.1 Common request headers
```

`{`

```json
"AscmRoleId": "1", "ResourceSetId": "1"
```

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.7 RemoveUsersFromUserGroup

Removes users from a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/removeUsersFromUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.8 RemoveRoleFromUserGroup

Removes a role from a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/removeRoleFromUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| RoleId | Integer | Body | Yes | 1 | The ID of the role. |
| UserGroupId | Integer | Body | Yes | 2 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.9 RemoveResourceSetFromUserGroup

Deletes a resource set from a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/removeResourceSetFromUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

###### 4.3.1.5.10 DeleteUserGroup

Deletes a user group.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/user/deleteUserGroup HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| UserGroupId | Integer | Body | Yes | 123 | The ID of the user group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | success | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |

| redirect | Boolean | false | Indicates whether the request is redirected. |
|---|---|---|---|
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

##### 4.3.1.6 Logon policies

###### 4.3.1.6.1 AddLoginPolicy

Creates a logon policy.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/loginPolicy/addLoginPolicy HTTP/1.1
```

**Request parameters**

| 88 |   |   |   |   | > Document Version: 2025110 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| name | String | Body | No | test | The name of the logon policy. |
| description | String | Body | No | description | The description of the logon policy. |
| rule | String | Body | No | deny | The type of the logon policy. Valid values: Allow and Deny. Allow specifies a whitelist. Deny specifies a blacklist. |
| ipRanges | Json | Body | No | {"IpRanges": [ { " ipRange": "X.X.X.X/24" }, { " ipRange": "X.X.X.X/24" } ]} | The list of CIDR blocks. |
| timeRanges | Json | Body | No | {"TimeRanges ": [ { "startTime ": "11:00", " endTime": " 13:35" }, { " startTime": "12: 00", "endTime": "12:30" } ]} | The list of time ranges. |
| enable | Boolea n | Body | No | true | Specifies whether the logon policy is valid. |
| organizationVi sibility | String | Body | No | organizationVi sibility.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization : The logon policy is shared within the same organization. organizationVisibility.orgAndSub Orgs: The logon policy is shared with subordinate organizations. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |

| cost | Integer | 1000 | The amount of time consumed by the operation. |
|---|---|---|---|
| data | Struct |   | The response data. |
| cuserId | String | admin | The user who created the logon policy. |
| default | Boolean | true | Indicates whether the logon policy is the default one. |
| description | String | desc test _ | The description of the logon policy. |
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRang |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | 111 | The UUID of the logon policy. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | defaultLoginPolicy. name | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared with subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |

| rule | String | ALLOW | The type of the logon policy. Valid values: Allow and Deny. Allow specifies a whitelist. Deny specifies a blacklist. |
|---|---|---|---|
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range queried. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The beginning of the time range queried. |
| message | String | success | The message. |
| pureListData | Boolean | true | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
POST /ascm/auth/loginPolicy/addLoginPolicy HTTP/1.1 Common request headers
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <default>true</default>
    <ownerOrganizationId>1</ownerOrganizationId>
    <enable>true</enable>
    <name>defaultLoginPolicy.name</name>
    <rule>ALLOW</rule>
    <description>desc_test</description>
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
        <startTime>00:00</startTime>
        <loginPolicyId>1</loginPolicyId>
        <endTime>24:00</endTime>
    </timeRanges>
</data> <success>true</success> <pureListData>true</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"muserId":"admin","default":"true","ownerOrganizationId":"1","enable":"true","name":"def ltLoginPolicy.name","rule":"ALLOW","description":"desc_test","id":"1","organizationVisibi ty":"organizationVisibility.global","lpId":"111","cuserId":"admin","ipRanges":[{"protoc ol":"IPV4","ipRange":"0.0.0.0/0","loginPolicyId":"1"}],"timeRanges": [{"startTime":"00:00","loginPolicyId":"1","endTime":"24:00"}]},"success":"true","pureList ta":"true","message":"success"}
```

###### 4.3.1.6.2 CheckLoginPolicy

Checks a logon policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | CheckLoginPolic y | The operation that you want to perform. Set the value to CheckLoginPolicy. |
|---|---|---|---|---|
| Ip | String | Yes | 1.1.1.1 | The IP address to be checked. Logon policies include whitelist and blacklist policies. A whitelist policy is used to check the IP addresses from which you can log on. A blacklist policy is used to check the IP addresses from which you cannot log on. |
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>true</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": "true",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.6.3 ListLoginPolicies

Queries the list of logon policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListLoginPolicies | The operation that you want to perform. Set the value to ListLoginPolicies. |
| Name | String | No | test | The name of the logon policy. |
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

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |
| endTime | String | 24:00 | The end of the time range for the query. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| startTime | String | 00:00 | The start of the time range for the query. |
| userCount | Integer | 12 | The number of users who use the logon policy. |
| message | String | success | The error message. |
| pageInfo | Struct |   | The page information. |
| currentPage | Integer | 1 | The page number of the returned page. |
| pageSize | Integer | 20 | The number of entries returned per page. |
| total | Integer | 39 | The total number of entries returned. |
| totalPage | Integer | 2 | The total number of pages returned. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |

| redirect | Boolean | false | Indicates whether redirections are performed. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListLoginPolicies &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <default>true</default>
    <userCount>12</userCount>
    <ownerOrganizationId>1</ownerOrganizationId>
    <enable>true</enable>
    <name>Indicates whether only data is returned and other parameters are not returned
.</name>
    <rule>ALLOW</rule>
    <id>1</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
    <lpId>1111</lpId>
    <cuserId>admin</cuserId>
</data> <data>
    <ipRanges>
        <ipRange>0.0.0.0/0</ipRange>
        <protocol>IPV4</protocol>
        <loginPolicyId>1</loginPolicyId>
    </ipRanges>
    <timeRanges>
        <startTime>00:00</startTime>
        <loginPolicyId>1</loginPolicyId>
        <endTime>24:00</endTime>
    </timeRanges>
</data> <success>true</success> <pageInfo>
    <total>39</total>
    <totalPage>2</totalPage>
    <pageSize>20</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

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
            "name": Indicates whether only data is returned and other parameters are
not returned.
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

`}` `],`

```json
            "timeRanges": [
```

`{`

```json
                    "startTime": "00:00",
                    "loginPolicyId": "1",
                    "endTime": "24:00"
```

`}` `]` `}` `],`

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

`}`

###### 4.3.1.6.4 ModifyLoginPolicy

Modifies a logon policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoginPolic y | The operation that you want to perform. Set the value to ModifyLoginPolicy. |
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
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| cuserId | String | admin | The creator of the logon policy. |

| default | Boolean | true | Indicates whether the logon policy is the default one. |
|---|---|---|---|
| enable | Boolean | true | Indicates whether the logon policy is valid. |
| id | Integer | 1 | The ID of the logon policy. |
| ipRanges | Array of ipRang |   | The list of CIDR blocks. |
| ipRange | String | 0.0.0.0/0 | The CIDR block. |
| loginPolicyId | Integer | 1 | The ID of the logon policy. |
| protocol | String | IPV4 | The protocol. |
| lpId | String | lp- 1010e681dc790aa b5041000y | The ID of the logon policy. |
| mtime | Long | 1608175299345 | The time when the logon policy was modified. |
| muserId | String | admin | The user who modified the logon policy. |
| name | String | testNew | The name of the logon policy. |
| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
| rule | String | ALLOW | The rule of the logon policy. Valid values: Allow and Deny. |
| timeRanges | Array of timeRang |   | The list of time ranges. |

| endTime | String | 24:00 | The end of the time range for the query. |
|---|---|---|---|
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <timeRanges>
        <startTime>00:00</startTime>
        <loginPolicyId>1</loginPolicyId>
        <endTime>24:00</endTime>
    </timeRanges>
    <rule>ALLOW</rule>
    <mtime>1608175299345</mtime>
    <lpId>lp-1010e681dc790aab5041000y</lpId>
    <ipRanges>
        <ipRange>0.0.0.0/0</ipRange>
        <protocol>IPV4</protocol>
        <loginPolicyId>1</loginPolicyId>
    </ipRanges>
    <default>true</default>
    <ownerOrganizationId>1</ownerOrganizationId>
    <enable>true</enable>
    <name>testNew</name>
    <id>1</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
    <cuserId>admin</cuserId>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "muserId": "admin",
        "timeRanges": [
```

`{`

```json
                "startTime": "00:00",
                "loginPolicyId": "1",
                "endTime": "24:00"
```

`}` `],`

```json
        "rule": "ALLOW",
        "mtime": "1608175299345",
        "lpId": "lp-1010e681dc790aab5041000y",
        "ipRanges": [
```

`{`

```json
                "ipRange": "0.0.0.0/0",
                "protocol": "IPV4",
                "loginPolicyId": "1"
```

`}` `],`

```json
        "default": "true",
        "ownerOrganizationId": "1",
        "enable": "true",
        "name": "testNew",
        "id": "1",
        "organizationVisibility": "organizationVisibility.global",
        "cuserId": "admin"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

###### 4.3.1.6.5 GetLoginPolicyById

Queries the information of a logon policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetLoginPolicyB yId | The operation that you want to perform. Set the value to GetLoginPolicyById. |
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
| name | String | defaultLoginPolicy. name | The name of the logon policy. |

| organizationVi sibility | String | organizationVisibili ty.global | The sharing scope of the logon policy. Valid values: organizationVisibility.global: The logon policy is globally shared. organizationVisibility.organization: The logon policy is shared within the same organization. organizationVisibility.orgAndSubOrgs: The logon policy is shared to subordinate organizations. |
|---|---|---|---|
| ownerOrganiz ationId | Integer | 1 | The ID of the organization. |
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

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
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
    <name>defaultLoginPolicy.name</name>
    <rule>ALLOW</rule>
    <id>1</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
    <lpId>111</lpId>
    <cuserId>admin</cuserId>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "ipRanges": [
```

`{`

```json
                "ipRange": "0.0.0.0/0",
                "protocol": "IPV4",
                "loginPolicyId": "1"
```

`}` `],`

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

`}` `],`

```json
        "enable": "true",
        "name": "defaultLoginPolicy.name",
        "rule": "ALLOW",
        "id": "1",
        "organizationVisibility": "organizationVisibility.global",
        "lpId": "111",
        "cuserId": "admin"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

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

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateQuota | The operation that you want to perform. Set the value to CreateQuota. |
| ProductName | String | Yes | ECS | The name of the service. Valid values: ECS, OSS, VPC, RDS, SLB, ODPS, EIP, ADB, GPDB, R-kvstore, DRDS, OTS, NAS, and DDS. |

| QuotaBody | Json | Yes | {"totalCpu":100, "totalMem":100, "totalGpu":100, "totalDisk cloud _ ssd":100,"total _ Disk cloud effici _ _ ency":100} | The parameters of the quota to update. The parameters vary with the specific service. ECS: {"totalCpu":100,"totalMem":10 0,"totalGpu":100,"totalDisk c _ loud ssd":100,"totalDisk clou _ _ d efficiency":100} _ OSS: {"totalAmount":100} VPC: {"totalVPC":100} RDS: {"totalCpu":100,"totalMem":10 0,"totalDisk":100} SLB: {"totalVipInternal":100,"tota lVipPublic":100} ODPS: {"totalCu":100,"totalDisk":10 0} EIP: {"totalEIP":100} |
|---|---|---|---|---|
| QuotaType | String | Yes | organization | Valid values: organization and resourceGroup. |
| QuotaTypeId | Integer | Yes | 1 | The ID of the quota type. Specify an organization ID when the QuotaType parameter is set to organization. Specify a resource set ID when the QuotaType parameter is set to resourceGroup. |
| RegionName | String | Yes | cn-******-****- d01 | The region name. |
| RequestId | String | No | d0c6ed24-45af- 4703-866f- 5103302b9a72 | The ID of the request. |
| ClusterName | String | No | "" | The name of the cluster. This reserved parameter is optional and can be left empty. |
| TargetType | String | No | MySQL | To create a quota for ApsaraDB RDS, specify the name of the engine. Valid values: MySQL and SQLServer. This parameter is optional and can be left empty for other services. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| data | Struct |   | The response. |
| allocateVPC | Integer | 1 | The number of allocated virtual private clouds (VPCs). |
| cluster | String | cn-qingdao-env17- d01 | The cluster. |
| ctime | Float | 1608519825999 | The creation time. |
| dtFlag | Boolean | false | The DTCenter flag. |
| id | Integer | 1 | The ID of the primary key. |
| quotaType | String | organization | The type of the quota. |
| quotaTypeId | Integer | 1 | The ID of the quota. |
| region | String | cn-qingdao-env17- d01 | The region. |
| targetType | String | mysql | The type of the cluster. |
| totalVPC | Integer | 10 | The total number of VPCs. |
| usedVPC | Integer | 1 | The number of used VPCs. |
| message | String | 200 | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |

| requestId | String | 111 | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```json
http(s)://[Endpoint]/? Action=CreateQuota &ProductName=ECS &QuotaBody={"totalCpu":100,"totalMem":100,"totalGpu":100, "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100} &QuotaType=organization &QuotaTypeId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <quotaType>organization</quotaType>
    <cluster>cn-qingdao-env17-d01</cluster>
    <totalVPC>10</totalVPC>
    <dtFlag>false</dtFlag>
    <quotaTypeId>1</quotaTypeId>
    <usedVPC>1</usedVPC>
    <ctime>1608519825999</ctime>
    <allocateVPC>1</allocateVPC>
    <targetType>mysql</targetType>
    <id>1</id>
    <region>cn-qingdao-env17-d01</region>
</data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "quotaType": "organization",
        "cluster": "cn-qingdao-env17-d01",
        "totalVPC": "10",
        "dtFlag": "false",
        "quotaTypeId": "1",
        "usedVPC": "1",
        "ctime": "1608519825999",
        "allocateVPC": "1",
        "targetType": "mysql",
        "id": "1",
        "region": "cn-qingdao-env17-d01"
```

`},`

```json
    "success": "true",
    "requestId": "111",
    "pureListData": "false",
    "message": "200"
```

`}`

##### 4.3.2.2 DescribeGpdbModifiableInstanceType

You can call this operation to query the AnalyticDB for PostgreSQL instance types that can be upgraded or downgraded.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGpdbM odifiableInstanc eType | The operation that you want to perform. Set the value to DescribeGpdbModifiableInstanceTyp e. |
| instanceId | String | Yes | sdfsdfsdfsfdsdf | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |
| result | Array of dataItem |   | The collection of results. |
| baseVersion | String | 3.13 | The version of the instance type. |

| cpu | String | 1 | The number of vCPUs. |
|---|---|---|---|
| engineVersion | String | 5.6 | The engine version of the instance. |
| gmtCreate | String | 2020-12-23 19:08:15 | The creation time. |
| gmtModified | String | 2020-12-23 19:08:15 | The modification time. |
| label | String | "" | Indicates whether the field is internationalized. Valid values: true and false. |
| memory | String | 4 | The memory size. |
| node | String | "" | The node. |
| regionId | String | cn-qingdao-env66- d01 | The ID of the region. |
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

`JSON` format `{`

```json
    "data": {
        "result": [
```

`{`

```json
                "engineVersion": "5.6",
                "gmtModified": "2020-12-23 19:08:15",
                "memory": "4",
                "baseVersion": "3.13",
                "cpu": "1",
                "specification": "gdb.r.13xlarge",
                "specFrom": "system",
                "storage": "20",
                "label": """",
                "gmtCreate": "2020-12-23 19:08:15",
                "node": """",
                "regionId": "cn-qingdao-env66-d01",
                "status": "Available",
                "resourceType": "GDB"
```

`}` `],`

```json
        "success": "true",
        "status": "200"
```

`},`

```json
    "host": """",
    "status": "200"
```

`}`

##### 4.3.2.3 UpdateQuota

You can call this operation to update a quota.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateQuota | The operation that you want to perform. Set the value to UpdateQuota. |
| ProductName | String | Yes | ECS | The name of the service. Valid values: ECS, OSS, VPC, RDS, SLB, ODPS, and EIP. |

| QuotaBody | Json | Yes | {"totalCpu":100, "totalMem":100, "totalGpu":100, "totalDisk cloud _ ssd":100,"total _ Disk cloud effici _ _ ency":100} | The parameters of the quota to update. The parameters vary with the specific service. ECS: {"totalCpu":100,"totalMem":10 0,"totalGpu":100,"totalDisk c _ loud ssd":100,"totalDisk clou _ _ d efficiency":100} _ OSS: {"totalAmount":100} VPC: {"totalVPC":100} RDS: {"totalCpu":100,"totalMem":10 0,"totalDisk":100} SLB: {"totalVipInternal":100,"tota lVipPublic":100} ODPS: {"totalCu":100,"totalDisk":10 0} EIP: {"totalEIP":100} |
|---|---|---|---|---|
| QuotaType | String | Yes | organization | The type of the quota. Valid values: organization and resourceGroup. |
| QuotaTypeId | Integer | Yes | 1 | The ID of the quota type. Specify an organization ID when the QuotaType parameter is set to organization. Specify a resource set ID when the QuotaType parameter is set to resourceGroup. |
| RegionName | String | Yes | cn-*******-****- d01 | The region name. |
| RequestId | String | No | 84319b92-835e- 4aeb-9190- 0c12c9****** | The ID of the request. |

| ClusterName | String | No | TEST | The name of the cluster. This reserved parameter is optional and can be left empty. |
|---|---|---|---|---|
| TargetType | String | No | MySQL |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| data | Struct |   | The response. |
| allocateVPC | Integer | 1 | The number of allocated virtual private clouds (VPCs). |
| cluster | String | cn-qingdao-env17- d01 | The cluster. |
| ctime | Float | 1608519825999 | The creation time. |
| dtFlag | Boolean | false | The DTCenter flag. |
| id | Integer | 1 | The ID of the primary key. |
| quotaType | String | organization | The type of the quota. |
| quotaTypeId | Integer | 1 | The ID of the quota. |
| region | String | cn-qingdao-env17- d01 | The region. |
| targetType | String | mysql | The type of the cluster. |
| totalVPC | Integer | 10 | The total number of VPCs. |
| usedVPC | Integer | 1 | The number of used VPCs. |
| message | String | 200 | The message. |

| pureListData | Boolean | false | Indicates whether only data is returned. |
|---|---|---|---|
| redirect | Boolean | false | Indicates whether redirections are performed. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```json
http(s)://[Endpoint]/? Action=UpdateQuota &ProductName=ECS &QuotaBody={"totalCpu":100,"totalMem":100,"totalGpu":100, "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100} &QuotaType=organization &QuotaTypeId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <quotaType>organization</quotaType>
    <cluster>cn-qingdao-env17-d01</cluster>
    <totalVPC>10</totalVPC>
    <dtFlag>false</dtFlag>
    <quotaTypeId>1</quotaTypeId>
    <usedVPC>1</usedVPC>
    <ctime>1608519825999</ctime>
    <allocateVPC>1</allocateVPC>
    <targetType>mysql</targetType>
    <id>1</id>
    <region>cn-qingdao-env17-d01</region>
</data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "quotaType": "organization",
        "cluster": "cn-qingdao-env17-d01",
        "totalVPC": "10",
        "dtFlag": "false",
        "quotaTypeId": "1",
        "usedVPC": "1",
        "ctime": "1608519825999",
        "allocateVPC": "1",
        "targetType": "mysql",
        "id": "1",
        "region": "cn-qingdao-env17-d01"
```

`},`

```json
    "success": "true",
    "requestId": "111",
    "pureListData": "false",
    "message": "200"
```

`}`

##### 4.3.2.4 DeleteQuota

Deletes a quota.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/quota/delete HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| quotaTypeId | Integer | Body | No | 10 | The ID of the quota type. |
| quotaType | String | Body | No | organization | The type of the quota. |
| productName | String | Body | No | rds | The name of the service. |
| regionName | String | Body | No | regionName | The name of the zone. |

| clusterName | String | Body | No | clusterName | The name of the cluster. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| message | String | 200 | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |
| requestId | String | 111 | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteQuota &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "requestId": "111",
    "pureListData": "false",
    "message": "200"
```

`}`

##### 4.3.2.5 GetQuota

Queries a quota.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/quota/query HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| quotaType | String | Body | No | organization | The type of the quota. |
| quotaTypeId | Integer | Body | No | 3 | The ID of the quota type. |
| productName | String | Body | No | RDS | The name of the service. |
| regionName | String | Body | No | regionName | The name of the zone. |
| clusterName | String | Body | No | clusterName | The name of the cluster. |
| targetType | String | Body | No | MySQL | The database type of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |

| cost | Integer | 1000 | The amount of time consumed by the operation. |
|---|---|---|---|
| data | Struct |   | The response data. |
| allocateAmoun t | Integer | 1 | The number of allocated quotas. |
| allocateCpu | Integer | 1 | The number of allocated CPUs. |
| allocateCu | Integer | 1 | The number of allocated CUs. |
| allocateDisk | Integer | 100 | The amount of allocated capacity of disks. |
| allocateDisk cl _ oud efficiency _ | Integer | 100 | The amount of allocated capacity of ultra disks. |
| allocateDisk cl _ oud ssd _ | Integer | 100 | The amount of allocated capacity of standard SSDs. |
| allocateGpu | Integer | 100 | The number of allocated GPUs. |
| allocateHAVIP | Integer | 5 | The number of allocated high-availability virtual IP addresses (HAVIPs). |
| allocateMQ | Integer | 5 | The number of allocated Message Queue instances. |
| allocateMem | Integer | 100 | The amount of allocated memory. |
| allocateVPC | Integer | 1 | The number of allocated VPCs. |
| allocateVipInte rnal | Integer | 1 | The number of allocated private virtual IP addresses (VIPs) . |
| allocateVipPub lic | Integer | 1 | The number of allocated public VIPs. |
| cluster | String | cn-qingdao-env17- d01 | The cluster. |
| ctime | Float | 1608519825999 | The time when the quota was created. |

| cuserId | String | admin | The creator. |
|---|---|---|---|
| dtFlag | Boolean | false | The DTCenter flag. |
| id | Integer | 1 | The primary key. |
| muserId | String | admin | The modifier. |
| quotaType | String | organization | The type of the quota. |
| quotaTypeId | Integer | 1 | The ID of the quota type. |
| region | String | cn-qingdao-env17- d01 | The zone. |
| targetType | String | mysql | The database type of the cluster. |
| totalAmount | Integer | 10 | The total number of quotas. |
| totalCpu | Integer | 1 | The total number of CPUs. |
| totalCu | Integer | 1 | The total number of CUs. |
| totalDisk | Integer | 100 | The total amount of capacity of disks. |
| totalDisk clou _ d efficiency _ | Integer | 100 | The total amount of capacity of ultra disks. |
| totalDisk clou _ d ssd _ | Integer | 100 | The total amount of capacity of standard SSDs. |
| totalGpu | Integer | 100 | The total number of GPUs. |
| totalHAVIP | Integer | 1 | The total number of HAVIPs. |
| totalMQ | Integer | 1 | The total number of Message Queue instances. |
| totalMem | Integer | 100 | The total amount of memory. |
| totalVPC | Integer | 1 | The total number of VPCs. |

| totalVipInterna l | Integer | 1 | The total number of private VIPs. |
|---|---|---|---|
| totalVipPublic | Integer | 1 | The total number of public VIPs. |
| usedAmount | Integer | 1 | The number of used quotas. |
| usedCpu | Integer | 1 | The number of used CPUs. |
| usedCu | Integer | 1 | The number of used CUs. |
| usedDisk | Integer | 100 | The amount of used capacity of disks. |
| usedDisk clou _ d efficiency _ | Integer | 100 | The amount of used capacity of ultra disks. |
| usedDisk clou _ d ssd _ | Integer | 100 | The amount of used capacity of standard SSDs. |
| usedGpu | Integer | 1 | The number of used GPUs. |
| usedHAVIP | Integer | 1 | The number of used HAVIPs. |
| usedMQ | Integer | 1 | The number of used Message Queue instances. |
| usedMem | Integer | 100 | The amout of used memory. |
| usedVPC | Integer | 1 | The number of used VPCs. |
| usedVipIntern al | Integer | 1 | The number of used private VIPs. |
| usedVipPublic | Integer | 1 | The number of used public VIPs. |
| message | String | 200 | The message. |
| pureListData | Boolean | false | Indicates whether only data is returned. |
| redirect | Boolean | false | Indicates whether the request is redirected. |

| requestId | String | 111 | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetQuota &ProductName=ECS &QuotaType=organization &QuotaTypeId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <usedVipInternal>1</usedVipInternal>
    <allocateDisk_cloud_ssd>100</allocateDisk_cloud_ssd>
    <muserId>admin</muserId>
    <cluster>cn-qingdao-env17-d01</cluster>
    <allocateVipPublic>1</allocateVipPublic>
    <totalVipInternal>1</totalVipInternal>
    <usedAmount>1</usedAmount>
    <allocateAmount>1</allocateAmount>
    <totalDisk_cloud_efficiency>100</totalDisk_cloud_efficiency>
    <usedMQ>1</usedMQ>
    <allocateCu>1</allocateCu>
    <totalDisk>100</totalDisk>
    <totalVPC>1</totalVPC>
    <usedDisk_cloud_ssd>100</usedDisk_cloud_ssd>
    <totalDisk_cloud_ssd>100</totalDisk_cloud_ssd>
    <totalCpu>1</totalCpu>
    <usedVPC>1</usedVPC>
    <ctime>1608519825999</ctime>
    <totalCu>1</totalCu>
    <usedGpu>1</usedGpu>
    <id>1</id>
    <allocateMem>100</allocateMem>
    <cuserId>admin</cuserId>
    <allocateDisk_cloud_efficiency>100</allocateDisk_cloud_efficiency>
    <allocateDisk>100</allocateDisk>
    <usedCpu>1</usedCpu>
    <totalGpu>100</totalGpu>
    <allocateMQ>5</allocateMQ>
    <totalVipPublic>1</totalVipPublic>
    <quotaTypeId>1</quotaTypeId>
<totalMQ>1</totalMQ>
```

```xml
    <totalMQ>1</totalMQ>
    <usedCu>1</usedCu>
    <usedVipPublic>1</usedVipPublic>
    <totalMem>100</totalMem>
    <allocateVipInternal>1</allocateVipInternal>
    <allocateVPC>1</allocateVPC>
    <allocateGpu>100</allocateGpu>
    <targetType>mysql</targetType>
    <usedDisk>100</usedDisk>
    <usedMem>100</usedMem>
    <allocateCpu>1</allocateCpu>
    <usedDisk_cloud_efficiency>100</usedDisk_cloud_efficiency>
    <totalAmount>10</totalAmount>
    <quotaType>organization</quotaType>
    <allocateHAVIP>5</allocateHAVIP>
    <dtFlag>false</dtFlag>
    <totalHAVIP>1</totalHAVIP>
    <usedHAVIP>1</usedHAVIP>
    <region>cn-qingdao-env17-d01</region>
</data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": {"usedVipInternal":"1","allocateDisk_cloud_ssd":"100","muserId":"admin","cluster":"cn-q ingdao-env17d01","allocateVipPublic":"1","totalVipInternal":"1","usedAmount":"1","allocateAmount":"1" totalDisk_cloud_efficiency":"100","usedMQ":"1","allocateCu":"1","totalDisk":"100","totalV ":"1","usedDisk_cloud_ssd":"100","totalDisk_cloud_ssd":"100","totalCpu":"1","usedVPC":"1" ctime":"1608519825999","totalCu":"1","usedGpu":"1","id":"1","allocateMem":"100","cuserId" admin","allocateDisk_cloud_efficiency":"100","allocateDisk":"100","usedCpu":"1","totalGpu "100","allocateMQ":"5","totalVipPublic":"1","quotaTypeId":"1","totalMQ":"1","usedCu":"1", sedVipPublic":"1","totalMem":"100","allocateVipInternal":"1","allocateVPC":"1","allocateG ":"100","targetType":"mysql","usedDisk":"100","usedMem":"100","allocateCpu":"1","usedDisk loud_efficiency":"100","totalAmount":"10","quotaType":"organization","allocateHAVIP":"5", tFlag":"false","totalHAVIP":"1","usedHAVIP":"1","region":"cn-qingdao-env17d01"},"success":"true","requestId":"111","pureListData":"false","message":"200"}
```

##### 4.3.2.6 MeteringQuery

You can call this operation to query the metering data.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | MeteringQuery | The operation that you want to perform. Set the value to MeteringQuery. |
|---|---|---|---|---|
| startTime | String | Yes | 2019-10- 10T00:00:00Z | The start of the time range for the query. The time must be in UTC. |
| endTime | String | Yes | 2019-10- 10T01:00:00Z | The end of the time range for the query. The time must be in UTC. |
| orgId | String | Yes | 1 | The ID of the organization. |
| pageSize | Integer | No | 500 | The number of entries to return on each page. Maximum value: 1000. |
| productName | String | Yes | ECS | The name of the service. Valid values: ECS, OSS, RDS, SLB, EIP, and VPC. |
| isParentId | Integer | Yes | 0 | A value of 1 specifies that the metering data of subordinate organizations under this organization is returned. If you do not specify this parameter or set the parameter to a value other than 1, only the metering data of this organization is returned. |
| resourceGId | String | No | test | The metering data of the specified resource set. By fault, if this parameter is empty or not specified, the metering data of all the resource sets in the specified organization is queried. Note If refined query is not required, we recommend that you do not specify the resourceGId, region, and insId parameters. You can query all the metering data of the specified organization to improve efficiency. |

| region | String | No | test | The metering data of the specified cluster. Note If refined query is not required, we recommend that you do not specify the resourceGId, region, and insId parameters. You can query all the metering data of the specified organization to improve efficiency. |
|---|---|---|---|---|
| insId | String | No | test | The metering data of the specified instance. Note If refined query is not required, we recommend that you do not specify the resourceGId, region, and insId parameters. You can query all the metering data of the specified organization to improve efficiency. |
| token | String | No | test | The token returned as an offset when the data volume to be queried is greater than the value of the pageSize parameter. You can query the data of the next page after you enter the token for the next request. You can ignore this parameter or enter an empty string for the first query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The returned status code. |
| cost | Integer | 1000 | The time consumed by the operation. |
| message | String | success | The returned information. |
| requestId | String | sddsdsd | The ID of the request. |
| success | Normal | true | Indicates whether the call was successful. |

| token | String | {"InsId":"i- 9fx013f0ueoh5fzc8 yww","Pos":"ECS 0 _ 000000003 2000- _ 01- 01T01:00:00Z","Re sourceGId":"2","Re gionId":"cn- qingdao-env-d01"} | The token used to query data by page. You can query the data of the next page after you enter the token for the next request. |
|---|---|---|---|
| total | Integer | 100 | The amount of data returned for this query. |
| data | String |   | The response. |
| Pos | String | ECS 0000000003 _ _ 2000-01- 01T01:00:00Z | The primary key of the metering data. The primary key consists of the service name, organization ID, and start time. |
| OrgName | String | test | The name of the organization. |
| ResourceGId | Integer | test | The ID of the resource set. |
| ResourceGName | String | test | The name of the resource set. |
| InsId | String | i- h5i05vhigf256qxq mg4h | The ID of the instance. |
| RegionId | String | cn-qingdao-env3b- d02 | The ID of the region. |
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
```

```json
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

`}` `],`

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

`}`

##### 4.3.2.7 SelectCommonSpec

Queries the specifications of a service based on a filter condition.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/commonSpec/select HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| Action | String | Quer y | Yes | SelectCommo nSpec | The operation that you want to perform. Set the value to SelectCommonSpec. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The response data. |
| result | Array of dataItem |   | The collection of results. |
| dataItem |   |   |   |
| baseVersion | String | 3.13 | The version of the specifications. |
| gmtCreate | String | 2019-10-27 17:47:27 | The time when the specifications were created. |

| gmtModified | String | 2019-10-27 17:47:27 | The time when the specifications were modified. |
|---|---|---|---|
| pageOrder | String | 1 | The page order. |
| pageSize | Integer | 5 | The number of entries returned per page. |
| pageSort | String | null | The sorting of pages. |
| pageStart | Integer | 1 | The page number of the returned page. Pages start from 1. |
| regionId | String | cn-qingdao-env66- d01 | The ID of the zone. |
| resourceType | String | RDS | The type of the resource. |
| specFrom | String | system | The source of the specifications. |
| status | String | Available | Indicates whether the specifications are available. |
| status | Integer | 200 | The HTTP status code returned. |
| success | String | true | Indicates whether the call is successful. |
| host | String | "" | This parameter is deprecated. |
| status | Integer | 200 | The HTTP status code returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SelectCommonSpec &<Common request parameters>
```

Sample success responses `XML` format

```xml
<data>
    <result>
        <gmtModified>2019-10-27 17:47:27</gmtModified>
        <pageOrder>1</pageOrder>
        <pageSort>null</pageSort>
        <regionId>cn-qingdao-env66-d01</regionId>
        <baseVersion>3.13</baseVersion>
        <pageStart>1</pageStart>
        <pageSize>5</pageSize>
        <specFrom>system</specFrom>
        <gmtCreate>2019-10-27 17:47:27</gmtCreate>
        <status>Available</status>
        <resourceType>RDS</resourceType>
    </result>
    <success>true</success>
    <status>200</status>
</data> <host>""</host> <status>200</status>
```

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

`}` `],`

```json
        "success": "true",
        "status": "200"
```

`},`

```json
    "host": "\"\"",
    "status": "200"
```

`}`

##### 4.3.2.8 AddCommonSpec

Adds custom specifications.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/commonSpec/add HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| status | String | Body | No | Available | The status of the specifications. |
| specName | String | Body | No | Enhanced Enterprise Edition | The name of the specifications. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The response data. |
| validationInfo | String | "" | The verification identiifier. |
| code | String | 200 | The HTTP status code. |
| httpOk | Boolean | true | Indicates whether the call is successful. Valid values: true and false. |
| ip | String | "" | The IP address. |
| message | String | success | The message. |
| requestId | String | 0a1ec3c21608775 9426241251d02bd | The ID of the request. |
| success | Boolean | true | Indicates whether the call is successful. |
| eagleEyeTrace Id | String | "" |   |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddCommonSpec &resourceType=RDS &specName=Enhanced Enterprise Edition &status=Available &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <success>true</success>
    <validationInfo>""</validationInfo>
</data> <httpOk>true</httpOk> <requestId>0a1ec3c216087759426241251d02bd</requestId> <success>true</success> <ip>""</ip> <message>success</message>
```

`JSON` format `{`

```json
    "code": "200",
    "data": {
        "success": "true",
        "validationInfo": """"
```

`},`

```json
    "httpOk": "true",
    "requestId": "0a1ec3c216087759426241251d02bd",
    "success": "true",
    "ip": """",
    "message": "success"
```

`}`

##### 4.3.2.9 UpdateCommonSpecStatus

You can call this operation to enable or disable specifications.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateCommon SpecStatus | The operation that you want to perform. Set the value to UpdateCommonSpecStatus. |
| ids | String | Yes | 1 | The IDs of the specifications. |

| status | String | Yes | Unavailable | The status. Valid values: Available and Unavailable. |
|---|---|---|---|---|

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

Sample success responses `XML` format

```xml
<code>200</code> <data>200</data> <success>true</success> <message>success</message>
```

`JSON` format `{`

```json
    "code": "200",
    "data": "200",
    "success": "true",
    "message": "success"
```

`}`

##### 4.3.2.10 BillQuery

Queries the bills of cloud services. You can query the bills of the following services: Elastic Compute Service (ECS) Object Storage Service (OSS) Server Load Balancer (SLB) Elastic IP Address (EIP) Virtual Private Cloud (VPC) ApsaraDB RDS Apsara File Storage NAS PolarDB-X V1.0 AnalyticDB for MySQL V3.0 Message Queue (MQ) Elastic Block Storage (EBS) Snapshot ApsaraDB for HBase Time Series Database (TSDB) AnalyticDB for MySQL V2.0

**Request headers**

This operation uses only common request headers. For more information, see Common request headers.

**Request syntax**

```
POST /ascm/billing/billing/web/query/public HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| billingCycle | String | Body | Yes | 2020-03 | The billing period. Note This parameter is required when the cycleType parameter is set to Monthly. Specify this parameter in the YYYY- MM format. |

|   |   | MM |
|---|---|---|

| cycleType | String | Body | Yes | Monthly | The time dimension of bills. Monthly: You can use this parameter only with the billingCycle parameter to query the bills of the instance within one month. Hourly: queries the bills of the instance by hour. The maximum query period is seven days. |
|---|---|---|---|---|---|
| endTime | String | Body | Yes | 2021-04- 14T08:14:16Z | The end time of the billing period. Note This parameter is required when the cycleType parameter is set to Daily or Hourly. Specify this parameter in the yyyy-MM- dd'T'HH:mm:ss'Z' format. |
| groupByType | String | Body | Yes | organization | instance: the sum of all billable items for an instance. organization: the bills for each service in an organization. orgAllProduct: the bills for all services in an organization. resourceSet: the bills for each service in a resource set. resAllProduct: the bills for all services in a resource set. product: the bills of a service. region: the bills for each service in a region. |
| startTime | String | Body | Yes | 2021-04- 13T07:14:16Z | The start time of the billing period. Note This parameter is required when the cycleType parameter is set to Daily or Hourly. Specify this parameter in the yyyy-MM- dd'T'HH:mm:ss'Z' format. |
| orgId | String | Body | No | 1 | The organization ID of the instance. Note The ID of the root organization is 1. You must specify a number greater than 1. |

|   |   |   | yyyy-MM- |   |
|---|---|---|---|---|
|   |   | dd'T'HH:mm:ss'Z' |   |   |

|   |   |   | yyyy-MM- |   |
|---|---|---|---|---|
|   |   | dd'T'HH:mm:ss'Z' |   |   |

| resourceSetId | String | Body | No | 1 | The resource set ID of the instance. Note If you specify this parameter, you must specify the ID of the resource set that corresponds to the orgId parameter. |
|---|---|---|---|---|---|
| productName | String | Body | No | RDS | The code of the service. |

|   |   |   |   |   | Note ECS: Elastic Compute Service OSS: Object Storage Service SLB: Server Load Balancer EIP: Elastic IP Address VPC: Virtual Private Cloud RDS: ApsaraDB RDS OTS: Tablestore DRDS: PolarDB-X V1.0 REDIS: ApsaraDB for Redis ADB: AnalyticDB for MySQL V3.0 GPDB: AnalyticDB for |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | Note ECS: Elastic Compute Service OSS: Object Storage Service SLB: Server Load Balancer EIP: Elastic IP Address VPC: Virtual Private Cloud RDS: ApsaraDB RDS OTS: Tablestore DRDS: PolarDB-X V1.0 REDIS: ApsaraDB for Redis ADB: AnalyticDB for MySQL V3.0 GPDB: AnalyticDB for |   |
| region | String | Body | No | cn-qingdao- ****-d01 |   | PostgreSQL The regionD IDDS o: fA tphsea rinasDtBa nfocer. MongoDB |   |
| insId | String | Body | No | am- z0ys4bh35jjmt 54g8 |   | ONS: Message Queue RDS POSTGRESQL: The ID of the i_nstance. ApsaraDB RDS for PostgreSQL |   |
| pageSize | Integer | Body | No | 20 |   | RDS SQLSERVER: _ The numbAepr soaf reanDtBri eRsD tSo froerturn on each paSgQeL. STehrev edrefault value is 20. SLS: Log Service |   |
|   |   |   |   | CAESEgoQCg4 |   | EBS: Elastic Block Storage The token that is used to display |   |
| token | String | Body | No | KCmdtdF9jcm VhdGUEARgBI kgKCQBwhGm PcAEAAAo7Az YAAAAxTDgw MDcxMjg3ZDJ hNmM3ZDguT DgwMDAwMD AwMDAwMzE1 MTIuTDgwMDc yZDMyZTJkYzg 3N2U |   | the returnSeNd AtPaSgHs OonT :m Sunlatpipslheot pages. DeEfaSuSl:t Avuatluoe S: c2a0li npgages. The token is contained in the HBASE: ApsaraDB for returned value. HBase |   |
|   |   |   |   |   |   | CLOUDAPI:API Note If the cycleType Gateway parameter is set to Daily or Hourly, TthSeD Bto: kTeimn eis Series containeDda tianb tahsee returned value. YAoDuS c:a Ann uaslyet itchDeB t ofokren to queryM tyhSeQ nLe Vx2t .p0age. |   |
| isParentId | Integer | Body | No | 1 | Specifies whether to return the bill data of the sub-organizations. 1: yes 0: no |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
| cost | Integer | 9 | The amount of time consumed by the operation. Unit: milliseconds. Note If the time consumed from the request to the response of an operation called by using ASAPI exceeds 10 seconds, the operation times out. |
| data | Array of data |   | Details about bills |
| billCycle | String | 2021-12 | The billing period. |
| billingChan | String | "" | The ID chain of each billing model. Note Example: Billable item 1 - Billable item 2 - Billing rule ID - Billing policy ID - Billing plan ID |
| billingTime | String | 2021-03- 17T05:08:55Z | The billing time. |
| currency | String | CNY | The billing currency. Note Only CNY is supported. |
| cycleType | String | Monthly | The billing cycle. |
| discountPrice | Float | 0.00 | The discounted price. |
| endTime | String | 2021-03- 15T16:00:00Z | The time when data collection ends. |
| groupByType | String | product | The grouping type. |
| insId | String | r-dmkwqoxb14e | The ID of the instance. |
| modifiedBy | String | 5003 | The ID of the last modifier of the bill. |
| modifiedTime | String | 1606675230000 | The time when the bill was last modified. |
| orgId | String | 1 | The organization ID of the instance. |

| orgName |   | String | test |   | The organization name of the instance. |   |
|---|---|---|---|---|---|---|
| originalPrice |   | Float | 3439217.00 |   | The original price of the bill. |   |
| payType |   | String | monthlyPay |   | The billing method of the bill. postPay: pay-as-you-go monthlyPay: monthly subscription |   |
| price |   | Float | 3370432.66 |   | The actual price of the bill. The actual price is calculated by using the following formula: Value of the price |   |
|   |   |   |   |   |   | Value of the price |
|   |   |   |   | 3370432.66 | parameter = Value of the |   |
|   |   |   |   |   | originalPrice parameter - Value of |   |
|   |   |   |   |   | the discountPrice parameter |   |
| product |   | String | RDS |   | The code of the service. |   |
| regionId |   | String | cn-qingdao-****- d01 |   | The region ID of the instance. |   |
| resourceGid |   | String | 1 |   | The resource set ID of the instance. |   |
| resourceGroup Name |   | String | testres |   | The name of the resource set to which the instance belongs. |   |
| startTime |   | String | 2021-02- 28T16:00:00Z |   | The start time for billing data collection. |   |
| errorCode |   | String | ascm billing Misse _ _ dArgument Produc _ tNotExist |   | The error code when the bill fails to be generated. |   |
| errorMessage |   | String | You must specify a service. |   | The error message when the bill fails to be generated. |   |
| message |   | String | success |   | The additional information returned. |   |
| pageSize |   | Integer | 20 |   | The number of entries returned per page. |   |
| requestId |   | String | 0a42b84c1615963 6344661720d8507 |   | The ID of the request. |   |

| success | Boolean | true | Indicates whether the call is successful. true false |
|---|---|---|---|
| token | String | CAESEgoQCg4KCm dtdF9jcmVhdGUEA RgBIkgKCQBwhGm PcAEAAAo7AzYAAA AxTDgwMDcxMjg3 ZDJhNmM3ZDguTD gwMDAwMDAwMD AwMzE1MTIuTDgw MDcyZDMyZTJkYzg 3N2U | The token that is used to display the returned tags on multiple pages. |

**Examples**

Sample requests

```
POST /ascm/billing/billing/web/query/public HTTP/1.1 Common request header
```

`{`

```json
    "orgId":1,
    "cycleType":"Monthly",
    "groupByType":"organization",
    "billingCycle":"2022-03"
```

`}` Sample success responses `XML` format

```xml
<cost>9</cost> <code>200</code> <data>
    <modifiedTime>1606675230000</modifiedTime>
    <resourceGid>1</resourceGid>
    <product>RDS</product>
    <resourceGroupName>testres</resourceGroupName>
    <orgName>test</orgName>
    <originalPrice>3439217.00</originalPrice>
    <billingTime>2021-03-17T05:08:55Z</billingTime>
    <discountPrice>0.00</discountPrice>
    <groupByType>product</groupByType>
    <orgId>1</orgId>
    <cycleType>Monthly</cycleType>
    <insId>r-dmkwqoxb14e</insId>
    <payType>monthlyPay</payType>
    <billingChan>""</billingChan>
    <regionId>cn-qingdao-****-d01</regionId>
    <price>3370432.66</price>
    <modifiedBy>5003</modifiedBy>
    <startTime>2021-02-28T16:00:00Z</startTime>
    <currency>CNY</currency>
    <endTime>2021-03-15T16:00:00Z</endTime>
    <billCycle>2021-12</billCycle>
</data> <success>true</success> <requestId>0a42b84c16159636344661720d8507</requestId> <errorMessage>You must specify a service.</errorMessage> <pageSize>20</pageSize> <errorCode>ascm_billing_MissedArgument_ProductNotExist</errorCode> <message>success</message> <token>CAESEgoQCg4KCmdtdF9jcmVhdGUEARgBIkgKCQBwhGmPcAEAAAo7AzYAAAAxTDgwMDcxMjg3ZDJhNmM3ZD TDgwMDAwMDAwMDAwMzE1MTIuTDgwMDcyZDMyZTJkYzg3N2U</token>
```

`JSON` format `{`

```json
    "cost": 9,
    "code": 200,
    "data": {
        "modifiedTime": 1606675230000,
        "resourceGid": 1,
        "product": "RDS",
        "resourceGroupName": "testres",
        "orgName": "test",
        "originalPrice": 3439217,
        "billingTime": "2021-03-17T05:08:55Z",
        "discountPrice": 0,
        "groupByType": "product",
        "orgId": 1,
        "cycleType": "Monthly",
        "insId": "r-dmkwqoxb14e",
        "payType": "monthlyPay",
        "billingChan": "\"\"",
        "regionId": "cn-qingdao-****-d01",
        "price": 3370432.66,
        "modifiedBy": 5003,
        "startTime": "2021-02-28T16:00:00Z",
        "currency": "CNY",
        "endTime": "2021-03-15T16:00:00Z",
        "billCycle": "2021-12"
```

`},`

```json
    "success": true,
    "requestId": "0a42b84c16159636344661720d8507",
    "errorMessage": "You must specify a service.",
    "pageSize": 20,
    "errorCode": "ascm_billing_MissedArgument_ProductNotExist",
    "message": "success",
    "token":
"CAESEgoQCg4KCmdtdF9jcmVhdGUEARgBIkgKCQBwhGmPcAEAAAo7AzYAAAAxTDgwMDcxMjg3ZDJhNmM3ZDguTDgw AwMDAwMDAwMzE1MTIuTDgwMDcyZDMyZTJkYzg3N2U"
```

`}`

#### 4.3.3 Cloud services

##### 4.3.3.1 DescribeModifiableInstanceType

You can call this operation to query the Elastic Compute Service (ECS) instance types that can be upgraded or downgraded.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeModifia bleInstanceType | The operation that you want to perform. Set the value to DescribeModifiableInstanceType. |
|---|---|---|---|---|
| destinationReso urce | String | Yes | sfdsf | Set the value to instanceType. |
| instanceId | String | Yes | sfdsfsfdsfsfdsf | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |
| result | Array of dataItem |   | The collection of data. |
| baselineCredit | Integer | 1 | The baseline vCPU computing performance (overall computing performance of all vCPUs) of the t5 or t6 burstable instance family. |
| cpuCoreCount | Integer | 1 | The number of vCPUs. |
| eniPrivateIpAd dressQuantity | Integer | 2 | The maximum number of private IP addresses per elastic network interface (ENI). |
| eniQuantity | Integer | 2 | The maximum number of ENIs that can be bound to an instance. |
| gPUAmount | Integer | 0 | The number of GPUs. |
| gPUSpec | String | "" | The GPU specifications. |
| initialCredit | Integer | 1 | The initial vCPU credits of the t5 or t6 burstable instance family. |
| instanceBand widthRx | Integer | 1 | The maximum inbound internal bandwidth. Unit: Kbit/s. |
| instanceBand widthTx | Integer | 1 | The maximum outbound internal bandwidth. Unit: Kbit/s. |

| instanceFamil yLevel | String | EnterpriseLevel | The level of the instance family. |
|---|---|---|---|
| instancePpsRx | Long | 1 | The inbound packet forwarding rate over the internal network. Unit: pps. |
| instancePpsTx | Long | 1 | The outbound packet forwarding rate over the internal network. Unit: pps. |
| instanceTypeF amily | String | ecs.sn2.large | The instance family. |
| instanceTypeI d | String | ecs.sn2.large | The ID of the instance type. |
| localStorageA mount | Integer | 1 | The number of local disks attached per instance. |
| localStorageC apacity | Long | 2000 | The capacity of each local disk attached per instance. Unit: GiB. |
| localStorageC ategory | String | 2000 | The capacity of each local disk attached per instance. Unit: GiB. |
| memorySize | Integer | 4 | The amount of memory. Unit: GiB. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeModifiableInstanceType &destinationResource=sfdsf &instanceId=sfdsfsfdsfsfdsf &<Common request parameters>
```

Sample success responses `XML` format

```xml
<data>
    <result>
        <instancePpsTx>1</instancePpsTx>
        <instanceTypeFamily>ecs.sn2.large</instanceTypeFamily>
        <localStorageCapacity>2000</localStorageCapacity>
        <instanceTypeId>ecs.sn2.large</instanceTypeId>
        <instancePpsRx>1</instancePpsRx>
        <cpuCoreCount>1</cpuCoreCount>
        <initialCredit>1</initialCredit>
        <localStorageAmount>1</localStorageAmount>
        <gPUAmount>0</gPUAmount>
        <memorySize>4</memorySize>
        <instanceFamilyLevel>EnterpriseLevel</instanceFamilyLevel>
        <eniQuantity>2</eniQuantity>
        <instanceBandwidthRx>1</instanceBandwidthRx>
        <eniPrivateIpAddressQuantity>2</eniPrivateIpAddressQuantity>
        <localStorageCategory>2000</localStorageCategory>
        <instanceBandwidthTx>1</instanceBandwidthTx>
        <baselineCredit>1</baselineCredit>
        <gPUSpec>""</gPUSpec>
    </result>
    <success>true</success>
    <status>200</status>
</data> <host>""</host> <status>200</status>
```

`JSON` format `{`

```json
    "data": {
        "result": [
```

`{`

```json
                "instancePpsTx": "1",
                "instanceTypeFamily": "ecs.sn2.large",
                "localStorageCapacity": "2000",
                "instanceTypeId": "ecs.sn2.large",
                "instancePpsRx": "1",
                "cpuCoreCount": "1",
                "initialCredit": "1",
                "localStorageAmount": "1",
                "gPUAmount": "0",
                "memorySize": "4",
                "instanceFamilyLevel": "EnterpriseLevel",
                "eniQuantity": "2",
                "instanceBandwidthRx": "1",
                "eniPrivateIpAddressQuantity": "2",
                "localStorageCategory": "2000",
                "instanceBandwidthTx": "1",
                "baselineCredit": "1",
                "gPUSpec": """"
```

`}` `],`

```json
        "success": "true",
        "status": "200"
```

`},`

```json
    "host": "\"\"",
    "status": "200"
```

`}`

##### 4.3.3.2 DescribeSeriesIdFamilies

Queries instance families.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/drdsSpec/describeSeriesIdFamilies HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| resourceType | String | Body | No | drds | The type of the resource. |

| status | String | Body | No | Available | The status of the resource. |
|---|---|---|---|---|---|
| label | String | Body | No | "" | The tag. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| api | String | "" | The information about the operation. |
| asapiRequestI d | String | "" | The ID of the request. |
| asapiSuccess | Boolean | true | Indicates whether the call is successful. |
| code | Integer | 200 | The HTTP status code. |
| data | Array of data |   | The result set. |
| creator | String | "" | The creator. |
| deleted | Boolean | true | Indicates whether the instance family is deleted. |
| gmtCreate | String | 2019-10-15 17:47:27 | The time when the instance family was created. |
| gmtModified | String | 2019-10-15 17:47:27 | The time when the instance family was modified. |
| isDeleted | String | "" | Indicates whether the instance family is deleted. |
| modifier | String | "" | The modifier. |
| orderBy | Struct |   | The sorting. |
| id | String | id | The ID. |
| pageOrder | String | desc | The sorting order. |

| pageSize | Integer | 5 | The number of entries returned per page. |
|---|---|---|---|
| pageSort | String | "" | The sorting of pages. |
| pageStart | Integer | 1 | The number of the start page. |
| resourceType | String | RDS | The type of the resource. |
| seriesId | String | drds.sn2.8c32g | The ID of the edition. |
| seriesName | String | High-availability Edition | The name of the edition. |
| seriesNameLa bel | String | Standard Edition | The label of the edition name. |
| domain | String | ascm.aliyuns.com | The domain name. |
| eagleEyeTrace Id | String | 0ab40ce81644981 3368341682e0020 | The EagleEye ID, which is used as a trace ID. |
| httpOk | Boolean | true | Indicates whether the call is successful. |
| message | String | "" | The message. |
| serverRole | String | "" | The name of the service in the request. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSeriesIdFamilies &<Common request parameters>
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

`JSON` format `{`

```json
    "serverRole": "",
    "eagleEyeTraceId": "0ab40ce816449813368341682e0020",
    "asapiSuccess": "true",
    "asapiRequestId": "",
    "code": "200",
    "data": [
```

`{`

```json
            "creator": "",
            "gmtModified": "2019-10-15 17:47:27",
            "seriesName": "",
            "modifier": "",
            "pageSize": "5",
            "gmtCreate": "",
            "seriesId": "drds.sn2.8c32g",
            "deleted": "",
            "pageOrder": "",
            "pageSort": "",
            "isDeleted": "",
            "pageStart": "1",
            "seriesNameLabel": "Standard Edition",
            "resourceType": "RDS",
            "orderBy": {
                "id": "id"
```

`}` `}` `],`

```json
    "httpOk": "true",
    "success": "true",
    "domain": "ascm.aliyuns.com",
    "api": "",
    "message": ""
```

`}`

##### 4.3.3.3 GroupCommonSpec

You can call this operation to query the valid values of the specifications-specific fields.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GroupCommonS pec | The operation that you want to perform. Set the value to GroupCommonSpec. |
| groupFiled | String | Yes | storageType | The field for which to query valid values. |

| resourceType | String | Yes | RDS | The resource type. |
|---|---|---|---|---|
| label | String | No | "" | The tag. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The dataset. |
| data | List | [ { "storageType":"Aut oTest Wn4MRxEkK _ K" }, { "storageType":"Aut oTest UZOBAEDvil _ " }, { "storageType":"Aut oTest 8WqAc6rtpp _ " }, { "storageType":"Aut oTest aCPiv2nIh3" _ }, { "storageType":"Sta ndard" }, { "storageType":"1" } ] | The collection of results. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=GroupCommonSpec &groupFiled=storageType &resourceType=RDS &<Common request parameters>
```

Sample success responses `XML` format

```json
<data>
    <data>[         {             "storageType":"AutoTest_Wn4MRxEkKK"         },
{ "storageType":"AutoTest_UZOBAEDvil" }, { "stora geType":"AutoTest_8WqAc6rtpp" }, { "storageType":"AutoTest_aCPiv2nIh3" }, { "storageType":"Standard" }, { "storageType":"1" } ]</data>
    <success>true</success>
    <status>200</status>
</data> <host>""</host> <status>200</status>
```

`JSON` format `{`

```json
    "data": {
        "data": "[         {             \"storageType\":\"AutoTest_Wn4MRxEkKK\"
}, { \"storageType\":\"AutoTest_UZOBAEDvil\" }, { \"storageType\":\"AutoTest_8WqAc6rtpp\" }, { \"storageType\":\"AutoTest_aCPiv2nIh3\" }, { \"storageType\":\"Standard\" }, { \"storageType\":\"1\" } ]",
        "success": "true",
        "status": "200"
```

`},`

```json
    "host": "\"\"",
    "status": "200"
```

`}`

##### 4.3.3.4 DescribeInstanceTypeFamilies

You can call this operation to query Elastic Compute Service (ECS) instance families.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanc eTypeFamilies | The operation that you want to perform. Set the value to DescribeInstanceTypeFamilies. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Struct |   | The collection of results. |

| result | Struct |   | The collection of data. |
|---|---|---|---|
| instanceTypeF amilies | Array of instanceTypeF amilie |   | The ECS instance families. |
| generation | String | "" | The code of the instance family. |
| instanceTypeF amilyId | String | ecs.se1ne | The ID of the instance family. |
| status | Integer | 200 | The returned status code. |
| success | String | true | The returned success code. |
| host | String | "" | The host address. |
| status | Integer | 200 | The returned status code. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeInstanceTypeFamilies &<Common request parameters>
```

Sample success responses `XML` format

```xml
<data>
    <result>
        <instanceTypeFamilies>
            <generation>""</generation>
            <instanceTypeFamilyId>ecs.se1ne</instanceTypeFamilyId>
        </instanceTypeFamilies>
    </result>
    <success>true</success>
    <status>200</status>
</data> <host>""</host> <status>200</status>
```

`JSON` format `{`

```json
    "data": {
        "result": {
            "instanceTypeFamilies": [
```

`{`

```json
                    "generation": "\"\"",
                    "instanceTypeFamilyId": "ecs.se1ne"
```

`}` `]` `},`

```json
        "success": "true",
        "status": "200"
```

`},`

```json
    "host": "\"\"",
    "status": "200"
```

`}`

##### 4.3.3.5 GetRegionsByProduct

Queries the region list of a service.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRegionsByPr oduct | The operation that you want to perform. Set the value to GetRegionsByProduct. |
| ProductName | String | Yes | ecs | The name of the service. |
| Organization | String | No | 1 | The ID of the organization. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| body | Struct |   | The response body. |
| RegionList | Array of Region |   | The list of regions. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region. |

| RegionType | String | center | The type of the region. center cell |
|---|---|---|---|
| code | Integer | 200 | The HTTP status code. |
| successRespo nse | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetRegionsByProduct &ProductName=ecs &<Common request parameters>
```

Sample success responses `XML` format

```xml
<successResponse>true</successResponse> <code>200</code> <body>
    <RegionList>
        <RegionType>center</RegionType>
        <RegionId>cn-qingdao-env17-d01</RegionId>
    </RegionList>
</body>
```

`JSON` format `{`

```json
    "successResponse": "true",
    "code": "200",
    "body": {
        "RegionList": [
```

`{`

```json
                "RegionType": "center",
                "RegionId": "cn-qingdao-env17-d01"
```

`}` `]` `}` `}`

##### 4.3.3.6 BindBucketPolicy

Associates a policy with an OSS bucket.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/ossIsolationVpc/bind HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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

Sample success responses `XML` format

```xml
<code>200</code> <success>true</success> <data/>
```

`JSON` format `{`

```json
    "code": 200,
    "success": true,
    "data": ""
```

`}`

##### 4.3.3.7 UnBindBucketPolicy

Disassociates a policy from an OSS bucket.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/manage/saleconf/ossIsolationVpc/unBind HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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
|---|---|---|---|

**Examples**

Sample requests

```
POST /ascm/manage/saleconf/ossIsolationVpc/unBind HTTP/1.1 Common request headers
```

Sample success responses `XML` format

```xml
<Code>200</Code> <Success>true</Success> <Data/>
```

`JSON` format `{`

```json
    "Code": 200,
    "Success": true,
    "Data": ""
```

`}`

#### 4.3.4 Configurations

##### 4.3.4.1 RemoveLoginPolicyById

Deletes a logon policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveLoginPol icyById | The operation that you want to perform. Set the value to RemoveLoginPolicyById. |
| Id | Integer | Yes | 2 | The ID of the logon policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |

| cost | Integer | 1000 | The amount of time taken to perform the operation. |
|---|---|---|---|
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveLoginPolicyById &Id=2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

##### 4.3.4.2 GetPasswordPolicy

Queries a password policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetPasswordPoli cy | The operation that you want to perform. Set the value to GetPasswordPolicy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| hardExpiry | Boolean | true | Indicates whether the password expires. |
| maxLoginAtte mps | Integer | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| maxPassword Age | Integer | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| minimumPass wordLength | Integer | 10 | The minimum number of characters in the password. |
| passwordError LockPeriod | Integer | 30 | The locking period of the password. |
| passwordError TolerancePerio d | Integer | 5 | The tolerance period of the password when a password error occurs. |
| passwordReus ePrevention | Integer | 5 | The number of previous passwords that the user is disallowed to reuse. Default value: 0. The default value indicates that the user can reuse previous passwords. |
| requireLowerc aseCharacters | Boolean | true | Indicates whether lowercase letters are required. |
| requireNumbe rs | Boolean | true | Indicates whether digits are required. |

| requireSymbol s | Boolean | true | Indicates whether special characters are required. |
|---|---|---|---|
| requireUpperc aseCharacters | Boolean | true | Indicates whether uppercase letters are required. |
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "passwordErrorTolerancePeriod": "5",
        "minimumPasswordLength": "10",
        "requireSymbols": "true",
        "passwordErrorLockPeriod": "30",
        "passwordReusePrevention": "5",
        "maxLoginAttemps": "5",
        "requireLowercaseCharacters": "true",
        "hardExpiry": "true",
        "requireNumbers": "true",
        "requireUppercaseCharacters": "true",
        "maxPasswordAge": "90"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

##### 4.3.4.3 ResetPasswordPolicy

Resets a password policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ResetPasswordP olicy | The operation that you want to perform. Set the value to ResetPasswordPolicy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| hardExpiry | Boolean | true | Indicates whether the password expires. |

| maxLoginAtte mps | Integer | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
|---|---|---|---|
| maxPassword Age | Integer | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| minimumPass wordLength | Integer | 10 | The minimum number of characters in the password. |
| passwordError LockPeriod | Integer | 30 | The locking period of the password. |
| passwordError TolerancePerio d | Integer | 5 | The tolerance period of the password when a password error occurs. |
| passwordReus ePrevention | Integer | 5 | The number of previous passwords that the user is disallowed to reuse. The default value is 0, which indicates that the users can reuse previous passwords. |
| requireLowerc aseCharacters | Boolean | true | Indicates whether lowercase letters are required. |
| requireNumbe rs | Boolean | true | Indicates whether digits are required. |
| requireSymbol s | Boolean | true | Indicates whether special characters are required. |
| requireUpperc aseCharacters | Boolean | true | Indicates whether uppercase letters are required. |
| message | String | success | The error message. |
| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ResetPasswordPolicy &<Common request parameters>
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "passwordErrorTolerancePeriod": "5",
        "minimumPasswordLength": "10",
        "requireSymbols": "true",
        "passwordErrorLockPeriod": "30",
        "passwordReusePrevention": "5",
        "maxLoginAttemps": "5",
        "requireLowercaseCharacters": "true",
        "hardExpiry": "true",
        "requireNumbers": "true",
        "requireUppercaseCharacters": "true",
        "maxPasswordAge": "90"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

##### 4.3.4.4 SetPasswordPolicy

Modifies a password policy.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetPasswordPoli cy | The operation that you want to perform. Set the value to SetPasswordPolicy. |
| HardExpiry | Boolean | No | true | Specifies whether the password expires. |
| RequireNumbers | Boolean | No | true | Specifies whether digits are required. |
| RequireSymbols | Boolean | No | true | Specifies whether special characters are required. |
| RequireLowerca seCharacters | Boolean | No | true | Specifies whether lowercase letters are required. |
| RequireUpperca seCharacters | Boolean | No | true | Specifies whether uppercase letters are required. |
| MaxLoginAttemp s | Integer | No | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| MaxPasswordAg e | Integer | No | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| MinimumPasswo rdLength | Integer | No | 10 | The minimum required number of characters in the password. |
| PasswordReuseP revention | Integer | No | 5 | The number of previous passwords that the user is disallowed to reuse. Default value: 0. The default value indicates that the user can reuse previous passwords. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| code | String | 200 | The HTTP status code. |
|---|---|---|---|
| cost | Integer | 1000 | The amount of time taken to perform the operation. |
| data | Struct |   | The response. |
| hardExpiry | Boolean | true | Indicates whether the password expires. |
| maxLoginAtte mps | Integer | 5 | The maximum number of logon attempts within 1 hour when the password is incorrect. |
| maxPassword Age | Integer | 90 | The validity period of the password. Unit: days. 0 indicates that the password expiration policy is disabled. |
| minimumPass wordLength | Integer | 10 | The minimum number of characters in the password. |
| passwordError LockPeriod | Integer | 30 | The locking period of the password. |
| passwordError TolerancePerio d | Integer | 5 | The tolerance period of the password when a password error occurs. |
| passwordReus ePrevention | Integer | 5 | The number of previous passwords that the user is disallowed to reuse. Default value: 0. The default value indicates that the user can reuse previous passwords. |
| requireLowerc aseCharacters | Boolean | true | Indicates whether lowercase letters are required. |
| requireNumbe rs | Boolean | true | Indicates whether digits are required. |
| requireSymbol s | Boolean | true | Indicates whether special characters are required. |
| requireUpperc aseCharacters | Boolean | true | Indicates whether uppercase letters are required. |
| message | String | success | The error message. |

| pureListData | Boolean | false | Indicates whether only data is returned and other parameters are not returned. |
|---|---|---|---|
| redirect | Boolean | false | Indicates whether redirections are performed. |
| success | Boolean | true | Indicates whether the call is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetPasswordPolicy &<Common request parameters>
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

`JSON` format `{`

```json
    "redirect": "false",
    "cost": "1000",
    "code": "200",
    "data": {
        "passwordErrorTolerancePeriod": "5",
        "minimumPasswordLength": "10",
        "requireSymbols": "true",
        "passwordErrorLockPeriod": "30",
        "passwordReusePrevention": "5",
        "maxLoginAttemps": "5",
        "requireLowercaseCharacters": "true",
        "hardExpiry": "true",
        "requireNumbers": "true",
        "requireUppercaseCharacters": "true",
        "maxPasswordAge": "90"
```

`},`

```json
    "success": "true",
    "pureListData": "false",
    "message": "success"
```

`}`

##### 4.3.4.5 ListRAMServiceRoles

Queries the list of RAM roles.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/role/listRAMServiceRoles HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| regionName | String | Body | No | test region _ | The ID of the zone. |
| productName | String | Body | No | pro test _ | The name of the service. |
| roleName | String | Body | No | role test _ | The name of the role. |
| organizationId | Integer | Body | No | 1 | The ID of the organization. |

| currentPage | Integer | Body | No | 1 | The number of the page to return. |
|---|---|---|---|---|---|
| pageSize | Integer | Body | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |
| cost | Integer | 1000 | The amount of time consumed by the operation. |
| data | Array of itemData |   | The response data. |
| aliyunUserId | Integer | 12 | The ID of the Apsara Stack tenant account. |
| arn | String | 123 | The ARN. |
| assumeRolePo licyDocument | String | 123 | The file of the policy based on which the role is assumed. |
| description | String | test | The description. |
| id | Integer | 1 | The ID. |
| organizationId | Integer | 1 | The ID of the organization. |
| organizationN ame | String | organization test _ | The name of the organization. |
| policies | Array of itemPolicy |   | The list of policies. |
| aliyunUserId | Integer | 1 | The ID of the Apsara Stack tenant account. |
| ascmRamPolic yId | Integer | 1 | The ID of the RAM policy in the Apsara Uni- manager Management Console. |
| attachDate | Long | 1645234235 | This parameter is deprecated. |

| defaultVersion | String | 1 | The default version. |
|---|---|---|---|
| description | String | testdescription | The description. |
| id | Integer | 1 | The ID. |
| policyDocume nt | String | 123 | The file of the policy. |
| policyName | String | test | The name of the policy. |
| policyType | String | test | The type of the policy. |
| privilegeId | Integer | 1 | This parameter is deprecated. |
| ramGroupId | Integer | 1 | The ID of the RAM user group. |
| ramRoleId | Integer | 1 | The ID of the RAM role. |
| region | String | cn-qingdao-env17- d01 | The zone. |
| resourceSetId | Integer | 1 | The ID of the resource set. |
| product | String | 123 | The ID of the service. |
| region | String | cn-qingdao-env17- d01 | The ID of the zone. |
| roleId | String | 1 | The ID of the role. |
| roleName | String | defaultRole.resourc eUser.name | The name of the role. |
| roleType | String | ROLETYPE ASCM _ | The type of the role. Valid values: ROLETYPE RAM and ROLETYPE ASCM. _ _ ROLETYPE RAM specifies a RAM role. _ ROLETYPE ASCM specifies a custom role. _ |
| message | String | success | The message. |
| pageInfo | Struct |   | The pagination information. |

| currentPage | Integer | 1 | The page number of the returned page. |
|---|---|---|---|
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

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": [{"organizationId":"","aliyunUserId":"","product":"","organizationName":"","assumeRolePol yDocument":"","roleId":"1","roleName":"defaultRole.resourceUser.name","description":"","i :"","roleType":"ROLETYPE_ASCM","region":"cn-qingdao-env17-d01","arn":"","policies":[{"p olicyDocument":"","ramRoleId":"","ramGroupId":"","policyName":"","description":"","ascmRa olicyId":"","aliyunUserId":"","privilegeId":"","attachDate":"","policyType":"","id":"","r ourceSetId":"","region":"","defaultVersion":""}]}],"success":"true","pageInfo":{"total" :"10","totalPage":"2","pageSize":"5","currentPage":"1"},"pureListData":"false","message": uccess"}
```

##### 4.3.4.6 ListRAMPolicies

Queries the list of RAM policies.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/role/listRAMPolicies HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
|---|---|---|---|---|---|
| PolicyName | String | Body | No | test policy _ | The name of the policy. |
| Description | String | Body | No | test | The description of the policy. |
| RoleId | Integer | Body | No | 1 | The ID of the role. |
| CurrentPage | Integer | Body | No | 1 | The number of the page to return. |
| PageSize | Integer | Body | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| code | String | 200 | The HTTP status code. |

| cost | Integer | 1000 | The amount of time consumed by the operation. |
|---|---|---|---|
| data | Array of itemData |   | The response data. |
| ctime | Long | 16223113123 | The time when the policy was created. |
| id | Integer | 1 | The ID of the policy. |
| mtime | Long | 16223113123 | The time when the policy was modified. |
| muserId | String | admin | The modifier. |
| policyDocume nt | String | a | The file of the policy. |
| policyName | String | test policy _ | The name of the policy. |
| region | String | cn-qingdao-env17- d01 | The zone. |
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

`JSON` format `{`

```json
    "redirect": "",
    "cost": "",
    "code": "",
    "data": [
```

`{`

```json
            "policyDocument": "",
            "muserId": "",
            "policyName": "",
            "ctime": "",
            "id": "",
            "region": "",
            "mtime": ""
```

`}` `],`

```json
    "success": "",
    "pageInfo": {
        "total": "",
        "totalPage": "",
        "pageSize": "",
        "currentPage": ""
```

`},`

```json
    "pureListData": "",
    "message": ""
```

`}`

##### 4.3.4.7 ListRAMPoliciesForUser

Queries the list of RAM policies that are attached to a role.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/dataPrivilege/listRAMPoliciesForUser HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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

`}` Sample success responses `XML` format

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

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","data": [{"ascmRamPolicyId":"1","aliyunUserId":"123","policyDocument":"ccc","ramGroupId":"1","pol yName":"test","attachDate":"1638414294","policyType":"1","description":"test","id":"1","r ion":"cn-qingdao-env17-d01","defaultVersion":"3"}],"success":"true","pageInfo":{"total" :"10","totalPage":"2","pageSize":"5","currentPage":"1"},"pureListData":"false","message": uccess"}
```

##### 4.3.4.8 RemoveLoginPolicyByName

Deletes a logon policy.

**Request headers**

This operation uses only common request headers and does not have operation-specific request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request syntax**

```
POST /ascm/auth/loginPolicy/removeLoginPolicyByName HTTP/1.1
```

**Request parameters**

| Parameter | Type | Posit ion | Requir ed | Example | Description |
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

`}` Sample success responses `XML` format

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

`JSON` format

```json
{"redirect":"false","cost":"1000","code":"200","success":"true","pureListData":"false","m sage":"success"}
```

#### 4.3.5 Parameters related to the MeteringQuery operation

**MeteringQuery operation**

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

| Parameter | Name | Description |
|---|---|---|
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
| InstanceName | Instance name | The name of the ECS instance. |

| psara Uni-manager Man | agemen |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| PrivateIpAddress | Internal IP address | The private IP address of the instance in a virtual private cloud (VPC). When InstanceNetworkType is set to vpc, this parameter value can consist of multiple IP addresses. |
| OSName | Operating system name | The name of the operating system installed on the instance. |
| EipAddress | Elastic IP address (EIP) | The EIPs of the instance. |
| NatIpAddress | Network translation address | The public or private IP address of the ECS instance. |
| VpcId | VPC ID | The ID of the VPC. |
| EipBandwidth | EIP bandwidth | The bandwidth of the EIP associated with the ECS instance. |
| IoOptimized | Whether I/O optimization is enabled | Indicates whether the instance is I/O optimized. |
| InternetMaxBandwidth In | Maximum inbound public bandwidth | Valid values: 1 to 200. Unit: Mbit/s. |
| GPUAmount | Number of GPUs | The number of GPUs that the GPU-accelerated instance has. |
| GPUSpec | GPU model | The model of GPUs used by the GPU-accelerated instance. |
| InstanceBandwidthTx | Maximum outbound internal bandwidth | Unit: KB/s. |
| Memory | Memory | The amount of memory. Unit: MB. |
| Cpu | Processor | The number of processors. |

| Parameter | Name | Description |
|---|---|---|
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
| CreateTime | Instance creation time | The time when the instance was created. |

| Parameter | Name | Description |
|---|---|---|
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

| Parameter | Name | Description |
|---|---|---|
| SelectScanSize | Volume of scanned data | The volume of scanned data that is queried by using the SELECT statement. |
| NetworkOut | Outbound traffic | The traffic sent from OSS to external networks, which occurred between the specified start time and the specified end time. Unit: byte. |
| Storage | Volume of stored data | The amount of used Standard LRS storage space. Unit: byte. |
| NetworkIn | Inbound traffic | The traffic sent from external networks to OSS, which occurred between the specified start time and the specified end time. Unit: byte. |
| Availability Average _ | Average availability value | The average availability obtained from CloudMonitor at the specified end time. |
| Availability Maximum _ | Maximum availability value | The maximum availability value obtained from CloudMonitor at the specified end time. |
| Availability Minimum _ | Minimum availability value | The minimum availability value obtained from CloudMonitor at the specified end time. |
| MeteringStorageUtiliza tion Average _ | Average capacity value | The average capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |
| MeteringStorageUtiliza tion Maximum _ | Maximum capacity value | The maximum capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |
| MeteringStorageUtiliza tion Minimum _ | Minimum capacity value | The minimum capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |

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

|   |   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc | n r n e |
|---|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| ChargedDatasize | Actually billed storage space | The actually billed Infrequent Access (IA) locally redundant storage (LRS) or OSS Archive LRS space. Unit: byte. |
| GetRequest | The number of GET requests. | The number of GET requests that occurred between the specified start time and the specified end time. |
| RetrievalData | Volume of retrieved data | The volume of retrieved IA or Archive data. Unit: byte. |
| PutRequest | The number of PUT requests. | The number of PUT requests that occurred between the specified start time and the specified end time. |
| IntranetOut | Outbound traffic from the internal network | Unit: byte. |
| ProcessI | Number of video snapshots | The number of video snapshots. |
| ProcessImgSize | Volume of processed images | The volume of processed images. Unit: byte. |
| SelectScanSize | Volume of scanned data | The volume of scanned data that is queried by using the SELECT statement. |
| NetworkOut | Outbound traffic | The traffic sent from OSS to external networks, which occurred between the specified start time and the specified end time. Unit: byte. |
| Storage | Volume of stored data | The amount of used Standard LRS storage space. Unit: byte. |
| NetworkIn | Inbound traffic | The traffic sent from external networks to OSS, which occurred between the specified start time and the specified end time. Unit: byte. |

| Parameter | Name | Description |
|---|---|---|
| Availability Average _ | Average availability value | The average availability obtained from CloudMonitor at the specified end time. |
| Availability Maximum _ | Maximum availability value | The maximum availability value obtained from CloudMonitor at the specified end time. |
| Availability Minimum _ | Minimum availability value | The minimum availability value obtained from CloudMonitor at the specified end time. |
| MeteringStorageUtiliza tion Average _ | Average capacity value | The average capacity value obtained from CloudMonitor at the specified end time. Unit: byte. |
| MeteringStorageUtiliza tion Maximum _ | Maximum capacity value | The maximum capacity value obtained from CloudMonitor at the end time. Unit: byte. |
| MeteringStorageUtiliza tion Minimum _ | Minimum capacity value | The minimum capacity value obtained from CloudMonitor at the end time. Unit: byte. |

##### 4.3.5.4 EIP

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to EIP.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the EIP belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the EIP belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the EIP belongs. |

|   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa a Uni-manager Management Co |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| InsId | EIP ID | The ID of the EIP. |
| RegionId | Region | The ID of the region to which to the EIP belongs. |
| StartTime | Start time | The beginning of the time range queried. The time is displayed in UTC. |
| EndTime | End time | The end of the time range queried. The time is displayed in UTC. |
| CreateTime | EIP creation time | The time when the EIP was created. |
| PrivateIpAddress | Private IP address | The IP address in the vSwitch CIDR block. |
| Name | EIP name | The name of the EIP. |
| ExpiredTime | Expiration time | The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. The time is displayed in UTC. |
| BandwidthPackageId | ID of the EIP bandwidth plan | The ID of the EIP bandwidth plan. |
| Status | EIP status | The state of the EIP. Valid values: Associating: The EIP is being associated. Unassociating: The EIP is being disassociated. InUse: The EIP is allocated. Available: The EIP is available. |
| ISP | Line type | The line type. Valid values: BGP CUCC AZ1 _ CMCC AZ1 _ PrivateEIP AZ1 _ CTC AZ1 _ |

| Parameter | Name | Description |
|---|---|---|
| Mode | Association mode | The association mode. Default value: NAT. Valid values: NAT: standard NAT mode MULTI BINDED: multi-EIP-to-ENI mode _ BINDED: cut-through mode This parameter is returned only if InstanceType is set to NetworkInterface. |
| BandwidthPackageTyp e | Bandwidth type | The type of the bandwidth. Only CommonBandwidthPackage that specifies an EIP bandwidth plan is returned. |
| IpAddress | IP address | The EIP. |
| BindInstanceId | ID of the associated instance | The ID of the instance with which the EIP is associated. |
| BindInstanceType | Type of the associated instance | The type of the instance with which the EIP is associated. Valid values: EcsInstance: an ECS instance in a VPC SlbInstance: a SLB instance in a VPC Nat: a NAT gateway HaVip: a HAVIP NetworkInterface: a secondary ENI |
| BindInstanceName | Name of the associated instance | The name of the instance with which the EIP is associated. In this example, the name of an ECS instance is returned. |
| Bandwidth | Maximum bandwidth | The maximum bandwidth of the EIP. Unit: Mbit/s. |

##### 4.3.5.5 VPC

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Virtual Private Cloud (VPC).

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |

|   |   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc | n r n e |
|---|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| OrgName | Organization name | The name of the organization to which the virtual private cloud (VPC) belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the VPC belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the VPC belongs. |
| InsId | VPC ID | The ID of the VPC. |
| RegionId | Region | The ID of the region where the VPC resides. |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | VPC creation time | The time when the VPC was created. |
| Status | VPC status | The status of the VPC. Valid values: Pending: The VPC is being configured. Available: The VPC is available. |
| CidrBlock | IPv4 CIDR block | The IPv4 CIDR block of the VPC. |
| VRouterId | Router ID | The ID of the vRouter. |
| VpcName | VPC name | The name of the VPC. |
| Ipv6CidrBlock | IPv6 CIDR block | The IPv6 CIDR block of the VPC. |
| Description | Description | The description of the VPC. |

| Parameter | Name | Description |
|---|---|---|
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
| RegionId | Region | The ID of the region to which the instance belongs. |
| StartTime | Start time | The beginning of the time range queried. The time is displayed in UTC. |
| EndTime | End time | The end of the time range queried. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| DBInstanceDescription | Instance description | The description of the instance. |

|   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| Category | Instance edition | The edition of the instance. Valid values: Finance: Enterprise Edition HighAvailability: High-availability Edition |
| ClassCode | Instance type | The type of the instance. Example: rds.mysql.t1.small. |
| DBType | Engine type | The type of the database engine. Example: MySQL. |
| DBVersion | Engine version | The version of the database engine. Example: 8.0. |
| Zone | Zone ID | The ID of the zone. |
| DBInstanceStatus | Instance status | The state of the instance. |
| DBInstanceType | Instance role | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| LockMode | Lock mode | The lock mode of the instance. Valid values: Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked when it expires. LockByRestoration: The instance is automatically locked before it is rolled backed. LockByDiskQuota: The instance is automatically locked when its disk capacity is exhausted. LockReadInstanceByDiskQuota: The instance is a read-only instance and is automatically locked when its disk capacity is exhausted. |
| Port | Port | The port that is used to connect to the instance over an internal network. |

| psara Uni-manager Man Console Developer Guid Uni-manager Managem | agemen e·Apsar ent Con |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| DBInstanceClassType | Instance family | The instance family to which the instance belongs. Valid values: s: shared instance family x: general purpose instance family d: dedicated instance family h: dedicated host instance family |
| DBInstanceStorageTyp e | Storage type | The storage type that is used for the instance. Valid values: local ssd or ephemeral ssd: local SSD _ _ cloud ssd: standard SSD _ cloud essd: ESSD _ |
| AvailabilityValue | Availability | The availability state of the instance in percentage. |
| IpAddress | IP address | The IP address. |
| VPCId | VPC ID | The ID of the VPC. |
| BackupStorage | Backup storage | Unit: bytes. |
| NetworkIn | Inbound traffic | The traffic sent from external networks to the instance, which occurred from the specified start time to the specified end time. Unit: bytes. |
| NetworkOut | Outbound traffic | The traffic sent from the instance to external networks, which occurred from the specified start time to the specified end time. Unit: bytes. |
| Storage | Storage capacity | The total amount of storage capacity. Unit: bytes. |
| UsedStorage | Used storage capacity | The amount of used storage capacity. Unit: bytes. |
| AccountMaxQuantity | Maximum number of accounts that can be created | The maximum number of accounts that can be created on the instance. |
| DBInstanceCPU | Number of CPUs | The number of CPUs that are configured for the instance. |

|   |   | t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc |
|---|---|---|
| Parameter | Name | Description |
| MaxConnections | Maximum number of connections | The maximum number of concurrent connections that can be supported by the instance. |
| DBInstanceMemory | Memory | The memory size of the instance. Unit: MB. |
| MaxIOPS | Maximum IOPS | The maximum IOPS that can be supported by the instance. |
| DBMaxQuantity | Maximum number of databases that can be created | The maximum number of databases that can be created on the instance. |
| CpuUsage Maximum _ | Maximum CPU utilization | The maximum CPU utilization obtained from CloudMonitor at the specified end time. |
| CpuUsage Minimum _ | Minimum CPU utilization | The minimum CPU utilization obtained from CloudMonitor at the specified end time. |
| DiskUsage Average _ | Average disk usage | The average disk usage obtained from CloudMonitor at the specified end time. |
| DiskUsage Maximum _ | Maximum disk usage | The maximum disk usage obtained from CloudMonitor at the specified end time. |
| DiskUsage Minimum _ | Minimum disk usage | The minimum disk usage obtained from CloudMonitor at the specified end time. |
| IOPSUsage Average _ | Average IOPS usage | The average IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUsage Maximum _ | Maximum IOPS usage | The maximum IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUsage Minimum _ | Minimum IOPS usage | The minimum IOPS usage obtained from CloudMonitor at the specified end time. |
| MemoryUsage Averag _ e | Average memory usage | The average memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsage Maxim _ um | Maximum memory usage | The maximum memory usage obtained from CloudMonitor at the specified end time. |

| A t a s | psara Uni-manager Man Console Developer Guid Uni-manager Managem ole API Reference | agemen e·Apsar ent Con |   |   |
|---|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| MemoryUsage Minimu _ m | Minimum memory usage | The minimum memory usage obtained from CloudMonitor at the specified end time. |

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

|   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| InstanceName | Instance name | The name of the instance. |
| Description | Instance description | The description of the instance. |
| Status | Instance status | The status of the instance. |
| Version | Engine version | The database engine version. |

##### 4.3.5.8 ApsaraDB for Redis

After you call the MeteringQuery operation to query statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB for Redis.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region to which the instance belongs. |
| StartTime | Start time | The beginning of the time range queried. The time is displayed in UTC. |
| EndTime | End time | The end of the time range queried. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |

| Uni-manager Managem ole API Reference | ent Con |   |
|---|---|---|
| Parameter | Name | Description |
| ConnectionDomain | Private IP address | The private IP address of the instance. |
| NetworkType | Network type | The network type of the instance. Valid values: CLASSIC VPC |
| InstanceStatus | Instance status | The state of the instance. |
| PackageType | Plan type | The type of the plan. Valid values: standard: standard plan customized: custom plan |
| InstanceType | Instance category | The category of the instance. |
| ArchitectureType | Instance architecture | The architecture of the instance. Valid values: cluster: cluster architecture standard: standard architecture rwsplit: read/write splitting architecture |
| EngineVersion | Engine version | The version of the database engine. |
| ZoneId | Zone ID | The ID of the zone. |
| InstanceClass | Instance type | The instance type of the instance. |
| InstanceName | Instance name | The name of the instance. |
| NodeType | Node type | The type of the node. Valid values: double: master and replica nodes single: a master node |
| HasRenewChangeOrde r | Whether an order for renewal and configuration change that has not taken effect exists | Indicates whether an order for renewal and configuration change that has not taken effect exists. Valid values: true false |

| Parameter | Name | Description |
|---|---|---|
| IsRds | Whether the instance is managed by ApsaraDB RDS | Indicates whether the instance is managed by ApsaraDB RDS. Valid values: true false |
| Connections | Maximum number of connections | The maximum number of connections supported by the instance. |
| Port | Port | The service port of the instance. |
| QPS | QPS | The expected maximum QPS. |
| Capacity | Storage capacity | The storage capacity of the instance. Unit: MB. |
| Bandwidth | Bandwidth | The bandwidth. Unit: MB/s. |
| ConnectionUsage Aver _ age | Average connection usage | The average connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUsage Max _ imum | Maximum connection usage | The maximum connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUsage Mini _ mum | Minimum connection usage | The minimum connection usage obtained from CloudMonitor at the specified end time. |
| FailedCount Average _ | Average number of failures | The average number of failures obtained from CloudMonitor at the specified end time. |
| FailedCount Maximum _ | Maximum number of failures | The maximum number of failures obtained from CloudMonitor at the specified end time. |
| FailedCount Minimum _ | Minimum number of failures | The minimum number of failures obtained from CloudMonitor at the specified end time. |
| IntranetIn Average _ | Average write bandwidth | The average write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetIn Maximum _ | Maximum write bandwidth | The maximum write bandwidth obtained from CloudMonitor at the specified end time. |

| psara Uni-manager Man Console Developer Guid Uni-manager Managem ole API Reference | agemen e·Apsar ent Con |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| IntranetIn Minimum _ | Minimum write bandwidth | The minimum write bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetInRatio Averag _ e | Average write bandwidth usage | The average write bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetInRatio Maxim _ um | Maximum write bandwidth usage | The maximum write bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetInRatio Minim _ um | Minimum write bandwidth usage | The minimum write bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetOut Average _ | Average read bandwidth | The average read bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetOut Maximum _ | Maximum read bandwidth | The maximum read bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetOut Minimum _ | Minimum read bandwidth | The minimum read bandwidth obtained from CloudMonitor at the specified end time. |
| IntranetOutRatio Aver _ age | Average read bandwidth usage | The average read bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetOutRatio Maxi _ mum | Maximum read bandwidth usage | The maximum read bandwidth usage obtained from CloudMonitor at the specified end time. |
| IntranetOutRatio Mini _ mum | Minimum read bandwidth usage | The minimum read bandwidth usage obtained from CloudMonitor at the specified end time. |
| MemoryUsage Averag _ e | Average memory usage | The average memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsage Maxim _ um | Maximum memory usage | The maximum memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUsage Minimu _ m | Minimum memory usage | The minimum memory usage obtained from CloudMonitor at the specified end time. |

##### 4.3.5.9 AnalyticDB for PostgreSQL

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parametersGPDBspecific to AnalyticDB for PostgreSQL.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region to which the instance belongs. |
| StartTime | Start time | The beginning of the time range queried. The time is displayed in UTC. |
| EndTime | End time | The end of the time range queried. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| EngineVersion | Engine version | The version of the database engine. |
| ZoneId | Zone ID | The ID of the zone. |
| DBInstanceNetType | NIC type | The type of the NIC that is used by the instance. |
| InstanceNetworkType | Network type | The network type of the instance. Valid values: Classic VPC |
| DBInstanceDescription | Instance description | The description of the instance. |

| Console Developer Guid Uni-manager Managem ole API Reference | e·Apsar ent Con |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| Engine | Database engine | The database engine of the instance. |
| DBInstanceStatus | Instance status | The state of the instance. |
| LockMode | Lock mode | The lock mode of the instance. Valid values: Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked when it expires. LockByRestoration: The instance is automatically locked before it is rolled backed. LockByDiskQuota: The instance is automatically locked when its disk capacity is exhausted. |
| LockReason | Lock reason | The reason why the instance is locked. |
| ConnectionMode | Access mode | The access mode of the instance. Performance: the standard mode Safety: the safe mode |
| HostType | Storage type of compute nodes | The storage type of compute nodes. Valid values: 0: standard SSD 1: HDD |
| DBInstanceClass | Instance type | The instance type of the instance. |
| DBInstanceClassType | Instance family | The instance family. Valid values: s: shared instance family x: general purpose instance family d: dedicated instance family h: dedicated host instance family |
| AvailabilityValue | Availability status | The availability state of the instance in percentage. |
| VpcId | VPC ID | The ID of the VPC. |

|   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| Port | Port | The port number. |
| DBInstanceDiskMBPS | Disk throughput | The maximum disk throughput of a compute node. Unit: Mbit/s. |
| MaxConnections | Maximum number of connections | The maximum number of concurrent connections that can be supported by the instance. |
| DBInstanceGroupCoun t | Number of compute nodes | The number of compute nodes. |
| DBInstanceMemory | Memory | The memory size of the instance. Unit: MB. |
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |
| DBInstanceCpuCores | CPU | The number of CPU cores. |

##### 4.3.5.10 ApsaraDB for MongoDB

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB for MongoDB.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region where the instance resides. |

| Uni-manager Managem ole API Reference | ent Con |   |
|---|---|---|
| Parameter | Name | Description |
| StartTime | Start time | The beginning of the time range to query. The time is displayed in UTC. |
| EndTime | End time | The end of the time range to query. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| EngineVersion | Engine version | The database engine version. |
| ZoneId | Zone ID | The zone ID of the instance. |
| DBInstanceStatus | Instance status | The status of the instance. |
| DBInstanceClass | Instance type | The instance type. Example: dds.mongo.mid. |
| DBInstanceType | Instance architecture | The architecture of the instance. Valid values: replicate: the replica set instance sharding: the sharded cluster instance |
| LockMode | Lock status | The lock status of the instance. Unlock: The instance is not locked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked because it has expired. LockByRestoration: The instance is automatically locked for a rollback. LockByDiskQuota: The instance is automatically locked because its disk space is used up. Released: The instance is released. When the instance is in the Released state, it cannot be unlocked. You must use backup data to create a new instance. It may take an extended period of time to create another instance. |

| Parameter | Name | Description |
|---|---|---|
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
| CPUUtilization Averag _ e | Average CPU utilization | The average CPU utilization obtained from CloudMonitor at the specified end time. |
| CPUUtilization Maximu _ m | Maximum CPU utilization | The maximum CPU utilization obtained from CloudMonitor at the specified end time. |
| CPUUtilization Minimu _ m | Minimum CPU utilization | The minimum CPU utilization obtained from CloudMonitor at the specified end time. |
| ConnectionAmount Av _ erage | Average number of connections | The average number of connections obtained from CloudMonitor at the specified end time. |

| Parameter | Name | Description |
|---|---|---|
| ConnectionAmount Ma _ ximum | Maximum number of connections | The maximum number of connections obtained from CloudMonitor at the specified end time. |
| ConnectionAmount Mi _ nimum | Minimum number of connections | The minimum number of connections obtained from CloudMonitor at the specified end time. |
| ConnectionUtilization _ Average | Average connection usage | The average connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUtilization _ Maximum | Maximum connection usage | The maximum connection usage obtained from CloudMonitor at the specified end time. |
| ConnectionUtilization _ Minimum | Minimum connection usage | The minimum connection usage obtained from CloudMonitor at the specified end time. |
| DiskUtilization Averag _ e | Average disk usage | The average disk usage obtained from CloudMonitor at the specified end time. |
| DiskUtilization Maximu _ m | Maximum disk usage | The maximum disk usage obtained from CloudMonitor at the specified end time. |
| DiskUtilization Minimu _ m | Minimum disk usage | The minimum disk usage obtained from CloudMonitor at the specified end time. |
| IOPSUtilization Averag _ e | Average IOPS usage | The average IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUtilization Maxim _ um | Maximum IOPS usage | The maximum IOPS usage obtained from CloudMonitor at the specified end time. |
| IOPSUtilization Minimu _ m | Minimum IOPS usage | The minimum IOPS usage obtained from CloudMonitor at the specified end time. |
| MemoryUtilization Ave _ rage | Average memory usage | The average memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUtilization Ma _ ximum | Minimum memory usage | The minimum memory usage obtained from CloudMonitor at the specified end time. |
| MemoryUtilization Min _ imum | Maximum memory usage | The maximum memory usage obtained from CloudMonitor at the specified end time. |

|   |   | t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| QPS Average _ | Average QPS | The average queries per second (QPS) obtained from CloudMonitor at the specified end time. |
| QPS Maximum _ | Maximum QPS | The maximum QPS obtained from CloudMonitor at the specified end time. |
| QPS Minimum _ | Minimum QPS | The minimum QPS obtained from CloudMonitor at the specified end time. |

##### 4.3.5.11 Message Queue for Apache RocketMQ

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to Message Queue for Apache RocketMQ.

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

| Console Developer Guid Uni-manager Managem ole API Reference | e·Apsar ent Con |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| cluster | Cluster ID | The ID of the cluster. |
| instanceName | Instance name | The name of the instance. |
| spInstanceId | Instance ID | The ID of the instance. |
| independentNaming | Whether a separate namespace is configured | Indicates whether a separate namespace is configured. |
| instanceType | Instance type | The instance type of the instance. |
| instanceStatus | Instance status | The status of the instance. |
| topicCapacity | Topic capacity | The number of topics. |

##### 4.3.5.12 ApsaraDB RDS for PostgreSQL

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB RDS for PostgreSQL.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |

|   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa a Uni-manager Management Co |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| RegionId | Region | The ID of the region to which the instance belongs. |
| StartTime | Start time | The beginning of the time range queried. The time is displayed in UTC. |
| EndTime | End time | The end of the time range queried. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| Port | Port | The port that is used to connect to the instance over an internal network. |
| DBInstanceClassType | Instance family | The instance family to which the instance belongs. Valid values: s: shared instance family x: general purpose instance family d: dedicated instance family h: dedicated host instance family |
| DBInstanceClass | Instance type | The instance type of the instance. Example: rds.mys2.small. |
| DBInstanceNetType | Internal network or Internet | The type of the network over which the instance is connected. Valid values: Internet: Internet Intranet: internal network |
| DBInstanceType | Instance role | The role of the instance. Valid values: Primary: primary instance Readonly: read-only instance Guard: disaster recovery instance Temp: temporary instance |
| InstanceNetworkType | Network type | The network type of the instance. Valid values: Classic VPC |

| Parameter | Name | Description |
|---|---|---|
| DBInstanceDescription | Instance description | The description of the instance. |
| DBType | Database type | The type of the database. |
| DBVersion | Database version | The version of the database. |
| ZoneId | Zone ID | The ID of the zone. |
| LockMode | Lock mode | The lock mode of the instance. Valid values: Unlock: The instance is unlocked. ManualLock: The instance is manually locked. LockByExpiration: The instance is automatically locked when it expires. LockByRestoration: The instance is automatically locked before it is rolled backed. LockByDiskQuota: The instance is automatically locked when its disk capacity is exhausted. LockReadInstanceByDiskQuota: The instance is a read-only instance and is automatically locked when its disk capacity is exhausted. |
| ConnectionMode | Access mode | The access mode of the instance. Valid values: Standard: standard mode Safe: database proxy mode |
| DBInstanceStorageTyp e | Storage type | The storage type of the instance. Valid values: local ssd or ephemeral ssd: local SSD _ _ cloud ssd: standard SSD _ cloud essd: ESSD _ |
| DBInstanceStatus | Instance status | The state of the instance. |
| AvailabilityValue | Availability status | The availability state of the instance in percentage. |
| IpAddress | IP address | The IP address. |
| VPCId | VPC ID | The ID of the VPC. |

|   |   |   | t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc | r n e |
|---|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| AccountMaxQuantity | Maximum number of accounts that can be created | The maximum number of accounts that can be created for the instance. |
| DBInstanceCPU | Number of CPUs on the instance | The number of CPUs that are configured for the instance. |
| MaxConnections | Maximum number of concurrent connections | The maximum number of concurrent connections that are supported by the instance. |
| DBInstanceMemory | Memory | The memory size of the instance. Unit: MB. |
| DBInstanceDiskUsed | Used storage | The used storage. Unit: bytes. |
| MaxIOPS | Maximum IOPS | The maximum IOPS that can be supported by the instance. |
| DBMaxQuantity | Maximum number of databases that can be created | The maximum number of databases that can be created on the instance. |
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |

##### 4.3.5.13 ApsaraDB RDS for SQL Server

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to ApsaraDB RDS for SQL Server.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |
| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |

| psara Uni-manager Man Console Developer Guid Uni-manager Managem | agemen e·Apsar ent Con |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
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
| DBInstanceStorageTyp e | Storage type | The type of storage media that is used by the instance. Valid values: local ssd or ephemeral ssd: local SSD _ _ cloud ssd: standard SSD. _ cloud essd: enhanced SSD _ |
| AvailabilityValue | Availability status | The availability status of the instance. Unit: %. |
| IpAddress | IP address | The IP address. |

| Console Developer Guid Uni-manager Managem ole API Reference | e·Apsar ent Con |   |
|---|---|---|

| Parameter | Name | Description |
|---|---|---|
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
| MaxIOPS | Maximum IOPS | The maximum number of I/O requests that the instance can process per second. |
| DBMaxQuantity | Maximum number of databases that can be created | The maximum number of databases that can be created on the instance. |

| Parameter | Name | Description |
|---|---|---|
| DBInstanceStorage | Storage | The storage capacity of the instance. Unit: GB. |

##### 4.3.5.14 Log Service

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

| Console Developer Guid Uni-manager Managem ole API Reference | e·Apsar ent Con |   |
|---|---|---|
| Parameter | Name | Description |
| OutflowSize | Read traffic | The volume of compressed read traffic of Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| InflowSize | Write traffic | The volume of compressed write traffic of Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| WriteCount | Number of writes | The number of writes to Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| ReadCount | Number of reads | The number of reads from Log Service between the specified start time and the specified end time, and also at the specified start time. Unit byte. |
| IndexSum | Total index volume | The total volume of indexes occupied by Log Service. Unit: byte. |
| RawSum | Total data size | The total size of data occupied by Log Service. Unit: byte. |
| IndexSize | Volume of index data | The volume of index data between the specified start time and the specified end time, and also at the specified start time. Unit byte. |

##### 4.3.5.15 EBS

After you call the MeteringQuery operation to query statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to EBS.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |
| OrgName | Organization name | The name of the organization to which the instance belongs. |

| ResourceGId | Resource set ID | The ID of the resource set to which the instance belongs. |
|---|---|---|
| ResourceGName | Resource set name | The name of the resource set to which the instance belongs. |
| InsId | Instance ID | The ID of the instance. |
| RegionId | Region | The ID of the region to which the instance belongs. |
| StartTime | Start time | The beginning of the time range queried. The time is displayed in UTC. |
| EndTime | End time | The end of the time range queried. The time is displayed in UTC. |
| CreateTime | Instance creation time | The time when the instance was created. |
| Description | Description | The description of the cloud disk or local disk. |
| DiskCategory | Disk category | The category of the cloud disk or local disk. Valid values: all: all disks categories cloud: basic disk cloud efficiency: ultra disk _ cloud ssd: standard SSD _ cloud essd: ESSD _ local ssd pro: I/O-intensive local disk _ _ local hdd pro: throughput-intensive local disk _ _ ephemeral: (Retired) local disk ephemeral ssd: (Retired) local SSD _ Default value: all. |
| ExpiredTime | Expiration time | The time when the cloud disk expires. |
| ImageId | Image ID | The ID of the image that is used to create the ECS instance. This parameter is empty only unless the cloud disk was created from an image. The value of this parameter remains unchanged throughout the lifecycle of the cloud disk. |

| Status | Cloud disk status | The state of the cloud disk. Valid values: In use _ Available Attaching Detaching Creating ReIniting All Default value: All. |
|---|---|---|
| AttachedTime | Attachment time | The time when the cloud disk was attached. The time follows the ISO 8601 standard. The time is displayed in UTC+0. This parameter is valid only if the Status parameter is set to Available. |
| BindInstanceId | ID of the instance to which the disk is attached | The ID of the instance to which the cloud disk or local disk is attached. This parameter is empty only unless the Status parameter is set to In use. _ |
| Device | Mount target | The mount target of the cloud disk or local disk. |
| DiskName | Disk name | The name of the cloud disk or local disk. |
| Type | Disk type | The type of the cloud disk or local disk. Valid values: system: system disk data: data disk |
| DiskSize | Disk size | The size of the cloud disk or local disk. Unit: GiB. |

##### 4.3.5.16 Snapshots

After you call the MeteringQuery operation to obtain statistical data, common response parameters and service-specific response parameters are returned. This topic describes the response parameters specific to the snapshot feature.

| Parameter | Name | Description |
|---|---|---|
| Pos | Primary key | The primary key consists of the service ID, organization ID, and start time. |

| Parameter | Name | Description |
|---|---|---|
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

| Parameter | Name | Description |
|---|---|---|
| Usage | Whether the snapshot has been used | Indicates whether the snapshot has been used to create images or disks. Valid values: image: The snapshot has been used to create custom images. disk: The snapshot has been used to create disks. image disk: The snapshot has been used to _ create custom images and data disks. none: The snapshot has not been used to create custom images or disks. |
| Description | Snapshot description | The description of the snapshot. |
| SnapshotCategory | Snapshot type | The type of the snapshot. Valid values: standard: normal snapshot flash: local snapshot |
| SnapshotName | Snapshot name | The name of the snapshot. |
| SourceDiskId | Source disk ID | The ID of the source disk. |
| SourceStorageType | Source disk type | The type of the source disk. |
| SnapshotSN | Snapshot serial number | The serial number of the snapshot. |
| LastModifiedTime | Time when the snapshot was last changed | The time when the snapshot was last changed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| SnapshotType | Type of snapshot creation | The type of snapshot creation. Valid values: auto or timer: automatically created snapshot user: manually created snapshot all: all snapshot types |
| SourceDiskType | Source disk attribute | The attribute of the source disk. The value is set to systemdata. |
| SourceDiskSize | Source disk size | The size of the system disk. Unit: GB. |

|   |   |   | t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc | r n e |
|---|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| RetentionDays | Retention period of the automatic snapshot | The retention period of the automatic snapshot. |

##### 4.3.5.17 Auto Scaling

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

| Parameter | Name | Description |
|---|---|---|
| LifecycleState | Status | The status of the scaling group. Valid values: Active: The scaling group is active. Active scaling groups can receive requests to execute scaling rules and trigger scaling activities. Inactive: The scaling group is inactive. Inactive scaling groups cannot receive requests to execute scaling rules. Deleting: The scaling group is being deleted. Scaling groups that are being deleted cannot receive requests to execute scaling rules and their parameters cannot be modified. |
| ScalingPolicy | Reclaim mode | Indicates the reclaim mode of the scaling group. Valid values: recycle: The reclaim mode of the scaling group is set to Shutdown and Reclaim Mode. release: The reclaim mode of the scaling group is set to Release Mode. |
| VSwitchId | vSwitch ID | The ID of the vSwitch that is associated with the scaling group. |
| ScalingGroupName | ScalinggGroup name | The name of the scaling group. |
| VpcId | VPC ID | The ID of the virtual private cloud (VPC) to which the scaling group belongs. |
| MultiAZPolicy | Multi-zone scaling policy | The Elastic Compute Service (ECS) instance scaling policy for the multi-zone scaling group. Valid values: PRIORITY: ECS instances are scaled based on the specified vSwitch. When an ECS instance cannot be created in the zone where the vSwitch that has the highest priority resides, the system uses the vSwitch that has the next highest priority to create the instance. COST OPTIMIZED: ECS instances are created _ based on the unit price of vCPU in ascending order. Preemptible instances are preferentially created when preemptible instance types are specified in the active scaling configuration. BALANCE: ECS instances are evenly distributed in multiple zones specified for the scaling group. |
| PendingWaitCapacity | Number of instances in the Pending state | The number of ECS instances that are in the Pending state in the scaling group. |

|   |   |   | Apsara Uni-manager Manageme t Console Developer Guide·Apsa a Uni-manager Management Co sole API Referenc | n r n e |
|---|---|---|---|---|

| Parameter | Name | Description |
|---|---|---|
| TotalCapacity | Total capacity | Indicates the total weighted capacity of all ECS instances in the scaling group if the instance type weight is specified for the scaling group. If the instance type weight is not specified, this parameter indicates the total number of ECS instances in the scaling group. |
| RemovingWaitCapacit y | Number of instances in the Suspending state | The number of ECS instances that are in the Suspending state in the scaling group. |
| ProtectedCapacity | Number of instances in the Protected state | The number of ECS instances that are in the Protected state in the scaling group. |
| StandbyCapacity | Number of instances in the Standby state | The number of instances that are in the Standby state in the scaling group. |
| RemovingCapacity | Number of instances in the Removing state | The number of ECS instances that are in the Removing state in the scaling group. |
| PendingCapacity | Number of instances in the Adding state | The number of ECS instances that are being added to the scaling group and are still being configured. |
| ActiveCapacity | Number of instances in the In Service state | The number of ECS instances that have been added to the scaling group and are running normally. |
| StoppedCapacity | Number of stopped instances | The number of instances that are in the Stopped state in the scaling group. |
| MaxSize | Maximum number of instances | The maximum number of ECS instances in the scaling group. |
| MinSize | Minimum number of instances | The minimum number of ECS instances in the scaling group. |
| DefaultCooldown | Default cooldown time | The default cooldown time of the scaling group. Unit: seconds. During the cooldown time, Auto Scaling executes only scaling activities that are triggered by CloudMonitor event-triggered tasks. |

##### 4.3.5.18 API Gateway

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
| ApiName | API name | The name of the API. |
| GroupId | API group ID | The ID of the specified API group. |
| GroupName | API group name | The name of the specified API group. |
| Visibility | Type | The type of the API. |

Monitor API Reference

## 5 CloudMonitor API Reference

**Reference**

### 5.1 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack API requests. Table 1. Table of common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Action | Strin g | Yes | The operation that you want to perform. For more information, see Obtain API information. |
| Product | Strin g | Yes | The name of the service to which the API operation belongs. Valid value: cms |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Example value: 2019-01-01. |
| RegionId | Strin g | Yes | The ID of the region. For more information, see Obtain the values of common header parameters. |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is used to access the service. For more information, see Obtain AccessKey credentials. |
| Signature | Strin g | Yes | The signature string. For more information, see Request signatures. |
| SignatureMe thod | Strin g | Yes | The encryption method of the signature string. Valid values: HMAC-SHA1 and HMAC-SHA256. |
| SignatureVer sion | Strin g | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNo nce | Strin g | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | Strin g | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2018-01-01T12:00:00Z. |
| Format | Strin g | No | The format of the response. Set the value to JSON. |

**Note**

The Signature, SignatureMethod, SignatureVersion, SignatureNonce, Timestamp, and Format parameters are encapsulated into the SDK. You do not need to specify these parameters. You can obtain the values of the `Product` and `Version` parameters in the Apsara Unimanager Management Console by performing the following steps:
1. Log on to the Apsara Uni-manager Management Console.
Monitor API Reference
2. In the top navigation bar, choose **Products > Others > API Tool**.
3. In the left-side navigation pane, click **API Directory**.
4. In the **Search by operation name** search box, enter the name of an operation to query its
information.

**Common header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see Obtain the values of common header parameters. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see Obtain the values of common header parameters. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. For more information about how to obtain an instance ID, see Obtain the values of common header parameters. |

**Note**

When you call the API operations of cloud services, you must specify the **x-**
**acs-organizationid**, **x-acs-resourcegroupid**, and **x-acs-instanceid** parameters to
identify the instance on which you want to perform the operation, and the organization and resource set to which the instance belongs. If you call an API operation to create an instance or query the information about one or more instances, you do not need to specify the x-acs-instanceid header. If you do not specify the headers when you call an API operation, the organization and resource set at the root level are used by default.

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful.

### 5.2 Metrics for Apsara Stack services

**services**

This topic describes the metrics available for each service.

**Precautions**

You can call API operations to query monitoring data of the last 31 days. The **Dimensions** value is a JSON string, in the format of `{"instanceId":"<Instance ID of`

```
an Apsara Stack service>"} .
```

When you call an API operation provided by Cloud Monitor, set the **Namespace** and
**Period** parameters.

**Elastic Compute Service (ECS)**

Monitor API Reference

**Basic metrics**

Set **Namespace** to **acs_ecs_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

**Note**

The following metrics are collected from the virtual host layer and are slightly different from metrics collected inside the operating system.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (ECS) CPUUtilization | % | CPUUtilization | userId and instanceId | The CPU usage. |
| (ECS) InternetInRate | bits/s | InternetInRate | userId and instanceId | The rate of inbound traffic to the Internet. |
| (ECS) IntranetInRate | bits/s | IntranetInRate | userId and instanceId | The rate of inbound traffic to the intranet. |
| (ECS) InternetOutRate | bits/s | InternetOutRate | userId and instanceId | The rate of outbound traffic from the Internet. |
| (ECS) IntranetOutRate | bits/s | IntranetOutRate | userId and instanceId | The rate of outbound traffic from the intranet. |
| (ECS) DiskReadBPS | Byte/s | DiskReadBPS | userId and instanceId | The number of bytes read from all disks per second. |
| (ECS) DiskWriteBPS | Byte/s | DiskReadBPS | userId and instanceId | The number of bytes written to all disks per second. |
| (ECS) DiskReadIOPS | Count/s | DiskReadIOPS | userId and instanceId | The number of read I/O operations per second (IOPS) of all disks. |
| (ECS) DiskWriteIOPS | Count/s | DiskReadIOPS | userId and instanceId | The number of write IOPS of all disks. |

**Operating system metrics**

Set **Namespace** to **acs_ecs_dashboard**. Set **Period** to **15** or a multiple of 15. Unit: seconds. Monitor API Reference

**Note**

For ECS instances, you must install a monitoring plug-in to collect metrics at the operating system level. Installation method: In the left-side navigation pane of the Cloud Monitor console, choose Cloud Service Monitoring and click **ECS**. In the **ECS** monitoring list, select the instances that you want to monitor, and click **Batch Install** in the lower part of the page. Metric data is displayed in the monitoring chart in 5 to 10 minutes after the monitoring plug-in is installed.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (Agent) Host.cpu total _ | % | cpu total _ | userId and instanceId | The CPU usage. |
| (Agent) Host.mem.used.u tilization | % | memory usedutil _ ization | userId and instanceId | The memory usage. |
| (Agent) Host.load15 | N/A | load 15m _ | userId and instanceId | The system load in the last 15 minutes. Note This metric is not available for Windows. |
| (Agent) Host.load1 | N/A | load 1m _ | userId and instanceId | The system load in the last 1 minute. Note This metric is not available for Windows. |
| (Agent) Host.load5 | N/A | load 5m _ | userId and instanceId | The system load in the last 5 minutes. Note This metric is not available for Windows. |
| (Agent) Host.disk.utilizati on | % | diskusage utiliza _ tion | userId, instanceId, and device | The disk space usage. |

Monitor API Reference

| (Agent) Host.fs.inode | % | fs inodeutilizatio _ n | userId, instanceId, and device | The inode usage. Note This metric is available only for Linux. |
|---|---|---|---|---|
| (Agent) Host.disk.readbyt es | Byte/s | disk readbytes _ | userId, instanceId, and device | The number of bytes read from the disk per second. |
| (Agent) Host.disk.readiop s | Count/s | disk readiops _ | userId, instanceId, and device | The number of read IOPS of the disk. |
| (Agent) Host.disk.writebyt es | Byte/s | disk writebytes _ | userId, instanceId, and device | The number of bytes written to the disk per second. |
| (Agent) Host.disk.writeiop s | Count/s | disk writeiops _ | userId, instanceId, and device | The number of write IOPS of the disk. |
| (Agent) Host.tcpconnecti on | Count | net tcpconnectio _ n | userId, instanceId, and state | The number of Transmission Control Protocol (TCP) connections in each state. |

**ApsaraDB RDS**

By default, an old link is used for ApsaraDB RDS. The period of collected data is 60 to 300 seconds. Set **Namespace** to **acs_rds_dashboard**. Set **Period** to a value **from 60 to 300**. Unit: seconds. ApsaraDB RDS supports four engines: MySQL, SQL Server, PolarDB, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |

Monitor API Reference

| MemoryUsage | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| MySQL NetworkI _ nNew | bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL NetworkO _ utNew | bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS _ | Count/s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second for the ApsaraDB RDS for MySQL instance. |

**ApsaraDB RDS for SQL Server**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |
| SQLServer Netwo _ rkInNew | bit/s | SQLServer Netw _ orkInNew | userId and instanceId | The inbound traffic to the ApsaraDB RDS for SQL Server instance per second. |
| SQLServer Netwo _ rkOutNew | bit/s | SQLServer Netw _ orkOutNew | userId and instanceId | The outbound traffic from the ApsaraDB RDS for SQL Server instance per second. |

**ApsaraDB RDS for PolarDB**

Monitor API Reference

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage | userId and instanceId | The disk utilization. |
| IOPSUsage | % | IOPSUsage | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |

**ApsaraDB RDS (new link)**

ApsaraDB RDS also supports a new link. The period of collected data is 60 seconds. Set **Namespace** to **acs_rds_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds. ApsaraDB RDS (new link) supports three engines: MySQL, PolarDB, and PostgreSQL.

**ApsaraDB RDS for MySQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage new _ | userId and instanceId | The disk usage. |

Monitor API Reference

| IOPSUsage | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
|---|---|---|---|---|
| MemoryUsage | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |
| MySQL NetworkI _ nNew | bit/s | MySQL NetworkI _ nNew new _ | userId and instanceId | The inbound traffic to the ApsaraDB RDS for MySQL instance per second. |
| MySQL NetworkO _ utNew | bit/s | MySQL NetworkO _ utNew new _ | userId and instanceId | The outbound traffic from the ApsaraDB RDS for MySQL instance per second. |
| MySQL QPS _ | Count/s | MySQL QPS new _ _ | userId and instanceId | The number of queries per second for the ApsaraDB RDS for MySQL instance. |
| DockerCpuUsage | % | DockerCpuUsage new _ | userId and instanceId | The CPU usage of the Docker. |

**ApsaraDB RDS for PolarDB**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage new _ | userId and instanceId | The CPU usage. |
| DiskUsage | % | DiskUsage new _ | userId and instanceId | The disk usage. |
| IOPSUsage | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |

**ApsaraDB RDS for PostgreSQL**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ConnectionUsage | % | ConnectionUsage new _ | userId and instanceId | The connection usage. |
| CpuUsage | % | CpuUsage new _ | userId and instanceId | The CPU usage. |

Monitor API Reference

| DiskUsage | % | DiskUsage new _ | userId and instanceId | The disk usage. |
|---|---|---|---|---|
| IOPSUsage | % | IOPSUsage new _ | userId and instanceId | The number of I/O requests per second. |
| MemoryUsage | % | MemoryUsage n _ ew | userId and instanceId | The memory usage. |

**Server Load Balancer (SLB)**

Set **Namespace** to **acs_slb_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ActiveConnection | Count | ActiveConnection | userId, instanceId, port, and protocol | The number of active TCP connections. |
| InactiveConnecti on | Count | InactiveConnecti on | userId, instanceId, port, and protocol | The number of inactive connections on the port. |
| MaxConnection | Count/s | MaxConnection | userId, instanceId, port, and protocol | The number of concurrent connections per second on the port. |
| NewConnection | Count | NewConnection | userId, instanceId, port, and protocol | The number of new TCP connections. |
| PacketRX | Count/s | PacketRX | userId, instanceId, port, and protocol | The number of outbound packets per second. |
| PacketTX | Count/s | PacketTX | userId, instanceId, port, and protocol | The number of inbound packets per second. |
| TrafficRXNew | bit/s | TrafficRXNew | userId, instanceId, port, and protocol | The inbound bandwidth. |
| TrafficTXNew | bit/s | TrafficTXNew | userId, instanceId, port, and protocol | The outbound bandwidth. |
| UnhealthyServer Count | Count | UnhealthyServer Count | userId, instanceId, port, and vip | The number of unhealthy ECS instances. |

**Object Storage Service (OSS)**

Set **Namespace** to **acs_oss_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

**Overview**

Monitor API Reference

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| RequestValidRate | % | RequestValidRat e | userId and BucketName | The rate of valid requests. |
| ValidRequestCou nt | Count | ValidRequestCou nt | userId and BucketName | The number of valid requests. |
| TotalRequestCou nt | Count | TotalRequestCou nt | userId and BucketName | The total number of requests. |
| Availability | % | Availability | userId and BucketName | The availability. Stay alert if this metric is lower than 100%. |
| InternetSend | Byte | InternetSend | userId and BucketName | The outbound traffic from the Internet. |
| InternetRecv | Byte | InternetRecv | userId and BucketName | The inbound traffic to the Internet. |
| IntranetSend | Byte | IntranetSend | userId and BucketName | The outbound traffic from the intranet. |
| IntranetRecv | Byte | IntranetRecv | userId and BucketName | The inbound traffic to the intranet. |
| CdnSend | Byte | CdnSend | userId and BucketName | The CDN outbound traffic. |
| CdnRecv | Byte | CdnRecv | userId and BucketName | The CDN inbound traffic. |
| SyncSend | Byte | SyncSend | userId and BucketName | The cross-region replication outbound traffic. |
| SyncRecv | Byte | SyncRecv | userId and BucketName | The cross-region replication inbound traffic. |
| MeteringStorage Utilization | Byte | MeteringStorage Utilization | userId and BucketName | The currently used storage. |

**Request status details**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| ServerErrorCount | Count | ServerErrorCount | userId and BucketName | The number of requests with a server error. |
| ServerErrorRate | % | ServerErrorRate | userId and BucketName | The ratio of requests with a server error. |

Monitor API Reference

| NetworkErrorCou nt | Count | NetworkErrorCou nt | userId and BucketName | The number of requests with a network error. |
|---|---|---|---|---|
| NetworkErrorRate | % | NetworkErrorRat e | userId and BucketName | The ratio of requests with a network error. |
| AuthorizationErro rCount | Count | AuthorizationErro rCount | userId and BucketName | The number of requests with an authorization error. |
| ResourceNotFoun dErrorCount | Count | ResourceNotFoun dErrorCount | userId and BucketName | The number of requests with an error that indicates resources cannot be found. |
| ClientTimeoutErr orCount | Count | ClientTimeoutErr orCount | userId and BucketName | The number of requests with a client timeout error. |
| ClientOtherErrorC ount | Count | ClientOtherError Count | userId and BucketName | The number of requests with other client errors. |
| AuthorizationErro rRate | % | AuthorizationErro rRate | userId and BucketName | The ratio of requests with an authorization error. |
| ResourceNotFoun dErrorRate | % | ResourceNotFoun dErrorRate | userId and BucketName | The ratio of requests with an error that indicates resources cannot be found. |
| ClientTimeoutErr orRate | % | ClientTimeoutErr orRate | userId and BucketName | The ratio of requests with a client timeout error. |
| ClientOtherErrorR ate | N/A | ClientOtherError Rate | userId and BucketName | The ratio of requests with other client errors. |
| SuccessCount | Count | SuccessCount | userId and BucketName | The number of successful requests. |
| RedirectCount | Count | RedirectCount | userId and BucketName | The number of redirected requests. |

Monitor API Reference

| SuccessRate | % | SuccessRate | userId and BucketName | The ratio of successful requests. |
|---|---|---|---|---|
| RedirectRate | % | RedirectRate | userId and BucketName | The ratio of redirected requests. |

**Maximum latency**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| MaxGetObjectE2 eLatency | Milliseconds | MaxGetObjectE2 eLatency | userId and BucketName | The maximum E2E latency of GetObject requests. |
| MaxGetObjectSer verLatency | Milliseconds | MaxGetObjectSer verLatency | userId and BucketName | The maximum server latency of GetObject requests. |
| MaxHeadObjectE 2eLatency | Milliseconds | MaxHeadObjectE 2eLatency | userId and BucketName | The maximum E2E latency of HeadObject requests. |
| MaxHeadObjectS erverLatency | Milliseconds | MaxHeadObjectS erverLatency | userId and BucketName | The maximum server latency of HeadObject requests. |
| MaxPutObjectE2e Latency | Milliseconds | MaxPutObjectE2e Latency | userId and BucketName | The maximum E2E latency of PutObject requests. |
| MaxPutObjectSer verLatency | Milliseconds | MaxPutObjectSer verLatency | userId and BucketName | The maximum server latency of PutObject requests. |
| MaxAppendObjec tE2eLatency | Milliseconds | MaxAppendObjec tE2eLatency | userId and BucketName | The maximum E2E latency of AppendObject requests. |
| MaxAppendObjec tServerLatency | Milliseconds | MaxAppendObjec tServerLatency | userId and BucketName | The maximum server latency of AppendObject requests. |
| MaxUploadPartE2 eLatency | Milliseconds | MaxUploadPartE2 eLatency | userId and BucketName | The maximum E2E latency of UploadPart requests. |
| MaxUploadPartSe rverLatency | Milliseconds | MaxUploadPartSe rverLatency | userId and BucketName | The maximum server latency of UploadPart requests. |

Monitor API Reference

| MaxUploadPartCo pyE2eLatency | Milliseconds | MaxUploadPartC opyE2eLatency | userId and BucketName | The maximum E2E latency of UploadPartCopy requests. |
|---|---|---|---|---|
| MaxUploadPartCo pyServerLatency | Milliseconds | MaxUploadPartC opyServerLatenc y | userId and BucketName | The maximum server latency of UploadPartCopy requests. |

**Successful requests of different types**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| GetObjectCount | Frequency | GetObjectCount | userId and BucketName | The number of successful GetObject requests. |
| HeadObjectCount | Count | HeadObjectCount | userId and BucketName | The number of successful HeadObject requests. |
| PostObjectCount | Count | PostObjectCount | userId and BucketName | The number of successful PostObject requests. |
| AppendObjectCo unt | Count | AppendObjectCo unt | userId and BucketName | The number of successful AppendObject requests. |
| UploadPartCount | Count | UploadPartCount | userId and BucketName | The number of successful UploadPart requests. |
| UploadPartCopyC ount | Count | UploadPartCopyC ount | userId and BucketName | The number of successful UploadPartCopy requests. |
| DeleteObjectCou nt | Count | DeleteObjectCou nt | userId and BucketName | The number of successful DeleteObject requests. |
| DeleteObjectsCo unt | Count | DeleteObjectsCo unt | userId and BucketName | The number of successful DeleteObjects requests. |

**KVStore for Redis**

Set **Namespace** to **acs_kvstore**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|

Monitor API Reference

| ConnectionUsage | % | ConnectionUsage | userId and instanceId | The connection usage. |
|---|---|---|---|---|
| CpuUsage | % | CpuUsage | userId and instanceId | The CPU usage. |
| FailedCount | Count/S | FailedCount | userId and instanceId | The number of failed operations. |
| IntranetIn | Byte/s | IntranetIn | userId and instanceId | The inbound traffic to the intranet. |
| IntranetInRatio | % | IntranetInRatio | userId and instanceId | The write bandwidth usage. |
| IntranetOut | Byte/s | IntranetOut | userId and instanceId | The outbound traffic from the intranet. |
| IntranetOutRatio | % | IntranetOutRatio | userId and instanceId | The read bandwidth usage. |
| MemoryUsage | % | MemoryUsage | userId and instanceId | The memory usage. |
| UsedQPS | Count/S | UsedQPS | userId and instanceId | The number of used queries per second (QPS). |

**ApsaraDB for MongoDB**

Set **Namespace** to **acs_mongodb**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

**Basic metrics**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| CPUUtilization | % | CPUUtilization | userId, instanceId, and role | The CPU usage. |
| MemoryUtilizatio n | % | MemoryUtilizatio n | userId, instanceId, and role | The memory usage. |
| DiskUtilization | % | DiskUtilization | userId, instanceId, and role | The ratio of used disk space. |
| IOPSUtilization | % | IOPSUtilization | userId, instanceId, and role | The IOPS usage. |
| ConnectionAmou nt | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

Monitor API Reference

| QPS | Count | QPS | userId, instanceId, and role | The number of requests per second. |
|---|---|---|---|---|
| ConnectionAmou nt | Count | ConnectionAmou nt | userId, instanceId, and role | The number of used connections. |

**Disk capacity**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| InstanceDiskAmo unt | Byte | InstanceDiskAmo unt | userId, instanceId, and role | The disk space occupied by the instance. |
| DataDiskAmount | Byte | DataDiskAmount | userId, instanceId, and role | The disk space occupied by data. |
| LogDiskAmount | Byte | LogDiskAmount | userId, instanceId, and role | The disk space occupied by logs. |

**Network requests**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| IntranetIn | Byte | IntranetIn | userId, instanceId, and role | The inbound traffic to the intranet. |
| IntranetOut | Byte | IntranetOut | userId, instanceId, and role | The outbound traffic from the intranet. |
| NumberRequests | Count | NumberRequests | userId, instanceId, and role | The number of requests. |

**Operation count**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| OpCommand | Count | OpCommand | userId, instanceId, and role | The number of Command operations. |
| OpDelete | Count | OpDelete | userId, instanceId, and role | The number of Delete operations. |
| OpGetmore | Count | OpGetmore | userId, instanceId, and role | The number of Getmore operations. |
| OpInsert | Count | OpInsert | userId, instanceId, and role | The number of Insert operations. |

Monitor API Reference

| OpQuery | Count | OpQuery | userId, instanceId, and role | The number of Query operations. |
|---|---|---|---|---|
| OpUpdate | Count | OpUpdate | userId, instanceId, and role | The number of Update operations. |

**AnalyticDB for PostgreSQL**

Set **Namespace** to **acs_hybriddb**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| (Resource reservation) ConnectionUsage | % | ConnectionUsage | userId, instanceId, and role | The connection usage. |
| (Resource reservation) CpuUsage | % | CpuUsage | userId, instanceId, and role | The CPU usage. |
| (Resource reservation) DiskUsage | % | DiskUsage | userId, instanceId, and role | The disk usage. |
| (Resource reservation) IOPSUsage | % | IOPSUsage | userId, instanceId, and role | The IOPS usage. |
| (Resource reservation) MemoryUsage | % | MemoryUsage | userId, instanceId, and role | The memory usage. |

**VPN Gateway**

Set **Namespace** to **acs_vpn**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| ipsec.rxPkgs | pps | ipsec.rxPkgs | userId, instanceId, and ipsecId | The rate of inbound packets of the connection. |
| ipsec.txPkgs | pps | ipsec.txPkgs | userId, instanceId, and ipsecId | The rate of outbound packets for the connection. |
| ipsec rx.rate _ | bits/s | ipsec rx.rate _ | userId, instanceId, and ipsecId | The number of inbound bits per second for the connection. |
| ipsec tx.rate _ | bits/s | ipsec tx.rate _ | userId, instanceId, and ipsecId | The number of outbound bits per second for the connection. |

Monitor API Reference

| ssl client.count _ | count | ssl client.count _ | userId and instanceId | The number of connections. |
|---|---|---|---|---|

**AnalyticDB for MySQL 3.0**

Set **Namespace** to **acs_adb**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| connections | count | connections | userId and instanceId | The number of cluster connections. |
| worker avg cpu _ _ _ used | % | worker avg cpu _ _ _ used | userId and instanceId | The CPU usage of the worker. |
| executor avg cp _ _ u used _ | % | executor avg cp _ _ u used _ | userId and instanceId | The CPU usage of the executor. |
| worker max nod _ _ e disk used perc _ _ _ ent | % | worker max nod _ _ e disk used perc _ _ _ ent | userId and instanceId | The maximum disk usage of the worker in reserved mode. |
| disk used percen _ _ t | % | disk used percen _ _ t | userId and instanceId | The disk usage in reserved mode. |
| worker max nod _ _ e disk used MB _ _ _ | Mbyte | worker max nod _ _ e disk used MB _ _ _ | userId and instanceId | The maximum used disk space of the worker in elastic mode. |
| ColdDataDiskUsa ge | Mbyte | ColdDataDiskUsa ge | userId and instanceId | The used disk space for cold data in elastic mode. |
| HotDataDiskUsag e | Mbyte | HotDataDiskUsag e | userId and instanceId | The used disk space for hot data in elastic mode. |
| worker avg read _ _ bytes _ | Mbyte | worker avg read _ _ bytes _ | userId and instanceId | The read throughput of the worker. |
| worker avg write _ _ bytes _ | Mbyte | worker avg write _ _ bytes _ | userId and instanceId | The write throughput of the worker. |
| executor avg rea _ _ d bytes MB _ _ | Mbyte | executor avg re _ _ ad bytes MB _ _ | userId and instanceId | The read throughput of the executor. |
| executor avg wri _ _ te bytes MB _ _ | Mbyte | executor avg wri _ _ te bytes MB _ _ | userId and instanceId | The write throughput of the executor. |
| worker avg read _ _ iops _ | count/s | worker avg read _ _ iops _ | userId and instanceId | The read IOPS of the worker. |

Monitor API Reference

| worker avg write _ _ iops _ | count/s | worker avg write _ _ iops _ | userId and instanceId | The write IOPS of the worker. |
|---|---|---|---|---|
| executor avg rea _ _ d iops _ | count/s | executor avg re _ _ ad iops _ | userId and instanceId | The read IOPS of the executor. |
| executor avg wri _ _ te iops _ | count/s | executor avg wri _ _ te iops _ | userId and instanceId | The write IOPS of the executor. |
| worker avg io ut _ _ _ il | % | worker avg io ut _ _ _ il | userId and instanceId | The disk I/O usage. |
| QPS | count/s | qps | userId and instanceId | The number of requests per second. |
| query avg rt _ _ | ms | query avg rt _ _ | userId and instanceId | The average query time. |
| query max rt _ _ | ms | query max rt _ _ | userId and instanceId | The maximum query time. |
| query total wait _ _ _ time | ms | query total wait _ _ _ time | userId and instanceId | The average query waiting time. |
| query max wait _ _ _ time | ms | query max wait _ _ _ time | userId and instanceId | The maximum query waiting time. |
| tps | count/s | tps | userId and instanceId | The number of transactions per second. |
| insert avg rt _ _ | ms | insert avg rt _ _ | userId and instanceId | The average write response time. |
| insert max rt _ _ | ms | insert max rt _ _ | userId and instanceId | The maximum write response time. |
| insert in bytes _ _ | Mbyte | insert in bytes _ _ | userId and instanceId | The write throughput. |

**Elastic IP Address (EIP)**

Set **Namespace** to **acs_vpc_eip**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | Metric | Dimensions | Description |
|---|---|---|---|---|
| net rx.rate _ | bit/s | net rx.rate _ | userId and instanceId | The inbound bandwidth. |
| net rxPkgs.rate _ | count/S | net rxPkgs.rate _ | userId and instanceId | The rate of inbound packets. |
| net tx.rate _ | bit/s | net tx.rate _ | userId and instanceId | The outbound bandwidth. |

Monitor API Reference

| net txPkgs.rate _ | count/ | net txPkgs.rate _ | userId and instanceId | The rate of outbound packets. |
|---|---|---|---|---|
| out ratelimit dro _ _ p speed _ | count/s | out ratelimit dro _ _ p speed _ | userId and instanceId | The rate at which packets are dropped due to throttling. |

**API Gateway**

Set **Namespace** to **acs_apigateway_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| Latency | ms | Latency | userId, region, and apiUid | The response time. |
| SumQPS | Count | SumQPS | userId, region, and apiUid | The total number of requests. |
| TrafficRX | KBytes | TrafficRX | userId, region, and apiUid | The inbound traffic. |
| TrafficTX | KBytes | TrafficTX | userId, region, and apiUid | The outbound traffic. |
| code2XX | Count | code2XX | userId, region, and apiUid | The number of times a 2XX HTTP status code is returned. |
| code4XX | Count | code4XX | userId, region, and apiUid | The number of times a 4XX HTTP status code is returned. |
| code5XX | Count | code5XX | userId, region, and apiUid | The number of times a 5XX HTTP status code is returned. |

**Hologres**

Set **Namespace** to **acs_hologres**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

**Instance status**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| connection num _ | Count | connection num _ | userId and instanceId | The number of connections. |
| connection usag _ e | % | connection usag _ e | userId and instanceId | The connection usage. |
| cpu usage _ | % | cpu usage _ | userId and instanceId | The CPU usage. |

Monitor API Reference

| memory usage _ | % | memory usage _ | userId and instanceId | The memory usage. |
|---|---|---|---|---|
| storage usage _ | Bytes | storage usage _ | userId and instanceId | The used storage. |
| io write through _ _ put | Bytes | io write through _ _ put | userId and instanceId | The I/O write throughput per second. |
| io read throughp _ _ ut | Bytes | io read throughp _ _ ut | userId and instanceId | The I/O read throughput per second. |

**Running status**

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| failed query qps _ _ | count/s | failed query qps _ _ | userId and instanceId | The number of failed queries per second. |
| query latency _ | ms | query latency _ | instanceId, userId, and cmdType | The latency of the query. |
| Query QPS | count/s | query qps _ | instanceId, userId, and cmdType | The QPS. |
| dml rps _ | count/s | dml rps _ | instanceId, userId, and cmdType | The number of write records per second. |

**Tablestore**

Set **Namespace** to **acs_ots_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|
| InstanceVCU | count/s | InstanceVCU | userId and instanceName | The VCUs of the instance. |
| InstanceReserved VCU | count/s | InstanceReserve dVCU | userId and instanceName | The reserved VCUs of the instance. |
| InstanceFreeRea dCU NoOp _ | count/s | InstanceFreeRea dCU NoOp _ | userId and instanceName | The internal read CUs. |
| InstanceFreeWrit eCU NoOp _ | count/s | InstanceFreeWrit eCU NoOp _ | userId and instanceName | The internal write CUs. |
| InstanceOverRea dCU NoOp _ | count/s | InstanceOverRea dCU NoOp _ | userId and instanceName | The excess read CUs of the instance. |
| InstanceOverWrit eCU NoOp _ | count/s | InstanceOverWrit eCU NoOp _ | userId and instanceName | The excess write CUs of the instance. |

Monitor API Reference

| InstanceReadCU _ NoOp | count/s | InstanceReadCU _ NoOp | userId and instanceName | The operation read CUs. |
|---|---|---|---|---|
| InstanceWriteCU _ NoOp | count/s | InstanceWriteCU _ NoOp | userId and instanceName | The operation write CUs. |
| InstanceRequest Number NoOp _ | count/s | InstanceRequest Number NoOp _ | userId and instanceName | The total number of requests. |
| InstanceCount2x xNumber NoOp _ | count/s | InstanceCount2x xNumber NoOp _ | userId and instanceName | The number of requests that return a 2XX HTTP status code. |
| InstanceCount42 9Number NoOp _ | count/s | InstanceCount42 9Number NoOp _ | userId and instanceName | The number of requests that return HTTP status code 429. |
| InstanceCount4x xNumber NoOp _ | count/s | InstanceCount4x xNumber NoOp _ | userId and instanceName | The number of requests that return a 4XX HTTP status code. |
| InstanceCount5x xNumber NoOp _ | count/s | InstanceCount5x xNumber NoOp _ | userId and instanceName | The number of requests that return a 5XX HTTP status code. |
| InstanceExtranetI n NoOp _ | Bytes/s | InstanceExtranetI n NoOp _ | userId and instanceName | The inbound traffic to the Internet. |
| InstanceExtranet Out NoOp _ | Bytes/s | InstanceExtranet Out NoOp _ | userId and instanceName | The outbound traffic from the Internet. |
| InstanceFreeExtr anetOut NoOp _ | Bytes/s | InstanceFreeExtr anetOut NoOp _ | userId and instanceName | The outbound traffic from the Internet that is free of charge. |
| InstanceRowCoun t NoOp _ | count/s | InstanceRowCou nt NoOp _ | userId and instanceName | The total number of rows. |
| InstanceFailRowC ount NoOp _ | count/s | InstanceFailRowC ount NoOp _ | userId and instanceName | The number of failed rows. |

**Elasticsearch**

Set **Namespace** to **acs_ots_dashboard**. Set **Period** to **60** or a multiple of 60. Unit: seconds.

| Metric | Unit | MetricName | Dimensions | Description |
|---|---|---|---|---|

Monitor API Reference

| ClusterStatus | Value | ClusterStatus | userId and instanceId | The status of the cluster. Valid values: 0: green, which indicates normal. 1: yellow, which indicates warning. 2: red, which indicates exception. |
|---|---|---|---|---|
| NodeCPUUtilizati on | % | NodeCPUUtilizati on | userId and instanceId | The CPU usage of the instance node. |
| NodeDiskUtilizati on | % | NodeDiskUtilizati on | userId and instanceId | The disk usage of the instance node. |
| NodeHeapMemor yUtilization | % | NodeHeapMemor yUtilization | userId and instanceId | The HeapMemory usage of the instance node. |

### 5.3 API Reference

#### 5.3.1 Cloud Products

##### 5.3.1.1 DescribeProjectMeta

You can call this operation to query information of monitored services in Cloud Monitor. The information obtained by this operation includes the service description, namespace, and tags.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeProject Meta | The operation that you want to perform. Set the value to DescribeProjectMeta. |
| callerType | String | No | "" | The type of the caller. |

Monitor API Reference

|   |   |   |   |   |   | The tags of metrics. You can specify tags of metrics to filter services. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag |   |
|   |   |   |   |   |   | name","value":"Tag value"}, |   |   |
|   |   |   |   |   |   | {"name":"Tag name","value":"Tag |   |   |
|   |   |   |   |   |   | value"}] |   |   |
| Labels |   | String | No | [{"name":"prod uct","value":"EC S"}] |   |   |   |   |
| PageNumber |   | Integer | No | 1 |   | The number of the page to return. Default value: 1. |   |   |

Monitor API Reference

| PageSize | Integer | No | 30 | The number of entries to return on each page. Default value: 30. Note Apsara Stack does not limit the value of this parameter. If you want to view all desired entries on a small number of pages, set this parameter to a greater value. |
|---|---|---|---|---|
| RequestId | string | No | sdsdsdd | The ID of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RequestId | String | 4C2061B2-3B1B- 43BF-A4A4- C53426F479C0 | The ID of the request. |
| Resources | Array | N/A | The information of services found. |
| Resource | N/A | N/A | The information of a service found. |
| Description | String | CDN | The description of the service. |

Monitor API Reference

|   |   |   |   |   |   | The tags of metrics. Services were filtered based on the specified tags. A tag of a metric is used as a special mark of alerts triggered by the metric. For example, a tag can specify the service specification to which an alert belongs and whether an alert rule can be configured for a metric. The format is [{"name":"Tag name","value":"Tag |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"Tag name","value":"Tag |   |
|   |   |   |   |   |   | value"},{"name":"Tag |   |   |
|   |   |   |   |   |   | name","value":"Tag value"}] |   |   |
|   | Labels | String |   |   | [{"groupFlag":true }] |   |   |   |
|   | Namespace | String |   |   | acs cdn _ | The namespace of the service, which is used to distinguish between services. Typically, the value of the format is acs Abbreviation of the service _ name . |   |   |
|   |   |   |   |   |   |   | acs Abbreviation of the service _ |   |
|   |   |   |   |   |   | name |   |   |
|   | Success | Boolean |   |   | true | Indicates whether the call was successful. |   |   |

Monitor API Reference

| Total | String | 12 | The total number of entries returned. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeProjectMeta &<Common request parameters>
```

Sample success responses

**Note**

The response content varies with the services that are actually monitored. `JSON` format `{`

```json
 "PageNumber":1,
 "PageSize":5,
 "RequestId":"4C2061B2-3B1B-43BF-A4A4-C53426F479C0",
 "Success":true,
 "Code":200,
 "Total":62,
 "Resources":{
  "Resource":[{
     "Description": "ECS",
     "Labels": "[{\"name\":\"product\",\"value\":\"ECS\"},
{\"name\":\"productCategory\",\"value\":\"ecs,ecs_net_interface,hpc_node,hpc_cluster\"}, {\"name\":\"groupFlag\",\"value\":\"true\"},{\"name\":\"cnName\",\"value\":\"ECS\"},{\" name\":\"enName\",\"value\":\"ECS\"}]",
     "Namespace": "acs_ecs_dashboard"
```

`},` `]` `}` `}`

##### 5.3.1.2 DescribeMetricLast

You can call this operation to query the latest monitoring data of a monitored object.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricL ast | The operation that you want to perform. Set the value to DescribeMetricLast. |

Monitor API Reference

| MetricName | String | Yes | CPUUtilization | The name of the metric. |   |   |   |
|---|---|---|---|---|---|---|---|
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. Specify the value in the format of acs Service name. _ |   |   |   |
| Dimensions | String | No | [{"instanceId":" XXXXXX"}] | The dimension map of the monitored resources. The value is a collection of key- value pairs. A typical key- value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note If you hope to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |   |   |   |
|   |   |   |   |   |   | key- |   |
|   |   |   |   |   | key- |   |   |
| EndTime | String | No | 2019-01-31 10:10:00 | The end of the time range for the query. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Note Only a time range within the last 270 days can be specified to query. |   |   |   |
| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression for real-time computation on the query results. |   |   |   |
| Length | String | No | 1000 | The number of entries to return on each page. Default value: 1000. |   |   |   |

|   | value |   |
|---|---|---|
|   | value |   |

Monitor API Reference

| NextToken | String | No | 1576143285000 9dd70bb64cff1f 0fff6c0b08ffff07 3be5fb1e785e2 b020f7fed9b5e1 37bd810a6d6cff 5ae**** | The pagination cursor. If the number of entries that match the search criteria exceeds the maximum number allowed on a single page, a pagination cursor is returned. This pagination cursor can be used as an input parameter to obtain entries on the next page. If a response does not contain pagination cursors, all query results are returned. |
|---|---|---|---|---|
| Period | String | No | 60 | The time interval at which to query monitoring data. Typically, the time interval is the same as the interval for reporting metric data. Unit: seconds. If you do not specify this parameter, raw data is queried at the reporting interval specified when the corresponding metric was created. If a statistical period was specified for the corresponding alert rule, raw data is queried based on the statistical period. |
| StartTime | String | No | 2019-01-31 10:00:00 | The start of the time range for the query. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Note Only a time range that covers a maximum of 31 days within the last 270 days can be specified to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 021472A6-25E3- 4094-8D00- BA4B6A5486C3 | The ID of the request. |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |

Monitor API Reference

| Success | Boolean | true | Indicates whether the call was successful. |
|---|---|---|---|
| Period | String | 60 | The time interval at which monitoring data was queried. Unit: seconds. |
| NextToken | String | xxxxxx | The pagination cursor. |
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The list of monitoring data. |
| Message | String | Success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMetricLast &MetricName=CPUUtilization &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

```xml
<QueryMetricListResponse>
    <Period>60</Period>
    <Datapoints>
        <Datapoints>
            <timestamp>1490152860000</timestamp>
            <Maximum>100</Maximum>
            <userId> 123456789876****</userId>
            <Minimum>93.1</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.52</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490152920000</timestamp>
            <Maximum>100</Maximum>
            <userId> 123456789876**** </userId>
            <Minimum>92.59</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.49</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490152980000</timestamp>
<Maximum>100</Maximum>
```

Monitor API Reference

```xml
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.86</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.44</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153040000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>91.43</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.36</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153100000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>93.55</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.51</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153160000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>93.1</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.52</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153220000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
            <Minimum>92.59</Minimum>
            <instanceId>i-abcdefgh12****</instanceId>
            <Average>99.42</Average>
        </Datapoints>
        <Datapoints>
            <timestamp>1490153280000</timestamp>
            <Maximum>100</Maximum>
            <userId>123456789876****</userId>
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
```

Monitor API Reference `p`

```xml
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

`JSON` format `{`

```json
 "Period":"60",
 "Datapoints":[
```

`{`

```json
   "timestamp":1490152860000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490152920000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.49
```

`},` `{`

```json
   "timestamp":1490152980000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.44
```

`},` `{`

```json
   "timestamp":1490153040000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.43,
   "Average":99.36
```

`},` `{`

```json
   "timestamp":1490153100000,
   "Maximum":100,
"userId":"123456789876****"
```

Monitor API Reference

```json
   userId:123456789876****,
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.55,
   "Average":99.51
```

`},` `{`

```json
   "timestamp":1490153160000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490153220000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.42
```

`},` `{`

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

`}` `],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

`}`

##### 5.3.1.3 DescribeMetricList

Monitor API Reference You can call this operation to query the monitoring data of time series metrics of Apsara Stack services in a specified period. For more information about how to assign values to the Namespace, Project, Metric, Period, and Dimensions parameters for Apsara Stack services, see Metrics for Apsara Stack services.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|
| Action | String | Yes | DescribeMetricLi st | The operation that you want to perform. Set the value to DescribeMetricList. |   |   |   |
| MetricName | String | Yes | cpu idle _ | The name of the metric that you want to query. |   |   |   |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. Specify the value in the format of acs Service name. _ |   |   |   |
| Dimensions | String | No | [{"instanceId": "i- abcdefgh12****" }] | The dimension map of the monitored resources. The value is a collection of key- value pairs. A typical key- value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note If you want to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |   |   |   |
|   |   |   |   |   |   | key- |   |
|   |   |   |   |   | key- |   |   |
| EndTime | String | No | 2019-01-30 00:10:00 | The end of the time range for the query. Supported formats: UNIX timestamp: The value can be a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Time format: The value can be in the YYYY-MM-DDThh:mm:ssZ format. |   |   |   |

|   | value |   |
|---|---|---|
|   | value |   |

Monitor API Reference

| Express | String | No | {"groupby": ["userId","instan ceId"]} | The expression for real-time computation on the query results. Only the groupby expression is supported, which is similar to the groupby statement used in databases. |
|---|---|---|---|---|
| Length | String | No | 1000 | The number of entries to return on each page. Default value: 1000. |
| NextToken | String | No | 1576148535000 9dd70bb64cff1f 0fff750b08ffff07 3be5fb1e785e2 b020f1a949d5e a14aea7fed82f0 1dd87311 | The pagination cursor. Note You do not need to specify this parameter if you only want to obtain entries on the first page. The pagination cursor returned in a response can be used as an input parameter for obtaining entries on the next page. If a response contains no pagination cursors, all the query result has been returned. |
| Period | String | No | 60 | The time interval at which monitoring data is queried. Unit: seconds. Valid values: 60, 300, and 900, which represent 1 minute, 5 minutes, and 15 minutes. Note Set this parameter to suit your needs. For example, if you set this parameter to 60, only 1,000 records are returned, though a total of 1,440 records are generated. This is because the maximum number of records that can be returned for each query is 1,000. If you set this parameter to 300, 288 records are returned. |

Monitor API Reference

| StartTime | String | No | 2019-01-30 00:00:00 | The start of the time range for the query. Supported formats: UNIX timestamp: The value can be a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. Time format: The value can be in the YYYY-MM-DDThh:mm:ssZ format. Note The period specified by StartTime and EndTime includes the time point specified by EndTime but does not include the time point specified by StartTime. StartTime must be earlier than EndTime. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3121AE7D-4AFF- 4C25-8F1D- C8226EBB1F42 | The ID of the request. |
| Code | String | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Success | Boolean | true | Indicates whether the call was successful. |
| NextToken | String | 15761441850009d d70bb64cff1f0fff6d 0b08ffff073be5fb1 e785e2b020f7fed9 b5e137bd810a6d6 cff5aee816 | The pagination cursor. Note If this parameter was not specified, only entries on the first page were returned. If a response contains a pagination cursor, more entries are to be returned. If a response contains no pagination cursors, all the query result has been returned. |

Monitor API Reference

| Period | String | 60 | The time interval at which monitoring data was queried. Unit: seconds. Valid values: 60, 300, and 900. |
|---|---|---|---|
| Datapoints | String | [{"timestamp":154 8777660000,"userI d":"123","instanceI d":"i- abc","Minimum":9. 92,"Average":9.92, "Maximum":9.92}] | The list of monitoring data. |
| Message | String | Success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DescribeMetricList &MetricName=cpu_idle &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses `XML` format

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
```

`ti` `t`

```
1490153040000/ti
```

`t` Monitor API Reference

```xml
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
</Datapoints>
```

Monitor API Reference

```xml
</Datapoints> <RequestId>6A5F022D-AC7C-460E-94AE-B9E75083D027</RequestId> <Success>true</Success> <Code>200</Code>
```

`JSON` format `{`

```json
 "Period":"60",
 "Datapoints":[
```

`{`

```json
   "timestamp":1490152860000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490152920000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.49
```

`},` `{`

```json
   "timestamp":1490152980000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.86,
   "Average":99.44
```

`},` `{`

```json
   "timestamp":1490153040000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":91.43,
   "Average":99.36
```

`},` `{`

```json
   "timestamp":1490153100000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.55,
   "Average":99.51
```

`},` `{`

```json
   "timestamp":1490153160000,
   "Maximum":100,
   "userId":"123456789876****",
```

Monitor API Reference

```json
   "instanceId":"i-abcdefgh12****",
   "Minimum":93.1,
   "Average":99.52
```

`},` `{`

```json
   "timestamp":1490153220000,
   "Maximum":100,
   "userId":"123456789876****",
   "instanceId":"i-abcdefgh12****",
   "Minimum":92.59,
   "Average":99.42
```

`},` `{`

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

`}` `],`

```json
 "RequestId":"6A5F022D-AC7C-460E-94AE-B9E75083D027",
 "Success":true,
 "Code":"200"
```

`}`

##### 5.3.1.4 DescribeMetricMetaList

Queries the descriptions of time series metrics that are supported in CloudMonitor. This operation is used with DescribeMetricList and DescribeMetricLast.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

Monitor API Reference

|   | Action | String |   | Yes |   | DescribeMetricM etaList | The operation that you want to perform. Set the value to DescribeMetricMetaList. |   |
|---|---|---|---|---|---|---|---|---|
|   | Namespace | String |   | Yes |   | acs kvstore _ | The namespace of the service. You can call the DescribeProjectMeta operation to query the namespace of each service. |   |
|   |   |   |   |   |   |   | The tags of the metric. You must specify the tags in the following format: [{&quot;name&quot;:&quot |   |
|   |   |   |   |   |   |   |   | [{&quot;name&quot;:&quot |
|   |   |   |   |   |   |   | ;Tag |   |
|   |   |   |   |   |   |   | key&quot;,&quot;value&quot;:&quo |   |
|   |   |   |   |   |   |   | t;Tag value&quot;}, |   |
|   |   |   |   |   |   |   | {&quot;name&quot;:&quot;Tag |   |
|   |   |   |   |   |   |   | key&quot;,&quot;value&quot;:&quo |   |
|   |   |   |   |   |   | [{&quot;name& | t;Tag value&quot;}] |   |
|   | Labels | String |   | No |   | quot;:&quot;pro ductCategory&q uot;,&quot;value &quot;:&quot;kv store old&quot; _ }] |   |   |
|   | MetricName | String |   | No |   | CPUUtilization | The name of the metric. The metric with the specified name is matched. |   |
|   | PageNumber | Integer |   | No |   | 1 | The number of the page to return. Default value: 1. |   |
|   | PageSize | Integer |   | No |   | 30 | The number of entries to return on each page. Default value: 30. |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the request is successful. |

Monitor API Reference

| Code | String |   | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |   |
|---|---|---|---|---|---|
| RequestId | String |   | 0CCE0AF0-053C- 4B13-A583- DC9A85785D49 | The request ID for troubleshooting. |   |
| Message | String |   | success | The error message returned. |   |
| Resources |   |   |   | The information of metrics found. |   |
| Resource |   |   |   | The information of a metric found. |   |
| Description | String |   | CPUUtilization | The description of the metric. |   |
| Dimensions | String |   | instanceId | The dimensions of the metric. Separate multiple dimensions with commas (,). |   |
|   |   |   | [{&quot;name&qu ot;:&quot;alertUnit &quot;,&quot;value &quot;:&quot;Byte s&quot;}, {&quot;name&quo t;:&quot;minAlertP eriod&quot;,&quot; | The tags of the metric. The value is a JSON array string in the format of [{&quot;name&quot;:&quot;Tag |   |
|   |   |   |   |   | [{&quot;name&quot;:&quot;Tag |
|   |   |   | value&quot;:&quot | name&quot;,&quot;value&quot;:&quot;Ta |   |
|   |   |   | ;60&quot;}, {&quot;name&quo | g value&quot;}] |   |
| Labels | String |   | t;:&quot;metricCat egory&quot;,&quot ;value&quot;:&quo t;instanceId&quot; }, {&quot;name&quo t;:&quot;instanceT ype&quot;,&quot;v alue&quot;:&quot; disaster&quot;}, {&quot;name&quo t;:&quot;is alarm& _ quot;,&quot;value& quot;:&quot;true&q uot;}, {&quot;name&quo t;:&quot;productCa tegory&quot;,&quo t;value&quot;:&qu ot;kvstore old&quo _ t;}] |   |   |
| MetricName | String |   | CPUUtilization | The name of the metric that you want to query. |   |

Monitor API Reference

| Namespace | String | acs kvstore _ | The namespace of the service. The namespace is in the format of acs Service _ name. |
|---|---|---|---|
| Periods | String | 60,300 | The statistical period of the metric. Separate multiple periods with commas (,). Example: 15,60,900. |
| Statistics | String | Average,Minimum, Maximum | The statistical method of the metric. Separate multiple statistical methods with commas (,). Example: Average,Minimum,Maximum. |
| Unit | String | % | The unit of the metric. |
| TotalCount | String | 12 | The total number of records. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricMetaList &Namespace=acs_ecs_dashboard &<Common request parameters>
```

Sample success responses

**Note**

The response content varies with the services that are actually monitored. `XML` format

```json
<DescribeMetricMetaListResponse>
    <TotalCount>120</TotalCount>
    <RequestId>EA94B362-973C-4D6B-BE94-6774E18915C2</RequestId>
    <Success>true</Success>
    <Code>200</Code>
    <Resources>
        <Resource>
            <Description>ECS.CPUUtilization</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>CPUUtilization</MetricName>
            <Labels>[{"name":"alertUnit","value":"%"},
{"name":"alertDefault","value":"80"},{"name":"minAlertPeriod","value":"60"}, {"name":"metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Lab els>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
```

Monitor API Reference

```json
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The number of read operations performed on the system disk per
second.</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"instanceId"},{ "name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Maximum,Minimum</Statistics>
            <MetricName>DiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"instanceId"},{"name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description>The number of write operations performed on the system disk
per second.</Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>DiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"instanceId"},{ "name":"is_alarm","value":"true"}]</Labels>
            <Dimensions>userId,instanceId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupCPUUtilization</MetricName>
```

Monitor API Reference

```json
            <Labels>[{"name":"alertUnit","value":"%"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>%</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskReadIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>Count/Second</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteBPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Mbytes/s"},
{"name":"minAlertPeriod","value":"60"},{"name":"unitFactor","value":"1048576"},{"name": "metricCategory","value":"groupId"}]</Labels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
            <Unit>bytes/s</Unit>
        </Resource>
        <Resource>
            <Description></Description>
            <Statistics>Average,Minimum,Maximum</Statistics>
            <MetricName>GroupDiskWriteIOPS</MetricName>
            <Labels>[{"name":"alertUnit","value":"Count/Second"},
{"name":"minAlertPeriod","value":"60"},{"name":"metricCategory","value":"groupId"}]</La bels>
            <Dimensions>groupId</Dimensions>
            <Namespace>acs_ecs_dashboard</Namespace>
            <Periods>60,300</Periods>
```

Monitor API Reference

```xml
            <Unit>Count/Second</Unit>
        </Resource>
    </Resources>
</DescribeMetricMetaListResponse>
```

`JSON` format `{`

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
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"300\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"Mbytes\"}, {\"name\":\"productCategory\",\"value\":\"ads\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"300\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"300\"}, {\"name\":\"metricCategory\",\"value\":\"workerId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId,tableSchema,workerId",
    "Namespace":"acs_ads",
    "Periods":"300",
    "Unit":"%"
```

Monitor API Reference `},` `{`

```json
    "Description":"The number of unconsumed messages in the queue",
    "MetricName":"QueueMessageAccumulation",
    "Statistics":"Maximum",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
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
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"n ame\":\"unitFactor\",\"value\":\"1\"},{ \"name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
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
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"queue\"}]",
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
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"},
```

Monitor API Reference

```json
{\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
    "Dimensions":"userId,regionId,vhostName",
    "Namespace":"acs_amqp",
    "Periods":"60,300",
    "Unit":"count/min"
```

`},` `{`

```json
    "Description":"The number of messages consumed by the instance per minute",
    "MetricName":"VhostMessageOutput",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"minAlertPeriod\",\"value\":\"60\"},
{\"name\":\"alertDefault\",\"value\":\"\"},{\"name\":\"unitFactor\",\"value\":\"1\"},{\ "name\":\"alertUnit\",\"value\":\"count/min\"}, {\"name\":\"productCategory\",\"value\":\"amqp\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}, {\"name\":\"metricCategory\",\"value\":\"vhost\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"ms\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\" \"\" tiCt \"\"
```

`l`

```
\"\"i
```

`t`

```
Id\"}
```

Monitor API Reference

```json
{\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"KBytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"tru\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]", "Dimensions":"userIdregionapiUid"
```

Monitor API Reference

```json
    Dimensions:userId,region,apiUid,
    "Namespace":"acs_apigateway_dashboard",
    "Periods":"60,300",
    "Unit":"count"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_rx.Pkgs",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1048576\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"pps\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1048576\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]", "Dimensions":"userId,instanceId",
```

Monitor API Reference

```
esos:use
```

`d,`

```json
staced,
    "Namespace":"acs_bandwidth_package",
    "Periods":"60,300,600",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"net_tx.ratePercent",
    "Statistics":"Value",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbits/s\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"groupId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}]",
    "Dimensions":"userId,groupId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"bits/s"
```

`},` `{`

```json
    "Description":"",
    "MetricName":"GroupInternetOut",
    "Statistics":"Sum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"groupId\"},
```

Monitor API Reference

```json
{\"name\":\"unitFactor\",\"value\":\"1000\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Mbytes\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"unitFactor\",\"value\":\"1000000\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"unitFactor\",\"value\":\"1000\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"alertDefault\",\"value\":\"Count\"}, {\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
```

Monitor API Reference

```json
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"Count\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
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
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"userId\"}]",
    "Dimensions":"userId",
    "Namespace":"acs_cdn",
    "Periods":"60",
    "Unit":"%"
```

`},` `{`

```json
    "Description":"The percentage of 4XX HTTP status codes over total status codes in t
he specified time range",
    "MetricName":"code4xx",
    "Statistics":"Average,Minimum,Maximum",
    "Labels":"[{\"name\":\"alertUnit\",\"value\":\"%\"},
{\"name\":\"minAlertPeriod\",\"value\":\"60\"}, {\"name\":\"metricCategory\",\"value\":\"instanceId\"}, {\"name\":\"is_alarm\",\"value\":\"true\"}]",
    "Dimensions":"userId,instanceId",
    "Namespace":"acs_cdn",
    "Periods":"60,300",
    "Unit":"%"
```

`}` `]` `}` `}`

#### 5.3.2 Threshold-triggered alert rules

##### 5.3.2.1 DescribeMetricRuleList

Queries alert rules. Monitor API Reference

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMetricR uleList | The operation that you want to perform. Set the value to DescribeMetricRuleList. |
| Namespace | String | No | acs ecs dashbo _ _ ard | The namespace of the service. Note For more information, see Metrics for Apsara Stack services. |
| MetricName | String | No | cpu total _ | The name of the metric. Note For more information, see Metrics for Apsara Stack services. |
| EnableState | Boolean | No | true | Specifies whether to query enabled or disabled alert rules. Valid values: true: queries enabled alert rules. false: queries disabled alert rules. This parameter is empty by default, which indicates that both enabled and disabled rules are queried. |
| Page | String | No | 1 | The number of pages in which the results are returned. Default value: 1. |
| PageSize | String | No | 10 | The number of entries to return on each page. Default value: 10. |
| AlertState | String | No | ALARM | The status of the alert rule. Valid values: OK: No active alerts are triggered. ALARM: At least one alert is triggered. INSUFFICIENT DATA: No data is _ available. |

Monitor API Reference

| Dimensions | String | No | {&quot;instance Id&quot;:&quot;i - xy123****&quot ;} | The dimension map of the monitored resources. The value is a collection of key- value pairs. A typical key- value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), forward _ slashes (/), and backslashes (\). Note If you hope to see a key-value map expressed by JSON strings, set Dimensions to ordered strings. |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | key- |   |
|   |   |   |   |   | key- |   |   |
| RuleName | String | No | ECS CPU alert rule | The name of the alert rule. Note This parameter supports fuzzy match. |   |   |   |
| GroupId | String | No | 123456 | The ID of the application group. |   |   |   |
| RuleIds | String | No | a151cd6023eac ee2f0978e0386 3cc1697c89508 12**** | The ID of the alert rule. Note You can specify up to 20 IDs at a time. Separate multiple IDs with commas (,). |   |   |   |

|   | value |   |
|---|---|---|
|   | value |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0E657631-CD6C- 4C24-9637- 98D000B9272C | The ID of the request. |
| Code | Integer | 200 | The HTTP status code. Note A code of 200 indicates that the request succeeds. |

Monitor API Reference

| Total | String | 21 | The total number of returned entries. |
|---|---|---|---|
| Success | Boolean | true | Indicates whether the call was successful. |
| Alarms | Array | None | The list of alert rules. |
| Alarm | None | None | Details of the alert rule. |
| AlertState | String | OK | The status of the alert rule. Valid values: OK: No active alerts are triggered. ALARM: At least one alert is triggered. INSUFFICIENT DATA: No data is _ available. |
| ContactGroups | String | Default alert contacts | The contact information about alerts. |
| Dimensions | String | {&quot;userId&quo t;:&quot;4342&quo t;,&quot;instanceId &quot;:&quot;2123 12&quot;} | The dimension map of the monitored resources. The value is a collection of key-value pairs. A typical key-value pair is instanceId:XXXXXX . The key and value must each be 1 to 64 bytes in length. Excessive bytes are truncated from the string. The key and value can contain letters, digits, periods (.), hyphens (-), underscores ( ), _ forward slashes (/), and backslashes (\). Note If you hope to see a key- value map expressed by JSON strings, set Dimensions to ordered strings. |
| EffectiveInterv al | String | 00:00-23:59 | The time period during which the alert rule is effective. |
| EnableState | Boolean | true | Indicates whether enabled or disabled alert rules are queried. Valid values: true: Enabled alert rules are queried. false: Disabled alert rules are queried. This parameter is empty by default, which indicates that both enabled and disabled rules are queried. |

|   | key-value |
|---|---|
| key-value |   |

Monitor API Reference

| Escalations | None | None | The conditions that trigger different levels of alerts. |
|---|---|---|---|
| Critical | None | None | The conditions that trigger critical-level alerts. |
| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator of the threshold for critical-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
| Statistics | String | Average | The statistical method for critical-level alerts. |
| Threshold | String | 90 | The threshold for critical-level alerts. |
| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for critical-level alerts before a critical-level alert is triggered. |
| Info | None | None | The conditions for triggering info-level alerts. |

Monitor API Reference

| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator of the threshold for info-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
|---|---|---|---|
| Statistics | String | Average | The statistical method for info-level alerts. |
| Threshold | String | 90 | The threshold for info-level alerts. |
| Times | String | 1 | The consecutive number of times for which the metric value exceeds the threshold for info-level alerts before an alert is triggered. |
| Warn | None | None | The conditions for triggering warn-level alerts. |

Monitor API Reference

| ComparisonOp erator | String | GreaterThanOrEqu alToThreshold | The comparison operator of the threshold for warn-level alerts. Valid values: GreaterThanOrEqualToThreshold: greater than or equal to GreaterThanThreshold: greater than LessThanOrEqualToThreshold: less than or equal to LessThanThreshold: less than NotEqualToThreshold: not equal to GreaterThanYesterday: greater than the metric value at the same time yesterday LessThanYesterday: less than the metric value at the same time yesterday GreaterThanLastWeek: greater than the metric value at the same time last week LessThanLastWeek: less than the metric value at the same time last week GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle LessThanLastPeriod: less than the metric value in the last monitoring cycle |
|---|---|---|---|
| Statistics | String | Average | The statistical method for warn-level alerts. |
| Threshold | String | 90 | The threshold for warn-level alerts. |
| Times | String | 3 | The consecutive number of times for which the metric value exceeds the threshold for warn-level alerts before a warn-level alert is triggered. |
| GroupId | String | 123456 | The ID of the application group. |
| GroupName | String | My application group | The name of the application group. Note If the alert rule is associated with an application group, the name of the application group is returned in this parameter. |
| MailSubject | String | An alert occurs | The subject of the alert notification email. |
| MetricName | String | cpu total _ | The name of the metric. |
| Namespace | String | acs ecs dashboard _ _ | The namespace of the service. |

Monitor API Reference

| NoEffectiveInt erval | String | 00:00-23:59 | The time period during which the alert rule is ineffective. |
|---|---|---|---|
| Period | String | 60 | The statistical period. |
| Resources | String | [{\&quot;instanceI d\&quot;:\&quot;i- a2d5q7pm3f9yr29 e****\&quot;}, {\&quot;instanceId \&quot;:\&quot;i- a2d5q7pm3f9yr29 e****\&quot;} | The resources that are associated with the alert rule. |
| RuleId | String | a151cd6023eacee 2f0978e03863cc16 97c895012**** | The ID of the alert rule. |
| RuleName | String | My alert rule | The name of the alert rule. |
| SilenceTime | String | 86400 | The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: 86400. Minimum value: 3600. Only one alert is sent during each mute duration, even if the metric value exceeds the alert rule threshold several times. |
| SourceType | String | METRIC | The type of the alert rule. Valid values: METRIC: the alert rule for time series metrics. EVENT: the alert rule for event-type metrics. This type was used in earlier versions and has been discarded. |
| Webhook | String | http://www.aliyun.c om | The callback URL. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleList &amp;<公共请求参数>
```

Sample success responses `XML` format

```xml
<Alarms>
    <Alarm>
```

`/` Monitor API Reference

```xml
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
        <ComparisonOperator>>=</ComparisonOperator>
        <Resources>[{&quot;instanceId&quot;:&quot;i-a2d5q7pm3f12****&quot;}]
</Resources>
    </Alarm>
    <Alarm>
        <Period>60</Period>
        <Statistics>Average</Statistics>
        <GroupName>demo</GroupName>
        <Webhook/>
        <Subject>${serviceType}-${metricName}-
${levelDescription}Notification{dimensions})</Subject>
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
```

Monitor API Reference

```xml
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
        <ComparisonOperator>>=</ComparisonOperator>
        <Resources>[{&quot;instanceId&quot;:&quot;host-fTcUci7****&quot;}</Resources>
    </Alarm>
</Alarms> <RequestId>0F05309F-8863-4B2A-8F52-C6AA00E701B4</RequestId> <Success>true</Success><Code>200</Code><Total>102</Total>
```

`JSON` format Monitor API Reference

```
{ &quot;RequestId&quot;:&quot;0F05309F-8863-4B2A-8F52-C6AA00E701B4&quot;, &quot;Alarms&quot;:{ &quot;Alarm&quot;:[ { &quot;Period&quot;:60, &quot;Statistics&quot;:&quot;Average&quot;, &quot;GroupName&quot;:&quot;Group name&quot ;, &quot;Webhook&quot;:&quot;&quot;, &quot;Subject&quot;:&quot;aaabbb&quot;, &quot;Effe ctiveInterval&quot;:&quot;00:00-23:59&quot;, &quot;RuleName&quot;:&quot;My alert rule&q uot;, &quot;NoEffectiveInterval&quot;:&quot;&quot;, &quot;GroupId&quot;:&quot;3596360&quot;, &quot;EvaluationCount&quot;:3, &quot;MetricName&quot;:&quot;cpu_total&quot;, &quot;State&quot;:&quot;OK&quot;, &quot;T hreshold&quot;:&quot;92&quot;, &quot;Enable&quot;:true, &quot;SilenceTime&quot;:86400, &quot;Dimensions&quot;:&quot;[{}]&quot;, &quot;RuleId&quot;:&quot;a151cd6023eacee2f0978e03863cc1697c89508e2b61****&quot;, &quot; Namespace&quot;:&quot;acs_ecs_dashboard&quot;, &quot;ContactGroups&quot;:&quot;Test&quot;, &quot;ComparisonOperator&quot;:&quot;>=&quot;, &quot;Escalations&quot;:{ &quot;Critical&quot;:{ &quot;Statistics&quot;:&quot;Average&quot;, &quot;Threshold&quot;:&quot;92&quot;, &quot;Times&quot;:3, &quot;ComparisonOperator&quot;:&quot;GreaterThanOrEqualToThreshold&quot; }, &quot;Info&quot;:{}, &quot;Warn&quot;:{} }, &quot;Resources&quot;:&quot; [{\&quot;instanceId\&quot;:\&quot;i-a2d5q7pm3f12****\&quot;}]&quot; }, { &quot;Period&quot;:60, &quot;Statistics&quot;:&quot;Average&quot;, &quot;GroupName&quot;:&quot;demo&quot;, &quot;Webhook&quot;:&quot;&quot;, &quot;Subject&quot;:&quot;${serviceType}-${metricName}- ${levelDescription}Notification(${dimensions})&quot;, &quot;EffectiveInterval&quot;:&quot;00:00-23:59&quot;, &quot;RuleName&quot;:&quot;xxxxxxxxxxxxxxx&quot;, &quot;NoEffectiveInterval&quot;:&quot;&quot;, &quot;GroupId&quot;:&quot;12345&quot;, &q uot;EvaluationCount&quot;:3, &quot;MetricName&quot;:&quot;cpu_total&quot;, &quot;State&quot;:&quot;OK&quot;, &quot;Threshold&quot;:&quot;90&quot;, &quot;Enable&quot;:true, &quot;SilenceTime&quot;:86400, &quot;Dimensions&quot;:&quot;[{ }]&quot;, &quot;RuleId&quot;:&quot;alarmRule_uuid_adbe286748952b82c6a4ebe3a07521697bb706****&quot;, &quot;Namespace&quot;:&quot;acs_ecs_dashboard&quot;, &quot;ContactGroups&quot;:&quot;rongfei&quot;, &quot;ComparisonOperator&quot;:&quot;>=&quot;, &quot;Escalations&quot;:{ &quot;Critical&quot;:{ &quot;Statistics&quot;:&quot;Average&quot;, &quot;Threshold&quot;:&quot;6666&quot;, &quot;Times&quot;:3, &quot;ComparisonOperator&quot;:&quot;GreaterThanOrEqualToThreshold&quot; }, &quot;Info&quot;:{}, &quot;Warn&quot;:{} }, &quot;Resources&quot;:&quot; [{\&quot;instanceId\&quot;:\&quot;host-fTcUci7****\&quot;}&quot; } ] }, &quot;Success&quot;:true, &quot;Code&quot;:&quot;200&quot;, &quot;Total&quot;:102 }
```

##### 5.3.2.2 PutResourceMetricRule

Creates an alert rule for a performance metric of a resource. For more information about the sample values of request parameters such as `Namespace` , `MetricName` and `Dimensions` for cloud services, see Metrics for Apsara Stack services.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

Monitor API Reference

| Action | String | Yes | PutResourceMet ricRule | The operation that you want to perform. Set the value to PutResourceMetricRule. |
|---|---|---|---|---|
| ContactGroups | String | Yes | Default alert contact group | The alert contact groups. Note Separate multiple groups with commas (,). |
| MetricName | String | Yes | cpu total _ | The name of the metric. Note For more information, see Metrics for Apsara Stack services. |
| Namespace | String | Yes | acs ecs dashbo _ _ ard | The namespace of the service. Note For more information, see Metrics for Apsara Stack services. |
| Resources | String | Yes | [{"instanceId":"x xxxxxx"}] | The resource for which the alert rule is applied. Note For more information, see the Dimensions of the metric in Metrics for Apsara Stack services. |
| RuleId | String | Yes | a151cd6023eac ee2f0978e0386 3cc1697c89508 **** | The ID of the alert rule. Note The ID is generated by the caller. You can specify an existing ID to modify the corresponding alert rule or specify a new ID to create an alert rule. |
| RuleName | String | Yes | My alert rule | The name of the alert rule. |
| Webhook | String | No | http://ww.aliyun. com | The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. |
| EffectiveInterv al | String | No | 00:00-23:59 | The time period during which the alert rule is effective. |

Monitor API Reference

| NoEffectiveInt erval | String | No | 00:00-06:00 | The time period during which the alert rule is ineffective. |
|---|---|---|---|---|
| SilenceTime | Integer | No | 86400 | The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: 86400. Note Only one alert is reported during each mute period even if the metric value consecutively exceeds the alert rule threshold several times. |
| Interval | String | No | 60 | The interval at which the system checks whether the alert rule is triggered. The default value is the lowest frequency at which the metric is checked. Unit: seconds. Note For more information about the frequency at which the metric is checked, see DescribeMetricMetaList. |
| EmailSubject | String | No | An alert occurs | The subject of the alert notification email. |
| Period | String | No | 60 | The aggregation cycle of monitoring data. The value is an integer multiple of 60. Unit: seconds. The default value is the frequency at which monitoring data is collected. |
| Escalations.Cri tical.Statistics | String | No | Average | The statistical methods for Critical- level alerts. |

Monitor API Reference

| Escalations.Cri tical.Comparis onOperator | String | No |   |   | The operator that is used to compare the metric value with the threshold. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in last monitoring cycle LessThanLastPeriod : less than the metric value in last monitoring cycle |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Cri tical.Threshold | String | No |   | 90 | The threshold for Critical-level alerts. |   |   |
| Escalations.Cri tical.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the trigger condition before a Critical- level alert is triggered. |   |   |
| Escalations.Wa rn.Statistics | String | No |   | Average | The statistical methods for Warn- level alerts. |   |   |

Monitor API Reference

| Escalations.Wa rn.Comparison Operator | String | No |   |   | The operator that is used to compare the metric value with the threshold. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in last monitoring cycle LessThanLastPeriod : less than the metric value in last monitoring cycle |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Wa rn.Threshold | String | No |   | 90 | The threshold for Warn-level alerts. |   |   |
| Escalations.Wa rn.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the trigger condition before a Warn-level alert is triggered. |   |   |
| Escalations.Inf o.Statistics | String | No |   | Average | The statistical methods for Info-level alerts. |   |   |

Monitor API Reference

| Escalations.Inf o.Comparison Operator | String | No |   |   | The operator that is used to compare the metric value with the threshold. Valid values: GreaterThanOrEqualToThreshold : greater than or equal to the threshold GreaterThanThreshold : greater than the threshold LessThanOrEqualToThreshold : less than or equal to the threshold LessThanThreshold : less than the threshold NotEqualToThreshold : not equal to the threshold GreaterThanYesterday : greater than the metric value at the same time yesterday LessThanYesterday : less than the metric value at the same time yesterday GreaterThanLastWeek : greater than the metric value at the same time last week LessThanLastWeek : less than the metric value at the same time last week GreaterThanLastPeriod : greater than the metric value in last monitoring cycle LessThanLastPeriod : less than the metric value in last monitoring cycle |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | GreaterThanOrEqualToThreshold |   |
|   |   |   |   | GreaterThanOrE qualToThreshold |   |   |   |
| Escalations.Inf o.Threshold | String | No |   | 90 | The threshold for Info-level alerts. |   |   |
| Escalations.Inf o.Times | Integer | No |   | 3 | The consecutive number of times for which the metric value meets the trigger condition before an Info-level alert is triggered. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request succeeded. |

Monitor API Reference

| Message | String | success | The error message. |
|---|---|---|---|
| RequestId | String | 65D50468-ECEF- 48F1-A6E1- D952E89D9436 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=PutResourceMetricRule &amp;ContactGroups=Default alert con tact group &amp;MetricName=cpu_total &amp;Namespace=acs_ecs_dashboard &amp;Resources=[{ &quot;instanceId&quot;:&quot;xxxxxxx&quot;}] &amp;RuleId=a151cd6023eacee2f0978e03863cc1697c89508**** &amp;RuleName=My alert rule &am
```

p;<公共请求参数`>` Sample success responses `XML` format

```xml
<Code>200</Code><Message>success</Message> <RequestId>65D50468-ECEF-48F1-A6E1-D952E89D9436</RequestId> <Success>true</Success>
```

`JSON` format

```
{ &quot;Message&quot;:&quot;success&quot;, &quot;RequestId&quot;:&quot;65D50468-ECEF-48 F1-A6E1-D952E89D9436&quot;, &quot;Success&quot;:true, &quot;Code&quot;:&quot;200&quot;
```

`}`

##### 5.3.2.3 DescribeMetricRuleCount

Queries the number of alert rules in each state.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | No | DescribeMetricR uleCount | The operation that you want to perform. Set the value to DescribeMetricRuleCount. |
| MetricName | String | No | cpu total _ | The name of the metric . |

Monitor API Reference

| Namespace | String | No | acs ecs dashbo _ _ ard | The namespace of the service. You can call the DescribeMetricMetaList operation to query namespaces. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call is successful. |
| Message | String | The Request is not authorization. | The returned message. |
| MetricRuleCou nt | N/A | N/A | The number of alert rules in each state. |
| Alarm | Integer | 5 | The number of alert rules based on which alerts were triggered and not cleared. |
| Disable | Integer | 0 | The number of disabled alert rules. |
| Nodata | Integer | 0 | The number of alert rules for which status data is unavailable. |
| Ok | Integer | 40 | The number of alert rules that do not have active alerts triggered. |
| Total | Integer | 45 | The total number of alert rules. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the request is successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMetricRuleCount &<Common request parameters>
```

Sample success responses `XML` format Monitor API Reference

```xml
<DescribeMetricRuleCountResponse>
      <Success>true</Success>
      <Code>200</Code>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <MetricRuleCount>
            <Ok>40</Ok>
            <Disable>0</Disable>
            <Total>45</Total>
            <Nodata>0</Nodata>
            <Alarm>5</Alarm>
      </MetricRuleCount>
</DescribeMetricRuleCountResponse>
```

`JSON` format `{`

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

`}` `}`

##### 5.3.2.4 DeleteMetricRules

You can call this operation to delete one or more alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Id.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c7e12*** * | The ID of the alert rule. |
| Action | String | No | DeleteMetricRul es | The operation that you want to perform. Set the value to DeleteMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

Monitor API Reference

| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
|---|---|---|---|
| Message | String | success | The error message. |
| RequestId | String | E5599964-8D0D- 40DC-8E90- 27A619384B81 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DeleteMetricRules &Id.1=ab05733c97b7ce239fb1b53393dc1697c7e12**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</DeleteMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"E5599964-8D0D-40DC-8E90-27A619384B81",
 "Success":true,
 "Code":"200"
```

`}`

##### 5.3.2.5 EnableMetricRules

Enables one or more alert rules.

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request parameters**

Monitor API Reference

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| RuleId.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c123**** | The ID of the alert rule. |
| Action | String | No | EnableMetricRul es | The operation that you want to perform. Set the value to EnableMetricRules. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The returned message. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c123**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnableMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</EnableMetricRulesResponse>
```

`JSON` format Monitor API Reference `{`

```json
 "Message":"success",
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":200
```

`}`

**Error codes**

For a list of error codes, visit the API Error Center.

##### 5.3.2.6 DisableMetricRules

You can call this operation to disable one or more alert rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableMetricRul es | The operation that you want to perform. Set the value to DisableMetricRules. |
| RuleId.N | RepeatL ist | Yes | ab05733c97b7c e239fb1b53393 dc1697c7e012** ** | The ID of the alert rule. Valid values of N: 1 to 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The HTTP status code. The status code 200 indicates that the call was successful. |
| Message | String | success | The error message. |
| RequestId | String | FF38D33A-67C1- 40EB-AB65- FAEE51EDB644 | The ID of the request, which can be used for troubleshooting. |
| Success | Boolean | true | Indicates whether the call was successful. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DisableMetricRules &RuleId.1=ab05733c97b7ce239fb1b53393dc1697c7e012**** &<Common request parameters>
```

Monitor API Reference Sample success responses `XML` format

```xml
<DisableMetricRulesResponse>
      <Code>200</Code>
      <Message>success</Message>
      <RequestId>FF38D33A-67C1-40EB-AB65-FAEE51EDB644</RequestId>
      <Success>true</Success>
</DisableMetricRulesResponse>
```

`JSON` format `{`

```json
 "Message":"success",
 "RequestId":"FF38D33A-67C1-40EB-AB65-FAEE51EDB644",
 "Success":true,
 "Code":"200"
```

`}`

##### 5.3.2.7 DescribeAlertingMetricRuleResources

You can call this operation to query the resources that have active alerts triggered based on an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlerting MetricRuleResou rces | The operation that you want to perform. Set the value to DescribeAlertingMetricRuleResources . |
| GroupId | String | No | 123456 | The ID of the application group. |
| Page | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Default value: 10. |

Monitor API Reference

| RuleId | String | No | alerRuleId**** | The ID of the alert rule. Note You must specify at least one of the GroupId and RuleId parameters. If you specify both parameters, only entries that meet both conditions are returned. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B868619-77B4- 4623-AD64- 6181EA7CF8FA | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Code | Integer | 200 | The HTTP status code. Note The status code 200 indicates that the call was successful. |
| Total | Integer | 1 | The total number of entries returned. |
| Resources | Array | None | The list of resources to which the alert rule applies. |
| Resource | None | None | The information of a resource to which the alert rule applies. |
| Enable | String | true | Indicates whether the alert rule is enabled for the resource. |
| GroupId | String | 123456 | The ID of the application group. Note If the alert rule is associated with an application group, the ID of the application group is returned in this parameter. |

Monitor API Reference

| LastAlertTime | String | 1554718182000 | The last time when an alert was triggered for the resource based on the alert rule. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
|---|---|---|---|
| LastModifyTim e | String | 1554723762000 | The time when the resource was last modified. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| MetricValues | String | {"timestamp":155 4723720000,"Valu e":631} | The metric value that triggered the alert based on the alert rule. The value is a JSON string. |
| Resource | String | userId=177541323 192****,taskId=3** **,instanceId=i- bp1a0v6yzqrms01 k**** | The resource for which an alert was triggered based on the alert rule. |
| RetryTimes | String | 3 | The consecutive number of times for which the metric value was measured before an alert was triggered. |
| RuleId | String | alerRuleId**** | The ID of the alert rule. |
| RuleName | String | cpuAlert | The name of the alert rule. |
| StartTime | String | 1545901080000 | The time when the resource was associated with the alert rule. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC. |
| Threshold | String | 400 | The alert threshold. |
| Message | String | success | The error message. |

**Examples**

Sample requests Monitor API Reference

```
http(s)://[Endpoint]/? Action=DescribeAlertingMetricRuleResources &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Total>1</Total> <Resources>
    <Resource>
        <Enable>true</Enable>
        <Resource>userId=12****,instanceId=i-bp1a012****</Resource>
        <RuleId>alerRuleId****</RuleId>
        <RetryTimes>3</RetryTimes>
        <LastAlertTime>1554718182000</LastAlertTime>
        <MetricValues>{"timestamp":1554723720000,"Value":631}</MetricValues>
        <LastModifyTime>1554723762000</LastModifyTime>
        <StartTime>1545901080000</StartTime>
        <RuleName>cpuAlert</RuleName>
        <Threshold>400</Threshold>
        <GroupId>123456</GroupId>
    </Resource>
</Resources> <Success>true</Success>
```

`JSON` format `{`

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

`}` `]` `}` `}`

##### 5.3.2.8 DeleteMetricRuleResources

Monitor API Reference Disassociates resources from an alert rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMetricRul eResources | The operation that you want to perform. Set the value to DeleteMetricRuleResources. |
| Resources | String | Yes | [{"instanceId":"* ****ixxxId1"}] | The associated resources. The value is a JSON array. |
| RuleId | String | No | rr- bp18017n6iolv* *** | The ID of the alert rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D8A35882-90C6- 4F03-BBEB- 153C180398EA | The ID of the request. |
| Success | Boolean | true | Indicates whether the call was successful. |
| Code | String | 200 | The HTTP status code. Note The HTTP status code 200 indicates that the request succeeded. |
| Message | String | success | The error message. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMetricRuleResources &amp;Resources= [{&quot;instanceId&quot;:&quot;*****ixxxId1&quot;}] &amp;RuleId=rr-bp18017n6iolv**** &a
```

mp;<公共请求参数`>` Sample success responses `XML` format

```xml
<RequestId>0671A721-0D7A-4F11-BB77-2416325D65AB</RequestId> <Success>true</Success> <Message>success</Message><Code>200</Code>
```

Monitor API Reference `JSON` format `{`

```json
    "Message":"success",
    "RequestId":"0671A721-0D7A-4F11-BB77-2416325D65AB",
    "Success":true,
    "Code":"200"
```

`}`
