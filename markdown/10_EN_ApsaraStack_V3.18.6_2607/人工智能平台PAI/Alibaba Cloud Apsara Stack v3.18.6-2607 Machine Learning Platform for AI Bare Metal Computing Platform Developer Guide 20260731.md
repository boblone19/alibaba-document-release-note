---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Machine Learning Platform for AI Bare Metal Computing Platform Developer Guide 20260731"
product_version: "V3.18.6_2607"
doc_version: "20260731"
pdf_pages: 355
source_pdf: "7779ada17d41158e_Alibaba Cloud Apsara Stack v3.18.6-2607 Machine Learning Platform for AI Bare Metal Computing Platfo"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%B9%B3%E5%8F%B0PAI/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Machine%20Learning%20Platform%20for%20AI%20Bare%20Metal%20Computing%20Platform%20Developer%20Guide%2020260731.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Machine Learning Platform for AI Bare Metal Computing Platform Developer Guide 20260731

## Table of Contents

- 1 Development overview
- 2 Preparations
- 3 Obtain an AccessKey
- 4 Call API operations by using generic calls
- 5 API reference
  - 5.1 Cluster management
    - 5.1.1 Bare metal - intelligent computing cluster
      - 5.1.1.1 CreateBmcpCluster
      - 5.1.1.2 ListBmcpMachineType
      - 5.1.1.3 ListBmcpCluster
      - 5.1.1.4 DescribeBmcpCluster
      - 5.1.1.5 AddBmcpClusterInstances
      - 5.1.1.6 ListAvailableBmcpInstance
      - 5.1.1.7 DeleteBmcpClusterInstances
      - 5.1.1.8 DeleteBmcpCluster
    - 5.1.2 ACK - intelligent computing cluster
      - 5.1.2.1 CreateAckCluster
      - 5.1.2.2 ListAckCluster
      - 5.1.2.3 DescribeAckCluster
      - 5.1.2.4 AddAckClusterInstances
      - 5.1.2.5 ListAckClusterInstances
      - 5.1.2.6 ListAckClusterNodePool
      - 5.1.2.7 DeleteAckClusterInstances
      - 5.1.2.8 ModifyAckClusterDeletionProtection
      - 5.1.2.9 ListAckInstanceType
      - 5.1.2.10 ListApps
      - 5.1.2.11 DescribeApp
      - 5.1.2.12 GetOssStsToken
      - 5.1.2.13 UploadCustomApp
      - 5.1.2.14 ListCustomApps
      - 5.1.2.15 DescribeCustomApp
      - 5.1.2.16 DeleteCustomApp
      - 5.1.2.17 InstallAiInstanceResource
      - 5.1.2.18 UnInstallAiInstanceResource
      - 5.1.2.19 InstallAiApplication
      - 5.1.2.20 UpgradeAiApplication
      - 5.1.2.21 UnInstallAiApplication
      - 5.1.2.22 ListInstanceTypeDiskCategory
      - 5.1.2.23 ListAckClusterEcsWorkerInstances
      - 5.1.2.24 DescribeAckClusterLogs
      - 5.1.2.25 GetClusterNamespaces
      - 5.1.2.26 ListHistoryEvent
      - 5.1.2.27 ListReStartEvent
      - 5.1.2.28 DeleteAckCluster
    - 5.1.3 Bare metal – supercomputing cluster
      - 5.1.3.1 CreateEhpcCluster
      - 5.1.3.2 ListEhpcCluster
      - 5.1.3.3 DescribeEhpcCluster
      - 5.1.3.4 AddEhpcClusterInstances
      - 5.1.3.5 DeleteEhpcClusterInstances
      - 5.1.3.6 DeleteEhpcCluster
    - 5.1.4 Converged computing cluster
      - 5.1.4.1 CreateBFICluster
      - 5.1.4.2 ListBFICluster
      - 5.1.4.3 DescribeBFICluster
      - 5.1.4.4 ExpandBFICluster
      - 5.1.4.5 ShrinkBFICluster
      - 5.1.4.6 DeleteBFICluster
    - 5.1.5 ListInstance
    - 5.1.6 GetVswitchSwitchMethod
    - 5.1.7 ClusterDryRun
    - 5.1.8 TagResources
    - 5.1.9 RetryFailedInstance
  - 5.2 Storage management
    - 5.2.1 CreateCpfsClientCluster
    - 5.2.2 DescribeCpfsClientClusterType
    - 5.2.3 MountFilesystem
    - 5.2.4 UnmountFilesystem
    - 5.2.5 DeleteCpfsClientCluster
  - 5.3 EVPC
    - 5.3.1 CreateEvpc
    - 5.3.2 ListEvpc
    - 5.3.3 ListEvpcConnections
    - 5.3.4 ModifyEvpc
    - 5.3.5 DeleteEvpc
  - 5.4 Security group
    - 5.4.1 CreateSecurityGroup
    - 5.4.2 ListSecurityGroup
    - 5.4.3 ModifySecurityGroup
    - 5.4.4 DeleteSecurityGroup
    - 5.4.5 AddSecurityGroupRule
    - 5.4.6 ListSecurityGroupRule
    - 5.4.7 ModifySecurityGroupRule
    - 5.4.8 DeleteSecurityGroupRule
    - 5.4.9 AddSecurityGroupInstance
    - 5.4.10 ListSecurityGroupInstance
    - 5.4.11 DeleteSecurityGroupInstance
  - 5.5 Key pair
    - 5.5.1 CreateKeyPair
    - 5.5.2 ListKeyPair
    - 5.5.3 ConfigKeyPair
    - 5.5.4 UnbindKeyPair
    - 5.5.5 DeleteKeyPair
  - 5.6 Elastic cache acceleration
    - 5.6.1 CreateEdaCluster
    - 5.6.2 DeleteEdaCluster
  - 5.7 Data distribution
    - 5.7.1 ListMP2pTask
    - 5.7.2 CreateMP2pTask
    - 5.7.3 DeleteMP2pTask
  - 5.8 Node management
    - 5.8.1 DiagnoseQuery
    - 5.8.2 TaskQuery
    - 5.8.3 DiagnosePoint
  - 5.9 Auto-healing event tickets
    - 5.9.1 ListOrder
    - 5.9.2 GetOrderDetail
    - 5.9.3 UpdateOrder
  - 5.10 Recycle bin
    - 5.10.1 ListRecycleBMCPMachine
    - 5.10.2 RevertMachine
    - 5.10.3 ReleaseMachine

erview

## 1 Development overview

Before you use Bare Metal Computing Platform (BMCP) features, you must understand the productservice names and API versions that are required for different features, as well as the complete workflow. This helps you correctly integrate with and call BMCP.

**Feature call description**

Before you use BMCP API operations to implement a specific feature, you must understand the differences in service names and API versions that are required to call the API operations of different BMCP features.

| ProductService name | API version |
|---|---|
| EasyAI | 2023-11-01 |

**Workflow**

| Preparations Obtain public Obtain the Configure access header parameters endpoint credentials | Make an API call Call the API by SDK |
|---|---|

The following table describes the call workflow.

| Stage | Operatio n | Description |
|---|---|---|
| Preparatio ns | Obtain an AccessKe y | When you call a cloud service API operation, you must provide multiple header parameters, including x-acs-regionid (the region ID), x-acs- organizationid (the organization ID), x-acs-resourcegroupid (the resource group ID), and x-acs-instanceid (the cloud service resource ID). |
|   | Obtain an AccessKe y | When you call a BMCP API operation, you must use the endpoint of the BMCP business domain. You can obtain the endpoint from an Alibaba Cloud on-site O&M engineer or obtain it by yourself. |
|   | Obtain an AccessKe y | Obtain an AccessKey, configure the access credentials as environment variables. Configuring access credentials as environment variables prevents sensitive information from being hardcoded in your code and improves security. |
| Formal call | Call API operation s by using generic calls | Call RPC-style API operations by using generic calls. |

## 2 Preparations

Before you use an SDK to call Bare Metal Computing Platform (BMCP) API operations, you must obtain the access credentials, common headers, and endpoint.

**Obtain common header parameters**

When you call an Apsara Stack API operation, you must provide multiple header parameters. The following table describes the common header parameters.

| Name | Descriptio n | Example | How to obtain |
|---|---|---|---|
| x-acs- regionid | The ID of the region. | cn-********-d01 | 1. Log on to the Apsara Uni-manager Management Console as an administrator. 2. In the top navigation bar, click Enterprise. 3. In the left-side navigation pane, choose Resource Management > Region Management. 4. Click the name of the target organization. 5. View the region ID in the Region List section on the right. |
| x-acs- organizatio nid | The ID of the organization to which the resource belongs. | org- 10385eca88860a d8******** | Important You must obtain these parameters if you use a personal AccessKey pair. You do not need to obtain them if you use an organization AccessKey pair. 1. Log on to the Apsara Uni-manager Management Console as an administrator. 2. In the top navigation bar, click Enterprise. 3. In the left-side navigation pane, choose Resource Management > Organization Management. 4. Click the name of the target organization and view the organization ID in the Basic Information section. 5. On the Resource Group List tab, view the resource group ID in the Resource Group Name/ID column. You can also obtain the organization ID and resource group ID by calling API operations. For more information, see the GetOrganizationList and ListResourceGroup topics in Apsara Uni- manager Development Guide. |
| x-acs- resourcegr oupid | The ID of the resource group to which the resource belongs. | rs- 10385eca8c100a bc******** |   |

| x-acs- instanceid | The ID of the resource on which you want to perform the operation. | bmcp-bpnopt**** | You can obtain the resource ID from the cloud service instance list in the Apsara Uni-manager Management Console. 1. Log on to the Apsara Uni-manager Management Console. 2. In the top navigation bar, choose Products > Computing > Bare Metal Computing Platform (BMCP). 3. In the left-side navigation pane, click Cluster Management and Node Management. 4. View the resource ID, such as a cluster ID or a node ID, in the corresponding resource list. |
|---|---|---|---|

**Note**

For cloud service resource instance API operations that return lists, the response includes the ResourceGroupName (the resource group name), ResourceGroup (the resource group ID), DepartmentName (the organization name), and Department (the organization ID) parameters by default.

**Obtain the endpoint**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Apsara Infrastructure**
**Management > O&M Tools**.
3. On the **Service Registration Variable Dashboard** page, obtain the endpoint of the
required service based on the feature that you want to use. i. Select **Service** and enter **easyAIControllerService**. ii. In the **Service Registration** column of the **easyAIControllerService** service, click the icon, and then click the displayed information. iii. In the **Registration Variables** dialog box, view the value of **EasyAIPopDomain**, which is the `Endpoint` .

**Configure access credentials**

Obtain an AccessKey, configure the access credentials as environment variables. This section uses an AccessKey pair as an example.

| Method | Variable name | Description |
|---|---|---|
| Use an AccessKey pair | ALIBABA CLOUD ACCESS KEY _ _ _ ID and _ ALIBABA CLOUD ACCESS KEY _ _ _ SECRET _ | Use a personal AccessKey pair or an organization AccessKey pair. |

| Use Security Token Service (STS) temporary access credentials | ALIBABA CLOUD ACCESS KEY _ _ _ ID, _ ALIBABA CLOUD ACCESS KEY _ _ _ SECRET, and _ ALIBABA CLOUD SESSION TO _ _ _ KEN | An AccessKey ID obtained from STS starts with STS, for example, STS.**************** . Use the temporary identity credentials that are obtained from STS, which include an AccessKey ID, an AccessKey secret, and a security token. |
|---|---|---|

**Important**

After the configuration is complete, restart or refresh the build and runtime environment, including the IDE, command-line interface, other desktop applications, and background services, to ensure that the latest system environment variables are loaded.

**Linux**

1. Run the following command in the command-line interface to append the environment
variable settings to the ~/.bashrc file.

```
echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```

2. Run the following command to apply the changes.

```
source ~/.bashrc
```

3. Run the following command to check whether the environment variables take effect.

```
echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. Run the following command in the terminal to view the default shell type.

```
echo $SHELL
```

2. Perform operations based on the default shell type.

**Zsh**

i. Run the following command to append the environment variable settings to the ~/.zshrc file.

```
echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
```

ii. Run the following command to apply the changes.

```
source ~/.zshrc
```

iii. Run the following command to check whether the environment variables take effect.

```
echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**Bash**

i. Run the following command to append the environment variable settings to the ~/.bash_profile file.

```
echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_p rofile
```

ii. Run the following command to apply the changes.

```
source ~/.bash_profile
```

iii. Run the following command to check whether the environment variables take effect.

```
echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**Windows**

**CMD**

1. Run the following command in CMD.

```
setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. Run the following command to check whether the environment variables take effect.

```
echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. Run the following command in PowerShell.

```
[Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. Run the following command to check whether the environment variables take effect.

```
[Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

Key

## 3 Obtain an AccessKey

If your application is deployed and runs in a highly secure and stable environment isolated from external attacks, requires long-term access to the service, and requires infrequent credential rotation, you can use an AccessKey pair (consisting of an AccessKey ID and an AccessKey Secret) to initialize the credential provider.

**Background information**

**Warning**

The AccessKey pair of a personal account is a restricted AccessKey pair that is managed by the permission system of the Apsara Uni-manager Management Console. In contrast, an organization AccessKey pair has broader permissions, and administrators must verify the security of the operations. The Apsara Uni-manager Management Console provides both personal and organization AccessKey pairs. (Note that only operations administrators and first-level organization administrators can obtain an organization AccessKey pair.) We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and related cloud services.

**Note**

If you use the AccessKey pair of a personal account, you must add the following parameters to the request header: x-acs-regionid (the region ID), x-acs-organizationid (the organization ID), x-acs-resourcegroupid (the resource group ID), and x-acs-instanceid (the cloud service resource ID). For specific operations, see the preparations topic of each service.

**Obtain the AccessKey pair of a personal account**

1. Log in to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the console, click the profile picture of the current user and then
click **User Information**.
3. In the **AccessKey** section, view the AccessKey information of your personal account.

**Note**

The AccessKey ID and AccessKey Secret are the credentials that you use to access cloud resources. They grant full permissions of the account. Keep them secure.

**Obtain an organization AccessKey pair**

1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprises**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization structure, click the name of the target first-level organization.
5. Click **Manage AccessKey Pairs**.
6. In the dialog box that appears, view the organization AccessKey information.
ns by using generic calls

## 4 Call API operations by using generic calls

**using generic calls**

Bare Metal Computing Platform (BMCP) API operations do not provide SDKs. As an alternative, you can use generic calls. This topic illustrates how to call Remote Procedure Call (RPC)-style API operations via generic calls, with sample code provided for various programming languages.

**Background information**

Generic calls that allow you to call any API operation have the following benefits: Lightweight: You need to install only the Alibaba Cloud core SDK, without the need for individual cloud service SDKs. Simple: You need to construct only a generic request parameter object and then use a generic request client to call a generic function to initiate the request. The response is also returned in a generic format. To initiate a generic call, you must obtain the values of the following parameters from the API reference of the corresponding service: domain: the service endpoint version: the version of the API operation, in the YYYY-MM-DD format. For BMCP, the product name is EasyAI and the API version is 2023-11-01. Operation information: the name of the operation that you want to call. You must obtain the `Action` parameter and specify the API name in the request.

| For example, to call the | DescribeBmcpCluster |   |
|---|---|---|
| setAction("DescribeBmcpCluster") |   |   |
|   |   | to specify |

**Note**

Replace the variables in the sample code in this topic with actual values. Do not retain the angle brackets (<>) in your final code.

**Java example**

**Install the core SDK**

Add the following dependency to the pom.xml file to install the core SDK.

```xml
<dependency>
     <groupId>com.aliyun</groupId>
     <artifactId>aliyun-java-sdk-core</artifactId>
     // You can select a version.
     <version>[(4.0.0,5.0.0)]</version>
</dependency>
```

**Complete example**

The following example calls the DescribeBmcpCluster operation to query the details of a bare metal - intelligent computing cluster. Replace `<your_region_id>` with the ID of the region to which the cluster belongs. The AccessKey pair is obtained from environment variables. Replace `<bmcpDomain>` with the endpoint of BMCP**.** Configure the other variables as needed. ns by using generic calls

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
  public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    DefaultProfile profile = DefaultProfile.getProfile(
      // Your region ID.
      "<your-region-id>",
      // Obtain the AccessKey ID of the RAM user from an environment variable.
      System.getenv("AccessKey"),
      // Obtain the AccessKey secret of the RAM user from an environment variable.
      System.getenv("AccessKeySecret"));
    IAcsClient client = new DefaultAcsClient(profile);
    // Create an API request and set the parameters.
    CommonRequest request = new CommonRequest();
    request.setSysDomain("<bmcpDomain>");
    request.setSysProduct("EasyAI");
    request.setSysVersion("2023-11-01");
    request.setSysAction("DescribeBmcpCluster");
    request.setSysMethod(MethodType.POST);
    request.setProtocol(com.aliyuncs.http.ProtocolType.HTTP);
    request.putQueryParameter("ClusterId", "bmcp-bpnopt****");
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

**Python example**

**Install the core SDK**

Run the following command in the terminal to install the core SDK.

```
pip install aliyun-python-sdk-core
```

**Complete example**

ns by using generic calls The following example calls the DescribeBmcpCluster operation to query the details of a bare metal - intelligent computing cluster. Replace `<your_region_id>` with the ID of the region to which the cluster belongs. The AccessKey pair is obtained from environment variables. Replace `<bmcpDomain>` with the endpoint of BMCP**.** Configure the other variable parameters as needed.

```java
# coding=utf-8
import os from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest class Sample:
    @staticmethod
    def main():
        region_id = "<your_region_id>"
        bmcp_domain = "<bmcpDomain>"
        cluster_id = "bmcp-bpnopt****"
        client = AcsClient(
            os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"],
            os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"],
            region_id,
            verify=False
```

`)`

```python
        request = CommonRequest()
        request.set_domain(bmcp_domain)
        request.set_product("EasyAI")
        request.set_version("2023-11-01")
        request.set_action_name("DescribeBmcpCluster")
        request.set_method("POST")
        request.set_protocol_type("HTTP")
        request.add_body_params("ClusterId", cluster_id)
        response = client.do_action_with_exception(request)
        print(response.decode("utf-8"))
if __name__ == "__main__":
    Sample.main()
```

**Go example**

**Install the core SDK**

Run the following command in the terminal to install the core SDK.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

ns by using generic calls

**Complete example**

The following example calls the DescribeBmcpCluster operation to query the details of a bare metal - intelligent computing cluster. Replace `<your_region_id>` with the ID of the region to which the cluster belongs. The AccessKey pair is obtained from environment variables. Replace `<bmcpDomain>` with the endpoint of BMCP**.** Configure the other variable parameters as needed.

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
 RegionId := "<your_region_id>"
 bmcpDomain := "<bmcpDomain>"
 client, err := sdk.NewClientWithAccessKey(
  RegionId,
  os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
  os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
```

`)`

```
 if err != nil {
  panic(err)
```

`}`

```
 request := requests.NewCommonRequest()
 request.Domain = bmcpDomain
 request.Product = "EasyAI"
 request.Version = "2023-11-01"
 request.ApiName = "DescribeBmcpCluster"
 request.Method = "POST"
 request.Scheme = "http"
 request.QueryParams["ClusterId"] = "bmcp-bpnopt****"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
```

`}`

```
 fmt.Print(response.GetHttpContentString())
```

`}`

## 5 API reference

### 5.1 Cluster management

#### 5.1.1 Bare metal - intelligent computing cluster

**cluster**

##### 5.1.1.1 CreateBmcpCluster

Create a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The cluster name. The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The cluster description. The description must be 0 to 1000 characters in length. |

| Password | Strin g | Quer y | No | Pwd***** | The login password of the machines in the cluster. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters: ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/. |
|---|---|---|---|---|---|
| AddBmsIns tanceList | Json | Quer y | No | null | This parameter is deprecated. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | [ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****", "ActivationId": "a- hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC- 9AB1-890F1234****" } ] | The list of parameters for requesting bare metal servers. This parameter is required when ClusterArchType is set to managed. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the available zone. |

| ClusterArc hType | Strin g | Quer y | No | standard | The cluster type. Valid values: standard: Intelligent computing high- bandwidth network managed: Managed intelligent computing base: Basic intelligent computing aspeed: Intelligent computing training and inference |
|---|---|---|---|---|---|
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal server types to be added to the supercomputing cluster. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| VswitchIdL ist | Json | Quer y | No | null | This parameter is deprecated. |
| StandardV switchId | Strin g | Quer y | No | vsw- 3gagdup8scary04iq**** | The ID of the vSwitch, used to build the management and control service network channel. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard or aspeed. You can call the ListEvpc operation to query the EVPC ID. |
| VolumeId | Strin g | Quer y | No | null | This parameter is deprecated. |
| MountPath | Strin g | Quer y | No | null | This parameter is deprecated. |

| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The ID of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
|---|---|---|---|---|---|
| Activation Code | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The code of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| IsCreateCp fsCluster | Bool ean | Quer y | No | true | Specifies whether to enable the high- performance storage client cluster. Valid values: true: Enable false: Disable Default value: false. This parameter is optional when ClusterArchType is set to standard or aspeed. |
| CpfsCluste rType | Strin g | Quer y | No | CPFS | The type of the high- performance storage client cluster. Valid values: CPFS APFS This parameter is required when IsCreateCpfsCluster is set to true. |

| VolumeInf o | Json | Quer y | No | [ { "VolumeType": "iscsi", "VolumeParams": { "IP": "127.0.0.1", "ServerIQN": "iqn.2023- 04.com.bms:server", "ClientIQN": "", "ChapEnabled": "true", "UserID": "bms", "Password": "xxxx", "LunID": "0", "Description": "", "ClientAttachPath": "/mnt" } }, { "VolumeType": "nfs", "VolumeParams": { "IP": "127.0.0.1", "Description": "", "ServerPath": "/home/nfstestdir", "ClientAttachPath": "/mnt" } }, { "VolumeType": "mount", "VolumeParams": { "Description": "", "ServerPath": "/dev/sdl1", "ClientAttachPath": "/mnt", "MountParams": "--bind" } } ] | The third-party storage mount information. This parameter is optional when ClusterArchType is set to managed. |
|---|---|---|---|---|---|
| IsInstallYu ndunAegis | Bool ean | Quer y | No | true | Specifies whether to enable Aegis. Valid values: true: Enable false: Disable Default value: false. |
| SwitchMet hod | Strin g | Quer y | No | CHSW | The networking mode of the vSwitch. When ClusterArchType is set to standard, base, or aspeed, this parameter must be set to CHSW. When ClusterArchType is set to managed, this parameter can be set to CHSW or HSW. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values: true: Enable false: Disable Default value: false. |

| EvpcEnabl eIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable EVPC IPv6. IPv6 can be enabled only when EvpcId is specified. Valid values: true: Enable false: Disable Default value: false. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp- bpnopt****" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the response. Successful: true Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateBmcpCluster http://[Endpoint]/?Action=CreateEhpcCluster &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-env***-d01 &ZoneId=cn-wulan-env***-****-a &VpcId=vpc-bp1b1xjllp3ve5yze**** &ClusterName=cluster-name &ClusterArchType=standard &MachineTypeList=[
```

`{`

```json
 "MachineType": "test",
 "Arch": "x86",
 "CpuCount": 2,
 "MemCount": 4,
 "FlopsCount": 4.8,
 "VideoMemCount": 5,
 "NodeCount": 10,
 "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&StandardVswitchId=vsw-3gagdup8scary04iq**** &EvpcId=evpc-htchvitxlfjyso**** &ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC**** &ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &IsCreateCpfsCluster=true &CpfsClusterType=CPFS &SwitchMethod=CHSW &EnableIpv6=true &EvpcEnableIpv6=true &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bmcp-bpnopt****",
  "ClusterName":"testname"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <ClusterName>testname</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.1.2 ListBmcpMachineType

Query the list of Bare Metal Computing Platform (BMCP) machine types.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| MachineTy pe | Strin g | Quer y | No | QPG78P4M8G3V.03BB | The machine type name. |
| CPUArch | Strin g | Quer y | No | x86 64 _ | The CPU architecture. Valid values: x86 64 _ arm64 |
| DiskType | Strin g | Quer y | No | cloud ssd _ | The disk type. Valid values: HDD SSD SATA |
| Manufactu rer | Strin g | Quer y | No | NVIDIA | The manufacturer name. |

| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the zone. If this parameter is specified, the number of available standard instances in the specified zone is counted. If this parameter is not specified, the number of available standard instances across all zones for this machine type is counted. |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| DeployTyp es | Json | Quer y | No | "["bmcp"]" | The list of machine type categories to query. Valid values: bmcp: intelligent computing with high- bandwidth networking ehpc: High- Performance Computing (HPC) with high-bandwidth networking base: intelligent computing basic aspeed: training and inference optimization bfi: converged high- bandwidth networking bfi base: converged _ basic |
| Specificati on | Strin g | Quer y | No | gBMC-Ch4ce8hdr | The machine type specification. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |

| errorTitle | String | “” | The error title. |
|---|---|---|---|
| errorMessage | String | "“ | The error message. |
| data | Map | { "PageNumber": 1, "PageSize": 10, "TotalCount": 10, "MachineTypeList": [ { "ratedPower": "1", "memory": 500, "defaultFmin": "", "gpuManufacturer" : "NVIDIA", "CPUNumber": 128, "networkCardType" : "10G", "unitNum": 2, "description": "", "updateTime": "2024-03- 14T10:48:43+08:0 0", "CPUArch": "x86 64", "gpu": _ "T4", "deployType": "bmcp", "manufacturer": "HW", "networkCardNum" : 2, "GpuNum": 4, "disk": 500, "cpuManufacturer": "Hygon", "createTime": "2024-03- 14T10:48:43+08:0 0", "name": "T4", "ID": 2, "diskType": "SSD", "CPUModel": "Hygon C86 7285 32-core Processor", "StandardInstance Count": 10, "Specification": "xxxx" } ] } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListBmcpMachineType &MachineType=MachineType &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{},
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data /> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.1.3 ListBmcpCluster

Query the list of bare metal - intelligent computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt**** | The ID of the cluster. |
| Status | Strin g | Quer y | No | active | The cluster status. Valid values: creating: Creating active: Running createFailed: Creation failed deleting: Deleting deleteFailed: Deletion failed scalingDown: Scaling in scalingDownFailed: Scale-in failed scalingUp: Scaling out scalingUpFailed: Scale- out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| Zone | Strin g | Quer y | No | cn-****-env**-d01-a | The ID of the available zone. |

| ClusterArc hType | Strin g | Quer y | No | standard | The cluster type. Valid values: standard: Intelligent computing high- bandwidth network managed: Managed intelligent computing base: Basic intelligent computing aspeed: Intelligent computing training and inference. |
|---|---|---|---|---|---|
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise Virtual Private Cloud (EVPC). You can call the ListEvpc operation to query the EVPC ID. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
|   |   | { "ClusterList": [ { "Description": "testDescription", "Organization": "5", "IsSetPassword": true, "SwitchMethod": "CHSW", "CpfsClusterType": "APFS", "Gpu": [ { "GpuNum": 32, "GpuModel": "NVIDIA Ampere A _ _ 10 80G NVLink" } _ _ ], "EvpcId": "evpc- pi2q***z8b", "EnableIpv6": true, |   |

|   |   | "FlopsCount": 9984, "Department": 5, "CpuCount": 512, |   |
|---|---|---|---|
| data | Map | "ClusterName": "cluster-name", "ResourceGroup": 4, "Status": "active", "ActiveNodeCount" : 4, "NodeCount": 4, "ClusterId": "bmcp- v8***QVZT", "Zone": "cn-wulan- env***-d01-a", "CreateTime": "2026-01- 12T10:44:46+08:0 0", "Specification": [ { "Count": 3, "Name": "gBMC- Ci8af8nbr" } ], "CpfsClusterState": "active", "AscmCreateUser": "admin", "MemCount": 8192, "ClusterArchType": "standard", "VpcId": "vpc- 7kkjbu****od7pxs6 10", "OldClusterBzid": "", "UpdateTime": "2026-01- 22T15:58:01+08:0 0", "Region": "cn- wulan-env***-d01", "CpfsMountFs": "efs-01***08", "RegionId": "cn- wulan-env***-d01", "VideoMemory": 2560, "EnableIpv6": true, "EvpcEnableIpv6": true } ], "PageSize": 10, "TotalCount": 1, "PageNumber": 1 } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| success | Boolean | true | The status of the response. Successful: true Failed: false |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListBmcpCluster &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-env***-d01 &ZoneId=cn-wulan-env***-****-a &VpcId=vpc-bp1b1xjllp3ve5yze**** &ClusterName=cluster-name &Common request parameters&Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "ClusterList":[
```

`{`

```json
    "Description":"testDescription",
    "Organization":"5",
    "IsSetPassword":true,
    "SwitchMethod":"CHSW",
    "CpfsClusterType":"APFS",
    "Gpu":[
```

`{`

```json
      "GpuNum":32,
      "GpuModel":"NVIDIA_Ampere_A10_80G_NVLink"
```

`}` `],`

```json
    "EvpcId":"evpc-pi2q***z8b",
    "EnableIpv6":true,
    "FlopsCount":9984,
    "Department":5,
    "CpuCount":512,
    "EvpcEnableIpv6":true,
    "ClusterName":"cluster-name",
    "ResourceGroup":4,
    "Status":"active",
    "ActiveNodeCount":4,
    "NodeCount":4,
```

```json
    "ClusterId":"bmcp-v8***QVZT",
    "Zone":"cn-wulan-env***-d01-a",
    "CreateTime":"2026-01-12T10:44:46+08:00",
    "Specification":[
```

`{`

```json
      "Count":3,
      "Name":"gBMC-Ci8af8nbr"
```

`}` `],`

```json
    "CpfsClusterState":"active",
    "AscmCreateUser":"admin",
    "MemCount":8192,
    "ClusterArchType":"standard",
    "VpcId":"vpc-7kkjbu****od7pxs610",
    "OldClusterBzid":"",
    "UpdateTime":"2026-01-22T15:58:01+08:00",
    "Region":"cn-wulan-env***-d01",
    "CpfsMountFs":"efs-01***08",
    "RegionId":"cn-wulan-env***-d01",
    "VideoMemory":2560
```

`}` `],`

```json
  "PageSize":10,
  "PageNumber":1
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>1</TotalCount>
 <ClusterList>
  <Description>testDescription</Description>
  <Organization>5</Organization>
  <IsSetPassword>true</IsSetPassword>
  <SwitchMethod>CHSW</SwitchMethod>
  <CpfsClusterType>APFS</CpfsClusterType>
  <Gpu>
   <GpuNum>32</GpuNum>
   <GpuModel>NVIDIA_Ampere_A10_80G_NVLink</GpuModel>
  </Gpu>
  <EvpcId>evpc-pi2q***z8b</EvpcId>
  <EnableIpv6>true</EnableIpv6>
  <FlopsCount>9984</FlopsCount>
  <Department>5</Department>
  <CpuCount>512</CpuCount>
  <EvpcEnableIpv6>true</EvpcEnableIpv6>
  <ClusterName>cluster-name</ClusterName>
  <ResourceGroup>4</ResourceGroup>
  <Status>active</Status>
  <ActiveNodeCount>4</ActiveNodeCount>
  <NodeCount>4</NodeCount>
  <ClusterId>bmcp-v8***QVZT</ClusterId>
  <Zone>cn-wulan-env***-d01-a</Zone>
  <CreateTime>2026-01-12T10:44:46+08:00</CreateTime>
  <Specification>
   <Count>3</Count>
   <Name>gBMC-Ci8af8nbr</Name>
  </Specification>
  <CpfsClusterState>active</CpfsClusterState>
  <AscmCreateUser>admin</AscmCreateUser>
  <MemCount>8192</MemCount>
  <ClusterArchType>standard</ClusterArchType>
  <VpcId>vpc-7kkjbu****od7pxs610</VpcId>
  <OldClusterBzid />
  <UpdateTime>2026-01-22T15:58:01+08:00</UpdateTime>
  <Region>cn-wulan-env***-d01</Region>
  <CpfsMountFs>efs-01***08</CpfsMountFs>
  <RegionId>cn-wulan-env***-d01</RegionId>
  <VideoMemory>2560</VideoMemory>
 </ClusterList>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.1.4 DescribeBmcpCluster

Query the details of a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt**** | The ID of the bare metal - intelligent computing cluster. You can call the ListBmcpCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

|   |   | { "ClusterId": "bmcp- bpnopt****", "ClusterName": "cluster-name", "Description": "testDescription", "Status": "active", |   |
|---|---|---|---|
| data | Map | "CreateTime": "2023-11- 29T17:08:15+08:0 0", "UpdateTime": "2023-12- 13T15:15:25+08:0 0", "NodeCount": 3, "ActiveNodeCount" : 1, "CpuCount": 10, "MemCount": 36, "FlopsCount": 50, "VideoMemory": 50, "Region": "cn- ****-env**-d01", "Organization": "4", "ResourceGroup": "3", "InstanceList": [ "i- d8offheheob5qaf0* ***", "i- d620b2eheobcabte ****", "i- d75ppnuheobcnhq o****" ], "VpcId": "vpc- bp1b1xjllp3ve5yze ****", "ClusterArchType": "standard", "EvpcId": "evpc- htchvitxlfjyso****", "Zone": "cn-****- env**-d01-a", "IsSetPassword": true } | The response data. |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| success | Boolean | true | The status of the response. Successful: true Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DescribeBmcpCluster &ClusterId=bmcp-bpnopt**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "Status":"active",
  "Description":"testDescription",
  "ActiveNodeCount":1,
  "Organization":"4",
  "IsSetPassword":true,
  "NodeCount":3,
  "ClusterId":"bmcp-bpnopt****",
  "Zone":"cn-****-env**-d01-a",
  "CreateTime":"2023-11-29T17:08:15+08:00",
  "MemCount":36,
  "EvpcId":"evpc-htchvitxlfjyso****",
  "ClusterArchType":"standard",
  "FlopsCount":50,
  "CpuCount":10,
  "VpcId":"vpc-bp1b1xjllp3ve5yze****",
  "UpdateTime":"2023-12-13T15:15:25+08:00",
  "ClusterName":"cluster-name",
  "Region":"cn-****-env**-d01",
  "VideoMemory":50,
  "InstanceList":[
   "i-d8offheheob5qaf0****",
   "i-d620b2eheobcabte****",
   "i-d75ppnuheobcnhqo****"
```

`],`

```json
  "ResourceGroup":"3"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <Status>active</Status>
 <Description>testDescription</Description>
 <ActiveNodeCount>1</ActiveNodeCount>
 <Organization>4</Organization>
 <IsSetPassword>true</IsSetPassword>
 <NodeCount>3</NodeCount>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <Zone>cn-****-env**-d01-a</Zone>
 <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
 <MemCount>36</MemCount>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
 <ClusterArchType>standard</ClusterArchType>
 <FlopsCount>50</FlopsCount>
 <CpuCount>10</CpuCount>
 <VpcId>vpc-bp1b1xjllp3ve5yze****</VpcId>
 <UpdateTime>2023-12-13T15:15:25+08:00</UpdateTime>
 <ClusterName>cluster-name</ClusterName>
 <Region>cn-****-env**-d01</Region>
 <VideoMemory>50</VideoMemory>
 <InstanceList>i-d8offheheob5qaf0****</InstanceList>
 <InstanceList>i-d620b2eheobcabte****</InstanceList>
 <InstanceList>i-d75ppnuheobcnhqo****</InstanceList>
 <ResourceGroup>3</ResourceGroup>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.1.5 AddBmcpClusterInstances

Scale out a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterId | Strin g | Quer y | No | bmcp-bpnopt**** | The ID of the bare metal - intelligent computing cluster. You can call ListEhpcCluster to query the cluster ID. |
|---|---|---|---|---|---|
| InstanceLis t | Json | Quer y | No | null | This parameter is deprecated. |
| Password | Strin g | Quer y | No | null | This parameter is deprecated. |
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal server types to be added to the intelligent computing cluster. This parameter is required When ClusterArchType is set to standard, base, or aspeed. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | [ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****", "ActivationId": "a- hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC- 9AB1-890F1234****" } ] | The list of parameters required for requesting bare metal servers. This parameter is required when ClusterArchType is set to managed. |
| VswitchIdL ist | Json | Quer y | No | null | This parameter Is deprecated. |

| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The ID of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
|---|---|---|---|---|---|
| Activation Code | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The code of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| ZoneId | Strin g | Quer y | No | cn-****-env**-d01-a | The ID of the available zone. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp- bpnopt****" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the response. Successful: true Failed: false |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bmcp-bpnopt****",
  "ClusterName":"testname"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <ClusterName>testname</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.1.6 ListAvailableBmcpInstance

Query the list of available Bare Metal Computing Platform (BMCP) BMCP instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource setgroup. |
| VpcId | Strin g | Quer y | No | vpc- 4uftp58qtzn7t663xajtj | The ID of the Virtual Private Cloud (VPC). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "InstanceList": [ { "InstanceId": "1", "InstanceIp": "192.168.1.1", "InstanceAlias": "c25d0****.cloud.d 04.****", "HostName": "c25d0****.cloud.d 04.****", "SN": "98001716037**** ", "InstacneType": "VM", "CpuCount": 192, "MemCount": 256, "FlopsCount": 2496, "VideoMemCount": 640, "VpcId": "vpc- xxxx" } ] } | The response data. |
| status | Integer | 0 | The status of the responsequest. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListAvailableBmcpInstance &Department=4 &ResourceGroup=3 &VpcId=vpc-4uftp58qtzn7t663xajtj &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "InstanceList":[
```

`{`

```json
    "FlopsCount":2496,
    "CpuCount":192,
    "VideoMemCount":640,
    "VpcId":"vpc-xxxx",
    "InstanceId":"1",
    "InstanceAlias":"c25d0****.cloud.d04.****",
    "InstanceIp":"192.168.1.1",
    "SN":"98001716037****",
    "InstacneType":"VM",
    "HostName":"c25d0****.cloud.d04.****",
    "MemCount":256
```

`}` `]` `},`

```json
 "errorTitle":"""""",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\""",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <InstanceList>
  <FlopsCount>2496</FlopsCount>
  <CpuCount>192</CpuCount>
  <VideoMemCount>640</VideoMemCount>
  <VpcId>vpc-xxxx</VpcId>
  <InstanceId>1</InstanceId>
  <InstanceAlias>c25d0****.cloud.d04.****</InstanceAlias>
  <InstanceIp>192.168.1.1</InstanceIp>
  <SN>98001716037****</SN>
  <InstacneType>VM</InstacneType>
  <HostName>c25d0****.cloud.d04.****</HostName>
  <MemCount>256</MemCount>
 </InstanceList>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.1.7 DeleteBmcpClusterInstances

Scale in a bare metal cluster instance.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt**** | The ID of the bare metal - supercomputing cluster. You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceId List | Json | Quer y | No | ["i- d92sc86heobfdsc1****"] | The list of node IDs to be removed from the cluster. |

| InstanceLis t | Json | Quer y | No | [ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ] | The list of bare metal servers to be removed from the cluster. This parameter is optional. |
|---|---|---|---|---|---|
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when machines are released. true: Clean false: Do not clean |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period. Unit: hours. Valid values: 1 to 720. Default value: 168. After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp- bpnopt****" } | The response data. |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the response. Successful: true Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteBmcpClusterInstances &ClusterId=bmcp-bpnopt**** &InstanceIdList=["i-d92sc86heobfdsc1****"] &ZoneId=cn-wulan-env***-****-a &InstanceList=
```

`[` `{`

```json
    "InstanceId": "11",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "VideoMemCount": 30
```

`}` `]`

```
&OsUpdate=true &RetentionPeriod=168 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bmcp-bpnopt****",
  "ClusterName":"testname"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>bmcp-bpnopt****</ClusterId>
 <ClusterName>testname</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.1.8 DeleteBmcpCluster

Delete a bare metal - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bmcp-bpnopt**** | The ID of the bare metal - supercomputing cluster. You can call the ListEhpcCluster operation to query the cluster ID. |

| InstanceLis t | Json | Quer y | No | [ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ] | The list of bare metal servers to be removed from the cluster. |
|---|---|---|---|---|---|
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when machines are released. true: Clean false: Do not clean |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period of instances in the recycle bin. Unit: hours. Value range: 1 to 720. Default value: 168. After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "bmcp- bpnopt****" } | The response data. |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the response. Successful: true Failed: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteBmcpCluster &ClusterId=bmcp-bpnopt**** &InstanceList=[
```

`{`

```json
 "InstanceId": "i-d8offl6heob05q4v****",
 "InstanceIp": "127.0.0.1",
 "SN": "980017160373****",
 "InstanceType": "P5N1",
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30
```

`}` `]`

```
&OsUpdate=true &RetentionPeriod=168 &Common request parameters
```

Sample success responses

#### 5.1.2 ACK - intelligent computing cluster

##### 5.1.2.1 CreateAckCluster

Create a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the cluster. Length: 0–1000 characters. |
| Password | Strin g | Quer y | No | Pwd***** | The login password for machines in the cluster. The password must be 8– 30 characters in length, and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include `()~!@#$%^&*- +=\|{} _ []:;'<>.,?/. |

| ApplyBmsI nstanceLis t | Json | Quer y | No | [ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****", "ActivationId": "a- hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC- 9AB1-890F1234****" } ] | The list of Bare Metal Computing Platform (BMCP) instances for managed intelligent computing clusters. |
|---|---|---|---|---|---|
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). The cluster is deployed in the specified VPC. |
| VswitchIdL ist | Json | Quer y | No | ["vsw- 2ze3ds0mdip0hdz8i****", "vsw- 3gagdup8scary04iq****"] | The list of master node vSwitch IDs. Valid values for the number of vSwitches: [1,3] . To ensure high availability of the cluster, we recommend that you select 3 vSwitches across different availability zones. |

| Kubernete sVersion | Strin g | Quer y | No | 1.32.7-aliyun.1 | The version of the Kubernetes which is aligned with the Kubernetes community baseline version. We recommend that you select the latest version. If not specified, the latest version is used by default. You can call the DescribeKubernetesVersi onMetadata operation to query details of supported Kubernetes versions. For more information, see the Query Kubernetes version details section in the Container Service for Kubernetes Developer Guide. |
|---|---|---|---|---|---|
| Runtime | Strin g | Quer y | No | {docker 19.03.5} | The container runtime. Supported runtimes: containerd, Docker, and Sandboxed- Container.runv. The parameter runtime includes the following two information: name: Container runtime name Version: Container runtime version You can call the DescribeKubernetesVersi onMetadata operation to query supported runtime information. For more information, see the Query Kubernetes version details section in the Container Service for Kubernetes Developer Guide. |
| MasterCou nt | Integ er | Quer y | No | 3 | The number of master nodes. Valid values: 3 or 5. |

| MasterInst anceTypeL ist | Json | Quer y | No | ["ecs.n4.xlarge","ecs.n4.2 xlarge"] | The list of master node instance types. You can call the ListAckInstanceType operation to query instance types supported by master nodes (NodeType is set to master). |
|---|---|---|---|---|---|
| MasterSyst emDiskCat egory | Strin g | Quer y | No | cloud ssd _ | The system disk type of master nodes. Valid values: cloud efficiency: Ultra _ disk cloud ssd: Solid-State _ Disk (SSD) cloud pperf: High- _ performance disk cloud sperf: Standard _ performance disk Default value: cloud efficiency. _ The parameter MasterSystemDiskCatego ry must match MasterInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query system disk types supported by master node instance types. |
| MasterSyst emDiskSiz e | Strin g | Quer y | No | 40 | The system disk size of master nodes (GiB). Valid values: 40 to 500. |
| WorkerCou nt | Integ er | Quer y | No | 5 | The number of Elastic Compute Service (ECS) worker nodes. Valid values: 0 ≤ WorkerCount ≤ 100 − MasterCount. |
| WorkerSys temDiskSiz e | Strin g | Quer y | Access Denied | 40 | The system disk size of ECS worker nodes. Unit: GiB. Valid values: 40 to 500. |

| WorkerSys temDiskCa tegory | Strin g | Quer y | Access Denied | cloud ssd _ | The system disk type of ECS worker nodes. Valid values: cloud efficiency: Ultra _ disk cloud ssd: SSD cloud _ disk cloud pperf: High- _ performance disk cloud sperf: Standard _ performance disk Default value: cloud efficiency. _ The parameter WorkerSystemDiskCatego ry must match WorkerInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query the system disk types supported by worker node instance types. |
|---|---|---|---|---|---|
| WorkerVs witchIdList | Json | Quer y | Access Denied | ["vsw- 2ze3ds0mdip0hdz8i****", "vsw- 3gagdup8scary04iq****"] | The list of ECS worker node vSwitches. Valid values: [1,3] . To ensure high availability, we recommend that you select vSwitches in different availability zones. |
| WorkerInst anceTypeL ist | Json | Quer y | Access Denied | ["ecs.n4.xlarge","ecs.n4.2 xlarge"] | The list of ECS worker node instance types. Up to 10 instance types can be specified. You can call the ListAckInstanceType operation to query the instance types supported by master nodes (NodeType is set to worker). |

| WorkerDat aDiskList | Json | Quer y | Access Denied | [{"Category": "cloud ssd","Size":60,"En _ crypted":false}] | The data disk information of ECS worker nodes. Up to 10 data disks are supported. WorkerDataDiskList includes the following three parameters: Category: The data disk type. Valid values: cloud efficiency: _ Ultra disk cloud ssd: SSD _ cloud pperf: High- _ performance disk cloud sperf: _ Standard performance disk The parameter Category must match WorkerInstanceTypeLis t. You can call the ListInstanceTypeDiskC ategory operation to query supported data disk types for worker nodes. Size: The data disk size. Unit: GiB. Valid values: 40 to 500. Encrypted: Whether encrypted. |
|---|---|---|---|---|---|
| Os | Strin g | Quer y | No | Linux | The type of the operating system. Windows Linux Default value: Linux. |
| Platform | Strin g | Quer y | No | AliyunLinux | The operating system distribution. You can call the DescribeKubernetesVersi onMetadata operation to query supported image information. For details, see the Query Kubernetes version details section in the Container Service for Kubernetes Developer Guide. |

| ImageType | Strin g | Quer y | No | AliyunLinux3 | The type of the image. You can call the DescribeKubernetesVersi onMetadata operation to query supported image types. For details, see the Query Kubernetes version details section in the Container Service for Kubernetes Developer Guide. |
|---|---|---|---|---|---|
| PodCidr | Strin g | Quer y | No | 172.20.0.0/16 | The Pod network CIDR block. It must not overlap with the VPC CIDR block. |
| ServiceCid r | Strin g | Quer y | No | 172.21.0.0/20 | The Service network CIDR block. Valid range: 10.0.0.0/16–24, 172.16– 31.0.0/16–24, and 192.168.0.0/16–24. It must not overlap with the VPC CIDR block 10.1.0.0/21 or any CIDR block already used by existing Kubernetes clusters in the VPC. It cannot be modified after creation. |
| SnatEntry | Bool ean | Quer y | No | true | Specifies whether to configure SNAT (Source Network Address Translation) for the VPC. Valid values: true: Automatically create a Network Address Translation (NAT) gateway and configure SNAT entries. Set this parameter to true if nodes and applications in the cluster require Internet access. false: Do not create a NAT gateway or SNAT entries. Nodes and applications in the cluster cannot access the Internet. Default value: false. |

| EndpointP ublicAcces s | Bool ean | Quer y | No | true | Specifies whether to enable public access. Valid values: true: Enable public access. Expose the API server via an Elastic IP Address (EIP) to enable cluster access over the Internet. false: Disable public access. If disabled, the cluster API server cannot be accessed over the Internet. Default value: false. |
|---|---|---|---|---|---|
| SshFlag | Bool ean | Quer y | No | true | Specifies whether to enable public Secure Shell (SSH) login. Valid values: true: Enable false: Disable Default value: false. This parameter is required if EndpointPublicAccess is set to true. |
| LogService | Bool ean | Quer y | No | true | Specifies whether to enable the log service. Valid values: true: Enable false: Disable Default value: false. |
| LogProject | Strin g | Quer y | No | k8s-log- c2345xxxxxxxxxxxx | The name of the log project. You can configure this parameter when LogService is set to true. If not specified, a log project is automatically created. |
| DeleteProt ection | Bool ean | Quer y | No | true | Specifies whether to enable cluster deletion protection. Valid values: true: Enable false: Disable Default value: false. |

| InstanceD eleteProte ction | Bool ean | Quer y | No | true | Specifies whether to enable instance deletion protection. Valid values: true: Enable false: Disable Default value: false. |
|---|---|---|---|---|---|
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the available zone. |
| ClusterArc hType | Strin g | Quer y | No | standard | The type of the cluster. Valid values: standard: Intelligent computing high- bandwidth network managed: Managed intelligent computing base: Basic intelligent computing aspeed: Intelligent computing training and inference |
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "NodePoolName": "bmcp- node-pool" , "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal instance types to be added to the cluster. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| BmsVswitc hIdList | Json | Quer y | No | null | This parameter is deprecated. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard or aspeed. You can call the ListEvpc operation to query the EVPC ID. |

| ActivationI d | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The ID of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
|---|---|---|---|---|---|
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The code of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| VolumeId | Strin g | Quer y | No | null | This parameter is deprecated. |
| MountPath | Strin g | Quer y | No | null | This parameter is deprecated. |
| IsCreateCp fsCluster | Bool ean | Quer y | No | true | Specifies whether to enable the high- performance storage client cluster. Valid values: true: Enable false: Disable Default Value: false. You can configure this parameter when ClusterArchType is set to standard or aspeed. To enable the high- performance storage cluster, the following conditions must be met: evpcId is selected; the number of Cloud Parallel File System (CPFS)-type bare metal nodes is at least 3; and the number of Apple File System (APFS) cluster bare metal nodes is at least 1. |

| CpfsCluste rType | Strin g | Quer y | No | CPFS | The type of the high- performance storage client cluster. Valid values: CPFS APFS This parameter is required when IsCreateCpfsCluster is set to true. |
|---|---|---|---|---|---|
| ClassicSlb Spec | Strin g | Quer y | No | slb.s2.small | The Server Load Balancer (SLB) specification. |
| VolumeInf o | Json | Quer y | No | [ { "VolumeType": "iscsi", "VolumeParams": { "IP": "127.0.0.1", "ServerIQN": "iqn.2023- 04.com.bms:server", "ClientIQN": "", "ChapEnabled": "true", "UserID": "bms", "Password": "xxxx", "LunID": "0", "Description": "", "ClientAttachPath": "/mnt" } }, { "VolumeType": "nfs", "VolumeParams": { "IP": "127.0.0.1", "Description": "", "ServerPath": "/home/nfstestdir", "ClientAttachPath": "/mnt" } }, { "VolumeType": "mount", "VolumeParams": { "Description": "", "ServerPath": "/dev/sdl1", "ClientAttachPath": "/mnt", "MountParams": "--bind" } } ] | The third-party storage mount information. You can configure this parameter when ClusterArchType is set to managed. |
| AppNameL ist | Json | Quer y | No | ["ai-task- inspector","fluid"] | The list of components to install. You can call the ListApps operation to query the available component list. |
| EnabledDr agonfly | Bool ean | Quer y | No | null | This parameter is deprecated. |

| AddonSyst emDiskSiz e | Integ er | Quer y | No | 40 | The system disk size of the software instances. Unit: GiB. Valid values: 40 to 500. |
|---|---|---|---|---|---|
| AddonSyst emDiskCat egory | Strin g | Quer y | No | cloud ssd _ | The system disk specifications of the software instances. Valid values: cloud efficiency: Ultra _ disk cloud ssd: SSD cloud _ disk cloud pperf: High- _ performance disk cloud spPerf: Standard _ performance disk The parameter AddonSystemDiskCategor y must match AddonInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query system disk types supported by software instance types. |

| DataDisk | Json | Quer y | No | * | The list of software instance data disk. WorkerDataDiskList includes the following two parameters: Category: The data disk type. Valid values: cloud efficiency: _ Ultra disk cloud ssd: SSD _ cloud pperf: High- _ performance disk cloud sperf: _ Standard performance disk Size: The data disk size. Unit: GiB. Valid values: 40 to 500. The parameter Category must match AddonInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query data disk types supported by worker node instance types. |
|---|---|---|---|---|---|
| ImageId | Strin g | Quer y | No | aliyun 4 x86 64 20G co _ _ _ _ _ ntainer optimized alibase _ _ 20260407.vhd _ | The ID of the image used by the software instance. If not configured, it defaults to the image used by the cluster. To configure this parameter, call the DescribeKubernetesVer sionMetadata operation to query supported image IDs. For details, see the Query Kubernetes version details section in the Contain er Service for Kuber netes Developer Gui de. |
| AdminUid | Strin g | Quer y | No | ** | This parameter is deprecated. |
| AIRootPwd | Strin g | Quer y | No | * | This parameter is deprecated. |

| AIUserNam e | Strin g | Quer y | No | * | This parameter is deprecated. |
|---|---|---|---|---|---|
| AIPwd | Strin g | Quer y | No | * | This parameter is deprecated. |
| Accelerato rVendorNa me | Strin g | Quer y | No | * | The name of the Nanhu Insight accelerator provider. This parameter is required when Nanhu Insight is installed for the AppNameList. |
| NanhuInsi ghtClusterI d | Strin g | Quer y | No | * | The ID of the Nanhu Insight cluster. This parameter is required when Nanhu Insight is installed for the AppNameList. |
| PeerEvpcId | Strin g | Quer y | No | evpc-***hvitxlfjyso**** | The ID of the Nanhu Insight peer EVPC. This parameter is required when Nanhu Insight is installed for the AppNameList. |
| AddonInst anceTypeL ist | Json | Quer y | No | ["ecs.g6s-k10- c1m1.4xlarge","ecs.n4.4x large"] | The list of software instance types. Up to 10 types are supported. You can call the ListAckInstanceType operation to query software instance types. The minimum software instance type is 16 vCPU and 16 GB. |
| IsCreateEd aCluster | Bool ean | Quer y | Access Denied | true | Specifies whether to enable cache acceleration clusters. Valid values: true: Enable false: Disable This parameter is required when ClusterArchType is set to standard, base, or aspeed. |

| IsInstallYu ndunAegis | Bool ean | Quer y | Access Denied | true | Specifies whether to install Server Guard. Valid values: true: Enable false: Disable Default value: false. |
|---|---|---|---|---|---|
| IsAutoDisk | Bool ean | Quer y | Access Denied | true | Specifies whether to mount Kubernetes images and pods for BMCP nodes to the data disk. |
| SwitchMet hod | Strin g | Quer y | Access Denied | CHSW | The networking mode for the vSwitch. This parameter must be CHSW when ClusterArchType is set to standard, base, or aspeed. This parameter can be CHSW or HSW when ClusterArchType is set to managed. |
| StandardV switchId | Strin g | Quer y | No | vsw- 2ze3ds0mdip0hdz8i**** | Monitoring channel vSwitch, used for building the cluster management and O&M channel. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable the IPv6 feature. true: Enable false: Disable Default value: false |
| EvpcEnabl eIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable EVPC IPv6. Valid values: IPv6 can be enabled only when EvpcId is configured. true: Enable false: Disable Default value: false |

| NodeCidrM ask | Strin g | Quer y | No | 25 | The number of node IPs, determined by the CIDR of the specified network. This parameter takes effect only for clusters that use the Flannel network plug-in. Default value: 25. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "ClusterName": "testname", "ClusterId": "ack- E7qLEr****", "AckClusterName": "testname" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ack-E7qLEr****",
  "ClusterName":"testname",
  "AckClusterName":"testname"
```

`},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>ack-E7qLEr****</ClusterId>
 <ClusterName>testname</ClusterName>
 <AckClusterName>testname</AckClusterName>
</data> <errorTitle /> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

##### 5.1.2.2 ListAckCluster

Query the list of Container Service for Kubernete (ACK) - intelligent computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |

| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
|---|---|---|---|---|---|
| AckCluster Name | Strin g | Quer y | No | cluster-name | The name of the ACK cluster. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |
| AckCluster Id | Strin g | Quer y | No | cef51d60a6778415ab3a8 026c24***** | The ID of the ACK cluster. |
| Status | Strin g | Quer y | No | ** | The status of the cluster status. Valid values: creating: Creating active: Running createFailed: Creation failed deleting: Deleting deleteFailed: Deletion failed scalingDown: Scaling in ScalingDownFailed: Scale-in failed SaclingUp: Scaling out ScalingUpFailed: Scale- out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number, used for pagination query. Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page, which specifies the number of results returned per page. Default value: 10. |
| Zone | Strin g | Quer y | No | cn-****-env**-d01-a | The ID of the available zone. |

| AiStatus | Strin g | Quer y | No | active | The status of the software installed in the cluster. notInstall: Not installed active: Running installFailed: Installation failed installing: Installing uninstalling: Uninstalling unInstallFailed: Uninstallation failed |
|---|---|---|---|---|---|
| ClusterArc hType | Strin g | Quer y | No | standard | The type of the cluster. Valid values: standard: Intelligent computing high- bandwidth network managed: Managed intelligent computing base: Basic intelligent computing aspeed: Intelligent computing training and inference |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard or aspeed. You can call the ListEvpc operation to query the EvpcId. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). |

| EdaCluster State | Strin g | Quer y | No | RUNNING | The status of the cache acceleration cluster. Valid values: INITIAL: Creating RUNNING: Running SHRINKING: Scaling in EXPANDING: Scaling out RELEASING: Releasing |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
|   |   | { "TotalCount": 1, "PageNumber": 1, "PageSize": 10, "ClusterList": [ { "ClusterId": "ack- 8EEjd6****", "AckClusterId": "c4ecce05e63814a 9592b92ad18e59* ***", "ClusterName": "cluster-name", "CpfsClusterType": "CPFS", "CpfsMountFs": "", "CpfsClusterState": "", "AckClusterName": "cluster-name", "Description": "testDescription", "Status": "active", "Version": "1.20.11- aliyunedge.1", "CreateTime": "2023-12- 29T10:00:00+08:0 0", "UpdateTime": "2023-12- 29T10:00:00+08:0 0", "NodeCount": 5, "ClusterResourceT |   |

| data | Map | ype": "bmcp", "BmsNodeCount": 2, "BmsActiveNodeCo unt": 1, "Region": "cn-wulan-env***- d01", "Organization": "69", "ResourceGroup": "69", "SpId": "", "AiStatus": "notInstall", "VpcId": "vpc- bp1b1xjllp3ve5yze ****", "SlbIp": "", "CpuCount": 0, "MemCount": 0, "FlopsCount": 0, "VideoMemory": 0, | The response data. |
|---|---|---|---|
|   |   | "Zone": "cn-wulan- env***-****-a", "ClusterArchType": "standard", "EvpcId": "evpc- htchvitxlfjyso****", "EcsNodeCount": 3, "IsSetPassword": true, "Gpu": [ { "GpuNum": 3, "GpuModel": "NvidiaTeslaA100" } ], "SwitchMethod": "CHSW", "EdaClusterState": "RUNNING" } ] } |   |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListAckCluster &Department=4 &ResourceGroup=3 &Zone=cn-****-env**-d01-a &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "ClusterList":[
```

`{`

```json
    "EcsNodeCount":3,
    "Description":"testDescription",
    "Organization":"69",
    "IsSetPassword":true,
    "BmsActiveNodeCount":1,
    "SwitchMethod":"CHSW",
    "CpfsClusterType":"CPFS",
    "Gpu":[
```

`{`

```json
      "GpuNum":3,
      "GpuModel":"NvidiaTeslaA100"
```

`}` `],`

```json
    "EvpcId":"evpc-htchvitxlfjyso****",
    "FlopsCount":0,
    "CpuCount":0,
    "SlbIp":"",
    "Version":"1.20.11-aliyunedge.1",
    "ClusterResourceType":"bmcp",
    "AiStatus":"notInstall",
    "ClusterName":"cluster-name",
    "ResourceGroup":"69",
    "SpId":"",
    "Status":"active",
    "AckClusterId":"c4ecce05e63814a9592b92ad18e59****",
    "NodeCount":5,
    "ClusterId":"ack-8EEjd6****",
    "Zone":"cn-wulan-env***-****-a",
    "CreateTime":"2023-12-29T10:00:00+08:00",
    "AckClusterName":"cluster-name",
    "CpfsClusterState":"",
    "MemCount":0,
    "ClusterArchType":"standard",
    "VpcId":"vpc-bp1b1xjllp3ve5yze****",
    "BmsNodeCount":2,
    "UpdateTime":"2023-12-29T10:00:00+08:00",
    "CpfsMountFs":"",
    "Region":"cn-wulan-env***-d01",
```

```json
    "EdaClusterState":"RUNNING",
    "VideoMemory":0
```

`}` `],`

```json
  "PageSize":10,
  "PageNumber":1
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data /> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.2.3 DescribeAckCluster

Query the details of a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

| data | Map | { "ClusterId": "ack- 8EEjd6****", "AckClusterId": "c4ecce05e63814a 9592b92ad18e59* ***", "ClusterName": "cluster-name", "AckClusterName": "zpftest1", "Organization": "69", "ResourceGroup": "69", "Region": "cn-wulan-env***- d01", "Description": "testDescription", "Status": "active", "Version": "1.20.11- aliyunedge.1", "CreateTime": "2023-12- 29T10:00:00+08:0 0", "UpdateTime": "2023-12- 29T10:00:00+08:0 0", "NodeCount": 3, "BmsNodeCount": 2, "BmsActiveNodeCo unt": 1, "AliUid": "111", "SpId": "", "AiStatus": "notInstall", "VpcId": "vpc- bp1b1xjllp3ve5yze ****", "DeletionProtection ": false, "CpuCount": 0, "MemCount": 0, "FlopsCount": 0, "VideoMemory": 0, "SlbIp": "", "Zone": "cn-wulan-env***- ****-a", "ClusterArchType": "standard", "EvpcId": "evpc- htchvitxlfjyso****", "EcsNodeCount": 3, "IsSetPassword": true } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DescribeAckCluster&Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "EcsNodeCount":3,
  "Organization":"69",
  "Description":"testDescription",
  "IsSetPassword":true,
  "BmsActiveNodeCount":1,
  "EvpcId":"evpc-htchvitxlfjyso****",
  "FlopsCount":0,
  "CpuCount":0,
  "SlbIp":"",
  "Version":"1.20.11-aliyunedge.1",
  "AiStatus":"notInstall",
  "ClusterName":"cluster-name",
  "ResourceGroup":"69",
  "SpId":"",
  "Status":"active",
  "AckClusterId":"c4ecce05e63814a9592b92ad18e59****",
  "NodeCount":3,
  "ClusterId":"ack-8EEjd6****",
  "Zone":"cn-wulan-env***-****-a",
  "CreateTime":"2023-12-29T10:00:00+08:00",
  "AckClusterName":"zpftest1",
  "DeletionProtection":false,
  "MemCount":0,
  "ClusterArchType":"standard",
  "VpcId":"vpc-bp1b1xjllp3ve5yze****",
  "BmsNodeCount":2,
  "UpdateTime":"2023-12-29T10:00:00+08:00",
  "Region":"cn-wulan-env***-d01",
  "VideoMemory":0,
  "AliUid":"111"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <EcsNodeCount>3</EcsNodeCount>
 <Organization>69</Organization>
 <Description>testDescription</Description>
 <IsSetPassword>true</IsSetPassword>
 <BmsActiveNodeCount>1</BmsActiveNodeCount>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
 <FlopsCount>0</FlopsCount>
 <CpuCount>0</CpuCount>
 <SlbIp  />
 <Version>1.20.11-aliyunedge.1</Version>
 <AiStatus>notInstall</AiStatus>
 <ClusterName>cluster-name</ClusterName>
 <ResourceGroup>69</ResourceGroup>
 <SpId  />
 <Status>active</Status>
 <AckClusterId>c4ecce05e63814a9592b92ad18e59****</AckClusterId>
 <NodeCount>3</NodeCount>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <Zone>cn-wulan-env***-****-a</Zone>
 <CreateTime>2023-12-29T10:00:00+08:00</CreateTime>
 <AckClusterName>zpftest1</AckClusterName>
 <DeletionProtection>false</DeletionProtection>
 <MemCount>0</MemCount>
 <ClusterArchType>standard</ClusterArchType>
 <VpcId>vpc-bp1b1xjllp3ve5yze****</VpcId>
 <BmsNodeCount>2</BmsNodeCount>
 <UpdateTime>2023-12-29T10:00:00+08:00</UpdateTime>
 <Region>cn-wulan-env***-d01</Region>
 <VideoMemory>0</VideoMemory>
 <AliUid>111</AliUid>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>200</status>
```

##### 5.1.2.4 AddAckClusterInstances

Scale out a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| > Document V | ersion: 2 | 026073 | 1 |   | 7 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
| ApplyBmsI nstanceLis t | Json | Quer y | No | [ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****", "ActivationId": "a- hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC- 9AB1-890F1234****" } ] | The list of parameters for requesting bare metal servers. This parameter is required when ClusterArchType is set to managed. |
| Password | Strin g | Quer y | No | Pwd***** | The password of the bare metal instance to be modified. This parameter is required if no password has been set for the cluster. |
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal instance types to be added to the supercomputing cluster. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| BmsVswitc hIdList | Json | Quer y | No | null | This parameter is deprecated. |

| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The ID of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
|---|---|---|---|---|---|
| Activation Code | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The code of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard, base, or aspeed. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the available zone. |
| WorkerCou nt | Integ er | Quer y | No | 5 | The number of Elastic Compute Service (ECS) worker nodes. Valid values: 0 ≤ WorkerCount ≤ 100 - MasterCount. |
| WorkerSys temDiskSiz e | Strin g | Quer y | No | 40 | The system disk size to be scaled out for ECS worker nodes. Unit: GiB. Valid values: 40-500. |
| WorkerSys temDiskCa tegory | Strin g | Quer y | No | cloud ssd _ | The system disk type of ECS worker nodes. Valid values: cloud efficiency: Ultra _ disk cloud ssd: SSD cloud disk _ cloud pperf: High- _ performance disk cloud sperf: Standard _ performance disk Default value: cloud efficiency. _ The parameter WorkerSystemDiskCatego ry must match WorkerInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query the system disk types supported by worker node instance types. |

| WorkerVs witchIdList | Json | Quer y | No | ["vsw- 2ze3ds0mdip0hdz8i****", "vsw- 3gagdup8scary04iq****"] | The list of ECS worker node vSwitchs. Valid values: [1, 3]. To ensure high availability, we recommend selecting vSwitches in different availability zones. |
|---|---|---|---|---|---|
| WorkerInst anceTypeL ist | Json | Quer y | No | ["ecs.n4.xlarge","ecs.n4.2 xlarge"] | The list of instance types for scaling out ECS worker nodes. Up to 10 instance types can be specified. You can call the ListAckInstanceType operation to query the instance types supported by master nodes (NodeType is set to worker). |

| WorkerDat aDiskList | Json | Quer y | No | [{"Category": "cloud ssd","Size":60,"En _ crypted":false}] | The data disk configurations for scaling out ECS worker nodes. Up to 10 data disks are supported. WorkerDataDiskList includes the following three parameters: Category: The data disk type. Valid values: cloud efficiency: _ Ultra disk cloud ssd: Solid- _ State Disk (SSD) cloud pperf: High- _ performance disk cloud sperf: _ Standard performance disk The parameter Category must match WorkerInstanceTypeLis t. You can call the ListInstanceTypeDiskC ategory operation to query supported data disk types for worker nodes. Size: The data disk size. Unit: GiB. Valid values: 40 to 500. Encrypted: Whether encrypted. |
|---|---|---|---|---|---|
| IsAutoDisk | Bool ean | Quer y | No | true | Specifies whether to mount Kubernetes images and pods on Bare Metal Computing Platform (BMCP) nodes to data disks. |
| WorkerIma geId | Strin g | Quer y | No | aliyun 4 x86 64 20G co _ _ _ _ _ ntainer optimized alibase _ _ 20260407.vhd _ | The ID of the ECS worker node image. You can call the DescribeKubernetesVersi onMetadata operation to query supported images. For details, see the Query Kubernetes version details section in the Container Service for Kubernetes Developer Guide. |

| WorkerIma geType | Strin g | Quer y | No | AliyunLinux3 | The type of the ECS worker node image. You can call the DescribeKubernetesVersi onMetadata operation to query supported images. For details, see the Query Kubernetes version details section in the Container Service for Kubernetes Developer Guide. |
|---|---|---|---|---|---|
| WorkerPlat form | Strin g | Quer y | No | AliyunLinux | The operating system distribution of the ECS worker image platform. You can call the DescribeKubernetesVersi onMetadata operation to query supported images. For details, see the Query Kubernetes version details Section in the Container Service for Kubernetes Developer Guide. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "ack- 8EEjd6****", "AckClusterId": "cef51d60a677841 5ab3a8026c24**** *", "AckClusterName": "cluster-name" } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
  "ClusterId":"ack-8EEjd6****",
  "ClusterName":"cluster-name",
  "AckClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
 <AckClusterName>cluster-name</AckClusterName>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.5 ListAckClusterInstances

Query the list of nodes in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |
| State | Strin g | Quer y | No | running | The status of the node. If this parameter is not specified, nodes in all states are returned. pending: creating running: running starting: starting stopping: stopping stopped: stopped |
| NodePoolI d | Strin g | Quer y | No | bmcp | The ID of the node pool. This parameter is left blank by defaut. You can call ListAckClusterNodePool to query the node pool ID. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TotalCount": 1, "PageNumber": 1, "PageSize": 10, "InstanceList": [ { "InstanceName": "worker-k8s-for-cs- c42bb3189a****c2 608634943d67", "NodePoolId": "npba2cf***acd093 eb12d5e", "NodeName": "cn****- d01.192.168.99.14 4", "InstanceId": "i- ****", "State": "running", "CreateTime": "2024-06- 20T15:15:24+08:0 0", "IP": "192.***.**.144", "ImageId": "aliyun 2 1903 x8 _ _ _ 6 64 ***** 202211 _ _ _ 18.vhd", "InstanceRole": "Worker", "InstanceType": "ecs.sn1.medium", "HostName": "iZ0sv0****9c4las1 hZ", "NodeStatus": "Ready", "SN": "xxxx", "VirtualStrategy": "1", "SupportVirtStg":" [\"1\"]", "BmcpStatus":"", "BmcpState": "", "BmcpMappingStat us":"", "BMcpRunningStat e": "" }, ] } | The response data. |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "PageSize":10,
  "PageNumber":1,
  "InstanceList":[
```

`{`

```json
    "BMcpRunningState":"",
    "NodeName":"cn****-d01.192.168.99.144",
    "InstanceId":"i-****",
    "CreateTime":"2024-06-20T15:15:24+08:00",
    "IP":"192.***.**.144",
    "SupportVirtStg":"[\"1\"]",
    "BmcpState":"",
    "InstanceName":"worker-k8s-for-cs-c42bb3189a****c2608634943d67",
    "BmcpMappingStatus":"",
    "NodePoolId":"npba2cf***acd093eb12d5e",
    "State":"running",
    "ImageId":"aliyun_2_1903_x86_64_*****_20221118.vhd",
    "InstanceRole":"Worker",
    "VirtualStrategy":"1",
    "BmcpStatus":"",
    "SN":"xxxx",
    "InstanceType":"ecs.sn1.medium",
    "HostName":"iZ0sv0****9c4las1hZ",
    "NodeStatus":"Ready"
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>1</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <InstanceList>
  <BMcpRunningState  />
  <NodeName>cn****-d01.192.168.99.144</NodeName>
  <InstanceId>i-****</InstanceId>
  <CreateTime>2024-06-20T15:15:24+08:00</CreateTime>
  <IP>192.***.**.144</IP>
  <SupportVirtStg>[&quot;1&quot;]</SupportVirtStg>
  <BmcpState  />
  <InstanceName>worker-k8s-for-cs-c42bb3189a****c2608634943d67</InstanceName>
  <BmcpMappingStatus  />
  <NodePoolId>npba2cf***acd093eb12d5e</NodePoolId>
  <State>running</State>
  <ImageId>aliyun_2_1903_x86_64_*****_20221118.vhd</ImageId>
  <InstanceRole>Worker</InstanceRole>
  <VirtualStrategy>1</VirtualStrategy>
  <BmcpStatus  />
  <SN>xxxx</SN>
  <InstanceType>ecs.sn1.medium</InstanceType>
  <HostName>iZ0sv0****9c4las1hZ</HostName>
  <NodeStatus>Ready</NodeStatus>
 </InstanceList>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>200</status>
```

##### 5.1.2.6 ListAckClusterNodePool

Query the list of node pools in a container intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |

| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | Yes | ack-8EEjd6**** | The ID of the cluster. You can call ListAckCluster to query the cluster ID. |
| Type | Strin g | Quer y | No | bmcp | The node pool type. Valid values: bmcp ecs If this parameter is not specified, node pools of all types are returned. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "NodePools": [ { "NodePoolId": "npe576****3c944 b1****d144c0263* ***", "NodePoolName": "test1", "NodePoolType": "bmcp" }, { "NodePoolId": "npcdcf****2bb946 288****ab9aa34*** *", "NodePoolName": "test1", "NodePoolType": "ess" } ] } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the response. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListAckClusterNodePool &Department=4 &ResourceGroup=3 &ClusterId=ack-8EEjd6**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "NodePools":[
```

`{`

```json
    "NodePoolId":"npe576****3c944b1****d144c0263****",
    "NodePoolName":"test1",
    "NodePoolType":"bmcp"
```

`},` `{`

```json
    "NodePoolId":"npcdcf****2bb946288****ab9aa34****",
    "NodePoolName":"test1",
    "NodePoolType":"ess"
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <NodePools>
  <NodePoolId>npe576****3c944b1****d144c0263****</NodePoolId>
  <NodePoolName>test1</NodePoolName>
  <NodePoolType>bmcp</NodePoolType>
 </NodePools>
 <NodePools>
  <NodePoolId>npcdcf****2bb946288****ab9aa34****</NodePoolId>
  <NodePoolName>test1</NodePoolName>
  <NodePoolType>ess</NodePoolType>
 </NodePools>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.7 DeleteAckClusterInstances

Remove nodes from a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call ListAckCluster to query the cluster ID. |
| InstanceId List | Json | Quer y | No | ["11"] | The list of bare metal node IDs to remove from the cluster. You can call ListBmcpInstance to query the bare metal node ID. For more information, see ListBmcpInstance in the BMS Developer Guide. |

| InstanceLis t | Json | Quer y | No | [ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ] | The list of bare metal nodes to remove from the cluster. |
|---|---|---|---|---|---|
| EcsInstanc eIdList | Json | Quer y | No | ["i- d92sc86heobfdsc1****"] | The list of Elastic Compute Service (ECS) worker node IDs to remove from the cluster. You can call ListAckClusterEcsWorkerI nstances to query the ECS worker node ID. |
| OsUpdate | Bool ean | Quer y | No | false | Whether to clear data disks when releasing the instance. Valid values: true: Clear data disks. false: Do not clear data disks. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period. Unit: hours. Valid values: 1 to 720 Default value: 168 After a Bare Metal Computing Platform (BMCP) node is removed from the cluster, it is placed in the recycle bin. You can restore the node from the recycle bin to the original cluster within the retention period. After the retention period expires, the node is automatically released to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |

| errorMessage | String | "“ | The error message. |
|---|---|---|---|
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "ack- 8EEjd6****", "AckClusterId": "cef51d60a677841 5ab3a8026c24**** *", "AckClusterName": "cluster-name" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteAckClusterInstances &ClusterId=ack-8EEjd6**** &InstanceIdList=["11"] &InstanceList=
```

`[` `{`

```json
    "InstanceId": "11",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "VideoMemCount": 30
```

`}` `]`

```
&OsUpdate=true &RetentionPeriod=168 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
  "ClusterId":"ack-8EEjd6****",
  "ClusterName":"cluster-name",
  "AckClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
 <AckClusterName>cluster-name</AckClusterName>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.8 ModifyAckClusterDeletionProtection

Modify the deletion protection status of a Container Service for Kubernetes (ACK)-intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK- intelligent computing cluster. You can call ListAckCluster to query the cluster ID. |
|---|---|---|---|---|---|
| DeletionPr otection | Bool ean | Quer y | No | true | The deletion protection status. Valid values: true: Enable deletion protection. false: Disable deletion protection. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | "The modification was successful" | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON` format `{`

```json
    "errorCode": "",
    "errorTitle": "",
    "errorMessage": "",
    "code": "",
    "data": "The modification was successful",
    "status": 0,
    "requestId": "d239ef18-a5f1-11ee-a470-16f363c78ec1",
    "success": true,
    "responseVersion": ""
```

`}` `XML` format

```xml
<errorCode /> <errorTitle /> <errorMessage /> <code /> <data>The modification was successful</data> <status>0</status> <requestId>d239ef18-a5f1-11ee-a470-16f363c78ec1</requestId> <success>true</success> <responseVersion />
```

##### 5.1.2.9 ListAckInstanceType

Query the instance types supported by Container Service for Kubernete (ACK) - intelligent computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | ** | This parameter is deprecated. |

| AckCluster Name | Strin g | Quer y | No | ** | This parameter is deprecated. |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ** | This parameter is deprecated. |
| AckCluster Id | Strin g | Quer y | No | ** | This parameter is deprecated. |
| Status | Strin g | Quer y | No | ** | This parameter is deprecated. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the available zone. Separate multiple zone IDs with commas (,), example: zone1,zone2 . |
| VpcAdvanc edResourc e | Bool ean | Quer y | No | true | Specifies whether to enable Virtual Private Cloud (VPC) advanced features. Valid values: true: Enable false: Disable Default Value: false. |
| NodeType | Strin g | Quer y | No | master | The node type of the ACK. Valid values: master worker |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

| data | Map | { "InstanceTypes": [ { "MemorySize": 4, "MultiIpPodCount": 0, "CpuCoreCount": 2, "EniTrunkSupporte d": false, "InstanceTypeFami ly": "ecs.n4", "Zone": "cn-wulan- env***-****-a", "EniQuantity": 1, "ExclusivePodCoun t": 0, "GPUAmount": 0, "ExclusiveMode": false, "WarningInfos": [ "If the resource specifications are low, business operations may be affected, so we recommend that you use them only for small-scale verification tests" ], "MultiIpMode": false, "GPUSpec": "", "InstanceTypeId": "ecs.n4.large", "TrunkPodCount": 0 } ] } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListAckInstanceType &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-env***-d01 &ZoneId=cn-wulan-env***-****-a &VpcAdvancedResource=true &NodeType=master &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "InstanceTypes":[
```

`{`

```json
    "MemorySize":4,
    "MultiIpPodCount":0,
    "CpuCoreCount":2,
    "EniTrunkSupported":false,
    "InstanceTypeFamily":"ecs.n4",
    "Zone":"cn-wulan-env***-****-a",
    "EniQuantity":1,
    "ExclusivePodCount":0,
    "GPUAmount":0,
    "ExclusiveMode":false,
    "WarningInfos":[
     "If the resource specifications are low, business operations may be affected, so w
e recommend that you use them only for small-scale verification tests"
```

`],`

```json
    "MultiIpMode":false,
    "GPUSpec":"",
    "InstanceTypeId":"ecs.n4.large",
    "TrunkPodCount":0
```

`}` `]` `},`

```json
 "errorTitle":"",
 "requestId":"**",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <InstanceTypes>
  <MemorySize>4</MemorySize>
  <MultiIpPodCount>0</MultiIpPodCount>
  <CpuCoreCount>2</CpuCoreCount>
  <EniTrunkSupported>false</EniTrunkSupported>
  <InstanceTypeFamily>ecs.n4</InstanceTypeFamily>
  <Zone>cn-wulan-env***-****-a</Zone>
  <EniQuantity>1</EniQuantity>
  <ExclusivePodCount>0</ExclusivePodCount>
  <GPUAmount>0</GPUAmount>
  <ExclusiveMode>false</ExclusiveMode>
  <WarningInfos>If the resource specifications are low, business operations may be affe
cted, so we recommend that you use them only for small-scale verification tests</Warnin gInfos>
  <MultiIpMode>false</MultiIpMode>
  <GPUSpec  />
  <InstanceTypeId>ecs.n4.large</InstanceTypeId>
  <TrunkPodCount>0</TrunkPodCount>
 </InstanceTypes>
</data> <errorTitle /> <requestId>**</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>200</status>
```

##### 5.1.2.10 ListApps

Query the list of available components.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AppType | Strin g | Quer y | No | BMCP | The application type. Valid values: BMCP ACK |

| Group | Strin g | Quer y | No | AIComputing | The component group. Different component groups apply to different AI computing scenarios. Valid values: OpsStability InferenceOptimize DataAccelerate AIComputing |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| SearchVal ue | Strin g | Quer y | No | test | The search keyword. |
| Language | Strin g | Quer y | No | zh CN _ | The locale. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
|   |   | { "PageSize": 10, "PageNumber": 1, "Total": 3, "Apps": [ { "AppVersion": "1.2.0", "ChartVersion": "1.2.0", "Group": "AIComputing", "Description": "A unified management controller for Bare Metal Computing Platform (BMCP) device plugins (such as |   |

|   |   | DevicePlugin and Exporter). Once |   |
|---|---|---|---|
| data | Map | deployed, it enables unified management and orchestration of Container Service for Kubernetes (ACK)-side GPU plugins, and installs the Node Feature Discovery (NFD) component to automatically tag nodes.", "Arch": [ "amd64", "arm64" ], "AppType": "BMCP", "AppName": "bmcp-gpu- operator" }, { "AppVersion": "1.0.0", "ChartVersion": "1.0.0", "Group": "AIComputing", "Description": "The BMCP GPU deployment engine supports flexible, adaptable, and upgradeable GPU component deployments. You need to create a GPU component deployment task based on the custom resource (CR) BMCPClusterPolicy. ", "Arch": [ "amd64", "arm64" ], "AppType": "BMCP", "AppName": "gpu- deploy-engine" }, { "AppVersion": "1.2.0", "ChartVersion": "1.2.0", "Group": "AIComputing", "Description": "A cloud-native component that provides Alibaba Platform GPU (APG) user-space virtualization, supporting the isolation of compute capabilities and GPU memory. Currently, only APG | The response data. |

|   |   | is supported. The BMCP GPU toolkit must be installed before use.", "Arch": [ "amd64", "arm64" ], "AppType": "BMCP", "AppName": "kgpu" } ] } |   |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListApps &AppType=BMCP &Group=Group &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "PageSize":10,
  "PageNumber":1,
  "Total":3,
  "Apps":[
```

`{`

```json
    "AppVersion":"1.2.0",
    "ChartVersion":"1.2.0",
    "Group":"AIComputing",
    "Description":"A unified management controller for Bare Metal Computing Platform (B
MCP) device plugins (such as DevicePlugin and Exporter). Once deployed, it enables unif ied management and orchestration of Container Service for Kubernetes (ACK)-side GPU plu gins, and installs the Node Feature Discovery (NFD) component to automatically tag node s.",
    "Arch":[
     "amd64",
     "arm64"
```

`]` `],`

```json
    "AppType":"BMCP",
    "AppName":"bmcp-gpu-operator"
```

`},` `{`

```json
    "AppVersion":"1.0.0",
    "ChartVersion":"1.0.0",
    "Group":"AIComputing",
    "Description":"The BMCP GPU deployment engine supports flexible, adaptable, and upg
radeable GPU component deployments. You need to create a GPU component deployment task based on the custom resource (CR) BMCPClusterPolicy.",
    "Arch":[
     "amd64",
     "arm64"
```

`],`

```json
    "AppType":"BMCP",
    "AppName":"gpu-deploy-engine"
```

`},` `{`

```json
    "AppVersion":"1.2.0",
    "ChartVersion":"1.2.0",
    "Group":"AIComputing",
    "Description":"A cloud-native component that provides Alibaba Platform GPU (APG) us
er-space virtualization, supporting the isolation of compute capabilities and GPU memor y. Currently, only APG is supported. The BMCP GPU toolkit must be installed before use.
```

`",`

```json
    "Arch":[
     "amd64",
     "arm64"
```

`],`

```json
    "AppType":"BMCP",
    "AppName":"kgpu"
```

`}` `]` `},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <Total>3</Total>
 <Apps>
  <AppVersion>1.2.0</AppVersion>
  <ChartVersion>1.2.0</ChartVersion>
  <Group>AIComputing</Group>
  <Description>A unified management controller for Bare Metal Computing Platform (BMCP)
device plugins (such as DevicePlugin and Exporter). Once deployed, it enables unified m anagement and orchestration of Container Service for Kubernetes (ACK)-side GPU plugins, and installs the Node Feature Discovery (NFD) component to automatically tag nodes.</De scription>
  <Arch>amd64</Arch>
  <Arch>arm64</Arch>
  <AppType>BMCP</AppType>
  <AppName>bmcp-gpu-operator</AppName>
 </Apps>
 <Apps>
  <AppVersion>1.0.0</AppVersion>
  <ChartVersion>1.0.0</ChartVersion>
  <Group>AIComputing</Group>
  <Description>The BMCP GPU deployment engine supports flexible, adaptable, and upgrade
able GPU component deployments. You need to create a GPU component deployment task base d on the custom resource (CR) BMCPClusterPolicy.</Description>
  <Arch>amd64</Arch>
  <Arch>arm64</Arch>
  <AppType>BMCP</AppType>
  <AppName>gpu-deploy-engine</AppName>
 </Apps>
 <Apps>
  <AppVersion>1.2.0</AppVersion>
  <ChartVersion>1.2.0</ChartVersion>
  <Group>AIComputing</Group>
  <Description>A cloud-native component that provides Alibaba Platform GPU (APG) user-s
pace virtualization, supporting the isolation of compute capabilities and GPU memory. C urrently, only APG is supported. The BMCP GPU toolkit must be installed before use.</De scription>
  <Arch>amd64</Arch>
  <Arch>arm64</Arch>
  <AppType>BMCP</AppType>
  <AppName>kgpu</AppName>
 </Apps>
</data> <errorTitle /> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

##### 5.1.2.11 DescribeApp

Query the details and configuration parameters of an application.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AppName | Strin g | Quer y | Yes | ai-profiling | The name of the application. You can call the ListApps operation to query the application name. |
| Language | Strin g | Quer y | No | zh CN _ | The locale. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

|   |   | { "data": { "AppVersion": "0.1.2", "ChartVersion": "0.1.2", |   |
|---|---|---|---|
| data | Map | "Description": "AI performance analysis and tuning tool that provides training and inference performance analysis", "Details": "# AI Performance Analysis (ai- profiling) ai-profiling is an AI training and inference performance analysis tool that helps developers optimize model performance. ## Components - **ai-profiling**: core performance analysis component ## Functions and features - Training job performance analysis and bottleneck identification - GPU resource utilization monitoring - Inference latency and throughput analysis - Performance optimization suggestions and report generation", "Arch": [ "amd64" ], "AppType": "BMCP", "AppName": "ai- profiling" } } | The response data. |
| 10 |   |   | > Document Version: 2026073 |

| status | Integer | 0 | The status of the response. |
|---|---|---|---|
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the requeste. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DescribeApp &AppName=ai-profiling &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "AppVersion":"0.1.2",
   "ChartVersion":"0.1.2",
   "Description":"AI performance analysis and tuning tool that provides training and in
ference performance analysis",
   "Details":"# AI Performance Analysis (ai-profiling)ai-profiling is an AI training an
d inference performance analysis tool that helps developers optimize model performance.## Components- **ai-profiling**: core performance analysis component## Func tions and features- Training job performance analysis and bottleneck identification- GP U resource utilization monitoring- Inference latency and throughput analysis- Performan ce optimization suggestions and report generation", "Arch":[ "amd64"
```

`],`

```json
"AppType":"BMCP", "AppName":"ai-profiling"
```

`}` `},`

```json
"errorTitle":"", "requestId":"66dfddc6-b547-11ee-aa84-acde4800****", "success":true, "errorMessage":"", "errorCode":"", "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <AppVersion>0.1.2</AppVersion>
  <ChartVersion>0.1.2</ChartVersion>
  <Description>AI performance analysis and tuning tool that provides training and infer
ence performance analysis</Description>
  <Details># AI Performance Analysis (ai-profiling)<br>ai-profiling is an AI training a
nd inference performance analysis tool that helps developers optimize model performance .<br>## Components<br>- **ai-profiling**: core performance analysis component<br>## Fun ctions and features<br>- Training job performance analysis and bottleneck identificatio n<br>- GPU resource utilization monitoring<br>- Inference latency and throughput analys is<br>- Performance optimization suggestions and report generation</Details>
   <Arch>amd64</Arch>
   <AppType>BMCP</AppType>
   <AppName>ai-profiling</AppName>
  </data>
 </data>
 <errorTitle></errorTitle>
 <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId>
 <success>true</success>
 <errorMessage />
 <errorCode  />
 <status>0</status>
```

##### 5.1.2.12 GetOssStsToken

Obtain an Object Storage Service (OSS) temporary security token (STS Token) for temporary authorized access to Alibaba Cloud OSS resources.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

| data | Map | { "data": { "SecurityToken": "CAISrgJ1q6Ft5B6* ***", "Bucket": "baremetal- service-bmcp-cn- wulan-****-d01", "AccessKeyId": "STS.47W****cKpt* ***wRHDaQf****", "AccessKeySecret": "Ak2Miq****LaFsS wrd****ytZX1****3 ************", "Expiration": "2026-07- 28T15:10:49Z", "RegionId": "cn- wulan-*****-d01", "EndPoint": "oss- cn-wulan-*****- d01- a.intra.*****.*****.c om" } } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=GetOssStsToken &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "SecurityToken":"CAISrgJ1q6Ft5B6****",
   "Bucket":"baremetal-service-bmcp-cn-wulan-****-d01",
   "AccessKeyId":"STS.47W****cKpt****wRHDaQf****",
   "AccessKeySecret":"Ak2Miq****************ytZX1*****************",
   "Expiration":"2026-07-28T15:10:49Z",
   "RegionId":"cn-wulan-*****-d01",
   "EndPoint":"oss-cn-wulan-*****-d01-a.intra.*****.*****.com"
```

`}` `},`

```json
 "errorTitle":"""""",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\""",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <SecurityToken>CAISrgJ1q6Ft5B6****</SecurityToken>
  <Bucket>baremetal-service-bmcp-cn-wulan-****-d01</Bucket>
  <AccessKeyId>STS.47W****cKpt****wRHDaQf****</AccessKeyId>
  <AccessKeySecret>Ak2Miq****************ytZX1*****************</AccessKeySecret>
  <Expiration>2026-07-28T15:10:49Z</Expiration>
  <RegionId>cn-wulan-*****-d01</RegionId>
  <EndPoint>oss-cn-wulan-*****-d01-a.intra.*****.*****.com</EndPoint>
 </data>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.13 UploadCustomApp

Upload a custom application.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileType | Strin g | Quer y | Yes | YAML | The type of the application package. Valid values: YAML TGZ |
| AddonNam e | Strin g | Quer y | No | test | The name of the application. This parameter is required when FileType is set to YAML. This parameter must be left blank when FileType is set to TGZ. |
| AppVersio n | Strin g | Quer y | No | 0.0.1 | The version of the component. This parameter is required when FileType is set to YAML. This parameter must be left blank when FileType is set to TGZ. |
| ConfigCont ent | Strin g | Quer y | No | {} | The configuration content. This parameter is required when FileType is set to YAML. The value must be in YAML format. This parameter must be left blank when FileType is set to TGZ. |

| OssUrl | Strin g | Quer y | No | https://****.oss-ap- ****.aliyuncs.com/gpu- deploy-engine-1.0.0.tgz | The Object Storage Service (OSS) Uniform Resource Locator (URL) of the component. This parameter must be left blank when FileType is set to YAML. This parameter is required when FileType is set to TGZ. |
|---|---|---|---|---|---|
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the component. This parameter is optional when FileType is set to YAML. This parameter must be left blank when FileType is set to TGZ. |
| Details | Strin g | Quer y | No | "" | The details of the component. This parameter is optional when FileType is set to YAML. This parameter must be left blank when FileType is set to TGZ. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "upload sucess" } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UploadCustomApp &FileType=TGZ &OssUrl=https://****.oss-ap-****.aliyuncs.com/gpu-deploy-engine-1.0.0.tgz &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"upload success"
```

`},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>upload sucess</data>
</data> <errorTitle></errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

##### 5.1.2.14 ListCustomApps

Query the list of custom components.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SourceTyp e | Strin g | Quer y | No | UPLOAD | The source of the component package. Only UPLOAD is supported. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

| data | Map | { "PageSize": 12, "PageNumber": 1, "Total": 2, "Items": [ { "ChartVersion": "", "AppVersion": "0.0.2", "Description": "", "Details": "", "FileType": "YAML", "ChartName": "test1", "SourceType": "UPLOAD", "OssPath": "", "CreateTime": "2026-07-21 15:46:40", "UpdateTime": "2026-07-21 15:46:40", "AddonName": "test1" } ] } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListCustomApps &SourceType=UPLOAD &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "PageSize":12,
  "PageNumber":1,
  "Total":2,
  "Items":[
```

`{`

```json
    "ChartVersion":"",
    "AppVersion":"0.0.2",
    "Description":"",
    "Details":"",
    "FileType":"YAML",
    "ChartName":"test1",
    "SourceType":"UPLOAD",
    "OssPath":"",
    "CreateTime":"2026-07-21 15:46:40",
    "UpdateTime":"2026-07-21 15:46:40",
    "AddonName":"test1"
```

`},` `{`

```json
    "ChartVersion":"",
    "AppVersion":"0.0.1",
    "Description":"",
    "Details":"",
    "FileType":"YAML",
    "ChartName":"nginx-chart-bw",
    "SourceType":"UPLOAD",
    "OssPath":"",
    "CreateTime":"2026-06-02 10:58:08",
    "UpdateTime":"2026-06-02 10:58:08",
    "AddonName":"nginx-chart-bw"
```

`}` `]` `},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <PageSize>12</PageSize>
 <PageNumber>1</PageNumber>
 <Total>2</Total>
 <Items>
  <ChartVersion  />
  <AppVersion>0.0.2</AppVersion>
  <Description  />
  <Details  />
  <FileType>YAML</FileType>
  <ChartName>test1</ChartName>
  <SourceType>UPLOAD</SourceType>
  <OssPath  />
  <CreateTime>2026-07-21 15:46:40</CreateTime>
  <UpdateTime>2026-07-21 15:46:40</UpdateTime>
  <AddonName>test1</AddonName>
 </Items>
 <Items>
  <ChartVersion  />
  <AppVersion>0.0.1</AppVersion>
  <Description  />
  <Details  />
  <FileType>YAML</FileType>
  <ChartName>nginx-chart-bw</ChartName>
  <SourceType>UPLOAD</SourceType>
  <OssPath  />
  <CreateTime>2026-06-02 10:58:08</CreateTime>
  <UpdateTime>2026-06-02 10:58:08</UpdateTime>
  <AddonName>nginx-chart-bw</AddonName>
 </Items>
</data> <errorTitle></errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage></errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.15 DescribeCustomApp

Query the details of a custom component.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| AddonNam e | Strin g | Quer y | Yes | test | The name of the custom component. You can call the ListCustomApps operation to query the custom component name. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": { "ChartVersion": "", "AppVersion": "0.0.2", "Description": "", "Details": "", "FileType": "YAML", "ChartName": "test1", "SourceType": "UPLOAD", "OssPath": "", "CreateTime": "2026-07-21 15:46:40", "UpdateTime": "2026-07-21 15:46:40", "AddonName": "test1" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DescribeCustomApp &AddonName=test &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "ChartVersion":"",
   "AppVersion":"0.0.2",
   "Description":"",
   "Details":"",
   "FileType":"YAML",
   "ChartName":"test1",
   "SourceType":"UPLOAD",
   "OssPath":"",
   "CreateTime":"2026-07-21 15:46:40",
   "UpdateTime":"2026-07-21 15:46:40",
   "AddonName":"test1"
```

`}` `},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <ChartVersion  />
  <AppVersion>0.0.2</AppVersion>
  <Description  />
  <Details  />
  <FileType>YAML</FileType>
  <ChartName>test1</ChartName>
  <SourceType>UPLOAD</SourceType>
  <OssPath  />
  <CreateTime>2026-07-21 15:46:40</CreateTime>
  <UpdateTime>2026-07-21 15:46:40</UpdateTime>
  <AddonName>test1</AddonName>
 </data>
</data> <errorTitle></errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

##### 5.1.2.16 DeleteCustomApp

Delete a custom component.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AddonNam e | Strin g | Quer y | Yes | test | The name of the custom component. You can call the ListCustomApps operation to query the custom component name. |
| AppVersio n | Strin g | Quer y | Yes | 1.2.0 | The version of the custom component. You can call the ListCustomApps operation to query the custom component and its version. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | {"data": "Delete success"} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteCustomApp &AddonName=test &AppVersion=1.2.0 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"Delete success"
```

`},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>Delete success</data>
</data> <errorTitle></errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

##### 5.1.2.17 InstallAiInstanceResource

Install AI instance resources for a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |

| VswitchIdL ist | Json | Quer y | No | ["vsw- 2ze3ds0mdip0hdz8i****", "vsw- 3gagdup8scary04iq****"] | The list of vSwitch IDs for master nodes. The number of vSwitches ranges from 1 to 3. To ensure high availability of the cluster, we recommend that you select three vSwitches in different zones. |
|---|---|---|---|---|---|
| AddonSyst emDiskCat egory | Strin g | Quer y | No | cloud ssd _ | The system disk category of the instance where the software is to be installed. Valid values: cloud efficiency: Ultra _ disk cloud ssd: Solid-State _ Disk (SSD) cloud pperf: Premium _ Enterprise SSD (ESSD) cloud sperf: Basic disk _ AddonSystemDiskCategor y must match AddonInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query the system disk categories supported by the types of the instance where the software is to be installed. |
| AddonSyst emDiskSiz e | Integ er | Quer y | No | 40 | The system disk size of the instance where the software is to be installed. Unit: GiB. Valid values: 40 to 500 |

| DataDisk | Json | Quer y | No | [{"Category": "cloud ssd","Size":60}] _ | The list of data disks of the instance where the software is to be installed. WorkerDataDiskList contains the following two fields: Category: The data disk category. Valid values: cloud efficiency: _ Ultra disk cloud ssd: SSD _ cloud pperf: _ Premium ESSD cloud sperf: Basic _ disk Size: The data disk size. Unit: GiB. Valid values: 40 to 500 Category must match AddonInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query the data disk categories supported by the worker node types. |
|---|---|---|---|---|---|
| Platform | Strin g | Quer y | No | AliyunLinux | The OS distribution. You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide. |

| ImageId | Strin g | Quer y | No | aliyun 4 x86 64 20G co _ _ _ _ _ ntainer optimized alibase _ _ 20260407.vhd _ | The ID of the image used by the instance where the software is to be installed. If this parameter is not specified, the default value is the ID of the image used by the cluster. To specify a value, call the DescribeKubernetesVer sionMetadata operation to query the IDs of the supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide. |
|---|---|---|---|---|---|
| AddonInst anceTypeL ist | Json | Quer y | No | ["ecs.g6s-k10- c1m1.4xlarge","ecs.n4.4x large"] | The type list of the instance where the software is to be installed. A maximum of 10 instance types can be specified. You can call the ListAckInstanceType operation to query the instance types. The minimum instance type is 16 vCPUs and 16 GB. |

| Runtime | Strin g | Quer y | No | {docker 19.03.5} | The container runtime. Three runtimes are supported: containerd, Docker, and Sandboxed- Container.runv. Runtime contains the following two fields: name: The container runtime name version: The container runtime version You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported runtimes. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide. |
|---|---|---|---|---|---|
| ClassicSlb Spec | Strin g | Quer y | No | slb.s2.small | The Server Load Balancer (SLB) specification. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "The resource is being installed" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=InstallAiInstanceResource &ClusterId=ack-8EEjd6**** &VswitchIdList= ["vsw-2ze3ds0mdip0hdz8i****","vsw-3gagdup8scary04iq****"] &AddonSystemDiskCategory=cloud_ssd &AddonSystemDiskSize=40 &DataDisk=[{"Category": "cloud_ssd","Size":60}] &Platform=AliyunLinux &ImageId=aliyun_4_x86_64_20G_container_optimized_alibase_20260407.vhd &AddonInstanceTypeList=["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4xlarge"] &Runtime={docker 19.03.5} &ClassicSlbSpec=slb.s2.small &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The resource is being installed"
```

`},`

```json
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The resource is being installed</data>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.18 UnInstallAiInstanceResource

Uninstall cluster O&M services from a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
| AppNameL ist | Json | Quer y | No | ["ai-task- inspector","fluid"] | The list of apps to delete. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {"data": "The resource is being deleted",} | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UnInstallAiInstanceResource &ClusterId=ack-8EEjd6**** &AppNameList=["ai-task-inspector","fluid"] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The resource is being deleted"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The resource is being deleted</data>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.19 InstallAiApplication

Install an application in a Container Service for Kubernetes (ACK) - AI computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - AI computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
| AppName | Strin g | Quer y | No | [ "ai-profiling" ] | The name of the application to install. You can call the ListAckClusterApp operation to query the application name. |
| IsInstallInst anceResou rce | Bool ean | Quer y | No | true | Specifies whether to install resources on the type of the instance where the software is to be installed in the ACK cluster. |
| VswitchIdL ist | Json | Quer y | No | ["vsw- 2ze3ds0mdip0hdz8i****", "vsw- 3gagdup8scary04iq****"] | The list of vSwitch IDs. Specifies the vSwitches to which the bare metal instances will be connected. |
| AddonSyst emDiskCat egory | Strin g | Quer y | No | cloud ssd _ | The system disk category of the instance where the software is to be installed. Valid values: cloud efficiency: Ultra _ disk cloud ssd: Soliad-State _ Disk (SSD) cloud pperf: Premium _ Enterprise SSD (ESSD) cloud sperf: Basic disk _ AddonSystemDiskCategor y must match AddonInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query the system disk categories supported by the type of the instance where the software is to be installed. |

| AddonSyst emDiskSiz e | Integ er | Quer y | No | 40 | The system disk size of the instance where the software is to be installed. Unit: GiB. Valid values: 40 to 500 |
|---|---|---|---|---|---|
| DataDisk | Json | Quer y | No | [{"Category": "cloud ssd","Size":60}] _ | The list of data disks of the instance where the software is to be installed. DataDiskList contains the following two fields: Category: The data disk category. Valid values: cloud efficiency: _ Ultra disk cloud ssd: SSD _ cloud pperf: ESSD _ cloud sperf: Basic _ disk Size: The data disk size. Unit: GiB. Valid values: 40 to 500 Category must match AddonInstanceTypeList. You can call the ListInstanceTypeDiskCate gory operation to query the data disk categories supported by the worker node types. |

| Password | Strin g | Quer y | No | Pwd***** | The logon password of the machines in the cluster. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters include ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/. |
|---|---|---|---|---|---|
| Platform | Strin g | Quer y | No | AliyunLinux | The OS distribution. You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide. |

| ImageId | Strin g | Quer y | No | aliyun 4 x86 64 20G co _ _ _ _ _ ntainer optimized alibase _ _ 20260407.vhd _ | The ID of the image used by the instance where the software is to be installed. If this parameter is not specified, the default value is the ID of the image used by the cluster. To specify a value, call the DescribeKubernetesVer sionMetadata operation to query the IDs of supported images. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide. |
|---|---|---|---|---|---|
| AddonInst anceTypeL ist | Json | Quer y | No | ["ecs.g6s-k10- c1m1.4xlarge","ecs.n4.4x large"] | The type list of the instance where the software is to be installed. A maximum of 10 instance types can be specified. You can call the ListAckInstanceType operation to query the instance types. The minimum instance type is 16 vCPUs and 16 GB. |
| AdminUid | Strin g | Quer y | No | ** | This parameter is deprecated. |
| AIRootPwd | Strin g | Quer y | No | ** | This parameter is deprecated. |
| AIUserNam e | Strin g | Quer y | No | ** | This parameter is deprecated. |
| AIPwd | Strin g | Quer y | No | ** | This parameter is deprecated. |

| Accelerato rVendorNa me | Strin g | Quer y | No | * | The name of the Nanhu Insight accelerator vendor. This parameter is required when Nanhu Insight is included in the AppNameList. |
|---|---|---|---|---|---|
| NanhuInsi ghtClusterI d | Strin g | Quer y | No | cluster001 | The ID of the Nanhu Insight cluster. This parameter is required when Nanhu Insight is included in the AppNameList. |
| PeerEvpcId | Strin g | Quer y | No | evpc-***hvitxlfjyso**** | The ID of the peer Enterprise Virtual Private Cloud (EVPC) for Nanhu Insight. This parameter is required when Nanhu Insight is included in the AppNameList. |
| Runtime | Strin g | Quer y | No | {docker 19.03.5} | The container runtime. Three runtimes are supported: containerd, Docker, and Sandboxed- Container.runv. Runtime contains the following two fields: name: The name of the container runtime. version: The version of the container runtime. You can call the DescribeKubernetesVersi onMetadata operation to query the information about the supported runtimes. For more information, see the "Query Kubernetes version details" section in the Container Service for Kubernetes Developer Guide. |
| NasEndpoi nt | Strin g | Quer y | No | ** | This parameter is deprecated. |
| SlbIp | Strin g | Quer y | No | 192.16*.*.* | The Server Load Balancer (SLB) IP address. |

| ReleaseNa me | Strin g | Quer y | No | ** | This parameter is deprecated. |
|---|---|---|---|---|---|
| Namespac e | Strin g | Quer y | No | default | The namespace. |
| AppVersio n | Strin g | Quer y | No | 1.2.0 | The application version. |
| ExtraPara ms | Json | Quer y | No | {} | The extra rendering parameters. If the application requires additional rendering variables in key- value format, pass them in JSON format. |

|   | value |
|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": "The app is being installed" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=InstallAiApplication &ClusterId=ack-8EEjd6**** &AppName= [ "ai-profiling" ] &IsInstallInstanceResource=true &VswitchIdList= ["vsw-2ze3ds0mdip0hdz8i****","vsw-3gagdup8scary04iq****"] &AddonSystemDiskCategory=cloud_ssd &AddonSystemDiskSize=40 &DataDisk= [{"Category": "cloud_ssd","Size":60}] &Platform=AliyunLinux &ImageId=aliyun_4_x86_64_20G_container_optimized_alibase_20260407.vhd &AddonInstanceTypeList=["ecs.g6s-k10-c1m1.4xlarge","ecs.n4.4xlarge"] &Runtime={docker 19.03.5} &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The app is being installed"
```

`},`

```json
 "errorTitle":"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The app is being installed</data>
</data> <errorTitle></errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage></errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.20 UpgradeAiApplication

Upgrade an application in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
| AppName | Strin g | Quer y | No | ai-profiling | The name of the application to upgrade. |
| ReleaseNa me | Strin g | Quer y | No | ** | This parameter is deprecated. |
| Namespac e | Strin g | Quer y | No | default | The namespace. |
| AppVersio n | Strin g | Quer y | No | 1.2.0 | The application version. |
| ExtraPara ms | Json | Quer y | No | {} | The extra rendering parameters. If the application requires additional rendering variables as key- value pairs, pass them in JSON format. |

|   | value |
|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

| data | Map | { "data": "The app is being upgraded" } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UpgradeAiApplication &ClusterId=ack-8EEjd6**** &AppName=ai-profiling &Namespace=default &AppVersion=1.2.0 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The app is being upgraded"
```

`},`

```json
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The app is being upgraded</data>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.21 UnInstallAiApplication

Uninstall an application from a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
| AppName | Strin g | Quer y | No | ai-profiling | The name of the application to uninstall. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |

| data | Map | {"data": "The app is being uninstalled"} | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UnInstallAiApplication &ClusterId=ack-8EEjd6**** &AppName=ai-profiling &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The app is being uninstalled"
```

`},`

```json
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The app is being uninstalled</data>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.22 ListInstanceTypeDiskCategory

Query the supported disk categories for instance types.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | ** | The parameter is deprecated. |
| AckCluster Name | Strin g | Quer y | No | ** | This parameter is deprecated. |
| ClusterId | Strin g | Quer y | No | ** | The parameter is deprecated. |
| AckCluster Id | Strin g | Quer y | No | ** | The parameter is deprecated. |
| Status | Strin g | Quer y | No | ** | The parameter is deprecated. |

| InstanceTy peList | Json | Quer y | No | ["ecs.n4.xlarge","ecs.n4.2 xlarge"] | The list of instance types. You can call the ListAckInstanceType operation to query instance types supported by Container Service for Kubernete (ACK) - intelligent computing clusters. |
|---|---|---|---|---|---|
| DiskType | Strin g | Quer y | No | SystemDisk | The category of the disk to query. Valid values: SystemDisk DataDisk |
| SystemDis kCategory | Strin g | Quer y | No | cloud ssd _ | This parameter is required when DiskType is set to DataDisk. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | [ "cloud sperf", _ "cloud efficiency", _ "cloud ssd", _ "cloud pperf" ] _ | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListInstanceTypeDiskCategory &Department=4 &ResourceGroup=3 &InstanceTypeList=["ecs.n4.xlarge","ecs.n4.2xlarge"] &DiskType=SystemDisk &Common request parameters
```

Sample success responses `JSON` format `{`

```json
  "errorCode": "",
  "errorTitle": "",
  "errorMessage": "",
  "code": "",
  "data": [
    "cloud_sperf",
    "cloud_efficiency",
    "cloud_ssd",
    "cloud_pperf"
```

`],`

```json
  "status": 0,
  "requestId": "d239ef18-a5f1-11ee-a470-16f363c78ec1",
  "success": true,
  "responseVersion": ""
```

`}` `XML` format

```xml
<errorCode /> <errorTitle /> <errorMessage /> <code /> <data>cloud_sperf</data> <data>cloud_efficiency</data> <data>cloud_ssd</data> <data>cloud_pperf</data> <status>0</status> <requestId>d239ef18-a5f1-11ee-a470-16f363c78ec1</requestId> <success>true</success> <responseVersion />
```

##### 5.1.2.23 ListAckClusterEcsWorkerInstances

Query the list of Elastic Compute Service (ECS) worker instances in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource group. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call ListAckCluster to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

| data | Map | { "InstanceList": [ { "InstanceName": "worker-k8s-for-cs- c42bb****b88c260 8634943d67", "NodePoolId": "npba2cfc3a07364 ******d093eb12d5 e", "NodeName": "cn- wula*****68.99.14 4", "InstanceId": "i- 0sv0******c4las1h" , "State": "running", "CreateTime": "2024-06- 20T15:15:24+08:0 0", "IP": "192.***.**.144", "ImageId": "aliyun 2 1903 x8 _ _ _ 6 64**** 2022111 _ _ 8.vhd", "InstanceRole": "Worker", "InstanceType": "ecs.sn1.medium", "HostName": "iZ0sv0****4las1hZ ", "NodeStatus": "Ready" } ] } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "InstanceList":[
```

`{`

```json
    "InstanceName":"worker-k8s-for-cs-c42bb****b88c2608634943d67",
    "NodePoolId":"npba2cfc3a07364******d093eb12d5e",
    "NodeName":"cn-wula*****68.99.144",
    "InstanceId":"i-0sv0******c4las1h",
    "State":"running",
    "CreateTime":"2024-06-20T15:15:24+08:00",
    "IP":"192.***.**.144",
    "ImageId":"aliyun_2_1903_x86_64****_20221118.vhd",
    "InstanceRole":"Worker",
    "InstanceType":"ecs.sn1.medium",
    "HostName":"iZ0sv0****4las1hZ",
    "NodeStatus":"Ready"
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <InstanceList>
  <InstanceName>worker-k8s-for-cs-c42bb****b88c2608634943d67</InstanceName>
  <NodePoolId>npba2cfc3a07364******d093eb12d5e</NodePoolId>
  <NodeName>cn-wula*****68.99.144</NodeName>
  <InstanceId>i-0sv0******c4las1h</InstanceId>
  <State>running</State>
  <CreateTime>2024-06-20T15:15:24+08:00</CreateTime>
  <IP>192.***.**.144</IP>
  <ImageId>aliyun_2_1903_x86_64****_20221118.vhd</ImageId>
  <InstanceRole>Worker</InstanceRole>
  <InstanceType>ecs.sn1.medium</InstanceType>
  <HostName>iZ0sv0****4las1hZ</HostName>
  <NodeStatus>Ready</NodeStatus>
 </InstanceList>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.24 DescribeAckClusterLogs

Query the log information of a Container Service for Kubernetes (ACK)-intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK- intelligent computing cluster. You can call ListAckCluster to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| errorCode | String | "" | The error code. |
|---|---|---|---|
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "data": [ { "Id": "4833****", "ClusterId": "ack- ZRy3J8****", "AckClusterId": "c2342******7163f d19af***", "ClusterLog": "start to update cluster status to CREATE COMPLET _ E", "CreateTime": "2026-06- 10T10:11:51+08:0 0", "UpdateTime": "2026-06- 11T10:11:51+08:0 0" } ] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":[
```

`{`

```json
    "AckClusterId":"c2342******7163fd19af***",
    "ClusterId":"ack-ZRy3J8****",
    "CreateTime":"2026-06-10T10:11:51+08:00",
    "UpdateTime":"2026-06-11T10:11:51+08:00",
    "ClusterLog":"start to update cluster status to CREATE_COMPLETE",
    "Id":"4833****"
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <AckClusterId>c2342******7163fd19af***</AckClusterId>
  <ClusterId>ack-ZRy3J8****</ClusterId>
  <CreateTime>2026-06-10T10:11:51+08:00</CreateTime>
  <UpdateTime>2026-06-11T10:11:51+08:00</UpdateTime>
  <ClusterLog>start to update cluster status to CREATE_COMPLETE</ClusterLog>
  <Id>4833****</Id>
 </data>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.25 GetClusterNamespaces

Query the namespace list in a Container Service for Kubernetes (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | Yes | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "Namespaces": [ "default", "kube- system", "kube- public", "kube- node-lease", "ack- system", "arms- prom", "arms- spyhole" ] } | The response data. |
| status | Integer | 0 | The status of the responsequest. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=GetClusterNamespaces &ClusterId=ack-8EEjd6**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "Namespaces":[
   "default",
   "kube-system",
   "kube-public",
   "kube-node-lease",
   "ack-system",
   "arms-prom",
   "arms-spyhole"
```

`]` `},`

```json
 "errorTitle":"""""",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\""",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <Namespaces>default</Namespaces>
 <Namespaces>kube-system</Namespaces>
 <Namespaces>kube-public</Namespaces>
 <Namespaces>kube-node-lease</Namespaces>
 <Namespaces>ack-system</Namespaces>
 <Namespaces>arms-prom</Namespaces>
 <Namespaces>arms-spyhole</Namespaces>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.26 ListHistoryEvent

Query the list of historical tasks.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| StartTime | Strin g | Quer y | No | "2026-07-01" | The start time in YYYY- MM-DD format. This parameter specifies the start time of the time range for historical tasks. It is not required if LastAddon is set to true. |
| EndTime | Strin g | Quer y | No | "2026-07-05" | The end time in YYYY-MM- DD format. This parameter specifies the end time of the time range for historical tasks. It is not required if LastAddon is set to true. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| LastAddon | Bool ean | Quer y | No | true | Specifies whether to query only the most recent task. Valid values: true false Default value: false |
| EventType | Strin g | Quer y | No | all | The task type. Valid values: all: All tasks cluster: Cluster tasks ai: AI suite tasks Default value: all |

| EventNam e | Strin g | Quer y | No | CreateAckCluster | The task name. Valid values: CreateBmsCluster AddBmsInstance DeleteBmsCluster DeleteBmsClusterInsta nces CreateAckCluster AddAckClusterInstance s DeleteAckClusterInstan ces DeleteAckCluster InstallAiAddon UnInstallAiAddon UpgradeAiAddon UnInstallResource CreateEhpcCluster DeleteEhpcCluster DeleteEhpcClusterInsta nce RevertBmsMachine RevertAckMachine RevertEhpcMachine CreateBFICluster ExpandBFICluster DeleteBFICluster ShrinkBFICluster RevertBFIMachine AddEhpcClusterInstanc e CreateCpfsClientCluste r DeleteCpfsClientCluste r MountFileSystem UnMountFileSystem CreateEdaCluster DeleteEdaCluster |
|---|---|---|---|---|---|

| Status | Strin g | Quer y | No | success | The task status. success: Succeeded failed: Failed submitted: Submitted processing: In progress |
|---|---|---|---|---|---|
| TaskId | Strin g | Quer y | No | 1284c8b8-9571-11ee- a39e-16f363c7**** | The task ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
|   |   | { "total": 1, "pageNumber": 1, "data": [ { "Status": "success", "TaskId": "376ea30f-75b4- 11f1-81c7- 02420a26*****", "EndTime": "2026- 07- 02T09:20:33+08:0 0", "Message": "success", "RequestId": "376ea30f-75b4- 11f1-81c7- 02420a26*****", "ClusterId": "bfi- 6nkkQA*****", "CreateTime": "2026-07- 02T09:20:31+08:0 0", "StartTime": "2026-07- 02T09:20:31+08:0 0", "EventName": "ShrinkBFICluster", "modifyFields": [ { "paramsValue": [], "canModify": false, "paramsKey": "BmsVswitchIdList" }, { |   |

| data | Map | "paramsValue": "", "canModify": false, "paramsKey": "EvpcId" }, { "paramsValue": [], "canModify": false, "paramsKey": "ApplyFailedInstan ceList" } ], "UpdateTime": "2026-07- 02T09:20:33+08:0 0", "ID": 747, "DisplaySummary": false, "events": [ { "Status": "success", "TaskId": "376ea30f-75b4- 11f1-81c7- | The response data. |
|---|---|---|---|
|   |   | 02420a26*****", "EndTime": "2026- 07- 02T09:20:33+08:0 0", "CreateTime": "2026-07- 02T09:20:31+08:0 0", "StartTime": "2026-07- 02T09:20:31+08:0 0", "Params": "", "EventStepName": "BatchReleaseInsta nceStep", "IsIgnore": false, "ApplyFailedList": "", "UpdateTime": "2026-07- 02T09:20:33+08:0 0", "ClusterBzid": "bfi-6nkkQA*****", "ID": 2138, "ErrorMessage": "" } ] } ], "pageSize": 10 } |   |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
"2026-07-05"http://[Endpoint]/?Action=ListHistoryEvent &ClusterId=ack-8EEjd6**** &StartTime="2026-07-01" &EndTime="2026-07-05" &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":1,
  "data":[
```

`{`

```json
    "Status":"success",
    "TaskId":"376ea30f-75b4-11f1-81c7-02420a26*****",
    "EndTime":"2026-07-02T09:20:33+08:00",
    "Message":"success",
    "RequestId":"376ea30f-75b4-11f1-81c7-02420a26*****",
    "ClusterId":"bfi-6nkkQA*****",
    "CreateTime":"2026-07-02T09:20:31+08:00",
    "StartTime":"2026-07-02T09:20:31+08:00",
    "EventName":"ShrinkBFICluster",
    "modifyFields":[
```

`{`

```json
      "paramsValue":[],
      "canModify":false,
      "paramsKey":"BmsVswitchIdList"
```

`},` `{`

```json
      "paramsValue":"",
      "canModify":false,
      "paramsKey":"EvpcId"
```

`},` `{`

```json
      "paramsValue":[],
      "canModify":false,
      "paramsKey":"ApplyFailedInstanceList"
```

`}` `],`

```json
    "UpdateTime":"2026-07-02T09:20:33+08:00",
    "ID":747,
    "DisplaySummary":false,
    "events":[
```

`{`

```json
      "Status":"success",
      "TaskId":"376ea30f-75b4-11f1-81c7-02420a26*****",
      "EndTime":"2026-07-02T09:20:33+08:00",
      "CreateTime":"2026-07-02T09:20:31+08:00",
"StartTime":"2026-07-02T09:20:31+08:00",
```

```json
      StartTime:20260702T09:20:31+08:00,
      "Params":"",
      "EventStepName":"BatchReleaseInstanceStep",
      "IsIgnore":false,
      "ApplyFailedList":"",
      "UpdateTime":"2026-07-02T09:20:33+08:00",
      "ClusterBzid":"bfi-6nkkQA*****",
      "ID":2138,
      "ErrorMessage":""
```

`}` `]` `}` `],`

```json
  "pageSize":10
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <total>1</total>
 <pageNumber>1</pageNumber>
 <data>
  <Status>success</Status>
  <TaskId>376ea30f-75b4-11f1-81c7-02420a26*****</TaskId>
  <EndTime>2026-07-02T09:20:33+08:00</EndTime>
  <Message>success</Message>
  <RequestId>376ea30f-75b4-11f1-81c7-02420a26*****</RequestId>
  <ClusterId>bfi-6nkkQA*****</ClusterId>
  <CreateTime>2026-07-02T09:20:31+08:00</CreateTime>
  <StartTime>2026-07-02T09:20:31+08:00</StartTime>
  <EventName>ShrinkBFICluster</EventName>
  <modifyFields>
   <paramsValue  />
   <canModify>false</canModify>
   <paramsKey>BmsVswitchIdList</paramsKey>
  </modifyFields>
  <modifyFields>
   <paramsValue  />
   <canModify>false</canModify>
   <paramsKey>EvpcId</paramsKey>
  </modifyFields>
  <modifyFields>
   <paramsValue  />
   <canModify>false</canModify>
   <paramsKey>ApplyFailedInstanceList</paramsKey>
  </modifyFields>
UdtTi 20260702T0920330800/UdtTi
```

```xml
  <UpdateTime>2026-07-02T09:20:33+08:00</UpdateTime>
  <ID>747</ID>
  <DisplaySummary>false</DisplaySummary>
  <events>
   <Status>success</Status>
   <TaskId>376ea30f-75b4-11f1-81c7-02420a26*****</TaskId>
   <EndTime>2026-07-02T09:20:33+08:00</EndTime>
   <CreateTime>2026-07-02T09:20:31+08:00</CreateTime>
   <StartTime>2026-07-02T09:20:31+08:00</StartTime>
   <Params  />
   <EventStepName>BatchReleaseInstanceStep</EventStepName>
   <IsIgnore>false</IsIgnore>
   <ApplyFailedList  />
   <UpdateTime>2026-07-02T09:20:33+08:00</UpdateTime>
   <ClusterBzid>bfi-6nkkQA*****</ClusterBzid>
   <ID>2138</ID>
   <ErrorMessage  />
  </events>
 </data>
 <pageSize>10</pageSize>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.2.27 ListReStartEvent

Retry a cluster task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Quer y | No | edbea3ce-76f4-11f1- a9ab-02420a26**** | The task ID. You can call ListHistoryEvent to query the task ID. |
| VswitchIdL ist | Json | Quer y | No | ["vsw- 2ze3ds0mdip0hdz8i****"] | The vSwitch to which the bare metal instance belongs during retry. |

| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise Virtual Private Cloud (EVPC) to which the cluster belongs during retry. |
|---|---|---|---|---|---|
| DeleteAppl yFailedInst anceName List | Json | Quer y | No | ** | The name list of instance names of bare metal instances failed to be createdinstances whose application failed and need to be removed. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | {} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the requestsponse. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListReStartEvent &TaskId=edbea3ce-76f4-11f1-a9ab-02420a26**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":"The retry succeeded",
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>The retry succeeded</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>200</status>
```

##### 5.1.2.28 DeleteAckCluster

Delete a Container Service for Kubernete (ACK) - intelligent computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the ACK - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |

| InstanceLis t | Json | Quer y | No | [ { "hostname": "test", "InstanceId": "i- d8offl6heob05q4v****", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30 } ] | The list of bare metal servers to be removed from the cluster. |
|---|---|---|---|---|---|
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when servers are released. Valid values: true: Yes false: No Default Value: false. |
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period. Unit: hours. Valid values: 1 to 720. Default value: 168. After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the node from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

| data | Map | { "ClusterName": "cluster-name", "ClusterId": "ack- 8EEjd6****", "AckClusterId": "cef51d60a677841 5ab3a8026c24**** *", "AckClusterName": "cluster-name" } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteAckCluster &ClusterId=ack-8EEjd6**** &InstanceList=[
```

`{`

```json
    "hostname": "test",
    "InstanceId": "i-d8offl6heob05q4v****",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "FlopsCount": 30,
    "VideoMemCount": 30
```

`}` `]`

```
&OsUpdate=true &RetentionPeriod=168 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
  "ClusterId":"ack-8EEjd6****",
  "ClusterName":"cluster-name",
  "AckClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
 <ClusterId>ack-8EEjd6****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
 <AckClusterName>cluster-name</AckClusterName>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.1.3 Bare metal – supercomputing cluster

##### 5.1.3.1 CreateEhpcCluster

Create a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization, which identifies the organization to which the resource belongs. |
|---|---|---|---|---|---|
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set, used to classify and manage resources. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region, which indicates the geological location of the cluster. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the available zone. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the cluster. The description must be 0 to 1000 characters in length. |
| Password | Strin g | Quer y | No | Pwd***** | The login password for machines in the cluster to ensure cluster security. |
| DeployMod e | Strin g | Quer y | No | Tiny | The deployment type. Only Tiny is supported. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). The cluster is deployed in the specified VPC. |

| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal server types to be added to the supercomputing cluster. This parameter is required when ClusterArchType is set to standard. |
|---|---|---|---|---|---|
| BmsVswitc hIdList | Json | Quer y | No | null | This parameter is deprecated. |
| StandardV switchId | Strin g | Quer y | No | vsw- 3gagdup8scary04iq**** | The ID of the vSwitch, used to build the management and control service network channel. |
| AccountTy pe | Strin g | Quer y | No | null | This parameter is deprecated. |
| Scheduler Type | Strin g | Quer y | No | pbs | The scheduling type. Valid values: slurm pbs |
| ActivationI d | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The ID of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The code of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard. |
| OsTag | Strin g | Quer y | No | null | This parameter is deprecated. |

| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise VPC (EVPC). You can call the ListEvpc operation to query the EVPC ID. |
|---|---|---|---|---|---|
| IsCreateCp fsCluster | Strin g | Quer y | No | true | This parameter is required when ClusterArchType is set to standard. Only true is supported. |
| CPFSFileSy stem | Strin g | Quer y | No | efs-0137**** | The ID of the high- performance storage file system. Cloud Parallel File System (CPFS) and Apple File System (APFS) file systems are supported. This parameter is optional when ClusterArchType is set to standard. |
| SwitchMet hod | Strin g | Quer y | No | HSW | The vSwitch networking mode. Valid values: CHSW HSW This parameter is required when ClusterArchType is set to managed. |

| VolumeInf o | Json | Quer y | No | [ { "VolumeType": "iscsi", "VolumeParams": { "IP": "127.0.0.1", "ServerIQN": "iqn.2023- 04.com.bms:server", "ClientIQN": "", "ChapEnabled": "true", "UserID": "bms", "Password": "xxxx", "LunID": "0", "Description": "", "ClientAttachPath": "/mnt" } }, { "VolumeType": "nfs", "VolumeParams": { "IP": "127.0.0.1", "Description": "", "ServerPath": "/home/nfstestdir", "ClientAttachPath": "/mnt" } }, { "VolumeType": "mount", "VolumeParams": { "Description": "", "ServerPath": "/dev/sdl1", "ClientAttachPath": "/mnt", "MountParams": "--bind" } } ] | The third-party storage mount information. |
|---|---|---|---|---|---|
| ClusterArc hType | Strin g | Quer y | No | standard | The type of the cluster. Valid values: standard: High- performance computing network managed: High- performance computing management |

| ApplyBmsI nstanceLis t | Json | Quer y | No | [ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****", "ActivationId": "a- hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC- 9AB1-890F1234****" } ] | The list of parameters for requesting bare metal servers. This parameter is required when ClusterArchType is set to managed. |
|---|---|---|---|---|---|
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values: true: Enable false: Disable Default value: false. |
| EvpcEnabl eIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable EVPC IPv6. Valid values: IPv6 can be enabled only when EvpcId is specified. true: Enable false: Disable Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

| data | Map | { "ClusterName":"clu ster-name", "ClusterId": "ehpc- FYUr32****" } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateEhpcCluster &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-env***-d01 &ZoneId=cn-wulan-env***-****-a &ClusterName=cluster-name &DeployMode=Tiny &VpcId=vpc-bp1b1xjllp3ve5yze**** &MachineTypeList=[
```

`{`

```json
 "MachineType": "test",
 "Arch": "x86",
 "CpuCount": 2,
 "MemCount": 4,
 "FlopsCount": 4.8,
 "VideoMemCount": 5,
 "NodeCount": 10,
 "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&StandardVswitchId=vsw-3gagdup8scary04iq**** &SchedulerType=pbs &ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC**** &ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &EvpcId=evpc-htchvitxlfjyso**** &IsCreateCpfsCluster=true &CPFSFileSystem=efs-0137**** &ClusterArchType=standard &EnableIpv6=true &EvpcEnableIpv6=true &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-FYUr32****",
  "ClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>ehpc-FYUr32****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.3.2 ListEhpcCluster

Query the list of bare metal - supercomputing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 12 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 12 | The ID of the resource group. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| EhpcCluste rName | Strin g | Quer y | No | cluster-name | The name of the Elastic High Performance Computing (EHPC) cluster. |
| ClusterId | Strin g | Quer y | No | ehpc-FYUr32**** | The ID of the cluster. |
| EhpcCluste rId | Strin g | Quer y | No | ehpc-123sda | The ID of the EHPC cluster. |

| Status | Strin g | Quer y | No | active | The status of the cluster. Valid values: creating: Creating active: Running createFailed: Creation failed deleting: Deleting deleteFailed: Deletion failed scalingDown: Scaling in scalingDownFailed: Scale-in failed scalingUp: Scaling out scalingUpFailed: Scale- out failed |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| Zone | Strin g | Quer y | No | cn-****-env**-d01-a | The ID of the available zone. |
| ClusterArc hType | Strin g | Quer y | No | standard | The type of the cluster. Valid values: standard: High performance computing high- network cluster managed: High performance computing managed cluster |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise VPC (EVPC). You can call the ListEvpc operation to query the EVPC ID. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). The cluster is deployed in the specified VPC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "TotalCount": 2, "PageNumber": 1, "PageSize": 10, "ClusterList": [ { "ClusterId": "ehpc- SH7mwNVS9r", "ClusterName": "ehpc1", "CpfsClusterState": "", "Description": "Test cluster", "Status": "active", "CreateTime": "2023-11- 29T17:08:15+08:0 0", "UpdateTime": "2023-12- 08T10:25:37+08:0 0", "NodeCount": 3, "ActiveNodeCount" : 1, "CpuCount": 10, "MemCount": 36, "FlopsCount": 50, "VideoMemory": 50, "Region": "local", "Organization": "zpf", "ResourceGroup": "zpf1", "VpcId": "vpc-xxxxxxx", "ClusterArchType": "standard", "EvpcId": "evpc- xxx", "Zone": "xxxxx", "IsSetPassword": true, "SchedulerType": "slurm" }, { "ClusterId": "ehpc- sdfsdfsd", "ClusterName": "ehpc2", "Description": "test", "Status": "active", "CreateTime": | The response data. |

|   |   | "2023-12- 07T10:00:00+08:0 0", "UpdateTime": "2023-12- 07T10:00:00+08:0 0", "NodeCount": 2, "CpuCount": 11, "MemCount": 12, "FlopsCount": 13, "VideoMemory": 50, "Region": "local", "Organization": "zpf", "ResourceGroup": "zpf1", "VpcId": "vpc-xxxxxxx", "ClusterArchType": "standard", "EvpcId": "evpc- xxx", "Zone": "xxxxx", "IsSetPassword": true, "SchedulerType": "slurm" } ] } |   |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

`JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":2,
  "ClusterList":[
```

`{`

```json
    "Status":"active",
    "Description":"Test cluster",
    "ActiveNodeCount":1,
    "Organization":"zpf",
    "IsSetPassword":true,
    "NodeCount":3,
    "ClusterId":"ehpc-SH7mwNVS9r",
    "Zone":"xxxxx",
"CreateTime":"2023-11-29T17:08:15+08:00",
```

```json
    CreateTime:20231129T17:08:15+08:00,
    "SchedulerType":"slurm",
    "CpfsClusterState":"",
    "MemCount":36,
    "EvpcId":"evpc-xxx",
    "ClusterArchType":"standard",
    "FlopsCount":50,
    "CpuCount":10,
    "VpcId":"vpc-xxxxxxx",
    "UpdateTime":"2023-12-08T10:25:37+08:00",
    "ClusterName":"ehpc1",
    "Region":"local",
    "VideoMemory":50,
    "ResourceGroup":"zpf1"
```

`},` `{`

```json
    "Status":"active",
    "Description":"test",
    "Organization":"zpf",
    "IsSetPassword":true,
    "NodeCount":2,
    "ClusterId":"ehpc-sdfsdfsd",
    "Zone":"xxxxx",
    "CreateTime":"2023-12-07T10:00:00+08:00",
    "SchedulerType":"slurm",
    "MemCount":12,
    "EvpcId":"evpc-xxx",
    "ClusterArchType":"standard",
    "FlopsCount":13,
    "CpuCount":11,
    "VpcId":"vpc-xxxxxxx",
    "UpdateTime":"2023-12-07T10:00:00+08:00",
    "ClusterName":"ehpc2",
    "Region":"local",
    "VideoMemory":50,
    "ResourceGroup":"zpf1"
```

`}` `],`

```json
  "PageSize":10,
  "PageNumber":1
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>2</TotalCount>
<Cl
```

`t`

```
Lit>
```

|   | Bare Metal Computing Platform D Machine Learning Platform for AI eveloper Guide·API referenc | e |
|---|---|---|
|   | <ClusterList> <Status>active</Status> <Description>Test cluster</Description> <ActiveNodeCount>1</ActiveNodeCount> <Organization>zpf</Organization> <IsSetPassword>true</IsSetPassword> <NodeCount>3</NodeCount> <ClusterId>ehpc-SH7mwNVS9r</ClusterId> <Zone>xxxxx</Zone> <CreateTime>2023-11-29T17:08:15+08:00</CreateTime> <SchedulerType>slurm</SchedulerType> <CpfsClusterState /> <MemCount>36</MemCount> <EvpcId>evpc-xxx</EvpcId> <ClusterArchType>standard</ClusterArchType> <FlopsCount>50</FlopsCount> <CpuCount>10</CpuCount> <VpcId>vpc-xxxxxxx</VpcId> <UpdateTime>2023-12-08T10:25:37+08:00</UpdateTime> <ClusterName>ehpc1</ClusterName> <Region>local</Region> <VideoMemory>50</VideoMemory> <ResourceGroup>zpf1</ResourceGroup> </ClusterList> <ClusterList> <Status>active</Status> <Description>test</Description> <Organization>zpf</Organization> <IsSetPassword>true</IsSetPassword> <NodeCount>2</NodeCount> <ClusterId>ehpc-sdfsdfsd</ClusterId> <Zone>xxxxx</Zone> <CreateTime>2023-12-07T10:00:00+08:00</CreateTime> <SchedulerType>slurm</SchedulerType> <MemCount>12</MemCount> <EvpcId>evpc-xxx</EvpcId> <ClusterArchType>standard</ClusterArchType> <FlopsCount>13</FlopsCount> <CpuCount>11</CpuCount> <VpcId>vpc-xxxxxxx</VpcId> <UpdateTime>2023-12-07T10:00:00+08:00</UpdateTime> <ClusterName>ehpc2</ClusterName> <Region>local</Region> <VideoMemory>50</VideoMemory> <ResourceGroup>zpf1</ResourceGroup> </ClusterList> <PageSize>10</PageSize> <PageNumber>1</PageNumber> </data> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status> |   |

```xml
<status>200</status>
```

##### 5.1.3.3 DescribeEhpcCluster

Query the details of a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ehpc-TsrIaN**** | The ID of the bare metal - supercomputing cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

|   |   | { "ClusterId": "ehpc- SH7mwNVS9r", "ClusterName": "ehpc1", "Description": "Test cluster", "Status": "scalingDown", "CreateTime": "2023-11- |   |
|---|---|---|---|
| data | Map | 29T17:08:15+08:0 0", "UpdateTime": "2023-12- 13T15:15:25+08:0 0", "NodeCount": 3, "ActiveNodeCount" : 1, "CpuCount": 10, "MemCount": 36, "FlopsCount": 50, "VideoMemory": 50, "Region": "cn- ****-env**-d01", "Organization": "zpf", "ResourceGroup": "zpf1", "InstanceList": [ "11", "22", "33" ], "VpcId": "vpc- xxxxxxx", "ClusterArchType": "standard", "EvpcId": "evpc- 67mby5210ty3ul** **", "Zone": "cn- ****-env**-d01-a", "IsSetPassword": true, "SchedulerType": "slurm", "CpfsClusterType": "CPFS", "CpfsMountFs": "xxxx", "CpfsClusterState": "", "EnableIpv6": false, "EvpcEnableIpv6": false } | The response data. |
| > Document Versi | on: 20260731 |   | 18 |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DescribeEhpcCluster &ClusterId=ehpc-TsrIaN**** &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "Description":"Test cluster",
  "Organization":"zpf",
  "IsSetPassword":true,
  "CpfsClusterType":"CPFS",
  "EvpcId":"evpc-67mby5210ty3ul****",
  "EnableIpv6":false,
  "FlopsCount":50,
  "CpuCount":10,
  "EvpcEnableIpv6":false,
  "ClusterName":"ehpc1",
  "ResourceGroup":"zpf1",
  "Status":"scalingDown",
  "ActiveNodeCount":1,
  "NodeCount":3,
  "ClusterId":"ehpc-SH7mwNVS9r",
  "Zone":"cn-****-env**-d01-a",
  "CreateTime":"2023-11-29T17:08:15+08:00",
  "SchedulerType":"slurm",
  "CpfsClusterState":"",
  "MemCount":36,
  "ClusterArchType":"standard",
  "VpcId":"vpc-xxxxxxx",
  "UpdateTime":"2023-12-13T15:15:25+08:00",
  "Region":"cn-****-env**-d01",
  "CpfsMountFs":"xxxx",
  "VideoMemory":50,
  "InstanceList":[
   "11",
   "22",
   "33"
```

`]` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <Description>Test cluster</Description>
 <Organization>zpf</Organization>
 <IsSetPassword>true</IsSetPassword>
 <CpfsClusterType>CPFS</CpfsClusterType>
 <EvpcId>evpc-67mby5210ty3ul****</EvpcId>
 <EnableIpv6>false</EnableIpv6>
 <FlopsCount>50</FlopsCount>
 <CpuCount>10</CpuCount>
 <EvpcEnableIpv6>false</EvpcEnableIpv6>
 <ClusterName>ehpc1</ClusterName>
 <ResourceGroup>zpf1</ResourceGroup>
 <Status>scalingDown</Status>
 <ActiveNodeCount>1</ActiveNodeCount>
 <NodeCount>3</NodeCount>
 <ClusterId>ehpc-SH7mwNVS9r</ClusterId>
 <Zone>cn-****-env**-d01-a</Zone>
 <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
 <SchedulerType>slurm</SchedulerType>
 <CpfsClusterState />
 <MemCount>36</MemCount>
 <ClusterArchType>standard</ClusterArchType>
 <VpcId>vpc-xxxxxxx</VpcId>
 <UpdateTime>2023-12-13T15:15:25+08:00</UpdateTime>
 <Region>cn-****-env**-d01</Region>
 <CpfsMountFs>xxxx</CpfsMountFs>
 <VideoMemory>50</VideoMemory>
 <InstanceList>11</InstanceList>
 <InstanceList>22</InstanceList>
 <InstanceList>33</InstanceList>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.3.4 AddEhpcClusterInstances

Scale out a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterId | Strin g | Quer y | No | ehpc-FYUr32**** | The ID of the bare metal - supercomputing cluster. You can call the ListEhpcCluster operation to query the cluster ID. |
|---|---|---|---|---|---|
| Password | Strin g | Quer y | No | Pwd***** | The bare metal server password to be modified. If no password has been set for the cluster, you must specify this parameter. |
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal server types to be added to the supercomputing cluster. This parameter is required when ClusterArchType is set to standard. |
| BmsVswitc hIdList | Json | Quer y | No | null | This parameter is deprecated. |
| ActivationI d | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The ID of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The code of the Cloud Assistant activation code. This parameter is required when ClusterArchType is set to standard. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the available zone. |

| ApplyBmsI nstanceLis t | Json | Quer y | No | [ { "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30, "InstanceName": "myinstance", "UseOriginImage": true, "ImageType": "", "Image": "", "HostName": "xxx", "InstanceAlias": "xxx", "Description": "testDescription", "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****", "ActivationId": "a- hz0ch3SwhOlE1234+Xo3 2lAZC****", "ActivationCode": "4ECEEE12-56F1-4FBC- 9AB1-890F1234****" } ] | The list of parameters for requesting bare metal servers. This parameter is required when ClusterArchType is set to managed. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "test", "ClusterId": "ehpc-WbetRt****" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=AddEhpcClusterInstances &ClusterId=ehpc-FYUr32**** &Password=Pwd***** &ZoneId=cn-wulan-env***-****-a &MachineTypeList=
```

`[` `{`

```json
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30,
 "InstanceName": "myinstance",
 "UseOriginImage": true,
 "ImageType": "",
 "Image": "",
 "HostName": "xxx",
 "InstanceAlias": "xxx",
 "Description": "testDescription",
 "NodePoolName": "bmcp-node-pool",
 "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC**** &ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-WbetRt****",
  "ClusterName":"test"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>ehpc-WbetRt****</ClusterId>
 <ClusterName>test</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.3.5 DeleteEhpcClusterInstances

Scale in a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ehpc-TsrIaN**** | The ID of the bare metal - supercomputing cluster. You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceId List | Json | Quer y | No | ["i- d92sc86heobfdsc1****"] | The list of node IDs to be removed from the cluster. |
| InstanceLis t | Json | Quer y | No | [ { "hostname": "test", "InstanceId": "i- d8offl6heob05q4v****", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30 } ] | The list of bare metal servers to be removed from the cluster. |

| OsUpdate | Bool ean | Quer y | No | false | Specifies whether to clean data disks when machines are released. true: Clean false: Do not clean |
|---|---|---|---|---|---|
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period. Unit: hours. Value range: 1 to 720. Default value: 168. After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName": "test", "ClusterId": "ehpc-WbetRt****" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteEhpcClusterInstances &ClusterId=ehpc-FYUr32**** &InstanceIdList=["i-d92sc86heobfdsc1****","i-d8t4ltuheob3s2j0****"] &ZoneId=cn-wulan-env***-****-a &InstanceList=
```

`[` `{`

```json
 "hostname": "test",
 "InstanceId": "i-d8offl6heob05q4v****",
 "InstanceIp": "127.0.0.1",
 "SN": "980017160373****",
 "InstanceType": "P5N1",
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30
```

`}` `]`

```
&ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC**** &ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-WbetRt****",
  "ClusterName":"test"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>ehpc-WbetRt****</ClusterId>
 <ClusterName>test</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

##### 5.1.3.6 DeleteEhpcCluster

Delete a bare metal - supercomputing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ehpc-FYUr32**** | The ID of the bare metal - supercomputing cluster. You can call the ListEhpcCluster operation to query the cluster ID. |
| InstanceLis t | Json | Quer y | No | [ { "hostname": "test", "InstanceId": "i- d8offl6heob05q4v****", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "FlopsCount": 30, "VideoMemCount": 30 } ] | The list of bare metal servers to be removed from the cluster. |
| OsUpdate | Bool ean | Quer y | No | true | Specifies whether to clean data disks when machines are released. Valid values: true: Yes false: No Default value: false. |

| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period. Unit: hours. Value range: 1 to 720. Default value: 168. After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterName":"tes t", "ClusterId": "ehpc-WbetRt****" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteEhpcCluster &ClusterId=ehpc-FYUr32**** &InstanceList=[
```

`{`

```json
 "hostname": "test",
 "InstanceId": "i-d8offl6heob05q4v****",
 "InstanceIp": "127.0.0.1",
 "SN": "980017160373****",
 "InstanceType": "P5N1",
 "CpuCount": 2,
 "MemCount": 16,
 "FlopsCount": 30,
 "VideoMemCount": 30
```

`}` `]`

```
&OsUpdate=true &RetentionPeriod=168 &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"ehpc-WbetRt****",
  "ClusterName":"test"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>ehpc-WbetRt****</ClusterId>
 <ClusterName>test</ClusterName>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.1.4 Converged computing cluster

##### 5.1.4.1 CreateBFICluster

Create a converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The cluster name, which must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). |
| Descriptio n | Strin g | Quer y | No | testDescription | The cluster description, which must be 0 to 1,000 characters in length. |
| Password | Strin g | Quer y | No | Pwd***** | The login password of the machines in the cluster. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters, including ()`~!@#$%^&*- +=\|{} _ []:;'<>,.?/ |

| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the zone. |
|---|---|---|---|---|---|
| ClusterArc hType | Strin g | Quer y | No | standard | The cluster type. Valid values: standard: converged high-bandwidth network base: converged basic |
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal server types to be added to the cluster. |
| VswitchIdL ist | Json | Quer y | No | null | This parameter is deprecated. |
| StandardV switchId | Strin g | Quer y | No | vsw- 3gagdup8scary04iq**** | The ID of the vSwitch for building the management and control service network channel. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the Enterprise VPC (EVPC). This parameter is required when ClusterArchType is set to standard. You can call the ListEvpc operation to query the EVPC ID. |
| ActivationI d | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The ID of the Cloud Assistant activation code. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The code of the Cloud Assistant activation code. |

| IsCreateCp fsCluster | Bool ean | Quer y | No | true | Specifies whether to enable the high- performance storage client cluster. Valid values: true: Enable the cluster. false: Disable the cluster. Default value: false This parameter can be configured when ClusterArchType is set to standard. To enable the high- performance storage cluster, make sure that an EVPC ID is selected, the number of Cloud Parallel File System (CPFS)-type bare metal nodes is at least 3, and the number of Apple File System (APFS)-bare metal nodes is at least 1. |
|---|---|---|---|---|---|
| CpfsCluste rType | Strin g | Quer y | No | CPFS | The type of the high- performance storage client cluster. Valid values: CPFS APFS This parameter is required when IsCreateCpfsCluster is set to true. |
| IsInstallYu ndunAegis | Bool ean | Quer y | No | true | Specifies whether to install Server Guard. Valid values: true: Install Server Guard. false: Do not install Server Guard. Default value: true |

| SwitchMet hod | Strin g | Quer y | No | HSW | The switch networking method. Currently, only EHSW is supported. |
|---|---|---|---|---|---|
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values: true: Enable IPv6. false: Disable IPv6. Default value: false |
| EvpcEnabl eIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable EVPC IPv6. EVPC IPv6 can be enabled only when EvpcId is configured. true: Enable EVPC IPv6. false: Disable EVPC IPv6. Default value: false |
| SecurityGr oupId | Strin g | Quer y | No | sg-bp67acfmxazb4p**** | The security group ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterName":"clu ster-name", "ClusterId": "bfi- ZZMA5n****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateBFICluster &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-env***-d01 &ZoneId=cn-wulan-env***-****-a &VpcId=vpc-bp1b1xjllp3ve5yze**** &ClusterName=cluster-name &ClusterArchType=standard &MachineTypeList=[
```

`{`

```json
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&StandardVswitchId=vsw-3gagdup8scary04iq**** &EvpcId=evpc-htchvitxlfjyso**** &ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC**** &ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &IsCreateCpfsCluster=true &CpfsClusterType=CPFS &SwitchMethod=EHSW &EnableIpv6=true &EvpcEnableIpv6=true &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.4.2 ListBFICluster

Query the list of converged computing clusters.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |

| ClusterId | Strin g | Quer y | No | bfi-ZZMA5n**** | The ID of the converged computing cluster. |
|---|---|---|---|---|---|
| Status | Strin g | Quer y | No | active | The cluster status. Valid values: creating: Creating active: Running createFailed: Creation failed deleting: Deleting deleteFailed: Deletion failed scalingDown: Scaling in scalingDownFailed: Scale-in failed scalingUp: Scaling out scalingUpFailed: Scale- out failed |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
|   |   | { "ClusterList": [ { "Description": "ycc- apfs", "Organization": "5", "IsSetPassword": true, "SwitchMethod": "CHSW", "CpfsClusterType": "APFS", "Gpu": [ { "GpuNum": 32, |   |

|   |   |   | eveloper Guide·API referenc |
|---|---|---|---|
| data | Map | "GpuModel": "NVIDIA Ampere A _ _ 100 80G NVLink" } _ _ ], "EvpcId": "evpc- pi2q***z8b", "EnableIpv6": false, "FlopsCount": 9984, "VolumeId": "", "Department": 5, "CpuCount": 512, "ClusterName": "ycc-apfs", "ResourceGroup": 4, "Status": "active", "ActiveNodeCount" : 4, "NodeCount": 4, "ClusterId": "bfi- v8***QVZT", "Zone": "cn- ne****test236001- a", "CreateTime": "2026-01- 12T10:44:46+08:0 0", "Specification": [ { "Count": 3, "Name": "gBMC- Ci8af8nbr" } ], "CpfsClusterState": "error", "AscmCreateUser": "admin", "MemCount": 8192, "ClusterArchType": "standard", "VpcId": "vpc- 7kkjbu****od7pxs6 10", "OldClusterBzid": "", "UpdateTime": "2026-01- 22T15:58:01+08:0 0", "Region": "cn- ne****6e-d01", "CpfsMountFs": "efs-01***08", "RegionId": "cn- ****-d01", "VideoMemory": 2560, "EnableIpv6": true, "EvpcEnableIpv6": true } ], "PageSize": 10, "TotalCount": 3, "PageNumber": 1 } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListBFICluster &Department=4 &ResourceGroup=3 &Status=active &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":3,
  "ClusterList":[
```

`{`

```json
    "Description":"ycc-apfs",
    "Organization":"5",
    "IsSetPassword":true,
    "SwitchMethod":"CHSW",
    "CpfsClusterType":"APFS",
    "Gpu":[
```

`{`

```json
      "GpuNum":32,
      "GpuModel":"NVIDIA_Ampere_A100_80G_NVLink"
```

`}` `],`

```json
    "EvpcId":"evpc-pi2q***z8b",
    "EnableIpv6":true,
    "FlopsCount":9984,
    "VolumeId":"",
    "Department":5,
    "CpuCount":512,
    "EvpcEnableIpv6":true,
    "ClusterName":"ycc-apfs",
    "ResourceGroup":4,
    "Status":"active",
    "ActiveNodeCount":4,
    "NodeCount":4,
"ClsterId""bfi 8***QVZT"
```

```json
    "ClusterId":"bfi-v8***QVZT",
    "Zone":"cn-ne****test236001-a",
    "CreateTime":"2026-01-12T10:44:46+08:00",
    "Specification":[
```

`{`

```json
      "Count":3,
      "Name":"gBMC-Ci8af8nbr"
```

`}` `],`

```json
    "CpfsClusterState":"error",
    "AscmCreateUser":"admin",
    "MemCount":8192,
    "ClusterArchType":"standard",
    "VpcId":"vpc-7kkjbu****od7pxs610",
    "OldClusterBzid":"",
    "UpdateTime":"2026-01-22T15:58:01+08:00",
    "Region":"cn-ne****6e-d01",
    "CpfsMountFs":"efs-01***08",
    "RegionId":"cn-****-d01",
    "VideoMemory":2560
```

`}` `],`

```json
  "PageSize":10,
  "PageNumber":1
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>3</TotalCount>
 <ClusterList>
  <Description>ycc-apfs</Description>
  <Organization>5</Organization>
  <IsSetPassword>true</IsSetPassword>
  <SwitchMethod>CHSW</SwitchMethod>
  <CpfsClusterType>APFS</CpfsClusterType>
  <Gpu>
   <GpuNum>32</GpuNum>
   <GpuModel>NVIDIA_Ampere_A100_80G_NVLink</GpuModel>
  </Gpu>
  <EvpcId>evpc-pi2q***z8b</EvpcId>
  <EnableIpv6>true</EnableIpv6>
  <FlopsCount>9984</FlopsCount>
  <VolumeId  />
  <Department>5</Department>
  <CpuCount>512</CpuCount>
  <EvpcEnableIpv6>true</EvpcEnableIpv6>
  <ClusterName>ycc-apfs</ClusterName>
  <ResourceGroup>4</ResourceGroup>
  <Status>active</Status>
  <ActiveNodeCount>4</ActiveNodeCount>
  <NodeCount>4</NodeCount>
  <ClusterId>bfi-v8***QVZT</ClusterId>
  <Zone>cn-ne****test236001-a</Zone>
  <CreateTime>2026-01-12T10:44:46+08:00</CreateTime>
  <Specification>
   <Count>3</Count>
   <Name>gBMC-Ci8af8nbr</Name>
  </Specification>
  <CpfsClusterState>error</CpfsClusterState>
  <AscmCreateUser>admin</AscmCreateUser>
  <MemCount>8192</MemCount>
  <ClusterArchType>standard</ClusterArchType>
  <VpcId>vpc-7kkjbu****od7pxs610</VpcId>
  <OldClusterBzid  />
  <UpdateTime>2026-01-22T15:58:01+08:00</UpdateTime>
  <Region>cn-ne****6e-d01</Region>
  <CpfsMountFs>efs-01***08</CpfsMountFs>
  <RegionId>cn-****-d01</RegionId>
  <VideoMemory>2560</VideoMemory>
 </ClusterList>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.4.3 DescribeBFICluster

Query the details of a Big Data Federation Infrastructure (BFI) cluster, including cluster status, node list, resource configuration, and runtime metrics.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bfi-ZZMA5n**** | The ID of the converged computing cluster. You can call the ListBFICluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

|   |   | { "Status": "active", "Description": "testDescription", "ActiveNodeCount" : 1, "Organization": "4", "IsSetPassword": true, "NodeCount": |   |
|---|---|---|---|
| data | Map | 3, "ClusterId": "bfi- ZZMA5n****", "Zone": "cn-****- env**-d01-a", "CreateTime": "2023-11- 29T17:08:15+08:0 0", "MemCount": 36, "EvpcId": "evpc- htchvitxlfjyso****", "ClusterArchType": "standard", "FlopsCount": 50, "CpuCount": 10, "VpcId": "vpc- bp1b1xjllp3ve5yze ****", "UpdateTime": "2023-12- 13T15:15:25+08:0 0", "ClusterName": "cluster-name", "Region": "cn-****- env**-d01", "VideoMemory": 50, "InstanceList": [ "i- d8offheheob5qaf0* ***", "i- d620b2eheobcabte ****", "i- d75ppnuheobcnhq o****" ], "ResourceGroup": "3" } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBFICluster &ClusterId=bfi-ZZMA5n**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"1.0",
 "data":{
  "Status":"active",
  "Description":"testDescription",
  "ActiveNodeCount":1,
  "Organization":"4",
  "IsSetPassword":true,
  "NodeCount":3,
  "ClusterId":"bfi-ZZMA5n****",
  "Zone":"cn-****-env**-d01-a",
  "CreateTime":"2023-11-29T17:08:15+08:00",
  "MemCount":36,
  "EvpcId":"evpc-htchvitxlfjyso****",
  "ClusterArchType":"standard",
  "FlopsCount":50,
  "CpuCount":10,
  "VpcId":"vpc-bp1b1xjllp3ve5yze****",
  "UpdateTime":"2023-12-13T15:15:25+08:00",
  "ClusterName":"cluster-name",
  "Region":"cn-****-env**-d01",
  "VideoMemory":50,
  "InstanceList":[
   "i-d8offheheob5qaf0****",
   "i-d620b2eheobcabte****",
   "i-d75ppnuheobcnhqo****"
```

`],`

```json
  "ResourceGroup":"3"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>1.0</responseVersion> <data>
 <Status>active</Status>
 <Description>testDescription</Description>
 <ActiveNodeCount>1</ActiveNodeCount>
 <Organization>4</Organization>
 <IsSetPassword>true</IsSetPassword>
 <NodeCount>3</NodeCount>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <Zone>cn-****-env**-d01-a</Zone>
 <CreateTime>2023-11-29T17:08:15+08:00</CreateTime>
 <MemCount>36</MemCount>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
 <ClusterArchType>standard</ClusterArchType>
 <FlopsCount>50</FlopsCount>
 <CpuCount>10</CpuCount>
 <VpcId>vpc-bp1b1xjllp3ve5yze****</VpcId>
 <UpdateTime>2023-12-13T15:15:25+08:00</UpdateTime>
 <ClusterName>cluster-name</ClusterName>
 <Region>cn-****-env**-d01</Region>
 <VideoMemory>50</VideoMemory>
 <InstanceList>i-d8offheheob5qaf0****</InstanceList>
 <InstanceList>i-d620b2eheobcabte****</InstanceList>
 <InstanceList>i-d75ppnuheobcnhqo****</InstanceList>
 <ResourceGroup>3</ResourceGroup>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.4.4 ExpandBFICluster

Scale out a converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bfi-ZZMA5n**** | The ID of the converged computing cluster. You can call the ListBFICluster operation to query the cluster ID. |

| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal server types to be added to the cluster. This parameter is required when ClusterArchType is set to standard or base. |
|---|---|---|---|---|---|
| VswitchIdL ist | Json | Quer y | No | ["vsw- 2ze3ds0mdip0hdz8i****", "vsw- 3gagdup8scary04iq****"] | The vSwitch list for the node pool, used for network configuration. |
| ActivationI d | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The ID of the Cloud Assistant activation code. |
| Activation Code | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The code of the Cloud Assistant activation code. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the zone where the clutser is deployed. |
| SecurityGr oupId | Strin g | Quer y | No | sg-bp67acfmxazb4p**** | The security group ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "ClusterName": "cluster-name", "ClusterId": "bfi- ZZMA5n****" } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the API response, which is used to handle APIs of different versions. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ExpandBFICluster &ClusterId=bfi-ZZMA5n**** &MachineTypeList=[
```

`{`

```json
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&VswitchIdList= ["vsw-2ze3ds0mdip0hdz8i****","vsw-3gagdup8scary04iq****"] &ActivationId=a-hz0ch3SwhOlE1234+Xo32lAZC**** &ActivationCode=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &ZoneId=cn-wulan-env***-****-a &SecurityGroupId=sg-bp67acfmxazb4p**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"1.0",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>1.0</responseVersion> <data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

##### 5.1.4.5 ShrinkBFICluster

Scale in a converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bfi-FYUr32**** | The ID of the converged computing cluster. You can call the ListBFICluster operation to query the cluster ID. |
| InstanceId List | Json | Quer y | No | ["1","2"] | The ID list of instances to be removed from the cluster. |
| InstanceLis t | Json | Quer y | No | [ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ] | The list of bare metal instances to be removed from the cluster. |

| OsUpdate | Bool ean | Quer y | No | false | Specifies whether to clean data disks when machines are released. Valid values: true: Clean data disks. false: Do not clean data disks. |
|---|---|---|---|---|---|
| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period. Unit: hours. Valid values: 1 to 720 Default value: 168 After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "ClusterName":"clu ster-name", "ClusterId": "bfi- ZZMA5n****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ShrinkBFICluster &ClusterId=bfi-FYUr32**** &InstanceIdList=["11","21"] &ZoneId=cn-wulan-env***-****-a &InstanceList=
```

`[` `{`

```json
    "InstanceId": "11",
    "InstanceIp": "127.0.0.1",
    "SN": "980017160373****",
    "InstanceType": "P5N1",
    "CpuCount": 2,
    "MemCount": 16,
    "VideoMemCount": 30
```

`}` `]`

```
&OsUpdate=true &RetentionPeriod=168 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

##### 5.1.4.6 DeleteBFICluster

Delete a specified converged computing cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bfi-FYUr32**** | The ID of the converged computing cluster. You can call the ListBFICluster operation to query the cluster ID. |
| OsUpdate | Bool ean | Quer y | No | false | Specifies whether to clean data disks when machines are released. true: Clean data disks. false: Do not clean data disks. |

| RetentionP eriod | Integ er | Quer y | No | 5 | The retention period of instances in the recycle bin. Unit: hours. Valid values: 1 to 720 Default value: 168 After scaling in a Bare Metal Computing Platform (BMCP) cluster, the system moves the removed nodes to the recycle bin. Within the retention period, you can restore the nodes from the recycle bin to the original cluster. After the retention period expires, the system automatically releases the nodes back to the resource pool. |
|---|---|---|---|---|---|
| InstanceLis t | Json | Quer y | No | [ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ] | The list of bare metal instances to be removed from the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "ClusterName":"clu ster-name", "ClusterId": "bfi- ZZMA5n****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```json
http://[Endpoint]/?Action=DeleteBFICluster &ClusterId=bfi-ZZMA5n**** &OsUpdate=false &RetentionPeriod=5 &InstanceList=[ { "InstanceId": "11", "InstanceIp": "127.0.0.1", "SN": "980017160373****", "InstanceType": "P5N1", "CpuCount": 2, "MemCount": 16, "VideoMemCount": 30 } ] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterId":"bfi-ZZMA5n****",
  "ClusterName":"cluster-name"
```

`},`

```json
 "errorTitle":"",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterId>bfi-ZZMA5n****</ClusterId>
 <ClusterName>cluster-name</ClusterName>
</data> <errorTitle></errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

#### 5.1.5 ListInstance

Query the list of Bare Metal Computing Platform (BMCP) instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| InstanceN ame | Strin g | Quer y | No | myinstance | The instance name. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | "" | The error title. |
| errorMessage | String | "" | The error message. |
|   |   | { "data": { "DeployType": "bfi base", _ "RunningState": "offline", "CGWPorts": "TwoHundredGigE1 /0/65:1,TwoHundre dGigE1/0/65:2,Two HundredGigE1/0/6 6:1,TwoHundredGi gE1/0/66:2", "IDC": "amtest****", "SANZone": "", "Image": "alinux 3 x86 64 _ _ _ _ aiext 20260623 bf _ _ |   |

|   |   | 3.qcow2", "InnerBandwidth": "", "Gpu": "", |   |
|---|---|---|---|
|   |   | "ImageType": "", "InstanceAlias": "i- 7c4ba42a32f64*** *", "AliYunAssistID": "mi- rg6owzr81e****", "ID": 108, "Disk": 0, "RawIP": "192.168.***.***", "HostName": "SN- 2106196KUPXDP50 0****", "Disable": false, "ErrorDescription": "[a-87c59321- 7ac5-11f1-9014- 02420a2608cd]reo nlineNcEni timeout, eniList not ready", "Status": "power on", _ "DeviceModel": "BFIBaseStack", "Protected": true, "IP": "192.168.***.***", "DefaultHostName" : "SN- 2106196KUPXDP50 0****", "PrimaryEniId": "eni- 9lpy8hgva2pl0g*** *", "WarrantyPeriod": "2027-01- 01T00:00:00+08:0 0", "InstanceName": "i- d8t4ltuheob3s2j0** **", "SecondaryEniId": "eni- 3ga00weu4ouu93b c****", "SSHUser": "", "State": "error", "BMCIP": "10.38.***.****", "Region": "cn- wulan-****-d01", "NetworkCardType ": "", "AgentID": 48, "Subnet": "EHSW-1-****-A- ****", "RackUnit": "21", "Organization": "4", "Description": "", "VPCID": "vpc- 3gasnqceysuxdia5 k****", |   |

| data | Map | "ImageSize": 0, "IPv6": "", "Config": { "Memory": 0, "CPUNumber": 0 }, "BMCPassword": "", "DpuInfo": { "ErrorDescription": "", "Status": "power on", _ "LoginName": "root", "MachineSN": "2106196KUPXDP5 00****", "RunningState": "running", "CGWPorts": "THGigabitEthe**** 0/20:1,THGigabitEt hernet0/20:1", "Zone": "", "Hostname": "c25d0****.cloud.d 03.am****", "MachineType": "PG58P2M6S2****. 32", "BMCPassword": "****", "Specification": "", "BMCPort": "", "InstanceName": "dpu-i- 0919****ad914**** ", "BMCIP": "10.38.***.****", "LastHeartbeatTim e": "2026-07- 15T17:28:46+08:0 0", "ID": 1, "SN": "MT2430XZ****", "BMCUser": "****", "ASWID": "****", "Subnet": "", "RawIP": "10.38.***.***", "LoginPwd": "" }, "SSHRsaId": "", "MappingStatus": "OperatedFailed", "Rack": "D03", "ApplicationGroup" : "instance", "GpuNum": 0, "NetworkCardNum" : 0, "SubnetIP": "10.38.***.***", "VPCSubnet": "vsw- 3ga970i9dqzq7byb m****", "SN": "****", "BMCUser": "****", "Deleted": false, "Room": "C2- 5", "ResourceGroup": | The response data. |
|---|---|---|---|
| 22 |   |   | > Document Version: 2026073 |

|   |   | "3", "SSHPwd": "", "ImageUniqueKey": "", "UserName": "", "OS": "", "UnitNum": 0, "Zone": "cn-wulan- ****-amte****-a", "CreateTime": "2026-06- 24T17:19:05+08:0 0", "MachineType": "PG58P2M6S****.3 2", "NetworkMode": "vpc", "CPUArch": "", "BMCPort": "", "WWN": "", "Extra": "", "DefaultImage": "alinux 3 x86 64 _ _ _ _ aiext 20260623 bf _ _ 3.qcow2", "UserId": "127756957048*** *", "UpdateTime": "2026-07- 08T20:26:43+08:0 0", "LastHeartbeatTim e": "2026-07- 09T13:54:42+08:0 0", "ASWID": "****", "Tag": "" } } |   |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. true: Success false: Failure |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListInstance &Common request parameters
```

Sample success responses `JSON` format `{` `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "DeployType":"bfi_base",
   "RunningState":"offline",
"CGWPorts":"TwoHundredGigE1/0/65:1,TwoHundredGigE1/0/65:2,TwoHundredGigE1/0/66:1,TwoHundr GigE1/0/66:2",
   "IDC":"amtest****",
   "SANZone":"",
   "Image":"alinux_3_x86_64_aiext_20260623_bf3.qcow2",
   "InnerBandwidth":"",
   "Gpu":"",
   "ImageType":"",
   "InstanceAlias":"i-7c4ba42a32f64****",
   "AliYunAssistID":"mi-rg6owzr81e****",
   "ID":108,
   "Disk":0,
   "RawIP":"192.168.***.***",
   "HostName":"SN-2106196KUPXDP500****",
   "Disable":false,
   "ErrorDescription":"[a-87c59321-7ac5-11f1-9014-02420a2608cd]reonlineNcEni timeout, e
niList not ready",
   "Status":"power_on",
   "DeviceModel":"BFIBaseStack",
   "Protected":true,
   "IP":"192.168.***.***",
   "DefaultHostName":"SN-2106196KUPXDP500****",
   "PrimaryEniId":"eni-9lpy8hgva2pl0g****",
   "WarrantyPeriod":"2027-01-01T00:00:00+08:00",
   "InstanceName":"i-d8t4ltuheob3s2j0****",
   "SecondaryEniId":"eni-3ga00weu4ouu93bc****",
   "SSHUser":"",
   "State":"error",
   "BMCIP":"10.38.***.****",
   "Region":"cn-wulan-****-d01",
   "NetworkCardType":"",
   "AgentID":48,
   "Subnet":"EHSW-1-****-A-****",
   "RackUnit":"21",
   "Organization":"4",
   "Description":"",
   "VPCID":"vpc-3gasnqceysuxdia5k****",
   "ImageSize":0,
   "IPv6":"",
   "Config":{
    "Memory":0,
    "CPUNumber":0
```

`},`

```json
   "BMCPassword":"",
   "DpuInfo":{
    "ErrorDescription":"",
    "Status":"power_on",
"LoginName":"root"
```

```json
    LoginName:root,
    "MachineSN":"2106196KUPXDP500****",
    "RunningState":"running",
    "CGWPorts":"THGigabitEthe****0/20:1,THGigabitEthernet0/20:1",
    "Zone":"",
    "Hostname":"c25d0****.cloud.d03.am****",
    "MachineType":"PG58P2M6S2****.32",
    "BMCPassword":"****",
    "Specification":"",
    "BMCPort":"",
    "InstanceName":"dpu-i-0919****ad914****",
    "BMCIP":"10.38.***.****",
    "LastHeartbeatTime":"2026-07-15T17:28:46+08:00",
    "ID":1,
    "SN":"MT2430XZ****",
    "BMCUser":"****",
    "ASWID":"****",
    "Subnet":"",
    "RawIP":"10.38.***.***",
    "LoginPwd":""
```

`},`

```json
   "SSHRsaId":"",
   "MappingStatus":"OperatedFailed",
   "Rack":"D03",
   "ApplicationGroup":"instance",
   "GpuNum":0,
   "NetworkCardNum":0,
   "SubnetIP":"10.38.***.***",
   "VPCSubnet":"vsw-3ga970i9dqzq7bybm****",
   "SN":"****",
   "BMCUser":"****",
   "Deleted":false,
   "Room":"C2-5",
   "ResourceGroup":"3",
   "SSHPwd":"",
   "ImageUniqueKey":"",
   "UserName":"",
   "OS":"",
   "UnitNum":0,
   "Zone":"cn-wulan-****-amte****-a",
   "CreateTime":"2026-06-24T17:19:05+08:00",
   "MachineType":"PG58P2M6S****.32",
   "NetworkMode":"vpc",
   "CPUArch":"",
   "BMCPort":"",
   "WWN":"",
   "Extra":"",
   "DefaultImage":"alinux_3_x86_64_aiext_20260623_bf3.qcow2",
   "UserId":"127756957048****",
   "UpdateTime":"2026-07-08T20:26:43+08:00",
   "LastHeartbeatTime":"2026-07-09T13:54:42+08:00",
   "ASWID":"****",
   "Tag":""
```

`}` `},` `},`

```json
 "errorTitle":"\"\"",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"\"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <DeployType>bfi_base</DeployType>
  <RunningState>offline</RunningState>
<CGWPorts>TwoHundredGigE1/0/65:1,TwoHundredGigE1/0/65:2,TwoHundredGigE1/0/66:1,TwoHundred gE1/0/66:2</CGWPorts>
  <IDC>amtest****</IDC>
  <SANZone  />
  <Image>alinux_3_x86_64_aiext_20260623_bf3.qcow2</Image>
  <InnerBandwidth  />
  <Gpu  />
  <ImageType  />
  <InstanceAlias>i-7c4ba42a32f64****</InstanceAlias>
  <AliYunAssistID>mi-rg6owzr81e****</AliYunAssistID>
  <ID>108</ID>
  <Disk>0</Disk>
  <RawIP>192.168.***.***</RawIP>
  <HostName>SN-2106196KUPXDP500****</HostName>
  <Disable>false</Disable>
  <ErrorDescription>[a-87c59321-7ac5-11f1-9014-02420a2608cd]reonlineNcEni timeout, eniL
ist not ready</ErrorDescription>
  <Status>power_on</Status>
  <DeviceModel>BFIBaseStack</DeviceModel>
  <Protected>true</Protected>
  <IP>192.168.***.***</IP>
  <DefaultHostName>SN-2106196KUPXDP500****</DefaultHostName>
  <PrimaryEniId>eni-9lpy8hgva2pl0g****</PrimaryEniId>
  <WarrantyPeriod>2027-01-01T00:00:00+08:00</WarrantyPeriod>
  <InstanceName>i-d8t4ltuheob3s2j0****</InstanceName>
  <SecondaryEniId>eni-3ga00weu4ouu93bc****</SecondaryEniId>
  <SSHUser  />
  <State>error</State>
  <BMCIP>10.38.***.****</BMCIP>
  <Region>cn-wulan-****-d01</Region>
  <NetworkCardType  />
  <AgentID>48</AgentID>
  <Subnet>EHSW-1-****-A-****</Subnet>
  <RackUnit>21</RackUnit>
  <Organization>4</Organization>
  <Description  />
  <VPCID>vpc-3gasnqceysuxdia5k****</VPCID>
<ImageSie>0</ImageSie>
```

```xml
  <ImageSize>0</ImageSize>
  <IPv6  />
  <Config>
   <Memory>0</Memory>
   <CPUNumber>0</CPUNumber>
  </Config>
  <BMCPassword  />
  <DpuInfo>
   <ErrorDescription  />
   <Status>power_on</Status>
   <LoginName>root</LoginName>
   <MachineSN>2106196KUPXDP500****</MachineSN>
   <RunningState>running</RunningState>
   <CGWPorts>THGigabitEthe****0/20:1,THGigabitEthernet0/20:1</CGWPorts>
   <Zone  />
   <Hostname>c25d0****.cloud.d03.am****</Hostname>
   <MachineType>PG58P2M6S2****.32</MachineType>
   <BMCPassword>****</BMCPassword>
   <Specification  />
   <BMCPort  />
   <InstanceName>dpu-i-0919****ad914****</InstanceName>
   <BMCIP>10.38.***.****</BMCIP>
   <LastHeartbeatTime>2026-07-15T17:28:46+08:00</LastHeartbeatTime>
   <ID>1</ID>
   <SN>MT2430XZ****</SN>
   <BMCUser>****</BMCUser>
   <ASWID>****</ASWID>
   <Subnet  />
   <RawIP>10.38.***.***</RawIP>
   <LoginPwd  />
  </DpuInfo>
  <SSHRsaId  />
  <MappingStatus>OperatedFailed</MappingStatus>
  <Rack>D03</Rack>
  <ApplicationGroup>instance</ApplicationGroup>
  <GpuNum>0</GpuNum>
  <NetworkCardNum>0</NetworkCardNum>
  <SubnetIP>10.38.***.***</SubnetIP>
  <VPCSubnet>vsw-3ga970i9dqzq7bybm****</VPCSubnet>
  <SN>****</SN>
  <BMCUser>****</BMCUser>
  <Deleted>false</Deleted>
  <Room>C2-5</Room>
  <ResourceGroup>3</ResourceGroup>
  <SSHPwd  />
  <ImageUniqueKey  />
  <UserName  />
  <OS  />
  <UnitNum>0</UnitNum>
  <Zone>cn-wulan-****-amte****-a</Zone>
  <CreateTime>2026-06-24T17:19:05+08:00</CreateTime>
  <MachineType>PG58P2M6S****.32</MachineType>
  <NetworkMode>vpc</NetworkMode>
  <CPUArch  />
<BMCPort
```

`/>`

```xml
  <BMCPort  />
  <WWN  />
  <Extra  />
  <DefaultImage>alinux_3_x86_64_aiext_20260623_bf3.qcow2</DefaultImage>
  <UserId>127756957048****</UserId>
  <UpdateTime>2026-07-08T20:26:43+08:00</UpdateTime>
  <LastHeartbeatTime>2026-07-09T13:54:42+08:00</LastHeartbeatTime>
  <ASWID>****</ASWID>
  <Tag  />
 </data>
</data> <errorTitle>""</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;"</errorMessage> <errorCode /> <status>0</status>
```

#### 5.1.6 GetVswitchSwitchMethod

Query the types of physical switches connected to bare metal dedicated switches in a Virtual Private Cloud (VPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the VPC. |
| ZoneId | Strin g | Quer y | No | cn-wulan-env***-****-a | The ID of the zone. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

| data | Map | { "vsw- 1clbm6xp5ml6jlpt9 ****": "CHSW", "vsw- 1cl4ewc5dmbdujs0 w****": "HSW" } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "vsw-1clbm6xp5ml6jlpt9****":"CHSW",
  "vsw-1cl4ewc5dmbdujs0w****":"HSW"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <vsw-1clbm6xp5ml6jlpt9****>CHSW</vsw-1clbm6xp5ml6jlpt9****>
 <vsw-1cl4ewc5dmbdujs0w****>HSW</vsw-1cl4ewc5dmbdujs0w****>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.1.7 ClusterDryRun

Simulate a cluster operation without actually performing it to validate configurations, check for potential errors, or evaluate the impact of changes. Cluster creation precheck

```
http://[Endpoint]/?Action=ClusterDryRun &ClusterType=ack &ClusterArchType=standard &MachineTypeList=[
```

`{`

```json
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "NodePoolName": "bmcp-node-pool",
    "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA**** &Common request parameters
```

Cluster scale-out precheck

```
http://[Endpoint]/?Action=ClusterDryRun &ClusterId=ack-8EEjd6**** &ClusterType=ack &ClusterArchType=standard &MachineTypeList=[
```

`{`

```json
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "NodePoolName": "bmcp-node-pool",
    "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA**** &Common request parameters
```

Node restoration to cluster precheck

```
http://[Endpoint]/?Action=ClusterDryRun &ClusterId=ack-8EEjd6**** &ClusterType=ack &ClusterArchType=standard &InstanceNameList=["i-d9jfbieheob5ghiu****"] &RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA**** &Common request parameters
```

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |

| ClusterTyp e | Strin g | Quer y | No | ack | The cluster type. Valid values: bmcp: Bare metal computing cluster ack: Container Service for Kubernetes (ACK) computing cluster bfi: Converged computing cluster |
|---|---|---|---|---|---|
| ClusterArc hType | Strin g | Quer y | No | standard | The cluster instance type. Valid values: standard: Intelligent computing high- bandwidth network base: Basic intelligent computing aspeed: Intelligent computing training and inference bfi: Converged high- bandwidth network bfi base: Converged _ basic |
| MachineTy peList | Json | Quer y | No | [ { "MachineType": "test", "Arch": "x86", "CpuCount": 2, "MemCount": 4, "FlopsCount": 4.8, "VideoMemCount": 5, "NodeCount": 10, "NodePoolName": "bmcp- node-pool", "VswitchId": "vsw- 3gagdup8scary04iq****" } ] | The list of bare metal instance types. |
| RequestTo ken | Strin g | Quer y | No | 869F3EDC-C0CA-45E4- AA11-C4638CDA**** | The request token. |

| InstanceN ameList | Json | Quer y | No | ["i-d9jfbieheob5ghiu****"] | The list of instance names. This parameter can be configured only when ClusterId is specified. It indicates a node restoration to cluster precheck. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |

| data | Map | { "RequestToken": "869F3EDC-C0CA- 45E4-AA11- C4638CDA****", "NeedWarning": true, "ClusterDriverVersi on": { "gpu driver": [ _ "1.5.3-5239a4" ], "gpu sdk": [ "12.3" _ ], "gpu tag": [ _ "1ded:6001" ] }, "InstanceDriverVer sion": [ { "components": [ { "lastReportedAt": 1782274630000, "componentKey": "gpu driver", _ "actualVersion": "2.2.0" }, { "lastReportedAt": 1782274630000, "componentKey": "gpu sdk", _ "actualVersion": "12.2" }, { "lastReportedAt": 1782274630000, "componentKey": "gpu tag", _ "actualVersion": "nvidia" } ], "componentCount" : 0, "machineSN": "test", "hasReportedData" : false } ] } | The response data. |
|---|---|---|---|
| status | Integer | 0 | The status of the request. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ClusterDryRun &ClusterType=ack &ClusterArchType=standard &MachineTypeList=[
```

`{`

```json
    "MachineType": "test",
    "Arch": "x86",
    "CpuCount": 2,
    "MemCount": 4,
    "FlopsCount": 4.8,
    "VideoMemCount": 5,
    "NodeCount": 10,
    "NodePoolName": "bmcp-node-pool",
    "VswitchId": "vsw-3gagdup8scary04iq****"
```

`}` `]`

```
&RequestToken=869F3EDC-C0CA-45E4-AA11-C4638CDA**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "RequestToken":"869F3EDC-C0CA-45E4-AA11-C4638CDA****",
  "NeedWarning":true,
  "ClusterDriverVersion":{
   "gpu_driver":[
    "1.5.3-5239a4"
```

`],`

```json
   "gpu_sdk":[
    "12.3"
```

`],`

```json
   "gpu_tag":[
    "1ded:6001"
```

`]` `},`

```json
  "InstanceDriverVersion":[
```

`{`

```json
    "components":[
```

`{`

```json
      "lastReportedAt":1782274630000,
      "componentKey":"gpu_driver",
      "actualVersion":"2.2.0"
```

`},` `{`

```json
      "lastReportedAt":1782274630000,
      "componentKey":"gpu_sdk",
      "actualVersion":"12.2"
```

`},` `{`

```json
      "lastReportedAt":1782274630000,
      "componentKey":"gpu_tag",
      "actualVersion":"nvidia"
```

`}` `],`

```json
    "componentCount":0,
    "machineSN":"test",
    "hasReportedData":false
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <RequestToken>869F3EDC-C0CA-45E4-AA11-C4638CDA****</RequestToken>
 <NeedWarning>true</NeedWarning>
 <ClusterDriverVersion>
  <gpu_driver>1.5.3-5239a4</gpu_driver>
  <gpu_sdk>12.3</gpu_sdk>
  <gpu_tag>1ded:6001</gpu_tag>
 </ClusterDriverVersion>
 <InstanceDriverVersion>
  <components>
   <lastReportedAt>1782274630000</lastReportedAt>
   <componentKey>gpu_driver</componentKey>
   <actualVersion>2.2.0</actualVersion>
  </components>
  <components>
   <lastReportedAt>1782274630000</lastReportedAt>
   <componentKey>gpu_sdk</componentKey>
   <actualVersion>12.2</actualVersion>
  </components>
  <components>
   <lastReportedAt>1782274630000</lastReportedAt>
   <componentKey>gpu_tag</componentKey>
   <actualVersion>nvidia</actualVersion>
  </components>
  <componentCount>0</componentCount>
  <machineSN>test</machineSN>
  <hasReportedData>false</hasReportedData>
 </InstanceDriverVersion>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.1.8 TagResources

Tag a cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| RegionId | Strin g | Quer y | Yes | cn-wulan-****-d01 | The ID of the region to which the resource belongs. |
|---|---|---|---|---|---|
| ResourceT ype | Strin g | Quer y | Yes | CLUSTER | The resource type. Currently, only CLUSTER is supported. |
| Tags | Json | Quer y | No | [ {"key":"testacktagk- 1","value":"testackv-1"}, {"key":"testacktagk- 2","value":"testackv-2"} ] | The tag key-value pairs of the resource. Array length range: [1,20] It cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| ResourceId s | Json | Quer y | No | ["ack-ezVaql****","ack- 99VDuz****"] | The list of resource IDs. Note that the IDs are Container Service for Kubernetes (ACK) cluster IDs. |

|   | aliyun |
|---|---|
| acs: |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "RequestId": "2D69A58F-345C- 4FDE-88E4- BF51894*****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```json
http://[Endpoint]/?Action=TagResources &RegionId=cn-wulan-****-d01 &ResourceType=CLUSTER &Tags=[
  {"key":"testacktagk-1","value":"testackv-1"},
  {"key":"testacktagk-2","value":"testackv-2"}
```

`]`

```
&ResourceIds=["ack-ezVaql****","ack-99VDuz****"] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "RequestId":"2D69A58F-345C-4FDE-88E4-BF51894*****"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <RequestId>2D69A58F-345C-4FDE-88E4-BF51894*****</RequestId>
</data> <errorTitle>“”</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.1.9 RetryFailedInstance

Retry instances that failed to be scaled out or scaled in for bare metal and Container Service for Kubernetes (ACK) clusters. After the retry, a new scale-out or scale-in task is initiated.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Quer y | No | 1284c8b8-9571-11ee- a39e-16f363c7**** | The ID of the task. |
| InstanceN ameList | Json | Quer y | No | ["i-d9jfbieheob5ghiu****"] | The list of IDs of the instances to retry. |
| ActivationI d | Strin g | Quer y | No | 4ECEEE12-56F1-4FBC- 9AB1-890F1234**** | The ID of the Cloud Assistant activation code. This parameter is required when the instances to retry are being scaled out to the cluster. |
| Activation Code | Strin g | Quer y | No | a- hz0ch3SwhOlE1234+Xo3 2lAZC**** | The code of the Cloud Assistant activation code. This parameter is required when the instances to retry are being scaled out to the cluster. |
| OsUpdate | Bool ean | Quer y | No | false | Whether to clear data disks. This parameter is required when the instances are being removed from the cluster. Valid values: true: Clear data disks. false: Do not clear data disks. |

| RetentionP eriod | Integ er | Quer y | No | 168 | The retention period of instances in the recycle bin. Unit: hours. Valid values: 1 to 720 This parameter is required when the instances to retry are being removed from the cluster. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TaskId": "0d1fa517-8576- 11f1-9d26- 02420a260d50" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=RetryFailedInstance &TaskId=1284c8b8-9571-11ee-a39e-16f363c7**** &InstanceNameList=["i-d9jfbieheob5ghiu****"] &ActivationId=4ECEEE12-56F1-4FBC-9AB1-890F1234**** &ActivationCode=a-hz0ch3SwhOlE1234+Xo32lAZC**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TaskId":"0d1fa517-8576-11f1-9d26-02420a260d50"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TaskId>0d1fa517-8576-11f1-9d26-02420a260d50</TaskId>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

### 5.2 Storage management

#### 5.2.1 CreateCpfsClientCluster

Enable high-performance storage for clusters of high-performance network instances and computing-optimized training & inference instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. The system only supports clusters with high- performance network instances and computing-optimized training & inference instances. Different storage types have different limits on the number of Bare Metal Computing Platform (BMCP) nodes: Cloud Parallel File System (CPFS): The minimum number of nodes is 3. Apple File System (APFS): The minimum number of nodes is 1. |
|---|---|---|---|---|---|
| CpfsCluste rType | Strin g | Quer y | No | CPFS | The type of high- performance storage client. Valid values: CPFS APFS |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"data": "The asynchronous workflow task for enabling high- performance storage has been initiated"} | The response data. |
| status | Integer | 200 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateCpfsClientCluster &ClusterId=ack-8EEjd6**** &CpfsClusterType=CPFS &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The asynchronous workflow task for enabling high-performance storage has been
initiated"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The asynchronous workflow task for enabling high-performance storage has been in
itiated</data> </data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.2.2 DescribeCpfsClientClusterType

Query the available high-performance storage client types in the environment.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ClusterType": [ "CPFS", "APFS" ] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the response. Success: true Failure: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "ClusterType":[
   "CPFS",
   "APFS"
```

`]` `},`

```json
 "errorTitle":"InternalError",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <ClusterType>CPFS</ClusterType>
 <ClusterType>APFS</ClusterType>
</data> <errorTitle>InternalError</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.2.3 MountFilesystem

Mount high-performance storage for a cluster.

**Operation description**

You can only mount high-performance storage to clusters with **high-performance**
**network instances** and **computing-optimized training & inference instances**.
Before mounting, call the CreateCpfsClientCluster operation to enable high-performance storage for the cluster. Different storage types have different requirements for the number of Bare Metal Computing Platform (BMCP) nodes in a cluster: Cloud Parallel File System (CPFS): The minimum number of nodes is 3. Apple File System (APFS): The minimum number of nodes is 1.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | bmcp-noBklp**** | The ID of the cluster. |
| FileSystem Id | Strin g | Quer y | No | efs-0137**** | The ID of the file system. CPFS or APFS file systems are supported. CPFS: bmcpfs-01ae**** APFS: efs-0137**** |
| MountPoin t | Json | Quer y | No | /dev/xvda | The mount point. |

| MountDire ctory | Json | Quer y | No | /ai model training _ _ |   | The local mount path of the file system. Mount path requirements: After you set the mount path, the system automatically creates a directory. Manual creation is not needed.. Recommended format: /[business name] [purpose] . _ For example, /ai model training. _ _ To ensure stability, avoid using the following paths: System critical directories, such as / , /bin , /etc , and /tmp . Paths that start with /efs (including /efs/custom-path). System reserved paths. For example, when the ID of the file system is efs- 123456, the default mount path is /efs/123456. If the directory already contains files, the original files will be temporarily hidden after mounting and will be restored after unmounting. |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | /[business |   |
|   |   |   |   |   |   | name] [purpose] _ |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

| data | Map | { "data" :"Launch success" } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the response. Success: true Failure: false |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=MountFilesystem &ClusterId=bmcp-noBklp**** &FileSystemId=efs-0137**** &MountPoint=/dev/xvda &MountDirectory=/ai_model_training &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"Launch success"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>Launch success</data>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.2.4 UnmountFilesystem

Unmount a file system from a cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data" :"unmount success" } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| success | Boolean | true | The status of the response. Success: true Failure: false |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UnmountFilesystem &ClusterId=ack-8EEjd6**** &common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"unmount success"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>unmount success</data>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.2.5 DeleteCpfsClientCluster

Unmount high-performance storage from clusters with high-performance network instances and computing-optimized training & inference instances.

**Operation description**

When you unmount a file system, all processes that are using the file system in the current cluster will be terminated, which may cause data loss or service interruption. Proceed with caution.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"data": "The asynchronous workflow task for disabling high- performance storage has been initiated"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":"The asynchronous workflow task for disabling high-performance storage has bee
n initiated"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>The asynchronous workflow task for disabling high-performance storage has been i
nitiated</data> </data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

### 5.3 EVPC

#### 5.3.1 CreateEvpc

Create an Enterprise Virtual Private Cloud (EVPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Departme nt | Strin g | Quer y | No | test | The ID of the organization, which identifies the organization or department to which the EVPC belongs. |
|---|---|---|---|---|---|
| ResourceG roup | Strin g | Quer y | No | ResourceSet(test) | The ID of the resource set, used to classify the EVPC to a specified resource group. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region, which specifies the geographical location where the EVPC is created. |
| EvpcName | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The name of the EVPC, used to identify the created EVPC instance. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the EVPC, used to provide more information about the EVPC. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values: true: Enable false: Disable Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "EvpcId": "evpc- htchvitxlfjyso****" } | The response data. |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateEvpc &Department=test &ResourceGroup=ResourceSet(test) &RegionId=cn-wulan-env***-d01 &EvpcName=evpc-htchvitxlfjyso**** &EnableIpv6=true &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "EvpcId":"evpc-htchvitxlfjyso****"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.3.2 ListEvpc

Query the list of Enterprise Virtual Private Clouds (EVPCs).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number, used for pagination query. Default value: 1. |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The unique identifier of the EVPC. |
| EvpcName | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The name of the EVPC. |
| Cidr | Strin g | Quer y | No | 20.41.*.*/16 | The IPv4 CIDR block information of the EVPC. |
| Departme nt | Strin g | Quer y | No | test | The ID of the organization to which the EVPC belongs. |

| ResourceG roup | Strin g | Quer y | No | ResourceSet(test) | The ID of the resource set to which the EVPC belongs. |
|---|---|---|---|---|---|
| Status | Strin g | Quer y | No | Available | The current status of the EVPC. Valid values: Available: Normal Not Available: Unavailable Deleting: Deleting DeletingFailed: Deletion failed |
| TenantId | Strin g | Quer y | No | 28065796931554**** | The ID of the tenant associated with the EVPC. |
| Descriptio n | Bool ean | Quer y | No | testDescription | The detailed description of the EVPC. |
| EnableIpv6 | Bool ean | Quer y | No | true | Specifies whether to enable IPv6. Valid values: true: Enabled false: Disabled Default value: false. |
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster associated with the EVPC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

| data | Map | { "PageNumber": 1, "PageSize": 10, "TotalCount": 1, "EvpcList": [ { "EvpcId": "evpc- htchvitxlfjyso****", "ClusterId": "ack- 8EEjd6****", "EvpcName": "evpc- htchvitxlfjyso****", "Description":"test" , "Cidr": "20.41.*.*/16", "TenantId": "28065796931554 ****", "Status": "Available", "RegionId": "cn- wulan-env***-d01", "Department":"test ", "ResourceGroup": "ResourceSet(test) ", "CreateTime": "2026-06- 01T12:05:00Z", "UpdateTime": "2026-07- 01T12:05:00Z", "EnableIpv6": true, "Ipv6Cidr": "1007:1100:****::/ 64" } ] } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListEvpc &Department=test &ResourceGroup=ResourceSet(test) &RegionId=cn-wulan-env***-d01 &Status=Available &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "PageSize":10,
  "EvpcList":[
```

`{`

```json
    "Status":"Available",
    "Description":"test",
    "ClusterId":"ack-8EEjd6****",
    "CreateTime":"2026-06-01T12:05:00Z",
    "EvpcName":"evpc-htchvitxlfjyso****",
    "EvpcId":"evpc-htchvitxlfjyso****",
    "EnableIpv6":true,
    "TenantId":"28065796931554****",
    "Department":"test",
    "Cidr":"20.41.*.*/16",
    "UpdateTime":"2026-07-01T12:05:00Z",
    "RegionId":"cn-wulan-env***-d01",
    "ResourceGroup":"ResourceSet(test)",
    "Ipv6Cidr":"1007:1100:****::/64"
```

`}` `],`

```json
  "PageNumber":1
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>1</TotalCount>
 <PageSize>10</PageSize>
 <EvpcList>
  <Status>xxxxx</Status>
  <Description>xxxx</Description>
  <ClusterId>xxxxxx</ClusterId>
  <CreateTime>xxxx</CreateTime>
  <EvpcName>xxxx</EvpcName>
  <EvpcId>xxxxxxxxxx</EvpcId>
  <EnableIpv6>true</EnableIpv6>
  <TenantId>xxxx</TenantId>
  <Department>xxxx</Department>
  <Cidr>xxxx</Cidr>
  <UpdateTime>xxxx</UpdateTime>
  <RegionId>xxxx</RegionId>
  <ResourceGroup>xxxxx</ResourceGroup>
  <Ipv6Cidr>1007:1100:1100::/64</Ipv6Cidr>
 </EvpcList>
 <PageNumber>1</PageNumber>
</data> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.3.3 ListEvpcConnections

Query the Enterprise Virtual Private Cloud (EVPC) connections of an EVPC.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The unique identifier of the EVPC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "Connections": [ { // EvpcConnectionId "EvpcConnectionId ": "125489", // LocalEvpcId "LocalEvpcId": "evpc- htchvitxlfjyso****", // LocalEvpcName "LocalEvpcName": "test1", // PeerEvpcId "PeerEvpcId": "evpc- b9wfut1m1ry6sh** **", // PeerEvpcName "PeerEvpcName": "test2", // status "Status": "Success" } ] } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListEvpcConnections &EvpcId=evpc-htchvitxlfjyso**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "Connections":[
```

`{`

```json
    "PeerEvpcId":"evpc-b9wfut1m1ry6sh****",
    "Status":"Success",
    "LocalEvpcId":"evpc-htchvitxlfjyso****",
    "PeerEvpcName":"test2",
    "LocalEvpcName":"test1",
    "EvpcConnectionId":"125489"
```

`}` `]` `},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <Connections>
  <PeerEvpcId>evpc-b9wfut1m1ry6sh****</PeerEvpcId>
  <Status>Success</Status>
  <LocalEvpcId>evpc-htchvitxlfjyso****</LocalEvpcId>
  <PeerEvpcName>test2</PeerEvpcName>
  <LocalEvpcName>test1</LocalEvpcName>
  <EvpcConnectionId>125489</EvpcConnectionId>
 </Connections>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.3.4 ModifyEvpc

Modify the name or description of an Enterprise Virtual Private Cloud (EVPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| EvpcName | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The new name of the EVPC, used to update the display name of the EVPC. |
| Descriptio n | Strin g | Quer y | No | testDescription | The new description of the EVPC, used to provide more details about the EVPC. |
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The unique identifier of the EVPC. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"EvpcId": "evpc- htchvitxlfjyso****"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ModifyEvpc &EvpcId=evpc-htchvitxlfjyso**** &EvpcName=evpc-htchvitxlfjyso**** &Description=testDescription &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "EvpcId":"evpc-htchvitxlfjyso****"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <EvpcId>evpc-htchvitxlfjyso****</EvpcId>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.3.5 DeleteEvpc

Delete an Enterprise Virtual Private Cloud (EVPC).

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| EvpcId | Strin g | Quer y | No | evpc-htchvitxlfjyso**** | The ID of the EVPC, which is the unique identifier of the EVPC. |
| Force | Bool ean | Quer y | No | false | Specifies whether to forcibly delete the EVPC. Valid values: true: Yes false: No Default value: false. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | {"describe":"The deletion task has been submitted"} | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListEvpcConnections &EvpcId=evpc-htchvitxlfjyso**** &Force=false &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "describe":"The deletion task has been submitted"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data /> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

### 5.4 Security group

#### 5.4.1 CreateSecurityGroup

Create a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Departme nt | Strin g | Quer y | No | test | The ID of the organization. |
|---|---|---|---|---|---|
| ResourceG roup | Strin g | Quer y | No | ResourceTest(test) | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region. |
| Name | Strin g | Quer y | No | test | The name of the security group. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, underscores ( ), _ hyphens (-), and colons (:). It cannot start with http:// or https:// . |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC) instance. |
| Type | Strin g | Quer y | No | null | The type of the security group. This parameter is not available. |
| DeployTyp e | Strin g | Quer y | No | bmcp | The deployment type. Only bmcp is supported. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description. The description must be 2 to 256 characters in length, and must start with a letter. It can contain digits, underscores ( ), hyphens _ (-), full-width periods (。), full-width commas (，), half-width commas (,), full-width colons (：), colons (:), and slashes (/). It cannot start with http:// or https:// . |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg- 7s186nsxfz01wa5x ****", "ID": "3", "name": "test" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateSecurityGroup &Department=test &ResourceGroup=ResourceTest(test) &RegionId=cn-wulan-env***-d01 &Name=test &VpcId=vpc-bp1b1xjllp3ve5yze**** &DeployType=bmcp &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "name":"test",
   "sgId":"sg-7s186nsxfz01wa5x****",
   "ID":"3"
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <name>test</name>
  <sgId>sg-7s186nsxfz01wa5x****</sgId>
  <ID>3</ID>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.2 ListSecurityGroup

Query the list of security groups.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | test | The ID of the organization. |

| ResourceG roup | Strin g | Quer y | No | ResourceSet(test) | The ID of the resource set. |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region. |
| Name | Strin g | Quer y | No | test | The name of the security group. |
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |
| VpcId | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the Virtual Private Cloud (VPC). |
| Type | Strin g | Quer y | No | null | The type of the security group. This parameter is not available. |
| DeployTyp e | Strin g | Quer y | No | bmcp | The deployment type. Only bmcp is supported. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

| data | Map | { "data": [ { "ID": 6, "sgId": "sg- bp197668l6iupljy** **", "name": "test", "region": "cn- wulan-env***-d01", "organization": "4", "resourceGroup": "3", "vpcId": "vpc- bp1b1xjllp3ve5yze ****", "type": "", "deployType": "bmcp", "description": "testDescription", "AliUid": "127756957048*** *", "shared": 0, "version": 0, "deleted": false, "createTime": "2026-07- 03T14:50:26+08:0 0", "updateTime": "2026-07- 03T14:50:26+08:0 0" } ], "total": 1, "pageNumber": 10, "pageSize": 1 } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListSecurityGroup &Department=test &ResourceGroup=ResourceTest(test) &RegionId=cn-wulan-env***-d01 &Name=test &VpcId=vpc-bp1b1xjllp3ve5yze**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":10,
  "data":[
```

`{`

```json
    "resourceGroup":"3",
    "shared":0,
    "description":"testDescription",
    "updateTime":"2026-07-03T14:50:26+08:00",
    "type":"",
    "version":0,
    "deployType":"bmcp",
    "deleted":false,
    "createTime":"2026-07-03T14:50:26+08:00",
    "organization":"4",
    "vpcId":"vpc-bp1b1xjllp3ve5yze****",
    "name":"test",
    "sgId":"sg-bp197668l6iupljy****",
    "ID":6,
    "region":"cn-wulan-env***-d01",
    "AliUid":"127756957048****"
```

`}` `],`

```json
  "pageSize":1
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <total>1</total>
 <pageNumber>10</pageNumber>
 <data>
  <resourceGroup>3</resourceGroup>
  <shared>0</shared>
  <description>testDescription</description>
  <updateTime>2026-07-03T14:50:26+08:00</updateTime>
  <type />
  <version>0</version>
  <deployType>bmcp</deployType>
  <deleted>false</deleted>
  <createTime>2026-07-03T14:50:26+08:00</createTime>
  <organization>4</organization>
  <vpcId>vpc-bp1b1xjllp3ve5yze****</vpcId>
  <name>test</name>
  <sgId>sg-bp197668l6iupljy****</sgId>
  <ID>6</ID>
  <region>cn-wulan-env***-d01</region>
  <AliUid>127756957048****</AliUid>
 </data>
 <pageSize>1</pageSize>
</data> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.3 ModifySecurityGroup

Modify the name or description of a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |

| Name | Strin g | Quer y | No | test | The name of the security group. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, underscores ( ), _ hyphens (-), and colons (:). It cannot start with http:// or https:// . |
|---|---|---|---|---|---|
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the security group. The description must be 2 to 256 characters in length, and must start with a letter. It can contain digits, underscores ( ), hyphens _ (-), full-width periods (。), full-width commas (，), half-width commas (,), full-width colons (：), colons (:), and slashes (/). It cannot start with http:// or https:// . |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg- 7s186nsxfz01wa5x ****", "ID": "3", "name": "test" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |

| success | Boolean | true | The status of the request. |
|---|---|---|---|
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ModifySecurityGroup &SgId=sg-bp197668l6iupljy**** &Name=test &Description=testDescription &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "name":"test",
   "sgId":"sg-7s186nsxfz01wa5x****",
   "ID":"3"
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <name>test</name>
  <sgId>sg-7s186nsxfz01wa5x****</sgId>
  <ID>3</ID>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.4 DeleteSecurityGroup

Delete a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "" } } | The response data. |
| status | Integer | 200 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteSecurityGroup &SgId=sg-bp197668l6iupljy**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "sgId":""
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <sgId />
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.5 AddSecurityGroupRule

Add a security group rule.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |
| Direction | Strin g | Quer y | No | ingress | The rule direction. Valid values: ingress: Inbound egress: Outbound |
| AccessPoli cy | Strin g | Quer y | No | accept | The access policy. Valid values: accept: Allow access. drop: Deny access. No rejection message is returned. The initiator may experience request timeouts or connection failures. Default value: accept. |
| IpProtocol | Strin g | Quer y | No | tcp | The transport layer protocol (case- insensitive). Valid values: ICMP GRE TCP UDP ALL: All protocols are supported. |

| PortRange | Strin g | Quer y | No | 80/80 | The port range. Value range: TCP/UDP: Valid values are 1 to 65535. Use a forward slash (/) to separate the start port and end port. For example, 1/200. ICMP: -1/-1. GRE: -1/-1. When IpProtocol is set to ALL: -1/-1. |
|---|---|---|---|---|---|
| Priority | Integ er | Quer y | No | 1 | The priority of the security group rule. A smaller number indicates a higher priority. Value range: 1 to 100. Default value: 1. |
| IpVersion | Strin g | Quer y | No | ipv4 | The IP version. Only ipv4 is supported. |
| CidrIp | Strin g | Quer y | No | 192.168.0.1 | The source IPv4 CIDR block. |
| RelatedGr oupId | Strin g | Quer y | No | sg- 7s186nsxfz01wa5x**** | The ID of the authorized security group. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the security group rule for easier management. The description must be 1 to 512 characters in length, and cannot start with http:// and https:// . |

|   | http:// |
|---|---|
| https:// |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |

| errorTitle | String | Successful | The error title. |
|---|---|---|---|
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg- bp197668l6iupljy** **", "sgrId": "sgr- tllvexl60s9khyld3p mr" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=AddSecurityGroupRule &SgId=sg-bp197668l6iupljy**** &AccessPolicy=accept &Direction=ingress &IpProtocol=tcp &PortRange=80/80 &CidrIp=192.168.0.1 &IpVersion=ipv4 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "sgId":"sg-bp197668l6iupljy****",
   "sgrId":"sgr-tllvexl60s9khyld3pmr"
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <sgId>sg-bp197668l6iupljy****</sgId>
  <sgrId>sgr-tllvexl60s9khyld3pmr</sgrId>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.6 ListSecurityGroupRule

Query the list of security group rules.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |

| Direction | Strin g | Quer y | No | ingress | The rule direction. |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 10 | The page number. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "total": 1, "pageNumber": 1, "data": [ { "portRange": "80/80", "SgId": "sg- 5gh79x2ijuk9yzjo** **", "description": "test", "updateTime": "2026-07- 03T16:55:26+08:0 0", "ipProtocol": "tcp", "priority": 1, "relatedGroupId": "", "ipVersion": "ipv4", "deleted": false, "createTime": "2026-07- 03T16:55:26+08:0 0", "ID": 3, "accessPolicy": "ACCEPT", "sgrId": "sgr- tllvexl60s9khyld*** *", "cidrIp": "192.168.0.1", "direction": "ingress" } ], "pageSize": 10 } | The response data. |
| status | Integer | 200 | The status of the response. |

| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListSecurityGroupRule &SgId=sg-bp197668l6iupljy**** &PageNumber=10 &PageSize=1 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":1,
  "data":[
```

`{`

```json
    "portRange":"80/80",
    "SgId":"sg-5gh79x2ijuk9yzjo****",
    "description":"test",
    "updateTime":"2026-07-03T16:55:26+08:00",
    "ipProtocol":"tcp",
    "priority":1,
    "relatedGroupId":"",
    "ipVersion":"ipv4",
    "deleted":false,
    "createTime":"2026-07-03T16:55:26+08:00",
    "ID":3,
    "accessPolicy":"ACCEPT",
    "sgrId":"sgr-tllvexl60s9khyld****",
    "cidrIp":"192.168.0.1",
    "direction":"ingress"
```

`}` `],`

```json
  "pageSize":10
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <total>1</total>
 <pageNumber>1</pageNumber>
 <data>
  <portRange>80/80</portRange>
  <SgId>sg-5gh79x2ijuk9yzjo****</SgId>
  <description>test</description>
  <updateTime>2026-07-03T16:55:26+08:00</updateTime>
  <ipProtocol>tcp</ipProtocol>
  <priority>1</priority>
  <relatedGroupId />
  <ipVersion>ipv4</ipVersion>
  <deleted>false</deleted>
  <createTime>2026-07-03T16:55:26+08:00</createTime>
  <ID>3</ID>
  <accessPolicy>ACCEPT</accessPolicy>
  <sgrId>sgr-tllvexl60s9khyld****</sgrId>
  <cidrIp>192.168.0.1</cidrIp>
  <direction>ingress</direction>
 </data>
 <pageSize>10</pageSize>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.7 ModifySecurityGroupRule

Modify a security group rule.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |
| SgrId | Strin g | Quer y | No | sgr-tllvexl60s9khyld**** | The ID of the rule. |

| Direction | Strin g | Quer y | No | ingress | The rule direction. Valid values: ingress: Inbound egress: Outbound |
|---|---|---|---|---|---|
| AccessPoli cy | Strin g | Quer y | No | accept | The access policy. Valid values: accept: Allow access. drop: Deny access. No rejection message is returned. The initiator may experience request timeouts or connection failures. Default value: accept. |
| IpProtocol | Strin g | Quer y | No | tcp | The transport layer protocol (case- insensitive). Valid values: ICMP GRE TCP UDP ALL: All protocols are supported. |
| PortRange | Strin g | Quer y | No | 80/80 | The port range. Value range: TCP/UDP: Valid values are 1 to 65535. Use a forward slash (/) to separate the start port and end port. For example, 1/200. ICMP protocol:-1/-1. GRE protocol:-1/-1. When IpProtocol is set to ALL: -1/-1. |
| Priority | Integ er | Quer y | No | 1 | The priority of the security group rule. A smaller number indicates a higher priority. Value range: 1 to 100. Default value: 1. |
| IpVersion | Strin g | Quer y | No | ipv4 | The IP version. Only ipv4 is supported. |

| CidrIp | Strin g | Quer y | No | 192.168.0.1 | The source IPv4 CIDR block. |
|---|---|---|---|---|---|
| RelatedGr oupId | Strin g | Quer y | No | sg- 7s186nsxfz01wa5x**** | The ID of the authorized security group. |
| Descriptio n | Strin g | Quer y | No | testDescription | The description of the security group rule for easier management. The description must be 1 to 512 characters in length, and cannot start with http:// and https:// . |

|   | http:// |
|---|---|
| https:// |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "sgId": "sg- bp197668l6iupljy** **", "sgrId": "sgr- tllvexl60s9khyld3p mr" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ModifySecurityGroupRule &SgId=sg-bp197668l6iupljy**** &AccessPolicy=accept &Direction=ingress &IpProtocol=tcp &PortRange=80/80 &CidrIp=192.168.0.1 &IpVersion=ipv4 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "sgId":"sg-bp197668l6iupljy****",
   "sgrId":"sgr-tllvexl60s9khyld3pmr"
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <sgId>sg-bp197668l6iupljy****</sgId>
  <sgrId>sgr-tllvexl60s9khyld3pmr</sgrId>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.8 DeleteSecurityGroupRule

Delete a security group rule.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. You can call the ListSecurityGroup operation to query the security group ID. |
| SgrId | Strin g | Quer y | No | sgr-tllvexl60s9khyld**** | The ID of the security group rule. You can call the ListSecurityGroupRule operation to query the rule ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "SgId": "", "SgrId": "" } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteSecurityGroupRule &SgId=sg-bp197668l6iupljy**** &SgrId=sgr-tllvexl60s9khyld**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "SgId":"",
   "SgrId":""
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <SgId />
  <SgrId />
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.9 AddSecurityGroupInstance

Add Bare Metal Computing Platform (BMCP) instances to a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |
| InstanceN ameList | Json | Quer y | No | ["test1","test2"] | The list of instance names. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "SgId": "sg- bp197668l6iupljy** **", "InstanceNameList ":["test1","test2"] } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=AddSecurityGroupInstance &SgId=sg-bp197668l6iupljy**** &InstanceNameList=["test1","test2"] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "SgId":"sg-bp197668l6iupljy****",
   "InstanceNameList":[
    "test1",
    "test2"
```

`]` `}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <SgId>sg-bp197668l6iupljy****</SgId>
  <InstanceNameList>test1</InstanceNameList>
  <InstanceNameList>test2</InstanceNameList>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.10 ListSecurityGroupInstance

Query the list of instances bound to a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| 92 |   |   |   | > D | ocument Version: 2026073 |
|---|---|---|---|---|---|

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |
| SN | Strin g | Quer y | No | 007269004887****** | The serial number (SN). |
| InstanceN ame | Strin g | Quer y | No | myinstance | The name of the instance. |
| PageNumb er | Integ er | Quer y | No | 10 | The page number. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |

| data | Map | { "data": [ { "ID": 0, "sn": "007269004887*** ***", "ip": "10.66.****.***", "rawIp": "10.66.****.***", "instanceName": "myinstance", "runningState": "running", "state": "online", "errorDescription": "", "status": "power on", _ "machineType": "myinstance", "vpcId": "vpc- 3gaat6wvtl0sbwxx n****", "vpcSubnet": "vsw- 3gady7f50dgpp41j 8****", "networkMode": "" } ], "total": 1, "pageNumber": 10, "pageSize": 1 } | The response data. |
|---|---|---|---|
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListSecurityGroupInstance &SgId=sg-bp197668l6iupljy**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "total":1,
  "pageNumber":10,
  "data":[
```

`{`

```json
    "networkMode":"",
    "errorDescription":"",
    "instanceName":"myinstance",
    "ip":"10.66.****.***",
    "vpcId":"vpc-3gaat6wvtl0sbwxxn****",
    "runningState":"running",
    "ID":0,
    "sn":"007269004887******",
    "rawIp":"10.66.****.***",
    "state":"online",
    "machineType":"myinstance",
    "vpcSubnet":"vsw-3gady7f50dgpp41j8****",
    "status":"power_on"
```

`}` `],`

```json
  "pageSize":1
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <total>1</total>
 <pageNumber>10</pageNumber>
 <data>
  <networkMode  />
  <errorDescription  />
  <instanceName>myinstance</instanceName>
  <ip>10.66.****.***</ip>
  <vpcId>vpc-3gaat6wvtl0sbwxxn****</vpcId>
  <runningState>running</runningState>
  <ID>0</ID>
  <sn>007269004887******</sn>
  <rawIp>10.66.****.***</rawIp>
  <state>online</state>
  <machineType>myinstance</machineType>
  <vpcSubnet>vsw-3gady7f50dgpp41j8****</vpcSubnet>
  <status>power_on</status>
 </data>
 <pageSize>1</pageSize>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.4.11 DeleteSecurityGroupInstance

Remove Bare Metal Computing Platform (BMCP) instances from a security group.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Quer y | No | sg-bp197668l6iupljy**** | The ID of the security group. |
| InstanceN ameList | Json | Quer y | No | ["test1","test2"] | The list of instance names. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data": { "SgId": "sg- bp197668l6iupljy** **", "InstanceNameList ": ["",""] } } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | 66dfddc6-b547- 11ee-aa84- acde4800**** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteSecurityGroupInstance &SgId=sg-bp197668l6iupljy**** &InstanceNameList=["test1","test2"] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "SgId":"sg-bp197668l6iupljy****",
   "InstanceNameList":[
    "",
```

`""` `]` `}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"66dfddc6-b547-11ee-aa84-acde4800****",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <SgId>sg-bp197668l6iupljy****</SgId>
  <InstanceNameList  />
  <InstanceNameList  />
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>66dfddc6-b547-11ee-aa84-acde4800****</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

### 5.5 Key pair

#### 5.5.1 CreateKeyPair

Create a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Name | Strin g | Quer y | No | test | The name of the key pair. The name cannot be the same as an existing key pair. Itmust be 2 to 128 characters in length, and cannot start with a special character or a digit. It can contain only periods (.), underscores ( ), hyphens (-), and _ colons (:) for special characters. |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | Iaas test _ | The name of the organization, which identifies the organization to which the resource belongs. |
| ResourceG roup | Strin g | Quer y | No | ResourceTest | The ID of the resource set, used to categorize and manage resoures. |
| RegionId | Strin g | Quer y | No | cn-wulan-env***-d01 | The ID of the region. |
| PublicKey | Strin g | Quer y | No | ssh-rsa**** | The public key. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "ID": 0, "name": "test", "publicKey": "", "privateKey": "", "keyPairFingerPrint ": "4096 SHA256:xsodVF6lB pYzC5043KdGxoXd RoKuoby6rJDK7h** ** root@vm01003800 **** (RSA)" } | The response data. |

| status | Integer | 200 | The status of the response. |
|---|---|---|---|
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateKeyPair &Name=test &Department=Iaas_test &ResourceGroup=ResourceTest &RegionId=cn-wulan-env***-d01 &PublicKey=ssh-rsa**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "privateKey":"",
  "name":"test",
  "ID":0,
  "publicKey":"",
  "keyPairFingerPrint":"4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7h**** root@vm0
1003800**** (RSA)"
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <privateKey />
 <name>test</name>
 <ID>0</ID>
 <publicKey />
 <keyPairFingerPrint>4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7h**** root@vm0100
3800**** (RSA)</keyPairFingerPrint> </data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.5.2 ListKeyPair

Query the list of key pairs.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | Strin g | Quer y | No | test | The name of the key pair. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10. |
| KeyPairFin gerPrint | Strin g | Quer y | No | 4096 SHA256:xsodVF6lBpYzC5 043KdGxoXdRoKuoby6rJD K7hR**** root@vm01003800**** (RSA) | The fingerprint of the key pair. |

**Response parameters**

| > Document Versi | on: 20260731 |   | 30 |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":[ { "name": "test", "region": "cn-test- ****-d01", "organization": "4", "resourceGroup": "3", "keyPairFingerPrint ": "4096 SHA256:xsodVF6lB pYzC5043KdGxoXd RoKuoby6rJDK7hR* *** root@vm01003800 **** (RSA)", "createTime": "0001-01- 01T00:00:00Z", "updateTime": "0001-01- 01T00:00:00Z" } ], "total":1, "pageNum":1, "pageSize":1 } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListKeyPair &KeyPairName=test &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "total":1,
  "data":[
```

`{`

```json
    "resourceGroup":"3",
    "createTime":"0001-01-01T00:00:00Z",
    "organization":"4",
    "name":"test",
    "updateTime":"0001-01-01T00:00:00Z",
    "region":"cn-test-****-d01",
    "keyPairFingerPrint":"4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7hR**** root@
vm01003800**** (RSA)"
```

`}` `],`

```json
  "pageSize":1,
  "pageNum":1
```

`},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <total>1</total>
 <data>
  <resourceGroup>3</resourceGroup>
  <createTime>0001-01-01T00:00:00Z</createTime>
  <organization>4</organization>
  <name>test</name>
  <updateTime>0001-01-01T00:00:00Z</updateTime>
  <region>cn-test-****-d01</region>
  <keyPairFingerPrint>4096 SHA256:xsodVF6lBpYzC5043KdGxoXdRoKuoby6rJDK7hR**** root@vm01
003800**** (RSA)</keyPairFingerPrint>
 </data>
 <pageSize>1</pageSize>
 <pageNum>1</pageNum>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.5.3 ConfigKeyPair

Attach a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | Strin g | Quer y | No | test | The name of the key pair. |
| MachineSN List | Json | Quer y | No | ["980017160373****","98 0020500749****"] | The list of Bare Metal Computing Platform (BMCP) instance serial numbers (SNs). Each instance can be attached with only one key pair. If the instance has been attached with a key pair, the new key pair automatically replaces the original one after attaching. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":[ { "MachineSN":"980 017160373***", "Message":"succes sful", "Success":true } ], } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | ** | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ConfigKeyPair &MachineSNList=["980017160373****","980020500749****"] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":[
```

`{`

```json
    "MachineSN":"980017160373***",
    "Message":"successful",
    "Success":true
```

`}` `]` `},`

```json
 "errorTitle":"Successful",
 "requestId":"**",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <MachineSN>980017160373***</MachineSN>
  <Message>successful</Message>
  <Success>true</Success>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>**</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.5.4 UnbindKeyPair

Detach a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| KeyPairNa me | Strin g | Quer y | No | KeyPair Name _ | The name of the key pair. |
|---|---|---|---|---|---|
| MachineSN List | Json | Quer y | No | ["980017160373****","98 0020500749****"] | The list of Bare Metal Computing Platform (BMCP) instance serial numbers (SNs). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":[ { "MachineSN":"980 017160373****", "Message":"succes sful", "Success":true } ], } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UnbindKeyPair &KeyPairName=KeyPair_Name &MachineSNList=["980017160373****","980020500749****"] &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":[
```

`{`

```json
    "MachineSN":"980017160373****",
    "Message":"successful",
    "Success":true
```

`}` `]` `},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <MachineSN>980017160373****</MachineSN>
  <Message>successful</Message>
  <Success>true</Success>
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

#### 5.5.5 DeleteKeyPair

Delete a key pair.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| KeyPairNa me | Strin g | Quer y | No | test-KeyPairName | The name of the key pair. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | Successful | The error code. |
| errorTitle | String | Successful | The error title. |
| errorMessage | String | Successful | The error message. |
| data | Map | { "data":{ "name":"", "success": true }, } | The response data. |
| status | Integer | 200 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteKeyPair &KeyPairName=test-KeyPairName &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "success":true,
   "name":""
```

`}` `},`

```json
 "errorTitle":"Successful",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"Successful",
 "errorCode":"Successful",
 "status":200
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <success>true</success>
  <name />
 </data>
</data> <errorTitle>Successful</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>Successful</errorMessage> <errorCode>Successful</errorCode> <status>200</status>
```

### 5.6 Elastic cache acceleration

#### 5.6.1 CreateEdaCluster

Enable an elastic cache acceleration cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the Container Service for Kubernetes (ACK) - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TaskId":"1284c8b 8-9571-11ee-a39e- 16f363c7****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateEdaCluster &ClusterId=ack-8EEjd6**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TaskId":"1284c8b8-9571-11ee-a39e-16f363c7****"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TaskId>1284c8b8-9571-11ee-a39e-16f363c7****</TaskId>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.6.2 DeleteEdaCluster

Disable an elastic cache acceleration cluster.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the Container Service for Kubernetes (ACK) - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "TaskId": "1284c8b8-9571- 11ee-a39e- 16f363c7****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteEdaCluster &ClusterId=ack-8EEjd6**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TaskId":"1284c8b8-9571-11ee-a39e-16f363c7****"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TaskId>1284c8b8-9571-11ee-a39e-16f363c7****</TaskId>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

### 5.7 Data distribution

#### 5.7.1 ListMP2pTask

Query the list of data distribution tasks.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| AckCluster ID | Strin g | Quer y | No | cef51d60a6778415ab3a8 026c24***** | The unique ID of the Container Service for Kubernetes (ACK) cluster in the Bare Metal Computing Platform (BMCP) cluster. |

| TaskName | Strin g | Quer y | No | task-name | The name of the task. |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": { "TotalCount": 1, "PageSize": 10, "PageNumber": 1, "TaskList": [ { "PreheatTimeout": "30m", "Status": "Failed", "TaskID": "0040705d-0f0b- 4650-9399- d9b78d5d****", "AckClusterId": "c4c2f574d483740 5b90132ea1b898* ***", "Message": "Unknown", "TaskName": "test", "PreheatConcurren cy": 8, "OSSUrl": "oss://{bucket}.en dpoint", "PreheatNodeList": [ "i- d8pmruuheob4fv1 m****" ] } ] } } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response, which is used to handle different versions of the operation |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListMP2pTask &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "TotalCount":1,
   "PageSize":10,
   "PageNumber":1,
   "TaskList":[
```

`{`

```json
     "PreheatTimeout":"30m",
     "Status":"Failed",
     "TaskID":"0040705d-0f0b-4650-9399-d9b78d5d****",
     "AckClusterId":"c4c2f574d4837405b90132ea1b898****",
     "Message":"Unknown",
     "TaskName":"test",
     "PreheatConcurrency":8,
     "OSSUrl":"oss://{bucket}.endpoint",
     "PreheatNodeList":[
      "i-d8pmruuheob4fv1m****"
```

`]` `}` `]` `}` `},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <PageNumber>1</PageNumber>
  <TaskList>
   <PreheatTimeout>30m</PreheatTimeout>
   <Status>Failed</Status>
   <TaskID>0040705d-0f0b-4650-9399-d9b78d5d****</TaskID>
   <AckClusterId>c4c2f574d4837405b90132ea1b898****</AckClusterId>
   <Message>Unknown</Message>
   <TaskName>test</TaskName>
   <PreheatConcurrency>8</PreheatConcurrency>
   <OSSUrl>oss://{bucket}.endpoint</OSSUrl>
   <PreheatNodeList>i-d8pmruuheob4fv1m****</PreheatNodeList>
  </TaskList>
 </data>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

#### 5.7.2 CreateMP2pTask

Create a data distribution task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| TaskName | Strin g | Quer y | Yes | Task1 | The name of the task. |
| AckCluster ID | Strin g | Quer y | Yes | cef51d60a6778415ab3a8 026c24***** | The ID of the Container Service for Kubernetes (ACK) cluster. |
| PreheatNo deList | Json | Quer y | No | ["node1","node2"] | The list of preheat nodes. |

| OSSUrl | Strin g | Quer y | Yes | oss://{bucket}.endpoint | The Uniform Resource Identifier (URI) of the data file in Object Storage Service (OSS). |
|---|---|---|---|---|---|
| PreheatCo ncurrency | Integ er | Quer y | No | 8 | The preheat concurrency. Valid values: integers from 1 to 100 |
| PreheatTi meout | Integ er | Quer y | No | 30 | The preheat timeout period. Unit: minutes Set an appropriate prehaeat timeout period based on the data size. We recommend that you set at least one minute for every 30 GB of data. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "data": { "TaskName": "Task1", "AckClusterId": "cef51d60a677841 5ab3a8026c24**** *" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response, which is used to handle different versions of the operation. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=CreateMP2pTask &TaskName=Task1 &AckClusterID=cef51d60a6778415ab3a8026c24***** &PreheatNodeList=["node1","node2"] &OSSUrl=oss://{bucket}.endpoint &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "data":{
   "AckClusterId":"cef51d60a6778415ab3a8026c24*****",
   "TaskName":"Task1"
```

`}` `},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <data>
  <AckClusterId>cef51d60a6778415ab3a8026c24*****</AckClusterId>
  <TaskName>Task1</TaskName>
 </data>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

#### 5.7.3 DeleteMP2pTask

Delete a data distribution task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| TaskID | Strin g | Quer y | No | 1284c8b8-9571-11ee- a39e-16f363c7**** | The ID of the data distribution task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "TaskID": "0040705d-0f0b- 4650-9399- d9b78d5d****", "AckClusterId": "c4c2f574d483740 5b90132ea1b898* ***" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DeleteMP2pTask &TaskID=1284c8b8-9571-11ee-a39e-16f363c7**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TaskID":"0040705d-0f0b-4650-9399-d9b78d5d****",
  "AckClusterId":"c4c2f574d4837405b90132ea1b898****"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TaskID>0040705d-0f0b-4650-9399-d9b78d5d****</TaskID>
 <AckClusterId>c4c2f574d4837405b90132ea1b898****</AckClusterId>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

### 5.8 Node management

#### 5.8.1 DiagnoseQuery

Start an intelligent diagnosis task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Query | Strin g | Quer y | Yes | validateMachineInfo error, hsw is not exists | The fault error message. |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-****-d01 | The ID of the region. |
| Language | Strin g | Quer y | No | zh CN _ | The locale. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "status": "pending", "result": "Starting diagnosis", "created at": _ "2026-07- 09T23:58:44+08:0 0" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | 1.0 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DiagnoseQuery &Query=validateMachineInfo error, hsw is not exists &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-****-d01 &Language=zh_CN &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"1.0",
 "data":{
  "result":"Starting diagnosis",
  "created_at":"2026-07-09T23:58:44+08:00",
  "status":"pending"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>1.0</responseVersion> <data>
 <result>Starting diagnosis</result>
 <created_at>2026-07-09T23:58:44+08:00</created_at>
 <status>pending</status>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.8.2 TaskQuery

Query the execution progress and results of a fault diagnosis task.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Quer y | Yes | 1284c8b8-9571-11ee- a39e-16f363c7**** | The ID of the fault diagnosis task. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "allTaskStatus": "processing/compl eted", "response": [ { "isAdvice": true, "solution": "Solution description", "taskStatus": "pending", "progress": 0.5, "errMessage": "Error message", "subTaskid": "sub- task-001", "subQuery": "Subtask query information" }, { "isAdvice": false, "solution": "Another solution", "taskStatus": "success", "progress": 1.0, "errMessage": "", "subTaskid": "sub- task-002", "subQuery": "Additional query details" } ] } | The response data. |
| status | Integer | 0 | The status of the response. |

| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=TaskQuery &TaskId=1284c8b8-9571-11ee-a39e-16f363c7**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "allTaskStatus":"processing/completed",
  "response":[
```

`{`

```json
    "solution":"Solution description",
    "isAdvice":true,
    "progress":0.5,
    "subTaskid":"sub-task-001",
    "taskStatus":"pending",
    "errMessage":"Error message",
    "subQuery":"Subtask query information"
```

`},` `{`

```json
    "solution":"Another solution",
    "isAdvice":false,
    "progress":1.0,
    "subTaskid":"sub-task-002",
    "taskStatus":"success",
    "errMessage":"",
    "subQuery":"Additional query details"
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <allTaskStatus>processing/completed</allTaskStatus>
 <response>
  <solution>Solution description</solution>
  <isAdvice>true</isAdvice>
  <progress>0.5</progress>
  <subTaskid>sub-task-001</subTaskid>
  <taskStatus>pending</taskStatus>
  <errMessage>Error message</errMessage>
  <subQuery>Subtask query information</subQuery>
 </response>
 <response>
  <solution>Another solution</solution>
  <isAdvice>false</isAdvice>
  <progress>1</progress>
  <subTaskid>sub-task-002</subTaskid>
  <taskStatus>success</taskStatus>
  <errMessage  />
  <subQuery>Additional query details</subQuery>
 </response>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.8.3 DiagnosePoint

Rate the intelligent diagnosis results.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| TaskId | Strin g | Quer y | Yes | 1284c8b8-9571-11ee- a39e-16f363c7**** | The ID of the task. |
| Score | Float | Quer y | Yes | 5 | The rating, in stars. Valid values: 1 to 5 stars, in increments of 0.5 stars. |

| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
|---|---|---|---|---|---|
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RegionId | Strin g | Quer y | No | cn-wulan-****-d01 | The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "score": 5, "task id": _ "1284c8b8-9571- 11ee-a39e- 16f363c7****" } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=DiagnosePoint &Department=4 &ResourceGroup=3 &RegionId=cn-wulan-****-d01 &TaskId=1284c8b8-9571-11ee-a39e-16f363c7**** &Score=5 &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "score":5,
  "task_id":"1284c8b8-9571-11ee-a39e-16f363c7****"
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <score>5</score>
 <task_id>1284c8b8-9571-11ee-a39e-16f363c7****</task_id>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

### 5.9 Auto-healing event tickets

#### 5.9.1 ListOrder

Query the list of auto-healing event tickets.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| OrderId | Strin g | Quer y | No | yg9Ve6**** | The ID of the event ticket. |
| OrderType | Strin g | Quer y | No | auto healing _ | The type of the event ticket. Currently, only auto healing is _ supported. |
| Status | Strin g | Quer y | No | fixed | The ticket status. Valid values: created: Pending approval fixed: Closed timeout: Expired approved: Approved rejected: Rejected |
| InstanceId | Strin g | Quer y | No | i-d8pms5uheob3l5ij**** | The ID of the node. |
| ClusterId | Strin g | Quer y | No | ack-ZRy3J8b75x | The ID of the Container Service for Kubernetes (ACK) - intelligent computing cluster. You can call the ListAckCluster operation to query the cluster ID. |
| CreateTim e | Strin g | Quer y | No | 2021-10-15 08:56:23 | The time when the ticket was created. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| errorCode | String | "" | The error code. |
|---|---|---|---|
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "TotalCount": 1, "PageSize": 10, "PageNumber": 1, "OrderList": [ { "handler": "", "creator": "b225****-e2ab- 47fa-afa3- 34f7488c****-0", "cluster id": "ack- _ ZRy3J8b75x", "event id": _ "b225****-e2ab- 47fa-afa3- 34f7488c****-0-0", "instance id": "i- _ d8pms5uheob3l5ij* ***", "create time": _ "2026-07- 13T01:04:11+08:0 0", "order source": _ "bmcp healing", _ "order id": _ "yg9Ve6****", "order type": _ "auto healing", _ "status": "timeout" } ] } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListOrder &OrderType=auto_healing &Status=fixed &ClusterId=ack-ZRy3J8b75x &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":1,
  "PageSize":10,
  "PageNumber":1,
  "OrderList":[
```

`{`

```json
    "handler":"",
    "creator":"b225****-e2ab-47fa-afa3-34f7488c****-0",
    "cluster_id":"ack-ZRy3J8b75x",
    "event_id":"b225****-e2ab-47fa-afa3-34f7488c****-0-0",
    "instance_id":"i-d8pms5uheob3l5ij****",
    "create_time":"2026-07-13T01:04:11+08:00",
    "order_source":"bmcp_healing",
    "order_id":"yg9Ve6****",
    "order_type":"auto_healing",
    "status":"timeout"
```

`}` `]` `},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>1</TotalCount>
 <PageSize>10</PageSize>
 <PageNumber>1</PageNumber>
 <OrderList>
  <handler  />
  <creator>b225****-e2ab-47fa-afa3-34f7488c****-0</creator>
  <cluster_id>ack-ZRy3J8b75x</cluster_id>
  <event_id>b225****-e2ab-47fa-afa3-34f7488c****-0-0</event_id>
  <instance_id>i-d8pms5uheob3l5ij****</instance_id>
  <create_time>2026-07-13T01:04:11+08:00</create_time>
  <order_source>bmcp_healing</order_source>
  <order_id>yg9Ve6****</order_id>
  <order_type>auto_healing</order_type>
  <status>timeout</status>
 </OrderList>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

#### 5.9.2 GetOrderDetail

Query the details of an auto-healing event ticket.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OrderId | Strin g | Quer y | No | yg9Ve6**** | The ID of the event ticket. You can call the ListOrder operation to query the event ticket ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |

| errorTitle | String | “” | The error title. |
|---|---|---|---|
| errorMessage | String | "" | The error message. |
| data | Map | { "order detail": { _ "handler": "", "creator": "4d92****-06ed- 4fac-8658- 0ddd7734****-0", "cluster id": "ack- _ ZRy3J8****", "event id": _ "4d92****-06ed- 4fac-8658- 0ddd7734****-0- 0", "instance id": _ "i- d8pms5uheob3l5ij* ***", "create time": _ "2026-07- 09T23:58:11+08:0 0", "complete time": _ "2026-07- 13T01:02:11+08:0 0", "approved time": _ "2026-07- 09T23:58:44+08:0 0", "order source": _ "bmcp healing", _ "order id": _ "QG0J0u****", "order type": _ "auto healing", _ "status": "fixed" } } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | v1 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=GetOrderDetail &OrderId=yg9Ve6**** &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"",
 "data":"",
 "errorTitle":"",
 "requestId":"",
 "success":"",
 "errorMessage":"",
 "errorCode":"",
 "status":""
```

`}`

#### 5.9.3 UpdateOrder

Approve an auto-healing event ticket.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| OrderId | Strin g | Quer y | No | yg9Ve6**** | The ID of the event ticket. You can call the ListOrder operation to query the event ticket ID. |

| Status | Strin g | Quer y | No | fixed | The status of the event ticket. Valid values: created: Pending approval fixed: Closed timeout: Expired approved: Approved rejected: Rejected |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "" | The error message. |
| data | Map | { "order detail": { _ "handler": "", "creator": "4d92****-06ed- 4fac-8658- 0ddd7734****-0", "cluster id": "ack- _ ZRy3J8****", "event id": _ "4d92****-06ed- 4fac-8658- 0ddd7734****-0- 0", "instance id": _ "i- d8pms5uheob3l5ij* ***", "create time": _ "2026-07- 09T23:58:11+08:0 0", "complete time": _ "2026-07- 13T01:02:11+08:0 0", "approved time": _ "2026-07- 09T23:58:44+08:0 0", "order source": _ "bmcp healing", _ "order id": _ "QG0J0u****", "order type": _ "auto healing", _ "status": "fixed" } } | The response data. |

| status | Integer | 0 | The status of the response. |
|---|---|---|---|
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=UpdateOrder &OrderId=yg9Ve6**** &Status=fixed &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "order_detail":{
   "handler":"",
   "creator":"4d92****-06ed-4fac-8658-0ddd7734****-0",
   "cluster_id":"ack-ZRy3J8****",
   "event_id":"4d92****-06ed-4fac-8658-0ddd7734****-0-0",
   "instance_id":"i-d8pms5uheob3l5ij****",
   "create_time":"2026-07-09T23:58:11+08:00",
   "complete_time":"2026-07-13T01:02:11+08:00",
   "approved_time":"2026-07-09T23:58:44+08:00",
   "order_source":"bmcp_healing",
   "order_id":"QG0J0u****",
   "order_type":"auto_healing",
   "status":"fixed"
```

`}` `},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <order_detail>
  <handler  />
  <creator>4d92****-06ed-4fac-8658-0ddd7734****-0</creator>
  <cluster_id>ack-ZRy3J8****</cluster_id>
  <event_id>4d92****-06ed-4fac-8658-0ddd7734****-0-0</event_id>
  <instance_id>i-d8pms5uheob3l5ij****</instance_id>
  <create_time>2026-07-09T23:58:11+08:00</create_time>
  <complete_time>2026-07-13T01:02:11+08:00</complete_time>
  <approved_time>2026-07-09T23:58:44+08:00</approved_time>
  <order_source>bmcp_healing</order_source>
  <order_id>QG0J0u****</order_id>
  <order_type>auto_healing</order_type>
  <status>fixed</status>
 </order_detail>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage /> <errorCode /> <status>0</status>
```

### 5.10 Recycle bin

#### 5.10.1 ListRecycleBMCPMachine

Query information about recycled Bare Metal Computing Platform (BMCP) bare metal instances.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |

| Application Group | Strin g | Quer y | No | recycle | The type of the resource. Currently, only recycle is supported. |
|---|---|---|---|---|---|
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Default value: 1 |
| PageSize | Integ er | Quer y | No | 10 | The number of entries per page. Default value: 10 |
| InstanceN ameList | Json | Quer y | No | ["test1","test2"] | The list of node names. |
| KeyPairNa me | Strin g | Quer y | No | test-KeyPairName | The name of the key pair. |
| DeployTyp e | Strin g | Quer y | No | bmcp | The type of the instance deployed. Valid values: bmcp: Intelligent computing high- bandwidth network bmcp managed: _ Intelligent computing - managed bmcp no clone: _ _ Intelligent computing - in-band managed ehpc: High- performance computing (HPC) high- bandwidth network ehpc managed: HPC - _ managed aspeed: Training and inference optimization base: Basic intelligent computing bfi: Converged high- bandwidth network bfi base: Cconverged _ basic |
| SecurityGr oupId | Strin g | Quer y | No | sg-bp67acfmxazb4p**** | The ID of the security group. |

| ClusterTyp e | Strin g | Quer y | No | bmcp | The cluster type. Valid values: bmcp: Bare metal - intelligent computing cluster ack: Container Service for Kubernetes (ACK) - intelligent computing cluster ehpcp: Bare metal - HPC cluster bfi: Converged computing cluster |
|---|---|---|---|---|---|
| ClusterId | Strin g | Quer y | No | ack-8EEjd6**** | The ID of the cluster. |
| ClusterNa me | Strin g | Quer y | No | cluster-name | The name of the cluster. |
| State | Strin g | Quer y | No | offline | The operation status of the node. If you leave this parameter empty, nodes in all statuses are returned. Valid values: manageable: Running available: Completed enroll, rolling: Creating operating: Under O&M cleaning: Releasing deleting: Deleting rebooting: Restarting powering on: Starting _ shutting down: _ Stopping offline: No heartbeat error: Failed unknown: Unknown |
| RunningSt ate | Strin g | Quer y | No | running | The heartbeat status. Valid values: running: Running offline: No heartbeat |
| InstanceN ame | Strin g | Quer y | No | i-d8pms5uheob4fv1m**** | The name of the node. |

| InstanceAli as | Strin g | Quer y | No | c25j0****.cloud.j06.**** | The alias of the node, which is an alternative name for easy identification. |
|---|---|---|---|---|---|
| ID | Strin g | Quer y | No | 2 | The ID of the node. |
| SN | Strin g | Quer y | No | 21061****JXDP400**** | The serial number (SN) of the node. |
| IP | Strin g | Quer y | No | 192.168.1.1 | The IP address of the node. |
| BMCIP | Strin g | Quer y | No | 192.168.1.1 | The BMC IP address of the node. |
| MachineTy pe | Strin g | Quer y | No | QPG78P4M****.03BB | The name of the instance type. |
| VPCID | Strin g | Quer y | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the virtual private cloud (VPC). |
| AliYunAssi stID | Strin g | Quer y | No | mi-hz034jn***yxhc0 | The globally unique ID of Cloud Assistant. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
|   |   | { "PageSize": 10, "data": { "RecycleBMCPMac hineList": [ { "DeployType": "bfi base", _ "RunningState": "running", "Image": "alinux 3 x86 64 _ _ _ _ uefi 20260423 bf3 _ _ .qcow2", "Gpu": |   |

| veloper Guide·AP | I reference |   | Machine Learning Platform for A |
|---|---|---|---|
|   |   | "NVIDIA **** PCIe" _ _ , "Department": 4, "OverlayEnabled": false, "InstanceAlias": "i- 7c4ba42a32f64*** *", "AliYunAssistID": "", "ID": 181, "RawIP": "10.66.****.4", "HostName": "test name", _ "Status": "power on", _ "OsUpdate": false, "IP": "10.66.****.4", "InstanceName": "test neme", _ "State": "offline", "Region": "cn- wulan-****-d01", "BMCIP": "10.38.****.47", "DepartmentName ": "iaas test", _ "NetworkCardType ": "0", "AgentID": 24, "VideoMemory": 640, "ResourceGroupNa me": "ResourceSet(iaas _ test)", "Organization": "4", "Description": "test", "VPCID": "vpc- 3gas7mox8s04hkd 38****", "TflopsFP32": 6048, "Config": { "Memory": 18, "CPUNumber": 14 }, "Operation": "", "RecycleTime": "", "DpuInfo": { "ErrorDescription": "", "Status": "power on", _ "LoginName": "root", "MachineSN": "2106****UPXDP50 0****", "RunningState": "running", "CGWPorts": "", "Zone": "", "Hostname": "c25d0****.cloud.d 03.****", "MachineType": "PG****M6S2****.3 |   |

| data | Map | 2", "BMCPassword": "", "Specification": "", "BMCPort": "", "InstanceName": "test", "BMCIP": "10.38.****.44", "LastHeartbeatTim e": "2026-07- 30T02:33:25+08:0 0", "ID": 1, "SN": "****30XZ0****", "BMCUser": "", "ASWID": "EHSW- 200G-D-G3-POD1- RMC2-5-****-35-3- 1.****", "Subnet": "", "RawIP": "10.****.****.5", "LoginPwd": "" }, "MappingStatus": "Offline", "ApplicationGroup" : "recycle", "GpuNum": 8, "Monitor": "", "NetworkCardNum" : 1, "VPCSubnet": "vsw- 3ga6o6e1eywm8a yat****", "ClusterName": "test", "VirtualStrategy": "", "RMRegionId": "cn-wulan-****- d01", "SN": "test- name", "ResourceGroup": 3, "ImageUniqueKey": "i- d86q88mheobd49s t****", "OS": "Aliyun", "ClusterId": "bfi- sqFetW****", "Zone": "cn-wulan- ****-****-a", "CreateTime": "2026-06- 12T14:47:26+08:0 0", "MachineType": "test name", _ "SupportVirtStg": "", "Specification": "dpu-host-default- bfi-base", "ClusterType": "bfi", "LvmCapacity": "0", "RetentionPeriod": 0, | The response data. |
|---|---|---|---|
|   |   | "ClusterArchType": "", "Extra": "", |   |

|   |   | "DefaultImage": "alinux 3 x86 64 _ _ _ _ uefi 20260423 bf3 _ _ .qcow2", "ReleaseTime": "", "UserId": "127756957048*** *", "RecycleStatus": "", "RegionId": "cn- wulan-****-d01" } ] }, "TotalCount": 11, "PageNumber": 2 } |   |
|---|---|---|---|
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |
| responseVersi on | String | v1 | The version of the response. |

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ListRecycleBMCPMachine &Department=4 &ResourceGroup=3 &ApplicationGroup=recycle &ClusterType=bmcp &DeployType=bmcp &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"v1",
 "data":{
  "TotalCount":11,
  "PageSize":10,
  "data":{
   "RecycleBMCPMachineList":[
```

`{`

```json
     "DeployType":"bfi_base",
     "RunningState":"running",
     "Image":"alinux_3_x86_64_uefi_20260423_bf3.qcow2",
     "Gpu":"NVIDIA_****_PCIe",
     "Department":4,
```

```json
     "OverlayEnabled":false,
     "InstanceAlias":"i-7c4ba42a32f64****",
     "AliYunAssistID":"",
     "ID":181,
     "RawIP":"10.66.****.4",
     "HostName":"test_name",
     "Status":"power_on",
     "OsUpdate":false,
     "IP":"10.66.****.4",
     "InstanceName":"test_neme",
     "State":"offline",
     "Region":"cn-wulan-****-d01",
     "BMCIP":"10.38.****.47",
     "DepartmentName":"iaas_test",
     "NetworkCardType":"0",
     "AgentID":24,
     "VideoMemory":640,
     "ResourceGroupName":"ResourceSet(iaas_test)",
     "Organization":"4",
     "Description":"test",
     "VPCID":"vpc-3gas7mox8s04hkd38****",
     "TflopsFP32":6048,
     "Config":{
      "Memory":18,
      "CPUNumber":14
```

`},`

```json
     "Operation":"",
     "RecycleTime":"",
     "DpuInfo":{
      "ErrorDescription":"",
      "Status":"power_on",
      "LoginName":"root",
      "MachineSN":"2106****UPXDP500****",
      "RunningState":"running",
      "CGWPorts":"",
      "Zone":"",
      "Hostname":"c25d0****.cloud.d03.****",
      "MachineType":"PG****M6S2****.32",
      "BMCPassword":"",
      "Specification":"",
      "BMCPort":"",
      "InstanceName":"test",
      "BMCIP":"10.38.****.44",
      "LastHeartbeatTime":"2026-07-30T02:33:25+08:00",
      "ID":1,
      "SN":"****30XZ0****",
      "BMCUser":"",
      "ASWID":"EHSW-200G-D-G3-POD1-RMC2-5-****-35-3-1.****",
      "Subnet":"",
      "RawIP":"10.****.****.5",
      "LoginPwd":""
```

`},`

```json
     "MappingStatus":"Offline",
     "ApplicationGroup":"recycle",
```

`"G` `N` `"``8`

```json
     "GpuNum":8,
     "Monitor":"",
     "NetworkCardNum":1,
     "VPCSubnet":"vsw-3ga6o6e1eywm8ayat****",
     "ClusterName":"test",
     "VirtualStrategy":"",
     "RMRegionId":"cn-wulan-****-d01",
     "SN":"test-name",
     "ResourceGroup":3,
     "ImageUniqueKey":"i-d86q88mheobd49st****",
     "OS":"Aliyun",
     "ClusterId":"bfi-sqFetW****",
     "Zone":"cn-wulan-****-****-a",
     "CreateTime":"2026-06-12T14:47:26+08:00",
     "MachineType":"test_name",
     "SupportVirtStg":"",
     "Specification":"dpu-host-default-bfi-base",
     "ClusterType":"bfi",
     "LvmCapacity":"0",
     "RetentionPeriod":0,
     "ClusterArchType":"",
     "Extra":"",
     "DefaultImage":"alinux_3_x86_64_uefi_20260423_bf3.qcow2",
     "ReleaseTime":"",
     "UserId":"127756957048****",
     "RecycleStatus":"",
     "RegionId":"cn-wulan-****-d01"
```

`}` `]` `},`

```json
  "PageNumber":2
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>v1</responseVersion> <data>
 <TotalCount>11</TotalCount>
 <PageSize>10</PageSize>
 <data>
  <RecycleBMCPMachineList>
   <DeployType>bfi_base</DeployType>
   <RunningState>running</RunningState>
   <Image>alinux_3_x86_64_uefi_20260423_bf3.qcow2</Image>
   <Gpu>NVIDIA_****_PCIe</Gpu>
   <Department>4</Department>
   <OverlayEnabled>false</OverlayEnabled>
```

```xml
   <InstanceAlias>i-7c4ba42a32f64****</InstanceAlias>
   <AliYunAssistID  />
   <ID>181</ID>
   <RawIP>10.66.****.4</RawIP>
   <HostName>test_name</HostName>
   <Status>power_on</Status>
   <OsUpdate>false</OsUpdate>
   <IP>10.66.****.4</IP>
   <InstanceName>test_neme</InstanceName>
   <State>offline</State>
   <Region>cn-wulan-****-d01</Region>
   <BMCIP>10.38.****.47</BMCIP>
   <DepartmentName>iaas_test</DepartmentName>
   <NetworkCardType>0</NetworkCardType>
   <AgentID>24</AgentID>
   <VideoMemory>640</VideoMemory>
   <ResourceGroupName>ResourceSet(iaas_test)</ResourceGroupName>
   <Organization>4</Organization>
   <Description>test</Description>
   <VPCID>vpc-3gas7mox8s04hkd38****</VPCID>
   <TflopsFP32>6048</TflopsFP32>
   <Config>
    <Memory>18</Memory>
    <CPUNumber>14</CPUNumber>
   </Config>
   <Operation  />
   <RecycleTime  />
   <DpuInfo>
    <ErrorDescription  />
    <Status>power_on</Status>
    <LoginName>root</LoginName>
    <MachineSN>2106****UPXDP500****</MachineSN>
    <RunningState>running</RunningState>
    <CGWPorts  />
    <Zone  />
    <Hostname>c25d0****.cloud.d03.****</Hostname>
    <MachineType>PG****M6S2****.32</MachineType>
    <BMCPassword  />
    <Specification  />
    <BMCPort  />
    <InstanceName>test</InstanceName>
    <BMCIP>10.38.****.44</BMCIP>
    <LastHeartbeatTime>2026-07-30T02:33:25+08:00</LastHeartbeatTime>
    <ID>1</ID>
    <SN>****30XZ0****</SN>
    <BMCUser  />
    <ASWID>EHSW-200G-D-G3-POD1-RMC2-5-****-35-3-1.****</ASWID>
    <Subnet  />
    <RawIP>10.****.****.5</RawIP>
    <LoginPwd  />
   </DpuInfo>
   <MappingStatus>Offline</MappingStatus>
   <ApplicationGroup>recycle</ApplicationGroup>
   <GpuNum>8</GpuNum>
```

`/`

```xml
   <Monitor  />
   <NetworkCardNum>1</NetworkCardNum>
   <VPCSubnet>vsw-3ga6o6e1eywm8ayat****</VPCSubnet>
   <ClusterName>test</ClusterName>
   <VirtualStrategy  />
   <RMRegionId>cn-wulan-****-d01</RMRegionId>
   <SN>test-name</SN>
   <ResourceGroup>3</ResourceGroup>
   <ImageUniqueKey>i-d86q88mheobd49st****</ImageUniqueKey>
   <OS>Aliyun</OS>
   <ClusterId>bfi-sqFetW****</ClusterId>
   <Zone>cn-wulan-****-****-a</Zone>
   <CreateTime>2026-06-12T14:47:26+08:00</CreateTime>
   <MachineType>test_name</MachineType>
   <SupportVirtStg  />
   <Specification>dpu-host-default-bfi-base</Specification>
   <ClusterType>bfi</ClusterType>
   <LvmCapacity>0</LvmCapacity>
   <RetentionPeriod>0</RetentionPeriod>
   <ClusterArchType  />
   <Extra  />
   <DefaultImage>alinux_3_x86_64_uefi_20260423_bf3.qcow2</DefaultImage>
   <ReleaseTime  />
   <UserId>127756957048****</UserId>
   <RecycleStatus  />
   <RegionId>cn-wulan-****-d01</RegionId>
  </RecycleBMCPMachineList>
 </data>
 <PageNumber>2</PageNumber>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.10.2 RevertMachine

Restore instances from the recycle bin.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
|---|---|---|---|---|---|
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| RevertMac hineList | Json | Quer y | No | [ { "InstanceName": "i- d8pms5uheob4fv1m****" , "ClusterBzid": "", "ClusterType": "bmcp" }, { "InstanceName": "i- d9jfbieheob5ghiu****", "ClusterBzid": "", "ClusterType": "bmcp" } ] | The list of bare metal instances to restore. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "data": [ { "InstanceName": "i- d8pms5uheob4fv1 m****", "ClusterBzid": "", "ClusterType": "bmcp" }, { "InstanceName": "i- d9jfbieheob5ghiu** **", "ClusterBzid": "", "ClusterType": "bmcp" } ], "total": 10, "pageNum": 1, "pageSize": 10 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | 1.0 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=RevertMachine &Department=4 &ResourceGroup=3 &RevertMachineList=[
```

`{`

```json
    "InstanceName": "i-d8pms5uheob4fv1m****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
```

`},` `{`

```json
    "InstanceName": "i-d9jfbieheob5ghiu****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
```

`}` `]`

```
&Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"1.0",
 "data":{
  "total":10,
  "data":[
```

`{`

```json
    "InstanceName":"i-d8pms5uheob4fv1m****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
```

`},` `{`

```json
    "InstanceName":"i-d9jfbieheob5ghiu****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
```

`}` `],`

```json
  "pageSize":10,
  "pageNum":1
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>1.0</responseVersion> <data>
 <total>10</total>
 <data>
  <InstanceName>i-d8pms5uheob4fv1m****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <data>
  <InstanceName>i-d9jfbieheob5ghiu****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```

#### 5.10.3 ReleaseMachine

Release machines from the recycle bin back to the resource pool.

**Request headers**

This operation uses common request headers only. For more information, see the documentation on common request parameters.

**Request parameters**

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Quer y | No | 4 | The ID of the organization. |
| ResourceG roup | Strin g | Quer y | No | 3 | The ID of the resource set. |
| ReleaseMa chineList | Json | Quer y | No | [ { "InstanceName": "i- d8pms5uheob4fv1m****" , "ClusterBzid": "", "ClusterType": "bmcp" }, { "InstanceName": "i- d9jfbieheob5ghiu****", "ClusterBzid": "", "ClusterType": "bmcp" } ] | The list of bare metal instances to restore. |
| OsUpdate | Bool ean | Quer y | No | false | Whether to clear data disks. Valid values: true: Clear data disks. After the data is permanently deleted, you must initialize the node in the resource pool to fully reinstall the node. false: Do not clear data disks. Default value: false |

| IsQuickCle an | Bool ean | Quer y | No | false | Whether to quickly clear the system disk. Valid values: true: Clear the system disk. The system disk of the node is restored to its initial image and the node is quickly released. After the release, you can quickly apply for the resource again. false: Do not clear the system disk. Default value: false |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | "" | The error code. |
| errorTitle | String | “” | The error title. |
| errorMessage | String | "“ | The error message. |
| data | Map | { "data": [ { "InstanceName": "i- d8pms5uheob4fv1 m****", "ClusterBzid": "", "ClusterType": "bmcp" }, { "InstanceName": "i- d9jfbieheob5ghiu** **", "ClusterBzid": "", "ClusterType": "bmcp" } ], "total": 10, "pageNum": 1, "pageSize": 10 } | The response data. |
| status | Integer | 0 | The status of the response. |
| requestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| success | Boolean | true | The status of the request. |

| responseVersi on | String | 1.0 | The version of the response. |
|---|---|---|---|

**Examples**

Sample requests

```
http://[Endpoint]/?Action=ReleaseMachine &Department=4 &ResourceGroup=3 &RevertMachineList=[
```

`{`

```json
    "InstanceName": "i-d8pms5uheob4fv1m****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
```

`},` `{`

```json
    "InstanceName": "i-d9jfbieheob5ghiu****",
    "ClusterBzid": "",
    "ClusterType": "bmcp"
```

`}` `]`

```
&OsUpdate=false &Common request parameters
```

Sample success responses `JSON` format `{`

```json
 "responseVersion":"1.0",
 "data":{
  "total":10,
  "data":[
```

`{`

```json
    "InstanceName":"i-d8pms5uheob4fv1m****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
```

`},` `{`

```json
    "InstanceName":"i-d9jfbieheob5ghiu****",
    "ClusterBzid":"",
    "ClusterType":"bmcp"
```

`}` `],`

```json
  "pageSize":10,
  "pageNum":1
```

`},`

```json
 "errorTitle":"“”",
 "requestId":"F0A8A039-930D-5EC1-97C8-************",
 "success":true,
 "errorMessage":"\"“",
 "errorCode":"",
 "status":0
```

`}` `XML` format

```xml
<responseVersion>1.0</responseVersion> <data>
 <total>10</total>
 <data>
  <InstanceName>i-d8pms5uheob4fv1m****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <data>
  <InstanceName>i-d9jfbieheob5ghiu****</InstanceName>
  <ClusterBzid  />
  <ClusterType>bmcp</ClusterType>
 </data>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data> <errorTitle>“”</errorTitle> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <success>true</success> <errorMessage>&quot;“</errorMessage> <errorCode /> <status>0</status>
```
