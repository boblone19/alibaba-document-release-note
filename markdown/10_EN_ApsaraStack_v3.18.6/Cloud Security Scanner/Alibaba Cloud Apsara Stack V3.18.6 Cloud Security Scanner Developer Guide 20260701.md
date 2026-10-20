---
title: "Cloud Security Scanner Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 233
source_pdf: "ca8d4b4a75b5cf54_Alibaba Cloud Apsara Stack V3.18.6 Cloud Security Scanner Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%EF%BC%88%E9%BB%98%E5%AE%89%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Security%20Scanner%20Developer%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Cloud Security Scanner Developer Guide 20260701

## Table of Contents

- 1 Getting started
  - 1.1 Obtain the developer guide
  - 1.2 Call an API operation
- 2 Before you begin
  - 2.1 Log on to OpenAPI Explorer
  - 2.2 Obtain API information
  - 2.3 Obtain an access credential assigned by RAM
  - 2.4 Obtain an access credential assigned by STS
  - 2.5 Obtain an endpoint
- 3 Call examples
  - 3.1 SDK for Python
    - 3.1.1 Getting started
    - 3.1.2 User guide
      - 3.1.2.1 Install Apsara Stack SDK for Python
      - 3.1.2.2 Use CommonRequest to call API operations
  - 3.2 SDK for Go
    - 3.2.1 Getting started
    - 3.2.2 User guide
      - 3.2.2.1 Install the core library of Apsara Stack SDK for Go
      - 3.2.2.2 Use CommonRequest to call API operations
- 4 Common parameters
- 5 Cloud Security Scanner
  - 5.1 Templates
    - 5.1.1 TemplateAssetDetectionAdd
    - 5.1.2 TemplateListGetByType
    - 5.1.3 TemplateRiskScanAdd
    - 5.1.4 TemplateAssetDetectionDetail
    - 5.1.5 GetAssetImportTaskInfo
    - 5.1.6 GetRiskScanTaskTemplate
    - 5.1.7 TemplateDelete
    - 5.1.8 TemplateList
    - 5.1.9 TemplateRiskScanDetail
    - 5.1.10 TemplateWebMonitorConf
    - 5.1.11 BasicRiskOption
    - 5.1.12 GetCommonVulnItemList
  - 5.2 Tasks
    - 5.2.1 BatchStartTasks
    - 5.2.2 TaskAssetScanCreate
    - 5.2.3 TaskList
    - 5.2.4 BatchStopTasks
    - 5.2.5 BatchDeleteTasks
    - 5.2.6 TaskProcessV2
    - 5.2.7 TaskStart
    - 5.2.8 TaskStop
    - 5.2.9 BatchSuspendTasks
    - 5.2.10 TaskProcess
    - 5.2.11 TaskRestart
    - 5.2.12 TaskDelete
    - 5.2.13 TaskRiskScanDetail
    - 5.2.14 GetAssetScanTaskInfo
    - 5.2.15 TaskAssetImportDetail
    - 5.2.16 TaskAssetScanDetail
    - 5.2.17 TaskAssetImportChildDetail
    - 5.2.18 CycleTaskAssetStats
    - 5.2.19 TaskAssetScanCycleRunning
    - 5.2.20 TaskAssetImport
    - 5.2.21 TaskRiskScanCreate
    - 5.2.22 TaskAssetImportDetailExists
    - 5.2.23 TaskQueueTaskDetail
    - 5.2.24 TaskAssetImportBaseInfo
    - 5.2.25 TaskRiskScanCycleRunning
    - 5.2.26 GetAssetRiskScanTaskInfo
    - 5.2.27 BatchRestartTasks
    - 5.2.28 TaskQueueTaskList
    - 5.2.29 TaskQueueTaskInfo
    - 5.2.30 TaskStatusStats
    - 5.2.31 TaskQueueTaskListDetail
    - 5.2.32 TaskRunTypeStats
    - 5.2.33 TaskQueueTaskCount
    - 5.2.34 SuspendStatus
- 6 Vulnerability Scan V2
  - 6.1 Asset API
    - 6.1.1 Host assets
      - 6.1.1.1 DescribeHostAssetList
    - 6.1.2 Website assets
      - 6.1.2.1 DescribeWebsiteAssetList
    - 6.1.3 Domain name assets
      - 6.1.3.1 DescribeDomainAssetList
    - 6.1.4 DeleteAsset
  - 6.2 Task API
    - 6.2.1 Asset import task
      - 6.2.1.1 CreateAssetImportTask
      - 6.2.1.2 DescribeAssetImportTask
      - 6.2.1.3 DescribeAssetImportTaskResult
    - 6.2.2 Asset scan
      - 6.2.2.1 CreateAssetScanTask
      - 6.2.2.2 DescribeAssetScanTask
    - 6.2.3 Risk scanning
      - 6.2.3.1 CreateRiskScanTask
      - 6.2.3.2 DescribeRiskScanTask
      - 6.2.3.3 DescribeRiskScanTaskResult
    - 6.2.4 DescribeTaskList
    - 6.2.5 StartTask
    - 6.2.6 StopTask
    - 6.2.7 SuspendTask
    - 6.2.8 DeleteTask
  - 6.3 Risk API
    - 6.3.1 Security vulnerability
      - 6.3.1.1 DescribeRiskList
    - 6.3.2 Public access
      - 6.3.2.1 DescribeBaselineRiskList
    - 6.3.3 Compliance vulnerability
      - 6.3.3.1 DescribeComplianceRiskList
- 7 Security audit
  - 7.1 GetData
  - 7.2 LouauditCleanData

## 1 Getting started

### 1.1 Obtain the developer guide

This topic describes how to find the required developer guide when you call an API operation of an Apsara Stack service.

**Flowchart**

You can follow the procedure described in the following figure to view the specific developer guide.

**Prerequisites**

The Apsara Stack version is obtained from an O&M or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center to view the required documentation.
1. Go to the Apsara Stack documentation center.
2. Click the **Enterprise**, **Agility&XStack**, or **All-in-one** tab based on the Apsara Stack
edition that you use.
3. Select the Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service whose documentation you
want to view.
5. Find the developer guide and click **View Details** or **Download PDF**.

### 1.2 Call an API operation

Apsara Stack allows you to call API operations by using the POP gateway. To ensure that Apsara Stack provides the same experience as Alibaba Cloud Public Cloud, API operations in Apsara Stack V3.16.0 and later are called by using the POP gateway by default. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

**Procedure**

1. Obtain the access credential.
Obtain the access credential that is required to call an API operation. For more information, see Obtain an access credential assigned by RAM or Obtain an access credential assigned by STS.

> **Note:** We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or an access credential assigned by Security Token Service (STS) to call the API operations of the Apsara Uni-manager Management Console and cloud services.

2. Obtain the region ID.
3. Obtain the organization ID and resource set ID.
You must call an API operation to obtain an organization ID. For more information, see GetO rganizationList in Apsara Uni-manager Management Console Developer Guide. You must call an API operation to obtain a resource set ID. For more information, see ListRe sourceGroup in Apsara Uni-manager Management Console Developer Guide.

> **Note:** When you call an API operation, set the `<x-acs-organizationid>` header to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` header to the resource set ID that you obtained. This way, you can query resources in the specified organization and resource set.
> If you do not specify the `<x-acs-organizationid>` header, the organization to which the current user belongs is used by default.
> If you do not specify the `<x-acs-resourcegroupid>` header, this header is left empty by default. If you specify a resource set ID, you must also specify an organization ID.

4. View the developer guide of the cloud service on which you want to perform the operation.
To learn the features of API operations and how to call the API operations, obtain the developer guide of the cloud service that you want to use. For more information, see Obtain the developer guide.
5. Obtain the endpoint of the cloud service.
6. Obtain the cloud service SDK and call an API operation.

## 2 Before you begin

### 2.1 Log on to OpenAPI Explorer

You can log on to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from a deployment engineer. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of your
browser and press the Enter key.
2. Enter your username and password.
You need to obtain the username and password from an operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account as prompted. For security purposes, your password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the following
operations based on your logon scenario: Scenario 1: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device as prompted. b. Re-enter the username and password as described in Step 2 and click **Log On**. c. Enter the six-digit MFA verification code and click **Authenticate**. Scenario 2: You log on to the Apsara Uni-manager Management Console after MFA is enabled and an MFA device is bound. Enter the six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see **Bind a virtual MFA device to enable MFA** in **Apsara** **Uni-manager Management Console User Guide**.

5. In the top navigation bar, choose **Products > Development Tools > OpenAPI Explorer**.

### 2.2 Obtain API information

To call an API operation by using an SDK, you must first obtain information about the API operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page in the Apsara Uni-manager Management Console is for reference only. For information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Development****Tools** > **OpenAPI****Explorer**.
3. In the top navigation bar of the OpenAPI Explorer page, choose **API****Integration** > **API**
**Debugging**.
4. In the left-side navigation pane, select the cloud service that you want to manage. In the
API operation list, you can view all API operations of the current version. If multiple API versions exist, you can select the required API version from the **Version** drop-down list.

### 2.3 Obtain an access credential assigned by RAM

**assigned by RAM**

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use either type of access credential for authentication when you make an API request. This topic describes how to obtain an access credential that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an access credential for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an access credential assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, you must configure the headers in the following table. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console and has limited permissions. The AccessKey pair of an organization has greater permissions. If you want to use such an AccessKey pair, make sure that your operation is allowed by an administrator to ensure security.

| Header | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. For example, you can use the ID of an Elastic Compute Service (ECS) instance obtained from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the avatar in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair.

> **Note:** The AccessKey pair provides full permissions on cloud resources within your account. You must keep the AccessKey pair strictly confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page, click **Manage AccessKey Pairs**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.4 Obtain an access credential assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

Alibaba Cloud STS allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to call API operations in Apsara Stack. An access credential assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, these three elements are required.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your Resource Access Management
(RAM) role. i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your RAM role.
2. Obtain the access credential assigned by STS.

> **Note:** Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <yourRegionID>: Replace this variable with the actual region ID.
> <yourAccessKeyID>: Replace this variable with your AccessKey ID.
> <yourAccessKeySecret>: Replace this variable with your AccessKey secret.
> <yourRoleSessionName>: Replace this variable with the actual session name.
> You can customize the session name. We recommend that you set the session name to your identity information such as username. This way, users who assume the same RAM role to perform operations can be distinguished based on the value of the `RoleSessionName` variable. This implements user-specific auditing. The value of this variable must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_).
> <yourRoleArn>: Replace this variable with the actual ARN of your RAM role.
> "sts.aliyuns.com": Replace this variable with the actual endpoint of STS.

```java
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize it.
    // Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the
actual region ID, your AccessKey ID, and your AccessKey secret.
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
    // Obtain the access credential assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace sts.aliyuns.com with the actual endpoint of STS. The format of an STS
endpoint is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the actual session name.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace <yourRoleArn> with the ARN of your RAM role that is obtained in the pr
evious step.
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

3. Use the access credential assigned by STS to call an API operation of a service. The
following sample code provides an example on how to call the `DescribeZones` operation of Elastic Compute Service (ECS):

> **Note:** Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <yourRegionID>: Replace this variable with the actual region ID.
> <yourStsAccesskeyID>: Replace this variable with the AccessKey ID assigned by STS.
> <yourStsAccessKeySecret>: Replace this variable with the AccessKey secret assigned by STS.
> <yourStsToken>: Replace this variable with the security token assigned by STS.
> <yourResourceGroupID>: Replace this variable with the actual resource set ID.
> <yourOrganizationID>: Replace this variable with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace <yourRegionID> with the actual region ID.
    // Replace <yourStsAccessKeyID> and <yourStsAccessKeySecret> with the AccessKey I
D and AccessKey secret assigned by STS, which are obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
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
    // Replace <yourRegionID> with the actual region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace <yourStsToken> with the security token assigned by STS, which is obtai
ned in the previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace <yourResourceGroupID> with the actual resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Optional. Replace <yourOrganizationID> with the actual organization ID.
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

### 2.5 Obtain an endpoint

This topic describes how to obtain the endpoint of an Apsara Stack Security service.

**Background information**

To use the POP gateway to call the API operations of a cloud service, you must specify the endpoint of the cloud service. You can obtain an endpoint from onsite Apsara Stack O&M engineers. You can also perform the following steps to obtain an endpoint.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform****Operation** > **Apsara****Infrastructure**
**Management** > **Resource****Management**.
3. In the left-side navigation pane, choose **Resource****Management** > **Product & Cluster**
**O&M**.
4. Enter sas-securityoperationscentercluster in the **Product | Cluster** search box. Then, click
**Cluster Details** in the Actions column.
5. On the **Services** tab, click the name of the service.
6. Click **yundun-soc** in the **Components** pane. Then, click the **Registration Variables** tab
and enter yundunsoc.pop.endpoint in the search box to obtain the endpoint of the service.
7. The endpoint of a cloud service is in the following format:

```
${EndpointPre}.${global:region}.${global:internet-domain}
```

## 3 Call examples

### 3.1 SDK for Python

#### 3.1.1 Getting started

This topic describes how to obtain and use Apsara Stack SDK for Python.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Python. For more information, see Obtain an access credential assigned by RAM. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Install the core library of Apsara Stack SDK for Python**

If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip3 install aliyun-python-sdk-core-v3
```

**Use Apsara Stack SDK for Python**

To use Apsara Stack SDK for Python, perform the following steps:
1. Create a client instance.
Before you create a client instance, you must obtain a region ID, an AccessKey ID, and an AccessKey secret.
2. Create an API request and specify the required parameters.
3. Initiate the API request and manage the response or exceptions.

> **Note:** Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <your_region_id>: Replace this variable with the region ID.
> <your_access_key_id>: Replace this variable with your AccessKey ID.
> <your_access_key_secret>: Replace this variable with your AccessKey secret.
> <your-endpoint>: Replace this variable with the endpoint of the service.
> <API-version>: Replace the value of this parameter with the version of the API.
> <your-action>: Replace this variable with the name of the API operation.

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>')// The endpoint of the service. request.set_version('<API-version>')// The version of the API. request.set_action_name('<your-action>')// The name of the API operation.
# or:
# request =
CommonRequest(domain='<your-endpoint>', version='<API-version>', action_name='<your-action>') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

#### 3.1.2 User guide

##### 3.1.2.1 Install Apsara Stack SDK for Python

This topic describes how to install and use Apsara Stack SDK for Python.

##### 3.1.2.2 Use CommonRequest to call API operations

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest**

Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code provides an example on how to use CommonRequest to call an API operation:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<YOUR-ENDPOINT>') // The endpoint of the service. request.set_version('<API-version>') // The version of the API. request.set_action_name('<YOUR-ACTION>')// The name of the API operation.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

### 3.2 SDK for Go

#### 3.2.1 Getting started

Apsara Stack SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Apsara Stack SDK for Go.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Go. You can view and obtain your AccessKey pair in the Apsara Unimanager Management Console. For more information, see Obtain an access credential assigned by RAM. The endpoint of the service is obtained. For more information, see Obtain an endpoint.

**Install the core library of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use Apsara Stack SDK for Go**

To use Apsara Stack SDK for Go, perform the following steps:
1. Initialize a client instance.
2. Create an API request and specify the required parameters.
3. Initiate the API request and manage the response or exceptions.

> **Note:** Replace the variables in the following sample code with actual values. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <your_region_id>: Replace this variable with the region ID.
> <your_access_key_id>: Replace this variable with your AccessKey ID.
> <your_access_key_secret>: Replace this variable with your AccessKey secret.
> <your-endpoint>: Replace this variable with the endpoint of the service.
> <API-version>: Replace this variable with the version of the API.
> <your-action>: Replace this variable with the name of the API operation.

```java
package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "fmt"
```

`)`

```
func main() { client, err := sdk.NewClientWithAccessKey("<your_region_id>", "{your_access_key_id}", "{your_access_key_secret}") if err != nil { panic(err)
 request
:= requests.NewCommonRequest() request.Domain = "<your-endpoint>"// The endpoint of the service. request.Version = "<API-version>"// The version of the API. request.ApiName = "<your-action>"// The name of the API operation. request.QueryParams["PageNumber"] = "1" request.QueryParams["PageSize"] = "30" response, err := client.ProcessCommonRequest(request) if err != nil { panic(err) fmt.Print(response.GetHttpContentString())
```

#### 3.2.2 User guide

##### 3.2.2.1 Install the core library of Apsara Stack SDK for Go

**for Go**

This topic describes how to install the core library of Apsara Stack SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 3.2.2.2 Use CommonRequest to call API operations

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest**

Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code provides an example on how to use CommonRequest to call an API operation:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("cn-hangzhou", "{your_access_key_id}", "{
your_access_key_secret}")
    if err != nil {
        panic(err)
    request := requests.NewCommonRequest()
    request.Domain = "<YOUR-ENDPOINT>"// The endpoint of the service.
    request.Version = "<API-version>"// The version of the API.
    request.ApiName = "<YOUR-ACTION>"// The name of the API operation.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

## 4 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack Security API requests. Table 1. Common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the response. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: 2018-01-16: Auditprivate. 2019-07-23: yundunnextsoc. 2018-12-03: Sas. 2016-11-11: aegis. 2021-10-11: yundun-css. 2019-08-05: secspy. 2018-01-16: Ddosprivate. 2018-06-30: hsm-private. 2017-12-07: Cloudfw. 2019-01-03: Sddp. 2020-07-01: semawaf. 2018-12-03: soar. |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is provided by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is provided by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

| Product | Strin g | Yes | The code of the service to which the API operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security. yundunnextsoc: Security Operations Center (SOC). Sas: Threat Detection Service. aegis: Server Guard. yundun-css: Container Protection. secspy: Network Detection and Response. Ddosprivate: Anti-DDoS Service. hsm-private: Cloud Hardware Security Module (HSM). Cloudfw: Cloud Firewall (CFW). Sddp: Sensitive Data Discovery and Protection (SDDP). semawaf: Web Application Firewall (WAF). soar: Security Orchestration and Automation Response (SOAR). |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the API operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security. yundunnextsoc-pop: the prefix in the endpoint of SOC. tds: the prefix in the endpoint of Threat Detection Service. aegis: the prefix in the endpoint of Server Guard. yundun-css: the prefix in the endpoint of Container Protection. secspy-share: the prefix in the endpoint of Network Detection and Response. ddosprivate: the prefix in the endpoint of Anti-DDoS Service. hsmprivate: the prefix in the endpoint of HSM. cloudfw: the prefix in the endpoint of CFW. sddp-api: the prefix in the endpoint of SDDP. semawaf: the prefix in the endpoint of WAF. soar: the prefix in the endpoint of SOAR. |

**Common response parameters**

Responses are returned in the unified format for API requests. The following HTTP status codes indicate the request status: 2xx: indicates that the request is successful. 4xx or 5xx: indicates that the request failed. Responses are returned in the JSON format. Each response returns a unique request ID regardless of whether the request is successful.

## 5 Cloud Security Scanner

### 5.1 Templates

#### 5.1.1 TemplateAssetDetectionAdd

Creates an asset scan template. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateAssetDetectio nAdd | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| alive port _ s | Strin g | Body | No |   | The ports to be scanned. |
| baseline | Integ er | Body | No | 1 | The baseline ID. |
| baseline r _ ule | Integ er | Body | No | 1 | The baseline rule. |
| custom p _ ort | Strin g | Body | No |   | The additional ports. |
| disable su _ bdomain _ api | Integ er | Body | No | 1 | Specifies whether to enable subdomain brute forcing. |
| disable su _ bdomain _ dict | Integ er | Body | No | 1 | Specifies whether to enable subdomain brute forcing. |

| loud Security | Scanner | Develope |   |   |   |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| exclude p _ orts | Strin g | Body | No |   | The excluded ports. |
| icmp ech _ o | Integ er | Body | No | 1 | Specifies whether to enable ICMP echo scan. |
| inherit att _ rs | Integ er | Body | No | 1 | Specifies whether to enable automatic synchronization of asset information. |
| ip2domain | Integ er | Body | No | 1 | Specifies whether to enable reverse lookup of IP addresses. |
| ip scan _ | Integ er | Body | No | 1 | Specifies whether to enable automatic import of associated IP addresses. |
| name | Strin g | Body | No | Full risk scan template | The template name. |
| no status _ | Integ er | Body | No | 1 | Specifies whether to enable stateless scan. |
| port area _ | Strin g | Body | No | ALL | The port range. |
| retry time _ s | Integ er | Body | No | 1 | The maximum number of retries. |
| scan spee _ d | Strin g | Body | No |   | The scan rate. |
| sctp | Integ er | Body | No | 1 | Specifies whether to enable SCTP scan. |
| spc ports _ | Strin g | Body | No |   |   |
| sub doma _ in brute r _ _ ate | Integ er | Body | No | 1 | The subdomain brute forcing rate. |
| sub doma _ in scan _ | Integ er | Body | No | 1 | Specifies whether to enable subdomain API query. |

|   |   |   |   | Cloud r Gu | Security Scanner Develop ide·Cloud Security Scanne |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| tcp ack _ | Integ er | Body | No | 1 | Specifies whether to enable TCP ACK scan. |
| tcp syn _ | Integ er | Body | No | 1 | Specifies whether to enable TCP SYN scan. |
| udp | Integ er | Body | No | 1 | Specifies whether to enable UDP scan. |
| vpc id _ | Strin g | Body | No |   | The virtual private cloud (VPC) ID. |
| wait time _ out | Integ er | Body | No | 1 | The timeout period. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| data | Integer | 1 | The template ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateAssetDetectionAdd&RegionId=cnhangzhou&alive_ports=&baseline=1&baseline_rule=1&custom_port=&disable_subdomain_api=1&dis le_subdomain_dict=1&exclude_ports=&icmp_echo=1&inherit_attrs=1&ip2domain=1&ip_scan=1&name ull risk scan template&no_status=1&port_area=ALL&retry_times=1&scan_speed=&sctp=1&sub_domain_brute_rate &sub_domain_scan=1&tcp_ack=1&tcp_syn=1&udp=1&vpc_id=&wait_timeout=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
```

`XML` format

```xml
Content-Type:application/xml <TemplateAssetDetectionAddResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
</TemplateAssetDetectionAddResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.2 TemplateListGetByType

Queries a list of templates by type. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateListGetByTyp e | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| template _ type | Integ er | Body | No | 1 | The template type. Valid values: 1: risk scan template. 4: availability monitoring template. 5: asset scan template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -create tm _ | Integer |   | The time when the template was created. |
| -creator | String |   | The user who created the template. |
| -id | Integer |   | The template ID. |
| -is default _ | Integer |   | Indicates whether the template is the default one. |
| -name | String |   | The template name. |
| -org full id _ _ | String |   | The full organization ID. |
| -org id _ | String |   | The organization ID. |
| -type | Integer |   | The template type. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateListGetByType&RegionId=cn-hangzhou&template_type=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "creator":"",
            "create_tm":"",
            "org_id":"",
            "name":"",
            "id":"",
            "is_default":"",
            "type":"",
            "org_full_id":""
```

`]` `XML` format

```xml
Content-Type:application/xml <TemplateListGetByTypeResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <create_tm></create_tm>
        <creator></creator>
        <id></id>
        <is_default></is_default>
        <name></name>
        <org_full_id></org_full_id>
        <org_id></org_id>
        <type></type>
    </data>
</TemplateListGetByTypeResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.3 TemplateRiskScanAdd

Creates a risk scan template. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateRiskScanAdd | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| advanced scan _ | Strin g | Body | No |   | The advanced scan configurations. |
| basic sca _ n | Strin g | Body | No |   | The basic scan configurations. |
| emergent scan _ | Strin g | Body | No |   | The emergency scan configurations. |
| exclude p _ orts | Strin g | Body | No |   | The excluded ports. |
| name | Strin g | Body | No | Full risk scan template | The template name. |
| user agen _ t | Strin g | Body | No |   | The user agent string. |
| vpc id _ | Strin g | Body | No |   | The virtual private cloud (VPC) ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| data | Integer | 1 | The template ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateRiskScanAdd&RegionId=cnhangzhou&advanced_scan=&basic_scan=&emergent_scan=&exclude_ports=&name=Full risk scan t emplate&user_agent=&vpc_id=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
```

`XML` format

```xml
Content-Type:application/xml <TemplateRiskScanAddResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
</TemplateRiskScanAddResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.4 TemplateAssetDetectionDetail

Queries the details of an asset scan template. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateAssetDetectio nDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The template ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| alive ports _ | String |   | The ports to be scanned. |
| baseline id _ | Integer |   | The baseline ID. |
| baseline name _ | String |   | The baseline name. |
| baseline rule _ | Integer |   | The baseline rule. |
| custom port _ | String |   | The additional ports. |
| disable subdo _ main api _ | Integer |   | Indicates whether subdomain brute forcing is enabled. |
| disable subdo _ main dict _ | Integer |   | Indicates whether subdomain brute forcing is enabled. |
| exclude ports _ | String |   | The excluded ports. |
| icmp echo _ | Integer |   | Indicates whether ICMP echo scan is enabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| inherit attrs _ | Integer |   | Indicates whether automatic synchronization of asset information is enabled. |
| ip2domain | Integer |   | Indicates whether reverse lookup of IP addresses is enabled. |
| ip scan _ | Integer |   | Indicates whether automatic import of associated IP addresses is enabled. |
| name | String |   | The template name. |
| no status _ | Integer |   | Indicates whether stateless scan is enabled. |
| opt | String |   | The options. |
| port area _ | String |   | The port range. |
| retry times _ | Integer |   | The maximum number of retries. |
| scan speed _ | String |   | The scan rate. |
| sctp | Integer |   | Indicates whether SCTP scan is enabled. |
| sub domain b _ _ rute rate _ | Integer |   | The subdomain brute forcing rate. |
| sub domain s _ _ can | Integer |   | Indicates whether subdomain API query is enabled. |
| target type _ | String |   | The asset type. |
| tcp ack _ | Integer |   | Indicates whether TCP ACK scan is enabled. |
| tcp syn _ | Integer |   | Indicates whether TCP SYN scan is enabled. |
| type | String |   | The exposure type. Valid values: port and service. |

|   |   |   | Cloud Security Scanner Develop r Guide·Cloud Security Scanne |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| udp | Integer |   | Indicates whether UDP scan is enabled. |
| value | String |   | The exposed ports or services. |
| vpc id _ | String |   | The virtual private cloud (VPC) ID. |
| wait timeout _ | Integer |   | The timeout period. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateAssetDetectionDetail&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "alive_ports":"",
    "baseline_id":"",
    "baseline_name":"",
    "baseline_rule":"",
    "custom_port":"",
    "disable_subdomain_api":"",
    "disable_subdomain_dict":"",
    "exclude_ports":"",
    "icmp_echo":"",
    "inherit_attrs":"",
    "ip2domain":"",
    "ip_scan":"",
    "name":"",
    "no_status":"",
    "opt":"",
    "port_area":"",
    "retry_times":"",
    "scan_speed":"",
    "sctp":"",
    "sub_domain_brute_rate":"",
    "sub_domain_scan":"",
    "target_type":"",
    "tcp_ack":"",
    "tcp_syn":"",
    "type":"",
    "udp":"",
    "value":"",
    "vpc_id":"",
    "wait_timeout":""
```

`XML` format

```xml
Content-Type:application/xml <TemplateAssetDetectionDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <alive_ports></alive_ports>
    <baseline_id></baseline_id>
    <baseline_name></baseline_name>
    <baseline_rule></baseline_rule>
    <custom_port></custom_port>
    <disable_subdomain_api></disable_subdomain_api>
    <disable_subdomain_dict></disable_subdomain_dict>
    <exclude_ports></exclude_ports>
    <icmp_echo></icmp_echo>
    <inherit_attrs></inherit_attrs>
    <ip2domain></ip2domain>
    <ip_scan></ip_scan>
    <name></name>
    <no_status></no_status>
    <opt></opt>
    <port_area></port_area>
    <retry_times></retry_times>
    <scan_speed></scan_speed>
    <sctp></sctp>
    <sub_domain_brute_rate></sub_domain_brute_rate>
    <sub_domain_scan></sub_domain_scan>
    <target_type></target_type>
    <tcp_ack></tcp_ack>
    <tcp_syn></tcp_syn>
    <type></type>
    <udp></udp>
    <value></value>
    <vpc_id></vpc_id>
    <wait_timeout></wait_timeout>
</TemplateAssetDetectionDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.5 GetAssetImportTaskInfo

Queries the information about an asset import task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:GetAssetImportTaskInf o | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| asset list _ | String |   | The assets. Example: 1.1.1.1. |
| tag names _ | String |   | The tags. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| group id _ | Integer | 1 | The group ID. |
| screen shot _ | Integer | 1 | Indicates whether website screenshot is enabled. A value of 1 indicates that website screenshot is enabled. A value of 0 indicates that website screenshot is disabled. |
| staff id _ | Integer | 1 | The user ID. |
| task name _ | String | test | The task name. |
| template id _ | Integer | 1 | The template ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetAssetImportTaskInfo&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "group_id":1,
    "screen_shot":1,
    "staff_id":1,
    "task_name":"test",
    "template_id":1
```

`XML` format

```xml
Content-Type:application/xml <GetAssetImportTaskInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <asset_list>
        <asset_list></asset_list>
    </asset_list>
    <group_id>1</group_id>
    <screen_shot>1</screen_shot>
    <staff_id>1</staff_id>
    <tag_names>
        <tag_name></tag_name>
    </tag_names>
    <task_name>test</task_name>
    <template_id>1</template_id>
</GetAssetImportTaskInfoResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.6 GetRiskScanTaskTemplate

Queries the information about a risk scan template.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:GetRiskScanTaskTempl ate | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The template ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| exclude ports _ | String |   | The excluded ports. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| advanced sca _ n | Map |   | The advanced scan configurations. |
| basic scan _ | Map |   | The basic scan configurations. |
| emergent sca _ n | Map |   | The emergency scan configurations. |
| name | String | Asset scan template-test | The template name. |
| user agent _ | String | xxx | The user agent string. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetRiskScanTaskTemplate&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "advanced_scan":"",
    "basic_scan":"",
    "emergent_scan":"",
    "name":"Asset scan template-test",
    "user_agent":"xxx"
```

`XML` format

```xml
Content-Type:application/xml <GetRiskScanTaskTemplateResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <advanced_scan></advanced_scan>
    <basic_scan></basic_scan>
    <emergent_scan></emergent_scan>
    <exclude_ports>
        <exclude_port></exclude_port>
    </exclude_ports>
    <name>Asset scan template-test</name>
    <user_agent>xxx</user_agent>
</GetRiskScanTaskTemplateResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.7 TemplateDelete

Deletes templates. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateDelete | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ids | Strin g | Body | No |   | The template IDs. Example: [85,86]. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateDelete&RegionId=cn-hangzhou&ids=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <TemplateDeleteResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</TemplateDeleteResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.8 TemplateList

Queries a list of templates. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TemplateList | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2024-08-01 23:59:59 | The end of the time range to query. |
| page | Integ er | Body | No | 1 | The page number. |

| loud Security | Scanner | Develope |   |   |   |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| search | Strin g | Body | No | Template | The filter conditions. You can query templates by name in fuzzy match mode. |
| start time _ | Strin g | Body | No | 2024-07-01 00:00:00 | The beginning of the time range to query. |
| template _ types | Strin g | Body | No |   | The template type. Valid values: 1: risk scan template. 4: availability monitoring template. 5: asset scan template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -create tm _ | Integer |   | The time when the template was created. |
| -creator | String |   | The user who created the template. |
| -id | Integer |   | The template ID. |
| -is default _ | Integer |   | Indicates whether the template is the default one. |
| -name | String |   | The template name. |
| -org full id _ _ | String |   | The full organization ID. |
| -org id _ | String |   | The organization ID. |
| -type | Integer |   | The template type. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

|   |   |   | Cloud Security Scanner Develop r Guide·Cloud Security Scanne |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| count | Integer |   | The total number of tasks. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateList&RegionId=cn-hangzhou&end_time=2024-08-01 23:59: 59&page=1&page_size=10&search=Template&start_time=2024-07-01 00:00:00&template_types=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "creator":"",
            "create_tm":"",
            "org_id":"",
            "name":"",
            "id":"",
            "is_default":"",
            "type":"",
            "org_full_id":""
```

`]` `XML` format

```xml
Content-Type:application/xml <TemplateListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <create_tm></create_tm>
        <creator></creator>
        <id></id>
        <is_default></is_default>
        <name></name>
        <org_full_id></org_full_id>
        <org_id></org_id>
        <type></type>
    </results>
</TemplateListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.9 TemplateRiskScanDetail

Queries the details of a risk scan template. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateRiskScanDeta il | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The template ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| exclude ports _ | String |   | The excluded ports. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| advanced sca _ n | Map |   | The advanced scan configurations. |
| basic scan _ | Map |   | The basic scan configurations. |
| emergent sca _ n | Map |   | The emergency scan configurations. |
| name | String | Asset scan template-test | The template name. |
| user agent _ | String | xxx | The user agent string. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateRiskScanDetail&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "advanced_scan":"",
    "basic_scan":"",
    "emergent_scan":"",
    "name":"Asset scan template-test",
    "user_agent":"xxx"
```

`XML` format

```xml
Content-Type:application/xml <TemplateRiskScanDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <advanced_scan></advanced_scan>
    <basic_scan></basic_scan>
    <emergent_scan></emergent_scan>
    <exclude_ports>
        <exclude_port></exclude_port>
    </exclude_ports>
    <name>Asset scan template-test</name>
    <user_agent>xxx</user_agent>
</TemplateRiskScanDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.10 TemplateWebMonitorConf

Queries the web monitoring configurations. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TemplateWebMonitorC onf | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| default crawl _ _ depth | Integer |   | The default crawl depth. |
| default monito _ r cycle _ | String |   | The default monitoring cycle. |
| default url lim _ _ it | Integer |   | The default URL limit. |
| monitor optio _ n | Map |   | The monitoring parameters. |
| scan param _ | Map |   | The scan parameters. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TemplateWebMonitorConf&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "default_crawl_depth":"",
    "default_monitor_cycle":"",
    "default_url_limit":"",
    "monitor_option":"",
    "scan_param":""
```

`XML` format

```xml
Content-Type:application/xml <TemplateWebMonitorConfResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <default_crawl_depth></default_crawl_depth>
    <default_monitor_cycle></default_monitor_cycle>
    <default_url_limit></default_url_limit>
    <monitor_option></monitor_option>
    <scan_param></scan_param>
</TemplateWebMonitorConfResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.11 BasicRiskOption

Queries the basic risk scan items.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:BasicRiskOption | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| type | Integ er | Body | No |   | The type of risk scan. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -define | String |   | The definition of the scan item. |
| -name | String |   | The name of the scan item. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=BasicRiskOption&RegionId=cn-hangzhou&type=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "define":"",
            "name":""
```

`]` `XML` format

```xml
Content-Type:application/xml <BasicRiskOptionResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <define></define>
        <name></name>
    </data>
</BasicRiskOptionResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.1.12 GetCommonVulnItemList

Queries a list of vulnerabilities.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:GetCommonVulnItemLi st | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| general ty _ pe | Strin g | Body | No |   | The vulnerability type. |
| page | Integ er | Body | No |   | The page number. |
| page size _ | Integ er | Body | No |   | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -module count _ | Integer |   | The number of modules. |

|   |   |   | Cloud Security Scanner Develop |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -name | String |   | The vulnerability name. |
| -risk count _ | Integer |   | The number of risks. |
| -status | Integer |   | The vulnerability status. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The number of entries per page. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetCommonVulnItemList&RegionId=cnhangzhou&general_type=&page=&page_size=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "risk_count":"",
            "module_count":"",
            "name":"",
            "status":""
```

`]` `XML` format

```xml
Content-Type:application/xml <GetCommonVulnItemListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <module_count></module_count>
        <name></name>
        <risk_count></risk_count>
        <status></status>
    </results>
</GetCommonVulnItemListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

### 5.2 Tasks

#### 5.2.1 BatchStartTasks

Starts multiple tasks at a time. This operation is supported by Cloud Security Scanner V3.2.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:BatchStartTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The end of the time range. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| parent ta _ sk id _ | Integ er | Body | No |   |   |
| run types _ | Strin g | Body | No |   | The task execution mode. Valid values: cycle, once, and immediately. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks by task ID, task name, and asset address. |
| start time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The beginning of the time range. |
| statuses | Strin g | Body | No |   | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task id _ | Integ er | Body | No | 1 | The task ID. |
| task ids _ | Strin g | Body | No |   | The task IDs. Example: [1,2,3]. |
| task types _ | Strin g | Body | No |   | The task type. Valid values: assetImport, assetRisk, and assetScan. |
| template | Integ er | Body | No | 1 | The template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |

| Guide·Cloud Sec | urity Scanner |   |   |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -task id _ | Integer | 173 | The task ID. |
| - task instance _ _ id | Integer | 208 | The task instance ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=BatchStartTasks&RegionId=cn-hangzhou&end_time=2020-01-01 00: 00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&statuses=&task_id=1&task_ids=&task_types=&template=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "task_instance_id":208,
            "task_id":173
```

`]` `XML` format

```xml
Content-Type:application/xml <BatchStartTasksResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
</BatchStartTasksResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.2 TaskAssetScanCreate

Creates an asset scan task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetScanCreate | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| cycle | Strin g | Body | No | SPEC | The type of task cycle. Valid values: SPEC, MONTH, and WEEK. |
| end tm _ | Strin g | Body | No | 24:00 | The time when the task ends. Example: 24:00. |
| is immedi _ ately | Integ er | Body | No | 1 | Specifies whether to run the task immediately after it is created. |
| month | Strin g | Body | No |   | The days of the month on which the task is run. Example: [1,2]. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| screen sh _ ot | Integ er | Body | No | 1 | Specifies whether to enable website screenshot. Valid values: 1 and 0. |
| spec cycl _ e | Integ er | Body | No | 1 | The interval at which the task is run. Unit: day. |
| start tm _ | Strin g | Body | No | 2023-09-14 16:36:18 | The time when the task starts. Examples: 00:00 for a periodic task and 2023-09-14 16:36:18 for a one-time task. |
| targets | Strin g | Body | No |   | The assets to be scanned. Example: ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3]. |
| task nam _ e | Strin g | Body | No | Risk scan task-test | The task name. |
| template i _ d | Integ er | Body | No | 1 | The template ID. |
| vpc id _ | Strin g | Body | No | 1 | The virtual private cloud (VPC) ID. |
| week | Strin g | Body | No |   | The days of the week on which the task is run. Example: [1,2]. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| data | Integer | 1 | The task ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetScanCreate&RegionId=cnhangzhou&cycle=SPEC&end_tm=24:00&is_immediately=1&month=&screen_shot=1&spec_cycle=1&start m=2023-09-14 16:36:18&targets=&task_name=Risk scan tasktest&template_id=1&vpc_id=1&week=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
```

`XML` format

```xml
Content-Type:application/xml <TaskAssetScanCreateResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
</TaskAssetScanCreateResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.3 TaskList

Queries a list of tasks. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskList | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The end of the time range to query. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| parent ta _ sk id _ | Integ er | Body | No |   |   |
| run types _ | Strin g | Body | No |   | The task execution mode. Valid values: cycle, once, and immediately. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks by task ID, task name, and asset address. |
| start time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| statuses | Strin g | Body | No |   | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task id _ | Integ er | Body | No | 1 | The task ID. |
| task ids _ | Strin g | Body | No |   | The task IDs. Example: [1,2,3]. |
| task types _ | Strin g | Body | No |   | The task type. Valid values: assetImport, assetRisk, and assetScan. |

|   |   |   |   |   | Cloud r Gu | Security Scanner Develop ide·Cloud Security Scanne | e r |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| template | Integ er | Body | No | 1 | The template ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -asset info _ | String |   | The assets. Example: 1.1.1.1. |
| -creator | String | admin | The user who created the task. |
| -cycle count _ | Integer | 10 | The number of cycles the task is run. |
| -end time _ | Integer | 1620000000 | The time when the task ends. |
| -id | Integer | 1 | The task ID. |
| -inster time _ | Integer | 1620000000 | The time when the task was created. |
| - is immediately _ | Integer | 1 | Indicates whether the task was run immediately after it was created. A value of 1 indicates that the task was run immediately after it was created. A value of 0 indicates that the task was not run immediately after it was created. |
| - is public asset _ _ | Integer | 1 | Indicates whether the assets are public network assets. A value of 1 indicates that the assets are public network assets. A value of 0 indicates that the assets are not public network assets. |
| -process | String | 100% | The task progress. |
| -start time _ | Integer | 1620000000 | The time when the task started. |
| -status | String | INIT | The task status. Valid values: INIT, RUNNING, FINISH, and STOP. |
| -sub type _ | Integer | 1 | The task subtype. |

| Cloud Security Sca Guide·Cloud Sec | nner Develope urity Scanner |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -task cycle _ | Integer | 0 | The task cycle. |
| - task instance _ _ id | Integer | 123 | The task instance ID. |
| -task name _ | String | Asset scan task- test | The task name. |
| -task type _ | Integer | 6 | The task type. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer | 10 | The total number of tasks. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskList&RegionId=cn-hangzhou&end_time=2020-01-01 00:00:00&p age=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&statuses=&task_id=1&task_ids=&task_types=&template=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":10,
    "results":[
            "cycle_count":10,
            "task_name":"Asset scan task-test",
            "creator":"admin",
            "process":"100%",
            "end_time":1620000000,
            "inster_time":1620000000,
            "is_public_asset":1,
            "task_instance_id":123,
            "start_time":1620000000,
            "task_cycle":0,
            "sub_type":1,
            "id":1,
            "is_immediately":1,
            "task_type":6,
            "status":"INIT"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <asset_info>
            <asset_info></asset_info>
        </asset_info>
        <creator>admin</creator>
        <cycle_count>10</cycle_count>
        <end_time>1620000000</end_time>
        <id>1</id>
        <inster_time>1620000000</inster_time>
        <is_immediately>1</is_immediately>
        <is_public_asset>1</is_public_asset>
        <process>100%</process>
        <start_time>1620000000</start_time>
        <status>INIT</status>
        <sub_type>1</sub_type>
        <task_cycle>0</task_cycle>
        <task_instance_id>123</task_instance_id>
        <task_name>Asset scan task-test</task_name>
        <task_type>6</task_type>
    </results>
</TaskListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.4 BatchStopTasks

Stops multiple tasks at a time. This operation is supported by Cloud Security Scanner V3.2.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:BatchStopTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The end of the time range. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| parent ta _ sk id _ | Integ er | Body | No |   |   |
| run types _ | Strin g | Body | No |   | The task execution mode. Valid values: cycle, once, and immediately. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks by task ID, task name, and asset address. |
| start time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The beginning of the time range. |
| statuses | Strin g | Body | No |   | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task id _ | Integ er | Body | No | 1 | The task ID. |
| task ids _ | Strin g | Body | No |   | The task IDs. Example: [1,2,3]. |
| task types _ | Strin g | Body | No |   | The task type. Valid values: assetImport, assetRisk, and assetScan. |

| r | Cloud Security Guide·Cloud | Scanner Security | Develope Scanner |   |   |   |   |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| template | Integ er | Body | No | 1 | The template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=BatchStopTasks&RegionId=cn-hangzhou&end_time=2020-01-01 00:0 0:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&statuses=&task_id=1&task_ids=&task_types=&template=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <BatchStopTasksResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</BatchStopTasksResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.5 BatchDeleteTasks

Deletes multiple tasks at a time. This operation is supported by Cloud Security Scanner V3.2.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:BatchDeleteTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The end of the time range. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| parent ta _ sk id _ | Integ er | Body | No |   |   |
| run types _ | Strin g | Body | No |   | The task execution mode. Valid values: cycle, once, and immediately. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks by task ID, task name, and asset address. |
| start time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The beginning of the time range. |
| statuses | Strin g | Body | No |   | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task id _ | Integ er | Body | No | 1 | The task ID. |
| task ids _ | Strin g | Body | No |   | The task IDs. Example: [1,2,3]. |
| task types _ | Strin g | Body | No |   | The task type. Valid values: assetImport, assetRisk, and assetScan. |
| template | Integ er | Body | No | 1 | The template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=BatchDeleteTasks&RegionId=cn-hangzhou&end_time=2020-01-01 00 :00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&s tatuses=&task_id=1&task_ids=&task_types=&template=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <BatchDeleteTasksResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</BatchDeleteTasksResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.6 TaskProcessV2

Queries the task progress. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskProcessV2 | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| all | Boole an | Body | No | True | Specifies whether to query all tasks. Valid values: True and False. |
| insert tm _ _ order | Integ er | Body | No | 1 | Specifies whether to sort the results in order of creation time. Valid values: 1 and -1. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| risk type _ | Integ er | Body | No | 2 | The risk type. Valid values: 2: security vulnerability. 3: compliance vulnerability. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. |
| task insta _ nce id _ | Integ er | Body | No | 1 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -insert tm _ | Integer | 1620000000 | The time when the task was created. |
| -risk addr _ | String | http://1.1.1.1 | The address of the risk. |
| -risk id _ | Integer | 1 | The ID of the risk. |
| -risk level _ | String | LOW | The level of the risk. Valid values: LOW, MEDIUM, and HIGH. |
| -risk name _ | String | xxx security vulnerability | The name of the risk. |

|   |   |   | Cloud Security Scanner Develop r Guide·Cloud Security Scanne |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -risk type _ | Integer | 3 | The risk type. Valid values: 2: security vulnerability. 3: compliance vulnerability. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The total number of tasks. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskProcessV2&RegionId=cnhangzhou&all=True&insert_tm_order=1&page=1&page_size=10&risk_type=2&search=1_1_1_1_1&task nstance_id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "risk_addr":"http://1.1.1.1",
            "risk_level":"LOW",
            "risk_id":1,
            "risk_type":3,
            "insert_tm":1620000000,
            "risk_name":"xxx security vulnerability"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskProcessV2Response>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <insert_tm>1620000000</insert_tm>
        <risk_addr>http://1.1.1.1</risk_addr>
        <risk_id>1</risk_id>
        <risk_level>LOW</risk_level>
        <risk_name>xxx security vulnerability</risk_name>
        <risk_type>3</risk_type>
    </results>
</TaskProcessV2Response>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.7 TaskStart

Starts a task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskStart | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -task id _ | Integer | 173 | The task ID. |
| - task instance _ _ id | Integer | 208 | The task instance ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskStart&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "task_instance_id":208,
            "task_id":173
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskStartResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
</TaskStartResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.8 TaskStop

Stops a task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskStop | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskStop&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <TaskStopResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</TaskStopResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.9 BatchSuspendTasks

Suspends multiple tasks at a time.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:BatchSuspendTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The end of the time range. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| parent ta _ sk id _ | Integ er | Body | No |   |   |
| run types _ | Strin g | Body | No |   | The task execution mode. Valid values: cycle, once, and immediately. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks by task ID, task name, and asset address. |
| start time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The beginning of the time range. |
| statuses | Strin g | Body | No |   | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task id _ | Integ er | Body | No | 1 | The task ID. |

|   |   |   |   | Cloud r Gu | Security Scanner Develop ide·Cloud Security Scanne |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| task ids _ | Strin g | Body | No |   | The task IDs. Example: [1,2,3]. |
| task types _ | Strin g | Body | No |   | The task type. Valid values: assetImport, assetRisk, and assetScan. |
| template | Integ er | Body | No | 1 | The template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=BatchSuspendTasks&RegionId=cn-hangzhou&end_time=2020-01-01 0 0:00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00& statuses=&task_id=1&task_ids=&task_types=&template=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <BatchSuspendTasksResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</BatchSuspendTasksResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.10 TaskProcess

Queries the task progress. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskProcess | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| all | Boole an | Body | No | True | Specifies whether to query all tasks. Valid values: True and False. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| insert tm _ _ order | Integ er | Body | No | 1 | Specifies whether to sort the results in order of creation time. Valid values: 1 and -1. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries returned per page. |
| risk type _ | Integ er | Body | No | 2 | The risk type. Valid values: 2: security vulnerability. 3: compliance vulnerability. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. |
| task insta _ nce id _ | Integ er | Body | No | 1 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -asset id _ | Integer | 1 | The asset ID. |
| -behavior | String | Checking website: … | The behavior. |
| -id | Integer | 1 | The task ID. |
| -insert tm _ | Integer | 1620000000 | The time when the task was created. |
| -is deleted _ | Integer | 0 | Indicates whether the asset is deleted. Valid values: 1: deleted. 0: not deleted. |
| -risk id _ | Integer | 1 | The risk ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

| r | Cloud Security Sca Guide·Cloud Sec | nner Develope urity Scanner |   |   |   |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| count | Integer |   | The number of entries per page. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskProcess&RegionId=cnhangzhou&all=True&insert_tm_order=1&page=1&page_size=10&risk_type=2&search=1_1_1_1_1&task nstance_id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "risk_id":1,
            "is_deleted":0,
            "insert_tm":1620000000,
            "asset_id":1,
            "id":1,
            "behavior":"Checking website: …"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskProcessResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <asset_id>1</asset_id>
        <behavior>Checking website: …</behavior>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>0</is_deleted>
        <risk_id>1</risk_id>
    </results>
</TaskProcessResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.11 TaskRestart

Restarts a task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskRestart | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -task id _ | Integer | 173 | The task ID. |
| - task instance _ _ id | Integer | 208 | The task instance ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskRestart&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "task_instance_id":208,
            "task_id":173
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskRestartResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
</TaskRestartResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.12 TaskDelete

Deletes a task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:TaskDelete | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskDelete&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <TaskDeleteResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</TaskDeleteResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.13 TaskRiskScanDetail

Queries the details of a risk scan task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskRiskScanDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| targets | Array |   |   |
| -target | String |   | The scanned asset. |
| -type | String | ALL | The asset type. Valid values: ALL ASSET, _ ALL IP, and ALL WEBSITE. _ _ |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| cycle count _ | Integer | 10 | The number of cycles the task was run. |
| finish time _ | Integer | 1600000000 | The time when the task ended. |
| host risk coun _ _ t | Integer | 10 | The number of host vulnerabilities. |
| id | Integer | 1 | The task ID. |
| insert tm _ | Integer | 1600000000 | The time when the task was created. |
| name | String | xx risk scan | The task name. |
| process | String | 100% | The task progress. |
| risk count _ | Integer | 10 | The number of security vulnerabilities. |
| start tm _ | Integer | 1600000000 | The time when the task started. |
| status | String | RUNNING | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task instance _ _ id | Integer | 1 | The task instance ID. |
| template id _ | Integer | 1 | The template ID. |
| template nam _ e | String | xx risk scan template | The template name. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskRiskScanDetail&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle_count":10,
    "finish_time":1600000000,
    "host_risk_count":10,
    "id":1,
    "insert_tm":1600000000,
    "name":"xx risk scan",
    "process":"100%",
    "risk_count":10,
    "start_tm":1600000000,
    "status":"RUNNING",
    "targets":[
            "type":"ALL"
```

`],`

```json
    "task_instance_id":1,
    "template_id":1,
    "template_name":"xx risk scan template"
```

`XML` format

```xml
Content-Type:application/xml <TaskRiskScanDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle_count>10</cycle_count>
    <finish_time>1600000000</finish_time>
    <host_risk_count>10</host_risk_count>
    <id>1</id>
    <insert_tm>1600000000</insert_tm>
    <name>xx risk scan</name>
    <process>100%</process>
    <risk_count>10</risk_count>
    <start_tm>1600000000</start_tm>
    <status>RUNNING</status>
    <targets>
        <target>
            <target></target>
        </target>
        <type>ALL</type>
    </targets>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
    <template_name>xx risk scan template</template_name>
</TaskRiskScanDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.14 GetAssetScanTaskInfo

Queries the information about an asset scan task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:GetAssetScanTaskInfo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| month | Integer |   | The days of the month on which the task is run. Example: [1,2]. |
| week | Integer |   | The days of the week on which the task is run. Example: [1,2]. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| cycle | String | SPEC | The type of task cycle. Valid values: SPEC, MONTH, and WEEK. |
| end tm _ | String | 24:00 | The time when the task ends. Example: 24:00. |
| is immediately _ | Integer | 1 | Indicates whether the task is run immediately after it is created. |
| screen shot _ | Integer | 1 | Indicates whether website screenshot is enabled. Valid values: 1: enabled. 0: disabled. |
| spec cycle _ | Integer | 1 | The interval at which the task is run. Unit: day. |
| start tm _ | String | 2023-09-14 16:36:18 | The time when the task starts. Examples: 00:00 for a periodic task and 2023-09-14 16:36:18 for a one-time task. |
| targets | Map |   | The scanned assets. |

|   |   |   |   | Cloud Security Scanner Develop r Guide·Cloud Security Scanne | e r |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| task name _ | String | test | The task name. |
| task type _ | Integer | 6 | The task type. |
| template id _ | Integer | 1 | The template ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetAssetScanTaskInfo&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle":"SPEC",
    "end_tm":"24:00",
    "is_immediately":1,
    "screen_shot":1,
    "spec_cycle":1,
    "start_tm":"2023-09-14 16:36:18",
    "targets":"",
    "task_name":"test",
    "task_type":6,
    "template_id":1
```

`XML` format

```xml
Content-Type:application/xml <GetAssetScanTaskInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle>SPEC</cycle>
    <end_tm>24:00</end_tm>
    <is_immediately>1</is_immediately>
    <month>
        <month></month>
    </month>
    <screen_shot>1</screen_shot>
    <spec_cycle>1</spec_cycle>
    <start_tm>2023-09-14 16:36:18</start_tm>
    <targets></targets>
    <task_name>test</task_name>
    <task_type>6</task_type>
    <template_id>1</template_id>
    <week>
        <week></week>
    </week>
</GetAssetScanTaskInfoResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.15 TaskAssetImportDetail

Queries the details of an asset import task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetImportDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| asset typ _ e | Strin g | Body | No | IP | The asset type. Valid values: IP, WEBSITE, and DOMAIN. |
| is new _ | Integ er | Body | No | 1 | Specifies whether the asset is newly discovered. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. |
| task insta _ nce id _ | Integ er | Body | No | 1 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -children | String |   | The subtask name. |
| -asset name _ | String | 1.1.1.1 | The asset name. |
| -asset source _ | String | Host import | The asset source. |
| -has childs _ | Integer | 0 | Indicates whether the asset is a child asset. A value of 1 indicates that the asset is a child asset. A value of 0 indicates that the asset is not a child asset. |
| -id | Integer | 1 | The task ID. |
| -insert tm _ | Integer | 1620000000 | The time when the task was created. |

| Cloud Security Sca Guide·Cloud Sec | nner Develope urity Scanner |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -is deleted _ | Boolean | False | Indicates whether the asset is deleted. Valid values: True and False. |
| -is new _ | Integer | 1 | Indicates whether the asset is newly discovered. A value of 1 indicates that the asset is newly discovered. A value of 0 indicates that the asset is not newly discovered. |
| - task instance _ _ id | Integer | 1 | The task instance ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The number of entries per page. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetImportDetail&RegionId=cnhangzhou&asset_type=IP&is_new=1&page=1&page_size=10&search=1_1_1_1_1&task_instance_id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "is_deleted":false,
            "asset_name":"1.1.1.1",
            "is_new":1,
            "asset_source":"Host import",
            "task_instance_id":1,
            "has_childs":0,
            "insert_tm":1620000000,
            "id":1
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskAssetImportDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <asset_name>1.1.1.1</asset_name>
        <asset_source>Host import</asset_source>
        <children>
            <children></children>
        </children>
        <has_childs>0</has_childs>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>False</is_deleted>
        <is_new>1</is_new>
        <task_instance_id>1</task_instance_id>
    </results>
</TaskAssetImportDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.16 TaskAssetScanDetail

Queries the details of an asset scan task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetScanDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Requestparameters**

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| targets | Array |   |   |
| -target | String |   | The scanned asset. |
| -type | String | ALL | The asset type. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| cycle count _ | Integer | 10 | The number of cycles the task was run. |
| finish time _ | Integer | 1600000000 | The time when the task ended. |
| host risk coun _ _ t | Integer | 10 | The number of host vulnerabilities. |
| id | Integer | 1 | The asset ID. |
| import count _ | Map |   | The number of imported assets. |
| insert tm _ | Integer | 1600000000 | The time when the task was created. |
| name | String | xx asset scan | The task name. |
| process | String | 100% | The task progress. |
| risk count _ | Integer | 10 | The number of security vulnerabilities. |
| start tm _ | Integer | 1600000000 | The time when the task started. |
| status | String | RUNNING | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |

|   |   |   | Cloud Security Scanner Develop r Guide·Cloud Security Scanne |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| task instance _ _ id | Integer | 1 | The task instance ID. |
| template id _ | Integer | 1 | The template ID. |
| template nam _ e | String | xx asset scan template | The template name. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetScanDetail&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle_count":10,
    "finish_time":1600000000,
    "host_risk_count":10,
    "id":1,
    "import_count":"",
    "insert_tm":1600000000,
    "name":"xx asset scan",
    "process":"100%",
    "risk_count":10,
    "start_tm":1600000000,
    "status":"RUNNING",
    "targets":[
            "type":"ALL"
```

`],`

```json
    "task_instance_id":1,
    "template_id":1,
    "template_name":"xx asset scan template"
```

`XML` format

```xml
Content-Type:application/xml <TaskAssetScanDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle_count>10</cycle_count>
    <finish_time>1600000000</finish_time>
    <host_risk_count>10</host_risk_count>
    <id>1</id>
    <import_count></import_count>
    <insert_tm>1600000000</insert_tm>
    <name>xx asset scan</name>
    <process>100%</process>
    <risk_count>10</risk_count>
    <start_tm>1600000000</start_tm>
    <status>RUNNING</status>
    <targets>
        <target>
            <target></target>
        </target>
        <type>ALL</type>
    </targets>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
    <template_name>xx asset scan template</template_name>
</TaskAssetScanDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.17 TaskAssetImportChildDetail

Queries the details of an asset import subtask. This operation is supported by Cloud Security Scanner V3.1.0 later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetImportChildD etail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| asset id _ | Integ er | Body | No | 1 | The asset ID. |
| is new _ | Integ er | Body | No | 1 | Specifies whether the asset is newly discovered. Valid values: 1 and 0. |
| task insta _ nce id _ | Integ er | Body | No | 1 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -children | String |   | The subtask name. |
| -asset name _ | String | 1.1.1.1 | The asset name. |
| -asset source _ | String | Host import | The asset source. |
| -has childs _ | Integer | 0 | Indicates whether the asset is a child asset. A value of 1 indicates that the asset is a child asset. A value of 0 indicates that the asset is not a child asset. |
| -id | Integer | 1 | The task ID. |
| -insert tm _ | Integer | 1620000000 | The time when the subtask was created. |
| -is deleted _ | Boolean | False | Indicates whether the asset is deleted. Valid values: True and False. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -is new _ | Integer | 1 | Indicates whether the asset is newly discovered. A value of 1 indicates that the asset is newly discovered. A value of 0 indicates that the asset is not newly discovered. |
| - task instance _ _ id | Integer | 1 | The task instance ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetImportChildDetail&RegionId=cnhangzhou&asset_id=1&is_new=1&task_instance_id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "is_deleted":false,
            "asset_name":"1.1.1.1",
            "is_new":1,
            "asset_source":"Host import",
            "task_instance_id":1,
            "has_childs":0,
            "insert_tm":1620000000,
            "id":1
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskAssetImportChildDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <asset_name>1.1.1.1</asset_name>
        <asset_source>Host import</asset_source>
        <children>
            <children></children>
        </children>
        <has_childs>0</has_childs>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>False</is_deleted>
        <is_new>1</is_new>
        <task_instance_id>1</task_instance_id>
    </data>
</TaskAssetImportChildDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.18 CycleTaskAssetStats

Queries the statistics on periodic asset scan tasks. This operation is supported by Cloud Security Scanner V3.4.1 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:CycleTaskAssetStats | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=CycleTaskAssetStats&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`XML` format

```xml
Content-Type:application/xml <CycleTaskAssetStatsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</CycleTaskAssetStatsResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.19 TaskAssetScanCycleRunning

Queries whether periodic asset scan tasks exist. This operation is supported by Cloud Security Scanner V3.4.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetScanCycleRu nning | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetScanCycleRunning&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`XML` format

```xml
Content-Type:application/xml <TaskAssetScanCycleRunningResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</TaskAssetScanCycleRunningResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.20 TaskAssetImport

Creates an asset import task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetImport | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| asset met _ adatas | Strin g | Body | No |   | The asset metadata. |
| content m _ onitor | Integ er | Body | No |   |   |
| customize asset list _ _ | Strin g | Body | No |   |   |
| group id _ | Integ er | Body | No | 0 | The group ID. |
| is immedi _ ately | Integ er | Body | No | 1 | Specifies whether to run the task immediately after it is created. |
| is public _ _ asset | Integ er | Body | No |   | Specifies whether the assets are public network assets. |

|   |   |   |   | Cloud r Gu | Security Scanner Develop ide·Cloud Security Scanne |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| network t _ ype | Integ er | Body | No | 1 | The network type. Valid values: 1 and 2. |
| not alive _ _ report | Integ er | Body | No | 1 | Specifies whether to report non-alive assets. |
| screen sh _ ot | Integ er | Body | No | 1 | Specifies whether to enable website screenshot. A value of 1 specifies enabling website screenshot. A value of 0 specifies disabling website screenshot. |
| staff id _ | Integ er | Body | No | 1 | The user ID. |
| start tm _ | Strin g | Body | No | 2020-01-01 00:00:00 | The time when the task starts. |
| tag ids _ | Strin g | Body | No |   | The tag IDs. Example: [1,2,3]. |
| targets | Strin g | Body | No |   | The assets to be imported. Example: ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3]. |
| task nam _ e | Strin g | Body | No | Risk scan task-test | The task name. |
| template i _ d | Integ er | Body | No | 1 | The template ID. |
| vpc id _ | Strin g | Body | No | 1 | The virtual private cloud (VPC) ID. |
| web moni _ tor | Integ er | Body | No |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| data | Integer | 1 | The task ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetImport&RegionId=cnhangzhou&asset_metadatas=&group_id=0&is_immediately=1&is_public_asset=&network_type=1&not live_report=1&screen_shot=1&staff_id=1&start_tm=2020-01-01 00:00:00&tag_ids=&targets=&task_name=Risk scan task-test&template_id=1&vpc_id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
```

`XML` format

```xml
Content-Type:application/xml <TaskAssetImportResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
</TaskAssetImportResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.21 TaskRiskScanCreate

Creates a risk scan task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskRiskScanCreate | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| cycle | Strin g | Body | No | SPEC | The type of task cycle. Valid values: SPEC, MONTH, and WEEK. |
| end tm _ | Strin g | Body | No | 24:00 | The time when the task ends. Example: 24:00. |
| is immedi _ ately | Integ er | Body | No | 1 | Specifies whether to run the task immediately after it is created. |
| month | Strin g | Body | No |   | The days of the month on which the task is run. Example: [1,2]. |
| scan spee _ d | Strin g | Body | No |   | The scan rate. This parameter is no longer used. |
| spec cycl _ e | Integ er | Body | No | 1 | The interval at which the task is run. Unit: day. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| start tm _ | Strin g | Body | No | 2023-09-14 16:36:18 | The time when the task starts. Examples: 00:00 for a periodic task and 2023-09-14 16:36:18 for a one-time task. |
| targets | Strin g | Body | No |   | The assets to be scanned. Example: ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3]. |
| task nam _ e | Strin g | Body | No | Risk scan task-test | The task name. |
| template i _ d | Integ er | Body | No | 1 | The template ID. |
| vpc id _ | Strin g | Body | No | 1 | The virtual private cloud (VPC) ID. |
| week | Strin g | Body | No |   | The days of the week on which the task is run. Example: [1,2]. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| data | Integer | 1 | The task ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskRiskScanCreate&RegionId=cnhangzhou&cycle=SPEC&end_tm=24:00&is_immediately=1&month=&scan_speed=&spec_cycle=1&start_t 2023-09-14 16:36:18&targets=&task_name=Risk scan task-test&template_id=1&vpc_id=1&week=
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
```

`XML` format

```xml
Content-Type:application/xml <TaskRiskScanCreateResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
</TaskRiskScanCreateResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.22 TaskAssetImportDetailExists

Queries a list of assets that already exist from the results of an asset import task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetImportDetail Exists | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| asset typ _ e | Strin g | Body | No | IP | The asset type. Valid values: IP, WEBSITE, and DOMAIN. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries returned per page. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. |
| task insta _ nce id _ | Integ er | Body | No | 1 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -asset name _ | String | 1.1.1.1 | The asset name. |
| -asset source _ | String | Host import | The asset source. |
| -id | Integer | 1 | The asset ID. |
| -insert tm _ | Integer | 1620000000 | The time when the asset was imported. |
| -is deleted _ | Boolean | False | Indicates whether the asset is deleted. Valid values: True and False. |
| -is new _ | Integer | 1 | Indicates whether the asset is newly discovered. Valid values: 1: newly discovered. 0: not newly discovered. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The number of entries per page. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetImportDetailExists&RegionId=cnhangzhou&asset_type=IP&page=1&page_size=10&search=1_1_1_1_1&task_instance_id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "is_deleted":false,
            "asset_name":"1.1.1.1",
            "is_new":1,
            "asset_source":"Host import",
            "insert_tm":1620000000,
            "id":1
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskAssetImportDetailExistsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <asset_name>1.1.1.1</asset_name>
        <asset_source>Host import</asset_source>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>False</is_deleted>
        <is_new>1</is_new>
    </results>
</TaskAssetImportDetailExistsResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.23 TaskQueueTaskDetail

Queries the details of a task.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskQueueTaskDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Strin g | Body | No | 207 1 1 11 0 _ _ _ _ | The subtask ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| result | Map |   | The task details. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskQueueTaskDetail&RegionId=cn-hangzhou&id=207_1_1_11_0
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "result":""
```

`XML` format

```xml
Content-Type:application/xml <TaskQueueTaskDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <result></result>
</TaskQueueTaskDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.24 TaskAssetImportBaseInfo

Queries the basic information about an asset import task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskAssetImportBaseIn fo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| task insta _ nce id _ | Integ er | Body | No | 85 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| cycle count _ | Integer | 10 | The task cycle. |
| finish time _ | Integer | 1600000000 | The time when the task ended. |
| id | Integer | 1 | The task ID. |
| import count _ | Map |   | The number of imported assets. |
| import mode _ | String | MANUAL IMPORT _ | The import method. Valid values: MANUAL IMPORT and EXCEL IMPORT. _ _ |
| import res _ | Map |   | The imported data. |
| insert tm _ | Integer | 1600000000 | The time when the task was created. |
| is immediately _ | Integer | 1 | Indicates whether the task was run immediately after it was created. A value of 1 indicates that the task was run immediately after it was created. A value of 0 indicates that the task was not run immediately after it was created. |
| is public asset _ _ | Integer | 1 | Indicates whether the imported assets are public network assets. A value of 1 indicates that the assets are public network assets. A value of 0 indicates that the assets are not public network assets. |
| network type _ | Integer | 1 | The network type. This parameter is no longer used. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| not alive repo _ _ rt | Integer | 1 | Indicates whether non-alive assets were reported. A value of 1 indicates that non- alive assets were reported. A value of 0 indicates that non-alive assets were not reported. |
| process | String | 100% | The task progress. |
| screen shot _ | Integer | 1 | Indicates whether website screenshot is enabled. |
| start time _ | Integer | 1600000000 | The time when the task started. |
| status | String | INIT | The task status. Valid values: INIT, RUNNING, FINISH, and STOP. |
| target | Map |   | The imported assets. This parameter is no longer used. |
| task instance _ _ id | Integer | 1 | The task instance ID. |
| task name _ | String | Asset scan task- test | The task name. |
| template id _ | Integer | 1 | The template ID. |
| template nam _ e | String | Asset scan template-test | The template name. |
| username | String | admin | The username. |
| view detail _ | Map |   | The task details. A map or download link may be returned based on the import method. |
| vpc id _ | String | 1 | The virtual private cloud (VPC) ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskAssetImportBaseInfo&RegionId=cnhangzhou&task_instance_id=85
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle_count":10,
    "finish_time":1600000000,
    "id":1,
    "import_count":"",
    "import_mode":"MANUAL_IMPORT",
    "import_res":"",
    "insert_tm":1600000000,
    "is_immediately":1,
    "is_public_asset":1,
    "network_type":1,
    "not_alive_report":1,
    "process":"100%",
    "screen_shot":1,
    "start_time":1600000000,
    "status":"INIT",
    "target":"",
    "task_instance_id":1,
    "task_name":"Asset scan task-test",
    "template_id":1,
    "template_name":"Asset scan template-test",
    "username":"admin",
    "view_detail":"",
    "vpc_id":"1"
```

`XML` format

```xml
Content-Type:application/xml <TaskAssetImportBaseInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle_count>10</cycle_count>
    <finish_time>1600000000</finish_time>
    <id>1</id>
    <import_count></import_count>
    <import_mode>MANUAL_IMPORT</import_mode>
    <import_res></import_res>
    <insert_tm>1600000000</insert_tm>
    <is_immediately>1</is_immediately>
    <is_public_asset>1</is_public_asset>
    <network_type>1</network_type>
    <not_alive_report>1</not_alive_report>
    <process>100%</process>
    <screen_shot>1</screen_shot>
    <start_time>1600000000</start_time>
    <status>INIT</status>
    <target></target>
    <task_instance_id>1</task_instance_id>
    <task_name>Asset scan task-test</task_name>
    <template_id>1</template_id>
    <template_name>Asset scan template-test</template_name>
    <username>admin</username>
    <view_detail></view_detail>
    <vpc_id>1</vpc_id>
</TaskAssetImportBaseInfoResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.25 TaskRiskScanCycleRunning

Queries whether a risk scan task is running. This operation is supported by Cloud Security Scanner V3.4.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskRiskScanCycleRun ning | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskRiskScanCycleRunning&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

`XML` format

```xml
Content-Type:application/xml <TaskRiskScanCycleRunningResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</TaskRiskScanCycleRunningResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.26 GetAssetRiskScanTaskInfo

Queries the information about an asset scan task or a risk scan task. This operation is supported by Cloud Security Scanner V3.1.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:GetAssetRiskScanTaskI nfo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| id | Integ er | Body | No | 1 | The asset ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| month | Integer |   | The days of the month on which the task is run. Example: [1,2]. |
| week | Integer |   | The days of the week on which the task is run. Example: [1,2]. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| cycle | String | SPEC | The type of task cycle. Valid values: SPEC, MONTH, and WEEK. |
| end tm _ | String | 24:00 | The time when the task ends. Example: 24:00. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| is immediately _ | Integer | 1 | Indicates whether the task is run immediately after it is created. |
| scan speed _ | String |   | The scan speed. This parameter is no longer used. |
| spec cycle _ | Integer | 1 | The interval at which the task is run. Unit: day. |
| start tm _ | String | 2023-09-14 16:36:18 | The time when the task starts. Examples: 00:00 for a periodic task and 2023-09-14 16:36:18 for a one-time task. |
| targets | Map |   | The assets that are scanned. The value is in the JSON format. Example: {'ALL IP':0,'ALL WEBSITE':0,'ALL ASSET':0 _ _ _ ,'IP':[1],'WEBSITE':[1],'GROUP':[1]}. You can specify only one type of asset in the request. In the values of this parameter, an array indicates the asset IDs, 0 indicates selected, and 1 indicates not selected. |
| task name _ | String | test | The task name. |
| task type _ | Integer | 6 | The task type. |
| template id _ | Integer | 1 | The template ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetAssetRiskScanTaskInfo&RegionId=cn-hangzhou&id=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle":"SPEC",
    "end_tm":"24:00",
    "is_immediately":1,
    "scan_speed":"",
    "spec_cycle":1,
    "start_tm":"2023-09-14 16:36:18",
    "targets":"",
    "task_name":"test",
    "task_type":6,
    "template_id":1
```

`XML` format

```xml
Content-Type:application/xml <GetAssetRiskScanTaskInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle>SPEC</cycle>
    <end_tm>24:00</end_tm>
    <is_immediately>1</is_immediately>
    <month>
        <month></month>
    </month>
    <scan_speed></scan_speed>
    <spec_cycle>1</spec_cycle>
    <start_tm>2023-09-14 16:36:18</start_tm>
    <targets></targets>
    <task_name>test</task_name>
    <task_type>6</task_type>
    <template_id>1</template_id>
    <week>
        <week></week>
    </week>
</GetAssetRiskScanTaskInfoResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.27 BatchRestartTasks

Restarts multiple tasks at a time. This operation is supported by Cloud Security Scanner V3.2.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:BatchRestartTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The end of the time range. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| parent ta _ sk id _ | Integ er | Body | No |   |   |
| run types _ | Strin g | Body | No |   | The task execution mode. Valid values: cycle, once, and immediately. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks by task ID, task name, and asset address. |
| start time _ | Strin g | Body | No | 2020-01-01 00:00:00 | The beginning of the time range. |

|   |   |   |   | Cloud | Security Scanner Develop |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| statuses | Strin g | Body | No |   | The task status. Valid values: RUNNING, INIT, FINISH, and STOP. |
| task id _ | Integ er | Body | No | 1 | The task ID. |
| task ids _ | Strin g | Body | No |   | The task IDs. Example: [1,2,3]. |
| task types _ | Strin g | Body | No |   | The task type. Valid values: assetImport, assetRisk, and assetScan. |
| template | Integ er | Body | No | 1 | The template. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -task id _ | Integer | 173 | The task ID. |
| - task instance _ _ id | Integer | 208 | The task instance ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=BatchRestartTasks&RegionId=cn-hangzhou&end_time=2020-01-01 0 0:00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00& statuses=&task_id=1&task_ids=&task_types=&template=1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "task_instance_id":208,
            "task_id":173
```

`]` `XML` format

```xml
Content-Type:application/xml <BatchRestartTasksResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
</BatchRestartTasksResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.28 TaskQueueTaskList

Queries a list of tasks.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskQueueTaskList | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| search | Strin g | Body | No | 1 1 1 1 1 _ _ _ _ | The filter conditions. You can filter tasks only by subtask ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -group id _ | Integer | 0 | The device group ID. |
| -id | String | 0 11 0 _ _ | The queue name. |
| -list type _ | String | asset list _ | The queue type. Valid values: asset list _ and vuln list. _ |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The total number of tasks. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskQueueTaskList&RegionId=cnhangzhou&page=1&page_size=10&search=1_1_1_1_1
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "list_type":"asset_list",
            "group_id":0,
            "id":"0_11_0"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskQueueTaskListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <group_id>0</group_id>
        <id>0_11_0</id>
        <list_type>asset_list</list_type>
    </results>
</TaskQueueTaskListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.29 TaskQueueTaskInfo

Queries the information about the tasks in queues.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskQueueTaskInfo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| mode | Integ er | Body | No | 1 | The task status. Valid values: 0: waiting. 1: running. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -insert tm _ | Integer | 1722477664 | The time when the task was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - task instance _ _ id | Integer | 206 | The task instance ID. |
| -task name _ | String | dd | The task name. |
| -task pri _ | String | high | The task priority. Valid values: emergent, high, mid, and low. |
| -task run num _ _ | Integer | 1 | The number of tasks that are running. |
| -task type _ | String | asset monitor task _ _ | The task type. |
| - task wait num _ _ | Integer | 2 | The number of pending tasks. |

| r | Cloud Security Sca Guide·Cloud Sec | nner Develope urity Scanner |   |   |   |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -username | String | admin | The name of the user. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The total number of tasks. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskQueueTaskInfo&RegionId=cnhangzhou&mode=1&page=1&page_size=10
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "task_name":"dd",
            "task_wait_num":2,
            "task_instance_id":206,
            "insert_tm":1722477664,
            "task_type":"asset_monitor_task",
            "task_run_num":1,
            "task_pri":"high",
            "username":"admin"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskQueueTaskInfoResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <insert_tm>1722477664</insert_tm>
        <task_instance_id>206</task_instance_id>
        <task_name>dd</task_name>
        <task_pri>high</task_pri>
        <task_run_num>1</task_run_num>
        <task_type>asset_monitor_task</task_type>
        <task_wait_num>2</task_wait_num>
        <username>admin</username>
    </results>
</TaskQueueTaskInfoResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.30 TaskStatusStats

Queries the statistics on task status. This operation is supported by Cloud Security Scanner V3.4.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskStatusStats | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Array |   |   |
| -count | Integer | 10 | The number of tasks. |
| -status | String | RUNNING | The task status. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskStatusStats&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
            "count":10,
            "status":"RUNNING"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskStatusStatsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <count>10</count>
        <status>RUNNING</status>
    </data>
</TaskStatusStatsResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.31 TaskQueueTaskListDetail

Queries the details of the tasks in queues.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskQueueTaskListDet ail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| list name _ | Strin g | Body | No | 0 11 0 _ _ | The queue name. |
| page | Integ er | Body | No | 1 | The page number. |
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -id | String | 208 1 1 11 0 _ _ _ _ | The task ID. |

| Cloud Security Sca | nner Develope |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -list type _ | String | asset monitor task _ _ | The task type. Valid values: asset import task, asset monitor task, _ _ _ _ basic monitor task, and vuln verify task. _ _ _ _ |
| -name | String | dd | The task name. |
| -task level _ | String | high | The task priority. Valid values: emergent, high, mid, and low. |
| -user name _ | String | admin | The username. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| count | Integer |   | The total number of tasks. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskQueueTaskListDetail&RegionId=cnhangzhou&list_name=0_11_0&page=1&page_size=10
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
            "list_type":"asset_monitor_task",
            "user_name":"admin",
            "name":"dd",
            "id":"208_1_1_11_0",
            "task_level":"high"
```

`]` `XML` format

```xml
Content-Type:application/xml <TaskQueueTaskListDetailResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <id>208_1_1_11_0</id>
        <list_type>asset_monitor_task</list_type>
        <name>dd</name>
        <task_level>high</task_level>
        <user_name>admin</user_name>
    </results>
</TaskQueueTaskListDetailResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.32 TaskRunTypeStats

Queries the statistics on task execution modes. This operation is supported by Cloud Security Scanner V3.4.0 and later.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskRunTypeStats | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| cycle | Integer | 10 | The number of tasks that are periodically run. |
| immediately | Integer | 10 | The number of tasks that are run immediately after they are created. |
| once | Integer | 10 | The number of tasks that are run at the specified time. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskRunTypeStats&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle":10,
    "immediately":10,
    "once":10
```

`XML` format

```xml
Content-Type:application/xml <TaskRunTypeStatsResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle>10</cycle>
    <immediately>10</immediately>
    <once>10</once>
</TaskRunTypeStatsResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.33 TaskQueueTaskCount

Queries the statistics on tasks.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:TaskQueueTaskCount | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| await | Integer | 7 | The number of pending tasks. |
| run | Integer | 2 | The number of tasks that are running. |
| task queue _ | Integer | 1 | The number of task queues. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=TaskQueueTaskCount&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "await":7,
    "run":2,
    "task_queue":1
```

`XML` format

```xml
Content-Type:application/xml <TaskQueueTaskCountResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <await>7</await>
    <run>2</run>
    <task_queue>1</task_queue>
</TaskQueueTaskCountResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

#### 5.2.34 SuspendStatus

Queries the task status.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:SuspendStatus | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| data | String |   | The task status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=SuspendStatus&RegionId=cn-hangzhou
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":""
```

`XML` format

```xml
Content-Type:application/xml <SuspendStatusResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data></data>
</SuspendStatusResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

## 6 Vulnerability Scan V2

### 6.1 Asset API

#### 6.1.1 Host assets

##### 6.1.1.1 DescribeHostAssetList

Retrieves a list of host assets.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeHostAssetList | Read | acs:yundun-scanner:: {#accountId}: |

**Rate limit**

Single-user rate limit: 10 queries per second (QPS). API rate limit: 100 QPS.

**Request headers**

This operation uses common request headers and has no special request headers. For more information, see common parameters.

**Request parameters**

| Parameter | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | vpc- l0miygn8aj171l811 5eg1 | The VPC ID. |
| group ids _ | String | body | No | [1, 2] | The asset group IDs. |
| staff ids _ | String | body | No | [1, 2] | The asset owner IDs. |
| tag ids _ | String | body | No | [11, 22] | The IDs of the asset tags. |
| is alive _ | Boolean | body | No | true | Specifies whether to query only for assets that are online. |

| asset source _ | String | body | No | ["AUTO", "MANUAL"] | The source of the assets. MANUAL : manually added. AUTO : automatically discovered. |
|---|---|---|---|---|---|
| changings | String | body | No | ["NEW", "UPDATED"] | The change status of the assets. NEW : newly discovered. UPDATED : updated. SAME : unchanged. OFFLINE : offline. |
| device types _ | String | body | No | ["net product- _ server", "net product- _ router"] | The device types. |
| fingerprints | String | body | No | ["PHP", "Apache"] | The asset fingerprints. |
| host port _ | String | body | No | [22, 3306] | The host ports. |
| host service _ | String | body | No | ["ssh", "http"] | The host services. |
| insert tm en _ _ d | String | body | No | 2024-02-04 00:00:00 | The end of the asset creation time range. |
| insert tm sta _ _ rt | String | body | No | 2024-01-04 00:00:00 | The beginning of the asset creation time range. |
| is cdn _ | Boolean | body | No | true | Specifies whether the asset is behind a Content Delivery Network (CDN). |
| os | String | body | No | ["Ubuntu", "Debian"] | The operating system. |
| page | Integer | body | No | 1 | The page number. |
| page size _ | Integer | body | No | 20 | The page size. Default value: 20. |

|   | UPDATED |
|---|---|
| SAME |   |

| risk levels _ | String | body | No | ["HIGH","MIDDLE"] | The risk levels of the assets. HIGH : High risk MIDDLE : Medium risk LOW : Low risk HEALTH : Secure |
|---|---|---|---|---|---|
| search | String | body | No | 192.168 | The keyword for a fuzzy search. You can search for assets by asset name or IP address. |
| update tm e _ _ nd | String | body | No | 2024-02-04 00:00:00 | The end of the asset update time range. |
| update tm st _ _ art | String | body | No | 2024-01-04 00:00:00 | The beginning of the asset update time range. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The ID of the request, which is a unique identifier generated by Alibaba Cloud. You can use this ID to troubleshoot issues. |
| count | Integer | 10 | The total number of entries returned. |
| results | Array |   | The list of host assets. |
| results[].vpc id _ | String | vpc- l0miygn8aj171l8115eg 1 | The VPC ID. |
| results[].asset id _ | Integer | 123 | The asset ID. |
| results[].group id _ | Integer | 1 | The asset group ID. |
| results[].asset name _ | String | 192.168.100.100 | The asset name. |

| results[].group name _ | String | this is a group name | The asset group name. |
|---|---|---|---|
| results[].asset type _ | String | IP | The asset type. |
| results[].status | String | OK | The asset status. |
| results[].risk level _ | String | HIGH | The asset risk level. |
| results[].changing | String | NEW | The change status of the asset. |
| results[].is alive _ | Integer | 1 | The online status of the asset. A value of 1 means the asset is online. |
| results[].hostname | String | 192.168.100.100 | The hostname. |
| results[].service count _ | Integer | 100 | The number of open ports. |
| results[].risk count _ | Integer | 100 | The number of security vulnerabilities. |
| results[].compliance ri _ sk count _ | Integer | 100 | The number of compliance vulnerabilities. |
| results[].remark | String | this is a reremark | The remark. |
| results[].cdn | String |   | Information about the CDN. |
| results[].finger print _ | Array | [{}] | The asset fingerprint. |
| results[].asset tags _ | Array | [{"tag id": 11, _ "tag name": "EIP"}] _ | The asset tags. |
| results[].asset tags[].t _ ag id _ | Integer | 11 | The asset tag ID. |

| results[].asset tags[].t _ ag name _ | String | EIP | The tag name. |
|---|---|---|---|
| results[].staff | Object | {} | The owner information. |
| results[].asset source _ | String | System Discovered | The asset source. |
| results[].device types _ | Array | [""] | The device types. |
| results[].os | String | Ubuntu | The operating system. |
| results[].insert tm _ | Integer | 1774428275 | The timestamp when the asset was added. Unit: seconds. |
| results[].scan tm _ | Integer | 1774428275 | The timestamp of the last scan. Unit: seconds. |
| results[].update tm _ | Integer | 1774428275 | The timestamp of the last update. Unit: seconds. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DescribeHostAssetList&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "vpc-l0miygn8aj171l8115eg1",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
    11,
```

`],`

```json
  "is_alive": true,
  "asset_source": [
    "AUTO",
    "MANUAL"
```

`]` `],`

```json
  "changings": [
    "NEW",
    "UPDATED"
```

`],`

```json
  "device_types": [
    "net_product-server",
    "net_product-router"
```

`],`

```json
  "fingerprints": [
    "PHP",
    "Apache"
```

`],`

```json
  "host_port": [
    22,
```

`],`

```json
  "host_service": [
    "ssh",
    "http"
```

`],`

```json
  "insert_tm_end": "2024-02-04 00:00:00",
  "insert_tm_start": "2024-01-04 00:00:00",
  "is_cdn": true,
  "os": [
    "Ubuntu",
    "Debian"
```

`],`

```json
  "page": 1,
  "page_size": 20,
  "risk_levels": [
    "HIGH",
    "MIDDLE"
```

`],`

```json
  "search": "",
  "update_tm_end": "2024-02-04 00:00:00",
  "update_tm_start": "2024-01-04 00:00:00"
```

Response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
      "vpc_id": "vpc-l0miygn8aj171l8115eg1",
      "asset_id": 123,
      "group_id": 1,
      "asset_name": "192.168.100.100",
      "group_name": "this is a group name",
      "asset_type": "IP",
      "status": "OK",
      "risk_level": "HIGH",
      "changing": "NEW",
      "is_alive": 1,
      "hostname": "192.168.100.100",
      "service_count": 100,
      "risk_count": 100,
      "compliance_risk_count": 100,
      "remark": "this is a reremark",
      "cdn": "",
      "finger_print": [
```

`{}` `],`

```json
      "asset_tags": [
          "tag_id": 11,
          "tag_name": "EIP"
```

`],`

```json
      "staff": {},
      "asset_source": "System Discovered",
      "device_types": [
```

`""` `],`

```json
      "os": "Ubuntu",
      "insert_tm": 1774428275,
      "scan_tm": 1774428275,
      "update_tm": 1774428275
```

`]` `XML` format

```xml
Content-Type:application/xml <DescribeHostAssetListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <vpc_id>vpc-l0miygn8aj171l8115eg1</vpc_id>
            <asset_id>123</asset_id>
            <group_id>1</group_id>
            <asset_name>192.168.100.100</asset_name>
            <group_name>this is a group name</group_name>
            <asset_type>IP</asset_type>
            <status>OK</status>
            <risk_level>HIGH</risk_level>
            <changing>NEW</changing>
            <is_alive>1</is_alive>
            <hostname>192.168.100.100</hostname>
            <service_count>100</service_count>
            <risk_count>100</risk_count>
            <compliance_risk_count>100</compliance_risk_count>
            <remark>this is a reremark</remark>
            <cdn></cdn>
            <finger_print>
                <item></item>
            </finger_print>
            <asset_tags>
                <item>
                    <tag_id>11</tag_id>
                    <tag_name>EIP</tag_name>
                </item>
            </asset_tags>
            <staff></staff>
            <asset_source>System Discovered</asset_source>
            <device_types>
                <item></item>
            </device_types>
            <os>Ubuntu</os>
            <insert_tm>1774428275</insert_tm>
            <scan_tm>1774428275</scan_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
</DescribeHostAssetListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| 500 | 101 | server-side passthrough | An internal error occurred. This error is passed through from a backend service. |
|---|---|---|---|

#### 6.1.2 Website assets

##### 6.1.2.1 DescribeWebsiteAssetList

Retrieves a list of your website assets.

**Authorization information**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeWebsiteAssetL ist | Read | acs:yundun-scanner:: {#accountId}: |

**Throttling**

The request rate for a single user is limited to 10 queries per second (QPS). The total request rate for this API is limited to 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Locatio n | Require d | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | vpc- l0miygn8aj171l811 5eg1 | The ID of the VPC. |
| group ids _ | String | body | No | [1, 2] | The ID of the asset group. This parameter is a JSON array of integers. |
| staff ids _ | String | body | No | [1, 2] | The ID of the asset owner. This parameter is a JSON array of integers. |
| tag ids _ | String | body | No | [11, 22] | The ID of the asset tag. This parameter is a JSON array of integers. |

| website type _ | String | body | No | ["IP", "DOMAIN"] | The website type. This parameter is a JSON array of strings. Valid values: DOMAIN : Domain- based websites. IP : IP-based websites. |
|---|---|---|---|---|---|
| is alive _ | Boolea n | body | No | true | Filters assets by their liveness status. A value of true returns only online assets. |
| asset source _ | String | body | No | ["AUTO", "MANUAL"] | The asset source. This parameter is a JSON array of strings. Valid values: MANUAL : Assets that are manually added. |
| changings | String | body | No | ["NEW", "UPDATED"] | The type of asset change. This parameter is a JSON array of strings. Valid values: NEW : Newly detected. UPDATED : Updated. SAME : Unchanged. OFFLINE : Offline. |
| fingerprints | String | body | No | ["PHP", "Apache"] | The asset fingerprints to filter by. This parameter is a JSON array of strings. |
| insert tm end _ _ | String | body | No | 2024-02-04 00:00:00 | The end of the time range for filtering by asset import time. The time is in the yyyy-MM-dd HH:mm:ss format. |
| insert tm start _ _ | String | body | No | 2024-01-04 00:00:00 | The start of the time range for filtering by asset import time. The time is in the yyyy-MM-dd HH:mm:ss format. |

| is waf _ | Boolea n | body | No | true | Filters for assets with WAF protection. A value of true returns only assets that are protected by a WAF. |
|---|---|---|---|---|---|
| page | Integer | body | No | 1 | The page number. |
| page size _ | Integer | body | No | 20 | The number of entries to return on each page. |
| risk levels _ | String | body | No | ["HIGH","MIDDLE"] | The risk levels to filter by. This parameter is a JSON array of strings. Valid values: HIGH : High MIDDLE : Medium LOW : Low HEALTH : Healthy |
| search | String | body | No | https://163.com | The content to search for. This can be a domain or an IP address. |
| status codes _ | String | body | No | [403, 404] | The website HTTP status codes to filter by. This parameter is a JSON array of integers. |
| update tm end _ _ | String | body | No | 2024-02-04 00:00:00 | The end of the time range for filtering by asset update time. The time is in the yyyy-MM-dd HH:mm:ss format. |
| update tm start _ _ | String | body | No | 2024-01-04 00:00:00 | The start of the time range for filtering by asset update time. The time is in the yyyy-MM-dd HH:mm:ss format. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID generated for the request. This ID is used for troubleshooting. |
|---|---|---|---|
| count | Integer | 10 | The total number of entries returned. |
| results | Array |   | The list of website assets. |
| results[].vpc id _ | String | vpc- l0miygn8aj171l8115eg 1 | The ID of the VPC. |
| results[].asset id _ | Integer | 123 | The asset ID. |
| results[].group id _ | Integer | 1 | The group ID. |
| results[].asset name _ | String | 192.168.100.100 | The asset name. |
| results[].group name _ | String | this is a group name | The group name. |
| results[].asset type _ | String | IP | The asset type. |
| results[].website type _ | String | DOMAIN | The website type. |
| results[].status | String | OK | The status. |
| results[].risk level _ | String | HIGH | The risk level. |
| results[].changing | String | NEW | The type of asset change. |
| results[].is alive _ | Integer | 1 | The liveness status. A value of 1 indicates online, and 0 indicates offline. |
| results[].service | String | Grafana | The service detected on the website. |

| results[].risk count _ | Integer | 100 | The number of security vulnerabilities. |
|---|---|---|---|
| results[].compliance ri _ sk count _ | Integer | 100 | The number of compliance vulnerabilities. |
| results[].title | String | this is a title | The website title. |
| results[].custom title _ | String |   | The custom title. |
| results[].remark | String | this is a remark | The remark. |
| results[].waf | Boolean | true | Indicates whether the website is protected by a WAF. |
| results[].finger print _ | Array | [{}] | The asset fingerprint information. |
| results[].asset tags _ | Array | [{"tag id": 11, _ "tag name": "EIP"}] _ | The asset tags. |
| results[].asset tags[].t _ ag id _ | Integer | 11 | The asset tag ID. |
| results[].asset tags[].t _ ag name _ | String | EIP | The tag name. |
| results[].staff | Object | {} | The information of the asset owner. |
| results[].asset source _ | String | System Discovered | The source of the asset. |
| results[].screenshot | String |   | The website screenshot, encoded in Base64. |
| results[].status code _ | Integer | 200 | The HTTP status code of the website. |

| results[].insert tm _ | Integer | 1774428275 | The time the asset was imported. This value is a timestamp. |
|---|---|---|---|
| results[].scan tm _ | Integer | 1774428275 | The scan time. This value is a timestamp. |
| results[].update tm _ | Integer | 1774428275 | The time the asset was last updated. This value is a timestamp. |

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=DescribeWebsiteAssetList&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "vpc-l0miygn8aj171l8115eg1",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
    11,
```

`],`

```json
  "website_type": [
    "IP",
    "DOMAIN"
```

`],`

```json
  "is_alive": true,
  "asset_source": [
    "AUTO",
    "MANUAL"
```

`],`

```json
  "changings": [
    "NEW",
    "UPDATED"
```

`],`

```json
  "fingerprints": [
    "PHP",
    "Apache"
```

`],`

```json
  "insert_tm_end": "2024-02-04 00:00:00",
  "insert_tm_start": "2024-01-04 00:00:00",
  "is_waf": true,
  "page": 1,
  "page_size": 20,
  "risk_levels": [
    "HIGH",
    "MIDDLE"
```

`],`

```json
  "search": "",
  "status_codes": [
    403,
```

`],`

```json
  "update_tm_end": "2024-02-04 00:00:00",
  "update_tm_start": "2024-01-04 00:00:00"
```

Sample response `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
      "vpc_id": "vpc-l0miygn8aj171l8115eg1",
      "asset_id": 123,
      "group_id": 1,
      "asset_name": "192.168.100.100",
      "group_name": "this is a group name",
      "asset_type": "IP",
      "website_type": "DOMAIN",
      "status": "OK",
      "risk_level": "HIGH",
      "changing": "NEW",
      "is_alive": 1,
      "service": "Grafana",
      "risk_count": 100,
      "compliance_risk_count": 100,
      "title": "this is a title",
      "custom_title": "",
      "remark": "this is a reremark",
      "waf": true,
      "finger_print": [
```

`{}` `],`

```json
      "asset_tags": [
          "tag_id": 11,
          "tag_name": "EIP"
```

`],`

```json
      "staff": {},
      "asset_source": "System Discovered",
      "screenshot": "",
      "status_code": 200,
      "insert_tm": 1774428275,
      "scan_tm": 1774428275,
      "update_tm": 1774428275
```

`]` `XML` format

```xml
Content-Type:application/xml <DescribeWebsiteAssetListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <vpc_id>vpc-l0miygn8aj171l8115eg1</vpc_id>
            <asset_id>123</asset_id>
            <group_id>1</group_id>
            <asset_name>192.168.100.100</asset_name>
            <group_name>this is a group name</group_name>
            <asset_type>IP</asset_type>
            <website_type>DOMAIN</website_type>
            <status>OK</status>
            <risk_level>HIGH</risk_level>
            <changing>NEW</changing>
            <is_alive>1</is_alive>
            <service>Grafana</service>
            <risk_count>100</risk_count>
            <compliance_risk_count>100</compliance_risk_count>
            <title>this is a title</title>
            <custom_title></custom_title>
            <remark>this is a reremark</remark>
            <waf>true</waf>
            <finger_print>
                <item></item>
            </finger_print>
            <asset_tags>
                <item>
                    <tag_id>11</tag_id>
                    <tag_name>EIP</tag_name>
                </item>
            </asset_tags>
            <staff></staff>
            <asset_source>System Discovered</asset_source>
            <screenshot></screenshot>
            <status_code>200</status_code>
            <insert_tm>1774428275</insert_tm>
            <scan_tm>1774428275</scan_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
</DescribeWebsiteAssetListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|

| 500 | 101 | An internal server error occurred. | The server encountered an internal error and could not complete your request. |
|---|---|---|---|

#### 6.1.3 Domain name assets

##### 6.1.3.1 DescribeDomainAssetList

Queries a list of domain assets.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeDomainAssetL ist | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

A single user is limited to 10 queries per second (QPS). This API is limited to a total of 100 QPS across all users.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | In | Required | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | vpc- l0miygn8aj17 1l8115eg1 | The ID of the VPC. |
| group ids _ | String | body | No | [1, 2] | An array of asset group IDs. |
| staff ids _ | String | body | No | [1, 2] | An array of staff IDs. |
| tag ids _ | String | body | No | [11, 22] | An array of asset tag IDs. |
| is alive _ | Boolean | body | No | true | Specifies whether the asset is alive. |

| parse status _ | String | body | No | ["FAILED", "SUCCESS"] | The domain resolution status. Valid values: FAILED : The resolution failed. SUCCESS : The resolution succeeded. |   |   |
|---|---|---|---|---|---|---|---|
| asset source _ | String | body | No | ["AUTO", "MANUAL"] | The asset source. Valid values: MANUAL : The asset was manually added. AUTO : The asset was automatically discovered. |   |   |
| changings | String | body | No | ["NEW", "UPDATED"] | The type of asset change. Valid values: NEW : The asset is newly discovered. UPDATED : The asset has been updated. SAME : The asset has not changed. OFFLINE : The asset is offline. |   |   |
| insert tm en _ _ d | String | body | No | 2024-02-04 00:00:00 | The end of the creation time range. Specify the time in the yyyy-MM-dd HH:mm:ss format. |   |   |
|   |   |   |   |   |   | yyyy-MM-dd |   |
| insert tm sta _ _ rt | String | body | No | 2024-01-04 00:00:00 | The start of the creation time range. Specify the time in the yyyy-MM-dd HH:mm:ss format. |   |   |
|   |   |   |   |   |   | yyyy-MM-dd |   |
| is cdn _ | Boolean | body | No | true | Specifies whether a CDN is used for the domain asset. |   |   |
| is wildcard _ | Boolean | body | No | true | Specifies whether the asset is a wildcard domain. |   |   |
| page | Integer | body | No | 1 | The page number. |   |   |

|   | HH:mm:ss |
|---|---|

|   | HH:mm:ss |
|---|---|

| page size _ | Integer | body | No | 20 | The number of entries per page. |   |
|---|---|---|---|---|---|---|
| risk levels _ | String | body | No | ["HIGH", "MIDDLE"] | An array of risk levels. Valid values: HIGH MIDDLE LOW HEALTH |   |
| search | String | body | No | baidu.com | A keyword for a fuzzy search by domain name or IP address. |   |
| update tm e _ _ nd | String | body | No | 2024-02-04 00:00:00 | The end of the update time range. Specify the time in the yyyy-MM-dd HH:mm:ss format. |   |
| update tm st _ _ art | String | body | No | 2024-01-04 00:00:00 | The start of the update time range. Specify the time in the yyyy-MM-dd HH:mm:ss format. |   |

|   | HH:mm:ss |
|---|---|

|   | HH:mm:ss |
|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. This unique identifier is generated by Alibaba Cloud and can be used to troubleshoot issues. |
| count | Integer | 10 | The total count of domain assets that match the filter conditions. |
| results | Array |   | An array of domain asset objects. |
| results[].vpc id _ | String | vpc- l0miygn8aj171l8115eg 1 | The ID of the VPC. |

| results[].asset id _ | Integer | 123 | The asset ID. |
|---|---|---|---|
| results[].group id _ | Integer | 1 | The ID of the asset group. |
| results[].asset name _ | String | 192.168.100.100 | The asset name. |
| results[].group name _ | String | Default Group | The name of the asset group. |
| results[].asset type _ | String | IP | The asset type. |
| results[].status | String | OK | The asset status. |
| results[].risk level _ | String | HIGH | The risk level of the asset. |
| results[].changing | String | NEW | Asset change type |
| results[].is alive _ | Integer | 1 | The liveness status. A value of 1 indicates that the asset is alive. A value of 0 indicates that it is not. |
| results[].hostname | String | 192.168.100.100 | The hostname. |
| results[].remark | String | This is a remark. | Remarks for the asset. |
| results[].parsed | String |   | The domain resolution status. |
| results[].parse err _ | String | Domain resolution timed out. | The reason for a domain resolution failure. |
| results[].cdn | String | Alibaba Cloud | The CDN provider. |
| results[].asset tags _ | Array | [{"tag id": 11, _ "tag name": "EIP"}] _ | An array of asset tag objects. |

| results[].asset tags[].t _ ag id _ | Integer | 11 | The ID of the asset tag. |
|---|---|---|---|
| results[].asset tags[].t _ ag name _ | String | EIP | The name of the tag. |
| results[].staff | Object | {} | Information about the staff assigned to the asset. |
| results[].domain parse _ d | Array | [{"id": 123, "ip": "192.168.131.100", "insert tm": _ 1774428275, "update tm": _ 1774428275}] | The DNS records for the domain. |
| results[].domain parse _ d[].id | Integer | 123 | The ID of the DNS record. |
| results[].domain parse _ d[].ip | String | 192.168.131.100 | The IP address that the domain resolves to. |
| results[].domain parse _ d[].insert tm _ | Integer | 1774428275 | The time when the record was created. This value is a Unix timestamp. |
| results[].domain parse _ d[].update tm _ | Integer | 1774428275 | The time when the record was last updated. This value is a Unix timestamp. |
| results[].parsed histor _ y | Array | [{"id": 123, "ip": "192.168.131.100", "insert tm": _ 1774428275, "update tm": _ 1774428275}] | The DNS record history. |
| results[].parsed histor _ y[].id | Integer | 123 | The ID of the DNS record. |
| results[].parsed histor _ y[].ip | String | 192.168.131.100 | The IP address that the domain resolves to. |

| results[].parsed histor _ y[].insert tm _ | Integer | 1774428275 | The time when the record was created. This value is a Unix timestamp. |
|---|---|---|---|
| results[].parsed histor _ y[].update tm _ | Integer | 1774428275 | The time when the record was last updated. This value is a Unix timestamp. |
| results[].asset source _ | String | AUTO | The asset source. |
| results[].pan domain _ | Integer | 1 | Indicates whether the asset is a wildcard domain. A value of 1 indicates that it is a wildcard domain, and a value of 0 means it is not. |
| results[].insert tm _ | Integer | 1774428275 | The time when the asset was created. This value is a Unix timestamp. |
| results[].scan tm _ | Integer | 1774428275 | The time when the asset was last scanned. This value is a Unix timestamp. |
| results[].update tm _ | Integer | 1774428275 | The time when the asset was last updated. This value is a Unix timestamp. |

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=DescribeDomainAssetList&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "vpc-l0miygn8aj171l8115eg1",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
    11,
```

`],`

```json
  "is_alive": true,
  "parse_status": [
    "FAILED",
    "SUCCESS"
```

`],`

```json
  "asset_source": [
    "AUTO",
    "MANUAL"
```

`],`

```json
  "changings": [
    "NEW",
    "UPDATED"
```

`],`

```json
  "insert_tm_end": "2024-02-04 00:00:00",
  "insert_tm_start": "2024-01-04 00:00:00",
  "is_cdn": true,
  "is_wildcard": true,
  "page": 1,
  "page_size": 20,
  "risk_levels": [
    "HIGH",
    "MIDDLE"
```

`],`

```json
  "search": "",
  "update_tm_end": "2024-02-04 00:00:00",
  "update_tm_start": "2024-01-04 00:00:00"
```

Sample responses `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
```

```json
  "count": 10,
  "results": [
      "vpc_id": "vpc-l0miygn8aj171l8115eg1",
      "asset_id": 123,
      "group_id": 1,
      "asset_name": "192.168.100.100",
      "group_name": "Default Group",
      "asset_type": "IP",
      "status": "OK",
      "risk_level": "HIGH",
      "changing": "NEW",
      "is_alive": 1,
      "hostname": "192.168.100.100",
      "remark": "This is a remark.",
      "parsed": "",
      "parse_err": "Domain resolution timed out.",
      "cdn": "Alibaba Cloud",
      "asset_tags": [
          "tag_id": 11,
          "tag_name": "EIP"
```

`],`

```json
      "staff": {},
      "domain_parsed": [
          "id": 123,
          "ip": "192.168.131.100",
          "insert_tm": 1774428275,
          "update_tm": 1774428275
```

`],`

```json
      "parsed_history": [
          "id": 123,
          "ip": "192.168.131.100",
          "insert_tm": 1774428275,
          "update_tm": 1774428275
```

`],`

```json
      "asset_source": "AUTO",
      "pan_domain": 1,
      "insert_tm": 1774428275,
      "scan_tm": 1774428275,
      "update_tm": 1774428275
```

`]` `XML` format

```
Content-Type:application/xml
```

```xml
Cotet ype:app cato/ <DescribeDomainAssetListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <vpc_id>vpc-l0miygn8aj171l8115eg1</vpc_id>
            <asset_id>123</asset_id>
            <group_id>1</group_id>
            <asset_name>192.168.100.100</asset_name>
            <group_name>Default Group</group_name>
            <asset_type>IP</asset_type>
            <status>OK</status>
            <risk_level>HIGH</risk_level>
            <changing>NEW</changing>
            <is_alive>1</is_alive>
            <hostname>192.168.100.100</hostname>
            <remark>This is a remark.</remark>
            <parsed></parsed>
            <parse_err>Domain resolution timed out.</parse_err>
            <cdn>Alibaba Cloud</cdn>
            <asset_tags>
                <item>
                    <tag_id>11</tag_id>
                    <tag_name>EIP</tag_name>
                </item>
            </asset_tags>
            <staff></staff>
            <domain_parsed>
                <item>
                    <id>123</id>
                    <ip>192.168.131.100</ip>
                    <insert_tm>1774428275</insert_tm>
                    <update_tm>1774428275</update_tm>
                </item>
            </domain_parsed>
            <parsed_history>
                <item>
                    <id>123</id>
                    <ip>192.168.131.100</ip>
                    <insert_tm>1774428275</insert_tm>
                    <update_tm>1774428275</update_tm>
                </item>
            </parsed_history>
            <asset_source>AUTO</asset_source>
            <pan_domain>1</pan_domain>
            <insert_tm>1774428275</insert_tm>
            <scan_tm>1774428275</scan_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
</DescribeDomainAssetListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Internal server error. | An internal server error occurred. The error is passed from a backend service. |

#### 6.1.4 DeleteAsset

Deletes one or more assets.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun-scanner:DeleteAsset | Not specified | acs:yundun-scanner:: {#accountId}: |

**Rate limiting**

Rate limit per user: 10 queries per second (QPS). Rate limit for this API: 100 QPS.

**Request header**

This operation uses common request headers. For more information, see Common Request Parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| add white _ | Integer | body | No | 1 | Whether to add the asset to the whitelist. |
| ids | Array | body | No | [123, 456] | A list of asset IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique request ID generated by Alibaba Cloud. Use this ID to troubleshoot issues. |
|---|---|---|---|

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DeleteAsset&RegionId=cn-hangzhou Content-Type: application/json
  "add_white": 1,
  "ids": [
    123,
```

`]` Successful response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************"
```

`XML` format

```xml
Content-Type:application/xml <DeleteAssetResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
</DeleteAssetResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side passthrough | server-side passthrough |

### 6.2 Task API

#### 6.2.1 Asset import task

##### 6.2.1.1 CreateAssetImportTask

Creates an asset import task.

**Authorization**

| Actions | Access Level | Resource Type |
|---|---|---|
| yundun- scanner:CreateAssetImportTask | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Calls from a single user are limited to 10 queries per second (QPS). Calls to this API are limited to 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | In | Required | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | vpc 1 _ | The VPC ID. |
| template id _ | Integer | body | No | 1 | The template ID. |
| group id _ | Integer | body | No | 0 | The asset group ID. A value of 0 indicates the default group. |
| staff id _ | Integer | body | No | 1 | The owner ID. |
| tag ids _ | String | body | No | [1, 2, 3] | A list of tag IDs. |
| task name _ | String | body | Yes | Risk-Scan- Task-Test | The task name. |

| network type _ | Integer | body | No | 1 | Specifies the network type. Valid values include: - 1 : public network - 2 : private network |
|---|---|---|---|---|---|
| is immediatel _ y | Integer | body | No | 1 | Specifies whether to execute the task immediately. Valid values: 1 (Yes) and 0 (No). |
| is public asse _ _ t | Integer | body | No | 1 | Specifies whether the asset is on a public network. Valid values: 1 (Yes) and 0 (No). |
| asset metada _ tas | String | body | No | [{"hostName" : "xxlsk", "ip": "1.1.1.1", "instanceId": "xxx ss", _ "instanceNam e": "xxx ss", _ "osType": "linux"}] | A JSON- formatted string that contains an array of asset metadata objects. |

| not alive rep _ _ ort | Integer | body | No | 1 | Specifies whether to report inactive assets. Valid values include: - 1 : Report - 0 : Do not report |
|---|---|---|---|---|---|
| screen shot _ | Integer | body | No | 1 | Specifies whether to enable website screenshots. Valid values include: - 1 : Enable - 0 : Disable |
| start tm _ | String | body | No | 2020-01-01 00:00:00 | The time when the task is scheduled to start. The value must be in the 'YYYY-MM-DD hh:mm:ss' format. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID generated by Alibaba Cloud for this request. Use this ID to troubleshoot issues. |
| task instance id _ _ | Integer | 1 | The task instance ID. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=CreateAssetImportTask&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "1",
  "template_id": 1,
  "group_id": 0,
  "staff_id": 1,
  "tag_ids": [
```

`1,` `2,` `],`

```json
  "task_name": "Risk-Scan-Task-Test",
  "network_type": 1,
  "is_immediately": 1,
  "is_public_asset": 1,
  "asset_metadatas": [
      "hostName": "xxlsk",
      "ip": "1.1.1.1",
      "instanceId": "xxx_ss",
      "instanceName": "xxx_ss",
      "osType": "linux"
```

`],`

```json
  "not_alive_report": 1,
  "screen_shot": 1,
  "start_tm": "2020-01-01 00:00:00"
```

Successful response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "task_instance_id": 1
```

`XML` format

```xml
Content-Type:application/xml <CreateAssetImportTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <task_instance_id>1</task_instance_id>
</CreateAssetImportTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Internal service error | An internal server error occurred while processing the request. |

##### 6.2.1.2 DescribeAssetImportTask

Retrieves the details of an asset import task.

**Permissions**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeAssetImportTa sk | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Maximum call frequency for a single user: 10 queries per second (QPS). Maximum call frequency for this API: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see common parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| task instance _ id _ | Integer | Body | No | 1 | The task instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID generated for the request. Use this ID to troubleshoot issues. |
| vpc id _ | String | 1 | The VPC ID. |

| id | Integer | 1 | The task ID. |
|---|---|---|---|
| task instance id _ _ | Integer | 1 | The task instance ID. |
| template id _ | Integer | 1 | The template ID. |
| task name _ | String | Asset scanning task - test | The task name. |
| template name _ | String | Asset scanning template - test | The template name. |
| import mode _ | String | MANUAL IMPORT _ | The import mode. MANUAL IMPORT : Assets _ are imported manually. |
| network type _ | Integer | 1 | The network type. 1 : public network 2 : private network |
| status | String | INIT | The running status. INIT : The task is being initialized. |
| is immediately _ | Integer | 1 | Specifies whether to execute the task immediately. 1 : Yes 0 : No |
| is public asset _ _ | Integer | 1 | Specifies whether to import assets from the public network. 1 : Yes 0 : No |
| cycle count _ | Integer | 10 | The number of task cycles. |
| import count _ | Object | {} | The number of imported assets. |

| not alive report _ _ | Integer | 1 | Specifies whether to report inactive assets. 1 : Yes 0 : No |
|---|---|---|---|
| screen shot _ | Integer | 1 | Specifies whether to enable website screenshots. 1 : Enabled 0 : Disabled |
| finish time _ | Integer | 1774428275 | The task completion time. |
| insert tm _ | Integer | 1774428275 | The task creation time. |
| start time _ | Integer | 1774428275 | The task start time. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DescribeAssetImportTask&RegionId=cn-hangzhou Content-Type: application/json
  "task_instance_id": 1
```

Response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "vpc_id": "1",
  "id": 1,
  "task_instance_id": 1,
  "template_id": 1,
  "task_name": "Asset scanning task - test",
  "template_name": "Asset scanning template - test",
  "import_mode": "MANUAL_IMPORT",
  "network_type": 1,
  "status": "INIT",
  "is_immediately": 1,
  "is_public_asset": 1,
  "cycle_count": 10,
  "import_count": {},
  "not_alive_report": 1,
  "screen_shot": 1,
  "finish_time": 1774428275,
  "insert_tm": 1774428275,
  "start_time": 1774428275
```

`XML` format

```xml
Content-Type:application/xml <DescribeAssetImportTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <vpc_id>1</vpc_id>
    <id>1</id>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
    <task_name>Asset scanning task - test</task_name>
    <template_name>Asset scanning template - test</template_name>
    <import_mode>MANUAL_IMPORT</import_mode>
    <network_type>1</network_type>
    <status>INIT</status>
    <is_immediately>1</is_immediately>
    <is_public_asset>1</is_public_asset>
    <cycle_count>10</cycle_count>
    <import_count></import_count>
    <not_alive_report>1</not_alive_report>
    <screen_shot>1</screen_shot>
    <finish_time>1774428275</finish_time>
    <insert_tm>1774428275</insert_tm>
    <start_time>1774428275</start_time>
</DescribeAssetImportTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Server Passthrough | A pass-through error message from the server. |

##### 6.2.1.3 DescribeAssetImportTaskResult

Returns a list of results for an asset import task.

**Authorization information**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeAssetImportTa skResult | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Single-user rate limit: 10 QPS. API rate limit: 100 QPS.

**Request headers**

This operation uses common request headers and has no special request headers. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| task instance _ id _ | Integer | body | No | 1 | The task instance ID. |
| asset type _ | String | body | No | IP | The asset type. Valid values: IP WEBSITE DOMAIN |

| is new _ | Integer | body | No | 1 | Specifies whether the asset is newly discovered. 1 : Yes 0 : No |
|---|---|---|---|---|---|
| page | Integer | body | No | 1 | The page number. |
| page size _ | Integer | body | No | 10 | The page size. |
| search | String | body | No | 1.1.1.1 | The search keyword. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. |
| count | Integer | 100 | The total number of entries returned. |
| results | Array |   | The list of results. |
| results[].id | Integer | 1 | The ID of the entry. |
| results[].task instance _ id _ | Integer | 1 | The task instance ID. |
| results[].asset name _ | String | 1.1.1.1 | The asset name. |
| results[].is new _ | Integer | 1 | Indicates whether the asset is newly discovered. 1 : Yes 0 : No |

| results[].is deleted _ | Boolean | false | Indicates whether the asset is deleted. true : Yes false : No |
|---|---|---|---|
| results[].asset source _ | String | Host Import | The asset source. |
| results[].insert tm _ | Integer | 1774428275 | The time when the entry was created. This value is a UNIX timestamp. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DescribeAssetImportTaskResult&RegionId=cn-hangzhou Content-Type: application/json
  "task_instance_id": 1,
  "asset_type": "IP",
  "is_new": 1,
  "page": 1,
  "page_size": 10,
  "search": "1.1.1.1"
```

Response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 100,
  "results": [
      "id": 1,
      "task_instance_id": 1,
      "asset_name": "1.1.1.1",
      "is_new": 1,
      "is_deleted": false,
      "asset_source": "Host Import",
      "insert_tm": 1774428275
```

`]` `XML` format

```xml
Content-Type:application/xml <DescribeAssetImportTaskResultResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>100</count>
    <results>
        <item>
            <id>1</id>
            <task_instance_id>1</task_instance_id>
            <asset_name>1.1.1.1</asset_name>
            <is_new>1</is_new>
            <is_deleted>false</is_deleted>
            <asset_source>Host Import</asset_source>
            <insert_tm>1774428275</insert_tm>
        </item>
    </results>
</DescribeAssetImportTaskResultResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side pass- through | A server-side pass- through error occurred. |

#### 6.2.2 Asset scan

##### 6.2.2.1 CreateAssetScanTask

Creates an asset scan task.

**Permissions**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:CreateAssetScanTask | N/A | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Rate limit for a single user: 10 queries per second (QPS). Rate limit for this API: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request headers.

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | 1 | The ID of the VPC. |
| template id _ | Integer | body | No | 1 | The template ID. |
| task name _ | String | body | Yes | Risk-Scan- Task-Test | The task name. |
| targets | String | body | No |   | The scan targets, specified as a JSON-formatted string. You can scan all assets of a certain type ( ALL IP , _ ALL WEBSITE , _ ALL ASSET , _ ALL DOMAIN ) by setting _ the value to 1 , or scan specific asset groups by ID ( GROUP ). To scan specific IP assets by ID, use the IP key. To scan specific website or domain assets by ID, use the WEBSITE and DOMAIN keys. |
| screen shot _ | Integer | body | No | 1 | Specifies whether to capture website screenshots. Set the value to 1 to capture a website screenshot. Set the value to 0 not to capture a website screenshot. |

|   | WEBSITE |
|---|---|
| DOMAIN |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. |
|---|---|---|---|
| task id _ | Integer | 1 | The ID of the created asset scan task. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=CreateAssetScanTask&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "1",
  "template_id": 1,
  "task_name": "Risk-Scan-Task-Test",
  "targets": "",
  "screen_shot": 1
```

Response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "task_id": 1
```

`XML` format

```xml
Content-Type:application/xml <CreateAssetScanTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <task_id>1</task_id>
</CreateAssetScanTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | internal service error | The request failed due to an internal server error. |

##### 6.2.2.2 DescribeAssetScanTask

Retrieves the details of a specified asset scan task.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeAssetScanTas k | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

The request rate for a single user is limited to 10 queries per second (QPS). The total request rate for this API is limited to 100 QPS.

**Request headers**

This operation uses only common request parameters. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| id | Integer | body | No | 1 | The ID of the asset scan task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. Use this ID to troubleshoot issues. |
| id | Integer | 1 | The asset scan task ID. |
| task instance id _ _ | Integer | 1 | The task instance ID. |
| template id _ | Integer | 1 | The template ID. |
| name | String | Example asset scan | The asset scan task name. |

| template name _ | String | Example asset scan template | The task template name. |
|---|---|---|---|
| status | String | RUNNING | The task status. INIT : The task is initializing. |
| targets | Array | [{"type": "ALL", "target": [""]}] | The scan targets. |
| targets[].type | String | ALL | The scan target type. |
| targets[].target | Array | [""] | The specific scan targets. |
| cycle count _ | Integer | 10 | The number of scan cycles. |
| import count _ | Object | {} | The number of imported assets. |
| finish time _ | Integer | 1774428275 | The UNIX timestamp when the task finished. |
| insert tm _ | Integer | 1774428275 | The UNIX timestamp when the task was created. |
| start tm _ | Integer | 1774428275 | The UNIX timestamp when the task started. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DescribeAssetScanTask&RegionId=cn-hangzhou Content-Type: application/json
  "id": 1
```

Response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "id": 1,
  "task_instance_id": 1,
  "template_id": 1,
  "name": "Example asset scan",
  "template_name": "Example asset scan template",
  "status": "RUNNING",
  "targets": [
      "type": "ALL",
      "target": [
```

`""` `]` `],`

```json
  "cycle_count": 10,
  "import_count": {},
  "finish_time": 1774428275,
  "insert_tm": 1774428275,
  "start_tm": 1774428275
```

`XML` format

```xml
Content-Type:application/xml <DescribeAssetScanTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <id>1</id>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
    <name>Example asset scan</name>
    <template_name>Example asset scan template</template_name>
    <status>RUNNING</status>
    <targets>
        <item>
            <type>ALL</type>
            <target>
                <item></item>
            </target>
        </item>
    </targets>
    <cycle_count>10</cycle_count>
    <import_count></import_count>
    <finish_time>1774428275</finish_time>
    <insert_tm>1774428275</insert_tm>
    <start_tm>1774428275</start_tm>
</DescribeAssetScanTaskResponse>
```

**Error codes**

| HTTP code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Server-side Pass- through | An internal server error occurred. |

#### 6.2.3 Risk scanning

##### 6.2.3.1 CreateRiskScanTask

Creates a risk scan task.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:CreateRiskScanTask | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

The request rate for a single user is limited to 10 queries per second (QPS). The request rate for this API is limited to 100 queries per second (QPS).

**Request headers**

This operation has no special request headers. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| template id _ | Integer | body | No | 1 | The template ID. |
| vpc ids _ | String | body | No | ["vpc 1", _ "vpc 2"] _ | The VPC IDs. |
| task name _ | String | body | Yes | risk-scan-task- test | The task name. |
| targets | String | body | No |   | The scan targets. ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | A unique identifier for the request. You can use this ID to troubleshoot issues. |
| task id _ | Integer | 1 |   |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=CreateRiskScanTask&RegionId=cn-hangzhou Content-Type: application/json
  "template_id": 1,
  "vpc_ids": [
    "vpc_1",
    "vpc_2"
```

`],`

```json
  "task_name": "risk-scan-task-test",
  "targets": ""
```

Successful response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "task_id": 1
```

`XML` format

```xml
Content-Type:application/xml <CreateRiskScanTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <task_id>1</task_id>
</CreateRiskScanTaskResponse>
```

**Error codes**

| HTTP code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side passthrough | server-side passthrough |

##### 6.2.3.2 DescribeRiskScanTask

Retrieves the details of a specific risk scan task.

**Authorization**

| Operation | Access level | Resource type |
|---|---|---|

| yundun- scanner:DescribeRiskScanTask | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**Throttling**

Limit per user: 10 queries per second (QPS). Limit for this API: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| id | Integer | body | No | 1 | The ID of the risk scan task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID of the request, generated by Alibaba Cloud. This ID is required for troubleshooting. |
| id | Integer | 1 | The ID of the risk scan task. |
| task instance id _ _ | Integer | 1 | The ID of the task instance. |
| template id _ | Integer | 1 | The ID of the template. |
| name | String | xx risk scan | The name of the task. |
| template name _ | String | xx risk scan template | The name of the task template. |

| status | String | RUNNING | The status of the task. A value of INIT indicates that the task is initializing. |
|---|---|---|---|
| targets | Array | [{"type": "ALL", "target": [""]}] | The scan targets. |
| targets[].type | String | ALL | The type of the scan target. |
| targets[].target | Array | [""] | The specific scan target. |
| cycle count _ | Integer | 10 | The number of cycles for the task. |
| finish time _ | Integer | 1774428275 | The end time of the task. This value is a Unix timestamp. |
| insert tm _ | Integer | 1774428275 | The creation time of the task. This value is a Unix timestamp. |
| start tm _ | Integer | 1774428275 | The start time of the task. This value is a Unix timestamp. |

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=DescribeRiskScanTask&RegionId=cn-hangzhou Content-Type: application/json
  "id": 1
```

Sample response `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "id": 1,
  "task_instance_id": 1,
  "template_id": 1,
  "name": "xx risk scan",
  "template_name": "xx risk scan template",
  "status": "RUNNING",
  "targets": [
      "type": "ALL",
      "target": [
```

`""` `]` `],`

```json
  "cycle_count": 10,
  "finish_time": 1774428275,
  "insert_tm": 1774428275,
  "start_tm": 1774428275
```

`XML` format

```xml
Content-Type:application/xml <DescribeRiskScanTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <id>1</id>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
    <name>xx risk scan</name>
    <template_name>xx risk scan template</template_name>
    <status>RUNNING</status>
    <targets>
        <item>
            <type>ALL</type>
            <target>
                <item></item>
            </target>
        </item>
    </targets>
    <cycle_count>10</cycle_count>
    <finish_time>1774428275</finish_time>
    <insert_tm>1774428275</insert_tm>
    <start_tm>1774428275</start_tm>
</DescribeRiskScanTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server passthrough | The error message is passed through from an upstream server. |

##### 6.2.3.3 DescribeRiskScanTaskResult

Retrieves the results of a risk scan task.

**Permissions**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeRiskScanTask Result | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Rate limit per user: 10 queries per second (QPS). Rate limit for the API: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | In | Required | Example | Description |
|---|---|---|---|---|---|
| task instance _ id _ | Integer | body | No | 1 | The task instance ID. |
| risk type _ | Integer | body | No | 2 | The risk type. Valid values: 2: security vulnerability 3: compliance vulnerability |
| page | Integer | body | No | 1 | The page number. |

| page size _ | Integer | body | No | 10 | The number of entries to return on each page. |
|---|---|---|---|---|---|
| search | String | body | No | 1 1 1 1 1 _ _ _ _ | The search query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID of the request, generated by Alibaba Cloud. This ID is required for troubleshooting. |
| count | Integer | 100 | The total number of entries. |
| results | Array |   | The scan results. |
| results[].risk id _ | Integer | 1 | The risk ID. |
| results[].risk name _ | String | Example security vulnerability | The risk name. |
| results[].risk type _ | Integer | 3 | The risk type. Valid values: 2: security vulnerability 3: compliance vulnerability |
| results[].risk level _ | String | LOW | The risk level. Valid values: HIGH: High MIDDLE: Medium LOW: Low |
| results[].risk addr _ | String | http://1.1.1.1 | The risk address, such as a URL. |

| results[].insert tm _ | Integer | 1774428275 | The time the record was inserted, in Unix timestamp format. |
|---|---|---|---|

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=DescribeRiskScanTaskResult&RegionId=cn-hangzhou Content-Type: application/json
  "task_instance_id": 1,
  "risk_type": 2,
  "page": 1,
  "page_size": 10,
  "search": "1_1_1_1_1"
```

Sample response `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 100,
  "results": [
      "risk_id": 1,
      "risk_name": "Example security vulnerability",
      "risk_type": 3,
      "risk_level": "LOW",
      "risk_addr": "http://1.1.1.1",
      "insert_tm": 1774428275
```

`]` `XML` format

```xml
Content-Type:application/xml <DescribeRiskScanTaskResultResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>100</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <risk_name>Example security vulnerability</risk_name>
            <risk_type>3</risk_type>
            <risk_level>LOW</risk_level>
            <risk_addr>http://1.1.1.1</risk_addr>
            <insert_tm>1774428275</insert_tm>
        </item>
    </results>
</DescribeRiskScanTaskResultResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Server Passthrough | An internal server error occurred. |

#### 6.2.4 DescribeTaskList

Retrieves a list of tasks.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeTaskList | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Each user is limited to 10 queries per second (QPS). The system limits API calls to 100 per second (QPS).

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| template id _ | Integer | body | No | 1 | The template ID. |
| page | Integer | body | No | 1 | The page number. |
| page size _ | Integer | body | No | 10 | The number of entries per page. |
| run types _ | String | body | No | cycle | The running mode. cycle : periodic execution once : one-time execution at a specified time immediately : immediate execution |
| search | String | body | No | 1 1 1 1 _ _ _ _ 1 | The search keyword. You can search by the following fields: Task ID Task name Asset address |
| statuses | String | body | No | ["RUNNIN G", "INIT", "FINISH", "STOP"] | Filters tasks by status. RUNNING : Running INIT : Initializing FINISH : Finished STOP : Stopped |
| task types _ | String | body | No | ["assetIm port", "assetRis k", "assetSca n"] | Filters tasks by type. assetImport : asset import task assetScan : asset scan task assetRisk : risk scan task |
| end time _ | String | body | No | 2020-01- 01 00:00:00 | The end time. |

| start time _ | String | body | No | 2020-01- 01 00:00:00 | The start time. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID of the request. Provide this ID when you submit a ticket for troubleshooting. |
| count | Integer | 10 | The total number of tasks returned. |
| results | Array |   | An array of task objects. |
| results[].id | Integer | 1 | The task ID. |
| results[].task instance _ id _ | Integer | 123 | The task instance ID. |
| results[].task name _ | String | Asset Scan Task-Test | The task name. |
| results[].task type _ | Integer | 6 | The task type. |
| results[].status | String | INIT | The task status. RUNNING : Running INIT : Initializing FINISH : Finished STOP : Stopped |
| results[].is immediatel _ y | Integer | 1 | Indicates if the task was set to run immediately. 1 : Yes 0 : No |

| results[].is public asse _ _ t | Integer | 1 | Indicates if the task targets a public asset. 1 : Yes 0 : No |
|---|---|---|---|
| results[].cycle count _ | Integer | 10 | The number of cycles for a periodic task. |
| results[].task cycle _ | Integer | 0 | The task cycle. |
| results[].start time _ | Integer | 1774428275 | The task creation time, in a UNIX timestamp. |
| results[].end time _ | Integer | 1774428275 | The task end time, in a UNIX timestamp. |
| results[].insert tm _ | Integer | 1774428275 | The time when the task record was inserted into the database, in a UNIX timestamp. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DescribeTaskList&RegionId=cn-hangzhou Content-Type: application/json
  "template_id": 1,
  "page": 1,
  "page_size": 10,
  "run_types": "cycle",
  "search": "1_1_1_1_1",
  "statuses": [
    "RUNNING",
    "INIT",
    "FINISH",
    "STOP"
```

`],`

```json
  "task_types": [
    "assetImport",
    "assetRisk",
    "assetScan"
```

`],`

```json
  "end_time": "2020-01-01 00:00:00",
  "start_time": "2020-01-01 00:00:00"
```

Response example

```json
 JSON
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
      "id": 1,
      "task_instance_id": 123,
      "task_name": "Asset Scan Task-Test",
      "task_type": 6,
      "status": "INIT",
      "is_immediately": 1,
      "is_public_asset": 1,
      "cycle_count": 10,
      "task_cycle": 0,
      "start_time": 1774428275,
      "end_time": 1774428275,
      "insert_tm": 1774428275
```

`]`

```xml
 XML
Content-Type:application/xml <DescribeTaskListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <id>1</id>
            <task_instance_id>123</task_instance_id>
            <task_name>Asset Scan Task-Test</task_name>
            <task_type>6</task_type>
            <status>INIT</status>
            <is_immediately>1</is_immediately>
            <is_public_asset>1</is_public_asset>
            <cycle_count>10</cycle_count>
            <task_cycle>0</task_cycle>
            <start_time>1774428275</start_time>
            <end_time>1774428275</end_time>
            <insert_tm>1774428275</insert_tm>
        </item>
    </results>
</DescribeTaskListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server passthrough | A server passthrough error occurred. |

#### 6.2.5 StartTask

Starts one or more tasks.

**Authorization**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:StartTask | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Each user is limited to 10 queries per second (QPS). The API supports a total of 100 calls per second (QPS).

**Request headers**

This operation uses only common request headers. For details, see common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| task ids _ | Array | body | No | [1, 2, 3] | An array of task IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique ID of the request. Use this ID for troubleshooting. |
| data | Array | [{"task instance id": _ _ 208, "task id": 173}] _ | An array containing an object for each started task instance. |

| data[].task instance id _ _ | Integer | 208 | The task instance ID. |
|---|---|---|---|
| data[].task id _ | Integer | 173 | The task ID. |

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=StartTask&RegionId=cn-hangzhou Content-Type: application/json
  "task_ids": [
```

`1,` `2,` `]` Sample success response `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "data": [
      "task_instance_id": 208,
      "task_id": 173
```

`]` `XML` format

```xml
Content-Type:application/xml <StartTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>
        <item>
            <task_instance_id>208</task_instance_id>
            <task_id>173</task_id>
        </item>
    </data>
</StartTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side pass- through | An internal server error occurred. |

#### 6.2.6 StopTask

Stops a task.

**Permissions**

| Actions | Access level | Resource type |
|---|---|---|
| yundun-scanner:StopTask | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

Throttling limit per user: 10 QPS. Throttling limit for the API: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common Request Parameters.

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| task ids _ | String | body | No | [1, 2, 3] | The IDs of the tasks to stop. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique identifier for the request, generated by Alibaba Cloud for troubleshooting purposes. |

| status | String | OK | The status of the operation. A value of OK indicates that the request was successful. |
|---|---|---|---|

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=StopTask&RegionId=cn-hangzhou Content-Type: application/json
  "task_ids": [
```

`1,` `2,` `]` Sample responses `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "status": "OK"
```

`XML` format

```xml
Content-Type:application/xml <StopTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status>OK</status>
</StopTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side passthrough | An error from a dependent service was passed through. |

#### 6.2.7 SuspendTask

Suspends a task.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun-scanner:SuspendTask | undefined | acs:yundun-scanner:: {#accountId}: |

**Throttling**

The rate limit for a single user is 10 queries per second (QPS). The rate limit for this API is 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| task ids _ | String | body | No | [1, 2, 3] | The IDs of the tasks to suspend. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The unique request ID. Provide this ID to Alibaba Cloud when troubleshooting issues. |
| status | String | OK | The request status. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=SuspendTask&RegionId=cn-hangzhou Content-Type: application/json
  "task_ids": [
```

`1,` `2,` `]` Successful response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "status": "OK"
```

`XML` format

```xml
Content-Type:application/xml <SuspendTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status>OK</status>
</SuspendTaskResponse>
```

**Error codes**

| Http code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side pass- through | server-side pass- through |

#### 6.2.8 DeleteTask

Deletes one or more tasks.

**Permissions**

| Actions | Access level | Resource type |
|---|---|---|

| yundun-scanner:DeleteTask | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**Throttling**

Per user: 10 queries per second (QPS). Per API: 100 QPS.

**Request header**

This operation uses only common request headers. For more information, see common request parameters.

**Request parameters**

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| task ids _ | String | body | No | [1, 2, 3] | The IDs of the tasks to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | Alibaba Cloud generates this ID to help you troubleshoot issues. |
| status | String | OK | The status of the request. A value of OK indicates the request was successful. |

**Examples**

Request example

```json
POST https://[Endpoint]/?Action=DeleteTask&RegionId=cn-hangzhou Content-Type: application/json
  "task_ids": [
```

`1,` `2,` `]` Successful response example `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "status": "OK"
```

`XML` format

```xml
Content-Type:application/xml <DeleteTaskResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status>OK</status>
</DeleteTaskResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Server-side pass- through | This indicates a server-side pass- through error. |

### 6.3 Risk API

#### 6.3.1 Security vulnerability

##### 6.3.1.1 DescribeRiskList

Retrieves a list of security vulnerabilities.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeRiskList | undefined | acs:yundun-scanner:: {#accountId}: |

**Rate limits**

The rate limit for a single user is 10 queries per second (QPS). The rate limit for this API is 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | In | Req uire d | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | public network _ _ asset | The ID of the VPC. |
| asset id _ | Integer | body | No | 1 | The ID of the asset. |
| group ids _ | String | body | No | [1, 2] | The IDs of asset groups, formatted as a JSON array of integers. |
| staff ids _ | String | body | No | [1, 2] | The IDs of staff, formatted as a JSON array of integers. |
| tag ids _ | String | body | No | [1, 2] | The IDs of tags, formatted as a JSON array of integers. |
| status | String | body | No | REPAIRED | The handling status. Valid values: REPAIRED : The vulnerability is fixed. UNREPAIRED : The vulnerability is not fixed. |
| detect status _ | String | body | No | ["SUCCESS", "FAILED", "DETECTING"] | The detection statuses, formatted as a JSON array of strings. Valid values: SUCCESS : The detection was successful. FAILED : The detection failed. DETECTING : The detection is in progress. |
| source | String | body | No | ["1", "2"] | The risk sources, formatted as a JSON array of strings. |

| insert tm end _ _ | String | body | No | 2021-01-04 00:00:00 | The end of the discovery time range. The format is YYYY- MM-DD hh:mm:ss . |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | YYYY- |   |
| insert tm start _ _ | String | body | No | 2021-01-04 00:00:00 | The beginning of the discovery time range. The format is YYYY-MM-DD hh:mm:ss . |   |   |
| page | Integer | body | No | 1 | The page number. |   |   |
| page size _ | Integer | body | No | 10 | The number of entries per page. |   |   |
| process | String | body | No | ["NEW", "CONFIRMED", "IGNORED"] | The processing statuses of the security vulnerability, formatted as a JSON array of strings. Valid values: NEW : The vulnerability is not triaged. CONFIRMED : The vulnerability is confirmed. IGNORED : The vulnerability is ignored. |   |   |
| risk levels _ | String | body | No | ["LOW", "MIDDLE", "HIGH"] | The risk levels of the security vulnerability, formatted as a JSON array of strings. Valid values: HIGH : High MIDDLE : Medium LOW : Low |   |   |
| search | String | body | No | CVE-2021- 44228 | A keyword for a fuzzy search. You can search by risk name or vulnerability SN. |   |   |
| update tm end _ _ | String | body | No | 2021-01-04 00:00:00 | The end of the time range for the last update. The format is YYYY-MM-DD hh:mm:ss . |   |   |
| update tm start _ _ | String | body | No | 2021-01-04 00:00:00 | The beginning of the time range for the last update. The format is YYYY-MM-DD hh:mm:ss . |   |   |

|   | MM-DD hh:mm:ss |
|---|---|

|   |   | YYYY-MM-DD |   |
|---|---|---|---|
|   | hh:mm:ss |   |   |

|   |   | YYYY-MM-DD |   |
|---|---|---|---|
|   | hh:mm:ss |   |   |

| vuln types _ | String | body | No | [1, 2] | The vulnerability types, formatted as a JSON array of integers. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use this ID to troubleshoot issues. |
| count | Integer | 10 | The total number of matching entries. |
| results | Array |   | An array of security vulnerabilities. |
| results[].risk id _ | Integer | 1 | The ID of the risk. |
| results[].asset id _ | Integer | 1 | The ID of the asset. |
| results[].vuln id _ | Integer | 1 | The ID of the vulnerability. |
| results[].risk name _ | String | foo | The name of the risk. |
| results[].vuln type _ | String | XSS vulnerability | The vulnerability type. |
| results[].general type _ | String | web vuln _ | The general type of the risk. |
| results[].risk level _ | String | HIGH | The risk level. |
| results[].risk status _ | String | SUCCESS | The status of the risk. |
| results[].detect status _ | String | SUCCESS | The detection status. |
| results[].risk process _ | String | NEW | The processing status of the risk. |

| loud Security Scanner D Guide·Vulnerability Scan | evelope V2 |   |   |
|---|---|---|---|

| results[].source | String | AUTO | The source of the risk. |
|---|---|---|---|
| results[].risk addr _ | String | 192.168.0.1:3306 | The location of the risk, such as an IP address and port. |
| results[].ip | String | 192.168.0.1 | The IP address of the affected asset. |
| results[].related doma _ in | String | www.foo.com | The domain name associated with the risk. |
| results[].fail reason _ | String | xxx | The reason for the detection failure. |
| results[].ignore comm _ ent | String | xxx | The comment provided when the risk was ignored. |
| results[].risk sn _ | String | 2020-1-1- V100000000000 | The vulnerability SN. |
| results[].insert tm _ | Integer | 1774428275 | The time when the risk was recorded, as a UNIX timestamp. |
| results[].last detect t _ _ m | Integer | 1774428275 | The time of the last detection, as a UNIX timestamp. |
| results[].update tm _ | Integer | 1774428275 | The time of the last update, as a UNIX timestamp. |

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=DescribeRiskList&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "public_network_asset",
  "asset_id": 1,
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
```

`1,` `],`

```json
  "status": "REPAIRED",
  "detect_status": [
    "SUCCESS",
    "FAILED",
    "DETECTING"
```

`],`

```json
  "source": [
    "1",
    "2"
```

`],`

```json
  "insert_tm_end": "2021-01-04 00:00:00",
  "insert_tm_start": "2021-01-04 00:00:00",
  "page": 1,
  "page_size": 10,
  "process": [
    "NEW",
    "CONFIRMED",
    "IGNORED"
```

`],`

```json
  "risk_levels": [
    "LOW",
    "MIDDLE",
    "HIGH"
```

`],`

```json
  "search": "CVE-2021-44228",
  "update_tm_end": "2021-01-04 00:00:00",
  "update_tm_start": "2021-01-04 00:00:00",
  "vuln_types": [
```

`1,` `]` Sample success response Response in `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
      "risk_id": 1,
      "asset_id": 1,
      "vuln_id": 1,
      "risk_name": "foo",
      "vuln_type": "XSS vulnerability",
      "general_type": "web_vuln",
      "risk_level": "HIGH",
      "risk_status": "SUCCESS",
      "detect_status": "SUCCESS",
      "risk_process": "NEW",
      "source": "AUTO",
      "risk_addr": "192.168.0.1:3306",
      "ip": "192.168.0.1",
      "related_domain": "www.foo.com",
      "fail_reason": "xxx",
      "ignore_comment": "xxx",
      "risk_sn": "2020-1-1-V100000000000",
      "insert_tm": 1774428275,
      "last_detect_tm": 1774428275,
      "update_tm": 1774428275
```

`]` Response in `XML` format

```xml
Content-Type:application/xml <DescribeRiskListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <asset_id>1</asset_id>
            <vuln_id>1</vuln_id>
            <risk_name>foo</risk_name>
            <vuln_type>XSS vulnerability</vuln_type>
            <general_type>web_vuln</general_type>
            <risk_level>HIGH</risk_level>
            <risk_status>SUCCESS</risk_status>
            <detect_status>SUCCESS</detect_status>
            <risk_process>NEW</risk_process>
            <source>AUTO</source>
            <risk_addr>192.168.0.1:3306</risk_addr>
            <ip>192.168.0.1</ip>
            <related_domain>www.foo.com</related_domain>
            <fail_reason>xxx</fail_reason>
            <ignore_comment>xxx</ignore_comment>
            <risk_sn>2020-1-1-V100000000000</risk_sn>
            <insert_tm>1774428275</insert_tm>
            <last_detect_tm>1774428275</last_detect_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
</DescribeRiskListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | server-side pass- through | An internal error occurred. The response includes the original error message from the backend service. |

#### 6.3.2 Public access

##### 6.3.2.1 DescribeBaselineRiskList

Retrieves a list of baseline risks.

**Authorization**

| Actions | Access level | Resource type |
|---|---|---|
| yundun- scanner:DescribeBaselineRiskLi st | undefined | acs:yundun-scanner:: {#accountId}: |

**Rate limiting**

The rate limit for a single user is 10 queries per second (QPS). The rate limit for this operation is 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, refer to the documentation on common parameters.

**Request parameters**

| Parameter | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | public networ _ k asset _ | The VPC ID. |
| group ids _ | String | body | No | [1, 2] | The asset group ID. |
| staff ids _ | String | body | No | [1, 2] | The owner ID. |
| tag ids _ | String | body | No | [1, 2] | The tag ID. |
| status | String | body | No | REPAIRED | The remediation status. Valid values: REPAIRED (Repaired) and UNREPAIRED (Unrepaired). |
| detect status _ | String | body | No | ["SUCCESS", "FAILED", "DETECTING"] | The detection status. Valid values: SUCCESS (Success), FAILED (Failed), and DETECTING (Detecting). |

|   | SUCCESS |
|---|---|
| FAILED |   |

| insert tm end _ _ | String | body | No | 2021-01-04 00:00:00 | The end of the time range in which the risk was recorded. The time is in the YYYY-MM-DD hh:mm:ss format. |   |
|---|---|---|---|---|---|---|
| insert tm star _ _ t | String | body | No | 2021-01-04 00:00:00 | The beginning of the time range in which the risk was recorded. The time is in the YYYY-MM-DD hh:mm:ss format. |   |
| page | Integer | body | No | 1 | The page number. |   |
| page size _ | Integer | body | No | 10 | The page size. |   |
| process | String | body | No | ["NEW", "CONFIRMED", "IGNORED"] | The confirmation status. Valid values: NEW (Unconfirmed), CONFIRMED (Confirmed), and IGNORED (Ignored). |   |
| risk levels _ | String | body | No | ["LOW", "MIDDLE", "HIGH"] | The risk level. Valid values: HIGH (High), MIDDLE (Medium), and LOW (Low). |   |
| search | String | body | No | CVE-2021- 44228 | The keyword for a fuzzy search, such as a risk name or CVE number. |   |
| update tm en _ _ d | String | body | No | 2021-01-04 00:00:00 | The end of the time range in which the risk was last updated. The time is in the YYYY-MM-DD hh:mm:ss format. |   |
| update tm st _ _ art | String | body | No | 2021-01-04 00:00:00 | The beginning of the time range in which the risk was last updated. The time is in the YYYY-MM- DD hh:mm:ss format. |   |

|   |   | YYYY-MM-DD |   |
|---|---|---|---|
|   | hh:mm:ss |   |   |

|   |   | YYYY-MM-DD |   |
|---|---|---|---|
|   | hh:mm:ss |   |   |

|   |   | YYYY-MM-DD |   |
|---|---|---|---|
|   | hh:mm:ss |   |   |

|   | DD hh:mm:ss |
|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The ID of the request. Provide this request ID for troubleshooting. |
| count | Integer | 10 | The total number of entries. |
| results | Array |   | The list of baseline risks. |
| results[].risk id _ | Integer | 1 | The ID of the risk. |
| results[].asset id _ | Integer | 1 | The ID of the asset. |
| results[].rule id _ | Integer | 1 | The ID of the rule. |
| results[].risk name _ | String | foo | The name of the risk. |
| results[].risk level _ | String | HIGH | The risk level. |
| results[].risk status _ | String | SUCCESS | The status of the risk. |
| results[].detect status _ | String | SUCCESS | The detection status. |
| results[].risk process _ | String | NEW | The confirmation status of the risk. |
| results[].risk addr _ | String | 192.168.0.1:443 | The address of the risk. |
| results[].ip | String | 192.168.0.1 | The IP address of the asset. |
| results[].related doma _ in | String | www.foo.com | The related domain. |
| results[].ignore comm _ ent | String | xxx | The reason provided for ignoring the risk. |

| results[].risk sn _ | String | 2020-1-1- V100000000000 | The serial number of the risk. |
|---|---|---|---|
| results[].vuln addr _ | String | 192.168.0.1:443 | The vulnerability address. |
| results[].insert tm _ | Integer | 1774428275 | The time when the risk was recorded. This value is a Unix timestamp. |
| results[].update tm _ | Integer | 1774428275 | The time when the risk was last updated. This value is a Unix timestamp. |

**Examples**

Example request

```json
POST https://[Endpoint]/?Action=DescribeBaselineRiskList&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "public_network_asset",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
```

`1,` `],`

```json
  "status": "REPAIRED",
  "detect_status": [
    "SUCCESS",
    "FAILED",
    "DETECTING"
```

`],`

```json
  "insert_tm_end": "2021-01-04 00:00:00",
  "insert_tm_start": "2021-01-04 00:00:00",
  "page": 1,
  "page_size": 10,
  "process": [
    "NEW",
    "CONFIRMED",
    "IGNORED"
```

`],`

```json
  "risk_levels": [
    "LOW",
    "MIDDLE",
    "HIGH"
```

`],`

```json
  "search": "CVE-2021-44228",
  "update_tm_end": "2021-01-04 00:00:00",
  "update_tm_start": "2021-01-04 00:00:00"
```

Example of a successful response `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
      "risk_id": 1,
      "asset_id": 1,
      "rule_id": 1,
      "risk_name": "foo",
      "risk_level": "HIGH",
      "risk_status": "SUCCESS",
      "detect_status": "SUCCESS",
      "risk_process": "NEW",
      "risk_addr": "192.168.0.1:443",
      "ip": "192.168.0.1",
      "related_domain": "www.foo.com",
      "ignore_comment": "xxx",
      "risk_sn": "2020-1-1-V100000000000",
      "vuln_addr": "192.168.0.1:443",
      "insert_tm": 1774428275,
      "update_tm": 1774428275
```

`]` `XML` format

```xml
Content-Type:application/xml <DescribeBaselineRiskListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <asset_id>1</asset_id>
            <rule_id>1</rule_id>
            <risk_name>foo</risk_name>
            <risk_level>HIGH</risk_level>
            <risk_status>SUCCESS</risk_status>
            <detect_status>SUCCESS</detect_status>
            <risk_process>NEW</risk_process>
            <risk_addr>192.168.0.1:443</risk_addr>
            <ip>192.168.0.1</ip>
            <related_domain>www.foo.com</related_domain>
            <ignore_comment>xxx</ignore_comment>
            <risk_sn>2020-1-1-V100000000000</risk_sn>
            <vuln_addr>192.168.0.1:443</vuln_addr>
            <insert_tm>1774428275</insert_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
</DescribeBaselineRiskListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Internal service error. | The server encountered an internal error. Try the request again later. |

#### 6.3.3 Compliance vulnerability

##### 6.3.3.1 DescribeComplianceRiskList

Describes a list of compliance vulnerabilities.

**Permissions**

| Action | Access level | Resource type |
|---|---|---|

| yundun- scanner:DescribeComplianceRis kList | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**Throttling**

Rate limit for a single user: 10 QPS. API rate limit: 100 QPS.

**Request headers**

This operation uses only common request headers. For more information, see Common Request Parameters.

**Request parameters**

| Parameter | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| vpc id _ | String | body | No | public netwo _ rk asset _ | The VPC ID. |
| asset id _ | Integer | body | No | 1 | The asset ID. |
| host asset id _ _ | Integer | body | No | 1 | The host asset ID. |
| group ids _ | String | body | No | [1, 2] | The asset group IDs. |
| staff ids _ | String | body | No | [1, 2] | The staff IDs. |
| tag ids _ | String | body | No | [1, 2] | The tag IDs. |
| status | String | body | No | REPAIRED | The status. Valid values: REPAIRED , UNREPAIRED |
| detect status _ | String | body | No | ["SUCCESS", "FAILED", "DETECTING" ] | The detection status. Valid values: SUCCESS , FAILED , DETECTING |
| source | String | body | No | ["1", "2"] | The source. |

| attack compl _ exity | String | body | No | HIGH |   | The attack complexity. Valid values: HIGH : High LOW : Low |   |   |
|---|---|---|---|---|---|---|---|---|
| privileges re _ quired | String | body | No | LOW |   | The privileges required. Valid values: HIGH : High LOW : Low NONE : None |   |   |
| availability i _ mpact | String | body | No | HIGH |   | The availability impact. Valid values: HIGH : High LOW : Low NONE : None |   |   |
| exploitability | String | body | No | ["UNPROOFE D", "POC", "EXP"] |   | The exploitability. Valid values: UNPROOFED : The vulnerability is unproven. POC : A proof-of- concept (PoC) exploit is available. EXP : An exploit is publicly available. |   |   |
| insert tm en _ _ d | String | body | No | 2021-01-04 00:00:00 |   | The discovery end time. The format is YYYY-MM- DD hh:mm:ss . |   |   |
|   |   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   |   | :00 | DD hh:mm:ss |   |   |
| insert tm sta _ _ rt | String | body | No | 2021-01-04 00:00:00 |   | The discovery start time. The format is YYYY-MM- DD hh:mm:ss . |   |   |
|   |   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   |   | :00 | DD hh:mm:ss |   |   |
| page | Integer | body | No | 1 |   | The page number. |   |   |
| page size _ | Integer | body | No | 10 |   | The page size. |   |   |
| ports | String | body | No | [80, 443] |   | The port numbers. |   |   |

| process | String | body | No | ["NEW", "CONFIRMED ", "IGNORED"] |   | The handling status. Valid values: NEW : Unconfirmed, CONFIRMED : Confirmed, IGNORED : Ignored. |   |   |
|---|---|---|---|---|---|---|---|---|
| risk levels _ | String | body | No | ["LOW", "MIDDLE", "HIGH"] |   | The risk levels. Valid values: HIGH : High MIDDLE : Medium LOW : Low |   |   |
| search | String | body | No | CVE-2021- 44228 |   | A search keyword, such as a CVE ID. |   |   |
| update tm e _ _ nd | String | body | No | 2021-01-04 00:00:00 |   | The update end time. The format is YYYY-MM-DD hh:mm:ss . |   |   |
|   |   |   |   |   |   |   | YYYY-MM-DD |   |
|   |   |   |   |   | :00:00 | hh:mm:ss |   |   |
| update tm st _ _ art | String | body | No | 2021-01-04 00:00:00 |   | The update start time. The format is YYYY-MM-DD hh:mm:ss . |   |   |
|   |   |   |   |   |   |   | YYYY-MM-DD |   |
|   |   |   |   |   | :00:00 | hh:mm:ss |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | The request ID. |
| count | Integer | 10 | The total number of entries returned. |
| results | Array |   | An array that contains the details of each compliance vulnerability. |
| results[].risk id _ | Integer | 1 | The risk ID. |
| results[].asset id _ | Integer | 1 | The asset ID. |

| results[].risk name _ | String | foo | The name of the risk. |
|---|---|---|---|
| results[].risk level _ | String | HIGH | The risk level. |
| results[].risk status _ | String | SUCCESS | The status of the risk. |
| results[].detect status _ | String | SUCCESS | The detection status. |
| results[].risk process _ | String | NEW | The handling status of the risk. |
| results[].source | String | AUTO | The source of the risk. |
| results[].asset addr _ | String | 192.168.0.1 | The address of the asset. |
| results[].ip | String | 192.168.0.1 | The IP address of the asset. |
| results[].port | String | 443 | The port number. |
| results[].service | String | nginx | The service that runs on the port. |
| results[].related doma _ in | String | www.foo.com | The related domain. |
| results[].cve | String | CVE-2021-44228 | The CVE ID. |
| results[].avd | String | AVD-2021-44228 | The AVD ID. |
| results[].cnvd | String | CNVD-2021-95914 | The CNVD ID. |
| results[].cnnvd | String | CNNVD-202112-799 | The CNNVD ID. |
| results[].attack compl _ exity | String | HIGH | The attack complexity. Valid values: HIGH and LOW . |

| results[].privileges req _ uired | String | LOW | The privileges required. Valid values: LOW , HIGH , and NONE . |
|---|---|---|---|
| results[].availability i _ mpact | String | HIGH | The availability impact. Valid values: HIGH , LOW , and NONE . |
| results[].exploitability | Array | ["UNPROOFED", "POC", "EXP"] | The exploitability. Valid values: UNPROOFED , POC , and EXP . |
| results[].ignore comm _ ent | String | xxx | The comment for an ignored risk. |
| results[].insert tm _ | Integer | 1774428275 | The discovery time, as a Unix timestamp. |
| results[].update tm _ | Integer | 1774428275 | The time of the last update, as a Unix timestamp. |

| UNPROOFED |   |
|---|---|
| POC |   |

**Examples**

Sample request

```json
POST https://[Endpoint]/?Action=DescribeComplianceRiskList&RegionId=cn-hangzhou Content-Type: application/json
  "vpc_id": "public_network_asset",
  "asset_id": 1,
  "host_asset_id": 1,
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
```

`1,` `],`

```json
  "status": "REPAIRED",
  "detect_status": [
    "SUCCESS",
```

`,`

```
    "FAILED",
    "DETECTING"
```

`],`

```json
  "source": [
    "1",
    "2"
```

`],`

```json
  "attack_complexity": "HIGH",
  "privileges_required": "LOW",
  "availability_impact": "HIGH",
  "exploitability": [
    "UNPROOFED",
    "POC",
    "EXP"
```

`],`

```json
  "insert_tm_end": "2021-01-04 00:00:00",
  "insert_tm_start": "2021-01-04 00:00:00",
  "page": 1,
  "page_size": 10,
  "ports": [
    80,
```

`],`

```json
  "process": [
    "NEW",
    "CONFIRMED",
    "IGNORED"
```

`],`

```json
  "risk_levels": [
    "LOW",
    "MIDDLE",
    "HIGH"
```

`],`

```json
  "search": "CVE-2021-44228",
  "update_tm_end": "2021-01-04 00:00:00",
  "update_tm_start": "2021-01-04 00:00:00"
```

Sample response `JSON` format

```json
Content-Type:application/json
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
      "risk_id": 1,
      "asset_id": 1,
      "risk_name": "foo",
      "risk_level": "HIGH",
      "risk_status": "SUCCESS",
      "detect_status": "SUCCESS",
      "risk_process": "NEW",
      "source": "AUTO",
      "asset_addr": "192.168.0.1",
      "ip": "192.168.0.1",
      "port": "443",
      "service": "nginx",
      "related_domain": "www.foo.com",
      "cve": "CVE-2021-44228",
      "avd": "AVD-2021-44228",
      "cnvd": "CNVD-2021-95914",
      "cnnvd": "CNNVD-202112-799",
      "attack_complexity": "HIGH",
      "privileges_required": "LOW",
      "availability_impact": "HIGH",
      "exploitability": [
        "UNPROOFED",
        "POC",
        "EXP"
```

`],`

```json
      "ignore_comment": "xxx",
      "insert_tm": 1774428275,
      "update_tm": 1774428275
```

`]` `XML` format

```xml
Content-Type:application/xml <DescribeComplianceRiskListResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <asset_id>1</asset_id>
            <risk_name>foo</risk_name>
            <risk_level>HIGH</risk_level>
            <risk_status>SUCCESS</risk_status>
            <detect_status>SUCCESS</detect_status>
            <risk_process>NEW</risk_process>
            <source>AUTO</source>
            <asset_addr>192.168.0.1</asset_addr>
            <ip>192.168.0.1</ip>
            <port>443</port>
            <service>nginx</service>
            <related_domain>www.foo.com</related_domain>
            <cve>CVE-2021-44228</cve>
            <avd>AVD-2021-44228</avd>
            <cnvd>CNVD-2021-95914</cnvd>
            <cnnvd>CNNVD-202112-799</cnnvd>
            <attack_complexity>HIGH</attack_complexity>
            <privileges_required>LOW</privileges_required>
            <availability_impact>HIGH</availability_impact>
            <exploitability>
                <item>UNPROOFED</item>
                <item>POC</item>
                <item>EXP</item>
            </exploitability>
            <ignore_comment>xxx</ignore_comment>
            <insert_tm>1774428275</insert_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
</DescribeComplianceRiskListResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 101 | Internal server error. | An internal server error occurred. Try again later. If the issue persists, submit a ticket. |

## 7 Security audit

### 7.1 GetData

Queries a list of audit logs.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun-scanner:GetData | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| company i _ d | Integ er | Body | No | 0 | The tenant ID. |
| csv | Integ er | Body | No | 1 | Specifies whether to export the report. A value of 1 specifies exporting the report. A value of 0 specifies not exporting the report. |
| end | Strin g | Body | No | 1722478948 | The end of the time range to query. |
| module | Strin g | Body | No | OTHER | The module to which the logs belong. |

| page | Integ er | Body | No | 1 | The page number. |
|---|---|---|---|---|---|
| page size _ | Integ er | Body | No | 10 | The number of entries per page. |
| search | Strin g | Body | No | 192.168.30.67 | The filter conditions. You can filter logs by username, IP address, and event. |
| start | Strin g | Body | No | 1722478944 | The beginning of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| results | Array |   |   |
| -audit event _ | String | Import assets | The log event. |
| -event attr _ | String | [rp] import | The log property. |
| -event result _ | String | SUCCESS | The event result. Valid values: SUCCESS and FAILED. |
| -id | Integer | 1947 | The event ID. |
| -insert tm _ | Integer | 1722478948 | The log time. |
| -login ip _ | String | 192.168.102.18 | The logon IP address. |
| - login usernam _ e | String | aliens | The username that was used for logon. |
| -module | String | ASSET | The log module. Valid values: ASSET, RISK, REPORT, CONFIG, and OTHER. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

|   |   |   | Cloud Security Scanner Develop r Guide·Security audi |
|---|---|---|---|

| count | Integer | 150 | The number of entries per page. |
|---|---|---|---|
| path | String | http://oss.xxxx.xxx x/xxx/xx | The download path. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetData&RegionId=cnhangzhou&company_id=0&csv=1&end=1722478948&module=OTHER&page=1&page_size=10&search=192.16 30.67&start=1722478944
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":150,
    "path":"http://oss.xxxx.xxxx/xxx/xx",
    "results":[
            "audit_event":"Import assets",
            "event_attr":"[rp] import",
            "module":"ASSET",
            "login_username":"aliens",
            "event_result":"SUCCESS",
            "insert_tm":1722478948,
            "id":1947,
            "login_ip":"192.168.102.18"
```

`]` `XML` format

```xml
Content-Type:application/xml <GetDataResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>150</count>
    <path>http://oss.xxxx.xxxx/xxx/xx</path>
    <results>
        <audit_event>Import assets</audit_event>
        <event_attr>[rp] import</event_attr>
        <event_result>SUCCESS</event_result>
        <id>1947</id>
        <insert_tm>1722478948</insert_tm>
        <login_ip>192.168.102.18</login_ip>
        <login_username>aliens</login_username>
        <module>ASSET</module>
    </results>
</GetDataResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |

### 7.2 LouauditCleanData

Clears audit logs.

**Authorization information**

| Action | Access level | Resource type |
|---|---|---|
| yundun- scanner:LouauditCleanData | undefined | acs:yundun-scanner:*: {#accountId}:* |

**Traffic throttling**

You can call this operation up to 10 times per second per account. You can call this operation up to 100 times per second.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| keep time _ | Integ er | Body | No | 1722478948 | The retention period. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| status | String |   | The request status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=LouauditCleanData&RegionId=cn-hangzhou&keep_time=1722478948
```

Sample success responses `JSON` format

```json
Content-Type:application/json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
```

`XML` format

```xml
Content-Type:application/xml <LouauditCleanDataResponse>
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
</LouauditCleanDataResponse>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | 1001API is required. |
| 500 |   | InternalError | An unknown error occurred. |
