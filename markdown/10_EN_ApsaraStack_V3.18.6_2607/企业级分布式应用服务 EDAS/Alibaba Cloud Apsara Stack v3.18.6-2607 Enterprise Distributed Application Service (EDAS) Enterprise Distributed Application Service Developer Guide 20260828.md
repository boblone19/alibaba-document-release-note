---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) Enterprise Distributed Application Service Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 201
source_pdf: "2d6d4da51556a5ab_Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) Enterprise"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%88%86%E5%B8%83%E5%BC%8F%E5%BA%94%E7%94%A8%E6%9C%8D%E5%8A%A1%20EDAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Enterprise%20Distributed%20Application%20Service%20%28EDAS%29%20Enterprise%20Distributed%20Application%20Service%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Enterprise Distributed Application Service (EDAS) Enterprise Distributed Application Service Developer Guide 20260828

## Table of Contents

- 1 API reference
  - 1.1 Instructions for making POP API requests
    - 1.1.1 Obtain the SDK
    - 1.1.2 Obtain the EDAS endpoint
    - 1.1.3 Obtain an AccessKey pair
    - 1.1.4 Common request parameters
    - 1.1.5 Sub-account use instructions
    - 1.1.6 Sample requests
    - 1.1.7 API overview
    - 1.1.8 Resource management
      - 1.1.8.1 General
        - 1.1.8.1.1 DeleteCluster
        - 1.1.8.1.2 ListCluster
        - 1.1.8.1.3 ListResourceGroup
      - 1.1.8.2 ECS clusters
        - 1.1.8.2.1 DeleteClusterMember
        - 1.1.8.2.2 ListClusterMembers
        - 1.1.8.2.3 ListEcsNotInCluster
        - 1.1.8.2.4 ListEcuByRegion
        - 1.1.8.2.5 ListScaleOutEcu
        - 1.1.8.2.6 QueryEccInfo
        - 1.1.8.2.7 SynchronizeResource
    - 1.1.9 Application hosting
      - 1.1.9.1 General
        - 1.1.9.1.1 BindSlb
        - 1.1.9.1.2 ContinuePipeline
        - 1.1.9.1.3 GetChangeOrderInfo
        - 1.1.9.1.4 GetCluster
        - 1.1.9.1.5 GetContainerConfiguration
        - 1.1.9.1.6 GetJvmConfiguration
        - 1.1.9.1.7 ListApplication
        - 1.1.9.1.8 ListBuildPack
        - 1.1.9.1.9 ListHistoryDeployVersion
        - 1.1.9.1.10 ListUserDefineRegion
        - 1.1.9.1.11 ResetApplication
        - 1.1.9.1.12 AbortChangeOrder
        - 1.1.9.1.13 AbortAndRollbackChangeOrder
        - 1.1.9.1.14 QueryApplicationStatus
        - 1.1.9.1.15 GetEffectiveSpringAppConfig
        - 1.1.9.1.16 GetEffectiveSpringAppConfigInText
        - 1.1.9.1.17 ListRecentChangeOrder
        - 1.1.9.1.18 CreateCanaryRule
        - 1.1.9.1.19 ListCanaryRules
        - 1.1.9.1.20 UpdateCanaryRule
        - 1.1.9.1.21 DeleteCanaryRule
      - 1.1.9.2 K8s clusters
        - 1.1.9.2.1 BindK8sSlb
        - 1.1.9.2.2 DeleteK8sApplication
        - 1.1.9.2.3 DeployK8sApplication
        - 1.1.9.2.4 GetK8sApplication
        - 1.1.9.2.5 InsertK8sApplication
        - 1.1.9.2.6 UnbindK8sSlb
        - 1.1.9.2.7 UpdateK8sApplicationConfig
        - 1.1.9.2.8 UpdateK8sSlb
        - 1.1.9.2.9 ScaleK8sApplication
        - 1.1.9.2.10 ImportK8sCluster
        - 1.1.9.2.11 ImportSelfK8sCluster
        - 1.1.9.2.12 StartK8sApplication
        - 1.1.9.2.13 StopK8sApplication
        - 1.1.9.2.14 RestartK8sApplication
      - 1.1.9.3 ECS clusters
        - 1.1.9.3.1 ChangeDeployGroup
        - 1.1.9.3.2 DeleteApplication
        - 1.1.9.3.3 DeployApplication
        - 1.1.9.3.4 DeleteDeployGroup
        - 1.1.9.3.5 GetApplication
        - 1.1.9.3.6 InsertApplication
        - 1.1.9.3.7 ListComponents
        - 1.1.9.3.8 ListDeployGroup
        - 1.1.9.3.9 RollbackApplication
        - 1.1.9.3.10 ScaleInApplication
        - 1.1.9.3.11 ScaleOutApplication
        - 1.1.9.3.12 ScaleoutApplicationWithNewInstances
        - 1.1.9.3.13 StartApplication
        - 1.1.9.3.14 StopApplication
        - 1.1.9.3.15 UnbindSlb
        - 1.1.9.3.16 UpdateApplicationBaseInfo
        - 1.1.9.3.17 UpdateHealthCheckUrl
        - 1.1.9.3.18 UpdateJvmConfiguration
        - 1.1.9.3.19 AddLogPath
        - 1.1.9.3.20 ModifyScalingRule
        - 1.1.9.3.21 RestartApplication
    - 1.1.10 Service administration
      - 1.1.10.1 GetServiceGovernanceConfig
      - 1.1.10.2 UpdateServiceGovernanceConfig
      - 1.1.10.3 UpdateServiceGovernanceConfigInternal
      - 1.1.10.4 ListConsumedServices
      - 1.1.10.5 ListServiceGroups
      - 1.1.10.6 ListPublishedServices
    - 1.1.11 Permission management
      - 1.1.11.1 AuthorizeApplication
      - 1.1.11.2 AuthorizeResourceGroup
      - 1.1.11.3 AuthorizeRole
      - 1.1.11.4 DeleteRole
      - 1.1.11.5 GetSecureToken
      - 1.1.11.6 InsertRole
      - 1.1.11.7 ListRole
    - 1.1.12 Configuration management
      - 1.1.12.1 GetJavaStartUpConfig
      - 1.1.12.2 DeleteConfigCenter
      - 1.1.12.3 InsertConfigCenter
      - 1.1.12.4 ListConfigCenters
      - 1.1.12.5 DeleteDockerConfigSecret
      - 1.1.12.6 ListConfigTemplates
      - 1.1.12.7 GetWebContainerConfig
    - 1.1.13 Auto Scaling
      - 1.1.13.1 CreateApplicationScalingRule
      - 1.1.13.2 DeleteApplicationScalingRule
      - 1.1.13.3 DisableApplicationScalingRule
      - 1.1.13.4 EnableApplicationScalingRule
      - 1.1.13.5 UpdateApplicationScalingRule
      - 1.1.13.6 DescribeApplicationScalingRules
- 2 SDK reference
  - 2.1 Call the Java SDK
    - 2.1.1 Getting Started
    - 2.1.2 User manual
      - 2.1.2.1 Install the Java SDK
      - 2.1.2.2 Configure authentication credentials
      - 2.1.2.3 Initiate a call
      - 2.1.2.4 Handle exceptions
      - 2.1.2.5 Common errors
  - 2.2 Call the EDAS Python SDK
    - 2.2.1 Getting started
    - 2.2.2 User manual
      - 2.2.2.1 Install the SDK for Python
      - 2.2.2.2 Set authentication credentials
      - 2.2.2.3 Initiate a call
      - 2.2.2.4 Set HTTPS requests
      - 2.2.2.5 Handle exceptions
      - 2.2.2.6 Errors and troubleshooting
  - 2.3 Obtain an EDAS SDK
- 3 Obtain an AccessKey pair

## 1 API reference

### 1.1 Instructions for making POP API requests

This topic describes the process of making POP API requests, including instructions on how to obtain the SDK and a description of the initialization parameters. It also provides an example of a specific API request.

#### 1.1.1 Obtain the SDK

You can download the JAR package from the following version list and add the package to your project. Version 2.14.0.private-SNAPSHOT: https://edas.oss-cn-hangzhou.aliyuncs.com/edas-pop-api/2.14.0.private- SNAPSHOT/aliyun-java-sdk-edas-2.14.0.private.jar

#### 1.1.2 Obtain the EDAS endpoint

You can obtain a product endpoint from the Apsara Uni-manager Operations Console.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, choose **Product O&M > Cloud Platform O&M > Apsara Infrastructure Management**.

> **Note:** The preceding menu path is for version 3.16.2. For later versions, the menu path is **Platform O&M > Apsara** **Infrastructure Management**.

3. In the menu bar, choose **O&M > Machine O&M** to open the **Machine O&M** page.

> **Note:** The preceding menu path is for version 3.16.2. For later versions, the menu path is **Resource Management >** **Machine Management**.

4. Select a machine and then click **Terminal** to log on to the machine.
5. Run the command **curl -l "http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?**
**c.sr.service_registration"** to obtain JSON data.
6. Find the edas_api_console_paas_domain key for the EDAS product. The value of this key is the EDAS endpoint.

```bash
curl -l "http://127.0.0.1:7070/api/v3/column/c.sr.service_registration,c.sr.id?c.sr.service_registration"|grep "eda s_api_console_paas_domain"
```

#### 1.1.3 Obtain an AccessKey pair

You can obtain the AccessKey pair on the Apsara Stack console.

**Obtain an AccessKey pair of a department**

Follow these steps:
1. Log on to the Apsara Stack console as an administrator.
2. In the top navigation bar, click the
icon, and then choose **User Center > Department Management**.
3. Select a department and click **Create AccessKey** to obtain an AccessKey pair of this department.

> **Note:** The AccessKey pair is automatically allocated to a level-1 department. The sub-departments use the same AccessKey pair as their level-1 department.

**Obtain an AccessKey pair of a personal account**

Follow these steps:
1. Log on to the Apsara Stack console as an administrator.
2. In the upper-right corner of the Web page, click your avatar and select **Personal Information**.
The system displays your AccessKey ID.
3. Click **Show** under ******************** to view the AccessKey Secret.

#### 1.1.4 Common request parameters

| Parameter | Description |
|---|---|
| regionId | The unique ID of the region where API Gateway is located. For more information, see the list of EDAS-supported regions. |

| accessKeyId/accessKeySecret | The AccessKeyId and AccessKeySecret of the account. This parameter differentiates between primary accounts and sub-accounts. |
|---|---|
| productName | The name of the product for which API requests are made. Set this parameter to EDAS. |
| domain | The domain of the endpoint for making API requests. The rule is as follows: edas-api.console. ${RegionId}. ${Global-Internet-Domain} edas-api.console.RegionId.{ Global-Internet-Domain} |

#### 1.1.5 Sub-account use instructions

Currently, API requests can be made by sub-accounts. In this case, enter the AccessKeyId and AccessKeySecret of each subaccount. In addition, sub-accounts must be authorized by primary accounts to use the corresponding resources.

#### 1.1.6 Sample requests

To make API requests, start the API client, configure an endpoint, and set common parameters, such as regionId and AccessKeyId. The following is a sample API request.

```
    public static void main(String[] args) throws ClientException{
        /**
         * The endpoint used to make the API request. Set this parameter based on the list of EDAS-supported regions
and the region where your instance is located.
```

`*/`

```
        String regionId = "XXXXX";
        /**
         * The AccessKeyId that is created in the Alibaba Cloud console for authentication.
```

`*/`

```
        String accessKeyId = "XXXXXXXXXXXXXXXXX";
        /**
         * The AccessKeySecret that is created in the Alibaba Cloud console for authentication.
```

`*/`

```
        String accessKeySecret = "XXXXXXXXXXXXXXXXX";
        /**
        * The name of the cloud product that you access through the API request. Set it to EDAS in this example.
```

`*/`

```
        String productName ="Edas";
        /**
         * The domain of the endpoint. For more information, see the domains in the list of EDAS-supported regions.
```

`*/`

```java
        String domain ="edas-api.console.XXXXX.aliyun.com";
        // Construct an API client.
        DefaultProfile.addEndpoint(regionId,regionId,productName,domain);
        DefaultProfile defaultProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessKeySecret);
        DefaultAcsClient defaultAcsClient = new DefaultAcsClient(defaultProfile);
        defaultAcsClient.setAutoRetry(false);
        // Construct the API request for listing application deployment groups. For more information about the input
parameters, see the operation descriptions.
        String appId = "xxxxxxxxx";
        ListDeployGroupRequest request = new ListDeployGroupRequest();
        // For more information about the input parameters, see the operation descriptions.
        request.setAppId(appId);
        ListDeployGroupResponse response = defaultAcsClient.getAcsResponse(request);
        // Result parsing (If Code 200 is returned, the call is successful. If any other code is returned, the call f
ails. For more information, see the error code list.)
        if (response.getCode() == 200) {
            // Parse the returned result (for more information, see the return value description of the corresponding
operation).
            List<DeployGroup> deployGroups = response.getDeployGroupList();
            if (CollectionUtils.isNotEmpty(deployGroups)) {
                for (DeployGroup deployGroup : deployGroups) {
                    System.out.println(deployGroup.getGroupName());
                    System.out.println(deployGroup.getGroupId());
        } else {
            // Print the cause of the error.
            System.out.println(response.getMessage());
```

#### 1.1.7 API overview

EDAS provides the following APIs:

| API | Description |
|---|---|
| ListApplicationRequest | Gets the list of applications. |
| InsertApplicationRequest | Creates an application. |
| ScaleOutApplicationRequest | Scales out an application instance. |
| DeployApplicationRequest | Deploys an application. |
| GetChangeOrderInfoRequest | Gets the details of a change order. |
| ListApplicationEcu | Gets the list of deployable ECUs. |

| GetApplicationRequest | Gets application information. |
|---|---|
| StartApplicationRequest | Starts an application. |
| StopApplicationRequest | Stops an application. |
| DeleteApplicationRequest | Deletes an application instance. |
| ListScaleOutEcuRequest | Gets the list of available instances for creating or scaling out an application. |
| QueryApplicationStatusRequest | Queries the status of an application. |
| ScaleInApplicationRequest | Unpublishes the application instance. |

#### 1.1.8 Resource management

##### 1.1.8.1 General

###### 1.1.8.1.1 DeleteCluster

You can call the DeleteCluster operation to delete an ECS cluster or unimport a Container Service for Kubernetes (K8s) cluster from EDAS.

**Request header**

This operation uses common request headers. No special request headers are required. For more information about common request headers, see Common request parameters.

```
DELETE /pop/v5/resource/cluster HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | Yes | 8b96ade0-0a07-****- af9d-5ed83640d076 | The ID of the cluster. Call the ListCluster operation to get the list of clusters and their IDs in a specific namespace. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| Data | Boolean | true | The result of the operation. |
| Message | String | success | Additional message. |

Request example

```json
DELETE /pop/v5/resource/cluster HTTP/1.1
  "ClusterId": "8b96ade0-0a07-****af9d-5ed83640d076"
```

Successful response example

```json
<Data>true</Data>
 "Data": true,
 "Message": "success",
 "Code": 200
```

###### 1.1.8.1.2 ListCluster

Queries a list of clusters in Enterprise Distributed Application Service (EDAS).

**Request header**

This operation uses common request headers. No special headers are required. For more information, see Common request parameters.

```
POST /pop/v5/resource/cluster_list HTTP/1.1
```

**Return data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| ClusterList | Array | - | A list of clusters. |
| -ClusterId | String | 0d247b93-8d62-4e34-****- ************ | The cluster ID. |
| -RegionId | String | cn-wulan-env205-d01:t1 | The ID of the microservices namespace. |
| -Description | String | test | The description of the cluster. |
| -ClusterName | String | my-cluster | The name of the cluster. |
| -ClusterType | Integer | 5 | Cluster type: 2: ECS cluster 5: Kubernetes cluster |
| -OversoldFactor | Integer | 1 | CPU oversold ratio (Docker cluster): 1: 1:1 ratio (no overselling) 2:1:2 oversubscription ratio. 4. A 1:4 oversubscription ratio. 8: 1:8 ratio |
| -NetworkMode | Integer | 1 | Network type: 1: Classic network 2: VPC |
| -VpcId | String | vpc-wz9b246z****** | The VPC ID. |
| -NodeNum | Integer | 4 | The number of node instances. |
| -Cpu | Integer | 4 | The total number of CPU cores. |

| Enterprise Distrib Service (EDAS) | uted Application |   | Enterprise Distributed Application Service Developer Guide·API refe rence |
|---|---|---|---|

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| -Mem | Integer | 4096 | The total memory size in MB. |
| -CpuUsed | Integer | 2 | The number of used CPU cores. |
| -MemUsed | Integer | 1024 | The used memory size in MB. |
| -CreateTime | Long | 1743960129507 | The UNIX timestamp that indicates when the cluster was created. |
| -UpdateTime | Long | 1743960588706 | The UNIX timestamp that indicates when the cluster was last modified. |
| -ClusterStatus | Integer | 1 | Cluster status: 1: Normal 2: Abnormal 3: Offline |
| -csClusterId | String | c71235a66231843ae979e 188390****** | The ID of the Container Service cluster. |
| -csClusterStatus | String | running | Container Cluster Status: running: The cluster is running. updating: The cluster is being updated. scaling: The cluster is being scaled up. upgrading: The cluster is being upgraded. |
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The request ID. |
| Code | Integer | 200 | The HTTP status code or POP error code. |
| Message | String | success | Additional information |

Request example

```
POST /pop/v5/resource/cluster_list HTTP/1.1
```

Successful response example

```json
 "ClusterList":[
   "Description":"test",
   "OversoldFactor":1,
   "NodeNum":4,
   "ClusterId":"0d247b93-8d62-4e34-****-************",
   "CreateTime":1743960129507,
   "Cpu":4,
   "ClusterType":5,
   "NetworkMode":1,
   "csClusterStatus":"running",
   "MemUsed":1024,
   "VpcId":"vpc-wz9b246z******",
   "Mem":4096,
   "UpdateTime":1743960588706,
   "ClusterName":"my-cluster",
   "csClusterId":"c71235a66231843ae979e188390******",
   "RegionId":"cn-wulan-env205-d01:t1",
   "CpuUsed":2,
   "ClusterStatus":1
```

`],`

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"success",
 "Code":200
<ClusterList>
 <Description>test</Description>
 <OversoldFactor>1</OversoldFactor>
 <NodeNum>4</NodeNum>
 <ClusterId>0d247b93-8d62-4e34-****-************</ClusterId>
 <CreateTime>1743960129507</CreateTime>
 <Cpu>4</Cpu>
 <ClusterType>5</ClusterType>
 <NetworkMode>1</NetworkMode>
 <csClusterStatus>running</csClusterStatus>
 <MemUsed>1024</MemUsed>
 <VpcId>vpc-wz9b246z******</VpcId>
 <Mem>4096</Mem>
 <UpdateTime>1743960588706</UpdateTime>
 <ClusterName>my-cluster</ClusterName>
 <csClusterId>c71235a66231843ae979e188390******</csClusterId>
 <RegionId>cn-wulan-env205-d01:t1</RegionId>
 <CpuUsed>2</CpuUsed>
 <ClusterStatus>1</ClusterStatus>
</ClusterList> <RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId>
```

###### 1.1.8.1.3 ListResourceGroup

The ListResourceGroup operation queries a list of resource groups.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the documentation about common parameters.

```
POST /pop/v5/resource/reg_group_list HTTP/1.1
```

This operation has no request parameters.

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The message that is returned. |
| ResourceGroupList | Array of ResGroupEntity |   | The list of resource groups. |
| ResGroupEntity |   |   |   |
| AdminUserId | String | ****@aliyun.com | The UID of the user. |
| CreateTime | Long | 1557890594376 | The UNIX timestamp for the creation time. |
| Description | String | QqLZDA3pBZ | The description of the resource group. |
| Id | Long | 8592 | The ID of the resource group. |
| Name | String | TIa2LGixyD | The name of the resource group. |
| RegionId | String | cn-qingdao | The ID of the region. |
| SlbList | Array of SlbEntity |   | The list of Server Load Balancer (SLB) instances. |
| SlbEntity |   |   |   |
| Address | String | 192.168.xxx.xx | The IP address. |
| AddressType | String | Intranet | The type of the address. Internet: an Internet address Intranet: a private address |
| Expired | Boolean | true | Alive |
| GroupId | Integer | 641897243 | The group ID. |
| NetworkType | String | vpc | The network type. classic network VPC |
| RegionId | String | cn-beijing | The region ID. |
| SlbId | String | lb-2zebf1fpbpkc7dnro**** | The unique ID of the SLB instance. |
| SlbName | String | a9315af59b4cd11e9a18c0 0163e1**** | The name of the SLB instance. |
| SlbStatus | String | active | The status of the SLB instance. |
| UserId | String | ****@aliyun.com | The UID of the user. |
| VpcId | String | vpc- m5e666n89m2bx8jar**** | The ID of the VPC. |

| VswitchId | String | vsw- mxxxxkxxxx4xxxxwbionj | The ID of the vSwitch. |
|---|---|---|---|
| UpdateTime | Long | 1573281040827 | The UNIX timestamp for the update time. |
| ecsList | Array of EcsEntity |   | The list of Elastic Compute Service (ECS) instances. |
| EcsEntity |   |   |   |
| Cpu | Integer | 2 | The total number of CPU cores. |
| Description | String | test | The description. |
| EcuEntity | Struct |   | The ECU entity. |
| AvailableCpu | Integer | 1 | The number of available CPU cores. |
| AvailableMem | Integer | 200 | The available memory. |
| Cpu | Integer | 2 | The total number of CPU cores. |
| CreateTime | Long | 1557890594376 | The UNIX timestamp for the creation time. |
| DockerEnv | Boolean | true | Indicates whether Docker is installed. true: Docker is installed. false: Docker is not installed. |
| EcuId | String | 0de2ebdb-9490-4fc4- be41*************** | The unique ID of the ECU. To obtain this ID, run the dmidecode command on the ECS instance. |
| HeartbeatTime | Long | 1573281040819 | The UNIX timestamp of the last heartbeat detection. |
| InstanceId | String | i-2zej4i2jdf********* | The instance ID. |
| IpAddr | String | 192.168.xxx.xx | The internal IP address of the ECU. |
| Mem | Integer | 200 | The total amount of memory, in MB. |
| Name | String | test | The name of the ECU. |
| Online | Boolean | true | Indicates whether the ECU is online. true: The ECU is online. false: The ECU is offline. |
| RegionId | String | cn-beijing | The region ID. |
| UpdateTime | Long | 1573281040827 | The UNIX timestamp for the update time. |
| UserId | String | edas **** test@aliyun- _ _ ****.com | The ID of the associated user. |
| VpcId | String | vpc- 2ze1ram356umxs598**** | The ID of the VPC. |
| ZoneId | String | cn-beijing-b | The ID of the zone. |

| Eip | String | 130.30.xx.xxx | The Elastic IP Address (EIP). |
|---|---|---|---|
| Expired | Boolean | true | Indicates whether the instance has expired. true: The instance has expired. false: The instance has not expired. |
| GroupId | String | 0 | The ID of the EDAS resource group. |
| HostName | String | iZm5e853hvvrodnvqus**** | The hostname. |
| InnerIp | String | 192.168.xx.xxx | The internal IP address. |
| InstanceId | String | i-m5e853hvvrodnvqu**** | The instance ID. |
| InstanceId | String | i-m5e853hvvrodnvqu**** | The instance ID. |
| InstanceName | String | betabjmixcoud 01 _ | The instance name. |
| Mem | Integer | 1 | The total amount of memory, in MB. |
| PrivateIp | String | 192.168.xx.xxx | The private IP address. |
| PublicIp | String | 130.30.xx.xxx | The public IP address. |
| RegionId | String | ch-hangzhou | The region ID. |
| SerialNum | String | 98b480b8-458b-4ff3-84b9- cf7097c5**** | The serial number. |
| SgId | String | sg-m5eajgzn6b8sg9mv**** | The ID of the security group. |
| Status | String | Running | The status of the instance. Pending: The instance is being created. Running: The instance is running. Starting: The instance is starting. Stopping: The instance is stopping. Stopped: The instance is stopped. |
| UserId | String | **** common ****@aliyun. _ _ com | The user account. |
| VpcEntity | Struct |   | The VPC-connected instance. |
| Cidrblock | String | 130.30 | The IPv4 CIDR block of the vSwitch. |
| Description | String | "" | The description. |
| EcsNum | Integer | 1 | The number of instances. |
| Expired | Boolean | true | Liveness |
| RegionId | String | cn-qingdao | The region where the instance is located. |
| Status | String | Running | The instance status. |

| ence |   |   | Service (EDAS |
|---|---|---|---|

| UserId | String | **** common ****@aliyun. _ _ com | The user ID. |
|---|---|---|---|
| VpcId | String | vpc- bp13evu4aayj2t1er**** | The unique ID of the VPC. |
| VpcName | String | test | The name of the VPC. |
| VpcId | String | vpc- bp13evu4aayj2t1er**** | The unique ID of the VPC. |
| ZoneId | String | cn-qingdao-h | The ID of the zone. |

Sample request

```
POST /pop/v5/resource/reg_group_list HTTP/1.1
```

Sample response

```xml
<RequestId>b197-40ab-9155-7ca7</RequestId> <ResourceGroupList>
    <ResGroupEntity>
        <Description>QqLZDA3pBZ</Description>
        <CreateTime>1557890594376</CreateTime>
        <UpdateTime>1573281040827</UpdateTime>
        <AdminUserId>117274586608****</AdminUserId>
        <RegionId>cn-qingdao</RegionId>
        <Id>8592</Id>
        <ecsList>
            <EcsEntity>
                <Status>Running</Status>
                <VpcEntity>
                    <Status>Running</Status>
                    <Description>""</Description>
                    <VpcId>vpc-bp13evu4aayj2t1er****</VpcId>
                    <UserId>****_common_****@aliyun.com</UserId>
                    <EcsNum>1</EcsNum>
                    <Expired>true</Expired>
                    <Cidrblock>130.3</Cidrblock>
                    <VpcName>test</VpcName>
                    <RegionId>cn-qingdao</RegionId>
                </VpcEntity>
                <Description>""</Description>
                <ZoneId>cn-qingdao-h</ZoneId>
                <InnerIp>192.168.xx.xxx</InnerIp>
                <PublicIp>130.30.xx.xxx</PublicIp>
                <InstanceId>i-m5e853hvvrodnvqu****</InstanceId>
                <SgId>sg-m5eajgzn6b8sg9mv****</SgId>
                <Cpu>2</Cpu>
                <Expired>true</Expired>
                <Eip>130.30.xx.xxx</Eip>
                <GroupId>0</GroupId>
                <InstanceName>betabjmixcoud_01</InstanceName>
                <SerialNum>98b480b8-458b-4ff3-84b9-cf7097c5****</SerialNum>
                <Mem>1</Mem>
                <VpcId>vpc-bp13evu4aayj2t1er****</VpcId>
                <PrivateIp>192.168.xx.xxx</PrivateIp>
                <UserId>****_common_****@aliyun.com</UserId>
                <EcuEntity>
                    <IpAddr>192.168.xxx.xx</IpAddr>
                    <ZoneId>cn-beijing-b</ZoneId>
                    <InstanceId>i-2zej4i2jdf*********</InstanceId>
```

```json
                    <CreateTime>1557890594376</CreateTime>
                    <Cpu>2</Cpu>
                    <EcuId>0de2ebdb-9490-4fc4-be41***************</EcuId>
                    <AvailableMem>200</AvailableMem>
                    <HeartbeatTime>1573281040819</HeartbeatTime>
                    <Name>test</Name>
                    <Mem>200</Mem>
                    <VpcId>vpc-2ze1ram356umxs598****</VpcId>
                    <UserId>edas_****_test@aliyun-****.com</UserId>
                    <UpdateTime>1573281040827</UpdateTime>
                    <RegionId>cn-beijing</RegionId>
                    <Online>true</Online>
                    <AvailableCpu>1</AvailableCpu>
                    <DockerEnv>true</DockerEnv>
                </EcuEntity>
                <RegionId>ch-hangzhou</RegionId>
                <HostName>iZm5e853hvvrodnvqus****</HostName>
            </EcsEntity>
        </ecsList>
        <SlbList>
            <SlbEntity>
                <SlbId>lb-2zebf1fpbpkc7dnro****</SlbId>
                <VpcId>641897243</VpcId>
                <Address>192.168.xxx.xx</Address>
                <NetworkType>vpc</NetworkType>
                <UserId>641897243</UserId>
                <Expired>true</Expired>
                <RegionId>cn-beijing</RegionId>
                <AddressType>Intranet</AddressType>
                <VswitchId>641897243</VswitchId>
                <SlbName>a9315af59b4cd11e9a18c00163e1****</SlbName>
                <GroupId>641897243</GroupId>
                <SlbStatus>active</SlbStatus>
            </SlbEntity>
        </SlbList>
        <Name>TIa2LGixyD</Name>
    </ResGroupEntity>
</ResourceGroupList>
    "RequestId": "b197-40ab-9155-7ca7",
    "Message": "success",
    "ResourceGroupList": {
        "ResGroupEntity": {
            "Description": "QqLZDA3pBZ",
            "CreateTime": 1557890594376,
            "UpdateTime": 1573281040827,
            "AdminUserId": "117274586608****",
            "RegionId": "cn-qingdao",
            "Id": 8592,
            "ecsList": {
                "EcsEntity": {
                    "Status": "Running",
                    "VpcEntity": {
                        "Status": "Running",
                        "Description": "\"\"",
                        "VpcId": "vpc-bp13evu4aayj2t1er****",
                        "UserId": "****_common_****@aliyun.com",
                        "EcsNum": 1,
                        "Expired": true,
                        "Cidrblock": 130.3,
                        "VpcName": "test",
                        "RegionId": "cn-qingdao"
```

`},`

```json
                    "Description": "\"\"",
                    "ZoneId": "cn-qingdao-h",
                    "InnerIp": "192.168.xx.xxx",
                    "PublicIp": "130.30.xx.xxx",
```

```json
                    "InstanceId": "i-m5e853hvvrodnvqu****",
                    "SgId": "sg-m5eajgzn6b8sg9mv****",
                    "Cpu": 2,
                    "Expired": true,
                    "Eip": "130.30.xx.xxx",
                    "GroupId": 0,
                    "InstanceName": "betabjmixcoud_01",
                    "SerialNum": "98b480b8-458b-4ff3-84b9-cf7097c5****",
                    "Mem": 1,
                    "VpcId": "vpc-bp13evu4aayj2t1er****",
                    "PrivateIp": "192.168.xx.xxx",
                    "UserId": "****_common_****@aliyun.com",
                    "EcuEntity": {
                        "IpAddr": "192.168.xxx.xx",
                        "ZoneId": "cn-beijing-b",
                        "InstanceId": "i-2zej4i2jdf*********",
                        "CreateTime": 1557890594376,
                        "Cpu": 2,
                        "EcuId": "0de2ebdb-9490-4fc4-be41***************",
                        "AvailableMem": 200,
                        "HeartbeatTime": 1573281040819,
                        "Name": "test",
                        "Mem": 200,
                        "VpcId": "vpc-2ze1ram356umxs598****",
                        "UserId": "edas_****_test@aliyun-****.com",
                        "UpdateTime": 1573281040827,
                        "RegionId": "cn-beijing",
                        "Online": true,
                        "AvailableCpu": 1,
                        "DockerEnv": true
```

`},`

```json
                    "RegionId": "ch-hangzhou",
                    "HostName": "iZm5e853hvvrodnvqus****"
```

`},`

```json
            "SlbList": {
                "SlbEntity": {
                    "SlbId": "lb-2zebf1fpbpkc7dnro****",
                    "VpcId": 641897243,
                    "Address": "192.168.xxx.xx",
                    "NetworkType": "vpc",
                    "UserId": 641897243,
                    "Expired": true,
                    "RegionId": "cn-beijing",
                    "AddressType": "Intranet",
                    "VswitchId": 641897243,
                    "SlbName": "a9315af59b4cd11e9a18c00163e1****",
                    "GroupId": 641897243,
                    "SlbStatus": "active"
```

`},`

```json
            "Name": "TIa2LGixyD"
```

`},`

```json
    "Code": 200
```

##### 1.1.8.2 ECS clusters

###### 1.1.8.2.1 DeleteClusterMember

Removes an instance from an ECS cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /pop/v5/resource/cluster_member HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | Yes | 52984524-****-****- 85f2-a34b0e5bb521 | The ID of the cluster. Call the ListCluster operation to obtain the list of clusters and their IDs. |
| ClusterMemberId | String | Query | Yes | i-2zej4i2jdf3****jigng | The ID of the ECS instance in the cluster. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| Data | Boolean | true | Indicates whether the operation was successful. |
| Message | String | success | Additional information. |

Sample request

```json
DELETE /pop/v5/resource/cluster_member HTTP/1.1 "ClusterId": "52984524-****-****-85f2-a34b0e5bb521", "ClusterMemberId": "i-2zej4i2jdf3****jigng"
```

Sample success response

```json
<Data>ok</Data>
 "Data": "ok",
 "Code": "200",
 "Message": "success"
```

###### 1.1.8.2.2 ListClusterMembers

You can call ListClusterMembers to retrieve a list of ECS instances.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
GET /pop/v5/resource/cluster_member_list HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterId | String | Query | Yes | 52984524-6d48- 4bbd-85f2- a34b0e5b**** | The ID of the cluster. Call ListCluster to get this ID. |
|---|---|---|---|---|---|
| CurrentPage | Integer | Query | No | 1 | The page number to return. If you do not set this parameter, the first page is returned by default. |
| PageSize | Integer | Query | No | 50 | The number of entries to return on each page. If you do not set this parameter, all ECS instances in the cluster are returned. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ClusterMemberPage | Struct |   | The page of ECS instances in the cluster. |
| ClusterMemberList | Array of ClusterMember |   | The list of instances in the cluster. |
| ClusterMember |   |   |   |
| ClusterId | String | 52984524-6d48-4bbd- 85f2-a34b0e5b**** | The ID of the cluster. |
| ClusterMemberId | String | adb03eeb-3adf-4d7e-afe1- 03d1ad45**** | The ID of the cluster member. |
| CreateTime | Integer | 2046224532 | The UNIX timestamp when the member was created. |
| EcsId | String | i-2zej4i2jdf3ntwhj**** | The ID of the ECS instance. |
| EcuId | String | 70ed3f59-b476-49aa- be09-9e6c375d**** | The unique ID of the ECU. Run dmidecode on the ECS instance to get this ID. |
| Status | Integer | 1 | The status of the instance. 1: running 0: converting -1: conversion failed -2: offline |
| UpdateTime | Integer | 2046224532 | The UNIX timestamp when the member was last updated. |
| CurrentPage | Integer | 1 | The page number for a paged query. The default value is 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| TotalSize | Integer | 5 | The total number of entries. |
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |

Request example

```json
GET /pop/v5/resource/cluster_member_list HTTP/1.1 "ClusterId": "52984524-6d48-4bbd-85f2-a34b0e5b****"
```

Successful response example

```json
<ClusterMemberPage>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <TotalSize>5</TotalSize>
    <ClusterMemberList>
        <Status>1</Status>
        <ClusterId>52984524-6d48-4bbd-85f2-a34b0e5b****</ClusterId>
        <CreateTime>1502888064561</CreateTime>
        <UpdateTime>1502888064561</UpdateTime>
        <EcuId>70ed3f59-b476-49aa-be09-9e6c375d****</EcuId>
        <ClusterMemberId>adb03eeb-3adf-4d7e-afe1-03d1ad45****</ClusterMemberId>
        <EcsId>i-2zej4i2jdf3ntwhj****</EcsId>
    </ClusterMemberList>
</ClusterMemberPage>
    "Message": "success",
    "ClusterMemberPage": {
        "PageSize": 10,
        "CurrentPage": 1,
        "TotalSize": 5,
        "ClusterMemberList": {
            "Status": 1,
            "ClusterId": "52984524-6d48-4bbd-85f2-a34b0e5b****",
            "CreateTime": 1502888064561,
            "UpdateTime": 1502888064561,
            "EcuId": "70ed3f59-b476-49aa-be09-9e6c375d****",
            "ClusterMemberId": "adb03eeb-3adf-4d7e-afe1-03d1ad45****",
            "EcsId": "i-2zej4i2jdf3ntwhj****"
```

`},`

```json
    "Code": 200
```

###### 1.1.8.2.3 ListEcsNotInCluster

The ListEcsNotInCluster operation retrieves all Elastic Compute Service (ECS) instances that have not been imported into a cluster.

**Request headers**

This operation uses common request headers and does not require any special request headers. For more information, see Common parameters.

```
GET /pop/v5/resource/ecs_not_in_cluster HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|

| NetworkMode | Integer | Query | Yes | 2 | The network type. 1: Classic network 2: Virtual private cloud (VPC) |
|---|---|---|---|---|---|
| VpcId | String | Query | No | vpc- 2zef6ob8****v8x3q4 6kp | The ID of the VPC. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| EcsEntityList | Array of EcsEntity |   | The list of ECS instances. |
| EcsEntity |   |   |   |
| Cpu | Integer | 2 | The number of CPU cores for the ECS instance. |
| Eip | String | 139.30.xxx.xx | The Elastic IP Address (EIP) of the ECS instance. |
| Expired | Boolean | false | Indicates whether the ECS instance has expired. |
| InnerIp | String | 192.168.20.113 | The private IP address of the ECS instance. |
| InstanceId | String | i-2ze7s2v0b*********** | The ID of the ECS instance. |
| InstanceName | String | worker-k8s-for-cs- c9dfa009a5e7c4faab2010 b87cae4**** | The name of the ECS instance. |
| Mem | Integer | 4096 | The memory size of the ECS instance. |
| PrivateIp | String | 192.168.*.** | The private IP address of the ECS instance. |
| PublicIp | String | 131.30.xxx.xx | The public IP address of the ECS instance. |
| RegionId | String | cn-beijing | The ID of the region where the ECS instance resides. |
| Status | String | Running | The instance status. Pending: The instance is being created. Running: The instance is running. Starting: The instance is starting. Stopping: The instance is stopping. Stopped: The instance is stopped. |
| VpcId | String | vpc- 2zef6ob8mrlzv8x3q**** | The ID of the VPC. |
| VpcName | String | test | The name of the VPC. |
| Message | String | success | The response message. |
| RequestId | String | b197-40ab-9155-**** | The request ID. |

Request example

```json
GET /pop/v5/resource/ecs_not_in_cluster HTTP/1.1 "NetworkMode": "2"
```

Response example

```json
<RequestId>b197-40ab-9155-****</RequestId> <EcsEntityList>
    <Status> Running</Status>
    <InstanceName>worker-k8s-for-cs-c9dfa009a5e7c4faab2010b87cae4****</InstanceName>
    <InnerIp>192.168.20.113</InnerIp>
    <Mem>4096</Mem>
    <VpcId>vpc-2zef6ob8mrlzv8x3q****</VpcId>
    <PrivateIp>192.168.*.**</PrivateIp>
    <PublicIp>131.30.xxx.xx</PublicIp>
    <InstanceId>i-2ze7s2v0b***********</InstanceId>
    <Cpu>2</Cpu>
    <Expired>false</Expired>
    <VpcName>test</VpcName>
    <RegionId>cn-beijing</RegionId>
    <Eip>139.30.xxx.xx</Eip>
</EcsEntityList>
    "RequestId": "b197-40ab-9155-****",
    "Message": "success",
    "Code": 200,
    "EcsEntityList": {
        "Status": "Running",
        "InstanceName": "worker-k8s-for-cs-c9dfa009a5e7c4faab2010b87cae4****",
        "InnerIp": "192.168.20.113",
        "Mem": 4096,
        "VpcId": "vpc-2zef6ob8mrlzv8x3q****",
        "PrivateIp": "192.168.*.**",
        "PublicIp": "131.30.xxx.xx",
        "InstanceId": "i-2ze7s2v0b***********",
        "Cpu": 2,
        "Expired": false,
        "VpcName": "test",
        "RegionId": "cn-beijing",
        "Eip": "139.30.xxx.xx"
```

###### 1.1.8.2.4 ListEcuByRegion

Call ListEcuByRegion to retrieve a list of available ECUs in a specified namespace.

**Terms**

**Namespace**: A namespace is a logical concept in Enterprise Distributed Application Service (EDAS) that isolates resources
and published microservices. Resources include clusters, Elastic Compute Service (ECS) instances, and applications. Each region has one default namespace and can have multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if resource and microservice isolation is not required.
**ECU**: An ECS instance becomes an ECU after it is imported into a cluster.
**ECC**: An ECU in a cluster becomes an ECC after it is deployed in an application.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/resource/ecu_list HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
| Act | String | Query | Yes | pop-query | A static field with the value pop-query . |   |   |
| LogicalRegionId | String | Query | No | cn-beijing or cn- | The ID of the namespace. The ID of a custom namespace is in the format of <Region ID>:<Namespace |   |   |
|   |   |   |   |   |   | <Region ID>:<Namespace |   |
|   |   |   |   | beijing:tdy218 | identifier> |   |   |
| EcuIds | String | Query | No | c96c494c-1b91- 4456-bbb3- b5afcd16**** | The ECU ID. Separate multiple ECU IDs with semicolons (;). |   |   |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| EcuEntityList | Array of EcuEntity |   | The list of ECUs. |
| EcuEntity |   |   |   |
| AvailableCpu | Integer | 4 | The number of available CPU cores of the ECU. |
| AvailableMem | Integer | 8192 | The available memory of the ECU. Unit: MB. |
| Cpu | Integer | 0 | The total number of CPU cores. |
| CreateTime | Long | 1572539283168 | The timestamp when the entry was created. |
| DockerEnv | Boolean | true | Indicates whether Docker is installed. true: Docker is installed. false: Docker is not installed. |
| EcuId | String | c96c494c-1b91-4456- bbb3-b5afcd16**** | The unique ID of this ECU. Run the dmidecode command on the ECS instance to get this ID. |
| HeartbeatTime | Long | 1572867865221 | The timestamp of the last heartbeat detection. |
| InstanceId | String | i-2ze82h8f4zcn449y**** | The ID of the ECU. |
| IpAddr | String | 192.168.0.115 | The private IP address of the ECU. |
| Mem | Integer | 500 | The total memory size. Unit: MB. |
| Name | String | worker-k8s-for | The name of the ECU. |

| Online | Boolean | false | Indicates whether the ECU is online. true: The ECU is online. false: The ECU is offline. |
|---|---|---|---|
| RegionId | String | cn-beijing | The ID of the region where the ECU resides. |
| UpdateTime | Long | 1572867895575 | The timestamp of the last change. |
| UserId | String | edas@aliyun-****.com | The ID of the account. |
| VpcId | String | vpc-2zew8mi6gqbo5wf**** | The ID of the VPC where the ECU resides. |
| ZoneId | String | cn-beijing-a | The ID of the zone where the ECU resides. |
| Message | String | success | The returned message. |

Request example

```json
GET /pop/v5/resource/ecu_list HTTP/1.1 "Act": "pop-query"
```

Response example

```xml
<EcuEntityList>
    <IpAddr>192.168.0.115</IpAddr>
    <ZoneId>cn-beijing-a</ZoneId>
    <InstanceId>i-2ze82h8f4zcn449y****</InstanceId>
    <CreateTime>1572539283168</CreateTime>
    <Cpu>0</Cpu>
    <EcuId>c96c494c-1b91-4456-bbb3-b5afcd16****</EcuId>
    <AvailableMem>8192</AvailableMem>
    <HeartbeatTime>1572867865221</HeartbeatTime>
    <Name>worker-k8s-for</Name>
    <Mem>500</Mem>
    <VpcId>vpc-2zew8mi6gqbo5wf****</VpcId>
    <UserId>edas@aliyun-****.com</UserId>
    <UpdateTime>1572867895575</UpdateTime>
    <RegionId>cn-beijing</RegionId>
    <Online>false</Online>
    <AvailableCpu>4</AvailableCpu>
    <DockerEnv>true</DockerEnv>
</EcuEntityList>
```

```json
    "Message": "success",
    "EcuEntityList": {
        "IpAddr": "192.168.0.115",
        "ZoneId": "cn-beijing-a",
        "InstanceId": "i-2ze82h8f4zcn449y****",
        "CreateTime": 1572539283168,
        "Cpu": 0,
        "EcuId": "c96c494c-1b91-4456-bbb3-b5afcd16****",
        "AvailableMem": 8192,
        "HeartbeatTime": 1572867865221,
        "Name": "worker-k8s-for",
        "Mem": 500,
        "VpcId": "vpc-2zew8mi6gqbo5wf****",
        "UserId": "edas@aliyun-****.com",
        "UpdateTime": 1572867895575,
        "RegionId": "cn-beijing",
        "Online": false,
        "AvailableCpu": 4,
        "DockerEnv": true
```

`},`

```json
    "Code": 200
```

###### 1.1.8.2.5 ListScaleOutEcu

Call the ListScaleOutEcu operation to retrieve a list of ECUs that are available for application scale-out from a specified cluster or from the cluster associated with an application. This operation applies only to ECS clusters.

**Terms**

**Namespace**: A logical concept in EDAS for isolating resources and microservices, such as clusters, ECS instances, and
applications. A namespace can be a default namespace or a custom namespace. Each region has one default namespace and can have multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not need to isolate resources and microservices.
**ECU**: An ECS instance becomes an ECU after it is imported into a cluster.
**ECC**: An ECU becomes an ECC after an application is deployed on it within a cluster.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

```
POST /pop/v5/resource/scale_out_ecu_list HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | No | 52984524-6d48- 4bbd- ****************** | The ID of the cluster. Use this parameter to query for available ECUs within a specific cluster. Note You must specify either the ClusterId or AppId parameter. |
| AppId | String | Query | No | b93024fd-8a9d-4ef7- 99f1-5f0d65cc**** | The ID of the application. Use this parameter to query for available ECUs in the cluster where the specified application is deployed. Note You must specify either the ClusterId or AppId parameter. |
| GroupId | String | Query | No | 8123db90-880f- 486f-****-**** | Queries the available ECUs in the application group's cluster. |

| Cpu | Integer | Query | No | 1 | The required number of CPU cores. The operation returns ECUs that meet this requirement. |
|---|---|---|---|---|---|
| Mem | Integer | Query | No | 200 | The required amount of available memory. The operation returns ECUs that meet this requirement. Unit: MB. |
| InstanceNum | Integer | Query | No | 1 | The number of ECUs to return. If you do not set this parameter, all ECUs that meet the filter criteria are returned. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| EcuInfoList | Array of EcuInfo |   | The list of ECUs. |
| EcuInfo |   |   |   |
| AvailableCpu | Integer | 2 | The number of available CPU cores in the ECU. |
| AvailableMem | Integer | 111 | The amount of available memory in the ECU. Unit: MB. |
| CreateTime | Long | 1573281040819 | The timestamp of the creation time. |
| DockerEnv | Boolean | false | Indicates whether Docker is installed. true: Docker is installed. false: Docker is not installed. |
| EcuId | String | 0de2ebdb-9490-4fc4- be41*************** | The unique ID of the ECU. To obtain this ID, run the dmidecode command on the ECS instance. |
| HeartbeatTime | Long | 1573281040819 | The timestamp of the last heartbeat detection. |
| InstanceId | String | i-2zej4i2jdf********* | The ID of the ECU instance. |
| IpAddr | String | 192.168.XX.XX | The private IP address of the ECU. |
| Name | String | test | The name of the ECU. |
| Online | Boolean | true | Indicates whether the instance is online and managed by EDAS. true: The instance is online. false: The instance is not online. |
| RegionId | String | cn-beijing | The ID of the region where the ECU is located. |
| UpdateTime | Long | 1573281040827 | The timestamp of the last modification. |
| UserId | String | 1172****6608**** | The ID of the account. |
| VpcId | String | vpc-2zef6ob8********** | The ID of the VPC instance where the ECU is located. |

| ZoneId | String | cn-beijing-h | The zone where the ECU is located. |
|---|---|---|---|
| Message | String | success | The returned message. |

Request example

```
POST /pop/v5/resource/scale_out_ecu_list HTTP/1.1
```

Response example

```json
<EcuInfoList>
    <IpAddr>192.168.XX.XX</IpAddr>
    <ZoneId>cn-beijing-h</ZoneId>
    <InstanceId>i-2zej4i2jdf*********</InstanceId>
    <CreateTime>1573281040819</CreateTime>
    <EcuId>0de2ebdb-9490-4fc4-be41***************</EcuId>
    <AvailableMem>111</AvailableMem>
    <HeartbeatTime>1573281040819</HeartbeatTime>
    <Name>test</Name>
    <VpcId>vpc-2zef6ob8**********</VpcId>
    <UserId>1172****6608****</UserId>
    <UpdateTime>1573281040827</UpdateTime>
    <RegionId>cn-beijing</RegionId>
    <Online>true</Online>
    <AvailableCpu>2</AvailableCpu>
    <DockerEnv>false</DockerEnv>
</EcuInfoList>
    "EcuInfoList": {
        "IpAddr": "192.168.XX.XX",
        "ZoneId": "cn-beijing-h",
        "InstanceId": "i-2zej4i2jdf*********",
        "CreateTime": 1573281040819,
        "EcuId": "0de2ebdb-9490-4fc4-be41***************",
        "AvailableMem": 111,
        "HeartbeatTime": 1573281040819,
        "Name": "test",
        "VpcId": "vpc-2zef6ob8**********",
        "UserId": "1172****6608****",
        "UpdateTime": 1573281040827,
        "RegionId": "cn-beijing",
        "Online": true,
        "AvailableCpu": 2,
        "DockerEnv": false
```

`},`

```json
    "Message": "success",
    "Code": 200
```

###### 1.1.8.2.6 QueryEccInfo

You can call the QueryEccInfo operation to query information about an Elastic Compute Component (ECC). This operation applies to ECS clusters.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/ecc HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| EccId | String | Query | Yes | b197-40ab-9155- **** | ECC ID |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | Code |
| EccInfo | Struct |   | The information about the ECC. |
| AppId | String | e809****-43d7-4c6b-8e01- b0d9d1db**** | The ID of the application. |
| EccId | String | a5b9****-40b4-4d7b-9c2a- 55d6c1c0**** | The ID of the ECC. |
| EcuId | String | 0d4e****-6d87-401f-ba81- 13df9877**** | The ID of the Elastic Compute Unit (ECU). |
| GroupId | String | 57cd****-2d3b-496f-bcce- 646d0a4d**** | The ID of the group. |
| GroupName | String | DEFAULT GROUP _ _ | The name of the group. |
| PackageMd5 | String | bab6****7a090e41ca9445 c9b3cd**** | The MD5 hash of the package. |
| PackageVersion | String | 20210209.153400 | The version of the package. |
| VpcId | String | vpc-23727**** | The ID of the VPC. |
| Message | String | success | Additional information. |
| RequestId | String | b197-40ab-9155-**** | The ID of the request. |

Sample request

```json
GET /pop/v5/ecc HTTP/1.1
  "EccId": ""
```

Sample responses

```json
<QueryEccInfoResponse>
  <EccInfo>
        <GroupName>_DEFAULT_GROUP</GroupName>
        <VpcId>vpc-23727****</VpcId>
        <AppId>e809****-43d7-4c6b-8e01-b0d9d1db****</AppId>
        <PackageMd5>bab6****7a090e41ca9445c9b3cd****</PackageMd5>
        <EcuId>0d4e****-6d87-401f-ba81-13df9877****</EcuId>
        <EccId>a5b9****-40b4-4d7b-9c2a-55d6c1c0****</EccId>
        <PackageVersion>20210209.153400</PackageVersion>
        <GroupId>57cd****-2d3b-496f-bcce-646d0a4d****</GroupId>
  </EccInfo>
  <RequestId>b197-40ab-9155-****</RequestId>
</QueryEccInfoResponse>
    "EccInfo": {
        "GroupName": "_DEFAULT_GROUP",
        "VpcId": "vpc-23727****",
        "AppId": "e809****-43d7-4c6b-8e01-b0d9d1db****",
        "PackageMd5": "bab6****7a090e41ca9445c9b3cd****",
        "EcuId": "0d4e****-6d87-401f-ba81-13df9877****",
        "EccId": "a5b9****-40b4-4d7b-9c2a-55d6c1c0****",
        "PackageVersion": 20210209.1534,
        "GroupId": "57cd****-2d3b-496f-bcce-646d0a4d****"
```

`},`

```json
    "RequestId": "b197-40ab-9155-****",
    "Message": "success",
    "Code": 200
```

###### 1.1.8.2.7 SynchronizeResource

The SynchronizeResource operation synchronizes your Alibaba Cloud resources with Enterprise Distributed Application Service (EDAS). This operation applies only to ECS clusters. When you synchronize ECS resources, all instance data is synchronized from ECS. If you have more than 100 ECS instances, avoid calling this operation frequently.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/resource/pop_sync_resource HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| Type | String | Query | Yes | ecs | The type of resource to synchronize. Valid values are ecs, slb, vpc, ram, and all. Other values are not supported. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code returned for the request. |
| Data | String | PopSyncResource success | The data returned for the request. |

| Message | String | success | The message returned for the request. |
|---|---|---|---|
| RequestId | String | F8DFGED- K98*************** | The unique identifier of the request. |
| Success | Boolean | true | The result of the request. Valid values: true: The request was successful. false: The request failed. |

Request example

```json
GET /pop/v5/resource/pop\_sync\_resource HTTP/1.1
  "Type": ""
```

Successful response examples

```json
<SynchronizeResourceResponse>
  <Data>PopSyncResource success</Data>
  <Success>true</Success>
</SynchronizeResourceResponse>
 "Message": "success",
 "Data": "PopSyncResource success",
 "Code": 200,
 "Success": true
```

**Notes**

A timeout error may occur when you call this operation because the default connection timeout is 10 seconds. To prevent this error, manually set the timeout period for reading the response from the POP API gateway to 30 seconds. The maximum processing time from the POP API gateway to the service endpoint is 30 seconds. For the Java SDK, set the read timeout in the client code as follows:

```
SynchronizeResourceRequest request = new SynchronizeResourceRequest(); request.setSysReadTimeout(30000); // Unit: milliseconds. The timeout period for the client to wait for a response from the POP API gateway. request.setType("ecs"); ........
```

For the Python SDK, set the read timeout in the client code as follows:

```
request = SynchronizeResourceRequest() request.set_read_timeout(30000) request.set_Type('ecs')
```

#### 1.1.9 Application hosting

##### 1.1.9.1 General

###### 1.1.9.1.1 BindSlb

The BindSlb operation attaches an SLB instance to an application in an ECS cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/app/bind_slb_json HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-********* | The application ID. |
| SlbId | String | Query | Yes | lb- wz96ph63r********** ** | The ID of the SLB instance. |
| SlbIp | String | Query | Yes | 192.16*.*.* | The IP address of the SLB instance. |
| Type | String | Query | Yes | intranet | The network type of the SLB instance. Internet: An Internet-facing SLB instance. Intranet: An internal-facing SLB instance. |
| ListenerPort | Integer | Query | No | 80 | The listener port of the SLB instance. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| Data | Struct |   | The data returned. |
| ExtSlbId | String | lb-bp1vceck3s3b9xs6x**** | The ID of the Internet-facing SLB instance. |
| ExtSlbIp | String | "" | The IP address of the Internet-facing SLB instance. |
| ExtSlbName | String | "" | The name of the Internet-facing SLB instance. |
| SlbId | String | lb-wz96ph63r************ | The ID of the SLB instance. |
| SlbIp | String | 192.16*.*.* | The IP address of the SLB instance. |
| SlbName | String | test********** | The name of the SLB instance. |
| SlbPort | Integer | 80 | The port of the SLB instance. |
| Message | String | bind slb success | Additional information |

Request example

```json
POST /pop/app/bind_slb_json HTTP/1.1 "AppId": "3616cdca-*********", "SlbId": "lb-wz96ph63r************", "SlbIp": "192.16*.*.*", "Type": "intranet"
```

Example of a successful response

```json
<Data>
    <SlbPort>80</SlbPort>
    <SlbId>lb-wz96ph63r************</SlbId>
    <SlbIp>192.168.*.*</SlbIp>
    <SlbName>test*********</SlbName>
</Data> <Message>bind slb success</Message>
 "Data": {
  "SlbPort": 80,
  "SlbId": "lb-wz96ph63r************",
  "SlbIp": "192.168.*.*",
  "SlbName": "test*********"
```

`},`

```json
 "Message": "bind slb success",
 "Code": 200
```

###### 1.1.9.1.2 ContinuePipeline

Continues a pipeline to the next release batch.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/changeorder/pipeline_batch_confirm HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| PipelineId | String | Query | Yes | 5648dbd7- df13**************** **** | The ID of the pipeline. Call the GetChangeOrderInfo operation to get the pipeline ID for a batch in a change process. |
| Confirm | Boolean | Query | No | true | Specifies whether to execute the next release batch. true: Execute the next release batch. false: Do not execute the next release batch. |

**Response elements**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. |

| Message | String | success | Additional information |
|---|---|---|---|
| RequestId | String | D16979DC-4D42- **************** | The ID of the request. |

Sample request

```json
GET /pop/v5/changeorder/pipeline_batch_confirm HTTP/1.1 "PipelineId": "5648dbd7-df13********************"
```

Sample responses

```json
<RequestId>D16979DC-4D42-****************</RequestId>
 "Message": "success",
 "Code": 200,
    "RequestId": "D16979DC-4D42-****************"
```

###### 1.1.9.1.3 GetChangeOrderInfo

You can call the GetChangeOrderInfo operation to retrieve the details of a change process.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/change_order_info HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ChangeOrderId | String | Query | Yes | 1074f3e2-e974- 4a0e-****- ************ | The ID of the change process. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| Message | String | success | More information. |
| changeOrderInfo | Struct |   | The details of the change process. |
| BatchCount | Integer | 1 | The number of batches for the change. |

| BatchType | String | Automatic | The method to execute the next batch in a phased release. Automatic Manual |
|---|---|---|---|
| ChangeOrderId | String | 1074f3e2-e974-4a0e-****- ************ | The ID of the change process. |
| CoType | String | Application Scale Out | The category of the change process. |
| CreateTime | String | 2019-11-13 14:23:46 | The time when the change process was created. |
| CreateUserId | String | edas com*** ****@******- _ _ *****.*** | The owner of the change process. |
| Desc | String | IP of Scale-Out Instance: 47.107.XX.XX | The description of the change process. |
| PipelineInfoList | Array of PipelineInfo |   | The list of tasks for the batched change. |
| PipelineInfo |   |   |   |
| PipelineId | String | 4c4ee320-5e47-4a48-****- ************ | The ID of the process for each batch in a phased change. |
| PipelineName | String | Batch: 1 | The name of the batch. |
| PipelineStatus | Integer | 2 | The status of the task. 0: Ready 1: Executing 2: Successful 3: Failed 6: Stopped 8: Waiting for manual confirmation to execute the next batch in a manual phased release. 9: Waiting for the next batch to be executed in an automatic phased release. 10: Failed due to a system exception. |
| StageList | Array of StageInfoDTO |   | The list of task stages in the change process. |
| StageInfoDTO |   |   |   |
| StageId | String | 358a143f-09a0-45e0-****- ************@** ******* ** _ _ *** | The ID of the stage. |
| StageName | String | Scale Out | The name of the stage. |
| StageResultDTO | Struct |   | The execution result of the stage task. |
| InstanceDTOList | Array of InstanceDTO |   | The execution results of the stage on each ECS instance. |
| InstanceDTO |   |   |   |
| InstanceIp | String | 47.XX.XX.12 (Public) <br>***.**.*.*** (*******) | The IP address of the instance. |
| InstanceName | String | EDAS-scaled | The name of the instance. |
| InstanceStageDTOLi st | Array of InstanceStageDTO |   | The list of stage execution results on each instance. |
| InstanceStageDTO |   |   |   |

| StageId | String | 5dd4c0f2-d81a-406f-****- ************ | The ID of the stage. |
|---|---|---|---|
| StageName | String | scale out | The name of the stage. |
| Status | Integer | 2 | The status of the stage. 0: Ready 1: Executing 2: Successful 3: Failed 6: Stopped 8: Waiting for manual confirmation to execute the next batch in a manual phased release. 9: Waiting for the next batch to be executed in an automatic phased release. 10: Failed due to a system exception. |
| Status | Integer | 2 | The running status. 0: Ready 1: Executing 2: Successful 3: Failed 6: Stopped 8: Waiting for manual confirmation to execute the next batch in a manual phased release. 9: Waiting for the next batch to be executed in an automatic phased release. 10: Failed due to a system exception. |
| ServiceStage | Struct |   | The execution result of the service stage. |
| Message | String | Success | The information about the execution result. |
| StageId | String | 358a143f-09a0-45e0-****- ************ | The ID of the stage. |
| StageName | String | Enable Tengine | The name of the stage. |
| Status | Integer | 2 | The running status. 0: Ready 1: Executing 2: Successful 3: Failed 6: Stopped 8: Waiting for manual confirmation to execute the next batch in a manual phased release. 9: Waiting for the next batch to be executed in an automatic phased release. 10: Failed due to a system exception. |
| Status | Integer | 2 | The status of the stage. 0: Ready 1: Executing 2: Successful 3: Failed 6: Stopped 8: Waiting for manual confirmation to execute the next batch in a manual phased release. 9: Waiting for the next batch to be executed in an automatic phased release. 10: Failed due to a system exception. |

| Status | Integer | 2 | The status of the change. 0: Ready 1: Executing 2: Successful 3: Failed 6: Stopped 8: Waiting for manual confirmation to execute the next batch in a manual phased release. 9: Waiting for the next batch to be executed in an automatic phased release. 10: Failed due to a system exception. |
|---|---|---|---|

Sample request

```json
POST /pop/v5/changeorder/change_order_info HTTP/1.1
  "ChangeOrderId": ""
```

Sample response

```xml
<changeOrderInfo>
    <Status>2</Status>
    <BatchCount>1</BatchCount>
    <CreateTime>2019-11-13 14:23:46</CreateTime>
    <BatchType>Automatic</BatchType>
    <CoType>Application Scale Out</CoType>
    <CreateUserId>edas_com***_****@******-*****.***</CreateUserId>
    <ChangeOrderId>1074f3e2-e974-4a0e-****-************</ChangeOrderId>
    <PipelineInfoList>
        <PipelineInfo>
            <StageList>
                <StageInfoDTO>
                    <StageId>316641fc-69a7-4cc4-****-************</StageId>
                    <Status>2</Status>
                    <StageName>Process Start </StageName>
                    <StageResultDTO>
                        <ServiceStage>
                            <StageId>316641fc-69a7-4cc4-****-************</StageId>
                            <Status>2</Status>
                            <StageName>Process Start </StageName>
                        </ServiceStage>
                        <InstanceDTOList>
                        </InstanceDTOList>
                    </StageResultDTO>
                </StageInfoDTO>
                <StageInfoDTO>
                    <StageId>358a143f-09a0-45e0-****-************@**_*******_*****</StageId>
                    <Status>2</Status>
                    <StageName>Scale Out</StageName>
                    <StageResultDTO>
                        <ServiceStage/>
                        <InstanceDTOList>
                            <InstanceDTO>
                                <Status>2</Status>
                                <InstanceStageDTOList>
                                    <InstanceStageDTO>
                                        <StageId>5dd4c0f2-d81a-406f-****-************</StageId>
                                        <Status>2</Status>
                                        <StageName> scale out </StageName>
                                    </InstanceStageDTO>
                                </InstanceStageDTOList>
                                <InstanceIp>47.XX.XX.27 (Public)&lt;br&gt;***.**.*.*** (*******)</InstanceIp>
<InstanceName>EDASscaledcluster:defaultcluster</InstanceName>
```

```xml
                                <InstanceName>EDAS-scaled-cluster:default-cluster</InstanceName>
                            </InstanceDTO>
                        </InstanceDTOList>
                    </StageResultDTO>
                </StageInfoDTO>
                <StageInfoDTO>
                    <StageId>358a143f-09a0-45e0-****-************</StageId>
                    <Status>2</Status>
                    <StageName>Enable Tengine</StageName>
                    <StageResultDTO>
                        <ServiceStage>
                            <StageId>358a143f-09a0-45e0-****-************</StageId>
                            <Status>2</Status>
                            <StageName>Enable Tengine</StageName>
                        </ServiceStage>
                        <InstanceDTOList>
                        </InstanceDTOList>
                    </StageResultDTO>
                </StageInfoDTO>
                <StageInfoDTO>
                    <StageId>628acb11-09dd-4709-****-************@**_*******_*****</StageId>
                    <Status>2</Status>
                    <StageName>Health Check</StageName>
                    <StageResultDTO>
                        <ServiceStage/>
                        <InstanceDTOList>
                            <InstanceDTO>
                                <Status>2</Status>
                                <InstanceStageDTOList>
                                    <InstanceStageDTO>
                                        <StageId>70fcced7-9b99-409f-****-************</StageId>
                                        <Status>2</Status>
                                        <StageName>Health Check</StageName>
                                    </InstanceStageDTO>
                                </InstanceStageDTOList>
                                <InstanceIp>47.XX.XX.27 (Public)&lt;br&gt;***.**.*.*** (*******)</InstanceIp>
                                <InstanceName>EDAS-scaled-cluster:default-cluster</InstanceName>
                            </InstanceDTO>
                        </InstanceDTOList>
                    </StageResultDTO>
                </StageInfoDTO>
                <StageInfoDTO>
                    <StageId>628acb11-09dd-4709-****-************</StageId>
                    <Status>2</Status>
                    <StageName>Enable SLB</StageName>
                    <StageResultDTO>
                        <ServiceStage>
                            <StageId>628acb11-09dd-4709-****-************</StageId>
                            <Status>2</Status>
                            <StageName>Enable SLB</StageName>
                        </ServiceStage>
                        <InstanceDTOList>
                        </InstanceDTOList>
                    </StageResultDTO>
                </StageInfoDTO>
                <StageInfoDTO>
                    <StageId>bf15f2b1-e7b2-4069-****-************</StageId>
                    <Status>2</Status>
                    <StageName>Process Complete</StageName>
                    <StageResultDTO>
                        <ServiceStage>
                            <StageId>bf15f2b1-e7b2-4069-****-************</StageId>
                            <Status>2</Status>
                            <StageName>Process Complete</StageName>
                        </ServiceStage>
                        <InstanceDTOList>
                        </InstanceDTOList>
                    </StageResultDTO>
                </StageInfoDTO>
```

```json
            </StageList>
            <PipelineName> Batch: 1</PipelineName>
            <PipelineStatus>2</PipelineStatus>
            <PipelineId>4c4ee320-5e47-4a48-****-************</PipelineId>
        </PipelineInfo>
    </PipelineInfoList>
    <Desc>IP of Scale-Out Instance: 47.XX.XX.27 (Public)</Desc>
</changeOrderInfo>
 "Message": "success",
 "changeOrderInfo": {
  "Status": 2,
    "BatchCount": 1,
    "CreateTime": "2019-11-13 14:23:46",
    "BatchType": "Automatic",
    "CoType": "Application Scale Out",
    "CreateUserId": "edas_com***_****@******-*****.***",
    "ChangeOrderId": "1074f3e2-e974-4a0e-****-************",
  "PipelineInfoList": {
    "PipelineInfo": [
            "StageList": {
                "StageInfoDTO": [
                        "StageId": "316641fc-69a7-4cc4-****-************",
                        "Status": 2,
                        "StageName": "Process Start ",
                        "StageResultDTO": {
                            "ServiceStage": {
                                "StageId": "316641fc-69a7-4cc4-****-************",
                                "Status": 2,
                                "StageName": "Process Start ",
                                "Message": "Success"
```

`},`

```json
                            "InstanceDTOList": {
                                "InstanceDTO": []
```

`},`

```json
                        "StageId": "358a143f-09a0-45e0-****-************@**_*******_*****",
                        "Status": 2,
                        "StageName": "Scale Out",
                        "StageResultDTO": {
                            "ServiceStage": {},
                            "InstanceDTOList": {
                                "InstanceDTO": [
                                        "Status": 2,
                                        "InstanceStageDTOList": {
                                            "InstanceStageDTO": [
                                                    "StageId": "5dd4c0f2-d81a-406f-****-************",
                                                    "Status": 2,
                                                    "StageName": " scale out "
```

`]` `},`

```json
                                        "InstanceIp": "47.XX.XX.27 (Public)<br>***.**.*.*** (*******)",
                                        "InstanceName": "EDAS-scaled-cluster:default-cluster"
```

`]` `},`

```json
                        "StageId": "358a143f-09a0-45e0-****-************",
```

`"S` `"`

```json
                        "Status": 2,
                        "StageName": "Enable Tengine",
                        "StageResultDTO": {
                            "ServiceStage": {
                                "StageId": "358a143f-09a0-45e0-****-************",
                                "Status": 2,
                                "StageName": "Enable Tengine",
                                "Message": "Success"
```

`},`

```json
                            "InstanceDTOList": {
                                "InstanceDTO": []
```

`},`

```json
                        "StageId": "628acb11-09dd-4709-****-************@**_*******_*****",
                        "Status": 2,
                        "StageName": "Health Check",
                        "StageResultDTO": {
                            "ServiceStage": {},
                            "InstanceDTOList": {
                                "InstanceDTO": [
                                        "Status": 2,
                                        "InstanceStageDTOList": {
                                            "InstanceStageDTO": [
                                                    "StageId": "70fcced7-9b99-409f-****-************",
                                                    "Status": 2,
                                                    "StageName": "Health Check"
```

`]` `},`

```json
                                        "InstanceIp": "47.XX.XX.27 (Public)<br>***.**.*.*** (*******)",
                                        "InstanceName": "EDAS-scaled-cluster:default-cluster"
```

`]` `},`

```json
                        "StageId": "628acb11-09dd-4709-****-************",
                        "Status": 2,
                        "StageName": "Enable SLB",
                        "StageResultDTO": {
                            "ServiceStage": {
                                "StageId": "628acb11-09dd-4709-****-************",
                                "Status": 2,
                                "StageName": "Enable SLB",
                                "Message": "Success"
```

`},`

```json
                            "InstanceDTOList": {
                                "InstanceDTO": []
```

`},`

```json
                        "StageId": "bf15f2b1-e7b2-4069-****-************",
                        "Status": 2,
                        "StageName": "Process Complete",
                        "StageResultDTO": {
                            "ServiceStage": {
                                "StageId": "bf15f2b1-e7b2-4069-****-************",
                                "Status": 2,
                                "StageName": "Process Complete",
                                "Message": "Success"
```

`},`

```json
                            "InstanceDTOList": {
                                "InstanceDTO": []
```

`]` `},`

```json
            "PipelineName": " Batch: 1",
            "PipelineStatus": 2,
            "PipelineId": "4c4ee320-5e47-4a48-****-************"
```

`]` `},`

```json
  "Desc": "IP of Scale-Out Instance: 47.XX.XX.27 (Public)"
```

`},`

```json
 "Code": 200
```

###### 1.1.9.1.4 GetCluster

You can call the GetCluster operation to obtain information about a specific cluster.

**Request headers**

This operation has no special request headers. For information about common request headers, see Common request parameters.

```
GET /pop/v5/resource/cluster HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | Yes | 5439271a-015b- 433d-****- d76db49**** | The ID of the cluster. Call the ListCluster operation to obtain this ID. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Cluster | Struct |   | The information about the cluster. |
| ClusterId | String | 5439271a-015b-433d- befb-d76db49xxxxx | The ID of the cluster. |
| ClusterName | String | ClusterTest | The name of the cluster. |
| ClusterType | Integer | 2 | The type of the cluster. 0: a regular Docker cluster 1: a Swarm cluster 2: an ECS cluster 3: a self-managed Kubernetes cluster in EDAS 4: a cluster for applications that are automatically registered with Pandora 5: a Container Service for Kubernetes (ACK) cluster |
| Cpu | Integer | 4 | The total number of CPU cores. |
| CpuUsed | Integer | 2 | The number of used CPU cores. |
| CreateTime | Long | 1570708232145 | The timestamp that indicates when the cluster was created. |
| Description | String | Test | The description. |

| IaasProvider | String | ALIYUN | The provider of Infrastructure as a Service (IaaS) resources. |
|---|---|---|---|
| Mem | Integer | 2048 | The total amount of memory. Unit: MB. |
| MemUsed | Integer | 1024 | The amount of used memory. |
| NetworkMode | Integer | 2 | The network type. 1: classic network 2: VPC |
| NodeNum | Integer | 4 | The number of ECS instances. |
| OversoldFactor | Integer | 2 | The CPU overcommitment ratio for the Docker cluster. 1: 1-to-1 ratio, which means no overcommitment. 2: 1-to-2 ratio. 4: 1-to-4 ratio. 8: 1-to-8 ratio. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| UpdateTime | Long | 1570708232145 | The timestamp that indicates when the cluster was last changed. |
| VpcId | String | vpc- xxxxz1mlwpbjx3e9mwe | The ID of the VPC. |
| Code | Integer | 200 | The status code. |
| Message | String | success | Details |
| RequestId | String | d76db491 | The ID of the request. |

Sample request

```json
GET /pop/v5/resource/cluster HTTP/1.1
  "ClusterId": "5439271a-015b-433d-xxxxxxxx"
```

Sample response

```json
<Cluster>
    <MemUsed>2048</MemUsed>
    <Mem>2048</Mem>
    <NetworkMode>2</NetworkMode>
    <UpdateTime>1570708232145</UpdateTime>
    <NodeNum>2</NodeNum>
    <VpcId>vpc-bp19z1mlwpbjx3e9mwefe</VpcId>
    <OversoldFactor>1</OversoldFactor>
    <Cpu>2</Cpu>
    <ClusterId>5439271a-015b-433d-befb-d76db4911b7c</ClusterId>
    <ClusterName>GTSDemoTesting</ClusterName>
    <CreateTime>1561444573420</CreateTime>
    <RegionId>cn-hangzhou</RegionId>
    <CpuUsed>2</CpuUsed>
    <ClusterType>2</ClusterType>
    <IaasProvider>ALIYUN</IaasProvider>
</Cluster>
 "Message": "success",
 "Code": 200,
 "Cluster": {
  "MemUsed": 2048,
  "Mem": 2048,
  "NetworkMode": 2,
  "UpdateTime": 1570708232145,
  "NodeNum": 2,
  "VpcId": "vpc-xxxxz1mlwxxxx3e9mxxxx",
  "OversoldFactor": 1,
  "Cpu": 2,
  "ClusterId": "xxxxxxa-015b-xxxx-befb-xxxxxxxxx",
  "ClusterName": "xxxDemoTesting",
  "CreateTime": 1561444573420,
  "RegionId": "cn-hangzhou",
  "CpuUsed": 2,
  "ClusterType": 2,
  "IaasProvider": "ALIYUN"
```

###### 1.1.9.1.5 GetContainerConfiguration

You can call the GetContainerConfiguration operation to retrieve the Tomcat configuration for an application or an application group.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

```
GET /pop/v5/app/container_config HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- ************** | The application ID. Call the ListApplication operation to obtain this ID. |

| GroupId | String | Query | No | 8123db90-880f- ************** | The ID of the application instance group. If you specify a group ID, the operation returns the Tomcat configuration for that application group. If you set this parameter to null , the operation returns the Tomcat configuration for the application. |
|---|---|---|---|---|---|

**Data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code for the call. |
| ContainerConfigurati on | Struct |   | The Tomcat configuration. |
| ContextPath | String | / | The Tomcat context path. |
| HttpPort | Integer | 8080 | The application port. The value set in the application configuration is returned. |
| MaxThreads | Integer | 400 | The maximum number of threads. The configured value is returned. If this parameter is not set for the application group, the value configured for the application is returned. If this parameter is not set for the application, the default value is returned. |
| URIEncoding | String | ISO-8859-1 | The URI encoding format. Valid values include ISO-8859- 1, GBK, GB2312, and UTF-8. The configured value is returned. If this parameter is not set for the application group, the value configured for the application is returned. If this parameter is not set for the application, the default value is returned. |
| UseBodyEncoding | Boolean | true | Indicates whether useBodyEncodingForURI is enabled. The configured value is returned. If this parameter is not set for the application group, the value configured for the application is returned. If this parameter is not set for the application, the default value is returned. |
| Message | String | success | The message returned for the call. |

Example request

```json
GET /pop/v5/app/container_config HTTP/1.1
  "AppId": ""
```

Example of a successful response

```json
<ContainerConfiguration>
    <UseBodyEncoding>true</UseBodyEncoding>
    <ContextPath>ROOT</ContextPath>
    <MaxThreads>400</MaxThreads>
    <HttpPort>8080</HttpPort>
    <URIEncoding>ISO-8859-1</URIEncoding>
</ContainerConfiguration>
 "Message": "success",
 "ContainerConfiguration": {
  "UseBodyEncoding": true,
  "ContextPath": "ROOT",
  "MaxThreads": 400,
  "HttpPort": 8080,
  "URIEncoding": "ISO-8859-1"
```

`},`

```json
 "Code": 200
```

###### 1.1.9.1.6 GetJvmConfiguration

You can call the GetJvmConfiguration operation to retrieve the Java Virtual Machine (JVM) settings for an application or an application group.

**Request header**

This operation uses only common request headers. For more information, see the document about common request parameters.

```
GET /pop/v5/app/app_jvm_config HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4*************** | The application ID. |
| GroupId | String | Query | No | 8123db90-880f- 48************** | The ID of the application instance group. If you specify an ID, the JVM configuration for the application instance group is returned. If you leave this parameter empty, the JVM configuration for the application is returned. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| JvmConfiguration | Struct |   | The JVM configuration of the application or application group. |
| MaxHeapSize | Integer | 1000 | The maximum heap memory size. Unit: MB. |
| MaxPermSize | Integer | 1000 | The permanent generation memory size. Unit: MB. |

| MinHeapSize | Integer | 500 | The initial heap memory size. Unit: MB. |
|---|---|---|---|
| Options | String | - XX:+UseConcMarkSweepG C -XX:-UseParNewGC | Custom parameters. |
| Message | String | success | Additional information. |

Request example

```json
GET /pop/v5/app/app_jvm_config HTTP/1.1
  "AppId": ""
```

Successful response example

```json
<JvmConfiguration>
    <MaxHeapSize>1000</MaxHeapSize>
    <MinHeapSize>500</MinHeapSize>
    <Options> -XX:+UseConcMarkSweepGC -XX:-UseParNewGC</Options>
</JvmConfiguration>
 "Message": "success",
 "JvmConfiguration": {
  "MaxHeapSize": 1000,
  "MinHeapSize": 500,
  "Options": " -XX:+UseConcMarkSweepGC -XX:-UseParNewGC"
```

`},`

```json
 "Code": 200
```

###### 1.1.9.1.7 ListApplication

You can call the ListApplication operation to retrieve a list of applications.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/app/app_list HTTP/1.1
```

None

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ApplicationList | Array of Application |   | The list of applications. |
| Application |   |   |   |
| AppId | String | 00ee517d-dd7d-4d4e-****- ************ | The ID of the application. |

| ApplicationType | String | FatJar | The deployment type of the application: War: The application is deployed from a WAR package. FatJar: The application is deployed from a JAR package. Image: The application is deployed from an image. Empty: The application is not deployed. |
|---|---|---|---|
| BuildPackageId | Long | 58 | The ID of the container version. |
| ClusterId | String | c37aec2a-bcca-4ec1-****- ************ | The ID of the cluster. |
| ClusterType | Integer | 2 | The type of the cluster where the application is deployed: 2: ECS cluster. 3: Self-managed Kubernetes cluster in EDAS. 5: Container Service for Kubernetes (ACK) cluster. |
| Cpu | Integer | 1 | The total number of CPU cores. |
| CreateTime | Long | 1542692376066 | The timestamp when the application was created. |
| Description | String | create by edas pop api | The description of the application. |
| Dockerize | Boolean | false | Indicates whether the application is a Docker application. Valid values: true: Yes false: No |
| HealthCheckUrl | String | http://127.0.0.1:8080/ ehc. _ html | The health check URL. |
| InstanceCount | Integer | 2 | The number of instances. |
| Memory | Integer | 500 | The total memory size. Unit: MB. |
| Name | String | doc-test-consumer | The name of the application. |
| Owner | String | 249763358688******** | The owner of the application. This is the user who created the application. |
| Port | Integer | 8080 | The default port of the application is 8080. Call the UpdateContainerConfiguration operation to change the port. |
| RegionId | String | cn-beijing:docTes | The ID of the region. |
| RunningInstanceCou nt | Integer | 0 | The number of running application instances. |
| UserId | String | tdy218@1362469756xxxx xx | The user ID of the application owner. |
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |

Request example

```
POST /pop/v5/app/app_list HTTP/1.1
```

Response example

```json
<RequestId>5d6fa0bc-cc3**********</RequestId> <ApplicationList>
    <Application>
        <BuildPackageId>58</BuildPackageId>
        <ApplicationType>FatJar</ApplicationType>
        <ResourceGroupId>rg-aek24j4s4b*****</ResourceGroupId>
        <AppId>00ee517d-dd7d-4d4e-****-************</AppId>
        <ClusterId>c37aec2a-bcca-4ec1-****-************</ClusterId>
        <ClusterType>2</ClusterType>
        <RegionId>cn-beijing:docTes</RegionId>
        <RunningInstanceCount>0</RunningInstanceCount>
        <Name>doc-test-consumer</Name>
    </Application>
</ApplicationList>
    "RequestId": "5d6fa0bc-cc3**********",
    "Message": "success",
    "ApplicationList": {
        "Application": {
            "BuildPackageId": 58,
            "ApplicationType": "FatJar",
            "ResourceGroupId": "rg-aek24j4s4b*****",
            "AppId": "00ee517d-dd7d-4d4e-****-************",
            "ClusterId": "c37aec2a-bcca-4ec1-****-************",
            "ClusterType": 2,
            "RegionId": "cn-beijing:docTes",
            "RunningInstanceCount": 0,
            "Name": "doc-test-consumer"
```

`},`

```json
    "Code": 200
```

###### 1.1.9.1.8 ListBuildPack

The ListBuildPack operation retrieves a list of container versions.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the documentation about common request parameters.

```
POST /pop/v5/app/build_pack_list HTTP/1.1
```

This operation has no request parameters.

**Response data**

| Name | Type | Example value | Description |
|---|---|---|---|
| BuildPackList | Array of BuildPack |   | A list of container versions. |
| BuildPack |   |   |   |

| ConfigId | Long | 57 | The ID of the container version. |
|---|---|---|---|
| Disabled | Boolean | false | Indicates whether the version is disabled. A disabled version cannot be used. |
| Feature | String | restful | The feature in public preview. |
| ImageId | String | registry.aliyuncs.com/ed**/ ****-*********:*.*.* | The ID of the base image for the container. |
| MultipleTenant | Boolean | true | Indicates whether multitenancy is supported. |
| PackVersion | String | 3.5.6 | The version number of the application. |
| PandoraDesc | String | test | The description of Pandora. |
| PandoraDownloadUrl | String | http://edas.oss-cn- hangzhou.aliyuncs.com/ed as- plugins/edas.sar.V3.5.6/tao bao-hsf.tgz | The download URL for Pandora. |
| PandoraVersion | String | edas.public.sar.V3.5.6 | The version number of Pandora. |
| PluginInfo | String | 1 | The description of the plugin. |
| ScriptName | String | default | The name of the shell script. |
| ScriptVersion | String | 1.0.3 | The version of the shell script. |
| SupportFeatures | String | tengine,fatjar,restful,eip n _ odeport,dpath | The supported features. |
| TengineDownloadUrl | String | http://edas.oss-cn- hangzhou.aliyuncs.com/co mponents/tengine/3.4.7/te ngine.sh | The download URL for the Tengine installation program. |
| TengineImageId | String | registry.aliyuncs.com/edas /****-*********-*****:*.*.* | The ID of the Tengine image for the container. |
| TomcatDesc | String | 1. Updated the config- client plugin to fix a cache read failure in multitenancy scenarios. 2. Updated the HSF plugin to resolve an issue where the Pandora QoS command fails and an issue where the endpoint is not found when many services are subscribed. 3. Upgraded all plugins that use FastJSON to the sec06 security version. | The description of Tomcat. |
| TomcatDownloadUrl | String | http://edas.oss-cn- hangzhou.aliyuncs.com/ed as- container/7.0.92/taobao- tomcat-production- 7.0.92.tar.gz | The download URL for the Tomcat installation program. |
| TomcatPath | String | taobao-tomcat-production- 7.0.59.3 | The name of the Tomcat folder. |
| TomcatVersion | String | 8.5.63 | The version number of Tomcat. |

| WithTengine | Boolean | true | Indicates whether traffic management is supported. |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |

Request example

```
POST /pop/v5/app/build_pack_list HTTP/1.1
```

Successful response example

```xml
<BuildPackList>
    <TomcatDesc>1. Updated the config-client plugin to fix a cache read failure in multitenancy scenarios. 2. Updated
the HSF plugin to resolve an issue where the Pandora QoS command fails and an issue where the endpoint is not found w hen many services are subscribed. 3. Upgraded all plugins that use FastJSON to the sec06 security version. </TomcatDesc>
    <ScriptVersion>1.0.3</ScriptVersion>
    <WithTengine>true</WithTengine>
    <TomcatDownloadUrl>http://edas.oss-cn-hangzhou.aliyuncs.com/edas-container/7.0.92/taobao-tomcat-production-7.0.92
.tar.gz</TomcatDownloadUrl>
    <Feature>restful</Feature>
    <PandoraVersion>edas.public.sar.V3.5.6</PandoraVersion>
    <PackVersion>3.5.6</PackVersion>
    <MultipleTenant>true</MultipleTenant>
    <PandoraDownloadUrl>http://edas.oss-cn-hangzhou.aliyuncs.com/edas-plugins/edas.sar.V3.5.6/taobao-
hsf.tgz</PandoraDownloadUrl>
    <PandoraDesc>test</PandoraDesc>
    <TomcatPath>taobao-tomcat-production-7.0.59.3</TomcatPath>
    <ScriptName>default</ScriptName>
    <ImageId>registry.aliyuncs.com/ed**/****-*********:*.*.*</ImageId>
    <TengineDownloadUrl>http://edas.oss-cn-
hangzhou.aliyuncs.com/components/tengine/3.4.7/tengine.sh</TengineDownloadUrl>
    <PluginInfo>1</PluginInfo>
    <TomcatVersion>8.5.63</TomcatVersion>
    <ConfigId>57</ConfigId>
    <Disabled>false</Disabled>
    <TengineImageId>registry.aliyuncs.com/edas/****-*********-*****:*.*.*</TengineImageId>
    <SupportFeatures>tengine,fatjar,restful,eip_nodeport,dpath</SupportFeatures>
</BuildPackList>
```

```json
    "Message": "success",
    "BuildPackList": {
        "TomcatDesc": "1. Updated the config-client plugin to fix a cache read failure in multitenancy scenarios. 2.
Updated the HSF plugin to resolve an issue where the Pandora QoS command fails and an issue where the endpoint is not found when many services are subscribed. 3. Upgraded all plugins that use FastJSON to the sec06 security version.",
        "ScriptVersion": "1.0.3",
        "WithTengine": true,
        "TomcatDownloadUrl": "http://edas.oss-cn-hangzhou.aliyuncs.com/edas-container/7.0.92/taobao-tomcat-
production-7.0.92.tar.gz",
        "Feature": "restful",
        "PandoraVersion": "edas.public.sar.V3.5.6",
        "PackVersion": "3.5.6",
        "MultipleTenant": true,
        "PandoraDownloadUrl": "http://edas.oss-cn-hangzhou.aliyuncs.com/edas-plugins/edas.sar.V3.5.6/taobao-hsf.tgz",
        "PandoraDesc": "test",
        "TomcatPath": "taobao-tomcat-production-7.0.59.3",
        "ScriptName": "default",
        "ImageId": "registry.aliyuncs.com/ed**/****-*********:*.*.*",
        "TengineDownloadUrl": "http://edas.oss-cn-hangzhou.aliyuncs.com/components/tengine/3.4.7/tengine.sh",
        "PluginInfo": 1,
        "TomcatVersion": "8.5.63",
        "ConfigId": 57,
        "Disabled": false,
        "TengineImageId": "registry.aliyuncs.com/edas/****-*********-*****:*.*.*",
        "SupportFeatures": "tengine,fatjar,restful,eip_nodeport,dpath"
```

`},`

```json
    "Code": 200
```

###### 1.1.9.1.9 ListHistoryDeployVersion

You can call the ListHistoryDeployVersion operation to retrieve the historical deployment versions of an application.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/app/deploy_history_version_list HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4413-****- ************ | The application ID. |

**Data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |
| PackageVersionList | Array of PackageVersion |   | The list of deployment package versions. |
| PackageVersion |   |   |   |
| AppId | String | 3616cdca-4f92-4413-****- ************ | The application ID. |
| CreateTime | Long | 1573627440892 | The creation timestamp. |

| Description | String | deploy | The description of the historical version. |
|---|---|---|---|
| Id | String | 441beb18-da42-44dc-****- ************ | The unique ID of the historical version. |
| PackageVersion | String | 1.0 | The published version. Use this version for rollbacks. |
| Type | String | url | The deployment type. url: The application is deployed using a JAR or WAR package. image: The application is deployed using an image. |
| UpdateTime | Long | 1573627440892 | The timestamp of the last update. |
| WarUrl | String | http://edas-sz.oss-cn- shenzhen**********/SPRIN G CLOUD PROVIDER.jar _ _ | The URL of the deployment package. |

Sample request

```json
GET /pop/v5/app/deploy_history_version_list HTTP/1.1 "AppId": "3616cdca-4f92-4413-****-************"
```

Sample responses

```json
<PackageVersionList>
    <Type>url</Type>
    <Description>deploy</Description>
    <AppId>3616cdca-4f92-4413-****-************</AppId>
    <WarUrl>http://edas-sz.oss-cn-shenzhen**********/SPRING_CLOUD_PROVIDER.jar</WarUrl>
    <CreateTime>1573627440892</CreateTime>
    <UpdateTime>1573627440892</UpdateTime>
    <Id>441beb18-da42-44dc-****-************</Id>
    <PackageVersion>1.0</PackageVersion>
</PackageVersionList>
    "PackageVersionList": {
        "Type": "url",
        "Description": "deploy",
        "AppId": "3616cdca-4f92-4413-****-************",
        "WarUrl": "http://edas-sz.oss-cn-shenzhen**********/SPRING_CLOUD_PROVIDER.jar",
        "CreateTime": 1573627440892,
        "UpdateTime": 1573627440892,
        "Id": "441beb18-da42-44dc-****-************",
        "PackageVersion": 1
```

`},`

```json
    "Message": "success",
    "Code": 200
```

###### 1.1.9.1.10 ListUserDefineRegion

You can call the ListUserDefineRegion operation to retrieve a list of user-defined namespaces.

**Request header**

This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

```
POST /pop/v5/user_region_defs HTTP/1.1
```

None

**Response data**

| Name | Type | Example value |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
| Code | Integer | 200 |   | The status code of the API call or a POP error code. |   |   |   |   |
| Message | String | success |   | Additional information |   |   |   |   |
| UserDefineRegionLis t | Array of UserDefineRegionEn tity |   |   | A list of user-defined namespaces. |   |   |   |   |
| UserDefineRegionEn tity |   |   |   |   |   |   |   |   |
| BelongRegion | String | cn-shenzhen |   | The region ID. |   |   |   |   |
| Description | String | betaappManager |   | The description of the namespace. |   |   |   |   |
| Id | Long | 1330 |   | The unique ID. |   |   |   |   |
| RegionId | String | cn- shenzhen:betaappManager |   | The ID of the namespace. Note The ID cannot be changed after creation. The format is Physical region |   |   |   |   |
|   |   |   |   |   | Note The ID cannot be changed after creation. The format is Physical region |   |   |   |
|   |   |   |   |   |   | Physical region |   |   |
|   |   |   |   |   | ID:Logical region identifier |   |   |   |
| RegionName | String | betaappManager |   | The name of the namespace. |   |   |   |   |
| UserId | String | edas **** test@aliyun- _ _ ****.com |   | The ID of the Alibaba Cloud account. |   |   |   |   |

Request example

```
POST /pop/v5/user_region_defs HTTP/1.1
```

Successful response examples

```json
<ListUserDefineRegionResponse>
  <UserDefineRegionList>
        <UserDefineRegionEntity>
              <Description>betaappManager</Description>
              <RegionName>betaappManager</RegionName>
              <BelongRegion>cn-shenzhen</BelongRegion>
              <RegionId>cn-shenzhen:betaappManager</RegionId>
              <Id>1330</Id>
              <UserId>edas_****_test@aliyun-****.com</UserId>
              <DebugEnable>false</DebugEnable>
        </UserDefineRegionEntity>
  </UserDefineRegionList>
</ListUserDefineRegionResponse>
 "Message": "success",
 "Code": 200,
 "UserDefineRegionList": {
  "UserDefineRegionEntity": [
    "Description": "betaappManager",
    "RegionName": "betaappManager",
    "BelongRegion": "cn-shenzhen",
    "RegionId": "cn-shenzhen:betaappManager",
    "Id": 1330,
    "UserId": "edas_****_test@aliyun-****.com",
    "DebugEnable": false
```

`]`

###### 1.1.9.1.11 ResetApplication

You can call the ResetApplication operation to reset an application.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_reset HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca- 4f92********* | The ID of the application. You can call the ListApplication operation to obtain the application ID. |
| EccInfo | String | Query | Yes | 0cf49a6c-*********** | The ECC IDs of the instances in the application that you want to reset. Separate multiple ECC IDs with commas (,). You can call the QueryApplicationStatus operation to obtain the ECC IDs. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|

| ChangeOrderId | String | 1c66548e-a082- 40************ | The ID of the change process. You can call the GetChangeOrderInfo operation to query the execution progress of the reset task. |
|---|---|---|---|
| Code | Integer | 200 | Code |
| Message | String | success | Additional information |

Request example

```json
POST /pop/v5/changeorder/co_reset HTTP/1.1
  "AppId": ""
  "EccInfo": ""
```

Successful response example

```json
<ResetApplicationResponse>
  <ChangeOrderId>1c66548e-a082-40************</ChangeOrderId>
</ResetApplicationResponse>
 "Message": "success",
 "ChangeOrderId": "1c66548e-a082-40************",
 "Code": 200
```

###### 1.1.9.1.12 AbortChangeOrder

You can call the AbortChangeOrder operation to stop a change flow.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /pop/v5/changeorder/change_order_abort HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| ChangeOrderId | String | Query | Yes | 4f038ddf-b27b-****- ****-88e44375**** | The ID of the change flow. For information about how to obtain this ID, see GetChangeOrderInfo. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | API status code or POP error code |

| Data | Struct |   | The change flow. |
|---|---|---|---|
| ChangeOrderId | String | 4f038ddf-b27b-****-****- 88e44375**** | The ID of the change flow. |
| ErrorCode | String | success | The error code. |
| Message | String | success | Additional information. |
| RequestId | String | 57F146F6-3C94-****-****- A66EF4B9***** | The ID of the request. |
| TraceId | String | 0b59000b15947****55688 656d**** | The trace ID. |

Request example

```json
PUT /pop/v5/changeorder/change_order_abort HTTP/1.1
  "ChangeOrderId": ""
```

Successful response example

```json
<AbortChangeOrder>
     <Data>
          <ChangeOrderId>4f038ddf-b27b-****-****-88e44375****</ChangeOrderId>
     </Data>
     <TraceId>0b59000b15947****55688656d****</TraceId>
        <RequestId>57F146F6-3C94-****-****-A66EF4B9*****</RequestId>
     <Success>true</Success>
     <ErrorCode>success</ErrorCode>
</AbortChangeOrder>
    "Data": {
        "ChangeOrderId": "4f038ddf-b27b-****-****-88e44375****"
```

`},`

```json
    "Message": "success",
    "TraceId": "0b59000b15947****55688656d****",
    "RequestId": "57F146F6-3C94-****-****-A66EF4B9*****",
    "ErrorCode": "success",
    "Code": 200
```

###### 1.1.9.1.13 AbortAndRollbackChangeOrder

The AbortAndRollbackChangeOrder operation stops and rolls back a change process. This operation is available for applications in Container Service for Kubernetes (ACK) clusters and Serverless Kubernetes (ASK) clusters. Currently, this operation supports only change processes for application deployments.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /pop/v5/changeorder/change_order_abort_and_rollback HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ChangeOrderId | String | Query | Yes | 30b2374d-9520- ****-****- 4d72795c**** | The ID of the change process. |

**Data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | API status code or POP error code |
| Data | Struct |   | The information about the change process. |
| ChangeOrderId | String | 30b2374d-9520-****-****- 4d72795c**** | The ID of the change process. |
| ErrorCode | String | success | The error code. |
| Message | String | success | Additional information |
| RequestId | String | 81E0B333-2871-****-****- B8F5FF43**** | The request ID. |
| TraceId | String | 0b59000b159471036****8 656d**** | The trace ID. |

Example request

```json
PUT /pop/v5/changeorder/change_order_abort_and_rollback HTTP/1.1
  "ChangeOrderId": "30b2374d-9520-****-****-4d72795c****"
```

Example response

```json
<ChangeOrderIdResponse>
      <Data>
            <ChangeOrderId>30b2374d-9520-****-****-4d72795c****</ChangeOrderId>
      </Data>
      <TraceId>0b59000b159471036****8656d****</TraceId>
      <RequestId>81E0B333-2871-****-****-B8F5FF43****</RequestId>
      <ErrorCode>success</ErrorCode>
</ChangeOrderIdResponse>
    "Data": {
        "ChangeOrderId": "30b2374d-9520-****-****-4d72795c****"
```

`},`

```json
    "Message": "success",
    "TraceId": "0b59000b159471036****8656d****",
    "RequestId": "81E0B333-2871-****-****-B8F5FF43****",
    "ErrorCode": "success",
    "Code": 200
```

###### 1.1.9.1.14 QueryApplicationStatus

You can call the QueryApplicationStatus operation to query the status of an application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
GET /pop/v5/app/app_status HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92-441************** | The ID of the application. |

**Return Data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D16979DC-4D42-******** | The ID of the request. |
| Code | Integer | 200 | The status of the API call or a POP error code. |
| Message | String | success | Additional information. |
| AppInfo | Struct |   | The information about the application. |
| -EcuList | Array |   | The information about the ECUs. |
| --EcuId | String |   | The unique ID of the ECU. Obtain this ID by running the dmidecode command on an ECS instance. |
| --Online | Boolean | false | Indicates whether the ECU is online. |
| --DockerEnv | Boolean | true | Indicates whether Docker is installed. |
| --CreateTime | Long | 169890764 | The time when the resource was created. |
| --UpdateTime | Long | 1573635952012 | The timestamp of the last update. |
| --IpAddr | String | 172.16.*.** | The internal IP address of the ECU. |
| --HeartbeatTime | Long | 1573635952012 | The timestamp of the last heartbeat. |
| --UserId | String | dd1f0-04a0-4d0e-be***** | The ID of the user. |
| --GroupId | String | 8123db90-880f-486f-****- ************ | The ID of the group. |
| --Name | String | xxx | The name. |
| --ZoneId | String | cn-shen****-* | The ID of the zone. |
| --RegionId | String | cn-wulan-env*** | The ID of the region. |

| Service (EDAS) |   |   | Service Developer Guide·API refe rence |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --InstanceId | String | i-wz9fp1ljg*********** | The ID of the instance. |
| --VpcId | String | vpc- wz9b246zg************ | The ID of the VPC. |
| --RegionId | String | cn-wulan-env*** | The ID of the region. |
| --AvailableCpu | Integer | 0 | The number of available CPU cores. |
| --AvailableMem | Integer | 0 | The available memory. |
| --Cpu | Integer | 0 | Processor |
| --Mem | Integer | 0 | The memory. |
| -EccList | Array |   | The information about the ECCs. |
| --EccId | String | 0cf49a6c-95a8-4aa8-****- ************ | The unique ID of the ECC. |
| --EcuId | String | 07bd417a-b863-477d-****- ************ | The unique ID of the ECU. |
| --AppId | String | 29e36f7-5d9e-4c2d***** | The ID of the application. |
| --AppState | Integer | 7 | The status of the application instance: 0: AGENT OFF. The agent is offline. 1: STOPPED. The _ application is stopped. 3: RUNNING BUT URL FAILED. The _ _ _ health check failed. 7: RUNNING. The application is running. |
| --TaskState | Integer | 3 | The status of the most recent task on the instance: 0: UNKNOWN. The status is unknown. 1: PROCESSING. The task is in progress. 2: SUCCESS. The task was successful. 3: FAILED. The task failed. |
| --CreateTime | Long | 169890764 | The time when the resource was created. |
| --UpdateTime | Long | 1573635952012 | The timestamp of the last update. |
| --Ip | String | 172.16.*.*** | The internal IP address of the ECU. |
| --VpcId | String | vpc- wz9b246zg************ | The ID of the VPC. |
| --GroupId | String | 8123db90-880f-486f-****- ************ | The ID of the group. |
| -GroupList | Array |   | The information about the groups. |
| --GroupId | String | 8123db90-880f-486f-****- ************ | The ID of the group. |
| --GroupName | String | DEFAULT GROUP _ _ | The name of the group. |
| --AppId | String | 29e36f7-5d9e-4c2d***** | The ID of the application. |

| Enterprise Distrib Service Developer | uted Application Guide·API refe |   | Enterprise Distributed Application Service (EDAS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --PackageVersionId | String | 441beb18-da42-44dc-****- ************ | The ID of the package that is deployed in the group. |
| --AppVersionId | String | changeorder a** ******* * _ _ _ * | The ID of the group deployment record. |
| --GroupType | Integer | 0 | The type of the group: 0: Default. 1: User-created. 2: Grayscale. |
| --ClusterId | String | 24ddd1f0-04a0-4d0e- bead**** | The ID of the cluster. |
| --CreateTime | Long | 169890764 | The time when the group was created. |
| --UpdateTime | Long | 1573627441388 | The timestamp of the last update. |
| -Application | Struct |   | The basic information about the application. |
| --ApplicationId | String | 29e36f7-5d9e-4c2d***** | The ID of the application. |
| --BuildPackageId | Integer | 0 | The ID of the build package. |
| --ClusterId | String | 24ddd1f0-04a0-4d0e- bead**** | The ID of the cluster. |
| --Cpu | Integer | 0 | Processor |
| --CreateTime | Long | 169890764 | The time when the application was created. |
| --Dockerize | Boolean | false | Indicates whether the application is deployed in a Docker container. |
| --Email | String | ***** | The email address. |
| --HealthCheckUrl | String | http://127.0.0.1:8080/runC heck | The health check URL. |
| --InstanceCount | Integer | 2 | The number of instances. |
| --LaunchTime | Long | 0 | The launch time. |
| --Memory | Integer | 0 | The memory. |
| --Name | String | xxx | Name |
| --Owner | String | 16989076 | The owner. |
| --Phone | String | 180******* | The phone number. |
| --Port | Integer | 80 | The port number. |
| --RegionId | String | cn-wulan-env*** | The ID of the region. |
| -- RunningInstanceCou nt | Integer | 2 | The total number of running instances. |

| Enterprise Distrib Service (EDAS) | uted Application |   | Service Developer Guide·API refe rence |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --UserId | String | dd1f0-04a0-4d0e-be***** | The ID of the user. |

Sample request

```
GET /pop/v5/app/app_status HTTP/1.1 &AppId=3616cdca-4f92-441************** &<Common request parameters>
```

Sample response

```json
 "RequestId":"D16979DC-4D42-********",
 "Message":"success",
 "Code":200,
 "AppInfo":{
  "-GroupList":{
   "GroupName":"_DEFAULT_GROUP",
   "AppId":"29e36f7-5d9e-4c2d*****",
   "GroupType":0,
   "ClusterId":"24ddd1f0-04a0-4d0e-bead****",
   "CreateTime":169890764,
   "UpdateTime":1573627441388,
   "PackageVersionId":"441beb18-da42-44dc-****-************",
   "AppVersionId":"changeorder_a**_*******_**",
   "GroupId":"8123db90-880f-486f-****-************"
```

`},`

```json
  "-Application":{
   "BuildPackageId":0,
   "Dockerize":false,
   "Owner":"16989076",
   "Email":"*****",
   "LaunchTime":0,
   "HealthCheckUrl":"http://127.0.0.1:8080/runCheck",
   "ClusterId":"24ddd1f0-04a0-4d0e-bead****",
   "Memory":0,
   "CreateTime":169890764,
   "Port":80,
   "Cpu":0,
   "Name":"xxx",
   "InstanceCount":2,
   "Phone":"180*******",
   "UserId":"dd1f0-04a0-4d0e-be*****",
   "RegionId":"cn-wulan-env***",
   "ApplicationId":"29e36f7-5d9e-4c2d*****",
   "RunningInstanceCount":2
```

`},`

```json
  "-EcuList":{
   "IpAddr":"172.16.*.**",
   "ZoneId":"cn-shen****-*",
   "InstanceId":"i-wz9fp1ljg***********",
   "CreateTime":169890764,
   "EcuId":"",
   "Cpu":0,
   "HeartbeatTime":1573635952012,
   "AvailableMem":0,
   "GroupId":"8123db90-880f-486f-****-************",
   "Name":"xxx",
   "VpcId":"vpc-wz9b246zg************",
   "Mem":0,
   "UserId":"dd1f0-04a0-4d0e-be*****",
   "UpdateTime":1573635952012,
   "RegionId":"cn-wulan-env***",
   "Online":false,
   "DockerEnv":true,
   "AvailableCpu":0
```

`},`

```json
  "-EccList":{
   "AppId":"29e36f7-5d9e-4c2d*****",
   "VpcId":"vpc-wz9b246zg************",
   "CreateTime":169890764,
   "Ip":"172.16.*.***",
   "UpdateTime":1573635952012,
   "EcuId":"07bd417a-b863-477d-****-************",
   "EccId":"0cf49a6c-95a8-4aa8-****-************",
   "AppState":7,
   "TaskState":3,
   "GroupId":"8123db90-880f-486f-****-************"
```

###### 1.1.9.1.15 GetEffectiveSpringAppConfig

Retrieves the configuration of a Spring application instance.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
GET /pop/v5/app/configExtract HTTP/1.1
```

| Parameter | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The application ID. |
| EccId | String | Query | Yes | csb-cop-broker-i- a4854351007a1e59f00-group-1-v1- 64f899747****** | The pod ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 69CD31EF-A412-42DD- 8AD9-1201D****** | The request ID. |
| Code | Integer | 200 | The status code. |
| Message | String | success | Additional information. |
| Data | Struct | - | The returned data. |
| ConfigList | Array | - | The list of configurations. |
| Name | String | jvmMachineProperties | The name of the configuration item. |
| ConfigType | String | jvmMachineProperties | The configuration type. |
|   |   | - javaagent:/home/admin/.o pt/ArmsAgent/arms- bootstrap-1.7.0- SNAPSHOT.jar - Darms.licenseKey=190532 8884798675@75360cd0b2 715e0 -Darms.appId=2dfea044- 479f-464a-b374- f14d328e7191 -Darms.agent.env=edas -Darms.agent.args= -Xms1g -Xmx1g -Xmn500m -XX:MetaspaceSize=128m |   |

|   |   | - XX:MaxMetaspaceSize=25 6m - |   |
|---|---|---|---|
| Content | String | XX:MaxDirectMemorySize= 256m - XX:ReservedCodeCacheSiz e=64m - XX:+HeapDumpOnOutOfM emoryError - XX:HeapDumpPath=/home /admin/cop-broker -Djava.awt.headless=true - Djava.security.egd=file:/de v/./urandom -Dfile.encoding=UTF-8 -Dproject.name=i- a4854351007a1e59f00 -Dahas.gateway.address= -Dahas.license= - Dahas.namespace=default -Dahas.agw.type=1 -Dahas.acm.enable=false -Dcsp.sentinel.app.type=1 - Dio.netty.allocator.type=u npooled - XX:ErrorFile=/home/admin/ cop-broker/csb-cop-broker- i-a4854351007a1e59f00- group-1-v1- 64f8997479q8pvf.hs err.2 _ 02410221118.log - Djavax.net.ssl.trustStore=/ usr/local/cloud/cacerts - Djavax.net.ssl.trustStorePa ssword=changeit - Dserver.tomcat.accesslog. encoding=UTF-8 - Dserver.tomcat.accesslog. prefix=csb-cop-broker-i- a4854351007a1e59f00- group-1-v1- 64f8997479q8pvf - Dserver.tomcat.accesslog.f ile-date-format=- yyyyMMdd - Dserver.tomcat.accesslog. suffix=-access-json.log - Dserver.tomcat.accesslog. directory=/home/admin/co p-broker - Dserver.tomcat.accesslog. enabled=true | The configuration content. |

|   |   | - Dserver.tomcat.accesslog. pattern= {\"x forwarded for\":\"% _ _ {X-Forwarded- For}i\",\"client ip\":\"%h\",\ _ "client user\":\"%l\",\"auth _ enticated\":\"%u\",\"reques t time\":\"%{yyyy-MM- _ dd'T'HH:mm:ss.SSSZ}t\",\" request url\":\"%r\",\"http _ _ code\":\"%s\",\"send bytes\ _ ":\"%b\",\"query string\":\" _ %q\",\"http referer\":\"% _ {Referer}i\",\"user agent\" _ :\"%{User- Agent}i\",\"request time _ _ ms\":\"%D\"} - |   |
|---|---|---|---|

Dloader.path=/home/admi n/cop-broker Request example

```
GET /pop/v5/app/configExtract HTTP/1.1 &AppId=2dfea044-479f-464a-b374-f14d32****** &EccId=csb-cop-broker-i-a4854351007a1e59f00-group-1-v1-64f899747****** &Common request parameters
```

Response example

```json
 "RequestId":"69CD31EF-A412-42DD-8AD9-1201D******",
 "Message":"success",
 "Data":{
  "ConfigList":[
    "Content":"-javaagent:/home/admin/.opt/ArmsAgent/arms-bootstrap-1.7.0-SNAPSHOT.jar\-
Darms.licenseKey=1905328884798675@75360cd0b2715e0\-Darms.appId=2dfea044-479f-464a-b374-f14d328e7191\- Darms.agent.env=edas\-Darms.agent.args=\-Xms1g\-Xmx1g\-Xmn500m\-XX:MetaspaceSize=128m\-XX:MaxMetaspaceSize=256m\-XX:M axDirectMemorySize=256m\-XX:ReservedCodeCacheSize=64m\-XX:+HeapDumpOnOutOfMemoryError\- XX:HeapDumpPath=/home/admin/cop-broker\-Djava.awt.headless=true\-Djava.security.egd=file:/dev/./urandom\-Dfile.encodi ng=UTF-8\-Dproject.name=i-a4854351007a1e59f00\-Dahas.gateway.address=\-Dahas.license=\-Dahas.namespace=default\-Dahas .agw.type=1\-Dahas.acm.enable=false\-Dcsp.sentinel.app.type=1\-Dio.netty.allocator.type=unpooled\- XX:ErrorFile=/home/admin/cop-broker/csb-cop-broker-i-a4854351007a1e59f00-group-1-v1- 64f8997479q8pvf.hs_err.202410221118.log\-Djavax.net.ssl.trustStore=/usr/local/cloud/cacerts\- Djavax.net.ssl.trustStorePassword=changeit\-Dserver.tomcat.accesslog.encoding=UTF-8\- Dserver.tomcat.accesslog.prefix=csb-cop-broker-i-a4854351007a1e59f00-group-1-v1-64f8997479q8pvf\- Dserver.tomcat.accesslog.file-date-format=-yyyyMMdd\-Dserver.tomcat.accesslog.suffix=-access-json.log\-Dserver.tomcat .accesslog.directory=/home/admin/cop-broker\-Dserver.tomcat.accesslog.enabled=true\-Dserver.tomcat.accesslog.pattern= {\\\"x_forwarded_for\\\":\\\"%{X-Forwarded- For}i\\\",\\\"client_ip\\\":\\\"%h\\\",\\\"client_user\\\":\\\"%l\\\",\\\"authenticated\\\":\\\"%u\\\",\\\"request_time ":\\\"%{yyyy-MMdd'T'HH:mm:ss.SSSZ}t\\\",\\\"request_url\\\":\\\"%r\\\",\\\"http_code\\\":\\\"%s\\\",\\\"send_bytes\\\":\\\"%b\\\",\\\" ry_string\\\":\\\"%q\\\",\\\"http_referer\\\":\\\"%{Referer}i\\\",\\\"user_agent\\\":\\\"%{User- Agent}i\\\",\\\"request_time_ms\\\":\\\"%D\\\"}\-Dloader.path=/home/admin/cop-broker",
    "ConfigType":"jvmMachineProperties",
    "Name":"jvmMachineProperties"
```

`]` `},`

```json
 "Code":200
```

```xml
<RequestId>69CD31EF-A412-42DD-8AD9-1201D******</RequestId> <Data>
 <ConfigList>
  <Content>-javaagent:/home/admin/.opt/ArmsAgent/arms-bootstrap-1.7.0-SNAPSHOT.jar-
Darms.licenseKey=1***@75360cd0b2715e0-Darms.appId=2dfea044-479f-464a-b374-f14d328e7191- Darms.agent.env=edas-Darms.agent.args=-Xms1g-Xmx1g-Xmn500m-XX:MetaspaceSize=128m-XX:MaxMetaspaceSize=256m-XX:MaxDirec tMemorySize=256m-XX:ReservedCodeCacheSize=64m-XX:+HeapDumpOnOutOfMemoryError-XX:HeapDumpPath=/home/admin/cop-broker-D java.awt.headless=true-Djava.security.egd=file:/dev/./urandom-Dfile.encoding=UTF-8-Dproject.name=ia4854351007a1e59f00-Dahas.gateway.address=-Dahas.license=-Dahas.namespace=default-Dahas.agw.type=1- Dahas.acm.enable=false-Dcsp.sentinel.app.type=1-Dio.netty.allocator.type=unpooled-XX:ErrorFile=/home/admin/cop-broker /csb-cop-broker-i-a4854351007a1e59f00-group-1-v1-64f8997479q8pvf.hs_err.202410221118.log- Djavax.net.ssl.trustStore=/usr/local/cloud/cacerts-Djavax.net.ssl.trustStorePassword=changeit- Dserver.tomcat.accesslog.encoding=UTF-8-Dserver.tomcat.accesslog.prefix=csb-cop-broker-i-a4854351007a1e59f00-group-1v1-64f8997479q8pvf-Dserver.tomcat.accesslog.file-date-format=-yyyyMMdd-Dserver.tomcat.accesslog.suffix=-access-json.l og-Dserver.tomcat.accesslog.directory=/home/admin/cop-broker-Dserver.tomcat.accesslog.enabled=true- Dserver.tomcat.accesslog.pattern={\&quot;x_forwarded_for\&quot;:\&quot;%{X-Forwarded- For}i\&quot;,\&quot;client_ip\&quot;:\&quot;%h\&quot;,\&quot;client_user\&quot;:\&quot;%l\&quot;,\&quot;authenticated\& t;:\&quot;%u\&quot;,\&quot;request_time\&quot;:\&quot;%{yyyy-MMdd&#x27;T&#x27;HH:mm:ss.SSSZ}t\&quot;,\&quot;request_url\&quot;:\&quot;%r\&quot;,\&quot;http_code\&quot;:\&quot;%s\&quo \&quot;send_bytes\&quot;:\&quot;%b\&quot;,\&quot;query_string\&quot;:\&quot;%q\&quot;,\&quot;http_referer\&quot;:\&quot {Referer}i\&quot;,\&quot;user_agent\&quot;:\&quot;%{User- Agent}i\&quot;,\&quot;request_time_ms\&quot;:\&quot;%D\&quot;}-Dloader.path=/home/admin/cop-broker</Content>
  <ConfigType>jvmMachineProperties</ConfigType>
  <Name>jvmMachineProperties</Name>
 </ConfigList>
</Data>
```

###### 1.1.9.1.16 GetEffectiveSpringAppConfigInText

Retrieves the configuration of a Spring application.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/app/configExtractExportForPop HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The ID of the application. |
| EccId | String | Query | Yes | csb-cop-broker-i- a4854351007a1e59f00-group-1-v1- 64f899747****** | The ID of the pod. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9D899A2E-2721-4E03- BFD0-725ED3****** | The ID of the request. |
| Code | Integer | 200 | The status code. |
| Message | String | success | Additional information. |

| Service (EDAS) |   |   | rence |
|---|---|---|---|
| Data | String | ################ # name is server.ports,type is other local.server.port=80 local.management.port=8 108 ################ # name is gateway- properties,type is other spring.webflux.hiddenmeth od.filter.enabled=false ################ # name is jvmMachineProperties,type is jvmMachineProperties - javaagent:/home/admin/.o pt/ArmsAgent/arms- bootstrap-1.7.0- SNAPSHOT.jar - Darms.licenseKey=190532 8884798675@75360cd0b2 715e0 -Darms.appId=2dfea044- 479f-464a-b374- f14d328e7191 -Darms.agent.env=edas -Darms.agent.args= -Xms1g -Xmx1g -Xmn500m -XX:MetaspaceSize=128m - XX:MaxMetaspaceSize=25 6m - XX:MaxDirectMemorySize= 256m - XX:ReservedCodeCacheSiz e=64m - XX:+HeapDumpOnOutOfM emoryError - XX:HeapDumpPath=/home /admin/cop-broker -Djava.awt.headless=true - Djava.security.egd=file:/de v/./urandom -Dfile.encoding=UTF-8 -Dproject.name=i- a4854351007a1e59f00 -Dahas.gateway.address= -Dahas.license= - Dahas.namespace=default -Dahas.agw.type=1 -Dahas.acm.enable=false -Dcsp.sentinel.app.type=1 - Dio.netty.allocator.type=u npooled | The returned data. |

|   |   | - XX:ErrorFile=/home/admin/ cop-broker/csb-cop-broker- i-a4854351007a1e59f00- group-1-v1- 64f8997479q8pvf.hs err.2 _ 02410221118.log - Djavax.net.ssl.trustStore=/ usr/local/cloud/cacerts - Djavax.net.ssl.trustStorePa ssword=changeit - Dserver.tomcat.accesslog. encoding=UTF-8 - Dserver.tomcat.accesslog. prefix=csb-cop-broker-i- a4854351007a1e59f00- group-1-v1- 64f8997479q8pvf - Dserver.tomcat.accesslog.f ile-date-format=- yyyyMMdd - Dserver.tomcat.accesslog. suffix=-access-json.log - Dserver.tomcat.accesslog. directory=/home/admin/co p-broker - Dserver.tomcat.accesslog. enabled=true - Dserver.tomcat.accesslog. pattern= {\"x forwarded for\":\"% _ _ {X-Forwarded- For}i\",\"client ip\":\"%h\",\ _ "client user\":\"%l\",\"auth _ enticated\":\"%u\",\"reques t time\":\"%{yyyy-MM- _ dd'T'HH:mm:ss.SSSZ}t\",\" request url\":\"%r\",\"http _ _ code\":\"%s\",\"send bytes\ _ ":\"%b\",\"query string\":\" _ %q\",\"http referer\":\"% _ {Referer}i\",\"user agent\" _ :\"%{User- Agent}i\",\"request time _ _ ms\":\"%D\"} - Dloader.path=/home/admi n/cop-broker |   |
|---|---|---|---|

Sample request

```
GET /pop/v5/app/configExtractExportForPop HTTP/1.1 &AppId=2dfea044-479f-464a-b374-f14d32****** &EccId=csb-cop-broker-i-a4854351007a1e59f00-group-1-v1-64f899747****** &<Common request parameters>
```

Sample responses

```
 JSON
```

```json
 "RequestId":"9D899A2E-2721-4E03-BFD0-725ED3******",
 "Message":"success",
 "Data":"################# name is server.ports,type is
other\local.server.port=80\local.management.port=8108\\\################# name is gateway-properties,type is other\sp ring.webflux.hiddenmethod.filter.enabled=false\\\################# name is jvmMachineProperties,type is jvmMachinePro perties\-javaagent:/home/admin/.opt/ArmsAgent/arms-bootstrap-1.7.0-SNAPSHOT.jar\- Darms.licenseKey=1905328884798675@75360cd0b2715e0\-Darms.appId=2dfea044-479f-464a-b374-f14d328e7191\- Darms.agent.env=edas\-Darms.agent.args=\-Xms1g\-Xmx1g\-Xmn500m\-XX:MetaspaceSize=128m\-XX:MaxMetaspaceSize=256m\-XX:M axDirectMemorySize=256m\-XX:ReservedCodeCacheSize=64m\-XX:+HeapDumpOnOutOfMemoryError\- XX:HeapDumpPath=/home/admin/cop-broker\-Djava.awt.headless=true\-Djava.security.egd=file:/dev/./urandom\-Dfile.encodi ng=UTF-8\-Dproject.name=i-a4854351007a1e59f00\-Dahas.gateway.address=\-Dahas.license=\-Dahas.namespace=default\-Dahas .agw.type=1\-Dahas.acm.enable=false\-Dcsp.sentinel.app.type=1\-Dio.netty.allocator.type=unpooled\- XX:ErrorFile=/home/admin/cop-broker/csb-cop-broker-i-a4854351007a1e59f00-group-1-v1- 64f8997479q8pvf.hs_err.202410221118.log\-Djavax.net.ssl.trustStore=/usr/local/cloud/cacerts\- Djavax.net.ssl.trustStorePassword=changeit\-Dserver.tomcat.accesslog.encoding=UTF-8\- Dserver.tomcat.accesslog.prefix=csb-cop-broker-i-a4854351007a1e59f00-group-1-v1-64f8997479q8pvf\- Dserver.tomcat.accesslog.file-date-format=-yyyyMMdd\-Dserver.tomcat.accesslog.suffix=-access-json.log\-Dserver.tomcat .accesslog.directory=/home/admin/cop-broker\-Dserver.tomcat.accesslog.enabled=true\-Dserver.tomcat.accesslog.pattern= {\\\"x_forwarded_for\\\":\\\"%{X-Forwarded- For}i\\\",\\\"client_ip\\\":\\\"%h\\\",\\\"client_user\\\":\\\"%l\\\",\\\"authenticated\\\":\\\"%u\\\",\\\"request_time ":\\\"%{yyyy-MMdd'T'HH:mm:ss.SSSZ}t\\\",\\\"request_url\\\":\\\"%r\\\",\\\"http_code\\\":\\\"%s\\\",\\\"send_bytes\\\":\\\"%b\\\",\\\" ry_string\\\":\\\"%q\\\",\\\"http_referer\\\":\\\"%{Referer}i\\\",\\\"user_agent\\\":\\\"%{User- Agent}i\\\",\\\"request_time_ms\\\":\\\"%D\\\"}\-Dloader.path=/home/admin/cop-broker\\\",
 "Code":200
 XML
<RequestId>9D899A2E-2721-4E03-BFD0-725ED3******</RequestId> <Data>################# name is server.ports,type is otherlocal.server.port=80local.management.port=8108################# name is gateway-properties,type is otherspring.w ebflux.hiddenmethod.filter.enabled=false################# name is jvmMachineProperties,type is jvmMachineProperties-j avaagent:/home/admin/.opt/ArmsAgent/arms-bootstrap-1.7.0-SNAPSHOT.jar- Darms.licenseKey=1***@75360cd0b2715e0-Darms.appId=2dfea044-479f-464a-b374-f14d328e7191- Darms.agent.env=edas-Darms.agent.args=-Xms1g-Xmx1g-Xmn500m-XX:MetaspaceSize=128m-XX:MaxMetaspaceSize=256m-XX:MaxDirec tMemorySize=256m-XX:ReservedCodeCacheSize=64m-XX:+HeapDumpOnOutOfMemoryError-XX:HeapDumpPath=/home/admin/cop-broker-D java.awt.headless=true-Djava.security.egd=file:/dev/./urandom-Dfile.encoding=UTF-8-Dproject.name=ia4854351007a1e59f00-Dahas.gateway.address=-Dahas.license=-Dahas.namespace=default-Dahas.agw.type=1- Dahas.acm.enable=false-Dcsp.sentinel.app.type=1-Dio.netty.allocator.type=unpooled-XX:ErrorFile=/home/admin/cop-broker /csb-cop-broker-i-a4854351007a1e59f00-group-1-v1-64f8997479q8pvf.hs_err.202410221118.log- Djavax.net.ssl.trustStore=/usr/local/cloud/cacerts-Djavax.net.ssl.trustStorePassword=changeit- Dserver.tomcat.accesslog.encoding=UTF-8-Dserver.tomcat.accesslog.prefix=csb-cop-broker-i-a4854351007a1e59f00-group-1v1-64f8997479q8pvf-Dserver.tomcat.accesslog.file-date-format=-yyyyMMdd-Dserver.tomcat.accesslog.suffix=-access-json.l og-Dserver.tomcat.accesslog.directory=/home/admin/cop-broker-Dserver.tomcat.accesslog.enabled=true- Dserver.tomcat.accesslog.pattern={\&quot;x_forwarded_for\&quot;:\&quot;%{X-Forwarded- For}i\&quot;,\&quot;client_ip\&quot;:\&quot;%h\&quot;,\&quot;client_user\&quot;:\&quot;%l\&quot;,\&quot;authenticated\& t;:\&quot;%u\&quot;,\&quot;request_time\&quot;:\&quot;%{yyyy-MMdd&#x27;T&#x27;HH:mm:ss.SSSZ}t\&quot;,\&quot;request_url\&quot;:\&quot;%r\&quot;,\&quot;http_code\&quot;:\&quot;%s\&quo \&quot;send_bytes\&quot;:\&quot;%b\&quot;,\&quot;query_string\&quot;:\&quot;%q\&quot;,\&quot;http_referer\&quot;:\&quot {Referer}i\&quot;,\&quot;user_agent\&quot;:\&quot;%{User- Agent}i\&quot;,\&quot;request_time_ms\&quot;:\&quot;%D\&quot;}-Dloader.path=/home/admin/cop-broker</Data>
```

###### 1.1.9.1.17 ListRecentChangeOrder

Call the ListRecentChangeOrder operation to retrieve the change order history for an application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/change_order_list HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92-4413-****- ************ | The ID of the application. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The additional information that is returned. |
| RequestId | String | D16979DC-4D42- ************ | The ID of the request. |
| ChangeOrderList | Array |   | The list of change records. |
| -ChangeOrderId | String | 1074f3e2-e974-4a0e-****- ************ | The unique ID of the change process. |
| -UserId | String | 1432536**** | The ID of the user who created the change process. |
| -BatchType | String | Automatic | The execution mode for the next batch in a phased release. Automatic Manual |
| -BatchCount | Integer | 1 | The number of release batches. The value must be an integer from 1 to 5. |
| -AppId | String | 3616cdca-4f92-4413-****- ************ | The ID of the application. |
| -GroupId | String | 8123db90-880f-486f-****- ************ | The ID of the application group for which the change is made. |
| -Status | Integer | 2 | You can change the flow status. 0: Ready 1: In progress 2: Succeeded 3: Failed 6: Stopped 8: Pending manual confirmation. This status is returned for manual phased releases. 9: Pending automatic execution 10: Failed due to a system error |
| -CreateTime | String | 2019-11-13 14:23:46 | The time when the change order was created. |
| -FinishTime | String | 2019-11-13 14:24:02 | End time. |
| -CoType | String | Application Scale Out | The type of the change process. |
| -CreateUserId | String | edas test1@aliyun- _ test.com | The user who created the change order. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CoTypeCode | String | CoDeploy | Change the flow type: CoCreateApp: Create an application. CoStartApplication: Start an application. CoStopApplication: Stop an application. CoRestartApplication: Restart an application. CoDeleteApp: Delete an application. CoStart: Start an application instance. CoStop: Stop an application instance. CoRestart: Restart an instance. CoDeploy: Deploy an application. CoReset: Reset an application instance. CoRollback: Roll back an application. CoScaleIn: Scale in application instances. CoScaleOut: Scale out application instances. CoChangeGroup: Change the group of an application instance. CoUpdateContainer: Update the deployment package version of an application. CoBindSlb: Attach an SLB instance. CoBindECSSlb: Attach an SLB instance to an ECS instance. CoUnbindECSSlb: Detach an SLB instance from an ECS instance. CoUnbindSlb: Detach an SLB instance. CoModifySlb: Configure an SLB instance. CoModifyConfig: Modify the configuration of an application. CoClusterScaleOut: Scale out a cluster. CoRescaleApplicationVertically: Vertically scale an application. |
| -Source | String | pop | The source of the change. console: EDAS console pop: POP API or a tool |
| - ChangeOrderDescrip tion | String | Version: 2020-05-14 20:02:33 \| Package name: hsf-pandora-boot-provider- 1.0.jar \| Deployment target: all groups | The description of the change process. |
| Code | Integer | 200 | The status of the API call or a POP error code. |

Request example

```json
POST /pop/v5/changeorder/change_order_list HTTP/1.1 "AppId":"3616cdca-4f92-4413-****-************"
```

Sample success response

```json
 "Message":"success",
 "RequestId":"D16979DC-4D42-************",
 "ChangeOrderList":{
  "Status":2,
  "CreateTime":"2019-11-13 14:23:46",
  "ChangeOrderId":"1074f3e2-e974-4a0e-****-************",
  "CreateUserId":"e***@aliyun-test.com",
  "BatchType":"Automatic",
  "Source":"pop",
  "GroupId":"8123db90-880f-486f-****-************",
  "AppId":"3616cdca-4f92-4413-****-************",
  "FinishTime":"2019-11-13 14:24:02",
  "CoTypeCode":"CoDeploy",
  "ChangeOrderDescription":"Version: 2020-05-14 20:02:33 | Package name: hsf-pandora-boot-provider-1.0.jar | Deployme
nt target: all groups",
  "UserId":"1432536****",
  "CoType":"Application Scale Out",
  "BatchCount":1
```

`},`

```json
 "Code":200
```

###### 1.1.9.1.18 CreateCanaryRule

Creates a canary release rule.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/k8s/acs/app_canary_rule HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The ID of the application. |
| Type | String | Query | Yes | canary by content _ _ | Type: Content-based grayscale |
| RuleName | String | Query | Yes | test-rule | The name of the rule. |
| Rules | String | Query | No | {"http":{"rules": [{"percent":100,"conditionType":" content","path":"/","triggerPolicy": "OR","conditions": [{"strategy":"PARAM","key":"nam e","operator":"EQ","values": ["zhangsan"]}]}]},"dubbo": {"rules":[]},"servicemesh": {"desired":2,"rules":[]}} | The details of the rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The ID of the request. |
| Code | Integer | 200 | The status code of the API operation or a POP error code. |
| Message | String | message | Additional information. |

Sample request

```json
POST /pop/v5/k8s/acs/app_canary_rule HTTP/1.1 "AppId":"2dfea044-479f-464a-b374-f14d32******", "Type":"canary_by_content", "RuleName":"test-rule"
```

Sample success response

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Code":200
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message>
```

###### 1.1.9.1.19 ListCanaryRules

Queries the phased release rules for a specified application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
GET /pop/v5/k8s/acs/app_canary_rules HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The application ID. |
| Type | String | Query | Yes | canary by content _ _ | Type: Content-based canary release. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The request ID. |
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | message | Additional information. |
| Result | Struct | - | The returned result. |
| -RuleList | Array | - | The list of rules. |
| --RuleId | String | fb05f0e8-e707-4a66-8978- a84672****** | The rule ID. |

| Enterprise Distrib Service Developer | uted Application Guide·API refe |   | Enterprise Distributed Application Service (EDAS |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| --RuleName | String | test-rule | The rule name. |
| --Rules | String | {"http":{"rules": [{"percent":100,"condition Type":"content","path":"/"," triggerPolicy":"OR","conditi ons": [{"strategy":"PARAM","key" :"name","operator":"EQ","v alues": ["zhangsan"]}]}]},"dubbo" :{"rules": []},"servicemesh": {"desired":2,"rules":[]}} | The rule details. |
| --Type | String | canary by content _ _ | Type: Content-based canary release. |

Sample request

```
GET /pop/v5/k8s/acs/app_canary_rules HTTP/1.1 &AppId=2dfea044-479f-464a-b374-f14d32****** &Type=canary_by_content &Common request parameters
```

Sample response

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Code":200,
 "Result":{
  "RuleList":[
    "Type":"canary_by_content",
    "RuleId":"fb05f0e8-e707-4a66-8978-a84672******",
    "Rules":"{\"http\":{\"rules\":
[{\"percent\":100,\"conditionType\":\"content\",\"path\":\"/\",\"triggerPolicy\":\"OR\",\"conditions\":[{\"strategy\" :\"PARAM\",\"key\":\"name\",\"operator\":\"EQ\",\"values\":[\"zhangsan\"]}]}]},\"dubbo\":{\"rules\": []},\"servicemesh\":{\"desired\":2,\"rules\":[]}}",
    "RuleName":"test-rule"
```

`]`

```xml
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message> <Result>
 <RuleList>
  <Type>canary_by_content</Type>
  <RuleId>fb05f0e8-e707-4a66-8978-a84672******</RuleId>
  <Rules>{&quot;http&quot;:{&quot;rules&quot;:
[{&quot;percent&quot;:100,&quot;conditionType&quot;:&quot;content&quot;,&quot;path&quot;:&quot;/&quot;,&quot;triggerPol &quot;:&quot;OR&quot;,&quot;conditions&quot;: [{&quot;strategy&quot;:&quot;PARAM&quot;,&quot;key&quot;:&quot;name&quot;,&quot;operator&quot;:&quot;EQ&quot;,&quot;val &quot;:[&quot;zhangsan&quot;]}]}]},&quot;dubbo&quot;:{&quot;rules&quot;:[]},&quot;servicemesh&quot;: {&quot;desired&quot;:2,&quot;rules&quot;:[]}}</Rules>
  <RuleName>test-rule</RuleName>
 </RuleList>
</Result>
```

###### 1.1.9.1.20 UpdateCanaryRule

Updates the phased release rule for the specified application.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

```
PUT /pop/v5/k8s/acs/app_canary_rule HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The ID of the application. |
| RuleId | String | Query | Yes | 76f681af-67d4-4aef-b03e- 066b65****** | The ID of the rule. |
| RuleName | String | Query | Yes | test-rule | The name of the rule. |
| Rules | String | Query | No | {"http":{"rules": [{"percent":100,"conditionType":" content","path":"/","triggerPolicy": "OR","conditions": [{"strategy":"PARAM","key":"nam e","operator":"EQ","values": ["lisi"]}]}]},"dubbo":{"rules": []},"servicemesh": {"desired":2,"rules":[]}} | The information about the rule. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The ID of the request. |
| Code | Integer | 200 | The status code of the API call. This can be an HTTP status code or a POP error code. |
| Message | String | message | Additional information |

Sample request

```json
PUT /pop/v5/k8s/acs/app_canary_rule HTTP/1.1 "AppId":"2dfea044-479f-464a-b374-f14d32******", "RuleId":"76f681af-67d4-4aef-b03e-066b65******", "RuleName":"test-rule"
```

Sample successful response

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Code":200
```

```xml
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message>
```

###### 1.1.9.1.21 DeleteCanaryRule

Deletes the specified phased release rule for an application.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /pop/v5/k8s/acs/app_canary_rule HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The ID of the application. |
| RuleId | String | Query | Yes | 76f681af-67d4-4aef-b03e- 066b65****** | The ID of the rule. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The ID of the request. |
| Code | Integer | 200 | The status code of the request. |
| Message | String | message | Additional information. |
| Result | Boolean | true | The result of the request. |

Request example

```
DELETE /pop/v5/k8s/acs/app_canary_rule HTTP/1.1 &AppId=2dfea044-479f-464a-b374-f14d32****** &RuleId=76f681af-67d4-4aef-b03e-066b65****** &<Common request parameters>
```

Successful response example

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Code":200,
 "Result":true
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message> <Result>true</Result>
```

##### 1.1.9.2 K8s clusters

###### 1.1.9.2.1 BindK8sSlb

Binds a Server Load Balancer (SLB) instance to an application in a Container Service for Kubernetes cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/k8s/acs/k8s_slb_binding HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 5a166fbd-****-****- a286-781659d9**** | The ID of the application. |
| ClusterId | String | Query | Yes | 712082c3-f554-****- ****-a947b5cd**** | The ID of the cluster. |
| Port | String | Query | Yes | 80 | The frontend port. The value must be between 1 and 65535. |
| SlbProtocol | String | Query | Yes | TCP | The protocol of the SLB instance. Supported protocols: TCP, HTTP, and HTTPS. |
| TargetPort | String | Query | Yes | 8080 | The backend port, which is the service port of the application. The value must be between 1 and 65535. |
| Type | String | Query | Yes | internet | The network type of the SLB instance. internet: Internet-facing intranet: internal-facing |
| SlbId | String | Query | No | lb- 2ze1quax9t****iz82b jt | The ID of the SLB instance. If you do not specify this parameter, EDAS automatically purchases a new SLB instance. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | b4b37bde-a125-****-****- 741f7f4a9ae3 | The ID of the change process. |
| Code | Integer | 200 | The HTTP status code returned. |
| Message | String | success | Additional information |

Request example

```json
POST /pop/v5/k8s/acs/k8s_slb_binding HTTP/1.1
  "AppId": "5a166fbd-****-****-a286-781659d9f54c"
  "ClusterId": "712082c3-f554-****-****-a947b5cde6ee"
  "Port": "80"
  "SlbProtocol": "TCP"
  "TargetPort": "8080"
  "Type": "internet"
```

Response example

```json
<ChangeOrderId>b4b37bde-a125-****-****-741f7f4a9ae3</ChangeOrderId>
    "Message": "success",
    "ChangeOrderId": "b4b37bde-a125-****-****-741f7f4a9ae3",
    "Code": 200
```

###### 1.1.9.2.2 DeleteK8sApplication

Deletes an application from a Container Service for Kubernetes (K8s) cluster.

**Request header**

This operation uses common request headers and does not require any special request headers. For more information, see Common request parameters.

```
DELETE /pop/v5/k8s/acs/k8s_apps HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | dbac7e3c-****-49bc- b6de-ffc550018b45 | The ID of the application. Call the ListApplication operation to obtain the application ID. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 0a34531a-****-49dc-8e7f- 0cbbbfa12cf0 | The ID of the change process. <note>If the application has instances that are not offline or an SLB instance that is not detached, a change process is created to delete the application. Call GetChangeOrderInfo to check the progress of the deletion. The value of `Code` indicates whether the deletion was successful.</note> |
| Code | Integer | 200 | The status code. |
| Message | String | success | Additional information |

Request example

```json
DELETE /pop/v5/k8s/acs/k8s_apps HTTP/1.1
  "AppId": "dbac7e3c-****-49bc-b6de-ffc550018b45"
```

Successful response example `XML` format

```xml
<ChangeOrderId>0a34531a-****-49dc-8e7f-0cbbbfa12cf0</ChangeOrderId>
```

`JSON` format

```json
 "Message": "success",
 "ChangeOrderId": "0a34531a-****-49dc-8e7f-0cbbbfa12cf0",
 "Code": 200
```

###### 1.1.9.2.3 DeployK8sApplication

The DeployK8sApplication operation deploys an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes (ASK) cluster.

**Request header**

This operation uses common request headers and does not have any special request headers. For more information, see Common request parameters.

```
POST /pop/v5/k8s/acs/k8s_apps HTTP/1.1
```

| Name | Type | Locatio n | Required |   | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|
| AppId | String | Query | Yes |   | e83acea6-****-47e1- 96ae-c0e953772cdc |   | The ID of the application. You can call the ListApplication operation to obtain this ID. |   |   |
| PreStop | String | Query | No |   | {\"exec\": {\"command\": [\"ls\",\"/\"]}}" |   | The script to execute before stopping the container. Example format: {"tcpSocket": |   |   |
|   |   |   |   |   |   |   |   |   | {"tcpSocket": |
|   |   |   |   |   |   | \": mand\": | {"host":"", "port":8080}} |   |   |
| Envs | String | Query | No |   | [{"name":"x","value" |   | The environment variables for the deployment. The value must be a JSON array of objects. Example: [{"name":"x","value":"y"}, |   |   |
|   |   |   |   |   |   |   |   | [{"name":"x","value":"y"}, |   |
|   |   |   |   |   | :"y"}, |   | {"name":"x2","value":"y2"}] |   |   |
|   |   |   |   |   | {"name":"x2","value ":"y2"}] |   |   |   |   |
| ImageTag | String | Query | No |   | latest |   | The tag of the image. |   |   |
| BatchWaitTime | Integer | Query | No |   | 0 |   | The minimum interval between batches for a phased release of pods. |   |   |

| " |   |   |
|---|---|---|

| > Document Versi | on: 20260 | 828 |   |   | 83 |
|---|---|---|---|---|---|

| Enterprise Distribu | ted Applic | ation |   |   |   |
|---|---|---|---|---|---|
| Service Developer ence | Guide·API | refe |   |   | Enterprise Distributed Application Service (EDAS |

| Command |   | String |   | Query | No | ls |   | The startup command for the container. Note To clear this configuration, set the value to an empty string ( "" ). |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PostStart |   | String |   | Query | No | {\"exec\": {\"command\": [\"ls\",\"/\"]}}" |   | The script to execute after the container starts. Example format: {"exec": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | {"exec": |   |   |
|   |   |   |   |   |   |   | ": | {"command":["cat","/etc/group"]}} . |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {} |   |
|   |   |   |   |   |   | {"failureThreshold": 3,"initialDelaySecon ds": |   | The readiness probe for the container. If the probe fails, traffic from the Kubernetes service is not routed to the container. Example format: {"failureThreshold": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | {"failureThreshold": |   |   |   |
|   |   |   |   |   |   | 5,"successThreshold |   | 3,"initialDelaySeconds": |   |   |   |   |   |
|   |   |   |   |   |   | ": |   | 5,"successThreshold": |   |   |   |   |   |
|   |   |   |   |   |   | 1,"timeoutSeconds": |   | 1,"timeoutSeconds": 1,"httpGet": |   |   |   |   |   |
| Readiness |   | String |   | Query | No | 1,"httpGet": {"path": "/consumer","port": |   | {"path": "/consumer","port": |   |   |   |   |   |
|   |   |   |   |   |   | 8080,"scheme": |   | 8080,"scheme": "HTTP","httpHeaders": |   |   |   |   |   |
|   |   |   |   |   |   | "HTTP","httpHeaders |   | [{"name": "test","value": |   |   |   |   |   |
|   |   |   |   |   |   | ": [{"name": |   | "testvalue"}]}} |   |   |   |   |   |
|   |   |   |   |   |   | "test","value": "testvalue"}]}} |   |   |   |   |   |   |   |
| Liveness |   |   |   |   |   | {"failureThreshold": 3,"initialDelaySecon |   | The liveness probe for the container. Example format: {"failureThreshold": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | {"failureThreshold": |   |   |   |   |
|   |   |   |   |   |   | ds": |   | 3,"initialDelaySeconds": |   |   |   |   |   |
|   |   |   |   |   |   | 5,"successThreshold |   | 5,"successThreshold": |   |   |   |   |   |
|   |   | String |   | Query | No | ": |   | 1,"timeoutSeconds": 1,"tcpSocket": |   |   |   |   |   |
|   |   |   |   |   |   | 1,"timeoutSeconds": |   | {"host":"", "port":8080}} |   |   |   |   |   |
|   |   |   |   |   |   | 1,"tcpSocket": {"host":"", "port":8080}} |   |   |   |   |   |   |   |
| Args |   | String |   | Query | No | ["args1","args2"] |   | The arguments for the container startup command. The value must be a JSON array of strings. Example: ["arg1","arg2"] . To clear this configuration, set the value to an empty JSON array ( "[]" ). |   |   |   |   |   |
| Replicas |   | Integer |   | Query | No | 1 |   | The number of application instances. The minimum value is 0. |   |   |   |   |   |
| Image |   | String |   | Query | No | registry-vpc.cn- beijing.aliyuncs.com/ t****/app:v1 |   | The full URL of the image. This parameter overwrites the ImageTag parameter. |   |   |   |   |   |
| CpuLimit |   | Integer |   | Query | No | 1 |   | The CPU limit for the application instance during runtime. Unit: cores. A value of 0 means no limit. |   |   |   |   |   |
| MemoryLimit |   | Integer |   | Query | No | 0 |   | The memory limit for the application instance during runtime. Unit: MB. A value of 0 means no limit. |   |   |   |   |   |

| CpuRequest |   |   | Integer | Query |   |   | No | 0 |   | The CPU quota that the application instance requests during runtime. We recommend that you set this parameter. Unit: cores. A value of 0 means no limit. Note If you set this parameter, you must also set the CpuLimit parameter. The value of CpuRequest must be less than or equal to the value of CpuLimit. |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MemoryRequest |   |   | Integer | Query |   |   | No | 0 |   | The memory quota that the application instance requests during runtime. We recommend that you set this parameter. Unit: MB. A value of 0 means no request. Note If you set this parameter, you must also set the MemoryLimit parameter. The value of MemoryRequest must be less than or equal to the value of MemoryLimit. |   |   |   |
| NasId |   |   | String | Query |   |   | No | dfs23**** |   | The ID of the Apsara File Storage NAS (NAS) file system to mount. The NAS file system must be in the same region as the cluster. The NAS file system must have an available mount target quota, or its mount target must already be attached to a vSwitch in the VPC. If you do not set this parameter but the MountDescs parameter is set, a NAS file system is automatically purchased and mounted to a vSwitch in the VPC. |   |   |   |
| MountDescs |   |   | String | Query |   |   |   | [{"nasPath": "/k8s","mountPath": |   | The mount configuration, which is a serialized JSON string. Example: [{"nasPath": |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{"nasPath": |   |
|   |   |   |   |   |   |   |   |   | ath": mountPath": | "/k8s","mountPath": "/mnt"}, |   |   |   |
|   |   |   |   |   | uery |   | No | "/mnt"},{"nasPath": |   | {"nasPath": "/files","mountPath": |   |   |   |
|   |   |   |   |   |   |   |   | "/files","mountPath": |   | "/app/files"}] |   |   |   |
|   |   |   |   |   |   |   |   | "/app/files"}] |   |   |   |   |   |
| StorageType |   |   | String | Query |   |   | No | Performance |   | The storage class of the mounted application. Currently, only SSD is supported. |   |   |   |
| LocalVolume |   |   |   |   |   |   |   | [{"type":"","nodePat h":"/localfiles","mou |   | The configuration for mounting a host file to a container. Example: [{"type":"","nodePath":"/localfiles","m |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{"type":"","nodePath":"/localfiles","m |   |   |
|   |   |   |   |   |   |   |   | ntPath":"/app/files"}, |   | ountPath":"/app/files"}, |   |   |   |
|   |   |   | String | Query |   |   | No | {"type":"Directory"," |   | {"type":"Directory","nodePath":"/mnt","m |   |   |   |
|   |   |   |   |   |   |   |   | nodePath":"/mnt","m ountPath":"/app/stor |   | ountPath":"/app/storage"}] |   |   |   |
|   |   |   |   |   |   |   |   | age"}] |   |   |   |   |   |
| PackageUrl |   |   | String | Query |   |   | No | https://e***.oss-cn- beijing.aliyuncs.com/ s***-1.0-SNAPSHOT- spring-boot.jar |   | The URL of the deployment package. You must configure this parameter for applications deployed using a FatJar or WAR package. Note The Java or Python software development kit (SDK) for EDAS POP API must be version 2.44.0 or later. |   |   |   |

| PackageVersion |   |   | String | Query |   | No | 20200720 | The version number of the deployment package. This parameter is required for WAR and FatJar packages. You can define the meaning of the version number. Note The Java or Python SDK for EDAS POP API must be version 2.44.0 or later. |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| JDK |   |   | String | Query |   | No | Open JDK 8 | The version of the Java Development Kit (JDK) that the deployment package depends on. Supported versions are Open JDK 7 and Open JDK 8. This parameter is not supported for image-based deployments. |   |   |
| WebContainer |   |   | String | Query |   | No | apache-tomcat- 7.0.91 | The version of Tomcat that the deployment package depends on. This parameter is applicable to Spring Cloud and Dubbo applications deployed using a WAR package. This parameter is not supported for image- based deployments. |   |   |
| EdasContainerVersio n |   |   | String | Query |   | No | 3.5.9 | The version of the EDAS Container that the deployment package depends on. This parameter is applicable to HSF applications deployed using a WAR package. This parameter is not supported for image-based deployments. |   |   |
| UriEncoding |   |   | String | Query |   | No | GBK | The URI encoding scheme. Supported schemes are ISO-8859-1, GBK, GB2312, and UTF-8. Note If you do not set this parameter in the application configuration, the default Tomcat value is used. |   |   |
| UseBodyEncoding |   |   | Boolean | Query |   | No | false | Specifies whether to enable `useBodyEncodingForURI`. Note If you do not set this parameter in the application configuration, the default value `false` is used. |   |   |
|   |   |   |   |   |   |   |   | The phased release policy. Example 1: One grayscale instance, followed by two batches, automatic batching, and a 1-minute interval between batches. {"type":"GrayBatchUpdate","batchUpda |   |   |
|   |   |   |   |   |   |   |   |   | {"type":"GrayBatchUpdate","batchUpda |   |
|   |   |   |   |   |   |   |   | te": |   |   |
|   |   |   |   |   |   |   |   | {"batch":2,"releaseType":"auto","batch |   |   |
|   |   |   |   |   |   |   | {"type":"GrayBatchU | WaitTime":1},"grayUpdate": |   |   |
|   |   |   |   |   |   |   | pdate","batchUpdate | {"gray":1}} |   |   |
| UpdateStrategy |   |   | String | Query |   | No | ": {"batch":2,"releaseT ype":"auto","batchW aitTime":1},"grayUp date":{"gray":1}} |   |   |   |
|   |   |   |   |   |   |   |   |   | {"type":"GrayBatchUpdate","batchUpda |   |
|   |   |   |   |   |   |   |   | te": |   |   |
|   |   |   |   |   |   |   |   | {"batch":2,"releaseType":"manual"},"gr |   |   |
|   |   |   |   |   |   |   |   | ayUpdate":{"gray":1}} |   |   |
|   |   |   |   |   |   |   |   |   | {"type":"BatchUpdate","batchUpdate": |   |
|   |   |   |   |   |   |   |   | {"batch":2,"releaseType":"auto","batch |   |   |
|   |   |   |   |   |   |   |   | WaitTime":0}} |   |   |

| McpuRequest | Integer | Query | No | 4 | The minimum CPU resources required. Unit: millicores. A value of 0 means no limit. Note When you set this parameter, you must also set the CpuLimit parameter. The value of this parameter must be less than or equal to the value of CpuLimit. |
|---|---|---|---|---|---|
| McpuLimit | Integer | Query | No | 0 | The maximum CPU resources that can be used. Unit: millicores. A value of 0 means no limit. |
| VolumesStr | String | Query | No | test | The data volumes. |
| PackageVersionId | String | Query | No | 2bcc******** | The ID of the deployment package version. |
| ChangeOrderDesc | String | Query | No | Upgrade | The description of the change record. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | cd65b247-****-475b-ad4b- 7039040d625c | The ID of the change process. You can call the GetChangeOrderInfo operation to obtain this ID. |
| Code | Integer | 200 | The HTTP status code returned. |
| Message | String | success | Additional information |

Request example

```json
POST /pop/v5/k8s/acs/k8s_apps HTTP/1.1 "AppId": "e83acea6-****-47e1-96ae-c0e953772cdc"
```

Successful response example

```json
<ChangeOrderId>cd65b247-****-475b-ad4b-7039040d625c</ChangeOrderId>
    "Message": "success",
    "ChangeOrderId": "cd65b247-****-475b-ad4b-7039040d625c",
    "Code": 200
```

###### 1.1.9.2.4 GetK8sApplication

Retrieves the details of a Kubernetes application.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/changeorder/co_application HTTP/1.1
```

| Parameter | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 5a166fbd-****-4f98-a286- 781659d9**** | The ID of the application. You can call the ListApplication operation to obtain the ID. |
| From | String | Query | No | deploy | The source of the query. If you do not set this parameter, a standard query is performed. deploy: The query is initiated from the deployment page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| Message | String | success | The additional information. |
| RequestId | String | 89F78814-AB00-40E3- 90D2-025EC8****** | The request ID. |
| TraceId | String | 0a9514681729847189560 3045****** | The trace ID. |
| Application | Struct | - | The application information. |
| DeployGroups | Array | - | The deployment groups. |
| Components | Array | - | The components. |
| Type | String | JDK | The component type. |
| ComponentId | String | 8 | The component ID. |
| ComponentKey | String | Open JDK 8 | The component keyword. |
| CreateTime | Long | 1729660967920 | The creation time. |
| PackagePublicUrl | String | https://fileserver.edas.inter .***.shuguang.com//prod/d emo/SPRING CLOUD PROV _ _ IDER.jar | The URL of the deployment package. |
| LastUpdateTime | Long | 1729661480013 | The time of the last update. |

| UpdateTime | Long | 1729661480013 | The update time. |
|---|---|---|---|
| NameSpace | String | default | The namespace. |
| GroupType | Integer | 0 | The group type. |
| CsClusterId | String | c6887edebfccd4452a41b6 7219aec61fc | The ID of the Container Service cluster. |
| GroupName | String | DEFAULT GROUP _ _ | The group name. |
| DeploymentName | String | k8s-sc-provider-t1-group-1- v2 | The name of the deployment. |
| MemoryLimit | String | 300 | The memory limit. Unit: MB. |
| MemoryRequest | String | 500 | The requested memory size. Unit: MB. |
| PackageVersion | String | 2024-10-23 13:30:30 | The version number of the deployment package. This parameter is required for WAR and FatJar packages. You can define the meaning of the version number. |
| Selector | String | {\"matchLabels\":{\"edas- domain\":\"edas- admin\",\"edas.appid\":\"c5 e90f13-583e-4837-82dc- ab4d841afe08\",\"edas.co mponent\":\"app\",\"edas.c ontrolplane\":\"edas- oam\",\"edas.groupid\":\"d efaultGroup\",\"edas.oam.a cname\":\"k8s-sc-provider- t1\",\"edas.oam.componen tname\":\"k8s-sc-provider- t1-group-1\"}} | The selector. |
| VExtServerGroupId | String | 11 | The ID of the extension server group. |
| Strategy | String | {\"rollingUpdate\": {\"maxSurge\":\"25%\",\"m axUnavailable\":\"25%\"},\ "type\":\"RollingUpdate\"} | The update policy. |
| PackageVersionId | String | 9a4c3b2b0c0a5319f74f14 2f70e96bdb | The version ID. |
| ClusterName | String | test | The cluster name. |
| Env | String | [{"Name":"env- k1","Value":"env-v1"}] | The environment variables. |
| GroupId | String | dea9b0b803ffb63a41a4ea cf0efb6dd6 | The group ID. |
| AppVersionId | String | 08bfb0b803ffb6lkd3a4eacf 0efbas6f | The application version ID. |
| ClusterId | String | 52b86925-0ac3-47dc- bb1c-0691fef74b27 | The cluster ID. |

| AppId | String | c5e90f13-583e-4837-82dc- ab4d84****** | The application ID. |
|---|---|---|---|
| CpuLimit | String | 300 | The CPU limit. Unit: millicores. 1,000 millicores equals 1 vCPU. |
| CpuRequest | String | 500 | The requested CPU size. Unit: millicores. 1,000 millicores equals 1 vCPU. |
| Status | String | 0 | The status value. |
| PackageUrl | String | https://fileserver.edas.inter .***.shuguang.com//prod/d emo/SPRING CLOUD PROV _ _ IDER.jar | The URL of the deployment package. |
| BaseComponentMet aName | String | k8s-sc-provider-t1-group-1 | The component name. |
| Instances | Array | - | The application instances. |
| AppId | String | c5e90f13-583e-4837-82dc- ab4d84****** | The application ID. |
| AppState | Integer | 7 | The application status. |
| ContainerIp | String | 10.3.0.226 | The IP address of the container. |
| ContainerStatus | String | Running | The container status. |
| EccId | String | k8s-sc-provider-t1-group-1- v2-7675c86b9d-x4fct | The pod ID. |
| Expired | Boolean | false | Indicates whether the instance has expired. |
| GroupId | String | dea9b0b803ffb63a41a4ea cf0efb6dd6 | The group ID. |
| GroupName | String | DEFAULT GROUP _ _ | The group name. |
| GroupType | Integer | 0 | The group type. |
| Id | String | k8s-sc-provider-t1-group-1- v2-7675c86b9d-x4fct | The instance ID. |
| Online | Integer | 0 | The online status. |
| PackageVersion | String | 2024-10-23 13:30:30 | The version number. |
| PrivateIp | String | 172.16.0.120 | The IP address of the host. |
| Running | Boolean | false | Indicates whether the instance is running. |
| Status | Integer | 0 | The status. |

| Url | String | cr.registry.inter.env149.sh uguang.com/edas- 1905328884798675/k8s- sc-provider-t1:k8s-sc- provider-t1-1729661431 | The URL. |
|---|---|---|---|
| AppId | String | c5e90f13-583e-4837-82dc- ab4d84****** | The application ID. |
| ImageInfo | Struct | - | The image information. |
| ImageUrl | String | cr.registry.inter.env149.sh uguang.com/edas- 1905328884798675/k8s- sc-provider-t1:k8s-sc- provider-t1-1729661431 | The image URL. |
| RepoName | String | test-repo | The repository name. |
| RegionId | String | cn-wulan-env149-d01 | The region ID. |
| RepoId | String | -1 | The repository ID. |
| RepoNamespace | String | default | The repository namespace. |
| RepoOriginType | String | ALI HUB _ | The repository type. |
| Tag | String | v1 | The tag. |
| App | Struct | - | The application information. |
| CmdArgs | String | {"CmdArg":[]} | The command-line arguments. |
| EnvList | Array | - | The list of environment information. |
| Name | String | env-k1 | The key of the environment variable. |
| Value | String | env-v1 | The value of the environment variable. |
| Name | String | k8s-sc-provider-t1 | The application name. |
| CreateTime | Long | 1729660967919 | The creation time. |
| RegionId | String | cn-wulan-env149- d01:autoK8sNs | The ID of the microservices namespace. |
| SlbPort | Integer | 0 | The SLB port. |

| SlbInfo | String | [{\"addressType\":\"intrane t\",\"externalTrafficPolicy\": \"Local\",\"ip\":\"172.16.0.1 56\",\"name\":\"intranet- k8s-sc-provider- t1c5e90f\",\"portMappings\ ": [{\"loadBalancerProtocol\": \"TCP\",\"servicePort\": {\"port\":8080,\"protocol\": \"TCP\",\"targetPort\":8080 }}],\"serviceType\":\"Load Balancer\",\"slbId\":\"lb- z2nub1egt6358ceb2nbfq\" }] | The SLB information. |
|---|---|---|---|
| RequestMem | Long | 300 | The requested memory size. Unit: MB. |
| LimitMem | Long | 500 | The memory limit. Unit: MB. |
| LimitCpuM | Long | 500 | The CPU limit. |
| RequestCpuM | Long | 1000 | The requested CPU size. |
| UserId | String | ascm-org-1728884798547 | The user ID. |
| Memory | Long | 300 | The memory size. |
| Cpu | Long | 500 | The CPU size. |
| InstanceCount | Integer | 1 | The number of instances. |
| RunningInstanceCou nt | Integer | 1 | The number of running instances. |
| ApplicationType | String | FatJar | The application type. |
| Owner | String | ascm-org-1728884798547 | The owner. |
| K8sNamespace | String | default | The Kubernetes namespace. |
| Port | Integer | 0 | The port. |
| InstancesBeforeScali ng | Integer | 0 | The number of instances before scaling. |
| ClusterType | Integer | 5 | The type of the application cluster. Valid values: 2: ECS cluster 3: EDAS-provided Kubernetes cluster 5: Kubernetes cluster |
| BuildpackId | Long | 0 | The build ID. |
| BuildPackageId | Long | 0 | The build package ID. |
| Cmd | String | ls /home | The command to execute. |

| DeployType | String | Image | The deployment type. |
|---|---|---|---|
| EdasContainerVersio n | String | 18 | The EDAS container version. |
| BuildpackId | Integer | 0 | The build ID. |
| TomcatVersion | String | 8.5.63 | The Tomcat version. |
| InstancesBeforeScali ng | Integer | 0 | The number of instances before scaling. |
| AppId | String | c5e90f13-583e-4837-82dc- ab4d84****** | The application ID. |
| ApplicationName | String | k8s-sc-provider-t1 | The application name. |
| ClusterId | String | 52b86925-0ac3-47dc- bb1c-0691fe****** | The cluster ID. |
| ClusterName | String | test | The cluster name. |
| Instances | Integer | 1 | The number of instances. |
| CsClusterId | String | c6887edebfccd4452a41b6 7219a****** |   |
| ImagePullPolicy | String | IfNotPresent | The image pull policy. Always: Always pulls the latest version of the image from the image repository when a pod is created. IfNotPresent: Pulls the image from the image repository only if the image is not available on the node. Never: Never pulls the image from the image repository. Only uses the image that is available on the node. |
| LastChangeOrderId | String | 826795ec-6f7c-4e58-97f1- 279638****** | The ID of the last change order. |
| ServiceAccount | String | default | The name of the service account. |
| WorkloadStrategy | String | RollingUpdate | The update policy. RollingUpdate: rolling update. Recreate: recreate. |
| HostAliases | String | [{\"ip\":\"10.212.1.1\",\"hos tnames\":[\"master1\"]}] | The domain name alias. |
| DnsConfig | String | {\"nameservers\": [\"10.212.1.1\"],\"searches\ ": [\"my.dns.search.example\ ",\"my.dns.search.suffix\"],\ "options\": [{\"isNewAdd\":true,\"nam e\":\"ndots\",\"value\":\"2\" }]} | The DNS configuration. |

| DnsPolicy | String | ClusterFirstWithHostNet | The DNS policy. ClusterFirst (default): The pod inherits the DNS settings of the cluster. The DNS queries are handled by CoreDNS. None: The pod uses the DNS settings specified by DnsConfig. The DNS settings of the cluster and node are ignored. Default: The pod inherits the DNS settings of the node. ClusterFirstWithHostNet: This policy is used with hostNetwork enabled. |
|---|---|---|---|
| Labels | String | {\"label-k1\":\"label-v1\"} | You can set tags. |
| Annotations | String | {\"anno-k1\":\"anno-v1\"} | You can set annotations. |
| State | String | RUNNING | The status of the application instance. AGENT OFF: The agent is offline. _ STOPPED: The application is stopped. RUNNING: The application is running. |
| AppContainerSecurit yContext | String | {\"privileged\":false} | The security context of the application container. |
| PodSecurityContext | String | {\"fsGroup\":11111,\"runAs Group\":11111,\"runAsUser \":11111} | Privileged Pod Settings. |
| AliasName | String | testapp | The alias of the application. |
| MountArmsApm | Boolean | true |   |
| LatestVersion | Struct | - | The information about the latest deployment package. |
| PackageVersion | String | 2024-10-23 13:30:30 | The version number. |
| Url | String | https://fileserver.edas.inter .***.shuguang.com//prod/d emo/SPRING CLOUD PROV _ _ IDER.jar | The URL of the deployment package. |
| WarUrl | String | https://fileserver.edas.inter .***.shuguang.com//prod/d emo/SPRING CLOUD PROV _ _ IDER.jar | The URL of the deployment package. |
| Conf | Struct | - | The configuration information. |
| JarStartArgs | String | -Dfile.encoding=UTF-8 | The startup parameters for the JAR package. This parameter is deprecated. |
| JarStartOptions | String | -Xmx121m -Xms21m | The startup options for the JAR package. This parameter is deprecated. |
| K8sCmd | String | ls /root | The Kubernetes command. |
| K8sCmdArgs | String | -l | The Kubernetes parameters. |

| K8sLocalvolumeInfo | String | {\"localVolumeDOs\": [{\"name\":\"localvolume- 0\",\"nodePath\":\"/tmp/tes t\",\"mountPath\":\"/tmp/te st\",\"opsAuth\":0}]} | The local storage. |
|---|---|---|---|
| K8sNasInfo | String | [{"nasPath":"/mnt/","moun tPath":"/mnt/"}] | The NAS storage information. |
| K8sVolumeInfo | String | {\"configMountDescs\":\" [{\\\"mountPath\\\":\\\"/tmp /config\\\",\\\"name\\\":\\\"t est-demo- config\\\",\\\"type\\\":\\\"Co nfigMap\\\"}]\",\"hostPaths\ ":\" [{\\\"path\\\":\\\"/tmp/test\\\ ",\\\"mountPath\\\":\\\"/tmp/ test\\\",\\\"name\\\":\\\"local volume- 0\\\",\\\"type\\\":\\\"\\\"}]\",\ "emptyDirs\":\" []\",\"pvcMountDescs\":\" []\"} | The Kubernetes storage information. |
| Liveness | String | {"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"tcpSocket":{"host":"", "port":8080}} | The liveness probe for the Kubernetes container. |
| PostStart | String | {\"exec\":{\"command\": [\"ls\",\"/\"]}} | The post-start hook for the Kubernetes container. |
| PreStop | String | {\"exec\":{\"command\": [\"ls\",\"/\"]}} | The pre-stop hook for the Kubernetes container. |
| Readiness | String | {"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"httpGet": {"path": "/consumer","port": 8080,"scheme": "HTTP","httpHeaders": \ [{"name": "test","value": "testvalue"}\]}} | The readiness probe for the Kubernetes container. |
| RuntimeClassName | String | runc | The pod runtime class. This parameter applies only to clusters that use sandboxed containers. |
| DeployAcrossZones | String | true | Specifies whether to distribute application instances across multiple zones. true: Yes. Other values: No. |
| AhasEnabled | Boolean | false | Specifies whether to connect to AHAS. |
| DeployAcrossNodes | String | false | Specifies whether to distribute application instances across multiple nodes. true: Yes. Other values: No. |

| ApmBinderLogFileCo nfigs | String | [] | The APM log file configurations. |
|---|---|---|---|

| Affinity | String | {\"additionalProperties\": {},\"nodeAffinity\": {\"additionalProperties\": {},\"preferredDuringSched ulingIgnoredDuringExecuti on\": [{\"additionalProperties\": {},\"preference\": {\"additionalProperties\": {},\"matchExpressions\": [{\"additionalProperties\": {},\"key\":\"kubernetes.io/ os\",\"operator\":\"In\",\"val ues\": [\"linux\"]}],\"matchFields\" : []},\"weight\":5}],\"require dDuringSchedulingIgnored DuringExecution\": {\"additionalProperties\": {},\"nodeSelectorTerms\": [{\"additionalProperties\": {},\"matchExpressions\": [{\"additionalProperties\": {},\"key\":\"beta.kubernet es.io/arch\",\"operator\":\" NotIn\",\"values\": [\"arm64\",\"arm32\"]}],\" matchFields\": []}]}},\"podAffinity\": {\"additionalProperties\": {},\"preferredDuringSched ulingIgnoredDuringExecuti on\": [],\"requiredDuringScheduli ngIgnoredDuringExecution\ ":[]},\"podAntiAffinity\": {\"additionalProperties\": {},\"preferredDuringSched ulingIgnoredDuringExecuti on\": [],\"requiredDuringScheduli ngIgnoredDuringExecution\ ":[]}} | The pod affinity configuration. |
|---|---|---|---|

Sample request

```
GET /pop/v5/changeorder/co_application HTTP/1.1 &AppId=5a166fbd-****-4f98-a286-781659d9**** &<Common request parameters>
```

Sample responses

```json
 "Message":"success",
 "RequestId":"89F78814-AB00-40E3-90D2-025EC8******",
 "TraceId":"0a95146817298471895603045******",
 "Applcation":{
  "App":{
   "DeployType":"Image",
   "ServiceAccount":"default",
   "AppContainerSecurityContext":"{\\\"privileged\\\":false}",
   "Owner":"ascm-org-1728884798547",
   "LimitCpuM":500,
   "MountArmsApm":true,
   "Memory":300,
   "Port":0,
   "BuildpackId":0,
   "Cpu":500,
   "CsClusterId":"c6887edebfccd4452a41b67219a******",
   "Name":"k8s-sc-provider-t1",
   "K8sNamespace":"default",
   "SlbPort":0,
   "Annotations":"{\\\"anno-k1\\\":\\\"anno-v1\\\"}",
   "DnsConfig":"{\\\"nameservers\\\":[\\\"10.212.1.1\\\"],\\\"searches\\\":
[\\\"my.dns.search.example\\\",\\\"my.dns.search.suffix\\\"],\\\"options\\\": [{\\\"isNewAdd\\\":true,\\\"name\\\":\\\"ndots\\\",\\\"value\\\":\\\"2\\\"}]}",
   "AliasName":"testapp",
   "ClusterName":"test",
   "RequestCpuM":1000,
   "Cmd":"ls /home",
   "BuildPackageId":0,
   "RequestMem":300,
   "ApplicationName":"k8s-sc-provider-t1",
   "ClusterId":"52b86925-0ac3-47dc-bb1c-0691fe******",
   "PodSecurityContext":"{\\\"fsGroup\\\":11111,\\\"runAsGroup\\\":11111,\\\"runAsUser\\\":11111}",
   "CreateTime":1729660967919,
   "EnvList":[
     "Value":"env-v1",
     "Name":"env-k1"
```

`],`

```json
   "Labels":"{\\\"label-k1\\\":\\\"label-v1\\\"}",
   "ClusterType":5,
   "InstancesBeforeScaling":0,
   "SlbInfo":"
[{\\\"addressType\\\":\\\"intranet\\\",\\\"externalTrafficPolicy\\\":\\\"Local\\\",\\\"ip\\\":\\\"172.16.0.156\\\",\\\" e\\\":\\\"intranet-k8s-sc-provider-t1c5e90f\\\",\\\"portMappings\\\": [{\\\"loadBalancerProtocol\\\":\\\"TCP\\\",\\\"servicePort\\\": {\\\"port\\\":8080,\\\"protocol\\\":\\\"TCP\\\",\\\"targetPort\\\":8080}}],\\\"serviceType\\\":\\\"LoadBalancer\\\",\\\ bId\\\":\\\"lb-z2nub1egt6358ceb2nbfq\\\"}]",
   "Instances":1,
   "HostAliases":"[{\\\"ip\\\":\\\"10.212.1.1\\\",\\\"hostnames\\\":[\\\"master1\\\"]}]",
   "InstanceCount":1,
   "ApplicationType":"FatJar",
   "AppId":"c5e90f13-583e-4837-82dc-ab4d84******",
   "ImagePullPolicy":"IfNotPresent",
   "CmdArgs":"{\"CmdArg\":[]}",
   "EdasContainerVersion":"18",
   "UserId":"ascm-org-1728884798547",
   "DnsPolicy":"ClusterFirstWithHostNet",
   "State":"RUNNING",
   "LastChangeOrderId":"826795ec-6f7c-4e58-97f1-279638******",
   "RegionId":"cn-wulan-env149-d01:autoK8sNs",
   "TomcatVersion":"8.5.63",
"WorkloadStrategy":"RollingUpdate"
```

```json
   "WorkloadStrategy":"RollingUpdate",
   "RunningInstanceCount":1,
   "LimitMem":500
```

`},`

```json
  "DeployGroups":[
    "GroupName":"_DEFAULT_GROUP",
    "Components":[
      "Type":"JDK",
      "ComponentKey":"Open JDK 8",
      "ComponentId":"8"
```

`],`

```json
    "MemoryRequest":"500",
    "NameSpace":"default",
    "CsClusterId":"c6887edebfccd4452a41b67219aec61fc",
    "Env":"[{\"Name\":\"env-k1\",\"Value\":\"env-v1\"}]",
    "AppVersionId":"08bfb0b803ffb6lkd3a4eacf0efbas6f",
    "PackageVersion":"2024-10-23 13:30:30",
    "LastUpdateTime":1729661480013,
    "ClusterName":"test",
    "Selector":"{\\\"matchLabels\\\":{\\\"edas-domain\\\":\\\"edas-admin\\\",\\\"edas.appid\\\":\\\"c5e90f13-583e-483
7-82dc-ab4d841afe08\\\",\\\"edas.component\\\":\\\"app\\\",\\\"edas.controlplane\\\":\\\"edasoam\\\",\\\"edas.groupid\\\":\\\"defaultGroup\\\",\\\"edas.oam.acname\\\":\\\"k8s-sc-providert1\\\",\\\"edas.oam.componentname\\\":\\\"k8s-sc-provider-t1-group-1\\\"}} ",
    "Status":"0",
    "DeploymentName":"k8s-sc-provider-t1-group-1-v2",
    "CpuLimit":"300",
    "ClusterId":"52b86925-0ac3-47dc-bb1c-0691fef74b27",
    "CreateTime":1729660967920,
    "PackageVersionId":"9a4c3b2b0c0a5319f74f142f70e96bdb",
    "BaseComponentMetaName":"k8s-sc-provider-t1-group-1",
    "GroupId":"dea9b0b803ffb63a41a4eacf0efb6dd6",
    "MemoryLimit":"300",
    "GroupType":0,
    "AppId":"c5e90f13-583e-4837-82dc-ab4d84******",
    "VExtServerGroupId":"11",
    "UpdateTime":1729661480013,
    "PackageUrl":"https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar",
    "Strategy":"{\\\"rollingUpdate\\\":
{\\\"maxSurge\\\":\\\"25%\\\",\\\"maxUnavailable\\\":\\\"25%\\\"},\\\"type\\\":\\\"RollingUpdate\\\"}",
    "CpuRequest":"500",
    "PackagePublicUrl":"https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar"
```

`],`

```json
  "ImageInfo":{
   "RepoNamespace":"default",
   "RepoOriginType":"ALI_HUB",
   "RepoName":"test-repo",
   "ImageUrl":"cr.registry.inter.env149.shuguang.com/edas-1905328884798675/k8s-sc-provider-t1:k8s-sc-provider-t1-1729
661431",
   "RegionId":"cn-wulan-env149-d01",
   "Tag":"v1",
   "RepoId":"-1"
```

`},`

```json
  "AppId":"c5e90f13-583e-4837-82dc-ab4d84******",
  "LatestVersion":{
   "WarUrl":"https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar",
   "PackageVersion":"2024-10-23 13:30:30",
   "Url":"https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar"
```

`},`

```json
  "Instances":[
    "GroupName":"_DEFAULT_GROUP",
    "Status":0,
    "ContainerIp":"10.3.0.226",
    "Expired":false,
    "PackageVersion":"2024-10-23 13:30:30",
    "Url":"cr.registry.inter.env149.shuguang.com/edas-1905328884798675/k8s-sc-provider-t1:k8s-sc-provider-t1-17296614
31",
    "GroupId":"dea9b0b803ffb63a41a4eacf0efb6dd6",
```

```json
    "ContainerStatus":"Running",
    "AppId":"c5e90f13-583e-4837-82dc-ab4d84******",
    "GroupType":0,
    "PrivateIp":"172.16.0.120",
    "Running":false,
    "EccId":"k8s-sc-provider-t1-group-1-v2-7675c86b9d-x4fct",
    "Id":"k8s-sc-provider-t1-group-1-v2-7675c86b9d-x4fct",
    "AppState":7,
    "Online":0
```

`],`

```json
  "Conf":{
   "Liveness":"{\"failureThreshold\": 3,\"initialDelaySeconds\": 5,\"successThreshold\": 1,\"timeoutSeconds\": 1,\"tc
pSocket\":{\"host\":\"\", \"port\":8080}}",
   "PostStart":"{\\\"exec\\\":{\\\"command\\\":[\\\"ls\\\",\\\"/\\\"]}}",
   "DeployAcrossZones":"true",
   "JarStartOptions":"-Xmx121m -Xms21m",
   "K8sLocalvolumeInfo":"{\\\"localVolumeDOs\\\":[{\\\"name\\\":\\\"localvolume-
0\\\",\\\"nodePath\\\":\\\"/tmp/test\\\",\\\"mountPath\\\":\\\"/tmp/test\\\",\\\"opsAuth\\\":0}]}",
   "AhasEnabled":false,
   "K8sNasInfo":"[{\"nasPath\":\"/mnt/\",\"mountPath\":\"/mnt/\"}]",
   "ApmBinderLogFileConfigs":"[]",
   "JarStartArgs":"-Dfile.encoding=UTF-8",
   "K8sCmd":"ls /root",
   "K8sVolumeInfo":"{\\\"configMountDescs\\\":\\\"
[{\\\\\\\"mountPath\\\\\\\":\\\\\\\"/tmp/config\\\\\\\",\\\\\\\"name\\\\\\\":\\\\\\\"test-democonfig\\\\\\\",\\\\\\\"type\\\\\\\":\\\\\\\"ConfigMap\\\\\\\"}]\\\",\\\"hostPaths\\\":\\\" [{\\\\\\\"path\\\\\\\":\\\\\\\"/tmp/test\\\\\\\",\\\\\\\"mountPath\\\\\\\":\\\\\\\"/tmp/test\\\\\\\",\\\\\\\"name\\\\\\ \\\\\\\"localvolume-0\\\\\\\",\\\\\\\"type\\\\\\\":\\\\\\\"\\\\\\\"}]\\\",\\\"emptyDirs\\\":\\\" []\\\",\\\"pvcMountDescs\\\":\\\"[]\\\"}",
   "K8sCmdArgs":"-l",
   "PreStop":"{\\\"exec\\\":{\\\"command\\\":[\\\"ls\\\",\\\"/\\\"]}}",
   "Readiness":"{\"failureThreshold\": 3,\"initialDelaySeconds\": 5,\"successThreshold\": 1,\"timeoutSeconds\": 1,\"h
ttpGet\": {\"path\": \"/consumer\",\"port\": 8080,\"scheme\": \"HTTP\",\"httpHeaders\": \\[{\"name\": \"test\",\"value\": \"testvalue\"}\\]}}",
   "DeployAcrossNodes":"false",
   "RuntimeClassName":"runc",
   "Affinity":"{\\\"additionalProperties\\\":{},\\\"nodeAffinity\\\":{\\\"additionalProperties\\\":
{},\\\"preferredDuringSchedulingIgnoredDuringExecution\\\":[{\\\"additionalProperties\\\":{},\\\"preference\\\":{\\\" additionalProperties\\\":{},\\\"matchExpressions\\\":[{\\\"additionalProperties\\\": {},\\\"key\\\":\\\"kubernetes.io/os\\\",\\\"operator\\\":\\\"In\\\",\\\"values\\\": [\\\"linux\\\"]}],\\\"matchFields\\\":[]},\\\"weight\\\":5}],\\\"requiredDuringSchedulingIgnoredDuringExecution\\\":{ \\\"additionalProperties\\\":{},\\\"nodeSelectorTerms\\\":[{\\\"additionalProperties\\\":{},\\\"matchExpressions\\\": [{\\\"additionalProperties\\\": {},\\\"key\\\":\\\"beta.kubernetes.io/arch\\\",\\\"operator\\\":\\\"NotIn\\\",\\\"values\\\": [\\\"arm64\\\",\\\"arm32\\\"]}],\\\"matchFields\\\":[]}]}},\\\"podAffinity\\\":{\\\"additionalProperties\\\":{},\\\"p referredDuringSchedulingIgnoredDuringExecution\\\":[],\\\"requiredDuringSchedulingIgnoredDuringExecution\\\":[]},\\\" podAntiAffinity\\\":{\\\"additionalProperties\\\":{},\\\"preferredDuringSchedulingIgnoredDuringExecution\\\":[],\\\"r equiredDuringSchedulingIgnoredDuringExecution\\\":[]}}"
```

`},`

```json
 "Code":200
<RequestId>89F78814-AB00-40E3-90D2-025EC8******</RequestId> <TraceId>0a95146817298471895603045******</TraceId> <Applcation>
 <App>
  <DeployType>Image</DeployType>
  <ServiceAccount>default</ServiceAccount>
  <AppContainerSecurityContext>{\&quot;privileged\&quot;:false}</AppContainerSecurityContext>
  <Owner>ascm-org-1728884798547</Owner>
  <LimitCpuM>500</LimitCpuM>
  <MountArmsApm>true</MountArmsApm>
  <Memory>300</Memory>
  <Port>0</Port>
  <BuildpackId>0</BuildpackId>
  <Cpu>500</Cpu>
CCl
```

`d`

```
6887dbf d445241b67219******/CCl
```

`d`

```xml
  <CsClusterId>c6887edebfccd4452a41b67219a******</CsClusterId>
  <Name>k8s-sc-provider-t1</Name>
  <K8sNamespace>default</K8sNamespace>
  <SlbPort>0</SlbPort>
  <Annotations>{\&quot;anno-k1\&quot;:\&quot;anno-v1\&quot;}</Annotations>
  <DnsConfig>{\&quot;nameservers\&quot;:[\&quot;10.212.1.1\&quot;],\&quot;searches\&quot;:
[\&quot;my.dns.search.example\&quot;,\&quot;my.dns.search.suffix\&quot;],\&quot;options\&quot;: [{\&quot;isNewAdd\&quot;:true,\&quot;name\&quot;:\&quot;ndots\&quot;,\&quot;value\&quot;:\&quot;2\&quot;}]}</DnsConfi
```

`g>`

```xml
  <AliasName>testapp</AliasName>
  <ClusterName>test</ClusterName>
  <RequestCpuM>1000</RequestCpuM>
  <Cmd>ls /home</Cmd>
  <BuildPackageId>0</BuildPackageId>
  <RequestMem>300</RequestMem>
  <ApplicationName>k8s-sc-provider-t1</ApplicationName>
  <ClusterId>52b86925-0ac3-47dc-bb1c-0691fe******</ClusterId>
  <PodSecurityContext>{\&quot;fsGroup\&quot;:11111,\&quot;runAsGroup\&quot;:11111,\&quot;runAsUser\&quot;:11111}</Pod
SecurityContext>
  <CreateTime>1729660967919</CreateTime>
  <EnvList>
   <Value>env-v1</Value>
   <Name>env-k1</Name>
  </EnvList>
  <Labels>{\&quot;label-k1\&quot;:\&quot;label-v1\&quot;}</Labels>
  <ClusterType>5</ClusterType>
  <InstancesBeforeScaling>0</InstancesBeforeScaling>
  <SlbInfo>
[{\&quot;addressType\&quot;:\&quot;intranet\&quot;,\&quot;externalTrafficPolicy\&quot;:\&quot;Local\&quot;,\&quot;ip\&q ;:\&quot;172.16.0.156\&quot;,\&quot;name\&quot;:\&quot;intranet-k8s-sc-providert1c5e90f\&quot;,\&quot;portMappings\&quot;: [{\&quot;loadBalancerProtocol\&quot;:\&quot;TCP\&quot;,\&quot;servicePort\&quot;: {\&quot;port\&quot;:8080,\&quot;protocol\&quot;:\&quot;TCP\&quot;,\&quot;targetPort\&quot;:8080}}],\&quot;serviceType\& t;:\&quot;LoadBalancer\&quot;,\&quot;slbId\&quot;:\&quot;lb-z2nub1egt6358ceb2nbfq\&quot;}]</SlbInfo>
  <Instances>1</Instances>
  <HostAliases>[{\&quot;ip\&quot;:\&quot;10.212.1.1\&quot;,\&quot;hostnames\&quot;:[\&quot;master1\&quot;]}]</HostAli
ases>
  <InstanceCount>1</InstanceCount>
  <ApplicationType>FatJar</ApplicationType>
  <AppId>c5e90f13-583e-4837-82dc-ab4d84******</AppId>
  <ImagePullPolicy>IfNotPresent</ImagePullPolicy>
  <CmdArgs>{&quot;CmdArg&quot;:[]}</CmdArgs>
  <EdasContainerVersion>18</EdasContainerVersion>
  <UserId>ascm-org-1728884798547</UserId>
  <DnsPolicy>ClusterFirstWithHostNet</DnsPolicy>
  <State>RUNNING</State>
  <LastChangeOrderId>826795ec-6f7c-4e58-97f1-279638******</LastChangeOrderId>
  <RegionId>cn-wulan-env149-d01:autoK8sNs</RegionId>
  <TomcatVersion>8.5.63</TomcatVersion>
  <WorkloadStrategy>RollingUpdate</WorkloadStrategy>
  <RunningInstanceCount>1</RunningInstanceCount>
  <LimitMem>500</LimitMem>
 </App>
 <DeployGroups>
  <GroupName>_DEFAULT_GROUP</GroupName>
  <Components>
   <Type>JDK</Type>
   <ComponentKey>Open JDK 8</ComponentKey>
   <ComponentId>8</ComponentId>
  </Components>
  <MemoryRequest>500</MemoryRequest>
  <NameSpace>default</NameSpace>
  <CsClusterId>c6887edebfccd4452a41b67219aec61fc</CsClusterId>
  <Env>[{&quot;Name&quot;:&quot;env-k1&quot;,&quot;Value&quot;:&quot;env-v1&quot;}]</Env>
  <AppVersionId>08bfb0b803ffb6lkd3a4eacf0efbas6f</AppVersionId>
  <PackageVersion>2024-10-23 13:30:30</PackageVersion>
  <LastUpdateTime>1729661480013</LastUpdateTime>
  <ClusterName>test</ClusterName>
  <Selector>{\&quot;matchLabels\&quot;:{\&quot;edas-domain\&quot;:\&quot;edas-
admin\&quot;,\&quot;edas.appid\&quot;:\&quot;c5e90f13-583e-4837-82dcab4d841afe08\&quot;,\&quot;edas.component\&quot;:\&quot;app\&quot;,\&quot;edas.controlplane\&quot;:\&quot;edas-oam\&q uot;,\&quot;edas.groupid\&quot;:\&quot;defaultGroup\&quot;,\&quot;edas.oam.acname\&quot;:\&quot;k8s-sc-provider-t1\&q
```

```xml
uot;,\&quot;edas.oam.componentname\&quot;:\&quot;k8s-sc-provider-t1-group-1\&quot;}} </Selector>
  <Status>0</Status>
  <DeploymentName>k8s-sc-provider-t1-group-1-v2</DeploymentName>
  <CpuLimit>300</CpuLimit>
  <ClusterId>52b86925-0ac3-47dc-bb1c-0691fef74b27</ClusterId>
  <CreateTime>1729660967920</CreateTime>
  <PackageVersionId>9a4c3b2b0c0a5319f74f142f70e96bdb</PackageVersionId>
  <BaseComponentMetaName>k8s-sc-provider-t1-group-1</BaseComponentMetaName>
  <GroupId>dea9b0b803ffb63a41a4eacf0efb6dd6</GroupId>
  <MemoryLimit>300</MemoryLimit>
  <GroupType>0</GroupType>
  <AppId>c5e90f13-583e-4837-82dc-ab4d84******</AppId>
  <VExtServerGroupId>11</VExtServerGroupId>
  <UpdateTime>1729661480013</UpdateTime>
  <PackageUrl>https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar</PackageUrl>
  <Strategy>{\&quot;rollingUpdate\&quot;:
{\&quot;maxSurge\&quot;:\&quot;25%\&quot;,\&quot;maxUnavailable\&quot;:\&quot;25%\&quot;},\&quot;type\&quot;:\&quot;Rol gUpdate\&quot;}</Strategy>
  <CpuRequest>500</CpuRequest>
<PackagePublicUrl>https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar</PackagePublicUrl
 </DeployGroups>
 <ImageInfo>
  <RepoNamespace>default</RepoNamespace>
  <RepoOriginType>ALI_HUB</RepoOriginType>
  <RepoName>test-repo</RepoName>
  <ImageUrl>cr.registry.inter.env149.shuguang.com/edas-1905328884798675/k8s-sc-provider-t1:k8s-sc-provider-t1-1729661
431</ImageUrl>
  <RegionId>cn-wulan-env149-d01</RegionId>
  <Tag>v1</Tag>
  <RepoId>-1</RepoId>
 </ImageInfo>
 <AppId>c5e90f13-583e-4837-82dc-ab4d84******</AppId>
 <LatestVersion>
  <WarUrl>https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar</WarUrl>
  <PackageVersion>2024-10-23 13:30:30</PackageVersion>
  <Url>https://fileserver.edas.inter.***.shuguang.com//prod/demo/SPRING_CLOUD_PROVIDER.jar</Url>
 </LatestVersion>
 <Instances>
  <GroupName>_DEFAULT_GROUP</GroupName>
  <Status>0</Status>
  <ContainerIp>10.3.0.226</ContainerIp>
  <Expired>false</Expired>
  <PackageVersion>2024-10-23 13:30:30</PackageVersion>
  <Url>cr.registry.inter.env149.shuguang.com/edas-1905328884798675/k8s-sc-provider-t1:k8s-sc-provider-t1-1729661431</
Url>
  <GroupId>dea9b0b803ffb63a41a4eacf0efb6dd6</GroupId>
  <ContainerStatus>Running</ContainerStatus>
  <AppId>c5e90f13-583e-4837-82dc-ab4d84******</AppId>
  <GroupType>0</GroupType>
  <PrivateIp>172.16.0.120</PrivateIp>
  <Running>false</Running>
  <EccId>k8s-sc-provider-t1-group-1-v2-7675c86b9d-x4fct</EccId>
  <Id>k8s-sc-provider-t1-group-1-v2-7675c86b9d-x4fct</Id>
  <AppState>7</AppState>
  <Online>0</Online>
 </Instances>
 <Conf>
  <Liveness>{&quot;failureThreshold&quot;: 3,&quot;initialDelaySeconds&quot;: 5,&quot;successThreshold&quot;: 1,&quot
;timeoutSeconds&quot;: 1,&quot;tcpSocket&quot;:{&quot;host&quot;:&quot;&quot;, &quot;port&quot;:8080}}</Liveness>
  <PostStart>{\&quot;exec\&quot;:{\&quot;command\&quot;:[\&quot;ls\&quot;,\&quot;/\&quot;]}}</PostStart>
  <DeployAcrossZones>true</DeployAcrossZones>
  <JarStartOptions>-Xmx121m -Xms21m</JarStartOptions>
  <K8sLocalvolumeInfo>{\&quot;localVolumeDOs\&quot;:[{\&quot;name\&quot;:\&quot;localvolume-
0\&quot;,\&quot;nodePath\&quot;:\&quot;/tmp/test\&quot;,\&quot;mountPath\&quot;:\&quot;/tmp/test\&quot;,\&quot;opsAuth\ ot;:0}]}</K8sLocalvolumeInfo>
  <AhasEnabled>false</AhasEnabled>
  <K8sNasInfo>[{&quot;nasPath&quot;:&quot;/mnt/&quot;,&quot;mountPath&quot;:&quot;/mnt/&quot;}]</K8sNasInfo>
  <ApmBinderLogFileConfigs>[]</ApmBinderLogFileConfigs>
  <JarStartArgs>-Dfile.encoding=UTF-8</JarStartArgs>
<K8sCmd>ls/root</K8sCmd>
```

```xml
  <K8sCmd>ls /root</K8sCmd>
  <K8sVolumeInfo>{\&quot;configMountDescs\&quot;:\&quot;
[{\\\&quot;mountPath\\\&quot;:\\\&quot;/tmp/config\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;test-demo-config\\\&quot; ,\\\&quot;type\\\&quot;:\\\&quot;ConfigMap\\\&quot;}]\&quot;,\&quot;hostPaths\&quot;:\&quot; [{\\\&quot;path\\\&quot;:\\\&quot;/tmp/test\\\&quot;,\\\&quot;mountPath\\\&quot;:\\\&quot;/tmp/test\\\&quot;,\\\&quot;n \\\&quot;:\\\&quot;localvolume- 0\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;\\\&quot;}]\&quot;,\&quot;emptyDirs\&quot;:\&quot; []\&quot;,\&quot;pvcMountDescs\&quot;:\&quot;[]\&quot;}</K8sVolumeInfo>
  <K8sCmdArgs>-l</K8sCmdArgs>
  <PreStop>{\&quot;exec\&quot;:{\&quot;command\&quot;:[\&quot;ls\&quot;,\&quot;/\&quot;]}}</PreStop>
  <Readiness>{&quot;failureThreshold&quot;: 3,&quot;initialDelaySeconds&quot;: 5,&quot;successThreshold&quot;: 1,&quo
t;timeoutSeconds&quot;: 1,&quot;httpGet&quot;: {&quot;path&quot;: &quot;/consumer&quot;,&quot;port&quot;: 8080,&quot; scheme&quot;: &quot;HTTP&quot;,&quot;httpHeaders&quot;: \[{&quot;name&quot;: &quot;test&quot;,&quot;value&quot;: &quo t;testvalue&quot;}\]}}</Readiness>
  <DeployAcrossNodes>false</DeployAcrossNodes>
  <RuntimeClassName>runc</RuntimeClassName>
  <Affinity>{\&quot;additionalProperties\&quot;:{},\&quot;nodeAffinity\&quot;:{\&quot;additionalProperties\&quot;:{},
\&quot;preferredDuringSchedulingIgnoredDuringExecution\&quot;:[{\&quot;additionalProperties\&quot;: {},\&quot;preference\&quot;:{\&quot;additionalProperties\&quot;:{},\&quot;matchExpressions\&quot;: [{\&quot;additionalProperties\&quot;: {},\&quot;key\&quot;:\&quot;kubernetes.io/os\&quot;,\&quot;operator\&quot;:\&quot;In\&quot;,\&quot;values\&quot;:[\&q uot;linux\&quot;]}],\&quot;matchFields\&quot;: []},\&quot;weight\&quot;:5}],\&quot;requiredDuringSchedulingIgnoredDuringExecution\&quot;: {\&quot;additionalProperties\&quot;:{},\&quot;nodeSelectorTerms\&quot;:[{\&quot;additionalProperties\&quot;:{},\&quot ;matchExpressions\&quot;:[{\&quot;additionalProperties\&quot;: {},\&quot;key\&quot;:\&quot;beta.kubernetes.io/arch\&quot;,\&quot;operator\&quot;:\&quot;NotIn\&quot;,\&quot;values\&qu :[\&quot;arm64\&quot;,\&quot;arm32\&quot;]}],\&quot;matchFields\&quot;:[]}]}},\&quot;podAffinity\&quot;:{\&quot;addit ionalProperties\&quot;:{},\&quot;preferredDuringSchedulingIgnoredDuringExecution\&quot;: [],\&quot;requiredDuringSchedulingIgnoredDuringExecution\&quot;:[]},\&quot;podAntiAffinity\&quot;: {\&quot;additionalProperties\&quot;:{},\&quot;preferredDuringSchedulingIgnoredDuringExecution\&quot;: [],\&quot;requiredDuringSchedulingIgnoredDuringExecution\&quot;:[]}}</Affinity>
 </Conf>
</Applcation>
```

###### 1.1.9.2.5 InsertK8sApplication

You can call the InsertK8sApplication operation to create an application in a Container Service K8s cluster or a Serverless K8s cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/k8s/acs/create_k8s_app HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppName | String | Query | Yes | doc-test | The name of the application. The name must start with a letter and can contain digits, letters, and hyphens (-). The name can be up to 36 characters long. |
| ClusterId | String | Query | Yes | c9cd**** | The ID of the cluster. Call the ListCluster operation to obtain the cluster ID. |
| ImageUrl | String | Query | No | registry.cn- beijing.aliyuncs.com/ **** test/****- _ cons****:1.0 | The address of the image. This parameter is required when you set PackageType to Image . |
| logicalRegionId | String | Query | No | cn-hangzhou:doc | The ID of the microservices namespace. |

| ApplicationDescriptio n | String | Query | No | production- environment- application |   | The description of the application. |   |   |
|---|---|---|---|---|---|---|---|---|
| RepoId | String | Query | No | ced******** |   | The ID of the image repository. |   |   |
| Replicas | Integer | Query | No | 4 |   | The number of application instances. |   |   |
| LimitCpu | Integer | Query | No | 4 |   | The CPU limit for each application instance. Unit: cores. |   |   |
| LimitMem | Integer | Query | No | 2 |   | The memory limit for each application instance. Unit: MB. |   |   |
| RequestsCpu | Integer | Query | No | 0 |   | The number of CPU cores requested for each application instance. Unit: cores. A value of 0 indicates no limit. |   |   |
| RequestsMem | Integer | Query | No | 0 |   | The amount of memory requested for each application instance. Unit: MB. A value of 0 indicates no limit. |   |   |
| Command | String | Query | No | ls |   | The command to run. If you specify this parameter, the command overrides the startup command in the image. |   |   |
| CommandArgs | String | Query | No | -lh |   | The arguments for the command. The arguments must be a JSON array string. Example: [{"argument":"-c"}, |   |   |
|   |   |   |   |   |   |   | [{"argument":"-c"}, |   |
|   |   |   |   |   |   | {"argument":"test"}] |   |   |
| IntranetSlbId | String | Query | No | ae93******** |   | The ID of the internal-facing Server Load Balancer (SLB) instance. If you do not specify this parameter, EDAS automatically purchases a new SLB instance. |   |   |
| IntranetSlbProtocol | String | Query | No | TCP |   | The protocol for the internal-facing SLB instance. Valid values: TCP, HTTP, and HTTPS. |   |   |
| IntranetSlbPort | Integer | Query | No | 80 |   | The frontend port of the internal-facing SLB instance. The value must be in the range of 1 to 65535. |   |   |
| IntranetTargetPort | Integer | Query | No | 80 |   | The backend port of the internal-facing SLB instance. This port is also the service port of the application. The value must be in the range of 1 to 65535. |   |   |
| InternetSlbId | String | Query | No | a3d4******** |   | The ID of the Internet-facing SLB instance. If you do not specify this parameter, EDAS automatically purchases a new SLB instance. |   |   |
| InternetSlbProtocol | String | Query | No | TCP |   | The protocol for the Internet-facing SLB instance. Valid values: TCP, HTTP, and HTTPS. |   |   |
| InternetSlbPort | Integer | Query | No | 80 |   | The frontend port of the Internet-facing SLB instance. The value must be in the range of 1 to 65535. |   |   |
| InternetTargetPort | Integer | Query | No | 8080 |   | The backend port of the Internet-facing SLB instance. This port is also the service port of the application. The value must be in the range of 1 to 65535. |   |   |

| Envs |   | String |   | Query | No |   |   | \ [{"name":"x","value" |   | The environment variables for the deployment. The value must be a JSON array of objects. Example: [{"name":"x","value":"y"}, |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   | [{"name":"x","value":"y"}, |   |   |   |   |
|   |   |   |   |   |   |   |   | :"y"}, |   | {"name":"x2","value":"y2"}] |   |   |   |   |   |
|   |   |   |   |   |   |   |   | {"name":"x2","value ":"y2"}\] |   |   |   |   |   |   |   |
| Liveness |   |   |   |   |   |   |   | {"failureThreshold": |   | The liveness probe for the container. Example format: {"failureThreshold": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | {"failureThreshold": |   |   |   |
|   |   |   |   |   |   |   |   | 3,"initialDelaySecon |   | 3,"initialDelaySeconds": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ds": 5,"successThreshold |   | 5,"successThreshold": |   |   |   |   |   |
|   |   | String |   | Query | No |   |   | ": |   | 1,"timeoutSeconds": 1,"tcpSocket": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | 1,"timeoutSeconds": |   | {"host":"", "port":8080}} |   |   |   |   |   |
|   |   |   |   |   |   |   |   | 1,"tcpSocket": {"host":"", "port":8080}} |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | {"failureThreshold": 3,"initialDelaySecon |   | The readiness probe for the container. If the check fails, traffic is not routed to the container through the Kubernetes Service. Example format: {"failureThreshold": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | {"failureThreshold": |   |   |
|   |   |   |   |   |   |   |   | ds": 5,"successThreshold |   | 3,"initialDelaySeconds": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ": |   | 5,"successThreshold": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | 1,"timeoutSeconds": |   | 1,"timeoutSeconds": 1,"httpGet": |   |   |   |   |   |
| Readiness |   | String |   | Query | No |   |   | 1,"httpGet": {"path": |   | {"path": "/consumer","port": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | "/consumer","port": 8080,"scheme": |   | 8080,"scheme": "HTTP","httpHeaders": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | "HTTP","httpHeaders |   | [{"name": "test","value": |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ": [{"name": |   | "testvalue"}]}} |   |   |   |   |   |
|   |   |   |   |   |   |   |   | "test","value": "testvalue"}]}} |   |   |   |   |   |   |   |
| PostStart |   | String |   | Query | No |   |   | {\"exec\": {\"command\": [\"ls\",\"/\"]}}" |   | The post-start script. Example format: {"exec":{"command": |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | {"exec":{"command": |   |   |   |   |
|   |   |   |   |   |   |   |   |   | {\"exec\": {\"command\": | ["cat","/etc/group"]}} |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | "" |   |
| PreStop |   | String |   | Query | No |   |   |   |   | The pre-stop script. Example format: {"tcpSocket":{"host":"", |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | {"tcpSocket":{"host":"", |   |   |   |   |
|   |   |   |   |   |   |   |   | {\"exec\": {\"command\": |   | "port":8080}} |   |   |   |   |   |
|   |   |   |   |   |   |   |   | [\"ls\",\"/\"]}}" |   |   |   |   |   |   |   |

**Returned Data**

| Name | Type | Example | Description |
|---|---|---|---|
| ApplicationInfo | Struct |   | The details of the application. |
| AppId | String | e83acea6-****-47e1-96ae- c0e95377**** | The ID of the application. Call the ListApplication operation to obtain the application ID. |
| AppName | String | test | The name of the application. |
| ChangeOrderId | String | cd65b247-****-475b-ad4b- 7039040d625c | The ID of the change process. Call the GetChangeOrderInfo operation to obtain the ID. |

| ClusterType | Integer | 5 | The type of the cluster where the application is deployed. 0: regular Docker cluster 1: Swarm cluster (discontinued) 2: ECS cluster 3: self-managed Kubernetes cluster in EDAS (discontinued) 4: Pandora auto-registered application cluster 5: Container Service K8s clusters and Serverless K8s clusters |
|---|---|---|---|
| Dockerize | Boolean | true | Indicates whether the application is a Docker application. true false |
| EdasId | String | 1172****6608**** | The ID of the user account. |
| Owner | String | zp | The owner. |
| RegionId | String | cn-beijing | The ID of the region. |
| UserId | String | edas test****@aliyun****.c _ om | The Alibaba Cloud account. |
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |

Request example

```json
POST /pop/v5/k8s/acs/create_k8s_app HTTP/1.1 "AppName": "doc-test", "ClusterId": "c9cd****", "ImageUrl": "registry.cn-beijing.aliyuncs.com/****_test/****-cons****:1.0"
```

Sample success response

```xml
<ApplicationInfo>
    <Dockerize>true</Dockerize>
    <EdasId>1172****6608****</EdasId>
    <Owner>zp</Owner>
    <AppId>e83acea6-****-47e1-96ae-c0e95377****</AppId>
    <UserId>edas_test****@aliyun****.com</UserId>
    <ChangeOrderId>cd65b247-****-475b-ad4b-7039040d625c</ChangeOrderId>
    <RegionId>cn-beijing</RegionId>
    <ClusterType>5</ClusterType>
    <AppName>test</AppName>
</ApplicationInfo>
```

```json
    "Message": "success",
    "ApplicationInfo": {
        "Dockerize": true,
        "EdasId": "1172****6608****",
        "Owner": "zp",
        "AppId": "e83acea6-****-47e1-96ae-c0e95377****",
        "UserId": "edas_test****@aliyun****.com",
        "ChangeOrderId": "cd65b247-****-475b-ad4b-7039040d625c",
        "RegionId": "cn-beijing",
        "ClusterType": 5,
        "AppName": "test"
```

`},`

```json
    "Code": 200
```

###### 1.1.9.2.6 UnbindK8sSlb

Unbinds a Server Load Balancer (SLB) instance from a Container Service for Kubernetes (ACK) application.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

```
DELETE /pop/v5/k8s/acs/k8s_slb_binding HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 5a166fbd-****-****- a286-781659d9f54c | The ID of the application. |
| ClusterId | String | Query | Yes | 712082c3-****-****- 9217-a947b5cde6ee | The ID of the cluster. |
| Type | String | Query | Yes | internet | The type of the SLB instance. Valid values: internet and intranet. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | b0a8441e-****-4e8e-9874- b56dea02952f | The ID of the change process. |
| Code | Integer | 200 | The status code. |
| Message | String | success | The returned message. |

Request example

```json
DELETE /pop/v5/k8s/acs/k8s_slb_binding HTTP/1.1
  "AppId": "5a166fbd-****-****-a286-781659d9f54c"
  "ClusterId": "712082c3-****-****-9217-a947b5cde6ee"
  "Type": "Internet"
```

Successful response examples

```json
<UnbindK8sSlbResponse>
  <ChangeOrderId>b0a8441e-****-4e8e-9874-b56dea02952f</ChangeOrderId>
</UnbindK8sSlbResponse>
 "Message": "success",
 "ChangeOrderId": "b0a8441e-****-4e8e-9874-b56dea02952f",
 "Code": 200
```

###### 1.1.9.2.7 UpdateK8sApplicationConfig

Modifies the configuration of an application in a Container Service for Kubernetes or a Serverless Kubernetes cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /pop/v5/k8s/acs/k8s_app_configuration HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 23bf94d9-****-4994- 9917-616a827aa777 | The ID of the application. Call the ListApplication operation to obtain this ID. For more information, see ListApplication. |
| ClusterId | String | Query | Yes | 9c28bbb9-****-44b3- b953-54ef8a2d0be2 | The ID of the cluster. Call the ListCluster operation to obtain this ID. For more information, see ListCluster. |
| CpuLimit | String | Query | Yes | 1 | The CPU limit for each application instance. Unit: cores. |
| MemoryLimit | String | Query | Yes | 4 | The memory limit for each application instance. Unit: MB. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 8806d1c6-****-48eb-9373- 6bdef3007466 | The ID of the change order. |
| Code | Integer | 200 | API status or POP error code |
| Message | String | success | The response message. |

Example request

```json
PUT /pop/v5/k8s/acs/k8s_app_configuration HTTP/1.1 "AppId": "23bf94d9-****-4994-9917-616a827aa777", "ClusterId": "9c28bbb9-****-44b3-b953-54ef8a2d0be2", "CpuLimit": "1", "MemoryLimit": "400"
```

Example of a successful response

```json
<UpdateK8sApplicationConfigResponse>
  <ChangeOrderId>8806d1c6-****-48eb-9373-6bdef3007466</ChangeOrderId>
</UpdateK8sApplicationConfigResponse>
    "Message": "success",
    "ChangeOrderId": "8806d1c6-****-48eb-9373-6bdef3007466",
    "Code": 200
```

###### 1.1.9.2.8 UpdateK8sSlb

Updates the SLB for an application in Container Service for Kubernetes.

**Request headers**

This operation uses common request headers and has no special request headers. For more information about common request headers, see Common request parameters.

```
PUT /pop/v5/k8s/acs/k8s_slb_binding HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 5a166fbd-****-****- a286-781659d9f54c | The ID of the application. |
| ClusterId | String | Query | Yes | 712082c3-****-****- 9217-a947b5cde6ee | The ID of the cluster. |
| Port | String | Query | Yes | 80 | The frontend port. The value must be in the range of 1 to 65535. |
| SlbProtocol | String | Query | Yes | TCP | The protocol for the SLB instance. Only TCP is supported. Set this parameter to TCP. |
| TargetPort | String | Query | Yes | 8082 | The backend port, which is also the service port of the application. The value must be in the range of 1 to 65535. |
| Type | String | Query | Yes | Internet | The type of the SLB instance. Valid values: Internet and Intranet. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 9a1dcdee-****-****-ad37- cbf9dc91fba9 | The ID of the change process. |
| Code | Integer | 200 | Code |
| Message | String | success | The message returned. |

Request example

```json
PUT /pop/v5/k8s/acs/k8s_slb_binding HTTP/1.1 "AppId": "5a166fbd-****-****-a286-781659d9f54c", "ClusterId": "712082c3-****-****-9217-a947b5cde6ee", "Type": "Internet"
```

Example of a successful response

```json
<UpdateK8sSlbResponse>
  <RequestId></RequestId>
  <ChangeOrderId>9a1dcdee-****-****-ad37-cbf9dc91fba9</ChangeOrderId>
</UpdateK8sSlbResponse>
 "Message": "success",
 "RequestId": "",
 "ChangeOrderId": "9a1dcdee-****-****-ad37-cbf9dc91fba9",
 "Code": 200
```

###### 1.1.9.2.9 ScaleK8sApplication

Scales application instances in a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /pop/v5/k8s/acs/k8s_apps HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 23bf94d9-****-4994- ****-616a827aa777 | The ID of the application. Call the ListApplication operation to obtain the application ID. |
| Replicas | Integer | Query | Yes | 2 | The target number of application instances. The minimum value is 0. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 9d7232b2-****-****-b9d9- 7e17695779ab | The ID of the change order. Call the GetChangeOrderInfo operation to query the progress of the scale-out or scale- in task. |
| Code | Integer | 200 | The status code of the request. |
| Message | String | success | The returned message. |

Sample request

```json
PUT /pop/v5/k8s/acs/k8s_apps HTTP/1.1 "AppId": "23bf94d9-****-4994-****-616a827aa777", "Replicas": "2"
```

Sample successful response

```json
<ScaleK8sApplicationResponse>
  <RequestId>a5281053-08e4-47a5-b2ab-5c0323de7b5a</RequestId>
  <ChangeOrderId>9d7232b2-****-****-b9d9-7e17695779ab</ChangeOrderId>
</ScaleK8sApplicationResponse>
    "RequestId": "a5281053-08e4-47a5-b2ab-5c0323de7b5a",
    "Message": "success",
    "ChangeOrderId": "9d7232b2-****-****-b9d9-7e17695779ab",
    "Code": 200
```

###### 1.1.9.2.10 ImportK8sCluster

You can call the ImportK8sCluster operation to import a Container Service K8s cluster or a serverless K8s cluster into EDAS.

**Request headers**

This operation has no special request headers. For more information about common request headers, see Common parameters.

```
POST /pop/v5/import_k8s_cluster HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | Yes | 9c28bbb9-****-44b3- b953-54ef8a2d0be2 | The ID of the cluster. Call the GetK8sCluster operation to obtain the ID. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|

| Code | Integer | 200 | The status code of the call. |
|---|---|---|---|
| Data | String | cf96d49a-6be2-4b6d-****- 75c7fb86**** | The change record information. |
| Message | String | success | Additional information. |

Sample request

```json
POST /pop/v5/import_k8s_cluster HTTP/1.1
  "ClusterId": "9c28bbb9-****-44b3-b953-54ef8a2d0be2"
```

Sample successful response

```json
<Data>cf96d49a-6be2-4b6d-****-75c7fb86****</Data>
    "Message": "success",
    "Data": "cf96d49a-6be2-4b6d-****-75c7fb86****",
    "Code": 200
```

###### 1.1.9.2.11 ImportSelfK8sCluster

Imports a self-managed Kubernetes cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/resource/k8s_cluster_self_build HTTP/1.1
```

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterName | String | Body | Yes | testselfk8s | The name of the cluster. |
| RegionId | String | Body | Yes | cn-wulan-env149-d01:lybtest | The region ID. |
| ApiServerEndp oint | String | Body | Yes | https://192.168.0.1:6443 | The endpoint of the API server. |
|   |   |   |   | {"apiVersion":"v1","clusters": [{"cluster":{"certificate-authority- data":"LS0tLS1CRUdJTiBDRVJUSU ZJQ0FURS0tLS0tCk1JSUM2VENDQ WRHZ0F3SUJBZ0lCQURBTkJna3Fo a2lHOXcwQkFRc0ZBREFWTVJNd0 VRWURWUVFERXdwcmRXSmwKY 201bGRHVnpNQ0FYRFRJME1ERXl NVEF5TURNd00xb1lEekl4TWpNeE 1qSTRNREl3TXpBeldqQVZNUk13R VFZRApWUVFERXdwcmRXSmxjbT VsZEdWek1JSUJJakFOQmdrcWhra Uc5dzBCQVFFRkFBT0NBUThBTUlJ |   |

| Enterprise Dis Service (EDAS | tributed ) | Application |   | Enterp Servic | rise Distributed Application e Developer Guide·API refe rence |
|---|---|---|---|---|---|
| Parameter | Type | Location | Required | QkNnS0NBUUVBCnJ1elQ3aXBFd2 wEx1NaWmdpqlTeTZUelhJVERXN3ZEV041 | Description |
|   |   |   |   | aXlNbkV6d3J2Sm5Ra3BXekE2djhT ZGlCM1E5aEhCbTAvQWIKcFdDWl ducmM0bEc4S3A1ck1XWTNJenVR TENTZEdlaTd2cHBLVzBFVzB6c25 2OFQ4UW5RblBISUJURkQyck5xaA pjRVdMczNKZy9SUGJPdVRtblAwb 3dqb0tUUUROTFdGcFB2VHNhWDl qbnppb2xjTWdEQjBTa2tmNzRBZT dra3JJClc5NDJKNFYreEJLaGFONnJk ZkQ5N2VsZTVrUC9zd1pyWXBiUFl KR2QrU291Y3dudVE4YlIzNXRhUX FlVHZMNXkKUFcyNXlqMlRHM3dW Vi95REwwdXVLbEl0VFYxSW5JVVZ RTlpmb0R111111ZVRVMwYi9FND hVczl4Uk9YVwpUdVdMaGlJZkFrW StzU05xeU5sYllRSURBUUFCbzBJd 1FEQU9CZ05WSFE4QkFmOEVCQ U1DQXFRd0R3WURWUjBUCkFRSC 9CQVV3QXdFQi96QWRcccUVVVTy txRy9iL3ZCMnZKcVNqb3YxaGxSa kdwdk13RFFZSktvWkkKaHZjTkFR RUxCUUFEZ2dFQkFEeEhZSDBGKz lOSTNkKzdMaTcrS3lRR0RFWG0xa VI1YTJ0eFhIWW1yNE9BSXIzeAorU jV1emlrYU1sUXhadGorcld2UnVocl IwZWhiUS84Zk1jRXIvN25JQnBsW mtRd1FsdUVGN2Zud1JZaXltdEtrC nV4cVNiSlRwMERUcVZhR3JXVjZO Q1J0UHJMRkNtU1VhNzZjNXNVMX Bydk8zYjB5OUJ4Y3BGTW5TNWlVe GRuVkgKSStlbzJpZjA4KzhJNXE2Zn puZ1BxdFJncmJQV3ByMEhIOU1Q WHFvaitKU3F0bm13aXJTVVdpNXh EY1FBcHlSRwpoQWJ3ZXRtQ0VvbE 03TUVFTkNWOTdNNXJBbmlUajZy MURXbkY1ZTNZSUtFNmh6Q0Vxd FdVZmNPSmZwM0xBUFZZClNHV WV6Q3BGM1h4VzhDVWVKbG0vd GVkeU5rdEF3VEk5bFF4Z2pyaz0K LS0tLS1FTkQgQ0VSVElGSUNBVEU tLS0tLQo=","server":"https://192. 168.0.1:6443"},"name":"kubernet es"}],"contexts":[{"context": {"cluster":"kubernetes","user":"ku bernetes- admin"},"name":"kubernetes- admin@kubernetes"}],"current- context":"kubernetes- admin@kubernetes","kind":"Confi g","preferences":{},"users": [{"name":"kubernetes- admin","user":{"client-certificate- data":"LS0tLS1CRUdJTiBDRVJUSU ZJQ0FURS0tLS0tCk1JSURGVENDQ WYyZ0F3SUJBZ0lJRm16NVQ5U2JZ NzR3RFFZSktvWklodmNOQVFFTEJ RQXdGVEVUTUJFR0ExVUUKQXhN S2EzVmlaWEp1WlhSbGN6QWdGd zB5TkRBeE1qRXdNakF6TUROYUd BOHlNVEl6TVRJeU9EQXlNRE13TlZ vdwpOREVYTUJVR0ExVUVDaE1PY zNsemRHVnRPbTFoYzNSbGNuTXh HVEFYQmdOVkJBTVRFR3QxWW1 WeWJtVjBaWE10CllXUnRhVzR3Z2 dFaU1BMEdDU3FHU0liM0RRRUJB UVVBQTRJQkR3QXdnZ0VLQW9JQk FRRGt3anlGaE1aV3pHMEwKQTlW SjNQS1FhbEhCYWNQOXQwV3JmV 2crRzIvbEdJZFpCTHNjMTJpRjZwM CsrVGNIRnlpTWxQN3o5Y3RrTjBLe ApQQVpLc3NUTHFVMDliaVN3S1V qZnBSUS9obGlYSytIN21HcTJWM2 9qRmVKcU1WVzE2SkErYzg3cUdF TlFoK0swCkpqTEY0WXUvNEhMK2 9tQXJwSXIwZm5xUXlpYSs5M0J3c S9oeWQwQnFNaEprVzhtcnRzMHc 3cWhoNm03OFUxREQKZFNGZm9 6bW9IMkE0TFFtMHJqQkxJSElSa2Z EccccCtINyt6NzVPVldPMlZ3c1FzS VBIUUl0K1dlRwp0SXZsZTRXdCtIZ 1pEZGNQQnNJb2tlOG1nU1ZkNFp HVktjcEZKY21CL0o1M2lXOXlWdX BFWTVsaHp1a1FURjRyCnh2eUt6d XkxQWdNQkFBR2pTREJHTUE0R0E xVWREd0VCL3dRRUF3SUZvREFU QmdOVkhTVUVEREFLQmdnckJnR |   |

| Parameter | Type | Location | Required | UYKQlFjREFqQWZCZ05WSFNNRU dEExQaVmdnpQlelJRNzZvYjl2KzhIYThtcEtP | Description The Kubeconfig file of the self- |
|---|---|---|---|---|---|
| Kubeconfig | String | Body | Yes | aS9XR1ZHTWFtOHpBTkJna3Foa2l HOXcwQgpBUXNGQUFPQ0FRRUF Xa3B4UStZeTZKS0V2cHY0MzluSn IzaTZVRzVic3dSVnVCelhTMUdNM ndBUU5tOWtoZFJSCkpw11rrcEVF b2czbWZRcU9zRnhadU5FcVlLbzJV Nk9EREJOLzdMU3lsa2U5SUNGWm VaRFAzREhtdmtjSjgKNm1aamFiN 3ptT2dKTERhTmhuT3prOEs1eDI2 b0Z3QnluRVRvZmVpVWFLcjZBY3 VoNU9jUUwvTStoTHZVNzFDRQpja nZQYjFmWnQyMG9oVG1rcUxBays 2Mkg1R050M1JmVXpmTjl1YTZzN 1ZBYnQ2NmZ3MzhKMlpwOEp4Tn YyTkJFCnl1Z1REMklSR0Q2dGFEa DFkT0dIREdvR1Fjc1F0ZDhwakllL2 9mUjNLQ0pFemlrZC9PVVFHYjl1a UVZUE5RdjEKVkJlZ2VFSGdpdnpiU nA0UC80Ui9GVDBiN2VrTVN0THEx Zz09Ci0tLS0tRU5EIENFUlRJRklDQ VRFLS0tLS0K","client-key- data":"LS0tLS1CRUdJTiBSU0EgUFJ JVkFURSBLRVktLS0tLQpNSUlFcEFJ QkFBS0NBUUVBNU1JOGhZVEdWc 3h0Q3dQVlNkenlrR3BSd1duRC9iZ EZxMzFvUGh0djVSaUhXUVM3Ckh OZG9oZXFkUHZrM0J4Y29qSlQrOC 9YTFpEZENzVHdHU3JMRXk2bE5Q VzRrc0NsSTM2VVVQNFpZbHl2aCs 1aHEKdGxkNkl4WGlhakZWdGVpU VBuUE82aGhEVUlmaXRDWXl4ZU dMditCeS9xSmdLNlNLOUg1NmtN b212dmR3Y0t2NApjbmRBYWpJU1 pGdkpxN2JOTU82b1llcHUvRk5Rdz NVaFg2TTVxQjlnT0MwSnRLNHdTe UJ5RVpIdzRoWDlMUk5KCnJ5L2grL 3MrK1RsVmp0bGNMRUxDRHgwQ 0xmbG5oclNMNVh1RnJmaDRHUT NYRHdiQ0tKSHZKb0VsWGVHUmx TbksKUlNYSmdmeWVkNGx2Y2xic VJHT1pZYzdwRUV4ZUs4Yjhpczdzd FFJREFRQUJBb0lCQVFEZlJZbEdsQ0 gxZzg4RwpDamE1d2ZIcDdDdGhp SFpuZ3VKNEQ0MlgyTFdzdC9VYW VGaWNQTTVpcm12TmsvWVdjSTc rTDBwc0dFSHN6VmJGCm41MVFl UTFFN2poYU5jK1BOS3hReEZGdjh 4TXljUDArMERPUFJ2QUpvSWw5T ml1K3dYOVB4VDUyRXpwWU5saV oKbGhMR09tNW8xNHZGWmZ4U mZHYTNYVjhKUkpUdW1zRHo0Zn NxajBWYXdaUUNtODJRMjlGcUxrS UFTaWpaYjEzUApLSjZGVUhGclE3 WEVlWFFoVDBQNU1LSVZoZHZ5N VhSVEJ5eXNqS0g3cFA0ZE1WSnB yVWlENEF3eURUN1BDQ0lxCm45b mZPc0F5dmpmZmJoVFJkbmJZZG ZDbTJONHpoejZLUUxIcmJaNitYeH NsTkJRZHV4NExYdDNoMnd1dUow T3AKUmhFZHpoMDlBb0dCQU85bl k0U0dTMXFZVzBVNkdFcUZIR1NB c09YQ09VSGw1RzRoTnBZckR2Mz RieUVFc1BnVwozcVVJSVEzccccVV WJDQ1czd295VXBnSWFISGZtbDR vQllIZ0Noc0xENUhsTS9IS3FUNzd Da0JCCklac3ZxbzFQNTM5bWNiRU RDeFUwQkd1QXRIUzlSeUo0Qmls M1cwK21QNzVHUDByUk9CTmVm aG0vQW9HQkFQU2QKN3IxVUdrR 2xVcStrNmx6OVRaUHNrVXNQYXF NUjNKM0hLN2tHMXBJTDgwMnRJV nBRS3FzdmN0RWlkdzBBUmlmdA p6NHVhQ3dVeDV2dGxseUptZkJ6 U2kzUkNYakpIMlFCMFVnTmh4RFJ COWFYTlZZWmZoSU9malVTNUpG b2FmWXRmCnk2VXFiUTlXaUhuaD FmSzZyUHIvc0QwbG1mMnRBTitv eVQ3RHNZNkxBb0dBS21EQjFBYT F0ZzY4TVUvc1Z0eWoKUHdNc3pT OEpWYW50T3JWMFpUYXdDN0w3 | managed Kubernetes cluster, in JSON format. |
|   |   |   |   | Y1B2VW04WG9tWXdMMWQ5MW1 aM1g1dXNCWnF3N3k3VUpQRlBX SFFWMwovNWhXU2c2Smt3am1v UXpmTDdORDg2d3RNM0hheWE3 OTFPdW1KQ2VkMGdaL1g1Y3JVaE NJSzhOM3JpYUhQZ25ECkJYb1VWd |   |

| Parameter | Type | Location | Required | EFWL29lTzBwNmdiNFZOaXg4Q2d ZERxUaFm6Zp2lZeEa0lXb3c4ZmFXQVJBU | Description |
|---|---|---|---|---|---|
|   |   |   |   | FdoQUVpcDd5Y3ZIVm1meCtKWk wKMWtEVE14bUxxTTM4dkpPdkRK WWZUOVNHajFXK3dWekVwV0Z1 ak1hV05RSkJCSUZyWWQ5WUEra nVhODBtRWdMbgpIT0FZb0tjNW5 wZk94Q25wYys5THppbGVXK0hh QWkwQ1dpL2N3Y0Z4bTY3Q1Evc EZQZmRqMm15MFFmeVlNc2w0C kR6eEdiYmNDZ1lCSDBWMlZEZW wyMHVuSU9PZk1PazE2eEVvR1Rn ZmVPSzlTY3VpQVFicEpXVVFHd1N aTXJNRFIKdDdVYUhOc0V2VWhFT UtVMUF6MmNENjBOelNKVzJydGN 1N3JNM2VSNVF5eExwUG9Yc3VTd FRYWDlkYmxLbUVzNQpoUk5PN2t HYWVUZU1SNDhDMUYyVUVkY0t WZVhJYVFoSTNwL25zRG9rS3gzO UliN3NSZHo5clE9PQotLS0tLUVOR CBSU0EgUFJJVkFURSBLRVktLS0tL |   |
| Description | String | Body | No | Qo="}}]} test-self-k8s | The description. |
| ManagedBy | String | Body | No | OAM | The management type: SIMPLE (non-OAM) OAM |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | df85ff3c-e299-4dd9-9485- 8b0c63354a60 | The request ID. |
| Code | Integer | 200 | The status code. |
| Message | String | success | The returned message. |
| Data | String | df85ff3c-e299-4dd9-9485- 8b0c63354a60 | The returned data. |

Sample request

```json
POST /pop/v5/resource/k8s_cluster_self_build HTTP/1.1 "ClusterName":"testselfk8s", "RegionId":"cn-wulan-env149-d01:lybtest", "ApiServerEndpoint":"https://192.168.0.1:6443", "Kubeconfig":"{"apiVersion":"v1","clusters":[{"cluster":{"certificate-authoritydata":"LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM2VENDQWRHZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFE wcmRXSmwKY201bGRHVnpNQ0FYRFRJME1ERXlNVEF5TURNd00xb1lEekl4TWpNeE1qSTRNREl3TXpBeldqQVZNUk13RVFZRApWUVFERXdwcmRXSmxjbTVsZE k1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBCnJ1elQ3aXBFd2w1NWdqTTZUelhJVERXN3ZEV041aXlNbkV6d3J2Sm5Ra3BX 2djhTZGlCM1E5aEhCbTAvQWIKcFdDWlducmM0bEc4S3A1ck1XWTNJenVRTENTZEdlaTd2cHBLVzBFVzB6c252OFQ4UW5RblBISUJURkQyck5xaApjRVdMcz y9SUGJPdVRtblAwb3dqb0tUUUROTFdGcFB2VHNhWDlqbnppb2xjTWdEQjBTa2tmNzRBZTdra3JJClc5NDJKNFYreEJLaGFONnJkZkQ5N2VsZTVrUC9zd1py iUFlKR2QrU291Y3dudVE4YlIzNXRhUXFlVHZMNXkKUFcyNXlqMlRHM3dWVi95REwwdXVLbEl0VFYxSW5JVVZRTlpmb0R111111ZVRVMwYi9FNDhVczl4Uk9 pUdVdMaGlJZkFrWStzU05xeU5sYllRSURBUUFCbzBJd1FEQU9CZ05WSFE4QkFmOEVCQU1DQXFRd0R3WURWUjBUCkFRSC9CQVV3QXdFQi96QWRcccUVVVTyt 9iL3ZCMnZKcVNqb3YxaGxSakdwdk13RFFZSktvWkkKaHZjTkFRRUxCUUFEZ2dFQkFEeEhZSDBGKzlOSTNkKzdMaTcrS3lRR0RFWG0xaVI1YTJ0eFhIWW1yN SXIzeAorUjV1emlrYU1sUXhadGorcld2UnVoclIwZWhiUS84Zk1jRXIvN25JQnBsWmtRd1FsdUVGN2Zud1JZaXltdEtrCnV4cVNiSlRwMERUcVZhR3JXVjZ J0UHJMRkNtU1VhNzZjNXNVMXBydk8zYjB5OUJ4Y3BGTW5TNWlVeGRuVkgKSStlbzJpZjA4KzhJNXE2ZnpuZ1BxdFJncmJQV3ByMEhIOU1QWHFvaitKU3F0b aXJTVVdpNXhEY1FBcHlSRwpoQWJ3ZXRtQ0VvbE03TUVFTkNWOTdNNXJBbmlUajZyMURXbkY1ZTNZSUtFNmh6Q0VxdFdVZmNPSmZwM0xBUFZZClNHVWV6Q3B h4VzhDVWVKbG0vdGVkeU5rdEF3VEk5bFF4Z2pyaz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=","server":"https://192.168.0.1:6443"},"n ":"kubernetes"}],"contexts":[{"context":{"cluster":"kubernetes","user":"kubernetes-admin"},"name":"kubernetes-admin@k ubernetes"}],"current-context":"kubernetes-admin@kubernetes","kind":"Config","preferences":{},"users":[{"name":"kuber netes-admin","user":{"client-certificatedata":"LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURGVENDQWYyZ0F3SUJBZ0lJRm16NVQ5U2JZNzR3RFFZSktvWklodmNOQVFFTEJRQXdGVEVU FR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWdGdzB5TkRBeE1qRXdNakF6TUROYUdBOHlNVEl6TVRJeU9EQXlNRE13TlZvdwpOREVYTUJVR0ExVUVDaE1PYz mRHVnRPbTFoYzNSbGNuTXhHVEFYQmdOVkJBTVRFR3QxWW1WeWJtVjBaWE10CllXUnRhVzR3Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VL JQkFRRGt3anlGaE1aV3pHMEwKQTlWSjNQS1FhbEhCYWNQOXQwV3JmV2crRzIvbEdJZFpCTHNjMTJpRjZwMCsrVGNIRnlpTWxQN3o5Y3RrTjBLeApQQVpLc3 HFVMDliaVN3S1VqZnBSUS9obGlYSytIN21HcTJWM29qRmVKcU1WVzE2SkErYzg3cUdFTlFoK0swCkpqTEY0WXUvNEhMK29tQXJwSXIwZm5xUXlpYSs5M0J3 oeWQwQnFNaEprVzhtcnRzMHc3cWhoNm03OFUxREQKZFNGZm96bW9IMkE0TFFtMHJqQkxJSElSa2ZEccccCtINyt6NzVPVldPMlZ3c1FzSVBIUUl0K1dlRwp ZsZTRXdCtIZ1pEZGNQQnNJb2tlOG1nU1ZkNFpHVktjcEZKY21CL0o1M2lXOXlWdXBFWTVsaHp1a1FURjRyCnh2eUt6dXkxQWdNQkFBR2pTREJHTUE0R0ExV d0VCL3dRRUF3SUZvREFUQmdOVkhTVUVEREFLQmdnckJnRUYKQlFjREFqQWZCZ05WSFNNRUdEQVdnQlJRNzZvYjl2KzhIYThtcEtPaS9XR1ZHTWFtOHpBTkJ Foa2lHOXcwQgpBUXNGQUFPQ0FRRUFXa3B4UStZeTZKS0V2cHY0MzluSnIzaTZVRzVic3dSVnVCelhTMUdNMndBUU5tOWtoZFJSCkpw11rrcEVFb2czbWZRc RnhadU5FcVlLbzJVNk9EREJOLzdMU3lsa2U5SUNGWmVaRFAzREhtdmtjSjgKNm1aamFiN3ptT2dKTERhTmhuT3prOEs1eDI2b0Z3QnluRVRvZmVpVWFLcjZ VoNU9jUUwvTStoTHZVNzFDRQpjanZQYjFmWnQyMG9oVG1rcUxBays2Mkg1R050M1JmVXpmTjl1YTZzN1ZBYnQ2NmZ3MzhKMlpwOEp4TnYyTkJFCnl1Z1REM R0Q2dGFEaDFkT0dIREdvR1Fjc1F0ZDhwakllL29mUjNLQ0pFemlrZC9PVVFHYjl1aUVZUE5RdjEKVkJlZ2VFSGdpdnpiUnA0UC80Ui9GVDBiN2VrTVN0THE 09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K","client-keydata":"LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEFJQkFBS0NBUUVBNU1JOGhZVEdWc3h0Q3dQVlNkenlrR3BSd1duRC9iZEZxMzFv 0djVSaUhXUVM3CkhOZG9oZXFkUHZrM0J4Y29qSlQrOC9YTFpEZENzVHdHU3JMRXk2bE5QVzRrc0NsSTM2VVVQNFpZbHl2aCs1aHEKdGxkNkl4WGlhakZWdG VBuUE82aGhEVUlmaXRDWXl4ZUdMditCeS9xSmdLNlNLOUg1NmtNb212dmR3Y0t2NApjbmRBYWpJU1pGdkpxN2JOTU82b1llcHUvRk5RdzNVaFg2TTVxQjln wSnRLNHdTeUJ5RVpIdzRoWDlMUk5KCnJ5L2grL3MrK1RsVmp0bGNMRUxDRHgwQ0xmbG5oclNMNVh1RnJmaDRHUTNYRHdiQ0tKSHZKb0VsWGVHUmxTbksKUl mdmeWVkNGx2Y2xicVJHT1pZYzdwRUV4ZUs4YjhpczdzdFFJREFRQUJBb0lCQVFEZlJZbEdsQ0gxZzg4RwpDamE1d2ZIcDdDdGhpSFpuZ3VKNEQ0MlgyTFdz VYWVGaWNQTTVpcm12TmsvWVdjSTcrTDBwc0dFSHN6VmJGCm41MVFlUTFFN2poYU5jK1BOS3hReEZGdjh4TXljUDArMERPUFJ2QUpvSWw5Tml1K3dYOVB4VD XpwWU5saVoKbGhMR09tNW8xNHZGWmZ4UmZHYTNYVjhKUkpUdW1zRHo0ZnNxajBWYXdaUUNtODJRMjlGcUxrSUFTaWpaYjEzUApLSjZGVUhGclE3WEVlWFFo QNU1LSVZoZHZ5NVhSVEJ5eXNqS0g3cFA0ZE1WSnByVWlENEF3eURUN1BDQ0lxCm45bmZPc0F5dmpmZmJoVFJkbmJZZGZDbTJONHpoejZLUUxIcmJaNitYeH kJRZHV4NExYdDNoMnd1dUowT3AKUmhFZHpoMDlBb0dCQU85blk0U0dTMXFZVzBVNkdFcUZIR1NBc09YQ09VSGw1RzRoTnBZckR2MzRieUVFc1BnVwozcVVJ zccccVVWJDQ1czd295VXBnSWFISGZtbDRvQllIZ0Noc0xENUhsTS9IS3FUNzdDa0JCCklac3ZxbzFQNTM5bWNiRURDeFUwQkd1QXRIUzlSeUo0QmlsM1cwK NzVHUDByUk9CTmVmaG0vQW9HQkFQU2QKN3IxVUdrR2xVcStrNmx6OVRaUHNrVXNQYXFNUjNKM0hLN2tHMXBJTDgwMnRJVnBRS3FzdmN0RWlkdzBBUmlmdAp VhQ3dVeDV2dGxseUptZkJ6U2kzUkNYakpIMlFCMFVnTmh4RFJCOWFYTlZZWmZoSU9malVTNUpGb2FmWXRmCnk2VXFiUTlXaUhuaDFmSzZyUHIvc0QwbG1mM TitveVQ3RHNZNkxBb0dBS21EQjFBYTF0ZzY4TVUvc1Z0eWoKUHdNc3pTOEpWYW50T3JWMFpUYXdDN0w3Y1B2VW04WG9tWXdMMWQ5MW1aM1g1dXNCWnF3N3k pQRlBXSFFWMwovNWhXU2c2Smt3am1vUXpmTDdORDg2d3RNM0hheWE3OTFPdW1KQ2VkMGdaL1g1Y3JVaENJSzhOM3JpYUhQZ25ECkJYb1VWdEFWL29lTzBwN NFZOaXg4Q2dZRUF6Z2ZEa0lXb3c4ZmFXQVJBUFdoQUVpcDd5Y3ZIVm1meCtKWkwKMWtEVE14bUxxTTM4dkpPdkRKWWZUOVNHajFXK3dWekVwV0Z1ak1hV05 JCSUZyWWQ5WUEranVhODBtRWdMbgpIT0FZb0tjNW5wZk94Q25wYys5THppbGVXK0hhQWkwQ1dpL2N3Y0Z4bTY3Q1EvcEZQZmRqMm15MFFmeVlNc2w0CkR6e YmNDZ1lCSDBWMlZEZWwyMHVuSU9PZk1PazE2eEVvR1RnZmVPSzlTY3VpQVFicEpXVVFHd1NaTXJNRFIKdDdVYUhOc0V2VWhFTUtVMUF6MmNENjBOelNKVzJ N1N3JNM2VSNVF5eExwUG9Yc3VTdFRYWDlkYmxLbUVzNQpoUk5PN2tHYWVUZU1SNDhDMUYyVUVkY0tWZVhJYVFoSTNwL25zRG9rS3gzOUliN3NSZHo5clE9P LS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo="}}]}"
```

Sample success response

```json
 "RequestId":"df85ff3c-e299-4dd9-9485-8b0c63354a60",
 "Message":"success",
 "Data":"df85ff3c-e299-4dd9-9485-8b0c63354a60",
 "Code":200
```

```xml
<RequestId>df85ff3c-e299-4dd9-9485-8b0c63354a60</RequestId> <Data>df85ff3c-e299-4dd9-9485-8b0c63354a60</Data>
```

###### 1.1.9.2.12 StartK8sApplication

Starts an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes (ASK) cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/k8s/acs/start_k8s_app HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 93fdd228-*******- ed2ae98de18d | The ID of the application. You can call the ListApplication operation to obtain this ID. For more information, see ListApplication. |
| Replicas | Integer | Query | No | 2 | The number of application instances to start. |
| Timeout | Integer | Query | No | 60 | The timeout period for the change process, in seconds. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | *********d237-4827-a4f4- ed2ae98de18d | The ID of the change process. |
| Code | Integer | 200 | API status message or POP error code |
| Message | String | success | Additional information |
| RequestId | String | 03FD1520-0FD6-436A- ****-265318D7**** | The ID of the request. |

Example request

```json
POST /pop/v5/k8s/acs/start_k8s_app HTTP/1.1 "AppId": "93fdd228-*******-ed2ae98de18d"
```

Example response

```xml
<RequestId>03FD1520-0FD6-436A-****-265318D7****</RequestId> <ChangeOrderId>*********d237-4827-a4f4-ed2ae98de18d</ChangeOrderId>
```

```json
    "RequestId": "03FD1520-0FD6-436A-****-265318D7****",
    "Message": "success",
    "ChangeOrderId": "*********d237-4827-a4f4-ed2ae98de18d",
    "Code": 200
```

###### 1.1.9.2.13 StopK8sApplication

The StopK8sApplication operation stops an application that is deployed in a Container Service for Kubernetes (ACK) cluster or a Serverless K8s cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/k8s/acs/stop_k8s_app HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 93fdd228-d237- *******8de18d | The ID of the application. Call the ListApplication operation to obtain the application ID. For more information, see ListApplication. |
| Timeout | Integer | Query | No | 60 | The timeout period for the change process, in seconds. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | *******27-a4f4- ed2ae98de18d | The ID of the change process. |
| Code | Integer | 200 | API call status or POP error code |
| Message | String | success | Additional information |
| RequestId | String | 03FD1520-0FD6-436A- ****-265318D7**** | The ID of the request. |

Request example

```json
POST /pop/v5/k8s/acs/stop_k8s_app HTTP/1.1 "AppId": "93fdd228-d237-*******8de18d"
```

Successful response example

```xml
<RequestId>03FD1520-0FD6-436A-****-265318D7****</RequestId> <ChangeOrderId>*******27-a4f4-ed2ae98de18d</ChangeOrderId>
```

```json
    "RequestId": "03FD1520-0FD6-436A-****-265318D7****",
    "Message": "success",
    "ChangeOrderId": "*******27-a4f4-ed2ae98de18d",
    "Code": 200
```

###### 1.1.9.2.14 RestartK8sApplication

Restarts an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes (ASK) cluster.

**Request header**

This operation uses only common request headers. For more information, see the documentation on common request parameters.

```
POST /pop/v5/k8s/acs/restart_k8s_app HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 93fdd228- ********ed2ae98de1 8d | The ID of the application. Call the ListApplication operation to obtain this ID. For more information, see ListApplication. |
| Timeout | Integer | Query | No | 60 | The timeout period for the change record, in seconds. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | *********-ed2ae98de18d | The ID of the change record for this operation. |
| Code | Integer | 200 | API status or POP error code |
| Message | String | success | Additional information |
| RequestId | String | 03FD1520-0FD6-436A- ****-265318D7**** | The ID of the request. |

Request example

```json
POST /pop/v5/k8s/acs/restart_k8s_app HTTP/1.1 "AppId": "93fdd228-********ed2ae98de18d"
```

Successful response example

```xml
<RequestId>03FD1520-0FD6-436A-****-265318D7****</RequestId> <ChangeOrderId>*********-ed2ae98de18d</ChangeOrderId>
```

```json
    "RequestId": "03FD1520-0FD6-436A-****-265318D7****",
    "Message": "success",
    "ChangeOrderId": "*********-ed2ae98de18d",
    "Code": 200
```

##### 1.1.9.3 ECS clusters

###### 1.1.9.3.1 ChangeDeployGroup

Call the ChangeDeployGroup operation to change the group of an application instance in an ECS cluster.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_change_group HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- ********** | The application ID. |
| EccInfo | String | Query | Yes | 0cf49a6c-95a8- 4aa8****** | The ECC ID of the ECS instance for which you want to change the application instance group. <note>You can change the application instance group for only one ECS instance at a time.</note> |
| GroupName | String | Query | Yes | test | The name of the application instance group, such as group a or group b. The GroupName _ _ of the default group is _DEFAULT_GROUP . |
| ForceStatus | Boolean | Query | No | true | Specifies whether to forcefully change the group if the deployment package version of the ECC is different from that of the application instance group. true: Forcefully changes the deployment package version on the ECS instance to the version of the target application instance group. false: Does not forcefully change the group. The deployment package version on the ECS instance to be migrated is retained. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 435f- regfr4******************** | The change order ID. |
| Code | Integer | 200 | The status code. |
| Message | String | success | Additional information |

| RequestId | String | F9E4-FDS4- **************** | The request ID. |
|---|---|---|---|

Request example

```json
POST /pop/v5/changeorder/co_change_group HTTP/1.1 "AppId": "3616cdca-4f92-**********", "EccInfo": "0cf49a6c-95a8-4aa8******", "GroupName": "test"
```

Response example

```json
<RequestId>F9E4-FDS4-****************</RequestId> <ChangeOrderId>435f-regfr4********************</ChangeOrderId>
    "RequestId": "F9E4-FDS4-****************",
    "Message": "success",
    "ChangeOrderId": "435f-regfr4********************",
    "Code": 200
```

###### 1.1.9.3.2 DeleteApplication

You can call the DeleteApplication operation to delete an application from an ECS cluster.

**Request URL**

/pop/v5/changeorder/co_delete_app

**Request method**

DELETE

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /pop/v5/changeorder/co_delete_app HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-********* | The ID of the application. Call the ListApplication operation to obtain the application ID. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 0b8e3c0b-5818- 430************* | The ID of the change flow. |

| Code | Integer | 200 | The status code. |
|---|---|---|---|
| Message | String | success | Additional information. |

Request example

```
http(s)://[Endpoint]/?<Common request parameters>
```

Successful response examples

```json
<ChangeOrderId>0b8e3c0b-5818-430*************</ChangeOrderId>
 "Message": "success",
 "ChangeOrderId": "0b8e3c0b-5818-430****",
 "Code": 200
```

###### 1.1.9.3.3 DeployApplication

Deploys an application to an ECS cluster.

> **Note:** To deploy an application to a Container Service for Kubernetes (K8s) cluster that is imported into EDAS, call the DeployK8sApplication operation.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_deploy HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca- ******************** | The application ID. To obtain the application ID, call the ListApplication operation. |
| DeployType | String | Query | Yes | url | The deployment type. Valid values include url and image. The image value is deprecated. |
| GroupId | String | Query | Yes | all | The ID of the application instance group. To obtain the group ID, call the ListDeployGroup operation. Note To deploy the application to all groups, set this parameter to all . |
| PackageVersion | String | Query | Yes | 1.0 | The version of the deployment package. The value can be up to 64 characters long. A timestamp is recommended. |

| AppEnv | String | Query | No |   | [{\"name\":\"env na _ me 1\", _ \"value\":\"env value _ 1\"}, | The environment variables for the deployment. The value must be in the [{"name":"x","value":"y"}, |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | [{"name":"x","value":"y"}, |   |
|   |   |   |   |   | _ {\"name\":\"env na _ | {"name":"x2","value":"y2"}] |   |   |
|   |   |   |   |   | me 2\",\"value\":\"en _ v value 2\"}] _ _ |   |   |   |
| Desc | String | Query | No |   | Deploy by edas pop api | The description of the application deployment. |   |   |
| WarUrl | String | Query | No |   | https://edas.oss-cn- hangzhou.aliyuncs.c om/demo/hello- edas.war | The URL of the application deployment package, which can be a WAR or JAR file. This parameter is required if you set DeployType to url . Use the path of a deployment package stored in Object Storage Service (OSS). |   |   |
| ImageUrl | String | Query | No |   | registry.cn- hangzhou.aliyuncs.c om/mw/testapp:lates t | (Deprecated parameter) The URL of the application image. You can specify this parameter when you deploy an application in a Swarm cluster. Use an image URL from an Alibaba Cloud image repository. |   |   |
| Batch | Integer | Query | No |   | 1 | The number of batches per group. If you set GroupId to the ID of a specific application instance group, the application is deployed to that group. The minimum number of batches is 1. The maximum number of batches is the number of ECS instances in the Normal state in that group. If you set GroupId to all , the application is deployed to all application groups. The minimum number of batches is 1. The maximum number of batches is the number of ECS instances in the group that has the most ECS instances in the Normal state. |   |   |
| BatchWaitTime | Integer | Query | No |   | 0 | The wait time between batches. Unit: minutes. The default value is 0, which indicates no wait time. The maximum value is 5. If the number of batches is large, do not set this parameter to a large value. Otherwise, the deployment takes a long time. |   |   |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | adf86823-055b-48a4-a59f- fa5582****** | The ID of the change process for the application deployment. |
| Code | Integer | 200 | The status code. |
| Message | String | success | Additional information |

Example request

```json
POST /pop/v5/changeorder/co_deploy HTTP/1.1 "AppId": "3616cdca-********************", "DeployType": "url", "GroupId": "all", "PackageVersion": "1.0"
```

Example successful responses

```json
<ChangeOrderId>adf86823-055b-48a4-a59f-fa5582******</ChangeOrderId>
    "Message": "success",
    "ChangeOrderId": "adf86823-055b-48a4-a59f-fa5582******",
    "Code": 200
```

###### 1.1.9.3.4 DeleteDeployGroup

You can call the DeleteDeployGroup API to delete an application instance group in an ECS cluster.

**Request header**

This API uses common request headers. No special request headers are used. For more information, see Common request parameters.

```
DELETE /pop/v5/deploy_group HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4413- b31************* | The ID of the application. |
| GroupName | String | Query | Yes | test | The name of the application instance group. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code returned. |
| Data | String | 1 | The data returned. |
| Message | String | success | Additional information |

Request example

```json
DELETE /pop/v5/deploy_group HTTP/1.1
  "AppId": ""
  "GroupName": ""
```

Response example

```json
<Data>1</Data>
    "Message": "success",
    "Data": 1,
    "Code": 200
```

###### 1.1.9.3.5 GetApplication

Call the GetApplication operation to retrieve information about an application in an ECS cluster.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/app/app_info HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 29f0**************** ** | The ID of the application. Call the ListApplication operation to get this ID. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Application | Struct |   | The application information. |
| AppId | String | cfac****-847e-4325-ad56- b5c2bc54**** | The application ID. |
| ApplicationType | String | FatJar | The deployment type of the application. War: deployed from a WAR package FatJar: deployed from a JAR package Empty: not deployed |
| BuildPackageId | Long | 59 | The ID of the container version. |
| ClusterId | String | 5ffc5895-****-b03a- c223c6c3**** | The ID of the ECS cluster where the application is deployed. |

| ClusterType | Integer | 2 | The type of the cluster environment for the application. 0: Regular Docker cluster 1: Swarm cluster 2: ECS cluster 3: Kubernetes cluster 4: Pandora auto-registered application cluster |
|---|---|---|---|
| Cpu | Integer | 1 | The number of CPU cores. |
| CreateTime | Long | 1610550324226 | The timestamp of when the application was created. |
| Description | String | test | The description of the application. |
| Dockerize | Boolean | false | Indicates whether it is a Docker application. false: Not a Docker application. true: A Docker application. |
| HealthCheckUrl | String | http://127.0.0.1:8080/xyz.h tml | The health check URL of the application. |
| InstanceCount | Integer | 1 | The number of instances in the application. |
| Memory | Integer | 1024 | The memory size of the application instance. The unit is MB. |
| Name | String | test | The application name. |
| Owner | String | ouou@117274586608**** | The creator of the application. |
| Port | Integer | 8080 | The service port of the application. |
| RegionId | String | cn-hangzhou | The ID of the region where the application resides. |
| RunningInstanceCou nt | Integer | 1 | The number of running application instances. |
| UserId | String | test@dd****** | The Alibaba Cloud account ID. |
| Code | Integer | 200 | The status code. |
| Message | String | success | Additional information. |

Request example

```json
POST /pop/v5/app/app_info HTTP/1.1
  "AppId": "f4ccf3-****-****-****"
```

Response example

```json
<Application>
    <BuildPackageId>59</BuildPackageId>
    <Dockerize>false</Dockerize>
    <Owner>ouou@117274586608****</Owner>
    <Description>test</Description>
    <HealthCheckUrl>http://127.0.0.1:8080/xyz.html</HealthCheckUrl>
    <ClusterId>5ffc5895-****-b03a-c223c6c3****</ClusterId>
    <Memory>1024</Memory>
    <CreateTime>1610550324226</CreateTime>
    <Port>8080</Port>
    <Cpu>1</Cpu>
    <ClusterType>2</ClusterType>
    <Name>test</Name>
    <ApplicationType>FatJar</ApplicationType>
    <InstanceCount>1</InstanceCount>
    <AppId>cfac****-847e-4325-ad56-b5c2bc54****</AppId>
    <UserId>test@dd******</UserId>
    <RegionId>cn-hangzhou</RegionId>
    <RunningInstanceCount>1</RunningInstanceCount>
</Application>
    "Message": "success",
    "Application": {
        "BuildPackageId": 59,
        "Dockerize": false,
        "Owner": "ouou@117274586608****",
        "Description": "test",
        "HealthCheckUrl": "http://127.0.0.1:8080/xyz.html",
        "ClusterId": "5ffc5895-****-b03a-c223c6c3****",
        "Memory": 1024,
        "CreateTime": 1610550324226,
        "Port": 8080,
        "Cpu": 1,
        "ClusterType": 2,
        "Name": "test",
        "ApplicationType": "FatJar",
        "InstanceCount": 1,
        "AppId": "cfac****-847e-4325-ad56-b5c2bc54****",
        "UserId": "test@dd******",
        "RegionId": "cn-hangzhou",
        "RunningInstanceCount": 1
```

`},`

```json
    "Code": 200
```

###### 1.1.9.3.6 InsertApplication

You can call the InsertApplication operation to create an application in an ECS cluster.

> **Note:** To create an application in a Kubernetes cluster, call the InsertK8sApplication operation.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see the Common request parameters document.

```
POST /pop/v5/changeorder/co_create_app HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ApplicationName | String | Query | Yes | hello-edas-test-1 | The name of the application. The name can contain only digits, letters, hyphens (-), and underscores ( ). It must start with a letter and _ can be up to 36 characters in length. |
| BuildPackId | Integer | Query | Yes | 59 | The build package number of EDAS- Container. This parameter is required when you create a High-Speed Framework (HSF) application. You can obtain the build package number in one of the following ways: Call the ListBuildPack operation to query the list of container versions. Obtain the number from the Build Package Number column in the container version table. |
| EcuInfo | String | Query | No | 07bd417a-b863- 477d-****- ************ | The ecu id of the ECS instance to be scaled _ out. The ecu_id is the unique identity of an ECS instance that is imported to EDAS. Separate multiple ecu_id s with commas (,). You can call the ListScaleOutEcu operation to query the ecu_id . |
| Description | String | Query | No | create by edas pop api | The description of the application. |
| HealthCheckURL | String | Query | No | http://127.0.0.1:808 0/ ehc.html _ | The health check URL of the application. |
| dockerize | Boolean | Query | No | false | Specifies whether the application is a Docker application. true false |
| ClusterId | String | Query | No | 13136119-f384- 4f50-b76e- xxxxxxxxxxx | The ID of the ECS cluster in which you want to create the application. If you do not specify this parameter, the application is created in the default cluster. We recommend that you specify this parameter. |
| Cpu | Integer | Query | No | 2 | (Deprecated) The number of CPU cores for the application container in a Swarm cluster. |
| Mem | Integer | Query | No | 2048 | (Deprecated) The memory size for the application container in a Swarm cluster. |
| ReservedPortStr | String | Query | No | 8090 | (Deprecated) The reserved port number for the application. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| ApplicationInfo | Struct |   | The application object that is returned after the application is created. |
| AppId | String | 6c733bcd-6efb-47a1-8226- cf722c****** | The ID of the application. This ID is the unique identifier of an EDAS application. |
| AppName | String | hello-edas-test-1 | The name of the application. |
| ChangeOrderId | String | d0cf569e-dce3-4efb-****- 08b70021**** | The ID of the change process. |

| Dockerize | Boolean | false | Indicates whether the application is a Docker application. Valid values: true false |
|---|---|---|---|
| Owner | String | 249763358688******** | The owner of the application, which is the user who created the application. |
| Port | Integer | 8080 | The default port number of the application, which is 8080. You can call the UpdateContainerConfiguration operation to change the port number. |
| RegionName | String | cn-hangzhou | The name of the region. |
| UserId | String | tdy218@1362469756xxxx xx | The user ID of the application owner. |
| Code | Integer | 200 | The status code of the response. |
| Message | String | The application name test- hsy-C5039-paas-6 had been created successfully. | The message returned. |

Sample request

```json
POST /pop/v5/changeorder/co_create_app HTTP/1.1 "ApplicationName": "hello-edas-test-1", "BuildPackId": "59"
```

Sample response

```xml
<RequestId>4264F69C-686C-4107-B493-0599C8xxxxxx</RequestId> <Message>The application name test-hsy-C5039-paas-6 had been created successfully.</Message> <ApplicationInfo>
    <Dockerize>false</Dockerize>
    <Owner>249763358688********</Owner>
    <AppId>6c733bcd-6efb-47a1-8226-cf722c******</AppId>
    <RegionName>cn-hangzhou</RegionName>
    <UserId>tdy218@1362469756xxxxxx</UserId>
    <Port>8080</Port>
    <ChangeOrderId>d0cf569e-dce3-4efb-****-08b70021****</ChangeOrderId>
    <AppName>hello-edas-test-1</AppName>
</ApplicationInfo>
```

```json
    "RequestId": "4264F69C-686C-4107-B493-0599C8xxxxxx",
    "Message": "The application name test-hsy-C5039-paas-6 had been created successfully.",
    "ApplicationInfo": {
        "Dockerize": false,
        "Owner": "249763358688********",
        "AppId": "6c733bcd-6efb-47a1-8226-cf722c******",
        "RegionName": "cn-hangzhou",
        "UserId": "tdy218@1362469756xxxxxx",
        "Port": 8080,
        "ChangeOrderId": "d0cf569e-dce3-4efb-****-08b70021****",
        "AppName": "hello-edas-test-1"
```

`},`

```json
    "Code": 200
```

**Main parameters for common applications**

1. Key parameters for creating native Dubbo or Java web applications that use the EDAS Java SDK and Apache Tomcat as the
application runtime environment:

```
    InsertApplicationRequest request = new InsertApplicationRequest();
    request.setApplicationName("hello-edas-test-1"); // The name of the application.
    request.setPackageType("war"); // The package type of the application. You can also leave this parameter unspecif
ied.
    request.setComponentIds("7");  // 7 or 4. 7 indicates Apache Tomcat 8.5.42, and 4 indicates Apache Tomcat 7.0.91.
    request.setLogicalRegionId("cn-hangzhou:prod");  // The ID of the namespace, not the name of the namespace. This
parameter is required if the specified cluster is not in the default namespace.
    request.setClusterId("ebc364ca-1875-4266-ae1f-ad0e7c179417"); // Creates the application in the ECS cluster with
the specified cluster ID.
```

2. Key parameters for creating native Spring Boot or Spring Cloud applications of the FatJar type that use the EDAS Java SDK
and the standard Java application runtime environment:

```
    InsertApplicationRequest request = new InsertApplicationRequest();
    request.setApplicationName("hello-edas-test-2"); // The name of the application.
    request.setPackageType("jar"); // The package type of the application. You can also leave this parameter unspecif
ied.
    request.setComponentIds("5");  // 5 or 6. Both 5 and 6 indicate OpenJDK 1.8.0. You can also leave this parameter
unspecified. By default, OpenJDK 1.8.0 is used.
    request.setLogicalRegionId("cn-hangzhou:prod");  // The ID of the namespace, not the name of the namespace. This
parameter is required if the specified cluster is not in the default namespace.
   request.setClusterId("ebc364ca-1875-4266-ae1f-ad0e7c179417"); // Creates the application in the ECS cluster with t
he specified cluster ID.
```

3. Key parameters for creating HSF applications that use the EDAS Java SDK and EDAS-Container as the application runtime
environment:

```
    InsertApplicationRequest request = new InsertApplicationRequest();
    request.setBuildPackId(59); // The version number of the EDAS-Container build package. 59 indicates edas-containe
r 3.5.8.
    request.setApplicationName("hello-edas-test-3"); // The name of the application.
    request.setPackageType("war"); // The package type of the application. Valid values: war and jar. You can also le
ave this parameter unspecified.
    request.setLogicalRegionId("cn-hangzhou:prod");  // The ID of the namespace, not the name of the namespace. This
parameter is required if the specified cluster is not in the default namespace.
    request.setClusterId("ebc364ca-1875-4266-ae1f-ad0e7c179417"); // Creates the application in the ECS cluster with
the specified cluster ID.
```

###### 1.1.9.3.7 ListComponents

The ListComponents operation queries a list of components for applications in ECS clusters.

**Request headers**

This operation has no special request headers. For more information, see Common parameters.

```
GET /pop/v5/resource/components HTTP/1.1
```

This operation has no request parameters.

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| ComponentList | Array of Component |   | The list of components. |
| Component |   |   |   |
| ComponentId | String | 1 | The component ID. |
| Expired | Boolean | false | Indicates whether the component has expired. Valid values: false: The component has not expired. true: The component has expired. |
| Type | String | JDK | The component type. Valid values: JDK TOMCAT TENGINE |
| Version | String | oraclejdk7 | The version. |
| Message | String | success | Additional information |

Sample request

```
GET /pop/v5/resource/components HTTP/1.1
```

Sample response

```xml
<ComponentList>
    <Component>
        <Desc>JDK 7</Desc>
        <Type>JDK</Type>
        <Version>oraclejdk7</Version>
        <ComponentKey>JDK 7</ComponentKey>
        <Expired>false</Expired>
        <ComponentId>1</ComponentId>
    </Component>
</ComponentList>
```

```json
    "Message": "success",
    "ComponentList": {
        "Component": {
            "Desc": "JDK 7",
            "Type": "JDK",
            "Version": "oraclejdk7",
            "ComponentKey": "JDK 7",
            "Expired": false,
            "ComponentId": 1
```

`},`

```json
    "Code": 200
```

###### 1.1.9.3.8 ListDeployGroup

Call ListDeployGroup to retrieve a list of deployment groups.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/app/deploy_group_list HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4413-****- ************ | The ID of the application. Call the ListApplication operation to get this ID. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| DeployGroupList | Array of DeployGroup |   | The list of deployment groups. |
| DeployGroup |   |   |   |
| AppId | String | 3616cdca-4f92-4413-****- ************ | The application ID. |
| AppVersionId | String | changeorder a** ******* * _ _ _ * | The ID of the group deployment record. |
| ClusterId | String | 0d247b93-8d62-4e34-****- ************ | The cluster ID. |
| CreateTime | Long | 1573627695779 | The timestamp when the group was created. |
| GroupId | String | 577f4c50-16ee-43d8-****- ************ | The group ID. |
| GroupName | String | DEFAULT GROUP _ _ | The group name. |

| GroupType | Integer | 1 | The group type: 0: Default group. 1: Grayscale release is not enabled for traffic management. 2: Grayscale release is enabled for flow management. |
|---|---|---|---|
| PackageVersionId | String | a7d48fe8-ad8f-****-89bd- 74cc1ee6**** | The ID of the version deployed in this group. |
| UpdateTime | Long | 1573627695779 | The timestamp when the group was last updated. |
| Message | String | sucess | The returned message. |

Request example

```json
POST /pop/v5/app/deploy_group_list HTTP/1.1 "AppId": "3616cdca-4f92-4413-****-************"
```

Successful response example

```json
<DeployGroupList>
    <GroupName>_DEFAULT_GROUP</GroupName>
    <GroupType>1</GroupType>
    <AppId>3616cdca-4f92-4413-****-************</AppId>
    <ClusterId>0d247b93-8d62-4e34-****-************</ClusterId>
    <CreateTime>1573627695779</CreateTime>
    <UpdateTime>1573627695779</UpdateTime>
    <AppVersionId>changeorder_a**_*******_**</AppVersionId>
    <PackageVersionId>a7d48fe8-ad8f-****-89bd-74cc1ee6****</PackageVersionId>
    <GroupId>577f4c50-16ee-43d8-****-************</GroupId>
</DeployGroupList> <Message>sucess</Message>
    "DeployGroupList": {
        "GroupName": "_DEFAULT_GROUP",
        "GroupType": 1,
        "AppId": "3616cdca-4f92-4413-****-************",
        "ClusterId": "0d247b93-8d62-4e34-****-************",
        "CreateTime": 1573627695779,
        "UpdateTime": 1573627695779,
        "AppVersionId": "changeorder_a**_*******_**",
        "PackageVersionId": "a7d48fe8-ad8f-****-89bd-74cc1ee6****",
        "GroupId": "577f4c50-16ee-43d8-****-************"
```

`},`

```json
    "Message": "sucess",
    "Code": 200
```

###### 1.1.9.3.9 RollbackApplication

Rolls back an application to a previous version.

**Request header**

This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_rollback HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4413-************ | The ID of the application. For information about how to obtain an application ID, see ListApplication. |
| GroupId | String | Query | Yes | 8123db90-880f- 48*************** | The ID of the application group. For information about how to obtain an application group ID, see ListDeployGroup. <note>To roll back the application in all groups, set this parameter to all .</note> |
| HistoryVersion | String | Query | Yes | 2019-11-13 14:22:22 | The historical version to which the application is rolled back. Set this parameter to the value of the PackageVersion parameter that is returned by the ListHistoryDeployVersion operation. |
| Batch | Integer | Query | No | 1 | The number of batches for the rollback. The default value is 1. The maximum value is 5. |
| BatchWaitTime | Integer | Query | No | 0 | The wait time between batches, in minutes. The default value is 0, which indicates no wait time. The maximum value is 5. |

**Response elements**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 921026b8-d1be- ************ | The ID of the change process. For information about how to query the execution progress of the rollback, see GetChangeOrderInfo. |
| Code | Integer | 200 | The response code. |
| Message | String | success | Contains additional information. |

Sample request

```json
POST /pop/v5/changeorder/co_rollback HTTP/1.1 "AppId": "3616cdca-4f92-4413-************", "GroupId": "8123db90-880f-48***************", "HistoryVersion": "2019-11-13 14:22:22"
```

Sample success response

```xml
<RollbackApplicationResponse>
  <RequestId>D16979DC-4D42-*********</RequestId>
  <ChangeOrderId>921026b8-d1be-************</ChangeOrderId>
</RollbackApplicationResponse>
```

```json
    "RequestId": "D16979DC-4D42-*********",
    "Message": "success",
    "ChangeOrderId": "921026b8-d1be-************",
    "Code": 200
```

###### 1.1.9.3.10 ScaleInApplication

The ScaleInApplication operation scales in application instances.

**Request header**

This operation uses common request headers. No special request headers are required. For more information about common request headers, see Common request parameters.

```
POST /pop/v5/changeorder/co_scale_in HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 44****************** ***** | The ID of the application. Call the ListApplication operation to obtain the ID. |
| EccInfo | String | Query | Yes | 7040f221-42df-48e8- 9******************* | The ECC IDs of the machines to remove from the application. Separate multiple IDs with commas (,). Call the QueryApplicationStatus operation to obtain the ECC IDs. |
| ForceStatus | Boolean | Query | No | false | Specifies whether to forcibly take the instances offline. Set this parameter to `true` only when the ECS instances have expired. In normal cases, this parameter is not required. |

**Data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | ddf5a4c7-a507- 4a6e**************** | The ID of the change order. Call the GetChangeOrderInfo operation to query the progress of the scale-in task. If `ForceStatus` is set to `true`, this ID is not returned. In that case, check the `Code` value to determine whether the operation succeeded. |
| Code | Integer | 200 | Code. |
| Message | String | success | The response message. |

Sample request

```json
POST /pop/v5/changeorder/co_scale_in HTTP/1.1
  "AppId": ""
  "EccInfo": ""
```

Sample success response

```json
<ScaleInApplicationResponse>
  <ChangeOrderId>ddf5a4c7-a507-4a6e****************</ChangeOrderId>
</ScaleInApplicationResponse>
 "Message": "success",
 "ChangeOrderId": "ddf5a4c7-a507-4a6e****************",
 "Code": 200
```

###### 1.1.9.3.11 ScaleOutApplication

Scales out an application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_scale_out HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4413**************** * | The ID of the application. To obtain the application ID, see ListApplication. |
| DeployGroup | String | Query | Yes | 4f1fb6f5-6769- 4bd6**************** ** | The application instance group that you want to scale out. To obtain the application instance group, see QueryApplicationStatus. |
| EcuInfo | String | Query | Yes | 8123db90-880f- 486f- b*************** | The elastic compute units (ECUs) to which you want to add instances for the scale-out. To obtain the ECU IDs, see ListScaleOutEcu. Separate multiple ECU IDs with commas (,). |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | f4208118-7171-4e20- 92************ | The ID of the change process. Call the GetChangeOrderInfo operation to query the progress of this scale-out. For more information, see GetChangeOrderInfo. |
| Code | Integer | 200 | The status code returned. |
| Message | String | success | The message returned. |

Request example

```json
POST /pop/v5/changeorder/co_scale_out HTTP/1.1 "AppId": "3616cdca-4f92-4413*****************", "DeployGroup": "4f1fb6f5-6769-4bd6******************", "EcuInfo": "8123db90-880f-486f-b***************"
```

Response example

```json
<ScaleOutApplicationResponse>
  <ChangeOrderId>f4208118-7171-4e20-92************</ChangeOrderId>
</ScaleOutApplicationResponse>
 "Message": "success",
 "ChangeOrderId": "f4208118-7171-4e20-92************",
 "Code": 200
```

###### 1.1.9.3.12 ScaleoutApplicationWithNewInstances

Call the ScaleoutApplicationWithNewInstances operation to purchase Elastic Compute Service (ECS) instances in Enterprise Distributed Application Service (EDAS) and add the instances to a specified application group.

**Limits**

If an application has an Auto Scaling rule enabled, instances purchased by calling this operation are removed first when an automatic scale-in is triggered.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see the common request parameters document.

```
POST /pop/v5/scaling/scale_out HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | e370c17f-*****- 3df0721a327 | The ID of the application to scale out. Call the ListApplication operation to obtain this ID. For more information, see ListApplication. |
| GroupId | String | Query | Yes | e37**********- 33df0721a327 | The ID of the target application group for the scale-out. Call the ListDeployGroup operation to obtain this ID. For more information, see ListDeployGroup. |
| ScalingNum | Integer | Query | Yes | 2 | The number of instances to add in this scale- out. |
| TemplateId | String | Query | No | lt-****hy9s2 | The ID of the ECS launch template. Call the DescribeLaunchTemplates operation to obtain this ID. For more information, see DescribeLaunchTemplates. |

| TemplateVersion | String | Query | No | -1 | The version of the ECS launch template. Call the DescribeLaunchTemplateVersions operation to obtain the version. For more information, see DescribeLaunchTemplateVersions. Note Set this parameter to -1 to use the default launch template version. |
|---|---|---|---|---|---|
| ScalingPolicy | String | Query | No | release | The reclamation mode of the scaling group. Valid values: recycle: The scaling group is in Stop mode. release: The scaling group is in Release mode. For more information about removing instances from a scaling group, see RemoveInstances. |
| TemplateInstanceId | String | Query | No | i-28wt4**** | The ID of an existing ECS instance to use as a template. If specified, new ECS instances are purchased with the same specifications and configuration as this instance. |

**Returned Data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | e370c17f-*****- 3df0721a327 | The ID of the change record for the application scale-out. |
| Code | Integer | 200 | The status code returned. |
| Message | String | success | The returned message. |
| RequestId | String | e370c17f-*****- 3df0721a327 | The ID of the request. |

Request example

```json
POST /pop/v5/scaling/scale_out HTTP/1.1 "AppId": "e370c17f-*****-3df0721a327", "GroupId": "e37**********-33df0721a327", "ScalingNum": "2", "TemplateInstanceId": "i-28wt4****"
```

Successful response example

```json
<ScaleoutApplicationWithNewInstancesResponse>
  <RequestId>e370c17f-*****-3df0721a327</RequestId>
  <ChangeOrderId>e370c17f-*****-3df0721a327</ChangeOrderId>
  <InstanceIds>i-28wt4****</InstanceIds>
  <InstanceIds>i-28wt4****</InstanceIds>
</ScaleoutApplicationWithNewInstancesResponse> {"Message":"success","RequestId":"e370c17f-*****-3df0721a327","ChangeOrderId":"e370c17f-*****- 3df0721a327","InstanceIds":["i-28wt4****","i-28wt4****"],"Code":"200"}
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | Edas.errorcode.Permission Denied.message | You are not authorized to perform the operation. | Permission denied. |

###### 1.1.9.3.13 StartApplication

Starts an application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_start HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 3616cdca-4f92- 4413********** | The ID of the application. You can call ListApplication to obtain the application ID. |
| EccInfo | String | Query | No | "" | The ECC IDs of the instances to reset. Separate multiple IDs with a comma (,). You can call QueryApplicationStatus to obtain the ECC IDs. |

**Response elements**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | 426d3328- 11a*************** | The ID of the change process. CallG etChangeOrderInfo to query the progress of the startup. |
| Code | Integer | 200 | The response code. |
| Message | String | success | The returned message. |

Request example

```json
POST /pop/v5/changeorder/co_start HTTP/1.1
  "AppId": ""
```

Successful response example

```xml
<StartApplicationResponse>
  <ChangeOrderId>426d3328-11a***************</ChangeOrderId>
</StartApplicationResponse>
```

```json
 "Message": "success",
 "ChangeOrderId": "426d3328-11a***************",
 "Code": 200
```

###### 1.1.9.3.14 StopApplication

Stops an application in an Alibaba Cloud ECS cluster or a hybrid cloud ECS cluster.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_stop HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | c627c157- 560d******* | The ID of the application. Call the ListApplication operation to obtain the ID. For more information, see ListApplication. |
| EccInfo | String | Query | No | 74ee9166-****1f6- bcb60e5b**** | The EccId of the ECS instance to stop. Call the QueryApplicationStatus operation to obtain the EccId. For more information, see QueryApplicationStatus. To stop multiple ECS instances, separate their EccIds with commas (,). If you do not set this parameter, all instances in the application are stopped. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | a9557bac-ddd7- ********************* | The ID of the change process. Call the GetChangeOrderInfo operation to obtain the details of the process. For more information, see GetChangeOrderInfo. |
| Code | Integer | 200 | Code |
| Message | String | success | The returned message. |

Request example

```json
POST /pop/v5/changeorder/co_stop HTTP/1.1 "AppId": "c627c157-560d*******"
```

Successful response example

```xml
<StopApplicationResponse>
  <ChangeOrderId>a9557bac-ddd7-*********************</ChangeOrderId>
</StopApplicationResponse>
```

```json
 "Message": "success",
 "ChangeOrderId": "a9557bac-ddd7-*********************",
 "Code": 200
```

###### 1.1.9.3.15 UnbindSlb

You can call the UnbindSlb operation to detach an SLB instance.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/app/unbind_slb_json HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | c627c157-560d- ******************** | The application ID. |
| SlbId | String | Query | Yes | lb- wz9vo49************ **** | The SLB instance ID. |
| Type | String | Query | Yes | internet | The network type of the SLB instance. internet: A public-facing instance. intranet: An internal instance. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The request status code. |
| Data | String | {} | The success or failure information. |
| Message | String | Unbind slb success | The returned information. |

Example request

```json
POST /pop/app/unbind_slb_json HTTP/1.1
  "AppId": ""
  "SlbId": ""
  "Type": ""
```

Example of a successful response

```xml
<UnbindSlbResponse>
  <Data></Data>
  <Message>Unbind slb success</Message>
</UnbindSlbResponse>
```

```json
 "Data": {},
 "Message": "Unbind slb success",
 "Code": 200
```

###### 1.1.9.3.16 UpdateApplicationBaseInfo

The UpdateApplicationBaseInfo operation modifies the name, description, and owner of an application.

**Request headers**

This operation uses only common request headers. For more information, see the Common request parameters document.

```
POST /pop/v5/app/update_app_info HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | c627c157-560d-43ff- ****-************ | The ID of the application. |
| AppName | String | Query | No | hello-edas | The name of the application. The name can be up to 32 characters long. |
| String | Query | No | hello | hello | The description of the application. |

**Returned Data**

| Name | Type | Example | Description |
|---|---|---|---|
| Applcation | Struct |   | Applications. |
| AppId | String | c627c157-560d-43ff-****- ************ | The ID of the application. |
| ApplicationType | String | FatJar | The deployment type of the application. Valid values: War: The application is deployed using a WAR package. FatJar: The application is deployed using a JAR package. Image: The application is deployed using an image. Empty: The application is not deployed. |
| BuildPackageId | Long | 58 | The ID of the container version. |
| ClusterId | String | d7730a49-629a-47bd-****- f45eb01f**** | The ID of the cluster. |
| ClusterType | Integer | 2 | The type of the cluster where the application is deployed. Valid values: 0: Regular Docker cluster. 1: Swarm cluster. 2: ECS cluster. 3: EDAS-K8s cluster. 4: Cluster for applications that are automatically registered with Pandora. 5: Container Service K8s cluster. |
| Cpu | Integer | 0 | The number of CPU cores. |

| CreateTime | Long | 1577259573911 | The timestamp that indicates when the application was created. |
|---|---|---|---|
| Description | String | test | The description of the application. |
| Dockerize | Boolean | false | Indicates whether the application is a Docker application. |
| ExtSlbId | String | ace93******* | The ID of the Internet-facing Server Load Balancer (SLB) instance. |
| ExtSlbIp | String | 39.97.XX.XX | The IP address of the Internet-facing SLB instance. |
| ExtSlbName | String | test | The name of the Internet-facing SLB instance. |
| HealthCheckUrl | String | http://127.0.XX.XX:8080/ e _ tc.html | The URL for the health check. |
| InstanceCount | Integer | 1 | The number of application instances. |
| Memory | Integer | 0 | The memory size of the application instance. Unit: MB. |
| Name | String | test | The name of the application. |
| Owner | String | test@aliyun XXX.com _ | The owner of the application. |
| Port | Integer | 8080 | The port used by the application. |
| RegionId | String | cn-beijing:**** | The ID of the region. |
| RunningInstanceCou nt | Integer | 1 | The number of running application instances. |
| SlbId | String | a3d4******* | The ID of the internal-facing SLB instance. |
| SlbIp | String | 192.168.XX.XX | The IP address of the internal-facing SLB instance. |
| SlbName | String | test | The name of the internal-facing SLB instance. |
| SlbPort | Integer | 80 | The port of the internal-facing SLB instance. |
| UserId | String | edas com***@****.*** _ | The ID of the Alibaba Cloud account. |
| Message | String | success | The returned message. |
| Code | Integer | 200 | Code. |

Example request

```json
POST /pop/v5/app/update_app_info HTTP/1.1 "AppId": "c627c157-560d-43ff-****-************"
```

Example response

```json
<UpdateApplicationBaseInfoResponse>
  <Applcation>
        <SlbPort>0</SlbPort>
        <BuildPackageId>0</BuildPackageId>
        <AppId>c627c157-560d-43ff-****-************</AppId>
        <Memory>0</Memory>
        <Cpu>0</Cpu>
        <Dockerize>false</Dockerize>
        <ApplicationType>FatJar</ApplicationType>
        <Owner>edas_com***_****@******-*****.***</Owner>
        <Description>Ol432236</Description>
        <RunningInstanceCount>0</RunningInstanceCount>
        <UserId>edas_com***_****@******-*****.***</UserId>
        <InstanceCount>1</InstanceCount>
        <Name>testpopapi1120</Name>
        <Port>8080</Port>
        <ClusterId>0d247b93-8d62-4e34-****-************</ClusterId>
        <RegionId>cn-shenzhen:****</RegionId>
        <CreateTime>1574249022930</CreateTime>
        <ClusterType>2</ClusterType>
  </Applcation>
</UpdateApplicationBaseInfoResponse>
 "Message": "success",
 "Applcation": {
    "SlbPort": 0,
    "BuildPackageId": 0,
    "AppId": "c627c157-560d-43ff-****-************",
    "Memory": 0,
    "Cpu": 0,
    "Dockerize": false,
    "ApplicationType": "FatJar",
    "Owner": "edas_com***_****@******-*****.***",
    "Description": "Ol432236",
    "RunningInstanceCount": 0,
    "UserId": "edas_com***_****@******-*****.***",
    "InstanceCount": 1,
    "Name": "testpopapi1120",
    "Port": 8080,
    "ClusterId": "0d247b93-8d62-4e34-****-************",
    "RegionId": "cn-shenzhen:****",
    "CreateTime": 1574249022930,
    "ClusterType": 2
```

`},`

```json
 "Code": 200
```

###### 1.1.9.3.17 UpdateHealthCheckUrl

Sets the health check URL for an application.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/app/modify_hc_url HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | c627c157-560d-43ff- *************** | The application ID. |
| hcURL | String | Query | No | http://127.0.0.1:808 0/ ehc.html _ | The health check URL. The URL must start with http:// and have a maximum length of 255 characters. For example: http://127.0.0.1:8080/_ehc.html . If you do not specify this parameter, the health check URL of the application is not modified. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. |
| HealthCheckURL | String | http://127.0.0.1:8080/ ehc. _ html | The health check URL. |
| Message | String | success | The response message. |

Sample request

```json
POST /pop/v5/app/modify_hc_url HTTP/1.1 "AppId": "c627c157-560d-43ff-***************"
```

Sample response

```json
<UpdateHealthCheckUrlResponse>
  <RequestId>D16979DC-4D42-*****************</RequestId>
  <HealthCheckURL>http://127.0.0.1:8080/_ehc.html</HealthCheckURL>
</UpdateHealthCheckUrlResponse>
    "RequestId": "D16979DC-4D42-*****************",
    "Message": "success",
    "HealthCheckURL": "http://127.0.0.1:8080/_ehc.html",
    "Code": 200
```

###### 1.1.9.3.18 UpdateJvmConfiguration

You can call the UpdateJvmConfiguration operation to configure the Java Virtual Machine (JVM) for an application or an application group.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

```
POST /pop/v5/app/app_jvm_config HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | c627c157-560d- ************* | The ID of the application. |
| GroupId | String | Query | No | 0afc726e-077e- 4357-98b2- db9f7145**** | The ID of the group. You can call ListDeployGroup to query the ID. Note If you specify this parameter, the configuration applies to the group. If you leave this parameter empty, the configuration applies to the application. |
| Options | String | Query | No | -Dproperty=value | The custom parameters. Note If you do not set this parameter for a group, the application's configuration is used. If you do not set this parameter for an application, the default value is used. |
| MinHeapSize | Integer | Query | No | 500 | The initial heap memory size. Unit: MB. Note If you do not set this parameter for a group, the application's configuration is used. If you do not set this parameter for an application, the default value is used. |
| MaxPermSize | Integer | Query | No | 1000 | The permanent generation memory size. Unit: MB. Note If you do not set this parameter for a group, the application's configuration is used. If you do not set this parameter for an application, the default value is used. |
| MaxHeapSize | Integer | Query | No | 500 | The maximum heap memory size. Unit: MB. Note If you do not set this parameter for a group, the application's configuration is used. If you do not set this parameter for an application, the default value is used. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| JvmConfiguration | Struct |   | The JVM parameters. |

| MaxHeapSize | Integer | 500 | The maximum heap memory size. Unit: MB. |
|---|---|---|---|
| MaxPermSize | Integer | 1000 | The permanent generation memory size. Unit: MB. |
| MinHeapSize | Integer | 500 | The initial heap memory size. Unit: MB. |
| Options | String | "" | The custom parameters. |
| Message | String | success | The returned message. |

Request example

```json
POST /pop/v5/app/app_jvm_config HTTP/1.1
  "AppId": ""
```

Example of a successful response

```json
<UpdateJvmConfigurationResponse>
  <JvmConfiguration>
        <MaxPermSize>1000</MaxPermSize>
        <MaxHeapSize>500</MaxHeapSize>
        <MinHeapSize>500</MinHeapSize>
        <Options></Options>
  </JvmConfiguration>
</UpdateJvmConfigurationResponse>
 "Message": "success",
 "JvmConfiguration": {
  "MaxPermSize": 1000,
  "MaxHeapSize": 500,
  "MinHeapSize": 500,
  "Options": ""
```

`},`

```json
 "Code": 200
```

###### 1.1.9.3.19 AddLogPath

The AddLogPath operation adds a log folder for applications that are deployed in Alibaba Cloud ECS clusters and clusters that are not hosted on Alibaba Cloud.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/log/popListLogDirs HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|

| AppId | String | Query | Yes | 3616cdca-4f92- 4413********** | The ID of the application. To obtain the application ID, call the `ListApplication` operation. For more information, see ListApplication. |
|---|---|---|---|---|---|
| Path | String | Query | Yes | /temp/log/ | The absolute path of the application log to collect. The path must start and end with / and must contain /log or /logs . The default EDAS folders are as follows: /home/admin/edas-container/logs/ /home/admin/taobao-tomcat-7.0.59/logs/ /home/admin/taobao-tomcat-production- 7.0.59.3/logs/ /home/admin/taobao-tomcat-production- 7.0.70/logs/ /home/admin/edas-agent/logs/ |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status of the API call or the POP error code. |
| Message | String | success | Additional information. |
| RequestId | String | 3616cdca-4f92- 4413********** | The ID of the request. |

Example request

```json
POST /pop/v5/log/popListLogDirs HTTP/1.1 "AppId": "3616cdca-4f92-4413**********", "Path": "/temp/log/"
```

Example successful response

```json
<RequestId>3616cdca-4f92-4413**********</RequestId>
 "Message": "success",
 "RequestId": "3616cdca-4f92-4413**********",
 "Code": 200
```

###### 1.1.9.3.20 ModifyScalingRule

The ModifyScalingRule operation modifies an auto scaling rule.

**Request headers**

This operation uses common request headers and no special request headers. For more information, see Common request parameters.

```
POST|PUT /pop/v5/app/scaling_rules HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 74ee****-db65- 4322-a1f6- bcb60e5b**** | The ID of the application. |
| GroupId | String | Query | Yes | 8123db90-880f- 486f-****- ************ | The ID of the deployment group. |
| InCpu | Integer | Query | Yes | 50 | The trigger metric: CPU utilization. |
| InDuration | Integer | Query | Yes | 50 | The duration in minutes. |
| InEnable | Boolean | Query | Yes | true | Specifies whether to include a scale-in rule. true: A scale-in rule is included. false: A scale-in rule is not included. |
| InInstanceNum | Integer | Query | Yes | 3 | The minimum number of instances to retain in the group during a scale-in. |
| InLoad | Integer | Query | Yes | 50 | The trigger metric: system load. |
| InRT | Integer | Query | Yes | 50 | The trigger metric: service latency. |
| InStep | Integer | Query | Yes | 1 | The number of instances to remove in each scale-in. |
| OutCPU | Integer | Query | Yes | 50 | The trigger metric: CPU utilization. |
| OutDuration | Integer | Query | Yes | 50 | The duration in minutes. |
| OutEnable | Boolean | Query | Yes | true | Specifies whether to include a scale-out rule. |
| OutInstanceNum | Integer | Query | Yes | 10 | The maximum number of instances in the group after a scale-out. |
| OutLoad | Integer | Query | Yes | 50 | The trigger metric: system load. |
| OutRT | Integer | Query | Yes | 0 | The trigger metric: service latency. |
| OutStep | Integer | Query | Yes | 0 | The number of instances to add in each scale- out. |
| InCondition | String | Query | No | "OR" | The trigger condition. OR: Any condition is met. AND: All conditions are met. |
| OutCondition | String | Query | No | "OR" | The trigger condition. OR: Any condition is met. AND: All conditions are met. |

| ResourceFrom | String | Query | No | "AVAILABLE" | The source of instances for scale-out. NEW: new elastic resources. AVAILABLE: existing resources. The AVAILABLE FIRST policy is prioritized. _ If you set this parameter to NEW or AVAILABLE FIRST, you must specify the _ parameters for elastic scale-out. Elastic scale- out supports two modes: launch template and existing instance-based rule. |
|---|---|---|---|---|---|
| MultiAzPolicy | String | Query | No | "PRIORITY" | The multi-AZ scaling policy for elastic scale- out. Valid values: PRIORITY: The priority-based policy. BALANCE: The balanced distribution policy. |
| VpcId | String | Query | No | "vpc- bp1j55oz3bgd7zepx xxxxxx" | The ID of the VPC associated with the launch template or the existing instance-based rule for elastic scale-out. |
| VSwitchIds | String | Query | No | "vsw- bp1ldxs3d4fdgikyxxx xxx" | A list of vSwitch IDs in the specified VPC. Separate multiple IDs with commas (,). |
| ScalingPolicy | String | Query | No | "release" | The reclamation mode for elastic scale-out. release: The release mode. recycle: The shutdown and reclamation mode. |
| TemplateInstanceId | String | Query | No | "1" | The ID of the instance for the existing instance-based rule. This parameter takes effect only when OutEnable is set to true. |
| TemplateInstanceNa me | String | Query | No | "tpl-tdy218" | The name of the instance for the existing instance-based rule. This parameter takes effect only when TemplateInstanceId is specified. |
| Password | String | Query | No | "Pwdxxxxxxx" | The logon password of the instance. This parameter is valid only when you use an existing instance-based rule for elastic scale- out. |
| KeyPairName | String | Query | No | "tdy218" | The name of the key pair for logging on to the instance. This parameter is valid only when you use an existing instance-based rule for elastic scale-out. |
| AcceptEULA | Boolean | Query | No | true | If you use elastic scale-out, this parameter must be set to true. |
| TemplateId | String | Query | No | "lt- wz9hkhn8wpq2zxxxx " | The ID of the launch template for elastic scale-out. This parameter takes effect only when OutEnable is set to true. This parameter has a higher priority than TemplateInstanceId. |
| TemplateVersion | Integer | Query | No | -1 | The version of the launch template for elastic scale-out. This parameter is valid only when TemplateId is specified. To use the default template, set this parameter to -1 . Otherwise, set it to a specific version number. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|

| Code | Integer | 200 | The response code. |
|---|---|---|---|
| Message | String | success | The response message. |

Request example

```json
POST /pop/v5/app/scaling_rules HTTP/1.1 "AppId": "74ee****-db65-4322-a1f6-bcb60e5b****", "GroupId": "8123db90-880f-486f-****-************", "InCpu": "50", "InDuration": "50", "InEnable": "true", "InInstanceNum": "3", "InLoad": "50", "InRT": "50", "InStep": "1", "OutCPU": "50", "OutDuration": "50", "OutEnable": "true", "OutInstanceNum": "10", "OutLoad": "50", "OutRT": "0", "OutStep": "0"
```

Successful response

```json
<ModifyScalingRuleResponse> </ModifyScalingRuleResponse>
    "Message": "success",
    "Code": 200
```

###### 1.1.9.3.21 RestartApplication

The RestartApplication operation restarts applications that are deployed in Alibaba Cloud ECS clusters and hybrid cloud ECS clusters.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/changeorder/co_restart HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | c627c157- 560d******* | The ID of the application. For more information about how to obtain the application ID, see ListApplication. |

| EccInfo | String | Query | Yes | 006c0ea5-5f8d- 4398-af1e-********** | The EccId of the ECS instance in the application that you want to restart. For more information about how to obtain the EccId, see QueryApplicationStatus. If you specify multiple EccIds, separate them with commas (,). If you do not set this parameter, all instances in the application are restarted. |
|---|---|---|---|---|---|

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| ChangeOrderId | String | a9557bac-ddd7- ********************* | The ID of the change process. For more information about how to query the progress of the restart, see GetChangeOrderInfo. |
| Code | Integer | 200 | Code |
| Message | String | success | Invocation details |
| RequestId | String | D16979DC-4D42- **************** | The ID of the request. |

Request example

```json
POST /pop/v5/changeorder/co_restart HTTP/1.1 "AppId": "c627c157-560d*******"
```

Example of a successful response

```json
<ChangeOrderId>a9557bac-ddd7-*********************</ChangeOrderId>
 "Message": "success",
 "ChangeOrderId": "a9557bac-ddd7-*********************",
 "Code": 200
```

#### 1.1.10 Service administration

##### 1.1.10.1 GetServiceGovernanceConfig

Retrieves the service governance configuration details for a specified application.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
GET /pop/v5/app/service_governance_config HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 2dfea044-479f-464a-b374- f14d32****** | The application ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The request ID. |
| Code | Integer | 200 | The HTTP status code or a POP error code. |
| Message | String | message | Additional information. |
| Data | Struct | - | The data returned. |
| - LosslessOnlineEnabl ed | Boolean | false | Indicates whether the graceful start feature is enabled. |
| - LosslessOnlineWarm up | Integer | 120 | The warm-up duration. Unit: seconds. |
| -LosslessOnlineDelay | Integer | 30 | The delayed registration time. Unit: seconds. |
| - LosslessOnlineFuncT ype | Integer | 2 | The shape of the QPS curve during the warm-up process. For example, a value of 2 indicates that the curve is quadratic. |
| - EmptyPushProtectio nEnabled | Boolean | false | Indicates whether empty push protection is enabled. This feature improves client reliability when list subscriptions are abnormal due to changes in the service registry (such as upgrades or downgrades), unexpected events (such as network or power outages in a zone), or other unforeseeable circumstances. |
| -LocalityEnabled | Boolean | false | Indicates whether the locality policy is enabled. This policy preferentially routes requests to servers in the same location as the client. |
| -LocalityThreshold | Float | 0.8 | The threshold for data locality. If the ratio of local data access exceeds this value, the data is considered highly local and can be optimized. |

Sample request

```
GET /pop/v5/app/service_governance_config HTTP/1.1 &AppId=2dfea044-479f-464a-b374-f14d32****** &<Common request parameters>
```

Sample responses

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Data":{
  "LosslessOnlineDelay":30,
  "LocalityEnabled":false,
  "LosslessOnlineEnabled":false,
  "LosslessOnlineWarmup":120,
  "LocalityThreshold":0.8,
  "EmptyPushProtectionEnabled":false,
  "LosslessOnlineFuncType":2
```

`},`

```json
 "Code":200
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message> <Data>
 <LosslessOnlineDelay>30</LosslessOnlineDelay>
 <LocalityEnabled>false</LocalityEnabled>
 <LosslessOnlineEnabled>false</LosslessOnlineEnabled>
 <LosslessOnlineWarmup>120</LosslessOnlineWarmup>
 <LocalityThreshold>0.8</LocalityThreshold>
 <EmptyPushProtectionEnabled>false</EmptyPushProtectionEnabled>
 <LosslessOnlineFuncType>2</LosslessOnlineFuncType>
</Data>
```

##### 1.1.10.2 UpdateServiceGovernanceConfig

Updates the configuration for service administration.

**Request header**

This operation uses only common request headers. For more information, see the document on common request parameters.

```
POST /pop/v5/app/service_governance_config HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Body | No | 2dfea044-479f-464a-b374- f14d32****** | The ID of the application. |
| LosslessOnline Enabled | Boolean | Body | No | true | Specifies whether to enable the graceful start feature. |
| LosslessOnline Warmup | Integer | Body | No | 120 | The warmup duration. Unit: seconds. |
| LosslessOnline Delay | Integer | Body | No | 30 | The registration delay. Unit: seconds. |
| LosslessOnline FuncType | Integer | Body | No | 2 | The shape of the queries per second (QPS) curve during the warmup process. For example, a value of 2 indicates a quadratic curve. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| EmptyPushProt ectionEnabled | Boolean | Body | No | true | Specifies whether to enable empty push protection. This feature improves client reliability during abnormal list subscriptions. Abnormal subscriptions can occur when the registry center undergoes changes, such as upgrades or downgrades, or encounters unexpected events like zone-wide network failures or power outages. |
| LocalityEnable d | Boolean | Body | No | true | Specifies whether to disable the locality policy. If the policy is disabled, requests can be scheduled freely among servers in any region. |
| LocalityThresh old | Float | Body | No | 0.8 | The threshold that triggers locality-based scheduling. When the affinity score between a task and a node is higher than this value, the task is preferentially scheduled to that node. |

**Returned Data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The request ID. |
| Code | Integer | 200 | The status code of the response. This can be an API status code or a POP error code. |
| Message | String | message | Additional information. |
| Data | Struct | - | The data returned. |
| - LosslessOnlineEnabl ed | Boolean | true | Indicates whether the graceful start feature is enabled. |
| - LosslessOnlineWarm up | Integer | 120 | The warmup duration. Unit: seconds. |
| -LosslessOnlineDelay | Integer | 30 | The registration delay. Unit: seconds. |
| - LosslessOnlineFuncT ype | Integer | 2 | The shape of the QPS curve during the warmup process. For example, a value of 2 indicates a quadratic curve. |
| - EmptyPushProtectio nEnabled | Boolean | true | Indicates whether empty push protection is enabled. |
| -LocalityEnabled | Boolean | true | Indicates whether the locality policy is disabled. If the policy is disabled, requests are not preferentially routed to local nodes. |
| -LocalityThreshold | Float | 0.8 | The threshold that triggers locality-based scheduling. When the affinity score between a task and a node is higher than this value, the task is preferentially scheduled to that node. |

Request example

```
POST /pop/v5/app/service_governance_config HTTP/1.1
```

Response example

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Data":{
  "LosslessOnlineDelay":30,
  "LocalityEnabled":true,
  "LosslessOnlineEnabled":true,
  "LosslessOnlineWarmup":120,
  "LocalityThreshold":0.8,
  "EmptyPushProtectionEnabled":true,
  "LosslessOnlineFuncType":2
```

`},`

```json
 "Code":200
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message> <Data>
 <LosslessOnlineDelay>30</LosslessOnlineDelay>
 <LocalityEnabled>true</LocalityEnabled>
 <LosslessOnlineEnabled>true</LosslessOnlineEnabled>
 <LosslessOnlineWarmup>120</LosslessOnlineWarmup>
 <LocalityThreshold>0.8</LocalityThreshold>
 <EmptyPushProtectionEnabled>true</EmptyPushProtectionEnabled>
 <LosslessOnlineFuncType>2</LosslessOnlineFuncType>
</Data>
```

##### 1.1.10.3 UpdateServiceGovernanceConfigInternal

This operation updates the service administration configuration and supports features such as lossless online and offline, empty push protection, and regional traffic shaping.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/internal/app/service_governance_config HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Body | No | 2dfea044-479f-464a-b374- f14d32****** | The application ID. |
| LosslessOnline Enabled | Boolean | Body | No | true | Specifies whether to enable the lossless online feature. This feature ensures high-quality data transmission and processing. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| LosslessOnline Warmup | Integer | Body | No | 120 | The warm-up duration, in seconds. If you enable the lossless online feature, the system preloads cached data during the warm-up period to improve service performance without data loss. |
| LosslessOnline Delay | Integer | Body | No | 30 | The registration delay, in seconds. |
| LosslessOnline FuncType | Integer | Body | No | 2 | The shape of the queries per second (QPS) curve during the warm-up process. For example, a value of 2 indicates a quadratic curve. |
| EmptyPushProt ectionEnabled | Boolean | Body | No | true | Specifies whether to enable empty push protection. This feature prevents the system from sending push messages with empty payloads to clients. |
| LocalityEnable d | Boolean | Body | No | true | Specifies whether to enable the locality policy. This policy prioritizes routing requests to local nodes. |
| LocalityThresh old | Float | Body | No | 0.5 | The threshold for locality-based scheduling. If the affinity score between a task and a node is higher than this threshold, the task is preferentially scheduled to that node. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1EB9475F-4C6E-4B5F- 8EEF-BFCF2B****** | The request ID. |
| Code | Integer | 200 | The status code. |
| Message | String | message | Additional information |
| Data | Struct | - | The data returned. |
| - LosslessOnlineEnabl ed | Boolean | true | Indicates whether the lossless online feature is enabled. This feature allows for real-time transmission or playback of high-quality audio or data without compression. |
| - LosslessOnlineWarm up | Integer | 120 | The warm-up duration, in seconds. This feature ensures a smooth traffic transition when the service starts and prevents sudden high loads. |
| -LosslessOnlineDelay | Integer | 30 | This indicates a 30 ms latency from the system during lossless online transmission, a process typically used to ensure data integrity and synchronization. |
| - LosslessOnlineFuncT ype | Integer | 2 | The shape of the QPS curve during the warm-up process. For example, a value of 2 indicates a quadratic curve. |

| r | Enterprise Distrib Service Developer ence | uted Application Guide·API refe |   | Enterprise Distributed Application Service (EDAS | ) |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - EmptyPushProtectio nEnabled | Boolean | true | Indicates whether empty push protection is enabled. This feature prevents the system from sending push messages with empty payloads to clients. |
| -LocalityEnabled | Boolean | true | Indicates whether the localization feature is enabled. This feature allows the system to provide services or content based on the user's geographical location. |
| -LocalityThreshold | Float | 0.5 | The tolerance threshold for locality priority in task scheduling. A lower value indicates a stronger preference for strict locality-based scheduling. A value of 0.5 indicates medium tolerance. |

Sample request

```
POST /pop/v5/internal/app/service_governance_config HTTP/1.1
```

Sample response

```json
 "RequestId":"1EB9475F-4C6E-4B5F-8EEF-BFCF2B******",
 "Message":"message",
 "Data":{
  "LosslessOnlineDelay":30,
  "LocalityEnabled":true,
  "LosslessOnlineEnabled":true,
  "LosslessOnlineWarmup":120,
  "LocalityThreshold":0.5,
  "EmptyPushProtectionEnabled":true,
  "LosslessOnlineFuncType":2
```

`},`

```json
 "Code":200
<RequestId>1EB9475F-4C6E-4B5F-8EEF-BFCF2B******</RequestId> <Message>message</Message> <Data>
 <LosslessOnlineDelay>30</LosslessOnlineDelay>
 <LocalityEnabled>true</LocalityEnabled>
 <LosslessOnlineEnabled>true</LosslessOnlineEnabled>
 <LosslessOnlineWarmup>120</LosslessOnlineWarmup>
 <LocalityThreshold>0.5</LocalityThreshold>
 <EmptyPushProtectionEnabled>true</EmptyPushProtectionEnabled>
 <LosslessOnlineFuncType>2</LosslessOnlineFuncType>
</Data>
```

##### 1.1.10.4 ListConsumedServices

You can call ListConsumedServices to query consumed services.

**Request headers**

This operation uses common request headers and does not have special request headers. For more information, see Common request parameters.

```
GET /pop/v5/service/listConsumedServices HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | a66c5d1f-****-****- 8c2b-6925f781b203 | The ID of the application. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| ConsumedServicesLi st | Array of ListConsumedServic es |   | The list of consumed services. |
| ListConsumedServic es |   |   |   |
| AppId | String | a5281053-08e4-47a5- b2ab-5c0323de7b5a | The ID of the application. |
| DockerApplication | Boolean | true | Indicates whether the application is a Docker application. |
| Group2Ip | String | "" | This parameter is reserved and has no practical use. |
| Groups | List | group | The group of the consumed service. |
| Ips | List | 102.XX.XX.23 | The subscription endpoint of the service. |
| Name | String | service | The name of the consumed service. |
| Type | String | HSF | The type of the published service. |
| Version | String | 1.0 | The version of the consumed service. |
| Message | String | success | The returned message. |

Request example

```json
GET /pop/v5/service/listConsumedServices HTTP/1.1 "AppId": "a66c5d1f-****-****-8c2b-6925f781b203"
```

Successful response examples

```json
<ConsumedServicesList>
    <Type>HSF</Type>
    <Group2Ip>""</Group2Ip>
    <AppId>a5281053-08e4-47a5-b2ab-5c0323de7b5a</AppId>
    <Version>1.0</Version>
    <DockerApplication>true</DockerApplication>
    <Name>service</Name>
    <Groups>group</Groups>
    <Ips>102.XX.XX.23</Ips>
</ConsumedServicesList>
    "Message": "success",
    "ConsumedServicesList": {
        "Type": "HSF",
        "Group2Ip": "\"\"",
        "AppId": "a5281053-08e4-47a5-b2ab-5c0323de7b5a",
        "Version": 1,
        "DockerApplication": true,
        "Name": "service",
        "Groups": "group",
        "Ips": "102.XX.XX.23"
```

`},`

```json
    "Code": 200
```

##### 1.1.10.5 ListServiceGroups

The ListServiceGroups operation queries the service groups of a High-Speed Service Framework (HSF) application.

**Request headers**

This operation has no special request headers. For information about common request headers, see Common request parameters.

```
GET /pop/v5/service/serviceGroups HTTP/1.1
```

This operation has no request parameters.

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The message returned. |
| ServiceGroupsList | Array of ListServiceGroups |   | The list of service groups. |
| ListServiceGroups |   |   |   |
| CreateTime | String | 1575357165770 | The UNIX timestamp when the service group was created. |
| GroupId | String | 789d9cda-74b1-****-****- 05e21a0a7661 | The ID of the service group. |
| GroupName | String | edas-test-group | The name of the service group. |

Request example

```
GET /pop/v5/service/serviceGroups HTTP/1.1
```

Successful response example

```json
<ServiceGroupsList>
    <GroupName>edas-test-group</GroupName>
    <CreateTime>1575357165770</CreateTime>
    <GroupId>789d9cda-74b1-****-****-05e21a0a7661</GroupId>
</ServiceGroupsList>
    "ServiceGroupsList": {
        "GroupName": "edas-test-group",
        "CreateTime": 1575357165770,
        "GroupId": "789d9cda-74b1-****-****-05e21a0a7661"
```

`},`

```json
    "Message": "success",
    "Code": 200
```

##### 1.1.10.6 ListPublishedServices

You can call the ListPublishedServices operation to query published services.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/service/listPublishedServices HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 1fbd8b72-****-****- bdfe-478dbc914121 | The application ID. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |
| PublishedServicesLis t | Array of ListPublishedService s |   | The list of published services. |
| ListPublishedService s |   |   |   |
| AppId | String | ECD1D6FC-4307-4583- BA6F-215F3857E**** | The application ID. |

| DockerApplication | Boolean | false | Indicates whether the application is a Docker application. |
|---|---|---|---|
| Group2Ip | String | "" | A reserved field. |
| Groups | List | DEFAULT GROUP _ | The group of the consumed service. |
| Ips | List | 112.XX.XX.24 | The subscription address of the service. |
| Name | String | providers:com.**** | The name of the published service. |
| Route | String | "" | This parameter is not used in Apsara Stack. |
| Tenants | List | ["adcvcc-*"] | The service unit information. |
| Type | String | RESTful | The type of the published service. |
| Unit | String | center | The unit information. This parameter is not used in Apsara Stack. |
| UnitType | String | region | The unit type. This parameter is not used in Apsara Stack. |
| Version | String | v1 | The version of the published service. |
| WriteMode | String | w | The write model. This parameter is not used in Apsara Stack. |

Request example

```json
GET /pop/v5/service/listPublishedServices HTTP/1.1 "AppId": "1fbd8b72-****-****-bdfe-478dbc914121"
```

Successful response example

```xml
<PublishedServicesList>
    <ListPublishedServices>
        <Groups>
            <group>DEFAULT_GROUP</group>
        </Groups>
        <Name>providers:com.****</Name>
        <DockerApplication>false</DockerApplication>
        <Type>RESTful</Type>
        <Group2Ip/>
        <Version>--</Version>
        <Ips>
        </Ips>
    </ListPublishedServices>
</PublishedServicesList>
```

```json
 "Message": "success",
 "Code": 200,
 "PublishedServicesList": {
  "ListPublishedServices": [
    "Groups": {
     "group": [
      "DEFAULT_GROUP"
```

`]` `},`

```json
    "Name": "providers:com.****",
    "DockerApplication": false,
    "Type": "RESTful",
    "Group2Ip": {},
    "Version": "--",
    "Ips": {
     "ip": []
```

`]`

#### 1.1.11 Permission management

##### 1.1.11.1 AuthorizeApplication

Grants a Resource Access Management (RAM) user permissions on an application.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/account/authorize_app HTTP/1.1
```

| Name | Type | Locatio n | Required | Example |   | Description |   |
|---|---|---|---|---|---|---|---|
| AppIds | String | Query | Yes | 5fdf50e8-*****;696- ****** |   | The ID of the application. To specify multiple IDs, separate them with a semicolon (;). Set this parameter to null to revoke the permissions on all applications. |   |
| TargetUserId | String | Query | Yes | test@133434434**** |   | The user ID of the RAM user to be granted permissions. The ID must be in the RAM |   |
|   |   |   |   |   |   |   | RAM |
|   |   |   |   |   |   | user name@Alibaba Cloud account UID |   |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | Additional information. |

Request example

```json
POST /pop/v5/account/authorize_app HTTP/1.1 "AppIds": "5fdf50e8-*****;696-******", "TargetUserId": "test@133434434****"
```

Successful response

```json
    "Message": "success",
    "Code": 200
```

##### 1.1.11.2 AuthorizeResourceGroup

You can call the AuthorizeResourceGroup operation to grant a Resource Access Management (RAM) user permissions on specified resource groups.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/account/authorize_res_group HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| ResourceGroupIds | String | Query | No | 461;462 | The ID of the resource group. Call the ListResourceGroup operation to obtain this ID. For more information, see ListResourceGroup. To specify multiple resource groups, separate their IDs with semicolons (;). |
| TargetUserId | String | Query | Yes | test@13333******** | The ID of the RAM user. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code of the API call or a POP error code. |
| Message | String | success | Information |
| RequestId | String | 57609587-DFA2-********** | The request ID. |

Sample request

```json
POST /pop/v5/account/authorize_res_group HTTP/1.1 "ResourceGroupIds": "461;462", "TargetUserId": "test@13333********"
```

Sample response

```json
<RequestId>57609587-DFA2-41EC-**********</RequestId>
 "RequestId": "57609587-DFA2-41EC-**********",
 "Code": "200",
 "Message": "success"
```

##### 1.1.11.3 AuthorizeRole

Call the AuthorizeRole operation to grant role permissions to a RAM user.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/account/authorize_role HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| TargetUserId | String | Query | Yes | test@133****** | The ID of the RAM user to be authorized. |
| RoleIds | String | Query | No | 1;2 | The ID of the role. Separate multiple IDs with semicolons (;). Set this parameter to null to revoke the permissions for all roles. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code of the request. |
| Message | String | success | Additional information |

Request example

```json
POST /pop/v5/account/authorize_role HTTP/1.1 "TargetUserId": "test@133******"
```

Successful response example

```json
    "Message": "success",
    "Code": 200
```

##### 1.1.11.4 DeleteRole

The DeleteRole operation deletes a role.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/account/delete_role HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| RoleId | Integer | Query | Yes | 99999999 | The ID of the role. |

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response status code. |
| Message | String | success | Additional information |

Request example

```json
POST /pop/v5/account/delete_role HTTP/1.1 "RoleId": "99999999"
```

Example of a successful response

```json
    "Message": "success",
    "Code": 200
```

##### 1.1.11.5 GetSecureToken

Obtains the SecureToken information for a specific namespace. This information includes the AccessKey ID, AccessKey secret, TenantId, and the domain name of the address server.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/secure_token HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|
| NamespaceId | String | Query | Yes | cn-shenzhen:x***** | The ID of the namespace. Examples: cn- beijing and cn-beijing:prod . |   |   |   |
|   |   |   |   |   |   |   | cn- |   |
|   |   |   |   |   |   | cn-beijing:prod |   |   |

|   | beijing |
|---|---|

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The message returned for the request. |
| RequestId | String | D16979DC-4D42- ************* | The ID of the request. |
| SecureToken | Struct |   | The SecureToken object returned for the request. |
| AccessKey | String | f676f1************** | The AccessKey ID of the namespace. |
| AddressServerHost | String | addr-****- ****.edas.aliyun.com | The address of the address server for the namespace. |
| BelongRegion | String | cn-shenzhen | The ID of the region to which the namespace belongs. |
| Description | String | "" | The description of the namespace. |
| EdasId | String | 11727458******** | The EdasId of the user, which is the Alibaba Cloud UID. |
| Id | Long | 7279 | The ID of the SecureToken. |
| RegionId | String | cn-shenzhen:x******* | The ID of the region where the namespace is located. |
| RegionName | String | x****** | The name of the region where the namespace is located. |
| SecretKey | String | ********************** | The AccessKey secret of the namespace. |
| TenantId | String | 401b7bc8-9441-4693-****- ************ | The tenant ID of the namespace. |
| UserId | String | edas com*** ****@******- _ _ *****.*** | The UID of the user. |

Sample request

```json
GET /pop/v5/secure_token HTTP/1.1 "NamespaceId": "cn-shenzhen:x*****"
```

Sample response

```json
<SecureToken>
    <EdasId>11727458********</EdasId>
    <TenantId>401b7bc8-9441-4693-****-************</TenantId>
    <SecretKey>gOSgbgR2R*************</SecretKey>
    <Description>""</Description>
    <RegionName>x******</RegionName>
    <UserId>edas_com***_****@******-*****.***</UserId>
    <AddressServerHost>addr-****-****.edas.aliyun.com</AddressServerHost>
    <AccessKey>f676f1**************</AccessKey>
    <RegionId>cn-shenzhen:x*******</RegionId>
    <Id>7279</Id>
    <BelongRegion>cn-shenzhen</BelongRegion>
</SecureToken> <RequestId>D16979DC-4D42-*************</RequestId>
    "SecureToken": {
        "EdasId": "11727458********",
        "TenantId": "401b7bc8-9441-4693-****-************",
        "SecretKey": "gOSgbgR2R*************",
        "Description": "\"\"",
        "RegionName": "x******",
        "UserId": "edas_com***_****@******-*****.***",
        "AddressServerHost": "addr-****-****.edas.aliyun.com",
        "AccessKey": "f676f1**************",
        "RegionId": "cn-shenzhen:x*******",
        "Id": 7279,
        "BelongRegion": "cn-shenzhen"
```

`},`

```json
    "RequestId": "D16979DC-4D42-*************",
    "Message": "success",
    "Code": 200
```

##### 1.1.11.6 InsertRole

The InsertRole operation creates a role.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

```
POST /pop/v5/account/create_role HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|

| ActionData | String | Query | Yes | 15:1;14:2 | A collection of operation permissions. The format is PermissionGroupID1:PermissionCode1;...;Per missionGroupIDn:PermissionCoden. For example: 1:1;1:2;2:1;2:2. For more information about permission groups and permission codes, see ListAuthority. |
|---|---|---|---|---|---|
| RoleName | String | Query | Yes | testrole | The name of the role. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The returned message. |
| RoleId | Integer | 33 | The ID of the role. |

Request example

```json
POST /pop/v5/account/create_role HTTP/1.1 "ActionData": "15:1;14:2", "RoleName": "testrole"
```

Successful response example

```json
<RoleId>33</RoleId>
    "Message": "success",
    "RoleId": 33,
    "Code": 200
```

##### 1.1.11.7 ListRole

Call the ListRole operation to retrieve a list of roles.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common parameters.

```
POST /pop/v5/account/role_list HTTP/1.1
```

This operation has no request parameters.

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. |
| Message | String | success | The response message. |
| RoleList | Array of RoleItem |   | The list of roles. |
| RoleItem |   |   |   |
| ActionList | Array of Action |   | The collection of operation permissions. |
| Action |   |   |   |
| Code | String | 1 | The permission code. |
| Description | String | Operation record | The permission description. |
| GroupId | String | 31 | The ID of the permission group. |
| Name | String | Operation record | The name of the permission. |
| Role | Struct |   | The list of roles. |
| AdminUserId | String | test**@aliyun.com | The ID of the Alibaba Cloud account. |
| CreateTime | Long | 1542717260156 | The UNIX timestamp that indicates when the role was created. |
| Id | Integer | 1 | The ID of the role. |
| IsDefault | Boolean | false | Indicates whether the role is a default role. |
| Name | String | Super Admin(All privileges) | The name of the role. |
| UpdateTime | Long | 1542717260156 | The UNIX timestamp that indicates when the role was last updated. |

Request example

```
POST /pop/v5/account/role_list HTTP/1.1
```

Response example

```json
<RoleList>
    <ActionList>
        <Description>Operation record</Description>
        <Code>1</Code>
        <Name>Operation record</Name>
        <GroupId>31</GroupId>
    </ActionList>
    <Role>
        <IsDefault>false</IsDefault>
        <CreateTime>1542717260156</CreateTime>
        <UpdateTime>1542717260156</UpdateTime>
        <AdminUserId>test**@aliyun.com</AdminUserId>
        <Id>1</Id>
        <Name>Super Admin(All privileges)</Name>
    </Role>
</RoleList>
    "Message": "success",
    "RoleList": {
        "ActionList": {
            "Description": "Operation record",
            "Code": 1,
            "Name": "Operation record",
            "GroupId": 31
```

`},`

```json
        "Role": {
            "IsDefault": false,
            "CreateTime": 1542717260156,
            "UpdateTime": 1542717260156,
            "AdminUserId": "test**@aliyun.com",
            "Id": 1,
            "Name": "Super Admin(All privileges)"
```

`},`

```json
    "Code": 200
```

#### 1.1.12 Configuration management

##### 1.1.12.1 GetJavaStartUpConfig

Call the GetJavaStartUpConfig operation to retrieve the Java startup parameter settings for an application.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/oam/java_start_up_config HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 5fdf50e8-* | The ID of the application. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | success | The returned message. |

| ence |   |   | Service (EDAS |
|---|---|---|---|
| Parameter | Type | Example | Description |

| RequestId | String | 4823-bhjf-23u4-eiufh | The ID of the request. |
|---|---|---|---|
| JavaStartUpConfig | String | { "originalConfigs": " {\"CustomParams\": {\"original\":\"- Dtest=test\",\"startup\":\"- Dtest=test\"}}", "startUpArgs": "- Dtest=test" } | The Java startup parameter settings. |
| Code | Integer | 200 | The status code of the operation or a POP error code. |

Sample request

```
GET /pop/v5/oam/java_start_up_config HTTP/1.1 &AppId=5fdf50e8-* &Common request parameters
```

Sample successful response

```json
 "Message":"success",
 "RequestId":"4823-bhjf-23u4-eiufh",
 "JavaStartUpConfig":"{<br/>\"originalConfigs\": \"{\\\"CustomParams\\\":{\\\"original\\\":\\\"-
Dtest=test\\\",\\\"startup\\\":\\\"-Dtest=test\\\"}}\",<br/>\"startUpArgs\": \"-Dtest=test\"<br/>}",
 "Code":200
}<br/><br/><br/> <RequestId>4823-bhjf-23u4-eiufh</RequestId> <JavaStartUpConfig>{ &quot;originalConfigs&quot;: &quot;{\&quot;CustomParams\&quot;:{\&quot;original\&quot;:\&quot;- Dtest=test\&quot;,\&quot;startup\&quot;:\&quot;-Dtest=test\&quot;}}&quot;, &quot;startUpArgs&quot;: &quot;-Dtest=test&quot; }</JavaStartUpConfig>
```

##### 1.1.12.2 DeleteConfigCenter

Deletes a configuration. Features

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
DELETE /pop/v5/configCenter HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| DataId | String | Query | Yes | dubbo.registry.confi g | The key of the configuration item. |

| Group | String | Query | Yes | dubbo-registry-test | The group of the configuration item. |
|---|---|---|---|---|---|

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code of the request. |
| Message | String | Success | Additional information |

Request example

```json
DELETE /pop/v5/configCenter HTTP/1.1 "DataId": "dubbo.registry.config", "Group": "dubbo-registry-test"
```

Successful response example

```json
{"Message":"Success","Code":"200"}
```

##### 1.1.12.3 InsertConfigCenter

You can call the InsertConfigCenter operation to add a configuration.

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information about common request headers, see Common request parameters.

```
POST /pop/v5/configCenter HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| Data | String | Query | Yes | Hello World | The value of the configuration item. |
| DataId | String | Query | Yes | com.aliyun.acm.exa mple | The key of the configuration item. |
| Group | String | Query | Yes | DEFAULT GROUP _ | The group of the configuration item. |
| LogicalRegionId | String | Query | Yes | cn-beijing:test | The target microservices namespace for the configuration. |
| AppName | String | Query | No | testapp | The name of the target application for the configuration. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code of the request or a POP error code. |
| Message | String | success | Additional information. |
| RequestId | String | a5281053-08e4-47a5- b2ab-5c0323de***** | The ID of the request. |

Request example

```json
POST /pop/v5/configCenter HTTP/1.1 "Data": "Hello World", "DataId": "com.aliyun.acm.example", "Group": "DEFAULT_GROUP ", "LogicalRegionId": "cn-beijing:test"
```

Successful response example

```json
<RequestId>a5281053-08e4-47a5-b2ab-5c0323de*****</RequestId>
    "RequestId": "a5281053-08e4-47a5-b2ab-5c0323de*****",
    "Message": "success",
    "Code": 200
```

##### 1.1.12.4 ListConfigCenters

Lists microservice configurations.

**Request headers**

This operation has no special request headers. For more information, see Common request parameters.

```
GET /pop/v5/configCenters HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| Group | String | Query | Yes | test-group | The microservice configuration group. |
| DataIdPattern | String | Query | No | test* | The regular expression used to match the DataId. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code of the request. This can be an HTTP status code or a POP error code. |

| ConfigCentersList | Array of ListConfigCenters |   | The list of microservice configurations. |
|---|---|---|---|
| ListConfigCenters |   |   |   |
| DataId | String | test1 | The data name. |
| Group | String | test-group | The microservice configuration group. |
| Id | String | 6891** | The unique ID of the microservice configuration. |
| Message | String | success | Additional information. |

Sample request

```json
GET /pop/v5/configCenters HTTP/1.1 "Group": "test-group"
```

Sample responses

```json
<ConfigCentersList>
    <Group>test-group</Group>
    <DataId>test1</DataId>
    <Id>6891**</Id>
</ConfigCentersList>
    "Message": "success",
    "ConfigCentersList": {
        "Group": "test-group",
        "DataId": "test1",
        "Id": "6891**"
```

`},`

```json
    "Code": 200
```

##### 1.1.12.5 DeleteDockerConfigSecret

Deletes a Secret for a custom image.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | String | Query | Yes | b0e014a7-1e7a-42ef-8***** | The ID of the EDAS cluster. |
| K8sNameSpac e | String | Query | Yes | default | The namespace of the Kubernetes cluster. |
| Name | String | Query | Yes | aaa | Secret name |

**Returned Data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The response code. A value of 200 indicates that the request was successful. |
| Message | String | success | Additional information |
| RequestId | String | 132BF104-A660-40C7- 936B-F805967***** | The ID of the request. |
| TraceId | String | 0a98a334170226880xxxxx xx | The trace ID. |
| Data | String | xxxxxxx | Data details |

Sample request

```
DELETE /pop/v5/k8s/secret/docker_config_secret HTTP/1.1 &ClusterId=b0e014a7-1e7a-42ef-8***** &K8sNameSpace=default &Name=aaa &<Common request parameters>
```

Sample response

```json
 "Message":"success",
 "RequestId":"132BF104-A660-40C7-936B-F805967*****",
 "TraceId":"0a98a334170226880xxxxxxx",
 "Data":"xxxxxxx",
 "Code":200
<RequestId>132BF104-A660-40C7-936B-F805967*****</RequestId> <TraceId>0a98a334170226880xxxxxxx</TraceId> <Data>xxxxxxx</Data>
```

##### 1.1.12.6 ListConfigTemplates

Call the ListConfigTemplates operation to retrieve a list of configuration templates.

**Request header**

This operation uses common request headers and has no special request headers. For more information, see the Common request parameters document.

```
GET /pop/v5/config_template HTTP/1.1
```

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| CurrentPage | Long | Query | No | 1 | The page number. Pages start from page 1. |

| PageSize | Long | Query | No | 10 | The number of entries per page. |
|---|---|---|---|---|---|
| Id | Long | Query | No | 3d84efaf-37d9-49fb-a3a8- b38d5c****** | The ID of the configuration template. |
| Name | String | Query | No | config-tmpl-1 | The name of the configuration template. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4D9F-DR94- FD**************** | The ID of the request. |
| Message | String | success | Additional information. |
| Data | Struct |   | The query results. |
| -Result | Array |   | The results. |
| --Id | String | xxxxxx | The ID. |
| --Name | String | xxx | The name. |
| --Format | String | int | The format. |
| --Description | String | Not Found | The description. |
| --Content | String | xxxxxxxxx | The content of the configuration. |
| --GmtCreate | Long | 202108 | The time when the template was created. |
| --GmtModified | Long | 202108 | The time when the template was last updated. |
| -CurrentPage | Integer | 10000 | The current page number. |
| -PageSize | Integer | 1 | The number of entries per page. |
| -TotalSize | Long | 100 | The total number of pages. |
| Code | Integer | 200 | API status code or POP error code. |

Sample request

```
GET /pop/v5/config_template HTTP/1.1 &Common request parameters
```

Sample successful response

```json
 "RequestId":"4D9F-DR94-FD****************",
 "Message":"success",
 "Data":{
  "-Result":{
   "GmtCreate":202108,
   "Format":"int",
   "Description":"Not Found",
   "Content":"xxxxxxxxx",
   "GmtModified":202108,
   "Id":"xxxxxx",
   "Name":"xxx"
```

`},`

```json
  "PageSize":1,
  "CurrentPage":10000,
  "TotalSize":100
```

`},`

```json
 "Code":200
<RequestId>4D9F-DR94-FD****************</RequestId> <Data>
 <-Result>
  <GmtCreate>202108</GmtCreate>
  <Format>int</Format>
  <Description>Not Found</Description>
  <Content>xxxxxxxxx</Content>
  <GmtModified>202108</GmtModified>
  <Id>xxxxxx</Id>
  <Name>xxx</Name>
 </-Result>
 <PageSize>1</PageSize>
 <CurrentPage>10000</CurrentPage>
 <TotalSize>100</TotalSize>
</Data>
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 500 | 605 | Edas.errorcode.PermissionDenied.messag e | You are not authorized to perform the operation. |

##### 1.1.12.7 GetWebContainerConfig

Retrieves the Tomcat configuration for an application.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
GET /pop/v5/oam/web_container_config HTTP/1.1
```

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 5a166fbd-****-**** | The ID of the application. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4823-bhjf-23u4-eiufh | The ID of the request. |
| Message | String | success | Additional information. |
| Code | Integer | 200 | The status of the operation or a POP error code. |
| WebContainerConfig | Struct |   | The content of the Tomcat configuration. |
| -ContextInputType | String | root | The type of the context path. |
| -ContextPath | String | ROOT | The context path. |
| -HttpPort | Integer | 8080 | The HTTP service port. |
| -MaxThreads | Integer | 500 | The maximum number of threads. |
| -ServerXml | String |   | The content of the advanced Server XML configuration. |
| -UriEncoding | String | ISO-8859-1 | The URI encoding type. |
| - UseAdvancedServer Xml | Boolean | true | Indicates whether advanced configurations are used. |
| -UseBodyEncoding | Boolean | true | Indicates whether body character encoding is used. |
| -UseDefaultConfig | Boolean | true | Indicates whether default configurations are used. |

Sample request

```
GET /pop/v5/oam/web_container_config HTTP/1.1 &AppId=5a166fbd-****-**** &Common request parameters
```

Sample response

```json
 "RequestId":"4823-bhjf-23u4-eiufh",
 "Message":"success",
 "Code":200,
 "WebContainerConfig":{
  "HttpPort":8080,
  "UriEncoding":"ISO-8859-1",
  "ContextPath":"ROOT",
  "ContextInputType":"root",
  "ServerXml":"<Server port=*****",
  "UseBodyEncoding":true,
  "MaxThreads":500,
  "UseAdvancedServerXml":true,
  "UseDefaultConfig":true
```

```xml
<RequestId>4823-bhjf-23u4-eiufh</RequestId> <WebContainerConfig>
 <HttpPort>8080</HttpPort>
 <UriEncoding>ISO-8859-1</UriEncoding>
 <ContextPath>ROOT</ContextPath>
 <ContextInputType>root</ContextInputType>
 <ServerXml>&lt;Server port=*****</ServerXml>
 <UseBodyEncoding>true</UseBodyEncoding>
 <MaxThreads>500</MaxThreads>
 <UseAdvancedServerXml>true</UseAdvancedServerXml>
 <UseDefaultConfig>true</UseDefaultConfig>
</WebContainerConfig>
```

#### 1.1.13 Auto Scaling

##### 1.1.13.1 CreateApplicationScalingRule

You can call the CreateApplicationScalingRule operation to create a scaling rule for an application.

**Request headers**

This operation uses only common request headers. For more information, see the common request parameters document.

```
POST /pop/v1/eam/scale/application_scaling_rule HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 78194c76-3dca- 418e-a263- cccd1ab4**** | The ID of the application. Call the ListApplication operation to obtain this ID. |

| ScalingRuleMetric | Json | Query | Yes | {"maxReplicas":3,"m inReplicas":1,"metric s": [{"metricType":"CPU ","metricTargetAvera geUtilization":20}, {"metricType":"MEM ORY","metricTargetA verageUtilization":30 }, {"metricType":"tcpA ctiveConn","metricTa rgetAverageUtilizatio n":20}, {"metricType":"SLB _ QPS","MetricTargetA verageUtilization":25 ,"SlbProject":"aliyun- fc-cn-hangzhou- d95881d9-5d3c- 5f26-a6b8- ************","SlbLog store":"function- log","Vport":"80"}, {"metricType":"SLB _ RT","MetricTargetAv erageUtilization":35, "SlbProject":"aliyun- fc-cn-hangzhou- d95881d9-5d3c- 5f26-a6b8- ************","SlbLog store":"function- log","Vport":"80"}],"s caleUpRules": {"step":"100","disabl ed":false,"stabilizatio nWindowSeconds":0 },"scaleDownRules": {"step":"100","disabl ed":false,"stabilizatio nWindowSeconds":3 00}} | The scaling rule. For more information about the parameters, see ScalingRuleTriggerDTO. |
|---|---|---|---|---|---|
| ScalingRuleName | String | Query | Yes | cpu-trigger | The name of the scaling rule. The name must start with a lowercase letter and can contain lowercase letters, digits, and hyphens (-). The name must be 1 to 32 characters in length. |
| ScalingRuleType | String | Query | Yes | trigger | The type of the scaling rule. Only the `trigger` type is supported. |

public class ScalingRuleTriggerDTO { / * The maximum number of instances. The upper limit is 1000. */ Integer maxReplicas; / The minimum number of instances. The lower limit is 0. */ Integer minReplicas; / * The list of triggers. Multiple triggers are supported. */ List<Trigger> triggers; @Data @ToString @Builder

**@AllArgsConstructor @NoArgsConstructor public static class Trigger { /**

The type of the trigger. Valid values: cron (scheduled) and app_metric (application monitoring). */ String type; / * The name of the trigger. The name must start with a letter and can contain digits, letters, hyphens (-),

**and underscores (_). The name can be up to 30 characters in length. / String name; /**

The metadata of the trigger. This is a JSON map of string-to-string key-value pairs. The supported metadata varies depending on the trigger type.
1. cron
{"period":"weekly","dryRun":"false","timerInDay":{"atTime":"08:00","targetReplicas":2}, {"atTime":"20:00","targetReplicas":1},"timerInWeek":"Sat","Thu"} period: The recurrence period. Valid values are daily, weekly, and monthly. dryRun: If set to false, the system observes and scales the application. If set to true, the system only observes. timerInDay: Specifies the daily scaling cycle. You can specify points in time during the day to scale the application to a target number of replicas. timerInWeek: The day of the week for the scaling rule to take effect. For example, Fri.
2. app_metric
{\"metricName\":\"arms_appstat.incall_QPS\",\"dryRun\":\"false\",\"targetValAvg\":\"true\",\"targetAverageValue\":\"100\"} metricName: arms_appstat.incall_QPS (queries per second, QPS) arms_appstat.incall_rt (response time, RT) arms_appstat.system_CPU (CPU usage) arms_appstat.system_MEM (memory usage) dryRun: Same as for the cron type. targetValAvg: Specifies whether to use the average value of the metric. Set this parameter to `true` to use the average value. This parameter must be set to `true` for QPS and `false` for other metrics. targetAverageValue/targetValue: The threshold of the metric. If `targetValAvg` is set to `true`, use `targetAverageValue`. Otherwise, use `targetValue`. */ String metadata;

**Returned data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code. |
| Data | String | "" | The returned data. You can ignore this parameter. Determine the result based on the `Code` parameter. |
| Message | String | success | The returned message. |
| RequestId | String | a5281053-08e4-47a5- b2ab-5c0323de**** | The unique ID of the request. |
| TraceId | String | c6459282-6a4d-4413- 894c-e4ea3968**** | The ID passed from the event source. This ID is used for troubleshooting. |

Sample request

```json
POST /pop/v1/eam/scale/application_scaling_rule HTTP/1.1 "AppId": "78194c76-3dca-418e-a263-cccd1ab4****", "ScalingRuleMetric": "", "ScalingRuleName": "cpu-trigger", "ScalingRuleType": "trigger"
```

Sample responses

```json
<RequestId>a5281053-08e4-47a5-b2ab-5c0323de****</RequestId> <TraceId>c6459282-6a4d-4413-894c-e4ea3968****</TraceId> <Data/> {"RequestId":"a5281053-08e4-47a5-b2ab-5c0323de****","Message":"success","TraceId":"c6459282-6a4d-4413-894c-e4ea3968**
**","Data":"","Code":"200"}
```

##### 1.1.13.2 DeleteApplicationScalingRule

Call the DeleteApplicationScalingRule operation to delete an Auto Scaling rule for an application. This topic describes the authorization information for this API. You can add this information to the Action element of a Resource Access Management (RAM) policy statement to grant a RAM user or RAM role the permissions to call this API. This information includes the following: Operation: The specific permission. Access level: The access level of each operation. Valid values are Write, Read, and List. Resource type: The resource type that supports authorization for the operation.
  - Required resource types are in bold.
Condition key: The condition key defined by the cloud product. Associated operation: Other permissions required for the operation to succeed. You must have the permissions for the associated operations to successfully call this operation.

**Request headers**

This operation uses common request headers and does not have any special request headers. For more information, see the documentation about common request parameters.

```
DELETE /pop/v1/eam/scale/application_scaling_rule HTTP/1.1
```

| Name | Type | Positio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | 78194c76-3dca- 418e-a263- cccd1ab4**** | The ID of the application. Call the ListApplication operation to obtain this ID. |
| ScalingRuleName | String | Query | Yes | cpu-trigger | cpu-trigger |

Name | Type | Required | Description | Example Value

| ------- | ------- | ------ | -------- |   |
|---|---|---|---|---|
| ScalingRuleName | string | No | The name of the Auto Scaling policy. | cpu-trigger |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The return code. A value of 200 indicates that the request was successful. |
| Data | String | true | The data returned. The result of the operation is determined by the `Code` parameter. |
| Message | String | Abnormal parameters | The error message returned if the request fails. |
| RequestId | String | 5d6fa0bc-cc3********** | The unique ID of the request. |
| TraceId | String | ab1680******** | The ID of the call chain. |

Example request

```json
DELETE /pop/v1/eam/scale/application_scaling_rule HTTP/1.1 "AppId": "78194c76-3dca-418e-a263-cccd1ab4****", "ScalingRuleName": "cpu-trigger"
```

Example response

```json
<RequestId>5d6fa0bc-cc3**********</RequestId> {"RequestId":"5d6fa0bc-cc3**********","Message":"","TraceId":"","Data":"","Code":""}
```

##### 1.1.13.3 DisableApplicationScalingRule

You can call the DisableApplicationScalingRule operation to disable an auto scaling policy.

**Request header**

This operation uses only common request headers. For more information, see Common parameters.

```
PUT /pop/v1/eam/scale/disable_application_scaling_rule HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | a23dc-* | The ID of the EDAS application. |
| ScalingRuleName | String | Query | Yes | mem-85 | The name of the scaling rule. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. A value of 200 indicates that the request was successful. |
| Data | String | true | The data returned. This parameter is not used. Check the value of the Code parameter to determine whether the request was successful. |
| Message | String | The request parameters are invalid. | The error message returned if the value of Code is not 200. |
| RequestId | String | 8FAD132C-* | The unique ID of the request. |
| TraceId | String | ae13688-* | The call chain ID of the request. |

Sample request

```json
PUT /pop/v1/eam/scale/disable_application_scaling_rule HTTP/1.1 "AppId": "a23dc-*", "ScalingRuleName": "mem-85"
```

Sample response

```json
{"RequestId":"8FAD132C-*","Message":"Invalid request parameters","TraceId":"ae13688-*","Data":"true","Code":"200"}
```

##### 1.1.13.4 EnableApplicationScalingRule

Enables a scaling rule for an application.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

```
PUT /pop/v1/eam/scale/enable_application_scaling_rule HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | a1789*** | The ID of the application. |
| ScalingRuleName | String | Query | Yes | mem-85 | The name of the scaling rule. |

**Return data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The status code returned. A value of 200 indicates that the request was successful. Other values indicate that the request failed. |
| Data | String | "" | The data returned. This parameter is not used. Use the Code parameter to determine the result of the operation. |
| Message | String | The application does not exist. | The error message that is returned when the value of Code is not 200. |
| RequestId | String | AE78* | The unique ID of the request. |
| TraceId | String | ab202209* | The ID of the call chain. |

Request example

```json
PUT /pop/v1/eam/scale/enable_application_scaling_rule HTTP/1.1 "AppId": "", "ScalingRuleName": ""
```

Successful response example

```json
{"RequestId":"AE78*","Message":"The application does not exist.","TraceId":"ab202209*","Data":"\"\"","Code":"200"}
```

##### 1.1.13.5 UpdateApplicationScalingRule

Updates a scaling rule.

**Request headers**

This operation uses common request headers and has no special request headers. For more information, see Common request parameters.

```
PUT /pop/v1/eam/scale/application_scaling_rule HTTP/1.1
```

| Name | Type | Locatio n | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | a13270bdef-* | The ID of the application. Call the ListApplication operation to obtain this ID. |
| ScalingRuleMetric | Json | Query | Yes | {"maxReplicas":3,"m inReplicas":1,"metric s": [{"metricType":"CPU ","metricTargetAvera geUtilization":20}, {"metricType":"MEM ORY","metricTargetA verageUtilization":30 }, {"metricType":"tcpA ctiveConn","metricTa rgetAverageUtilizatio n":20}, {"metricType":"SLB _ QPS","MetricTargetA verageUtilization":25 ,"SlbProject":"aliyun- fc-cn-hangzhou- d95881d9-5d3c- 5f26-a6b8- ************","SlbLog store":"function- log","Vport":"80"}, {"metricType":"SLB _ RT","MetricTargetAv erageUtilization":35, "SlbProject":"aliyun- fc-cn-hangzhou- d95881d9-5d3c- 5f26-a6b8- ************","SlbLog store":"function- log","Vport":"80"}],"s caleUpRules": {"step":"100","disabl ed":false,"stabilizatio nWindowSeconds":0 },"scaleDownRules": {"step":"100","disabl ed":false,"stabilizatio nWindowSeconds":3 00}} | The scaling rule. For more information about the parameters, see the description of `ScalingRuleTriggerDTO`. |
| ScalingRuleName | String | Query | Yes | cpu-99 | The name of the scaling rule. |
| ScalingRuleType | String | Query | Yes | trigger | The trigger type. Only `trigger` is supported. |

public class ScalingRuleTriggerDTO { /* * The maximum number of replicas. The upper limit is 1,000. */ Integer maxReplicas; /* The minimum number of replicas. The lower limit is 0. */ Integer minReplicas; /* * A list of triggers. Multiple triggers are supported. */ List<Trigger> triggers; @Data @ToString @Builder

**@AllArgsConstructor @NoArgsConstructor public static class Trigger { /**

The trigger type. Valid values: `cron` (scheduled) and `app_metric` (application monitoring). */ String type; /* * The name of the trigger. It must start with a letter and can contain digits, letters, hyphens (-), and

**underscores (_). The name can be up to 30 characters long. / String name; /**

The trigger metadata. This parameter is a map in JSON format that contains key-value pairs of the string type. The supported metadata varies depending on the trigger type.
1. cron
{"period":"weekly","dryRun":"false","timerInDay":{"atTime":"08:00","targetReplicas":2}, {"atTime":"20:00","targetReplicas":1},"timerInWeek":"Sat","Thu"} `period`: The period. Valid values: `daily`, `weekly`, and `monthly`. `dryRun`: If set to `false`, the system monitors and scales the application. If set to `true`, the system only monitors the application. `timerInDay`: Describes the daily scaling period. It specifies the time to start maintaining a specific number of replicas. `timerInWeek`: The day of the week for the cron expression, such as `Fri`.
2. app_metric
{\"metricName\":\"arms_appstat.incall_QPS\",\"dryRun\":\"false\",\"targetValAvg\":\"true\",\"targetAverageValue\":\"100\"} `metricName`: `arms_appstat.incall_QPS`: Queries per second (QPS). `arms_appstat.incall_rt`: Response time (RT). `arms_appstat.system_CPU`: CPU usage. `arms_appstat.system_MEM`: Memory usage. `dryRun`: Same as for the `cron` type. `targetValAvg`: Specifies whether to calculate the average value. A value of `true` indicates that the average is calculated, while a value of `false` indicates that it is not. Set this parameter to `true` only for QPS. For all other metrics, set it to `false`. `targetAverageValue`/`targetValue`: Use `targetAverageValue` if `targetValAvg` is `true`. Use `targetValue` if `targetValAvg` is `false`. */ String metadata;

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The result code. A value of 200 indicates that the request was successful. |

| Data | String | " {\"maxReplicas\":3,\"minR eplicas\":1,\"metrics\": [{\"metricType\":\"CPU\",\" metricTargetAverageUtiliza tion\":20}, {\"metricType\":\"MEMORY \",\"metricTargetAverageUt ilization\":30}, {\"metricType\":\"tcpActive Conn\",\"metricTargetAver ageUtilization\":20}, {\"metricType\":\"SLB QPS _ \",\"MetricTargetAverageUt ilization\":25,\"SlbProject\": \"aliyun-fc-cn-hangzhou- d95881d9-5d3c-5f26-a6b8- ************\",\"SlbLogstor e\":\"function- log\",\"Vport\":\"80\"}, {\"metricType\":\"SLB RT\" _ ,\"MetricTargetAverageUtili zation\":35,\"SlbProject\":\" aliyun-fc-cn-hangzhou- d95881d9-5d3c-5f26-a6b8- ************\",\"SlbLogstor e\":\"function- log\",\"Vport\":\"80\"}],\"sc aleUpRules\": {\"step\":\"100\",\"disabled \":false,\"stabilizationWind owSeconds\":0},\"scaleDo wnRules\": {\"step\":\"100\",\"disabled \":false,\"stabilizationWind owSeconds\":300}}" | The returned result. You can ignore this parameter and determine whether the request was successful based on the `Code` parameter. |
|---|---|---|---|
| Message | String | The parameter is invalid. | The error message that is returned when the value of `Code` is not 200. |
| RequestId | String | ABE0198-* | The unique ID of the request. |
| TraceId | String | ab20220917* | The call chain ID of the request. |

Request example

```json
PUT /pop/v1/eam/scale/application_scaling_rule HTTP/1.1 "AppId": "", "ScalingRuleMetric": "", "ScalingRuleName": "", "ScalingRuleType": ""
```

Response example Format: `JSON`

```json
{"RequestId":"ABE0198-*","Message":"The parameter is invalid.","TraceId":"ab20220917*","Data":"\" {\\\"maxReplicas\\\":3,\\\"minReplicas\\\":1,\\\"metrics\\\": [{\\\"metricType\\\":\\\"CPU\\\",\\\"metricTargetAverageUtilization\\\":20}, {\\\"metricType\\\":\\\"MEMORY\\\",\\\"metricTargetAverageUtilization\\\":30}, {\\\"metricType\\\":\\\"tcpActiveConn\\\",\\\"metricTargetAverageUtilization\\\":20}, {\\\"metricType\\\":\\\"SLB_QPS\\\",\\\"MetricTargetAverageUtilization\\\":25,\\\"SlbProject\\\":\\\"aliyun-fc-cn-han gzhou-d95881d9-5d3c-5f26-a6b8-************\\\",\\\"SlbLogstore\\\":\\\"function-log\\\",\\\"Vport\\\":\\\"80\\\"},{\\ \"metricType\\\":\\\"SLB_RT\\\",\\\"MetricTargetAverageUtilization\\\":35,\\\"SlbProject\\\":\\\"aliyun-fc-cn-hangzho u-d95881d9-5d3c-5f26-a6b8-************\\\",\\\"SlbLogstore\\\":\\\"functionlog\\\",\\\"Vport\\\":\\\"80\\\"}],\\\"scaleUpRules\\\": {\\\"step\\\":\\\"100\\\",\\\"disabled\\\":false,\\\"stabilizationWindowSeconds\\\":0},\\\"scaleDownRules\\\":{\\\"st ep\\\":\\\"100\\\",\\\"disabled\\\":false,\\\"stabilizationWindowSeconds\\\":300}}\"","Code":"200"}
```

##### 1.1.13.6 DescribeApplicationScalingRules

Call the DescribeApplicationScalingRules operation to retrieve a list of Auto Scaling rules.

**Request headers**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

```
GET /pop/v1/eam/scale/application_scaling_rules HTTP/1.1
```

| Parameter | Type | Location | Required | Example | Description |
|---|---|---|---|---|---|
| AppId | String | Query | Yes | a43454-* | The ID of the application. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | Integer | 200 | The HTTP status code. A value of 200 indicates that the request is successful. |
| Message | String | The application does not exist | The error message returned. This parameter is returned only if the request fails. |
| RequestId | String | AEC870*** | The ID of the request. |
| TraceId | String | ae202209**** | The ID of the call chain. |
| Data | String | " {\"CurrentPage\":1,\"PageS ize\":10,\"TotalSize\":20,\"R esult\": [{\"UpdateTime\":2321232 3123,\"CreateTime\":2321 2323123,\"AppId\":\"78194 c76-3dca-418e-a263- cccd1ab4****\",\"LastDisab leTime\":23212323123,\"M axReplicas\":1,\"ScaleRule Enabled\":true,\"ScaleRule Type\":\"trigger\",\"MinRepl icas\":1,\"ScaleRuleName\" :\"cpu-trigger\",\"Metric\": {\"MinReplicas\":1,\"MaxRe plicas\":1,\"Metrics\": [{\"MetricTargetAverageUt ilization\":1,\"MetricType\": \"asd\"}]},\"Trigger\": {\"MinReplicas\":1,\"MaxRe plicas\":122,\"Triggers\": [{\"Type\":\"cron\",\"MetaD ata\":\" {\\\"dryRun\\\":true}\",\"Na me\":\"cron- trigger\"}]}}]}" | The list of Auto Scaling rules. |

Sample request

```
GET /pop/v1/eam/scale/application_scaling_rules HTTP/1.1 &AppId=a43454-* &<Common request parameters>
```

Sample response

```json
 "Message":"The application does not exist",
 "RequestId":"AEC870***",
 "TraceId":"ae202209****",
 "Data":"\"{\\\"CurrentPage\\\":1,\\\"PageSize\\\":10,\\\"TotalSize\\\":20,\\\"Result\\\":
[{\\\"UpdateTime\\\":23212323123,\\\"CreateTime\\\":23212323123,\\\"AppId\\\":\\\"78194c76-3dca-418e-a263-cccd1ab4*** *\\\",\\\"LastDisableTime\\\":23212323123,\\\"MaxReplicas\\\":1,\\\"ScaleRuleEnabled\\\":true,\\\"ScaleRuleType\\\":\\\ igger\\\",\\\"MinReplicas\\\":1,\\\"ScaleRuleName\\\":\\\"cpu-trigger\\\",\\\"Metric\\\": {\\\"MinReplicas\\\":1,\\\"MaxReplicas\\\":1,\\\"Metrics\\\": [{\\\"MetricTargetAverageUtilization\\\":1,\\\"MetricType\\\":\\\"asd\\\"}]},\\\"Trigger\\\": {\\\"MinReplicas\\\":1,\\\"MaxReplicas\\\":122,\\\"Triggers\\\":[{\\\"Type\\\":\\\"cron\\\",\\\"MetaData\\\":\\\"{\\\ \\\\"dryRun\\\\\\\":true}\\\",\\\"Name\\\":\\\"cron-trigger\\\"}]}}]}\"",
 "Code":200
```

erence

## 2 SDK reference

### 2.1 Call the Java SDK

#### 2.1.1 Getting Started

This topic describes how to obtain the EDAS Java SDK and start making API calls.

**Prerequisites**

An authorized account and an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, are required. To obtain and view your AccessKey pair in the Apsara Uni-manager Operations Console, see . Obtain the product endpoint. For more information, see . The Apsara Stack Java SDK requires JDK 1.6 or later.

**Install the Apsara Stack Java SDK**

If you use Apache Maven to manage your Java project, you can import the JAR file into the project's pom.xml file. To use the SDK, you must install both the SDK core library and the product-specific SDK. The version of the SDK core library is 3.7.1, and the version of the EDAS SDK is 2.14.0 private.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>3.7.1</version>
            <scope>system</scope>
            <systemPath>${project.basedir}/lib/aliyun-java-sdk-core-3.7.1.jar</systemPath>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-edas</artifactId>
            <version>2.14.0.private</version>
            <scope>system</scope>
            <systemPath>${project.basedir}/lib/aliyun-java-sdk-edas-2.14.0.private.jar</systemPath>
        </dependency>
    </dependencies>
```

**Use the Java SDK**

The following shows the three main steps for using the Apsara Stack Java SDK to make an API call:
1. Create and initialize a DefaultAcsClient instance.
2. Create an API request and set the parameters.
3. Send the request and handle the response or exception.
erence

```
    public static void main(String[] args) throws ClientException{
        /**
         * The endpoint of the OpenAPI. Set this parameter based on the list of EDAS-supported regions and the regi
on where your instance is located.
```

`*/`

```
        String regionId = "XXXXX";
        /**
         * The AccessKey ID for authentication. Get it from the Apsara Uni-manager Operations Console.
```

`*/`

```
        String accessKeyId = "XXXXXXXXXXXXXXXXX";
        /**
         * The AccessKey secret for authentication. Get it from the Apsara Uni-manager Operations Console.
```

`*/`

```
        String accessKeySecret = "XXXXXXXXXXXXXXXXX";
        /**
        * The name of the cloud product to access through the OpenAPI. Set this to Edas.
```

`*/`

```
        String productName ="Edas";
        /**
         * The domain name of the endpoint. For more information, see the domain in the list of EDAS-supported regi
ons.
```

`*/`

```java
        String domain ="edas-api.console.XXXXX.aliyun.com";
        // Build the OpenAPI client.
        DefaultProfile.addEndpoint(regionId,regionId,productName,domain);
        DefaultProfile defaultProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessKeySecret);
        DefaultAcsClient defaultAcsClient = new DefaultAcsClient(defaultProfile);
        defaultAcsClient.setAutoRetry(false);
        // Build the request for the API to list application deployment groups. For information about the request p
arameters, see the API reference.
        String appId = "xxxxxxxxx";
        ListDeployGroupRequest request = new ListDeployGroupRequest();
        // For information about the request parameters, see the API reference.
        request.setAppId(appId);
        ListDeployGroupResponse response = defaultAcsClient.getAcsResponse(request);
        // Parse the result. A code of 200 indicates that the call was successful. Other codes indicate that the ca
ll failed. For more information, see the list of error codes.
        if (response.getCode() == 200) {
            // Parse the specific result. For more information, see the return values of the API.
            List<DeployGroup> deployGroups = response.getDeployGroupList();
            if (CollectionUtils.isNotEmpty(deployGroups)) {
                for (DeployGroup deployGroup : deployGroups) {
                    System.out.println(deployGroup.getGroupName());
                    System.out.println(deployGroup.getGroupId());
        } else {
            // Print the cause of the error.
            System.out.println(response.getMessage());
```

#### 2.1.2 User manual

##### 2.1.2.1 Install the Java SDK

This topic describes how to install and use the Enterprise Distributed Application Service (EDAS) Java SDK. The Apsara Stack Java SDK supports JDK 1.6 and later. You can install the SDK by importing the JAR file. For information about how to obtain the Java SDK package, see Obtain the SDK package for a cloud product. Whether you use Eclipse or IntelliJ as your integrated development environment (IDE), you can install the EDAS Java SDK by importing the JAR package. Install the SDK as follows: Installation in Eclipse To install the EDAS Java SDK in your Eclipse project, perform the following steps: i. Copy the downloaded `aliyun-java-sdk-edas-2.14.0.private.jar` file to your project folder. erence ii. Open your project in Eclipse, right-click the project, and then click **Properties**. iii. In the dialog box that appears, click **Java Build Path > Libraries > Add JARs** to add the downloaded JAR file. iv. Click **Apply and Close**. Installation in IntelliJ To install the Apsara Stack Java SDK in your IntelliJ project, perform the following steps: i. Copy the downloaded `aliyun-java-sdk-edas-2.14.0.private.jar` file to your project folder. ii. Open your project in IntelliJ. On the menu bar, click **File > Project Structure**. iii. Click **Apply**, and then click **OK**.

##### 2.1.2.2 Configure authentication credentials

When you use an Apsara Stack software development kit (SDK) to access Apsara Stack services, you must provide credentials from an authorized account for authentication. If you use an AccessKey pair as access credentials, set the credentials when you initialize the client.

> **Important:** Do not leak code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your Apsara Stack account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<your-region-id>",          // The region ID.
    "<your-access-key-id>",      // The AccessKey ID.
    "<your-access-key-secret>"); // The AccessKey secret.
```

##### 2.1.2.3 Initiate a call

This topic describes how to use the EDAS Java SDK to initiate a request.

**Procedure**

1. Create an AcsClient.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The request class naming convention is ${apiName}Request . **${apiName}** is the API name, such as ListApplicationRequest. When multiple SDKs are used, different requests may have the same name. Therefore, differentiate the requests based on the package size.

```
ListApplicationRequestRequest request = new ListApplicationRequestRequest(); request.setPageSize(10);
```

3. Initiate a call and return a response after processing.

```java
ListApplicationRequestResponse response; try {
    response = client.getAcsResponse(request);
    for (ListApplicationRequestResponse.Instance instance:response.getInstances()) {
        System.out.println(instance.getPublicIpAddress());
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
```

All the returned fields are deserialized into the response. You can directly call `response.getXXX()` to retrieve the response fields.

```
instanceStatus := response.getStatus()
```

However, if an exception occurs or you want to retrieve the original HTTP response, use `doAction()` to retrieve the original response.

```
HttpResponse response = client.doAction(request);
```

##### 2.1.2.4 Handle exceptions

erence When using the Java SDK, if EDAS or the SDK client encounters an exception, the corresponding exception information is returned. An SDK client refers to either a provider or consumer that has the SDK installed. The exception information contains error details, such as error codes and error messages. Among the errors returned by the EDAS Java SDK, you do not need to handle the SDK errors. Instead, you need only to handle EDAS-related exceptions based on the error messages. `ServerException` is the error message for EDAS. `ClientException` is the error message for the SDK client. For example, if the following exception occurs, you can modify the AccessKeyId based on the error message.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you need to handle SDK exceptions, develop your code by referring to the following example:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handles the response.
    //...
}catch (ServerException e){
    // You can add your own exception handling logic here.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the problem persists, you can open a ticket with the request ID included.
    System.out.println("ResponseId=" + e.getRequestId());
} catch (ClientException e) {
    // You can add your own exception handling logic here.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

##### 2.1.2.5 Common errors

This topic lists the causes and solutions for some common errors you may experience when you use the SDK.

|   |   | Error code |   |   |   |   | Error message |   |   |   | Cause | Solution |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   | SDK.CanNotResolveEnd |   |   |   |   | Can not resolve |   |   |   |   | Check whether the specified region ID and endpoint are correct. After you have obtained the correct endpoint, you can use the following code to set the endpoint: DefaultProfile.addEndpoint("your-region- id", "your-region-id", "product", "endpoint""); |   |
|   |   |   |   |   |   |   |   | Can not resolve |   |   | The error message | endpoint, endpoint: |   |
|   |   |   | SDK.C |   |   | anNotResolveEnd | endp |   |   | oint, please | returned because SDK cannot acce |   |   |
|   |   | point |   |   |   |   | check the user |   |   |   |   |   |   |
|   |   |   |   |   |   |   | guide |   |   |   |   |   |   |
|   |   | SDK.JsonUnmarshalErr |   |   |   |   |   |   |   |   | The error message returned because the SDK failed to deserialize the response from the API. In most cases, deserialization failures occur because the structure of the response received by the SDK does not match the API metadata, such as mismatched fields or invalid formats. | You can use the client.doAction(request) method to obtain the original HTTP response. |   |
|   |   |   | SDK.JsonUnmarshalErr |   |   |   |   |   | Failed to unmarshal |   | deseria occur b |   |   |
|   |   | or |   |   |   |   | response |   |   |   |   |   |   |
|   |   |   |   |   |   |   | The request timed |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | The request timed |   |   |   |   |   |
|   |   |   |   |   |   |   | out 4 times(3 for |   |   |   | The error message |   |   |
|   |   | SDK.TimeoutError |   |   |   |   | retry), perhaps we |   |   |   | returned because the | In scenarios such recommend that |   |
|   |   |   |   |   |   |   | should have the |   |   |   | request timed out and |   |   |
|   |   |   |   |   |   |   | threshold raised a |   |   |   | all r |   |   |
|   |   |   |   |   |   |   | little? |   |   |   |   |   |   |

erence

|   |   |   |   |   |   | Your request is |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | Your request is |   |   |   |   |   |
|   |   |   |   |   |   | denied as lack of |   |   |   |   |   |   |
|   |   |   |   |   |   | ssl |   |   |   |   |   |   |
|   |   |   |   |   |   | protect.Recommend:htt |   |   | The error message | Before you send the request, add the following code: |   |   |
|   |   |   | SDK.ServerError:Inva |   |   | ps://error- |   |   | returned because the |   | request.setProtocol(ProtocolType.HTTPS) |   |
|   |   | lidProtocol.NeedSsl |   |   |   | center.aliyun.com/sta |   |   | API supports only HTTPS |   |   |   |
|   |   |   |   |   |   | tus/search? |   |   | requests. |   |   |   |
|   |   |   |   |   |   | Keyword=InvalidProtoc |   |   |   |   |   |   |
|   |   |   |   |   |   | ol.NeedSsl&source=Pop |   |   |   |   |   |   |
|   |   |   |   |   |   | Gw |   |   |   |   |   |   |

### 2.2 Call the EDAS Python SDK

#### 2.2.1 Getting started

This topic describes how to obtain and use the Enterprise Distributed Application Service (EDAS) Python SDK.

**Prerequisites**

An authorized account and an AccessKey pair (an AccessKey ID and an AccessKey secret). For more information about how to obtain and view your AccessKey pair in the Apsara Uni-manager Operations Console, see . The product endpoint. For more information, see .

**Install the Python SDK**

Follow these steps to install the Python SDK:
1. Install the SDK core library.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip install aliyun-python-sdk-core-v3
```

2. Install the EDAS SDK.
Run the following command:

```
pip install aliyun-python-sdk-edas
```

**Use the Python SDK**

The following steps describe how to make a call using the Python SDK:
1. Create a Client instance. You must provide the region ID, AccessKey ID, and AccessKey secret when you create the
instance.
2. Create an API request and set the parameters.
3. Initiate the call and handle the response or exception.
erence

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
region_id = 'xxxxx' secret_id = 'xxxxx' secret_key = 'xxxxx'
# product config
product_name = 'Edas' endpoint = 'edas.example.com'
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(secret_id, secret_key, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json')
# get response
response = clt.do_action_with_exception(request) print response
```

#### 2.2.2 User manual

##### 2.2.2.1 Install the SDK for Python

This document describes how to install and use the EDAS SDK for Python. The SDK for Python supports Python 2.6.x, 2.7.x, 3.x, and later. You can install the SDK in several ways: Install using pip (Recommended) You can run the following commands to install the SDK using pip.

```
pip install aliyun-python-sdk-core # Install the Alibaba Cloud SDK core library pip install aliyun-python-sdk-edas # Install the EDAS SDK
```

| Note If you use Python 3.x, change pip install aliyun-python-sdk-core to pip install aliyun-python-sdk- core-v3 . |   |   |
|---|---|---|
|   | pip install aliyun-python-sdk- |   |

Install from GitHub You can obtain the SDK code and install it. For more information about how to obtain the SDK package, see Obtain SDK data packets for cloud products.

```bash
git clone https://github.com/aliyun/aliyun-openapi-python-sdk.git
# Install the SDK core library
cd aliyun-python-sdk-core python setup.py install
# Install the EDAS SDK
cd aliyun-python-sdk-edas python setup.py install
```

Install from source code i. You can download and decompress the SDK package from the Apsara Stack O&M API platform. For more information about how to obtain the SDK package, see Obtain SDK data packets for cloud products. ii. You can install the package using one of the following methods: You can modify sys.path to add the directory where you decompressed the SDK package. For example:

```
>>> import sys >>> sys.path.append('/Users/michael/my_py_scripts')
```

> **Note:** This change is temporary and only applies to the current runtime session.

erence You can set the PYTHONPATH environment variable to include the directory where you decompressed the SDK package. The content of this environment variable is automatically added to the module search path. You can set the PYTHONPATH environment variable in the same way that you set the Path environment variable. You can place the decompressed SDK package in your project. You can then use the SDK in the project.

##### 2.2.2.2 Set authentication credentials

When you use an Alibaba Cloud software development kit (SDK) to access Apsara Stack services, you must provide an authorized account for identity verification. The Python SDK uses an AccessKey for identity verification. For more information, see . To use an AccessKey as an access credential, set the credential during client initialization.

> **Important:** Ensure that code containing your AccessKey is not leaked. For example, do not commit it to a public GitHub project. Otherwise, the security of your account will be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

##### 2.2.2.3 Initiate a call

This topic describes how to use the EDAS Python SDK to initiate a request.

**Procedure**

1. Import the EDAS Python SDK.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkedas.request.v20170801 import ListAliyunRegionRequest
```

2. Create an AcsClient.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(secret_id, secret_key, region_id)
```

3. Create a request object.

```
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json')
```

4. Initiate a call and return a response after processing.

```
response = clt.do_action_with_exception(request) print response
```

##### 2.2.2.4 Set HTTPS requests

The EDAS Python SDK allows you to initiate API requests over HTTP and HTTPS. When using the EDAS Python SDK, you can specify a protocol, either HTTP or HTTPS, for specific requests, or set a global protocol for all requests.

> **Note:** If you specify a protocol for a service, the specified protocol takes precedence.

**Add OpenSSL support**

The HTTPS protocol for the EDAS Python SDK is dependent on the OpenSSL support in Python. To use the EDAS Python SDK to send HTTPS requests, you must add the OpenSSL dependency for Python. Run the `python -c "import` `ssl"` command to make sure that the OpenSSL dependency is added. If the error message

```
 ImportError: No module named
```

`ssl` is not displayed, then the OpenSSL dependency has been added. If OpenSSL is not available, run the following command to install it:

```
pip install pyopenssl
```

**Set the protocol to HTTP or HTTPS for a request**

Call an API over HTTPS by referring to the following sample code: erence

```bash
request = CreateInstanceRequest.CreateInstanceRequest() request.set_protocol_type("https")
# Valid values: "https" or "http".
```

**Set a default protocol for all requests globally**

The following code provides an example of how to set a default protocol for all requests globally:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

##### 2.2.2.5 Handle exceptions

When using the Python SDK, if EDAS or the SDK client encounters an exception, the corresponding exception information is returned. An SDK client refers to either a provider or consumer that has the SDK installed. The exception information contains error details, such as error codes and error messages. Among the errors returned by the EDAS Python SDK, you do not need to handle the SDK errors. Instead, you need only to handle EDAS-related exceptions based on the error messages. `ServerException` is the error message for EDAS. `ClientException` is the error message for the SDK client. For example, if the following exception occurs, you can modify the AccessKeyId based on the error message.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

If you need to handle SDK exceptions, develop your code by referring to the following example:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # You can add your own exception handling logic here.
    # For example, print the error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

##### 2.2.2.6 Errors and troubleshooting

This topic describes how to troubleshoot common errors you may encounter during the use of SDKs.

|   |   |   | Error code |   |   |   |   | Error message |   |   | Cause | Solution |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   | SDK.InvalidRegionId |   |   |   |   | Can not find |   |   | The SDK cannot automatically obtain the endpoint of the called service in the specified region. | Check whether the provided region ID and endpoint are correct. Use the following code to set the endpoint: from aliyunsdkcore.profile import region_provider region_provider.modify_point('product_name' , 'region_id', 'endpoint') |   |   |   |
|   |   |   |   | SDK.InvalidRegionId |   |   |   |   | Can not find |   | automatically endpoint of t |   |   |   |   |
|   |   |   |   |   |   |   |   | endpoint to access. |   |   |   |   |   |   |   |
|   |   |   | SDK.TimeoutError |   |   |   |   | — |   |   | The request times out and all retry attempts fail. | In scenarios such as low network quality, we recommend that you increase the timeout period or the maximum number of retries. |   |   |   |
|   |   |   |   |   |   |   |   | Your request is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | Your request is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | denied as lack of |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ssl |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | Before sending a request, add the following code: |   |   |   |
|   |   |   |   | SDK.ServerError： |   |   |   | protect.Recommend:h |   | tt | The API only accepts |   |   |   |   |
|   |   |   | InvalidProtocol.NeedS |   |   |   |   |   | ps://error- |   | HTTPS requests but not |   | request.set_protocol_type('https') |   |   |
|   |   |   | sl |   |   |   |   | center.aliyun.com/sta |   |   | HTTP requests. |   |   |   |   |
|   |   |   |   |   |   |   |   | tus/search? |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | Keyword=InvalidProtoc |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ol.NeedSsl&source=Pop |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | Gw |   |   |   |   |   |   |   |

erence

### 2.3 Obtain an EDAS SDK

You can obtain an Enterprise Distributed Application Service (EDAS) SDK from the API Tools console.

**Background information**

You can download the EDAS SDK for Java or EDAS SDK for Python from the **API Tools console**.
1. Log on to the API Tool console.
2. In the left-side navigation pane, click **SDK Tools**.
3. In the upper-right corner of the page, click **Customize SDK**.
4. In the **Customize SDK** dialog box, set the parameters.

| Parameter | Description |
|---|---|
| Apsara Stack Version | Select an Apsara Stack version from the drop-down list. |
| Product Name | Select a service from the drop-down list. |
| API Version | Select an API version from the drop-down list. |
| Language | Select an SDK language. EDAS supports Java and Python. |

5. Click **Preview API** to view the operations of the specified API version.
6. Click **Create SDK**.
7. On the **SDK Tools** page, find the SDK and click **Download** in the **Actions** column.
an AccessKey pair

## 3 Obtain an AccessKey pair

This topic describes how to obtain an AccessKey pair.

**Method 1: Obtain the AccessKey pair in the EDAS console**

1. Log on to the Apsara Uni-manager Management Console, click the profile picture in the upper-right corner of the page, and
then select **User Information** from the drop-down list.
2. Obtain the AccessKey pair on the page that appears.

**Method 2: Obtain the AccessKey pair in the Apsara Infrastructure Management**

**console**

1. Log on to the Apsara Uni-manager Operations Console.
For more information about how to log on to the Apsara Uni-manager Operations Console, see the **Routine Maintenance**
**> Log On To Apsara Infrastructure Management** section of the **O&M Guide**.
2. In the navigation pane on the left, choose **Operations > Cluster Operations**. On the Clusters page, enter
`baseService` in the search box in the **Project** drop-down list to search for the cluster. Click the cluster name that appears.
3. On the **Cluster Details** page, click the **Cluster Resource** tab. Enter
`ummak` in the search box in the **Name** drop-down list to search for the resource. The ummak resource appears. Click **Details** in the **Application Result** column.
4. In the **Application Result** dialog box, view the connection information of the ummak database.
an AccessKey pair
5. Use the mysql command to log on to the ummak database from a virtual machine (VM) in which an EDAS backend
component is deployed or from a terminal server.

```
mysql -h ummak.mysql.minirds.env.shuguang-ops.com -u ummak -P 3070 -p Enter password: Welcome to the MySQL monitor. Commands end with ; or \g. Your MySQL connection id is 316**** Server version: 5.6.39-log Source distribution Type 'help;' or '\h' for help. Type '\c' to clear the current input statement. mysql> use ummak; Database changed mysql> select * from accesskey_table where user_id='100067051211****'\G;
*************************** 1. row ***************************
                access_id: <yourAccessKeyId>
               access_key: <yourAccessKeySecret>
                  user_id: <yourUserId>
                  ower_id: <yourOwerId>
                  version: 17
              create_time: 1570512118957
            modified_time: 1570512118957
              user_remark:
             enabled_flag: 1
              hidden_flag: 0
             deleted_flag: 0
               oss_status: 0
               ots_status: 0
               rds_status: 0
               oms_status: 0
               cdn_status: 0
            render_status: 0
               mqs_status: 0
                      bid: 26842
              osps_status: 0
               oas_status: 0
               sls_status: 0
        opensearch_status: 0
             video_status: 0
               ons_status: 0
               dpc_status: 0
               ram_status: 0
              odps_status: 0
          access_key_type: symmetric
              expire_time: 0
              mfa_present: 0
                 proxy_id: NULL
trust_proxy_security_info: 0 1 row in set (0.00 sec)
```
