---
title: "Alibaba Cloud Apsara Stack V3.18.3 Server Load Balancer Developer Guide 20241105"
product_version: "V3.18.3"
doc_version: "20241105"
pdf_pages: 184
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Server Load Balancer Developer Guide 20241105.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Server%20Load%20Balancer%20Developer%20Guide%2020241105.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.3 Server Load Balancer Developer Guide 20241105

## Table of Contents

- 1 Getting Started
  - 1.1 Apsara Stack documentation
  - 1.2 Procedure for API calls
- 2 Preparations
  - 2.1 Log on to the API Tool console
  - 2.2 Obtain the information and the endpoint of an API operation
  - 2.3 Obtain an AccessKey pair
  - 2.4 Obtain STS credentials
  - 2.5 Obtain the values of common header parameters
  - 2.6 Obtain the SLB SDK
- 3 Use POP to make API calls
  - 3.1 Preparations
  - 3.2 SDK for Java
  - 3.3 SDK for Go
  - 3.4 SDK for Python
- 4 Call examples for SDK for Java
  - 4.1 Quick start
  - 4.2 Work with SLB SDK for Java
    - 4.2.1 Install SLB SDK for Java
    - 4.2.2 Configure authentication credentials
    - 4.2.3 Call SLB SDK for Java
    - 4.2.4 Handle errors
- 5 Use SLB SDK for Python to make API calls
  - 5.1 Quick start
  - 5.2 Work with SLB SDK for Python
    - 5.2.1 Install SDK for Python
    - 5.2.2 Configure authentication credentials
    - 5.2.3 Set HTTPS requests
    - 5.2.4 Call SLB SDK for Python
    - 5.2.5 Troubleshooting
- 6 Use SLB SDK for Go to make API calls
  - 6.1 Quick start
  - 6.2 Work with SLB SDK for Go
    - 6.2.1 Install the core package of SDK for Go
    - 6.2.2 Configure authentication credentials
    - 6.2.3 Call SLB SDK for Go
    - 6.2.4 Troubleshooting
- 7 API Reference
  - 7.1 Methods for API calls
  - 7.2 RAM authentication
  - 7.3 Common parameters
  - 7.4 SLB instance
    - 7.4.1 CreateLoadBalancer
    - 7.4.2 DeleteLoadBalancer
    - 7.4.3 ModifyLoadBalancerInstanceSpec
    - 7.4.4 ModifyLoadBalancerInternetSpec
    - 7.4.5 SetLoadBalancerName
    - 7.4.6 SetLoadBalancerStatus
    - 7.4.7 DescribeLoadBalancerAttribute
    - 7.4.8 DescribeLoadBalancers
    - 7.4.9 DescribeRegions
    - 7.4.10 DescribeZones
  - 7.5 Listeners
    - 7.5.1 TCP listeners
      - 7.5.1.1 CreateLoadBalancerTCPListener
      - 7.5.1.2 SetLoadBalancerTCPListenerAttribute
      - 7.5.1.3 DescribeLoadBalancerTCPListenerAttribute
    - 7.5.2 UDP listeners
      - 7.5.2.1 CreateLoadBalancerUDPListener
      - 7.5.2.2 SetLoadBalancerUDPListenerAttribute
      - 7.5.2.3 DescribeLoadBalancerUDPListenerAttribute
    - 7.5.3 HTTP listeners
      - 7.5.3.1 CreateLoadBalancerHTTPListener
      - 7.5.3.2 SetLoadBalancerHTTPListenerAttribute
      - 7.5.3.3 DescribeLoadBalancerHTTPListenerAttribute
    - 7.5.4 HTTPS listeners
      - 7.5.4.1 CreateLoadBalancerHTTPSListener
      - 7.5.4.2 SetLoadBalancerHTTPSListenerAttribute
      - 7.5.4.3 DescribeLoadBalancerHTTPSListenerAttribute
      - 7.5.4.4 DescribeHealthStatus
    - 7.5.5 Access control
      - 7.5.5.1 SetListenerAccessControlStatus
      - 7.5.5.2 DescribeListenerAccessControlAttribute
      - 7.5.5.3 AddListenerWhiteListItem
      - 7.5.5.4 RemoveListenerWhiteListItem
      - 7.5.5.5 CreateAccessControlList
      - 7.5.5.6 DeleteAccessControlList
      - 7.5.5.7 DescribeAccessControlLists
      - 7.5.5.8 DescribeAccessControlListAttribute
      - 7.5.5.9 SetAccessControlListAttribute
      - 7.5.5.10 AddAccessControlListEntry
      - 7.5.5.11 RemoveAccessControlListEntry
    - 7.5.6 DeleteLoadBalancerListener
    - 7.5.7 StopLoadBalancerListener
    - 7.5.8 StartLoadBalancerListener
  - 7.6 Forwarding rules
  - 7.7 Access logs
  - 7.8 Server certificates
    - 7.8.1 UploadServerCertificate
    - 7.8.2 DeleteServerCertificate
    - 7.8.3 DescribeServerCertificates
    - 7.8.4 SetServerCertificateName
    - 7.8.5 UploadCACertificate
    - 7.8.6 DeleteCACertificate
    - 7.8.7 DescribeCACertificates
    - 7.8.8 SetCACertificateName
  - 7.9 Backend servers
    - 7.9.1 AddBackendServers
    - 7.9.2 RemoveBackendServers
    - 7.9.3 SetBackendServers
  - 7.10 vServer groups
    - 7.10.1 CreateVServerGroup
    - 7.10.2 SetVServerGroupAttribute
    - 7.10.3 AddVServerGroupBackendServers
    - 7.10.4 RemoveVServerGroupBackendServers
    - 7.10.5 ModifyVServerGroupBackendServers
    - 7.10.6 DeleteVServerGroup
    - 7.10.7 DescribeVServerGroups
    - 7.10.8 DescribeVServerGroupAttribute
  - 7.11 Primary/secondary server groups
    - 7.11.1 CreateMasterSlaveServerGroup
    - 7.11.2 DeleteMasterSlaveServerGroup
    - 7.11.3 DescribeMasterSlaveServerGroups
    - 7.11.4 DescribeMasterSlaveServerGroupAttribute
  - 7.12 Tags
    - 7.12.1 AddTags
    - 7.12.2 DescribeTags
    - 7.12.3 RemoveTags
  - 7.13 Error codes
- 8 Appendix
  - 8.1 STS overview
    - 8.1.1 What is STS?
    - 8.1.2 AssumeRole
- 9 DescribeLoadBalancerListeners
- 10 SetLoadBalancerModificationProtection
- 11 SetLoadBalancerDeleteProtection

## 1 Getting Started

### 1.1 Apsara Stack documentation

This topic describes how to view the references of an Apsara Stack service when you call Apsara Stack API.

**Workflow**

The following figure shows how to find your desired information in the Apsara Stack documentation.

**Prerequisites**

The Apsara Stack version is obtained from O&M personnel or an operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center to view the documentation of an Apsara Stack service.
1. Go to the Apsara Stack documentation center.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service.
5. In the upper-right corner of the documentation section, click **View Details** or **Download PDF**.

### 1.2 Procedure for API calls

Apsara Stack allows you to call API operations by using the point of presence (POP) gateway. To ensure that Apsara Stack provides the same experience as Alibaba Cloud Public Cloud, API operations in Apsara Stack Enterprise V3.16.0 and later are called by using the POP gateway by default. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

**Procedure**

1. Obtain the AccessKey credential.
Obtain the AccessKey credential that is required for calling an API operation. For more information, see Obtain an AccessKey pair or Obtain an AccessKey pair assigned by STS.

> **Note:** We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or an access credential assigned by Security Token Service (STS) to call the API operations of the Apsara Uni-manager Management Console and cloud services.

2. Obtain the region ID.
For more information about how to obtain a region ID, see Obtain the values of common header parameters.
3. Obtain the organization ID and the resource set ID.
Obtain the organization ID by calling the GetOrganizationList operation. For more information, see GetOrganizationList in Apsara Un i-manager Management Console Developer Guide. Obtain the resource set ID by calling the ListResourceGroup operation. For more information, see ListResourceGroup in Apsara Unimanager Management Console Developer Guide.

> **Note:** When you call an API operation, set the `<x-acs-organizationid>` header to the organization ID that you queried, and set the
> `<x-acs-resourcegroupid>` header to the resource set ID that you queried. This way, you can query resources in the specified organization and resource set.
> If you do not specify the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is used.
> If you do not specify the `<x-acs-resourcegroupid>` parameter, this parameter is left empty. If you specify a resource set, you must also specify an organization ID.

4. Obtain the API references.
To learn the features of API operations and how to call the API operations, obtain the developer guide of the Apsara Stack service that you want to use. For more information, see Apsara Stack documentation.
5. Obtain the endpoint of the service.
6. Obtain the service SDK and use the SDK to call the API operations of the service.

## 2 Preparations

### 2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment engineer. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of a browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log On**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding operations in the following scenarios:
This is your first time logging on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Re-enter the username and password as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management** **Console User Guide**.

5.

### 2.2 Obtain the information and the endpoint of an API operation

**an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter on the Parameter tab.

### 2.3 Obtain an AccessKey pair

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You only need to provide one type of AccessKey credential for authentication when you call API operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of request senders. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an AccessKey pair for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3-tuple. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts or organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni- manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to obtain.
5. Click **Management AccessKey** on the right side of the page.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.4 Obtain STS credentials

This topic describes how to use Security Token Service (STS) credentials to make API calls.

**Background information**

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. You can use STS credentials to make API calls. To call Apsara Stack APIs, you must obtain an AccessKey ID, an AccessKey secret, and a security token assigned by STS. For more information, see STS.

**Procedure**

1. Obtain the `Resource Access Management (RAM) role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User Information**. iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, you can obtain information about the `RAM role` that is assigned to the current user.
2. Obtain the STS credentials.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) before you submit the code.
> The following section describes the parameters:
> <yourRegionID>: Replace it with the region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourRoleSessionName>: Replace it with the name of the current session.
> <yourRoleArn>: Replace it with your RAM role.
> "sts.aliyuns.com": Replace it with the endpoint of STS.

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
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
    // Obtain the AccessKey ID, AccessKey secret, and security token assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the actual endpoint of the STS. In most cases, endpoint is in the following format: s
ts-vpc.${global:region}.${global:internet-domain}.
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
    return null;
```

3. The following sample code shows how to use STS credentials to call the DescribeLoadBalancers operation of the Server Load
Balancer (SLB) API:

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) before you submit the code.
> The following section describes the parameters:
> <yourRegionID>: Replace it with the region ID.
> <yourStsAccesskeyID>: Replace it with your STS AccessKey ID.
> <yourAccessKeySecret>: Replace it with your STS AccessKey secret.
> <yourStsToken>. Replace it with your STS security token.
> <yourRegionID>: Replace it with the actual resource set ID.
> <yourRegionID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey ID and AccessKey secret assigned by
STS.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<yourStsAccessSecret>");
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

### 2.5 Obtain the values of common header parameters

**parameters**

You must set header parameters when you call API operations. This topic describes the header parameters and how to obtain the values of the parameters. This topic also describes the values of some response parameters after you call API operations.

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance on which you want to perform operations. For more information about how to obtain instance IDs, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization that you want to view.
5. View the region ID in the **Regions** section on the right.

**Obtain an organization ID**

You must call an operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an elastic IP address (EIP), perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **ProductsNetworkingServer Load Balancer**.
3. In the left-side navigation pane, choose **Instances & Images > Instances**.
4. View the **instance ID** in the instance list.
The following response parameters are returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 2.6 Obtain the SLB SDK

When you call API operations of a cloud service in Apsara Stack by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK. This topic describes how to obtain Alibaba Cloud SDK.

**Background information**

To use Server Load Balancer (SLB) features, you must install both the SLB SDK and the Alibaba Cloud core library. For example, to use SLB SDK for Java, you must download `aliyun-java-sdk-sl` and `aliyun-java-sdk-core` . The SLB SDK encapsulates the API released on May 15, 2014. The SDK identifies callers based on their AccessKey pairs and provides features such as automatic signing to allow you to create and manage resources by calling API operations. Alibaba Cloud SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. We recommend that you use the SDK core library that is provided on the Alibaba Cloud website. The SDK core library is ideal for all cloud services and is compatible with Apsara Stack.

**Instructions**

Alibaba Cloud SDK supports Java, Python, and Go. You can select an SDK from Alibaba Cloud SDK based on your business requirements.

> **Note:** We recommend that you use an SDK for Java, Python, or Go. If you use SDKs in other programming languages, the SDKs may be incompatible with your system.

e API calls

## 3 Use POP to make API calls

### 3.1 Preparations

Like in the public cloud, you can use the POP gateway to call API operations in Apsara Stack. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

In Apsara Stack, you can use both ASAPI and POP gateways to call API operations. To use the same method and produce the same user experience as in the public cloud, we recommend that you use the POP gateway to call API operations in Apsara Stack.

**Obtain service endpoints**

To use the POP gateway to call API operations, you must use the service endpoints. You can obtain the service endpoints from Alibaba Cloud onsite O&M engineers. You can also obtain the service endpoints by yourself. The following example describes how to obtain the ECS endpoints.
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **O&M**. iii. In the left-side navigation pane, choose **Product Management** > **Products**. iv. In the Apsara Stack O&M section, click **Apsara Infrastructure Management Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for `Registration Vars of Services` and click the report name.
4. On the **Registration Vars of Services** page, click the
icon next to **Service** and search for `ECS` .
5. Find the `ecs-yaochi` service, right-click the **Service Registration** column, and then select **Show More** from the shortcut menu.
On the **Details** page, view the **internal.openapi.endpoint** value, which is the `endpoint` .

**Obtain common parameters**

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain common header parameters.

### 3.2 SDK for Java

Before you use Apsara Stack API (ASAPI) SDK for POP for Java to access ASAPI, you must know the remote procedure call (RPC) and resource-oriented architecture (ROA) styles that are supported for API calls. ASAPI is compatible with both styles. Their difference lies in the ASAPI endpoints that are used for API calls.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS.

**Background information**

ASAPI supports only the HTTPS request protocol.

**Difference between two styles**

When you use the RPC or ROA style to make API calls, take note that the two styles use different ASAPI endpoints. e API calls

```bash
# ASAPI endpoint for the RPC style:
public.asapi.<global:region>.<global:internet-domain>/asapi/v3
# ASAPI endpoint for the ROA style:
public.asapi.<global:region>.<global:internet-domain>/asapi/v3/roa
```

**Call examples**

The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
package com.aliyuns.client.pop.ecs; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.ecs.model.v20140526.DescribeInstancesRequest; import com.aliyuncs.ecs.model.v20140526.DescribeInstancesResponse; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import java.util.List; public class DescribeInstancesTest {
    public static void main(String[] args) {
        // Specify the endpoint of ASAPI.
        String endpoint = "public.asapi.<global:region>.<global:internet-domain>/asapi/v3";
        // Specify the region where the ECS service resides.
        String region = "<global:region>";
        // Specify the name of the service that you want to access.
        String product = "ECS";
        // Specify your AccessKey pair.
        String ak = "<accessKeyId>";
        String sk = "<accessKeySecret>";
        try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(region, ak, sk);
            // Ignore SSL certificate validation.
            HttpClientConfig clientConfig = HttpClientConfig.getDefault();
            clientConfig.setIgnoreSSLCerts(true);
            // Set the connection timeout period.
            clientConfig.setConnectionTimeoutMillis(3000L);
            // Set the read timeout period.
            clientConfig.setReadTimeoutMillis(10000L);
            clientProfile.setHttpClientConfig(clientConfig);
            // Create a connection.
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            // Create a request.
            DescribeInstancesRequest request = new DescribeInstancesRequest();
            // Specify the endpoint of ASAPI.
            request.setSysEndpoint(endpoint);
            // Specify the name of the service that you want to access and the region where the service resides.
            request.setSysLocationProduct(product);
            request.setSysRegionId(region);
            // Set the request protocol to HTTPS.
            request.setSysProtocol(ProtocolType.HTTPS);
            DescribeInstancesResponse result =  acsClient.getAcsResponse(request);
            List<DescribeInstancesResponse.Instance> instances = result.getInstances();
            for (DescribeInstancesResponse.Instance instance: instances) {
                System.out.println(instance.getInstanceId());
                System.out.println(instance.getInstanceName());
        } catch (Exception e) {
            e.printStackTrace();
```

The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code: e API calls

```java
package com.aliyuns.client.pop.cr; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceListTest {
    public static void main(String[] args) {
        // Specify the endpoint of ASAPI.
        String endpoint = "public.asapi.<global:region>.<global:internet-domain>/asapi/v3/roa";
        // Specify the region where the Container Registry service resides.
        String region = "<global:region>";
        // Specify the name of the service that you want to access.
        String product = "cr";
        // Specify your AccessKey pair.
        String ak = "<accessKeyId>";
        String sk = "<accessKeySecret>";
        DefaultProfile profile = DefaultProfile.getProfile(region, ak, sk);
        // Ignore SSL certificate validation.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        // Set the connection timeout period.
        clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        // Create a connection for the client.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create a request.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTPS);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of ASAPI.
        request.setSysDomain(endpoint);
        // Specify the version of the API.
        request.setSysVersion("2016-06-07");
        // Specify the pattern of the uniform resource identifier (URI).
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where the service resides.
        request.setSysLocationProduct(product);
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

> **Important:** If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

### 3.3 SDK for Go

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. e API calls

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Only the remote procedure call (RPC) style is supported for API calls.

**Call examples**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
package main import (
 "fmt"
 "time"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses"
```

`)`

```
func getSdkConfig() *sdk.Config {
 return sdk.NewConfig().
  WithTimeout(time.Duration(30) * time.Second).
  WithEnableAsync(true).
  WithGoRoutinePoolSize(100).
  WithMaxTaskQueueSize(10000).
  WithDebug(false).
  WithScheme("HTTP")
func main(){
 ak := "<The AccessKey ID of your Apsara Stack tenant account.>"
 sk := "<The AccessKey secret of your Apsara Stack tenant account.>"
 regionId := "<The region where the ECS service resides.>"
 endpoint := "<The endpoint of ASAPI.>" // No network protocol.
 request := requests.NewCommonRequest()
  request.SetReadTimeout(10 * time.Second) // Set the read timeout period of the request to 10 seconds.
  request.SetConnectTimeout(5 * time.Second)  // Set the connection timeout period of the request to 5 seconds.
 request.Method = requests.GET
 request.Domain = endpoint         // Location Service will not be enabled if the host is specified. For example, the service
with a certification type-bearer token must be specified.
 request.Version = "2014-05-26"            // Specify the version of the API.
 request.Scheme = "https"                // Specify the request protocol. Default value: http.
 request.ApiName = "DescribeInstances"
 request.QueryParams["Product"] = "Ecs"  // Specify the name of the service that you want to access.
 request.TransToAcsRequest()
 client, err := sdk.NewClientWithOptions(regionId,getSdkConfig(),credentials.NewAccessKeyCredential(ak,sk))
 // If relevant parameters are not set for the request, the client settings are used.
  //client.SetReadTimeout(10 * time.Second)              // Set the read timeout period of the client to 10 seconds.
 //client.SetConnectTimeout(5 * time.Second)            // Set the connection timeout period of the client to 5 seconds.
  resp := responses.BaseResponse{}
  err = client.DoAction(request, &resp)
    if err != nil {
        panic(err)
 fmt.Print(endpoint)
```

**Configure proxies**

You can configure proxies in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code: e API calls

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment variable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment variable.
```

Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

### 3.4 SDK for Python

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python.

**Prerequisites**

An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed.

**Background information**

Only the remote procedure call (RPC) style is supported for API calls.

**Call examples**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code: e API calls

```java
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest import os
# Create an AcsClient instance.
client = AcsClient(
   "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>",
   timeout=1000,  # Set the timeout period.
    verify=False, # Ignore certificate validation. or verify='<The location where the certificate is stored.>'
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def hello_ecs_instance():
    # Create a request and set the parameters.
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    params = {"PageNumber":"1", "Product":"Ecs","Version": "2014-05-26","Action": "DescribeInstances"};
    request.set_body_params(params)
    # The endpoint that contains no network protocol is in the following format: ASAPI domain name/asapi/v3.
    request.set_endpoint('<The endpoint of ASAPI.>')
    # Set the following parameter if the endpoint contains no network protocol:
    request.set_protocol_type("https")
    request.set_PageSize(10)
    # Initiate the API request and obtain the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
```

**Configure proxies**

Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

or SDK for Java

## 4 Call examples for SDK for Java

### 4.1 Quick start

This topic describes how to obtain and use the Server Load Balancer (SLB) SDK for Java.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. For more information about how to obtain the endpoint of the SLB API, see Obtain the endpoint of the SLB API. Java Development Kit (JDK) 1.8 or later is installed. SDKs for Java provided by Alibaba Cloudrequire JDK 1.8or later.

**Install Alibaba Cloud SDK for Java**

If you use Apache Maven to manage a Java project, import the JAR file to the pom.xml file of the project. To use the SLB SDK, you must install the SDK core library and the SLB SDK. We recommend that you use version 4.5.17 or later for the SDK core library. In this example, the SLB SDK uses version 3.3.8.

**Procedure**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code.
> The following list describes the parameters:
> <yourRegionID>: Replace the parameter with the region ID.
> <yourAccessKeyID>: Replace the parameter with your AccessKey ID.
> <yourAccessKeySecret>: Replace the parameter with your AccessKey secret.

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.alibaba.fastjson.JSON; import java.util.*; import com.aliyuncs.slb.model.v20140515.*; public class DescribeImages {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",
            "<yourAccessKeyID>",
            "<yourAccessKeySecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the required parameters.
        DescribeLoadBalancersRequest request = new DescribeLoadBalancersRequest();
        request.setResourceOwnerAccount("test"); // This value is for reference only. Enter a value based on your business r
equirements.
        request.setResourceOwnerId("1"); // This value is for reference only. Enter a value based on your business requireme
nts.
        request.setRegionId("test"); // This value is for reference only. Enter a value based on your business requirements.
        request.setServerId("test"); // This value is for reference only. Enter a value based on your business requirements.
        request.setAddressIPVersion("test"); // This value is for reference only. Enter a value based on your business requi
rements.
        request.setLoadBalancerStatus("test"); // This value is for reference only. Enter a value based on your business req
uirements.
        request.setLoadBalancerId("test"); // This value is for reference only. Enter a value based on your business require
ments.
```

or SDK for Java

```
        request.setLoadBalancerName("test"); // This value is for reference only. Enter a value based on your business requi
rements.
        request.setServerIntranetAddress("test"); // This value is for reference only. Enter a value based on your business
requirements.
        request.setAddressType("test"); // This value is for reference only. Enter a value based on your business requiremen
ts.
        request.setInternetChargeType("test"); // This value is for reference only. Enter a value based on your business req
uirements.
        request.setVpcId("test"); // This value is for reference only. Enter a value based on your business requirements.
        request.setVSwitchId("test"); // This value is for reference only. Enter a value based on your business requirements
```

`.`

```java
        request.setNetworkType("test"); // This value is for reference only. Enter a value based on your business requiremen
ts.
        request.setAddress("test"); // This value is for reference only. Enter a value based on your business requirements.
        request.setMasterZoneId("test"); // This value is for reference only. Enter a value based on your business requireme
nts.
        request.setSlaveZoneId("test"); // This value is for reference only. Enter a value based on your business requiremen
ts.
        request.setOwnerAccount("test"); // This value is for reference only. Enter a value based on your business requireme
nts.
        request.setTags("test"); // This value is for reference only. Enter a value based on your business requirements.
        request.setPayType("test"); // This value is for reference only. Enter a value based on your business requirements.
        request.setResourceGroupId("test"); // This value is for reference only. Enter a value based on your business requir
ements.
        try {
            DescribeLoadBalancersResponse response = client.getAcsResponse(request);
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

### 4.2 Work with SLB SDK for Java

#### 4.2.1 Install SLB SDK for Java

This topic describes how to install Server Load Balancer (SLB) SDK for Java and how to use the SDK to make API calls. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. Before you start, you must install the core library of Apsara Stack SDK for Java and SLB SDK for Java. We recommend that you use the core library version 4.5.17 or later, and use the SDK for Java 3.3.9. To use SLB SDK for Java, you must install the core library of Apsara Stack SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Apsara Stack SDK. or SDK for Java

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

#### 4.2.2 Configure authentication credentials

When you use Apsara Stack SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. SDK for Java supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

> **Note:** Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace it with your region ID.
    "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
```

> **Note:** Replace the preceding variables with your actual information. Remove the angle brackets (<>) when you specify the parameters.

#### 4.2.3 Call SLB SDK for Java

This topic describes how to call SLB SDK for Java.

**Procedure**

1. Create an AcsClient.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request , where **${apiName}** is the API name such as DescribeLoadBalancers. When the SDKs of multiple services are used, different requests may have the same name. Differentiate the requests by SDK package. or SDK for Java

```
DescribeLoadBalancersRequest request = new DescribeLoadBalancersRequest(); // Set service-specific parameters. request.setResourceOwnerAccount("test"); // This value is for reference only. Enter a value based on your business requirements. request.setResourceOwnerId("1"); // This value is for reference only. Enter a value based on your business requirements. request.setRegionId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setServerId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setAddressIPVersion("test"); // This value is for reference only. Enter a value based on your business requirements. request.setLoadBalancerStatus("test"); // This value is for reference only. Enter a value based on your business requirements. request.setLoadBalancerId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setLoadBalancerName("test"); // This value is for reference only. Enter a value based on your business requirements. request.setServerIntranetAddress("test"); // This value is for reference only. Enter a value based on your business requirements. request.setAddressType("test"); // This value is for reference only. Enter a value based on your business requirements. request.setInternetChargeType("test"); // This value is for reference only. Enter a value based on your business requirements. request.setVpcId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setVSwitchId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setNetworkType("test"); // This value is for reference only. Enter a value based on your business requirements. request.setAddress("test"); // This value is for reference only. Enter a value based on your business requirements. request.setMasterZoneId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setSlaveZoneId("test"); // This value is for reference only. Enter a value based on your business requirements. request.setOwnerAccount("test"); // This value is for reference only. Enter a value based on your business requirements. request.setTags("test"); // This value is for reference only. Enter a value based on your business requirements. request.setPayType("test"); // This value is for reference only. Enter a value based on your business requirements. request.setResourceGroupId("test"); // This value is for reference only. Enter a value based on your business requirements.
```

3. Initiate the request and handle the response.

```java
DescribeLoadBalancersResponse response = client.getAcsResponse(request); System.out.println(JSON.toJSONString(response));
```

#### 4.2.4 Handle errors

Server Load Balancer (SLB) SDK for Java returns error codes and messages when errors occur on the server side or the SDK side. You do not need to handle the errors returned by the SDK. You need to only handle the errors on the server side. `ServerException` indicates a server error. `ClientException` indicates an error returned by the SDK. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

The following code provides an example on how to handle errors returned by the SDK: or SDK for Java

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

r Python to make API calls

## 5 Use SLB SDK for Python to make API calls

**calls**

### 5.1 Quick start

This topic describes how to obtain and use Server Load Balancer (SLB) SDK for Python.

**Prerequisites**

An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. The endpoint of the SLB API is obtained. For more information, see Obtain the endpoint of the SLB API.

**Install SLB SDK for Python**

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

To call SLB SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must obtain a region ID, your AccessKey ID, and your AccessKey
secret.
2. Create an API request and set the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code.
> The following section describes the parameters:
> <yourRegionID>: Replace the parameter with the region ID.
> <yourAccessKeyID>: Replace the parameter with your AccessKey ID.
> <yourAccessKeySecret>: Replace the parameter with your AccessKey secret.
> <your-endpoint>: Replace the value of this parameter with the endpoint of the service.

```
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest client = AcsClient('<yourAccessKeyID>', '<yourAccessKeySecret>', '<yourRegionID>') // Create an API request and set the required parameters. request = DescribeLoadBalancersRequest() // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerId("1") // This value is for reference only. Enter a value based on your business requirements. request.set_RegionId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerId("test")
```

r Python to make API calls

```python
// This value is for reference only. Enter a value based on your business requirements. request.set_AddressIPVersion("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerStatus("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerName("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerIntranetAddress("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_InternetChargeType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VpcId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VSwitchId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_NetworkType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Address("test") // This value is for reference only. Enter a value based on your business requirements. request.set_MasterZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_SlaveZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_OwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Tags("test") // This value is for reference only. Enter a value based on your business requirements. request.set_PayType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceGroupId("test") response = client.do_action_with_exception(request) // Print the required return values.
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 5.2 Work with SLB SDK for Python

#### 5.2.1 Install SDK for Python

This topic describes how to install and use Server Load Balancer (SLB) SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK of an Apsara Stack service, you must install the core library of Alibaba Cloud SDK for Python. For example, if you want to use SLB SDK for Python, you must install the SDK core library for Python and SLB SDK for Python.

If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

r Python to make API calls The following example describes how to install the SLB SDK. If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-slb==3.3.8
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-slb==3.3.8
```

#### 5.2.2 Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. SDK for Python supports authentication through an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

> **Important:** Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 5.2.3 Set HTTPS requests

SDK for Python allows you to send API requests by using HTTP and HTTPS. You can specify a protocol (HTTP or HTTPS) for a specific request, or set a global default protocol.

> **Note:** The default protocol of the service takes precedence over the global default protocol.

**Add OpenSSL support**

OpenSSL support in Python is required for sending HTTPS requests by using SDK for Python. To use Alibaba Cloud SDK for Python to send requests over HTTPS, you need to add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later.

| Run the | python -c "import ssl" | c |
|---|---|---|
| ImportError: No module named ssl |   |   |

Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the error message `ImportError: No module named ssl` does not appear, OpenSSL is supported. If OpenSSL is not supported, run the following command to install it:

```
pip install pyopenssl
```

**Set the protocol to HTTP or HTTPS for a request**

The following code shows how to set HTTPS as the protocol for a request:

```bash
request = DescribeLoadBalancersRequest() request.set_protocol_type("https")
# Set the value to https or http.
```

**Set a global protocol for all service requests**

The following code shows how to set a global protocol for all service requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 5.2.4 Call SLB SDK for Python

This topic describes how to call Server Load Balancer (SLB) SDK for Python.

**Procedure**

1. Import SLB SDK for Python.

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest
```

2. Create an AcsClient instance.

```
client = AcsClient('<yourAccessKeyId>', '<yourAccessKeySecret>', '<yourRegionID>')
```

3. Create a Request object.
r Python to make API calls

```
request = DescribeLoadBalancersRequest() // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceOwnerId("1") // This value is for reference only. Enter a value based on your business requirements. request.set_RegionId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressIPVersion("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerStatus("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_LoadBalancerName("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ServerIntranetAddress("test") // This value is for reference only. Enter a value based on your business requirements. request.set_AddressType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_InternetChargeType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VpcId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_VSwitchId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_NetworkType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Address("test") // This value is for reference only. Enter a value based on your business requirements. request.set_MasterZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_SlaveZoneId("test") // This value is for reference only. Enter a value based on your business requirements. request.set_OwnerAccount("test") // This value is for reference only. Enter a value based on your business requirements. request.set_Tags("test") // This value is for reference only. Enter a value based on your business requirements. request.set_PayType("test") // This value is for reference only. Enter a value based on your business requirements. request.set_ResourceGroupId("test")
```

4. Initiate a call and handle the response.

```python
response = client.do_action_with_exception(request) // Print the required return values.
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

#### 5.2.5 Troubleshooting

The Python SDK returns error messages when errors occur on the server side or the SDK side. These errors contain detailed error information, including the error code and the error message. r Python to make API calls You do not need to handle the errors returned by the SDK. You only need to handle server errors based on the error messages generated on the server side. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
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

r Go to make API calls

## 6 Use SLB SDK for Go to make API calls

### 6.1 Quick start

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Server Load Balancer (SLB) SDK for Go.

**Prerequisites**

An Apsara Stack tenant account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are obtained. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of the SLB API is obtained. For more information, see Obtain the endpoint of the SLB API.

**Install the core package of Apsara Stack SDK for Go**

Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

To call SLB SDK for Go, perform the following steps:
1. Initialize a client instance.
2. Create an API request and set the required parameters.
3. Initiate the API request and manage the response or exceptions.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets <> in the final code.
> The following list describes the parameters:
> <yourRegionID>: Replace the variable with the region ID.
> <yourAccessKeyID>: Replace the variable with your AccessKey ID.
> <yourAccessKeySecret>: Replace the variable with your AccessKey secret.
> <Endpoint>: Replace the variable with the endpoint.

```java
package main import (
  "fmt"
  slb "github.com/aliyun/alibaba-cloud-sdk-go/services/slb"
```

`)`

```
func main() {
  client, err := slb.NewClientWithAccessKey("cn-hangzhou", "<yourAccessKeyID>", "<yourAccessKeySecret>")
  // Create an API request and set the required parameters.
  request := ecs.CreateDescribeLoadBalancersRequest()
  // This value is for reference only. Enter a value based on your business requirements.
  request.ResourceOwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ResourceOwnerId = "1"
  // This value is for reference only. Enter a value based on your business requirements.
  request.RegionId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ServerId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.AddressIPVersion = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.LoadBalancerStatus = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.LoadBalancerId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.LoadBalancerName = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ServerIntranetAddress = "test"
```

r Go to make API calls

```
  // This value is for reference only. Enter a value based on your business requirements.
  request.AddressType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.InternetChargeType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.VpcId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.VSwitchId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.NetworkType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.Address = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.MasterZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.SlaveZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.OwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.Tags = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.PayType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ResourceGroupId = "test"
  response, err := client.DescribeLoadBalancers(request)
  if err != nil {
    fmt.Println(err)
    return
  // Print response parameters. In this example, the RequestId parameter is printed.
  fmt.Println(response.RequestId)
```

4. Optional. Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### 6.2 Work with SLB SDK for Go

#### 6.2.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 6.2.2 Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. SDK for Go supports authentication based on an AccessKey pair. For more information, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

> **Important:** Do not disclose any code containing your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

```
client, err := slb.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

r Go to make API calls

> **Note:** In the preceding code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code.

#### 6.2.3 Call SLB SDK for Go

This topic describes how to call Server Load Balancer (SLB) SDK for Go.
1. Import SLB SDK for Go.

```java
import (
  "fmt"
  slb "github.com/aliyun/alibaba-cloud-sdk-go/services/slb"
```

`)`
2. Create a client that includes all of the API operations.

> **Note:** In the following code, replace the parameters with your actual information. Delete the angle brackets (<>) in the final code.

```
client, err := slb.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>")
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request .
**${service}** specifies the service name in lowercase, such as slb.
**${apiName}** is an API name such as DescribeLoadBalancers.
r Go to make API calls

```
request := slb.CreateDescribeLoadBalancersRequest()
 // This value is for reference only. Enter a value based on your business requirements.
  request.ResourceOwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ResourceOwnerId = "1"
  // This value is for reference only. Enter a value based on your business requirements.
  request.RegionId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ServerId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.AddressIPVersion = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.LoadBalancerStatus = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.LoadBalancerId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.LoadBalancerName = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ServerIntranetAddress = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.AddressType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.InternetChargeType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.VpcId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.VSwitchId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.NetworkType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.Address = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.MasterZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.SlaveZoneId = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.OwnerAccount = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.Tags = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.PayType = "test"
  // This value is for reference only. Enter a value based on your business requirements.
  request.ResourceGroupId = "test"
```

4. Initiate the call.

```
response, err := client.DescribeLoadBalancers(request)
```

#### 6.2.4 Troubleshooting

| ClientError |   | o |
|---|---|---|
| in | sdk.errors |   |

When you use Alibaba Cloud SDK for Go, a `ClientError` or a `ServerError` is returned if an error occurs on the server side or on the SDK side. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface, so they can be handled in a similar way as standard Go errors. You can use the following code to handle errors: r Go to make API calls

```
  response, err := client.DescribeLoadBalancers(request)
  if err != nil {
    fmt.Println(err)
    return
```

**ClientError**

When you make a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a `ClientError` . The following code shows how to identify and obtain the error message in the `ClientError` :

| Important When you use a specific error struct, you must add the error package github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors by using the following code: package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // The error package that you want to add. "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |   |   |
|---|---|---|
|   | github.com/aliyun/alibaba-cloud-sdk- |   |

```
response, err := client.DescribeLoadBalancers(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

**ServerError**

When the server returns an error message, the SDK wraps the message into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following code shows how to identify and obtain the error message in ServerError and Response:

| Important When you use a specific error struct, you must add the error package github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors by using the following code: package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // The error package that you want to add. "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |   |   |
|---|---|---|
|   | github.com/aliyun/alibaba-cloud-sdk- |   |

```
response, err := client.DescribeLoadBalancers(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

## 7 API Reference

### 7.1 Methods for API calls

To call a Server Load Balancer (SLB) API operation, you must send an HTTP GET request to the endpoint of the SLB API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. Requests and responses are encoded in UTF-8.

**Request syntax**

SLB API operations use the RPC protocol. You can call SLB API operations by sending HTTP GET requests. The following request syntax is used:

```
http://Endpoint/?Action=xx&Parameters
```

Take note of the following parameters:
**Endpoint**: The endpoint of the SLB API is slb.example.com.
**Action**: the name of the operation being performed. For example, to query SLB instances, you must set the Action parameter to
DescribeLoadBalancers.
**Version**: the version of the API that you want to use. The current SLB API version is 2014-05-15.
**Parameters**: the request parameters for the operation. Separate multiple parameters with ampersands (&).
Request parameters include both common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information, see Common parameters. The following example demonstrates how to call the DescribeLoadBalancers operation in SLB.

> **Note:** The sample request is formatted to improve readability.

```
https://slb.example.com/?Action=DescribeLoadBalancers &Format=xml &Version=2014-05-15 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &TimeStamp=2016-02-23T12:46:24Z ...
```

**API authorization**

To ensure the security of your account, we recommend that you use a RAM user to call API operations. To call the SLB API as a RAM user, you must create and attach a policy to the RAM user. For more information about the resources and operations that can be authorized to a RAM user, see RAM authentication.

**Signature**

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. SLB implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users. An AccessKey pair is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information, see Obtain an AccessKey pair. You must add the signature to the API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-
4e0ad82fd6cf
```

Take the DescribeLoadBalancers operation as an example. If the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the pre-signed request URL is:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-26 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeLoadBalancers&Format%3DXML&SignatureMethod%3DHMAC- SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02- 23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Append an ampersand (&) to the AccessKey secret as the key for calculating the HMAC value. In this example, the key is

| testsecret& | . |
|---|---|
| CT9X0VtwR86fNWSnsc6v8YG****E= |   |

3. Add the signature string to the request:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-15 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 7.2 RAM authentication

Before calling an SLB API as a RAM user, you must use an Alibaba Cloud account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, you must use an Alibaba Cloud Resource Name (ARN) as the unique identifier of the resource.

**Available SLB resources**

The following table describes the ARN format for different types of SLB resources.

| Resource type | ARN format |
|---|---|
| LoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:slb:$regionid:$accountid:loadbalancer/* |
|   | acs:slb:*:$accountid:loadbalancer/* |
|   | acs:slb:*:*:loadbalancer/* |
| Certificate | acs:slb:$regionid:$accountid:certificate/$servercertificateId |
|   | acs:slb:$regionid:$accountid:certificate/* |

$regionid/accoutid/servercertificateId is the resource ID. `*` indicates the corresponding resources.

**SLB APIs**

The following table lists the APIs that can be authorized and their corresponding ARN formats.

| API | ARN format |
|---|---|
| CreateLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/* |
| ModifyLoadBalancerInternetSpec | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DeleteLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerStatus | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerName | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancers | acs:slb:$regionid:$accountid:loadbalancer/* |
| DescribeLoadBalancerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeRegions | acs:slb:*:$accountid:* |
| UploadServerCertificate | acs:slb:%s:%s:certificate/* |
| DeleteServerCertificate | acs:slb:%s:%s:certificate/% |
| DescribeServerCertificate | acs:slb:%s:%s:certificate/% |

| SetServerCertificateName | acs:slb:%s:%s:certificate/% |
|---|---|
| DescribeServerCertificates | acs:slb:%s:%s:certificate/* |
| CreateLoadBalancerHTTPListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| CreateLoadBalancerHTTPSListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:slb:%s:%s:certificate/% |
| CreateLoadBalancerTCPListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| CreateLoadBalancerUDPListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DeleteLoadBalancerListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| StartLoadBalancerListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| StopLoadBalancerListener | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerHTTPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerHTTPSListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:slb:%s:%s:certificate/% |
| SetLoadBalancerTCPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| SetLoadBalancerUDPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerHTTPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerHTTPSListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerTCPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeLoadBalancerUDPListenerAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| AddBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |
| RemoveBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |
| SetBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |
| DescribeHealthStatus | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| CreateVServerGroup | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |
| SetVServerGroupAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DeleteVServerGroup | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeVServerGroups | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| DescribeVServerGroupAttribute | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
| AddVServerGroupBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |
| RemoveVServerGroupBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |
| ModifyVServerGroupBackendServers | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |

### 7.3 Common parameters

**Common request parameters**

Common request parameters are request parameters that you must use when you call any API. Table 1. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | String | Yes | The API version in the format of YYYY-MM-DD . Valid values: 2014-05-15 |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access a service. |
| Signature | String | Yes | The signature result string. |
| SignatureMethod | String | Yes | The algorithm used to create the request signature. Valid values: HMAC-SHA1 |
| Timestamp | String | Yes | The request timestamp. The timestamp uses UTC and it complies with the ISO 8601 standard. The timestamp format is YYYY-MM-DDThh:mm:ssZ . For example, 20:00:00 on January 1st, 2013 in China Standard Time (UTC +8) would be written as 2013-01-10T12:00:00Z. |
| SignatureVersion | String | Yes | The signature algorithm version. Valid value: 1.0 |
| SignatureNonce | String | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2014-05-19T10%3A33%3A56Z &Format=xml &AccessKeyId=testid &Action=DescribeLoadBalancerAttribute &SignatureMethod=Hmac-SHA1 &LoadBalancerId=loadBalancerID &SignatureNonce=NwDAxvLU6tFE0DVb &Version=2014-05-15 &SignatureVersion=1.0 &Signature=Signature
```

**Common response parameters**

API responses use a unified format. The 2xx HTTP status code indicates a successful invocation. The 4xx or 5xx HTTP status code indicates a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time a request is sent to call an API, the system returns a unique identifier **RequestId**, regardless of whether the invocation is successful.

```xml
<? xml version="1.0" encoding="utf-8"? >
    <!—Result root node-->
    <API name+Response>
        <!—Returned request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Returned result-->
    </API name+Response>
```

`{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /*Returned result*/
```

### 7.4 SLB instance

#### 7.4.1 CreateLoadBalancer

Creates a Server Load Balancer (SLB) instance. Before you call this operation, take note of the following items: Before you create an SLB instance, call the DescribeAvailableResource operation to query the resources available for purchase in the zone where you want to create the SLB instance. You are charged for the SLB instances that you create. For more information, see Create an SLB instance. If you do not set **LoadBalancerSpec**, a shared-resource SLB instance is created. We recommend that you set the
**LoadBalancerSpec** parameter to specify the specification of the SLB instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalancer | The operation that you want to perform. Set the value to CreateLoadBalancer. |
| RegionId | String | Yes | cn-east-hangzhou-01 | The ID of the region where you want to create the SLB instance. You can call the DescribeRegions operation to query region IDs. |
| AddressType | String | No | internet | The network type of the SLB instance. Valid values: internet and intranet. internet: After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. intranet: After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |
| InternetChargeType | String | No | paybytraffic | The billing method of the Internet-facing SLB instance. Set the value to paybytraffic. |
| Bandwidth | Integer | No | 10 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 to 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit for each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. For more information, see Bandwidth of a shared-resource SLB instance. |
| ClientToken | String | No | 5A2CFF0E-5718-45B5- 9D4D-70B3FF3898 | This parameter is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LoadBalancerName | String | No | abc | The name of the SLB instance. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores (), and _ hyphens (-). It must start with a letter. If this parameter is not set, the system automatically creates a name for the SLB instance. |
| VpcId | String | No | vpc- bp1aevy8sofi8mh1***** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |

| VSwitchId | String | No | vsw- bp12mw1f8k3jgy***** | The ID of the vSwitch to which the internal-facing SLB instance belongs. The vSwitch must be deployed in a VPC. To create an internal-facing SLB instance that is deployed in a VPC, you must set this parameter. If this parameter is set, the value of the AddessType parameter is set to intranet by default. |
|---|---|---|---|---|
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| accesskeyid _ _ | String | No | 111 | The AccessKey ID. |
| Tags | String | No | test | The tags that you want to add to the SLB instance. |
| EnableVpcVipFlow | String | No | 1 | The flow log. |
| LoadBalancerSpec | String | No | slb.s2.small | Apsara Stack provides two types of SLB instance: shared-resource SLB instances and high-performance SLB instances. You can create high-performance SLB instances of different specifications. Valid values: slb.s1.small slb.s2.small slb.s3.small slb.s2.medium For more information about the specifications of high- performance SLB instances, see High-performance SLB instances. |
| AddressIPVersion | String | No | ipv4 | The IP version that is used by the SLB instance. Valid values: ipv4 and ipv6. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-hddhfjg******* | The ID of the SLB instance. |
| Address | String | 42.250.**.** | The IP address that is allocated to the SLB instance. |
| VpcId | String | vpc-25dvzy9***** | The ID of the VPC to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecr*** | The ID of the vSwitch to which the SLB instance belongs. |
| LoadBalancerName | String | abc | The name of the SLB instance. |
| AddressIPVersion | String | ipv4 | The IP version that is used by the SLB instance. |
| NetworkType | String | classic | The type of network where the SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateLoadBalancer &RegionId=cn-east-hangzhou-01
```

Sample success responses

| XML | format |
|---|---|
| <CreateLoadBalancerResponse> <NetworkType>vpc</NetworkType> <LoadBalancerName>abc</LoadBalancerName> <Address>192.168.0.**</Address> <ResourceGroupId>rg-acfmxazb***</ResourceGroupId> <RequestId>AB197CF0-D9E9-4475-A89D-35DBCCF13BBE</RequestId> <AddressIPVersion>ipv4</AddressIPVersion> <LoadBalancerId>lb-bp1b6c719dfa0***</LoadBalancerId> <VSwitchId>vsw-bp12mw1f8k3jgygk9****</VSwitchId> <VpcId>vpc-bp1aevy8sofi8mh1q***</VpcId> </CreateLoadBalancerResponse> |   |

| JSON | format |
|---|---|
| {"LoadBalancerName":"abc", "VpcId":"vpc-25dvzy9*****", "Address":"42.250.**.**", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "NetworkType":"classic", "AddressIPVersion":"ipv4", "VSwitchId":"vsw-255ecr***", "LoadBalancerId":"lb-hddhfjg*******"} |   |

#### 7.4.2 DeleteLoadBalancer

Deletes a pay-as-you-go Server Load Balancer (SLB) instance.

> **Note:** After you delete an SLB instance, the listeners configured for the SLB instance and the tags added to the SLB instance are deleted.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalancer | The operation that you want to perform. Set the value to DeleteLoadBalancer. |
| LoadBalancerId | String | Yes | lb-bp1h66tp5uat8**** | The ID of the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

If the SLB instance that you want to delete has deletion protection enabled, the system reports an error in the following formats: `{`

```json
 "RequestId": "7B7AB375-1EA6-4A18-9D1C-F258F2D57638",
 "HostId": "slb.aliyuncs.com",
 "Code": "OperationDenied.DeleteProtectionIsOn",
 "Message": "The loadbalancer can't be deleted due to DeleteProtection is enabled."
```

```xml
   <?xml version="1.0" encoding="UTF-8" ?>
        <DeleteLoadBabalancerResponse>
 <RequestId>7B7AB375-1EA6-4A18-9D1C-F258F2D57638</RequestId>
 <HostId>slb.aliyuncs.com</HostId>
 <Code>OperationDenied.DeleteProtectionIsOn</Code>
 <Message>The loadbalancer can't be deleted due to DeleteProtection is enabled.</Message>
       </DeleteLoadBabalancerResponse>
http(s)://[Endpoint]/?Action=DeleteLoadBalancer &LoadBalancerId=lb-bp1h66tp5uat8********
```

Sample success responses

| XML | format |
|---|---|
| <DeleteLoadBabalancerResponse> <RequestId>E3F602B8-A162-4683-A7EC-49364E597259</RequestId> </DeleteLoadBabalancerResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "0D9B7343-AC1F-498C-A18A-78FE14A7C3A3" } |   |

#### 7.4.3 ModifyLoadBalancerInstanceSpec

Modifies the specification of a Server Load Balancer (SLB) instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalancerInsta nceSpec | The operation that you want to perform. Set the value to ModifyLoadBalancerInstanceSpec. |
| LoadBalancerId | String | Yes | lb-bp1b6c719df**** | The ID of the SLB instance. |
| LoadBalancerSpec | String | Yes | slb.s1.small | The specification of the SLB instance. Valid values: slb.s1.small slb.s2.small slb.s2.medium slb.s3.small slb.s3.medium slb.s3.large The supported specifications vary by region. For more information, see Instance types . Note When you change a shared-resource SLB instance to a high-performance SLB instance, your service may be temporarily interrupted for 10 to 30 seconds. Therefore, we recommend that you modify the specification during off-peak hours. In addition, you can use Alibaba Cloud DNS (DNS) to schedule your workloads to another SLB instance before you modify the specification. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInstanceSpec &LoadBalancerId=lb-bp1b6c719df**** &LoadBalancerSpec=slb.s2.small
```

Sample success responses

| XML | format |
|---|---|
| <ModifyLoadBalancerInstanceSpecResponse> <RequestId>D456A34A-6E40-4379-8DAF-9175760FE215</RequestId> </ModifyLoadBalancerInstanceSpecResponse> |   |

| JSON | format |
|---|---|
| { "ModifyLoadBalancerInstanceSpecResponse": { "RequestId": "D456A34A-6E40-4379-8DAF-9175760FE215" } } |   |

#### 7.4.4 ModifyLoadBalancerInternetSpec

Modifies the billing method of an Internet-facing Server Load Balancer (SLB) instance. You can modify the billing method of an Internet-facing SLB instance in the following ways: Change the bandwidth limit of a pay-by-bandwidth SLB instance. The new bandwidth limit immediately takes effect. Change the billing method of an SLB instance from pay-by-data-transfer to pay-by-bandwidth. The new billing method takes effect at 00:00 the following day. Change the billing method of an SLB instance from pay-by-bandwidth to pay-by-data-transfer. The new billing method takes effect at 00:00 the following day.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalancerInter netSpec | The operation that you want to perform. Set the value to ModifyLoadBalancerInternetSpec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | 10 | The bandwidth limit of the Internet-facing SLB instance that is billed on a pay-by-bandwidth basis. Unit: Mbit/s. Valid values: 1 to 5000. The bandwidth limit varies based on the region where the SLB instance is created. Note You do not need to set this parameter for pay-by-data-transfer SLB instances. In this case, the value of InternetChargeType is paybytraffic. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInternetSpec &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

Sample success responses

```xml
<ModifyLoadBalancerInternetSpecResponse>
      <RequestId>E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED</RequestId>
</ModifyLoadBalancerInternetSpecResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED" } |   |

#### 7.4.5 SetLoadBalancerName

Modifies the name of a Server Load Balancer (SLB) instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerName | The operation that you want to perform. Set the value to SetLoadBalancerName. |
| LoadBalancerId | String | Yes | lb-bp1b6c719dfa08e**** | The ID of the SLB instance. |
| LoadBalancerName | String | Yes | lb-instance-test | The name of the SLB instance. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (), _ and hyphens (-). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerName &LoadBalancerId=lb-bp1b6c719dfa08e**** &LoadBalancerName=abc1
```

Sample success responses

| XML | format |
|---|---|
| <SetLoadBalancerStatusResponse> <RequestId>3C7F675E-9F82-4806-BA47-FF57E3ACC850</RequestId> </SetLoadBalancerStatusResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "3C7F675E-9F82-4806-BA47-FF57E3ACC850" } |   |

#### 7.4.6 SetLoadBalancerStatus

Sets the state of a Server Load Balancer (SLB) instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerStatus | The operation that you want to perform. Set the value to SetLoadBalancerStatus. |

| LoadBalancerId | String | Yes | lb-bp1b6c719dfa08e**** | The ID of the SLB instance. |
|---|---|---|---|---|
| LoadBalancerStatus | String | Yes | active | The state of the SLB instance. Valid values: active and inactive. active (default) When an SLB instance is in the Active state, listeners of the SLB instance can forward inbound traffic based on forwarding rules. inactive When an SLB instance is in the inactive state, listeners of the SLB instance do not forward inbound traffic. Note If all listeners of an SLB instance are deleted, the SLB instance automatically switches to the inactive state. |
| accesskeyid _ _ | String | No | acc- hp34s2h0xx1ht4nwo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The key and value of the tag. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerStatus &LoadBalancerId=lb-bp1b6c719dfa08e****** &LoadBalancerStatus=active
```

Sample success responses

| XML | format |
|---|---|
| <SetLoadBalancerStatusResponse> <RequestId>E6DDFE22-F019-4F34-B8DD-FD14973450A6</RequestId> </SetLoadBalancerStatusResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "E6DDFE22-F019-4F34-B8DD-FD14973450A6" } |   |

#### 7.4.7 DescribeLoadBalancerAttribute

Queries detailed information about a specified Server Load Balancer (SLB) instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBalancerAtt ribute | The operation that you want to perform. Set the value to DescribeLoadBalancerAttribute. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| LoadBalancerId | String | lb-dhhd**** | The ID of the SLB instance. |
|---|---|---|---|
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |
| RegionIdAlias | String | cn-qingdao-env17-d01 | The alias of the region where the SLB instance is deployed. |
| LoadBalancerName | String | abc | The name of the SLB instance. |
| LoadBalancerStatus | String | active | The state of the SLB instance. Valid values: inactive: The SLB instance is stopped. SLB instances in the inactive state do not forward traffic. active: The SLB instance runs as expected. Newly created SLB instances are in the active state by default. locked: The SLB instance is locked. SLB instances may be locked due to overdue payments or other reasons. |
| Address | String | 42.XX.XX.6 | The IP address that the SLB instance uses to provide services. |
| AddressType | String | internet | The type of IP address that the SLB instance uses to provide services. |
| NetworkType | String | vpc | The type of network where the SLB instance is deployed. |
| VpcId | String | vpc-25dvzy9f8**** | The ID of the virtual private cloud (VPC) where the internal- facing SLB instance is deployed. |
| Bandwidth | Integer | 5 | The bandwidth limit of the Internet-facing SLB instance that is billed on a pay-by-bandwidth basis. |
| CreateTime | String | 2017-08-31T02:49:05Z | The time when the SLB instance was created. |
| ListenerPorts | List | 80 | The list of frontend ports that are used by the SLB instance. |
| ListenerPortsAndProto col | Array of ListenerPortAndProtoc ol |   | The list of frontend ports and protocols that are used by the SLB instance. |
| ListenerPortAndProtoc ol |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtocol | String | https | The frontend protocol that is used by the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers that are added to the SLB instance. |
| BackendServer |   |   |   |
| ServerId | String | i-djghr2**** | The ID of the backend server. |
| Weight | Integer | 90 | The weight of the backend server. |
| ServerIp | String | 192.168.0.1 | The IP address of the backend server. |
| Type | String | ecs | The type of the backend server. |
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |
| AutoReleaseTime | Long | 1513947075 | The timestamp that indicates when the SLB instance was released. |

| CreateTimeStamp | Long | 1504147745000 | The timestamp that indicates when the SLB instance was created. |
|---|---|---|---|
| EndTime | String | 2999-09-08T16:00:00Z | The time when the SLB instance was suspended. |
| EndTimeStamp | Long | 32493801600000 | The timestamp that indicates when the SLB instance was suspended. |
| InternetChargeType | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Valid values: paybybandwidth and paybytraffic. paybybandwidth: pay-by-bandwidth paybytraffic (default): pay-by-data-transfer |
| ListenerPortsAndProto cal | Array of ListenerPortAndProtoc al |   | The port and protocol of the listener. |
| ListenerPortAndProtoc al |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtocal | String | http | The frontend protocol that is used by the SLB instance. |
| LoadBalancerSpec | String | slb.s2.small | The specification of the SLB instance. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecrwq5**** | The ID of the vSwitch to which the internal-facing SLB instance belongs. |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerAttribute &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

Sample success responses

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

`{`

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

`]` `},`

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

#### 7.4.8 DescribeLoadBalancers

Queries Server Load Balancer (SLB) instances.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBalancers | The operation that you want to perform. Set the value to DescribeLoadBalancers. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. You can query the region ID from the Regions and zones list or by calling the DescribeRegions operation. |
| ServerId | String | No | vm-23**** | The ID of the backend server that is added to the SLB instance. |
| LoadBalancerId | String | No | lb-bp1b6c719dfa**** | The ID of the SLB instance. You can specify at most 10 IDs in each request. Separate multiple IDs with commas (,). |

| LoadBalancerName | String | No | abc1 | The name of the SLB instance. You can specify at most 10 names in each request. Separate multiple names with commas (,). |
|---|---|---|---|---|
| ServerIntranetAddress | String | No | 10.XX.XX.6 | The private IP address of the backend server that is added to the SLB instance. You can specify multiple IP addresses to query SLB instances. Separate multiple IP addresses with commas (,). |
| AddressType | String | No | intranet | The type of network where the SLB instance is deployed. Valid values: intranet and internet. internet: After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. intranet: After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |
| InternetChargeType | String | No | paybybandwidth | The billing method of the Internet-facing SLB instance. Valid values: paybybandwidth and paybytraffic. paybybandwidth: pay-by-bandwidth paybytraffic: pay-by-data-transfer. Note If you do not specify this parameter, the billing method of the SLB instance remains unchanged. |
| VpcId | String | No | vpc-bp1aevy8sof**** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |
| VSwitchId | String | No | vsw-bp12mw1f8k3**** | The ID of the vSwitch to which the SLB instance belongs. |
| NetworkType | String | No | vpc | The type of network where the internal-facing SLB instance is deployed. Valid values: vpc and classic. vpc: a VPC classic: a classic network |
| Address | String | No | 192.168.0.1 | The IP address that the SLB instance uses to provide services. |
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. Multiple zones are not supported for users whose workloads are deployed on Alibaba Finance Cloud. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The list of tags that are added to the SLB instances. The tags must be key-value pairs in a JSON dictionary. You can specify at most 10 tags in each request. |
| PayType | String | No | PayOnDemand | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. PayOnDemand: pay-as-you-go PrePay: subscription |

| AddressIPVersion | String | No | ipv4 | The IP version. Valid values: ipv4 and ipv6. Note You can create high-performance IPv6 SLB instances only in the following zones: Hangzhou Zone E and Hangzhou Zone F in the China (Hangzhou) region, Beijing Zone F and Beijing Zone G in the China (Beijing) region, Nantong Zone D and Nantong Zone E in the China (Nantong) region, Zhangjiakou Zone A and Zhangjiakou Zone B in the China (Zhangjiakou) region, and Shenzhen Zone D and Shenzhen Zone E in the China (Shenzhen) region. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancers | Array of LoadBalancer |   | The list of SLB instances. |
| LoadBalancer |   |   |   |
| LoadBalancerId | String | lb-hjfng**** | The ID of the SLB instance. |
| LoadBalancerName | String | def | The name of the SLB instance. |
| LoadBalancerStatus | String | active | The state of the SLB instance. Valid values: inactive: Listeners do not forward requests. active: Newly created SLB instances are in the active state by default. locked: The SLB instance is locked. |
| Address | String | 100.XX.XX.28 | The IP address of the SLB instance. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |
| RegionIdAlias | String | cn-qingdao-env17-d01 | The name of the region where the SLB instance is deployed. |
| AddressType | String | intranet | The type of network where the SLB instance is deployed. |
| VSwitchId | String | vsw-255ecr**** | The ID of the vSwitch to which the internal-facing SLB instance belongs. |
| VpcId | String | vpc-25dvzy9f8**** | The ID of the VPC to which the internal-facing SLB instance belongs. |
| NetworkType | String | vpc | The type of network where the internal-facing SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| CreateTime | String | 2017-08-31T02:49:05Z | The time when the SLB instance was created. |
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone where the SLB instance is deployed. |
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone where the SLB instance is deployed. |
| AddressIPVersion | String | ipv4 | The IP version. Valid values: ipv4 and ipv6. |
| CreateTimeStamp | Long | 1504147745000 | The timestamp generated when the SLB instance was created. |

| InternetChargeType | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Set the value to paybytraffic. paybytraffic (default): pay-by-data-transfer Note If the value of the PayType parameter is set to PrePay, only pay-by-bandwidth is supported. |
|---|---|---|---|
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancers &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <DescribeLoadBalancersResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <PageSize>50</PageSize> <LoadBalancers> <LoadBalancer> <CreateTimeStamp>1541679713000</CreateTimeStamp> <LoadBalancerName>abc1</LoadBalancerName> <RegionIdAlias>cn-hangzhou</RegionIdAlias> <ResourceGroupId>rg-acfmxaz*******y</ResourceGroupId> <AddressIPVersion>ipv4</AddressIPVersion> <LoadBalancerId>lb-bp1b6c********fuca5</LoadBalancerId> <VSwitchId>vsw-bp12mw1f********bmlj</VSwitchId> <InternetChargeType>4</InternetChargeType> <VpcId>vpc-bp1aevy8*********5cm</VpcId> <SlaveZoneId>cn-hangzhou-d</SlaveZoneId> <NetworkType>vpc</NetworkType> <MasterZoneId>cn-hangzhou-b</MasterZoneId> <CreateTime>2018-11-08T20:21Z</CreateTime> <Address>192.168.0.**</Address> <RegionId>cn-hangzhou</RegionId> <AddressType>intranet</AddressType> <PayType>PayOnDemand</PayType> <LoadBalancerStatus>active</LoadBalancerStatus> </LoadBalancer> </LoadBalancers> <RequestId>1C7445CB-C21C-4C19-9A3C-65C3190D1944</RequestId> </DescribeLoadBalancersResponse> |   |

`{`

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

`},`

```json
        "RequestId": "1C7445CB-C21C-4C19-9A3C-65C3190D1944"
```

#### 7.4.9 DescribeRegions

Queries regions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | The list of regions. |
| Region |   |   |   |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region. |
| LocalName | String | China (Qingdao) | The name of the region. |
| RequestId | String | 1651FBB6-4FBF-49FF-A9F5- DF5D696C7EC6 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeRegions
```

Sample success responses

```xml
<RequestId>1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6</RequestId> <Regions>
    <Region>
        <RegionId>cn-beijing</RegionId>
        <LocalName>China (Beijing)</LocalName>
    </Region>
</Regions>
```

| JSON | format |
|---|---|
| { "RequestId": "1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6", "Regions": { "Region": { "RegionId": "cn-beijing", "LocalName": "China (Beijing)" } } } |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Acquire the permissions and try again. |

#### 7.4.10 DescribeZones

Queries zones in a specified region.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

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
| RequestId | String | A48D35FF-440A-4BC0-A4A2- A9BF69B7E43A | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeZones &RegionId=cn-east-hangzhou-01
```

Sample success responses

| XML | format |
|---|---|
| <DescribeZonesResponse> <RequestId>3FF183FF-F4AA-40E8-8B5D-90788C6799C2</RequestId> <Zones> <Zone> <SlaveZones> <SlaveZone> <ZoneId>cn-hangzhou-g</ZoneId> <LocalName>Hangzhou Zone G</LocalName> </SlaveZone> <SlaveZone> <ZoneId>cn-hangzhou-d</ZoneId> <LocalName>Hangzhou Zone D</LocalName> </SlaveZone> </SlaveZones> <ZoneId>cn-hangzhou-b</ZoneId> <LocalName>Hangzhou Zone B</LocalName> </Zone> <Zone> <SlaveZones> <SlaveZone> <ZoneId>cn-hangzhou-e</ZoneId> <LocalName>Hangzhou Zone E</LocalName> </SlaveZone> </SlaveZones> <ZoneId>cn-hangzhou-d</ZoneId> <LocalName>Hangzhou Zone D</LocalName> </Zone> <Zone> <SlaveZones> <SlaveZone> <ZoneId>cn-hangzhou-f</ZoneId> <LocalName>Hangzhou Zone F</LocalName> </SlaveZone> <SlaveZone> <ZoneId>cn-hangzhou-d</ZoneId> <LocalName>Hangzhou Zone D</LocalName> </SlaveZone> </SlaveZones> <ZoneId>cn-hangzhou-e</ZoneId> <LocalName>Hangzhou Zone E</LocalName> </Zone> <Zone> <SlaveZones> <SlaveZone> <ZoneId>cn-hangzhou-e</ZoneId> <LocalName>Hangzhou Zone E</LocalName> </SlaveZone> </SlaveZones> <ZoneId>cn-hangzhou-f</ZoneId> <LocalName>Hangzhou Zone F</LocalName> </Zone> <Zone> <SlaveZones> <SlaveZone> <ZoneId>cn-hangzhou-h</ZoneId> <LocalName>Hangzhou Zone H</LocalName> </SlaveZone> <SlaveZone> <ZoneId>cn-hangzhou-b</ZoneId> <LocalName>Hangzhou Zone B</LocalName> </SlaveZone> </SlaveZones> <ZoneId>cn-hangzhou-g</ZoneId> <LocalName>Hangzhou Zone G</LocalName> </Zone> <Zone> <SlaveZones> <SlaveZone> <ZoneId>cn-hangzhou-g</ZoneId> |   |
| 58 > Document Version: 20241105 |   |

```xml
               <ZoneId>cnhangzhoug</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-h</ZoneId>
         <LocalName>Hangzhou Zone H</LocalName>
      </Zone>
   </Zones>
</DescribeZonesResponse>
```

| JSON | format |
|---|---|
| { "DescribeZonesResponse": { "RequestId": "3FF183FF-F4AA-40E8-8B5D-90788C6799C2", "Zones": { "Zone": [ { "SlaveZones": { "SlaveZone": [ { "ZoneId": "cn-hangzhou-g", "LocalName": "Hangzhou Zone G" }, { "ZoneId": "cn-hangzhou-d", "LocalName": "Hangzhou Zone D" } ] }, "ZoneId": "cn-hangzhou-b", "LocalName": "Hangzhou Zone B" }, { "SlaveZones": { "SlaveZone": { "ZoneId": "cn-hangzhou-e", "LocalName": "Hangzhou Zone E" } }, "ZoneId": "cn-hangzhou-d", "LocalName": "Hangzhou Zone D" }, { "SlaveZones": { "SlaveZone": [ { "ZoneId": "cn-hangzhou-f", "LocalName": "Hangzhou Zone F" }, { "ZoneId": "cn-hangzhou-d", "LocalName": "Hangzhou Zone D" } ] }, "ZoneId": "cn-hangzhou-e", "LocalName": "Hangzhou Zone E" }, { "SlaveZones": { "SlaveZone": { "ZoneId": "cn-hangzhou-e", "LocalName": "Hangzhou Zone E" } }, "ZoneId": "cn-hangzhou-f", "LocalName": "Hangzhou Zone F" }, { "SlaveZones": { "SlaveZone": [ { "ZoneId": "cn-hangzhou-h", "LocalName": "Hangzhou Zone H" }, { |   |

```json
                                "ZoneId": "cn-hangzhou-b",
                                "LocalName": "Hangzhou Zone B"
```

`]` `},`

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

`},`

```json
                    "ZoneId": "cn-hangzhou-h",
                    "LocalName": "Hangzhou Zone H"
```

`]`

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Request the permissions and try again. |

### 7.5 Listeners

#### 7.5.1 TCP listeners

##### 7.5.1.1 CreateLoadBalancerTCPListener

Creates a TCP listener.

> **Note:** Newly created listeners are in the Stopped state. After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalancerTCPL istener | The operation that you want to perform. Set the value to CreateLoadBalancerTCPListener. |
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 to 5120 and -1. -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit of each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |
| BackendServerPort | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 to 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. tch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. Note Only high-performance SLB instances support the sch and tch consistent hashing algorithms. |
|---|---|---|---|---|
| PersistenceTimeout | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 to 3600. Unit: seconds. Default value: 0. By default, session persistence is disabled. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. |
| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. |
| HealthCheckConnectTime out | Integer | No | 100 | The timeout period of a health check response. Valid values: 1 to 300. Unit: seconds. Default value: 5. |
| HealthCheckConnectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 to 65535. If you do not set this parameter, the port of the backend server is used for health checks. |
| healthCheckInterval | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| HealthCheckDomain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ip: The private IP address of the backend server. _ If the $ip parameter is set or the _ HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.),and hyphens (-). |

| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter to enable HTTP health checks for the TCP listener. If this parameter is not set, TCP health checks are performed. |
|---|---|---|---|---|
| HealthCheckHttpCode | String | No | http2xx,http3xx _ _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: http2xx, http3xx, http4xx, and _ _ _ http5xx. Default value: http2xx. _ _ |
| HealthCheckType | String | No | tcp | The type of health checks. Valid values: tcp and http. Default value: tcp. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| MasterSlaveServerGroupI d | String | No | rsp-0bfucw**** | The ID of the primary/secondary server group. Note You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| EstablishedTimeout | Integer | No | 500 | The timeout period of a connection. Valid values: 10 to 900. Unit: seconds. |
| Description | String | No | CreateListeners. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also _ contain Chinese characters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerTCPListener &Bandwidth=-1 &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex******
```

Sample success responses

| XML | format |
|---|---|
| <CreateLoadBalancerTCPListenerResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </CreateLoadBalancerTCPListenerResponse> |   |

| JSON | format |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 400 | Abs.VServerGroupIdAndMast erSlaveServerGroupId.MissM atch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the VServerGroupId parameter or the MasterSlaveServerGroupId parameter does not match. |
|---|---|---|---|

##### 7.5.1.2 SetLoadBalancerTCPListenerAttribute

Modifes the configurations of a TCP listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerTCPListe nerAttribute | The operation that you want to perform. Set the value to SetLoadBalancerTCPListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp1ygod3yctvg1y**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | 43 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1 and 1 to 5120. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit of each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. tch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. Note Only high-performance SLB instances support the sch and tch consistent hashing algorithms. |
| PersistenceTimeout | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 to 3600. Unit: seconds. Default value: 0. If you set the value to 0, session persistence is disabled. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. |
| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. |

| HealthCheckConnectTime out | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the health check fails. Valid values: 1 to 300. Unit: seconds. Note If the value of the HealthCheckConnectTimeout parameter is smaller than that of the HealthCheckInterval parameter, the value of the HCTimeout parameter is ignored and the value of the HealthCheckInterval parameter is used as the timeout period. |
|---|---|---|---|---|
| HealthCheckConnectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. If this parameter is not set, the port specified in BackendServerPort is used for health checks. |
| HealthCheckInterval | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| HealthCheckDomain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. $ip: The private IP address of the backend server. _ If you do not set this parameter or set the parameter to $ip, the SLB instance uses the private _ IP address of each backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. ) |
| HealthCheckHttpCode | String | No | http2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: http2xx, http3xx, http4xx, and _ _ _ http5xx. _ |
| HealthCheckType | String | No | tcp | The type of health checks. Valid values: tcp and http. |
| SynProxy | String | No | enable | Specifies whether to enable SynProxy to protect backend servers against attacks. We recommend that you use the default value for this parameter. Valid values: enable and disable. |
| MaxConnection | Integer | No | 20 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and off. You cannot set both VserverGroup and MasterSlaveServerGroup to on. |

| VServerGroupId | String | No | rsp-cige6j5**** | The ID of the vServer group. |
|---|---|---|---|---|
| MasterSlaveServerGroupI d | String | No | rsp-cige**** | The ID of the primary/secondary server group. Note You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| MasterSlaveServerGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and off. You cannot set both VserverGroup and MasterSlaveServerGroup to on. |
| EstablishedTimeout | Integer | No | 500 | The timeout period of connections. Valid values: 10 to 900. Unit: seconds. |
| Description | String | No | test | The description of the TCP listener. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y****
```

Sample success responses

| XML | format |
|---|---|
| <SetLoadBalancerTCPListenerAttributeResponse> <RequestId>59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1</RequestId> </SetLoadBalancerTCPListenerAttributeResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1" } |   |

##### 7.5.1.3 DescribeLoadBalancerTCPListenerAttribute

Queries the configurations of a TCP listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBalancerTC PListenerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerTCPListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp1ygod3yctvg1y**** | The ID of the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerPort | Integer | 80 | The backend port that is used by the SLB instance. Note When the SLB instance uses a vServer group, this parameter is not displayed. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing SLB instance, this value is set to -1. This indicates that the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, a bandwidth limit is set for each listener. The sum of bandwidth limit values that are set for all listeners of an SLB instance does not exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and stopped. running: indicates that the listener runs as expected. stopped: indicates that the listener is stopped. |
| SynProxy | String | enable | Indicates whether SynProxy is enabled. SynProxy is a feature that protects SLB from attacks. We recommend that you use the default value for this parameter. Valid values: Enable: SynProxy is enabled. Disable: SynProxy is disabled. |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| PersistenceTimeout | Integer | 0 | Indicates whether session persistence is enabled. If the value is set to 0, it indicates that session persistence is disabled. |
| HealthCheckType | String | tcp | The health check method that is used by the TCP listener. Valid values: tcp and http. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and off. |
| HealthyThreshold | Integer | 4 | The healthy threshold. |
| UnhealthyThreshold | Integer | 4 | The unhealthy threshold. |
| HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. |
| HealthCheckInterval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| HealthCheckDomain | String | www.domain.com | The domain name that is used for health checks. |

|   | HealthCheckURI | String |   | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | hyphens (-), forward slashes |   |
|   |   |   |   |   | (/), periods (.),%?number signs (#), and ampersands |   |   |
|   |   |   |   |   | (&) |   |   |
|   | HealthCheckHttpCode | String |   | http2xx _ | The HTTP status code that indicates a successful health check. Valid values: http2xx, http3xx, http4xx, and http5xx. _ _ _ _ Default value: http2xx. _ |   |   |
|   | VServerGroupId | String |   | rsp-cige6******8 | The ID of the associated vServer group. |   |   |
|   | Description | String |   | Description. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (- ), forward slashes (/), periods (.),and underscores (). It can _ also contain Chinese characters. |   |   |
|   | EstablishedTimeout | Integer |   | 500 | The timeout period of connections. Valid values: 10 to 900. Unit: seconds. |   |   |
|   | HealthCheckConnectTi meout | Integer |   | 100 | The timeout period of a health check response. |   |   |
|   | MasterSlaveServerGro upId | String |   | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |   |   |
|   | MaxConnection | Integer |   | 10 | The maximum number of connections. |   |   |
|   | RequestId | String |   | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |   |   |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y******
```

Sample success responses

| XML | format |
|---|---|
| <DescribeLoadBalancerTCPListenerAttributeResponse> <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode> <PersistenceTimeout>0</PersistenceTimeout> <HealthCheckType>tcp</HealthCheckType> <HealthyThreshold>3</HealthyThreshold> <Scheduler>wrr</Scheduler> <UnhealthyThreshold>3</UnhealthyThreshold> <Bandwidth>-1</Bandwidth> <Description>tcp_80</Description> <AclStatus>off</AclStatus> <HealthCheckURI>/</HealthCheckURI> <HealthCheck>on</HealthCheck> <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout> <ListenerPort>80</ListenerPort> <Status>running</Status> <EstablishedTimeout>900</EstablishedTimeout> <HealthCheckDomain></HealthCheckDomain> <HealthCheckInterval>2</HealthCheckInterval> <RequestId>9A113A8C-BB8F-475E-9533-7819ECA2FFC1</RequestId> <BackendServerPort>80</BackendServerPort> </DescribeLoadBalancerTCPListenerAttributeResponse> |   |

`{`

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

#### 7.5.2 UDP listeners

##### 7.5.2.1 CreateLoadBalancerUDPListener

Creates a UDP listener.

> **Note:** You cannot view the source IP addresses of network traffic if you create UDP listeners for a Server Load Balancer (SLB) instance that is deployed in a classic network. In addition, newly created listeners are in the **stopped** state. After a listener is created, you must call the StartLoadBalancerListener operation to enable the listener. This way, the listener can forward network traffic.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalancerUDPL istener | The operation that you want to perform. Set the value to CreateLoadBalancerUDPListener. |
| Bandwidth | Integer | Yes | 34 | The bandwidth limit of the listener. Unit: Mbit/s. Set the value to -1.For a pay-by-data-transfer Internet- facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1y7**** | The ID of the SLB instance. |
| BackendServerPort | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 to 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. tch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. qch: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Note Only high-performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
|---|---|---|---|---|
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. |
| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. |
| HealthCheckConnectTime out | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 to 300. Unit: seconds. |
| HealthCheckConnectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 to 65535. If you do not specify this parameter, the backend port is used to send health check probes. |
| healthCheckInterval | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| healthCheckReq | String | No | hello | Specifies the request string for UDP listener health checks. The request string must be 1 to 500 characters in length, and can contain only letters and digits. |
| healthCheckExp | String | No | ok | Specifies the response string for UDP listener health checks. The response string must be 1 to 500 characters in length, and can contain only letters and digits. |
| VServerGroupId | String | No | rsp-cige6j****8 | The ID of the vServer group. |
| MasterSlaveServerGroupI d | String | No | rsp-0bfucwu**** | The ID of the primary/secondary server group. Note You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |

| Description | String | No | test | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also _ contain Chinese characters. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerUDPListener &Bandwidth=34 &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y7******
```

Sample success responses

| XML | format |
|---|---|
| <CreateLoadBalancerUDPListenerResponse> <RequestId>06F00FBB-3D9E-4CCE-9D43-1A6946A75456</RequestId> </CreateLoadBalancerUDPListenerResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "06F00FBB-3D9E-4CCE-9D43-1A6946A75456" } |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.VServerGroupIdAndMast erSlaveServerGroupId.MissM atch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the VServerGroupId parameter or the MasterSlaveServerGroupId parameter does not match. |

##### 7.5.2.2 SetLoadBalancerUDPListenerAttribute

Modifies the configurations of a UDP listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerUDPList enerAttribute | The operation that you want to perform. Set the value to SetLoadBalancerUDPListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb43ecu4sf- c**** | The ID of the SLB instance. |

| Bandwidth | Integer | No | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 to 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify a value as the bandwidth limit for each listener. The sum of maximum bandwidth values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. For more information, see Bandwidth limit of a shared-resource SLB instance. |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. tch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. qch: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Note Only high-performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. |
| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. |
| HealthCheckConnectTime out | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 to 300. Note If the value of the HealthCheckConnectTimeout parameter is smaller than that of the HealthCheckInterval parameter, the value of the HealthCheckConnectTimeout parameter is ignored and the value of the HealthCheckInterval parameter is regarded as the timeout period. |
| HealthCheckConnectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 to 65535. |
| HealthCheckInterval | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |

| healthCheckReq | String | No | hello | The request string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |
|---|---|---|---|---|
| healthCheckExp | String | No | ok | The response string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and off. Note You cannot set both VserverGroup and MasterSlaveServerGroup to on. |
| VServerGroupId | String | No | rsp-cige6**** | The ID of the vServer group. |
| MasterSlaveServerGroupI d | String | No | rsp-0bfuc**** | The ID of the primary/secondary server group. Note You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| MasterSlaveServerGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and off. You cannot set both VserverGroup and MasterSlaveServerGroup to on. |
| Description | String | No | test | The description of the listener. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43ecu4sf-c****
```

Sample success responses

| XML | format |
|---|---|
| <SetLoadBalancerUDPListenerAttributeResponse> <RequestId>A0F0643E-D653-4F6F-A67F-205B2A92BE18</RequestId> </SetLoadBalancerUDPListenerAttributeResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "A0F0643E-D653-4F6F-A67F-205B2A92BE18" } |   |

##### 7.5.2.3 DescribeLoadBalancerUDPListenerAttribute

Queries the configurations of a UDP listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBalancerUD PListenerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerUDPListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb43e**** | The ID of the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerPort | Integer | 53 | The backend port that is used by the SLB instance. Note If the listener is associated with a vServer group, this parameter is not returned. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing SLB instance, this value is set to -1. This indicates that the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, each listener has a bandwidth limit. The sum of bandwidth limit values that are set for all listeners of an SLB instance does not exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and stopped. running: indicates that the listener runs as expected. stopped: indicates that the listener is stopped. |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and off. |
| HealthyThreshold | Integer | 4 | The healthy threshold. |
| UnhealthyThreshold | Integer | 4 | The unhealthy threshold. |
| HealthCheckConnectTi meout | Integer | 100 | The timeout period for a health check response. |
| HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. Note This parameter takes effect only when the HealthCheck parameter is set to on. |

| HealthCheckInterval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the listener. |
| Description | String | AccessControlDescription. | The description of access control. |
| HealthCheckExp | String | ok | The response string for UDP listener health checks. |
| HealthCheckReq | String | hello | The request string for UDP listener health checks. |
| MasterSlaveServerGro upId | String | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |
| MaxConnection | Integer | 10 | The maximum number of connections. |
| PersistenceTimeout | Integer | 0 | The timeout period of session persistence. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43e****
```

Sample success responses

| XML | format |
|---|---|
| <DescribeLoadBalancerUDPListenerAttributeResponse> <AclStatus>off</AclStatus> <HealthCheck>on</HealthCheck> <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout> <PersistenceTimeout>0</PersistenceTimeout> <ListenerPort>80</ListenerPort> <Status>stopped</Status> <Scheduler>wrr</Scheduler> <HealthyThreshold>3</HealthyThreshold> <HealthCheckInterval>2</HealthCheckInterval> <RequestId>9C103591-2533-432B-9E6B-6DB098C0E65C</RequestId> <UnhealthyThreshold>3</UnhealthyThreshold> <BackendServerPort>34</BackendServerPort> <Bandwidth>67</Bandwidth> </DescribeLoadBalancerUDPListenerAttributeResponse> |   |

| JSON | format |
|---|---|
| { "AclStatus":"off", "HealthCheck":"on", "HealthCheckConnectTimeout":5, "PersistenceTimeout":0, "ListenerPort":80, "Status":"stopped", "Scheduler":"wrr", "HealthyThreshold":3, "HealthCheckInterval":2, "RequestId":"9C103591-2533-432B-9E6B-6DB098C0E65C", "UnhealthyThreshold":3, "BackendServerPort":34, "Bandwidth":67 } |   |

#### 7.5.3 HTTP listeners

##### 7.5.3.1 CreateLoadBalancerHTTPListener

Creates an HTTP listener.

> **Note:** Newly created listeners are in the **stopped** state.

After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalancerHTTP Listener | The operation that you want to perform. Set the value to CreateLoadBalancerHTTPListener. |
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: If you set the value to -1, the bandwidth of the listener is unlimited. 1 to 5120: If you set a value from 1 to 5120, the value that you specify equals the bandwidth limit of the listener. The sum of bandwidth limit values that you specify for all listeners of the Server Load Balancer (SLB) instance cannot exceed the bandwidth limit of the SLB instance. Note This parameter applies only to mainland China. |
| HealthCheck | String | Yes | on | Specifies whether to enable health checks. Valid values: on and off. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1c9vixxjh92q83tw**** | The ID of the SLB instance. |
| StickySession | String | Yes | off | Specifies whether to enable session persistence. Valid values: on and off. |
| BackendServerPort | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 to 65535. Note If the VServerGroupId parameter is not set, this parameter is required. |
| XForwardedFor | String | No | on | Specifies whether to use the X-Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |

| StickySessionType |   | String | No | insert |   | The method that is used to handle a cookie. Valid values: insert: inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will forward the request to the recorded backend server. Note If you set the StickySession parameter to on, this parameter is required. |   |   |
|---|---|---|---|---|---|---|---|---|
| CookieTimeout |   | Integer | No | 500 |   | The timeout period of a cookie. Valid values: 1 to 86400. Unit: seconds. Note If you set the StickySession parameter to on and the StickySessionType parameter to insert, this parameter is required. |   |   |
| Cookie |   | String | No | B490B5EBF6F3CD402E5 15D22BCDA1598 |   | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Note If you set the StickySession parameter to on and the StickySessionType parameter to server, this parameter is required. |   |   |
| HealthCheckDomain |   | String | No | 172.XX.XX.6 |   | The domain name that is used for health checks. Valid values: $ip: The private IP address of the backend server. _ If the $ip parameter is set or the _ HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). Note This parameter takes effect only when the HealthCheck parameter is set to on. |   |   |
| HealthCheckURI |   |   |   |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward |   |   |
|   |   |   |   |   |   |   | hyphens (-), forward |   |
|   |   |   |   |   |   | slashes (/), periods (.),%?number signs (#), |   |   |
|   | RI | String | No | /test/index.html |   | and ampersands (&) |   |   |
| HealthyThreshold |   | Integer | No | 4 |   | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |   |   |

| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
|---|---|---|---|---|
| HealthCheckTimeout | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. This parameter takes effect only when the HealthCheck parameter is set to on. Valid values: 1 to 300. Unit: seconds. Note If the value of the HealthCHeckTimeout parameter is smaller than that of the HealthCheckInterval parameter, the value of the HealthCHeckTimeout parameter is invalid and the value of the HealthCheckInterval parameter is used as the timeout period. |
| HealthCheckConnectPort | Integer | No | 80 | The backend port that is used for health checks. Valid values: 1 to 65535. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckInterval | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckHttpCode | String | No | http2xx,http3xx _ _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Default value: http2xx. _ Valid values: http2xx, http3xx, http4xx, and _ _ _ http5xx. _ Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| XForwardedForSLBIP _ | String | No | on | Specifies whether to use the SLB-IP header to obtain the real IP address of the client. Valid values: on and off. Default value: off. |
| XForwardedForSLBID _ | String | No | on | Specifies whether to use the SLB-ID header to obtain the ID of the SLB instance. Valid values: on and off. Default value: off. |
| XForwardedForproto _ | String | No | on | Specifies whether to use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and off. Default value: off. |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Default value: on. Valid values: on and off. Default value: off. |

| IdleTimeout | Integer | No | 3 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |
|---|---|---|---|---|
| RequestTimeout | Integer | No | 6 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |
| ListenerForward | String | No | off | Specifies whether to enable HTTP-to-HTTPS redirection. Valid values: on and off. |
| ForwardPort | Integer | No | 443 | The listening port that is used to redirect HTTP requests to HTTPS. |
| Description | String | No | ListenerDescription | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also _ contain Chinese characters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPListener &HealthCheck=off &ListenerPort=80 &LoadBalancerId=lb-bp1c9vixxjh92q83tw***** &StickySession=off &BackendServerPort=80
```

Sample success responses

| XML | format |
|---|---|
| <CreateLoadBalancerHTTPListenerResponse> <RequestId>1FF504CB-BFFF-4508-A51A-58A416604FC8</RequestId> </CreateLoadBalancerHTTPListenerResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "1FF504CB-BFFF-4508-A51A-58A416604FC8" } |   |

##### 7.5.3.2 SetLoadBalancerHTTPListenerAttribute

Modifies the configurations of an HTTP listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerHTTPList enerAttribute | The operation that you want to perform. Set the value to SetLoadBalancerHTTPListenerAttribute. |

| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
|---|---|---|---|---|
| LoadBalancerId | String | Yes | lb-bp1qjwo61pqz3ah**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. |
| XForwardedFor | String | No | on | Specifies whether to use the X-Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and off. |
| StickySessionType | String | No | insert | The method that is used to handle a cookie. Valid values: insert: inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will forward the request to the recorded backend server. Note If you set the StickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 to 86400. Unit: seconds. Note If you set the StickySession parameter to on and the StickySessionType parameter to insert, this parameter is required. |
| Cookie | String | No | B490B5EBF6F3CD402E5 15D22BCDA1598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Note If you set the StickySession parameter to on and the StickySessionType parameter to server, this parameter is required. |

| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and off. |
|---|---|---|---|---|
| HealthCheckDomain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ip: The private IP address of the backend server. _ If the $ip parameter is specified or the _ HealthCheckDomain parameter is not specified, the SLB instance uses the private IP address of the backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckTimeout | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the health check fails. This parameter takes effect only when the HealthCheck parameter is set to on. Valid values: 1 to 300. Unit: seconds. Note If the value of the HealthCHeckTimeout parameter is smaller than that of the HealthCheckInterval parameter, the value of the HealthCHeckTimeout parameter is invalid and the value of the HealthCheckInterval parameter is used as the timeout period. |
| HealthCheckInterval | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckConnectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. Note This parameter takes effect only when the HealthCheck parameter is set to on. |

| HealthCheckHttpCode | String | No | http2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: http2xx, http3xx, http4xx, and _ _ _ http5xx. _ Note This parameter takes effect only when the HealthCheck parameter is set to on. |
|---|---|---|---|---|
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and off. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the server group. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The key and value of the tag. |
| XForwardedForSLBIP _ | String | No | on | Specifies whether to use the SLB-IP header to obtain the real IP address of the client. Valid values: on and off. |
| XForwardedForSLBID _ | String | No | on | Specifies whether to use the SLB-ID header to obtain the ID of the SLB instance. Valid values: on and off. |
| XForwardedForproto _ | String | No | on | Specifies whether to use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and off. |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and off. |
| IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| RequestTimeout | Integer | No | 3 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |
| Description | String | No | test | The description of the listener. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1qjwo61pqz3ah****
```

Sample success responses

```json
<SetLoadBalancerHTTPListenerAttributeResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPListenerAttributeResponse> {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

##### 7.5.3.3 DescribeLoadBalancerHTTPListenerAttribute

Queries the configurations of an HTTP listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBalancerHT TPListenerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHTTPListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp1o94dp5**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-east-hangzhou-01 | The ID of the region where the SLB instance is deployed. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1: If -1 is returned, it indicates that the bandwidth of the listener is unlimited. 1 to 5120: the maximum bandwidth of the listener. The sum of the maximum bandwidth of all listeners added to an SLB instance cannot exceed the maximum bandwidth of the SLB instance. Note This parameter is available only in the Chinese mainland. |
| Status | String | stopped | The status of the listener. Valid values: running stopped |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to retrieve client IP addresses. Valid values: on and off. |

| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections to a backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |
|---|---|---|---|
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and off. Default value: off. |
| StickySessionType | String | insert | The method that is used to handle a cookie. Valid values: insert and server. insert: inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client carries the user-defined cookie, and the listener will distribute this request to the recorded backend server. Note This parameter is required if the StickySession parameter is set to on. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. Unit: seconds. Valid values: 1 to 86400. |
| Cookie | String | B490B5EBF6F3CD402E515D 22BCDA1598 | The cookie that is configured on the backend server. The cookie is 1 to 200 characters in length, and can contain only ASCII characters and digits. It does not contain commas (,), semicolons (;), or space characters. It does not start with a dollar sign ($). |
| HealthCheck | String | on | Indicates whether the health check feature is enabled. Valid values: on and off. |
| HealthCheckDomain | String | www.example.com | The domain name that is used for health checks. |
| HealthCheckURI | String | /test/index.html | The URL path that is used for health checks. It is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL path is not a single forward slash (/) but it starts with a forward slash (/). ) |
| HealthyThreshold | Integer | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from fail to success. Valid values: 2 to 10. |
| UnhealthyThreshold | Integer | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from success to fail. Valid values: 2 to 10. |

| HealthCheckTimeout | Integer | 3 | The timeout period of a health check response. Unit: seconds. Valid values: 1 to 300. |
|---|---|---|---|
| HealthCheckInterval | Integer | 5 | The interval at which health checks are performed. Unit: seconds. Valid values: 1 to 50. |
| HealthCheckHttpCode | String | http2xx _ | The HTTP status code for a successful health check. Multiple HTTP status codes are separated by commas (,). Valid values: http2xx (default), http3xx, http4xx, and http5xx. _ _ _ _ Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. Note This parameter takes effect only if the HealthCheck parameter is set to on. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the forwarding rule. |
| Gzip | String | on | Indicates whether Gzip compression is enabled to compress specific types of files. Valid values: on and off. |
| AclId | String | acl-bp1l0kk4gxce43kz****** | The ID of the network access control list (ACL) that is associated with the listener. If AclStatus is set to on, this parameter is required. |
| AclStatus | String | off | Indicates whether access control is enabled. Valid values: on and off. |
| AclType | String | white | The type of the network ACL. Valid values: white: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application. After a whitelist is configured, only IP addresses in the whitelist can access the SLB listener. Risks may arise if the whitelist is improperly set. If a whitelist is configured but no IP address is added to the whitelist, the listener forwards all requests. black: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are blocked. Blacklists apply to scenarios in which you want to deny access from specific IP addresses to an application. If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests. Note This parameter takes effect if AclStatus is set to on. |
| BackendServerPort | Integer | 80 | The backend port that is used by the SLB instance. |
| Description | String | test | The description of the HTTP listener. The description is 1 to 80 characters in length, and can contain letters, digits, hyphens (- ), forward slashes (/), periods (.), and underscores (). _ |
| ForwardPort | Integer | 80 | The listening port that is used to redirect HTTP requests to HTTPS. Note If the ListenerForward parameter is set to off, this parameter is not returned. |

| IdleTimeout | Integer | 2 | The timeout period of an idle connection. Unit: seconds. Valid values: 1~60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
|---|---|---|---|
| ListenerForward | String | on | Indicates whether HTTP-to-HTTPS redirection is enabled. Valid values: on: enabled off: disabled |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeout | Integer | 34 | The request timeout period. Unit: seconds. Valid values: 1 to 180. Unit: seconds. Default value: 60. If no response is received from a backend server within the specified timeout period, SLB returns the HTTP 504 error code to the client. |
| Rules | Array of Rule |   | The list of forwarding rules. |
| Rule |   |   |   |
| Domain | String | www.example.com | The domain name. |
| RuleId | String | rule-xjsq****** | The ID of the forwarding rule. |
| RuleName | String | example | The name of the forwarding rule. |
| Url | String | /example | The request path. |
| VServerGroupId | String | rsp-bp****** | The ID of the vServer group that is associated with the forwarding rule. |
| SecurityStatus | String | on | Indicates whether the listener is in the Secure state. Valid values: on and off. |
| XForwardedForSLBID _ | String | on | Indicates whether the SLB-ID header is used to retrieve the ID of the SLB instance. |
| XForwardedForSLBIP _ | String | on | Indicates whether the SLB-IP header is used to retrieve the IP address of the SLB instance. |
| XForwardedForproto _ | String | on | Indicates whether the X-Forwarded-Proto header is used to retrieve the listening protocol. |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5*********
```

Sample success responses

```xml
<DescribeLoadBalancerHTTPListenerAttributeResponse>
    <ForwardPort>443</ForwardPort>
    <ListenerPort>80</ListenerPort>
    <Status>stopped</Status>
    <RequestId>99439CEF-192C-4B01-A45A-2D5BD5BCDA62</RequestId>
    <ListenerForward>on</ListenerForward>
</DescribeLoadBalancerHTTPListenerAttributeResponse>
```

| JSON | format |
|---|---|
| {"CookieTimeout":"500","VServerGroupId":"rsp- cige6j****","Description":"test","UnhealthyThreshold":"4","HealthCheckURI":"/test/index.html","Scheduler":"wrr","HealthCheck":" IdleTimeout":"2","BackendServerPort":"80","XForwardedFor_SLBID":"on","HealthCheckConnectPort":"8080","SecurityStatus":"on","Ban h":"-1","Gzip":"on","StickySessionType":"insert ","XForwardedFor_SLBIP":"on","HealthCheckHttpCode":"http_2xx","Cookie":"B490B5EBF6F3CD402E515D22BCDA1598","Status":"stopped","R tTimeout":"34","ListenerPort":"80","HealthCheckInterval":"5","RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710","AclId":"acl- bp1l0kk4gxce43kz******","HealthCheckTimeout":"3","Rules":[{"VServerGroupId":"rsp-bp******","RuleId":"rule- xjsq******","Domain":"www.example.com","Url":"/example","RuleName":"example"}],"ListenerForward":"on","StickySession":"on","For ort":"80","AclStatus":"off","HealthyThreshold":"4","XForwardedFor":"on","HealthCheckDomain":"www.example.com","AclType":"white" rwardedFor_proto":"on"} |   |

#### 7.5.4 HTTPS listeners

##### 7.5.4.1 CreateLoadBalancerHTTPSListener

Creates an HTTPS listener.

> **Note:** Newly created listeners are in the stopped state. After a listener is created, call the `StartLoadBalancerListener` operation to enable the listener to forward network traffic.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalancerHTTP SListener | The operation that you want to perform. Set the value to CreateLoadBalancerHTTPSListener. |
| Bandwidth | Integer | Yes | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set this parameter to -1. This way, the bandwidth of the listener is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the maximum bandwidth of each listener. The sum of the maximum bandwidth of all listeners cannot exceed the maximum bandwidth of the SLB instance. |
| HealthCheck | String | Yes | on | Specifies whether to enable the health check feature. Valid values: on and off. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp1o94dp5i6earr**** | The ID of the SLB instance. |
| StickySession | String | Yes | on | Specifies whether to enable session persistence. Valid values: on and off. |
| BackendServerPort | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 to 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| XForwardedFor | String | No | on | Specifies whether to use the X-Forwarded-For header to retrieve client IP addresses. Set the value to on. |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The routing algorithm. Valid values: wrr (default): Backend servers with higher weights receive more requests than backend servers with lower weights. wlc: Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections to a backend server. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySessionType | String | No | insert | The method that is used to handle a cookie. Default value: Insert. Valid values: insert: inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client carries this cookie, and the listener will distribute the request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, SLB rewrites the original cookie with the user-defined cookie. The next request from the client carries the user-defined cookie, and the listener distributes the request to the recorded backend server. Note This parameter is required when the StickySession parameter is set to on. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Unit: seconds. Valid values: 1 to 86400. Note If StickySession is set to on and StickySessionType is set to insert, this parameter is required. |
| Cookie | String | No | B490B5EBF6F3CD402E5 15D22BCDA1598 | The cookie that is configured on the backend server. It must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Note This parameter is required if the StickySession parameter is set to on and the StickySessionType parameter is set to server. |
| HealthCheckMethod | String | No | get | The health check method used in HTTP health checks. Valid values: head and get. Note This parameter takes effect only if the HealthCheck parameter is set to on. |
| HealthCheckDomain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ip: the private IP addresses of the backend _ servers. If you do not set this parameter or set the parameter to $ip, SLB uses the private IP address _ of each backend server for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.), and hyphens (-). Note This parameter takes effect only when the HealthCheck parameter is set to on. |

| HealthCheckURI | String | No | /test/index.html | The URI that is used for health checks. It must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: - / . % ? # & . The URL path is not a single forward slash (/) but it starts with a forward slash (/). Note This parameter takes effect when the HealthCheck parameter is set to on. |
|---|---|---|---|---|
| HealthyThreshold | Integer | No | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from fail to success. Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| UnhealthyThreshold | Integer | No | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from success to fail. Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckTimeout | Integer | No | 3 | The timeout period of a health check. If a backend server, such as an Elastic Compute Service (ECS) instance, does not return a health check response within the specified timeout period, the server fails the health check. Unit: seconds. Valid values: 1 to 300. If the value of the HealthCheckTimeout parameter is smaller than that of the HealthCheckInterval parameter, the timeout period specified by the HealthCheckTimeout parameter is ignored and the value of the HealthCheckInterval parameter is used as the timeout period. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckConnectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. Note This parameter takes effect only if the HealthCheck parameter is set to on. |
| HealthCheckInterval | Integer | No | 5 | The interval between two consecutive health checks. Unit: seconds. Valid values: 1 to 50. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckHttpCode | String | No | http2xx _ | The HTTP status code that is returned when a health check is successful. Separate multiple HTTP status codes with commas (,). Default value: http2xx. _ Valid values: http2xx, http3xx, http4xx, and _ _ _ http5xx. _ Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| ServerCertificateId | String | No | idkp-123-cn-test-**** | The ID of the server certificate. |
| VServerGroupId | String | No | rsp-cige6j5e7p**** | The ID of the server group. |

| CACertificateId | String | No | 139a00604ad-cn-east- hangzh**** | The ID of the certification authority (CA) certificate. To enable mutual authentication, upload a CA certificate and a server certificate. To enable one-way authentication, upload only a server certificate. |
|---|---|---|---|---|
| XForwardedForSLBIP _ | String | No | on | Specifies whether to use the SLB-IP header to retrieve client IP addresses. Valid values: on and off. Default value: off. |
| XForwardedForSLBID _ | String | No | on | Specifies whether to use the SLB-ID header to retrieve the ID of the SLB instance. Valid values: on and off. Default value: off. |
| XForwardedForproto _ | String | No | on | Specifies whether to use the X-Forwarded-Proto header to retrieve the listener protocol. Valid values: on and off. Default value: off. |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and off. Default value: off. |
| IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When a request is received, SLB establishes a new connection. |
| RequestTimeout | Integer | No | 23 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the request timeout period, SLB returns the HTTP 504 error code to the client. |

| TLSCipherPolicy | String | No | tlscipherpolicy11 _ _ _ _ | You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes TLS protocol versions and cipher suites that are available for HTTPS. The following security policies are supported. For more information about the differences, see Differences in TLS security policies. tlscipherpolicy10: _ _ _ _ Supported TLS versions: TLS 1.0, TLS 1.1, and TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM-SHA256, AES256- GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA tlscipherpolicy11: _ _ _ _ Supported TLS versions: TLS 1.1 and TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM-SHA256, AES256- GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA tlscipherpolicy12 _ _ _ _ Supported TLS version: TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM-SHA256, AES256- GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA tlscipherpolicy12strict _ _ _ _ _ Supported TLS version: TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA |
|---|---|---|---|---|
| Description | String | No | CreateListeners | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (). _ |
| RegionId | String | Yes | cn-east-hangzhou-01 | The ID of the region where the SLB instance is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| AclId | String | No | acl- bp1l0kk4gxce43kz****** | The ID of the network ACL that is associated with the listener. If AclStatus is set to on, this parameter is required. |

| AclType | String | No | white | The type of the ACL. Valid values: white: an allowlist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Allowlists apply to scenarios in which you want to allow only specified IP addresses to access an application. After an allowlist is configured, only IP addresses in the allowlist can access the SLB listener. Risks may arise if the allowlist is improperly set. If an allowlist is configured but no IP address is added to the allowlist, the listener forwards all requests. black: a denylist. All requests from the IP addresses or CIDR blocks in the network ACL are blocked. Denylists apply to scenarios in which you want to deny access from specific IP addresses or CIDR blocks to an application. If a denylist is configured for a listener but no IP address is added to the denylist, the listener forwards all requests. Note If AclStatus is set to on, this parameter is required. |
|---|---|---|---|---|
| AclStatus | String | No | off | Specifies whether to enable access control. Valid values: Valid values: on and off. Default value: off. |
| EnableHttp2 | String | No | off | Specifies whether to enable HTTP/2. Valid values: on and off. Default value: off. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPSListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5i6earr***** &StickySession=on
```

Sample responses

| XML | format |
|---|---|
| <CreateLoadBalancerHTTPSListenerResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </CreateLoadBalancerHTTPSListenerResponse> |   |

| JSON | format |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertSubjectDNAlias is _ duplicate. Please change to a different one. | The error message returned because the value of XForwardedForClientCertSubjectDNAlias is _ duplicate. |
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertIssuerDNAlias is _ duplicate. Please change to a different one. | The error message returned because the value of XForwardedForClientCertIssuerDNAlias is _ duplicate. |

| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertFingerprintAlias is _ duplicate. Please change to a different one. | The error message returned because the value of XForwardedForClientCertFingerprintAlias is _ duplicate. |
|---|---|---|---|
| 400 | ParamDuplicateError | The specified parameter value of XForwardedForClientCertClientVerifyAlias is _ duplicate. Please change to a different one. | The error message returned because the value of XForwardedForClientCertClientVerifyAlias is _ duplicate. |
| 400 | IpVersionConflict | The ip version of this LoadBalancer and the Acl is conflict. | The error message returned because the specified IP version is not supported by the network ACL. |
| 400 | InvalidParameter.IdleTimeout | The specified IdleTimeout exceeds the limit. | The error message returned because the specified timeout period of idle connections is invalid. Specify a valid value and try again. |
| 400 | InvalidParameter.RequestTim eout | The specified RequestTimeout exceeds the limit. | The error message returned because the specified timeout period of requests is invalid. Specify a valid value and try again. |
| 400 | ListenerForwardNotSupport | X-Forward-For is not supported to a ipv6 instance. | The error message returned because SLB instances that have IPv6 enabled do not support the X-Forward-For header. |
| 400 | InvalidParameter.RegionNotS upport | The region does not support the parameter: %s. | The error message returned because the parameter is not supported in the region. |
| 400 | InvalidParameter.SpecNotSu pport | The loadBalancer of shared spec does not support the parameter: %s. | The error message returned because the parameter is not supported by shared- resource SLB instances. |
| 400 | ListenerProcessing | A previous configuration of the listener is pending,please try again later. | The error message returned because the specified listener is being configured. Try again later. |
| 400 | Certkey.Forbidden | The specified certkey is not owned by the current user. | The error message returned because the specified certificate key does not belong to the current account. |
| 400 | InvalidParameter.ListenerPor tConflict | There is conflict listener port exists. | The error message returned because the specified listening port already exists. |
| 400 | ResourceNotAvailible.HttpsLi stener | The specified Zone did not have enough resource. | The error message returned because resources are insufficient in the specified zone. |
| 400 | OperationUnsupported.Creat eLoadBalancerLayer7Listener | The slb instance does not support create HTTP or HTTPS listener. | The error message returned because the specified SLB instance does not support HTTP or HTTPS listeners. |
| 400 | InvalidParameter.VServerGro upId | The MasterSlaveServerGroup can not be attached to HTTP or HTTPS listener. | The error message returned because HTTP and HTTPS listeners do not support primary/secondary server groups. |
| 400 | MissingParam.HealthCheckD omain | The HealthCheckDomain is required when HealthCheckHttpVersion is http1.1. | The error message returned because the HealthCheckDomain parameter is not set. |
| 400 | InvalidParameter.HealthChec kHttpVersion | The param HealthCheckHttpVersion is invalid. | The error message returned because the specified HTTP version for health checks is invalid. Specify a valid value and try again. |
| 400 | QuotaLimitExceeds.AclAttach edToListener | %s. | The error message returned because the number of listeners associated with the network ACL has reached the upper limit. |
| 400 | QuotaLimitExceeds.TotalAclE ntry | %s. | The error message returned because the number of network ACL rules has reached the upper limit. |
| 400 | Duplicated.AclEntry | %s. | The error message returned because the specified ACL rule already exists. |
| 400 | CertificateNotExist | The specified CertificateId does not exist. | The error message returned because the specified certificate does not exist. |
| 400 | OperationFailed.InsufficientR esources | The loadbalancer does not support this operation because of insufficient resources. | The error message returned because the operation failed due to insufficient resources. |
| 400 | InvalidTLSPolicyId.NotExist | The specified TLS cipher policy does not exist. | The error message returned because the specified TLS policy does not exist. |
| 400 | TLSPolicyConfiguring | The specified TLS cipher policy is configuring. | The error message returned because the specified TLS policy is being modified. |

| 400 | TLSCipherPolicyVipRelationO verLimit | The number of listeners associated with a policy has exceeded. | The error message returned because the number of TLS policies has reached the upper limit. |
|---|---|---|---|
| 400 | CertificateTypeMismatched | The certificate type does not match. | The error message returned because the specified certificate type is invalid. |
| 400 | MissingParam.ServerCertifica tes | Server certificates are required. | The error message returned because the ServerCertificates parameter is not set. |
| 400 | TooManyCertificates | The number of certificates must not be greater than one. | The error message returned because the number of certificates cannot exceed 1. |
| 400 | CnCertificateNotSupport | The cn certificate is not support. | The error message returned because ShangMi (SM) cipher suites are not supported. |
| 400 | InvalidParam.CertificateBindi ngType | The param CertificateBindingType is invalid. | The error message returned because the CertificateBindingType parameter is set to an invalid value. Specify a valid value and try again. |
| 400 | InvalidParamSize.ServerCerti ficates | The size of param ServerCertificates is invalid. | The error message returned because the value of the ServerCertificates parameter is in an invalid length. Specify a valid value and try again. |
| 400 | TooManyCertificates.ServerC ertificates | The number of certificates must not be greater than one. | The error message returned because the number of certificates cannot exceed 1. |
| 400 | LbNotSupportTcpssl | You cannot create a TCP SSL type listener for the specified load balancer. | The error message returned because the specified instance does not allow you to create TCP SSL listeners. |
| 400 | LbSupportTcpsslOnly | The specified load balancer supports TCP SSL type listener only. | The error message returned because the specified instance allows you to create only TCP SSL listeners. |
| 400 | ListenerNotSupportRule | You cannot create a rule for the specified listener. | The error message returned because the specified listener does not allow you to create forwarding rules. |
| 400 | Mismatch.SlbSpecTypeAndLis tenerProtocol | The SlbSpecType and ListenerProtocol are mismatched. | The error message returned because the specified instance type and listener type do not match. |

##### 7.5.4.2 SetLoadBalancerHTTPSListenerAttribute

Modifies the configurations of an HTTPS listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerHTTPSLi stenerAttribute | The operation that you want to perform. Set the value to SetLoadBalancerHTTPSListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-sjhfdji**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | Specify the bandwidth limit of the listener. Valid values: 1 to 5120 and -1. -1: If you set the value to -1, the bandwidth is unlimited. 1 to 5120: If you set a value from 1 to 5120, the value that you specify equals the bandwidth limit of the listener. The sum of bandwidth limit values that you specify for all listeners of the SLB instance cannot exceed the bandwidth limit of the SLB instance. |
| XForwardedFor | String | No | on | Specifies whether to use the X-Forwarded-For header to obtain the real IP address of the client. Valid values: on and off. |

| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
|---|---|---|---|---|
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and off. |
| StickySessionType | String | No | insert | The method that is used to handle a cookie. Valid values: insert: inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Note If you set the StickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 to 86400. Unit: seconds. Note If you set the StickySession parameter to on and the StickySessionType parameter to insert, this parameter is required. |
| Cookie | String | No | B490B5EBF6F3CD402E5 15D22BCDA1598 | The cookie that is configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Note If you set the StickySession parameter to on and the StickySessionType parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and off. |
| HealthCheckDomain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ip: The private IP address of the backend server. _ If the $ip parameter is set or the _ HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.),and hyphens (-). Note This parameter takes effect only when the HealthCheck parameter is set to on. |

| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). Note This parameter takes effect only when the HealthCheck parameter is set to on. |
|---|---|---|---|---|
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from fail to success). Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| UnhealthyThreshold | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to fail). Valid values: 2 to 10. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckTimeout | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 to 300. Unit: seconds. Note If the value of the HealthCheckTimeout parameter is smaller than that of the HealthCheckInterval parameter, the value of the HealthCheckTimeout parameter is ignored and the value of the HealthCheckInterval parameter is used as the timeout period. This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckInterval | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckConnectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| HealthCheckHttpCode | String | No | http2xx,http3xx _ _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: http2xx, http3xx, http4xx, and _ _ _ http5xx. _ Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| ServerCertificateId | String | No | idkp-123-cn-te**** | The ID of the server certificate. |

| CACertificateId | String | No | 139a00604ad-cn-east- **** | The ID of the CA certificate. If both the CA certificate and the server certificate are uploaded, two-factor authentication is used. If you upload only the server certificate, single- factor authentication is used. |
|---|---|---|---|---|
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and off. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| Tags | String | No | loadbalancerhttps**** | The tags. |
| XForwardedForSLBIP _ | String | No | on | Specifies whether to use the SLB-IP header to obtain the real IP address of the client. Valid values: on and off. |
| XForwardedForSLBID _ | String | No | on | Specifies whether to use the SLB-ID header to obtain the ID of the SLB instance. Valid values: on and off. |
| XForwardedForproto _ | String | No | on | Specifies whether to use the X-Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and off. |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and off. |
| IdleTimeout | Integer | No | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |
| RequestTimeout | Integer | No | 223 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server during the specified timeout period, SLB sends an HTTP 504 error code to the client. |

| TLSCipherPolicy | String | No | tlscipherpolicy12 _ _ _ _ | You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes TLS protocol versions and cipher suites that are available for HTTPS. You can select a security policy based on your requirements. The following security policies are supported: tlscipherpolicy10: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM-SHA256, AES256- GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. tlscipherpolicy11: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM-SHA256, AES256- GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. tlscipherpolicy12 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM-SHA256, AES256- GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. tlscipherpolicy12strict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128- GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA. |   |   |
|---|---|---|---|---|---|---|
| Description | String | No | ListenerDescription | The description of the listener. The description must be 2 to 256 characters in length. It can contain only characters in the following string: ^([^\x00-\xff]\| [\w.,;/@-]){2,256}$ . |   |   |
|   |   |   |   |   | ^([^\x00-\xff]\| |   |

|   | [\w.,;/@-]){2,256}$ |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-sjhfdji****************
```

Sample success responses

| XML | format |
|---|---|
| <SetLoadBalancerHTTPSListenerAttributeResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </SetLoadBalancerHTTPSListenerAttributeResponse> |   |

`{`

```json
 "RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

##### 7.5.4.3 DescribeLoadBalancerHTTPSListenerAttribute

Queries the configurations of an HTTPS listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBalancerHT TPSListenerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHTTPSListenerAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp1mxu5r8lau**** | The ID of the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerPort | Integer | 80 | The backend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. |
| Status | String | stopped | The state of the listener. Valid values: running and stopped. |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to obtain the real IP address of the client. Valid values: on and off. |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and off. |

| StickySessionType | String | insert | The method that is used to handle a cookie. If you set the StickySession parameter to on, this parameter is required. Valid values: insert and server. insert: inserts a cookie into the response. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Note If you set the StickySession parameter to on, this parameter is required. |
|---|---|---|---|
| CookieTimeout | Integer | 500 | The timeout period of a cookie. |
| Cookie | String | B490B5EBF6F3CD402E515D 22BCDA1598 | The cookie configured on the backend server. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and off. |
| HealthCheckDomain | String | www.test.com | The domain name that is used for health checks. |
| HealthCheckURI | String | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must start with a forward slash (/) but cannot contain only a forward slash (/). |
| HealthyThreshold | Integer | 4 | The healthy threshold. |
| UnhealthyThreshold | Integer | 4 | The unhealthy threshold. |
| HealthCheckTimeout | Integer | 3 | The timeout period of a health check response. Unit: seconds. |
| HealthCheckInterval | Integer | 5 | The time interval between two consecutive health checks. Unit: seconds. Valid values: 1 to 50. |
| HealthCheckHttpCode | String | http2xx _ | The HTTP status code that indicates a successful health check. Multiple status codes are separated with commas (,). Valid values: http2xx (default), http3xx, http4xx, and _ _ _ http5xx. _ |
| HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. Note This parameter takes effect only when the HealthCheck parameter is set to on. |
| ServerCertificateId | String | idkp-123-cn-test-**** | The ID of the server certificate. |
| CACertificateId | String | idkp-234-cn-test-**** | The ID of the CA certificate. |
| VServerGroupId | String | rsp-cige6j5e**** | The ID of the associated vServer group. |

| Gzip | String | on | Indicates whether gzip compression is enabled. Valid values: on and off. |
|---|---|---|---|
| Description | String | ListenerDescription | The description of the listener. The description must be 2 to 256 characters in length. It can contain only Chinese characters and characters in the following string: /^([^\x00- \xff]\|[\w.,;/@-]){2,256}$/. |
| IdleTimeout | Integer | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| MaxConnection | Integer | 10 |   |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeout | Integer | 43 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If the backend server does not respond within the specified timeout period, SLB returns the HTTP 504 error code to the client. |
| SecurityStatus | String | on | The security status. Valid values: on and off. |
| TLSCipherPolicy | String | tlscipherpolicy10 _ _ _ _ | The security policy. You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes different TLS protocol versions and cipher suites for HTTPS. The following security policies are supported. For more information about the differences, see Differences in TLS security policies. You can specify a security policy based on your requirements. Valid values: tlscipherpolicy10: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256- SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. tlscipherpolicy11: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256- SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. tlscipherpolicy12 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256- SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. tlscipherpolicy12strict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA-AES128- SHA, and ECDHE-RSA-AES256-SHA. |

| XForwardedForSLBID _ | String | on | Indicates whether the SLB-ID header is used to obtain the ID of the SLB instance. Valid values: on and off. |
|---|---|---|---|
| XForwardedForSLBIP _ | String | on | Indicates whether the SLB-IP header is used to obtain the real IP address of the client. Valid values: on and off. |
| XForwardedForproto _ | String | on | Indicates whether the X-Forwarded-Proto header is used to obtain the listener protocol of the SLB instance. Valid values: on and off. |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1mxu5r8lau*******
```

Sample success responses

| XML | format |
|---|---|
| <DescribeLoadBalancerHTTPSListenerAttributeResponse> <RequestId>11F52428-64ED-40F7-98C2-DBB6D0BB0AD7</RequestId> <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode> <HealthCheckTimeout>5</HealthCheckTimeout> <ServerCertificateId>1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746</ServerCertificateId> <XForwardedFor_SLBID>off</XForwardedFor_SLBID> <Gzip>on</Gzip> <HealthyThreshold>3</HealthyThreshold> <Scheduler>wrr</Scheduler> <StickySession>off</StickySession> <UnhealthyThreshold>3</UnhealthyThreshold> <XForwardedFor_SLBIP>off</XForwardedFor_SLBIP> <XForwardedFor_proto>off</XForwardedFor_proto> <Bandwidth>-1</Bandwidth> <HealthCheckURI>/</HealthCheckURI> <VServerGroupId>rsp-0xiju72x******</VServerGroupId> <HealthCheck>on</HealthCheck> <ListenerPort>443</ListenerPort> <Status>running</Status> <XForwardedFor>on</XForwardedFor> <HealthCheckDomain></HealthCheckDomain> <HealthCheckInterval>2</HealthCheckInterval> <BackendServerPort>443</BackendServerPort> </DescribeLoadBalancerHTTPSListenerAttributeResponse> |   |

`{`

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

##### 7.5.4.4 DescribeHealthStatus

Queries the health status of backend servers.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHealthStatus | The operation that you want to perform. Set the value to DescribeHealthStatus. |
| LoadBalancerId | String | Yes | lb-bp1qjwo61pqz3ah**** | The ID of the Server Load Balancer (SLB) instance. |
| ListenerPort | Integer | No | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. Note If you do not specify this parameter, the health status of all ports is returned. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the SLB instance is deployed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-bp1h5u3fv54ytf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |
| ServerHealthStatus | String | abnormal | The health status of the backend server: normal: The backend server is healthy. abnormal: The backend server is unhealthy. unavailable: The health check is not completed. |
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| port | Integer | 80 |   |

| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |
|---|---|---|---|

```
http(s)://[Endpoint]/?Action=DescribeHealthStatus &LoadBalancerId=lb-bp1qjwo61pqz3ah****
```

Sample success responses

| XML | format |
|---|---|
| <DescribeHealthStatusResponse> <RequestId>E69BA4CE-2B55-45EC-94CA-E47B16759459</RequestId> <BackendServers> <BackendServer> <ListenerPort>80</ListenerPort> <ServerId>i-bp1h5u3fv54ytf0******</ServerId> <Port>80</Port> <ServerIp>192.168.0.**</ServerIp> <ServerHealthStatus>abnormal</ServerHealthStatus> <Protocol>http</Protocol> </BackendServer> <BackendServer> <ListenerPort>8080</ListenerPort> <ServerId>i-bp1h5u3fv54ytf0******</ServerId> <Port>80</Port> <ServerIp>192.168.0.**</ServerIp> <ServerHealthStatus>abnormal</ServerHealthStatus> <Protocol>tcp</Protocol> </BackendServer> </BackendServers> </DescribeHealthStatusResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "E69BA4CE-2B55-45EC-94CA-E47B16759459", "BackendServers": { "BackendServer": [ { "ListenerPort": 80, "ServerId": "i-bp1h5u3fv54ytf*****", "Port": 80, "ServerIp": "192.168.**.**", "ServerHealthStatus": "abnormal", "Protocol": "http" }, { "ListenerPort": 8080, "ServerId": "i-bp1h5u3fv54ytf0******", "Port": 80, "ServerIp": "192.168.**.**", "ServerHealthStatus": "abnormal", "Protocol": "tcp" } ] } } |   |

#### 7.5.5 Access control

##### 7.5.5.1 SetListenerAccessControlStatus

Enables or disables the whitelist of a specified listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | SetListenerAccessControl Status | The operation that you want to perform. Set the value to SetListenerAccessControlStatus. |
|---|---|---|---|---|
| AccessControlStatus | String | Yes | openwhitelist _ _ | Specifies whether to enable the whitelist. Valid values: openwhitelist: enables the whitelist. _ _ close: disables the whitelist. Note After the whitelist is enabled, if no IP address is added to the whitelist, the Server Load Balancer (SLB) instance does not distribute network traffic. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |
| accesskeyid _ _ | String | No | acc- hp34s2h0xx1ht4nwo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The key and value of the tag. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetListenerAccessControlStatus &AccessControlStatus=open_white_list &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex****
```

Sample success responses

| XML | format |
|---|---|
| <SetListenerAccessControlStatusResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </SetListenerAccessControlStatusResponse> |   |

| JSON | format |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |   |

##### 7.5.5.2 DescribeListenerAccessControlAttribute

Queries the whitelist configurations of a listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeListenerAccessC ontrolAttribute | The operation that you want to perform. Set the value to DescribeListenerAccessControlAttribute. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |

| LoadBalancerId | String | Yes | lb- 8vb86hxixo8*******6jaz | The ID of the SLB instance. |
|---|---|---|---|---|
| Tags | String | No | listeneraccesscontrolslb* *** | The tags. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessControlStatus | String | openwhitelist _ _ | Indicates whether the whitelist is enabled. Valid values: openwhitelist: the whitelist is enabled. _ _ close: the whitelist is disabled. |
| SourceItems | String | 192.168.0.1 | The IP addresses or CIDR blocks that are added to the whitelist. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeListenerAccessControlAttribute &ListenerPort=80 &LoadBalancerId=lb-8vb86hxixo8*******6jaz
```

Sample success responses

| XML | format |
|---|---|
| <DescribeListenerAccessControlAttributeResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <AccessControlStatus>open_white_list</AccessControlStatus> <SourceItems>192.168.0.1</SourceItems> </DescribeListenerAccessControlAttributeResponse> |   |

| JSON | format |
|---|---|
| {"AccessControlStatus":"open_white_list", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "SourceItems":"192.168.0.1"} |   |

##### 7.5.5.3 AddListenerWhiteListItem

Adds IP addresses to the whitelist of a listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddListenerWhiteListIte m | The operation that you want to perform. Set the value to AddListenerWhiteListItem. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | 139a00604ad-cn-east- hangzhou-01 | The ID of the SLB instance. |

| SourceItems | String | Yes | 1.XX.XX.1,1.XX.XX.0/21 | The IP addresses or CIDR blocks that you want to add to the whitelist. This parameter takes effect only when AccessControlStatus of the listener is set to openwhitelist. _ _ Separate multiple IP addresses or CIDR blocks with commas (,). You cannot enter 0.0.0.0 or 0.0.0.0/0. You can call the SetListenerAccessControlStatus operation to set the value of the AccessControlStatus parameter to close. This indicates that access control is disabled. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=AddListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=139a00604ad-cn-east-hangzhou-01 &SourceItems=1.XX.XX.1,XX.XX.1.0/21
```

Sample success responses

| XML | format |
|---|---|
| <AddListenerWhiteListItemResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </AddListenerWhiteListItemResponse> |   |

| JSON | format |
|---|---|
| { "AddListenerWhiteListItemResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } } |   |

##### 7.5.5.4 RemoveListenerWhiteListItem

Removes IP addresses from the whitelist of a listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveListenerWhiteList Item | The operation that you want to perform. Set the value to RemoveListenerWhiteListItem. |
| ListenerPort | Integer | Yes | 80 | The listener port. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the Server Load Balancer (SLB) instance. |

| SourceItems | String | Yes | 192.168.0.1/24 | The IP addresses or CIDR blocks to be removed. Separate multiple IP addresses or CIDR blocks with commas (,). Note If all IP addresses are removed from the whitelist, the listener does not forward requests. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=RemoveListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex**** &SourceItems=192.168.0.1
```

Sample success responses

| XML | format |
|---|---|
| <RemoveListenerWhiteListItemResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </RemoveListenerWhiteListItemResponse> |   |

| JSON | format |
|---|---|
| {"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"} |   |

##### 7.5.5.5 CreateAccessControlList

Creates an access control list (ACL). You can create multiple ACLs. Each ACL can contain one or more IP addresses or CIDR blocks. Before you create an ACL, take note of the following limits: Each Apsara Stack tenant account can create at most 50 ACLs in a region. The maximum number of IP addresses that an Apsara Stack tenant account can add to an ACL is 50. The maximum number of IP addresses or CIDR blocks that can be added to an ACL is 300. The maximum number of ACLs that can be associated with a listener is 50.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccessControlList | The operation that you want to perform. Set the value to CreateAccessControlList. |
| AclName | String | Yes | rule1 | The name of the ACL. ACL names must be unique within the region. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where you want to create the ACL. |
| AddressIPVersion | String | No | ipv4 | The IP version. Valid values: ipv4 and ipv6. Note You can create high-performance IPv6 Server Load Balancer (SLB) instances only in the following zones: Hangzhou Zone E and Hangzhou Zone F, Beijing Zone F and Beijing Zone G, Shenzhen Zone D and Shenzhen Zone E, and all zones in the China (Shanghai) region. |

| ResourceGroupId | String | No | rg-atstuj3rt**** | The ID of the resource group to which the ACL belongs. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclId | String | acl-rj9xpxzcwxrukois**** | The ID of the ACL. |
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateAccessControlList &AclName=rule1 &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <CreateAccessControlListResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> <AclId>acl-rj9xpxzcwxrukois******</AclId> </CreateAccessControlListResponse> |   |

| JSON | format |
|---|---|
| {"RequestId":"988CB45E-1643-48C0-87B4-928DDF77EA49","AclId":"acl-rj9xpxzcwxrukois****"} |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAction.RegionNotSupp ort | The region does not support this action. | The error message returned because the parameter is not supported in the current region. |
| 400 | AclNumberOverLimit | The Acl number has reached to the max quota limit. | The error message returned because the number of ACLs has reached the upper limit. |
| 400 | InvalidResourceGroupId.NotF ound | The specified ResourceGroupId is not found. | The error message returned because the specified resource group does not exist. |
| 400 | ResourceInConfiguring.Acl | The specified resource is configuring, please try again later. | The error message returned because the specified ACL is being configured. Try again later. |

##### 7.5.5.6 DeleteAccessControlList

Deletes an access control list (ACL). You can delete an ACL only if it is not associated with a listener.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccessControlList | The operation that you want to perform. Set the value to DeleteAccessControlList. |
| AclId | String | Yes | acl- bp1l0kk4gxce43kz**** | The ID of the ACL. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the ACL is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DeleteAccessControlList &AclId=acl-bp1l0kk4gxce43kz****** &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <DeleteAccessControlListResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </DeleteAccessControlListResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationFailed.AclBindedWi thVip | The ACL has binded with vip. | The error message returned because the ACL is associated with a listener and the operation failed. |

##### 7.5.5.7 DescribeAccessControlLists

Queries network access control lists (ACLs).

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessControlLis ts | The operation that you want to perform. Set the value to DescribeAccessControlLists. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the network ACL is created. You can call the DescribeRegions operation to query the most recent region list. |
| AclName | String | No | acl | The name of the network ACL. The name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), hyphens (-), forward slashes (/), and underscores (). The name of the network ACL must be _ unique within the region. |
| AddressIPVersion | String | No | ipv4 | The IP version of the Server Load Balancer (SLB) instance with which the network ACL is associated. Valid values: ipv4: IPv4 ipv6: IPv6 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| ResourceGroupId | String | No | rg-atstuj3rtop**** | The ID of the resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Acls | Array of Acl |   | A list of network ACLs. |
| Acl |   |   |   |
| AclId | String | acl-bp1l0kk4gxce43k***** | The ID of the network ACL. |
| AclName | String | rule1 | The name of the network ACL. |
| AddressIPVersion | String | ipv4 | The IP version that is used by the associated SLB instance. |
| ResourceGroupId | String | rg-jfenf*********** | The ID of the resource group. |
| Count | Integer | 5 | The number of network ACLs on the current page. |
| PageNumber | Integer | 2 | The number of the returned page. Minimum value: 1. Default value: 1. |
| PageSize | Integer | 3 | The number of entries returned per page. Default value: 10. |
| RequestId | String | 3CB646EF-6147-4566-A9D9- CE8FBE86F971 | The ID of the request. |
| TotalCount | Integer | 3 | The number of network ACLs. |

```
http(s)://[Endpoint]/?Action=DescribeAccessControlLists &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <DescribeAccessControlListsResponse> <RequestId>3CB646EF-6147-4566-A9D9-CE8FBE86F971</RequestId> <Acls> <Acl> <AclId>acl-bp1j9vn2g7wm9wn0*****</AclId> <AclName>test</AclName> <AddressIPVersion>ipv4</AddressIPVersion> </Acl> <Acl> <AclId>acl-bp1l0kk4gxce43*****</AclId> <AclName>doctest</AclName> <AddressIPVersion>ipv4</AddressIPVersion> </Acl> </Acls> </DescribeAccessControlListsResponse> |   |

`{`

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

`]`

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidResourceGroupId.NotF ound | The specified ResourceGroupId is not found. | The error message returned because the specified resource group does not exist. |

##### 7.5.5.8 DescribeAccessControlListAttribute

Queries the configurations of a network access control list (ACL).

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessControlLis tAttribute | The operation that you want to perform. Set the value to DescribeAccessControlListAttribute. |
| AclId | String | Yes | acl- bp1l0kk4gxce43kzet04s | The ID of the network ACL that you want to query. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the network ACL is created. You can call the DescribeRegions operation to query the most recent region list. |
| AclEntryComment | String | No | test | The description of the network ACL entry. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclEntrys | Array of AclEntry |   | A list of ACL entries. |
| AclEntry |   |   |   |
| AclEntryComment | String | The network ACL entry. | The description of the ACL entry. |
| AclEntryIP | String | 192.168.0.1 | The IP address specified in the network ACL entry. |
| AclId | String | acl-bp1l0kk4gxce43kzet04s | The ID of the network ACL. |
| AclName | String | doctest | The name of the network ACL. |
| AddressIPVersion | String | ipv4 | The IP version of the instance with which the network ACL is associated. |
| RelatedListeners | Array of RelatedListener |   | A list of listeners with which the network ACL is associated. |
| RelatedListener |   |   |   |

| AclType | String | white | The type of the network ACL. Valid values: black: a denylist. white: an allowlist. |
|---|---|---|---|
| ListenerPort | Integer | 443 | The frontend port of the listener with which the network ACL is associated. |
| LoadBalancerId | String | lb-bp13jaf5qli5xmgl1miup | The ID of the SLB instance. |
| Protocol | String | https | The type of protocol that the associated listener uses. Valid values: tcp udp http https |
| RequestId | String | C9906A1D-86F7-4C9C-A369- 54DA42EF206A | The ID of the request. |
| ResourceGroupId | String | rg-atstuj3rtop**** | The ID of the resource group. |

```
/?Action=DescribeAccessControlListAttribute &AclId=acl-bp1l0kk4gxce43kzet04s &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <DescribeAccessControlListAttributeResponse> <AclId>acl-bp1l0kk4gxce43kzet04s</AclId> <RelatedListeners> <RelatedListener> <AclType>white</AclType> <LoadBalancerId>lb-bp13jaf5qli5xmgl1miup</LoadBalancerId> <Protocol>https</Protocol> <ListenerPort>443</ListenerPort> </RelatedListener> </RelatedListeners> <AclName>doctest</AclName> <RequestId>C9906A1D-86F7-4C9C-A369-54DA42EF206A</RequestId> <AddressIPVersion>ipv4</AddressIPVersion> </DescribeAccessControlListAttributeResponse> |   |

| JSON | format |
|---|---|
| clEntrys":{"AclEntry":[{"AclEntryComment":"Network ACL entry","AclEntryIP":"192.168.0.1"}]},"ResourceGroupId":"rg- ******************","RequestId":"C9906A1D-86F7-4C9C-A369-54DA42EF206A","AddressIPVersion":"ipv4","AclId":"acl- bp1l0kk4gxce43kzet04s","RelatedListeners":{"RelatedListener":[{"ListenerPort":"443","AclType":"white","LoadBalancerId":"lb-bp1 3jaf5qli5xmgl1miup","Protocol":"https"}]},"AclName":"doctest"}{"A |   |

##### 7.5.5.9 SetAccessControlListAttribute

Changes the name of a network access control list (ACL).

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetAccessControlListAttri bute | The operation that you want to perform. Set the value to SetAccessControlListAttribute. |
| AclId | String | Yes | acl- bp1l0kk4gxce43kzet04s | The ID of the network ACL. |

| AclName | String | Yes | test1 | The name of the network ACL. The name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), hyphens (-), forward slashes (/), and underscores (). The name of the network ACL must be _ unique within the region. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the network ACL is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclId | String | acl-bp1l0kk4gxce43kzet04s | The ID of the network ACL. |
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetAccessControlListAttribute &AclId=acl-bp1l0kk4gxce43kzet04s &AclName=test1 &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <SetAccessControlListAttributeResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </SetAccessControlListAttributeResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |   |

##### 7.5.5.10 AddAccessControlListEntry

Adds IP addresses to an access control list (ACL). Each ACL can contain one or more IP addresses or CIDR blocks. The limits on ACLs are: The maximum number of IP addresses that an Apsara Stack tenant account can add to an ACL in each call is **50**. The maximum number of IP addresses or CIDR blocks that can be added to an ACL is **300**.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddAccessControlListEntr y | The operation that you want to perform. Set the value to AddAccessControlListEntry. |
| AclId | String | Yes | acl- bp1l0kk4gxce43kze***** | The ID of the ACL. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the ACL is created. |

| AclEntrys | String | No | [{"entry":"10.0.**.**/24"," comment":"privaterule1" }, {"entry":"192.168.**.**/1 6","comment":"privaterul e2"}] | The IP addresses that you want to add to the ACL. entry: the IP addresses or CIDR blocks that you want to add to the ACL. Separate multiple IP addresses or CIDR blocks with commas (,). comment: the comment on the ACL. Note You can add at most 50 IP addresses or CIDR blocks to an ACL in each call. If the IP address or CIDR block that you want to add to an ACL already exists, the IP address or CIDR block is not added. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA4 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=AddAccessControlListEntry &AclId=acl-bp1l0kk4gxce43kze***** &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <AddAccessControlListEntryResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </AddAccessControlListEntryResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |   |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParam.AclEntryExists | The specified aclEntry already exists in the acl. | The error message returned because the IP address or CIDR block is already in the ACL. |
| 400 | IllegalEntry | Entry version is conflict to the acl version. | The error message returned because the version of the IP address or CIDR block conflicts with the version of the ACL. |
| 400 | InvalidEntry | %s. | The error message returned because the value of a parameter is invalid. Specify a valid value and try again. |
| 400 | InvalidParam.Comment | The specified comment is invalid. | The error message returned because Comment is set to an invalid value. |
| 503 | ServiceUnavailable | Service is unavailable now. | The error message returned because the service is unavailable. |
| 400 | AclEntryExceedLimit | The maximum number of ACL entries is exceeded. | The error message returned because the number of specified IP addresses or CIDR blocks exceeds the upper limit. |

##### 7.5.5.11 RemoveAccessControlListEntry

Removes IP addresses from an access control list (ACL).

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | RemoveAccessControlLis tEntry | The operation that you want to perform. Set the value to RemoveAccessControlListEntry. |
|---|---|---|---|---|
| AclId | String | Yes | acl- bp1l0kk4gxce43k****** | The ID of the ACL. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the ACL is created. You can call the DescribeRegions operation to query the most recent region list. |
| AclEntrys | String | No | [{"entry":"10.0.**.**/24"," comment":"privaterule1" }] | The IP addresses that you want to remove from the ACL. entry: the IP address or CIDR block that you want to remove from the ACL. Separate multiple IP addresses or CIDR blocks with commas (,). comment: the comment of the ACL. Note If the ACL is associated with a listener, you cannot remove all IP addresses from the ACL. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 988CB45E-1643-48C0-87B4- 928DDF77EA49 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=RemoveAccessControlListEntry &AclId=acl-bp1l0kk4gxce43k****** &RegionId=cn-hangzhou
```

Sample responses

| XML | format |
|---|---|
| <RemoveAccessControlListEntryResponse> <RequestId>988CB45E-1643-48C0-87B4-928DDF77EA49</RequestId> </RemoveAccessControlListEntryResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "988CB45E-1643-48C0-87B4-928DDF77EA49" } |   |

#### 7.5.6 DeleteLoadBalancerListener

Deletes a listener.

> **Note:** You can delete only listeners that are in the **stopped** or **running** state.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalancerListe ner | The operation that you want to perform. Set the value to DeleteLoadBalancerListener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |

| LoadBalancerId | String | Yes | lb-bp13jaf5qli5xm**** | The ID of the SLB instance. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xm****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteLoadBalancerListenerResponse> <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId> </DeleteLoadBalancerListenerResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54" } |   |

#### 7.5.7 StopLoadBalancerListener

Disables a listener. When you call this operation, take note of the following items: If the operation is successful, the listener switches to the Stopped state. You cannot perform the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state.

> **Note:** After a listener is disabled, it stops forwarding requests to the associated backend servers. This may cause service interruptions. Proceed with caution.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopLoadBalancerListene r | The operation that you want to perform. Set the value to StopLoadBalancerListener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp13jaf5qli5xmgl**** | The ID of the SLB instance. |
| Tags | String | No | null | The key and value of the tag. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=StopLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xmgl****
```

Sample success responses

| XML | format |
|---|---|
| <StopLoadBalancerListenerResponse> <RequestId>21D2B318-650E-4B0B-A3B5-693D462247B3</RequestId> </StopLoadBalancerListenerResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "21D2B318-650E-4B0B-A3B5-693D462247B3" } |   |

#### 7.5.8 StartLoadBalancerListener

Enables a listener. When you call this operation, take note of the following items: You can call the operation only when the listener is in the Stopped state. If the operation is successful, the state of the listener changes to Starting. You cannot call the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartLoadBalancerListene r | The operation that you want to perform. Set the value to StartLoadBalancerListener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb-bp13jaf5qli5**** | The ID of the SLB instance. |
| Tags | String | No | {"tagKey":"Key1","tagVal ue":"Value1"} | The key and value of the tag. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=StartLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5****
```

Sample success responses

| XML | format |
|---|---|
| <StartLoadBalancerListenerResponse> <RequestId>CC000321-00F2-49B8-9BCA-60D822414960</RequestId> </StartLoadBalancerListenerResponse> |   |

`{`

```json
    "RequestId": "CC000321-00F2-49B8-9BCA-60D822414960"
```

### 7.6 Forwarding rules

### 7.7 Access logs

### 7.8 Server certificates

#### 7.8.1 UploadServerCertificate

Uploads a server certificate. You can upload only one server certificate and its private key in each request. The request is successful only when the server certificate and its private key are both uploaded. If the server certificate or its private key is not uploaded, the request fails. After a server certificate and its private key are uploaded, the fingerprints of all server certificates that belong to your account are returned.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadServerCertificate | The operation that you want to perform. Set the value to UploadServerCertificate. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the server certificate is created. You can call the DescribeRegions operation to query region IDs. |
| AliCloudCertificateId | String | No | 730912673******15d97 _ e7709a71445759hr789 _ _ 2****** | The ID of the server certificate that is provided by Apsara Stack SSL Certificates Service. This parameter is required if you use a server certificate that is provided by Apsara Stack SSL Certificates Service. |
| AliCloudCertificateName | String | No | testcertkey | The name of the server certificate that is provided by Apsara Stack SSL Certificates Service. |
| ServerCertificate | String | No | test | The public key certificate that you want to upload. Note This parameter is required if you use a server certificate that is provided by a third party. |
| PrivateKey | String | No | wmsa**** | The private key that you want to upload. Note This parameter is required if you use a server certificate that provided by a third party. |
| ServerCertificateName | String | No | mycert01 | The name of the server certificate that you want to upload. The name must be 1 to 80 characters in length and can contain digits, periods (.), underscores (), and _ hyphens (-). It must start with a letter. |
| Tags | String | No | ServerCertificate**** | The tag that you want to add to the server certificate. |
| StandardType | String | No | ServerCertificate | The type of the server certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| ServerCertificateId | String | xxxxidkp-123-cn-test**** | The ID of the server certificate. |
|---|---|---|---|
| ServerCertificateName | String | mycert01 | The name of the server certificate. |
| Fingerprint | String | 01:DF:AB:** | The fingerprint of the server certificate. |
| AliCloudCertificateId | String | 730912xxxxx15d97e7709a _ _ 71445759hr7**** _ | The ID of the server certificate if the server certificate is provided by Apsara Stack SSL Certificates Service. |
| AliCloudCertificateNa me | String | testcert**** | The name of the server certificate if the server certificate is provided by Apsara Stack SSL Certificates Service. |
| IsAliCloudCertificate | Integer | 0 | Indicates whether the server certificate is provided by Apsara Stack SSL Certificates Service. Valid values: 0: The server certificate is provided by a third-party CA. 1: The server certificate is provided by Apsara Stack SSL Certificates Service. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the server certificate is created. |
| RegionIdAlias | String | hangzhou | The name of the region where the server certificate is created. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=UploadServerCertificate &RegionId=cn-east-hangzhou-01
```

Sample success responses

| XML | format |
|---|---|
| <UploadServerCertificateResponse> <RegionIdAlias>cn-east-hangzhou-01</RegionIdAlias> <Fingerprint>01:DF:AB:**</Fingerprint> <AliCloudCertificateName>testcert***</AliCloudCertificateName> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <IsAliCloudCertificate>0</IsAliCloudCertificate> <ServerCertificateId>xxxxidkp-123-cn-test******</ServerCertificateId> <ServerCertificateName>mycert01</ServerCertificateName> <RegionId>cn-hangzhou</RegionId> <AliCloudCertificateId>730912xxxxx_15d97e7709a_71445759hr_7*******</AliCloudCertificateId> </UploadServerCertificateResponse> |   |

| JSON | format |
|---|---|
| { "UploadServerCertificateResponse": { "RegionIdAlias": "cn-east-hangzhou-01", "Fingerprint": "01:DF:AB:**", "AliCloudCertificateName": "testcert***", "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "IsAliCloudCertificate": 0, "ServerCertificateId": "xxxxidkp-123-cn-test******", "ServerCertificateName": "mycert01", "RegionId": "cn-hangzhou", "AliCloudCertificateId": "730912xxxxx_15d97e7709a_71445759hr_7*******" } } |   |

#### 7.8.2 DeleteServerCertificate

Deletes a server certificate.

> **Note:** You cannot delete a server certificate that is in use.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteServerCertificate | The operation that you want to perform. Set the value to DeleteServerCertificate. |
| ServerCertificateId | String | Yes | 123157****166f820468 _ 917147634087099**** _ _ | The ID of the server certificate. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DeleteServerCertificate &ServerCertificateId=123157****_166f8204689_1714763408_7099****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteServerCertificateResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </DeleteServerCertificateResponse> |   |

| JSON | format |
|---|---|
| { "DeleteServerCertificateResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984" } } |   |

#### 7.8.3 DescribeServerCertificates

Queries server certificates in a specified region.

> **Note:** For security reasons, only fingerprints and names of the server certificates are returned. The content of the server certificates and private keys is not returned.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeServerCertificate s | The operation that you want to perform. Set the value to DescribeServerCertificates. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateId | String | No | 12315790xxxxxxx166f8 _ 204689171476340870 _ _ 9***** | The ID of the server certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerCertificates | Array of ServerCertificate |   | The list of server certificates. |
| ServerCertificate |   |   |   |
| ServerCertificateId | String | 123157xxxxxxxx166f82046 _ 891714763408709981430- _ _ cn-east-hangz****** | The ID of the server certificate. |
| ServerCertificateName | String | slb | The name of the server certificate. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the server certificate is created. |
| Fingerprint | String | 68:08:1a:f8:2c:97:69:a3:a1:e 6:16:41:4b:ca:4f:5d:ee:a5:ef: 0d | The fingerprint of the server certificate. |
| AliCloudCertificateId | String | 7309xxxxxxxx15d97e7709a _ 71445759hr78928***** _ _ | The ID of the server certificate from Apsara Stack SSL Certificates Service. |
| AliCloudCertificateNa me | String | testcertkey | The name of the server certificate from Apsara Stack SSL Certificates Service. |
| IsAliCloudCertificate | Integer | 0 | Indicates whether the server certificate is from Apsara Stack SSL Certificates Service. Valid values: 1: yes 0: no |
| RegionIdAlias | String | cn-qingdao-env17-d01 | The name of the region where the SLB instance is deployed. |
| StandardType | String | ServerCertificate | The type of the server certificate. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeServerCertificates
```

Sample success responses

```xml
<DescribeServerCertificatesResponse>
      <RequestId>9FFF450B-CC09-4FFB-900F-E347EB7AA2CC</RequestId>
      <ServerCertificates>
            <ServerCertificate>
                  <CreateTimeStamp>1541761156000</CreateTimeStamp>
                  <CommonName>*.example1.com</CommonName>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:ef:0d</Fingerprint>
                  <ServerCertificateId>1231579xxxxxx_166f8204689_1714763408_709981430</ServerCertificateId>
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
                  <Fingerprint>cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:84:8d</Fingerprint>
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

`{`

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
                    "Fingerprint": "68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:ef:0d",
                    "ServerCertificateId": "1231579xxxxxx_166f8204689_1714763408_709981430",
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
                    "Fingerprint": "cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:84:8d",
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

`]`

#### 7.8.4 SetServerCertificateName

Sets the name of a server certificate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetServerCertificateNam e | The operation that you want to perform. Set the value to SetServerCertificateName. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateId | String | Yes | 139a****-cn-qingdao- env17-d01 | The ID of the server certificate. |
| ServerCertificateName | String | Yes | slb-servercertificate-cn- east-hangzhou**** | The name of the server certificate. The name must be 1 to 80 characters in length and can contain digits, periods (.), underscores (), and hyphens (-). It must _ start with a letter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FE7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetServerCertificateName &RegionId=cn-east-hangzhou-01 &ServerCertificateId=139a****-cn-east-hangzhou-01 &ServerCertificateName=slb-servercertificate-cn-east-hangzhou****
```

Sample success responses

| XML | format |
|---|---|
| <SetServerCertificateNameResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId> </SetServerCertificateNameResponse> |   |

| JSON | format |
|---|---|
| { "SetServerCertificateNameResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984" } } |   |

#### 7.8.5 UploadCACertificate

Uploads a CA certificate. You can upload only one CA certificate in each call. After a CA certificate is uploaded, the ID, name, and fingerprint of the certificate are returned.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadCACertificate | The operation that you want to perform. Set the value to UploadCACertificate. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| CACertificate | String | Yes | test | The content of the CA certificate that you want to upload. |
| CACertificateName | String | No | mycacert01 | The name of the CA certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificateId | String | 139a00604ad-cn-east- hangzh**** | The ID of the CA certificate. |
| CACertificateName | String | mycacert01 | The name of the CA certificate. |
| Fingerprint | String | 02:DF:AB:ED | The fingerprint of the CA certificate. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=UploadCACertificate &RegionId=cn-qingdao-env17-d01 &CACertificate=test
```

Sample success responses

| XML | format |
|---|---|
| <UploadCACertificateResponse> <Fingerprint>02:DF:AB:ED</Fingerprint> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <CACertificateId>139a00604ad-cn-east-hangzh*****</CACertificateId> <CACertificateName>mycacert01</CACertificateName> </UploadCACertificateResponse> |   |

| JSON | format |
|---|---|
| { "UploadCACertificateResponse": { "Fingerprint": "02:DF:AB:ED", "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "CACertificateId": "139a00604ad-cn-east-hangzh*****", "CACertificateName": "mycacert01" } } |   |

#### 7.8.6 DeleteCACertificate

Deletes a CA certificate.

> **Note:** You cannot delete a CA certificate that is in use.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCACertificate | The operation that you want to perform. Set the value to DeleteCACertificate. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 123157908****15c73d7 _ 7203-986300114- _ _ 2110544**** | The ID of the CA certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FF7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DeleteCACertificate &RegionId=cn-east-hangzhou-01 &CACertificateId=123157908****_15c73d77203_-986300114_-211054****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteCACertificateResponse> <RequestId>CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId> </DeleteCACertificateResponse> |   |

`{`

```json
    "DeleteCACertificateResponse": {
        "RequestId": "CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984"
```

#### 7.8.7 DescribeCACertificates

Queries CA certificates.

> **Note:** For security reasons, only fingerprints and names of the CA certificates are returned, the content of the CA certificates is not returned.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCACertificates | The operation that you want to perform. Set the value to DescribeCACertificates. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the CA certificate is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | No | 139a006****-cn-qingdao- env17-d01 | The ID of the CA certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificates | Array of CACertificate |   | Information about the CA certificate. |
| CACertificate |   |   |   |
| CACertificateId | String | 139a006****-cn-qingdao- env17-d01 | The ID of the CA certificate. |
| CACertificateName | String | test | The name of the CA certificate. |
| RegionId | String | cn-qingdao-env17-d01 | The ID of the region where the CA certificate is created. |
| Fingerprint | String | AC:BE:FD | The fingerprint of the CA certificate. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeCACertificates &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <DescribeCACertificateResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <CACertificates> <CACertificateName>test</CACertificateName> <Fingerprint>AC:BE:FD</Fingerprint> <RegionId>cn-east-hangzhou-01</RegionId> <CACertificateId>139a006****-cn-east-hangzhou-02</CACertificateId> </CACertificates> </DescribeCACertificateResponse> |   |

| JSON | format |
|---|---|
| { "DescribeCACertificateResponse": { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "CACertificates": { "CACertificateName": "test", "Fingerprint": "AC:BE:FD", "RegionId": "cn-east-hangzhou-01", "CACertificateId": "139a006****-cn-east-hangzhou-02" } } } |   |

#### 7.8.8 SetCACertificateName

Sets the name of a CA certificate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetCACertificateName | The operation that you want to perform. Set the value to SetCACertificateName. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 139a0****-cn-qingdao- env17-d01 | The ID of the CA certificate. |
| CACertificateName | String | Yes | mycacert02 | The name of the CA certificate. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores (), and hyphens (-). It must start with _ a letter. |
| accesskeyid _ _ | String | No | acc- hp34s2h0xx1ht4nwo**** | The AccessKey ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6-4AE8-B225- F876FE7BA984 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetCACertificateName &RegionId=cn-qingdao-env17-d01 &CACertificateId=139a0****-cn-qingdao-env17-d01 &CACertificateName=mycacert02
```

Sample success responses

| XML | format |
|---|---|
| <SetCACertificateNameResponse> <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId> </SetCACertificateNameResponse> |   |

| JSON | format |
|---|---|
| { "SetCACertificateNameResponse": { "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984" } } |   |

### 7.9 Backend servers

#### 7.9.1 AddBackendServers

Adds backend servers.

> **Note:** If multiple identical Elastic Compute Service (ECS) instances are specified in a request, only the first ECS instance is added. The other ECS instances are ignored. If the backend server that you add is the same as one of the existing backend servers that are already associated with the listener, an error message is returned.

|   | Parameter |   |   | Type | Required |   |   | Example |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Action |   |   | String | Yes |   |   | AddBackendServers |   | The operation that you want to perform. Set the value to AddBackendServers. |   |   |   |   |
|   | LoadBalancerId |   |   | String | Yes |   |   | lb- 2ze7o5h52g02kkzz**** |   | The ID of the Server Load Balancer (SLB) instance. |   |   |   |   |
|   | BackendServers |   |   | String | Yes |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description": "test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description": |   | The list of backend servers that you want to add to the SLB instance. The following parameters are used to specify the backend servers: ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. You can specify the ID of an ECS instance or an elastic network interface (ENI). If ServerId is set to the ID of an ENI, the Type parameter is required. Weight: The weight of the backend server. Valid values: 0 to 100. Default value: 100. Note If the weight is set to 0, no requests are forwarded to the backend server. Description: Optional. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. Type: Specify the type of backend server. Valid values: ecs (default): an ECS instance. eni: an ENI. ServerIp: Specify the IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   | "test-113" }] |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-2ze7o5h52g02kkzz**** | The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-2zej4lxhjoq1icu**** | The ID of the ECS instance or ENI. |
| Weight | String | 100 | The weight of the backend server. Valid values: 0 to 100. Default value: 100. If the value is set to 0, the SLB instance does not forward requests to the backend server. |
| Description | String | BackendServer | The description of the backend server. |
| RequestId | String | 34B82C81-F13B-4EEB-99F6- A048C67CC830 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=AddBackendServers &LoadBalancerId=lb-2ze7o5h52g02kkzz****
```

Sample success responses

| XML | format |
|---|---|
| <AddBackendServersResponse> <BackendServers> <BackendServer> <ServerId>i-2zej4lxhjoq1icu*****</ServerId> <Weight>100</Weight> <Type>ecs</Type> </BackendServer> <BackendServer> <ServerId>i-2ze1u9ywulp5pbv*****</ServerId> <Weight>100</Weight> <Type>ecs</Type> </BackendServer> </BackendServers> <RequestId>34B82C81-F13B-4EEB-99F6-A048C67CC830</RequestId> <LoadBalancerId>lb-2ze7o5h52g02kkzz*****</LoadBalancerId> </AddBackendServersResponse> |   |

`{`

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

`]` `},`

```json
        "RequestId": "34B82C81-F13B-4EEB-99F6-A048C67CC830",
        "LoadBalancerId": "lb-2ze7o5h52g02kkzz*****"
```

#### 7.9.2 RemoveBackendServers

Removes backend servers.

> **Note:** If the backend server that you want to remove does not belong to the specified Server Load Balancer (SLB) instance, the request fails. However, the system does not report an error.

| Parameter | Type | Required |   |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|---|
| Action | String | Yes |   |   | RemoveBackendServers | The operation that you want to perform. Set the value to RemoveBackendServers. |   |   |
| BackendServers | String | Yes |   |   | [{"ServerId":"i- 2zej4lxhjoq****", "Type": "ecs","Weight":"100"}] | The backend servers to be removed. Valid values: ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Type: Specify the type of the backend server. Valid values: ecs: an Elastic Compute Service (ECS) instance. This is the default value. eni: an elastic network interface (ENI). Note You can remove up to 20 backend servers in each call. Examples: ECS: [{"ServerId":"i- 2zej 4lxhjoq ***", |   |   |
|   |   |   |   |   |   |   | [{"ServerId":"i- 2zej 4lxhjoq ***", |   |
|   |   |   |   |   |   | "Type": "ecs","Weight":"100"}] |   |   |
|   |   |   |   |   |   | ENI: | [{"ServerId":"eni- 2ze 1sdp |   |
|   |   |   |   |   |   | 5***","Type": "eni","Weight":"100"}] |   |   |
| LoadBalancerId | String | Yes |   |   | lb-bp1qjwo61pqz3ahl**** | The ID of the SLB instance. |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-bp1vjkb671z53**** | The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |

| ServerId | String | i-jjgjgjgggd**** | The ID of the backend server. |
|---|---|---|---|
| Weight | Integer | 100 | The weight of the backend server. Valid values: 0 to 100. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=RemoveBackendServers &BackendServers=[{"ServerId":"i-2zej4lxhjoq****", "Type": "ecs","Weight":"100"}] &LoadBalancerId=lb-bp1qjwo61pqz3ahl****
```

Sample success responses

| XML | format |
|---|---|
| <RemoveBackendServersResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <LoadBalancerId>lb-bp1vjkb671z53cy******</LoadBalancerId> <BackendServers> <BackendServer> <ServerId>i-jjgjgjg*****</ServerId> <Weight>100</Weight> </BackendServer> <BackendServer> <ServerId>i-jjgjgituitu****</ServerId> <Weight>100</Weight> </BackendServer> </BackendServers> </RemoveBackendServersResponse> |   |

| JSON | format |
|---|---|
| { "RemoveBackendServers": { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "LoadBalancerId": "lb-bp1vjkb671z53cy******", "BackendServers": { "BackendServer": [ { "ServerId": "i-jjgjgjg*****", "Weight": 100 }, { "ServerId": "i-jjgjgituitu****", "Weight": 100 } ] } } } |   |

#### 7.9.3 SetBackendServers

Sets the weights of backend servers.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetBackendServers | The operation that you want to perform. Set the value to SetBackendServers. |
| LoadBalancerId | String | Yes | lb-bp1qjwo61pqz3a**** | The ID of the Server Load Balancer (SLB) instance. |

|   | BackendServers |   |   | String | Yes |   |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description": "test-112" }] |   | The list of backend servers that you want to add to the SLB instance. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. Type: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: Specify the IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-bp1qjwo61pqz3a**** | The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | eni-hg231**** | The ID of the ECS instance. |
| Weight | String | 100 | The weight of the backend server. |
| Description | String | BackendServer | The description of the backend server. |

| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetBackendServers &LoadBalancerId=lb-bp1qjwo61pqz3a****
```

Sample success responses

| XML | format |
|---|---|
| <SetBackendServersResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <LoadBalancerId>lb-dhf13*******</LoadBalancerId> <BackendServers> <BackendServer> <ServerId>eni-hg231**</ServerId> <Weight>100</Weight> <Type>eni</Type> </BackendServer> <BackendServer> <ServerId>eni-hfhf***</ServerId> <Weight>100</Weight> <Type>eni</Type> </BackendServer> </BackendServers> </SetBackendServersResponse> |   |

| JSON | format |
|---|---|
| { "SetBackendServersResponse": { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "LoadBalancerId": "lb-dhf13*******", "BackendServers": { "BackendServer": [ { "ServerId": "eni-hg231**", "Weight": 100, "Type": "eni" }, { "ServerId": "eni-hfhf***", "Weight": 100, "Type": "eni" } ] } } } |   |

### 7.10 vServer groups

#### 7.10.1 CreateVServerGroup

Creates a vServer group and adds backend servers to the vServer group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVServerGroup | The operation that you want to perform. Set the value to CreateVServerGroup. |

|   | LoadBalancerId |   |   | String | Yes |   |   | lb-bp1qjwo61pqz3ahl**** |   | The ID of the Server Load Balancer (SLB) instance. |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | RegionId |   |   | String | Yes |   |   | cn-qingdao-env17-d01 |   | The ID of the region where the SLB instance is deployed. |   |   |   |   |
|   | VServerGroupName |   |   | String | No |   |   | Group1 |   | The name of the vServer group. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). _ |   |   |   |   |
|   | BackendServers |   |   | String | No |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description": "test-112" }, { "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description": "test-112" }] |   | The list of backend servers to be added. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements in a list for each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. Type: Required. Specify the type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-2**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

| Description | String | vServerGroup | The description of the vServer group. |
|---|---|---|---|
| ServerType | String | ECS |   |
| Type | String | Type | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateVServerGroup &LoadBalancerId=lb-bp1qjwo61pqz3ahl**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <CreateVServerGroupResponse> <VServerGroupId>rsp-bp1i4c******</VServerGroupId> <RequestId>3EBBDBAE-8E8B-438F-A109-95C2FDB2C333</RequestId> <BackendServers> <BackendServer> <Type>ecs</Type> <ServerId>i-bp1ds2yjlk66********</ServerId> <Description>test-11244</Description> <Port>80</Port> <Weight>100</Weight> </BackendServer> </BackendServers> </CreateVServerGroupResponse> |   |

| JSON | format |
|---|---|
| { "VServerGroupId": "rsp-bp1i4c3******", "RequestId": "3EBBDBAE-8E8B-438F-A109-95C2FDB2C333", "BackendServers": { "BackendServer": [ { "Type": "ecs", "ServerId": "i-bp1ds2yjlk666******", "Description": "test-11244", "Port": 80, "Weight": 100 } ] } } |   |

#### 7.10.2 SetVServerGroupAttribute

Modifies the configurations of a vServer group. You can call the operation to modify only configurations such as the weight and port of a backend server.

| pecified vServer group, call the | ModifyVServerGroupBackendServers |   |
|---|---|---|
| AddVServerGroupBackendServers |   | operation. |

If you want to add backend servers, call the `AddVServerGroupBackendServers` operation.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetVServerGroupAttribut e | The operation that you want to perform. Set the value to SetVServerGroupAttribute. |

|   | RegionId |   |   | String | Yes |   |   | cn-qingdao-env17-d01 |   | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | VServerGroupId |   |   | String | Yes |   |   | rsp-cige6**** |   | The ID of the vServer group. |   |   |   |   |
|   | VServerGroupName |   |   | String | No |   |   | vserver-group-test |   | The name of the vServer group. |   |   |   |   |
|   | BackendServers |   |   | String | No |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description": "test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description": "test-113" }] |   | The backend servers in the vServer group. You can add up to 20 backend servers in each call. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. Type: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupName | String | Group1 | The name of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-bp1ek6yd7jvkx**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescription. | The description of the vServer group. |

| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

Sample success responses

| XML | format |
|---|---|
| <SetVServerGroupAttributeResponse> <BackendServers> <BackendServer> <ServerId>i-bp1ek6yd7jvkx*****</ServerId> <Port>80</Port> <Weight>100</Weight> <Type>ecs</Type> </BackendServer> </BackendServers> <RequestId>A4FDF333-F904-4540-88FC-ED6F87AEFFCB</RequestId> <VServerGroupId>rsp-bp1d2e3*****</VServerGroupId> <VServerGroupName>test1</VServerGroupName> </SetVServerGroupAttributeResponse> |   |

| JSON | format |
|---|---|
| { "SetVServerGroupAttributeResponse": { "BackendServers": { "BackendServer": { "ServerId": "i-bp1ek6yd7jvkx*****", "Port": 80, "Weight": 100, "Type": "ecs" } }, "RequestId": "A4FDF333-F904-4540-88FC-ED6F87AEFFCB", "VServerGroupId": "rsp-bp1d2e3*****", "VServerGroupName": "test1" } } |   |

#### 7.10.3 AddVServerGroupBackendServers

Adds backend servers to a specified vServer group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddVServerGroupBacken dServers | The operation that you want to perform. Set the value to AddVServerGroupBackendServers. |

|   | BackendServers |   |   | String | Yes |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6*", "Port":"80","Description": "test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description": "test-113" }] |   | The list of backend servers that you want to add to the vServer group. You can specify up to 20 backend servers in each request. The following parameters are used to specify the backend servers: ServerId: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). Port: Required. The port that is used by the backend server. Valid values: 1 to 65535. Weight: The weight of the backend server. Valid values: 0 to 100. Default value: 100. If the value is set to 0, no requests are forwarded to the backend server. Type: The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. Description: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |
|   | RegionId |   |   | String | Yes |   |   | cn-qingdao-env17-d01 |   | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |   |   |   |   |
|   | VServerGroupId |   |   | String | Yes |   |   | rsp-cige6**** |   | The ID of the vServer group. |   |   |   |   |

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
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```json
http(s)://[Endpoint]/?Action=AddVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }] &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

Sample success responses

| XML | format |
|---|---|
| <AddVServerGroupBackendServersResponse> <VServerGroupId>rsp-cige6j******</VServerGroupId> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <BackendServers> <Type>ecs</Type> <Description>test</Description> <ServerId>vm-231</ServerId> <Weight>100</Weight> <Port>70</Port> </BackendServers> </AddVServerGroupBackendServersResponse> |   |

| JSON | format |
|---|---|
| {"VServerGroupId":"rsp-cige6j******", "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "BackendServers":[ {"Type":"ecs","Description":"test","ServerId":"vm-231","Weight":"100","Port":"70"} ] } |   |

#### 7.10.4 RemoveVServerGroupBackendServers

Removes a backend server from a specified vServer group.

> **Note:** If one or more backend servers specified by **BackendServers** do not exist in the vServer group, the backend servers are ignored and no error message is returned.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveVServerGroupBa ckendServers | The operation that you want to perform. Set the value to RemoveVServerGroupBackendServers. |

| BackendServers | String | Yes | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description": "test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description": "test-113" }] | The list of backend servers that you want to remove from the vServer group. You can specify at most 20 backend servers for a vServer group in each call. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. Type: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. ServerIp: Specify the IP address of the ECS instance or ENI. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-230 | The ID of the ECS instance or ENI. |
| Port | Integer | 80 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```json
http(s)://[Endpoint]/?Action=RemoveVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }] &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

Sample success responses

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

| JSON | format |
|---|---|
| { "RemoveVServerGroupBackendServersResponse": { "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "VServerGroupId": "rsp-cige6******", "BackendServers": { "BackendServer": { "ServerId": "vm-231", "Port": "70", "Weight": "100", "Type": "ecs" } } } } |   |

#### 7.10.5 ModifyVServerGroupBackendServers

Replaces backend servers in a specified vServer group. You can call this operation to replace the backend servers in a specified vServer group. To modify the configurations of the backend servers, such as their weights, you can call the `SetVServerGroupAttribute` operation.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVServerGroupBack endServers | The operation that you want to perform. Set the value to ModifyVServerGroupBackendServers. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6j**** | The ID of the vServer group. |

|   | OldBackendServers |   |   | String | No |   |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Description": "test-112" }] |   | The list of backend servers to be replaced. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. Specify the description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese _ characters. Type: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an ENI ServerIp: Specify the IP address of the ECS instance or ENI Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |

|   | NewBackendServers |   |   | String | No |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description": "test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description": "test-113" }] |   | The list of backend servers to be added. You can specify at most 20 backend servers for a vServer group in each call. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. The description of the backend server. This parameter must be of the STRING type. It can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). It can also contain Chinese characters. _ Type: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI ServerIp: the IP address of the ECS instance or ENI Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI with multiple IP addresses: |   | [{ "ServerId": |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni", "ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-112" },{ |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "172.166.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","Description":"test-113" }] |   |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-236 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=ModifyVServerGroupBackendServers &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j****
```

Sample success responses

| XML | format |
|---|---|
| <ModifyVServerGroupBackendServersResponse> <VServerGroupId>rsp-cige6j******</VServerGroupId> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <BackendServers> <ServerId>vm-236</ServerId> <Weight>100</Weight> <Port>70</Port> </BackendServers> </ModifyVServerGroupBackendServersResponse> |   |

| JSON | format |
|---|---|
| { "ModifyVServerGroupBackendServersResponse": { "VServerGroupId": "rsp-cige6j******", "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "BackendServers": { "ServerId": "vm-236", "Weight": 100, "Port": 70 } } } |   |

#### 7.10.6 DeleteVServerGroup

Deletes a vServer group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVServerGroup | The operation that you want to perform. Set the value to DeleteVServerGroup. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6j**** | The ID of the vServer group. Note You cannot delete a vServer group that is in use. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DeleteVServerGroup &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j****
```

Sample success responses

| XML | format |
|---|---|
| <DeleteVServerGroupResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> </DeleteVServerGroupResponse> |   |

`{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

#### 7.10.7 DescribeVServerGroups

Queries the vServer groups of a Server Load Balancer (SLB) instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerGroups | The operation that you want to perform. Set the value to DescribeVServerGroups. |
| LoadBalancerId | String | Yes | lb-bp1o94dp5i6ea**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroups | Array of VServerGroup |   | The list of backend servers. |
| VServerGroup |   |   |   |
| VServerGroupId | String | rsp-bp1oygn**** | The ID of the vServer group. |
| VServerGroupName | String | k8s/31065/nginx-ingress- lb/kube-system/clust****" | The name of the vServer group. |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeVServerGroups &LoadBalancerId=lb-bp1o94dp5i6ea**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

```xml
<DescribeVServerGroupsResponse>
  <VServerGroups>
        <VServerGroup>
              <VServerGroupId>rsp-bp1oygn******</VServerGroupId>
              <VServerGroupName>k8s/31065/nginx-ingress-lb/kube-system/clust****</VServerGroupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1i6sn******</VServerGroupId>
              <VServerGroupName>k8s/31605/nginx-ingress-lb/kube-system/clusterid</VServerGroupName>
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

`{`

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

`},` `{`

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

`},` `{`

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

`]` `},`

```json
 "RequestId": "31ADDBCD-275F-4C37-B0A3-5DFC8564E686"
```

#### 7.10.8 DescribeVServerGroupAttribute

Queries detailed information about a vServer group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerGroupAtt ribute | The operation that you want to perform. Set the value to DescribeVServerGroupAttribute. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupName | String | Group1 | The name of the vServer group. The name is 1 to 80 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). _ |

| BackendServers | Array of BackendServer |   | The list of backend servers. |
|---|---|---|---|
| BackendServer |   |   |   |
| ServerId | String | vm-233 | The ID of the Elastic Compute Service (ECS) instance. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescription. | The description of the vServer group. |
| ServerType | String | ecs |   |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6****
```

Sample success responses

| XML | format |
|---|---|
| <DescribeVServerGroupAttributeResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <VServerGroupId>rsp-cige6******</VServerGroupId> <VServerGroupName>Group1</VServerGroupName> <BackendServers> <BackendServer> <ServerId>vm-232</ServerId> <Port>80</Port> <Weight>100</Weight> </BackendServer> <BackendServer> <ServerId>vm-233</ServerId> <Port>90</Port> <Weight>100</Weight> </BackendServer> </BackendServers> </DescribeVServerGroupAttributeResponse> |   |

| JSON | format |
|---|---|
| {"VServerGroupId":"rsp-cige6*****","RequestId":"9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C","VServerGroupName":"Group1","BackendServers":[{"ServerType":"ecs","Type":"ecs","ServerId":"vm- 233","Description":"vServerGroupDescription.","VpcId":"vpc-**","Port":"90","ServerIp":"192.168.*.*","Weight":"100"}]} |   |

### 7.11 Primary/secondary server groups

#### 7.11.1 CreateMasterSlaveServerGroup

Creates a primary/secondary server group. A primary/secondary server group contains only two Elastic Compute Service (ECS) instances. One of the ECS instances serves as the primary server. The other ECS instance serves as the secondary server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| 148 |   |   |   | > Document Version: 20241105 |
|---|---|---|---|---|

| Server Load Balanc | er |   |   | Developer Guide·API Reference |
|---|---|---|---|---|

| Action | String | Yes | CreateMasterSlaveServer Group | The operation that you want to perform. Set the value to CreateMasterSlaveServerGroup. |
|---|---|---|---|---|
| LoadBalancerId | String | Yes | lb-bp1hv944r69al4j**** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |
| MasterSlaveServerGroup Name | String | No | sg-atstuj3rtopty**** | The name of the primary/secondary server group. |

|   | MasterSlaveBackendServ ers |   |   | String | No |   |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","ServerType": "Master","Description":"t est-112" }, { "ServerId": "i-xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","ServerType": "Slave","Description":"tes t-112" }] |   | The list of backend servers in the primary/secondary server group. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each call. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port: Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight: Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Description: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). The description can contain Chinese _ characters. ServerType: Specify the type of the backend server. This parameter must be of the STRING type. Valid values: Master: primary server Slave: secondary server Type: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an elastic network interface (ENI) ServerIp: the IP address of the ECS instance or ENI. A primary/secondary server group can contain at most two backend servers. If you do not set this parameter, an empty primary/secondary server group is created. Examples: ECS: [{ "ServerId": "i-xxxxxxxxx", |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","ServerType":"Master","Description |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ":"test-112" }, |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | { "ServerId": "i-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "ecs", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","ServerType":"Slave","Description" |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | :"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxxxxxx", |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Weight": "100", "Type": "eni", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","ServerType":"Master","Description |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ":"test-112" }, |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | { "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni", "ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","ServerType":"Slave","Description" |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | :"test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | [{ "ServerId": |   |
|   |   |   |   |   |   |   |   |   |   | "eni-xxxxxxxxx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "eni","ServerIp": "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","ServerType":"Master","Description |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ":"test-112" }, |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | { "ServerId": "eni-xxxxxxxxx", "Weight": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "100", "Type": "eni","ServerIp": |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "192.168.**.**", |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | "Port":"80","ServerType":"Slave","Description" |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | :"test-112" }] |   |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveServerGro upId | String | rsp-cige6j**** | The ID of the primary/secondary server group. |
| MasterSlaveBackendS ervers | Array of MasterSlaveBackendS erver |   | The list of backend servers in the primary/secondary server group. |

| MasterSlaveBackendS erver |   |   |   |
|---|---|---|---|
| ServerId | String | vm-2h**** | The ID of the ECS instance or ENI that is added. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| ServerType | String | Slave | Indicates whether the backend server is a primary or secondary server. Valid values: Master and Slave. Default value: Master. |
| Description | String | Primary/SecondaryServerGro upDescription. | The description of the primary/secondary server group. The description is 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (). _ |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=CreateMasterSlaveServerGroup &LoadBalancerId=lb-bp1hv944r69al4j**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <CreateMasterSlaveServerGroupResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <MasterSlaveServerGroupId>rsp-cige******</MasterSlaveServerGroupId> <MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-gtgt***</ServerId> <Port>80</Port> <Weight>100</Weight> <ServerType>Master</ServerType> </MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-tygtyg****</ServerId> <Port>90</Port> <Weight>100</Weight> <ServerType>Slave</ServerType> </MasterSlaveBackendServers> </MasterSlaveBackendServers> </CreateMasterSlaveServerGroupResponse> |   |

`{`

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

`]`

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | BACKENDSERVERSNUM M _ _ _ USTBETWO _ _ | Backend servers num must be 2. | The error message returned because two backend servers must be specified. |
| 400 | BACKENDSERVERSHAVES _ _ _ AMEPORTANDSERVERID _ _ _ | Backend servers have same port and serverId. | The error message returned because a backend server with the same port and ID is already specified in the server group. |
| 400 | BACKENDSERVERSCANON _ _ _ LYCONTAINONEMASTERA _ _ _ _ NDONESLAVE _ _ | Backend servers can only contain one master and one slave. | The error message returned because a primary/secondary server group can contain only one primary server and one secondary server. |
| 400 | BACKENDSERVERIDCANN _ _ _ _ OTEMPTY _ | Backend server id can not empty. | The error message returned because the ID of the backend server is not specified. |
| 400 | INVALIDSERVERTYPE _ _ | Invalid server type. | The error message returned because the specified type of backend server is invalid. |
| 400 | BACKENDSERVERPORTCA _ _ _ NNOTEMPTY _ _ | Backend server port can not empty. | The error message returned because the port of the backend server is not specified. |
| 400 | RealServerPortNotSupport | Real server port not support. | The error message returned because the specified port of the backend server is invalid. |

#### 7.11.2 DeleteMasterSlaveServerGroup

Deletes a specified primary/secondary server group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMasterSlaveServer Group | The operation that you want to perform. Set the value to DeleteMasterSlaveServerGroup. |
| MasterSlaveServerGroupI d | String | Yes | rsp-cige6**** | The ID of the primary/secondary server group. Note You cannot delete a primary/secondary server group that is in use. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |
|---|---|---|---|

```
http(s)://[Endpoint]/?Action=DeleteMasterSlaveServerGroup &MasterSlaveServerGroupId=rsp-cige6**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <DeleteMasterSlaveServerGroupResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> </DeleteMasterSlaveServerGroupResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C" } |   |

#### 7.11.3 DescribeMasterSlaveServerGroups

Queries backend servers in a primary/secondary server group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSlaveServ erGroups | The operation that you want to perform. Set the value to DescribeMasterSlaveServerGroups. |
| LoadBalancerId | String | Yes | lb-bp14zi0n66zpg6o**** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveServerGro ups | Array of MasterSlaveServerGro up |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveServerGro up |   |   |   |
| MasterSlaveServerGro upId | String | rsp-0bfuc**** | The ID of the primary/secondary server group. |
| MasterSlaveServerGro upName | String | Group3 | The name of the primary/secondary server group. |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroups &LoadBalancerId=lb-bp14zi0n66zpg6o**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <DescribeMasterSlaveServerGroupsResponse> <RequestId>2631BB5E-B576-4925-BDED-07A66D23E5DE</RequestId> <MasterSlaveServerGroups> <MasterSlaveServerGroup> <MasterSlaveServerGroupId>rsp-bp1ro3mw******</MasterSlaveServerGroupId> <MasterSlaveServerGroupName>test</MasterSlaveServerGroupName> </MasterSlaveServerGroup> </MasterSlaveServerGroups> </DescribeMasterSlaveServerGroupsResponse> |   |

| JSON | format |
|---|---|
| { "RequestId": "265989FE-136B-4D6A-B549-FD40E7", "MasterSlaveServerGroups": { "MasterSlaveServerGroup": [ { "MasterSlaveServerGroupId": "rsp-bp1nly******", "MasterSlaveServerGroupName": "primary/secondary1", "AssociatedObjects": { "Listeners": { "Listener": [ ] } } } ] } } |   |

#### 7.11.4 DescribeMasterSlaveServerGroupAttribute

Queries detailed information about a primary/secondary server group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSlaveServ erGroupAttribute | The operation that you want to perform. Set the value to DescribeMasterSlaveServerGroupAttribute. |
| MasterSlaveServerGroupI d | String | Yes | rsp-cige6j**** | The ID of the primary/secondary server group. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveServerGro upId | String | rsp-cige6**** | The ID of the primary/secondary server group. |
| MasterSlaveServerGro upName | String | Group1 | The name of the primary/secondary server group. |
| MasterSlaveBackendS ervers | Array of MasterSlaveBackendS erver |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveBackendS erver |   |   |   |
| ServerId | String | vm-hrf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

| ServerType | String | Slave | The type of backend server. Valid values: Master and Slave. Default value: Master. |
|---|---|---|---|
| Description | String | Primary/SecondaryServerGro upDescription. | The description of the primary/secondary server group. |
| Type | String | ecs | The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |
| RequestId | String | 9DEC9C28-AB05-4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroupAttribute &MasterSlaveServerGroupId=rsp-cige6j**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

| XML | format |
|---|---|
| <DescribeMasterSlaveServerGroupAttributeResponse> <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId> <MasterSlaveServerGroupId>rsp-cige6******</MasterSlaveServerGroupId> <MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-sshssh****</ServerId> <Port>80</Port> <Weight>100</Weight> <ServerType>Master</ServerType> </MasterSlaveBackendServers> <MasterSlaveBackendServers> <ServerId>vm-ffff*****</ServerId> <Port>90</Port> <Weight>100</Weight> <ServerType>Slave</ServerType> </MasterSlaveBackendServers> </MasterSlaveBackendServers> </DescribeMasterSlaveServerGroupAttributeResponse> |   |

| JSON | format |
|---|---|
| { "DescribeMasterSlaveServerGroupAttributeResponse": { "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "MasterSlaveServerGroupId": "rsp-cige6******", "MasterSlaveBackendServers": { "MasterSlaveBackendServers": [ { "ServerId": "vm-sshssh****", "Port": "80", "Weight": "100", "ServerType": "Master" }, { "ServerId": "vm-ffff*****", "Port": "90", "Weight": "100", "ServerType": "Slave" } ] } } } |   |

### 7.12 Tags

#### 7.12.1 AddTags

Adds tags to a Server Load Balancer (SLB) instance. When you call this operation, take note of the following items: You can add at most 10 tags to an SLB instance. You can specify at most five tags in each request. All tags and keys added to an SLB instance must be unique. If you add a tag that has the same key as an existing tag but with a different value, the new tag overwrites the existing tag.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddTags | The operation that you want to perform. Set the value to AddTags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |
| Tags | String | Yes | [{"TagKey":"Key1","TagV alue":"Value1"}, {"TagKey":"Key2","TagV alue":"Value2"}] | The list of tags to be added. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=AddTags &LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}]
```

Sample success responses

| XML | format |
|---|---|
| <AddTagsResponse> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> </AddTagsResponse> |   |

| JSON | format |
|---|---|
| { "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710" } |   |

#### 7.12.2 DescribeTags

Queries a list of tags. When you call this operation, take note of the following items: You can query tags by instance ID, tag key, and tag value. If the operation is successful, the system returns all tags that match the specified conditions. If the logical relationship among the specified conditions is `AND` , only tags that match all of the specified conditions are returned. If the Tagkey parameter is specified and the Tagvalue parameter is not specified, all tags that contain the specified tag key are returned. If you have specified the Tagvalue parameter in a request, you must also specify the Tagkey parameter in this request. If you specify both the Tagkey and Tagvalue parameters, tags with the specified key-value pair are returned.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTags | The operation that you want to perform. Set the value to DescribeTags. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |
| Tags | String | No | [{"TagKey":"Key1","TagV alue":"Value1"}, {"TagKey":"Key2","TagV alue":"Value2"}] | The list of tags to be queried. |
| DistinctKey | Boolean | No | false | Specifies whether the tag is DistinctKey. Valid values: true and false. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | No | 1 | The number of the page to return. Minimum value: 1. Default value: 1. |

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
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=DescribeTags &RegionId=cn-qingdao-env17-d01
```

Sample success responses

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

| JSON | format |
|---|---|
| { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710", "TagSets": { "TagSet": [ { "TagKey": "test", "TagValue": "api" } ], "PageNumber": 1, "PageSize": 50, "TotalCount": 1 } } |   |

#### 7.12.3 RemoveTags

Removes tags from a Server Load Balancer (SLB) instance.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveTags | The operation that you want to perform. Set the value to RemoveTags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08ex**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao-env17-d01 | The ID of the region where the SLB instance is deployed. |
| Tags | String | Yes | [{"TagKey":"Key1","TagV alue":"Value1"}, {"TagKey":"Key2","TagV alue":"Value2"}] | The list of tags that you want to remove. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=RemoveTags &LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}]
```

Sample success responses

```xml
<RemoveTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</RemoveTagsResponse>
```

| JSON | format |
|---|---|
| { "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710" } |   |

### 7.13 Error codes

|   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   | CertificateAndPrivateKeyIsRe |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | The error message returned because the certificate is used by other resources. |   |
|   |   |   |   |   |   | CertificateAndPrivateKeyIsRe |   |   |   |   |   |   |   |   |   |   | Ce | rtificate and |   |   | 400 |   |   |
|   |   |   |   |   | fered |   |   |   |   |   |   |   |   |   |   | PrivateKey Is Refered. |   |   |   |   |   |   |   |
|   |   |   |   |   | CertificateNotMatchPrivateKe |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | The error message returned because the certificate and the private key do not match. |   |
|   |   |   |   |   |   | CertificateNotMatchPrivateKe |   |   |   |   |   |   |   |   |   |   | Certificate and key |   |   |   | 400 |   |   |
|   |   |   |   |   | y |   |   |   |   |   |   |   |   |   |   | does not match. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health-checked |   |   |   |   |   | The error message returned because health checks are disabled. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health-checked |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Listener to the specified |   |   |   |   |   |   |   |
|   |   |   |   |   |   | CheckedListenerNotFound |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not authorized to |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not authorized to |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the specified |   |   |   |   |   |   |   |
|   |   |   |   |   | Forbbiden.SubUser |   |   |   |   |   |   |   |   |   |   | resource as your |   |   |   |   | 403 | The error message retur |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | account |   |   |   |   |   | unau |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is created by another |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | user. |   |   |   |   |   |   |   |
|   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   | User not authorized to |   |   |   |   |   | The error message returned because you are unauthorized to perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not authorized to |   |   |   |   |   |   |
|   |   |   |   |   |   |   | den |   |   |   |   |   |   |   |   | operate on the specified |   |   |   |   | 403 | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource. |   |   |   |   |   |   |   |
|   |   |   |   |   | IncorrectListenerAccessContr |   |   |   |   |   |   |   |   |   |   | Current listener access |   |   |   |   |   | The error message returned because the access control configuration of the listener is in a state that does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Current listener access |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | control statu |   |   |   | s does not |   |   |   |
|   |   |   |   |   | olStatusStatus |   |   |   |   |   |   |   |   |   |   | support this |   |   |   |   | 500 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operation. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request processing |   |   |   |   |   | The error message returned because an internal error occurred. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request processing |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has failed due to backend |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InternalError |   |   |   |   |   |   |   |   |   | service |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exception. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request processing |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request processing |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has failed due to some |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InternalInvokeError |   |   |   |   |   |   |   |   |   | unknown error, exception |   |   |   |   | 500 | The er error o |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failure. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified LoadBalancer |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified LoadBalancer |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance's addresstype is |   |   |   |   |   | The error message returned because the network |   |
|   |   |   |   |   |   | InvalidBackendServers.Incons |   |   |   |   |   |   |   |   |   | priva |   |   | te, so it is |   | 400 | types of the Elastic Compute Service (ECS |   |
|   |   |   |   |   | istent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instances and that of |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | forbidden to add ecs vpc |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backendservers for now. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All BackendServers on |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All BackendServers on |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | one Specified |   |   |   |   |   | The error message returned because you ca |   |
|   |   |   |   |   |   | InvalidBackendServers.Incons |   |   |   |   |   |   |   |   |   | LoadB |   |   | alancer have to be |   | 400 | specify both ECS instances i |   |
|   |   |   |   |   | istent |   |   |   |   |   |   |   |   |   |   | in the same |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc or |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | all classic |   |   |   |   |   |   |   |
|   |   |   |   |   | InvalidIdentity |   |   |   |   |   |   |   |   |   |   | The request identity |   |   |   |   |   | The error message returned because you are unauthorized to perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request identity |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidI |   |   | dentity |   |   |   |   |   |   | was not allowed |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operated. |   |   |   |   |   |   |   |

|   |   |   |   |   |   |   | InvalidLoadBalancerId.NotFou |   |   |   |   |   | 404 | The error message returned because the specified SLB instance is invalid. |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | InvalidLoadBalancerId.NotFou |   |   |   | LoadBalancerId does not | 404 |   |   |
|   |   |   |   |   |   |   | nd |   |   |   | exist. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | dParameter |   | ServerCertificate format |   | 404 | T |   |
|   |   |   |   |   |   |   |   |   |   |   | is error. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the certificate is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | ServerCertificateId is |   | 40 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | empty. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the ID of the server certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | dParameter |   | ServerCertificateId is |   | 404 | Th |   |
|   |   |   |   |   |   |   |   |   |   |   | not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | support. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the certificate and the private key are not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | dParameter |   | ServerCertificate or Key |   | 404 | T |   |
|   |   |   |   |   |   |   |   |   |   |   | is empty. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   | 404 | The error message returned because the specified private key is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | key format is error. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | Specified region does |   | 404 | The error message returned because the specified region does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | Specified region does | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | not supported. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | Port is not Integer. |   | 400 | The error message returned because the specified port is invalid. Valid values: 1 to 65535. |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified port is |   | 400 | The error message returned because the specified port is invalid. Valid values: 1 to 65535. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified port is | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified bandwidth |   | 400 | The error message returned because the specified bandwidth limit is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified bandwidth | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | Specified parameter |   | 400 | The error message returned because a specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | Specified parameter | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Check is not valid. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of HealthCheckHttpCode is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | dParameter |   | HealthCheckHttpCode is |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | bandwidth is not valid, |   |   | The error message returned becau |   |
|   |   |   |   |   |   |   |   | InvalidParameter |   |   | out of the instance |   | 400 | value |   |
|   |   |   |   |   |   |   |   |   |   |   | total |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | bandwidth. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of Bandwidth is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | bandwidth is not valid. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified health check configuration is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | HealthCheck is not |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of SourceItem is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | SourceItem is not valid. |   | 400 |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified protocol |   | 400 | The error message returned because the specified protocol type is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified protocol | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | RS Pool is empty. |   | 400 | The error message returned because no backend server is available. |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | RS Pool doesn't exist. |   | 400 | The error message returned because no backend server is available. |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | Illegal user ID. |   | 400 | The error message returned because the user ID is invalid. |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | User ID is null |   | 400 | The error message returned because the user ID is not specified. |   |

|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified type of SLB instance is invalid. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | lb_type is not valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   | 400 | The error message returned because the specified value of Mode is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | mode is not valid.. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of AccessControlStatus is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   |   | dParameter |   | AccessControlStatus is |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | SourceItems is not |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of BackendServers is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | BackendServers is not |   | 4 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | Specified parameter is |   | 400 | The error message returned because a specified parameter is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | Specified parameter is | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   | 400 | The error message returned because the specified value of Domain is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   |   |   |   | Domain is not valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   | 400 | The error message returned because the specified value of URI is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | URI is not valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of Scheduler is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | Scheduler is not valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of ListenerStatus is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | ListenerStatus is not |   | 4 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of PersistenceTimeout is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | PersistenceTimeout is not |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of ConnectPort is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | ConnectPort is not |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of ConnectTimeout is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | ConnectTimeou is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of StickySessionType is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | StickySessionType is not |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of HealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | HealthyThreshold is not |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of UnhealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | UnhealthyThreshold is not |   | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of Interval is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |
|   |   |   |   |   |   |   |   |   |   |   | Interval is not valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of XForwardedFor is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | XForwardedFor is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   | The specified parameter |   |   | The error message returned because the specified value of IsPublicAddress is invalid. |
|   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter |   |   |
|   |   |   |   |   |   |   |   | Invali | dParameter |   | IsPublicAddress is not |   | 40 |   |
|   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   |   |   |   | InvalidRegionId.NotFound |   |   |   | Specified region does not exist. |   | 404 | The error message returned because the specified region is invalid. |

|   |   |   |   |   |   |   |   | InvalidServerId.Malformed |   |   |   |   |   |   |   | A specified server ID |   |   | The error message returned because the ID of the backend server is invalid. |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified server ID |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ServerId.Malformed |   |   |   |   | is not valid, flush |   | 400 | The error me |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | control ip chain |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | fail. |   |   |   |   |
|   |   |   |   |   |   |   |   | InvalidServerId.NotFound |   |   |   |   |   |   |   | The specified server is |   | 400 | The error message returned because the specified backend server is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified server is | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not found. |   |   |   |   |
|   |   |   |   |   |   |   |   | InvalidWeight.Malformed |   |   |   |   |   |   |   | A specified weight is |   | 400 | The error message returned because the specified value of weight is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified weight is | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |
|   |   |   |   |   |   |   |   | IpNotAvailable |   |   |   |   |   |   |   | The specified parameter |   |   | The error message returned because the specified value of Address is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified parameter | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Address is not valid. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | There is already a |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | There is already a |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener bound to the |   |   |   |   |
|   |   |   |   |   |   |   |   | ListenerAlreadyExists |   |   |   |   |   |   |   | port on the specified |   | 400 | The er |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | load |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | balancer. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to the |   |   | The error message returned because the specified listener is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to the |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified port of the |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ListenerNotFound |   |   |   |   |   |   | Load |   | 40 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Cookie that is mandatory |   |   |   |   |
|   |   |   |   |   |   |   |   |   | MissingParameter |   |   |   |   |   |   | for processing this |   | 400 | The error mess parameter is n |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BackendServerPort that is |   |   |   |   |
|   |   |   |   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   | mandatory for processing |   | 400 | The error message returned |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancerId that is |   |   |   |   |
|   |   |   |   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   | mandatory for processing |   | 400 | The error message returned |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | RegionId that is |   |   |   |   |
|   |   |   |   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   | mandatory for processing |   | 400 | The error message returne |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   | The combination of some |   |   | The error message returned because a required parameter is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The combination of some |   |   |   |
|   |   |   |   |   |   |   |   |   | Missin | gParameter |   |   |   |   |   | parameters violates the |   | 40 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | spec. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | OwnerId,OwnerAccount that |   |   |   |   |
|   |   |   |   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   | is mandatory for |   | 403 | The error message returned be |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | OwnerAcco |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing this request |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   | PrivateKeyEncryption |   |   |   |   |   |   |   | Key has Encrypted . |   | 400 | The error message returned because the private key is encrypted. |   |
|   |   |   |   |   |   |   |   | ProcessingSameRequest |   |   |   |   |   |   |   | The same request is |   |   | The error message returned because the same request is being processed. Try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The same request is |   |   |   |
|   |   |   |   |   |   |   |   |   | Processin |   |   | gSameRequest |   |   |   | being processed. Please |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | try later. |   |   |   |   |
|   |   |   |   |   |   |   |   | ServerCertificateId.NotFound |   |   |   |   |   |   |   | Specified |   |   | The error message returned because the specified certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   | ServerCertificateId.NotFound |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificateId does not exist. |   | 404 |   |   |

|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request has failed |   |   |   | The error message returned because the service is unavailable. |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request has failed |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | due to a temporary |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   | failure of the |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | server. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The error message returned because the specified name already exists. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavaila |   |   |   |   | ble |   |   |   |   |   | loadbalancer name has |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | been used. |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   | The error message returned because you cannot create TCP listeners. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loadbalancer doesn't |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | TcpNotSupportForHybridLb |   |   |   |   |   |   |   |   |   |   | support TCP type |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener. |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total number of |   |   |   | The error message returned because you cannot add more than 20 backend servers in each call. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total number of |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | input real servers |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | TooManyBackendServers |   |   |   |   |   |   |   |   |   |   | exceeds max supported |   |   | 400 | Th ad |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number: |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 20. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | TooManyBackendServers |   |   |   |   |   |   |   |   |   |   |   | The backend server |   |   |   | The error message returned because the number of backend servers exceeds the limit. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The backend server |   |   |   |   |
|   |   |   |   |   |   |   |   |   | TooManyBack |   |   | endServers |   |   |   |   |   |   |   | parameter has too many |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | entries. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | UnsupportedOperation |   |   |   |   |   |   |   |   |   |   |   | The Loadbalancer |   |   |   | The error message returned because the specified type of SLB instance does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The Loadbalancer |   |   | T |   |
|   |   |   |   |   |   |   |   |   | UnsupportedO |   |   |   | peration |   |   |   |   |   |   | doesn't support this |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | function. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | UnsupportedOperation |   |   |   |   |   |   |   |   |   |   |   | The specified action is |   |   | 400 | The error message returned because you cannot perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified action is |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not supported. |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified port has |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified port has |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | been assigned one type |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | UnsupportedOperationonfixedp |   |   |   |   |   |   |   |   |   |   | of protoca |   | l, and this | 400 | The error message returned because |   |
|   |   |   |   |   |   |   |   | rotocalport |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the specified |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | protocal doesn't support |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | UnsupportedParameter |   |   |   |   |   |   |   |   |   |   |   | The input parameter is |   |   | 400 | The error message returned because a specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input parameter is |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not unsupported. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   |   |   |   |   |   |   | The vip protocol is not |   |   | 400 | The error message returned because the protocol type of the listener and the protocol type of the backend server do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The vip protocol is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match with Rspool. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | VipTooManyListeners |   |   |   |   |   |   |   |   |   |   |   | The total number of |   |   |   | The error message returned because you cannot add more than 50 listeners in each call. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total number of |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | yListeners |   |   |   |   |   |   |   |   | input listeners exceeds |   |   | 400 | The error message ret |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | max supported number: |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 50. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   | The specified resource |   |   | 400 | The error message returned because the specified resource does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified resource |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | does not exist. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The error message returned because the specified instance is being configured. Try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | ble |   |   |   |   |   | loadbalancer is |   |   | 503 | The error message |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | configuring, please retry |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | later. |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, please |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, please |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | make sure the ECS exists |   |   |   | The error message retur |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   | and the status is |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | running. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   | The specified region |   |   | 503 | The error message returned because the specified region does not support VPCs. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified region |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not support VPC. |   |   |   |   |   |
|   |   |   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   | The specified vpc cloud |   |   |   | The error message returned because the specified VPC is deleted. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified vpc cloud |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance has deleted. |   |   |   |   |   |

## 8 Appendix

### 8.1 STS overview

#### 8.1.1 What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. You do not need to rotate STS tokens when they expire. You can attach policies to STS tokens to create fine-grained permissions on cloud resources based on your business requirements.

#### 8.1.2 AssumeRole

Obtains a Security Token Service (STS) token to assume a Resource Access Management (RAM) role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::123456789012** **:role/adminrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |
| RoleSessionName | String | Yes | alice | The custom name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the API caller. For example, you can specify a username. You can specify RoleSessionName to identify API callers that assume the same RAM role in ActionTrail logs. This allows you to track the users that perform the operations. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | The policy that specifies the permissions of the returned STS token. This allows you to implement more fine- grained access control. Limits: The policy must be 1 to 1,024 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71-4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | N/A | N/A | The STS credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1**** | The AccessKey ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessKeySecret | String | ***************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The STS token. |
| Expiration | String | 2015-04-09T11:52:19Z | The expiration time. |
| AssumedRoleUser | N/A | N/A | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789012****:r ole/adminrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495****:alice | The ID of the temporary identity that you use to assume the RAM role. |

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS credentials.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the credentials.

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
        // Replace "sts.aliyuns.com" with the actual endpoint of the STS API. In most cases, endpoint is in the following
format: sts-vpc.${global:region}.${global:internet-domain}.
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
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

**Sample code**

In this example, the `DescribeZones` operation is called to query the zones of Elastic Compute Service (ECS).

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and the AccessKey secret
obtained in the preceding step. The AccessKey ID and the AccessKey secret are assigned by STS.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "
<yourStsAccessKeySecret>");
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
        // Replace "<yourStsToken>" with the STS token that you obtained in the preceding step.
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

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter.RoleSessionNam e | The parameter RoleSessionName is wrongly formed. | The error message returned because the format of the RoleSessionName parameter is invalid. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (). _ |
| 400 | InvalidParameter.DurationSecond s | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The value must be greater than or equal to 900 and less than or equal to the MaxSessionDuration value. |
| 400 | InvalidParameter.PolicyGrammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the specified policy is invalid. |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |

Developer ners

## 9 DescribeLoadBalancerListeners

Queries the listeners of Server Load Balancer (SLB) instances.

**Prerequisites**

v3.16.2r-slb-SP009 is installed. An SLB instance is created. For more information, see `CreateLoadBalancer` . Listeners are configured for the SLB instance. For more information, see the following topics:

**Usage notes**

For more information about common request parameters, see `Common parameters` of the developer guide.

**Request headers**

This operation uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | No | cn-hangzhou | The ID of the region where the SLB instance is created. You can call the DescribeRegions operation to query the most recent region list. If the endpoint of the region is slb.aliyuncs.com, you must specify RegionId . |
| Action | String | Query | No | DescribeLoadBalancerListeners | The operation that you want to perform. Set the value to DescribeLoadBalancerListeners . |
| OwnerId | Long | Query | No |   |   |
| ResourceOwner Account | String | Query | No |   |   |
| ResourceOwnerI d | Long | Query | No |   |   |
| OwnerAccount | String | Query | No |   |   |
| NextToken | String | Query | No | FFmyTO70tTpLG6I3FmYAXGKPd**** | The pagination token that is used in the next request to retrieve a new page of results. Valid values: You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken. |
| MaxResults | Integer | Query | No | 50 | The number of entries per page. Valid values: 1 to 100 . If you do not specify a value, the default value 20 is used. |
| ListenerProtocol | String | Query | No | http | The listener protocol. Valid values: tcp udp http https |

Developer ners

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| LoadBalancerId | RepeatLis t | Query | No | LoadBalancerId.1=lb- uf6so8u4g35prnvsw****,LoadBalanc erId.2=lb-uf6s1l1kukqv4u5nt**** | The SLB instance IDs. You can specify up to 10 IDs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Listeners | Array |   | The listeners. This parameter is not returned if no listener is configured for the SLB instance. |
| -AclId | String | nacl-a2do9e413e0spzasx**** | The ACL ID. |
| -AclStatus | String | off | Indicates whether access control is enabled. Valid values: on off |
| -AclType | String | white | The type of ACL. Valid values: white : a whitelist. Only requests from the IP addresses or CIDR blocks in the ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application. Your service may be adversely affected if the whitelist is not properly configured. If a whitelist is configured, only requests from the IP addresses that are added to the whitelist are forwarded by the listener. If you enable a whitelist but do not add an IP address to the whitelist, the listener forwards all requests. black : a blacklist. All requests from the IP addresses or CIDR blocks in the ACL are denied. The blacklist applies to scenarios in which you want to deny access from specific IP addresses to an application. If a blacklist is configured for a listener but no IP addresses are added to the blacklist, the listener forwards all requests. |
| -BackendServerPort | Integer | 80 | The port of the backend server. This parameter takes effect only if VServerGroupId and MasterSlaveServerGroupId are empty. |
| -Bandwidth | Integer | -1 | The maximum bandwidth of the listener. Unit: Mbit/s. Valid values: -1 : If -1 is returned, the bandwidth of the listener is unlimited. 1 to 5120 : If a value from 1 to 5120 is returned, the value indicates the maximum bandwidth of the listener. The sum of the maximum bandwidth of all listeners added to an SLB instance does not exceed the maximum bandwidth of the SLB instance. |
| -Description | String | test | The description of the listener. |
| -ListenerPort | Integer | 80 | The listener port. |
| -ListenerProtocol | String | http | The listener protocol. |
| -LoadBalancerId | String | lb-bp1b6c719dfa**** | The SLB instance ID. |

Developer ners

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr : Backend servers with higher weights receive more requests than those with lower weights. rr : Requests are distributed to backend servers in sequence. |
| -Status | String | running | The status of the listener. Valid values: running stopped |
| -VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the listener. |
| -HTTPListenerConfig | Struct |   | The configuration of the HTTP listener. |
| --Cookie | String | B490B5EBF6F3CD402E515D 22BCDA**** | The cookie that is configured on the backend server. |
| --CookieTimeout | Integer | 500 | The timeout period of a cookie. Unit: seconds. Valid values: 1 to 86400 . |
| --ForwardPort | Integer | 80 | The listener port that is used to redirect requests from HTTP to HTTPS. If ListenerForward is set to off , this parameter is not returned. |
| --Gzip | String | on | Indicates whether GZIP compression is enabled. Valid values: on off |
| --HealthCheck | String | on | Indicates whether the health check feature is enabled. Valid values: on off |
| -- HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. This parameter takes effect only if HealthCheck is set to on . |
| --HealthCheckDomain | String | www.example.com | The domain name that is used for health checks. |
| -- HealthCheckHttpCode | String | http2xx,http3xx _ _ | The HTTP status code for a successful health check. |
| -- HealthCheckHttpVersi on | String | HTTP 1.0 | The HTTP version that is used for health checks. |
| --HealthCheckInterval | Integer | 5 | The interval at which you want to perform health checks. Unit: seconds. |
| --HealthCheckMethod | String | get | The health check method. Valid values: head and get . |
| --HealthCheckTimeout | Integer | 3 | The timeout period of a health check. Unit: seconds. |
| --HealthCheckType | String | tcp | The protocol that is used for health checks. |
| --HealthCheckURI | String | /test/index.html | The URI that is used for health checks. |

| Developer Guide·DescribeLo | adBalancerListe |   | Server Load Balancer |
|---|---|---|---|

ners

| Parameter | Type | Example | Description |
|---|---|---|---|
| --HealthyThreshold | Integer | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from fail to success . Valid values: 2 to 10 . |
| --IdleTimeout | Integer | 15 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60 . If no request is received within the specified timeout period, SLB closes the connection. When a request is received, SLB creates a new connection. |
| --ListenerForward | String | on | Indicates whether HTTP-to-HTTPS redirection is enabled. Valid values: on off |
| --RequestTimeout | Integer | 60 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180 . If no response is received from a backend server during the request timeout period, SLB sends the HTTP 504 status code to the client. |
| --StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on off |
| --StickySessionType | String | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client contains the cookie, and the listener forwards the request to the recorded backend server. server : rewrites a cookie. When SLB detects a user- defined cookie, SLB overwrites the original cookie with the user-defined cookie. The next request from the client contains the user-defined cookie, and the listener forwards the request to the recorded backend server. |
| --UnhealthyThreshold | Integer | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from success to fail . Valid values: 2 to 10 . |
| --XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to obtain client IP addresses. Valid values: on off |
| -- XForwardedForClient _ SrcPort | String | on | Indicates whether the XForwardedFor_ClientSrcPort header is used to obtain the client port. Valid values: on off |
| -- XForwardedForSLBID _ | String | on | Indicates whether the SLB-ID header is used to obtain the ID of the SLB instance. Valid values: on off |
| -- XForwardedForSLBIP _ | String | on | Indicates whether the SLB-IP header is used to obtain the virtual IP address (VIP) requested by the client. Valid values: on off |

| Server Load Balan | cer |   | Develope Guide·DescribeLoadBalancerListe ners |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- XForwardedForSLBPO _ RT | String | on | Indicates whether the XForwardedFor_SLBPORT header is used to obtain the listener port of the SLB instance. Valid values: on off |
| --XForwardedForproto _ | String | on | Indicates whether the X-Forwarded-Proto header is used to obtain the listener protocol. Valid values: on off |
| -HTTPSListenerConfig | Struct |   | The configuration of the HTTPS listener. |
| --CACertificateId | String | idkp-234-cn-test-0**** | The ID of the CA certificate. |
| --Cookie | String | B490B5EBF6F3CD402E515D 22BCDA**** | The cookie that is configured on the backend server. |
| --CookieTimeout | Integer | 500 | The timeout period of a cookie. Unit: seconds. Valid values: 1 to 86400 . |
| --EnableHttp2 | String | off | Indicates whether HTTP 2.0 is enabled. Valid values: on off |
| --Gzip | String | on | Indicates whether GZIP compression is enabled. Valid values: on off |
| --HealthCheck | String | on | Indicates whether the health check feature is enabled. Valid values: on off |
| -- HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. |
| --HealthCheckDomain | String | www.example.com | The domain name that is used for health checks. |
| -- HealthCheckHttpCode | String | http2xx,http3xx _ _ | The HTTP status code for a successful health check. |
| -- HealthCheckHttpVersi on | String | HTTP 1.0 | The HTTP version that is used for health checks. |
| --HealthCheckInterval | Integer | 5 | The interval at which the system performs health checks. Unit: seconds. |
| --HealthCheckMethod | String | get | The health check method. |
| --HealthCheckTimeout | Integer | 3 | The maximum timeout period of a health check. Unit: seconds. |
| --HealthCheckType | String | tcp | The protocol that is used for health checks. |
| --HealthCheckURI | String | /test/index.html | The URI that is used for health checks. |

| Developer |   |   |   |
|---|---|---|---|

ners

| Parameter | Type | Example | Description |
|---|---|---|---|
| --HealthyThreshold | Integer | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from fail to success . Valid values: 2 to 10 . |
| --IdleTimeout | Integer | 15 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60 . If no request is received within the specified timeout period, SLB closes the connection. When a request is received, SLB creates a new connection. |
| --RequestTimeout | Integer | 60 | The request timeout period. Unit: seconds. Valid values: 1 to 180 . If no response is received from a backend server during the request timeout period, SLB sends the HTTP 504 status code to the client. |
| --ServerCertificateId | String | idkp-123-cn-test-0**** | The ID of the server certificate. |
| --StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on off |
| --StickySessionType | String | insert | The method that is used to handle a cookie. insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client contains the cookie, and the listener forwards the request to the recorded backend server. server : rewrites a cookie. When SLB detects a user- defined cookie, SLB overwrites the original cookie with the user-defined cookie. The next request from the client contains the user-defined cookie, and the listener forwards the request to the recorded backend server. |

Developer ners

| Parameter | Type | Example | Description |
|---|---|---|---|
| --TLSCipherPolicy | String | tlscipherpolicy10 _ _ _ _ | Each security policy contains TLS protocol versions and cipher suites available for HTTPS. Valid values: tlscipherpolicy10 : _ _ _ _ Supported TLS versions: TLS 1.0, TLS 1.1, and TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256- SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA tlscipherpolicy11 : _ _ _ _ Supported TLS versions: TLS 1.1 and TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256- SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA tlscipherpolicy12 _ _ _ _ Supported TLS version: TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256- SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256- SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA tlscipherpolicy12strict _ _ _ _ _ Supported TLS version: TLS 1.2 Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128- SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA-AES128- SHA, and ECDHE-RSA-AES256-SHA tlscipherpolicy12strictwith13 _ _ _ _ _ _ _ _ Supported TLS versions: TLS 1.2 and TLS 1.3 Supported cipher suites: TLSAES128GCM SHA256, _ _ _ _ TLSAES256GCM SHA384, _ _ _ _ TLSCHACHA20POLY1305SHA256, _ _ _ TLSAES128CCM SHA256, TLSAES128CCM 8SHA256, _ _ _ _ _ _ _ _ _ ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA- AES256-GCM-SHA384, ECDHE-ECDSA-AES128-SHA256, ECDHE-ECDSA-AES256-SHA384, ECDHE-RSA-AES128-GCM- SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA- AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE- ECDSA-AES128-SHA, ECDHE-ECDSA-AES256-SHA, ECDHE- RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA |
| --UnhealthyThreshold | Integer | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from success to fail . Valid values: 2 to 10 . |
| --XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to obtain client IP addresses. Valid values: on off |
| -- XForwardedForClient _ CertClientVerify | String | off | Indicates whether the XForwardedFor_ClientCertClientVerify header is used to obtain the verification result of the client certificate. Valid values: on off |

Developer ners

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- XForwardedForClient _ CertFingerprint | String | off | Indicates whether the XForwardedFor_ClientCertFingerprint header is used to obtain the fingerprint of the client certificate. Valid values: on off |
| -- XForwardedForClient _ CertIssuerDN | String | off | Indicates whether the XForwardedFor_ClientCertIssuerDN header is used to obtain information about the authority that issues the client certificate. Valid values: on off |
| -- XForwardedForClient _ CertSubjectDN | String | off | Indicates whether the XForwardedFor_ClientCertSubjectDN header is used to obtain information about the owner of the client certificate. Valid values: on off |
| -- XForwardedForClient _ SrcPort | String | off | Indicates whether the XForwardedFor_ClientSrcPort header is used to obtain the client port. Valid values: on off |
| -- XForwardedForSLBID _ | String | on | Indicates whether the SLB-ID header is used to obtain the ID of the SLB instance. Valid values: on off |
| -- XForwardedForSLBIP _ | String | on | Indicates whether the SLB-IP header is used to obtain the VIP requested by the client. Valid values: on off |
| -- XForwardedForSLBPO _ RT | String | off | Indicates whether the XForwardedFor_SLBPORT header is used to obtain the listener port. Valid values: on off |
| --XForwardedForproto _ | String | on | Indicates whether the X-Forwarded-Proto header is used to obtain the listener protocol. Valid values: on off |
| -TCPListenerConfig | Struct |   | The configuration of the TCP listener. |
| --ConnectionDrain | String | off | Indicates whether connection draining is enabled. Valid values: on off |
| -- ConnectionDrainTimeo ut | Integer | 300 | The timeout period of connection draining. Unit: seconds. Value values: 10 to 900 . |
| --EstablishedTimeout | Integer | 500 | The timeout period of a connection. Unit: seconds. |

| Server Load Balan | cer |   | Develope Guide·DescribeLoadBalancerListe ners |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --HealthCheck | String | on | Indicates whether the health check feature is enabled. Valid values: on off |
| -- HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. |
| -- HealthCheckConnectTi meout | Integer | 100 | The timeout period of health checks. Unit: seconds. Valid values: 1 to 300 . |
| --HealthCheckDomain | String | www.example.com | The domain name that is used for health checks. |
| -- HealthCheckHttpCode | String | http2xx,http3xx _ _ | The HTTP status code for a successful health check. |
| --HealthCheckInterval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| --HealthCheckMethod | String | get | The health check method. |
| --HealthCheckType | String | tcp | The protocol that is used for health checks. |
| --HealthCheckURI | String | /test/index.html | The URI that is used for health checks. |
| --HealthyThreshold | Integer | 4 | The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from fail to success . Valid values: 2 to 10 . |
| -- MasterSlaveServerGro upId | String | rsp-0bfucw***** | The ID of the primary/secondary server group that is associated with the listener. |
| --PersistenceTimeout | Integer | 0 | Indicates whether session persistence is enabled. Unit: seconds. Valid values: 0 to 3600 . 0 indicates that session persistence is disabled. |
| --UnhealthyThreshold | Integer | 4 | The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from success to fail . Valid values: 2 to 10 . |
| -UDPListenerConfig | Struct |   | The configuration of the UDP listener. |
| --ConnectionDrain | String | off | Indicates whether connection draining is enabled. Valid values: on off |
| -- ConnectionDrainTimeo ut | Integer | 300 | The timeout period of connection draining. Unit: seconds. Valid values: 10 to 900 . |
| --HealthCheck | String | on | Indicates whether the health check feature is enabled. Valid values: on off |

|   | Developer Guide·DescribeLo ners | adBalancerListe |   | Server Load Balancer |   |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- HealthCheckConnectP ort | Integer | 8080 | The port that is used for health checks. |
| -- HealthCheckConnectTi meout | Integer | 100 | The timeout period for a health check response. |
| --HealthCheckExp | String | ok | The response string for UDP listener health checks. |
| --HealthCheckInterval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| --HealthCheckReq | String | hello | The request string for UDP listener health checks. |
| --HealthyThreshold | Integer | 4 | The number of times that a backend server must consecutively pass health checks before it is declared healthy. |
| -- MasterSlaveServerGro upId | String | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |
| --UnhealthyThreshold | Integer | 4 | The number of times that a backend server must consecutively fail health checks before it is declared unhealthy. |
| MaxResults | Integer | 50 | The number of entries per page. Valid values: 1 to 100 . If you do not specify this parameter, the default value 20 is used. |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXG KPd**** | A pagination token. It can be used in the next request to retrieve a new page of results. Valid values: If NextToken is empty, no next page exists. If a value is returned for NextToken , the value is the token that is used for the next query. |
| RequestId | String | 365F4154-92F6-4AE4-92F8- 7FF34B540710 | The request ID. |
| TotalCount | Integer | 10 | The total number of entries returned. |

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerListeners &Common request parameters
```

Sample success responses

| JSON | format |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "Listeners":{ "Status":"running", "ListenerPort":80, "VServerGroupId":"rsp-cige6j****", "Description":"test", "Scheduler":"wrr", "AclId":"nacl-a2do9e413e0spzasx****", "-HTTPListenerConfig":{ "CookieTimeout":500, "UnhealthyThreshold":4, "HealthCheckURI":"/test/index.html", "HealthCheck":"on", "IdleTimeout":15, "XForwardedFor_SLBID":"on", "HealthCheckConnectPort":8080, "XForwardedFor_SLBPORT":"on", |   |

Developer ners

```json
   "HealthCheckMethod":"get",
   "Gzip":"on",
   "StickySessionType":"insert",
   "XForwardedFor_SLBIP":"on",
   "HealthCheckHttpCode":"http_2xx,http_3xx",
   "Cookie":"B490B5EBF6F3CD402E515D22BCDA****",
   "RequestTimeout":60,
   "HealthCheckInterval":5,
   "HealthCheckHttpVersion":"HTTP 1.0",
   "HealthCheckTimeout":3,
   "ListenerForward":"on",
   "StickySession":"on",
   "ForwardPort":80,
   "HealthyThreshold":4,
   "XForwardedFor":"on",
   "XForwardedFor_ClientSrcPort":"on",
   "HealthCheckDomain":"www.example.com",
   "XForwardedFor_proto":"on",
   "HealthCheckType":"tcp"
```

`},`

```json
  "-UDPListenerConfig":{
   "ConnectionDrainTimeout":300,
   "HealthCheckInterval":5,
   "HealthCheckConnectPort":8080,
   "HealthCheckReq":"hello",
   "UnhealthyThreshold":4,
   "HealthCheckExp":"ok",
   "HealthyThreshold":4,
   "HealthCheck":"on",
   "HealthCheckConnectTimeout":100,
   "MasterSlaveServerGroupId":"rsp-0bfucw****",
   "ConnectionDrain":"off"
```

`},`

```json
  "LoadBalancerId":"lb-bp1b6c719dfa****",
  "BackendServerPort":80,
  "ListenerProtocol":"http",
  "-HTTPSListenerConfig":{
   "CookieTimeout":500,
   "UnhealthyThreshold":4,
   "HealthCheckURI":"/test/index.html",
   "HealthCheck":"on",
   "IdleTimeout":15,
   "XForwardedFor_SLBID":"on",
   "HealthCheckConnectPort":8080,
   "XForwardedFor_SLBPORT":"off",
   "HealthCheckMethod":"get",
   "Gzip":"on",
   "ServerCertificateId":"idkp-123-cn-test-0****",
   "StickySessionType":"insert",
   "XForwardedFor_SLBIP":"on",
   "HealthCheckHttpCode":"http_2xx,http_3xx",
   "Cookie":"B490B5EBF6F3CD402E515D22BCDA****",
   "RequestTimeout":60,
   "HealthCheckInterval":5,
   "TLSCipherPolicy":"tls_cipher_policy_1_0",
   "CACertificateId":"idkp-234-cn-test-0****",
   "XForwardedFor_ClientCertSubjectDN":"off",
   "HealthCheckHttpVersion":"HTTP 1.0",
   "HealthCheckTimeout":3,
   "XForwardedFor_ClientCertIssuerDN":"off",
   "StickySession":"on",
   "HealthyThreshold":4,
   "XForwardedFor":"on",
   "XForwardedFor_ClientSrcPort":"off",
   "HealthCheckDomain":"www.example.com",
   "XForwardedFor_proto":"on",
   "EnableHttp2":"off",
   "XForwardedFor_ClientCertClientVerify":"off",
   "XForwardedFor_ClientCertFingerprint":"off",
   "HealthCheckType":"tcp"
```

`},`

```json
  "-TCPListenerConfig":{
   "HealthCheckInterval":5,
   "UnhealthyThreshold":4,
   "HealthCheckURI":"/test/index.html",
   "HealthCheck":"on",
   "HealthCheckConnectTimeout":100,
```

Developer ners

```json
   "ConnectionDrain":"off",
   "ConnectionDrainTimeout":300,
   "PersistenceTimeout":0,
   "HealthCheckConnectPort":8080,
   "HealthCheckMethod":"get",
   "HealthyThreshold":4,
   "HealthCheckDomain":"www.example.com",
   "MasterSlaveServerGroupId":"rsp-0bfucw*****",
   "HealthCheckHttpCode":"http_2xx,http_3xx",
   "HealthCheckType":"tcp",
   "EstablishedTimeout":500
```

`},`

```json
  "AclStatus":"off",
  "Bandwidth":-1,
  "AclType":"white"
```

`},`

```json
 "TotalCount":10,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710",
 "MaxResults":50
```

| XML | format |
|---|---|
| <Listeners> <Status>running</Status> <ListenerPort>80</ListenerPort> <VServerGroupId>rsp-cige6j****</VServerGroupId> <Description>test</Description> <Scheduler>wrr</Scheduler> <AclId>nacl-a2do9e413e0spzasx****</AclId> <-HTTPListenerConfig> <CookieTimeout>500</CookieTimeout> <UnhealthyThreshold>4</UnhealthyThreshold> <HealthCheckURI>/test/index.html</HealthCheckURI> <HealthCheck>on</HealthCheck> <IdleTimeout>15</IdleTimeout> <XForwardedFor_SLBID>on</XForwardedFor_SLBID> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <XForwardedFor_SLBPORT>on</XForwardedFor_SLBPORT> <HealthCheckMethod>get</HealthCheckMethod> <Gzip>on</Gzip> <StickySessionType>insert</StickySessionType> <XForwardedFor_SLBIP>on</XForwardedFor_SLBIP> <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode> <Cookie>B490B5EBF6F3CD402E515D22BCDA****</Cookie> <RequestTimeout>60</RequestTimeout> <HealthCheckInterval>5</HealthCheckInterval> <HealthCheckHttpVersion>HTTP 1.0</HealthCheckHttpVersion> <HealthCheckTimeout>3</HealthCheckTimeout> <ListenerForward>on</ListenerForward> <StickySession>on</StickySession> <ForwardPort>80</ForwardPort> <HealthyThreshold>4</HealthyThreshold> <XForwardedFor>on</XForwardedFor> <XForwardedFor_ClientSrcPort>on</XForwardedFor_ClientSrcPort> <HealthCheckDomain>www.example.com</HealthCheckDomain> <XForwardedFor_proto>on</XForwardedFor_proto> <HealthCheckType>tcp</HealthCheckType> </-HTTPListenerConfig> <-UDPListenerConfig> <ConnectionDrainTimeout>300</ConnectionDrainTimeout> <HealthCheckInterval>5</HealthCheckInterval> <HealthCheckConnectPort>8080</HealthCheckConnectPort> <HealthCheckReq>hello</HealthCheckReq> <UnhealthyThreshold>4</UnhealthyThreshold> <HealthCheckExp>ok</HealthCheckExp> <HealthyThreshold>4</HealthyThreshold> <HealthCheck>on</HealthCheck> <HealthCheckConnectTimeout>100</HealthCheckConnectTimeout> <MasterSlaveServerGroupId>rsp-0bfucw****</MasterSlaveServerGroupId> <ConnectionDrain>off</ConnectionDrain> </-UDPListenerConfig> <LoadBalancerId>lb-bp1b6c719dfa****</LoadBalancerId> <BackendServerPort>80</BackendServerPort> <ListenerProtocol>http</ListenerProtocol> |   |

Developer ners

```xml
 <-HTTPSListenerConfig>
  <CookieTimeout>500</CookieTimeout>
  <UnhealthyThreshold>4</UnhealthyThreshold>
  <HealthCheckURI>/test/index.html</HealthCheckURI>
  <HealthCheck>on</HealthCheck>
  <IdleTimeout>15</IdleTimeout>
  <XForwardedFor_SLBID>on</XForwardedFor_SLBID>
  <HealthCheckConnectPort>8080</HealthCheckConnectPort>
  <XForwardedFor_SLBPORT>off</XForwardedFor_SLBPORT>
  <HealthCheckMethod>get</HealthCheckMethod>
  <Gzip>on</Gzip>
  <ServerCertificateId>idkp-123-cn-test-0****</ServerCertificateId>
  <StickySessionType>insert</StickySessionType>
  <XForwardedFor_SLBIP>on</XForwardedFor_SLBIP>
  <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
  <Cookie>B490B5EBF6F3CD402E515D22BCDA****</Cookie>
  <RequestTimeout>60</RequestTimeout>
  <HealthCheckInterval>5</HealthCheckInterval>
  <TLSCipherPolicy>tls_cipher_policy_1_0</TLSCipherPolicy>
  <CACertificateId>idkp-234-cn-test-0****</CACertificateId>
  <XForwardedFor_ClientCertSubjectDN>off</XForwardedFor_ClientCertSubjectDN>
  <HealthCheckHttpVersion>HTTP 1.0</HealthCheckHttpVersion>
  <HealthCheckTimeout>3</HealthCheckTimeout>
  <XForwardedFor_ClientCertIssuerDN>off</XForwardedFor_ClientCertIssuerDN>
  <StickySession>on</StickySession>
  <HealthyThreshold>4</HealthyThreshold>
  <XForwardedFor>on</XForwardedFor>
  <XForwardedFor_ClientSrcPort>off</XForwardedFor_ClientSrcPort>
  <HealthCheckDomain>www.example.com</HealthCheckDomain>
  <XForwardedFor_proto>on</XForwardedFor_proto>
  <EnableHttp2>off</EnableHttp2>
  <XForwardedFor_ClientCertClientVerify>off</XForwardedFor_ClientCertClientVerify>
  <XForwardedFor_ClientCertFingerprint>off</XForwardedFor_ClientCertFingerprint>
  <HealthCheckType>tcp</HealthCheckType>
 </-HTTPSListenerConfig>
 <-TCPListenerConfig>
  <HealthCheckInterval>5</HealthCheckInterval>
  <UnhealthyThreshold>4</UnhealthyThreshold>
  <HealthCheckURI>/test/index.html</HealthCheckURI>
  <HealthCheck>on</HealthCheck>
  <HealthCheckConnectTimeout>100</HealthCheckConnectTimeout>
  <ConnectionDrain>off</ConnectionDrain>
  <ConnectionDrainTimeout>300</ConnectionDrainTimeout>
  <PersistenceTimeout>0</PersistenceTimeout>
  <HealthCheckConnectPort>8080</HealthCheckConnectPort>
  <HealthCheckMethod>get</HealthCheckMethod>
  <HealthyThreshold>4</HealthyThreshold>
  <HealthCheckDomain>www.example.com</HealthCheckDomain>
  <MasterSlaveServerGroupId>rsp-0bfucw*****</MasterSlaveServerGroupId>
  <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
  <HealthCheckType>tcp</HealthCheckType>
  <EstablishedTimeout>500</EstablishedTimeout>
 </-TCPListenerConfig>
 <AclStatus>off</AclStatus>
 <Bandwidth>-1</Bandwidth>
 <AclType>white</AclType>
</Listeners> <TotalCount>10</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId> <MaxResults>50</MaxResults>
```

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParam.ListenerProtoco l | IllegalParam.ListenerProtocol | The param of ListenerProtocol is illegal. |
| 400 | InvalidParam.PageSize | IllegalParam.MaxResults | The param of MaxResults is illegal. |
| 400 | QueryTokenInvalid | IllegalParam.NextToken | The param of NextToken is illegal. |
| 400 | InvalidParamSize.LoadBalanc erId | IllegalParamSize.LoadBalancerId | The param size of LoadBalancerId is illegal. |

rModificationProtection

## 10 SetLoadBalancerModificationProtection

Enables or disables the configuration read-only mode for a Classic Load Balancer (CLB) instance.

**Prerequisites**

v3.16.2r-slb-hotfeature-SP006 is installed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerModifica tionProtection | Set the value to SetLoadBalancerModifyProtection. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08e***** | The ID of the CLB instance. |
| ModificationProtectionSta tus | String | Yes | ConsoleProtection | Specifies whether to enable the configuration read- only mode for the CLB instance. Valid values: NonProtection: disables the configuration read- only mode. If you set ModificationProtectionStatus to NonProtection, the value of ModificationProtectionReason is cleared. ConsoleProtection: enables the configuration read-only mode. |
| LoadBalancerName | String | No | test1 | The CLB instance name. |
| accesskeyid _ _ | String | No | acc- hp34s2h0xx1ht4nwo**** | The AccessKey ID. |
| Tags | String | No | [{"tagKey":"Key1","tagVa lue":"Value1"}] | The tags that are added to the CLB instance. The tags must be key-value pairs that are contained in a JSON dictionary. You can specify up to 10 tags in each call. |
| ModificationProtectionRe ason | String | No | Modify configurations | The reason for enabling the configuration read-only mode. The value must be 1 to 80 characters in length. It must start with a letter and can contain digits, periods (.), underscores (), and hyphens (-). _ Note This parameter takes effect only if you set ModificationProtectionStatus to ConsoleProtection. |

| Parameter | Type | Example | Details |
|---|---|---|---|
| RequestId | String | 791D8B68-AE0F-4174-AF54- 088C8B3C5D54 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerModificationProtection &LoadBalancerId=lb-bp1b6c719dfa08e***** &ModificationProtectionStatus=ConsoleProtection
```

Sample success responses

| XML | format |
|---|---|
| <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId> |   |

| JSON | format |
|---|---|
| { "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54" } |   |

rModificationProtection

**Error code**

| HttpCode | Error code | Error message | Details |
|---|---|---|---|
| 400 | OperationUnsupported.SetLo adBalancerStatus | The zone of the loadBalancer does not support this operation. | The current CLB instance does not support this operation. |
| 400 | InvalidParam.ModificationPro tectionStatus | The param ModificationProtectionStatus is invalid. | ModificationProtectionStatus is set to an invalid value. Specify a valid value and try again. |
| 400 | InvalidParam.ModificationPro tectionReason | The param ModificationProtectionReason is invalid. | ModificationProtectionReason is set to an invalid value. Specify a valid value and try again. |

rDeleteProtection

## 11 SetLoadBalancerDeleteProtection

Enables or disables deletion protection for a Classic Load Balancer (CLB) instance.

**Prerequisites**

v3.16.2r-slb-hotfeature-SP006 is installed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancerDeletePr otection | The operation that you want to perform. Set the value to SetLoadBalancerDeleteProtection. |
| DeleteProtection | String | Yes | off | Specifies whether to enable deletion protection for the CLB instance. Valid values: on off |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08e***** | The CLB instance ID. |
| LoadBalancerName | String | No | test1 | The CLB instance name. |
| accesskeyid _ _ | String | No | acc- hp34s2h0xx1ht4nwo**** | The AccessKey ID. |
| Tags | String | No | [{"tagKey":"Key1","tagVa lue":"Value1"}] | The tags that are added to the CLB instance. The tags must be key-value pairs that are contained in a JSON dictionary. You can specify up to 10 tags in each call. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 791D8B68-AE0F-4174-AF54- 088C8B3C5D54 | The ID of the request. |

```
http(s)://[Endpoint]/?Action=SetLoadBalancerDeleteProtection &DeleteProtection=off &LoadBalancerId=lb-bp1b6c719dfa08e*****
```

Sample success responses

| XML | format |
|---|---|
| <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId> |   |

| JSON | format |
|---|---|
| { "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54" } |   |

**Error code**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationUnsupported.Delet eProtectionForPrePayInstanc e | The operation failed because prepay instance does not support delete protection. | Deletion protection is not supported by subscription CLB instances. |
