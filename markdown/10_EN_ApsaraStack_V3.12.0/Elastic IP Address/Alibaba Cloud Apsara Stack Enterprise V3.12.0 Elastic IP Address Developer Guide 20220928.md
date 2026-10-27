---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic IP Address Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 61
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic IP Address Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Elastic%20IP%20Address%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Elastic IP Address Developer Guide 20220928

## Table of Contents

- 1 API reference
  - 1.1 List of operations by function
  - 1.2 Make API requests
    - 1.2.1 Request syntax
    - 1.2.2 API authorization
    - 1.2.3 Request signature
  - 1.3 RAM authentication
  - 1.4 Common parameters
  - 1.5 Elastic IP Address (EIP)
    - 1.5.1 AllocateEipAddress
    - 1.5.2 AllocateEipAddressPro
    - 1.5.3 AssociateEipAddress
    - 1.5.4 UnassociateEipAddress
    - 1.5.5 ModifyEipAddressAttribute
    - 1.5.6 ReleaseEipAddress
    - 1.5.7 DescribeEipAddresses
    - 1.5.8 DescribeEipMonitorData
    - 1.5.9 MoveResourceGroup
    - 1.5.10 DescribeHighDefinitionMonitorLogAttribute
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
  - 2.10 Use the POP SDK to call API operations on ASAPI (Optional)

## 1 API reference

### 1.1 List of operations by function

The following table describes API operations available for use in Elastic IP Address (EIP).

| API | Description |
|---|---|
| AllocateEipAddress | Applies for an EIP. |
| AllocateEipAddressPro | Applies for a specified EIP. |
| AssociateEipAddress | Associates an EIP with an instance in the same region. |
| UnassociateEipAddress | Disassociates an EIP from a cloud resource. |
| ModifyEipAddressAttribute | Modifies the name, description, and bandwidth limit of a specified EIP. |
| ReleaseEipAddress | Releases a specified EIP. |
| DescribeEipAddresses | Queries the EIPs that you create in a specified region. |
| DescribeEipMonitorData | Queries monitoring information about EIPs. You can query monitoring data within the last 30 days and specify up to 400 data points in each request. |
| MoveResourceGroup | Modifies the resource group to which a specified cloud resource belongs. |
| DescribeHighDefinitionMonitorLogAttribute | Queries fine-grained monitoring configurations of an EIP. |

### 1.2 Make API requests

#### 1.2.1 Request syntax

To call an Elastic IP Address (EIP) API operation, you must send an HTTP GET request to the endpoint of the EIP API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8. EIP API operations use the RPC protocol. You can call EIP API operations by sending HTTP GET requests. The request syntax is:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the API. The endpoint of the EIP API is `vpc.`example `.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Uni-manager Operations Console. For more information, see Obtain the endpoint of ASAPI. Action: the name of the operation that you want to perform. For example, to query EIPs, you must set the Action parameter to DescribeEipAddresses. Version: the version of the API that you want to call. The current EIP API version is 2016-04-28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information, see Common parameters. The following example describes how to call the DescribeEipAddresses operation to query EIPs. Not e The sample requests are formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeEipAddresses &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 1.2.2 API authorization

To ensure the security of your account, we recommend that you call EIP API operations as a RAM user. To call the EIP API as a RAM user, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the EIP resources and API operations that allow the authorization, see RAM authentication.

#### 1.2.3 Request signature

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. EIP implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to the EIP API request in the following format: https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeEipAddresses as an example. If the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the following original request URL is obtained:

```
http://vpc.example.com/?Action=DescribeEipAddresses &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeEipAddresses&Format%3DXML&SignatureMethod %3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1 .0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter.

```
http://vpc.example.com/?Action=DescribeEipAddresses &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 1.3 RAM authentication

Before you call an EIP operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM account. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource. EIP resources that allow authorized access The following table lists the EIP resources that allow authorized access and their ARNs.

| Resource type | ARN |
|---|---|
| EIPs | acs:vpc:$regionid:$accountid:eip/$allocationid |
|   | acs:vpc:$regionid:$accountid:eip/* |
|   | acs:vpc:*:$accountid:eip/* |
| General resources | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accoutid`/`vrouterid are IDs of the specific resources, `*` represents all resources. EIP API operations that allow authorized access The following table lists the EIP API operations that allow authorized access and their ARNs.

| API | ARN |
|---|---|
| AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |
| AllocateEipAddressPro | acs:vpc:$regionid:$accountid:eip/* |
| AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |
|   | Associate an Elastic Compute Service (ECS) instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |
| DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |
| UnassociateEipAddress | Associate an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |
| ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |
| DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |

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

### 1.5 Elastic IP Address (EIP)

#### 1.5.1 AllocateEipAddress

Applies for an elastic IP address (EIP). Usage notes After you call this operation, the system randomly allocates an EIP that is in the Available state in the specified region. EIPs support only the following transport layer protocols: Internet Control Message Protocol (ICMP), Transmission Control Protocol (TCP), and User Datagram Protocol (UDP). Internet Group Management Protocol (IGMP) and Stream Control Transmission Protocol (SCTP) are not supported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddre ss | The operation that you want to perform. Set the value to Allocat eEipAddress. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | String | No | 1 | The bandwidth limit of the EIP. Unit: Mbit/s. Valid values: 1 to 200. Default value: 1. |
| Period | Integer | No | 1 | The subscription duration. When PricingCycle is set to Mont h, set Period to a value from 1 t o 9. When PricingCycle is set to Year, set Period to a value from 1 t o 3. This parameter is required when the value of the Inst anceChargeT ype parameter is set to PrePaid. When the value of the Inst anceChargeT ype parameter is set to Post Paid, you do not need to set this parameter. Not e This parameter is unavailable on the Apsara Stack International site. |
| ISP | String | No | BGP | The line type. Default value: BGP. If you are allowed to use BGP (Single-ISP), valid values are ChinaT elecom, ChinaUnicom, and ChinaMobile. If your services are deployed in China East 1 Finance, this parameter is required and you must set the value to BGP FinanceCloud. _ |
| Netmode | String | No | public | The network type. Set the value to public. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: f alse (default): disables automatic payment. If you select this option, you must go to the Order Center to complete the payment after an order is generated. t rue: enables automatic payment. Payments are automatically completed. This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. Not e This parameter is unavailable on the Apsara Stack International site. |
| PricingCycle | String | No | Month | The billing cycle for the subscription billing method. Valid values: Mont h (default): billed on a monthly basis Year: billed on an annual basis This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. Not e This parameter is unavailable on the Apsara Stack International site. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the EIP. Valid values: PrePaid: subscription Post Paid (default): pay-as-you-go When Inst anceChargeT ype is set to PrePaid, set Int ernet ChargeT ype to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. Not e For the Apsara Stack International site, you must set the value to Post Paid, which specifies the pay-as-you-go billing method. |
| InternetChargeTy pe | String | No | PayByTraffic | The metering method of the EIP. Valid values: PayByBandwidt h (default): pay- by-bandwidth PayByT raf f ic: pay-by-data-transfer When Inst anceChargeT ype is set to PrePaid, you must set Int ernet ChargeT ype to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. |
| ResourceGroupId | String | No | rg- acfmxazffggds** ** | The ID of the resource group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationId | String | eip- 25877c70gddh**** | The ID of the specified EIP. |
| EipAddress | String | 192.0.XX.XX | The allocated EIP. |
| OrderId | Long | 10 | The order number. This parameter is returned only when Inst anceChargeT ype is set to PrePaid. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| ResourceGroupI d | String | rg- acfmxazfdgdg**** | The ID of the resource group. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AllocateEipAddress &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateEipAddressResponse>
  <ResourceGroupId>rg-acfmxazfdgdg****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>192.0.XX.XX</EipAddress>
  <OrderId>10</OrderId>
</AllocateEipAddressResponse>
```

`JSON` format `{`

```json
    "ResourceGroupId": "rg-acfmxazfdgdg****",
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "AllocationId": "eip-25877c70gddh****",
    "EipAddress": "192.0.XX.XX",
    "OrderId": 10
```

`}` Error codes

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth value is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because you do not have sufficient balance within your Apsara Stack account. Add funds to your Apsara Stack account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs has reached the upper limit. We recommend that you use NAT gateways if you want to use more EIPs. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the specified EIP. |

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | InvalidRegion.NotSu pport | The specified region does not support. | The error message returned because the specified region does not support this operation. |
| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |
| 409 | OperationConflict | Request was denied due to conflict with a previos request. | The error message returned because your request is conflicting with another request. Try again later. |

#### 1.5.2 AllocateEipAddressPro

Applies for a specified elastic IP address (EIP). Usage notes After you call this operation, a specified EIP in the Available state in a specified region is allocated. EIPs support only the following transport layer protocols: Internet Control Message Protocol (ICMP), Transmission Control Protocol (TCP), and User Datagram Protocol (UDP). Internet Group Management Protocol (IGMP) and Stream Control Transmission Protocol (SCTP) are not supported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddre ssPro | The operation that you want to perform. Set the value to Allocat eEipAddressPro. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| IpAddress | String | No | 192.0.XX.XX | The EIP for which you want to apply. |
| InstanceId | String | No | eip- 25877c70gddh*** * | The ID of the EIP. Set IpAddress or Inst anceId. If you leave both parameters empty, the system randomly allocates an EIP. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | String | No | 1 | The bandwidth limit of the EIP. Unit: Mbit/s. Valid values: 1 to 200. Default value: 1. |
| Period | Integer | No | 1 | The subscription duration. When PricingCycle is set to Mont h, set Period to a value from 1 t o 9. When PricingCycle is set to Year, set Period to a value from 1 t o 3. This parameter is required when the value of the Inst anceChargeT ype parameter is set to PrePaid. When the value of the Inst anceChargeT ype parameter is set to Post Paid, you do not need to set this parameter. Not e This parameter is unavailable on the Apsara Stack International site. |
| ISP | String | No | BGP | The line type. Default value: BGP. If you are allowed to use BGP (Single-ISP), valid values are ChinaT elecom, ChinaUnicom, and ChinaMobile. If your services are deployed in China East 1 Finance, this parameter is required and you must set the value to BGP FinanceCloud. _ |
| Netmode | String | No | public | The network type. Set the value to public. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: f alse (default): disables automatic payment. If you select this option, you must go to the Order Center to complete the payment after an order is generated. t rue: enables automatic payment. Payments are automatically completed. This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. Not e This parameter is unavailable on the Apsara Stack International site. |
| PricingCycle | String | No | Month | The billing cycle for the subscription billing method. Valid values: Mont h (default): billed on a monthly basis Year: billed on an annual basis This parameter is required when Inst anceChargeT ype is set to PrePaid. This parameter is optional when Inst anceChargeT ype is set to Post Paid. Not e This parameter is unavailable on the Apsara Stack International site. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the EIP. Valid values: PrePaid: subscription Post Paid (default): pay-as-you-go When Inst anceChargeT ype is set to PrePaid, set Int ernet ChargeT ype to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. Not e For the Apsara Stack International site, you must set the value to Post Paid, which specifies the pay-as-you-go billing method. |
| InternetChargeTy pe | String | No | PayByTraffic | The metering method of the EIP. Valid values: PayByBandwidt h (default): pay- by-bandwidth PayByT raf f ic: pay-by-data-transfer When Inst anceChargeT ype is set to PrePaid, you must set Int ernet ChargeT ype to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. |
| ResourceGroupId | String | No | rg- acfmxazffggds** ** | The ID of the resource group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Not e If you do not set this parameter, the system automatically uses Request Id as Client T oken. Request Id may be different for each API request. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationId | String | eip- 25877c70gddh**** | The ID of the specified EIP. |
| EipAddress | String | 192.0.XX.XX | The IP address of the specified EIP. |
| OrderId | Long | 20190000 | The ID of the order. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| ResourceGroupI d | String | rg- resourcegroup**** | The ID of the resource group. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AllocateEipAddressPro &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateEipAddressProResponse>
  <ResourceGroupId>rg-resourcegroup****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>192.0.XX.XX</EipAddress>
  <OrderId>20190000</OrderId>
</AllocateEipAddressProResponse>
```

`JSON` format `{`

```json
    "ResourceGroupId": "rg-resourcegroup****",
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "AllocationId": "eip-25877c70gddh****",
    "EipAddress": "192.0.XX.XX",
    "OrderId": 20190000
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth value is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because you do not have sufficient balance within your Apsara Stack account. Add funds to your Apsara Stack account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs has reached the upper limit. We recommend that you use NAT gateways if you want to use more EIPs. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the specified EIP. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidRegion.NotSu pport | The specified region does not support. | The error message returned because the specified region does not support this operation. |
| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |

#### 1.5.3 AssociateEipAddress

Associates an EIP with a cloud resource that is deployed in the same region. Usage notes When you call this operation, take note of the following limits: You can associate only EIPs in the Available state. One EIP can be associated with only one instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateEipAddr ess | The operation that you want to perform. Set the value to Associat eEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7ujd34 2**** | The ID of the specified EIP. |
| InstanceId | String | Yes | i- 2zebb08phyczdw 32**** | The ID of the instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceType | String | No | EcsInstance | The ID of the cloud resource with which you want to associate the EIP. Valid values: EcsInst ance: an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC) SlbInst ance: a Server Load Balancer (SLB) instance in a VPC Nat : a NAT gateway Net workInt erf ace: a secondary elastic network interface (ENI) |
| InstanceRegionId | String | No | cn-qingdao- env17-d01 | The ID of the region where the instance to be associated with the EIP is deployed. Not e This parameter is required only when the EIP is associated with a shared- bandwidth Global Accelerator (GA) instance. |
| PrivateIpAddress | String | No | 192.168.XX.XX | An IP address in the CIDR block of the vSwitch. If you do not set this parameter, the system allocates a private IP address based on the VPC ID and vSwitch ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C0FD0EED-F90D- 4479-803D- DD62335357E5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateEipAddress &AllocationId=eip-2zeerraiwb7ujd342**** &InstanceId=i-2zebb08phyczdw32**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateEipAddressResponse>
  <RequestId>C0FD0EED-F90D-4479-803D-DD62335357E5</RequestId>
</AssociateEipAddressResponse>
```

`JSON` format `{`

```json
    "RequestId": "C0FD0EED-F90D-4479-803D-DD62335357E5"
```

`}` Error codes

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | InvalidAssociation.D uplicated | Specified instance already is associated. | The error message returned because an EIP or a GA instance is already associated with the specified instance. You must disassociate the EIP or GA instance from the specified instance before you can perform the operation. |
| 400 | OperationDenied | Specified instance is not in VPC. | The error message returned because the specified instance does not exist in the VPC. |
| 400 | InvalidParameter.Mis match | Specified elastic IP address and ECS instance are not in the same region. | The error message returned because the specified EIP and ECS instance do not belong to the same region. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation | The error message returned because the status of the EIP does not support the operation. |
| 404 | InvalidInstanId.NotF ound | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the instance ID is valid. |
| 400 | IncorrectInstanceSta tus | Current instance status does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |
| 400 | InvalidInstanceType. ValueNotSupported | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the parameter is set to an invalid value. |
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because the operation is not supported by EIPs in the default VPC. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatus | The eip binding status invalid. | The error message returned because the EIP is in an invalid state. |
| 400 | BIND INSTANCE HAV _ _ E PORTMAP OR BIN _ _ _ D EIP _ | The instance may have portMap or already bind eip. | The error message returned because a port forwarding rule is configured for the ECS instance. Delete the port forwarding rule and try again. |
| 400 | BIND INSTANCE OWE _ _ NER ERROR _ | Cannot operate the eip. | The error message returned because you are unauthorized to manage the specified EIP. |
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the specified value is valid. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the specified instance does not exist. |

#### 1.5.4 UnassociateEipAddress

Disassociates an elastic IP address (EIP) from an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateEipAd dress | The operation that you want to perform. Sett the value to Unassociat eEipAddress. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0 d**** | The ID of the EIP that you want to disassociate. |
| InstanceId | String | Yes | i- hp3akk9irtd69jad **** | The ID of the instance from which you want to disassociate the EIP. |
| Force | Boolean | No | false | Specifies whether to disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. Valid values: f alse (default): does not disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. t rue: disassociates the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. |
| InstanceType | String | No | EcsInstance | The type of instance from which you want to disassociate the EIP. Valid values: EcsInst ance: an Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC) SlbInst ance: a Server Load Balancer (SLB) instance that is deployed in a VPC Net workInt erf ace: a secondary elastic network interface (ENI) that is deployed in a VPC Nat : a NAT gateway |
| PrivateIpAddress | String | No | 192.168.XX.XX | The private IP address of the ECS instance or the secondary ENI from which you want to disassociate the EIP. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateEipAddress &AllocationId=eip-2zeerraiwb7uj6i0d**** &InstanceId=i-hp3akk9irtd69jad**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateEipAddressResponse>
  <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</UnassociateEipAddressResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the specified value is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because you cannot perform the operation when the specified EIP is in the current state. |
| 400 | InvalidInstanceId.Not Found | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the specified instance is valid. |
| 400 | IncorrectInstanceSta tus | The current status of instance does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |

| eveloper Guid | e·API reference |   | Elastic IP Addres |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidInstanceType. ValueNotSupported | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStatu s | This operation is denied because satus of the specified HaVip is neither Available nor InUse. | The error message returned because you cannot perform the operation when the specified high-availability virtual IP address (HAVIP) is in the Available or InUse state. |
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because the operation is not supported by EIPs in the default VPC. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the parameter is set to an invalid value. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatus | The eip binding status invalid. | The error message returned because the EIP is in an invalid state. |

#### 1.5.5 ModifyEipAddressAttribute

Modifies the name, description, and bandwidth limit of a specified elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyEipAddress Attribute | The operation that you want to perform. Set the value to Modif yEipAddressAt t ribut e. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0 d**** | The ID of the EIP that you want to modify. |

| lastic IP Address |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | String | No | 100 | The bandwidth limit of the EIP. Unit: Mbit/s. Valid values: 1 to 200. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the EIP. |
| Name | String | No | Test123 | The name of the EIP. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. It cannot start with http:// or https:// . |
| Description | String | No | abc | The description of the EIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyEipAddressAttribute &AllocationId=eip-2zeerraiwb7uj6i0d**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyEipAddressAttributeResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</ModifyEipAddressAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InsufficientBalance.Ei p | Your account does not have enough balance. | The error message returned because your Apsara Stack account does not have a sufficient balance. Top up your account and try again. |
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the specified value is valid. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not supported. | The error message returned because the specified bandwidth limit is invalid. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | Forbidden.ChargeTy peIsPrepaid | It’s forbidden to change prepaid EIP’s bandwidth by API. It can be changed on Aliyun web console. | The error message returned because you cannot change the bandwidth limit of a subscription EIP by calling the API operation. You can change the bandwidth limit in the console. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because you cannot perform the operation when the specified EIP is in the current state. |
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found.. | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | The parameter is invalid. | The error message returned because the parameter is set to an invalid value. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

#### 1.5.6 ReleaseEipAddress

Releases a specified elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseEipAddres s | The operation that you want to perform. Set the value to ReleaseEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0 d**** | The ID of the EIP that you want to release. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 748C38F6-9A3D- 482E-83FB- DB6C39C68AEA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ReleaseEipAddress &AllocationId=eip-2zeerraiwb7uj6i0d**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ReleaseEipAddressResponse>
  <RequestId>748C38F6-9A3D-482E-83FB-DB6C39C68AEA</RequestId>
</ReleaseEipAddressResponse>
```

`JSON` format `{`

```json
    "RequestId": "748C38F6-9A3D-482E-83FB-DB6C39C68AEA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the specified value is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because you cannot perform the operation when the specified EIP is in the current state. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | Forbidden.ChargeTy peIsPrepaid | It's forbidden to release a prepaid EIP | The error message returned because you cannot release subscription EIPs. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | TaskConflict.Associa teGlobalAcceleratio nInstance | Operate too frequent. | The error message returned because the number of requests that you send exceeds the upper limit. |

#### 1.5.7 DescribeEipAddresses

Queries elastic IP addresses (EIPs) in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEipAddre sses | The operation that you want to perform. Set the value to DescribeEipAddresses. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| Tag.N.Key | String | No | TestKey | The key of tag N of the EIP that you want to query. Valid values of N: 1 to 20. |
| Tag.N.Value | String | No | TestValue | The value of tag N of the EIP that you want to query. Valid values of N: 1 to 20. |
| IncludeReservatio nData | Boolean | No | true | Specifies whether to return data of orders that have not taken effect. Valid values: f alse (default): does not return information about orders that have not taken effect. t rue: returns data of orders that have not taken effect. |
| Status | String | No | Available | The status of the EIP. Valid values: Associat ing: being associated Unassociat ing: disassociated InUse: allocated Available: available |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EipAddress | String | No | 192.0.XX.XX | The IP address of the EIP that you want to query. You can enter up to 50 IP addresses of EIPs. Separate multiple IP addresses with commas (,). Not e If both the EipAddress and Allocat ionId parameters are set, you can enter up to 50 IP addresses of EIPs in EipAddress, and enter up to 50 IDs of EIPs in Allocat ionId. |
| AllocationId | String | No | eip- 2zeerraiwb7ujxsc d**** | The ID of the EIP that you want to query. You can enter up to 50 IDs of EIPs. Separate multiple IDs with commas (,). Not e If both the EipAddress and Allocat ionId parameters are set, you can enter up to 50 IDs of EIPs in Allocat ionId, and enter up to 50 IP addresses of EIPs in EipAddress. |
| ResourceGroupId | String | No | rg- acfmxazb4pcdvf* *** | The ID of the resource group to which the EIPs belong. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 100. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ISP | String | No | BGP | The line type. Default value: BGP. If you are allowed to use BGP (Single-ISP), valid values are ChinaT elecom, ChinaUnicom, and ChinaMobile. If your services are deployed in China East 1 Finance, this parameter is required and you must set the value to BGP FinanceCloud. _ |
| Filter.1.Key | String | No | CreationStartTim e | The filter key used to query resources. Set the value to Creat ionSt art T ime, which specifies the time when the system started to create the resource. |
| Filter.2.Key | String | No | CreationEndTime | The filter key used to query resources. Set the value to Creat ionEndT ime, which specifies the time when the system completed creating the resource. |
| Filter.1.Value | String | No | 2018-01- 22T09:12Z | The filter value used to query resources. Specify the time in the ISO 8601 standard in YYYY-MM- DDThh:mmZ format. The time must be in UTC. |
| Filter.2.Value | String | No | 2018-01- 22T09:15Z | The filter value used to query resources. Specify the time in the ISO 8601 standard in YYYY-MM- DDThh:mmZ format. The time must be in UTC. |
| LockReason | String | No | financial | The reason why the EIP is locked. Valid values: f inancial: The EIP is locked due to overdue payments. securit y: The EIP is locked for security reasons. |

|   | DDThh:mmZ |
|---|---|

|   | DDThh:mmZ |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AssociatedInstan ceType | String | No | EcsInstance | The type of the cloud resource with which you want to associate the EIP. Valid values: EcsInst ance (default): an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC) SlbInst ance: a Server Load Balancer (SLB) instance in a VPC Nat : a NAT gateway Net workInt erf ace: a secondary elastic network interface (ENI) You can associate only one EIP with each ECS instance or SLB instance. You can associate multiple EIPs with each NAT gateway. The number of EIPs that can be associated with a secondary ENI depends on the EIP association mode. |
| AssociatedInstan ceId | String | No | i- 2zebb08phyccdvf **** | The ID of the cloud resource with which the EIP is associated. |
| ChargeType | String | No | None | The billing method of the EIP. Valid values: Post Paid: pay-as-you-go PrePaid: subscription |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipAddresses | Array of EipAddress |   | The details about the EIP. |
| EipAddress |   |   |   |
| AllocationId | String | eip- 2zeerraiwb7ujcdvf** ** | The ID of the EIP. |
| AllocationTime | String | 2019-04- 23T01:37:38Z | The time when the EIP was created. |
| AvailableRegion s | List | cn-qingdao-env17- d01 | The ID of the region to which the EIP belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Bandwidth | String | 5 | The bandwidth limit of the EIP. Unit: Mbit/s. |
| BandwidthPack ageId | String | cbwp- bp1ego3i4j07ccdvf* *** | The ID of the EIP bandwidth plan. |
| BandwidthPack ageType | String | CommonBandwidth Package | The type of the bandwidth plan. Only CommonBandwidt hPackage (EIP Bandwidth Plan) is returned. |
| ChargeType | String | PostPaid | The billing method of the EIP. Valid values: PrePaid: subscription Post Paid: pay-as-you-go |
| Descritpion | String | abc | The description of the EIP. |
| EipBandwidth | String | 101 | The bandwidth limit of the EIP when it is not associated with an EIP bandwidth plan. |
| ExpiredTime | String | 2019-04-29T02:00Z | The expiration date. The time follows the ISO 8601 standard and is displayed in UTC. Format: YYYY-MM-ddTHH:mmZ . |
| HDMonitorStatu s | String | false | Indicates whether fine-grained monitoring is enabled for the EIP. Valid values: f alse: no t rue: yes |
| HasReservation Data | String | false | Indicates whether renewal data is included. This parameter returns t rue only when the IncludeReservat ionDat a parameter is set to t rue and some orders have not taken effect. |
| ISP | String | BGP | The line type. If this parameter is not set, BGP is returned by default. If you are allowed to use BGP (Single-ISP), valid values are ChinaT elecom, ChinaUnicom, and ChinaMobile. If your services are deployed in China East 1 Finance, BGP FinanceCloud is returned. _ |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | i- bp15zckdt37cdvf*** * | The ID of the instance with which the EIP is associated. |
| InstanceRegionI d | String | cn-qingdao-env17- d01 | The region ID of the associated resource. |
| InstanceType | String | EcsInstance | The type of the instance associated with the EIP. Valid values: EcsInst ance: an ECS instance in a VPC SlbInst ance: an SLB instance in a VPC Nat : a NAT gateway Net workInt erf ace: a secondary ENI |
| InternetCharge Type | String | PayByBandwidth | The metering method of the EIP. Valid values: PayByBandwidt h: pay-by-bandwidth PayByT raf f ic: pay-by-data-transfer |
| IpAddress | String | 192.0.XX.XX | The IP address of the EIP. |
| Mode | String | NAT | The association mode. Valid values: NAT : NAT mode MULT I BINDED: multi-EIP-to-ENI mode _ BINDED: cut-through mode This parameter is returned only when Inst anceT ype is set to Net workInt erf ace. |
| Name | String | test | The name of the EIP. |
| OperationLocks | Array of LockReason |   | The details about the locked EIP. |
| LockReason |   |   |   |
| LockReason | String | financial | The reason why the EIP is locked. Valid values: f inancial: The EIP is locked due to overdue payments. securit y: The EIP is locked for security reasons. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PrivateIpAddres s | String | 192.168.XX.XX | An IP address in the CIDR block of the vSwitch. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region to which the EIP belongs. |
| ReservationActi veTime | String | 2019-03- 11T16:00:00Z | The time when the renewal takes effect. |
| ReservationBan dwidth | String | 12 | The bandwidth after the renewal takes effect. |
| ReservationInte rnetChargeTyp e | String | PayByBandwidth | The metering method of the renewal. Valid values: PayByBandwidt h: pay-by-bandwidth PayByT raf f ic: pay-by-data-transfer |
| ReservationOrd erType | String | RENEWCHANGE | The type of the renewal order. Valid values: RENEWCHANGE: renewal with upgrade or downgrade T EMP UPGRADE: temporary upgrade _ UPGRADE: upgrade |
| ResourceGroupI d | String | rg-acfmxazcdxs**** | The ID of the resource group. |
| Status | String | Associating | The status of the EIP. Valid values: Associat ing: being associated Unassociat ing: being disassociated InUse: allocated Available: available |
| Tags | Array of Tag |   | The tags used to query resources. |
| Tag |   |   |   |
| Key | String | testX | The filter key used to query resources. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Value | String | testY | The filter value used to query resources. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. Default value: 10. Valid values: 1 to 50. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| TotalCount | Integer | 10 | The number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEipAddresses &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeEipAddressesResponse>
  <TotalCount>10</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <EipAddresses>
        <HDMonitorStatus>false</HDMonitorStatus>
        <PrivateIpAddress>192.168.XX.XX</PrivateIpAddress>
        <ResourceGroupId>rg-acfmxazcdxs****</ResourceGroupId>
        <AllocationId>eip-2zeerraiwb7ujcdvf****</AllocationId>
        <Name>test</Name>
        <ReservationOrderType>RENEWCHANGE</ReservationOrderType>
        <InstanceRegionId>cn-qingdao-env17-d01</InstanceRegionId>
        <ExpiredTime>2019-04-29T02:00Z</ExpiredTime>
        <Bandwidth>5</Bandwidth>
        <BandwidthPackageId>cbwp-bp1ego3i4j07ccdvf****</BandwidthPackageId>
        <ReservationActiveTime>2019-03-11T16:00:00Z</ReservationActiveTime>
        <InstanceType>EcsInstance</InstanceType>
        <ReservationBandwidth>12</ReservationBandwidth>
        <Status>Associating</Status>
        <InstanceId>i-bp15zckdt37cdvf****</InstanceId>
        <Mode>NAT</Mode>
        <ISP>BGP</ISP>
        <HasReservationData>false</HasReservationData>
        <BandwidthPackageType>CommonBandwidthPackage</BandwidthPackageType>
        <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
        <InternetChargeType>PayByBandwidth</InternetChargeType>
        <AllocationTime>2019-04-23T01:37:38Z</AllocationTime>
        <Descritpion>abc</Descritpion>
        <EipBandwidth>101</EipBandwidth>
        <ChargeType>PostPaid</ChargeType>
        <IpAddress>192.0.XX.XX</IpAddress>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <OperationLocks>
              <LockReason>financial</LockReason>
        </OperationLocks>
        <Tags>
              <Value>testY</Value>
              <Key>testX</Key>
        </Tags>
        <AvailableRegions>cn-qingdao-env17-d01</AvailableRegions>
  </EipAddresses>
  <PageNumber>1</PageNumber>
</DescribeEipAddressesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "EipAddresses": {
        "HDMonitorStatus": false,
        "PrivateIpAddress": "192.168.XX.XX",
        "ResourceGroupId": "rg-acfmxazcdxs****",
        "AllocationId": "eip-2zeerraiwb7ujcdvf****",
        "Name": "test",
        "ReservationOrderType": "RENEWCHANGE",
        "InstanceRegionId": "cn-qingdao-env17-d01",
        "ExpiredTime": "2019-04-29T02:00Z",
        "Bandwidth": 5,
        "BandwidthPackageId": "cbwp-bp1ego3i4j07ccdvf****",
        "ReservationActiveTime": "2019-03-11T16:00:00Z",
        "InstanceType": "EcsInstance",
        "ReservationBandwidth": 12,
        "Status": "Associating",
        "InstanceId": "i-bp15zckdt37cdvf****",
        "Mode": "NAT",
        "ISP": "BGP",
        "HasReservationData": false,
        "BandwidthPackageType": "CommonBandwidthPackage",
        "ReservationInternetChargeType": "PayByBandwidth",
        "InternetChargeType": "PayByBandwidth",
        "AllocationTime": "2019-04-23T01:37:38Z",
        "Descritpion": "abc",
        "EipBandwidth": 101,
        "ChargeType": "PostPaid",
        "IpAddress": "192.0.XX.XX",
        "RegionId": "cn-qingdao-env17-d01",
        "OperationLocks": {
            "LockReason": "financial"
```

`},`

```json
        "Tags": {
            "Value": "testY",
            "Key": "testX"
```

`},`

```json
        "AvailableRegions": "cn-qingdao-env17-d01"
```

`},`

```json
    "PageNumber": 1
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

| lastic IP Addre | ss |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.NotF ound |   | The error message returned because the specified filter key is invalid. |
| 404 | InvalidFilterValue |   | The error message returned because the specified filter value is invalid. |
| 404 | InvalidLockReason.N otFound | The specified LockReason is not found | The error message returned because the reason why the EIP is locked is unknown. |
| 400 | InvalidIAssociatedIns tanceType.ValueNot Supported | The specified value of AssociatedInstanceType is not supported. | The error message returned because AssociatedInstanceType is set to an invalid value. Check whether the value is valid. |
| 400 | InvalidChargeType.V alueNotSupported | The specified ChargeType is not supported. | The error message returned because the specified billing method is not supported. Set a supported billing method. |
| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |

#### 1.5.8 DescribeEipMonitorData

Queries the monitoring data of an elastic IP address (EIP). You can query monitoring data within the last 30 days and specify up to 400 data points in each request. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEipMonit orData | The operation that you want to perform. Set the value to DescribeEipMonit orDat a |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6id cfv**** | The ID of the EIP. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EndTime | String | Yes | 2020-01- 05T03:05:10Z | The end of the time range to query. The time must be in UTC. Specify the time in the ISO 8601 standard in YYYY-MM-DDThh:mm:ssZ format. For example, 2013-01- 10T12:00:00Z specifies 20:00:00 (UTC+8) on January 10, 2013. |
| StartTime | String | Yes | 2020-01- 05T01:05:05Z | The beginning of the time range to query. The time must be in UTC. Specify the time in the ISO 8601 standard in YYYY-MM-DDThh:mm:ssZ format. For example, 2013-01- 10T12:00:00Z specifies 20:00:00 (UTC+8) on January 10, 2013. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| Period | Integer | No | 60 | The duration of each monitoring data entry. Unit: seconds. Valid values: 60 (default), 300, 900, and 3600. If the value of (EndT ime - St art T ime)/Period is greater than 200, a maximum of 200 monitoring data entries are returned at a time. If the value of (EndT ime - St art T ime)/Period is less than or equal to 200, only the monitoring data collected between the start time and end time is returned. |

|   | 10T12:00:00Z |   |
|---|---|---|

|   | 10T12:00:00Z |   |
|---|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipMonitorData s | Array of EipMonitorData |   | The detailed information about the monitoring data of the EIP. |
| EipMonitorData |   |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|

| EipBandwidth | Integer | 10 | The average bandwidth value. This value is equal to EipFlow/Period. Unit: Byte/s. The default value of Period is 60. Unit: seconds. |   |   |
|---|---|---|---|---|---|
| EipFlow | Integer | 465 | The sum of inbound and outbound traffic. |   |   |
| EipPackets | Integer | 3434 | The number of packets. |   |   |
| EipRX | Integer | 122 | The inbound traffic. Unit: bytes. |   |   |
| EipTX | Integer | 343 | The outbound traffic. Unit: bytes. |   |   |
| TimeStamp | String | 2020-01- 21T09:50:23Z | The time when the monitoring information was queried. Specify the time in the ISO8601 standard. Example: 2020-01- 21T09:50:23Z . |   |   |
|   |   |   |   | 2020-01- |   |
| RequestId | String | C8B26B44-0189- 443E-9816- D951F59623A9 | The ID of the request. |   |   |

|   | 21T09:50:23Z |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEipMonitorData &AllocationId=eip-2zeerraiwb7uj6idcfv**** &EndTime=2020-01-05T03:05:10Z &StartTime=2020-01-05T01:05:05Z &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeEipMonitorDataResponse>
  <RequestId>C8B26B44-0189-443E-9816-D951F59623A9</RequestId>
  <EipMonitorDatas>
        <EipPackets>3434</EipPackets>
        <EipBandwidth>10</EipBandwidth>
        <EipFlow>465</EipFlow>
        <EipTX>343</EipTX>
        <TimeStamp>2020-01-21T09:50:23Z</TimeStamp>
        <EipRX>122</EipRX>
  </EipMonitorDatas>
</DescribeEipMonitorDataResponse>
```

`JSON` format `{`

```json
    "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9",
    "EipMonitorDatas": {
        "EipPackets": 3434,
        "EipBandwidth": 10,
        "EipFlow": 465,
        "EipTX": 343,
        "TimeStamp": "2020-01-21T09:50:23Z",
        "EipRX": 122
```

`}` `}` Error codes

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 404 | InvalidIpInstanceId.N otFound | The specified Eip InstanceId does not exist in our records. | The error message returned because the specified EIP does not exist. |
| 404 | InvalidInstanceId.Not Found | The InstanceId provided does not exist in our records. | The error message returned because the specified Elastic Compute Service (ECS) instance does not exist in the virtual private cloud (VPC). |
| 400 | InvalidStartTime.Mal formed | The specified parameter "StartTime" is not valid. | The error message returned because the value of the StartTime parameter is invalid. |
| 400 | InvalidEndTime.Malf ormed | The specified parameter "EndTime" is not valid. | The error message returned because the value of the EndTime parameter is invalid. |
| 400 | InvalidPeriod.ValueN otSupported | The specified parameter "Period" is not valid. | The error message returned because the value of the Period parameter is invalid. |

| lastic IP Addre | ss |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | InvalidStartTime.To oEarly | The specified parameter "StartTime" is too early. | The error message returned because the value of the StartTime parameter is invalid. |
| 400 | InvalidAllocationId.N otFound | Specified allocation id is not found. | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | OperationDenied.To oManyDataQueried | Specified operation is denied as too many data to return. | The error message returned because the number of data entries to be returned has reached the upper limit. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

#### 1.5.9 MoveResourceGroup

Moves a resource to a different resource group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MoveResourceGro up | The operation that you want to perform. Set the value to MoveResourceGroup. |
| NewResourceGro upId | String | Yes | rg- acfm3peow3k*** * | The ID of the resource group to which the cloud resource is to be moved. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the cloud resource. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId | String | Yes | vpc- hp31psbg8ec302 3s6**** | The ID of the cloud resource that you want to move. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ResourceType | String | Yes | vpc | The type of the resource. Valid values: vpc: a virtual private cloud (VPC) eip: an elastic IP address (EIP) bandwidt hpackage: an EIP bandwidth plan |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F84A05B3-7275- 4C8B-8AEE- 9088C639C271 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=MoveResourceGroup &NewResourceGroupId=rg-acfm3peow3k**** &RegionId=cn-qingdao-env66-d01 &ResourceId=vpc-hp31psbg8ec3023s6**** &ResourceType=vpc &<Common request parameters>
```

Sample success responses `XML` format

```xml
<MoveResourceGroupResponse>
  <RequestId>F84A05B3-7275-4C8B-8AEE-9088C639C271</RequestId>
</MoveResourceGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "F84A05B3-7275-4C8B-8AEE-9088C639C271"
```

`}` Error codes

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |

#### 1.5.10 DescribeHighDefinitionMonitorLogAttribute

Queries configurations about the fine-grained monitoring feature of an elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHighDefi nitionMonitorLog Attribute | The operation that you want to perform. Set the value to DescribeHighDef init ionMonit orLog At t ribut e. |
| InstanceId | String | Yes | eip- wz9fi6qboho9fw gx7**** | The ID of the instance whose fine- grained monitoring configurations you want to query. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceType | String | No | EIP | The type of the instance. Set the value to EIP. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | eip- wz9fi6qboho9fwgx 7**** | The ID of the instance whose fine-grained monitoring configurations you want to query. |
| InstanceType | String | EIP | The type of the instance. Only EIP is returned. |
| LogProject | String | hdmonitor-cn- qingdao- 1658206966225390 | The name of the project of Log Service. |
| LogStore | String | hdmonitor | The name of the Logstore of Log Service. |

| Developer Guide·AP | I reference |   | Elastic IP Addres |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |
| Success | String | true | Indicates whether the operation is performed. Valid values: t rue: yes f alse: no |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHighDefinitionMonitorLogAttribute &InstanceId=eip-wz9fi6qboho9fwgx7**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHighDefinitionMonitorLogAttributeResponse>
  <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
  <LogStore>hdmonitor</LogStore>
  <InstanceId>eip-wz9fi6qboho9fwgx7****</InstanceId>
  <InstanceType>EIP</InstanceType>
  <LogProject>hdmonitor-cn-qingdao-1658206966225390</LogProject>
  <Success>true</Success>
</DescribeHighDefinitionMonitorLogAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "54B48E3D-DF70-471B-AA93-08E683A1B457",
    "LogStore": "hdmonitor",
    "InstanceId": "eip-wz9fi6qboho9fwgx7****",
    "InstanceType": "EIP",
    "LogProject": "hdmonitor-cn-qingdao-1658206966225390",
    "Success": true
```

`}` using ASAPI

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

This topic describes how to obtain and use the Apsara Stack SDK for Java. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use the Apsara Stack SDK for Java. For more information about how to obtain and view your AccessKey pair in the Apsara Stack Cloud Management (ASCM) console, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. using ASAPI The Apsara Stack SDK for Java supports JDK 1.6 and later. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use the Apsara Stack SDK for Java You can call API operations on ASAPI by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests using ASAPI

```java
public class DescribeEipAddresses {
    public static void main(String[] args) {
        // Obtain the endpoint of ASAPI.
        String endpoint = "http://xxx/asapi/v3";
    // Set request parameters.
    Map<String, String> parameters = new HashMap<String, String>();
    // Set parameters for the product.
    parameters.put("Product", "vpc");            // The product name must be the same as
the name displayed in the corresponding API directory.
    parameters.put("Action", "DescribeEipAddresses");          // The API name must be in
the same case as that in the API directory.
    parameters.put("Version", "2016-04-28");      // The API version.
    // Set authorization-related parameters.
    parameters.put("AccessKeyId", "<your-access-key-id>");          // The AccessKey ID o
f the authorized account.
    parameters.put("AccessKeySecret", "<your-access-key-secret>");  // The AccessKey secr
et of the authorized account.
    // Set business parameters.
    parameters.put("username", "<your-username>");                  // The username used
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

This topic describes how to obtain and use the Apsara Stack SDK for Node.js. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use the Apsara Stack SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install the SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on eggjs, you must configure mocha.opts.
using ASAPI

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use the Apsara Stack SDK for Node.js The following example shows how to use the Apsara Stack SDK for Node.js:
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
3. Initiate the API request and handle the response or exceptions.

```
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set parameters. let params = {
    Action: 'DescribeEipAddresses',
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

### 2.10 Use the POP SDK to call API operations on ASAPI (Optional)

operations on ASAPI (Optional) If an application used the POP SDK to call cloud products, you must switch the gateway to ASAPI. Procedure
1. Switch the gateway to ASAPI and add common parameters to the request header.
using ASAPI
2. Add the Product Name field to the request header.
Examples The following example demonstrates how to use POP SDK to call the EIP API:

```java
try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessK
eySecret);
    // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "vpc", "<ASAPI gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
    DescribeEipAddressesRequest request = new DescribeEipAddressesRequest();
    request.setSysRegionId(regionId); // Or setRegionId(regionId)
    // Set common parameters based on the information about the current user.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    DescribeEipAddressesResponse result = (DescribeEipAddressesResponse) acsClient.getAcsRe
sponse(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```

`}`
