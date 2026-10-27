---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 NAT Gateway Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 86
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 NAT Gateway Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20NAT%20Gateway%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 NAT Gateway Developer Guide 20220928

## Table of Contents

- 1 API reference
  - 1.1 List of operations by function
  - 1.2 Make API requests
    - 1.2.1 Request structure
    - 1.2.2 API authorization
    - 1.2.3 Request signature
  - 1.3 RAM authentication
  - 1.4 Common parameters
  - 1.5 NAT gateways
    - 1.5.1 CreateNatGateway
    - 1.5.2 DeleteNatGateway
    - 1.5.3 ModifyNatGatewaySpec
    - 1.5.4 ModifyNatGatewayAttribute
    - 1.5.5 DescribeNatGateways
  - 1.6 DNAT tables
    - 1.6.1 CreateForwardEntry
    - 1.6.2 DeleteForwardEntry
    - 1.6.3 ModifyForwardEntry
    - 1.6.4 DescribeForwardTableEntries
  - 1.7 SNAT tables
    - 1.7.1 CreateSnatEntry
    - 1.7.2 DeleteSnatEntry
    - 1.7.3 ModifySnatEntry
    - 1.7.4 DescribeSnatTableEntries
  - 1.8 NAT bandwidth packages
    - 1.8.1 CreateBandwidthPackage
    - 1.8.2 ModifyBandwidthPackageSpec
    - 1.8.3 DescribeBandwidthPackages
    - 1.8.4 ModifyBandwidthPackageAttribute
    - 1.8.5 DeleteBandwidthPackage
    - 1.8.6 AddBandwidthPackageIps
    - 1.8.7 RemoveBandwidthPackageIps
- 2 Make SDK calls by using ASAPI
  - 2.1 Overview
  - 2.2 Log on to the API Tool console
  - 2.3 View the information about API operations
  - 2.4 Obtain the endpoint of ASAPI
  - 2.5 Obtain the core package for ASAPI
  - 2.6 Obtain an AccessKey pair
  - 2.7 Query the region ID
  - 2.8 SDK for Java
  - 2.9 SDK for Node.js
  - 2.10 Use POP SDK to call ASAPI (optional)

## 1 API reference

### 1.1 List of operations by function

The following table lists API operations available for use in NAT Gateway.

| API | Description |
|---|---|
| CreateNatGateway | Creates a network address translation (NAT) gateway. |
| ModifyNatGatewayAttribute | Modifies the name and description of a NAT gateway. |
| ModifyNatGatewaySpec | Resizes a NAT gateway. |
| DeleteNatGateway | Deletes a specified NAT gateway. |
| DescribeNatGateways | Queries NAT gateways. |
| CreateForwardEntry | Adds DNAT entries to a DNAT table. |
| DeleteForwardEntry | Deletes a specified DNAT entry. |
| ModifyForwardEntry | Modifies a specified DNAT entry. |
| DescribeForwardTableEntries | Queries DNAT entries in a specified DNAT table. |
| CreateSnatEntry | Adds SNAT entries to an SNAT table. |
| DeleteSnatEntry | Deletes a specified SNAT entry. |
| ModifySnatEntry | Modifies a specified SNAT entry. |
| DescribeSnatTableEntries | Queries SNAT entries in a specified SNAT table. |
| CreateBandwidthPackage | Creates a NAT service plan. |
| ModifyBandwidthPackageSpec | Modifies the bandwidth of a NAT service plan. |
| DescribeBandwidthPackages | Queries NAT service plans in a specified region. |
| ModifyBandwidthPackageAttribute | Modifies the name and description of a specified NAT service plan. |
| DeleteBandwidthPackage | Deletes a specified NAT service plan. |
| AddBandwidthPackageIps | Adds public IP addresses to a NAT service plan. |
| RemoveBandwidthPackageIps | Removes a public IP address from a NAT service plan. |

### 1.2 Make API requests

#### 1.2.1 Request structure

To send a NAT Gateway API request, you must send an HTTP GET request to the NAT Gateway endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. The request and response are encoded in UTF-8. NAT Gateway API operations use the RPC protocol. You can call NAT Gateway API operations by sending HTTP GET requests. When you send an HTTP GET request, use the following syntax:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the NAT Gateway API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Stack Operations (ASO) console. For more information, see Obtain the endpoint of Asapi. Action: the name of the operation being performed. For example, to query NAT gateways in a specified region, you must set the Action parameter to DescribeNatGateways. Version: the version of the API that you want to use. The current NAT Gateway API version is 2016-04 -28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters are used for all NAT Gateway API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the DescribeNatGateways operation in NAT Gateway: Not e The following code has been formatted for ease of reading.

```
https://vpc.example.com/?Action=DescribeNatGateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 1.2.2 API authorization

To ensure the security of your account, we recommend that you call NAT Gateway API operations as a RAM user. To call NAT Gateway API operations as a RAM user, you must create and attach authorization policies to the RAM user. For more information about the NAT Gateway resources and API operations that allow the authorization, see RAM authentication.

#### 1.2.3 Request signature

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. NAT Gateway implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to the NAT Gateway API request in the following format: https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeNatGateways as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the following code shows the original request URL:

```
http://vpc.example.com/?Action=DescribeNatGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Compose and encode a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeNatGateways&Format%3DXML&SignatureMethod% 3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1. 0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter.

```
http://vpc.example.com/?Action=DescribeNatGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 1.3 RAM authentication

Before you call a NAT Gateway operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource. NAT Gateway resources that allow authorized access The following table lists the NAT Gateway resources that allow authorized access and their ARNs.

| Resource type | ARN |
|---|---|
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

$regionid`/`accoutid`/`vrouterid are IDs of the specific resources, `*` represents all resources. NAT Gateway API operations that allow authorized access The following table lists the NAT Gateway API operations that allow authorized access and their ARNs.

| Operation | ARN |   |   |
|---|---|---|---|
| CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
| DescribeNatGateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:vpc:$regionid:$accountid:natgateway/* |   |   |
| ModifyNatGatewaySpec | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
| ModifyNatGatewayAttribute | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| DeleteNatGateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| DescribeBandwidthPackages | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| ModifyBandwidthPackageSpec | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| ModifyBandwidthPackageAttribute | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| AddBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| RemoveBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| DeleteBandwidthPackage | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| CreateForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| DeleteForwardEntry | eid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| ModifyForwardEntry | eid |   |   |

| eveloper Guide·API reference | NAT Gatewa |
|---|---|

| Operation | ARN |   |   |
|---|---|---|---|
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl eid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtabl |   |
| DescribeForwardTableEntries | eid |   |   |
| CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |   |   |
| ModifySnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| DescribeSnatTableEntries | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| DeleteSnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |

### 1.4 Common parameters

This topic describes common parameters, including common request parameters and common response parameters. Common parameters are required in all API operations, regardless of the operation being called. Common request parameters Common request parameters must be included in all EIP API requests. Common request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: JSON. |
| Version | String | Yes | The version number of the API. Format: YYYY-MM-DD . Set the value to 2016-04-28 |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1 |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2013-01-10T12:00:00Z. |

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| SignatureVersio n | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0 |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

Examples

```
http://vpc.example.com/?Action=DescribeEipAddresses &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Common response parameters API responses use the HTTP response format where a 2XX status code indicates a successful call and a 4XX or 5XX status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. Every response returns a unique RequestId regardless of whether the call is successful. XML format

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

### 1.5 NAT gateways

#### 1.5.1 CreateNatGateway

Creates a NAT gateway. Usage notes When you call this operation, take note of the following limits: You cannot deploy a NAT gateway and a user-created SNAT gateway in the same virtual private cloud (VPC) if the SNAT gateway is an Elastic Compute Service (ECS) instance. After a NAT gateway is created, a route entry is automatically added to the route table of the VPC. The destination CIDR block of the route entry is 0.0.0.0/0 and the next hop of the route entry is the NAT gateway. The route entry ensures that traffic is routed to the NAT gateway. If the route table of the VPC already contains a route entry whose destination CIDR block is 0.0.0.0/0, delete the route entry. Otherwise, you cannot create a NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNatGatewa y | The operation that you want to perform. Set the value to Creat eNat Gat eway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1di7uewzmtvf uq8**** | The ID of the VPC. |
| Name | String | No | fortest | The name of the NAT gateway. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https://. Not e If you do not set this parameter, the ID of the NAT gateway is used by default. |
| Description | String | No | testnat | The description of the NAT gateway. The description must be 2 to 256 characters in length. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |
| Spec | String | No | Small | The size of the NAT gateway. Valid values: Small (default): small Middle: medium Large: large |
| BandwidthPackag e.N.IpCount | Integer | No | 5 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. N indicates the sequence number of the NAT service plan. Valid values: 1 to 4. |
| BandwidthPackag e.N.Bandwidth | Integer | No | 5 | The bandwidth limit of NAT service plan N. Valid values: 5 to 5000. Unit: Mbit/s. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BandwidthPackag e.N.Zone | String | No | cn-qingdao- env17- amtest11001-a | The zone of NAT service plan N. If you do not set this parameter, the service plan is randomly allocated to a zone. Even if the IP addresses of the NAT service plan and the backend ECS instances belong to different zones, the ECS instances can still connect to the NAT gateway. However, you can reduce the network latency by allocating the NAT service plan to the zone where your ECS instances are deployed. |
| BandwidthPackag e.N.ISP | String | No | BGP | The line type of the Internet service provider (ISP) for NAT service plan N. Set the value to BGP, which specifies BGP (multi-ISP). |
| BandwidthPackag e.N.InternetCharg eType | String | No | PayByBandwidth | The billing method of NAT service plan N. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h: pay-by- bandwidth |
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the NAT gateway. Valid values: PrePaid: subscription Post Paid (default): pay-as-you-go |
| PricingCycle | String | No | Month | The billing cycle of the subscription NAT gateway. Valid values: Mont h (default): billed on a monthly basis Year: billed on an annual basis This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Duration | String | No | 1 | The subscription duration of the NAT gateway. When PricingCycle is set to Mont h, set Period to a value from 1 to 9. When PricingCycle is set to Year, set Period to a value from 1 to 3. Not e This parameter is required when Inst anceChargeT ype is set to PrePaid. |
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: Valid values: f alse (default): disables automatic payment. If you select this option, you must go to the Order Center to complete the payment after an order is generated. t rue: enables automatic payment. Payments are automatically completed. Not e This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. |
| VSwitchId | String | No | vsw- n2yf2tj1k2bfey5p q**** | The ID of the vSwitch. |
| InternetChargeTy pe | String | No | PayByLcu | The metering method of the NAT gateway. Set the value to PayByLcu, which specifies the pay-by-CU metering method. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPack ageIds | List | bwp-11odxu2k7**** | The ID of the NAT service plan. |
| ForwardTableId s | List | ftb-11tc6xgmv**** | The ID of the DNAT table. |
| NatGatewayId | String | ngw-112za33e4**** | The ID of the NAT gateway. |
| RequestId | String | 2315DEB7-5E92- 423A-91F7- 4C1EC9AD97C3 | The ID of the request. |
| SnatTableIds | List | stb- SnatTableIds**** | The ID of the SNAT table. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateNatGateway &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-bp1di7uewzmtvfuq8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateNatGatewayResponse>
  <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
  <SnatTableIds>stb-SnatTableIds****</SnatTableIds>
  <ForwardTableIds>ftb-11tc6xgmv****</ForwardTableIds>
  <BandwidthPackageIds>bwp-11odxu2k7****</BandwidthPackageIds>
  <NatGatewayId>ngw-112za33e4****</NatGatewayId>
</CreateNatGatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3",
    "SnatTableIds": "stb-SnatTableIds****",
    "ForwardTableIds": "ftb-11tc6xgmv****",
    "BandwidthPackageIds": "bwp-11odxu2k7****",
    "NatGatewayId": "ngw-112za33e4****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidVPCStatus | vpc incorrect status. | The error message returned because the operation is not supported when the VPC is in the current state. Check whether the state of the VPC is valid. |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidNatGatewayN ame.MalFormed | NatGateway name is not valid. | The error message returned because the specified gateway name is invalid. |
| 400 | InvalidNatGatewayD escription.MalForme d | NatGateway description is not valid. | The error message returned because the specified description is invalid. |
| 400 | MissingParameter.Ba ndwidthPackage | only support one BandwidthPackage be created with NatGateway. | The error message returned because no EIP bandwidth plan is specified. |
| 404 | InvalidVpcId.NotFou nd | Specified value of VpcId is not found in our record. | The error message returned because the specified VPC does not exist. Check whether the specified VPC is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all required parameters before you call this operation. |
| 404 | InvalidZoneId.NotFo und | Specified value of ZoneId is not exists. | The error message returned because the specified zone does not exist. |
| 404 | InvalidZoneId.NotFo und | Can not find ZoneId for allocated ip. | The error message returned because the zone of the specified IP address is invalid. |
| 400 | QuotaExceeded.Ban dwidthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Request a quota increase on the Quota Management page. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |

| eveloper Guid | e·API reference |   | NAT Gatewa |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | ZONE NO AVAILABLE _ _ IP _ | The Zone have no available ip. | The error message returned because no IP address is available in the zone. |
| 400 | InvalidParameter.Ba ndwidthPackage.n.IS P.ValueNotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified ISP of the EIP bandwidth plan is invalid. |
| 400 | InvalidNatGatewayId .NotFound | The NatGatewayId not exist. | The error message returned because the specified NAT gateway ID does not exist. Check whether the value of the NatGatewayId parameter is valid. |
| 400 | VswitchStatusError | The VSwitch is creating . | The error message returned because the operation is not supported when the vSwitch is being created. |
| 400 | VpcStatusError | The Vpc is creating . | The error message returned because the operation is not supported when the VPC is being created. |
| 400 | InvalidParameter.Sp ec.ValueNotSupport ed | The specified Spec is not valid. | The error message returned because the specified gateway size is invalid. |
| 400 | Forbidden.CheckEntr yRuleQuota | Route entry quota rule check error. | The error message returned because an error occurred when the system was checking the quota of route entries. |

#### 1.5.2 DeleteNatGateway

Deletes a specified NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNatGatewa y | The operation that you want to perform. Set the value to Delet eNat Gat eway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5 770**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT gateway. Valid values: t rue: yes f alse(default): no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNatGateway &NatGatewayId=ngw-bp1uewa15k4iy5770**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNatGatewayResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</DeleteNatGatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the value of the NatGatewayId parameter is valid. |
| 400 | DependencyViolatio n.BandwidthPackage s | There are BandwidthPackages on specified NatGateway not deleted. | The error message returned because one or more NAT service plans are associated with the NAT gateway. Disassociate all NAT service plans from the NAT gateway and try again. |

#### 1.5.3 ModifyNatGatewaySpec

Modifies the size of a NAT gateway. Usage notes NAT gateways are available in different sizes. The size of a NAT gateway determines the SNAT performance, which includes the maximum number of connections and the number of new connections per second. However, the size of a NAT gateway does not affect the data throughput. The following table describes the correlations between different sizes of NAT gateways and SNAT performance metrics.

| Size | Maximum number of connections | Number of new connections per second |
|---|---|---|
| Small | 10,000 | 1,000 |
| Medium | 50,000 | 5,000 |
| Large | 200,000 | 10,000 |

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatew aySpec | The operation that you want to perform. Set the value to Modif yNat Gat ewaySpec. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5 770**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Spec | String | Yes | Small | The new size of the NAT gateway. Valid values: Small: small Middle: medium Large: large |
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: t rue: yes f alse (default): no |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DBD4E4A2-786E- 4BD2-8EB6- 107FFC2B5B7D | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNatGatewaySpec &NatGatewayId=ngw-bp1uewa15k4iy5770**** &RegionId=cn-qingdao-env17-d01 &Spec=Small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyNatGatewaySpecResponse>
  <RequestId>DBD4E4A2-786E-4BD2-8EB6-107FFC2B5B7D</RequestId>
</ModifyNatGatewaySpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "DBD4E4A2-786E-4BD2-8EB6-107FFC2B5B7D"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | NATGW MODIFY SPE _ _ C SAME _ | The specified Spec is same with now. | The error message returned because the specified gateway size is the same as the current one. |
| 400 | InvalidParameter.Sp ec.ValueNotSupport ed | The specified Spec is not valid. | The error message returned because the specified gateway size is invalid. |

#### 1.5.4 ModifyNatGatewayAttribute

Modifies the name and description of a NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatew ayAttribute | The operation that you want to perform. Set the value to Modif yNat Gat ewayAt t ribut e. |
| NatGatewayId | String | Yes | ngw- 2ze0dcn4mq31qx 2jc**** | The ID of the NAT gateway whose configuration you want to modify. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | nat123 | The new name of the NAT gateway. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. It must start with a letter but cannot start with http:// or https:// . Not e You cannot leave both Name and Descript ion empty. |
| Description | String | No | fortest | The new description of the NAT gateway. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

|   | http:// |
|---|---|
| https:// |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AB5F62CF-2B60- 4458-A756- 42C9DFE108D1 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNatGatewayAttribute &NatGatewayId=ngw-2ze0dcn4mq31qx2jc**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyNatGatewayAttributeResponse>
  <RequestId>AB5F62CF-2B60-4458-A756-42C9DFE108D1</RequestId>
</ModifyNatGatewayAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "AB5F62CF-2B60-4458-A756-42C9DFE108D1"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the value of the NatGatewayId parameter is valid. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |

#### 1.5.5 DescribeNatGateways

Queries NAT gateways in a region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNatGate ways | The operation that you want to perform. Set the value to DescribeNat Gat eways. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway that you want to query. You can call the DescribeRegions operation to query the most recent region list. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iy5 770**** | The ID of the NAT gateway. |
| VpcId | String | No | vpc- bp15zckdt37pq7 2z**** | The ID of the virtual private cloud (VPC) where the NAT gateway is deployed. |
| Name | String | No | test | The name of the NAT gateway. |
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the NAT gateway. Valid values: Post Paid: pay-as-you-go PrePaid: subscription |
| Spec | String | No | Small | The size of the NAT gateway. Valid values: Small: small Middle: medium Large: large |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NatGateways | Array of NatGateway |   | The details about the NAT gateway. |
| NatGateway |   |   |   |
| AutoPay | Boolean | true | Specifies whether automatic payment is enabled. Valid values: f alse: Automatic payment is disabled. After an order is generated, you must go to the Order Center to complete the payment. t rue: Automatic payment is enabled. Payments are automatically completed. |
| BandwidthPack ageIds | List | bwp-s6lmotmkk**** | The ID of the service plan associated with the NAT gateway. |
| BusinessStatus | String | Normal | The status of the NAT gateway. Valid values: Normal: The NAT gateway works as expected. FinancialLocked: The NAT gateway is locked due to overdue payments. Securit yLocked: The NAT gateway is locked due to security reasons. |
| CreationTime | String | 2020-06- 08T12:20:55 | The time when the NAT gateway was created. The time follows the ISO 8601 standard in yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. |
| Description | String | NAT | The description of the NAT gateway. |
| ExpiredTime | String | 2020-08-26T16:00Z | The time when the NAT gateway expires. |
| ForwardTableId s | List | ftb- uf6gj3mhsg94qsqst **** | The ID of the DNAT table. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceCharge Type | String | PostPaid | The billing method of the NAT gateway. Valid values: Post Paid: pay-as-you-go PrePaid: subscription |
| IpLists | Array of IpList |   | Detailed information about the elastic IP address (EIP) that is associated with the NAT gateway. |
| IpList |   |   |   |
| AllocationId | String | eip- n2y6nbm9z7t1l3xfz **** | The ID of the EIP that is associated with the NAT gateway. |
| ApAccessEnabl ed | Boolean | false | Indicates whether access points are configured. Valid values: t rue: access points are configured. f alse: access points are not configured. |
| IpAddress | String | 116.62.XX.XX | The IP address of the EIP. |
| UsingStatus | String | UsedBySnatTable | The status of the EIP. |
| Name | String | abc | The name of the NAT gateway. |
| NatGatewayId | String | ngw- bp1047e2d4z7kf2ki* *** | The ID of the NAT gateway. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the NAT gateway is deployed. |
| SnatTableIds | List | stb- uf6dalcdu0krz423p* *** | The ID of the SNAT table. |
| Spec | String | Small | The size of the NAT gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Initiating | The status of the NAT gateway. Valid values: Init iat ing: being initialized Available: available Pending: being configured |
| VpcId | String | vpc- bp15zckdt37pq72z* *** | The ID of the VPC where the NAT gateway is deployed. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| TotalCount | Integer | 1 | The number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNatGateways &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeNatGatewaysResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <PageNumber>1</PageNumber>
  <NatGateways>
        <Status>Initiating</Status>
        <Description>NAT</Description>
        <VpcId>vpc-bp15zckdt37pq72z****</VpcId>
        <InstanceChargeType>PostPaid</InstanceChargeType>
        <ExpiredTime>2020-08-26T16:00Z</ExpiredTime>
        <CreationTime>2020-06-08T12:20:55</CreationTime>
        <AutoPay>true</AutoPay>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <Spec>Small</Spec>
        <BusinessStatus>Normal</BusinessStatus>
        <NatGatewayId>ngw-bp1047e2d4z7kf2ki****</NatGatewayId>
        <Name>abc</Name>
        <IpLists>
              <UsingStatus>UsedBySnatTable</UsingStatus>
              <ApAccessEnabled>false</ApAccessEnabled>
              <AllocationId>eip-n2y6nbm9z7t1l3xfz****</AllocationId>
              <IpAddress>116.62.XX.XX</IpAddress>
        </IpLists>
        <ForwardTableIds>ftb-uf6gj3mhsg94qsqst****</ForwardTableIds>
        <SnatTableIds>stb-uf6dalcdu0krz423p****</SnatTableIds>
        <BandwidthPackageIds>bwp-s6lmotmkk****</BandwidthPackageIds>
  </NatGateways>
</DescribeNatGatewaysResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "PageNumber": 1,
    "NatGateways": {
        "Status": "Initiating",
        "Description": "NAT",
        "VpcId": "vpc-bp15zckdt37pq72z****",
        "InstanceChargeType": "PostPaid",
        "ExpiredTime": "2020-08-26T16:00Z",
        "CreationTime": "2020-06-08T12:20:55",
        "AutoPay": true,
        "RegionId": "cn-qingdao-env17-d01",
        "Spec": "Small",
        "BusinessStatus": "Normal",
        "NatGatewayId": "ngw-bp1047e2d4z7kf2ki****",
        "Name": "abc",
        "IpLists": {
            "UsingStatus": "UsedBySnatTable",
            "ApAccessEnabled": false,
            "AllocationId": "eip-n2y6nbm9z7t1l3xfz****",
            "IpAddress": "116.62.XX.XX"
```

`},`

```json
        "ForwardTableIds": "ftb-uf6gj3mhsg94qsqst****",
        "SnatTableIds": "stb-uf6dalcdu0krz423p****",
        "BandwidthPackageIds": "bwp-s6lmotmkk****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

### 1.6 DNAT tables

#### 1.6.1 CreateForwardEntry

Adds a DNAT entry to a DNAT table. Usage notes Each DNAT entry consists of the following parameters: Ext ernalIp, Ext ernalPort , prot ocol, Int ernalIp, and Int ernalPort . After you add a DNAT entry, the NAT gateway forwards packets of the specified protocol from Ext ernalIp:Ext ernalPort to Int ernalIp:Int ernalPort and returns the response message. When you call this operation, take note of the following limits: The combinations of Ext ernalIp, Ext ernalPort , and Prot ocol used in DNAT entries must be unique. Requests cannot be distributed to more than one destination if these requests are from the same source IP address, forwarded by the same port, and use the same protocol. The combinations of Prot ocol, Int ernalIp, and Int ernalPort must be unique. If one or more DNAT entries in the DNAT table are in the Pending or Modif ying state, you cannot add DNAT entries to the DNAT table. The elastic IP address (EIP) specified in a DNAT entry cannot be used in another SNAT entry. The Ext ernalIp parameter indicates the EIP used in a DNAT entry. The private IP address (Int ernalIp) in a DNAT entry must meet the following requirements: Int ernalIp must belong to the CIDR block of the virtual private cloud (VPC) where the NAT gateway is deployed. The DNAT entry takes effect only when Int ernalIp is allocated to an ECS instance and the ECS instance is not assigned an EIP. If Int ernalIp is allocated to a non-ECS resource, such as a highavailability virtual IP address (HAVIP), Server Load Balancer (SLB) instance, or ApsaraDB RDS instance, the DNAT entry does not take effect. Consequently, Internet traffic cannot be forwarded to the private IP address. You can add at most 100 DNAT entries to a DNAT table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateForwardEn try | The operation that you want to perform. Set the value to Creat eForwardEnt ry. |
| ExternalIp | String | Yes | 116.22.XX.XX | The EIP to be specified in the DNAT entry. |
| ExternalPort | String | Yes | 8080 | The public port. Valid values: 1 to 65535. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlc qpa**** | The ID of the DNAT table. |
| InternalIp | String | Yes | 192.168.XX.XX | The destination private IP address. |
| InternalPort | String | Yes | 80 | The destination private port. Valid values: 1 to 65535. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpProtocol | String | Yes | TCP | The protocol type. Valid values: T CP: The NAT gateway forwards TCP packets. UDP: The NAT gateway forwards UDP packets. Any: The NAT gateway forwards packets of all protocols. |
| RegionId | String | Yes | cn-qingdao- env17-d0 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardEntryId | String | fwd- 119smw5tkasdf**** | The ID of the DNAT entry. |
| RequestId | String | A4AEE536-A97A- 40EB-9EBE- 53A6948A6928 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateForwardEntry &ExternalIp=116.22.XX.XX &ExternalPort=8080 &ForwardTableId=ftb-bp1mbjubq34hlcqpa**** &InternalIp=192.1.XX.XX &InternalPort=80 &IpProtocol=TCP &RegionId=cn-qingdao-env17-d0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateForwardEntryResponse>
  <RequestId>A4AEE536-A97A-40EB-9EBE-53A6948A6928</RequestId>
  <ForwardEntryId>fwd-119smw5tkasdf****</ForwardEntryId>
</CreateForwardEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "A4AEE536-A97A-40EB-9EBE-53A6948A6928",
    "ForwardEntryId": "fwd-119smw5tkasdf****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidExternalIp.Mal formed | The specified ExternalIp is not a valid IP address. | The error message returned because the specified EIP is invalid. |
| 400 | InvalidInternalIp.Malf ormed | The specified InternalIp is not a valid IP address. | The error message returned because the specified destination private IP address is invalid. |
| 400 | InvalidExternalPort.M alformed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInternalPort.M alformed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |
| 400 | Forbidden.Destnatio nIpOutOfVpcCIDR | The specified Internal Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.Valu eNotSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter and try again. |
| 404 | InvalidExternalIp.Not Found | Specified External Ip address does not found on the VRouter | The error message returned because the specified EIP does not exist. |
| 400 | Forbidden.ExternalIp .UsedInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified EIP is already used by an SNAT entry. Select a different EIP or delete the SNAT entry. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create forwarding rules. |
| 400 | Forbidden.InternalIp OutOfVpcCIDR | The specified Internal Ip is Out of VPC CIDR. | The error message returned because the private IP address does not fall within the CIDR block of the VPC. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Invalid.natgwNotExis t | The specified natgateway not exist. | The error message returned because the specified NAT gateway does not exist. |
| 400 | InvalidIp.NotInNatg w | The specified Ip not belong to natgateway. | The error message returned because the specified EIP is not associated with the NAT gateway. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |

#### 1.6.2 DeleteForwardEntry

Deletes a DNAT entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteForwardEn try | The operation that you want to perform. Set the value to Delet eForwardEnt ry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0 g**** | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb3 34**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteForwardEntry &ForwardEntryId=fwd-8vbn3bc8roygjp0g**** &ForwardTableId=ftb-8vbx8xu2lqj9qb334**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteForwardEntryResponse>
  <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteForwardEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardEntryI d.NotFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |

| NAT Gateway |   |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter and try again. |
| 400 | IncorretForwardEntr yStatus | The Specified forwardEntry is not exist | The error message returned because the specified DNAT entry does not exist. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |

#### 1.6.3 ModifyForwardEntry

Modifies a specified DNAT entry. Usage notes You cannot modify a DNAT entry if a DNAT entry in the DNAT table is in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyForwardEn try | The operation that you want to perform. Set the value to ModifyForwardEntry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0 gy**** | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb3 34**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ExternalIp | String | No | 116.22.XX.XX | The EIP specified in the DNAT entry. |

| eveloper Guide·API r | eference |   |   | NAT Gatewa |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ExternalPort | String | No | 80 | The public port used for port forwarding. Valid values: 1 to 65535. |
| InternalIp | String | No | 10.10.XX.XX | The private IP address of the Elastic Compute Service (ECS) instance that uses the DNAT entry for Internet communication. |
| InternalPort | String | No | 80 | The private port used for port forwarding. Valid values: 1 to 65535. |
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: The NAT gateway forwards TCP packets. UDP: The NAT gateway forwards UDP packets. Any: The NAT gateway forwards packets of all protocols. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A4AEE536-A97A- 40EB-9EBE- 53A6948A6928 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyForwardEntry &ForwardEntryId=fwd-8vbn3bc8roygjp0gy**** &ForwardTableId=ftb-8vbx8xu2lqj9qb334**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyForwardEntryResponse>
  <RequestId>A4AEE536-A97A-40EB-9EBE-53A6948A6928</RequestId>
</ModifyForwardEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "A4AEE536-A97A-40EB-9EBE-53A6948A6928"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidExternalIp.Mal formed | The specified ExternalIp is not a valid IP address. | The error message returned because the specified EIP is invalid. |
| 400 | InvalidInternalIp.Malf ormed | The specified InternalIp is not a valid IP address. | The error message returned because the specified destination private IP address is invalid. |
| 400 | InvalidExternalPort.M alformed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInternalPort.M alformed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |
| 400 | Forbidden.Destnatio nIpOutOfVpcCIDR | The specified Destination Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.Valu eNotSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 400 | QuotaExceeded | Forward entry quota exceeded in this route table. | The error message returned because the number of custom route entries in the same route table cannot exceed 200. Go to the Quota Management page to request a quota increase. |
| 404 | InvalidForwardEntryI d.NotFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidExternalIp.Not Found | Specified External Ip address does not found on the VRouter | The error message returned because the specified EIP does not exist. |
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter and try again. |
| 400 | Forbidden.ExternalIp .UsedInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified EIP is already used by an SNAT entry. Select a different EIP or delete the SNAT entry. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.Already.B ounded | The specified instance already bounded | The error message returned because the specified instance is associated with another DNAT entry. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |

#### 1.6.4 DescribeForwardTableEntries

Queries DNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeForward TableEntries | The operation that you want to perform. Set the value to DescribeForwardT ableEnt ries. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlc qpa**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryId | String | No | fwd- 8vbn3bc8roygjp0 gy**** | The ID of the DNAT entry to be queried. |
| ExternalIp | String | No | 116.11.XX.XX | The EIP specified in the DNAT entry. |
| ExternalPort | String | No | 8080 | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 192.168.XX.XX | The destination private IP address. |
| InternalPort | String | No | 80 | The destination private port. Valid values: 1 to 65535. |

| D | eveloper Guide·API r | eference |   |   | NAT Gatewa | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: The NAT gateway forwards TCP packets. UDP: The NAT gateway forwards UDP packets. Any: The NAT gateway forwards packets of all protocols. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| PageNumber | Integer | No | 1 | The page number of the returned page. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardTableE ntries | Array of ForwardTableE ntry |   | The details of the DNAT entries. |
| ForwardTableE ntry |   |   |   |
| ExternalIp | String | 116.11.XX.XX | The EIP specified in the DNAT entry. |
| ExternalPort | String | 80 | The public port. |
| ForwardEntryId | String | fwd-119smw5tk**** | The ID of the DNAT entry. |
| ForwardEntryN ame | String | ForwardEntry-1 | The name of the DNAT entry. |
| ForwardTableId | String | ftb-11tc6xgmv**** | The ID of the DNAT table to which the DNAT entry belongs. |

| NAT Gateway |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternalIp | String | 192.168.XX.XX | The private IP address. |
| InternalPort | String | 25 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | TCP | The protocol type. |
| Status | String | Available | The status of the DNAT entry. |
| TotalCount | Integer | 5 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | A6C4A8B1-7561- 4509-949C- 20DEB40D71E6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeForwardTableEntries &ForwardTableId=ftb-bp1mbjubq34hlcqpa**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeForwardTableEntriesResponse>
  <TotalCount>5</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>A6C4A8B1-7561-4509-949C-20DEB40D71E6</RequestId>
  <PageNumber>1</PageNumber>
  <ForwardTableEntries>
        <Status>Available</Status>
        <ExternalPort>80</ExternalPort>
        <ExternalIp>116.11.XX.XX</ExternalIp>
        <ForwardEntryId>fwd-119smw5tk****</ForwardEntryId>
        <IpProtocol>TCP</IpProtocol>
        <InternalPort>25</InternalPort>
        <ForwardEntryName>ForwardEntry-1</ForwardEntryName>
        <InternalIp>192.168.XX.XX</InternalIp>
        <ForwardTableId>ftb-11tc6xgmv****</ForwardTableId>
  </ForwardTableEntries>
</DescribeForwardTableEntriesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 5,
    "PageSize": 10,
    "RequestId": "A6C4A8B1-7561-4509-949C-20DEB40D71E6",
    "PageNumber": 1,
    "ForwardTableEntries": {
        "Status": "Available",
        "ExternalPort": 80,
        "ExternalIp": "116.11.XX.XX",
        "ForwardEntryId": "fwd-119smw5tk****",
        "IpProtocol": "TCP",
        "InternalPort": 25,
        "ForwardEntryName": "ForwardEntry-1",
        "InternalIp": "192.168.XX.XX",
        "ForwardTableId": "ftb-11tc6xgmv****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardTableI d.NotFound | Specified forwardTableId does not exist | The error message returned because the specified DNAT table does not exist. Check the parameter and try again. |

### 1.7 SNAT tables

#### 1.7.1 CreateSnatEntry

Adds an SNAT entry to an SNAT table. Descriptions When you call this operation, take note of the following limits: The vSwitch and Elastic Compute Service (ECS) instance specified in an SNAT entry must be created in the virtual private cloud (VPC) where the NAT gateway is deployed. Each vSwitch or ECS instance can be specified in only one SNAT entry. If a high-availability virtual IP address (HAVIP) exists in a vSwitch, you cannot create SNAT entries. You cannot specify the same elastic IP address (EIP) in both a DNAT entry and an SNAT entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSnatEntry | The operation that you want to perform. Set the value to Creat eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| SnatIp | String | Yes | 47.23.XX.XX | The EIPs specified in the SNAT entry. Separate multiple EIPs with commas (,). |

| Developer Guide·API r | eference |   |   | NAT Gatewa |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SnatTableId | String | Yes | stb- bp190wu8io1vge v**** | The ID of the SNAT table. |
| SourceVSwitchId | String | No | vsw- bp1nhx2s9ui5o*** * | The ID of the vSwitch that needs to access the Internet. |
| SourceCIDR | String | No | 10.1.1.0/24 | The CIDR block of the vSwitch or the IP address of the ECS instance. Specif y a vSwit ch: You can specify the CIDR block of a vSwitch, for example, 192.168.1.0/24. When the ECS instances that belong to the vSwitch send requests to the Internet, the NAT gateway provides SNAT services. If you specify only one EIP for the Snat Ip parameter, the ECS instance uses the specified EIP to access the Internet. If you specify multiple EIPs for the Snat Ip parameter, the ECS instance randomly selects an EIP from Snat Ip to access the Internet. Specif y an ECS inst ance: You can specify the IP address of an ECS instance, for example, 192.168.1.0/32. When the ECS instance needs to access the Internet, the NAT gateway provides the SNAT service for the ECS instance. If you specify only one EIP for the Snat Ip parameter, the ECS instance uses the specified EIP to access the Internet. If you specify multiple EIPs for the Snat Ip parameter, the ECS instance randomly selects an EIP from Snat Ip to access the Internet. Not e You cannot set this parameter and SourceVSwt ichId at the same time. If the SourceVSwit chId parameter is set, you cannot set the SourceCIDR parameter. If the SourceCIDR parameter is set, you cannot set the SourceVSwit chId parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |

|   | http:// |
|---|---|
| https:// |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatEntryId | String | snat-kmd6nv8fy**** | The ID of the SNAT entry. |
| RequestId | String | 2315DEB7-5E92- 423A-91F7- 4C1EC9AD97C3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSnatEntry &RegionId=cn-qingdao-env17-d01 &SnatIp=47.23.XX.XX &SnatTableId=stb-bp190wu8io1vgev**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateSnatEntryResponse>
      <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
      <SnatEntryId>snat-119smw5tkx****</SnatEntryId>
</CreateSnatEntryResponse>
```

`JSON` format `{`

```json
    "SnatEntryId": "snat-kmd6nv8fyx****",
    "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 400 | Forbidden.SourceVS witchId.IncludeHaVip | There is some HaVips under specified VSwitch | The error message returned because the specified vSwitch is associated with HAVIPs. |
| 400 | InvalidSnatIp.Malfor med | The specified SnatIp is not a valid IP address. | The error message returned because the specified EIP is invalid. |
| 400 | SNAT IP POOL COU _ _ _ NT TOO MANY _ _ | The Snat pool ip too many. | The error message returned because the number of IP addresses in the SNAT IP address pool has reached the upper limit. |
| 400 | Forbidden.SnatEntry CountLimited | SNAT entry in the specified SNAT table reach it?s limit. | The error message returned because the number of SNAT entries has reached the upper limit. |
| 400 | NOT ALLOW USE SO _ _ _ URCECIDR | The User not in nat scope unlimited white list. _ _ Cannot use SourceCidr param. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. |
| 404 | InvalidVSwitchId.Not Found | The specified virtual switch does not exists. | The error message returned because the specified vSwitch does not exist. Check whether the specified ID is valid. |
| 400 | INVALID PARAMETER _ | The parameter invalid. | The error message returned because the parameter is set to an invalid value. |
| 400 | Forbidden.SourceVS witchId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already created for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFou nd | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified EIP does not exist on the NAT gateway. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.IpUsedInF orwardTable | The specified SnatIp already used in forward table | The error message returned because the specified EIP is already used by a DNAT entry. Select another EIP or delete the DNAT rule that uses the specified EIP. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create DNAT entries. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |

#### 1.7.2 DeleteSnatEntry

Deletes a specified SNAT entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSnatEntry | The operation that you want to perform. Set the value to Delet eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0pl qc**** | The ID of the SNAT entry. |
| SnatTableId | String | Yes | stb- bp190wu8io1vge v80**** | The ID of the SNAT table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSnatEntry &RegionId=cn-qingdao-env17-d01 &SnatEntryId=snat-bp1vcgcf8tm0plqc**** &SnatTableId=stb-bp190wu8io1vgev80**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSnatEntryResponse>
  <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteSnatEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretSnatEntrySta tus | Some Snat entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more SNAT entries in the SNAT table are in the Pending or Modifying state. |
| 404 | InvalidSnatEntryId.N otFound | Specified Snat entry ID does not exist | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 404 | InvalidSnatEntryId.N otFound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |

#### 1.7.3 ModifySnatEntry

Modifies a specified SNAT entry. Not e You cannot modify SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySnatEntry | The operation that you want to perform. Set the value to Modif ySnat Ent ry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d0 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0pl qcg**** | The ID of the SNAT entry that you want to modify. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u 3t**** | The ID of the SNAT table to which the SNAT entry belongs. |
| SnatIp | String | No | 47.23.XX.XX | The elastic IP address (EIP) specified in the SNAT entry. Separate multiple EIPs with commas (,). |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

|   | http:// |
|---|---|
| https:// |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2315DEB7-5E92- 423A-91F7- 4C1EC9AD97C3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySnatEntry &RegionId=cn-qingdao-env17-d0 &SnatEntryId=snat-bp1vcgcf8tm0plqcg**** &SnatTableId=stb-8vbczigrhop8x5u3t**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySnatEntryResponse>
   <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifySnatEntryResponse>
```

`JSON` format `{`

```json
  "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 400 | InvalidSnatIp.Malfor med | The specified SnatIp is not a valid IP address. | The error message returned because the specified EIP is invalid. |
| 404 | InvalidSnatEntryId.N otFound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |

| eveloper Guid | e·API reference |   | NAT Gatewa |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.SourceVS witchId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already created for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFou nd | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified EIP does not exist on the NAT gateway. |
| 400 | Forbidden.IpUsedInF orwardTable | The specified SnatIp already used in forward table | The error message returned because the specified EIP is already used by a DNAT entry. Select another EIP or delete the DNAT rule that uses the specified EIP. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |

#### 1.7.4 DescribeSnatTableEntries

Queries SNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSnatTabl eEntries | The operation that you want to perform. Set the value to DescribeSnat T ableEnt ries. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u 3t**** | The ID of the SNAT table. |
| SnatEntryId | String | No | snat- 8vbae8uqh7rjpk7 d2**** | The ID of the SNAT entry. |
| SourceVSwitchId | String | No | vsw-3xb**** | The ID of the vSwitch that can access the Internet by using SNAT. |

| NAT Gateway |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| SourceCIDR | String | No | 192.168.XX.XX/1 6 | The source CIDR block specified in the SNAT entry. |
| SnatIp | String | No | 116.11.XX.XX | The elastic IP address (EIP) specified in the SNAT entry. |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

|   | http:// |
|---|---|
| https:// |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatTableEntrie s | Array of SnatTableEntry |   | The details about the queried SNAT entries. |
| SnatTableEntry |   |   |   |
| SnatEntryId | String | snat- 8vbae8uqh7rjpk7d2* *** | The ID of the SNAT entry. |
| SnatEntryName | String | SnatEntry-1 | The name of the SNAT entry. |
| SnatIp | String | 116.XX.XX.28 | The EIP specified in the SNAT entry. |
| SnatTableId | String | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table to which the SNAT entry belongs. |
| SourceCIDR | String | 192.168.XX.XX/16 | The source CIDR block specified in the SNAT entry. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SourceVSwitchI d | String | vsw-3xb**** | The ID of the vSwitch that can access the Internet by using SNAT. |
| Status | String | Pending | The status of the SNAT entry. |
| TotalCount | Integer | 1 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| RequestId | String | 6D7E89B1-1C5B- 412B-8585- 4908E222EED5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSnatTableEntries &RegionId=cn-qingdao-env17-d01 &SnatTableId=stb-8vbczigrhop8x5u3t**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSnatTableEntriesResponse>
  <TotalCount>1</TotalCount>
  <PageSize>5</PageSize>
  <RequestId>6D7E89B1-1C5B-412B-8585-4908E222EED5</RequestId>
  <PageNumber>1</PageNumber>
  <SnatTableEntries>
        <Status>Pending</Status>
        <SourceVSwitchId>vsw-3xb****</SourceVSwitchId>
        <SnatEntryName>SnatEntry-1</SnatEntryName>
        <SourceCIDR>192.168.XX.XX/16</SourceCIDR>
        <SnatEntryId>snat-8vbae8uqh7rjpk7d2****</SnatEntryId>
        <SnatIp>116.XX.XX.28</SnatIp>
        <SnatTableId>stb-8vbczigrhop8x5u3t****</SnatTableId>
  </SnatTableEntries>
</DescribeSnatTableEntriesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 5,
    "RequestId": "6D7E89B1-1C5B-412B-8585-4908E222EED5",
    "PageNumber": 1,
    "SnatTableEntries": {
        "Status": "Pending",
        "SourceVSwitchId": "vsw-3xb****",
        "SnatEntryName": "SnatEntry-1",
        "SourceCIDR": "192.168.XX.XX/16",
        "SnatEntryId": "snat-8vbae8uqh7rjpk7d2****",
        "SnatIp": "116.XX.XX.28",
        "SnatTableId": "stb-8vbczigrhop8x5u3t****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |

### 1.8 NAT bandwidth packages

#### 1.8.1 CreateBandwidthPackage

Creates a NAT service plan. Descriptions A NAT service plan consists of bandwidth resources and one or more public IP addresses. You can associate up to four NAT service plans with a NAT gateway. A NAT service plan includes: Bandwidth resources A group of public IP addresses Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBandwidth Package | The operation that you want to perform. Set the value to Creat eBandwidt hPackage. |
| Bandwidth | Integer | Yes | 5 | The bandwidth of the NAT service plan. Valid values: 5 to 1000. Unit: Mbit/s. |
| IpCount | Integer | Yes | 2 | The number of public IP addresses in the NAT service plan. Valid values: 1 t o 50. |
| NatGatewayId | String | Yes | ngw- 7mwb327j1**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | Name | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. It cannot start with http:// or https:// . |
| Description | String | No | Description | The description of the NAT service plan. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ISP | String | No | BGP | Only BGP is supported. |

|   | NAT Gateway |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Zone | String | No | cn-qingdao- env17- amtest11001-a | The zone to which the NAT service plan belongs. If you do not set this parameter, the service plan is randomly allocated to a zone. Not e Connectivity is not affected when the IP addresses provided by the NAT service plan and the backend Elastic Compute Service (ECS) instances belong to different zones. However, when the IP addresses and ECS instances belong to the same zone, latency can be reduced. |
| InternetChargeTy pe | String | No | PayByBandwidth | The metering method of the NAT service plan. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h: pay-by- bandwidth |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPack ageId | String | bwp-s6lmotmkk**** | The ID of the NAT service plan. |
| RequestId | String | 54ED4074-3F89- 4F11-B166- 837DD3E20FE3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateBandwidthPackage &Bandwidth=5 &IpCount=2 &NatGatewayId=ngw-7mwb327j1**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBandwidthPackageResponse>
  <RequestId>54ED4074-3F89-4F11-B166-837DD3E20FE3</RequestId>
  <BandwidthPackageId>bwp-s6lmotmkk****</BandwidthPackageId>
</CreateBandwidthPackageResponse>
```

`JSON` format `{`

```json
    "RequestId": "54ED4074-3F89-4F11-B166-837DD3E20FE3",
    "BandwidthPackageId": "bwp-s6lmotmkk****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidVpcId.NotFou nd | Specified value of VpcId is not found in our record. | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidZoneId.NotFo und | Specified value of ZoneId is not exists. | The error message returned because the specified zone does not exist. |
| 404 | InvalidZoneId.NotFo und | Can not find ZoneId for allocated ip. | The error message returned because the zone of the specified IP address is invalid. |
| 400 | QuotaExceeded.Ban dwidthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Request a quota increase on the Quota Management page. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Ban dwidthPackageCoun tOnNatGateway | BandwidthPackage count limit on one NatGateway exceeded. | The error message returned because the number of NAT service plans has reached the upper limit. You can associate up to four NAT service plans with a NAT gateway. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | InvalidParameter.Ba ndwidthPackage.n.IS P.ValueNotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified Internet service provider (ISP) of the bandwidth resources is invalid. |
| 400 | ZONE NO AVAILABLE _ _ IP _ | The Zone have no available ip. | The error message returned because no IP address is available in the zone. |

#### 1.8.2 ModifyBandwidthPackageSpec

Modifies the bandwidth of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidth PackageSpec | The operation that you want to perform. Set the value to Modif yBandwidt hPackageSpec. |
| Bandwidth | String | Yes | 5 | The bandwidth value of the NAT service plan. Valid values: 5 to 1000. Unit: Mbit/s. |
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1- 43E6-AC03- ADD96B6E4907 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBandwidthPackageSpec &Bandwidth=5 &BandwidthPackageId=bwp-s6lmotmkk**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBandwidthPackageSpecResponse>
  <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
</ModifyBandwidthPackageSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidBandwidth.Val ueNotSupported | The specified value of Bandwidth not supported. | The error message returned because the specified maximum bandwidth value is invalid. |
| 404 | BandwidthPackage.F inancialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

#### 1.8.3 DescribeBandwidthPackages

Queries NAT service plans in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBandwid thPackages | The operation that you want to perform. Set the value to DescribeBandwidt hPackages. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPackag eId | String | No | bwp- bp1xea10o8qxw dfs**** | The ID of the NAT service plan. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iydf re**** | The ID of the NAT gateway with which the NAT service plan is associated. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPack ages | Array of BandwidthPack age |   | The details about the NAT service plan. |
| BandwidthPack age |   |   |   |
| Bandwidth | String | 5 | The bandwidth value of the NAT service plan. Valid values: 5 to 5000. Unit: Mbit/s. |
| BandwidthPack ageId | String | bwp- xxoo123sfwr**** | The ID of the NAT service plan. |

| eveloper Guide·AP | I reference |   | NAT Gatewa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the NAT service plan. Normal: normal FinancialLocked: locked due to overdue payments Securit yLocked: locked for security reasons. |
| CreationTime | String | 2020-06- 08T12:20:55 | The time when the NAT service plan was created. The time follows the ISO 8601 in the YYYY-MM-DDThh:mmZ format. The time is displayed in UTC. |
| Description | String | test123 | The description of the NAT service plan. |
| ISP | String | BGP | Only BGP is supported. |
| InstanceCharge Type | String | PostPaid | The billing method of the NAT service plan. Only Post Paid (pay-as-you-go) is supported. |
| InternetCharge Type | String | PayByBandwidth | The metering method of the NAT service plan. PayByT raf f ic: pay-by-data-transfer PayByBandwidt h: pay-by-bandwidth |
| IpCount | String | 1 | The number of public IP addresses in the NAT service plan. |
| Name | String | abc | The name of the NAT service plan. |
| NatGatewayId | String | ngw- xxoo123ggtf**** | The ID of the NAT gateway with which the NAT service plan is associated. |
| PublicIpAddress es | Array of PublicIpAddress e |   | The details about the public IP addresses in the NAT service plan. |
| PublicIpAddress e |   |   |   |

| NAT Gateway |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationId | String | eip- 2zeerraiwb7ujdeds* *** | The ID of the public IP address. |
| ApAccessEnabl ed | Boolean | true | Indicates whether access points are configured. Valid values: t rue: yes f alse: no |
| IpAddress | String | 116.28.XX.XX | The public IP address. |
| UsingStatus | String | Available | The status of the public IP address. |
| RegionId | String | cn-qingdao-env17- d01 | The region ID of the NAT service plan. |
| Status | String | Available | The status of the NAT service plan. |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | The ID of the zone to which the NAT service plan belongs. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| TotalCount | Integer | 1 | The number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBandwidthPackages &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBandwidthPackagesResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <PageNumber>1</PageNumber>
  <BandwidthPackages>
        <Status>Available</Status>
        <IpCount>1</IpCount>
        <Description>test123</Description>
        <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
        <InstanceChargeType>PostPaid</InstanceChargeType>
        <ISP>BGP</ISP>
        <BusinessStatus>Normal</BusinessStatus>
        <InternetChargeType>PayByBandwidth</InternetChargeType>
        <Name>abc</Name>
        <Bandwidth>5</Bandwidth>
        <CreationTime>2020-06-08T12:20:55</CreationTime>
        <BandwidthPackageId>bwp-xxoo123sfwr****</BandwidthPackageId>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <NatGatewayId>ngw-xxoo123ggtf****</NatGatewayId>
        <PublicIpAddresses>
              <UsingStatus>Available</UsingStatus>
              <ApAccessEnabled>true</ApAccessEnabled>
              <AllocationId>eip-2zeerraiwb7ujdeds****</AllocationId>
              <IpAddress>116.28.XX.XX</IpAddress>
        </PublicIpAddresses>
  </BandwidthPackages>
</DescribeBandwidthPackagesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "PageNumber": 1,
    "BandwidthPackages": {
        "Status": "Available",
        "IpCount": 1,
        "Description": "test123",
        "ZoneId": "cn-qingdao-env17-amtest11001-a",
        "InstanceChargeType": "PostPaid",
        "ISP": "BGP",
        "BusinessStatus": "Normal",
        "InternetChargeType": "PayByBandwidth",
        "Name": "abc",
        "Bandwidth": 5,
        "CreationTime": "2020-06-08T12:20:55",
        "BandwidthPackageId": "bwp-xxoo123sfwr****",
        "RegionId": "cn-qingdao-env17-d01",
        "NatGatewayId": "ngw-xxoo123ggtf****",
        "PublicIpAddresses": {
            "UsingStatus": "Available",
            "ApAccessEnabled": true,
            "AllocationId": "eip-2zeerraiwb7ujdeds****",
            "IpAddress": "116.28.XX.XX"
```

`}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 1.8.4 ModifyBandwidthPackageAttribute

Modifies the name and description of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidth PackageAttribute | The operation that you want to perform. Set the value to Modif yBandwidt hPackageAt t ribut e . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | NATABC | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | This is NAT. | The description of the NAT service plan. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DFDDD35D-3F29- 4E15-AA28- 53F5341F9599 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBandwidthPackageAttribute &BandwidthPackageId=bwp-s6lmotmkk**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBandwidthPackageAttributeResponse>
  <RequestId>DFDDD35D-3F29-4E15-AA28-53F5341F9599</RequestId>
</ModifyBandwidthPackageAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "DFDDD35D-3F29-4E15-AA28-53F5341F9599"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidBandwidthPac kageId.NotFound | The specified bandwidthPackageId does not exist in our records. | The error message returned because the ID of the specified NAT service plan does not exist. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |

#### 1.8.5 DeleteBandwidthPackage

Deletes a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBandwidth Package | The operation that you want to perform. Set the value to Delet eBandwidt hPackage. |
| BandwidthPackag eId | String | Yes | bwp- bp1arsrmca9kp** ** | The ID of the NAT service plan. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT service plan. Valid values: f alse (default): no t rue: yes |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7D275A59-1EB0- 4775-8A20- 2A47055EAC5C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteBandwidthPackage &BandwidthPackageId=bwp-bp1arsrmca9kp**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBandwidthPackageResponse>
  <RequestId>7D275A59-1EB0-4775-8A20-2A47055EAC5C</RequestId>
</DeleteBandwidthPackageResponse>
```

`JSON` format `{`

```json
    "RequestId": "7D275A59-1EB0-4775-8A20-2A47055EAC5C"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | DependencyViolatio n.ForwardEntry | The specified BandwidthPackageId has dependent resource. | The error message returned because the NAT service plan is associated with SNAT or DNAT entries. Delete them and try again. |
| 400 | DependencyViolatio n.SnatEntry | The specified BandwidthPackageId has dependent resource. | The error message returned because the NAT service plan is associated with SNAT or DNAT entries. Delete them and try again. |

#### 1.8.6 AddBandwidthPackageIps

Adds one or more public IP addresses to a NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBandwidthPa ckageIps | The operation that you want to perform. Set the value to AddBandwidt hPackageIps. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| IpCount | String | Yes | 2 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. |
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e0**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EC0B5C51-7F40- 44D6-A642- 1DE764B547EC | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddBandwidthPackageIps &RegionId=cn-qingdao-env17-d01 &IpCount=2 &BandwidthPackageId=bwp-s6lmotmkk**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBandwidthPackageIpsResponse>
  <RequestId>EC0B5C51-7F40-44D6-A642-1DE764B547EC</RequestId>
</AddBandwidthPackageIpsResponse>
```

`JSON` format `{`

```json
    "RequestId": "EC0B5C51-7F40-44D6-A642-1DE764B547EC"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidIpCount.Value NotSupported | The specified value of IpCount not supported. | The error message returned because the value of the IpCount parameter is invalid. |
| 400 | QuotaExceeded.Ban dwidthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Request a quota increase on the Quota Management page. |
| 404 | BandwidthPackage.F inancialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

#### 1.8.7 RemoveBandwidthPackageIps

Removes public IP addresses from a NAT service plan. When you call this operation, you must specify the public IP addresses to be removed. You cannot remove all public IP addresses. If you specify all public IP addresses, this operation fails. If you specify public IP addresses that are not associated with the NAT service plan, this operation fails. If you specify public IP addresses that are used in DNAT or SNAT entries, this operation fails. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveBandwidt hPackageIps | The operation that you want to perform. Set the value to RemoveBandwidt hPackageIps. |
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan from which you want to remove the public IP addresses. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| RemovedIpAddre sses.N | RepeatLi st | Yes | 116.12.XX.XX | The ID of the public IP address to be removed. Valid values of N: 1 to 20. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7D275A59-1EB0- 4775-8A20- 2A47055EAC5C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveBandwidthPackageIps &BandwidthPackageId=bwp-s6lmotmkk**** &RegionId=cn-qingdao-env17-d01 &RemovedIpAddresses.1=116.12.XX.XX &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveBandwidthPackageIpsResponse>
  <RequestId>7D275A59-1EB0-4775-8A20-2A47055EAC5C</RequestId>
</RemoveBandwidthPackageIpsResponse>
```

`JSON` format `{`

```json
    "RequestId": "7D275A59-1EB0-4775-8A20-2A47055EAC5C"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | invalidRemovedIpAd dresses.NotFound | Some of the specified value of RemovedIpAddress not found in specified BandwidthPackage. | The error message returned because a specified public IP address is not associated with the NAT service plan. Check the specified IP addresses. |
| 400 | InvalidIpCount.Value NotSupported | Can not remove all ips of the bandwidthPackage. | The error message returned because you cannot remove all public IP addresses. |
| 400 | InvalidRemovedIpAd dresses.NotFound | Some of remove ip is not natPublicIp. | The error message returned because one or more specified public IP addresses are not associated with the NAT service plan. |
| 400 | DependencyViolatio n.ForwardEntry | The ip has been used by ForwardEntry. | The error message returned because one or more specified public IP addresses are used by port forwarding rules. Delete the rules before you call this operation. |
| 400 | DependencyViolatio n.SnatEntry | The ip has been used by SnatEntry. | The error message returned because one or more specified public IP addresses are used by SNAT entries. Delete the SNAT entries before you call this operation. |
| 404 | BandwidthPackage.F inancialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

using ASAPI

## 2 Make SDK calls by using ASAPI

### 2.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize operations and audit and manage their calls. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, avoiding inconsistent operations caused by different call methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a unified manner and customize development. ASAPI supports access of most cloud services deployed in Apsara Stack and passthrough or encapsulation of different backend APIs. This way, operations can be called with the same method. ASAPI allows you to use SDKs and API Portal to call APIs registered in ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. using ASAPI

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
operation name in the search box, and then click the search icon. using ASAPI
4. View and remember the service name, API operation name, and API version.

### 2.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), using ASAPI dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
of the Apsara ASAPI Management platform. using ASAPI

### 2.5 Obtain the core package for ASAPI

ASAPI Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 2.6 Obtain an AccessKey pair

An AccessKey pair is composed of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the AccessKey message, view the AccessKey pair of the organization.
using ASAPI Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
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

This topic describes how to obtain and use SDK for Java. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use NAT Gateway SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. using ASAPI NAT Gateway SDK for Java supports JDK 1.6 and later. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Usage You can call API operations on ASAPI by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests using ASAPI

```java
public class DescribeNatGateways {
    public static void main(String[] args) {
        // Set the endpoint of ASAPI.
        String endpoint = "http://xxx/asapi/v3";
    // Set request parameters.
    Map<String, String> parameters = new HashMap<String, String>();
    // Set parameters for the product.
    parameters.put("Product", "vpc");            // The product name, which must be the s
ame as the name displayed in the corresponding API directory.
    parameters.put("Action", "DescribeNatGateways");        //The API operation name, whi
ch must be in the same case as that in the API directory.
    parameters.put("Version", "2016-04-28");      // The API version.
    // Set authorization-related parameters.
    parameters.put("AccessKeyId", "<your-access-key-id>");          // The AccessKey ID o
f the authorized account.
    parameters.put("AccessKeySecret", "<your-access-key-secret>");  // The AccessKey secr
et of the authorized account.
    // Set business parameters.
    parameters.put("username", "<your-username>");                  // The user name used
to log on to the ASCM console.
    parameters.put("password", "<your-password>");                  // The password used
to log on to the ASCM console.
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("RegionId", "cn-hangzhou-env12-d01");
    parameters.put("json", jsonObject.toJSONString());
    // Create an ASClient instance for initiating requests.
    ASClient client = new ASClient();
    // Add request headers.
    client.addHeader("x-acs-resourceGroupId", "112233");
    // Initiate the request and obtain the response.
    String result = client.doPost(endpoint, parameters);
```

`}` `}`

### 2.9 SDK for Node.js

This topic describes how to obtain and use SDK for Node.js. Prerequisites You must have an Apsara Stack tenant account and an AccessKey pair (AccessKey ID and AccessKey secret) to use NAT Gateway SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, you must configure mocha.opts.
using ASAPI

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Usage The following example shows how to use SDK for Node.js:
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
3. Initiate the request and handle the response or exceptions.

```
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'DescribeNatGateways',
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
using ASAPI
2. Add the Product Name field to the request header.
Sample code The following code shows how to call a NAT Gateway API operation:

```java
try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessK
eySecret);
    // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "ecs", "<ASAPI gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
    DescribeNatGatewaysRequest request = new DescribeNatGatewaysRequest();
    request.setSysRegionId(regionId); // Or setRegionId(regionId)
    // Set common parameters based on the information about the current user.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    DescribeNatGatewaysResponse result = (DescribeNatGatewaysResponse) acsClient.getAcsResp
onse(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```

`}`
