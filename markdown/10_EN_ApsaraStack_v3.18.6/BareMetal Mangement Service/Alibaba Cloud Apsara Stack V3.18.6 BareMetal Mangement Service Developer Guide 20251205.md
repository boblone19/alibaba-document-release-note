---
title: "BareMetal Mangement Service Developer Guide 20251205"
product_version: "V3.18.6"
pdf_pages: 139
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 BareMetal Mangement Service Developer Guide 20251205.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E8%A3%B8%E6%9C%BA%E7%AE%A1%E7%90%86BMS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20BareMetal%C2%A0Mangement%C2%A0Service%20Developer%20Guide%2020251205.pdf"
converter: line-classifier (PyMuPDF)
---

# BareMetal Mangement Service Developer Guide 20251205

| Term | Common parameter | Description |
|---|---|---|
| Region | Region | An Alibaba Cloud data center. After you create a resource, its region cannot be changed. |
| Zone | Zone | A physical location with independent power grids and networks within a region. Each region includes multiple zones. Zones within the same region are connected over an internal network. When a zone is down, other zones are not affected. |
| Bare metal instance | InstanceId/ID | BMS allows you to apply for, release, delete, and reapply for physical bare metal servers. You can also perform remote O&M operations on existing bare metal instances, such as starting, stopping, and restarting them. |
| Image | Image | In general, an image includes an operating system and application software. Images are used to maintain image metadata that is required to install bare metal servers. |

BareMetal Mangement Service

## API introduction

If you are familiar with network service protocols and one or more programming languages, we recommend that you call Bare Metal Service (BMS) API operations to manage your cloud resources and develop your applications.

**Usage notes**

BMS API supports HTTP or HTTPS requests. You can use only the POST method to send and receive requests. You can use SDKs to call BMS API operations. For information about how to use SDKs to call BMS API operations, see the BMS Developer Guide. For information about how to call API operations by using different tools, see Calling methods.

**Resource terms**

| Applicati on group | ApplicationGrou p | Application groups are used to distinguish instance assets. Bare Metal Instances: BMS allows you to apply for, release, delete, and reapply for physical bare metal servers. You can also perform remote O&M operations on existing bare metal instances, such as starting, stopping, and restarting them. In-band Managed Instances: To meet user requirements for in-band hosting of existing servers, BMS allows you to add, search for, view displayed information of, monitor, and perform remote O&M operations on in-band managed instances. Out-of-band Managed Instances: To meet user requirements for out-of-band hosting of existing servers, BMS allows you to add, search for, view displayed information of, monitor, and perform remote O&M operations on out-of-band managed instances, and log into them from an out-of-band console. |
|---|---|---|

BareMetal Mangement Service

| Operation | METHO D | Url | action name _ |
|---|---|---|---|
| ListInstance | POST | /v1/ascm/instance/listInstance | ListInstance |
| ListInstanceOvervi ew | POST | /v1/ascm/instance/listInstanceO verview | ListInstanceOverview |
| ApplyManagedInst ance | POST | /v1/ascm/instance/applyManage dInstance | ApplyManagedInstance |
| ReApplyManagedIn stance | POST | /v1/ascm/instance/reApplyMana gedInstance | ReApplyManagedInstance |
| ListUnApplyCPUArc h | POST | url:/v1/ascm/instance/listUnAppl yCPUArch | ListUnApplyCPUArch |
| ListUnApplyCPUMfr | POST | /v1/ascm/instance/listUnApplyCP UMfr | ListUnApplyCPUMfr |
| ListUnApplyGPUMfr | POST | /v1/ascm/instance/listUnApplyGP UMfr | ListUnApplyGPUMfr |
| ListUnApplyMachin eType | POST | /v1/ascm/instance/listUnApplyM achineType | ListUnApplyMachineType |
| ListUnApplyInstanc e | POST | /v1/ascm/instance/listUnApplyIn stance | ListUnApplyInstance |

BareMetal Mangement Service

## API overview

The following tables list the API operations that are available for use in Bare Metal Service (BMS). API operations of `BMS version 2022-05-30` use the remote procedure call (RPC) protocol. For more information about signatures, seeRequest signatures. Developers can use the Portable OpenAPI Proxy (POP) gateway to directly call BMS API operations without the need to learn technical details. If the existing methods for calling BMS API operations cannot meet your requirements, send your feedback to us. Before you call an API operation, make sure that an Apsara Stack account is created and an AccessKey pair is created for the account. This way, you can call the API operation by using client tools such as SDKs and the CLI.

**API operations available for use in BMS**

| CheckIPAvailability | POST | /v1/ascm/instance/checkIPAvaila bility | CheckIPAvailability |
|---|---|---|---|
| ReleaseInstance | POST | /v1/ascm/instance/releaseInstan ce | ReleaseInstance |
| StartInstance | POST | /v1/ascm/instance/startInstance | StartInstance |
| StopInstance | POST | /v1/ascm/instance/stopInstance | StopInstance |
| ReStartInstance | POST | url:/v1/ascm/instance/reStartInst ance | ReStartInstance |
| ModifyHostNameIn stance | POST | /v1/ascm/instance/modifyHostNa meInstance | ModifyHostNameInstance |
| DescribeInstance | POST | /v1/ascm/instance/describeInsta nce | DescribeInstance |
| ListImageName | POST | /v1/ascm/image/listImageName | ListImageName |
| ListNetworkSubnet Name | POST | /v1/aso/network/listNetworkSub netName | ListNetworkSubnetName |
| ListOccupiedVPCId | POST | /v1/ascm/instance/listOccupiedV PCId | ListOccupiedVPCId |
| ListHistoryEvent | POST | /v1/event/listHistoryEvent | ListHistoryEvent |
| ListImage | POST | /v1/ascm/image/listImage | ListImage |
| UploadCustomizedI mage | POST | /v1/ascm/image/uploadCustomiz edImage | UploadCustomizedImage |
| DeleteImage | POST | /v1/ascm/image/deleteImage | DeleteImage |
| EnableImage | POST | /v1/ascm/image/enableImage | EnableImage |
| DisableImage | POST | /v1/ascm/image/disableImage | DisableImage |

BareMetal Mangement Service

| ListRelatedInstanc e | POST | /v1/ascm/image/listRelatedInsta nce | ListRelatedInstance |
|---|---|---|---|
| ListMachineType | POST | /v1/ascm/machineType/listMachi neType | ListMachineType |
| HostInstance | POST | /v1/ascm/instance/hostInstance | HostInstance |
| ReHostInstance | POST | /v1/ascm/instance/reHostInstanc e | ReHostInstance |
| DeleteHostedInsta nce | POST | /v1/ascm/instance/deleteHostedI nstance | DeleteHostedInstance |
| ListInstance | POST | /v1/ascm/instance/listInstance | ListInstance |
| ListCgw | POST | /v1/ascm/instance/listCgw | ListCgw |
| ListCgwPort | POST | /v1/ascm/instance/listCgwPort | ListCgwPort |
| DescribeManagedI nstanceQt | POST | /v1/ascm/instance/describeMana gedInstanceQt | DescribeManagedInstanceQt |
| DescribeHostedIns tanceQt | POST | /v1/ascm/instance/describeHost edInstanceQt | DescribeHostedInstanceQt |
| ListHealthScore | POST | /v1/aso/monitor/listHealthScore | ListHealthScore |
| ListWarningSumm ary | POST | /v1/aso/monitor/listWarningSum mary | ListWarningSummary |
| ListWarningDetail | POST | /v1/aso/monitor/listWarningDeta il | ListWarningDetail |
| CreateWarningEve nt | POST | /v1/aso/monitor/createWarningE vent | CreateWarningEvent |

BareMetal Mangement Service BareMetal Mangement Service

## Calling methods

You can call Bare Metal Service (BMS) API operations over HTTP. We recommend that you use aliyunsdkcore to encapsulate API requests. The following example shows how to use aliyunsdkcore to encapsulate API requests.

### Python-SDK

The following are version dependency and parameter configuration requirements of the SDK for Python:
1. aliyun-python-sdk-core>=2.13.8.
2. Specify verify=False for AcsClient.
3. Specify "https" for the protocol_type parameter in CommonRequest.
The following example shows how to call the ListInstance operation by using the SDK for Python, and the API URL is /v1/ascm/instance/listInstance. BareMetal Mangement Service

```bash
# coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest RegionId = "xxxxxx" bmsDomain := "{domain}" usrAccessSecret = "xxxxxx" # One part of the user AccessKey pair. usrAccessKey = "xxxxxx" # The other part of the user AccessKey pair. client = AcsClient(usrAccessKey, usrAccessSecret, RegionId, verify=False) r = CommonRequest()
# To access the service by using the HTTPS method, you need to set the protocol_type pa
rameter to "https".
# r.set_protocol_type("https")
r.set_domain(bmsDomain) r.set_version("2022-05-30") r.set_product("bms")
# The API URL.
r.set_uri_pattern("/v1/ascm/instance/listInstance") r.add_body_params("PageNumber", 1) # Required. r.add_body_params("PageSize", 10) # Required. r.add_body_params("QueryKey", "") # Optional. r.add_body_params("QueryValue", "") # Optional. r.add_body_params("SortType", "asc") # Optional. You can specify "asc" or "desc" for th is parameter. r.add_body_params("SortField", "") # Optional. If you do not specify this parameter, th e query results are sorted in descending order based on the creation time. r.add_body_params("ApplicationGroup", "instance") r.add_body_params("OwnerType", "") # Optional. r.add_body_params("State", "") # Optional. If you do not specify this parameter, the qu ery results are sorted in descending order based on the creation time. r.set_method("POST") resp = client.do_action(r)
```

### Go-SDK

The following are version dependency and parameter configuration requirements of the SDK for Go:
1. Go 1.10 or later.
The following example shows how to call the OpsListMachineType operation by using the SDK for Go, and the API URL is /v1/aso/machineType/listMachineType. BareMetal Mangement Service

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```bash
func main() {
    RegionId := "xxxxxx"
    bmsDomain := "xxxxxx"
    bmsAccessSecret := "xxxxxx"
    bmsAccessKey := "xxxxxx"
    // Create a client instance.
    client, err := sdk.NewClientWithAccessKey(
        RegionId, // Specify your zone ID.
        bmsAccessKey, // Specify your AccessKey ID.
        bmsAccessSecret) // Specify your AccessKey secret.
    if err != nil {
        // Handle exceptions.
        fmt.Println("NewClientWithAccessKey err")
        fmt.Println(err)
    }
    request := requests.NewCommonRequest()
    #request.Headers = map[string]string{
        #    "accessKey": "xxxxxx",
        #    "timestamp": "xxxxxx",
        #    "signature": "xxxxxx"}
    request.Method = "POST"
    request.Product = "bms"
    request.Domain = bmsDomain
    request.Version = "2022-05-30"
    request.Scheme = "http"
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "12"
    request.QueryParams["WithPagination"] = "true"
    request.PathPattern = "/v1/ascm/machineType/listMachineType"
    request.TransToAcsRequest()
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        fmt.Println(err)
        //panic(err)
        //return nil, err
    }
    fmt.Println("***flag***")
    fmt.Println("response")
    fmt.Println(response)
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AccessKey Id | Strin g | Query | No | 2835C***** | A common parameter that can be ignored. |
| ID | Integ er | Query | No | 1 | The synchronization parameter for Resource Management. This parameter can be ignored. |
| PageNum ber | Integ er | Query | No | 1 | The page number. |
| PageSize | Integ er | Query | No | 10 | The number of entries to return on each page. |
| QueryKey | Strin g | Query | No | InstanceAlias | The filter key. Valid values: InstanceAlias HostName |
| QueryValu e | Strin g | Query | No | MyTestInstance | The filter value. |

BareMetal Mangement Service

## API Reference

### Instances

You can call the following API operations to manage instances: ListInstance, DescribeInstance, DescribeTask, ListInstanceOverview, ApplyManagedInstance, ReApplyManagedInstance, ListUnApplyCPUMfr, ListUnApplyGPUMfr, ListUnApplyMachineType, ListUnApplyInstance, StartInstance, StopInstance, ReStartInstance, ReleaseInstance, ModifyHostNameInstance, CheckIPAvailability, ListImageName, and ListOccupiedVPCId.

#### Instance list

Call the ListInstance API to query all bare machine instances and display the results in a paginated list.

**Request header**

This operation uses only common request headers. For more information, see the common parameters document.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nGroup | Strin g | Query | No | instance | The resource type. Valid values: Onboarding a bare machine instance In-band managed stock: ib stock _ Out-of-band managed stock: oob stock _ |
| SortField | Strin g | Query | No | InstanceAlias | The field to sort by. Default value: CreateTime. Valid values: InstanceName CreateTime InstanceAlias |
| SortType | Strin g | Query | No | desc | The sort order. Valid values: asc desc |
| Departme nt | Strin g | Query | No | 1 | The ID of the organization. This parameter can be ignored. |
| OwnerTyp e | Strin g | Query | No | instance | This parameter has the same function as ApplicationGroup and can be ignored. |
| State | Strin g | Query | No | available,manageable,er ror,enroll,rolling | The state of the bare machine instance. |
| DeployTy pe | Strin g | Query | No | bms | The deployment type. If you do not specify this parameter, instances of all deployment types are returned. Valid values: bms ack no clone _ no clone ack _ _ |

BareMetal Mangement Service

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pes | Json | Query | No | bms,ack | The deployment types. You can specify multiple values. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |

BareMetal Mangement Service

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"pageNum": 1, "pageSize": 10,"total": 13, "data":[{ "DeployType": "bms", "Organization": "51", "Description": "", "RunningState": "running", "VPCID": "", "Config": { "Memory": 1, "CPUNumber": 1 }, "Operation": "", "Image": "rhel 7 9 x86 64 _ _ _ _ _ xxxxxx.qcow2", "Gpu": "", "MappingStatus": "Rebooting", "ApplicationGroup" : "resource", "GpuNum": 0, "Monitor": "", "InstanceAlias": "i- xxxxxxxxxx", "NetworkCardNum" : 1, "VPCSubnet": "", "AliYunAssistID": "", "ID": 1, "SN": "xxxxxxxxxx", "ResourceGroup": "60", "RawIP": "xx.xx.xx.xx", "HostName": "h- 21xxxxxx", "Status": "power on", _ "ImageUniqueKey": "i- cmdb4gxxxxxxxxx" , "OS": "RedHat", "IP": "", "CreateTime": "2024-01-11 16:51:27", "MachineType": "xxxxxx", "InstanceName": "i-xxxxxxxx", "DefaultImage": "rhel 7 9 x86 64 _ _ _ _ _ xxxxxxxx.qcow2", "State": "rebooting", "UserId": "1xxxxxxxxxxxxxx", "BMCIP": "xx.xx.xx.xx", "NetworkCardType ": "10G", "AgentID": 6, | The returned data. |

BareMetal Mangement Service

| Parameter | Type | "Tag": "3.xx.xx" Example }]} | Description |
|---|---|---|---|
| status | Integer | 200 | The status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The return status. |
| responseVersi on | String | v1 | Version |

BareMetal Mangement Service

**Examples**

Example request

```
&<Common request parameters>
```

Example of a successful response `JSON` format

```json
{
 "responseVersion":"v1",
 "data":{
  "total":13,
  "data":[
   {
    "DeployType":"bms",
    "Organization":"51",
    "Description":"",
    "RunningState":"running",
    "VPCID":"",
    "Config":{
     "Memory":1,
     "CPUNumber":1
    },
    "Operation":"",
    "Image":"rhel_7_9_x86_64_xxxxxx.qcow2",
    "Gpu":"",
    "MappingStatus":"Rebooting",
    "ApplicationGroup":"resource",
    "GpuNum":0,
    "Monitor":"",
    "InstanceAlias":"i-xxxxxxxxxx",
    "NetworkCardNum":1,
    "VPCSubnet":"",
    "AliYunAssistID":"",
    "ID":1,
    "SN":"xxxxxxxxxx",
    "ResourceGroup":"60",
    "RawIP":"xx.xx.xx.xx",
    "HostName":"h-21xxxxxx",
```

BareMetal Mangement Service ,

```json
    "Status":"power_on",
    "ImageUniqueKey":"i-cmdb4gxxxxxxxxx",
    "OS":"RedHat",
    "IP":"",
    "CreateTime":"2024-01-11 16:51:27",
    "MachineType":"xxxxxx",
    "InstanceName":"i-xxxxxxxx",
    "DefaultImage":"rhel_7_9_x86_64_xxxxxxxx.qcow2",
    "State":"rebooting",
    "UserId":"1xxxxxxxxxxxxxx",
    "BMCIP":"xx.xx.xx.xx",
    "NetworkCardType":"10G",
    "AgentID":6,
    "Tag":"3.xx.xx"
   }
```

`],`

```json
  "pageSize":10,
  "pageNum":1
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested service is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

`XML` format BareMetal Mangement Service

```xml
<responseVersion>v1</responseVersion> <data>
 <total>13</total>
 <data>
  <DeployType>bms</DeployType>
  <Organization>51</Organization>
  <Description  />
  <RunningState>running</RunningState>
  <VPCID  />
  <Config>
   <Memory>1</Memory>
   <CPUNumber>1</CPUNumber>
  </Config>
  <Operation  />
  <Image>rhel_7_9_x86_64_xxxxxx.qcow2</Image>
  <Gpu  />
  <MappingStatus>Rebooting</MappingStatus>
  <ApplicationGroup>resource</ApplicationGroup>
  <GpuNum>0</GpuNum>
  <Monitor  />
  <InstanceAlias>i-xxxxxxxxxx</InstanceAlias>
  <NetworkCardNum>1</NetworkCardNum>
  <VPCSubnet  />
  <AliYunAssistID  />
  <ID>1</ID>
  <SN>xxxxxxxxxx</SN>
  <ResourceGroup>60</ResourceGroup>
  <RawIP>xx.xx.xx.xx</RawIP>
  <HostName>h-21xxxxxx</HostName>
  <Status>power_on</Status>
  <ImageUniqueKey>i-cmdb4gxxxxxxxxx</ImageUniqueKey>
  <OS>RedHat</OS>
  <IP  />
  <CreateTime>2024-01-11 16:51:27</CreateTime>
  <MachineType>xxxxxx</MachineType>
  <InstanceName>i-xxxxxxxx</InstanceName>
  <DefaultImage>rhel_7_9_x86_64_xxxxxxxx.qcow2</DefaultImage>
  <State>rebooting</State>
  <UserId>1xxxxxxxxxxxxxx</UserId>
  <BMCIP>xx.xx.xx.xx</BMCIP>
  <NetworkCardType>10G</NetworkCardType>
  <AgentID>6</AgentID>
  <Tag>3.xx.xx</Tag>
 </data>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
</data> <errorTitle>InternalError</errorTitle> <requestId>*****-*****-*****</requestId> <success>true</success> <errorMessage>The requested service is xxxxx</errorMessage> <errorCode>InternalError</errorCode> <status>200</status>
```

BareMetal Mangement Service

#### ListInstanceOverview

Loads the full overview data of an instance, such as SN, IP address, VpcID, VswID, and AliUid. Request method: POST Request parameters: none

#### ApplyManagedInstance

Creates a bare metal instance in Bare Metal Service (BMS). Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  "StsTokenCallerUid": "xxxxxx",
  "UserName": "xxxxxx",
  "Department": "xxxxxx", # Required.
  "ResourceGroup": "xxxxxx", # Required.
  "RegionId": "xxxxxx", # Required.
  "ZoneId": "xxxxxx", # Required.
  "CPUArch": "x86_64", # Required.
  "SN": "xxxxxx", # Required.
  "MachineTypeName": "mtxxx", # Required.
  "IsUseOriginImage": false,
  "ImageType": "public", # Optional.
  "Image": "xxxxxx", # Optional.
  "HostName": "", # Optional.
  "CPUManufacturer": "xxxxxx", # Optional. You can obtain the data source by calling th
e available architecture API operation. If you specify "all" for this parameter, the qu ery results of all CPU manufacturers are returned.
  "GPUManufacturer": "xxxxxx", # Optional. You can obtain the data source by calling an
available architecture API operation. If you specify "all" for this parameter, the quer y results of all GPU manufacturers are returned.
  "IsSaveDataDisk": true, # Optional.
  "VPCId": "test-vpcId", # Required.
  "VPCSubnet": "test-vpcsubnet", # Required.
  "IP": "xxx.xxx.xxx.xxx", # Optional. Specify an IP address.
  "IsSetPassword": true, # Required.
  "LoginName": "xxxxxx", # Optional. If you select the tgz format for image reinstallat
ion, do not specify this parameter.
  "Password": "xxxxxx", # Optional. If you select the tgz format for image reinstallati
on, do not specify this parameter.
  "InstanceName": "xxxxxx",
  "Description": "",
  "DeployType": "service name",
  "ActivationId": "xxxxxx",
  "ActivationCode": "xxxxxx"
}
```

BareMetal Mangement Service

#### ReApplyManagedInstance

Re-applies for a bare metal instance that fails to be created. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  "ID": id,
  "UserId": "xxxxxx",
  "Organization": "xxxxxx", # Required.
  "ResourceGroup": "xxxxxx", # Required.
  "RegionId": "xxxxxx", # Required.
  "ZoneId": "xxxxxx", # Required.
  "CpuArch": "x86_64", # Required.
  "SN": "xxxxxx", # Required.
  "MachineTypeName": "mt***", # Required.
  "IsUseOriginImage": false, # Required.
  "ImageType": "public", # Optional.
  "Image": "xxxxxx", # Optional.
  "IsSaveDataDisk": true, # Required.
  "VPCId": "vpcId", # Required.
  "VPCSubnet": "vpcsubnet", # Required.
  "IP": "xxx.xxx.xxx.xxx", # Optional. Specify an IP address.
  "IsSetPassword": true, # Required.
  "LoginName": "xxxxxx", # Optional.
  "Password": "xxxxxx", # Optional. If you select the tgz format for image reinstallati
on, do not specify this parameter.
  "HostName": "xxxxxx", # Optional. If you select the tgz format for image reinstallati
on, do not specify this parameter.
  "CPUManufacturer": "xxxxxx", # Optional. You can obtain the data source by calling th
e available architecture API operation. If you specify "all" for this parameter, the qu ery results of all CPU manufacturers are returned.
  "GPUManufacturer": "xxxxxx", # Optional. You can obtain the data source by calling an
available architecture API operation. If you specify "all" for this parameter, the quer y results of all GPU manufacturers are returned. }
```

#### ListUnApplyCPUArch

Queries the architecture of instances that have not been applied for in the resource pool. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

BareMetal Mangement Service

```json
{
  "Region": "xxxxxx", # Required.
  "Zone": "xxxxxx", # Required.
  "DeployType": "service name"
}
```

#### ListUnApplyCPUMfr

Queries the CPU manufacturers of instances that can be applied for in the resource pool. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  "CPUArch": "CPUArch", # Required.
  "Region": "xxxxxx", # Required.
  "Zone": "xxxxxx", # Required.
  "DeployType": "service name"
}
```

#### ListUnApplyGPUMfr

Queries the GPU manufacturers of instances that can be applied for in the resource pool. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  "Region": "xxxxxx", # Required.
  "Zone": "xxxxxx", # Required.
  "CPUArch": "CPUArch", # Required.
  "DeployType": "service name"
}
```

#### ListUnApplyMachineType

Queries the models of instances that can be applied for in the resource pool. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

BareMetal Mangement Service

```json
{
  "CPUArch": "CPUArch", # Required.
  "Region": "xxxxxx", # Required.
  "Zone": "xxxxxx", # Required.
  "CPUManufacturer": "all", # Optional. If you specify "all" for this parameter, the qu
ery results of all CPU manufacturers are returned.
  "GPUManufacturer": "all", # Optional. If you specify "all" for this parameter, the qu
ery results of all GPU manufacturers are returned.
  "DeployType": "service name"
}
```

#### ListUnApplyInstance

Queries the instances that can be applied for in the resource pool. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  "CPUArch": "x86_64", # Required.
  "MachineType": "test-mt", # Required.
  "Region": "xxxxxxxx", # Required.
  "Zone": "xxxxxxxx", # Required.
  "CPUManufacturer": "all", # Optional. If you specify "all" for this parameter, the qu
ery results of all CPU manufacturers are returned.
  "GPUManufacturer": "all", # Optional. If you specify "all" for this parameter, the qu
ery results of all GPU manufacturers are returned.
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

#### CheckIPAvailability

Checks whether the specified IP address is duplicate and available. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "IP": "xxx.xxx.xxx.xxx" # Required.
}
```

#### ReleaseInstance

BareMetal Mangement Service Releases a bare metal instance. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "ID": 1 # Required.
}
```

#### StartInstance

Starts a bare metal instance. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "ID": 1 # Required.
}
```

#### StopInstance

Stops a bare metal instance that is in the Running state. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "ID": 1 # Required.
}
```

#### ReStartInstance

Restarts a bare metal instance that is in the Running state. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

BareMetal Mangement Service

```json
{
  "ID": 1 # Required.
}
```

#### ModifyHostNameInstance

Modifies the hostname of a bare metal instance. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "ID": 1 # Required.
  "HostName": "xxxxxx" # Required.
}
```

#### DescribeInstance

Loads the details of an instance. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "ID": 1 # Required.
}
```

#### ListImageName

Queries the image information when a bare metal instance is created. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "Status": "available", # Optional.
  "Type": "custom", # Required. You can specify this parameter as "public" for public i
mages or "customize" for custom images.
  "PackageType": 'type of the returned package to be returned'. # Required. Valid value
: image, software, or docker. }
```

BareMetal Mangement Service

#### ListNetworkSubnetName

Queries the subnet name when a bare metal instance is created. Request method: POST Request parameters: none

#### ListOccupiedVPCId

Queries a list of virtual private cloud (VPC) IDs that are used by all bare metal instances. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "DeployType": "service name"
}
```

#### ListHistoryEvent

Queries the information about the most recent operation or all operations that have been performed on a resource based on the resource ID. Request method: POST Request parameters: content-type: multipart/form-data; or content-type: application/json;

**Sample requests**

```json
{
  "ResourceId": 1, # Required. Specify the resource ID.
  "ResourceTable": "machine" # Required. Specify the type or source of the resource.
  "StartTime": "2022-07-12", # Optional. Specify this parameter in the 0000-00-00 forma
t. Default value: 0001-01. If you do not specify this parameter, the default value is u sed.
  "EndTime": "2022-07-12", # Optional. Specify this parameter in the 0000-00-00 format.
If you do not specify this parameter, the current time is used.
  "PageNumber": 1 # Required. The type of this parameter is int.
  "PageSize": 50 # Required. The type of this parameter is int. Valid value range: [1,
50]
```

#### ListBmcpInstance

Queries multiple bare metal instances at a time. You can filter and sort bare metal instances in multiple dimensions.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nGroup | Strin g | Query | No | instance | The resource type. Valid values: instance: a resource on the tenant side. resource: a resource in the resource pool. Multiple values are separated with commas (,). |
| DeployTy pe | Strin g | Query | No | bmcp | The deployment type. Valid values: bmcp bmcp no clone _ _ bmcp ack _ bmcp no clone ack _ _ _ bmcp managed _ bmcp managed ack _ _ training Multiple values are separated with commas (,). |

BareMetal Mangement Service This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| State | Strin g | Query | No | available,manageable,er ror,enroll,rolling | The instance status for filtering. Value values: manageable/available : The instance is running. enroll/rolling: The instance is being created. operating: The instance is under O&M. cleaning: The instance is being released. Deleting: The instance is being deleted. rebooting: The instance is being restarted. powering on: The _ instance is being started. shutting down: The _ instance is being stopped. offline: No heartbeat of the instance is detected. error: The instance fails. unknown: The instance status is unknown. Multiple values are separated with commas (,). |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |

BareMetal Mangement Service

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| QueryKey | Strin g | Query | No | InstanceAlias | The filter item. Valid values: InstanceName: the instance ID. InstanceAlias: the instance name. SN RawIP: the classic network IP address. IP: the virtual private cloud (VPC) IP address. BMCIP: the out-of- band IP address. MachineType: the model of the instance. |
| QueryValu e | Strin g | Query | No | MyTestInstance | The content of the filter item. |
| SortField | Strin g | Query | No | InstanceAlias | Specifies sorting of the query results. Default value: CreateTime. Valid values: InstanceName CreateTime InstanceAlias |
| SortType | Strin g | Query | No | desc | Specifies the sorting order of the query results. Valid values: asc desc |

BareMetal Mangement Service

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterAffi liation | Strin g | Query | No | in | Specifies whether an instance is in a cluster. Valid values: in: The instance is in the cluster. out: The instance is outside the cluster. Filtering note: If you specify "resource" for the ApplicationGroup parameter, the ClusterAffiliation parameter will not be used as a filter item. |
| InstanceN ame | Strin g | Query | No | DBServer1 | The instance ID, which is used for resource management synchronization. You can specify multiple instance IDs at a time and separate them with commas (,). If you specify InstanceName for the QueryKey parameter, the intersection of the filter results of that parameter and this parameter is returned. |
| UserId | Strin g | Query | No | agent@ccc-test | The user ID. |
| Disable | Boole an | Query | No | false | Specifies whether to disable an instance. Valid values: false: The instance is enabled. true: The instance is disabled. |

BareMetal Mangement Service

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceN ame | Strin g | Query | No | DBServer1 | The name of an instance. For example, the instance name DBServer1 represents the first database server instance. |
| IpConfig | Json | Query | No | {"type":"white", "ipList":"192.168.2.0/24" } | The source IP addresses of outbound traffic. You can add two to six source IP addresses. You must add at least two source IP addresses for outbound traffic to ensure high availability. We recommend that you add two IP addresses that reside in different zones. You can add up to six source IP addresses. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ModifyInstanceIpConfig

Modifies the IP address configurations of a bare metal instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyInstanceIpConfig &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ID | Long | Query | No | 1 | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### EnableInstance

Enables an instance in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| areMetal Mange | ment Service |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ID | Long | Query | No | 1 | The instance ID. |

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "responseVersion":"1.0",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### DisableInstance

Disables an instance in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "responseVersion":"1.0",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

Queries a list of bare metal instances by specifying multiple filter conditions.

#### ListManageableInstance

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |
| InstanceN ame | Strin g | Query | No | DBServer1 | The name of an instance. For example, the instance name DBServer1 represents the first database server instance. |
| InstanceAl ias | Strin g | Query | No | ProductionDB | The instance alias, another name for easy identification of the instance. |
| SN | Strin g | Query | No | ABC123456 | The serial number, which is a unique identifier of a hardware device or product. |
| BMCIP | Strin g | Query | No | 10.0.0.1 | The description. In this example, the description "10.0.0.1" of the BMCIP parameter indicates the baseboard management controller (BMC) IP address of the server, and this IP address is used for remote management. |

BareMetal Mangement Service

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MachineT ype | Strin g | Query | No | mt-**** | The model of the bare metal instance. If you specify this parameter, the overview data of the current model is queried. If you do not specify this parameter, the overview data of all models is queried. |
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |
| Disable | Boole an | Query | No | False | In programming or logic, if the value of the Disable parameter for a feature or option is False, it indicates that the feature or option is enabled and can be used. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | def456 |
| success | Boolean | true | The status of response. |

BareMetal Mangement Service

**Response parameters**

| BareMetal Mange | ment Service |  | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ApplyBmc pInstance List | Json | Query | No | ["instance001","instance 002","instance003"] | Specifies one or more instance names to which you want to apply Bare Metal Computing Platform (BMCP) configurations. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListManageableInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ApplyBmcpInstance

Performs flexible management and deployment of physical server resources in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | def456 |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ApplyBmc pInstance List | Json | Query | No | instance001,instance00 2,instance003 | Specifies one or more instance names to which you want to apply Bare Metal Computing Platform (BMCP) configurations. Instance IDs are separated with commas (,). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorCode | String | InternalError | The error code. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ReApplyBmcpInstance

Re-applies for a bare metal instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI Reference |  | BareMetal Mangement Servic |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ReApplyBmcpInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ReleaseBmcpInstance

Releases a bare metal instance.

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| BmcpInsta nceNameL ist | Json | Query | No | ["ins1","ins2","ins3"] | Specifies a group of Bare Metal Computing Platform (BMCP) instance names, which are used to identify different instance nodes. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorCode | String | InternalError | The error code. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceN ame | Strin g | Query | No | DBServer1 | The name of an instance. For example, the instance name DBServer1 represents the first database server instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |

BareMetal Mangement Service

```
http(s)://[Endpoint]/?Action=ReleaseBmcpInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### CreateInstanceLvm

Creates a logical volume manager (LVM) for an instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| areMetal Mange | ment Service |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

BareMetal Mangement Service

### Images

You can call the following API operations to manage images: ListImage, UploadCustomizedImage, DeleteImage, EnableImage, DisableImage, and ListRelatedInstance.

#### ListImage

Queries a list of images. You can dynamically specify query conditions to determine whether to paginate the responses of this operation. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "PageNumber": 1, # Required.
  "PageSize": 10, # Required. Valid values: 1 to 50.
  "QueryKey": "", # Optional. Specify the query field. Currently, only Name can be spec
ified.
  "QueryValue": "", # Optional. Specify the query field value. Fuzzy match is
supported. Special characters such as #, &, *, $, ^, and % are filtered out. If only a single special character is entered, all query results are returned after the special c haracter is filtered out.
  "Type": "custom", # Required. You can specify this parameter as "public" for public i
mages, "customize" for custom images, or "eflops" for Eflops dedicated images.
  "Department": "1", # Required. Fixed value: 1.
  "PackageType": 'type of the package to be returned'. # Required. Valid value: image o
r software. If you specify "image" for this parameter, an image package is returned. If you specify "software" for this parameter, a software package is returned. }
```

#### UploadCustomizedImage

Uploads an on-premises image file to an Elastic Compute Service (ECS) instance. The uploaded image file can be used as a custom image for later installations. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

BareMetal Mangement Service

```json
{
  "Name": "image name", # Required.
  "Size": 'image size, unit: byte', # Required.
  "URL": 'image IP address', # Required.
  "CheckSum": 'image md5 value', # Optional.
  "DiskFormat": 'image format, qcow2', # Required. The value is the substring after the
last dot (.) in the file name.
  "OsArch": 'system architecture, which may be x86 or ARM-based architecture', # Requir
ed.
  "Type": 'image type, which is used to distinguish public images and custom images. To
return a software package, specify this parameter to eflops', # Required.
  "Platform": 'platform', # Required. For more information about the platform range, se
e the following parameters.
  "ZoneId": 'zone', # Required.
  "RegionId": 'region', # Required.
  "Organization": 'organization', # Required. To return a software package, you can spe
cify this parameter as 1.
  "Description": 'description', # Optional.
  "Version": 'software package version', # Optional.
  "KernelVersion": 'image kernel version', # Optional. Ignore this parameter if you spe
cify "software" for the PackageType parameter.
  "PackageType": 'type of the package to be returned', # Optional. Valid values: image
and software. Default value: image. If you do not specify this parameter, the default v alue is used. If you specify "software" for this parameter, a software package is retur ned.
  "ComponentType": 'component type' # Optional. This parameter is required when a softw
are package is uploaded. Tentatively, the following component types are supported.Cloud-native Component: AppStack; Acceleration Suite: AcceleratorKit; Docker: docker. }
```

#### DeleteImage

Deletes a custom image. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "ID": "image ID", # Required.
  "Name": "image name", # Required.
}
```

#### EnableImage

Enables an image. BareMetal Mangement Service Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "ID":1 # Specify the image ID. Required.
}
```

#### DisableImage

Disables an image. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "ID":1 # Specify the image ID. Required.
}
```

#### ListRelatedInstance

Queries all bare metal instances that use an image by the image name. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "Name":1 # Specify the image name. Required.
}
```

### Models

You can call the ListMachineType operation to manage models.

#### ListMachineType

Queries a list of models. You can also dynamically specify query conditions to determine whether to paginate the responses of this operation. Query conditions include the data about model specifications, such as CPU utilization, memory usage, and disk usage. Request method: POST Request parameters: content-type: multipart/form-data; BareMetal Mangement Service

**Sample requests**

```json
{
  "MachineType": "test1", # Optional. Specify the model name.
  "CPUArch": "x86-32", # Optional. Specify the CPU architecture.
  "DiskType": "xxxxx", # Optional. Specify the disk type.
  "UnitNum": 1, # Optional. Specify the number of units.
  "Manufacturer": "xxxxx", # Optional. Specify the manufacturer.
  "CPUManufacturer": "xxxxx", # Optional. Specify the CPU manufacturer.
  "GPUManufacturer": "xxxxx", # Optional. Specify the GPU manufacturer.
  "WithPagination": "true or false", # Required. Specify whether to paginate the return
ed responses. Valid values: true and false. Default value: true. If you specify "false" for this parameter, all data is returned.
  "PageNumber": 1. Default value: 1.
  "PageSize":10. Default value: 50.
  "DeployType": "service name"
}
```

### Hosted instances

You can call the following API operations to manage hosted instances: HostInstance, ReHostInstance, DeleteHostedInstance, and ListInstance.

#### HostInstance

Hosts an in-band or out-of-band instance. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

BareMetal Mangement Service

```json
{
  # Fixed value.
  "OsUpdate": "true". # Specify whether to retain the data disk.
  # Fixed value. Specify a proper value for the specific instance.
  "ApplicationGroup": "ib_stock/oob_stock", # Specify "ib_stock" for this parameter to
host in-band instances, and "oob_stock" to host out-of-band instances.
  # Required.
  "Organization": "xxxxx", # Required.
  "ResourceGroup": "xxxxx", # Required.
  "RegionId": "xxxxx", # Required.
  "ZoneId": "xxxxx", # Required.
  "SN": "xxxxx", # Required. The SN must be unique.
  "InstanceName": "xxxxx", # Required. Specify a hostname.
  "IDC": "xxxxx", # Required. Specify a data center.
  "Room": "xxxxx", # Required. Specify a room.
  "Rack": "xxxxx", # Required. Specify a rack.
  "RackUnit": "xxxxx", # Required. Specify the rack unit number.
  # Required for in-band instances and not required for out-of-band instances.
  "ASWID": "xxxxx". # Specify a hybrid switch (HSW) gateway.
  "CGWPorts": "xxxxx". # Specify the HSW port.
  "VpcSubnet": "xxxxx",#VswitchId
  "VpcId": "xxxxx",    #vpc
  "IP": "ip". # Optional. Specify an IP address.
  "SSHUser": "xxxxx", # Specify a username.
  "SSHPwd": "xxxxx", # Specify a password.
  "Subnet": "",
  "RawIP": ""
  # Required for out-of-band instances and not required for in-band instances.
  "BMCIP": "xxxxx",
  "BMCUser": "xxxxx",
  "BMCPassword": "xxxxx",
  # Optional.
  "Description": "",
}
```

#### ReHostInstance

Rehosts an in-band or out-of-band instance. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

BareMetal Mangement Service

```json
{
  "ID": id,
  # Fixed value.
  "OsUpdate": "true". # Specify whether to retain the data disk.
  "ApplicationGroup": "ib_stock/oob_stock", # Specify "ib_stock" for this parameter to
host in-band instances, and "oob_stock" to host out-of-band instances.
  # Required.
  "Organization": "xxxxx",
  "ResourceGroup": "xxxxx",
  "RegionId": "xxxxx",
  "ZoneId": "xxxxx",
  "SN": "xxxxx", # The SN must be unique.
  "InstanceName": "xxxxx", # Specify a hostname.
  "IDC": "xxxxx", # Specify a data center.
  "Room": "xxxxx", # Specify a room.
  "Rack": "xxxxx", # Specify a rack.
  "RackUnit": "xxxxx", # Specify the rack unit number.
  # Required for in-band instances and not required for out-of-band instances.
  "ASWID": "xxxxx". # Specify a hybrid switch (HSW) gateway.
  "CGWPorts": "xxxxx". # Specify the HSW port.
  "VpcSubnet": "xxxxx",#VswitchId
  "VpcId": "xxxxx",    #vpc
  "IP": "ip". # Optional. Specify an IP address.
  "SSHUser": "xxxxx", # Specify a username.
  "SSHPwd": "xxxxx", # Specify a password.
  "Subnet": "",
  "RawIP": ""
  # Required for out-of-band instances and not required for in-band instances.
  "BMCIP": "xxx.xxx.xxx.xxx",
  "BMCUser": "xxxxx",
  "BMCPassword": "xxxxx",
  # Optional.
  "Description": "",
}
```

#### DeleteHostedInstance

Deletes an in-band or out-of-band hosted instance. Request method: POST Request parameters: content-type: multipart/form-data;

**Sample requests**

```json
{
  "ID": 1 # Required.
}
```

#### ListInstance

BareMetal Mangement Service Queries a list of in-band or out-of-band hosted instances. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  "PageNumber": 1,
  "PageSize": 10,
  "QueryKey": "InstanceName",
  "QueryValue": "xxxxxxxx",
  "SortField": "", # If you do not specify this parameter, the query results are sorted
in descending order based on the creation time.
  "SortType": "asc", # You can specify this parameter as asc or desc. Default value: de
sc.
  "ApplicationGroup": "ib_stoc/oob_stock/instance"
}
```

### Gateway

You can call the following API operations to manage gateway: ListCgw and ListCgwPort.

#### ListCgw

Queries a list of compute gateways (CGWs). Request method: POST Request parameters: content-type: application/json;

**Sample requests**

```json
{
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

#### ListCgwPort

Queries a list of compute gateway (CGW) ports. Request method: POST Request parameters: content-type: application/json;

**Sample requests**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |

BareMetal Mangement Service

```json
{
  "CgwName": "" # Required.
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

#### ListBorder

Queries a list of private line gateways that can be used to create private line resources.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### BindVswitchToBorder

Binds a vSwitch to a gateway. This operation is suitable for network configuration scenarios in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| BorderNa me1 | Strin g | Query | No | HSW-25GE-DA-C2-5- G02-1-1.**** | The name of private line gateway 1. |
| BorderNa me2 | Strin g | Query | No | HSW-25GE-DA-C2-5- G02-1-2.**** | The name of private line gateway 2. |
| VswitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
| VpcId | Strin g | Query | No | vpc | The virtual private cloud (VPC) ID. |
| RegionId | Strin g | Query | No | us | The region ID. |
| ZoneId | Strin g | Query | No | ZoneId | The zone ID. |
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |

BareMetal Mangement Service

**Response parameters**

| Developer Guide·A | PI Reference |  | BareMetal Mangement Servic |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=BindVswitchToBorder &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### UnBindVswitchToBorder

Unbinds a vSwitch from a gateway.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| B | areMetal Ma | ngement | Service |  | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VswitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UnBindVswitchToBorder &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |
| BorderNa me1 | Strin g | Query | No | HSW-25GE-DA-C2-5- G02-1-1.**** | The name of private line gateway 1. |
| BorderNa me2 | Strin g | Query | No | HSW-25GE-DA-C2-5- G02-1-2.**** | The name of private line gateway 2. |
| VswitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
| VpcId | Strin g | Query | No | vpc- 4uftp58qtzn7t663x**** | The virtual private cloud (VPC) ID. |
| RegionId | Strin g | Query | No | us | The region ID. |
| ZoneId | Strin g | Query | No | ZoneId | The zone ID. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ReBindVswitchToBorder

Rebinds a vSwitch to a gateway.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ReBindVswitchToBorder &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |
| VswitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ReUnbindVswitchToBorder

Unbinds a vSwitch from a gateway again.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| B | areMetal Mange | ment Service |  | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ReUnbindVswitchToBorder &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ListVswitchBindToBorder

Queries the binding relationship between a vSwitch and a gateway.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |
| BorderNa me1 | Strin g | Query | No | HSW-25GE-DA-C2-5- G02-1-1.**** | The name of private line gateway 1. |
| BorderNa me2 | Strin g | Query | No | HSW-25GE-DA-C2-5- G02-1-2.**** | The name of private line gateway 2. |
| VpcId | Strin g | Query | No | vpc | The virtual private cloud (VPC) ID. |
| VswitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The vSwitch ID. |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |
| RegionId | Strin g | Query | No | us | The region ID. |
| ZoneId | Strin g | Query | No | ZoneId | The zone ID. |
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource set. |
| UniqueKe y | Strin g | Query | No | 9876543210 | The unique key of a project. In project management software, each project is assigned a unique key, such as ProjectX, to help track and manage its progress and resources. |

BareMetal Mangement Service

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListVswitchBindToBorder &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterArc hType | Strin g | Query | No | standard | The type of the cluster. You can specify "standard" or "managed" for this parameter. The value in the example is for reference only. Valid values: standard: indicates an intelligent computing high- bandwidth networking instance. managed: indicates an intelligent computing managed instance. |
| ClusterId | Strin g | Query | No | 5b2b4ab4-efbc-4a81- 9c45-xxxxxxxxxxxxx | The ID of the cluster. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ListNetworkTopology

Queries the network topology in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SNList | Json | Query | No | ["SN001", "SN002", "SN003"] | A list of multiple serial numbers, typically a unique collection of serial numbers that are used to identify devices, products, or other project entities. |
| QueryPara ms | Json | Query | No | Custom | The query parameters. |
| IP | Strin g | Query | No | 192.168.1.1 | The IP address. |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |

BareMetal Mangement Service

**Response parameters**

| Developer Guide·A | PI Reference |  | BareMetal Mangement Servic |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkTopology &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### Security groups

#### CreateSecurityGroup

Creates a security group in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| B | areMetal Ma | ngement | Service |  | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Resource Group | Strin g | Query | No | MyResources | A |
| RegionId | Strin g | Query | No | us | west |
| Name | Strin g | Query | No | Bob | The instance name. Ignore this parameter for now. It will be supported in later versions. |
| VpcId | Strin g | Query | No | vpc | abcde12345 |
| Type | Strin g | Query | No | Image | The resource type. In this example, the resource is an Amazon Elastic Compute Cloud (EC2) instance, which provides compute services in the cloud. |
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |
| Descriptio n | Strin g | Query | No | Web server in the production environment | The descriptive information. In this example, high hardware temperature of a device may cause performance degradation of or damage to the device. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |

**Response parameters**

|  | Developer Guide·A | PI Reference |  | BareMetal Mangement Servic | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateSecurityGroup &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### DeleteSecurityGroup

Deletes a security group by specifying its ID.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSecurityGroup &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| Name | Strin g | Query | No | Bob | The instance name. Ignore this parameter for now. It will be supported in later versions. |
| Descriptio n | Strin g | Query | No | Description | The description of the security group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ModifySecurityGroup

Modifies security group configurations in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySecurityGroup &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| Direction | Strin g | Query | No | in | The network traffic direction. Valid values: in and out. |
| AccessPoli cy | Strin g | Query | No | ACCEPT | The access permissions specified in the security group rule. |
| IpProtocol | Strin g | Query | No | tcp | The IP protocol. Valid values: tcp, udp, icmp, or all of them. |
| PortRange | Strin g | Query | No | 22/22 | The port range. Valid values: 0 to 65535. |
| Priority | Integ er | Query | No | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| IpVersion | Strin g | Query | No | ipv4 | The version of IP addresses specified in the access control policy. Valid value: IPv4 (default) |
| CidrIp | Strin g | Query | No | 47.100.XX.XX/16 | The range of the source addresses that can access the Virtual Network Computing (VNC) service. You can use this parameter to specify the security group rule. |

BareMetal Mangement Service

#### AddSecurityGroupRule

Adds a rule for a security group in Bare Metal Service (BMS) to control network traffic.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RelatedGr oupId | Strin g | Query | No | sg-bp197668l6iupljy**** | The authorized security group ID. |
| Descriptio n | Strin g | Query | No | Description | The descriptive information. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddSecurityGroupRule &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| SgrId | Strin g | Query | No | sgr-12345678**** | The ID of the security group rule. |
| Direction | Strin g | Query | No | in | The network traffic direction. Valid values: in and out. |
| AccessPoli cy | Strin g | Query | No | DROP | The access permissions specified in the security group rule. |
| IpProtocol | Strin g | Query | No | tcp | The IP protocol. Valid values: tcp, udp, icmp, or all of them. |
| PortRange | Strin g | Query | No | 22/22 | The port range. Valid values: 0 to 65535. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ModifySecurityGroupRule

Flexibly adjusts the configurations of security group rules in Bare Metal Service (BMS) to meet different network access control requirements.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| areMetal Ma | ngement | Service |  | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Priority | Integ er | Query | No | 1 | The priority of the line. A value of 1 indicates the highest priority. A larger value indicates a lower priority. |
| IpVersion | Strin g | Query | No | ipv4 | The IP version used in the access control policy. Valid value: IPv4 (default) |
| CidrIp | Strin g | Query | No | 47.100.XX.XX/16 | The range of the source IP addresses that can access the Virtual Network Computing (VNC) service. You can use this parameter to specify the security group rule. |
| RelatedGr oupId | Strin g | Query | No | sg-bp12345678**** | The authorized security group ID. |
| Descriptio n | Strin g | Query | No | Description | The description of the security group specifications. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |

**Response parameters**

|  | Developer Guide·A | PI Reference |  | BareMetal Mangement Servic | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySecurityGroupRule &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ListSecurityGroupInstance

Queries a list of bare metal instances that are associated with a security group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| SN | Strin g | Query | No | ABC123456 | The serial number, which is a unique identifier of a hardware device or product. |
| InstanceN ame | Strin g | Query | No | DBServer1 | The name of an instance. For example, the instance name DBServer1 represents the first database server instance. |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

BareMetal Mangement Service

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListSecurityGroupInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ListSecurityGroup

Queries a list of security groups in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource set. |
| RegionId | Strin g | Query | No | us | The region ID. |
| Name | Strin g | Query | No | Bob | The instance name. Ignore this parameter for now. It will be supported in later versions. |
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| VpcId | Strin g | Query | No | vpc- 4uftp58qtzn7t663x**** | The virtual private cloud (VPC) ID. |
| Type | Strin g | Query | No | Image | The resource type. In this example, the resource is an Amazon Elastic Compute Cloud (EC2) instance, which provides compute services in the cloud. |
| DeployTy pe | Strin g | Query | No | bms | The deployment type. |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |

BareMetal Mangement Service

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| Direction | Strin g | Query | No | in | The network traffic direction. Valid values: in and out. |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ListSecurityGroupRule

Queries a list of security group rules.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Developer Guide·A | PI Reference |  | BareMetal Mangement Servic |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListSecurityGroupRule &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| InstanceN ameList | Json | Query | No | ["name1","name2"] | The instance names. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

#### AddSecurityGroupInstance

Adds a bare metal instance to a security group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| SgrId | Strin g | Query | No | sgr-**** | The ID of the security group rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddSecurityGroupInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### DeleteSecurityGroupRule

Deletes a security group rule.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| B | areMetal Mange | ment Service |  | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSecurityGroupRule &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| SgId | Strin g | Query | No | sg-bp197668l6iupljy**** | The security group ID. |
| InstanceN ameList | Json | Query | No | ["name1","name2"] | The instance names. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### DeleteSecurityGroupInstance

Deletes a bare metal instance from a specified security group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| B | areMetal Mange | ment Service |  | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSecurityGroupInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### Overview

You can call the following API operations to manage overview: DescribeManagedInstanceQt and DescribeManagedInstanceQt.

#### DescribeManagedInstanceQt

Queries the total number of managed instances. BareMetal Mangement Service url:/v1/ascm/instance/describeManagedInstanceQt Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "RegionId": "region" # Required.
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

#### DescribeHostedInstanceQt

Queries the total number of hosted instances. url:/v1/ascm/instance/describeHostedInstanceQt Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

### Alerts

You can call the following API operations to manage alerts: ListHealthScore, ListWarningSummary, ListWarningDetail, and CreateWarningEvent.

#### ListHealthScore

Queries the service health check score. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "ApplicationGroup": "application group" # Required.
  "Organization": "organization" # Required.
  "Organizations": "" # Required.
  "ResourceGroup": "resource set" # Optional.
  "RegionId": "region" # Required.
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

BareMetal Mangement Service

#### ListWarningSummary

Queries the total number of unhandled alerts. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "ApplicationGroup": "application group" # Required.
  "Organization": "organization" # Required.
  "Organizations": "" # Required.
  "ResourceGroup": "resource set" # Optional.
  "RegionId": "region" # Required.
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

#### ListWarningDetail

Queries a list of alerts. Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "pageNum": "1". # Required.
  "pageSize": "10". # Required.
  "ApplicationGroup": "resource set". # Required.
  "WarningType": "alert type". # Optional.
  "WarningLevel": "alert level" # Optional.
  "WarningCount": "number of alerts" # Optional.
  "WarningState": "handling status of alerts" # Optional. The values '', '0' and '1' in
dicate All, Unhandled, and Handled statuses, respectively.
  "IP": "" # Optional.
  "SN": "" # Optional.
  "StartTime": "" # Optional.
  "EndTime": "" # Optional.
  "Organizations": "" # Required.
  // Specify the service to which the resource belongs.
  "DeployType": "service name"
}
```

#### CreateWarningEvent

Queries a list of new alert events.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | us | The region ID. |
| InstanceN ame | Strin g | Query | No | DBServer1 | The name of an instance. For example, the instance name DBServer1 represents the first database server instance. |

BareMetal Mangement Service Request method: POST Request parameters: content-type: multipart/json;

**Sample requests**

```json
{
  "WarningID": "" # Required.
  "HandleMethod": "" # Required.
  "WarningState": "" # Required.
  "Description": "" # Required.
  "ClosedReason": "" # Required.
  "ClosedUser": "" # Required.
  "Organizations": "" # Required.
}
```

### Cloud Assistant

#### RunCommand

Runs custom commands on bare metal servers. This operation is suitable for automated O&M scenarios.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| areMetal Ma | ngement | Service |  | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | The command content. TDhees ccormipmtaiondn content can be plaintext or |
| Command Content | Strin g | Query | No | ZWNobyAxMjM= | Base64-encoded. Note: If you want to retain the command, make sure that the size of the Base64-encoded command content does not exceed 18 KB. If you do not want to retain the command, make sure that the size of the Base64-encoded command content does not exceed 24 KB. You can set the KeepCommand parameter to specify whether to retain the command. If the command content is Base64-encoded, you must set the ContentEncoding parameter to Base64. If you set EnableParameter to true, the custom parameter feature is enabled for the command content, and you can configure custom parameters based on the following rules: Define custom parameters in the {{}} format. Within {{}}, the spaces and line feeds before and after the parameter names are ignored. You can specify up to 20 custom parameters. The name of a custom parameter can contain only letters, digits, underscores ( ), _ and hyphens (-). The name is case- insensitive. The name of a custom parameter cannot exceed 64 bytes in length. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Timeout | Long | Query | No | 60 | The timeout period of the change process. Unit: seconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
&<Common request parameters>
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | us | The region ID. |
| InstanceN ame | Strin g | Query | No | DBServer1 | The name of an instance. For example, the instance name DBServer1 represents the first database server instance. |
| InvokeId | Strin g | Query | No | t- 7d2a745b412b4601b2d 47f6a768d3*** | The ID of the command execution task. You can call the DescribeInvocations operation to query the IDs of all command execution tasks. |

|  |  | DescribeInvocations |
|---|---|---|
| a768d3*** |  |  |

BareMetal Mangement Service Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### DescribeInvocationResults

Queries the command execution results of Cloud Assistant.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInvocationResults &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | No | Bob | The instance name. Ignore this parameter for now. It will be supported in later versions. |
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource set. |
| RegionId | Strin g | Query | No | us | The region ID. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### Key pairs

#### CreateKeyPair

Creates a Secure Shell (SSH) key pair for secure login to a bare metal server.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PublicKey | Strin g | Query | No | c3NoLWVkMjU1MTkgQU FBQUMzTnphQzFsWkRJM U5URTVBQUFBSUhVcjY4 UENFYWFzZjFYRVpNYTV sMlNBQytHV3FpeXVsRV pndkV4dmlPM28gcm9vd EA5NjBkMmNhOTcwYjU = | The public key. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | Strin g | Query | No | test-KeyPairName | The name of the key pair. The name must be 2 to 128 characters in length and can contain digits, letters, colons (:), underscores ( ), periods _ (.), and hyphens (-). |
| PageNum ber | Integ er | Query | No | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |

BareMetal Mangement Service `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ListKeyPair

Queries a list of key pairs in Bare Metal Service (BMS) to manage them. This operation is suitable for scenarios where you want to manage and retrieve multiple key pairs at a time.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairFin gerPrint | Strin g | Query | No | ABC1234567 | The fingerprint of the key pair. The message- digest algorithm 5 (MD5) is used based on the public key fingerprint format defined in RFC 4716. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | Strin g | Query | No | test-KeyPairName | The name of the key pair. The name must be 2 to 128 characters in length and can contain digits, letters, colons (:), underscores ( ), periods _ (.), and hyphens (-). |
| MachineS NList | Json | Query | No | ["SN1","SN2"] | The machine SNs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### ConfigKeyPair

Configures a key pair in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

|  | Developer Guide·A | PI Reference |  | BareMetal Mangement Servic | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

Unbinds a key pair from a specified bare metal server.

#### UnbindKeyPair

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | Strin g | Query | No | test-KeyPairName | The name of the key pair. The name must be 2 to 128 characters in length and can contain digits, letters, colons (:), underscores ( ), periods _ (.), and hyphens (-). |
| MachineS NList | Json | Query | No | ** | The machine SNs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| KeyPairNa me | Strin g | Query | No | test-KeyPairName | The name of the key pair. The name must be 2 to 128 characters in length and can contain digits, letters, colons (:), underscores ( ), periods _ (.), and hyphens (-). |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

#### DeleteKeyPair

Deletes a key pair.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | us | west |
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### Tasks

#### CreateTask

Creates a task in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| areMetal Mange | ment Service |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

Queries a list of tasks in Bare Metal Service (BMS).

#### ListTasks

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UID | Strin g | Query | No | 1133166938931507 | UID |
| TaskName | Strin g | Query | No | task-name | The task name. |
| Status | Strin g | Query | No | Active | The status of request. The example indicates that something or a request was rejected or not accepted. |
| AckCluste rID | Strin g | Query | No | cef51d60a6778415ab3a 8026c24***** | The ID of the cluster. |
| CreateTim e | Strin g | Query | No | 1607436917 | The time when the task was created. |
| EndTime | Strin g | Query | No | 2022 | The end time of the task. |
| PageNum ber | Integ er | Query | Yes | 99 | The page number, which is part of pagination configurations. |
| PageSize | Integ er | Query | Yes | 10 | The number of entries per page, which is part of pagination configurations. |
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Group | Strin g | Query | No | MyResources | The resource set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |

BareMetal Mangement Service

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| B | areMetal Mange | ment Service |  | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
&PageNumber=99 &PageSize=10 &<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UID | Strin g | Query | Yes | 1133166938931507 | UID |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

#### DescribeTask

Queries the details of a task in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| areMetal Mange | ment Service |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

**Examples**

Sample requests

```
&UID=1133166938931507 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

#### GetResult

Queries the execution results of a task in Bare Metal Service (BMS).

**Request headers**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UID | Strin g | Query | Yes | 1133166938931507 | UID |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

**Examples**

Sample requests

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Groups | Strin g | Query | No | 23 | The ID of the resource set. |

BareMetal Mangement Service

```
&UID=1133166938931507 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

### Diagnosis

#### GetDiagnoseItem

Queries the information about a diagnostic item in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DiagnoseT ype | Strin g | Query | No | 10 | The type of diagnosis. This parameter indicates a comorbidity diagnosis, where two or more unrelated diseases exist. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestID | String | *****-*****-***** | The request ID. |
| ExecuteStatus | Integer | success | The execution state of the query. success : The query is executed successfully. fail : The query fails. |
| Message | String | You do not have the permissions to access this file. | The detailed error message that is associated with the errorTitle parameter. This message explains why you do not have the permissions and how to resolve the issue. |
| Code | String | ERROR | 404 |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Groups | Strin g | Query | No | 23 | The ID of the resource set. |
| DiagnoseI d | Strin g | Query | No | vpndgn- uf6kuxbe3iv028k3s**** | The ID of the diagnostic task. When you call the DiagnoseVpnGateway operation, the system returns a corresponding ID of the diagnostic task. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestID | String | *****-*****-***** | The request ID. |
| ExecuteStatus | Integer | success | The execution state of the query. success : The query is executed successfully. fail : The query fails. |

BareMetal Mangement Service

```json
{
 "RequestID":"*****-*****-*****",
 "Message":"You do not have the permissions to access this file",
 "data":{
  "data":"xxxxxx Success!"
 },
 "ExecuteStatus":"",
 "Code":"ERROR"
}
```

#### GetDiagnoseStatusById

Queries the current status of a diagnostic task based on the task ID.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Message | String | You do not have the permissions to access this file. | The detailed error message that is associated with the errorTitle parameter. This message explains why you do not have the permissions and how to resolve the issue. |
| Code | String | ERROR | 404 |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | No | us | west |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetDiagnoseStatusById &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestID":"*****-*****-*****",
 "Message":"You do not have the permissions to access this file",
 "data":{
  "data":"xxxxxx Success!"
 },
 "ExecuteStatus":"",
 "Code":"ERROR"
}
```

#### GetDiagnoseDetail

Queries the details of a specific diagnostic task in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| B | areMetal Ma | ngement | Service |  | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Groups | Strin g | Query | No | 23 | The ID of the resource set. |
| DiagnoseI D | Strin g | Query | No | vpndgn- uf6kuxbe3iv028k3s**** | The ID of the diagnostic task. When you call the DiagnoseVpnGateway operation, the system returns a corresponding ID of the diagnostic task. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |
| PageNum | Integ er | Query | No | 1 | The page number, which is part of pagination configurations. The example indicates that the first page of the result set is requested. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestID | String | *****-*****-***** | The request ID. |
| ExecuteStatus | Integer | success | The execution state of the query. success : The query is executed successfully. fail : The query fails. |
| Message | String | You do not have the permissions to access this file. | The detailed error message that is associated with the errorTitle parameter. This message explains why you do not have the permissions and how to resolve the issue. |
| Code | String | ERROR | 404 |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Groups | Strin g | Query | No | 23 | The ID of the resource set. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestID":"*****-*****-*****",
 "Message":"You do not have the permissions to access this file",
 "data":{
  "data":"xxxxxx Success!"
 },
 "ExecuteStatus":"",
 "Code":"ERROR"
}
```

#### QueryDiagnose

Queries diagnostic records in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DiagnoseI D | Strin g | Query | No | vpndgn- uf6kuxbe3iv028k3s**** | The ID of the diagnostic task. When you call the DiagnoseVpnGateway operation, the system returns a corresponding ID of the diagnostic task. |
| Diagnose Name | Strin g | Query | No | RouteEntryConflict | The diagnostic item. Valid values: RouteEntryConflic t : route conflicts. VpnRouteQuota : the quota of destination-based routes for the VPN gateway. VpnIPsecQuota : the quota of IPsec- VPN connections for the VPN gateway. VpnPbrRouteQuot a : the quota of policy-based routes for the VPN gateway. VcoConfigConsisten cy : the consistency of the IPsec-VPN connection. VcoUserInternetIpC onnectivity : Internet connectivity of the customer gateway. VcoPrivateConnecti vity : private network connectivity. For more information about the diagnostic items, see Background information about quick diagnostics. |
| Status | Strin g | Query | No | Active | The status of request. The example indicates that something or a request was rejected or not accepted. |

BareMetal Mangement Service

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| StartTime | Strin g | Query | No | 2022 | The start time of the query. The value is a UNIX timestamp. Unit: seconds. This UNIX timestamp must indicate a point in time that is accurate to the minute. |
| EndTime | Strin g | Query | No | 2022 | The end time of the query. |
| DiagnoseT ype | Strin g | Query | No | 08 | The type of the diagnostic task. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |
| PageNum | Integ er | Query | No | 1 | The page number, which is part of pagination configurations. The example indicates that the first page of the result set is requested. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestID | String | *****-*****-***** | The request ID. |
| ExecuteStatus | Integer | success | The execution state of the query. success : The query is executed successfully. fail : The query fails. |
| Message | String | You do not have the permissions to access this file. | The detailed error message that is associated with the errorTitle parameter. This message explains why you do not have the permissions and how to resolve the issue. |

BareMetal Mangement Service

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Groups | Strin g | Query | No | 23 | The ID of the resource set. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestID":"*****-*****-*****",
 "Message":"You do not have the permissions to access this file",
 "data":{
  "data":"xxxxxx Success!"
 },
 "ExecuteStatus":"",
 "Code":"ERROR"
}
```

#### StartDiagnose

Starts a diagnostic task in Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DiagnoseI D | Strin g | Query | No | vpndgn- uf6kuxbe3iv028k3s**** | The ID of the diagnostic task. When you call the DiagnoseVpnGateway operation, the system returns a corresponding ID of the diagnostic task. |
| Diagnose Name | Strin g | Query | No | RouteEntryConflict | The diagnostic item. Valid values: RouteEntryConflic t : route conflicts. VpnRouteQuota : the quota of destination-based routes for the VPN gateway. VpnIPsecQuota : the quota of IPsec- VPN connections for the VPN gateway. VpnPbrRouteQuot a : the quota of policy-based routes for the VPN gateway. VcoConfigConsisten cy : the consistency of the IPsec-VPN connection. VcoUserInternetIpC onnectivity : Internet connectivity of the customer gateway. VcoPrivateConnecti vity : private network connectivity. For more information about the diagnostic items, see Background information about quick diagnostics. |
| DiagnoseI tem | Strin g | Query | No | MRI | The information about the diagnostic items. |
| Cluster | Strin g | Query | No | slbCluster-A-20231203- 005b | The cluster name. |

BareMetal Mangement Service

| B | areMetal Ma | ngement | Service |  | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DiagnoseT ype | Strin g | Query | No | 08 | The type of the diagnostic task. The value in the example indicates other types of diagnostic tasks and is used in special cases or for unclassified diagnostic tasks. |
| PageSize | Strin g | Query | No | 10 | The number of entries per page, which is part of pagination configurations. |
| PageNum | Strin g | Query | No | 1 | The page number, which is part of pagination configurations. The example indicates that the first page of the result set is requested. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestID | String | *****-*****-***** | The request ID. |
| ExecuteStatus | Integer | success | The execution state of the query. success : The query is executed successfully. fail : The query fails. |
| Message | String | You do not have the permissions to access this file. | The detailed error message that is associated with the errorTitle parameter. This message explains why you do not have the permissions and how to resolve the issue. |
| Code | String | ERROR | 404 |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

**Response parameters**

**Examples**

Sample requests

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | online | The returned HTTP or HTTPS status code. Valid values: offline: BMS is not deployed. online: BMS is deployed. |
| requestId | String | *****-*****-***** | The request ID. |

BareMetal Mangement Service

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestID":"*****-*****-*****",
 "Message":"You do not have the permissions to access this file",
 "data":{
  "data":"xxxxxx Success!"
 },
 "ExecuteStatus":"",
 "Code":"ERROR"
}
```

### DescribeServiceStatus

Queries the status of Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Response parameters**

| areMetal Mange | ment Service |  | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AckCluste rID | Strin g | Query | Yes | cef51d60a6778415ab3a 8026c24***** | The cluster ID. |
| ResourceT ype | Strin g | Query | No | instance | The type of the resource. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeServiceStatus
```

Sample success responses `JSON` format

```json
{
 "responseVersion":"1.0",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### QueryTotalAvailableResource

Queries the total amount of all available resources in a Container Service for Kubernetes (ACK) cluster.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Response parameters**

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=QueryTotalAvailableResource &AckClusterID=cef51d60a6778415ab3a8026c24***** &<Common request parameters>
```

Sample success responses `JSON` format

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

### ListCluster

Queries a list of Bare Metal Service (BMS) clusters.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Developer Guide·A | PI Reference |  | BareMetal Mangement Servic |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UID | Strin g | Query | Yes | 1133166938931507 | UID |

**Examples**

Sample requests Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### GetBaseline

Queries the performance baseline data of Bare Metal Service (BMS). If you call this operation to query performance baseline data after a performance evaluation task is complete, the data will be retrieved and compared.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&UID=1133166938931507 &<Common request parameters>
```

Sample success responses `JSON` format

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

### DescribeLicenseInfo

Queries the license information of Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ModelTyp e | Strin g | Query | No | 1 | The type of the model. Valid values: 0: public model. 1: custom model. |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLicenseInfo
```

Sample success responses `JSON` format

```json
{
 "responseVersion":"1.0",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "status":200
}
```

### ListModels

Queries a list of all models of Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Category | Strin g | Query | No | ecs | The abbreviation of the cloud service name. Valid values of N: 1 to 200. For information about how to query the abbreviations of cloud service names, see metricCategory in the response parameter Labels of the DescribeProjectMeta operation. |
| Framewor k | Strin g | Query | No | 1 | The type of the framework. Valid values: 1: Tensorflow. 2: PyTorch. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |

BareMetal Mangement Service

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

### GetLogLink

Queries the log link of a bare metal instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UID | Strin g | Query | Yes | 1133166938931507 | UID |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Request parameters**

**Response parameters**

**Examples**

Sample requests

```
&UID=1133166938931507 &<Common request parameters>
```

Sample success responses

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UID | Strin g | Query | Yes | 1133166938931507 | UID |
| TailLines | Strin g | Query | No | 10 | The number of lines read from the end of a file. For example, you can specify 10 for this parameter to display the last 10 lines of a log file. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| errorCode | String | InternalError | The error code. |

BareMetal Mangement Service `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":{
  "data":"xxxxxx Success!"
 },
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

### GetLog

Queries the logs of Bare Metal Service (BMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| errorTitle | String | InternalError | The error title. |
| errorMessage | String | The requested services is xxxxx | The error message. |
| dynamicCode | String | PlatformResponseE rror.%s | The dynamic error code. |
| dynamicMessa ge | String | The specified store %s does not exist. | The dynamic message. |
| data | String | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |
| status | Integer | 200 | The returned HTTP or HTTPS status code. |
| requestId | String | *****-*****-***** | The request ID. |
| success | Boolean | true | The status of response. |
| responseVersi on | String | 1.0 | The version of response. |

BareMetal Mangement Service

**Examples**

Sample requests

```
&UID=1133166938931507 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "dynamicCode":"PlatformResponseError.%s",
 "responseVersion":"1.0",
 "dynamicMessage":"The specified store %s does not exist.",
 "data":"{\"data\":\"xxxxxx Success!\"}",
 "errorTitle":"InternalError",
 "requestId":"*****-*****-*****",
 "success":true,
 "errorMessage":"The requested services is xxxxx",
 "errorCode":"InternalError",
 "Code":"ERROR",
 "status":200
}
```

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| CLusterNa me | Strin g | Query | No | **** product test2 _ _ | The name of the cluster. |
| Departme nt | Strin g | Query | No | test | The organization. |
| Resource Groups | Strin g | Query | No | 23 | The resource set ID. |
| ClusterTy pe | Strin g | Query | No | Kubernetes | The type of the cluster. The example shows that the cluster uses Kubernetes as its management and service orchestration platform. You can specify other cluster types such as Hadoop and Mesos. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestID | String | *****-*****-***** | The request ID. |
| ExecuteStatus | Integer | success | The execution state of the query. Valid values: success : The query is executed successfully. fail : The query fails. |
| Message | String | You do not have the permissions to access this file. | The detailed error message that is associated with the errorTitle parameter. This message explains why you do not have the permissions and how to resolve the issue. |

BareMetal Mangement Service

### GetMachineIDbyCluster

Queries the ID of a bare metal server based on the cluster information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | ERROR | 404 |
| data | Map | {"data":"xxxxxx Success!"} | The data object that typically contains information or results in the response of the API operation. |

BareMetal Mangement Service

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetMachineIDbyCluster &<Common request parameters>
```

Sample success responses `JSON` format

```json
{
 "RequestID":"*****-*****-*****",
 "Message":"You do not have the permissions to access this file",
 "data":{
  "data":"xxxxxx Success!"
 },
 "ExecuteStatus":"",
 "Code":"ERROR"
}
```
