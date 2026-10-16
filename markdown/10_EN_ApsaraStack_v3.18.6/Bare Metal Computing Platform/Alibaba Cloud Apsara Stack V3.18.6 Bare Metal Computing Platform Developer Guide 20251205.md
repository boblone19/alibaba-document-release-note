---
title: "Bare Metal Computing Platform Developer Guide 20251205"
product_version: "V3.18.6"
pdf_pages: 158
source_pdf: "c245a5536e4728eb_Alibaba Cloud Apsara Stack V3.18.6 Bare Metal Computing Platform Developer Guide 20251205.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%A3%B8%E9%87%91%E5%B1%9E%E7%AE%97%E5%8A%9B%E5%B9%B3%E5%8F%B0BMCP/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Bare%20Metal%20Computing%20Platform%20Developer%20Guide%2020251205.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Bare Metal Computing Platform Developer Guide 20251205

## Table of Contents

- 1 Getting started
  - 1.1 Obtain an AccessKey
  - 1.2 Obtain API information and endpoints
  - 1.3 Call Apsara Stack APIs using POP Gateway
- 2 API Reference
  - 2.1 ListPaiSSOInfo
  - 2.2 DescribePaiSSOInfo
  - 2.3 CreatePaiSSOInfo
  - 2.4 ModifyAckClusterDeletionProtection
  - 2.5 DescribeAckClusterLogs
  - 2.6 DescribeAckClusterAddon
  - 2.7 ListAvailableBmsInstance
  - 2.8 DeleteAiDomain
  - 2.9 CreateAiDomain
  - 2.10 InstallAIAddOn
  - 2.11 DeleteBmsCluster
  - 2.12 CreateSp
  - 2.13 DeleteAckCluster
  - 2.14 DeleteAIAddOn
  - 2.15 ListHistoryEvent
  - 2.16 DeleteBmsClusterInstances
  - 2.17 ListReStartEvent
  - 2.18 CreateBmsCluster
  - 2.19 AddBmsClusterInstances
  - 2.20 CreateAckCluster
  - 2.21 ListAckClusterInstances
  - 2.22 ListAckCluster
  - 2.23 DescribeBmsCluster
  - 2.24 DescribeAckCluster
  - 2.25 DeleteAckClusterInstances
  - 2.26 ListBmsCluster
  - 2.27 AddAckClusterInstances
  - 2.28 ListAckInstanceType
  - 2.29 DescribeEasyAIStatus
  - 2.30 ListInstanceTypeDiskCategory
  - 2.31 ModifySecurityGroupRule
  - 2.32 ModifySecurityGroup
  - 2.33 ListSecurityGroupRule
  - 2.34 GetAISuiteK8SToken
  - 2.35 ProxyAISuiteDev
  - 2.36 AIRListAcrImages
  - 2.37 ListQuota
  - 2.38 ListWorkspace
  - 2.39 ListInstance
  - 2.40 ListSecurityGroupInstance
  - 2.41 ListSecurityGroup
  - 2.42 ListKeyPair
  - 2.43 DeleteSecurityGroupRule
  - 2.44 DeleteSecurityGroup
  - 2.45 DeleteKeyPair
  - 2.46 CreateSecurityGroup
  - 2.47 DeleteSecurityGroupInstance
  - 2.48 AddSecurityGroupRule
  - 2.49 AddSecurityGroupInstance
  - 2.50 ListBmcpMachineType
  - 2.51 TagResources
  - 2.52 GetClusterInstanceInfo
  - 2.53 ModifyEvpc
  - 2.54 ListEvpcConnections
  - 2.55 ListEvpc
  - 2.56 DeleteEvpc
  - 2.57 CreateEvpc
  - 2.58 UpgradeAiApplication
  - 2.59 UnInstallAiInstanceResource
  - 2.60 UnInstallAiApplication
  - 2.61 ListAckClusterNodePool
  - 2.62 ListAckClusterApp
  - 2.63 GetClusterInfo
  - 2.64 InstallAiApplication
  - 2.65 DeleteCpfsClientCluster
  - 2.66 CreateCpfsClientCluster
  - 2.67 ListAckClusterEcsWorkerInstances
  - 2.68 UnbindKeyPair
  - 2.69 CreateKeyPair
  - 2.70 ConfigKeyPair
  - 2.71 AIRListConvertJobs
  - 2.72 AIRConvertImageToDADIImage
  - 2.73 CreateEhpcCluster
  - 2.74 DeleteEhpcClusterInstances
  - 2.75 DeleteEhpcCluster
  - 2.76 ListEhpcCluster
  - 2.77 AddEhpcClusterInstances
  - 2.78 DescribeEhpcCluster
  - 2.79 DescribeSpecification
  - 2.80 DescribeInstanceGpuVirt
  - 2.81 CreatInstanceCgpu
  - 2.82 StopInstanceGpuVirt
  - 2.83 CreatInstanceVxpu

## 1 Getting started

### 1.1 Obtain an AccessKey

This topic describes how to obtain an AccessKey ID and an AccessKey secret.

**Background information**

Identity verification uses symmetric encryption with an AccessKey ID and an AccessKey secret to authenticate the request sender. The AccessKey ID identifies the user. The AccessKey secret is a string used to create an encrypted signature. You can use the AccessKey of a personal account to call the APIs of Apsara Uni-manager Management Console and related cloud products.

**Prerequisites**

Only operations administrators and primary organization administrators can obtain an organization's AccessKey.

**Obtain the AccessKey for a personal account**

To obtain the AccessKey for a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the page, hover over your profile picture and click **Personal**
**Information**.
3. In the **Alibaba Cloud AccessKey** area, view the AccessKey information for your personal
account.

**Important**

Your AccessKey ID and AccessKey secret are your credentials for accessing your cloud resources. These keys grant full permissions to your account. Keep them secure.

**Obtain an organization's AccessKey**

**Warning**

The AccessKey pair for a personal account is managed by the permission system of the Apsara Uni-manager Management Console. An organization's AccessKey pair has more permissions than a personal account's AccessKey pair. If you want to obtain an organization's AccessKey pair, you must have approval from an administrator to ensure security. To obtain an organization's AccessKey pair, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management > Organization**
**Management**.
4. In the organization chart, click the name of the target primary organization.
5. Click **Manage AccessKey**.
6. In the dialog box that appears, view the organization's AccessKey information.

### 1.2 Obtain API information and endpoints

**endpoints**

First, you must obtain information about a product's API operations, such as the product name (code), the API operation name, and the API version.

**Background information**

The API information in the API directory of the Apsara Uni-manager Management Console is for reference only. For information about how to use a specific API, see the ASR-BR developer guide. In case of any discrepancy, the information in the developer guide takes precedence.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products > Developer Tools > API & Tools > Developer**
**Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. In the navigation pane on the left, choose **Bare Metal Compute Platform (BMCP)**.
5. From the **Version** drop-down list, select the desired API version.
6. In the API list, you can view all API operations for the current version.
7. Select the desired API operation. You can then view the API information, such as the BMCP
POP Endpoint and RegionId.

### 1.3 Call Apsara Stack APIs using POP Gateway

**POP Gateway**

To access product domains using the POP Java SDK, you must know the product's call method, which can be either RPC or ROA.

**Prerequisites**

Apsara Stack recommends using CommonRequest to make calls. To view the recommended SDK version and sample code, navigate to **Products** > **Application Services** > **Developer**
**Portal** and select **API Integration** > **SDK Sample** in the Apsara Uni-manager Management
Console.

**Important**

Do not download the SDK directly from the SDK Center for use in Apsara Stack. The public cloud SDK may not be compatible with Apsara Stack APIs, which can cause compatibility issues. Use it with caution.

**CommonRequest call example**

This example shows an RPC call with the following API details: Product (BMCP), API (GetClusterInstanceInfo), and Version (2023-11-01). The call example is as follows: Java

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
                // Your region ID.
                "<your-region-id>",
                // Get the AccessKey ID of the RAM user from an environment variable.
                System.getenv("AccessKey"),
                // Get the AccessKey secret of the RAM user from an environment variable.
                System.getenv("AccessKeySecret"));
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set its parameters.
        CommonRequest request = new CommonRequest();
        request.setSysDomain("<bmcpDomain>");
        request.setSysProduct("EasyAI");
        request.setSysVersion("2023-11-01");
        request.setSysAction("GetClusterInstanceInfo");
        request.setSysMethod(MethodType.POST);
        request.setProtocol(com.aliyuncs.http.ProtocolType.HTTP);
        request.putQueryParameter("ClusterId", "*****");
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

**Important**

When you use the HTTPS protocol to access OpenAPI, the SDK enables SSL/TLS certificate validation by default. If your code environment does not have a valid certificate, a certificate validation failed error is reported. To ensure communication security in a production environment, you must keep this feature enabled. To ignore certificate validation in a test environment, you can set the following parameter: Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate validation. clientConfig.setIgnoreSSLCerts(true)
```

## 2 API Reference

This topic provides the API reference.

### 2.1 ListPaiSSOInfo

Lists the PAI SSO logon information.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | No | 1 | The page number for paged queries. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page for a paged query. The default value is 10. |
| Departme nt | String | Query | No | ** | The name of the organization. Used to filter clusters that belong to a specific organization. |
| RegionId | String | Query | No | ** | The ID of the region that is used to filter clusters. |
| All | Boole an | Query | No | false | If this parameter is set to true, the paging parameters are ignored, and the PAI SSO logon information for all clusters is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.2 DescribePaiSSOInfo

Retrieves PAI Single Sign-On (SSO) information.

**Request header**

This operation uses common request headers and does not require any special request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the reused container cluster. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.3 CreatePaiSSOInfo

This operation registers a service provider (SP) with the specified parameters and records the information.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of an existing container cluster. |
| MetaData | String | Query | No | ** | The metadata used to register the SP. The value must be a Base64- encoded string. If you specify this parameter, this metadata is used for registration. If you do not specify this parameter, the system generates default metadata. |
| Uid | String | Query | No | ** | The UID of the account to associate during SP registration. |
| Admin | String | Query | No | ** | The redirect account for the Admin role in single sign-on (SSO) logon mode. |
| Auditor | String | Query | No | ** | The redirect account for the Auditor role in SSO logon mode. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Domain | String | Query | No | ** | The domain name of the PAI console. |
| SlbIp | String | Query | No | ** | The Server Load Balancer (SLB) IP address associated with the PAI console domain name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.4 ModifyAckClusterDeletionProtection

Modifies the deletion protection status of an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| DeletionPr otection | Boole an | Query | No | true | The deletion protection status. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |

|   |   |   | Bare Metal Computing Platform D eveloper Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.5 DescribeAckClusterLogs

Retrieves the logs of an ACK cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.6 DescribeAckClusterAddon

Retrieves the installation status of components in an ACK cluster.

**Request headers**

This operation requires only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| AddonTyp e | String | Query | No | AI | The type of the component. Valid value: AI. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.7 ListAvailableBmsInstance

Lists the instances that can be added to a cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The name of the organization to which the instance belongs. |
| ResourceG roup | String | Query | No | ** | The name of the resource set used to classify the instance. |
| VpcId | String | Query | No | "" | The ID of the Virtual Private Cloud (VPC). This parameter filters bare machine instances in a specific VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.8 DeleteAiDomain

Deletes a domain name from the AI console.

**Request header**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Paramet er Name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

**Returned data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the returned message. |
| errorMessage | String | Successful | The content of the returned message. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status code of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | The version of the response. |

### 2.9 CreateAiDomain

Creates a domain name for the AI console.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| SlbIp | String | Query | No | ** | The IP address of the Server Load Balancer (SLB) that is associated with the AI console domain name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.10 InstallAIAddOn

Installs the AI suite on an ACK cluster.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| VswitchIdL ist | Json | Query | No | ** | The list of vSwitch IDs for the node pool. This parameter is used for network configuration. |
| SystemDis kCategory | String | Query | No | ** | The type of the system disk, such as ultra disk. |
| SystemDis kSize | Integ er | Query | No | 1 | The size of the system disk for worker nodes, in GB. |
| DataDisk | Json | Query | No | ** | The list of data disk information, including the type and size. |
| Password | String | Query | No | ** | The logon password for the cluster nodes. |
| Platform | String | Query | No | ** | The platform type, such as x86 or arm. |
| ImageId | String | Query | No | ** | The ID of the image to use. |
| InstanceTy peList | Json | Query | No | ** | The list of instance types to add to the cluster. |
| AdminUid | String | Query | No | ** | The UID of the administrator who installs the AI suite. |
| Runtime | String | Query | No | ** | The container runtime environment. |
| NasEndpoi nt | String | Query | No | ** | The NAS endpoint. |

| Bare Metal Co | mputing | Platform D |   |   |   |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SlbIp | String | Query | No | ** | The IP address of the SLB instance that corresponds to the domain name of the AI console. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

### 2.11 DeleteBmsCluster

Deletes a basic bare machine cluster.

**Request headers**

This operation uses only common request headers. For more information, see the document about common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster to delete. |
| InstanceLi st | Json | Query | No | ** | The list of bare machines to delete from the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

| Bare Metal Compu veloper Guide·AP | ting Platform D I Reference |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersio n | String | v1 | The returned version. |

### 2.12 CreateSp

Creates an SP for an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.13 DeleteAckCluster

Deletes an ACK cluster.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| InstanceLi st | Json | Query | No | ** | The list of bare metal instances to remove from the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.14 DeleteAIAddOn

Deletes the AI suite installed on an ACK cluster.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to the title. |
| errorMessage | String | Successful | The message returned. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

### 2.15 ListHistoryEvent

This operation retrieves the details of historical tasks.

**Request header**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | String | Query | No | "0001-01-01" | The start time in YYYY- MM-DD format. This parameter specifies the beginning of the time range for the task history. This parameter is not used if LastAddon is set to true. |
| EndTime | String | Query | No | "" | The end time in YYYY- MM-DD format. This parameter specifies the end of the time range for the task history. This parameter is not used if LastAddon is set to true. |
| ClusterId | String | Query | No | "" | The cluster ID. This parameter filters the task history for a specific cluster. |
| PageNumb er | Integ er | Query | No | 1 | The page number for paging. This parameter specifies the page number of the returned results. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The page size for paging. This parameter specifies the number of results to return on each page. The default value is 10. |
| LastAddon | Boole an | Query | No | true | This is the most recent one. |
| EventType | String | Query | No | all | The task type. Valid values are 'all' for all tasks, 'cluster' for cluster tasks, and 'ai' for AI suite tasks. The default value is 'all'. |
| EventNam e | String | Query | No | "" | The task name. This parameter filters tasks by name. This is a new filter condition. |

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Status | String | Query | No | ** | The status. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The return message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.16 DeleteBmsClusterInstances

This operation scales in a bare machine cluster.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| InstanceId List | Json | Query | No | ** | The list of instance IDs to remove from the cluster. |
| InstanceLi st | Json | Query | No | ** | The list of bare machines to delete from the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.17 ListReStartEvent

Retries a specified task.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| TaskId | String | Query | No | ** | The unique identifier of the task. |

|   |   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VswitchIdL ist | Json | Query | No | ** | The vSwitch of the bare metal machine. You can change the vSwitch when you retry the task. |
| EvpcId | String | Query | No | ** | The EVPC of the cluster. You can change the EVPC when you retry the task. |
| DeleteApp lyFailedIns tanceNam eList | Json | Query | No | ** | The instance names of the bare metal machines to remove because their requests failed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.18 CreateBmsCluster

Creates a basic bare metal cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The name of the organization that owns the resource. |
| ResourceG roup | String | Query | No | ** | The name of the resource set. Use this to classify and manage resources. |
| RegionId | String | Query | No | ** | The ID of the region for the cluster deployment. |
| VpcId | String | Query | No | ** | The ID of the VPC where the cluster will be deployed. |

|   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | String | Query | No | ** | The name of the cluster. The name must be unique. |
| Descriptio n | String | Query | No | ** | A description of the cluster. |
| Password | String | Query | No | ** | The logon password for the cluster instances. This password secures the cluster. |
| AddBmsIn stanceList | Json | Query | No | [] | The list of instances. |
| ApplyBmsI nstanceLis t | Json | Query | No | ** | The list of parameters for requesting bare metal instances. This is used for managed clusters. |
| ZoneId | String | Query | No | ** | The ID of the zone where the cluster will be deployed. |
| ClusterArc hType | String | Query | No | ** | The instance type of the cluster. Valid values: `standard` (general- purpose intelligent computing cluster instance) and `managed` (managed intelligent computing cluster instance). |
| MachineTy peList | Json | Query | No | ** | The selected machine types and their quantities for creating a general-purpose bare metal cluster. |
| VswitchIdL ist | Json | Query | No | ** | The list of VSwitch IDs to which the bare metal instances will connect. |
| StandardV switchId | String | Query | No | ** | The VSwitch ID. |

| Bare Metal Co | mputing | Platform D |   |   |   |
|---|---|---|---|---|---|

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| EvpcId | String | Query | No | ** | This parameter is required for general- purpose clusters. If you specify this parameter, the instances are added to the corresponding EVPC. |
| VolumeId | String | Query | No | ** | The storage ID. |
| MountPath | String | Query | No | ** | The mount path. |
| ActivationI d | String | Query | No | ** | The Cloud Assistant activation ID for creating the bare metal cluster. |
| Activation Code | String | Query | No | ** | The Cloud Assistant activation code for creating the bare metal cluster. |
| IsCreateC pfsCluster | Boole an | Query | No | true | Specifies whether to create a CPFS cluster. This parameter is required for general- purpose clusters. To create a CPFS cluster, you must specify an `EvpcId` and have at least three bare metal nodes. |
| VolumeInf o | Json | Query | No | ** | The mount information for third-party storage. This parameter is used for managed clusters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | The version of the response. |

### 2.19 AddBmsClusterInstances

Adds instances to a basic bare machine cluster.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| InstanceLi st | Json | Query | No | [] | The list of instances. |
| Password | String | Query | No | ** | The password. |
| MachineTy peList | Json | Query | No | ** | The instance types and the number of instances required to scale out the general-purpose bare machine cluster. |
| ApplyBmsI nstanceLis t | Json | Query | No | ** | The list of parameters for requesting bare machines. This parameter is used for managed clusters. |
| VswitchIdL ist | Json | Query | No | ** | The list of VSwitch IDs. This parameter specifies the VSwitches to which the scale-out nodes connect and is required for scale-out operations. |
| ActivationI d | String | Query | No | ** | The unique identifier of Cloud Assistant for scaling out the bare machine cluster. |
| Activation Code | String | Query | No | ** | The Cloud Assistant activation code required for scaling out the bare machine cluster. |
| ZoneId | String | Query | No | ** | The ID of the zone where the cluster is located. This parameter is required if no zone is set for the cluster. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |

|   |   |   | Bare Metal Computing Platform D eveloper Guide·API Referenc |
|---|---|---|---|
| Parameter name | Type | Example | Description |
| errorTitle | String | Successful | Return to the title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.20 CreateAckCluster

Creates an ACK cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The name of the organization that owns the resource. |
| ResourceG roup | String | Query | No | ** | The name of the resource group. Use resource groups to classify and manage resources. |
| RegionId | String | Query | No | ** | The region ID. This specifies the geographic location where the cluster is deployed. |
| ClusterNa me | String | Query | No | ** | The unique name of the ACK cluster. |
| Descriptio n | String | Query | No | ** | The description of the cluster. |
| Password | String | Query | No | ** | The logon password for the machines in the cluster to ensure security. |
| ApplyBmsI nstanceLis t | Json | Query | No | [] | The list of requested instances. |
| VpcId | String | Query | No | ** | The ID of the VPC. The cluster is deployed in the specified VPC. |
| VswitchIdL ist | Json | Query | No | ** | A list of vSwitch IDs to which the bare metal instances connect. |
| Kubernete sVersion | String | Query | No | ** | The version of Kubernetes that the cluster runs. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Runtime | String | Query | No | ** | The container runtime. The example value is for reference only. |
| MasterCou nt | Integ er | Query | No | 1 | The number of primary nodes in the cluster. |
| MasterInst anceTypeL ist | Json | Query | No | ** | A list of instance types for the primary nodes. |
| MasterSys temDiskCa tegory | String | Query | No | ** | The type of the system disk for the primary nodes. |
| MasterSys temDiskSi ze | String | Query | No | ** | The size of the system disk for the primary nodes. |
| WorkerCo unt | Integ er | Query | No | 1 | The number of ECS worker nodes in the cluster. |
| WorkerSys temDiskSi ze | String | Query | No | 1 | The size of the system disk for the ECS worker nodes. |
| WorkerSys temDiskCa tegory | String | Query | No | ** | The type of the system disk for the ECS worker nodes. |
| WorkerVs witchIdList | Json | Query | No | ** | A list of vSwitches for the ECS worker nodes. |
| WorkerInst anceTypeL ist | Json | Query | No | ** | A list of instance types for the ECS worker nodes. You can specify up to 10 instance types. |
| WorkerDat aDiskList | Json | Query | No | ** | The information about the data disks for the ECS worker nodes. You can specify up to 10 data disks. |
| Os | String | Query | No | ** | The type of the operating system. |

| e | Bare Metal Co veloper Guid | mputing e·API Ref | Platform D erence |   |   |   |   |
|---|---|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Platform | String | Query | No | ** | The type of the platform. |
| ImageTyp e | String | Query | No | ** | The type of the image. |
| PodCidr | String | Query | No | ** | The CIDR block for pods. |
| ServiceCid r | String | Query | No | ** | The CIDR block for services. |
| SnatEntry | Boole an | Query | No | true | Specifies whether to configure an SNAT entry. |
| EndpointP ublicAcces s | Boole an | Query | No | true | Specifies whether to expose the API Server through an EIP. |
| SshFlag | Boole an | Query | No | true | This parameter is for general-purpose clusters. You must specify this parameter if `EndpointPublicAccess` is set to `true`. |
| LogServic e | Boole an | Query | No | true | Specifies whether to use Simple Log Service. |
| LogProject | String | Query | No | ** | The name of the log project. This parameter is required if you use Simple Log Service. |
| DeleteProt ection | Boole an | Query | No | true | Specifies whether to enable deletion protection for the cluster. |
| InstanceD eleteProte ction | Boole an | Query | No | true | Specifies whether to enable deletion protection for instances. |
| ZoneId | String | Query | No | ** | The ID of the zone. |
| ClusterArc hType | String | Query | No | ** | The type of the cluster. Valid values: `standard` and `managed`. |

|   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MachineTy peList | Json | Query | No | ** | A list of bare metal machine types to add to the ACK cluster. This parameter is used for general-purpose clusters. |
| BmsVswitc hIdList | Json | Query | No | ** | This parameter is required if you specify `MachineTypeList`. This parameter is used for general-purpose clusters. |
| EvpcId | String | Query | No | ** | The ID of the EVPC. This parameter is required for general-purpose clusters. |
| ActivationI d | String | Query | No | ** | The ID of the Cloud Assistant. This parameter is used for general-purpose clusters. |
| Activation Code | String | Query | No | ** | The activation code for Cloud Assistant. This parameter is used for general-purpose clusters. |
| VolumeId | String | Query | No | ** | The volume ID. |
| MountPath | String | Query | No | ** | The mount path. |
| IsCreateC pfsCluster | Boole an | Query | No | true | Specifies whether to create a CPFS cluster. This parameter is for general-purpose clusters. To create a CPFS cluster, you must specify an `EvpcId` and have three or more bare metal nodes. |
| ClassicSlb Spec | String | Query | No | ** | Classic Load Balancer |

| e | Bare Metal Co veloper Guid | mputing e·API Ref | Platform D erence |   |   |   |   |
|---|---|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IsCreateCl assicSlb | Boole an | Query | No | true | Specifies whether to create a CLB instance. |
| VolumeInf o | Json | Query | No | ** | The mount information for third-party storage on a managed cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | You can return to the title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The HTTP status code. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | The version of the response. |

### 2.21 ListAckClusterInstances

Lists ACK cluster instances.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | ** | The resource group. |
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |
| State | String | Query | No | "" | The running status of the node. The default value is empty. |
| NodePoolI d | String | Query | No | "" | The ID of the node pool. The default value is empty. |
| PageNumb er | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The default value is 10. |

**Response parameters**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

### 2.22 ListAckCluster

Lists ACK clusters.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | Filters the list of clusters by organization. |
| ResourceG roup | String | Query | No | ** | Filters the list of clusters by resource group. |
| ClusterNa me | String | Query | No | ** | Filters the list of clusters by cluster name. |
| AckCluster Name | String | Query | No | ** | Filters the list of clusters by ACK cluster name. |
| ClusterId | String | Query | No | ** | Filters the list of clusters by cluster ID. |
| AckCluster Id | String | Query | No | ** | Filters the list of clusters by ACK cluster ID. |
| Status | String | Query | No | ** | Filters the list of clusters by cluster status. |
| PageNumb er | Integ er | Query | No | 1 | The page number. Default value: 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page. Default value: 10. |

**Returned data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | Go back to the title. |

| Bare Metal Compu veloper Guide·AP | ting Platform D I Reference |   |   |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | Successful | Returned information. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | The response version. |

### 2.23 DescribeBmsCluster

Describes a bare machine cluster.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.24 DescribeAckCluster

Retrieves the details of an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.25 DeleteAckClusterInstances

Removes instances from an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |
| InstanceId List | Json | Query | No | ** | A list of instance IDs to remove from the cluster. |
| InstanceLi st | Json | Query | No | ** | A list of bare metal instances to remove from the cluster. |
| EcsInstanc eIdList | Json | Query | No | ** | A list of ECS node IDs to remove. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The response title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | The version of the response. |

### 2.26 ListBmsCluster

This operation lists basic bare machine clusters.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | Filters the list of clusters by organization. |
| ResourceG roup | String | Query | No | ** | Filters the list of clusters by resource group. |
| ClusterNa me | String | Query | No | ** | Filters the list of clusters by cluster name. |
| ClusterId | String | Query | No | ** | Filters the list of clusters by cluster ID. |
| Status | String | Query | No | ** | Filters the list of clusters by cluster status. |
| PageNumb er | Integ er | Query | No | 1 | The page number for a paged query. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries on each page for a paged query. The default value is 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to the title. |
| errorMessage | String | Successful | The returned message. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.27 AddAckClusterInstances

This operation scales out an ACK cluster.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the Common Request Parameters document.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| ApplyBmsI nstanceLis t | Json | Query | No |   | The list of requested instances. |
| Password | String | Query | No | ** | The password for the bare machine. This parameter is required if a password has not been set for the cluster. |
| MachineTy peList | Json | Query | No | ** | The list of bare machine instance types to add to the ACK cluster. This parameter is used for general-purpose clusters. |
| BmsVswitc hIdList | Json | Query | No | ** | The list of vSwitch IDs. This parameter is required when you scale out a general-purpose cluster. |
| ActivationI d | String | Query | No | ** | The ID of Cloud Assistant. This parameter is required for general-purpose clusters. |
| Activation Code | String | Query | No | ** | The activation code for Cloud Assistant. This parameter is required for general-purpose clusters. |
| ZoneId | String | Query | No | ** | The zone ID of the general-purpose cluster. This parameter is required if a zone has not been set for the cluster. |
| WorkerCo unt | Integ er | Query | No | 1 | The number of worker nodes to add. |
| WorkerSys temDiskSi ze | String | Query | No | 1 | Resize the system disk of an ECS node. |

| Bare Metal Co veloper Guid | mputing e·API Ref | Platform D erence |   |   |   |
|---|---|---|---|---|---|

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| WorkerSys temDiskCa tegory | String | Query | No | ** | The system disk type of the worker nodes to add. |
| WorkerVs witchIdList | Json | Query | No | ** | The list of vSwitches for the worker nodes to add. |
| WorkerInst anceTypeL ist | Json | Query | No | ** | The list of instance types for the worker nodes to add. You can specify up to 10 instance types. |
| WorkerDat aDiskList | Json | Query | No | ** | The information about the data disks for the worker nodes to add. You can specify up to 10 data disks. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.28 ListAckInstanceType

Lists the supported instance types for Container Service for Kubernetes (ACK) clusters.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | ** | The resource group. |
| ClusterNa me | String | Query | No | ** | The name of the cluster. |
| AckCluster Name | String | Query | No | ** | The name of the ACK cluster. |
| ClusterId | String | Query | No | ** | The ID of the cluster. |
| AckCluster Id | String | Query | No | ** | The ID of the ACK cluster. |

| e | Bare Metal Co veloper Guid | mputing e·API Ref | Platform D erence |   |   |   |   |
|---|---|---|---|---|---|---|---|

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Status | String | Query | No | ** | The status. |
| ZoneId | String | Query | No | ** | The zone. To specify multiple zones, separate them with commas (,). For example: `zone1,zone2`. |
| VpcAdvan cedResour ce | Boole an | Query | No | true | Specifies whether to enable advanced features for the VPC. |
| NodeType | String | Query | No | ** | The type of ACK node. Valid values: `master` and `worker`. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.29 DescribeEasyAIStatus

Queries the status of the EasyAI service.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Return to the title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The request ID. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.30 ListInstanceTypeDiskCategory

Lists the disk types that an instance type supports.

**Request header**

This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | ** | The resource set. |

|   |   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | String | Query | No | ** | The cluster name. |
| AckCluster Name | String | Query | No | ** | The ACK cluster name. |
| ClusterId | String | Query | No | ** | The cluster ID. |
| AckCluster Id | String | Query | No | ** | The ACK cluster ID. |
| Status | String | Query | No | ** | The status. |
| InstanceTy peList | Json | Query | No | ** | A list of instance types. |
| DiskType | String | Query | No | ** | The disk type to query. Valid values: `SystemDisk` and `DataDisk`. |
| SystemDis kCategory | String | Query | No | ** | This parameter is required if you set `DiskType` to `DataDisk`. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The return message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

| e | Bare Metal Compu veloper Guide·AP | ting Platform D I Reference |   |   |   |
|---|---|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.31 ModifySecurityGroupRule

Modifies a security group rule.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| SgrId | String | Query | No | ** | The ID of the rule. |
| Direction | String | Query | No | ** | The direction of the rule. |

|   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AccessPoli cy | String | Query | No | ** | The access permissions. |
| IpProtocol | String | Query | No | ** | The transport-layer protocol. |
| PortRange | String | Query | No | ** | The port range. |
| Priority | Integ er | Query | No | 1 | The priority of the rule. |
| IpVersion | String | Query | No | ** | The IP version. |
| CidrIp | String | Query | No | ** | The source IPv4 CIDR block. |
| RelatedGr oupId | String | Query | No | ** | The ID of the authorized security group. |
| Descriptio n | String | Query | No | ** | The description. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.32 ModifySecurityGroup

Modifies a security group.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| Name | String | Query | No | ** | The name of the security group. |
| Descriptio n | String | Query | No | ** | The description of the security group. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

Response in `JSON` format Response in `XML` format

### 2.33 ListSecurityGroupRule

Lists security group rules.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| Direction | String | Query | No | ** | The direction of the rule. |
| PageNumb er | Integ er | Query | No | 1 | The number of the page to return. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.34 GetAISuiteK8SToken

Retrieves the token for an AI suite.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| AckCluster Id | String | Query | No | ** | The ID of the ACK cluster. |
| UserId | String | Query | No | ** | The user ID. |
| Username | String | Query | No | ** | The username. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.35 ProxyAISuiteDev

Calls the AI suite.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AckCluster Id | String | Query | No | ** | The ID of the ACK cluster. |
| Path | String | Query | No | ** | The path. |
| Method | String | Query | No | ** | The method. |
| IsLongCon n | Boole an | Query | No | true | Specifies whether to use a long-lived connection. |
| ExtraHead er | Json | Query | No | {} | The header parameters. |
| ContentTy pe | String | Query | No | ** | The content type. |
| JSONBody | String | Query | No | ** | The body parameters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.36 AIRListAcrImages

Retrieves a list of ACR images.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Category | String | Query | No | ** | The filter item. |
| Search | String | Query | No | ** | The filter value. |
| Departme nt | String | Query | No | ** | The organization ID. |
| PageNumb er | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.37 ListQuota

Lists all quotas.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The ID of the cluster. |
| PageNumb er | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |
| SortField | String | Query | No | ** | The field to use for sorting. |
| SortType | String | Query | No | ** | The sort order. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.38 ListWorkspace

Retrieves a list of workspaces.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |
| ClusterId | String | Query | No | ** | The cluster ID. |

| Bare Metal Co veloper Guid | mputing e·API Ref | Platform D erence |   |   |   |
|---|---|---|---|---|---|

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SortField | String | Query | No | ** | The field to use for sorting. |
| SortType | String | Query | No | ** | The sort type. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.39 ListInstance

Retrieves a list of instances.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |
| InstanceN ame | String | Query | No | ** | The instance name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.40 ListSecurityGroupInstance

Lists the instances that are attached to a security group.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| SN | String | Query | No | ** | The SN. |

|   |   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceN ame | String | Query | No | ** | The name of the instance. |
| PageNumb er | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.41 ListSecurityGroup

Lists security groups.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er Name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | ** | The resource set. |
| RegionId | String | Query | No | ** | The region ID. |
| Name | String | Query | No | ** | The name of the security group. |
| SgId | String | Query | No | ** | The ID of the security group. |
| VpcId | String | Query | No | ** | The ID of the VPC. |
| Type | String | Query | No | ** | The type of the security group. |
| DeployTyp e | String | Query | No | ** | The deployment type. |
| PageNumb er | Integ er | Query | No | 1 | The page number. |

| Paramet er Name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 1 | The number of entries per page. |

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.42 ListKeyPair

Lists key pairs.

**Request header**

This operation uses common request headers. No special request headers are used. For more information, see Common Request Parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | String | Query | No | ** | Name |
| PageNumb er | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The default value is 10. |
| KeyPairFin gerPrint | String | Query | No | ** | The fingerprint of the key pair. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.43 DeleteSecurityGroupRule

Deletes a security group rule.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| SgrId | String | Query | No | ** | The ID of the rule. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.44 DeleteSecurityGroup

Deletes a security group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The returned version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.45 DeleteKeyPair

Deletes a key pair.

**Request header**

This operation uses common request headers and does not require any special request headers. For more information, see the Common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | String | Query | No | ** | The name of the key pair. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.46 CreateSecurityGroup

Creates a security group.

**Request header**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | Organization. |
| ResourceG roup | String | Query | No | ** | The resource group. |
| RegionId | String | Query | No | ** | The ID of the region. |
| Name | String | Query | No | ** | The name of the security group. |
| VpcId | String | Query | No | ** | The VPC instance ID. |
| Type | String | Query | No | ** | The type of the security group. |
| DeployTyp e | String | Query | No | ** | The deployment type. |
| Descriptio n | String | Query | No | ** | The description of the resource. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersio n | String | v1 | The version of the response. |

### 2.47 DeleteSecurityGroupInstance

You can configure a security group instance.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| InstanceN ameList | Json | Query | No | ** | A list of instance names. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Return to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.48 AddSecurityGroupRule

Adds a security group rule.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| Direction | String | Query | No | ** | The direction of the rule. |
| AccessPoli cy | String | Query | No | ** | The access permissions. |
| IpProtocol | String | Query | No | ** | The transport-layer protocol. |
| PortRange | String | Query | No | ** | The port range. |
| Priority | Integ er | Query | No | 1 | The priority of the rule. |
| IpVersion | String | Query | No | ** | The IP version. The example value is for reference only. |
| CidrIp | String | Query | No | ** | The source IPv4 CIDR block. |
| RelatedGr oupId | String | Query | No | ** | The ID of the authorized security group. |
| Descriptio n | String | Query | No | ** | The description. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | This operation returns the title. |
| errorMessage | String | Successful | The message returned. |

| Bare Metal Compu veloper Guide·AP | ting Platform D I Reference |   |   |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

### 2.49 AddSecurityGroupInstance

Adds an instance to a security group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | String | Query | No | ** | The ID of the security group. |
| InstanceN ameList | Json | Query | No | ** | A list of instance names. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.50 ListBmcpMachineType

Retrieves a list of BMCP machine types.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MachineTy pe | String | Query | No | "" | The name of the machine type. Use this parameter to filter for specific machine types. |
| CPUArch | String | Query | No | "" | The CPU architecture. Use this parameter to filter for machine types with a specific architecture. |
| DiskType | String | Query | No | "" | The disk type. Use this parameter to filter for machine types with a specific disk type. |
| Manufactu rer | String | Query | No | "" | The name of the manufacturer. Use this parameter to filter for machine types produced by a specific manufacturer. |

| Paramet er name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ZoneId | String | Query | No | "" | The zone. If a zone is specified, the system counts the number of available general- purpose instances in that zone. If a zone is not specified, the system counts the number of available general- purpose instances in all zones for the machine type. |
| PageNumb er | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The default value is 10. |
| DeployTyp es | Json | Query | No | "["bmcp"]" | A list of machine type categories to query. Valid values: bmcp and ehpc. |
| Specificati on | String | Query | No | ** | The specification. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

| Bare Metal Compu veloper Guide·AP | ting Platform D I Reference |   |   |
|---|---|---|---|
| Parameter name | Type | Example | Description |
| responseVersio n | String | v1 | The response version. |

### 2.51 TagResources

Adds tags to a cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | ** | The ID of the region where the resource resides. |
| ResourceT ype | String | Query | Yes | "CLUSTER" | The resource type. The value can only be `CLUSTER`. |

|   |   |   |   | Bare M ev | etal Computing Platform D eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Tags | Json | Query | No | ** | The key-value pairs of the tags. The array can contain 1 to 20 tags. Note: A tag key cannot start with `aliyun` or `acs:`, nor can it contain `http://` or `https://`. A tag value cannot be an empty string and can be up to 128 characters long. |
| ResourceI ds | Json | Query | No | ** | A list of resource IDs. Note: Use the cluster IDs of Container Service for Kubernetes (ACK) clusters. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.52 GetClusterInstanceInfo

Retrieves a list of cluster instances.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | ** | The resource group. |
| ClusterId | String | Query | No | ** | The cluster ID. |
| State | String | Query | No | ** | The running status of the cluster. |
| PageNumb er | Integ er | Query | No | 1 | The page number. |

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The value cannot exceed 50. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.53 ModifyEvpc

Modifies an Evpc.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| EvpcName | String | Query | No | "" | The new display name for the Evpc. |
| Descriptio n | String | Query | No | "" | The new description for the Evpc. |
| EvpcId | String | Query | No | ** | The unique identifier of the Evpc. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The response title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.54 ListEvpcConnections

Lists the connections for a specified Evpc.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| EvpcId | String | Query | No | "" | The unique ID of the Evpc. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

`JSON` example `XML` example

### 2.55 ListEvpc

Lists Evpcs.

**Request header**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Query | No | 1 | The page number for a paged query. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The default value is 10. |
| EvpcId | String | Query | No | "" | The unique identifier of the enterprise VPC. |
| EvpcName | String | Query | No | "" | The name of the enterprise VPC. |
| Cidr | String | Query | No | "" | The CIDR notation of the enterprise VPC. It specifies the IP address range. |
| Departme nt | String | Query | No | "" | The name of the organization to which the enterprise VPC belongs. |
| ResourceG roup | String | Query | No | "" | The name of the resource group to which the enterprise VPC belongs. |
| Status | String | Query | No | "" | The current status of the enterprise VPC. |
| TenantId | String | Query | No | "" | The ID of the tenant associated with the enterprise VPC. |
| Descriptio n | Boole an | Query | No | ** | The description. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The return message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.56 DeleteEvpc

Deletes an Evpc.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| EvpcId | String | Query | No | "" | The unique identifier of the Evpc. |
| Force | Boole an | Query | No | false | Specifies whether to force delete the Evpc and all its linked instances. The default value is false. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The response title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.57 CreateEvpc

Creates an Evpc.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | "" | The organization or department to which the Evpc belongs. |
| ResourceG roup | String | Query | No | "" | The resource group used to classify the Evpc. |
| RegionId | String | Query | No | "" | The ID of the region where you want to create the Evpc. |
| EvpcName | String | Query | No | "" | The name of the Evpc instance. |

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Descriptio n | String | Query | No | "" | A detailed description of the Evpc. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The return message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.58 UpgradeAiApplication

Upgrades an AI application in an ACK cluster.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The cluster ID. |
| AppName | String | Query | No | ** | The name of the application to update. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to the title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.59 UnInstallAiInstanceResource

Uninstalls an AI instance resource and all its AI applications from an ACK cluster.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The cluster ID. |
| AppNameL ist | Json | Query | No | ** | The list of apps to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to top. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.60 UnInstallAiApplication

Uninstalls an AI application from an ACK cluster.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The cluster ID. |
| AppName | String | Query | No | ** | The name of the application to uninstall. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.61 ListAckClusterNodePool

Lists the node pools for a container cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | ** | The resource group. |
| ClusterId | String | Query | Yes | ** | The unique identifier of the cluster. |
| Type | String | Query | No | ** | The type of the node pool. Valid values: bmcp and ecs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.62 ListAckClusterApp

Retrieves a list of AI applications in an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The return title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | Returns the current version. |

### 2.63 GetClusterInfo

Retrieves a list of ACK cluster information.

**Request headers**

This operation uses common request headers. For more information, see Common parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | Filters the cluster list by organization. |
| ResourceG roup | String | Query | No | ** | Filters the cluster list by resource group. |
| Status | String | Query | No | ** | Filters the cluster list by cluster status. |
| PageNumb er | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The default value is 10. |
| ClusterTyp e | String | Query | No | ** | The cluster type. |
| ClusterId | String | Query | No | ** | Filters the cluster list by cluster ID. |
| AckCluster Id | String | Query | No | ** | Filters the cluster list by ACK cluster ID. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | String | Query | No | ** | Filters the cluster list by cluster name. |
| AckCluster Name | String | Query | No | ** | Filters the cluster list by ACK cluster name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to the title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.64 InstallAiApplication

Installs an AI application in an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The ID of the cluster. |
| AppName | String | Query | No | ** | The name of the application to install. |
| IsInstallIns tanceReso urce | Boole an | Query | No | true | Specifies whether to install instance resources for the application in the ACK cluster. |
| VswitchIdL ist | Json | Query | No | ** | A list of virtual switch IDs. This specifies the VSwitches to which the bare metal instances connect. |
| AddonSyst emDiskCat egory | String | Query | No | ** | The type of the system disk, such as an ultra disk. |
| AddonSyst emDiskSiz e | Integ er | Query | No | 1 | The size of the system disk for worker nodes, in GB. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DataDisk | Json | Query | No | ** | A list of data disk information, such as the type and size. |
| Password | String | Query | No | ** | The password. |
| Platform | String | Query | No | ** | The platform type. |
| ImageId | String | Query | No | ** | The ID of the image to use. |
| AddonInst anceTypeL ist | Json | Query | No | ** | A list of instance types to add to the cluster. |
| AdminUid | String | Query | No | ** | The UID of the administrator who installs the AI suite. |
| Runtime | String | Query | No | ** | The runtime to use. |
| NasEndpoi nt | String | Query | No | ** | The NAS endpoint. |
| SlbIp | String | Query | No | ** | The SLB IP address. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The ID of the request. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | Retrieves the version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.65 DeleteCpfsClientCluster

Deletes a high-performance storage client cluster from a container cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique ID of the cluster. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The response code. |
| errorTitle | String | Successful | The response title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.66 CreateCpfsClientCluster

Creates a client cluster for high-performance storage in a container cluster.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.67 ListAckClusterEcsWorkerInstances

Lists the Elastic Compute Service (ECS) worker instances in an Alibaba Cloud Container Service for Kubernetes (ACK) cluster.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The organization. |
| ResourceG roup | String | Query | No | * | The resource set. |
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. The example value is for reference only. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |

|   |   |   | Bare Metal Computing Platform D eveloper Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.68 UnbindKeyPair

Detaches a key pair.

**Request header**

This operation uses only common request headers. For more information, see the Common request parameters document.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | String | Query | No | ** | The name of the key pair. |
| MachineS NList | Json | Query | No | ** | A list of machine serial numbers (SNs). |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.69 CreateKeyPair

Creates a key pair.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | String | Query | No | ** | The name of the key pair. |
| Departme nt | String | Query | No | ** | The name of the organization to which the resource belongs. |
| ResourceG roup | String | Query | No | ** | The name of the resource group used for resource classification. |
| RegionId | String | Query | No | ** | The region ID. This indicates the geographic location of the cluster deployment. |
| PublicKey | String | Query | No | ** | The public key. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |

| Bare Metal Compu | ting Platform D |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.70 ConfigKeyPair

Attaches a key pair.

**Request header**

This operation uses common request headers. For more information, see Common parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | String | Query | No | ** | The name of the key pair. |
| MachineS NList | Json | Query | No | ** | A list of machine serial numbers (SNs). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Go back to the title. |
| errorMessage | String | Successful | The information that is returned. |
| data | Map | {} | The data returned in the response. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | Indicates whether the request was successful. |
| responseVersio n | String | v1 | The version of the response. |

### 2.71 AIRListConvertJobs

Retrieves a list of accelerated image transformation jobs.

**Request headers**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum | Integ er | Query | No | 1 | The page number for paging. Default value: 1. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page for paging. Default value: 10. |
| ImageRef | String | Query | No | ** | The keyword for a fuzzy query of image names. |
| JobStatus | String | Query | No | ** | The search condition for the job status. Valid values: JOB RUNNING, _ JOB SUCCESS, and _ JOB FAILED. _ |
| OrderBy | String | Query | No | ** | The field to sort by. Valid values: jobID, jobStatus, imageRef, created at _ (sorts by CreatedAt), and updated at (sorts by _ UpdatedAt). |
| Desc | Boole an | Query | No | true | Specifies whether to sort the results in descending order. Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.72 AIRConvertImageToDADIImage

Converts a standard image to a DADI image.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ImageRef | String | Query | No | ** | The URL of the source image to accelerate. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersio n | String | v1 | The version of the response. |

### 2.73 CreateEhpcCluster

Creates an Elastic High Performance Computing (EHPC) cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er Name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | The name of the organization that owns the resource. |
| ResourceG roup | String | Query | No | ** | The name of the resource group used to classify and manage resources. |
| RegionId | String | Query | No | ** | The ID of the region where the cluster is deployed. |
| ZoneId | String | Query | No | ** | The ID of the zone. |

| Bare Metal Co | mputing | Platform D |   |   |   |
|---|---|---|---|---|---|

| Paramet er Name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | String | Query | No | ** | The name of the cluster. The name must be a unique identifier for the ACK cluster. |
| Descriptio n | String | Query | No | ** | A detailed description of the cluster. |
| Password | String | Query | No | ** | The logon password for the machines in the cluster. This password ensures the security of the cluster. |
| DeployMo de | String | Query | No | ** | The deployment type. |
| VpcId | String | Query | No | ** | The ID of the VPC where the cluster is deployed. |
| MachineTy peList | Json | Query | No | ** | A list of bare machine instance types to add to the ACK cluster. This parameter is used for general-purpose or basic clusters. |
| BmsVswitc hIdList | Json | Query | No | ** | This parameter is required if you specify `MachineTypeList`. It is used for general-purpose clusters. |
| StandardV switchId | String | Query | No | ** | The ID of the standard vSwitch. This vSwitch is used to build the network channel for management services. |
| AccountTy pe | String | Query | No | ** | The account type. |
| Scheduler Type | String | Query | No | ** | The scheduling type. |
| ActivationI d | String | Query | No | ** | The ID of Cloud Assistant. This parameter is used for general-purpose clusters. |

| Paramet er Name | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Activation Code | String | Query | No | ** | The activation code for Cloud Assistant. This parameter is used for general-purpose clusters. |
| OsTag | String | Query | No | ** | The operating system type. |
| EvpcId | String | Query | No | ** | The ID of the EVPC. This parameter is required for general-purpose clusters. |
| IsCreateC pfsCluster | String | Query | No | true | Specifies whether to create a CPFS cluster. This parameter is required for general- purpose clusters. To create a CPFS cluster, you must specify an `EvpcId` and have at least three bare machine nodes. |
| CPFSFileS ystem | String | Query | No | ** | The CPFS file system. |

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The title of the response. |
| errorMessage | String | Successful | The message returned. |
| data | Map | {} | The data returned. |
| status | Integer | 200 | The status returned. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

| Bare Metal Compu veloper Guide·AP | ting Platform D I Reference |   |   |
|---|---|---|---|
| Parameter Name | Type | Example | Description |
| responseVersio n | String | v1 | The version of the response. |

Sample response in `JSON` format Sample response in `XML` format

### 2.74 DeleteEhpcClusterInstances

Scales in an Elastic High Performance Computing (E-HPC) cluster.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| InstanceId List | Json | Query | No | ** | A list of instance IDs to remove from the cluster. |

|   |   |   |   | Bare M | etal Computing Platform D |
|---|---|---|---|---|---|

| Paramet er | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceLi st | Json | Query | No | ** | A list of bare metal instances to delete from the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Return to the title. |
| errorMessage | String | Successful | The response message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The response status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

### 2.75 DeleteEhpcCluster

Deletes an Elastic High Performance Computing (EHPC) cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| InstanceLi st | Json | Query | No | ** | The list of bare metal servers to remove from the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |

|   |   |   |   | Bare Metal Computing Platform D eveloper Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| responseVersio n | String | v1 | The response version. |

### 2.76 ListEhpcCluster

Retrieves a list of EHPC clusters.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the document on common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | String | Query | No | ** | Filters the list of clusters by organization. |
| ResourceG roup | String | Query | No | ** | Filters the list of clusters by resource group. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterNa me | String | Query | No | ** | Filters the list of clusters by cluster name. |
| EhpcClust erName | String | Query | No | ** | Filters the list of clusters by EHPC cluster name. |
| ClusterId | String | Query | No | ** | Filters the list of clusters by cluster ID. |
| EhpcClust erId | String | Query | No | ** | Filters the list of clusters by EHPC cluster ID. |
| Status | String | Query | No | ** | Filters the list of clusters by cluster status. |
| PageNumb er | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. The default value is 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The response version. |

Sample response in `JSON` format Sample response in `XML` format

### 2.77 AddEhpcClusterInstances

Scales out an ACK cluster.

**Request header**

This operation uses only common request headers. For more information, see the documentation about common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |
| Password | String | Query | No | ** | The password for the bare machine. This parameter is required if no password has been set for the cluster. |

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MachineTy peList | Json | Query | No | ** | A list of bare machine types to add to the ACK cluster. This parameter is used for general- purpose and basic clusters. |
| BmsVswitc hIdList | Json | Query | No | ** | A list of VSwitch IDs. This parameter is required when you scale out a general-purpose cluster. |
| ActivationI d | String | Query | No | ** | The ID of Cloud Assistant. This parameter is required for general-purpose clusters. |
| Activation Code | String | Query | No | ** | The activation code for Cloud Assistant. This parameter is required for general-purpose clusters. |
| ZoneId | String | Query | No | ** | The zone ID for the general-purpose cluster. This parameter is required if no zone has been set for the cluster. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | Back to top. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The request ID. |

|   |   |   | Bare Metal Computing Platform D eveloper Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The version of the response. |

### 2.78 DescribeEhpcCluster

Queries the details of a specified EHPC cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er name | Type | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | ** | The unique identifier of the cluster. |

| Parameter name | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The return code. |
| errorTitle | String | Successful | The returned title. |
| errorMessage | String | Successful | The returned message. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The returned status. |
| requestId | String | ** | The request ID. |
| success | Boolean | true | The request status. |
| responseVersio n | String | v1 | The returned version. |

### 2.79 DescribeSpecification

Queries the specifications of a GPU.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|
| Gpu | Strin g | Quer y | No | NVIDIA xxxxx | The GPU model. If you leave this parameter empty, all specifications are returned. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | UnknownError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | failed | The error message that is returned when the call fails. |

| data | Map | { "Specification": [ { "Specification": "testxxxx1", "ClusterType": "bmcp managed", _ "Gpu": "Nvidiaxxxxx1", "GpuNumber": 5, "CpuNumber": 1, "CpuManufacturer": "xxxx", "CpuModel": "xxxx", "Memory": 32, "VideoMemory": 0, "TflopsFP32": 0 }, { "Specification": "testxxxx2", "ClusterType": "bmcp managed", _ "Gpu": "Nvidiaxxxxx2", "GpuNumber": 5, "CpuNumber": 1, "CpuManufacturer": "xxxx", "CpuModel": "xxxx", "Memory": 32, "VideoMemory": 0, "TflopsFP32": 0 } ] } | The returned data. |
|---|---|---|---|
| status | Integer | 200 | The response status. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| success | Boolean | true | Returned status. true: The request was successful. Failed: No. |
| responseVersio n | String | v1 | The version number of the API response. It is used to handle different API versions. |

```json
 "data":{
  "Specification":[
    "GpuNumber":5,
    "CpuModel":"xxxx",
    "CpuNumber":1,
    "TflopsFP32":0,
    "Memory":32,
    "CpuManufacturer":"xxxx",
    "Specification":"testxxxx1",
    "ClusterType":"bmcp_managed",
    "VideoMemory":0,
    "Gpu":"Nvidiaxxxxx1"
```

`},`

```json
    "GpuNumber":5,
    "CpuModel":"xxxx",
    "CpuNumber":1,
    "TflopsFP32":0,
    "Memory":32,
    "CpuManufacturer":"xxxx",
    "Specification":"testxxxx2",
    "ClusterType":"bmcp_managed",
    "VideoMemory":0,
    "Gpu":"Nvidiaxxxxx2"
```

`]` `},`

```json
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "errorMessage":"failed",
 "errorCode":"UnknownError",
```

```xml
<data>
 <Specification>
  <GpuNumber>5</GpuNumber>
  <CpuModel>xxxx</CpuModel>
  <CpuNumber>1</CpuNumber>
  <TflopsFP32>0</TflopsFP32>
  <Memory>32</Memory>
  <CpuManufacturer>xxxx</CpuManufacturer>
  <Specification>testxxxx1</Specification>
  <ClusterType>bmcp_managed</ClusterType>
  <VideoMemory>0</VideoMemory>
  <Gpu>Nvidiaxxxxx1</Gpu>
 </Specification>
 <Specification>
  <GpuNumber>5</GpuNumber>
  <CpuModel>xxxx</CpuModel>
  <CpuNumber>1</CpuNumber>
  <TflopsFP32>0</TflopsFP32>
  <Memory>32</Memory>
  <CpuManufacturer>xxxx</CpuManufacturer>
  <Specification>testxxxx2</Specification>
  <ClusterType>bmcp_managed</ClusterType>
  <VideoMemory>0</VideoMemory>
  <Gpu>Nvidiaxxxxx2</Gpu>
 </Specification>
</data> <errorTitle>InternalError</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <errorMessage>failed</errorMessage> <errorCode>UnknownError</errorCode>
```

### 2.80 DescribeInstanceGpuVirt

This operation queries the details of GPU hardware virtualization.

**Request header**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

| Parameter | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|
| InstanceNa me | Strin g | Quer y | No | i-xxxxxxxx | The name of the instance. |

**Returned Data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | UnknownError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | failed | The error message returned if the call fails. |
| data | Map | { "MachineGpu": [ { "ID": "1", "Name": "11", "GPUID": "11", "SN": "1111", "InstanceId": "", "MachineId": "0", "MachineSN": "1111", "Manufacturer": "", "ModelName": "", "UUID": "", "BUSID": "", "DeployType": "", "MemoryUsed": "", "MemoryTotal": "22 Mib", "DriverName": "", "DriverVersion": "", "VbiosVersion": "", "VirtualEnable": true, "VirtualSpecificatio ns": " [{\"templateName\" : \"1g.10gb\",\"vdeic eNum\":2}, {\"templateName\": \"2g.10gb\",\"vdeic eNum\":1}]", "Deleted": false, "CreateTime": "2022-08- 11T07:50:45Z", "UpdateTime": "2022-08- 11T07:50:45Z" } ], "GpuVirtualTemplat e": [ { "ID": "1", "MachineSN": "1111", "Name": "1111", "AiCore": "", "Memory": "", "Deleted": false, "CreateTime": "2024-12- 11T03:23:15Z", "UpdateTime": "2024-12- 11T03:23:15Z" } ] } | The returned data. |
| status | Integer | 200 | The returned status. |

| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status returned. Success: true. Failed: false. |
| responseVersio n | String | v1 | The version number of the API response, used to handle different API versions. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeInstanceGpuVirt &Common request parameters
```

Response example

```json
 "data":{
  "GpuVirtualTemplate":[
    "MachineSN":"1111",
    "AiCore":"",
    "Memory":"",
    "CreateTime":"2024-12-11T03:23:15Z",
    "UpdateTime":"2024-12-11T03:23:15Z",
    "ID":"1",
    "Deleted":false,
    "Name":"1111"
```

`],`

```json
  "MachineGpu":[
    "DeployType":"",
    "MachineId":"0",
    "MachineSN":"1111",
    "VirtualSpecifications":"[{\"templateName\": \"1g.10gb\",\"vdeiceNum\":2},{\"template
Name\": \"2g.10gb\",\"vdeiceNum\":1}]",
    "ModelName":"",
    "InstanceId":"",
    "CreateTime":"2022-08-11T07:50:45Z",
    "DriverName":"",
    "GPUID":"11",
    "VbiosVersion":"",
    "Name":"11",
    "BUSID":"",
    "DriverVersion":"",
    "Manufacturer":"",
    "UpdateTime":"2022-08-11T07:50:45Z",
    "MemoryUsed":"",
    "ID":"1",
    "SN":"1111",
    "Deleted":false,
    "UUID":"",
    "VirtualEnable":true,
    "MemoryTotal":"22 Mib"
```

`]` `},`

```json
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "errorMessage":"failed",
 "errorCode":"UnknownError",
```

```xml
<data>
 <GpuVirtualTemplate>
  <MachineSN>1111</MachineSN>
  <AiCore  />
  <Memory  />
  <CreateTime>2024-12-11T03:23:15Z</CreateTime>
  <UpdateTime>2024-12-11T03:23:15Z</UpdateTime>
  <ID>1</ID>
  <Deleted>false</Deleted>
  <Name>1111</Name>
 </GpuVirtualTemplate>
 <MachineGpu>
  <DeployType  />
  <MachineId>0</MachineId>
  <MachineSN>1111</MachineSN>
  <VirtualSpecifications>[{&quot;templateName&quot;:
&quot;1g.10gb&quot;,&quot;vdeiceNum&quot;:2},{&quot;templateName&quot;: &quot;2g.10gb&quot;,&quot;vdeiceNum&quot;:1}]</VirtualSpecifications>
  <ModelName  />
  <InstanceId  />
  <CreateTime>2022-08-11T07:50:45Z</CreateTime>
  <DriverName  />
  <GPUID>11</GPUID>
  <VbiosVersion  />
  <Name>11</Name>
  <BUSID  />
  <DriverVersion  />
  <Manufacturer  />
  <UpdateTime>2022-08-11T07:50:45Z</UpdateTime>
  <MemoryUsed  />
  <ID>1</ID>
  <SN>1111</SN>
  <Deleted>false</Deleted>
  <UUID  />
  <VirtualEnable>true</VirtualEnable>
  <MemoryTotal>22 Mib</MemoryTotal>
 </MachineGpu>
</data> <errorTitle>InternalError</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <errorMessage>failed</errorMessage> <errorCode>UnknownError</errorCode>
```

### 2.81 CreatInstanceCgpu

Enables GPU kernel virtualization.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|
| InstanceNa me | Strin g | Quer y | No | i-xxxxxxxxx | The name of the instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | UnknownError | The error code. |
| errorTitle | String | InternalError | The title of the error. This provides a summary of why the error occurred. |
| errorMessage | String | xxxx failed | The error message returned when the call fails. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status code. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status that is returned. true: The request was successful. Failed: false |
| responseVersio n | String | v1 | The version number of the API response. This is used to handle different API versions. |

Request example

```
http(s)://[Endpoint]/?Action=CreatInstanceCgpu &Common request parameters
```

Successful response examples

```json
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "errorMessage":"xxxx failed",
 "errorCode":"UnknownError",
<errorTitle>InternalError</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <errorMessage>xxxx failed</errorMessage> <errorCode>UnknownError</errorCode>
```

### 2.82 StopInstanceGpuVirt

Stops GPU virtualization.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceN ame | String | Query | No | i-xxxxxxx | The name of the instance. |
| GpuCardID | String | Query | No | [1,2,3] | The IDs of the GPUs for which you want to clear hardware virtualization settings. The value is a JSON array of integers. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | UnknownError | The error code. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | InternalError | The title of the error. |
| errorMessage | String | failed | The error message returned when the call fails. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use this ID to troubleshoot issues. |
| success | Boolean | true | The status of the response. Success: true Failed: false. |
| responseVersio n | String | v1 | The version number of the API response. This is used to handle different API versions. |

Sample request

```
http(s)://[Endpoint]/?Action=StopInstanceGpuVirt &<Common request parameters>
```

Sample response

```json
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "errorMessage":"failed",
 "errorCode":"UnknownError",
```

```xml
<errorTitle>InternalError</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <errorMessage>failed</errorMessage> <errorCode>UnknownError</errorCode>
```

### 2.83 CreatInstanceVxpu

Enables GPU hardware virtualization.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Paramet er | Type | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceN ame | String | Query | No | i-xxxxxxxx | The name of the instance. |
| CreateVxp uParam | String | Query | No | {"cardId": 1, "type": "allTemplate": {"2g.10gb":2,"1g.10gb": 1}} | The hardware virtualization policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | UnknownError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | failed | The error message returned when the call fails. |
| data | Map | {} | The returned data. |
| status | Integer | 200 | The return status. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

|   |   |   | Bare Metal Computing Platform D |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The status of the response. true: The request was successful. The operation did not fail. |
| responseVersio n | String | v1 | The version number of the API response. This is used to handle different API versions. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateInstanceVxpu &Common request parameters
```

Sample response

```json
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "errorMessage":"failed",
 "errorCode":"UnknownError",
<errorTitle>InternalError</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <errorMessage>failed</errorMessage> <errorCode>UnknownError</errorCode>
```
