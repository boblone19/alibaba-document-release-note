---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Express Connect Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 28
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Express Connect Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Express%20Connect%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Express Connect Developer Guide 20220928

## Table of Contents

- 1 API Reference
  - 1.1 API overview
  - 1.2 Invoke APIs
    - 1.2.1 Request structure
    - 1.2.2 Authorization
    - 1.2.3 Signature
  - 1.3 RAM authentication
  - 1.4 Common parameters
  - 1.5 Connect two VPCs
    - 1.5.1 CreateRouterInterface
    - 1.5.2 ConnectRouterInterface
- 2 Make SDK calls by using ASAPI
  - 2.1 Overview
  - 2.2 Log on to the API Tool console
  - 2.3 View the information about API operations
  - 2.4 Obtain the endpoint of ASAPI
  - 2.5 Obtain the SDK package for Asapi
  - 2.6 Obtain an AccessKey pair
  - 2.7 Query the region ID
  - 2.8 SDK for Java
  - 2.9 SDK for Node.js
  - 2.10 Use POP SDK to call ASAPI (optional)

## 1 API Reference

### 1.1 API overview

The following tables list API operations available for use in Express Connect.

| Operation | Description |
|---|---|
| CreateRouterInterface | Creates a router interface. |
| ConnectRouterInterface | Initiates a connection from the initiator router interface to the acceptor router interface. |

### 1.2 Invoke APIs

#### 1.2.1 Request structure

To send an Express Connect API request, you must send an HTTP GET request to the Express Connect endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8. Express Connect API operations use the RPC protocol. You can call Express Connect API operations by sending HTTP GET requests. The following example shows the request syntax:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the Express Connect API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Stack Operations (ASO) console. For more information, see Obtain the endpoint of ASAPI. Action: the name of the operation being performed. To create a router interface, you must set the Action parameter to CreateRouterInterface. Version: the version of the API that you need to use. The current VPC API version is 2016-04-28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters are used for all Express Connect API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the CreateRouterInterface operation in Express Connect. The following code has been formatted to ease reading.

```
https://vpc.example.com/?Action=CreateRouterInterface &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 1.2.2 Authorization

To ensure the security of your account, we recommend that you call Express Connect API operations as a RAM user. To do so, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the Express Connect resources and API operations that allow the authorization, see RAM authentication.

#### 1.2.3 Signature

You must sign all API requests to ensure security. Request signatures are used to verify the identities of API callers. Express Connect implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, whereas the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to the Express Connect API request in the following format: https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take CreateRouterInterface as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the original request URL is shown in the following content:

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

To calculate the signature, perform the following operations:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC- SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeS tamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter.

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 1.3 RAM authentication

Before you call an Express Connect operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource. Resource types that can be authorized The following table lists the Express Connect resources that allow authorized access and their ARNs.

| Resource type | ARN |
|---|---|
| VPCs | acs:vpc:$regionid:$accountid:vpc/$vpcid |
|   | acs:vpc:$regionid:$accountid:vpc/* |
|   | acs:vpc:*:$accountid:vpc/* |
| VRouters | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
|   | acs:vpc:$regionid:$accountid:vrouter/* |
|   | acs:vpc:*:$accountid:vrouter/* |
| VSwitches | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
|   | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:*:$accountid:vswitch/* |

| eveloper Guide·API Refe |   |
|---|---|
|   | rence Express Connec |
| Resource type | ARN |
| Route tables | acs:vpc:$regionid:$accountid:routetable/$routetableid |
|   | acs:vpc:$regionid:$accountid:routetable/* |
|   | acs:vpc:*:$accountid:routetable/* |
| Elastic IP addresses (EIPs) | acs:vpc:$regionid:$accountid:eip/$allocationid |
|   | acs:vpc:$regionid:$accountid:eip/* |
|   | acs:vpc:*:$accountid:eip/* |
| NAT gateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|   | acs:vpc:$regionid:$accountid:natgateway/* |
|   | acs:vpc*:$accountid:vpc/* |
| NAT bandwidth packages | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
|   | aacs:vpc:*:$accountid:vpc/* |
| Forwarding tables | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
|   | acs:vpc:$regionid:$accountid:forwardtable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| SNAT tables | acs:vpc:$regionid:$accountid:snattable/$snattableid |
|   | acs:vpc:$regionid:$accountid:snattable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| General resources | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accountid`/`vrouterid indicates the ID of the specified resource, and `*` indicates all resources. API operations that allow authorized access The following table lists the Express Connect API operations that allow authorized access and their ARNs.

| Operation | ARN |
|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |

| xpress Connect | Developer Guide·API Referenc |   | e |
|---|---|---|---|
| Operation | ARN |   |   |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |   |   |
| vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |   |   |
| vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |   |   |
| vpc:DescribeVRouters | acs:vpc:$regionid:$accountid:vrouter/* |   |   |
|   | The VRouter ID is specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |   |   |
|   | The VRouter ID is not specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/*" |   |   |
| vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |   |   |
| vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |   |   |
|   | acs:vpc:$regionid:$accountid:vpc/$vpcid |   |   |
| vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |   |   |
| vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |   |   |
|   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |   |   |
| vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |   |   |
| vpc:CreateRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |   |
| vpc:DeleteRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |   |   |
| vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |   |   |
|   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vr outerid" |   |   |
|   |   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vr |   |
|   | outerid" |   |   |
| vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |   |   |
|   | Associates an EIP with an ECS instance. acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |   |   |

| Operation | ARN |   |   |
|---|---|---|---|
| vpc:UnassociateEipAddress | Disassociates an EIP from an ECS instance. acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |   |   |
| vpc:DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
| vpc:DescribeNatGateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
| vpc:ModifyNatGatewaySpec | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
| vpc:ModifyNatGatewayAttribute | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:DeleteNatGateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:DescribeBandwidthPackages | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:ModifyBandwidthPackageSpec | thpackageid |   |   |
| vpc:ModifyBandwidthPackageAttribu | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| te | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:AddBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:RemoveBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:DeleteBandwidthPackage | thpackageid |   |   |

| Operation | ARN |   |   |
|---|---|---|---|
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:CreateForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:DeleteForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:ModifyForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| vpc:DescribeForwardTableEntries | eid |   |   |
| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |   |   |
| vpc:ModifySnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| vpc:DescribeSnatTableEntries | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| vpc:DeleteSnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |

### 1.4 Common parameters

This topic describes the common parameters that are required for calling Express Connect API operations. Common request parameters Common request parameters must be included in all Express Connect API requests. Common request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: XML. |
| Version | String | Yes | The version number of the API. Format: YYYY-MM-DD . Set the value to 2016-04-28 |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1 |

|   | Developer Guide·AP | I Referen | ce | Express Connec | t |
|---|---|---|---|---|---|

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2013-01-10T12:00:00Z. |
| SignatureVersio n | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0 |
| SignatureNonce | String | Yes | A unique and random number used to prevent replay attacks. You must use different numbers for different requests. |

Examples

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Common response parameters API responses use the HTTP response format where a 2xx status code indicates a successful call and a 4xx or 5xx status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. Every response returns a unique RequestId regardless of whether the call is successful. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
      <!—Result Root Node-->
      <Interface Name+Response>
      <!—Return Request Tag-->
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
      <!—Return Result Data-->
      </Interface Name+Response>
```

JSON format `{`

```json
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
      /*Return Result Data*/
```

`}`

### 1.5 Connect two VPCs

#### 1.5.1 CreateRouterInterface

Creates a router interface. Description When you call this operation, make sure that the following requirements are met: You can create only one pair of interconnected router interfaces between two routers. You can create a maximum of five router interfaces for a router. If your account contains any router interface that has overdue payments, you cannot create new router interfaces. The destination CIDR block of routes in the same route table cannot be the same. You can only use a VBR for the side that initiates connections. In addition, the VBR must be activated. Not e Router interfaces created by calling the operation are billed on a daily basis. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouterInter face | The operation that you want to perform. Set the value to Creat eRout erInt erf ace. |
| OppositeRegionId | String | Yes | cn-shanghai | The region ID of the connection acceptor. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. |
| Role | String | Yes | InitiatingSide | The role of the router interface. Valid values: Init iat ingSide: connection initiator. Accept ingSide: connection acceptor. |
| RouterId | String | Yes | vrt-12345 | The ID of the router associated with the router interface. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouterType | String | Yes | VRouter | The type of the router associated with the router interface. Valid values: VRout er VBR |
| Spec | String | Yes | Large | The specification of the router interface. The following content lists available specifications and their bandwidth values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s Not e When Role is set to Accept ingSide (connection acceptor), the value of Spec is set to Negat ive. |
| OppositeInterfac eId | String | No | ri- 2zeo3xzyf38r4ur zd**** | The ID of the destination router interface. |
| OppositeRouterId | String | No | vrt- bp1lhl0taikrteen8 **** | The ID of the destination router. |
| OppositeRouterT ype | String | No | VRouter | The type of the router associated with the destination router interface. Valid values: VRout er VBR |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OppositeInterfac eOwnerId | String | No | fffsf | The ID of the account to which the destination router interface belongs. |
| HealthCheckSourc eIp | String | No | 116.62.222.XX | The source IP address that is used to perform health checks. It must be an unoccupied IP address of the source VPC. Not e You can specify this parameter when physical connections are used. |
| HealthCheckTarg etIp | String | No | 116.62.222.XX | The destination IP address that is used to perform health checks. Not e This parameter is required when the Healt hCheckSourceIp parameter is specified. |
| AccessPointId | String | No | ap-cn- shanghaiSZ-**** | The ID of the access point to which the VBR belongs. Not e You must specify this parameter when physical connections are used. |
| OppositeAccessP ointId | String | No | ap-cn- shanghaiSZ-**** | The ID of the access point of the destination router interface. Not e This parameter must be specified when the destination router interface is associated with a VBR. The specified value cannot be changed after the router interface is created. |
| Description | String | No | Router interface description | The description of the router interface. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https://. |

| http:// or | https://. |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | Router interface name | The name of the router interface. The name must be 2 to 128 characters in length. It can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter and cannot start with http:// or https:// . |
| Period | Integer | No | 3 | The length of the subscription. When the PricingCycle parameter is set to Month, valid values: 1-9. When the PricingCycle parameter is set to Year, valid values: 1-3. Not e T his paramet er is required when Inst anceChargeT ype is set to PrePaid. |
| InstanceChargeTy pe | String | No | PrePaid | The billing method of the router interface. |
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: f alse: Automatic payment is disabled. After an order is generated, you must go to the Order Center to make the payment. t rue: Automatic payment is enabled. Payments are automatically made. Not e T his paramet er is required when Inst anceChargeT ype is set to PrePaid. |

|   | http:// |
|---|---|
| https:// |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PricingCycle | String | No | Month | The billing cycle of the subscription. Valid values: Mont h (default): The instance is billed on a monthly basis. Year: The instance is billed on a yearly basis. Not e T his paramet er is required when Inst anceChargeT ype is set to PrePaid. |
| ClientToken | String | No | sjffha123334 | The client token that is used to ensure the idempotence of the request. The value of this parameter is generated by a client. The value must be unique among different requests and must be 1 to 64 ASCII characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1- 43E6-AC03- ADD96B6E4907 | The ID of the request. |
| RouterInterface Id | String | ri-2ze7fbuohm**** | The ID of the router interface. |
| OrderId | Long | 202008594930117 | The order number. This parameter is returned when InstanceChargeType is set to PrePaid. |

Examples Sample requests

```
http(s)://vpc.aliyuncs.com/? Action=CreateRouterInterface &OppositeRegionId=cn-shanghai &RegionId=cn-hangzhou &Role=InitiatingSide &RouterId=cn-hangzhou &RouterType=VRouter &Spec=Large &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouterInterfaceResponse>
      <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
      <RouterInterfaceId>ri-2ze7fbuohm****</RouterInterfaceId>
</CreateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB",
    "RouterInterfaceId": "ri-2ze7fbuohm****"
```

`}`

#### 1.5.2 ConnectRouterInterface

Initiates a connection from the initiator router interface to the acceptor router interface. After you call this operation, the router interface enters the Connecting state. When the connection is established, it enters the Active state. When you call this operation, make sure that the following requirements are met: Only an initiator router interface in the Idle state can initiate a connection. You can create only one pair of interconnected router interfaces between two routers. You cannot initiate a connection if your account contains a router interface with overdue payments. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConnectRouterInt erface | The operation that you want to perform. Set the value to Connect Rout erInt erf ace. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4ur zd**** | The ID of the initiator router interface. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DE77A7F3-3B74- 41C0-A5BC- CAFD188C28B6 | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.aliyuncs.com/? Action=ConnectRouterInterface &RegionId= cn-hangzhou &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ConnectRouterInterfaceResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ConnectRouterInterfaceResponse>
```

`JSON` format `{`

```json
 "RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}`

## 2 Make SDK calls by using ASAPI

### 2.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize operations and audit and manage their calls. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, avoiding inconsistent operations caused by different call methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a unified manner and customize development. ASAPI supports access of most cloud services deployed in Apsara Stack and passthrough or encapsulation of different backend APIs. This way, operations can be called with the same method. ASAPI allows you to use SDKs and API Portal to call APIs registered in ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

### 2.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 2.3 View the information about API operations

operations You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon.
4. View and remember the service name, API operation name, and API version.

### 2.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
3. Click Log On to go to the ASO console.
4. In the left-side navigation pane, choose Product s > Product List . On the Product List page, click
Apsara Inf rast ruct ure Management Framework.
5. In the left-side navigation pane of the Apsara Infrastructure Management Framework console, click
Report s.
6. On the All Report s page, search for Regist rat ion Vars of Services. Click Regist rat ion Vars of
Services.
7. On the Regist rat ion Vars of Services page, click the
icon next to Service. In the dialog box that appears, search for asapi.
8. Right-click the Service Regist rat ion column corresponding to asapi and select Show More.
9. In the Det ails dialog box, view the value of asapi.gat eway.endpoint . The value is the logon URL
of the Apsara ASAPI Management platform.

### 2.5 Obtain the SDK package for Asapi

Apsara Stack uses Asapi as the unified portal for all Apsara Stack products that are connected to Asapi. Asapi also provides SDKs to call product APIs. To obtain the SDK package for Asapi, see Apsara Stack documentation.

### 2.6 Obtain an AccessKey pair

An AccessKey pair is composed of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the AccessKey message, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

### 2.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

### 2.8 SDK for Java

This topic describes how to obtain and use SDK for Java. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Express Connect SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of ASAPI. Express Connect SDK for Java supports JDK 1.6 and later. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use SDK for Java You can call API operations on ASAPI by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests

```
// Obtain the endpoint of ASAPI. String endpoint = "http://xxx/asapi/v3"; // Set request parameters. Map<String, String> parameters = new HashMap<String, String>(); // Set parameters for the product. parameters.put("Product", "vpc"); // The product name must be the same as the name displayed in the corresponding API directory. parameters.put("Action", "CreateRouterInterface"); // The API name must be in th e same case as that in the API directory. parameters.put("Version", "2016-04-28"); // The API version. // Set authorization-related parameters. parameters.put("AccessKeyId", "<your-access-key-id>"); // The AccessKey ID of th e authorized account. parameters.put("AccessKeySecret", "<your-access-key-secret>"); // The AccessKey secret o f the authorized account. // Set business parameters. parameters.put("username", "<your-username>"); // The username used to l og on to the ASCM console. parameters.put("password", "<your-password>"); // The password used to l og on to the ASCM console. JSONObject jsonObject = new JSONObject(); jsonObject.put("RegionId", "cn-hangzhou-env12-d01"); parameters.put("json", jsonObject.toJSONString()); // Create an ASClient instance for initiating requests. ASClient client = new ASClient(); // Add request headers. client.addHeader("x-acs-resourceGroupId", "112233"); // Initiate the request and obtain the response. String result = client.doPost(endpoint, parameters);
```

### 2.9 SDK for Node.js

This topic describes how to obtain and use SDK for Node.js. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Express Connect SDK for Node.js. For more information about how to obtain the AccessKey pair, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of ASAPI. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install the SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, you must configure mocha.opts.

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows how to use SDK for Node.js:
1. Create a client instance. To create a client instance, you must set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. You can view the following example:

```
local: {
    regionId: 'obtained region ID',
    API_GATEWAY: 'obtained endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and configure parameters.
3. Initiate the API request and handle the response or exception.

```
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'CreateRouterInterface',
    Product: 'vpc',
    regionId: 'cn-hangzhou-env12-d01',
    accessKeyId: 'xxxxxxx',
    accessKeySecret: 'xxxxxxx',
    Version: '2016-04-28'
```

};

```
// Set parameters in the request header. asapiClient.addHeader("x-acs-regionId", "cn-hangzhou-env12-d01"); // Initiate the request and obtain the response. const result = await asapiClient.doRequest(API_GATEWAY, params, {});
```

### 2.10 Use POP SDK to call ASAPI (optional)

(optional) If an application used the POP SDK to call cloud services, you must switch the gateway to ASAPI. Procedure
1. Switch the gateway to ASAPI and add common parameters to the request header.
2. Add the Product Name field to the request header.
Code samples The following code uses the Express Connect openapi as an example.

```java
 try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessK
eySecret);
    // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "vpc", "<ASAPI gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
        CreateRouterInterfaceRequest request = new CreateRouterInterfaceRequest();
        request.setSysRegionId(regionId);
    // request.setRegionId(regionId);
    // Set common parameters based on the information about the current user.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    CreateRouterInterfaceResponse result = (CreateRouterInterfaceResponse) acsClient.getAcs
Response(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```

`}`
