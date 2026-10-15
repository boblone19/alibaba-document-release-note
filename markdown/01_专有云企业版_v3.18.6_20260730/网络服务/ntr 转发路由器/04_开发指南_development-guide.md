---
title: "转发路由器 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 137
source_pdf: "04_开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ntr/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 转发路由器 开发指南

## API参考

### API概览

本文汇总转发路由器提供的API接口列表。

| API | 说明 |
|---|---|
| CreateCen | 创建云企业网实例。 |
| ModifyCenAttribute | 修改云企业网实例的名称和描述信息。 |
| DescribeCens | 查询云企业网实例的信息。 |
| DescribeChildInstanceRegions | 查询转发路由器支持连接的网络实例的地域信息。 |
| DescribeCenAttachedChildInstanceAttribute | 查看加载到云企业网中的网络实例（VPC、VBR）的详细信息。 |
| DescribeCenAttachedChildInstances | 查询云企业网实例下已加载的网络实例的信息。 |
| DeleteCen | 删除云企业网实例。 |

| API | 说明 |
|---|---|
| CreateTransitRouter | 创建转发路由器实例。 |
| UpdateTransitRouter | 修改转发路由器实例的名称和描述信息。 |
| ListTransitRouters | 查询云企业网实例下转发路由器实例的信息。 |
| ListTransitRouterAvailableResource | 查询指定地域下转发路由器支持的可用区信息。 |
| DeleteTransitRouter | 删除转发路由器实例。 |

| API | 说明 |
|---|---|
| CreateTransitRouterCidr | 创建转发路由器地址段。 |
| ModifyTransitRouterCidr | 修改转发路由器地址段。 |
| ListTransitRouterCidr | 查询转发路由器地址段的信息。 |
| ListTransitRouterCidrAllocation | 查询转发路由器地址段的分配信息。 |
| DeleteTransitRouterCidr | 删除转发路由器地址段。 |

| API | 说明 |
|---|---|
| CreateTransitRouterVpcAttachment | 在转发路由器下创建VPC连接。 |
| UpdateTransitRouterVpcAttachmentAttribute | 修改转发路由器下VPC连接的名称和描述信息。 |
| ListTransitRouterVpcAttachments | 查询转发路由器下VPC连接的信息。 |
| DeleteTransitRouterVpcAttachment | 删除转发路由器下的VPC连接。 |

| UpdateTransitRouterVpcAttachmentZones | 修改VPC连接关联的可用区和交换机。 |
|---|---|
| ListGrantVSwitchesToCen | 查询云企业网实例已连接的跨账号VPC下交换机的信息。 |

| API | 说明 |
|---|---|
| CreateTransitRouterVbrAttachment | 在转发路由器下创建VBR连接。 |
| UpdateTransitRouterVbrAttachmentAttribute | 修改转发路由器下VBR连接的名称和描述信息。 |
| ListTransitRouterVbrAttachments | 查询转发路由器下的VBR连接信息。 |
| DeleteTransitRouterVbrAttachment | 删除转发路由器下的VBR连接。 |

| API | 说明 |
|---|---|
| CreateTransitRouterConnectAttachment | 创建Connect连接。 |
| UpdateTransitRouterConnectAttachmentAttribute | 修改Connect连接的配置。 |
| ListTransitRouterConnectAttachments | 查询Connect连接的信息。 |
| CreateTransitRouterConnectPeer | 创建Connect Peer。 |
| ListTransitRouterConnectPeers | 查询Connect Peer的信息。 |
| DeleteTransitRouterConnectPeer | 删除Connect Peer。 |
| DeleteTransitRouterConnectAttachment | 删除Connect连接。 |

| API | 说明 |
|---|---|
| DescribeGrantRulesToCen | 查询云企业网实例已获得授权的跨账号的网络实例的信息。 |
| DescribeGrantRulesToResource | 查询网络实例对跨账号云企业网实例的授权信息。 |
| RevokeInstanceFromTransitRouter | 取消转发路由器实例连接跨账号网络实例的权限。 |
| GrantInstanceToTransitRouter | 为转发路由器实例授予连接跨账号网络实例的权限。 |

| API | 说明 |
|---|---|
| CreateTransitRouterRouteEntry | 在转发路由器的路由表中添加路由条目。 |
| UpdateTransitRouterRouteEntry | 修改转发路由器路由表中自定义路由条目的名称和描述信息。 |
| DeleteTransitRouterRouteEntry | 删除转发路由器路由表中静态配置的路由条目。 |
| ListTransitRouterRouteEntries | 查询转发路由器路由表中的路由条目信息。 |

**路由**

| API | 说明 |
|---|---|

| ListCenChildInstanceRouteEntriesToAttachment | 查询转发路由器下网络实例路由表中指向网络实例连接的路由条目。 |
|---|---|
| DescribeRouteConflict | 查询网络实例中存在冲突的路由条目信息。 |
| DescribeCenRegionDomainRouteEntries | 查询云企业网实例中某个地域内路由条目的详细信息。 |
| DescribeCenChildInstanceRouteEntries | 查询云企业网中网络实例的路由条目信息。 |

| API | 说明 |
|---|---|
| CreateTransitRouterRouteTable | 为转发路由器创建自定义路由表。 |
| UpdateTransitRouterRouteTable | 修改转发路由器路由表的名称和描述信息。 |
| ListTransitRouterRouteTables | 查询转发路由器的路由表信息。 |
| DeleteTransitRouterRouteTable | 删除转发路由器的自定义路由表。 |

### 路由学习

| API | 说明 |
|---|---|
| EnableTransitRouterRouteTablePropagation | 创建路由学习关系。 |
| DisableTransitRouterRouteTablePropagation | 解除路由学习关系。 |
| ListTransitRouterRouteTablePropagations | 查询转发路由器路由表的路由学习关系。 |

### 关联转发

| API | 说明 |
|---|---|
| AssociateTransitRouterAttachmentWithRouteTable | 创建关联转发关系。 |
| DissociateTransitRouterAttachmentFromRouteTable | 解除关联转发关系。 |
| ListTransitRouterRouteTableAssociations | 查询转发路由器路由表或网络实例连接已创建的关联转发关系。 |

**组播**

| API | 说明 |
|---|---|
| CreateTransitRouterMulticastDomain | 创建组播域。 |
| ModifyTransitRouterMulticastDomain | 修改组播域的名称和描述信息。 |
| ListTransitRouterMulticastDomains | 查询组播域的信息。 |
| DeleteTransitRouterMulticastDomain | 删除组播域。 |
| AssociateTransitRouterMulticastDomain | 将VPC下的交换机关联至组播域。 |
| DisassociateTransitRouterMulticastDomain | 解除交换机与组播域的关联关系。 |
| ListTransitRouterMulticastDomainAssociations | 查询组播域的关联信息。 |
| RegisterTransitRouterMulticastGroupSources | 创建组播源。 |
| DeregisterTransitRouterMulticastGroupSources | 删除组播源。 |

| RegisterTransitRouterMulticastGroupMembers | 创建组播成员。 |
|---|---|
| DeregisterTransitRouterMulticastGroupMembers | 删除组播成员。 |
| ListTransitRouterMulticastGroups | 查询组播域下组播成员和组播源的信息。 |
| ListGrantVSwitchEnis | 查询VPC下可以成为组播源或者组播成员的弹性网卡的信息。 |
| ListTransitRouterMulticastDomainVSwitches | 查询VPC下已关联组播域的交换机的信息。 |

### 路由策略

| API | 说明 |
|---|---|
| CreateCenRouteMap | 创建路由策略。 |
| ModifyCenRouteMap | 修改路由策略。 |
| DescribeCenRouteMaps | 查询路由策略信息。 |
| DeleteCenRouteMap | 删除路由策略。 |

### 健康检查

| API | 说明 |
|---|---|
| EnableCenVbrHealthCheck | 开启边界路由器的健康检查功能，确保及时发现出现故障的物理专线，也支持修改VBR的健康检查配置。 |
| DescribeCenVbrHealthCheck | 查询指定地域内边界路由器的健康检查配置信息。 |
| DisableCenVbrHealthCheck | 关闭指定边界路由器的健康检查功能。 |

### 云企业网实例

#### 1.2.1. ModifyCenAttribute

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CenId | String | Query | 是 | cen-7qthudw0ll6jmc**** | 云企业网实例的ID。 |
| Name | String | Query | 否 | test | 云企业网实例的名称。 长度为2~128个字符，必须以大小写字母或中文开头，可包含数字、下划线（_）和短划线 （-），但不能以 http:// 或 https:// 开头。 |
| Description | String | Query | 否 | cen | 云企业网实例的描述信息。 描述可以为空或描述长度为2~256个字符，必须以大小写字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| ProtectionLevel | String | Query | 否 | REDUCED | 设置网段重叠的级别。 取值：REDUCED （默认值），表示网段可以有重叠，但是不能完全相同。 |
| Action | String | Query | 否 | ModifyCenAttribute | 系统规定参数。取值：ModifyCenAttribute 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 13526224-5780-4426-8BDF- BC8B08700F22 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyCenAttribute &CenId=cen-7qthudw0ll6jmc****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"13526224-5780-4426-8BDF-BC8B08700F22" } |  |

| XML | 格式 |
|---|---|
| <RequestId>13526224-5780-4426-8BDF-BC8B08700F22</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONENHANCEP _ _ _ ROTECTIONLEVEL _ | InvalidOperation.EnhanceProtectionLevel | Your request to enhance CBN protection level cannot be processed. Please contact customer support to continue this operation. |

#### 1.2.2. DescribeCenAttachedChildInstances

**使用说明**

通过指定**CenId**和**ChildInstanceRegionId**，查询云企业网实例在某一个地域下已加载的网络实例的信息。 通过指定**CenId**和**ChildInstanceType**，查询云企业网实例已加载的某一类型的网络实例的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCenAttachedChildInstances | 系统规定参数。取值：DescribeCenAttachedChildInstances 。 |
| PageNumber | Integer | Query | 否 | 1 | 查询页码。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。默认值为10，取值范围：1~50。 |
| CenId | String | Query | 是 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| ChildInstanceType | String | Query | 否 | VPC | 网络实例的类型，取值： VPC：专有网络实例。 VBR：边界路由器实例。 |
| ChildInstanceRegion Id | String | Query | 否 | cn-qingdao-env66-d01 | 网络实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ChildInstances | Array |  | 云企业网实例加载的网络实例信息列表。 |

| -CenId | String | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
|---|---|---|---|
| -ChildInstanceId | String | vpc-8vb1lu55yt9rlwgxl**** | 网络实例ID。 |
| -ChildInstanceType | String | VPC | 网络实例的类型，取值： VPC：专有网络实例。 VBR：边界路由器实例。 |
| -ChildInstanceRegionId | String | cn-qingdao-env66-d01 | 网络实例所属地域ID。 |
| -ChildInstanceOwnerId | Long | 1688000000000000 | 网络实例所属一级组织UID。 |
| -Status | String | Attached | 网络实例的状态，取值： Attaching：加载中。 Attached：已加载。 Detaching：卸载中。 |
| -ChildInstanceAttachTime | String | 2021-08-10T06:27Z | 网络实例的加载时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为：YYYY-MM- DDThh:mmZ。 |
| RequestId | String | B2063B16-852B-5B66-B73D- 4ED4D1A5E5C2 | 请求ID。 |
| TotalCount | Integer | 1 | 总条目数。 |
| PageNumber | Integer | 1 | 查询页码。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCenAttachedChildInstances &CenId=cen-j3jzhw1zpau2km****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "PageSize":10, "RequestId":"B2063B16-852B-5B66-B73D-4ED4D1A5E5C2", "PageNumber":1, "ChildInstances":{ "Status":"Attached", "ChildInstanceType":"VPC", "CenId":"cen-j3jzhw1zpau2km****", "ChildInstanceAttachTime":"2021-08-10T06:27Z", "ChildInstanceOwnerId":1688000000000000, "ChildInstanceId":"vpc-8vb1lu55yt9rlwgxl****", "ChildInstanceRegionId":"cn-qingdao-env66-d01" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>B2063B16-852B-5B66-B73D-4ED4D1A5E5C2</RequestId> <PageNumber>1</PageNumber> <ChildInstances> <Status>Attached</Status> <ChildInstanceType>VPC</ChildInstanceType> <CenId>cen-j3jzhw1zpau2km****</CenId> <ChildInstanceAttachTime>2021-08-10T06:27Z</ChildInstanceAttachTime> <ChildInstanceOwnerId>1688000000000000</ChildInstanceOwnerId> <ChildInstanceId>vpc-8vb1lu55yt9rlwgxl****</ChildInstanceId> <ChildInstanceRegionId>cn-qingdao-env66-d01</ChildInstanceRegionId> </ChildInstances> |  |

#### 1.2.3. DescribeCenAttachedChildInstanceAttribute

查看加载到云企业网中的网络实例（VPC、VBR）的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCenAttachedChildInstanceAttribute | 系统规定参数。取值：DescribeCenAttachedChildInstance Attribute。 |
| CenId | String | Query | 是 | cen-5mv960yjhja0dh**** | 云企业网实例ID。 |
| ChildInstanceId | String | Query | 是 | vpc-2zebdboka7d7t37vo**** | 云企业网实例已加载的网络实例ID。 |
| ChildInstanceType | String | Query | 是 | VPC | 网络实例的类型，取值： VPC：专有网络实例。 VBR：边界路由器实例。 |
| ChildInstanceRegion Id | String | Query | 是 | cn-qingdao-env66-d01 | 网络实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | ADD98358-D265-4060-87CB- A2427F5A8944 | 请求ID。 |
| CenId | String | cen-5mv960yjhja0dh**** | 云企业网实例ID。 |
| ChildInstanceId | String | vpc-2zebdboka7d7t37vo**** | 网络实例ID。 |
| ChildInstanceType | String | VPC | 网络实例的类型。 VPC：专有网络实例。 VBR：边界路由器实例。 |
| ChildInstanceRegionId | String | cn-qingdao-env66-d01 | 网络实例所属地域ID。 |
| ChildInstanceOwnerId | Long | 1688000000000000 | 网络实例所属的一级组织UID。 |
| Status | String | Attached | 网络实例的加载状态。 Attaching：加载中。 Attached：已加载。 Detaching：卸载中。 |
| ChildInstanceName | String | defaultvpc | 网络实例的名称。 |
| ChildInstanceAttachTime | String | 2018-07-30T07:53Z | 网络实例的加载时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为：YYYY-MM- DDThh:mmZ。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCenAttachedChildInstanceAttribute &CenId=cen-5mv960yjhja0dh**** &ChildInstanceId=vpc-2zebdboka7d7t37vo**** &ChildInstanceType=VPC &ChildInstanceRegionId=cn-qingdao-env66-d01
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Status":"Attached",
 "ChildInstanceType":"VPC",
 "RequestId":"ADD98358-D265-4060-87CB-A2427F5A8944",
 "CenId":"cen-5mv960yjhja0dh****",
 "ChildInstanceAttachTime":"2018-07-30T07:53Z",
 "ChildInstanceOwnerId":1688000000000000,
 "ChildInstanceName":"defaultvpc",
 "ChildInstanceId":"vpc-2zebdboka7d7t37vo****",
 "ChildInstanceRegionId":"cn-qingdao-env66-d01"
}
```

| XML | 格式 |
|---|---|
| <Status>Attached</Status> <ChildInstanceType>VPC</ChildInstanceType> <RequestId>ADD98358-D265-4060-87CB-A2427F5A8944</RequestId> <CenId>cen-5mv960yjhja0dh****</CenId> <ChildInstanceAttachTime>2018-07-30T07:53Z</ChildInstanceAttachTime> <ChildInstanceOwnerId>1688000000000000</ChildInstanceOwnerId> <ChildInstanceName>defaultvpc</ChildInstanceName> <ChildInstanceId>vpc-2zebdboka7d7t37vo****</ChildInstanceId> <ChildInstanceRegionId>cn-qingdao-env66-d01</ChildInstanceRegionId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | INSTANCENOTEXIST _ _ | ParameterError | The parameter is error. |
| 400 |  | SystemBusy | The system is busy. Please try again later. |

#### 1.2.4. DeleteCen

**使用说明**

转发路由器实例下不存在任何连接。具体操作，请参见DeleteTransitRouterVpcAttachmen、DeleteTransitRouterVbrAttachment和转发路由器实例下不存在自定义路由表。具体操作，请参见DeleteTransitRouterRouteTable。 转发路由器实例默认路由表下不存在自定义路由条目。具体操作，请参见DeleteTransitRouterRouteEntry。 转发路由器实例下不存在组播域。具体操作，请参见DeleteTransitRouterMulticastDomain。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CenId | String | Query | 是 | cen-7qthudw0ll6jmc**** | 云企业网实例ID。 |
| Action | String | Query | 否 | DeleteCen | 系统规定参数。取值：DeleteCen。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5903EE99-D542-4E14-BC65- AAC1CB2D3D03 | 请求ID。 |

**示例**

请求示例

```
&CenId=cen-7qthudw0ll6jmc****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"5903EE99-D542-4E14-BC65-AAC1CB2D3D03"
}
```

| XML | 格式 |
|---|---|
| <RequestId>5903EE99-D542-4E14-BC65-AAC1CB2D3D03</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationFailed.DeleteCenWithC ustomRouteTable | OperationFailed.DeleteCenWithCustomRouteTable | Operation failed because you are not allowed to delete the CEN with the custom transit router route table. |
| 400 | OperationFailed.DeleteCenWithRo uteEntry | OperationFailed.DeleteCenWithRouteEntry | Operation failed because you are not allowed to delete the CEN with the transit router route entry. |

#### 1.2.5. DescribeCens

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNumber | Integer | Query | 否 | 1 | 待查询的页码。默认值：1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。取值范围：1~50。默认值：10。 |
| Filter | RepeatList | Query | 否 |  | 过滤条件的信息。 一次最多支持输入5个过滤条件。 |
| -Key | String |  | 否 | CenId | 过滤条件。取值： CenId：云企业网实例ID。 Name：云企业网实例名称。 多个过滤条件之间默认是与的关系，即必须符合所有过滤条件，才视为匹配过滤条件。 一次最多支持输入5个过滤条件。 |
| -Value | RepeatList |  | 否 | cen-0xyeagctz5sfg9**** | 过滤条件的值。 根据Key指定过滤值。一个Key支持指定多个过滤值，多个过滤值之间是或的关系，即只要符合其中一个过滤值，则视为匹配该过滤条件。 一个过滤条件最多支持输入5个过滤值。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | tagtest | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | tagtest | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |
| Action | String | Query | 否 | DescribeCens | 系统规定参数。取值：DescribeCens。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalCount | Integer | 1 | 总条目数。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |
| RequestId | String | 2BFA6822-240E-4E27-B4C8- AA400EF7474D | 请求ID。 |
| PageNumber | Integer | 1 | 查询的页码。 |
| Cens | Array |  | 云企业网实例信息列表。 |
| -Tags | Array |  | 云企业网实例绑定的标签列表。 |
| --Key | String | tagkey | 标签键。 |
| --Value | String | tagvalue | 标签值。 |
| -Status | String | Active | 云企业网实例的状态。 Creating：创建中。 Active：运行中。 Deleting：删除中。 |
| -CreationTime | String | 2019-10-22T07:44Z | 云企业网实例的创建时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为： YYYY-MM- DDThh:mmZ 。 |
| -Ipv6Level | String | DISABLED | 云企业网实例是否已开启IPv6功能。 ENABLE：已开启。 DISABLED：未开启。 |
| -Description | String | desctest | 云企业网实例的描述信息。 |
| -CenId | String | cen-0xyeagctz5sfg9**** | 云企业网实例的ID。 |
| -ProtectionLevel | String | REDUCED | 网段重叠的级别。 REDUCED：表示网段可以有重叠，但是不能完全相同。 |
| -Name | String | nametest | 云企业网实例的名称。 |

|  | DDThh:mmZ |
|---|---|

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"2BFA6822-240E-4E27-B4C8-AA400EF7474D",
 "PageNumber":1,
 "Cens":{
  "Status":"Active",
  "ProtectionLevel":"REDUCED",
  "Description":"desctest",
  "-Tags":{
   "Value":"tagvalue",
   "Key":"tagkey"
  },
  "Ipv6Level":"DISABLED",
  "CreationTime":"2019-10-22T07:44Z",
  "CenId":"cen-0xyeagctz5sfg9****",
  "Name":"nametest"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>2BFA6822-240E-4E27-B4C8-AA400EF7474D</RequestId> <PageNumber>1</PageNumber> <Cens> <Status>Active</Status> <ProtectionLevel>REDUCED</ProtectionLevel> <Description>desctest</Description> <-Tags> <Value>tagvalue</Value> <Key>tagkey</Key> </-Tags> <Ipv6Level>DISABLED</Ipv6Level> <CreationTime>2019-10-22T07:44Z</CreationTime> <CenId>cen-0xyeagctz5sfg9****</CenId> <Name>nametest</Name> </Cens> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDTAGKEY _ _ | InvalidTagKey | The tag keys are not valid. |
| 400 | INVALIDTAGVALUE _ _ | InvalidTagValue | The tag values are not valid. |

#### 1.2.6. CreateCen

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| Name | String | Query | 否 | testname | 云企业网实例的名称。 长度为2~128个字符，必须以大小写字母或中文开头，可包含数字、下划线（_）和短划线（-）， 但不能以 http:// 或 https:// 开头。 |
| Description | String | Query | 否 | testdesc | 云企业网实例的描述信息。 长度为2~256个字符，必须以大小写字母或中文开头，但不能以 http:// 或 https:// 开头。 |

| ProtectionLevel | String | Query | 否 | REDUCED | 设置网段重叠的级别。 取值：REDUCED（默认值），表示网段可以有重叠，但是不能完全相同。 |
|---|---|---|---|---|---|
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | tagtest | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | tagtest | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |
| Action | String | Query | 是 | CreateCen | 系统规定参数。取值：CreateCen。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0C2EE7A8-74D4-4081-8236- CEBDE3BBCF50 | 请求ID。 |
| CenId | String | cen-dc4vwznpwbobrl**** | 云企业网实例的ID。 |

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50", "CenId":"cen-dc4vwznpwbobrl****" } |  |

| XML | 格式 |
|---|---|
| <RequestId>0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50</RequestId> <CenId>cen-dc4vwznpwbobrl****</CenId> |  |

#### 1.2.7. DescribeChildInstanceRegions

查询转发路由器支持连接的网络实例的地域信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProductType | String | Query | 否 | VPC | 网络实例的类型。取值： VPC：专有网络实例。 VBR：边界路由器实例。 |
| Action | String | Query | 否 | DescribeChildInstanceRegions | 系统规定参数。取值：DescribeChildInstanceRegions。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D5CEED59-36AA-47CC-9D81- 16F71C46BD80 | 请求ID。 |
| Regions | Array |  | 地域信息列表。 |
| -RegionId | String | cn-qingdao-env17e-d01 | 地域ID。 |
| -LocalName | String | cn-qingdao-env17e-d01 | 地域名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeChildInstanceRegions
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"D5CEED59-36AA-47CC-9D81-16F71C46BD80", "Regions":{ "RegionId":"cn-qingdao-env17e-d01", "LocalName":"cn-qingdao-env17e-d01" } } |  |

| XML | 格式 |
|---|---|
| <RequestId>D5CEED59-36AA-47CC-9D81-16F71C46BD80</RequestId> <Regions> <RegionId>cn-qingdao-env17e-d01</RegionId> <LocalName>cn-qingdao-env17e-d01</LocalName> </Regions> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.MissingOwnerIdOrOwnerAcco unt | MissingParameter.OwnerIdOrOwnerAccount | The input parameter OwnerAccount or OwnerId that is mandatory for processing this request is not supplied |

### 转发路由器实例

#### 1.3.1. CreateTransitRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouter | 系统规定参数。取值：CreateTransitRouter 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |
| CenId | String | Query | 是 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |

| 开发指南·API参 | 考 |  |  |  | 转发路由器 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-qingdao-env66-d01 | 转发路由器实例所属地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| TransitRouterName | String | Query | 否 | testname | 转发路由器实例的名称。 名称长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（_） 和短划线（-），但不能以 http:// 或 https:// 开头。 |
| TransitRouterDescr iption | String | Query | 否 | testdesc | 转发路由器实例的描述。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次创建请求执行预检，包括权限、实例状态校验等。取值： false （默认值）：发送正常请求，通过检查后直接创建转发路由器实例。 true ：发送检查请求，只进行校验，不会创建转发路由器实例。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 |
| SupportMulticast | Boolean | Query | 否 | false | 是否开启转发路由器的组播功能。取值： false （默认值）：不开启。 true ：开启。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | tagtest | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持 64个字符，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | TagValue | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入20个标签键对应的标签值。 |
| TransitRouterCidrLi st | RepeatList | Query | 否 |  | 转发路由器地址段列表。 一次最多支持添加5个转发路由器地址段。 |
| -Cidr | String |  | 否 | 192.168.10.0/24 | 转发路由器地址段。 |
| -Name | String |  | 否 | nametest | 转发路由器地址段的名称。 名称长度为1~128个字符。 |
| -Description | String |  | 否 | desctest | 转发路由器地址段的描述信息。 描述长度为1~256个字符。 |
| -PublishCidrRoute | Boolean |  | 否 | true | 是否允许系统自动在转发路由器路由表中添加转发路由器地址段的路由。 true （默认值）：允许。 false ：不允许。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterId | String | tr-uf6llz2286805i44g**** | 转发路由器实例ID。 |
| RequestId | String | 404DA7EC-F495-44B5-B543- 6EDCDF90F3D1 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouter &CenId=cen-j3jzhw1zpau2km**** &RegionId=cn-qingdao-env66-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"404DA7EC-F495-44B5-B543-6EDCDF90F3D1", "TransitRouterId":"tr-uf6llz2286805i44g****" } |  |

| XML | 格式 |
|---|---|
| <RequestId>404DA7EC-F495-44B5-B543-6EDCDF90F3D1</RequestId> <TransitRouterId>tr-uf6llz2286805i44g****</TransitRouterId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationUnsupported.RegionId | OperationUnsupported.RegionId | The specified Region is not supported. |
| 400 | InstanceExist.TransitRouterInstan ce | InstanceExist.TransitRouterInstance | The instance already exists. |
| 400 | USERNOTOPENTRSERVICE _ _ _ _ | Forbbiden.TransitRouterServiceNotOpen | The user has not open transit router service. |
| 400 | OperationUnsupported.SupportM ulticast | OperationUnsupported.SupportMulticast | The multicast is not supported in the specified region. |
| 400 | PARAMETERILLEGALTRANSITRO _ _ UTERREGIONID _ | OperationUnsupported.RegionId | The specified Region is not supported. |
| 400 | CENFULLLEVELNOTSUPPORT _ _ _ _ _ TR | OperationUnsupported.CenFullLevel | CEN full level does not support TransitRouter. |
| 400 | IllegalParam.Cidr | IllegalParam.Cidr | Cidr is illegal. |
| 400 | Illegal.TrType | Illegal.TrType | The TransitRouter type is illegal. |
| 400 | OperationUnsupported.TransitRo uterCidrList | OperationUnsupported.TransitRouterCidrList | The TransitRouterCidrList is not support in the specified Region. |
| 400 | CIDRCONFLICT _ | OperationFailed.CidrConflict | Operation is invalid because the cidr conflict. |
| 400 | IllegalParam.RegionId | IllegalParam.Region | The specified region is invalid. |

#### 1.3.2. DeleteTransitRouter

**使用说明**

转发路由器实例下不存在任何连接。具体操作，请参见DeleteTransitRouterVpcAttachment、DeleteTransitRouterConnectAttachment和转发路由器实例下不存在自定义路由表。具体操作，请参见DeleteTransitRouterRouteTable。 转发路由器实例默认路由表下不存在自定义路由条目。具体操作，请参见DeleteTransitRouterRouteEntry。 转发路由器实例下不存在组播域。具体操作，请参见DeleteTransitRouterMulticastDomain。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouter | 系统规定参数。取值：DeleteTransitRouter 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |

| 开发指南·API参 | 考 |  |  |  | 转发路由器 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| DryRun | Boolean | Query | 否 | false | 是否对此次删除请求执行预检，包括权限、实例状态校验等。取值： false （默认）：发送正常请求，通过检查后直接删除转发路由器实例。 true ：发送检查请求，只进行校验，不会删除转发路由器实例。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 |
| TransitRouterId | String | Query | 是 | tr-uf654ttymmljlvh2x**** | 转发路由器实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6DE3EE92-39C8-4BBD-A3AD- F568D74741BB | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouter &TransitRouterId=tr-uf654ttymmljlvh2x****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"6DE3EE92-39C8-4BBD-A3AD-F568D74741BB" } |  |

`XML` 格式

```xml
<RequestId>6DE3EE92-39C8-4BBD-A3AD-F568D74741BB</RequestId>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationFailed.DeleteTransitRou ter | OperationFailed.DeleteTransitRouter | Operation failed because TransitRouterRouteEntry exists |
| 400 | OperationFailed.DeleteTransitRou ter | OperationFailed.DeleteTransitRouter | Operation failed because TransitRouterRouteTable exists |
| 400 | IncorrectStatus.TransitRouterInst ance | IncorrectStatus.TransitRouterInstance | The status of TransitRouter is incorrect. |
| 400 | INVALIDOPERATIONCCNATTAC _ _ _ HED | OperationFailed.CCNAttached | Can not delete transit router because CCN still attached. |
| 400 | INVALIDOPERATIONBANDWIDT _ _ HLIMITEXIST _ _ | OperationFailed.BandwidthLimitExist | Operation is invalid because a bandwidth limit exist. |

#### 1.3.3. UpdateTransitRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | UpdateTransitRouter | 系统规定参数。取值：UpdateTransitRouter 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |

| 转发路由器 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| DryRun | Boolean | Query | 否 | false | 是否对此次修改请求执行预检，包括权限、实例状态校验等。取值： false （默认）：发送正常请求，通过检查后直接修改转发路由器实例的信息。 true ：发送检查请求，只进行校验，不会修改转发路由器实例的信息。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 转发路由器实例所属地域ID。 您可以通过调用DescribeRegions接口获取地域 ID。 |
| TransitRouterId | String | Query | 是 | tr-uf654ttymmljlvh2x**** | 转发路由器实例ID。 |
| TransitRouterName | String | Query | 否 | testname | 转发路由器实例的新名称。 名称长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（_） 和短划线（-），不能以 http:// 或 https:// 开头。 |
| TransitRouterDescr iption | String | Query | 否 | testdesc | 转发路由器实例新的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E9963DD7-998B-4F92-892D- 8293CB49EE81 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouter &RegionId=cn-qingdao-env17e-d01 &TransitRouterId=tr-uf654ttymmljlvh2x****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"E9963DD7-998B-4F92-892D-8293CB49EE81" } |  |

`XML` 格式

```xml
<RequestId>E9963DD7-998B-4F92-892D-8293CB49EE81</RequestId>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationUnsupported.RegionId | OperationUnsupported.RegionId | The specified region ID is not supported. |
| 400 | IncorrectStatus.TransitRouter | IncorrectStatus.TransitRouterInstance | The status of TransitRouter is incorrect. |

#### 1.3.4. ListTransitRouters

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouters | 系统规定参数。取值：ListTransitRouters 。 |

| 开发指南·API参 | 考 |  |  |  | 转发路由器 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNumber | Integer | Query | 否 | 1 | 列表的页码。默认值：1 。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。取值范围：1 ~50 。默认值：10 。 |
| CenId | String | Query | 否 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| TransitRouterId | String | Query | 否 | tr-uf654ttymmljlvh2x**** | 转发路由器实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env66-d01 | 转发路由器实例所属地域ID。 您可以通过调用DescribeRegions接口获取地域 ID。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | TagKey | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持 64个字符，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | TagValue | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入20个标签键对应的标签值。 |
| FeatureFilter | RepeatList | Query | 否 |  | 转发路由器功能筛选字段。 |
| -Key | String |  | 否 | Multicast | 转发路由器功能筛选字段键值。 目前支持字段：Multicast ，表示组播功能。 |
| -Value | RepeatList |  | 否 | Enabled | 转发路由器功能筛选字段值列表。 当键值为Multicast 时，只支持填入1个字段，支持字段内容为： Enabled ：支持组播。 Disabled ：不支持组播。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouters | Array |  | 转发路由器实例信息。 |
| -TransitRouterCidrList | Array |  | 转发路由器地址段列表。 |
| --Cidr | String | 192.168.1.0/24 | 转发路由器地址段。 |
| --Name | String | CIDRname | 转发路由器地址段的名称。 |
| --Description | String | CIDRdesc | 转发路由器地址段的描述信息。 |
| --TransitRouterCidrId | String | cidr-46p5ceg21e8152**** | 转发路由器地址段ID。 |
| --PublishCidrRoute | Boolean | true | 是否允许系统自动在转发路由器路由表中添加转发路由器地址段的路由。 true ：允许。 false ：不允许。 |
| -Tags | Array |  | 标签列表。 |
| --Key | String | TagKey | 标签键。 |

| 转发路由器 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Value | String | TagValue | 标签值。 |
| -CreationTime | String | 2021-03-15T09:39Z | 转发路由器实例的创建时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为： YYYY-MM- DDThh:mmZ 。 |
| -Type | String | Enterprise | 转发路由器实例的类型。 仅取值：Enterprise ，企业版。 |
| -Status | String | Active | 转发路由器实例的状态。 Creating ：创建中。 Active ：可用。 Modifying ：修改中。 Deleting ：删除中。 Upgrading ：升级中。 |
| -TransitRouterId | String | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| -TransitRouterDescription | String | testdesc | 转发路由器实例的描述信息。 |
| -TransitRouterName | String | testname | 转发路由器实例的名称。 |
| -CenId | String | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| -AliUid | Long | 1210123456123456 | 云企业网实例所属一级组织UID。 |
| -RegionId | String | cn-qingdao-env66-d01 | 转发路由器实例所属地域ID。 |
| -SupportMulticast | Boolean | false | 转发路由器实例是否开启了组播功能。 true ：已开启。 false ：未开启。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |
| RequestId | String | 68521297-5FA6-46CB-B4EB- 658F1C68C8CC | 请求ID。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| TotalCount | Integer | 1 | 列表条目数。 |

|  | DDThh:mmZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouters
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"68521297-5FA6-46CB-B4EB-658F1C68C8CC",
 "PageNumber":1,
 "TransitRouters":{
  "Status":"Active",
  "Type":"Enterprise",
  "SupportMulticast":false,
  "-Tags":{
   "Value":"TagValue",
   "Key":"TagKey"
  },
  "CreationTime":"2021-03-15T09:39Z",
  "CenId":"cen-j3jzhw1zpau2km****",
  "TransitRouterDescription":"testdesc",
  "TransitRouterName":"testname",
  "RegionId":"cn-qingdao-env66-d01",
  "-TransitRouterCidrList":{
   "Description":"CIDRdesc",
   "Cidr":"192.168.1.0/24",
   "TransitRouterCidrId":"cidr-46p5ceg21e8152****",
   "PublishCidrRoute":true,
   "Name":"CIDRname"
  },
  "TransitRouterId":"tr-bp1su1ytdxtataupl****",
  "AliUid":1210123456123456
 }
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDPARAMETERCOMBINATI _ _ ONTRASNITROUTER _ _ | InvalidParameterCombination.TransitRouter | Region ID is required if no TransitRouterId or CenId specified. |
| 400 | FILTERVALUENOTSUPPORT _ _ _ | InvalidOperation.UnsupportFilterValue | The specified FeatureFilter Value is not supported by this operation. |
| 400 | InvalidParameter.FeatureFilter | InvalidOperation.UnsupportFilter | The specified FeatureFilter is not supported by this operation. |

#### 1.3.5. ListTransitRouterAvailableResource

查询指定地域下转发路由器支持的可用区信息。

**使用说明**

您可以调用ListTransitRouterAvailableResource接口查询指定地域下转发路由器支持的普通可用区的信息或者支持的组播功能的可用区的信息。 如果您未指定**SupportMulticast** 参数的值为**true** ，则系统默认只查询转发路由器支持的普通可用区的信息。 如果您指定**SupportMulticast** 参数的支持为**true** ，则系统只查询转发路由器支持的组播功能的可用区的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterAvailableResource | 系统规定参数。取值：ListTransitRouterAvailableResour ce 。 |
| RegionId | String | Query | 否 | cn-qingdao-env66-d01 | 转发路由器所属的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| SupportMulticast | Boolean | Query | 否 | false | 是否只查询支持组播功能的可用区的信息。 true ：是。 开启查询功能后，如果ListTransitRouterAvailableResour ce 接口返回结果为空，则表示当前地域的转发路由器不支持组播功能。 false （默认值）：否。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SlaveZones | String | cn-qingdao-env17e- amtest17001-a | 备可用区ID列表。 |
| MasterZones | String | cn-qingdao-env17e- amtest17001-a | 主可用区ID列表。 |
| AvailableZones | String | cn-qingdao-env17e- amtest17001-a | 可用区ID列表。 |
| RequestId | String | B4F480E0-4E76-5E43-9966- 8322C28A158A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterAvailableResource
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"B4F480E0-4E76-5E43-9966-8322C28A158A", "AvailableZones":"cn-qingdao-env17e-amtest17001-a" } |  |

| XML | 格式 |
|---|---|
| <SlaveZones>cn-qingdao-env17e-amtest17001-a</SlaveZones> <RequestId>B4F480E0-4E76-5E43-9966-8322C28A158A</RequestId> <MasterZones>cn-qingdao-env17e-amtest17001-a</MasterZones> <AvailableZones>cn-qingdao-env17e-amtest17001-a</AvailableZones> |  |

### 转发路由器地址段

#### 1.4.1. CreateTransitRouterCidr

**使用说明**

转发路由器地址段是您为转发路由器自定义的一个地址段，该地址段类似于为路由器环回口（Loopback接口）分配IP地址的地址段。转发路由器地址段被用于为Connect Peer分配地址。更多信息，请参见《转发路由器用户指南》手册**实例管理**>**转发路由器地址段**章节。 CreateTransitRouterCidr接口仅适用于在您创建转发路由器后，为转发路由器添加地址段。 一个转发路由器最多支持配置5个地址段。 不支持配置100.64.0.0/10、224.0.0.0/4、127.0.0.0/8、169.254.0.0/16及其子网为转发路由器地址段。 每个转发路由器地址段不能与云企业网实例下所有待互通的网段冲突。同一个云企业网实例下，每个转发路由器地址段需确保唯一。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterCidr | 系统规定参数。取值：CreateTransitRouterCidr。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次API 请求的RequestId不一样。 |
| TransitRouterId | String | Query | 是 | tr-p0w3x8c9em72a40nw**** | 转发路由器实例ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 转发路由器实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |

| Name | String | Query | 否 | nametest | 转发路由器地址段的名称。 名称长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-），但不能以 http:// 或 https:// 开头。 |
|---|---|---|---|---|---|
| Description | String | Query | 否 | desctest | 转发路由器地址段的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会创建转发路由器地址段。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接创建转发路由器地址段。 |
| Cidr | String | Query | 是 | 192.168.10.0/24 | 转发路由器地址段。 |
| PublishCidrRoute | Boolean | Query | 否 | true | 是否允许系统自动在转发路由器路由表中添加转发路由器地址段的路由。 true（默认值）：允许。 false：不允许。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterCidrId | String | cidr-0zv0q9crqpntzz**** | 转发路由器地址段ID。 |
| RequestId | String | 0876E54E-3E36-5C31-89F0- 9EE8A9266F9A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterCidr &TransitRouterId=tr-p0w3x8c9em72a40nw**** &RegionId=cn-qingdao-env17e-d01 &Cidr=192.168.10.0/24
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A", "TransitRouterCidrId":"cidr-0zv0q9crqpntzz****" } |  |

| XML | 格式 |
|---|---|
| <RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId> <TransitRouterCidrId>cidr-0zv0q9crqpntzz****</TransitRouterCidrId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OverLappingExist.Cidr | OverLappingExist.Cidr | The cidr overlapping exist. |
| 400 | OperationUnsupported.TransitRo uterCidr | OperationUnsupported.TransitRouterCidr | Transit region does not support the operation. |
| 400 | IllegalParam.Cidr | IllegalParam.Cidr | The specified cidr is invalid. |

#### 1.4.2. ModifyTransitRouterCidr

**使用说明**

修改转发路由器地址段前，建议您先了解转发路由器地址段使用限制。更多信息，请参见《转发路由器用户指南》手册实例管理>转发路由器地址段章节。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ModifyTransitRouterCidr | 系统规定参数。取值：ModifyTransitRouterCidr 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| TransitRouterId | String | Query | 是 | tr-gw8ergozrv77rtbjd**** | 转发路由器实例ID。 |
| TransitRouterCidrId | String | Query | 是 | cidr-0zv0q9crqpntzz**** | 转发路由器地址段ID。 您可以通过调用ListTransitRouterCidr接口查询转发路由器地址段ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 转发路由器实例所属的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| Name | String | Query | 否 | nametest | 转发路由器地址段的新名称。 名称长度为2~128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（_） 和短划线（-），但不能以 http:// 或 https:// 开头。 |
| Description | String | Query | 否 | desctest | 转发路由器地址段新的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| Cidr | String | Query | 否 | 192.168.10.0/24 | 新的转发路由器地址段。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会修改转发路由器地址段。检查项包括是否填写了必需参数、 请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接修改转发路由器地址段。 |
| PublishCidrRoute | Boolean | Query | 否 | true | 是否允许系统自动在转发路由器路由表中添加转发路由器地址段的路由。 true ：允许。 false ：不允许。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0876E54E-3E36-5C31-89F0- 9EE8A9266F9A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyTransitRouterCidr &TransitRouterId=tr-gw8ergozrv77rtbjd**** &TransitRouterCidrId=cidr-0zv0q9crqpntzz**** &RegionId=cn-qingdao-env17e-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A" } |  |

| XML | 格式 |
|---|---|
| <RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId> |  |

#### 1.4.3. ListTransitRouterCidr

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterCidr | 系统规定参数。取值：ListTransitRouterCidr 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| TransitRouterId | String | Query | 是 | tr-p0w3x8c9em72a40nw**** | 转发路由器实例ID。 |
| TransitRouterCidrId | String | Query | 否 | cidr-0zv0q9crqpntzz**** | 转发路由器地址段ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 转发路由器实例所属的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会查询转发路由器已添加的地址段。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接查询转发路由器下已添加的地址段。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CidrLists | Array |  | 转发路由器地址段列表。 |
| -TransitRouterCidrId | String | cidr-0zv0q9crqpntzz**** | 转发路由器地址段ID。 |
| -Family | String | IPv4 | 转发路由器地址段类型。 仅取值：IPv4 ，表示转发路由器地址段为IPv4类型的地址段。 |
| -Name | String | nametest | 转发路由器地址段的名称。 |
| -Description | String | desctest | 转发路由器地址段的描述信息。 |
| -Cidr | String | 192.168.10.0/24 | 转发路由器地址段。 |
| -PublishCidrRoute | Boolean | true | 是否允许系统自动在转发路由器路由表中添加转发路由器地址段的路由。 true ：允许。 false ：不允许。 |

| 转发路由器 |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -TransitRouterId | String | tr-p0w3x8c9em72a40nw**** | 转发路由器实例ID。 |
| RequestId | String | 0876E54E-3E36-5C31-89F0- 9EE8A9266F9A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterCidr &TransitRouterId=tr-p0w3x8c9em72a40nw**** &RegionId=cn-qingdao-env17e-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A", "CidrLists":{ "Description":"desctest", "Cidr":"192.168.10.0/24", "TransitRouterCidrId":"cidr-0zv0q9crqpntzz****", "Family":"IPv4", "PublishCidrRoute":true, "Name":"nametest", "TransitRouterId":"tr-p0w3x8c9em72a40nw****" } } |  |

| XML | 格式 |
|---|---|
| <RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId> <CidrLists> <Description>desctest</Description> <Cidr>192.168.10.0/24</Cidr> <TransitRouterCidrId>cidr-0zv0q9crqpntzz****</TransitRouterCidrId> <Family>IPv4</Family> <PublishCidrRoute>true</PublishCidrRoute> <Name>nametest</Name> <TransitRouterId>tr-p0w3x8c9em72a40nw****</TransitRouterId> </CidrLists> |  |

#### 1.4.4. ListTransitRouterCidrAllocation

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterCidrAllocation | 系统规定参数。取值：ListTransitRouterCidrAllocation 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| TransitRouterId | String | Query | 是 | tr-p0w3x8c9em72a40nw**** | 转发路由器实例ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 转发路由器实例所属的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TransitRouterCidrId | String | Query | 否 | cidr-0zv0q9crqpntzz**** | 转发路由器地址段ID。 您可以通过调用ListTransitRouterCidr接口查询转发路由器地址段ID。 |
| CidrBlock | String | Query | 否 | 192.168.10.0/28 | 转发路由器地址段下已分配地址的网段。 |
| Cidr | String | Query | 否 | 192.168.10.0/24 | 转发路由器地址段。 |
| DedicatedOwnerId | String | Query | 否 | VPN | 专用网段。 仅取值：VPN ，表示您要查询系统保留的用于系统后台创建VPN连接的网段。 |
| AttachmentId | String | Query | 否 | tr-attach-2nalp6yksc805w**** | 网络实例连接ID。 |
| AttachmentName | String | Query | 否 | nametest | 网络实例连接的名称。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会开始查询转发路由器地址段分配详情。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过， 则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接查询转发路由器地址段分配详情。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时每次显示的条目数。 如果您不指定MaxResults 参数的值，则表示您不需要分批次查询。调用该接口后返回参数MaxResults 的值表示列表条目总数。 如果您指定MaxResults 参数的值，则表示您需要分批次查询。取值范围：1 ~100 。建议指定MaxResults 参数的值为20 。 调用该接口后返回参数MaxResults 的值表示当前查询批次下列表条目的数量。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken 值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterCidrAllocatio ns | Array |  | 转发路由器地址段分配详情。 |
| -TransitRouterCidrId | String | cidr-0zv0q9crqpntzz**** | 转发路由器地址段ID。 |
| -AllocatedCidrBlock | String | 192.168.10.0/28 | 转发路由器地址段下已分配地址的网段。 |
| -AttachmentId | String | tr-attach-2nalp6yksc805w**** | 网络实例连接ID。 |
| -Cidr | String | 192.168.10.0/24 | 转发路由器地址段。 |
| -AttachmentName | String | nametest | 网络实例连接的名称。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | 0876E54E-3E36-5C31-89F0- 9EE8A9266F9A | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| MaxResults | Integer | 1 | 分批次查询时每次显示的条目数。 如果您未指定请求参数MaxResults 的值，则表示您不需要分批次查询。返回参数MaxResults 的值表示列表条目总数。 如果您指定了请求参数MaxResults 的值，则表示您需要分批次查询。返回参数MaxResults 的值表示当前查询批次下列表条目的数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterCidrAllocation &TransitRouterId=tr-p0w3x8c9em72a40nw**** &RegionId=cn-qingdao-env17e-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A", "MaxResults":1, "TransitRouterCidrAllocations":{ "Cidr":"192.168.10.0/24", "AttachmentName":"nametest", "TransitRouterCidrId":"cidr-0zv0q9crqpntzz****", "AllocatedCidrBlock":"192.168.10.0/28", "AttachmentId":"tr-attach-2nalp6yksc805w****" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId> <MaxResults>1</MaxResults> <TransitRouterCidrAllocations> <Cidr>192.168.10.0/24</Cidr> <AttachmentName>nametest</AttachmentName> <TransitRouterCidrId>cidr-0zv0q9crqpntzz****</TransitRouterCidrId> <AllocatedCidrBlock>192.168.10.0/28</AllocatedCidrBlock> <AttachmentId>tr-attach-2nalp6yksc805w****</AttachmentId> </TransitRouterCidrAllocations> |  |

#### 1.4.5. DeleteTransitRouterCidr

**使用说明**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouterCidr | 系统规定参数。取值：DeleteTransitRouterCidr 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| TransitRouterId | String | Query | 是 | tr-p0w3x8c9em72a40nwXXXX | 转发路由器实例ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TransitRouterCidrId | String | Query | 是 | cidr-0zv0q9crqpntzzXXXX | 转发路由器地址段ID。 您可以通过调用ListTransitRouterCidr接口查询转发路由器地址段ID。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 转发路由器实例所属的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会删除转发路由器地址段。检查项包括是否填写了必需参数、 请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接删除转发路由器地址段。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0876E54E-3E36-5C31-89F0- 9EE8A9266F9A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterCidr &TransitRouterId=tr-p0w3x8c9em72a40nwXXXX &TransitRouterCidrId=cidr-0zv0q9crqpntzzXXXX &RegionId=cn-qingdao-env17e-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A" } |  |

| XML | 格式 |
|---|---|
| <RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | CIDRBLOCKALLOCATED _ _ | OperationFailed.CidrBlockAllocated | Cidr blocks are allocated from the cidr, which should be released first. |

### VPC连接

#### 1.5.1. CreateTransitRouterVpcAttachment

在转发路由器下创建专有网络VPC（Virtual Private Cloud）连接。

**使用说明**

创建VPC连接后，VPC连接默认不与任何转发路由器路由表建立路由学习关系和关联转发关系。 如果您要连接跨账号的网络实例，请先获得跨账号网络实例授权。具体操作，请参见GrantInstanceToTransitRouter。 对于仅支持一个可用区的地域，使用该地域的转发路由器连接VPC实例前，需确保VPC实例在该可用区中拥有至少一个交换机实例，且该交换机实例需要拥有一个空闲的 IP地址。 对于支持多个可用区的地域，使用该地域的转发路由器连接VPC实例前，需确保VPC实例拥有至少2个交换机实例，2个交换机实例位于不同的可用区，且每个交换机实例需要拥有一个空闲的IP地址。在VPC实例与转发路由器流量互通的过程中，这2个交换机实例可实现可用区级别的容灾。 对于转发路由器支持多个可用区的地域，推荐您在转发路由器支持的每个可用区中均创建一个交换机实例（每个交换机实例下需拥有一个空闲的IP地址），用于创建VPC连接。在VPC和转发路由器流量互通的过程中可以减少流量绕行，获得更低传输时延和更高性能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterVpcAttachment | 系统规定参数。取值：CreateTransitRouterVpcAttachment 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次API 请求的RequestId不一样。 |
| CenId | String | Query | 否 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| TransitRouterId | String | Query | 否 | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env17e-d01 | VPC实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| TransitRouterAttach mentName | String | Query | 否 | testname | VPC连接的名称。 名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）或短划线（-)。 |
| TransitRouterAttach mentDescription | String | Query | 否 | testname | VPC连接的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| VpcId | String | Query | 是 | vpc-bp1kbjcre9vtsebo1**** | VPC实例ID。 |
| VpcOwnerId | Long | Query | 否 | 1250123456123456 | VPC实例所属的一级组织UID。默认值为当前使用的一级组织UID。 如果您要加载跨账号的网络实例，本参数必填。 |
| ChargeType | String | Query | 否 |  |  |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认值）：发送正常请求，通过检查后直接创建VPC连接。 true：发送检查请求，只进行校验，不会创建 VPC连接。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。 如果检查通过，则返回错误码 DryRunOperation 。 |
| ZoneMappings | RepeatList | Query | 是 |  | 请在转发路由器的可用区中选择一个交换机实例。 一次最多支持添加10组信息。 |
| -VSwitchId | String |  | 是 | vsw-bp1a214sbus8z3b54**** | 在转发路由器支持的可用区中选择一个交换机实例。 一次最多支持为10个可用区选择交换机实例。 |
| -ZoneId | String |  | 是 | cn-qingdao-env17e-amtest17001-a | 转发路由器支持的可用区的ID。 您可以通过专有网络产品的DescribeZones接口查询可用区的ID。 一次最多支持选择10个可用区。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | tagtest | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| -Value | String |  | 否 | tagtest | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |
|---|---|---|---|---|---|

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterAttachmentI d | String | tr-attach-ia340z7xis7t5s**** | VPC连接ID。 |
| RequestId | String | C087A369-82B9-43EF-91F4- 4B63A9C6E6B6 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterVpcAttachment &VpcId=vpc-bp1kbjcre9vtsebo1****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TransitRouterAttachmentId":"tr-attach-ia340z7xis7t5s****", "RequestId":"C087A369-82B9-43EF-91F4-4B63A9C6E6B6" } |  |

| XML | 格式 |
|---|---|
| <TransitRouterAttachmentId>tr-attach-ia340z7xis7t5s****</TransitRouterAttachmentId> <RequestId>C087A369-82B9-43EF-91F4-4B63A9C6E6B6</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONALREADYA _ _ _ TTACHEDCENPROTECTIONLEV _ _ _ ELFULL _ | InvalidStatus.VpcAttachedFullModeCen | Operation is invalid because the instance has already attached to other cen with protection level FULL |
| 400 | ATTACHACROSSBIDFORBIDDE _ _ _ N | Forbbiden.AttachChildInstanceAcrossBid | Operation is invalid, please apply for cross-bid attaching. |
| 400 | OperationUnsupported.TransitRo uterRegionId | OperationUnsupported.TransitRouterRegionId | The specified TransitRouterRegion does not support the operation. |
| 400 | NoPermission.AliyunServiceRoleF orCEN | NoPermission.AliyunServiceRoleForCEN | You are not authorized to create the service linked role. Role Name: AliyunServiceRoleForCEN. Service Name: cen.aliyuncs.com. Make sure that the user has been granted the ram:CreateServiceLinkedRole permission. |
| 400 | PARAMETERILLEGALRESOURCE _ _ REGIONID _ | IllegalParam.RegionId | The Specified Parameter RegionId is illegal |
| 400 | MissingParam.CenId or RegionId | MissingParam.CenIdOrRegionId | Either CenId or RegionId must be specified. |
| 400 | IllegalParam.ZoneId | IllegalParam.ZoneId | The specified ZoneId is illegal. |
| 400 | IllegalParam.ChargeType | IllegalParam.ChargeType | The specified ChargeType is illegal. |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | The specified TransitRouterId is not found. |
| 400 | INVALIDOPERATIONRESOURCE _ _ _ ATTACHMENTSTATUS _ | IncorrectStatus.Attachment | The resource is not in a valid state for the attachment operation. |

| 400 | INVALIDVPCSTATUS _ _ | IncorrectStatus.Vpc | The resource is not in a valid state for the attachment operation. |
|---|---|---|---|
| 400 | UNESPECTEDVPCRESULT _ _ | IncorrectStatus.VpcOrVswitch | The Vpc Or Vswith is not in a valid state for the attachment operation. |
| 400 | NOTSUPPORTVPCAUTOPUBLIS _ _ _ _ HROUTE _ | OperationNotSupport.VpcAutoRoutesPublish | Auto publish vpc routes is not supported in this region. |
| 400 | INVALIDOPERATIONCENALREA _ _ _ DYAUTOPUBLISHROUTETOIN _ _ _ _ _ STANCE | InvalidOperation.VpcAutoRoutesPublishInOtherCEN | The operation is not supported because the VPC is already set autoRoutesPublish in other CEN. |
| 400 | QUOTAFULLPERTRVPCAUTO _ _ _ _ _ _ ROUTE | QuotaExceeded.VpcAutoRoutesPublishPerTransitRou ter | The count of VPC instance which set autoRoutesPublish in transitRouter is over limit. |
| 400 | VPNASSOCIATED _ | InvalidOperation.VpnAssociated | The operation is not supported because the VPC is associated with VPN. |
| 400 | USERNOTOPENTRSERVICE _ _ _ _ | Forbbiden.TransitRouterServiceNotOpen | The user has not open transit router service. |
| 400 | PARAMETERILLEGALZONEMAP _ _ _ PINGS | IllegalParam.ZoneMappings | The Specified Parameter ZoneMappings is illegal |
| 400 | OperationUnsupported.TransitRo uterType | OperationUnsupported.TransitRouterType | The specified TransitRouterType does not support the operation. |
| 400 | InvalidCenId.NotFound | InvalidCenId.NotFound | CenId is not found. |
| 400 | IllegalParam.VSwitchId | IllegalParam.VSwitchId | VSwitchId is illegal. |
| 400 | InvalidVSwitchId.NotFound | InvalidVSwitchId.NotFound | VSwitchId is not found. |
| 400 | IllegalParam.RegionId | IllegalParam.RegionId | RegionId is illegal. |
| 400 | IncorrectStatus.TransitRouter | IncorrectStatus.TransitRouterInstance | The status of TransitRouter is incorrect. |
| 400 | CENFULLLEVELNOTSUPPORT _ _ _ _ _ TR | OperationUnsupported.CenFullLevel | CEN full level does not support TransitRouter |

#### 1.5.2. UpdateTransitRouterVpcAttachmentAttribute

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | UpdateTransitRouterVpcAttachmentAttrib ute | 系统规定参数。取值：UpdateTransitRouterVpcAttachme ntAttribute 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-nls9fzkfat8934**** | VPC连接ID。 |
| TransitRouterAttac hmentName | String | Query | 否 | testname | VPC连接的名称。 名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）或短划线（-)。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TransitRouterAttac hmentDescription | String | Query | 否 | testdesc | VPC连接的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false （默认值）：发送正常请求，通过检查后直接修改VPC连接的名称和描述信息。 true ：发送检查请求，只进行校验，不会修改VPC连接的名称和描述信息。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E61D334-4025-41EF-9145- FC327B35301D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouterVpcAttachmentAttribute &TransitRouterAttachmentId=tr-attach-nls9fzkfat8934****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"7E61D334-4025-41EF-9145-FC327B35301D" } |  |

| XML | 格式 |
|---|---|
| <RequestId>7E61D334-4025-41EF-9145-FC327B35301D</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectStatus.TransitRouterAtta chmentId | IncorrectStatus.TransitRouterAttachmentId | TransitRouterAttachmentId status is invalid. |
| 400 | InvalidTransitRouterAttachmentId .NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | NOTSUPPORTVPCAUTOPUBLI _ _ _ _ SHROUTE _ | InvalidOperation.RegionNotSupport | The operation is not supported in this region. |
| 400 | INVALIDOPERATIONCENALREA _ _ _ DYAUTOPUBLISHROUTETOIN _ _ _ _ _ STANCE | InvalidOperation.VpcAutoRoutesPublishInOtherCEN | The operation is not supported because the VPC is already set autoRoutesPublish in other CEN. |
| 400 | QUOTAFULLPERTRVPCAUTO _ _ _ _ _ ROUTE _ | QuotaExceeded.VpcAutoRoutesPublishPerTransitRou ter | The count of VPC instance which set autoRoutesPublish in transitRouter is over limit. |
| 400 | VPNASSOCIATED _ | InvalidOperation.VpnAssociated | The operation is not supported because the VPC is associated with VPN. |

#### 1.5.3. ListTransitRouterVpcAttachments

查询转发路由器下专有网络VPC（Virtual Private Cloud）连接的信息。

**使用说明**

通过云企业网实例ID和转发路由器实例所属地域ID查询该转发路由器实例下所有VPC连接的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterVpcAttachments | 系统规定参数。取值：ListTransitRouterVpcAttachments。 |
| CenId | String | Query | 否 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env66-d01 | 转发路由器实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| TransitRouterAttach mentId | String | Query | 否 | tr-attach-nls9fzkfat8934**** | VPC连接ID。 |
| TransitRouterId | String | Query | 否 | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时每次显示的条目数。默认值为20。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| VpcId | String | Query | 否 | vpc-bp1kbjcre9vtsebo1**** | VPC实例ID。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | tagtest | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | tagtest | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterAttachments | Array |  | VPC连接信息列表。 |
| -ZoneMappings | Array |  | VPC连接的可用区信息及其关联的VPC实例的交换机和弹性网卡的信息。 |
| --ZoneId | String | cn-qingdao-env17e- amtest17001-a | 可用区ID。 |
| --VSwitchId | String | vsw-bp1a214sbus8z3b54**** | 交换机ID。 |
| --NetworkInterfaceId | String | eni-bp149hmyaqegerml**** | 转发路由器在交换机中创建的弹性网卡的ID。 |
| -Tags | Array |  | 标签键。 |
| --Key | String | tagtest | 资源的标签键。 |
| --Value | String | tagtest | 资源的标签值。 |
| -CreationTime | String | 2021-06-15T02:14Z | VPC连接的创建时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为：YYYY-MM- DDThh:mmZ。 |

| -Status | String | Attached | VPC连接的状态。 Attached：已加载。 Attaching：加载中。 Detaching：卸载中。 |
|---|---|---|---|
| -VpcId | String | vpc-bp1h8vbrbcgohcju5**** | VPC实例ID。 |
| - TransitRouterAttachmentI d | String | tr-attach-nls9fzkfat8934**** | VPC连接ID。 |
| -TransitRouterId | String | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| -ResourceType | String | VPC | 连接所属的资源类型。 仅取值：VPC，表示专有网络实例。 |
| - TransitRouterAttachment Description | String | testdesc | VPC连接的描述信息。 |
| -VpcOwnerId | Long | 1250123456123456 | VPC实例所属一级组织UID。 |
| -VpcRegionId | String | cn-qingdao-env17e-d01 | VPC实例所属地域ID。 |
| - TransitRouterAttachment Name | String | testname | VPC连接的名称。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | C97FF53F-3EF8-4883-B459- 60E171924B23 | 请求ID。 |
| TotalCount | Integer | 1 | 总条目数。 |
| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterVpcAttachments
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"C97FF53F-3EF8-4883-B459-60E171924B23",
 "MaxResults":20,
 "TransitRouterAttachments":{
  "Status":"Attached",
  "TransitRouterAttachmentId":"tr-attach-nls9fzkfat8934****",
  "-Tags":{
   "Value":"tagtest",
   "Key":"tagtest"
  },
  "TransitRouterAttachmentName":"testname",
  "ResourceType":"VPC",
  "VpcOwnerId":1250123456123456,
  "VpcId":"vpc-bp1h8vbrbcgohcju5****",
  "CreationTime":"2021-06-15T02:14Z",
  "VpcRegionId":"cn-qingdao-env17e-d01",
  "-ZoneMappings":{
   "ZoneId":"cn-qingdao-env17e-amtest17001-a",
   "VSwitchId":"vsw-bp1a214sbus8z3b54****",
   "NetworkInterfaceId":"eni-bp149hmyaqegerml****"
  },
  "TransitRouterAttachmentDescription":"testdesc",
  "TransitRouterId":"tr-bp1su1ytdxtataupl****"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>C97FF53F-3EF8-4883-B459-60E171924B23</RequestId> <MaxResults>20</MaxResults> <TransitRouterAttachments> <Status>Attached</Status> <TransitRouterAttachmentId>tr-attach-nls9fzkfat8934****</TransitRouterAttachmentId> <-Tags> <Value>tagtest</Value> <Key>tagtest</Key> </-Tags> <TransitRouterAttachmentName>testname</TransitRouterAttachmentName> <ResourceType>VPC</ResourceType> <VpcOwnerId>1250123456123456</VpcOwnerId> <VpcId>vpc-bp1h8vbrbcgohcju5****</VpcId> <CreationTime>2021-06-15T02:14Z</CreationTime> <VpcRegionId>cn-qingdao-env17e-d01</VpcRegionId> <-ZoneMappings> <ZoneId>cn-qingdao-env17e-amtest17001-a</ZoneId> <VSwitchId>vsw-bp1a214sbus8z3b54****</VSwitchId> <NetworkInterfaceId>eni-bp149hmyaqegerml****</NetworkInterfaceId> </-ZoneMappings> <TransitRouterAttachmentDescription>testdesc</TransitRouterAttachmentDescription> <TransitRouterId>tr-bp1su1ytdxtataupl****</TransitRouterId> </TransitRouterAttachments> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The specified NextToken is invalid. |
| 400 | IllegalParam.TrInstance | IllegalParam.TrInstance | The specified TransitRouter is invalid. |
| 400 | IllegalParam.Region | IllegalParam.Region | The specified Region is invalid. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is invalid. |
| 400 | IllegalParam.TransitRouterId | IllegalParam.TransitRouterId | The specified TransitRouterId is invalid. |
| 400 | IllegalParam.CenId Or RegionId | IllegalParam.CenIdOrRegionId | The specified CenId or RegionId is invalid. |

#### 1.5.4. DeleteTransitRouterVpcAttachment

删除转发路由器下的专有网络VPC（Virtual Private Cloud）连接。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-ia340z7xis7t5s**** | VPC连接ID。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false （默认值）：发送正常请求，通过检查后直接删除VPC连接。 true ：发送检查请求，只进行校验，不会删除VPC连接。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |
| Force | Boolean | Query | 否 | false | 是否强制删除VPC连接，取值： false （默认值）：删除VPC连接前校验是否存在相关资源依赖，如关联转发、路由学习等。如果存在相关依赖，则不允许删除，返回对应错误。 true ：删除VPC连接时，默认删除所有相关依赖。 |
| Action | String | Query | 否 | DeleteTransitRouterVpcAttachment | 系统规定参数。取值：DeleteTransitRouterVpcAttachme nt 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 7E61D334-4025-41EF-9145- FC327B35301D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterVpcAttachment &TransitRouterAttachmentId=tr-attach-ia340z7xis7t5s****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"7E61D334-4025-41EF-9145-FC327B35301D" } |  |

| XML | 格式 |
|---|---|
| <RequestId>7E61D334-4025-41EF-9145-FC327B35301D</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ATTACHMENTREFERENCEDBY _ _ _ VPCROUTEENTRY _ _ | OperationFailed.AttachmentReferencedVpcRouteEnt ryExisted | Operation is failed because there is at least one route entry which next hop is the specified attachment. |
| 400 | OperationFailed.RouteTableAssoc iationExist | OperationFailed.RouteTableAssociationExist | Operation failed because TransitRouterRouteTable exists |
| 400 | OperationFailed.RouteTablePropa gationExist | OperationFailed.RouteTablePropagationExist | The specified TransitRouterAttachment has configured RouteTablePropagation. Please remove the configuration first. |
| 400 | INVALIDOPERATIONMULTICAST _ _ DOMAINASSOCIATIONEXIST _ _ _ | OperationFailed.MulticastDomainAssociationExist | The specified TransitRouterAttachment has configured MulticastDomainAssociation. Please remove the configuration first. |

| 转发路由器 |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCode | 错误码 | 错误信息 | 描述 |

| 400 | OperationUnsupported.TransitRo uterType | OperationUnsupported.TransitRouterType | The specified TransitRouterType does not support the operation. |
|---|---|---|---|
| 400 | INVALIDOPERATIONPREFIXLIST _ _ _ EXIST | OperationFailed.PrefixListExist | Operation failed because PrefixList exists. |
| 400 | InvalidTrAttachmentId.NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | VPCROUTEENTRYSTATUSERR _ _ _ _ OR | IncorrectStatus.VpcRouteEntry | The resource is not in a valid state for the attachment operation. |
| 400 | VPCSWITCHSTATUSERROR _ _ _ | IncorrectStatus.VpcSwitch | The resource is not in a valid state for the attachment operation. |
| 400 | VPCROUTEENTRYSTATUSERR _ _ _ _ OR | IncorrectStatus.VpcRouteEntry | The resource is not in a valid state for the attachment operation. |
| 400 | VPCSWITCHSTATUSERROR _ _ _ | IncorrectStatus.VpcSwitch | The resource is not in a valid state for the attachment operation. |
| 400 | UNESPECTEDVPCRESULT _ _ | IncorrectStatus.Vpc | The resource is not in a valid state for the operation. |
| 400 | OperationFailed.RouteEntryExist | OperationFailed.RouteEntryExist | Operation failed because the TransitRouterAttachment exists in RouteTable. |

#### 1.5.5. UpdateTransitRouterVpcAttachmentZones

修改专有网络VPC（Virtual Private Cloud）连接关联的可用区和交换机。

**使用说明**

在为VPC连接添加可用区和交换机时，请确保交换机中拥有一个空闲的IP地址，在修改过程中，转发路由器将在交换机中创建一个弹性网卡 ENI（Elastic Network Interface）（该ENI将占用交换机下的一个IP地址），作为VPC实例与转发路由器流量互通的接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 |  | 系统规定参数。取值：UpdateTransitRouterVpcAttachme ntZones 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-42665544**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会修改VPC连接的可用区和交换机。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接修改VPC连接的可用区和交换机。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-9bbqyygouv4cpn**** | VPC连接ID。 |
| AddZoneMappings | RepeatList | Query | 否 |  | 待为VPC连接添加的可用区和交换机列表。 |
| -VSwitchId | String |  | 否 | vsw-wz9f5izl6wshndmta**** | 待为VPC连接添加的交换机ID。 一次最多支持添加 10 个交换机。 如果您当前使用的组织与VPC实例属于同一个组织，您可以调用专有网络产品 DescribeVSwitches接口查询VPC实例下交换机ID及其所属可用区的ID。 如果您当前使用的组织与VPC实例属于不同的组织，您可以调用 ListGrantVSwitchesToCen接口查询VPC实例下交换机ID及其所属可用区的ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -ZoneId | String |  | 否 | cn-qingdao-env17e-amtest17001-a | 待为VPC连接添加的交换机所属的可用区 ID。 一次最多支持添加10个交换机。 |
| RemoveZoneMappi ngs | RepeatList | Query | 否 |  | 待为VPC连接删除的可用区和交换机列表。 |
| -VSwitchId | String |  | 否 | vsw-wz9f5izl6wshndmta**** | 待为VPC连接删除的交换机ID。 一次最多支持删除10个交换机。 |
| -ZoneId | String |  | 否 | cn-qingdao-env17e-amtest17001-a | 待为VPC连接删除的交换机所属的可用区ID。 一次最多支持删除10个交换机。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 595AE52F-49FF-5788-A677- 0DD1467941A1 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouterVpcAttachmentZones &TransitRouterAttachmentId=tr-attach-9bbqyygouv4cpn****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"595AE52F-49FF-5788-A677-0DD1467941A1" } |  |

| XML | 格式 |
|---|---|
| <RequestId>595AE52F-49FF-5788-A677-0DD1467941A1</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.ZoneId | IllegalParam.ZoneId | The specified ZoneId is illegal. |
| 400 | IncorrectStatus.TransitRouterAtta chmentId | IncorrectStatus.TransitRouterAttachment | The status of TransitRouterAttachment is incorrect. |
| 400 | IllegalParam.VSwitchId | IllegalParam.VSwitchId | VSwitchId is illegal. |
| 400 | InvalidTransitRouterAttachmentId .NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | OperationUnsupported.ServiceMo de | OperationUnsupported.ServiceMode | The specified TransitRouter does not support the operation. |
| 400 | IllegalParam.AddZoneMappings Or RemoveZoneMappings | IllegalParam.AddOrRemoveZoneMappings | The specified AddZoneMappings or RemoveZoneMappings are illegal. |
| 400 | IncorrectStatus.VpcCbnStatus | IncorrectStatus.Vpc | The resource is not in a valid state for the attachment operation. |
| 400 | OperationDenied.RouteEntryOnE ni | OperationDenied.RouteEntryOnEni | Operation is failed because there is at least one route entry which next hop is the specified eni. |
| 400 | VPCROUTEENTRYSTATUSERR _ _ _ _ OR | IncorrectStatus.VpcRouteEntry | The resource is not in a valid state for the attachment operation. |
| 400 | VPCSWITCHSTATUSERROR _ _ _ | IncorrectStatus.VpcSwitch | The resource is not in a valid state for the attachment operation. |
| 404 | InvalidZoneId.NotFound | IllegalParam.ZoneId | The specified ZoneId is illegal. |

#### 1.5.6. ListGrantVSwitchesToCen

查询云企业网实例已连接的跨账号专有网络VPC（Virtual Private Cloud）下交换机的信息。

**使用说明**

在调用ListGrantVSwitchesToCen接口前，请确保云企业网实例已获得跨账号VPC实例的授权。具体操作，请参见GrantInstanceToCen。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListGrantVSwitchesToCen | 系统规定参数。取值：ListGrantVSwitchesToCen 。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | VPC实例所属地域ID。 您可以调用DescribeChildInstanceRegions接口获取地域ID。 |
| CenId | String | Query | 是 | cen-44m0p68spvlrqq**** | 云企业网实例ID。 |
| VpcId | String | Query | 是 | vpc-bp12ge2tq5gzdc915**** | VPC实例ID。 |
| PageNumber | Integer | Query | 否 | 1 | 列表的页码。默认值：1 。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。取值范围：1 ~50 。默认值：10 。 |
| ZoneId | String | Query | 否 | cn-qingdao-env17e-amtest17001-a | 可用区ID。 如果您指定可用区ID，则系统只查询VPC实例位于当前可用区的交换机的信息。 如果您不指定可用区ID，则系统默认查询该 VPC实例位于所有可用区的交换机的信息。 您可以调用专有网络产品DescribeZones接口获取可用区ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| VSwitches | Array |  | 交换机信息列表。 |
| -VpcId | String | vpc-bp12ge2tq5gzdc915**** | 交换机所属的VPC实例ID。 |
| -ZoneId | String | cn-qingdao-env17e- amtest17001-a | 交换机所属的可用区ID。 |
| -VSwitchId | String | vsw-bp1194lh263wx1gsk**** | 交换机实例ID。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |
| RequestId | String | A9288C78-881A-5D30-A8A9- 68E05EE0A086 | 请求ID。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| TotalCount | Integer | 2 | 列表的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListGrantVSwitchesToCen &RegionId=cn-qingdao-env17e-d01 &CenId=cen-44m0p68spvlrqq**** &VpcId=vpc-bp12ge2tq5gzdc915****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":2,
 "PageSize":10,
 "RequestId":"A9288C78-881A-5D30-A8A9-68E05EE0A086",
 "PageNumber":1,
 "VSwitches":{
  "VpcId":"vpc-bp12ge2tq5gzdc915****",
  "ZoneId":"cn-qingdao-env17e-amtest17001-a",
  "VSwitchId":"vsw-bp1194lh263wx1gsk****"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>2</TotalCount> <PageSize>10</PageSize> <RequestId>A9288C78-881A-5D30-A8A9-68E05EE0A086</RequestId> <PageNumber>1</PageNumber> <VSwitches> <VpcId>vpc-bp12ge2tq5gzdc915****</VpcId> <ZoneId>cn-qingdao-env17e-amtest17001-a</ZoneId> <VSwitchId>vsw-bp1194lh263wx1gsk****</VSwitchId> </VSwitches> |  |

### VBR连接

#### 1.6.1. CreateTransitRouterVbrAttachment

在转发路由器下创建边界路由器VBR（Virtual border router）连接。

**使用说明**

创建VBR连接后，VBR连接默认不与任何转发路由器路由表建立路由学习关系和关联转发关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterVbrAttachment | 系统规定参数。取值：CreateTransitRouterVbrAttachment 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| CenId | String | Query | 否 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| TransitRouterId | String | Query | 否 | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env17e-d01 | VBR实例所属地域ID。 您可以通过调用专有网络产品DescribeRegions 接口获取地域ID。 |
| TransitRouterAttach mentName | String | Query | 否 | testname | VBR连接名称。 名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）或短划线（-)。 |
| TransitRouterAttach mentDescription | String | Query | 否 | testdesc | VBR连接描述。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| VbrId | String | Query | 是 | vbr-bp1svadp4lq38janc**** | VBR实例ID。 |

| VbrOwnerId | Long | Query | 否 | 1250123456123456 | VBR实例所属一级组织UID。默认值为当前使用的组织UID。 如果您要加载跨账号的网络实例，本参数必填。 |
|---|---|---|---|---|---|
| AutoPublishRouteEn abled | Boolean | Query | 否 | false | 是否使转发路由器自动发布路由到VBR实例。 false（默认值）：否。 true：是。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认值）：发送正常请求，通过检查后直接创建VBR连接。 true：发送检查请求，只进行校验，不会创建 VBR连接。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。 如果检查通过，则返回对应请求ID。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | TagKey | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | TagValue | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterAttachmentI d | String | tr-attach-ia340z7xis7t5s**** | VBR连接ID。 |
| RequestId | String | C087A369-82B9-43EF-91F4- 4B63A9C6E6B6 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterVbrAttachment &VbrId=vbr-bp1svadp4lq38janc****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TransitRouterAttachmentId":"tr-attach-ia340z7xis7t5s****", "RequestId":"C087A369-82B9-43EF-91F4-4B63A9C6E6B6" } |  |

| XML | 格式 |
|---|---|
| <TransitRouterAttachmentId>tr-attach-ia340z7xis7t5s****</TransitRouterAttachmentId> <RequestId>C087A369-82B9-43EF-91F4-4B63A9C6E6B6</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

| 400 | NoPermission.AliyunServiceRoleP olicyForCEN | NoPermission.AliyunServiceRolePolicyForCEN | You are not authorized to create the service linked role. Role Name: AliyunServiceRolePolicyForCEN. Service Name: cen.aliyuncs.com. Make sure that the user has been granted the ram:CreateServiceLinkedRole permission. |
|---|---|---|---|
| 400 | OperationUnsupported.TransitRo uterRegionId | OperationUnsupported.TransitRouterRegionId | The specified TransitRouterRegion does not support the operation. |
| 400 | InvalidCenId.NotFound | InvalidCenId.NotFound | CenId is not found. |
| 400 | INVALIDOPERATIONRESOURCE _ _ _ ATTACHMENTSTATUS _ | InvalidStatus.ResourceStatus | The resource is not in a valid state for the attachment operation. |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | TransitRouterId is not found. |
| 400 | USERNOTOPENTRSERVICE _ _ _ _ | Forbbiden.TransitRouterServiceNotOpen | The user has not open transit router service. |
| 400 | OperationUnsupported.TransitRo uterType | OperationUnsupported.TransitRouterType | The specified TransitRouterType does not support the operation. |
| 400 | MissingParam.CenId or RegionId | MissingParam.CenIdOrRegionId | Either CenId or RegionId must be specified. |
| 400 | INVALIDVPCSTATUS _ _ | IncorrectStatus.Vpc | The resource is not in a valid state for the attachment operation. |
| 400 | DEVICEMODELFORBIDDEN _ _ | Forbidden.VbrDeviceModel | Attach VBR on some access device models are forbidden. |
| 403 | INVALIDOPERATIONDEVICEMO _ _ _ DELFORBIDDEN _ | Forbidden.VbrDeviceModel | The attached VBR on some access device models are not supported. Please submit a ticket to continue using this VBR on CEN. |

#### 1.6.2. ListTransitRouterVbrAttachments

查询转发路由器下的边界路由器VBR（Virtual border router）连接信息。

**使用说明**

通过云企业网实例ID和转发路由器实例所属地域ID查询该实例下所有VBR连接的信息。 可以单独通过**TransitRouterAttachmentId**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CenId | String | Query | 否 | cen-j3jzhw1zpau2km**** | 云企业网实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env66-d01 | 转发路由器实例所属地域ID。 您可以通过调用专有网络产品DescribeRegions 接口获取地域ID。 |
| TransitRouterAttac hmentId | String | Query | 否 | tr-attach-oyf70wfuorwx87**** | VBR连接ID。 |
| TransitRouterId | String | Query | 否 | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时，每次显示的最大条目数。默认值为20 。 |
| NextToken | String | Query | 否 | dd20**** | 分批次查询时，下一次查询的Token。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |

| 转发路由器 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Key | String |  | 否 | tagtest | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持 64个字符，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | tagtest | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入20个标签键对应的标签值。 |
| Action | String | Query | 否 | ListTransitRouterVbrAttachments | 系统规定参数。取值：ListTransitRouterVbrAttachment s 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalCount | Integer | 1 | 总条目数。 |
| NextToken | String | dd20**** | 分批次查询时，下一次查询的Token。 |
| RequestId | String | F42D9616-29EB-4E75-8CA8- 9654D4E07501 | 请求ID。 |
| MaxResults | Integer | 20 | 分批次查询时，每次显示的最大条目数。 |
| TransitRouterAttachments | Array |  | VBR连接信息列表。 |
| -Tags | Array |  | 标签列表。 |
| --Key | String | tagtest | 资源的标签键。 |
| --Value | String | tagtest | 资源的标签值。 |
| -CreationTime | String | 2021-06-15T15:20Z | VBR连接的创建时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为：YYYY-MM- DDThh:mmZ。 |
| -Status | String | Attached | VBR连接的状态。 Attached ：已加载。 Attaching ：加载中。 Detaching ：卸载中。 |
| - TransitRouterAttachmentI d | String | tr-attach-oyf70wfuorwx87**** | VBR连接ID。 |
| -TransitRouterId | String | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| -ResourceType | String | VBR | 连接所属的资源类型。 仅取值：VBR ，边界路由器实例。 |
| -VbrRegionId | String | cn-qingdao-env66-d01 | VBR实例所属地域ID。 |
| - TransitRouterAttachment Description | String | testdesc | VBR连接的描述信息。 |
| -VbrOwnerId | Long | 1250123456123456 | VBR实例所属一级组织UID。 |
| -AutoPublishRouteEnabled | Boolean | false | 转发路由器是否自动发布路由到VBR实例。 false （默认值）：否。 true ：是。 |

| 开发指南·API参考 |  |  | 转发路由器 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -VbrId | String | vbr-bp1svadp4lq38janc**** | VBR实例ID。 |
| - TransitRouterAttachment Name | String | testa | VBR连接的名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterVbrAttachments
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "NextToken":"dd20****", "RequestId":"F42D9616-29EB-4E75-8CA8-9654D4E07501", "MaxResults":20, "TransitRouterAttachments":{ "Status":"Attached", "TransitRouterAttachmentId":"tr-attach-oyf70wfuorwx87****", "AutoPublishRouteEnabled":false, "-Tags":{ "Value":"tagtest", "Key":"tagtest" }, "VbrOwnerId":1250123456123456, "CreationTime":"2021-06-15T15:20Z", "TransitRouterAttachmentName":"testa", "ResourceType":"VBR", "VbrRegionId":"cn-qingdao-env66-d01", "VbrId":"vbr-bp1svadp4lq38janc****", "TransitRouterAttachmentDescription":"testdesc", "TransitRouterId":"tr-bp1su1ytdxtataupl****" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>dd20****</NextToken> <RequestId>F42D9616-29EB-4E75-8CA8-9654D4E07501</RequestId> <MaxResults>20</MaxResults> <TransitRouterAttachments> <Status>Attached</Status> <TransitRouterAttachmentId>tr-attach-oyf70wfuorwx87****</TransitRouterAttachmentId> <AutoPublishRouteEnabled>false</AutoPublishRouteEnabled> <-Tags> <Value>tagtest</Value> <Key>tagtest</Key> </-Tags> <VbrOwnerId>1250123456123456</VbrOwnerId> <CreationTime>2021-06-15T15:20Z</CreationTime> <TransitRouterAttachmentName>testa</TransitRouterAttachmentName> <ResourceType>VBR</ResourceType> <VbrRegionId>cn-qingdao-env66-d01</VbrRegionId> <VbrId>vbr-bp1svadp4lq38janc****</VbrId> <TransitRouterAttachmentDescription>testdesc</TransitRouterAttachmentDescription> <TransitRouterId>tr-bp1su1ytdxtataupl****</TransitRouterId> </TransitRouterAttachments> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The specified NextToken is invalid. |
| 400 | IllegalParam.TrInstance | IllegalParam.TrInstance | The specified TransitRouter is invalid. |
| 400 | IllegalParam.Region | IllegalParam.Region | The specified Region is invalid. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is invalid. |
| 400 | IllegalParam.TransitRouterId | IllegalParam.TransitRouterId | The specified TransitRouterId is invalid. |
| 400 | IllegalParam.CenId Or RegionId | IllegalParam.CenIdOrRegionId | The specified CenId or RegionId is invalid. |

#### 1.6.3. UpdateTransitRouterVbrAttachmentAttribute

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | UpdateTransitRouterVbrAttachmentAttrib ute | 系统规定参数。取值：UpdateTransitRouterVbrAttachme ntAttribute 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-oyf70wfuorwx87**** | VBR连接ID。 |
| TransitRouterAttac hmentName | String | Query | 否 | testname | VBR连接的新名称。 名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）和短划线 （-）。 |
| TransitRouterAttac hmentDescription | String | Query | 否 | testdesc | VBR连接新的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |
| AutoPublishRouteE nabled | Boolean | Query | 否 | true | 是否允许转发路由器向VBR实例中自动发布路由。取值： true ：允许。 false ：禁止。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false （默认值）：发送正常请求，通过检查后直接修改VBR连接的名称和描述信息。 true ：发送检查请求，只进行校验，不会修改VBR连接的配置信息。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 91B36DC3-FF8A-45C3-AC1E- 456B1789136D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouterVbrAttachmentAttribute &TransitRouterAttachmentId=tr-attach-oyf70wfuorwx87****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"91B36DC3-FF8A-45C3-AC1E-456B1789136D" } |  |

| XML | 格式 |
|---|---|
| <RequestId>91B36DC3-FF8A-45C3-AC1E-456B1789136D</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterAttachmentId .NotFound | InvalidTransitRouterAttachmentId.NotFound | TransitRouterAttachmentId is not found. |
| 400 | IncorrectStatus.TransitRouterAtta chmentId | IncorrectStatus.TransitRouterAttachment | The status of TransitRouterAttachment is incorrect. |

#### 1.6.4. DeleteTransitRouterVbrAttachment

删除转发路由器下的边界路由器VBR（Virtual border router）连接。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouterVbrAttachment | 系统规定参数。取值：DeleteTransitRouterVbrAttachme nt 。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId 作为ClientToken 标识。每次API请求的RequestId 不一样。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-9nlnjv7by7n7a**** | VBR连接ID。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false （默认值）：发送正常请求，通过检查后直接删除VBR连接。 true ：发送检查请求，只进行校验，不会删除VBR连接。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |
| Force | Boolean | Query | 否 | false | 是否强制删除VBR连接，取值： false （默认值）：删除VBR连接前校验是否存在相关资源依赖，如关联转发、路由学习等。如果存在相关依赖，则不允许删除，返回对应错误。 true ：删除VBR连接时，默认删除所有相关依赖。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3EDA94DE-0AE5-41FC-A91E- 7170E408E0FD | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterVbrAttachment &TransitRouterAttachmentId=tr-attach-9nlnjv7by7n7a****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"3EDA94DE-0AE5-41FC-A91E-7170E408E0FD" } |  |

| XML | 格式 |
|---|---|
| <RequestId>3EDA94DE-0AE5-41FC-A91E-7170E408E0FD</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | OperationFailed.RouteTableAssoc iationExist | OperationFailed.RouteTableAssociationExist | Operation failed because TransitRouterRouteTable exists |
| 400 | OperationFailed.RouteEntryExist | OperationFailed.RouteEntryExist | Operation failed because the TransitRouterAttachment exists in RouteTable. |
| 400 | OperationFailed.RouteTablePropa gationExist | OperationFailed.RouteTablePropagationExist | The specified TransitRouterAttachment has configured RouteTablePropagation. Please remove the configuration first. |
| 400 | VBRATTACHEDVBRHA _ _ _ | OperationFailed.VbrAttachedVbrHa | The operation is failed because of VbrAttachedVbrHa. |
| 400 | OperationFailed.FlowLogExistOrNi sOpened | OperationFailed.FlowLogExistOrNisOpened | Operation failed because FlowLog exists or Nis opened. |
| 400 | OperationUnsupported.TransitRo uterType | OperationUnsupported.TransitRouterType | The specified TransitRouterType does not support the operation. |
| 400 | ATTACHMENTREFERENCEDBY _ _ _ VPCROUTEENTRY _ _ | InstanceReferenced.VpcRouteEntry | The specified attachment is referenced by vpc route entry. |

### Connect连接

#### 1.7.1. CreateTransitRouterConnectAttachment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterConnectAttachment | 系统规定参数。取值：CreateTransitRouterConnectAttac hment 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-42665544**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会创建Connect 连接。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接创建Connect连接。 |
| CenId | String | Query | 否 | cen-a7syd349kne38g**** | 云企业网实例ID。 |
| TransitRouterId | String | Query | 否 | tr-p0wr9p28r92d598y6**** | 转发路由器实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env17e-d01 | 转发路由器所属地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| TransitRouterAttac hmentName | String | Query | 否 | nametest | Connect连接的名称。 名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）和短划线（-)。 |
| TransitRouterAttac hmentDescription | String | Query | 否 | desctest | Connect连接的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceId | String | Query | 否 | vbr-group-iz5egnzmcm7wwv**** | 传输通道关联的资源ID。 当前参数暂不支持配置，系统默认基于转发路由器实例下的所有VBR连接传输 Connect连接的流量。 |
| ResourceOwnerUid | Long | Query | 否 | 1250123456123456 | 传输通道关联的资源所属的一级组织UID。 当前参数暂不支持配置，系统默认基于转发路由器实例下的所有VBR连接建立 Connect连接。 |
| Protocol | String | Query | 否 | gre | 隧道封装协议。仅取值：gre 。 |
| TransportType | String | Query | 否 | AllVbr | 传输通道类型。仅取值：AllVbr ，表示系统将通过转发路由器下的所有VBR连接建立 Connect连接。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterAttachmentI d | String | tr-attach-8b586cj3ugv12r**** | Connect连接ID。 |
| RequestId | String | 8B5DD40A-3A29-5AC0-B8DA- 05FD10D5C893 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterConnectAttachment
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TransitRouterAttachmentId":"tr-attach-8b586cj3ugv12r****", "RequestId":"8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893" } |  |

| XML | 格式 |
|---|---|
| <TransitRouterAttachmentId>tr-attach-8b586cj3ugv12r****</TransitRouterAttachmentId> <RequestId>8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893</RequestId> |  |

#### 1.7.2. UpdateTransitRouterConnectAttachmentAttribute

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | UpdateTransitRouterConnectAttachmentA ttribute | 系统规定参数。取值：UpdateTransitRouterConnectAtta chmentAttribute 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-42665544**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会修改Connect 连接的配置。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过， 则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接修改Connect连接的配置。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-8b586cj3ugv12r**** | Connect连接ID。 |
| TransitRouterAttac hmentName | String | Query | 否 | nametest | Connect连接的新名称。 名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）和短划线（-)。 |
| TransitRouterAttac hmentDescription | String | Query | 否 | desctest | Connect连接新的描述信息。 描述长度为2~256个字符，必须以字母或中文开头，但不能以 http:// 或 https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0876E54E-3E36-5C31-89F0- 9EE8A9266F9A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouterConnectAttachmentAttribute &TransitRouterAttachmentId=tr-attach-8b586cj3ugv12r****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"0876E54E-3E36-5C31-89F0-9EE8A9266F9A" } |  |

| XML | 格式 |
|---|---|
| <RequestId>0876E54E-3E36-5C31-89F0-9EE8A9266F9A</RequestId> |  |

#### 1.7.3. ListTransitRouterConnectAttachments

**使用说明**

通过输入**CenId** 和**RegionId** 通过输入**TransitRouterId** 通过输入**TransitRouterAttachmentId**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterConnectAttachments | 系统规定参数。取值：ListTransitRouterConnectAttachm ents 。 |
| CenId | String | Query | 否 | cen-a7syd349kne38g**** | 云企业网实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env17e-d01 | 转发路由器实例所属的地域ID。 您可以通过调用专有网络产品DescribeRegions 接口获取地域ID。 |

| 开发指南·API参 | 考 |  |  |  | 转发路由器 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TransitRouterAttac hmentId | String | Query | 否 | tr-attach-8b586cj3ugv12r**** | Connect连接ID。 |
| TransitRouterId | String | Query | 否 | tr-p0wr9p28r92d598y6**** | 转发路由器实例ID。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时每次显示的条目数。默认值：20 。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken 值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterAttachments | Array |  | Connect连接信息列表。 |
| -CreationTime | String | 2022-12-12T07:31Z | 创建Connect连接的时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为： YYYY-MM- DDThh:mmZ 。 |
| -Status | String | Attached | Connect连接的状态。 Attaching ：加载中。 Attached ：已加载。 Modifying ：修改中。 Detaching ：卸载中。 |
| - TransitRouterAttachmentI d | String | tr-attach-8b586cj3ugv12r**** | Connect连接ID。 |
| -TransitRouterId | String | tr-p0wr9p28r92d598y6**** | 转发路由器实例ID。 |
| -ResourceOwnerId | Long | 1250123456123456 | 传输通道关联的资源所属的一级组织UID。 |
| -ResourceType | Integer | Connect | 传输通道资源类型。 仅取值：Connect ，表示Connect连接。 |
| - TransitRouterAttachment Description | String | desctest | Connect连接的描述信息。 |
| -ResourceRegionId | String | cn-qingdao-env17e-d01 | 传输通道关联的资源所属的地域ID。 |
| -ResourceId | String | vbr-group-iz5egnzmcm7wwv**** | 传输通道关联的资源ID。 |
| - TransitRouterAttachment Name | String | nametest | Connect连接的名称。 |
| -Protocol | String | gre | 隧道封装协议。 |
| -TransportType | String | AllVbr | 传输通道类型。 仅取值：AllVbr ，表示系统将通过转发路由器下的所有VBR连接建立Connect 连接。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | 0C2EE7A8-74D4-4081-8236- CEBDE3BBCF50 | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 |

|  | DDThh:mmZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterConnectAttachments
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "RequestId":"0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50", "MaxResults":20, "TransitRouterAttachments":{ "Status":"Attached", "TransitRouterAttachmentId":"tr-attach-8b586cj3ugv12r****", "ResourceRegionId":"cn-qingdao-env17e-d01", "ResourceId":"vbr-group-iz5egnzmcm7wwv****", "CreationTime":"2022-12-12T07:31Z", "TransitRouterAttachmentName":"nametest", "ResourceType":Connect, "TransportType":"AllVbr", "Protocol":"gre", "ResourceOwnerId":1250123456123456, "TransitRouterAttachmentDescription":"desctest", "TransitRouterId":"tr-p0wr9p28r92d598y6****" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50</RequestId> <MaxResults>20</MaxResults> <TransitRouterAttachments> <Status>Attached</Status> <TransitRouterAttachmentId>tr-attach-8b586cj3ugv12r****</TransitRouterAttachmentId> <ResourceRegionId>cn-qingdao-env17e-d01</ResourceRegionId> <ResourceId>vbr-group-iz5egnzmcm7wwv****</ResourceId> <CreationTime>2022-12-12T07:31Z</CreationTime> <TransitRouterAttachmentName>nametest</TransitRouterAttachmentName> <ResourceType>Connect</ResourceType> <TransportType>AllVbr</TransportType> <Protocol>gre</Protocol> <ResourceOwnerId>1250123456123456</ResourceOwnerId> <TransitRouterAttachmentDescription>desctest</TransitRouterAttachmentDescription> <TransitRouterId>tr-p0wr9p28r92d598y6****</TransitRouterId> </TransitRouterAttachments> |  |

#### 1.7.4. CreateTransitRouterConnectPeer

创建Connect Peer。

**使用说明**

在创建Connect Peer前，请确保您已经为转发路由器添加了转发路由器地址段。具体操作，请参见CreateTransitRouterCidr。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterConnectPeer | 要执行的操作，取值：CreateTransitRouterConnectPee r 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-42665544**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会创建Connect Peer。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接创建Connect Peer。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-y89r3j7a51xeec**** | Connect连接ID。 |
| TransitRouterConn ectPeerName | String | Query | 否 | nametest | Connect Peer的名称。 |
| TransitRouterConn ectPeerLocalIp | String | Query | 否 | 192.168.0.1 | 转发路由器本地地址。 |
| TransitRouterConn ectPeerPeerIp | String | Query | 是 | 10.0.0.1 | Peer IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterConnectPeer Id | String | tr-connect-peer- ax66ixf6ubbajw**** | Connect Peer ID。 |
| RequestId | String | BCF96FD3-17C1-58DA-B9D6- 2CC347A71D79 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterConnectPeer &TransitRouterAttachmentId=tr-attach-y89r3j7a51xeec**** &TransitRouterConnectPeerPeerIp=10.0.0.1
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TransitRouterConnectPeerId":"tr-connect-peer-ax66ixf6ubbajw****", "RequestId":"BCF96FD3-17C1-58DA-B9D6-2CC347A71D79" } |  |

| XML | 格式 |
|---|---|
| <TransitRouterConnectPeerId>tr-connect-peer-ax66ixf6ubbajw****</TransitRouterConnectPeerId> <RequestId>BCF96FD3-17C1-58DA-B9D6-2CC347A71D79</RequestId> |  |

#### 1.7.5. ListTransitRouterConnectPeers

查询Connect Peer的信息。

**使用说明**

调用ListTransitRouterConnectPeers接口时，请求参数**TransitRouterAttachmentId** 和**TransitRouterConnectPeerId** 需至少输入一个。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterConnectPeers | 系统规定参数。取值：ListTransitRouterConnectPeers 。 |
| TransitRouterAttac hmentId | String | Query | 否 | tr-attach-k4x7usyt7hj719**** | Connect连接ID。 |
| TransitRouterConn ectPeerId | String | Query | 否 | tr-connect-peer-anr505utij7pvr**** | Connect Peer ID。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时每次显示的条目数。默认值：20 。 |

| 转发路由器 |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken 值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterConnectPeer s | Array |  | Connect Peer信息列表。 |
| -CreationTime | String | 2022-12-12T07:31Z | 创建Connect Peer的时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为： YYYY-MM- DDThh:mmZ 。 |
| -Status | String | Active | Connect Peer的状态。 Creating ：创建中。 Active ：可用。 Deleting ：删除中。 |
| - TransitRouterConnectPeer Id | String | tr-connect-peer- anr505utij7pvr**** | Connect Peer ID。 |
| - TransitRouterAttachmentI d | String | tr-attach-k4x7usyt7hj719**** | Connect连接ID。 |
| - TransitRouterConnectPeer Name | String | nametest | Connect Peer的名称。 |
| -TransitRouterId | Long | tr-p0wa3m41xs8806q2n**** | 转发路由器实例ID。 |
| - TransitRouterConnectPeer LocalIp | String | 192.168.0.1 | 转发路由器本地地址。 |
| -CenId | String | cen-wc1026dke30j67**** | 云企业网实例ID。 |
| - TransitRouterConnectPeer PeerIp | String | 10.0.0.1 | Peer IP地址。 |
| -TransitRouterRegionId | String | ap-southeast-2 | 转发路由器所属的地域ID。 您可以通过调用DescribeChildInstanceRegions接口获取地域ID代表的地域信息。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | 23CC4215-69A5-5635-8249- 65AD25B02E91 | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 MaxResults 的值表示当前查询批次下列表条目的数量。 |

|  | DDThh:mmZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterConnectPeers
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"23CC4215-69A5-5635-8249-65AD25B02E91",
 "MaxResults":20,
 "TransitRouterConnectPeers":{
  "Status":"Active",
  "TransitRouterAttachmentId":"tr-attach-k4x7usyt7hj719****",
  "TransitRouterConnectPeerId":"tr-connect-peer-anr505utij7pvr****",
  "TransitRouterConnectPeerName":"nametest",
  "TransitRouterConnectPeerLocalIp":"192.168.0.1",
  "CreationTime":"2022-12-12T07:31Z",
  "CenId":"cen-wc1026dke30j67****",
  "TransitRouterRegionId":"ap-southeast-2",
  "TransitRouterId":tr-p0wa3m41xs8806q2n****,
  "TransitRouterConnectPeerPeerIp":"10.0.0.1"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>23CC4215-69A5-5635-8249-65AD25B02E91</RequestId> <MaxResults>20</MaxResults> <TransitRouterConnectPeers> <Status>Active</Status> <TransitRouterAttachmentId>tr-attach-k4x7usyt7hj719****</TransitRouterAttachmentId> <TransitRouterConnectPeerId>tr-connect-peer-anr505utij7pvr****</TransitRouterConnectPeerId> <TransitRouterConnectPeerName>nametest</TransitRouterConnectPeerName> <TransitRouterConnectPeerLocalIp>192.168.0.1</TransitRouterConnectPeerLocalIp> <CreationTime>2022-12-12T07:31Z</CreationTime> <CenId>cen-wc1026dke30j67****</CenId> <TransitRouterRegionId>ap-southeast-2</TransitRouterRegionId> <TransitRouterId>tr-p0wa3m41xs8806q2n****</TransitRouterId> <TransitRouterConnectPeerPeerIp>10.0.0.1</TransitRouterConnectPeerPeerIp> </TransitRouterConnectPeers> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | MissingParam.TrConnectPeerId Or TrAttachmentId | MissingParam.TrConnectPeerIdOrTrAttachmentId | The parameter TrConnectPeerId Or TrAttachmentId is mandatory. |

#### 1.7.6. DeleteTransitRouterConnectPeer

删除Connect Peer。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouterConnectPeer | 系统规定参数。取值：DeleteTransitRouterConnectPee r 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-42665544**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会删除Connect Peer。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接删除Connect Peer。 |
| TransitRouterConn ectPeerId | String | Query | 否 | tr-connect-peer-y5osf8cbw1d75e**** | Connect Peer ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 8B5DD40A-3A29-5AC0-B8DA- 05FD10D5C893 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterConnectPeer
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893" } |  |

| XML | 格式 |
|---|---|
| <RequestId>8B5DD40A-3A29-5AC0-B8DA-05FD10D5C893</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONMULTICAST _ _ GROUPEXIST _ _ | OperationFailed.MulticastGroupExist | Operation is failed because connect peer exists in multicast groups. |

#### 1.7.7. DeleteTransitRouterConnectAttachment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouterConnectAttachment | 系统规定参数。取值：DeleteTransitRouterConnectAttac hment 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-42665544**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次 API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true ：发送检查请求，不会执行删除操作。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false （默认值）：发送正常请求，通过检查后直接执行删除操作。 |
| TransitRouterAttac hmentId | String | Query | 否 | tr-attach-r6g0m3epjehw57**** | Connect连接ID。 |
| Force | Boolean | Query | 否 | false | 是否强制删除Connect连接。取值： false （默认值）：删除Connect连接前系统会校验是否存在相关资源依赖，如Connect Peer、组播组等。如果存在相关资源依赖， 则不允许删除，调用接口后系统会返回对应错误信息。 true ：删除Connect连接时，系统默认会删除所有相关资源依赖。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9878790A-5C16-5A59-A6CB- 79B28C04637D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterConnectAttachment
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"9878790A-5C16-5A59-A6CB-79B28C04637D" } |  |

| XML | 格式 |
|---|---|
| <RequestId>9878790A-5C16-5A59-A6CB-79B28C04637D</RequestId> |  |

### 跨账号授权

#### 1.8.1. GrantInstanceToTransitRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | GrantInstanceToTransitRouter | 系统规定参数。取值：GrantInstanceToTransitRouter。 |
| CenId | String | Query | 是 | cen-44m0p68spvlrqq**** | 转发路由器实例所属的云企业网实例ID。 |
| InstanceId | String | Query | 是 | vpc-bp1h8vbrbcgohcju5**** | 网络实例ID。 |
| InstanceType | String | Query | 是 | VPC | 网络实例的类型。取值： VPC：表示VPC实例。 ExpressConnect：表示VBR实例。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 网络实例所属的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| CenOwnerId | Long | Query | 是 | 1250123456123456 | 云企业网实例所属的一级组织UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | C6E5992C-A57B-5A6C-9B26- 568074DC68BA | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GrantInstanceToTransitRouter &CenId=cen-44m0p68spvlrqq**** &InstanceId=vpc-bp1h8vbrbcgohcju5**** &InstanceType=VPC &RegionId=cn-qingdao-env17e-d01 &CenOwnerId=1250123456123456
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"C6E5992C-A57B-5A6C-9B26-568074DC68BA" } |  |

| XML | 格式 |
|---|---|
| <RequestId>C6E5992C-A57B-5A6C-9B26-568074DC68BA</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | USERNOTOPENTRSERVICE _ _ _ _ | Forbbiden.TransitRouterServiceNotOpen | The user has not open transit router service. |
| 400 | NoPermission.AliyunServiceRoleP olicyForCEN | NoPermission.AliyunServiceRoleForCEN | You are not authorized to create the service linked role. Role Name: AliyunServiceRoleForCEN. Service Name: cen.aliyuncs.com. Make sure that the user has been granted the ram:CreateServiceLinkedRole permission. |
| 400 | IllegalParam.CenInstanceId | IllegalParam.CenId | The specified CenId is invalid. |
| 400 | TaskConflict | OperationFailed.TaskConflict | The operation is too frequent, please wait a moment and try again. |
| 400 | InvalidVbr.NotFound | InvalidVbr.NotFound | vbr is not found. |
| 404 | INSTANCENOTEXIST _ _ | InvalidInstanceId.NotFound | InstanceId is not found. |

#### 1.8.2. RevokeInstanceFromTransitRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | RevokeInstanceFromTransitRouter | 系统规定参数。取值：RevokeInstanceFromTransitRouter 。 |
| CenId | String | Query | 是 | cen-44m0p68spvlrqq**** | 转发路由器实例所属的云企业网实例ID。 |
| InstanceId | String | Query | 是 | vpc-bp1h8vbrbcgohcju5**** | 网络实例ID。 |
| InstanceType | String | Query | 是 | VPC | 网络实例的类型。取值： VPC：表示VPC实例。 ExpressConnect：表示VBR实例。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 网络实例所属的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| CenOwnerId | Long | Query | 是 | 1250123456123456 | 云企业网实例所属的一级组织UID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | AA4BFFD1-5090-5896-935F- 4B353557F1A8 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RevokeInstanceFromTransitRouter &CenId=cen-44m0p68spvlrqq**** &InstanceId=vpc-bp1h8vbrbcgohcju5**** &InstanceType=VPC &RegionId=cn-qingdao-env17e-d01 &CenOwnerId=1250123456123456
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"AA4BFFD1-5090-5896-935F-4B353557F1A8" } |  |

| XML | 格式 |
|---|---|
| <RequestId>AA4BFFD1-5090-5896-935F-4B353557F1A8</RequestId> |  |

#### 1.8.3. DescribeGrantRulesToCen

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeGrantRulesToCen | 系统规定参数。取值：DescribeGrantRulesToCen。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 网络实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| CenId | String | Query | 是 | cen-nye53d7p3hzyu4**** | 云企业网实例ID。 |
| ProductType | String | Query | 是 | VPC | 网络实例的类型，取值： VPC：专有网络实例。 VBR：边界路由器实例。 |
| MaxResults | Long | Query | 否 | 20 | 如果您不指定MaxResults参数的值，则表示您不需要分批次查询。调用接口后返回参数MaxResults的值表示列表条目总数。 如果您指定MaxResults参数的值，则表示您需要分批次查询，MaxResults的值表示分批次查询时每次显示的条目数。取值范围：1~100。调用接口后返回参数MaxResults的值表示当前查询批次下列表条目的数量。建议指定MaxResults参数的值为20。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| GrantRules | Array |  | 授权信息列表。 |
| -ChildInstanceType | String | VPC | 网络实例的类型。 VPC：专有网络实例。 VBR：边界路由器实例。 |
| -ChildInstanceRegionId | String | cn-qingdao-env17e-d01 | 网络实例所属地域ID。 |

| -ChildInstanceOwnerId | Long | 1250123456123456 | 网络实例所属的一级组织UID。 |
|---|---|---|---|
| -ChildInstanceId | String | vpc-bp1rgeww9mdstuuar**** | 网络实例ID。 |
| -CenId | String | cen-nye53d7p3hzyu4**** | 云企业网实例ID。 |
| -CenOwnerId | Long | 1210123456123456 | 云企业网实例所属的一级组织UID。 |
| RequestId | String | 4906B209-8613-5C19-9CC9- B7A3FFDA731C | 请求ID。 |
| TotalCount | Long | 1 | 列表条目数。 |
| MaxResults | Long | 20 | 如果您未指定请求参数MaxResults的值，则表示您不需要分批次查询。返回参数MaxResults的值表示列表条目总数。 如果您指定了请求参数MaxResults的值，则表示您需要分批次查询。返回参数MaxResults的值表示当前查询批次下列表条目的数量。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGrantRulesToCen &RegionId=cn-qingdao-env17e-d01 &CenId=cen-nye53d7p3hzyu4**** &ProductType=VPC
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "RequestId":"4906B209-8613-5C19-9CC9-B7A3FFDA731C", "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "MaxResults":20, "GrantRules":{ "ChildInstanceType":"VPC", "OrderType":"", "CenOwnerId":1210123456123456, "CenId":"cen-nye53d7p3hzyu4****", "ChildInstanceOwnerId":1250123456123456, "ChildInstanceId":"vpc-bp1rgeww9mdstuuar****", "ChildInstanceRegionId":"cn-qingdao-env17e-d01" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <RequestId>4906B209-8613-5C19-9CC9-B7A3FFDA731C</RequestId> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <MaxResults>20</MaxResults> <GrantRules> <ChildInstanceType>VPC</ChildInstanceType> <OrderType /> <CenOwnerId>1210123456123456</CenOwnerId> <CenId>cen-nye53d7p3hzyu4****</CenId> <ChildInstanceOwnerId>1250123456123456</ChildInstanceOwnerId> <ChildInstanceId>vpc-bp1rgeww9mdstuuar****</ChildInstanceId> <ChildInstanceRegionId>cn-qingdao-env17e-d01</ChildInstanceRegionId> </GrantRules> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |

| 400 | MissingParameter | MissingParameter | Missing parameter. |
|---|---|---|---|
| 400 | SDK.InvalidRegionId : Can not find endpoint to access. | InvalidParameter.RegionId | The specified Region Id is invalid. |

#### 1.8.4. DescribeGrantRulesToResource

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeGrantRulesToResource | 系统规定参数。取值：DescribeGrantRulesToResource 。 |
| RegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 网络实例所属地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| ResourceId | String | Query | 是 | vpc-p0wfut1iqauelpdpb**** | 网络实例ID。 |
| ProductType | String | Query | 是 | VPC | 网络实例类型。取值： VPC ：表示专有网络VPC（Virtual Private Cloud）实例。 ExpressConnect ：表示边界路由器 VBR（Virtual border router）实例。 |
| MaxResults | Integer | Query | 否 | 20 | 如果您不指定MaxResults 参数的值，则表示您不需要分批次查询。调用该接口后返回参数MaxResults 的值表示列表条目总数。 如果您指定MaxResults 参数的值，则表示您需要分批次查询，MaxResults 的值表示分批次查询时每次显示的条目数。取值范围：1 ~100 。调用该接口后返回参数MaxResults 的值表示当前查询批次下列表条目的数量。建议指定MaxResults 参数的值为20 。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken 值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| GrantRules | Array |  | 授权信息列表。 |
| -CenOwnerId | Long | 1250123456123456 | 云企业网实例所属一级组织UID。 |
| -CenId | String | cen-44m0p68spvlrqq**** | 云企业网实例ID。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | C6E5992C-A57B-5A6C-9B26- 568074DC68BA | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| MaxResults | Integer | 1 | 如果您未指定请求参数MaxResults 的值，则表示您不需要分批次查询。返回参数MaxResults 的值表示列表条目总数。 如果您指定了请求参数MaxResults 的值，则表示您需要分批次查询。返回参数MaxResults 的值表示当前查询批次下列表条目的数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGrantRulesToResource &RegionId=cn-qingdao-env17e-d01 &ResourceId=vpc-p0wfut1iqauelpdpb**** &ProductType=VPC
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "RequestId":"C6E5992C-A57B-5A6C-9B26-568074DC68BA", "MaxResults":1, "GrantRules":{ "CenOwnerId":1250123456123456, "CenId":"cen-44m0p68spvlrqq****" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>C6E5992C-A57B-5A6C-9B26-568074DC68BA</RequestId> <MaxResults>1</MaxResults> <GrantRules> <CenOwnerId>1250123456123456</CenOwnerId> <CenId>cen-44m0p68spvlrqq****</CenId> </GrantRules> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | MissingParameter | MissingParameter | Missing parameter. |
| 400 | SDK.InvalidRegionId : Can not find endpoint to access. | InvalidParameter.RegionId | The specified Region Id is invalid. |

### 自定义路由条目

#### 1.9.1. CreateTransitRouterRouteEntry

在转发路由器的路由表中添加路由条目。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterRouteEntry | 系统规定参数。取值：CreateTransitRouterRouteEntry。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| TransitRouterRoute EntryName | String | Query | 否 | testname | 路由条目的名称。 名称长度为0~128个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_） 和短划线（-）。 |
| TransitRouterRoute EntryDescription | String | Query | 否 | testdesc | 路由条目的描述。 描述可以为空或描述长度为2~256个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、 at（@）、下划线（_）和短划线（-）。 |

| 开发指南·API参 | 考 |  |  |  | 转发路由器 |
|---|---|---|---|---|---|

| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器的路由表ID。 |
|---|---|---|---|---|---|
| TransitRouterRoute EntryNextHopType | String | Query | 是 | BlackHole | 下一跳类型。取值： BlackHole：表示指定该路由条目为黑洞路由。所有去往目标网段的路由均会被丢弃，无需指定具体的下一跳信息。 Attachment：表示指定该路由条目的下一跳为网络实例连接，且需要指定具体的网络实例连接ID。所有去往目标网段的路由均会被转发至指定的网络实例连接。 |
| TransitRouterRoute EntryDestinationCid rBlock | String | Query | 是 | 192.168.0.0/24 | 路由条目的目标网段。 |
| TransitRouterRoute EntryNextHopId | String | Query | 否 | tr-attach-nls9fzkfat8934**** | 路由条目的下一跳所关联的网络实例连接ID。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接创建路由条目。 true：发送检查请求，只进行校验，不会创建路由条目。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。 如果检查通过，则返回对应请求ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterRouteEntryI d | String | rte-75eg4jprkvk0pw**** | 路由条目ID。 |
| RequestId | String | 835E7F4B-B380-4E0F-96A5- 6EA572388047 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterRouteEntry &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50**** &TransitRouterRouteEntryNextHopType=BlackHole &TransitRouterRouteEntryDestinationCidrBlock=192.168.0.0/24
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"835E7F4B-B380-4E0F-96A5-6EA572388047", "TransitRouterRouteEntryId":"rte-75eg4jprkvk0pw****" } |  |

| XML | 格式 |
|---|---|
| <RequestId>835E7F4B-B380-4E0F-96A5-6EA572388047</RequestId> <TransitRouterRouteEntryId>rte-75eg4jprkvk0pw****</TransitRouterRouteEntryId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

| 400 | InvalidTransitRouterRouteTableId. NotFound | InvalidTransitRouterRouteTableId.NotFound | TransitRouterRouteTableId is not found. |
|---|---|---|---|
| 400 | TransitRouterRouteEntryNextHopI d.NotFound | TransitRouterRouteEntryNextHopId.NotFound | TransitRouterRouteEntryNextHopId is not found. |
| 400 | OperationFailed.CreateRouteEntr yWithCCNAttachment | OperationFailed.CreateRouteEntryWithCCNAttachme nt | Operation failed because Create RouteEntry to CCN Attachment does not support. |
| 400 | QuotaExceeded.TransitRouterRou tEntry | QuotaExceeded.TransitRouterRoutEntry | TransitRouterRoutEntry quota exceeded. |
| 400 | IllegalParam.TransitRouterDestin ationCidrBlock | IllegalParam.TransitRouterDestinationCidrBlock | TransitRouterDestinationCidrBlock is illegal. |
| 400 | InstanceExist.TransitRouterRoute Entry | InstanceExist.TransitRouterRouteEntry | The instance TransitRouterRouteEntry already exists. |
| 400 | IncorrectStatus.TransitRouterRou teTable | IncorrectStatus.TransitRouterRouteTable | TransitRouterRouteTable status is invalid. |
| 400 | ParamExclusive.RouteEntryIdAnd RouteTableIdOrDestCidrBlock | ParamExclusive.RouteEntryIdAndTransitRouterRoute TableIdOrDestCidrBlock | RouteEntryId and TransitRouterRouteTableIdOrDestCidrBlock is mutually exclusive. |
| 400 | InvalidDescription | InvalidDescription | Description is invalid. |
| 400 | InvalidName | InvalidName | Name is invalid. |
| 400 | IllegalParam.NextHopType | IllegalParam.NextHopType | The NextHopType is illegal. |
| 400 | MissingParam.TransitRouterRoute EntryNextHopId | MissingParam.TransitRouterRouteEntryNextHopId | The parameter TransitRouterRouteEntryNextHopId is mandatory |
| 400 | InvalidTransitRouterRouteEntryNe xtHopId.NotFound | InvalidTransitRouterRouteEntryNextHopId.NotFound | TransitRouterRouteEntryNextHopId is not found |
| 400 | ROUTECONFLICT _ | OperationFailed.CreateRouteEntryWithSameDestina tionCidrBlock | Operation failed because Create RouteEntry with same destination cidrblock does not support. |
| 400 | InvalidDestinationCidrBlock.NotFo und | InvalidDestinationCidrBlock.NotFound | DestinationCidrBlock is not found. |

#### 1.9.2. UpdateTransitRouterRouteEntry

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | UpdateTransitRouterRouteEntry | 系统规定参数。取值：UpdateTransitRouterRouteEntry。 |
| TransitRouterRoute EntryId | String | Query | 是 | rte-ksssq7kto4wfdx**** | 路由条目ID。 |
| TransitRouterRoute EntryName | String | Query | 否 | testname | 路由条目修改后的名称。 名称长度为0~128个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_） 和短划线（-）。 |

| TransitRouterRoute EntryDescription | String | Query | 否 | testdesc | 路由条目修改后的描述信息。 描述可以为空或描述长度为2~256个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、 at（@）、下划线（_）和短划线（-）。 |
|---|---|---|---|---|---|
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认值）：发送正常请求，通过检查后直接修改路由条目的名称和描述信息。 true：发送检查请求，只进行校验，不会修改路由条目的名称和描述信息。检查项包括是否填写了必需参数、请求格式等。如果检查不通过， 则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2D69CCEA-42D0-48B2-8C9A- 9BB207F76D6E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouterRouteEntry &TransitRouterRouteEntryId=rte-ksssq7kto4wfdx****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E" } |  |

| XML | 格式 |
|---|---|
| <RequestId>2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterRouteEntryId. NotFound | IllegalParam.TransitRouterRouteEntryId | TransitRouterRouteEntryId is not found. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | InvalidName | InvalidName | Name is invalid. |
| 400 | InvalidDescription | InvalidDescription | Description is invalid. |

#### 1.9.3. ListTransitRouterRouteEntries

查询转发路由器路由表中的路由条目信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ListTransitRouterRouteEntries | 系统规定参数。取值：ListTransitRouterRouteEntries。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时，每次显示的条目数。取值范围：1~100。默认值：20。 |
| TransitRouterRoute EntryDestinationCid rBlock | String | Query | 否 | 192.168.0.0/24 | 路由条目的目标网段（本参数即将废弃，建议使用 RouteFilter参数）。 |
| TransitRouterRoute EntryStatus | String | Query | 否 | Active | 路由条目的状态。取值： All：表示查询全部状态的路由条目。 Active（默认值）：表示仅查询生效状态的路由条目。 Rejected：表示仅查询因路由冲突而被拒绝的路由条目。 Prohibited：表示仅查询因匹配到路由策略而被禁止的路由条目。 Standby：表示仅查询作为备份的路由条目。 Candidate：表示仅查询作为候选的路由条目。 如果您未指定本参数的值，系统默认仅查询生效状态的路由条目。 |
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| NextToken | String | Query | 否 | fce19**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| TransitRouterRoute EntryNames | RepeatList | Query | 否 | testname | 路由条目的名称。 名称长度为0~128个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_） 和短划线（-）。 系统仅支持通过本参数查询当前路由表上静态配置的路由，且与 TransitRouterRouteEntryIds之外的其他查询条件不兼容。 |
| TransitRouterRoute EntryIds | RepeatList | Query | 否 | rte-oklkgwmj97z6dn**** | 路由条目ID。 系统仅支持通过本参数查询当前路由表上静态配置的路由，且与 TransitRouterRouteEntryNames之外的其他查询条件不兼容。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterRouteEntries | Array |  | 路由条目信息列表。 |
| - TransitRouterRouteEntryI d | String | rte-oklkgwmj97z6dn**** | 路由条目ID。 只有静态配置的路由才会返回该参数值。 |
| - TransitRouterRouteEntryD estinationCidrBlock | String | 192.168.0.0/24 | 路由条目的目标网段。 |
| - TransitRouterRouteEntryT ype | String | Static | 路由条目的类型。 Static：表示该路由条目为静态配置的路由。 Propagated：表示该路由条目为自动学习到的路由。 |

| -CreateTime | String | 2021-06-15T07:01Z | 路由条目的创建时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为：YYYY-MM- DDThh:mmZ。 只有静态配置的路由才会返回该参数值。 |
|---|---|---|---|
| - TransitRouterRouteEntryN ame | String | testname | 路由条目的名称。 只有静态配置的路由才会返回该参数值。 |
| - TransitRouterRouteEntryS tatus | String | Active | 路由条目的生效状态。 Active：生效。 Rejected：路由冲突拒绝。 Prohibited：路由策略禁止。 Standby：备份。 Candidate：候选。 Creating：添加中。 Deleting：删除中。 |
| - TransitRouterRouteEntryN extHopType | String | BlackHole | 路由条目的下一跳类型。 BlackHole：表示该路由条目为黑洞路由，所有去往目标网段的路由均会被丢弃。 Attachment：表示该路由条目的下一跳为网络实例连接，所有去往目标网段的路由均会被转发至指定的网络实例连接。 |
| - TransitRouterRouteEntryN extHopId | String | tr-attach-vx6iwhjr1x1j78**** | 路由条目的下一跳ID。黑洞路由不会返回该参数值。 |
| - TransitRouterRouteEntryD escription | String | CidrRoute | 路由条目的描述信息。 只有静态配置的路由才会返回该参数值。 |
| -OperationalMode | Boolean | false | 当前路由条目是否可操作。 true：可操作，表示您可以对当前路由条目执行删除操作。 false：不可操作，表示当前路由条目为系统自动生成，不支持编辑。 |
| -Tag | String | PermitVbr | 路由条目的标签。 仅取值：PermitVbr，表示当前路由条目仅会被传播至转发路由器实例下VBR实例的路由表中。 仅系统自动生成的转发路由器地址段的路由会返回当前参数。 |
| NextToken | String | fce19**** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | C3835E5E-1504-4344-B1BB- 98A4110F1079 | 请求ID。 |
| TotalCount | Integer | 6 | 总条目数。 |
| MaxResults | Integer | 20 | 分批次查询时，每次显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterRouteEntries &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":6,
 "NextToken":"fce19****",
 "RequestId":"C3835E5E-1504-4344-B1BB-98A4110F1079",
 "MaxResults":20,
 "TransitRouterRouteEntries":{
  "TransitRouterRouteEntryDestinationCidrBlock":"192.168.0.0/24",
  "TransitRouterRouteEntryNextHopId":"tr-attach-vx6iwhjr1x1j78****",
  "TransitRouterRouteEntryType":"Static",
  "TransitRouterRouteEntryDescription":"CidrRoute",
  "CreateTime":"2021-06-15T07:01Z",
  "TransitRouterRouteEntryNextHopType":"BlackHole",
  "TransitRouterRouteEntryName":"testname",
  "Tag":"PermitVbr",
  "OperationalMode":false,
  "TransitRouterRouteEntryId":"rte-oklkgwmj97z6dn****",
  "TransitRouterRouteEntryStatus":"Active"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>6</TotalCount> <NextToken>fce19****</NextToken> <RequestId>C3835E5E-1504-4344-B1BB-98A4110F1079</RequestId> <MaxResults>20</MaxResults> <TransitRouterRouteEntries> <TransitRouterRouteEntryDestinationCidrBlock>192.168.0.0/24</TransitRouterRouteEntryDestinationCidrBlock> <TransitRouterRouteEntryNextHopId>tr-attach-vx6iwhjr1x1j78****</TransitRouterRouteEntryNextHopId> <TransitRouterRouteEntryType>Static</TransitRouterRouteEntryType> <TransitRouterRouteEntryDescription>CidrRoute</TransitRouterRouteEntryDescription> <CreateTime>2021-06-15T07:01Z</CreateTime> <TransitRouterRouteEntryNextHopType>BlackHole</TransitRouterRouteEntryNextHopType> <TransitRouterRouteEntryName>testname</TransitRouterRouteEntryName> <Tag>PermitVbr</Tag> <OperationalMode>false</OperationalMode> <TransitRouterRouteEntryId>rte-oklkgwmj97z6dn****</TransitRouterRouteEntryId> <TransitRouterRouteEntryStatus>Active</TransitRouterRouteEntryStatus> </TransitRouterRouteEntries> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.TransitRouterRouteT ableId | IllegalParam.TransitRouterRouteTableId | TransitRouterRouteTableId is illegal. |
| 400 | IllegalParam.TransitRouterRouteE ntryStatus | IllegalParam.TransitRouterRouteEntryStatus | TransitRouterRouteEntryStatus is illegal. |
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | NextToken is illegal. |
| 400 | ParamExclusive.TransitRouterRou teEntryIdsAndTransitRouterRoute EntryStatus | ParamExclusive.RouteEntryIdsAndStatus | TransitRouterRouteEntryIds and TransitRouterRouteEntryStatus is mutually exclusive. |
| 400 | InvalidTransitRouterRouteTableId. NotFound | InvalidTransitRouterRouteTableId.NotFound | TransitRouterRouteTableId is not found. |
| 404 | ROUTETABLENOTFOUND _ _ _ | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |

#### 1.9.4. DeleteTransitRouterRouteEntry

删除转发路由器路由表中静态配置的路由条目。

**使用说明**

本接口只能删除静态配置的路由条目，不支持删除自动学习的路由条目。您可以通过调用ListTransitRouterRouteEntries接口查询路由条目的类型。 在您调用本接口删除路由条目前，请先了解以下信息： 如果您通过**TransitRouterRouteEntryId**删除指定的路由条目，则您无需填写**TransitRouterRouteTableId**和**TransitRouterRouteEntryDestinationCidrBlock**参数的值，否则会产生参数互斥。 如果您未通过**TransitRouterRouteEntryId**删除指定的路由条目，则您需依据路由条目的下一跳类型，填写相应参数： 如果您要删除黑洞路由，则您需要填写**TransitRouterRouteTableId**、**TransitRouterRouteEntryDestinationCidrBlock**、**TransitRouterRouteEntryNextHopType**参数的值。 如果您要删除非黑洞路由，则您需要填写**TransitRouterRouteTableId**、**TransitRouterRouteEntryDestinationCidrBlock**、**TransitRouterRouteEntryNextHopType**、**TransitRouter** 数的值。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouterRouteEntry | 系统规定参数。取值：DeleteTransitRouterRouteEntry。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接删除路由条目。 true：发送检查请求，只进行校验，不会删除路由条目。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。 如果检查通过，则返回对应请求ID。 |
| TransitRouterRoute EntryId | String | Query | 否 | rte-75eg4jprkvk0pw**** | 路由条目ID。 |
| TransitRouterRoute EntryNextHopType | String | Query | 否 | BlackHole | 下一跳类型。取值： BlackHole：表示该路由条目为黑洞路由，无需指定具体的下一跳信息。 Attachment：表示该路由条目的下一跳为网络实例连接，且需要指定下一跳的网络实例连接 ID。 |
| TransitRouterRoute EntryDestinationCid rBlock | String | Query | 否 | 192.168.0.0/24 | 目的网段。 |
| TransitRouterRoute EntryNextHopId | String | Query | 否 | tr-attach-nls9fzkfat8934**** | 路由条目的下一跳所关联的网络实例连接ID。 |
| TransitRouterRoute TableId | String | Query | 否 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2D69CCEA-42D0-48B2-8C9A- 9BB207F76D6E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterRouteEntry
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E" } |  |

| XML | 格式 |
|---|---|
| <RequestId>2D69CCEA-42D0-48B2-8C9A-9BB207F76D6E</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | InvalidTransitRouterRouteEntryId. NotFound | IllegalParam.TransitRouterRouteEntryId | TransitRouterRouteEntryId is not found. |
| 400 | ParamExclusive.RouteEntryIdAnd TransitRouterRouteTableIdOrDest CidrBlock | ParamExclusive.RouteEntryIdAndRouteTableIdOrDes tCidrBlock | RouteEntryId and TransitRouterRouteTableIdOrDestCidrBlock is mutually exclusive. |
| 400 | InvalidTransitRouterRouteEntry.N otFound | IllegalParam.TransitRouterRouteEntryId | TransitRouterRouteEntryId is not found. |

### 路由

#### 1.10.1. ListCenChildInstanceRouteEntriesToAttachment

查询转发路由器下网络实例路由表中指向网络实例连接的路由条目。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListCenChildInstanceRouteEntriesToAttach ment | 系统规定参数。取值：ListCenChildInstanceRouteEntries ToAttachment 。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时，每次显示的条目数。默认值为20 。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| CenId | String | Query | 否 | cen-dc4vwznpwbobrl**** | 云企业网实例ID。 |
| ChildInstanceRoute TableId | String | Query | 是 | vtb-bp174d1gje79u1g4t**** | 网络实例的路由表ID。 |
| TransitRouterAttac hmentId | String | Query | 是 | tr-attach-r6g0m3epjehw57**** | 网络实例连接ID。 |
| ServiceType | String | Query | 否 | TR | 路由托管的类型。如果该字段为空，即表示该路由没有被托管。取值：TR，表示托管类型为转发路由器类型。 |
| RouteFilter | RepeatList | Query | 否 |  | 目标网段过滤。 |
| -Key | String |  | 否 | prefix-exact-match | 路由匹配值模式。取值：prefix-exact- match ，完全匹配。 |
| -Value | RepeatList |  | 否 | 10.0.0.0/8 | 目标网段列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RouteEntry | Array |  | 路由条目的详细信息。 |
| -CenId | String | cen-9adwg6ghpq8oq4dp7q | 云企业网实例ID。 |
| - TransitRouterAttachmentI d | String | tr-attach-y463sghkkv1loe**** | 网络实例连接ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Status | String | Available | 路由条目的状态。取值： Available ：可用。 Pending ：配置中。 Modifying ：修改中。 |
| -ServiceType | String | TR | 路由托管的类型。如果该字段为空，即表示该路由没有被托管。取值：TR，表示托管类型为转发路由器类型。 |
| -DestinationCidrBlock | String | 10.0.0.0/8 | 路由条目的目标网段。 |
| - ChildInstanceRouteTableI d | String | vtb-bp1tlaj1c4nxr2t3e**** | 网络实例的路由表ID。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | 530BC816-F575-412A-AAB2- 435125D26328 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListCenChildInstanceRouteEntriesToAttachment &ChildInstanceRouteTableId=vtb-bp174d1gje79u1g4t**** &TransitRouterAttachmentId=tr-attach-r6g0m3epjehw57****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RouteEntry":{ "TransitRouterAttachmentId":"tr-attach-y463sghkkv1loe****", "Status":"Available", "ServiceType":"TR", "CenId":"cen-9adwg6ghpq8oq4dp7q", "DestinationCidrBlock":"10.0.0.0/8", "ChildInstanceRouteTableId":"vtb-bp1tlaj1c4nxr2t3e****" }, "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "RequestId":"530BC816-F575-412A-AAB2-435125D26328" } |  |

| XML | 格式 |
|---|---|
| <RouteEntry> <TransitRouterAttachmentId>tr-attach-y463sghkkv1loe****</TransitRouterAttachmentId> <Status>Available</Status> <ServiceType>TR</ServiceType> <CenId>cen-9adwg6ghpq8oq4dp7q</CenId> <DestinationCidrBlock>10.0.0.0/8</DestinationCidrBlock> <ChildInstanceRouteTableId>vtb-bp1tlaj1c4nxr2t3e****</ChildInstanceRouteTableId> </RouteEntry> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>530BC816-F575-412A-AAB2-435125D26328</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The parameter NextToken is invalid. |
| 400 | MissingParameter.TransitRouterA ttachmentId | MissingParam.TransitRouterAttachmentId | The parameter TransitRouterAttachmentId is Missing. |
| 400 | MissingParameter.ChildInstanceR outeTableId | MissingParam.ChildInstanceRouteTableId | The parameter ChildInstanceRouteTableId is Missing. |
| 400 | MissingParam.TransitRouterAttac hmentId | MissingParam.TransitRouterAttachmentId | The parameter TransitRouterAttachmentId is Missing. |
| 400 | MissingParam.ChildInstanceRoute TableId | MissingParam.ChildInstanceRouteTableId | The parameter TransitRouterAttachmentId is Missing. |
| 400 | InvalidParameter | InvalidParam.RouteFilter | The parameter RouteFilter is invalid. |

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTrAttachment.NotFound | ResourceNotFound.TransitRouterAttachment | The specified TransitRouterAttachment does not exist. |
| 400 | INVALIDROUTEFILTERKEY _ _ _ | InvalidParam.RoutFilterKey | The specified Key of RouteFilter is invalid. |
| 400 | PARAMETERCBNINSTANCEID _ _ _ | InvalidParam.CenId | The specified CEN does not exist. |
| 400 | INVALIDOPERATIONCBNINSTA _ _ _ NCESTATUS _ | OperationFailed.CenInstanceStatus | The CEN instance is not in a valid state for the operation. |
| 400 | ATTACHMENTNOTFOUND _ _ | ResourceNotFound.TransitRouterAttachment | The specified TransitRouterAttachment does not exist. |

#### 1.10.2. DescribeRouteConflict

查询网络实例中存在冲突的路由条目信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeRouteConflict | 系统规定参数。取值：DescribeRouteConflict。 |
| PageNumber | Integer | Query | 否 | 1 | 查询页码。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。默认值为10，取值范围：1~50。 |
| ChildInstanceId | String | Query | 是 | vpc-rj9gt5nll27onu**** | 要查询的网络实例ID。 |
| ChildInstanceType | String | Query | 是 | VPC | 网络实例的类型。取值： VPC：专有网络。 VBR：边界路由器。 |
| ChildInstanceRegion Id | String | Query | 是 | cn-qingdao-env66-d01 | 网络实例所属的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| ChildInstanceRoute TableId | String | Query | 是 | vtb-bp174d1gje79u1g4t**** | 要查询的网络实例的路由表ID。 |
| DestinationCidrBloc k | String | Query | 否 | 172.16.0.0/16 | 产生冲突的路由条目的目标网段。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RouteConflicts | Array |  | 产生冲突的路由条目的信息。 |
| -DestinationCidrBlock | String | 172.16.0.0/16 | 产生冲突的路由条目的目标网段。 |
| -RegionId | String | cn-qingdao-env66-d01 | 产生路由条目冲突的对端的网络实例所属地域ID。 |
| -InstanceId | String | vpc-rj9gt5nll27onu**** | 产生路由条目冲突的对端的网络实例ID。 |
| -InstanceType | String | VPC | 产生路由条目冲突的对端的网络实例类型。 VPC：专有网络。 VBR：边界路由器。 |
| -Status | String | conflict | 路由条目产生冲突的原因。 conflict：路由条目的目标网段相同造成的冲突。 overflow：其他网络实例路由表的路由条目数量超出限制造成的冲突。 |
| RequestId | String | EE3A2CC7-41F1-58DB-8306- CFC99D9C747B | 请求ID。 |

| PageNumber | Integer | 1 | 查询页码。 |
|---|---|---|---|
| TotalCount | Integer | 1 | 总条目数。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRouteConflict &ChildInstanceId=vpc-rj9gt5nll27onu**** &ChildInstanceType=VPC &ChildInstanceRegionId=cn-qingdao-env66-d01 &ChildInstanceRouteTableId=vtb-bp174d1gje79u1g4t****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "PageSize":10, "RequestId":"EE3A2CC7-41F1-58DB-8306-CFC99D9C747B", "PageNumber":1, "RouteConflicts":{ "Status":"conflict", "InstanceId":"vpc-rj9gt5nll27onu****", "DestinationCidrBlock":"172.16.0.0/16", "RegionId":"cn-qingdao-env66-d01", "InstanceType":"VPC" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>EE3A2CC7-41F1-58DB-8306-CFC99D9C747B</RequestId> <PageNumber>1</PageNumber> <RouteConflicts> <Status>conflict</Status> <InstanceId>vpc-rj9gt5nll27onu****</InstanceId> <DestinationCidrBlock>172.16.0.0/16</DestinationCidrBlock> <RegionId>cn-qingdao-env66-d01</RegionId> <InstanceType>VPC</InstanceType> </RouteConflicts> |  |

#### 1.10.3. DescribeCenRegionDomainRouteEntries

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCenRegionDomainRouteEntries | 系统规定参数。取值：DescribeCenRegionDomainRouteEn tries。 |
| CenId | String | Query | 是 | cen-7qthudw0ll6j**** | 云企业网实例ID。 |
| CenRegionId | String | Query | 是 | cn-qingdao-env66-d01 | 地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| PageNumber | Integer | Query | 否 | 1 | 查询页码。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。默认值为10，取值范围：1~50。 |

| Status | String | Query | 否 | Active | 路由条目的状态。取值： Active（默认值）：可用。 Candidate：候选。 Standby：备份 Rejected：拒绝。 Prohibited：禁用。 All：表示查询当前地域下所有状态的路由条目信息。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CenRouteEntries | Array |  | 路由条目信息列表。 |
| -AsPaths | Normal | 65501 | 路由条目的AS Path属性值。 |
| -Communities | Normal | 65501:1 | 路由条目的Community属性值。 |
| -CenRouteMapRecords | Array |  | 路由条目匹配到的入地域网关方向的路由策略。 |
| --RegionId | String | cn-qingdao-env66-d01 | 路由策略应用的地域ID。 |
| --RouteMapId | String | cenrmap-dbarzidzp7ek4k**** | 路由策略ID。 |
| -CenOutRouteMapRecords | Array |  | 路由条目匹配到的出地域网关方向的路由策略。 |
| --RegionId | String | cn-qingdao-env66-d01 | 路由策略应用的地域ID。 |
| --RouteMapId | String | cenrmap-dbarzidzp7ek4k**** | 路由策略ID。 |
| -DestinationCidrBlock | String | 192.168.1.0/24 | 路由条目的目标网段。 |
| -Type | String | CEN | 路由条目的类型。 CEN：表示通过云企业网传递的路由。 Custom：表示自定义路由。 System：表示系统路由。 |
| -NextHopInstanceId | String | vpc-bp1j8728mm6pweeod**** | 路由条目下一跳关联的网络实例ID。 |
| -NextHopType | String | VPC | 路由条目下一跳类型。 VPC：专有网络。 VBR：边界路由器。 local _service：表示当前路由条目为云服务系统路由，没有下一跳。 |
| -NextHopRegionId | String | cn-qingdao-env66-d01 | 路由条目下一跳关联的网络实例所属的地域ID。 |
| -Status | String | Active | 路由条目的状态。 Active：可用。 Candidate：候选。 Standby：备份 Rejected：拒绝。 Prohibited：禁用。 |
| -ToOtherRegionStatus | String | Active | 路由条目去往其他地域的状态。 Active：可用。 Prohibited：禁用。 |
| -Preference | Integer | 50 | 路由条目的优先级。 优先级数字越小，表示优先级越高。 |
| RequestId | String | 004E99FB-E996-5777-888E- BA1D8F215407 | 请求ID。 |

| PageNumber | Integer | 1 | 查询页码。 |
|---|---|---|---|
| TotalCount | Integer | 4 | 总条目数。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCenRegionDomainRouteEntries &CenId=cen-7qthudw0ll6j**** &CenRegionId=cn-qingdao-env66-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":4, "PageSize":10, "RequestId":"004E99FB-E996-5777-888E-BA1D8F215407", "PageNumber":1, "CenRouteEntries":{ "Status":"Active", "ToOtherRegionStatus":"Active", "NextHopType":"VPC", "NextHopRegionId":"cn-qingdao-env66-d01", "Type":"CEN", "Communities":"65501:1", "Preference":50, "-CenRouteMapRecords":{ "RegionId":"cn-qingdao-env66-d01", "RouteMapId":"cenrmap-cz5axczdxb7yfu****" }, "AsPaths":"65501", "DestinationCidrBlock":"192.168.1.0/24", "NextHopInstanceId":"vpc-bp1j8728mm6pweeod****", "-CenOutRouteMapRecords":{ "RegionId":"cn-qingdao-env66-d01", "RouteMapId":"cenrmap-dbarzidzp7ek4k****" } } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>4</TotalCount> <PageSize>10</PageSize> <RequestId>004E99FB-E996-5777-888E-BA1D8F215407</RequestId> <PageNumber>1</PageNumber> <CenRouteEntries> <Status>Active</Status> <ToOtherRegionStatus>Active</ToOtherRegionStatus> <NextHopType>VPC</NextHopType> <NextHopRegionId>cn-qingdao-env66-d01</NextHopRegionId> <Type>CEN</Type> <Communities>65501:1</Communities> <Preference>50</Preference> <-CenRouteMapRecords> <RegionId>cn-qingdao-env66-d01</RegionId> <RouteMapId>cenrmap-cz5axczdxb7yfu****</RouteMapId> </-CenRouteMapRecords> <AsPaths>65501</AsPaths> <DestinationCidrBlock>192.168.1.0/24</DestinationCidrBlock> <NextHopInstanceId>vpc-bp1j8728mm6pweeod****</NextHopInstanceId> <-CenOutRouteMapRecords> <RegionId>cn-qingdao-env66-d01</RegionId> <RouteMapId>cenrmap-dbarzidzp7ek4k****</RouteMapId> </-CenOutRouteMapRecords> </CenRouteEntries> |  |

#### 1.10.4. DescribeCenChildInstanceRouteEntries

查询云企业网中网络实例的路由条目信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCenChildInstanceRouteEntries | 系统规定参数。取值：DescribeCenChildInstanceRouteEntr ies。 |
| CenId | String | Query | 是 | cen-7qthudw0ll6jmc**** | 云企业网实例ID。 |
| ChildInstanceId | String | Query | 是 | vpc-bp18sth14qii3pnvo**** | 网络实例ID。 |
| ChildInstanceType | String | Query | 是 | VPC | 网络实例的类型。取值： VPC：专有网络实例。 VBR：边界路由器实例。 |
| Status | String | Query | 否 | Active | 路由条目的状态。取值： Active：可用。 Candidate：候选。 Standby：备份 Rejected：拒绝。 Prohibited：禁止。 All（默认值）：表示查询网络实例下所有状态的路由条目信息。 |
| PageNumber | Integer | Query | 否 | 1 | 查询页码。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。默认值为10，取值范围：1~50。 |
| ChildInstanceRegion Id | String | Query | 否 | cn-qingdao-env66-d01 | 网络实例所在的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CenRouteEntries | Array |  | 路由条目信息。 |
| -Communities | Normal | 65501:1 | 路由条目的Community属性值。 |
| -AsPaths | Normal | 65501 | 路由条目的AS Path属性值。 |
| -CenRouteMapRecords | Array |  | 路由条目匹配到的路由策略信息。 |
| --RouteMapId | String | cenrmap-w4yf7toozfol3q**** | 路由策略ID。 |
| --RegionId | String | cn-qingdao-env66-d01 | 产生路由条目冲突的对端的网络实例所属地域ID。 |
| -Conflicts | Array |  | 产生冲突的路由条目信息。 |
| --Status | String | conflict | 路由条目产生冲突的原因。取值： conflict：路由条目的目标网段相同造成的冲突。 overflow：其他网络实例路由表的路由条目数量超出限制造成的冲突。 |
| --DestinationCidrBlock | String | 192.168.1.0/24 | 产生冲突的路由条目的目标网段。 |
| --InstanceId | String | vbr-bp1svadp4lq38janc**** | 产生路由条目冲突的对端的网络实例ID。 |
| --InstanceType | String | VBR | 产生路由条目冲突的对端的网络实例类型。取值： VPC：专有网络。 VBR：边界路由器。 |
| --RegionId | String | cn-qingdao-env66-d01 | 产生路由条目冲突的对端的网络实例所属地域ID。 |

| -Status | String | Active | 路由条目的状态。取值： Active：可用。 Candidate：候选。 Standby：备份 Rejected：拒绝。 Prohibited：禁止。 |
|---|---|---|---|
| -Type | String | CEN | 路由条目的类型。取值： CEN：表示通过云企业网传递的路由。 System：表示系统路由。 Custom：表示自定义路由。 |
| -PublishStatus | String | Published | 路由条目在云企业网中的发布状态。取值： Published：已发布。 NonPublished：未发布。 |
| -NextHopType | String | VBR | 路由条目下一跳类型。取值： Instance：ECS实例。 HaVip：高可用虚拟IP。 RouterInterface：路由器接口。 NetworkInterface：弹性网卡。 VpnGateway：VPN网关。 IPv6Gateway：IPv6网关。 NatGateway：NAT网关。 Attachment：网络实例连接。 service：云服务。 VBR：边界路由器。 CCN：云连接网。 VPC：专有网络。 local：表示当前路由条目为网络实例的系统路由，没有下一跳。 TR：转发路由器。 BlackHole：表示当前路由条目为黑洞路由，没有下一跳。 EcRouterInterface：高速通道路由器接口。 HealthCheck：健康检查。 AS：云连接网接入网关。 classicLink：经典网络实例。 GatewayEndpoint：网关终端节点。 CPE：边界路由器连接的本地数据中心。 |
| -OperationalMode | Boolean | true | 是否允许发布或撤销该路由到云企业网。取值： true：允许发布或撤销。 false：不允许发布或撤销。 |
| -NextHopRegionId | String | cn-qingdao-env66-d01 | 路由条目下一跳关联的实例所属的地域ID。 |
| -NextHopInstanceId | String | vbr-bp13gtbhdp0pfqg6s**** | 路由条目下一跳关联的实例ID。 |
| -DestinationCidrBlock | String | 10.0.0.0/24 | 路由条目的目标网段。 |
| -RouteTableId | String | vtb-bp1r9pvl4xen8s9ju**** | 路由表ID。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |
| RequestId | String | 17A57456-EF48-419D-9AE6- 9B03D9996018 | 请求ID。 |
| PageNumber | Integer | 1 | 查询页码。 |
| TotalCount | Integer | 4 | 总条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCenChildInstanceRouteEntries &CenId=cen-7qthudw0ll6jmc**** &ChildInstanceId=vpc-bp18sth14qii3pnvo**** &ChildInstanceType=VPC
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":4, "PageSize":10, "RequestId":"17A57456-EF48-419D-9AE6-9B03D9996018", "PageNumber":1, "CenRouteEntries":{ "Status":"Active", "RouteTableId":"vtb-bp1r9pvl4xen8s9ju****", "Communities":"65501:1", "-Conflicts":{ "Status":"conflict", "InstanceId":"vbr-bp1svadp4lq38janc****", "DestinationCidrBlock":"192.168.1.0/24", "RegionId":"cn-qingdao-env66-d01", "InstanceType":"VBR" }, "DestinationCidrBlock":"10.0.0.0/24", "OperationalMode":true, "NextHopInstanceId":"vbr-bp13gtbhdp0pfqg6s****", "NextHopType":"VBR", "NextHopRegionId":"cn-qingdao-env66-d01", "Type":"CEN", "-CenRouteMapRecords":{ "RegionId":"cn-qingdao-env66-d01", "RouteMapId":"cenrmap-w4yf7toozfol3q****" }, "AsPaths":"65501", "PublishStatus":"Published" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>4</TotalCount> <PageSize>10</PageSize> <RequestId>17A57456-EF48-419D-9AE6-9B03D9996018</RequestId> <PageNumber>1</PageNumber> <CenRouteEntries> <Status>Active</Status> <RouteTableId>vtb-bp1r9pvl4xen8s9ju****</RouteTableId> <Communities>65501:1</Communities> <-Conflicts> <Status>conflict</Status> <InstanceId>vbr-bp1svadp4lq38janc****</InstanceId> <DestinationCidrBlock>192.168.1.0/24</DestinationCidrBlock> <RegionId>cn-qingdao-env66-d01</RegionId> <InstanceType>VBR</InstanceType> </-Conflicts> <DestinationCidrBlock>10.0.0.0/24</DestinationCidrBlock> <OperationalMode>true</OperationalMode> <NextHopInstanceId>vbr-bp13gtbhdp0pfqg6s****</NextHopInstanceId> <NextHopType>VBR</NextHopType> <NextHopRegionId>cn-qingdao-env66-d01</NextHopRegionId> <Type>CEN</Type> <-CenRouteMapRecords> <RegionId>cn-qingdao-env66-d01</RegionId> <RouteMapId>cenrmap-w4yf7toozfol3q****</RouteMapId> </-CenRouteMapRecords> <AsPaths>65501</AsPaths> <PublishStatus>Published</PublishStatus> </CenRouteEntries> |  |

### 自定义路由表

#### 1.11.1. UpdateTransitRouterRouteTable

修改转发路由器路由表的名称和描述信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | UpdateTransitRouterRouteTable | 系统规定参数。取值：UpdateTransitRouterRouteTable。 |
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| TransitRouterRoute TableName | String | Query | 否 | testname | 路由表的名称。 名称长度为0~128个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_） 和短划线（-）。 |
| TransitRouterRoute TableDescription | String | Query | 否 | testdesc | 路由表的描述信息。 描述可以为空或描述长度为2~256个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、 at（@）、下划线（_）和短划线（-）。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认值）：发送正常请求，通过检查后直接修改路由表的名称和描述信息。 true：发送检查请求，只进行校验，不会路由表的名称和描述信息。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9D6D5548-F271-41C4-AA9F- A62F5599085B | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateTransitRouterRouteTable &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"9D6D5548-F271-41C4-AA9F-A62F5599085B" } |  |

| XML | 格式 |
|---|---|
| <RequestId>9D6D5548-F271-41C4-AA9F-A62F5599085B</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterRouteTableId. NotFound | InvalidTransitRouterRouteTableId.NotFound | TransitRouterRouteTableId is not found. |
| 400 | InvalidName | InvalidName | Name is invalid. |

| 400 | InvalidDescription | InvalidDescription | Description is invalid. |
|---|---|---|---|

#### 1.11.2. DeleteTransitRouterRouteTable

**使用说明**

转发路由器默认路由表不支持删除。 当前自定义路由表中不存在任何关联转发关系。具体操作，请参见DissociateTransitRouterAttachmentFromRouteTable。 当前自定义路由表中不存在任何路由学习关系。具体操作，请参见DisableTransitRouterRouteTablePropagation。 当前自定义路由表中不存在任何自定义路由条目。具体操作，请参见DeleteTransitRouterRouteEntry。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteTransitRouterRouteTable | 系统规定参数。取值：DeleteTransitRouterRouteTable。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次删除请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接删除自定义路由表。 true：发送检查请求，只进行校验，不会删除自定义路由表。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1xbcgpgcz9axl9m**** | 自定义路由表ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | EAB2F133-8556-4D7C-9E91- 7EE4FE9CC7D2 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterRouteTable &TransitRouterRouteTableId=vtb-bp1xbcgpgcz9axl9m****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"EAB2F133-8556-4D7C-9E91-7EE4FE9CC7D2" } |  |

| XML | 格式 |
|---|---|
| <RequestId>EAB2F133-8556-4D7C-9E91-7EE4FE9CC7D2</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

| 400 | OperationFailed.DeleteSystemRo uteTable | OperationFailed.DeleteSystemRouteTable | Operation failed because You are not allowed to Delete System Transit Route Table. |
|---|---|---|---|
| 400 | InvalidTransitRouterRouteTableId. NotFound | InvalidTransitRouterRouteTableId.NotFound | TransitRouterRouteTableId is not found. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | MissingParam.TransitRouterRoute TableId | MissingParam.TransitRouterRouteTableId | The parameter TransitRouterRouteTableId is mandatory. |
| 400 | IncorrectStatus.TransitRouterRou teTable | IncorrectStatus.TransitRouterRouteTable | TransitRouterRouteTable status is invalid. |
| 400 | OperationFailed.DeleteRouteTabl eWithAssociation | OperationFailed.DeleteRouteTableWithAssociation | Operation failed because you are not allowed to delete TransitRouterRouteTable with association |
| 400 | OperationFailed.DeleteRouteTabl eWithPropagation | OperationFailed.DeleteRouteTableWithPropagation | Operation failed because you are not allowed to delete transit router route table with propagation |
| 400 | OperationFailed.DeleteRouteTabl eWithRouteEntry | OperationFailed.DeleteRouteTableWithRouteEntry | Operation failed because you are not allowed to delete transit touter route table with route entry |

#### 1.11.3. ListTransitRouterRouteTables

查询转发路由器的路由表信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ListTransitRouterRouteTables | 系统规定参数。取值：ListTransitRouterRouteTables。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时，每次显示的条目数。取值范围：1~100，默认值：20。 |
| NextToken | String | Query | 否 | dd20**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| TransitRouterRoute TableType | String | Query | 否 | Custom | 路由表的类型。取值： Custom：自定义路由表。 System：系统默认路由表。 |
| TransitRouterId | String | Query | 是 | tr-uf654ttymmljlvh2x**** | 转发路由器实例ID。 |
| TransitRouterRoute TableStatus | String | Query | 否 | Active | 路由表的状态。取值： Creating：创建中。 Deleting：删除中。 Active：可用。 |
| TransitRouterRoute TableNames | RepeatList | Query | 否 | testname | 路由表的名称。 您可以一次查询最多20个路由表的信息。 如果您同时通过TransitRouterRouteTableNames 和TransitRouterRouteTableIds查询路由表的信息时，路由表的名称和路由表的ID 需保持一致。 |
| TransitRouterRoute TableIds | RepeatList | Query | 否 | vtb-bp1l8awdb4iuo9uwu**** | 路由表的ID。 您可以一次查询最多20个路由表的信息。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |

| -Key | String |  | 否 | test | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
|---|---|---|---|---|---|
| -Value | String |  | 否 | test | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterRouteTables | Array |  | 路由表信息列表。 |
| -Tags | Array |  | 标签列表。 |
| --Key | String | test | 资源的标签键。 |
| --Value | String | test | 资源的标签值。 |
| - TransitRouterRouteTableS tatus | String | Active | 路由表的状态。 Creating：创建中。 Deleting：删除中。 Active：可用。 |
| - TransitRouterRouteTableT ype | String | System | 路由表的类型。 Custom：自定义路由表。 System：系统默认路由表。 |
| -CreateTime | String | 2021-03-15T09:39Z | 路由表的创建时间。 时间按照ISO8601标准表示，并使用UTC时间。格式为：YYYY-MM- DDThh:mmZ。 |
| - TransitRouterRouteTableI d | String | vtb-bp1dudbh2d5na6b50**** | 路由表ID。 |
| - TransitRouterRouteTableN ame | String | testname | 路由表的名称。 |
| - TransitRouterRouteTableD escription | String | testdesc | 路由表的描述信息。 |
| NextToken | String | dd20**** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | 82678F4A-C9F7-4CC1-8BF0- D619A63BFC57 | 请求ID。 |
| TotalCount | Integer | 1 | 总条目数。 |
| MaxResults | Integer | 20 | 分批次查询时，每次显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterRouteTables &TransitRouterId=tr-uf654ttymmljlvh2x****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "NextToken":"dd20****", "RequestId":"82678F4A-C9F7-4CC1-8BF0-D619A63BFC57", "TransitRouterRouteTables":{ "TransitRouterRouteTableId":"vtb-bp1dudbh2d5na6b50****", "TransitRouterRouteTableStatus":"Active", "TransitRouterRouteTableType":"System", "TransitRouterRouteTableDescription":"testdesc", "-Tags":{ "Value":"test", "Key":"test" }, "CreateTime":"2021-03-15T09:39Z", "TransitRouterRouteTableName":"testname" }, "MaxResults":20 } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>dd20****</NextToken> <RequestId>82678F4A-C9F7-4CC1-8BF0-D619A63BFC57</RequestId> <TransitRouterRouteTables> <TransitRouterRouteTableId>vtb-bp1dudbh2d5na6b50****</TransitRouterRouteTableId> <TransitRouterRouteTableStatus>Active</TransitRouterRouteTableStatus> <TransitRouterRouteTableType>System</TransitRouterRouteTableType> <TransitRouterRouteTableDescription>testdesc</TransitRouterRouteTableDescription> <-Tags> <Value>test</Value> <Key>test</Key> </-Tags> <CreateTime>2021-03-15T09:39Z</CreateTime> <TransitRouterRouteTableName>testname</TransitRouterRouteTableName> </TransitRouterRouteTables> <MaxResults>20</MaxResults> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | NextToken is illegal |
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | TransitRouterId is not found. |

#### 1.11.4. CreateTransitRouterRouteTable

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateTransitRouterRouteTable | 系统规定参数。取值：CreateTransitRouterRouteTable。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| TransitRouterRoute TableName | String | Query | 否 | testname | 自定义路由表名称。 名称长度为0~128个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_） 和短划线（-）。 |

| TransitRouterRoute TableDescription | String | Query | 否 | testdesc | 自定义路由表的描述信息。 描述可以为空或描述长度为2~256个字符，可包含英文字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、 at（@）、下划线（_）和短划线（-）。 |
|---|---|---|---|---|---|
| TransitRouterId | String | Query | 是 | tr-bp1su1ytdxtataupl**** | 转发路由器实例ID。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次创建请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，只进行校验， 通过检查后直接创建自定义路由表。 true：发送检查请求，只进行校验，不会创建自定义路由表。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | test | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | tagtest | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterRouteTableI d | String | vtb-bp1xbcgpgcz9axl9m**** | 自定义路由表ID。 |
| RequestId | String | 599904C8-A3DA-4E5F-83B6- D5364E664247 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterRouteTable &TransitRouterId=tr-bp1su1ytdxtataupl****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TransitRouterRouteTableId":"vtb-bp1xbcgpgcz9axl9m****", "RequestId":"599904C8-A3DA-4E5F-83B6-D5364E664247" } |  |

| XML | 格式 |
|---|---|
| <TransitRouterRouteTableId>vtb-bp1xbcgpgcz9axl9m****</TransitRouterRouteTableId> <RequestId>599904C8-A3DA-4E5F-83B6-D5364E664247</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | TransitRouterId is not found |
| 400 | OperationFailed.CCNTrNotSuppor t | OperationFailed.CCNTrNotSupport | Operation failed because the CCN transit router does not support route table. |

| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
|---|---|---|---|
| 400 | MissingParam.TransitRouterId | MissingParam.TransitRouterId | The parameter TransitrouterId is mandatory. |
| 400 | OperationFailed.BasicTrNotSuppo rt | OperationFailed.BasicTrNotSupport | Operation failed because the Basic TransitRouter does not support RouteTable |
| 400 | IncorrectStatus.TransitRouter | IncorrectStatus.TransitRouter | TransitRouter status is invalid. |
| 400 | QuotaExceeded.TransitRouterRou tTable | QuotaExceeded.TransitRouterRoutTable | TransitRouterRoutTable quota exceeded. |

### 路由学习

#### 1.12.1. DisableTransitRouterRouteTablePropagation

解除路由学习关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DisableTransitRouterRouteTablePropagation | 系统规定参数。取值：DisableTransitRouterRouteTablePro pagation。 |
| TransitRouterAttach mentId | String | Query | 是 | tr-attach-vx6iwhjr1x1j78**** | 网络实例连接ID。 |
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接解除路由学习关系。 true：发送检查请求，只进行校验，不会解除路由学习关系。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | A7C43F99-B1E5-4A53-AB64- 4BAE8AF4484E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DisableTransitRouterRouteTablePropagation &TransitRouterAttachmentId=tr-attach-vx6iwhjr1x1j78**** &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"A7C43F99-B1E5-4A53-AB64-4BAE8AF4484E"
}
```

| XML | 格式 |
|---|---|
| <RequestId>A7C43F99-B1E5-4A53-AB64-4BAE8AF4484E</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAttachmentId.NotFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 404 | InvalidRouteTableId.NotFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |

#### 1.12.2. ListTransitRouterRouteTablePropagations

查询转发路由器路由表的路由学习关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterRouteTablePropagations | 系统规定参数。取值：ListTransitRouterRouteTablePropag ations。 |
| MaxResults | Integer | Query | 否 | 50 | 分批次查询时，每次显示的条目数。默认值为50。 |
| NextToken | String | Query | 否 | dd20**** | 分批次查询时，下一次查询的Token。 |
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| TransitRouterAttach mentId | String | Query | 否 | tr-attach-vx6iwhjr1x1j78**** | 网络实例连接ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterPropagation s | Array |  | 路由学习关系信息列表。 |
| -Status | String | Active | 路由学习关系状态。 Enabling：加载中。 Disabling：卸载中。 Active：可用。 |
| - TransitRouterAttachmentI d | String | tr-attach-vx6iwhjr1x1j78**** | 网络实例连接ID。 |
| - TransitRouterRouteTableI d | String | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| -ResourceId | String | vpc-bp1h8vbrbcgohcju5**** | 下一跳资源ID。 |
| -ResourceType | String | VPC | 下一跳资源类型。 VPC：专有网络实例。 VBR：边界路由器实例。 |

| RequestId | String | 04C81E0D-945E-4D61-A561- 3DEA322F243B | 请求ID。 |
|---|---|---|---|
| TotalCount | Integer | 2 | 总条目数。 |
| MaxResults | Integer | 50 | 分批次查询时，每次显示的条目数。 |
| NextToken | String | dd20**** | 分批次查询时，下一次查询的Token。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterRouteTablePropagations &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":2, "NextToken":"dd20****", "RequestId":"04C81E0D-945E-4D61-A561-3DEA322F243B", "MaxResults":50, "TransitRouterPropagations":{ "Status":"Active", "TransitRouterAttachmentId":"tr-attach-vx6iwhjr1x1j78****", "TransitRouterRouteTableId":"vtb-bp1dudbh2d5na6b50****", "ResourceId":"vpc-bp1h8vbrbcgohcju5****", "ResourceType":"VPC" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>2</TotalCount> <NextToken>dd20****</NextToken> <RequestId>04C81E0D-945E-4D61-A561-3DEA322F243B</RequestId> <MaxResults>50</MaxResults> <TransitRouterPropagations> <Status>Active</Status> <TransitRouterAttachmentId>tr-attach-vx6iwhjr1x1j78****</TransitRouterAttachmentId> <TransitRouterRouteTableId>vtb-bp1dudbh2d5na6b50****</TransitRouterRouteTableId> <ResourceId>vpc-bp1h8vbrbcgohcju5****</ResourceId> <ResourceType>VPC</ResourceType> </TransitRouterPropagations> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The parameter NextToken is invalid. |

#### 1.12.3. EnableTransitRouterRouteTablePropagation

创建路由学习关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | EnableTransitRouterRouteTablePropagation | 系统规定参数。取值：EnableTransitRouterRouteTablePro pagation。 |
| TransitRouterAttach mentId | String | Query | 是 | tr-attach-nls9fzkfat8934**** | 网络实例连接ID。 |

| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
|---|---|---|---|---|---|
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接创建路由学习关系。 true：发送检查请求，只进行校验，不会创建路由学习关系。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 59CF8BF9-DE61-421E-B903- D56AF46A303C | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EnableTransitRouterRouteTablePropagation &TransitRouterAttachmentId=tr-attach-nls9fzkfat8934**** &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"59CF8BF9-DE61-421E-B903-D56AF46A303C" } |  |

| XML | 格式 |
|---|---|
| <RequestId>59CF8BF9-DE61-421E-B903-D56AF46A303C</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRouteTableId.NotFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |
| 404 | InvalidAttachmentId.NotFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |

### 关联转发

#### 1.13.1. DissociateTransitRouterAttachmentFromRouteTable

解除关联转发关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DissociateTransitRouterAttachmentFromRo uteTable | 系统规定参数。取值：DissociateTransitRouterAttachment FromRouteTable。 |

| TransitRouterAttach mentId | String | Query | 是 | tr-attach-nls9fzkfat8934**** | 网络实例连接ID。 |
|---|---|---|---|---|---|
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接解除关联转发关系。 true：发送检查请求，只进行校验，不会解除关联转发关系。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回对应请求ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DissociateTransitRouterAttachmentFromRouteTable &TransitRouterAttachmentId=tr-attach-nls9fzkfat8934**** &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

| XML | 格式 |
|---|---|
| <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectStatus.Status | IncorrectStatus.Status | RouteTableAssociation status is invalid. |
| 404 | InvalidAttachmentId.NotFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 404 | InvalidRouteTableId.NotFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |

#### 1.13.2. ListTransitRouterRouteTableAssociations

查询转发路由器路由表或网络实例连接已创建的关联转发关系。

**使用说明**

调用ListTransitRouterRouteTableAssociations接口时，请求参数**TransitRouterRouteTableId**和**TransitRouterAttachmentId**需至少输入一个： 如果仅指定了**TransitRouterRouteTableId**参数的值，则表示您要查询与转发路由器路由表创建关联转发关系的网络实例连接的信息。 如果仅指定了**TransitRouterAttachmentId**参数的值，则表示您要查询与网络实例连接创建关联转发关系的转发路由器路由表的信息。 如果同时指定了**TransitRouterRouteTableId**和**TransitRouterAttachmentId**参数的值，则表示您要查询网络实例连接与转发路由器路由表之间的关联转发关系。 如果网络实例连接和企业版转发路由器路由表之间存在关联转发关系，则系统正常返回关联转发关系的信息。 如果网络实例连接和企业版转发路由器路由表之间不存在关联转发关系，则**TransitRouterAssociations**数组返回为空值。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterRouteTableAssociations | 系统规定参数。取值：ListTransitRouterRouteTableAssoci ations。 |
| MaxResults | Integer | Query | 否 | 50 | 分批次查询时每次显示的条目数。默认值：50。 |
| NextToken | String | Query | 否 | a415**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| TransitRouterRoute TableId | String | Query | 否 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| TransitRouterAttach mentId | String | Query | 否 | tr-attach-nls9fzkfat8934**** | 网络实例连接ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterAssociations | Array |  | 关联转发关系信息列表。 |
| - TransitRouterAttachmentI d | String | tr-attach-nls9fzkfat8934**** | 网络实例连接ID。 |
| -Status | String | Associating | 关联转发的状态。 Active：可用。 Associating：加载中。 Dissociating：卸载中。 |
| -ResourceType | String | VPC | 下一跳资源类型。 VPC：专有网络实例。 VBR：边界路由器实例。 |
| -ResourceId | String | vpc-bp1h8vbrbcgohcju5**** | 下一跳资源ID。 |
| - TransitRouterRouteTableI d | String | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| NextToken | String | a415**** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | F6B1D9AB-176D-4399-801D- 8BC576F4EB0D | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| MaxResults | Integer | 50 | 分批次查询时每次显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterRouteTableAssociations
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "NextToken":"a415****",
 "RequestId":"F6B1D9AB-176D-4399-801D-8BC576F4EB0D",
 "MaxResults":50,
 "TransitRouterAssociations":{
  "TransitRouterAttachmentId":"tr-attach-nls9fzkfat8934****",
  "Status":"Associating",
  "TransitRouterRouteTableId":"vtb-bp1dudbh2d5na6b50****",
  "ResourceId":"vpc-bp1h8vbrbcgohcju5****",
  "ResourceType":"VPC"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <NextToken>a415****</NextToken> <RequestId>F6B1D9AB-176D-4399-801D-8BC576F4EB0D</RequestId> <MaxResults>50</MaxResults> <TransitRouterAssociations> <TransitRouterAttachmentId>tr-attach-nls9fzkfat8934****</TransitRouterAttachmentId> <Status>Associating</Status> <TransitRouterRouteTableId>vtb-bp1dudbh2d5na6b50****</TransitRouterRouteTableId> <ResourceId>vpc-bp1h8vbrbcgohcju5****</ResourceId> <ResourceType>VPC</ResourceType> </TransitRouterAssociations> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The parameter NextToken is invalid. |

#### 1.13.3. AssociateTransitRouterAttachmentWithRouteTable

创建关联转发关系。

**使用说明**

一个网络实例连接仅支持与一个转发路由器路由表建立关联转发关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | AssociateTransitRouterAttachmentWithRout eTable | 系统规定参数。取值：AssociateTransitRouterAttachment WithRouteTable。 |
| TransitRouterAttach mentId | String | Query | 是 | tr-attach-nls9fzkfat8934**** | 网络实例连接ID。 |
| TransitRouterRoute TableId | String | Query | 是 | vtb-bp1dudbh2d5na6b50**** | 转发路由器路由表ID。 |
| ClientToken | String | Query | 否 | 02fb3da4-130e-11e9-8e44-001**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。 |
| DryRun | Boolean | Query | 否 | false | 是否对此次请求执行预检，包括权限、实例状态校验等。取值： false（默认）：发送正常请求，通过检查后直接创建关联转发关系。 true：发送检查请求，只进行校验，不会创建关联转发关系。检查项包括是否填写了必需参数、请求格式等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534-BD0E- 403F3EE64CAF | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AssociateTransitRouterAttachmentWithRouteTable &TransitRouterAttachmentId=tr-attach-nls9fzkfat8934**** &TransitRouterRouteTableId=vtb-bp1dudbh2d5na6b50****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"4EC47282-1B74-4534-BD0E-403F3EE64CAF" } |  |

| XML | 格式 |
|---|---|
| <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | AssociationExist.TransitRouterTab le | AssociationExist.TransitRouterTable | The specified association already exists. |
| 404 | InvalidRouteTableId.NotFound | InvalidRouteTableId.NotFound | The specified RouteTableId is not found. |
| 404 | InvalidAttachmentId.NotFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |

### 组播

#### 1.14.1. CreateTransitRouterMulticastDomain

创建组播域。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | CreateTransitRouterMulticastDomain | 系统规定参数，取值：CreateTransitRouterMulticastDomai n。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-4266**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| CenId | String | Query | 否 | cen-a7syd349kne38g**** | 云企业网实例ID。 |
| TransitRouterId | String | Query | 否 | tr-p0wr9p28r92d598y6**** | 转发路由器实例ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env17e-d01 | 转发路由器实例所属的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |

| TransitRouterMultic astDomainName | String | Query | 否 | nametest | 组播域的名称。 名称长度为0~128个字符，可包含大小写字母、 数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线 （_）和短划线（-）。 |
|---|---|---|---|---|---|
| TransitRouterMultic astDomainDescripti on | String | Query | 否 | desctest | 组播域的描述信息。 描述长度为0~256个字符，可包含大小写字母、 数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线 （_）和短划线（-）。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会创建组播域。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接创建组播域。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | TagKey | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | TagValue | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterMulticastDo mainId | String | tr-mcast-domain- 40cwj0rgzgdtam**** | 组播域ID。 |
| RequestId | String | 94E19C6F-206F-5223-9A63- 64B85851BC04 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateTransitRouterMulticastDomain &Action=CreateTransitRouterMulticastDomain
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"94E19C6F-206F-5223-9A63-64B85851BC04", "TransitRouterMulticastDomainId":"tr-mcast-domain-40cwj0rgzgdtam****" } |  |

| XML | 格式 |
|---|---|
| <RequestId>94E19C6F-206F-5223-9A63-64B85851BC04</RequestId> <TransitRouterMulticastDomainId>tr-mcast-domain-40cwj0rgzgdtam****</TransitRouterMulticastDomainId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterId.NotFound | InvalidTransitRouterId.NotFound | The specified TransitRouterId is not found. |

| 400 | IllegalParam.TransitRouterId | IllegalParam.TransitRouterId | The specified TransitRouterId is illegal. |
|---|---|---|---|
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is illegal. |
| 400 | IllegalParam.RegionId | IllegalParam.RegionId | The specified RegionId is illegal. |
| 400 | InvalidCenId.NotFound | InvalidCenId.NotFound | The specified CenId is not found. |
| 400 | INVALIDOPERATIONTRANSITRO _ _ UTERNOTEXIST _ _ | InvalidOperation.TransitRouterNotExist | Operation is invalid because the transit router not exist. |
| 400 | INVALIDOPERATIONCBNINSTA _ _ _ NCESTATUS _ | InvalidOperation.CENInstanceStatus | The CEN instance is not in a valid state for the operation. |
| 400 | IncorrectStatus.TransitRouterInst ance | IncorrectStatus.TransitRouterInstance | The status of TransitRouter is incorrect. |
| 400 | OperationUnsupported.TransitRo uterType | OperationUnsupported.TransitRouterType | The specified TransitRouterType does not support the operation. |
| 400 | OperationUnsupported.ServiceMo de | OperationUnsupported.ServiceMode | The specified ServiceMode does not support the operation. |
| 400 | OperationUnsupported.TransitRo uterSupportMulticast | OperationUnsupported.TransitRouterSupportMultica st | The specified TransitRouterSupportMulticast does not support the operation. |
| 400 | OperationUnsupported.RegionId | OperationUnsupported.RegionId | The specified RegionId does not support the operation. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | IncorrectStatus.TransitRouter | IncorrectStatus.TransitRouter | The status of TransitRouter is incorrect. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.2. ModifyTransitRouterMulticastDomain

修改组播域的名称和描述信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ModifyTransitRouterMulticastDomain | 系统规定参数。取值：ModifyTransitRouterMulticastDoma in。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-4266**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-40cwj0rgzgdtam**** | 组播域ID。 |
| TransitRouterMultic astDomainName | String | Query | 否 | nametest | 组播域的新名称。 名称长度为0~128个字符，可包含大小写字母、 数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线 （_）和短划线（-）。 |
| TransitRouterMultic astDomainDescripti on | String | Query | 否 | desctest | 组播域新的描述信息。 描述长度为0~256个字符，可包含大小写字母、 数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线 （_）和短划线（-）。 |

| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会修改组播域的名称和描述信息。检查项包括是否填写了必需参数、 请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接修改组播域的名称和描述信息。 本参数暂不生效。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 26273D23-5CB0-5EFC-AF5F- 78A5448084C9 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyTransitRouterMulticastDomain &TransitRouterMulticastDomainId=tr-mcast-domain-40cwj0rgzgdtam****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"26273D23-5CB0-5EFC-AF5F-78A5448084C9" } |  |

| XML | 格式 |
|---|---|
| <RequestId>26273D23-5CB0-5EFC-AF5F-78A5448084C9</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NAMEILLEGAL _ | Illegal.Name | Name is illegal. |
| 400 | DESCRIPTIONILLEGAL _ | Illegal.Description | Description is illegal. |
| 400 | InvalidTransitRouterMulticastDom ainId.NotFound | InvalidMulticastDomainId.NotFound | The specified MulticastDomainId is not found. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.3. ListTransitRouterMulticastDomains

查询组播域的信息。

**使用说明**

**RegionId**必须和**CenId**组合使用，不能单独使用，否则将不会显示组播域的信息。但**TransitRouterId**和**TransitRouterMulticastDomainId**可以单独使用。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ListTransitRouterMulticastDomains | 系统规定参数。取值： ListTransitRouterMulticastDomains。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426655440000 | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |

| CenId | String | Query | 否 | cen-a7syd349kne38g**** | 云企业网实例ID。 |
|---|---|---|---|---|---|
| TransitRouterId | String | Query | 否 | tr-p0wr9p28r92d598y6**** | 转发路由器实例ID。 |
| TransitRouterMultic astDomainId | String | Query | 否 | tr-mcast-domain-3r3bvbypxqheej**** | 组播域ID。 |
| RegionId | String | Query | 否 | cn-qingdao-env17e-d01 | 转发路由器实例所属地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| MaxResults | Long | Query | 否 | 20 | 分批次查询时每次显示的条目数。默认值：20。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| Tag | RepeatList | Query | 否 |  | 标签信息。 一次最多支持输入20个标签信息。 |
| -Key | String |  | 否 | TagKey | 资源的标签键。 一旦传入该值，则不允许为空字符串。最多支持64 个字符，不能以 aliyun 或者 acs: 开头， 不能包含 http:// 或者 https:// 。 一次最多支持输入20个标签的标签键。 |
| -Value | String |  | 否 | TagValue | 资源的标签值。 标签值可以为空或输入不超过128个字符的字符串，不能以 aliyun 或者 acs: 开头，不能包含 http:// 或者 https:// 。 每一个标签键对应一个标签值，一次最多支持输入 20个标签键对应的标签值。 |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

| aliyun |  | acs: |
|---|---|---|
|  | https:// |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterMulticastDo mains | Array |  | 组播域信息列表。 |
| -Tags | Array |  | 标签列表。 |
| --Key | String | TagKey | 标签键。 |
| --Value | String | TagValue | 标签值。 |
| - TransitRouterMulticastDo mainId | String | tr-mcast-domain- 3r3bvbypxqheej**** | 组播域ID。 |
| - TransitRouterMulticastDo mainName | String | nametest | 组播域的名称。 |
| - TransitRouterMulticastDo mainDescription | String | desctest | 组播域的描述信息。 |
| -Status | String | Active | 组播域的状态。 仅取值：Active，表示组播域当前可用。 |
| -TransitRouterId | String | tr-bp1c23ijrl6d6c226h*** | 转发路由器实例ID。 |
| RequestId | String | 8A0F93D1-FD6C-56FC-B6D2- 668FC92D12D2 | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |

| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 |
|---|---|---|---|
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastDomains
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "RequestId":"8A0F93D1-FD6C-56FC-B6D2-668FC92D12D2", "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "MaxResults":20, "TransitRouterMulticastDomains":{ "Status":"Active", "-Tags":{ "Value":"TagValue", "Key":"TagKey" }, "TransitRouterMulticastDomainId":"tr-mcast-domain-3r3bvbypxqheej****", "TransitRouterMulticastDomainName":"nametest", "TransitRouterMulticastDomainDescription":"desctest", "TransitRouterId":"tr-bp1c23ijrl6d6c226h***" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <RequestId>8A0F93D1-FD6C-56FC-B6D2-668FC92D12D2</RequestId> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <MaxResults>20</MaxResults> <TransitRouterMulticastDomains> <Status>Active</Status> <-Tags> <Value>TagValue</Value> <Key>TagKey</Key> </-Tags> <TransitRouterMulticastDomainId>tr-mcast-domain-3r3bvbypxqheej****</TransitRouterMulticastDomainId> <TransitRouterMulticastDomainName>nametest</TransitRouterMulticastDomainName> <TransitRouterMulticastDomainDescription>desctest</TransitRouterMulticastDomainDescription> <TransitRouterId>tr-bp1c23ijrl6d6c226h***</TransitRouterId> </TransitRouterMulticastDomains> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The specified NextToken is illegal. |
| 400 | IllegalParam.TrInstance | IllegalParam.TrInstance | The specified TrInstance is illegal. |
| 400 | IllegalParam.CenId | IllegalParam.CenId | The specified CenId is illegal. |

#### 1.14.4. DeleteTransitRouterMulticastDomain

删除组播域。

**使用说明**

删除组播域前，请确保满足以下条件： 组播域未绑定任何交换机。具体操作，请参见DisassociateTransitRouterMulticastDomain 。 组播域下不存在组播源和组播成员。具体操作，请参见DeregisterTransitRouterMulticastGroupSources和DeregisterTransitRouterMulticastGroupMembers。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DeleteTransitRouterMulticastDomain | 系统规定参数。取值：DeleteTransitRouterMulticastDomai n。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-4266**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-40cwj0rgzgdtam**** | 组播域ID。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会删除组播域。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接删除组播域。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 40194E53-2484-5831-BB53- E11D123C1A32 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteTransitRouterMulticastDomain &TransitRouterMulticastDomainId=tr-mcast-domain-40cwj0rgzgdtam****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"40194E53-2484-5831-BB53-E11D123C1A32" } |  |

| XML | 格式 |
|---|---|
| <RequestId>40194E53-2484-5831-BB53-E11D123C1A32</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectStatus.MulticastDomain | IncorrectStatus.MulticastDomain | The status of MulticastDomain is incorrect. |
| 400 | INSTANCENOTEXIST _ _ | InstanceNotExist | The instance is not exist. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | IncorrectStatus.TransitRouter | IncorrectStatus.TransitRouter | The status of TransitRouter is incorrect. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINASSOCIATIONEXIST _ _ | InvalidOperation.MulticastDomainAssociationExist | Operation is invalid because multicast domain associations exist. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ GROUPEXIST _ | InvalidOperation.MulticastGroupExist | Operation is invalid because multicast groups exist. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAININGROUP _ _ | InvalidOperation.MulticastDomainInGroup | Operation is invalid because multicast domain has registered as multicast group member. |

| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
|---|---|---|---|

#### 1.14.5. AssociateTransitRouterMulticastDomain

将专有网络VPC（Virtual Private Cloud）下的交换机关联至组播域。

**使用说明**

一个交换机只支持关联至一个组播域。请确保待关联的交换机未与其他组播域建立关联关系。解除交换机与组播域的关联关系，请参见 DisassociateTransitRouterMulticastDomain。 交换机所属的VPC必须已经连接到转发路由器。创建VPC连接，请参见CreateTransitRouterVpcAttachment 。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | AssociateTransitRouterMulticastDomain | 系统规定参数。取值：AssociateTransitRouterMulticastDo main。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426655440000 | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-91wpg6wbhchjeq**** | 组播域ID。 |
| TransitRouterAttach mentId | String | Query | 是 | tr-attach-g3kz2k3u76amsk**** | VPC连接ID。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会将交换机关联至组播域。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接将交换机关联至组播域。 |
| VSwitchIds | RepeatList | Query | 否 | vsw-p0wxk12u6okfkr8xy**** | 交换机ID列表。 一次最多支持关联5个交换机，一个组播域最多支持关联 10 个交换机。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F88AC12C-943B-50E9-A344- 4F8820BB07A7 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AssociateTransitRouterMulticastDomain &TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq**** &TransitRouterAttachmentId=tr-attach-g3kz2k3u76amsk**** &Action=AssociateTransitRouterMulticastDomain
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"F88AC12C-943B-50E9-A344-4F8820BB07A7" } |  |

| XML | 格式 |
|---|---|
| <RequestId>F88AC12C-943B-50E9-A344-4F8820BB07A7</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidMulticastDomain.NotFound | InvalidMulticastDomain.NotFound | The specified MulticastDomain is not found. |
| 400 | IncorrectStatus.MulticastDomain | IncorrectStatus.MulticastDomain | The status of MulticastDomain is incorrect. |
| 400 | InvalidAttachmentId.NotFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 400 | IllegalParam.AttachmentId | IllegalParam.AttachmentId | The specified AttachmentId is illegal. |
| 400 | IncorrectStatus.Attachment | IncorrectStatus.Attachment | The status of Attachment is incorrect. |
| 400 | MissingParam.VSwitchIds | MissingParam.VSwitchIds | The parameter VSwitchIds is mandatory. |
| 400 | INSTANCENOTEXIST _ _ | InstanceNotExist | The instance is not exist. |
| 400 | OperationUnsupported.CLOUDB _ OXVPCNOTSUPPORT _ _ _ | OperationUnsupported.CloudBoxVpc | The specified CloudBoxVpc does not support the operation. |
| 400 | AssociationExist.VSwitchIds | AssociationExist.VSwitchIds | The association already exists. |
| 400 | QUOTAFULLMULTICASTVSWITC _ _ _ HPERDOMAIN _ _ | QuotaFull.VswitchPerMulticastDomain | The number of vswitch associated with multicast domain has exceed the maximum value that can be created. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |
| 400 | OperationFailed.-100118 | OperationUnsupported.VpcRegion | The specified Region is not support for this operation. |

#### 1.14.6. DisassociateTransitRouterMulticastDomain

解除交换机与组播域的关联关系。

**使用说明**

交换机和组播域解除关联前，请确保交换机下不存在组播源和组播成员。删除组播源和删除组播成员的操作，请参见DeregisterTransitRouterMulticastGroupSources和 DeregisterTransitRouterMulticastGroupMembers。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DisassociateTransitRouterMulticastDomain | 系统规定参数。取值：DisassociateTransitRouterMulticast Domain。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426655440000 | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-91wpg6wbhchjeq**** | 组播域ID。 |
| TransitRouterAttach mentId | String | Query | 是 | tr-attach-g3kz2k3u76amsk**** | VPC连接ID。 本参数为交换机所属的专有网络VPC（Virtual Private Cloud）被连接至转发路由器实例后生成的VPC连接的ID。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会解除交换机和组播域的关联关系。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过， 则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接解除交换机和组播域的关联关系。 |

| VSwitchIds | RepeatList | Query | 否 | vsw-p0w9s2ig1jnwgrbzl**** | 交换机ID列表。 一次最多支持与5个交换机解除关联关系。 当前参数为必填参数。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6F6B3FF0-45D1-5416-B189- C45A42A0222B | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DisassociateTransitRouterMulticastDomain &TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq**** &TransitRouterAttachmentId=tr-attach-g3kz2k3u76amsk****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"6F6B3FF0-45D1-5416-B189-C45A42A0222B" } |  |

| XML | 格式 |
|---|---|
| <RequestId>6F6B3FF0-45D1-5416-B189-C45A42A0222B</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidMulticastDomainId.NotFou nd | InvalidMulticastDomainId.NotFound | The specified MulticastDomainId is not found. |
| 400 | IncorrectStatus.MulticastDomain | IncorrectStatus.MulticastDomain | The status of MulticastDomain is incorrect. |
| 400 | INSTANCESTATUSNOTSUPPOR _ _ _ T | InstanceStatusNotSupport | The status of instance not support the operation. |
| 400 | InvalidAttachmentId.NotFound | InvalidAttachmentId.NotFound | The specified AttachmentId is not found. |
| 400 | IncorrectStatus.Attachment | IncorrectStatus.Attachment | The status of Attachment is incorrect. |
| 400 | IllegalParam.AttachmentId | IllegalParam.AttachmentId | The specified AttachmentId is illegal. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ GROUPEXIST _ | InvalidOperation.MulticastGroupExist | Operation is invalid because multicast groups exist. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.7. ListTransitRouterMulticastDomainAssociations

查询组播域的关联信息。

**使用说明**

调用接口时请求参数**TransitRouterMulticastDomainId** 和**TransitRouterAttachmentId** 必须输入一个。 输入**TransitRouterAttachmentId** 表示查询VPC实例下已绑定组播域的交换机的信息。 输入**TransitRouterMulticastDomainId** 表示查询组播域下已绑定的交换机的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ListTransitRouterMulticastDomainAssociati ons | 系统规定参数。取值：ListTransitRouterMulticastDomain Associations 。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-4266**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 否 | tr-mcast-domain-91wpg6wbhchjeq**** | 组播域ID。 |
| TransitRouterAttac hmentId | String | Query | 否 | tr-attach-p90y3ymbbwuvy5**** | 网络实例连接ID。 |
| ResourceType | String | Query | 否 | VPC | 组播域关联的资源类型。 仅取值：VPC 。 |
| ResourceId | String | Query | 否 | vpc-p0w9alkte4w2htrqe**** | 组播域关联的资源的ID。 |
| MaxResults | Long | Query | 否 | 20 | 分批次查询时每次显示的条目数。默认值：20 。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken 值。 |
| VSwitchIds | RepeatList | Query | 否 | vsw-p0w9s2ig1jnwgrbzl**** | 交换机ID列表。 最多支持输入20个交换机ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterMulticastAss ociations | Array |  | 关联信息列表。 |
| - TransitRouterMulticastDo mainId | String | tr-mcast-domain- 91wpg6wbhchjeq**** | 组播域ID。 |
| - TransitRouterAttachmentI d | String | tr-attach-p90y3ymbbwuvy5**** | 网络实例连接ID。 |
| -VSwitchId | String | vsw-p0wxk12u6okfkr8xy**** | 交换机ID。 |
| -Status | String | Dissociating | 关联状态。 Associated ：已关联。 Associating ：关联中。 Dissociating ：解除关联中。 |
| -ResourceType | String | VPC | 组播域关联的资源类型。 仅取值：VPC 。 |
| -ResourceOwnerId | Long | 1210123456123456 | 组播域关联的资源所属的一级组织UID。 |
| -ResourceId | String | vpc-p0w9b7g9l90yofr0n**** | 组播域关联的资源的ID。 |
| RequestId | String | 1CD0969B-A605-5D2D-BFF0- 699FD182FB7F | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastDomainAssociations
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "TransitRouterMulticastAssociations":{ "TransitRouterAttachmentId":"tr-attach-p90y3ymbbwuvy5****", "Status":"Dissociating", "ResourceId":"vpc-p0w9b7g9l90yofr0n****", "TransitRouterMulticastDomainId":"tr-mcast-domain-91wpg6wbhchjeq****", "VSwitchId":"vsw-p0wxk12u6okfkr8xy****", "ResourceType":"VPC", "ResourceOwnerId":1210123456123456 }, "RequestId":"1CD0969B-A605-5D2D-BFF0-699FD182FB7F", "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "MaxResults":20 } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <TransitRouterMulticastAssociations> <TransitRouterAttachmentId>tr-attach-p90y3ymbbwuvy5****</TransitRouterAttachmentId> <Status>Dissociating</Status> <ResourceId>vpc-p0w9b7g9l90yofr0n****</ResourceId> <TransitRouterMulticastDomainId>tr-mcast-domain-91wpg6wbhchjeq****</TransitRouterMulticastDomainId> <VSwitchId>vsw-p0wxk12u6okfkr8xy****</VSwitchId> <ResourceType>VPC</ResourceType> <ResourceOwnerId>1210123456123456</ResourceOwnerId> </TransitRouterMulticastAssociations> <RequestId>1CD0969B-A605-5D2D-BFF0-699FD182FB7F</RequestId> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <MaxResults>20</MaxResults> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The specified NextToken is illegal. |
| 400 | IllegalParam.TransitRouterMultica stDomainId | IllegalParam.TransitRouterMulticastDomainId | The specified TransitRouterMulticastDomainId is illegal. |

#### 1.14.8. RegisterTransitRouterMulticastGroupSources

创建组播源。

**使用说明**

当前仅支持将弹性网卡ENI（Elastic Network Interface）指定为组播源。 在调用RegisterTransitRouterMulticastGroupSources接口创建组播源前，请确保弹性网卡所在的交换机已被关联至组播域。具体操作，请参见

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | RegisterTransitRouterMulticastGroupSource s | 系统规定参数。取值：RegisterTransitRouterMulticastGro upSources。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-4266**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次API 请求的RequestId不一样。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-5mjb5gjb6dgu98**** | 组播源所属的组播域ID。 |

| GroupIpAddress | String | Query | 是 | 239.XX.XX.2 | 组播源所属的组播组的IP地址。取值范围：224.0.0.1~239.255.255.254。 如果当前组播域下不存在您指定的组播组，系统将自动为您创建新的组播组。 |
|---|---|---|---|---|---|
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会创建组播源。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接创建组播源。 |
| VpcId | String | Query | 否 | vpc-wz9fusm6zq8uy7cfa**** | 弹性网卡所属的VPC实例ID。 如果弹性网卡所属阿里云账号和您当前登录的阿里云账号为相同账号，本参数可不填。 如果弹性网卡所属阿里云账号和您当前登录的阿里云账号为不同账号，本参数必填。 |
| NetworkInterfaceIds | RepeatList | Query | 否 | eni-p0w92o2wupc3c05t**** | 弹性网卡ID列表。 当前本参数为必填参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9C5D5D70-0AFF-5E5C-8D8A- E92C90C8FB08 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RegisterTransitRouterMulticastGroupSources &TransitRouterMulticastDomainId=tr-mcast-domain-5mjb5gjb6dgu98**** &GroupIpAddress=239.XX.XX.2
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"9C5D5D70-0AFF-5E5C-8D8A-E92C90C8FB08" } |  |

| XML | 格式 |
|---|---|
| <RequestId>9C5D5D70-0AFF-5E5C-8D8A-E92C90C8FB08</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONPEERMULTI _ _ _ CASTDOMAINSOURCE _ _ | InvalidOperation.PeerMulticastDomainSource | Operation is invalid because peer multicast domain can not be group source. |
| 400 | IllegalParam.GroupIpAddress | IllegalParam.GroupIpAddress | The specified GroupIpAddress is illegal. |
| 400 | InvalidMulticastDomainId.NotFou nd | InvalidMulticastDomainId.NotFound | The specified AttachmentId is not found. |
| 400 | IncorrectStatus.MulticastDomainI d | IncorrectStatus.MulticastDomainId | The status of MulticastDomainId is incorrect. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | INSTANCEEXIST _ | InstanceExist | The instance already exists. |

| 400 | INVALIDOPERATIONNETWORKIN _ _ TERFACENOTEXIST _ _ | InvalidOperation.NetworkInterfaceNotExist | Operation is invalid bacause network interface not exist. |
|---|---|---|---|
| 400 | INVALIDOPERATIONNTRNETW _ _ _ ORKINTERFACENOTSUPPORT _ _ | InvalidOperation.NTRNetworkInterfaceNotSupport | Operation is invalid, due to ntr eni not support. |
| 400 | INSTANCENOTEXIST _ _ | InstanceNotExist | The instance is not exist. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINASSOCIATIONNOTEXIS _ _ _ T | InvalidOperation.MulticastDomainAssociationNotExis t | Operation is invalid because multicast association domain association not exist. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINASSOCIATIONSTATUS _ _ | InvalidOperation.MulticastDomainAssociationStatus | Operation is invalid, due to multicast domain association not Active. |
| 400 | QUOTAFULLMULTICASTGROUP _ _ _ PERDOMAIN _ _ | QuotaFull.MulticastGroupPerDomain | The number of multicast group has exceed the maximum value that can be created. |
| 400 | QUOTAFULLMULTICASTSOURC _ _ _ EPERGROUP _ _ | QuotaFull.MulticastSourcePerGroup | The number of multicast group source has exceed the maximum value that can be created. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.9. DeregisterTransitRouterMulticastGroupSources

删除组播源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DeregisterTransitRouterMulticastGroupSour ces | 系统规定参数。取值：DeregisterTransitRouterMulticastGr oupSources。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-4266**** | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-91wpg6wbhchjeq**** | 组播源所属的组播域ID。 |
| GroupIpAddress | String | Query | 是 | 239.XX.XX.2 | 组播源所属的组播组的IP地址。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会删除组播源。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接删除组播源。 |
| NetworkInterfaceIds | RepeatList | Query | 否 | eni-p0weuda3lszwzjly**** | 组播源ID列表。 当前一个组播组一次最多支持删除五个组播源。 当前本参数为必填参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 53E7E8BE-7F4E-5458-ACCA- 9B5C1D6A642D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeregisterTransitRouterMulticastGroupSources &TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq**** &GroupIpAddress=239.XX.XX.2
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"53E7E8BE-7F4E-5458-ACCA-9B5C1D6A642D" } |  |

| XML | 格式 |
|---|---|
| <RequestId>53E7E8BE-7F4E-5458-ACCA-9B5C1D6A642D</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterMulticastDom ainId.NotFound | InvalidTransitRouterMulticastDomainId.NotFound | The specified TransitRouterMulticastDomainId is not found. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINSTATUS _ | InvalidOperation.MulticastDomainStatus | Operation is invalid, due to multicast domain not Active. |
| 400 | IncorrectStatus.MulticastGroup | IncorrectStatus.MulticastGroup | The status of MulticastGroup is incorrect. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.10. RegisterTransitRouterMulticastGroupMembers

创建组播成员。

**使用说明**

当前转发路由器仅支持将弹性网卡ENI（Elastic Network Interface）指定为组播成员。请确保ENI所属的交换机已被关联至组播域。具体操作，请参见

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | RegisterTransitRouterMulticastGroupMembe rs | 系统规定参数。取值：RegisterTransitRouterMulticastGro upMembers。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426655440000 | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 若您未指定，则系统自动使用API请求的 RequestId作为ClientToken标识。每次API 请求的RequestId不一样。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-91wpg6wbhchjeq**** | 组播成员所属的组播域ID。 |
| GroupIpAddress | String | Query | 是 | 239.XX.XX.2 | 组播成员所属的组播组的IP地址。取值范围： 224.0.0.1~239.255.255.254。 如果当前组播域下不存在您指定的组播组，系统将自动在当前组播域下为您创建新的组播组。 |
| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会创建组播成员。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。 false（默认值）：发送正常请求，通过检查后直接创建组播成员。 |

| VpcId | String | Query | 否 | vpc-wz9fusm6zq8uy7cfa**** | 弹性网卡所属的VPC实例ID。 如果弹性网卡所属的一级组织和您当前使用的一级组织相同，本参数可不填。 如果弹性网卡所属的一级组织和您当前使用的一级组织不同，本参数必填。 |
|---|---|---|---|---|---|
| NetworkInterfaceIds | RepeatList | Query | 否 | eni-p0weuda3lszwzjly**** | 弹性网卡ID。 一次支持关联多个弹性网卡。请确保您指定的弹性网卡个数与跨地域组播域的个数之和小于或等于 5。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | EB985B7E-2CF8-5EC9-A7DB- F7C82ABD3ACE | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RegisterTransitRouterMulticastGroupMembers &TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq**** &GroupIpAddress=239.XX.XX.2
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"EB985B7E-2CF8-5EC9-A7DB-F7C82ABD3ACE" } |  |

| XML | 格式 |
|---|---|
| <RequestId>EB985B7E-2CF8-5EC9-A7DB-F7C82ABD3ACE</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.GroupIpAddress | IllegalParam.GroupIpAddress | The specified GroupIpAddress is illegal. |
| 400 | InvalidMulticastDomainId.NotFou nd | InvalidMulticastDomainId.NotFound | The specified AttachmentId is not found. |
| 400 | IncorrectStatus.MulticastDomainI d | IncorrectStatus.MulticastDomainId | The status of MulticastDomainId is incorrect. |
| 400 | IncorrectStatus.Cen | IncorrectStatus.Cen | The status of Cen is incorrect. |
| 400 | INSTANCENOTEXIST _ _ | InstanceNotExist | The instance is not exist. |
| 400 | INVALIDOPERATIONPEERMULTI _ _ _ CASTDOMAINREGION _ _ | InvalidOperation.PeerMulticastDomainRegion | Operation is invalid because to peer multicast domain in the same region with multicast domain. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINSTATUS _ | InvalidOperation.MulticastDomainStatus | Operation is invalid, due to multicast domain not Active. |
| 400 | INVALIDOPERATIONBANDWIDT _ _ HLIMITNOTEXIST _ _ _ | InvalidOperation.BandwidthLimitNotExist | Operation is invalid because a bandwidth limit not exist. |
| 400 | ATTACHMENTNOTFOUND _ _ | AttachmentNotFound | "The attachment does not exist. |
| 400 | IncorrectStatus.AttachmentId | IncorrectStatus.AttachmentId | The status of AttachmentId is incorrect. |
| 400 | INSTANCEEXIST _ | InstanceExist | The instance already exists. |

| 400 | INVALIDOPERATIONNETWORKIN _ _ TERFACENOTEXIST _ _ | InvalidOperation.NetworkInterfaceNotExist | Operation is invalid bacause network interface not exist. |
|---|---|---|---|
| 400 | INVALIDOPERATIONNTRNETW _ _ _ ORKINTERFACENOTSUPPORT _ _ | InvalidOperation.NTRNetworkInterfaceNotSupport | Operation is invalid, due to ntr eni not support. |
| 400 | INSTANCENOTEXIST _ _ | InstanceNotExist | The instance is not exist. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINASSOCIATIONNOTEXIS _ _ _ T | InvalidOperation.MulticastDomainAssociationNotExis t | Operation is invalid because multicast association domain association not exist. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINASSOCIATIONSTATUS _ _ | InvalidOperation.MulticastDomainAssociationStatus | Operation is invalid, due to multicast domain association not Active. |
| 400 | InvalidPeerTrMulticastDomainId.N otFound | InvalidPeerTrMulticastDomainId.NotFound | The specified PeerTrMulticastDomainId is not found. |
| 400 | IncorrectStatus.PeerTrMulticastD omainId | IncorrectStatus.PeerTrMulticastDomainId | The status of PeerTrMulticastDomainId is incorrect. |
| 400 | IllegalParam.PeerTrMulticastDom ainId | IllegalParam.PeerTrMulticastDomainId | The specified PeerTrMulticastDomainId is illegal. |
| 400 | INVALIDOPERATION _ | InvalidOperation | Operation is invalid. |
| 400 | QUOTAFULLMULTICASTGROUP _ _ _ PERDOMAIN _ _ | QuotaFull.MulticastGroupPerDomain | The number of multicast group has exceed the maximum value that can be created. |
| 400 | QUOTAFULLMULTICASTMEMBE _ _ _ RPERGROUP _ _ | QuotaFull.MulticastMemberPerGroup | The number of multicast group member has exceed the maximum value that can be created. |
| 400 | QUOTAFULLMULTICASTPEER _ _ _ _ MEMBERPERGROUP _ _ | QuotaFull.MulticastPeerMemberPerGroup | The number of multicast group member peer domain has exceed the maximum value that can be created. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.11. DeregisterTransitRouterMulticastGroupMembers

删除组播成员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | DeregisterTransitRouterMulticastGroupMem bers | 系统规定参数。取值：DeregisterTransitRouterMulticastGr oupMembers。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426655440000 | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 是 | tr-mcast-domain-91wpg6wbhchjeq**** | 组播成员所属的组播域ID。 |
| GroupIpAddress | String | Query | 是 | 239.XX.XX.2 | 组播成员所属的组播组的IP地址。 |

| DryRun | Boolean | Query | 否 | false | 是否只预检此次请求。取值： true：发送检查请求，不会删除组播成员。检查项包括是否填写了必需参数、请求格式、业务限制等。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码 DryRunOperation 。 false（默认值）：发送正常请求，通过检查后直接删除组播成员。 |
|---|---|---|---|---|---|
| NetworkInterfaceIds | RepeatList | Query | 否 | eni-p0weuda3lszwzjly**** | 弹性网卡ID列表。 一次支持删除多个弹性网卡。请确保您指定的弹性网卡个数小于或等于5。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 61D0A553-5E4E-53B5-9DA3- 01CBA076A286 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeregisterTransitRouterMulticastGroupMembers &TransitRouterMulticastDomainId=tr-mcast-domain-91wpg6wbhchjeq**** &GroupIpAddress=239.XX.XX.2
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"61D0A553-5E4E-53B5-9DA3-01CBA076A286" } |  |

| XML | 格式 |
|---|---|
| <RequestId>61D0A553-5E4E-53B5-9DA3-01CBA076A286</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTransitRouterMulticastDom ainId.NotFound | InvalidTransitRouterMulticastDomainId.NotFound | The specified TransitRouterMulticastDomainId is not found. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINSTATUS _ | InvalidOperation.MulticastDomainStatus | Operation is invalid, due to multicast domain not Active. |
| 400 | IncorrectStatus.MulticastGroup | IncorrectStatus.MulticastGroup | The status of MulticastGroup is incorrect. |
| 400 | DryRunOperation | DryRunOperation | Request validation has been passed with DryRun flag set. |

#### 1.14.12. ListTransitRouterMulticastGroups

查询组播域下组播成员和组播源的信息。

**使用说明**

您可以调用ListTransitRouterMulticastGroups接口查询组播域下组播成员和组播源（以下简称为组播资源）的信息。 如果您指定**GroupIpAddress**参数的值，则您可以查询组播域下指定组播组下的组播资源的信息。 如果您指定**VSwitchIds**参数的值，则您可以查询组播域下指定交换机下的组播资源的信息。 如果您指定**ResourceType**参数的值，则您可以查询组播域下属于某一资源类型的组播资源的信息。 如果您指定**ResourceId**参数的值，则您可以查询某一资源下组播资源的信息。 如果您仅指定**TransitRouterMulticastDomainId**参数的值，则您可以查询组播域下所有组播资源的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ListTransitRouterMulticastGroups | 系统规定参数。取值：ListTransitRouterMulticastGroups。 |
| ClientToken | String | Query | 否 | 123e4567-e89b-12d3-a456-426655440000 | 客户端Token，用于保证请求的幂等性。 从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。 |
| TransitRouterMultic astDomainId | String | Query | 否 | tr-mcast-domain-5mjb5gjb6dgu98**** | 组播域ID。 |
| GroupIpAddress | String | Query | 否 | 239.XX.XX.2 | 组播组的IP地址。 每个组播组通过一个组播IP地址进行标识。 |
| TransitRouterAttach mentId | String | Query | 否 | tr-attach-g3kz2k3u76amsk**** | 网络实例连接ID。 |
| ResourceType | String | Query | 否 | VPC | 组播资源的类型。 取值：VPC，表示查询专有网络VPC（Virtual Private Cloud）下的组播资源信息。 |
| ResourceId | String | Query | 否 | vpc-p0w9alkte4w2htrqe**** | 组播资源关联的资源ID。 |
| MaxResults | Long | Query | 否 | 20 | 分批次查询时每次显示的条目数。默认值：20。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| IsGroupSource | Boolean | Query | 否 | true | 是否查询组播源。 false ：否。 true：是。 和IsGroupMember配合使用。 |
| IsGroupMember | Boolean | Query | 否 | false | 是否查询组播成员。 false ：否。 true：是。 和IsGroupMember配合使用。 |
| VSwitchIds | RepeatList | Query | 否 | vsw-p0w9s2ig1jnwgrbzl**** | 交换机ID列表。 最多支持输入20个交换机ID。 |
| NetworkInterfaceIds | RepeatList | Query | 否 | eni-p0weuda3lszwzjly**** | 弹性网卡ID列表。 最多支持输入20个弹性网卡ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TransitRouterMulticastGro ups | Array |  | 组播组信息列表。 |
| -GroupIpAddress | String | 239.XX.XX.2 | 组播资源所属的组播组的IP地址。 |
| - TransitRouterAttachmentI d | String | tr-attach-g3kz2k3u76amsk**** | 网络实例连接ID。 |
| -VSwitchId | String | vsw-p0w9s2ig1jnwgrbzl**** | 组播资源所属交换机的ID。 |
| -NetworkInterfaceId | String | eni-p0weuda3lszwzjly**** | 弹性网卡ID（即组播资源ID）。 |

| -Status | String | Registered | 组播资源的状态。 Registering：创建中。 Registered：可用。 Deregistering：删除中。 |
|---|---|---|---|
| -GroupSource | Boolean | false | 当前组播资源是否是组播源。 true：是组播源。 false：不是组播源。 |
| -GroupMember | Boolean | true | 当前组播资源是否是组播成员。 true：是组播成员。 false：不是组播成员。 |
| -MemberType | String | Static | 组播源的类型。 仅返回：Static，表示当前组播源是通过手动方式指定的。 |
| -SourceType | String | Static | 组播成员的类型。 仅返回：Static，表示当前组播成员是通过手动方式指定的。 |
| -ResourceType | String | VPC | 组播资源的类型。 VPC：表示当前组播资源为VPC下的资源。 |
| -ResourceOwnerId | Long | 1250123456123456 | 组播资源所属的一级组织UID。 |
| -ResourceId | String | vpc-p0w9alkte4w2htrqe**** | 组播资源关联的资源ID。 |
| - TransitRouterMulticastDo mainId | String | tr-mcast-domain- kx0vk0v7fz8kx4**** | 组播域ID。 |
| RequestId | String | FB3C4A16-0933-5850-9D43- 0C3EA37BCBFB | 请求ID。 |
| TotalCount | Integer | 1 | 列表条目数。 |
| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastGroups
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "RequestId":"FB3C4A16-0933-5850-9D43-0C3EA37BCBFB",
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "MaxResults":20,
 "TransitRouterMulticastGroups":{
  "TransitRouterAttachmentId":"tr-attach-g3kz2k3u76amsk****",
  "Status":"Registered",
  "GroupMember":true,
  "VSwitchId":"vsw-p0w9s2ig1jnwgrbzl****",
  "SourceType":"Static",
  "ConnectPeerId":"tr-connect-peer-ax66ixf6ubbajw****",
  "ResourceType":"VPC",
  "NetworkInterfaceId":"eni-p0weuda3lszwzjly****",
  "ResourceOwnerId":1250123456123456,
  "GroupIpAddress":"239.XX.XX.2",
  "PeerTransitRouterMulticastDomainId":"tr-mcast-domain-91wpg6wbhchjeq****",
  "MemberType":"Static",
  "ResourceId":"vpc-p0w9alkte4w2htrqe****",
  "TransitRouterMulticastDomainId":"tr-mcast-domain-kx0vk0v7fz8kx4****",
  "GroupSource":false
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <RequestId>FB3C4A16-0933-5850-9D43-0C3EA37BCBFB</RequestId> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <MaxResults>20</MaxResults> <TransitRouterMulticastGroups> <TransitRouterAttachmentId>tr-attach-g3kz2k3u76amsk****</TransitRouterAttachmentId> <Status>Registered</Status> <GroupMember>true</GroupMember> <VSwitchId>vsw-p0w9s2ig1jnwgrbzl****</VSwitchId> <SourceType>Static</SourceType> <ConnectPeerId>tr-connect-peer-ax66ixf6ubbajw****</ConnectPeerId> <ResourceType>VPC</ResourceType> <NetworkInterfaceId>eni-p0weuda3lszwzjly****</NetworkInterfaceId> <ResourceOwnerId>1250123456123456</ResourceOwnerId> <GroupIpAddress>239.XX.XX.2</GroupIpAddress> <PeerTransitRouterMulticastDomainId>tr-mcast-domain-91wpg6wbhchjeq****</PeerTransitRouterMulticastDomainId> <MemberType>Static</MemberType> <ResourceId>vpc-p0w9alkte4w2htrqe****</ResourceId> <TransitRouterMulticastDomainId>tr-mcast-domain-kx0vk0v7fz8kx4****</TransitRouterMulticastDomainId> <GroupSource>false</GroupSource> </TransitRouterMulticastGroups> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The specified NextToken is illegal. |
| 400 | IllegalParam.TransitRouterMultica stDomainId | IllegalParam.TransitRouterMulticastDomainId | The specified TransitRouterMulticastDomainId is illegal. |

#### 1.14.13. ListGrantVSwitchEnis

查询专有网络VPC（Virtual Private Cloud）下可以成为组播源或者组播成员的弹性网卡的信息。

**使用说明**

调用ListGrantVSwitchEnis接口前，请确保VPC实例已被连接至转发路由器。具体操作，请参见CreateTransitRouterVpcAttachment。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | ListGrantVSwitchEnis | 系统规定参数。取值：ListGrantVSwitchEnis。 |
| CenId | String | Query | 是 | cen-a7syd349kne38g**** | VPC实例连接的云企业网实例的ID。 |

| VpcId | String | Query | 是 | vpc-p0w9alkte4w2htrqe**** | VPC实例的ID。 |
|---|---|---|---|---|---|
| VSwitchId | String | Query | 是 | vsw-p0w9s2ig1jnwgrbzl**** | VPC实例下的一个交换机ID。 一次仅支持查询一个交换机下的弹性网卡的信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| GrantVSwitchEnis | Array |  | 弹性网卡信息列表。 |
| -VpcId | String | vpc-p0w9alkte4w2htrqe**** | VPC实例ID。 |
| -VSwitchId | String | vsw-p0w9s2ig1jnwgrbzl**** | 交换机ID。 |
| -NetworkInterfaceId | String | eni-p0w172vv82kxzb49**** | 弹性网卡ID。 |
| -Description | String | created by CBN | 弹性网卡的描述信息。 |
| -TransitRouterFlag | Boolean | false | 当前弹性网卡是否是转发路由器创建的。 true：是。 false：否。 转发路由器创建的弹性网卡不支持成为组播源或者组播成员。 |
| RequestId | String | DBFE1736-2F33-5309-9954- 875B11E9519D | 请求ID。 |
| TotalCount | String | 6 | 列表条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListGrantVSwitchEnis &CenId=cen-a7syd349kne38g**** &VpcId=vpc-p0w9alkte4w2htrqe**** &VSwitchId=vsw-p0w9s2ig1jnwgrbzl****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":"6", "RequestId":"DBFE1736-2F33-5309-9954-875B11E9519D", "GrantVSwitchEnis":{ "Description":"created by CBN", "TransitRouterFlag":false, "VpcId":"vpc-p0w9alkte4w2htrqe****", "VSwitchId":"vsw-p0w9s2ig1jnwgrbzl****", "NetworkInterfaceId":"eni-p0w172vv82kxzb49****" } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>6</TotalCount> <RequestId>DBFE1736-2F33-5309-9954-875B11E9519D</RequestId> <GrantVSwitchEnis> <Description>created by CBN</Description> <TransitRouterFlag>false</TransitRouterFlag> <VpcId>vpc-p0w9alkte4w2htrqe****</VpcId> <VSwitchId>vsw-p0w9s2ig1jnwgrbzl****</VSwitchId> <NetworkInterfaceId>eni-p0w172vv82kxzb49****</NetworkInterfaceId> </GrantVSwitchEnis> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

| 400 | InvalidCenId.NotFound | InvalidCenId.NotFound | The specified CenId is not found. |
|---|---|---|---|
| 400 | InvalidVpcId.NotFound | InvalidVpcId.NotFound | The specified VpcId is not found. |
| 400 | INVALIDOPERATIONMULTICAST _ _ _ DOMAINASSOCIATIONNOTEXIS _ _ _ T | InvalidOperation.MulticastDomainAssociationNotExis t | Operation is invalid because multicast association domain association not exist. |

#### 1.14.14. ListTransitRouterMulticastDomainVSwitches

查询专有网络VPC（Virtual Private Cloud）实例下已关联组播域的交换机的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ListTransitRouterMulticastDomainVSwitches | 系统规定参数。取值：ListTransitRouterMulticastDomainV Switches。 |
| CenId | String | Query | 是 | cen-44m0p68spvlrqq**** | 云企业网实例ID。 |
| VpcId | String | Query | 是 | vpc-p0wr1cd4fcuxy3ui0**** | VPC实例ID。 |
| MaxResults | Integer | Query | 否 | 20 | 分批次查询时每次显示的条目数。最小值：0。默认值：20。 |
| NextToken | String | Query | 否 | FFmyTO70tTpLG6I3FmYAXGKPd**** | 是否拥有下一次查询的令牌（Token）。取值： 第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次API调用返回的NextToken值。 |
| VSwitchIds | RepeatList | Query | 否 | 交换机ID列表。 | 交换机ID列表。 一次最多支持输入50个交换机ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| VSwitchIds | String | vsw-p0w5ejr9bzfsttiza**** | 交换机ID列表。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken为空表示没有下一次查询。 如果NextToken有返回值，该取值表示下一次查询开始的令牌。 |
| RequestId | String | B0E7E43C-979A-5130-AA0D- B3ADA69E0827 | 请求ID。 |
| TotalCount | Integer | 2 | 列表条目数。 |
| MaxResults | Integer | 20 | 分批次查询时每次显示的条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListTransitRouterMulticastDomainVSwitches &CenId=cen-44m0p68spvlrqq**** &VpcId=vpc-p0wr1cd4fcuxy3ui0****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":2,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "RequestId":"B0E7E43C-979A-5130-AA0D-B3ADA69E0827",
 "VSwitchIds":"vsw-p0w5ejr9bzfsttiza****",
 "MaxResults":20
}
```

| XML | 格式 |
|---|---|
| <TotalCount>2</TotalCount> <NextToken>FFmyTO70tTpLG6I3FmYAXGKPd****</NextToken> <RequestId>B0E7E43C-979A-5130-AA0D-B3ADA69E0827</RequestId> <VSwitchIds>vsw-p0w5ejr9bzfsttiza****</VSwitchIds> <MaxResults>20</MaxResults> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IllegalParam.NextToken | IllegalParam.NextToken | The specified NextToken is invalid. |
| 400 | IllegalParam.TrInstance | IllegalParam.TrInstance | The specified TransitRouter is invalid. |
| 400 | IllegalParam.Region | IllegalParam.Region | The specified Region is invalid. |

### 路由策略

#### 1.15.1. CreateCenRouteMap

创建路由策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | CreateCenRouteMap | 系统规定操作。取值：CreateCenRouteMap。 |
| CenId | String | Query | 是 | cen-7qthudw0ll6jmc**** | 云企业网实例ID。 |
| CenRegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 路由策略应用的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| TransmitDirection | String | Query | 是 | RegionIn | 路由策略的应用方向。取值： RegionIn：入地域网关方向，表示路由传入云企业网地域网关的方向。 例如：路由从本地域的网络实例发布到本地域网关，或其他地域的路由发布到本地域网关。 RegionOut：出地域网关方向，表示路由传出云企业网地域网关的方向。 例如：路由从本地域网关发布到本地域下的网络实例，或发布到其他地域的地域网关。 |
| Description | String | Query | 否 | desctest | 路由策略的描述信息。 描述长度为2~256个字符，不能以 http:// 或 https:// 开始，必须以中文或英文开始，可包含数字、短划线（-）、半角句号（.）和下划线（_）。 |
| Priority | Integer | Query | 是 | 3 | 路由策略的优先级。取值范围：1~100。优先级数字越小，表示优先级越高。 同地域、同应用方向的路由策略优先级唯一。执行路由策略时，系统从优先级数字最小的路由策略开始匹配条件语句，因此在指定路由策略优先级时，要注意符合期望的匹配顺序。 |

| MapResult | String | Query | 是 | Permit | 所有条件都匹配后的策略行为。取值： Permit：允许匹配的路由通过。 Deny：拒绝匹配的路由通过。 |
|---|---|---|---|---|---|
| NextPriority | Integer | Query | 否 | 20 | 关联的下一条路由策略的优先级。 仅MapResult取值为Permit时，才支持设置关联策略优先级，且被允许通过的路由才会继续匹配关联的下一条路由策略。 要关联的下一条路由策略必须和当前路由策略拥有相同的地域和应用方向。 关联的下一条路由策略的优先级必须低于当前路由策略的优先级。 |
| CidrMatchMode | String | Query | 否 | Include | 前缀列表的匹配模式。取值： Include：模糊匹配。匹配条件中的路由前缀包含被匹配路由的路由前缀即判定为匹配成功。 例如：定义10.10.0.0/16的策略可以模糊匹配到 10.10.1.0/24的路由。 Complete：精确匹配。匹配条件中的路由前缀必须与被匹配路由的路由前缀一致，才判定为匹配成功。 例如：定义10.10.0.0/16的策略仅可以精确匹配到10.10.0.0/16的路由。 |
| AsPathMatchMode | String | Query | 否 | Include | AS Path列表的匹配模式。取值： Include：模糊匹配，匹配条件中的AS Path与被匹配路由的AS Path有重叠即判定为匹配成功。 Complete：精确匹配，匹配条件中的AS Path必须与被匹配路由的AS Path一致，才判定为匹配成功。 |
| CommunityMatchM ode | String | Query | 否 | Include | Community的匹配模式。取值： Include：模糊匹配，匹配条件中的 Community与被匹配路由的Community有重叠即判定为匹配成功。 Complete：精确匹配，匹配条件中的 Community必须与被匹配路由的Community 一致，才判定为匹配成功。 |
| CommunityOperate Mode | String | Query | 否 | Additive | Community的执行模式。取值： Additive：添加，表示为路由添加 Community。 Replace：替换，表示替换路由原有的 Community。 本参数表示路由通过匹配条件后，要执行的操作。 |
| Preference | Integer | Query | 否 | 50 | 修改路由的优先级。 取值范围：1~100。路由的优先级默认为50，取值越小优先级越高。 本参数表示路由通过匹配条件后，要执行的操作。 |
| SourceInstanceIdsR everseMatch | Boolean | Query | 否 | false | 是否使用源实例ID列表的排除匹配模式。取值： false（默认值）：否，即路由传递的源实例ID 在SourceInstanceIds.N中时，匹配通过。 true：是，即路由传递的源实例ID不在SourceInstanceIds.N中时，匹配通过。 |
| DestinationInstance IdsReverseMatch | Boolean | Query | 否 | false | 是否使用目的实例ID列表的排除匹配模式。取值： false（默认值）：否，即路由传递的目的实例 ID在DestinationInstanceIds.N中时，匹配通过。 true：是，即路由传递的目的实例ID不在DestinationInstanceIds.N中时，匹配通过。 |
| MatchAddressType | String | Query | 否 | IPv4 | 路由需匹配的IP地址类型。取值： IPv4：表示只匹配IPv4路由。 IPv6：表示只匹配IPv6路由。 本参数可以为空，表示匹配所有类型的路由。 |
| TransitRouterRoute TableId | String | Query | 否 | vtb-gw8nx3515m1mbd1z1**** | 转发路由器的路由表ID。 如果您不输入路由表ID，则路由策略自动关联至转发路由器的默认路由表。 |

| SourceInstanceIds | RepeatList | Query | 否 | vpc-adeg3544fdf34vf**** | 路由需匹配的源实例ID列表。支持输入以下类型的实例ID： 专有网络VPC（Virtual Private Cloud）实例 ID 边界路由器VBR（Virtual Border Router）实例ID 最多支持输入32个实例ID。 |
|---|---|---|---|---|---|
| DestinationInstance Ids | RepeatList | Query | 否 | vpc-afrfs434465fdf**** | 路由需匹配的目的实例ID列表。支持输入以下类型的实例ID： 专有网络VPC（Virtual Private Cloud）实例 ID 边界路由器VBR（Virtual Border Router）实例ID 最多支持输入32个实例ID。 仅路由策略的应用方向为出地域网关方向， 且目的实例ID为本地域下的实例ID时，目的实例ID列表才会生效。 |
| SourceRouteTableId s | RepeatList | Query | 否 | vtb-adfr233vf34rvd4**** | 路由需匹配的源路由表ID列表。最多支持输入32 个路由表ID。 |
| DestinationRouteTa bleIds | RepeatList | Query | 否 | vtb-adefrgtr144vf**** | 路由需匹配的目的路由表ID列表。最多支持输入 32个路由表ID。 仅路由策略的应用方向为出地域网关方向， 且目的路由表ID为本地域下网络实例的路由表ID时，目的路由表ID列表才会生效。 |
| SourceRegionIds | RepeatList | Query | 否 | cn-qingdao-env17e-d01 | 路由需匹配的源地域ID列表。最多支持输入32个地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| SourceChildInstance Types | RepeatList | Query | 否 | VPC | 路由需匹配的源实例类型列表。支持以下实例类型： VPC：专有网络实例。 VBR：边界路由器实例。 支持输入多种实例类型。 |
| DestinationChildInst anceTypes | RepeatList | Query | 否 | VPC | 路由需匹配的目的实例类型列表。支持以下实例类型： VPC：专有网络实例。 VBR：边界路由器实例。 支持输入多种实例类型。 仅路由策略的应用方向为出地域网关方向， 且目的实例类型为本地域下的实例类型时， 目的实例类型列表才会生效。 |
| DestinationCidrBloc ks | RepeatList | Query | 否 | 10.10.10.0/24 | 路由需匹配的前缀列表。 前缀列表中的IP地址段使用CIDR格式，最多支持输入32个IP地址段。 |
| RouteTypes | RepeatList | Query | 否 | System | 路由需匹配的路由类型列表。支持以下路由类型： System：系统路由，由系统自动生成的路由。 Custom：自定义路由，由用户手动添加的路由。 BGP：BGP路由，通过BGP路由协议传播的路由。 支持输入多种路由类型。 |
| MatchAsns | RepeatList | Query | 否 | 65501 | 路由需匹配的AS Path列表。 最多支持输入32个AS号码。 仅支持AS SEQUENCE，不支持AS SET、AS CONFED SEQUENCE和AS CONFED SET，即只能是AS号列表，不支持集合和子列表。 |

| MatchCommunitySe t | RepeatList | Query | 否 | 65501:1 | 路由需匹配的Community集合。 每个Community格式为n:m，n、m的取值范围为1~65535。Community需要符合RFC 1997，不支持Large Community（RFC 8092）。 最多支持输入32个Community。 Community配置错误可能会导致路由不能发布到本地数据中心。 |
|---|---|---|---|---|---|
| OperateCommunity Set | RepeatList | Query | 否 | 65501:1 | 要执行的Community集合。 每个Community格式为n:m，n、m的取值范围为1~65535。Community需要符合RFC 1997，不支持Large Communities（RFC 8092）。 最多支持输入32个Community。 Community配置错误可能会导致路由不能发布到本地数据中心。 |
| PrependAsPath | RepeatList | Query | 否 | 65501 | 地域网关接收或发布路由时附加的AS Path。 路由策略应用方向不同，配置附加AS Path的要求也不同，具体如下： 入地域网关方向配置附加AS Path时，匹配条件中必须配置源实例ID列表和源地域，且源地域必须与路由策略应用的地域一致。 出地域网关方向配置附加AS Path时，匹配条件中必须配置目的实例ID列表。 本参数表示路由通过匹配条件后，要执行的操作。 最多支持输入32个AS号码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RouteMapId | String | cenrmap-w4yf7toozfol3q**** | 路由策略的ID。 |
| RequestId | String | 62172DD5-6BAC-45DF-8D44- 56SDF467BAC | 请求ID。 |

**示例**

请求示例

```
&CenId=cen-7qthudw0ll6jmc**** &CenRegionId=cn-qingdao-env17e-d01 &TransmitDirection=RegionIn &Priority=3 &MapResult=Permit
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"62172DD5-6BAC-45DF-8D44-56SDF467BAC", "RouteMapId":"cenrmap-w4yf7toozfol3q****" } |  |

| XML | 格式 |
|---|---|
| <RequestId>62172DD5-6BAC-45DF-8D44-56SDF467BAC</RequestId> <RouteMapId>cenrmap-w4yf7toozfol3q****</RouteMapId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONROUTEMAP _ _ _ CONFIGEXIST _ | Forbidden.CenRouteMapExist | The specified CEN route map ID already exists. |
| 400 | PARAMETERILLEGALRMAPSRC _ _ _ _ REGION | Invid.Parameter | When using PrependAsPath in the RegionIn, SourceRegionId must be local region Id. |

| 400 | INVALIDOPERATIONROUTEMAP _ _ _ INVALIDACTION _ _ | InvalidOperation.NoEffictiveAction | No effective action be configured. |
|---|---|---|---|
| 400 | PARAMETERILLEGALRMAPWIT _ _ _ HGWREGIONSRCREGIONEMP _ _ _ _ _ TY | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be null |
| 400 | PARAMETERILLEGALRMAPWIT _ _ _ HGWREGIONGWZONEEMPTY _ _ _ _ _ | Invid.Parameter | When using GatewayRegionId, GatewayZoneId must not be null |
| 400 | PARAMETERILLEGALRMAPWIT _ _ _ HGWREGIONSRCREGIONILLE _ _ _ _ _ GAL | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be the same with tr region id |
| 400 | PARAMETERILLEGALRMAPGW _ _ _ _ REGIONID _ | Invid.Parameter | GatewayRegionId is invalid |
| 400 | INVALIDOPERATIONTRANSITRO _ _ UTERNOTEXIST _ _ | Invid.Parameter | TransitRouter not exist. |
| 400 | PARAMETERILLEGALRMAPSRC _ _ _ _ INSTANCE | Invid.Parameter | SourceInstanceId is invalid. |
| 400 | PARAMETERILLEGALRMAPDES _ _ _ TINSTANCE _ | Invid.Parameter | DestinationInstanceId is invalid. |
| 400 | IncorrectStatus.TransitRouter | IncorrectStatus.TransitRouterInstance | The status of TransitRouter is incorrect. |

#### 1.15.2. ModifyCenRouteMap

修改路由策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | ModifyCenRouteMap | 系统规定参数。取值：ModifyCenRouteMap。 |
| CenId | String | Query | 是 | cen-7qthudw0ll6jmc**** | 云企业网实例ID。 |
| CenRegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 路由策略应用的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| RouteMapId | String | Query | 是 | cenrmap-abcdedfghij**** | 路由策略的ID。 |
| Description | String | Query | 否 | desctest | 路由策略的描述信息。 描述不能以 http:// 或 https:// 开始， 必须以中文或英文开始，可包含数字、短划线 （-）、半角句号（.）和下划线（_）。 |
| MapResult | String | Query | 是 | Permit | 所有条件都匹配后的策略行为。取值： Permit：允许匹配的路由通过。 Deny：拒绝匹配的路由通过。 |
| NextPriority | Integer | Query | 否 | 20 | 关联的下一条路由策略的优先级。 仅MapResult取值为Permit时，才支持设置关联策略优先级，且被允许通过的路由才会继续匹配关联的下一条路由策略。 要关联的下一条路由策略必须和当前路由策略拥有相同的地域和应用方向。 关联的下一条路由策略的优先级必须低于（数字大于）当前路由策略的优先级。 |

| CidrMatchMode | String | Query | 否 | Include | 前缀列表的匹配模式。取值： Include：模糊匹配。匹配条件中的路由前缀包含被匹配路由的路由前缀即判定为匹配成功。 例如：定义10.10.0.0/16的策略可以模糊匹配到 10.10.1.0/24的路由。 Complete：精确匹配。匹配条件中的路由前缀必须与被匹配路由的路由前缀一致，才判定为匹配成功。 例如：定义10.10.0.0/16的策略仅可以精确匹配到10.10.0.0/16的路由。 |
|---|---|---|---|---|---|
| AsPathMatchMode | String | Query | 否 | Include | AS Path列表的匹配模式。取值： Include：模糊匹配，匹配条件中的AS Path与被匹配路由的AS Path有重叠即判定为匹配成功。 Complete：精确匹配，匹配条件中的AS Path必须与被匹配路由的AS Path一致，才判定为匹配成功。 |
| CommunityMatchM ode | String | Query | 否 | Include | Community的匹配模式。取值： Include：模糊匹配，匹配条件中的 Community与被匹配路由的Community有重叠即判定为匹配成功。 Complete：精确匹配，匹配条件中的 Community必须与被匹配路由的Community 一致，才判定为匹配成功。 |
| CommunityOperate Mode | String | Query | 否 | Additive | Community的执行模式。取值： Additive：添加，表示为路由添加 Community。 Replace：替换，表示替换路由原有的 Community。 本参数表示路由通过匹配条件后，要执行的操作。 |
| Preference | Integer | Query | 否 | 22 | 修改路由的优先级。 取值范围：1~100。路由的优先级默认为50，取值越小优先级越高。 本参数表示路由通过匹配条件后，要执行的操作。 |
| Priority | Integer | Query | 是 | 10 | 路由策略的优先级。取值范围：1~100。优先级数字越小，表示优先级越高。 同地域、同应用方向的路由策略优先级唯一。执行路由策略时，系统从优先级数字最小的路由策略开始匹配条件语句，因此在指定路由策略优先级时，要注意符合期望的匹配顺序。 |
| SourceInstanceIdsR everseMatch | Boolean | Query | 否 | false | 是否使用源实例ID列表的排除匹配模式。取值： false（默认值）：否，即路由传递的源实例ID 在SourceInstanceIds.N中时，匹配通过。 true：是，即路由传递的源实例ID不在SourceInstanceIds.N中时，匹配通过。 |
| DestinationInstance IdsReverseMatch | Boolean | Query | 否 | false | 是否使用目的实例ID列表的排除匹配模式。取值： false（默认值）：否，即路由传递的目的实例 ID在DestinationInstanceIds.N中时，匹配通过。 true：是，即路由传递的目的实例ID不在DestinationInstanceIds.N中时，匹配通过。 |
| MatchAddressType | String | Query | 否 | IPv4 | 路由需匹配的IP地址类型。取值： IPv4：表示只匹配IPv4路由。 IPv6：表示只匹配IPv6路由。 本参数可以为空，表示匹配所有类型的路由。 |

| SourceInstanceIds | RepeatList | Query | 否 | vpc-afsfdf5435vcvc**** | 路由需匹配的源实例ID列表。支持输入以下类型的实例ID： 专有网络VPC（Virtual Private Cloud）实例 ID 边界路由器VBR（Virtual Border Router）实例ID 云连接网CCN（Cloud Connect Network）实例ID 智能接入网关（Smart Access Gateway）实例ID IPsec连接ID 最多支持输入32个实例ID。 |
|---|---|---|---|---|---|
| DestinationInstance Ids | RepeatList | Query | 否 | vpc-avcdsg34ds**** | 路由需匹配的目的实例ID列表。支持输入以下类型的实例ID： 专有网络VPC（Virtual Private Cloud）实例 ID 边界路由器VBR（Virtual Border Router）实例ID 云连接网CCN（Cloud Connect Network）实例ID 智能接入网关（Smart Access Gateway）实例ID IPsec连接ID 最多支持输入32个实例ID。 仅路由策略的应用方向为出地域网关方向， 且目的实例ID为本地域下的实例ID时，目的实例ID列表才会生效。 |
| SourceRouteTableId s | RepeatList | Query | 否 | vtb-acdbvtbr342cd**** | 路由需匹配的源路由表ID列表。最多支持输入32 个路由表ID。 |
| DestinationRouteTa bleIds | RepeatList | Query | 否 | vtb-adfg53c322v**** | 路由需匹配的目的路由表ID列表。最多支持输入 32个路由表ID。 仅路由策略的应用方向为出地域网关方向， 且目的路由表ID为本地域下网络实例的路由表ID时，目的路由表ID列表才会生效。 |
| SourceRegionIds | RepeatList | Query | 否 | cn-qingdao-env17e-d01 | 路由需匹配的源地域ID列表。最多支持输入32个地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| SourceChildInstance Types | RepeatList | Query | 否 | VPC | 路由需匹配的源实例类型列表。支持以下实例类型： VPC：专有网络实例。 VBR：边界路由器实例。 |
| DestinationChildInst anceTypes | RepeatList | Query | 否 | VPC | 路由需匹配的目的实例类型列表。支持以下实例类型： VPC：专有网络实例。 VBR：边界路由器实例。 仅路由策略的应用方向为出地域网关方向，且目的实例类型为本地域下的实例类型时，目的实例类型列表才会生效。 |
| DestinationCidrBloc ks | RepeatList | Query | 否 | 10.10.10.0/24 | 路由需匹配的前缀列表。 前缀列表中的IP地址段使用CIDR格式，最多支持输入32个IP地址段。 |
| RouteTypes | RepeatList | Query | 否 | System | 路由需匹配的路由类型列表。支持以下路由类型： System：系统路由，由系统自动生成的路由。 Custom：自定义路由，由用户手动添加的路由。 BGP：BGP路由，通过BGP路由协议传播的路由。 |
| MatchAsns | RepeatList | Query | 否 | 65501 | 路由需匹配的AS Path列表。 仅支持AS SEQUENCE，不支持AS SET、AS CONFED SEQUENCE和AS CONFED SET，即只能是AS号列表，不支持集合和子列表。 |

| MatchCommunitySe t | RepeatList | Query | 否 | 65501:1 | 路由需匹配的Community集合。 每个Community格式为n:m，n、m的取值范围为1~65535。Community需要符合RFC 1997，不支持Large Community（RFC 8092）。 最多支持输入32个Community。 Community配置错误可能会导致路由不能发布到本地数据中心。 |
|---|---|---|---|---|---|
| OperateCommunity Set | RepeatList | Query | 否 | 65501:1 | 要执行的Community集合。 每个Community格式为n:m，n、m的取值范围为1~65535。Community需要符合RFC 1997，不支持Large Communities（RFC 8092）。 最多支持输入32个Community。 Community配置错误可能会导致路由不能发布到本地数据中心。 |
| PrependAsPath | RepeatList | Query | 否 | 65501 | 地域网关接收或发布路由时附加的AS Path。 路由策略应用方向不同，配置附加AS Path的要求也不同，具体如下： 入地域网关方向配置附加AS Path时，匹配条件中必须配置源实例ID列表和源地域，且源地域必须与路由策略应用的地域一致。 出地域网关方向配置附加AS Path时，匹配条件中必须配置目的实例ID列表。 本参数表示路由通过匹配条件后，要执行的操作。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 54B48E3D-DF70-471B-AA93- 08E683A1B457 | 请求ID。 |

**示例**

请求示例

```
&CenId=cen-7qthudw0ll6jmc**** &CenRegionId=cn-qingdao-env17e-d01 &RouteMapId=cenrmap-abcdedfghij**** &MapResult=Permit &Priority=10
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"54B48E3D-DF70-471B-AA93-08E683A1B457\t" } |  |

`XML` 格式

```xml
<RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457 </RequestId>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONROUTEMAP _ _ _ INVALIDACTION _ _ | InvalidOperation.NoEffictiveAction | No effective action be configured. |
| 400 | INVALIDOPERATIONROUTEMAP _ _ _ CONFIGEXIST _ | InvalidOperation.CenRouteMapExist | Operation is invalid because an route map config exist. |
| 400 | PARAMETERILLEGALRMAPWIT _ _ _ HGWREGIONSRCREGIONEMP _ _ _ _ _ TY | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be null |

| 400 | PARAMETERILLEGALRMAPWIT _ _ _ HGWREGIONGWZONEEMPTY _ _ _ _ _ | Invid.Parameter | When using GatewayRegionId, GatewayZoneId must not be null |
|---|---|---|---|
| 400 | PARAMETERILLEGALRMAPWIT _ _ _ HGWREGIONSRCREGIONILLE _ _ _ _ _ GAL | Invid.Parameter | When using GatewayRegionId, SourceRegionId must not be the same with tr region id |
| 400 | PARAMETERILLEGALRMAPGW _ _ _ _ REGIONID _ | Invid.Parameter | GatewayRegionId is invalid |

#### 1.15.3. DescribeCenRouteMaps

查询路由策略信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCenRouteMaps | 系统规定参数。取值：DescribeCenRouteMaps。 |
| PageNumber | Integer | Query | 否 | 1 | 列表的页码。默认值：1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。默认值：10。 |
| CenId | String | Query | 是 | cen-wx12mmlt17ld82**** | 云企业网实例ID。 |
| RouteMapId | String | Query | 否 | cenrmap-y40mxdvf7joc12**** | 路由策略ID。 |
| CenRegionId | String | Query | 否 | cn-qingdao-env66-d01 | 路由策略应用的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| TransmitDirection | String | Query | 否 | RegionOut | 路由策略的应用方向。取值： RegionIn：入地域网关方向，表示路由传入云企业网地域网关的方向。 例如：路由从本地域的网络实例发布到本地域网关，或其他地域的路由发布到本地域网关。 RegionOut：出地域网关方向，表示路由传出云企业网地域网关的方向。 例如：路由从本地域网关发布到本地域下的网络实例，或发布到其他地域的地域网关。 |
| TransitRouterRoute TableId | String | Query | 否 | vtb-gw8nx3515m1mbd1z1**** | 路由策略关联的转发路由器路由表ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RouteMaps | Array |  | 路由策略信息列表。 |
| -SourceRegionIds | Normal | cn-qingdao-env66-d01 | 路由需匹配的源地域ID列表。 |
| - SourceChildInstanceTypes | Normal | VPC | 路由需匹配的源实例类型列表。 VPC：专有网络实例。 VBR：边界路由器实例。 |
| -DestinationRouteTableIds | Normal | vtb-adefrgtr144vf**** | 路由需匹配的目的路由表ID列表。最多支持输入32个路由表ID。 仅路由策略的应用方向为出地域网关方向，且目的路由表ID为本地域下网络实例的路由表ID时，目的路由表ID列表才会生效。 |
| -SourceInstanceIds | Normal | vpc-adeg3544fdf34vf**** | 路由需匹配的源实例ID列表。 |
| -DestinationCidrBlocks | Normal | 10.10.10.0/24 | 路由需匹配的前缀列表。 |

| -SourceRouteTableIds | Normal | vtb-adfr233vf34rvd4**** | 路由需匹配的源路由表ID列表。 |
|---|---|---|---|
| -MatchCommunitySet | Normal | 65501:1 | 路由需匹配的Community集合。 |
| -PrependAsPath | Normal | 65501 | 地域网关接收或发布路由时附加的AS Path。 本参数表示路由通过匹配条件后，要执行的操作。 |
| -RouteTypes | Normal | System | 路由需匹配的路由类型列表。 System：系统路由，由系统自动生成的路由。 Custom：自定义路由，由用户手动添加的路由。 BGP：BGP路由，通过BGP路由协议传播的路由。 |
| - DestinationChildInstanceT ypes | Normal | VPC | 路由需匹配的目的实例类型列表。 VPC：专有网络实例。 VBR：边界路由器实例。 仅路由策略的应用方向为出地域网关方向，且目的实例类型为本地域下的实例类型时，目的实例类型列表才会生效。 |
| -DestinationInstanceIds | Normal | vpc-afrfs434465fdf**** | 路由需匹配的目的实例ID列表。 仅路由策略的应用方向为出地域网关方向，且目的实例ID为本地域下的实例 ID时，目的实例ID列表才会生效。 |
| -MatchAsns | Normal | 65501 | 路由需匹配的AS Path列表。 |
| -OperateCommunitySet | Normal | 65501:1 | 要执行的Community集合。 |
| -RouteMapId | String | cenrmap-y40mxdvf7joc12**** | 路由策略ID。 |
| -Status | String | Active | 路由策略的状态。 Creating：创建中。 Active：可用。 Deleting：删除中。 |
| -TransmitDirection | String | RegionOut | 路由策略的应用方向。 |
| - SourceInstanceIdsReverse Match | Boolean | false | 是否使用了源实例ID列表的排除匹配模式。 false：否，即路由传递的源实例ID在SourceInstanceIds.N中时，匹配通过。 true：是，即路由传递的源实例ID不在SourceInstanceIds.N中时，匹配通过。 |
| -CenRegionId | String | cn-qingdao-env66-d01 | 路由策略应用的地域ID。 |
| -CenId | String | cen-wx12mmlt17ld82**** | 云企业网实例ID。 |
| -Priority | Integer | 5000 | 路由策略的优先级。优先级数字越小，代表优先级越高。 |
| - TransitRouterRouteTableI d | String | vtb-gw8nx3515m1mbd1z1**** | 路由策略关联的转发路由器路由表ID。 |
| -CommunityOperateMode | String | Additive | Community的执行模式。 Additive：添加，表示为路由添加Community。 Replace：替换，表示替换路由原有的Community。 本参数表示路由通过匹配条件后，要执行的操作。 |
| -MapResult | String | Deny | 所有匹配条件都通过后的策略行为。 Permit：允许被匹配的路由通过。 Deny：拒绝被匹配的路由通过。 |
| -CommunityMatchMode | String | Include | Community的匹配模式。 Include：模糊匹配，匹配条件中的Community与被匹配路由的Community 有重叠即判定为匹配成功。 Complete：精确匹配，匹配条件中的Community必须与被匹配路由的 Community一致，才判定为匹配成功。 |

| -Description | String | desctest | 路由策略的描述信息。 |
|---|---|---|---|
| -AsPathMatchMode | String | Include | AS Path列表的匹配模式。 Include：模糊匹配，匹配条件中的AS Path与被匹配路由的AS Path有重叠即判定为匹配成功。 Complete：精确匹配，匹配条件中的AS Path必须与被匹配路由的AS Path 一致，才判定为匹配成功。 |
| -Preference | Integer | 20 | 要修改的路由的优先级。 优先级数字越小表示优先级越高。 本参数表示路由通过匹配条件后，要执行的操作。 |
| - DestinationInstanceIdsRe verseMatch | Boolean | false | 是否使用了目的实例ID列表的排除匹配模式。 false：否，即路由传递的目的实例ID在DestinationInstanceIds.N中时，匹配通过。 true：是，即路由传递的目的实例ID不在DestinationInstanceIds.N中时，匹配通过。 |
| -CidrMatchMode | String | Include | 前缀列表的匹配模式。取值： Include：模糊匹配。匹配条件中的路由前缀包含被匹配路由的路由前缀即判定为匹配成功。 例如：定义10.10.0.0/16的策略可以模糊匹配到10.10.1.0/24的路由。 Complete：精确匹配。匹配条件中的路由前缀必须与被匹配路由的路由前缀一致，才判定为匹配成功。 例如：定义10.10.0.0/16的策略仅可以精确匹配到10.10.0.0/16的路由。 |
| -NextPriority | Integer | 33 | 关联的下一条路由策略的优先级。 |
| -MatchAddressType | String | IPv4 | 路由需匹配的IP地址类型。 IPv4：表示只匹配IPv4路由。 IPv6：表示只匹配IPv6路由。 如果系统未返回该值，则表示同时匹配IPv4和IPv6的路由。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |
| RequestId | String | 24CE1987-D1D1-5324-9BAD- 2750B60E6ABB | 请求ID。 |
| PageNumber | Integer | 1 | 列表的页码。 |
| TotalCount | Integer | 1 | 列表条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCenRouteMaps &CenId=cen-wx12mmlt17ld82****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"24CE1987-D1D1-5324-9BAD-2750B60E6ABB",
 "PageNumber":1,
 "RouteMaps":{
  "MatchAddressType":"IPv4",
  "Description":"desctest",
  "SourceInstanceIdsReverseMatch":false,
  "TransmitDirection":"RegionOut",
  "MatchCommunitySet":"65501:1",
  "CenRegionId":"cn-qingdao-env66-d01",
  "SourceRouteTableIds":"vtb-adfr233vf34rvd4****",
  "DestinationInstanceIds":"vpc-afrfs434465fdf****",
  "SourceInstanceIds":"vpc-adeg3544fdf34vf****",
  "DestinationInstanceIdsReverseMatch":false,
  "DestinationRouteTableIds":"vtb-adefrgtr144vf****",
  "DestinationCidrBlocks":"10.10.10.0/24",
  "RouteMapId":"cenrmap-y40mxdvf7joc12****",
  "OperateCommunitySet":"65501:1",
  "DestinationChildInstanceTypes":"VPC",
  "Status":"Active",
  "Priority":5000,
  "SourceChildInstanceTypes":"VPC",
  "AsPathMatchMode":"Include",
  "MapResult":"Deny",
  "CidrMatchMode":"Include",
  "RouteTypes":"System",
  "TransitRouterRouteTableId":"vtb-gw8nx3515m1mbd1z1****",
  "Preference":20,
  "CommunityOperateMode":"Additive",
  "CenId":"cen-wx12mmlt17ld82****",
  "PrependAsPath":"65501",
  "NextPriority":33,
  "CommunityMatchMode":"Include",
  "MatchAsns":"65501",
  "SourceRegionIds":"cn-qingdao-env66-d01"
 }
}
```

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>24CE1987-D1D1-5324-9BAD-2750B60E6ABB</RequestId> <PageNumber>1</PageNumber> <RouteMaps> <MatchAddressType>IPv4</MatchAddressType> <Description>desctest</Description> <SourceInstanceIdsReverseMatch>false</SourceInstanceIdsReverseMatch> <TransmitDirection>RegionOut</TransmitDirection> <MatchCommunitySet>65501:1</MatchCommunitySet> <CenRegionId>cn-qingdao-env66-d01</CenRegionId> <SourceRouteTableIds>vtb-adfr233vf34rvd4****</SourceRouteTableIds> <DestinationInstanceIds>vpc-afrfs434465fdf****</DestinationInstanceIds> <SourceInstanceIds>vpc-adeg3544fdf34vf****</SourceInstanceIds> <DestinationInstanceIdsReverseMatch>false</DestinationInstanceIdsReverseMatch> <DestinationRouteTableIds>vtb-adefrgtr144vf****</DestinationRouteTableIds> <DestinationCidrBlocks>10.10.10.0/24</DestinationCidrBlocks> <RouteMapId>cenrmap-y40mxdvf7joc12****</RouteMapId> <OperateCommunitySet>65501:1</OperateCommunitySet> <DestinationChildInstanceTypes>VPC</DestinationChildInstanceTypes> <Status>Active</Status> <Priority>5000</Priority> <SourceChildInstanceTypes>VPC</SourceChildInstanceTypes> <AsPathMatchMode>Include</AsPathMatchMode> <MapResult>Deny</MapResult> <CidrMatchMode>Include</CidrMatchMode> <RouteTypes>System</RouteTypes> <TransitRouterRouteTableId>vtb-gw8nx3515m1mbd1z1****</TransitRouterRouteTableId> <Preference>20</Preference> <CommunityOperateMode>Additive</CommunityOperateMode> <CenId>cen-wx12mmlt17ld82****</CenId> <PrependAsPath>65501</PrependAsPath> <NextPriority>33</NextPriority> <CommunityMatchMode>Include</CommunityMatchMode> <MatchAsns>65501</MatchAsns> <SourceRegionIds>cn-qingdao-env66-d01</SourceRegionIds> </RouteMaps> |  |

#### 1.15.4. DeleteCenRouteMap

删除路由策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DeleteCenRouteMap | 系统规定参数。取值：DeleteCenRouteMap。 |
| CenId | String | Query | 是 | cen-7qthudw0ll6jm**** | 云企业网实例ID。 |
| CenRegionId | String | Query | 是 | cn-qingdao-env17e-d01 | 路由策略应用的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| RouteMapId | String | Query | 是 | cenrmap-abcdedfghij**** | 路由策略ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5903EE99-D542-4E14-BC65- AAC1CB2D3D03 | 请求ID。 |

**示例**

请求示例

```
&CenId=cen-7qthudw0ll6jm**** &CenRegionId=cn-qingdao-env17e-d01 &RouteMapId=cenrmap-abcdedfghij****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"5903EE99-D542-4E14-BC65-AAC1CB2D3D03" } |  |

| XML | 格式 |
|---|---|
| <RequestId>5903EE99-D542-4E14-BC65-AAC1CB2D3D03</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVALIDOPERATIONROUTEMAP _ _ _ STATUS _ | IncorrectStatus.RouteMap | Operation Failed. The specified route map is configuring, please try again later. |
| 400 | INVALIDOPERATIONTRANSITRO _ _ UTERNOTEXIST _ _ | InvalidOperation.TransitRouterNotExist | Operation is invalid because the transit router not exist. |

### 健康检查

#### 1.16.1. EnableCenVbrHealthCheck

开启边界路由器（VBR）的健康检查功能，确保及时发现出现故障的物理专线，也可修改VBR的健康检查配置。

**使用说明**

您可以通过为VBR实例设置健康检查，监测本地数据中心与阿里云之间物理专线的连接状况，以便及时发现问题。 在使用健康检查功能前，请先了解以下信息： 如果您的边界路由器实例使用的是静态路由，那么在您设置完健康检查后，您需要在边界路由器实例连接的本地数据中心中添加一条静态路由条目。静态路由的目标网段为健康检查的源IP地址，网段掩码为32位，下一跳为边界路由器实例的阿里云侧IP地址。 如果您的边界路由器实例使用的是BGP动态路由协议，则无需在本地数据中心添加路由条目。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | EnableCenVbrHealthCheck | 系统规定参数。取值：EnableCenVbrHealthCheck 。 |
| CenId | String | Query | 是 | cen-hahhfskfkseig**** | 云企业网实例ID。 |
| VbrInstanceRegionI d | String | Query | 是 | cn-qingdao-env17e-d01 | VBR实例所在的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| VbrInstanceId | String | Query | 是 | vbr-wz95o9aylj181n5mzk**** | VBR实例ID。 |
| HealthCheckSource Ip | String | Query | 否 | 192.XX.XX.1 | 指定健康检查源IP地址。支持以下两种配置方式： 自动生成源IP （推荐）：系统将自动分配 100.96.0.0/16网段内的IP地址。 自定义源IP ：源IP地址可以是10.0.0.0/8、 192.168.0.0/16、172.16.0.0/12三个网段内任意一个没有被使用的IP地址。但不能与云企业网中要互通的地址冲突，也不能与VBR实例的阿里云侧、客户侧IP地址冲突。 |
| HealthCheckTarget Ip | String | Query | 是 | 10.XX.XX.1 | 指定健康检查的目标IP地址。 目标IP地址为VBR实例客户侧IP地址。 |
| VbrInstanceOwnerI d | Long | Query | 否 | 1250123456123456 | VBR实例所属一级组织UID。 如果VBR实例和云企业网实例不属于同一个组织，本参数必填。 |
| HealthCheckInterv al | Integer | Query | 否 | 2 | 指定健康检查发送连续探测报文的时间间隔。单位：秒。 默认值：2 。取值范围：2~3 。 |
| HealthyThreshold | Integer | Query | 否 | 8 | 指定健康检查发送探测报文的个数。单位：个。 取值范围：3~8 。默认值：8 。 |
| HealthCheckOnly | Boolean | Query | 否 | false | 是否只开启健康检查的检测功能。取值： true ：是。 若只开启健康检查的检测功能，健康检查检测到链路不通时不会触发路由切换。 请确保您有其他方式保证链路的冗余性， 否则开启本功能后，可能会导致链路中断。 false （默认值）：否。 系统默认关闭本功能。健康检查检测到链路不通时，如果云企业网实例中存在冗余的路由，则健康检查会立刻触发路由切换使用可用链路。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1F59F19C-EFD2-40B1-94D5- 65B40CA8E34A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EnableCenVbrHealthCheck &CenId=cen-hahhfskfkseig**** &VbrInstanceRegionId=cn-qingdao-env17e-d01 &VbrInstanceId=vbr-wz95o9aylj181n5mzk**** &HealthCheckTargetIp=10.XX.XX.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1F59F19C-EFD2-40B1-94D5-65B40CA8E34A"
}
```

| XML | 格式 |
|---|---|
| <RequestId>1F59F19C-EFD2-40B1-94D5-65B40CA8E34A</RequestId> |  |

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | VBRCANNOTMODIFYHCCHEC _ _ _ _ _ K | InvalidStatus.HealthCheck | Can't modify，please delete health check config first. |
| 400 | ROUTECONFLICT _ | RouteConflict | The specified route already exists. |
| 400 | PARAMETERILLEGALSOURCEIP _ _ _ ORTARGETIP _ | Illegal.SourceIpOrTargetIp | The specified source IP address or destination IP address is invalid. |
| 400 | INVALIDOPERATIONVBRORVP _ _ _ _ CCBNATTACHMENTSTATUS _ _ _ | OperationFailed.StatusNotSupport | The VBR or VPC instance to CBN attachment is not in a valid state for the operation. |

#### 1.16.2. DisableCenVbrHealthCheck

关闭指定边界路由器的健康检查功能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DisableCenVbrHealthCheck | 系统规定参数。取值：DisableCenVbrHealthCheck。 |
| CenId | String | Query | 是 | cen-sjfoejfghhjgghjghkg**** | 云企业网实例ID。 |
| VbrInstanceRegionI d | String | Query | 是 | cn-qingdao-env17e-d01 | VBR实例所在的地域ID。 您可以通过调用DescribeChildInstanceRegions 接口获取地域ID。 |
| VbrInstanceId | String | Query | 是 | vbr-wz95o9aylj181n5**** | VBR实例ID。 |
| VbrInstanceOwnerId | Long | Query | 否 | 1250123456123456 | VBR实例所属的一级组织UID。 如果VBR实例和云企业网实例不属于同一个组织，本参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | A278B8A6-A5B8-4FDE-9F70- 95F0F6A1D68A | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DisableCenVbrHealthCheck &CenId=cen-sjfoejfghhjgghjghkg**** &VbrInstanceRegionId=cn-qingdao-env17e-d01 &VbrInstanceId=vbr-wz95o9aylj181n5****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"A278B8A6-A5B8-4FDE-9F70-95F0F6A1D68A" } |  |

| XML | 格式 |
|---|---|
| <RequestId>A278B8A6-A5B8-4FDE-9F70-95F0F6A1D68A</RequestId> |  |

#### 1.16.3. DescribeCenVbrHealthCheck

查询指定地域内边界路由器的健康检查配置信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | Query | 否 | DescribeCenVbrHealthCheck | 系统规定参数。取值：DescribeCenVbrHealthCheck 。 |
| CenId | String | Query | 否 | cen-6hpdgj7ni6pz1k**** | 云企业网实例ID。 |
| VbrInstanceRegionI d | String | Query | 是 | cn-qingdao-env66-d01 | VBR实例所在的地域ID。 您可以通过调用 DescribeChildInstanceRegions接口获取地域 ID。 |
| VbrInstanceId | String | Query | 否 | vbr-bp1kznorjeembsuhl**** | VBR实例ID。 |
| VbrInstanceOwnerI d | Long | Query | 否 | 253460731706911258 | VBR实例所属的一级组织UID。 如果VBR实例和云企业网实例不属于同一个组织，本参数必填。 |
| PageNumber | Integer | Query | 否 | 1 | 查询页码。默认值：1 。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页显示的条目数。取值范围：1 ~50 。默认值：10 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| VbrHealthChecks | Array |  | VBR实例的健康检查配置信息。 |
| -HealthCheckTargetIp | String | 192.XX.XX.1 | 健康检查的目标IP地址。 |
| -VbrInstanceId | String | vbr-bp1kznorjeembsuhl**** | VBR实例ID。 |
| -VbrInstanceRegionId | String | cn-qingdao-env66-d01 | VBR实例所在的地域ID。 |
| -CenId | String | cen-6hpdgj7ni6pz1k**** | 云企业网实例ID。 |
| -HealthyThreshold | Integer | 8 | 健康检查发送探测报文的个数。 |
| -HealthCheckInterval | Integer | 2 | 健康检查发送连续探测报文的时间间隔。单位：秒。 |
| -HealthCheckSourceIp | String | 172.XX.XX.1 | 健康检查的源IP地址。 |
| -HealthCheckOnly | Boolean | false | 是否只开启了健康检查的检测功能。 true ：是。 若只开启健康检查的检测功能，健康检查检测到链路不通时不会触发路由切换。 false ：否。 若未开启本功能，健康检查检测到链路不通时，如果云企业网实例中存在冗余的路由，健康检查会立刻触发路由切换使用可用链路。 |
| PageSize | Integer | 10 | 分页查询时每页显示的条目数。 |
| RequestId | String | B8C9702E-304A-4E18-AC89- BE2D91C2C176 | 请求ID。 |
| PageNumber | Integer | 1 | 查询页码。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalCount | Integer | 1 | 总条目数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCenVbrHealthCheck &VbrInstanceRegionId=cn-qingdao-env66-d01
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "TotalCount":1, "PageSize":10, "RequestId":"B8C9702E-304A-4E18-AC89-BE2D91C2C176", "PageNumber":1, "VbrHealthChecks":{ "VbrInstanceRegionId":"cn-qingdao-env66-d01", "HealthCheckInterval":2, "VbrInstanceId":"vbr-bp1kznorjeembsuhl****", "HealthyThreshold":8, "HealthCheckSourceIp":"172.XX.XX.1", "CenId":"cen-6hpdgj7ni6pz1k****", "HealthCheckTargetIp":"192.XX.XX.1", "HealthCheckOnly":false } } |  |

| XML | 格式 |
|---|---|
| <TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>B8C9702E-304A-4E18-AC89-BE2D91C2C176</RequestId> <PageNumber>1</PageNumber> <VbrHealthChecks> <VbrInstanceRegionId>cn-qingdao-env66-d01</VbrInstanceRegionId> <HealthCheckInterval>2</HealthCheckInterval> <VbrInstanceId>vbr-bp1kznorjeembsuhl****</VbrInstanceId> <HealthyThreshold>8</HealthyThreshold> <HealthCheckSourceIp>172.XX.XX.1</HealthCheckSourceIp> <CenId>cen-6hpdgj7ni6pz1k****</CenId> <PacketLoss /> <HealthCheckTargetIp>192.XX.XX.1</HealthCheckTargetIp> <HealthCheckOnly>false</HealthCheckOnly> </VbrHealthChecks> |  |
