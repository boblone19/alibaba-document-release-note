---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 IPv6 Gateway Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 53
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 IPv6 Gateway Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20IPv6%20Gateway%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 IPv6 Gateway Developer Guide 20220928

## Table of Contents

- 1 List of operations by function
- 2 Make API requests
  - 2.1 Request syntax
  - 2.2 API authorization
  - 2.3 Signature method
- 3 RAM authentication
- 4 Common parameters
- 5 IPv6 Gateway
  - 5.1 CreateIpv6Gateway
  - 5.2 DescribeIpv6Gateways
  - 5.3 DescribeIpv6GatewayAttribute
  - 5.4 ModifyIpv6GatewayAttribute
  - 5.5 ModifyIpv6GatewaySpec
  - 5.6 DeleteIpv6Gateway
  - 5.7 CreateIpv6EgressOnlyRule
  - 5.8 DescribeIpv6EgressOnlyRules
  - 5.9 DeleteIpv6EgressOnlyRule
  - 5.10 AllocateIpv6InternetBandwidth
  - 5.11 ModifyIpv6InternetBandwidth
  - 5.12 DeleteIpv6InternetBandwidth
  - 5.13 DescribeIpv6Addresses
  - 5.14 ModifyIpv6AddressAttribute
- 6 Make SDK calls by using Asapi
  - 6.1 Overview
  - 6.2 Log on to the API Tool console
  - 6.3 View the information about API operations
  - 6.4 Obtain the endpoint of ASAPI
  - 6.5 Obtain the core package for ASAPI
  - 6.6 Obtain an AccessKey pair
  - 6.7 Query the region ID
  - 6.8 SDK for Java
  - 6.9 SDK for Node.js
  - 6.10. (Optional) Use POP SDK to call Asapi

by function

## 1 List of operations by function

The following table lists API operations available for use in IPv6 Gateway.

| API | Description |
|---|---|
| CreateIpv6Gateway | Creates an IPv6 gateway. |
| DescribeIpv6Gateways | Queries IPv6 gateways in a specified region. |
| DescribeIpv6GatewayAttribute | Queries the detailed information of an IPV6 gateway. |
| ModifyIpv6GatewayAttribute | Modifies the information of an IPv6 gateway. |
| ModifyIpv6GatewaySpec | Modifies the edition of an IPv6 gateway. |
| DeleteIpv6Gateway | Deletes an IPv6 gateway. |
| DescribeIpv6EgressOnlyRules | Queries one or more egress-only rules. |
| CreateIpv6EgressOnlyRule | Creates an egress-only rule for an IPv6 address. |
| DeleteIpv6EgressOnlyRule | Deletes an egress-only rule. |
| AllocateIpv6InternetBandwidth | Purchases an Internet bandwidth plan for an IPv6 address. |
| ModifyIpv6InternetBandwidth | Modifies the Internet bandwidth plan of an IPv6 address. |
| DeleteIpv6InternetBandwidth | Deletes the Internet bandwidth plan from an IPv6 IP address. |
| DescribeIpv6Addresses | Queries one or more IPv6 addresses. |
| ModifyIpv6AddressAttribute | Modifies the name and description of an IPv6 address. |

## 2 Make API requests

### 2.1 Request syntax

To send an IPv6 Gateway API request, you must send an HTTP GET request to the IPv6 Gateway endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. The request and response are encoded in UTF-8. IPv6 Gateway API operations use the RPC protocol. You can call IPv6 Gateway API operations by sending HTTP GET requests. Use the following request syntax:

```
http://Endpoint/?Action=xx&Parameters
```

where Endpoint: The endpoint of the IPv6 Gateway API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Stack Operations console. For more information, see Obtain the endpoint of Asapi. Action: the name of the operation being performed. For example, to query IPv6 gateways in a specified region, you must set the Action parameter to DescribeIpv6Gateways. Version: the version of the API that you must use. The current IPv6 Gateway API version is 2016-04-28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters are used for all IPv6 Gateway API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the DescribeIpv6Gateways operation in IPv6 Gateway. Not e The examples in this topic have been formatted for ease of reading.

```
https://vpc.example.com/?Action=DescribeIpv6Gateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

### 2.2 API authorization

To ensure the security of your account, we recommend that you call IPv6 Gateway API operations as a RAM user. To call the IPv6 Gateway API as a RAM user, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the IPv6 Gateway resources and API operations that allow the authorization, see RAM authentication.

### 2.3 Signature method

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. IPv6 Gateway implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to the IPv6 Gateway API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

Take DescribeIpv6Gateways as an example. If the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the following code shows the original request URL:

```
http://vpc.example.com/?Action=DescribeIpv6Gateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeIpv6Gateways&Format%3DXML&SignatureMethod %3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1 .0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2016-04-28
```

2. Calculate the HMAC value of the string-to-sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter.

```
http://vpc.example.com/?Action=DescribeIpv6Gateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

n

## 3 RAM authentication

Before you call an IPv6 Gateway operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource. IPv6 Gateway resources that allow authorized access The following table lists the IPv6 Gateway resources that allow authorized access and their ARNs.

| Resource type | ARN |
|---|---|
| IPv6 gateways | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayid |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/* |
|   | acs:vpc:*:$accountid:ipv6gateway/* |
| IPv6 Internet bandwidth | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6instanceid |
|   | acs:vpc:$regionid:$accountid:ipv6bandwidth/* |
|   | acs:vpc:*:$accountid:ipv6bandwidth/* |
| General resources | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accoutid`/`vrouterid are IDs of the specific resources, and `*` represents all resources. IPv6 Gateway API operations that allow authorized access The following table lists the IPv6 Gateway API operations that allow authorized access and their ARNs.

| API | ARN |   |
|---|---|---|
| CreateIpv6Gateway | acs:vpc:$regionid:$accountid:ipv6gateway/* |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |
| DeleteIpv6Gateway | d |   |
| DescribeIpv6Gateways | acs:vpc:$regionid:$accountid:ipv6gateway/* |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |
|   | d |   |
| AllocateIpv6InternetBandwidth | acs:vpc:$regionid:$accountid:ipv6bandwidth/* |   |
| CreateIpv6EgressOnlyRule | acs:vpc:$regionid:$accountid:ipv6gateway/* |   |
| DeleteIpv6EgressOnlyRule | acs:vpc:$regionid:$accountid:ipv6gateway/$ruleid |   |

| eveloper Guide·RAM authenticatio | IPv6 Gatewa |
|---|---|

n

| API | ARN |   |   |
|---|---|---|---|
|   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6bandwi dthid |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6bandwi |   |
| DeleteIpv6InternetBandwidth | dthid |   |   |
| DescribeIpv6Addresses | acs:vpc:$regionid:$accountid:vpc/* |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| DescribeIpv6EgressOnlyRules | d |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| DescribeIpv6GatewayAttribute | d |   |   |
| ModifyIpv6AddressAttribute | acs:vpc:$regionid:$accountid:vpc/$ipv6instanceid |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| ModifyIpv6GatewayAttribute | d |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi d |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6gateway/$ipv6gatewayi |   |
| ModifyIpv6GatewaySpec | d |   |   |
|   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6instan ceid |   |   |
|   |   | acs:vpc:$regionid:$accountid:ipv6bandwidth/$ipv6instan |   |
| ModifyIpv6InternetBandwidth | ceid |   |   |

ers

## 4 Common parameters

This topic describes common parameters, including common request parameters and common response parameters. Common parameters are required in all API operations, regardless of the operation being called. Common request parameters Common request parameters must be included in all IPv6 Gateway API requests. Common request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: JSON. |
| Version | String | Yes | The version number of the API. Format: YYYY-MM-DD . Set the value to 2016-04-28 |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Apsara Stack. |
| Signature | String | Yes | The signature string in the current request. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1 |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time must be in UTC. For example, 2013-01-10T12:00:00Z. |
| SignatureVersio n | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0 |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |

Examples ers

```
http://vpc.example.com/?Action=DescribeIpv6Gateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
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

## 5 IPv6 Gateway

### 5.1 CreateIpv6Gateway

You can call this operation to create an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Gatew ay | The operation that you want to perform. Set the value to Creat eIpv6Gat eway. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- 123456defrde**** | The ID of the VPC for which you want to create the IPv6 gateway. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | ipv6gatewayforV PC1 | The description of the IPv6 gateway. The description must be 2 to 256 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with _ a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | ipv6GW | The name of the IPv6 gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Spec | String | No | Small | The specification of the IPv6 gateway. Valid values: Small (default): free edition Medium: enterprise edition Large: enhanced enterprise edition |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6GatewayId | String | ipv6gw- hp3y0l3ln89j8bgnh** ** | The ID of the IPv6 gateway. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=CreateIpv6Gateway &RegionId=cn-huhehaote &VpcId=vpc-hp3x04of74a6aqsw**** &Common request parameters
```

Sample responses `XML` format

```xml
<CreateIpv6GatewayResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
      <Ipv6GatewayId>vipv6gw-hp3y0l3ln89j8qsw****</Ipv6GatewayId>
</CreateIpv6GatewayResponse>
```

`JSON` format `{`

```json
 "RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
 "Ipv6GatewayId":"ipv6gw-hp3y0l3ln89j8qsw****"
```

### 5.2 DescribeIpv6Gateways

You can call this operation to query one or more IPv6 gateways. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gate ways | The operation that you want to perform. Set the value to DescribeIpv6Gat eways. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6GatewayId | String | No | ipv6gw- 123456xscd**** | The ID of the IPv6 gateway. |
| Name | String | No | ipv6GW | The name of the IPv6 gateway. |
| PageNumber | Integer | No | 1 | The number of the returned page. |
| PageSize | Integer | No | 10 | The number of entries returned per page. |
| VpcId | String | No | vpc- 123456xscd**** | The ID of the VPC to which the IPv6 gateway belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Gateways |   |   | The details of the IPv6 gateways |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments |
| CreationTime | String | 2018-12- 20T14:51:23Z | The time when the IPv6 gateway was created. |
| Description | String | descriptionforIPv6G W | The description of the IPv6 gateway. |
| ExpiredTime | String | 2018-12- 20T14:51:23Z | The time when the IPv6 gateway expires. |
| InstanceCharge Type | String | PostPaid | The billing method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw- hp3rwmtmfhgisxscd **** | The ID of the IPv6 gateway. |
| Name | String | name | The name of the IPv6 gateway. |
| RegionId | String | cn-huhehaote | The region ID of the IPv6 gateway. |
| Spec | String | Small | The specification of the IPv6 gateway. |
| Status | String | Available | The running status of the IPv6 gateway. |
| VpcId | String | vpc-123456xscd**** | The ID of the VPC to which the IPv6 gateway belongs. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 19 | The number of entries returned per page. |
| RequestId | String | E3A06196-3E7C- 490D-8F39- CB4B5A0CE8AD | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeIpv6Gateways &RegionId=cn-huhehaote &Common request parameters
```

Sample responses `XML` format

```xml
<DescribeIpv6GatewaysResponse>
   <PageNumber>1</PageNumber>
   <Ipv6Gateways>
      <Ipv6Gateway>
         <Name></Name>
         <CreationTime>2018-12-20T14:51:23Z</CreationTime>
         <Status>Available</Status>
         <Description></Description>
         <BusinessStatus>Normal</BusinessStatus>
         <Spec>Medium</Spec>
         <RegionId>cn-huhehaote</RegionId>
         <InstanceChargeType>PostPaid</InstanceChargeType>
         <ExpiredTime></ExpiredTime>
         <VpcId>vpc-hp3ag7ydchedxxscd****</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33of4uz4k4kxscd****</Ipv6GatewayId>
      </Ipv6Gateway>
      <Ipv6Gateway>
         <CreationTime>2018-12-05T09:21:35Z</CreationTime>
         <Name>IPv6 gateway</Name>
         <Status>Available</Status>
         <Description></Description>
         <BusinessStatus>Normal</BusinessStatus>
         <Spec>Medium</Spec>
         <RegionId>cn-huhehaote</RegionId>
         <InstanceChargeType>PostPaid</InstanceChargeType>
         <ExpiredTime></ExpiredTime>
         <VpcId>vpc-hp3kzilwd9yflxscd****</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33p10bdbt77xscd****</Ipv6GatewayId>
      </Ipv6Gateway>
   </Ipv6Gateways>
   <TotalCount>2</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD</RequestId>
</DescribeIpv6GatewaysResponse>
```

`JSON` format `{`

```json
 "Ipv6Gateways":{
  "Ipv6Gateway":[
```

`{`

```json
    "CreationTime":"2018-12-20T14:51:23Z",
    "Name":"",
    "Status":"Available",
    "Description":"",
    "Spec":"Medium",
    "BusinessStatus":"Normal",
    "RegionId":"cn-huhehaote",
    "InstanceChargeType":"PostPaid",
    "ExpiredTime":"",
    "VpcId":"vpc-hp3ag7ydchedxscd****",
    "Ipv6GatewayId":"ipv6gw-hp33of4uz4k4kxscd****"
```

`},` `{`

```json
    "Name":"IPv6 gateway",
    "CreationTime":"2018-12-05T09:21:35Z",
    "Status":"Available",
    "Description":"",
    "Spec":"Medium",
    "BusinessStatus":"Normal",
    "RegionId":"cn-huhehaote",
    "InstanceChargeType":"PostPaid",
    "ExpiredTime":"",
    "VpcId":"vpc-hp3kzilwd9yflxscd****",
    "Ipv6GatewayId":"ipv6gw-hp33p10bdbt77xscd****"
```

`]` `},`

```json
 "PageNumber":1,
 "TotalCount":2,
 "PageSize":10,
 "RequestId":"E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD"
```

### 5.3 DescribeIpv6GatewayAttribute

You can call this operation to query the details of an IPV6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gate wayAttribute | The operation that you want to perform. Set the value to DescribeIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456vfbg**** | The ID of the IPv6 gateway to query. |

| Pv6 Gateway |   |   |   | Developer Guide·IPv6 Gatewa |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments Securit yLocked: locked due to security reasons |
| CreationTime | String | 2018-12- 05T09:21:35Z | The time when the IPv6 gateway was created. |
| Description | String | test | The description of the IPv6 gateway. |
| ExpiredTime | String | 2018-12- 05T09:21:35Z | The time when the IPv6 gateway expires. |
| Ipv6GatewayId | String | ipv6gw- 123456xxxxxxxx | The instance ID of the IPv6 gateway. |
| Name | String | test | The name of the IPv6 gateway. |
| RegionId | String | cn-huhehaote | The region ID of the IPv6 gateway. |
| RequestId | String | ipv6gw- hp33p10bdbt77vfb g**** | The ID of the request. |
| Spec | String | Medium | The specification of the IPv6 gateway. |
| Status | String | Available | The status of the IPv6 gateway. |
| VpcId | String | vpc-123456vfbg**** | The ID of the VPC instance to which the IPv6 gateway belongs. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-hp33p10bdbt77vfbg**** &RegionId=cn-huhehaote &Common request parameters
```

Sample responses `XML` format

```xml
<DescribeIpv6GatewayAttributeResponse>
   <Name>ipv6gateway</Name>
   <CreationTime>2018-12-05T09:21:35Z</CreationTime>
   <Status>Available</Status>
   <Description></Description>
   <BusinessStatus>Normal</BusinessStatus>
   <Spec>Medium</Spec>
   <RequestId>F4517005-A716-40EB-8B80-F6AF8508B25F</RequestId>
   <RegionId>cn-huhehaote</RegionId>
   <ExpiredTime></ExpiredTime>
   <VpcId>vpc-hp3kzilwd9yflvfbg****</VpcId>
   <Ipv6GatewayId>ipv6gw-hp33p10bdbt77vfbg****</Ipv6GatewayId>
</DescribeIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
 "CreationTime":"2018-12-05T09:21:35Z",
 "Name":"ipv6gateway",
 "Status":"Available",
 "Description":"",
 "Spec":"Medium",
 "BusinessStatus":"Normal",
 "RegionId":"cn-huhehaote",
 "RequestId":"F4517005-A716-40EB-8B80-F6AF8508B25F",
 "ExpiredTime":"",
 "VpcId":"vpc-hp3kzilwd9yflvfbg****",
 "Ipv6GatewayId":"ipv6gw-hp33p10bdbt77vfbg****"
```

### 5.4 ModifyIpv6GatewayAttribute

You can call this operation to modify the name and description of an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gatew ayAttribute | The operation that you want to perform. Set the value to Modif yIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp39kh1ya51yzp 2lu**** | The ID of the IPv6 gateway to be modified. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Description | String | No | ipv6description | The description of the IPv6 gateway. |
| Name | String | No | ipv6name | The name of the IPv6 gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyIpv6GatewayAttribute &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-hp39kh1ya51yzp2lu**** &Common request parameters
```

Sample responses `XML` format

```xml
<ModifyIpv6GatewayAttributeResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId":"9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

### 5.5 ModifyIpv6GatewaySpec

You can call this operation to modify the specification of an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gatew aySpec | The operation that you want to perform. Set the value to Modif yIpv6Gat ewaySpec. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456nhmj**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Spec | String | Yes | Middle | The new specification you want to set for the IPv6 gateway. Valid values: Small (default): free edition Middle: enterprise edition Large: enhanced enterprise edition |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyIpv6GatewaySpec &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456cdvf**** &Spec=Middle &Common request parameters
```

Sample responses `XML` format

```xml
<ModifyIpv6GatewaySpecResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewaySpecResponse>
```

`JSON` format `{`

```json
 "RequestId":"9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

### 5.6 DeleteIpv6Gateway

You can call this operation to delete an IPv6 gateway. API description Before you can delete an IPv6 gateway of the enterprise or enhanced enterprise type, you must delete the egress-only rules of the IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Gatew ay | The operation that you want to perform. Set the value to Delet eIpv6Gat eway. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3y0l3ln89j8bgn h**** | The ID of the IPv6 gateway instance that you want to delete. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9A8AABE-A84B- 4AF2-A68A- 8E2EA190E7AE | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteIpv6Gateway &Ipv6GatewayId=ipv6gw-hp3y0l3ln89j8bgnh**** &RegionId=cn-huhehaote &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteIpv6GatewayResponse>
      <RequestId>E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE</RequestId>
</DeleteIpv6GatewayResponse>
```

`JSON` format `{`

```json
 "RequestId":"E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE"
```

### 5.7 CreateIpv6EgressOnlyRule

You can call this operation to create and configure an egress-only rule with an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Egress OnlyRule | The operation that you want to perform. Set the value to Creat eIpv6EgressOnlyRule. |
| InstanceId | String | Yes | ipv6- hp3nxjkfxn5pnhgl 5**** | The ID of the IPv6 address with which the egress-only rule will be configured. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3c2paq0ywaua sza**** | The ID of the IPv6 gateway to which the specified IPv6 address belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | ruledescription | The description of the egress-only rule. The description must be 2 to 256 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with _ a letter or Chinese character and cannot start with http:// or https:// . |
| InstanceType | String | No | IPv6Address | The type of the instance that will be configured with the egress-only rule. Set the value to: Ipv6Address (Default): IPv6 address |
| Name | String | No | rulename | The name of the egress-only rule. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressRuleI d | String | ipv6py- hp3w98rmlbqp0124 5**** | The ID of the egress-only rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=CreateIpv6EgressOnlyRule &RegionId=cn-huhehaote &InstanceId=ipv6-hp3nxjkfxn5pnhgl5**** &Ipv6GatewayId=ipv6gw-hp3c2paq0ywauasza**** &Common request parameters
```

Sample responses `XML` format

```xml
<CreateIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
   <Ipv6EgressRuleId>ipv6py-hp3w98rmlbqp01245****</Ipv6EgressRuleId>
</CreateIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
 "RequestId":"9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75",
 "Ipv6EgressRuleId":"ipv6py-hp3w98rmlbqp01245****"
```

### 5.8 DescribeIpv6EgressOnlyRules

You can call this operation to query the egress-only rules that match specific conditions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Egre ssOnlyRules | The operation that you want to perform. Set the value to DescribeIpv6EgressOnlyRules. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456cdvf**** | The ID of the IPv6 gateway with which the egress-only rules are configured. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceId | String | No | i-123456cdvf**** | The ID of the instance that is associated with the IPv6 address configured with the egress-only rules. |
| InstanceType | String | No | Ipv6Address | The type of the instance that is configured with the egress-only rules. Set the value to: Ipv6Address: IPv6 address |
| Ipv6EgressOnlyRul eId | String | No | ipv6gwpy- 123456cdvf**** | The ID of the egress-only rule that you want to query. |
| Name | String | No | rulename | The name of the egress-only rule. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressOnly Rules |   |   | The details of the egress-only rules. |
| Description | String | ruledescription | The description of the egress-only rule. |
| InstanceId | String | i-123456cdvf**** | The ID of the instance that is configured with the egress-only rule. |
| InstanceType | String | Ipv6Address | The type of the instance that is configured with the egress-only rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressOnly RuleId | String | ipv6gwpy- 123456cdvf**** | The ID of the egress-only rule. |
| Name | String | rulename | The name of the egress-only rule. |
| Status | String | Available | The status of the egress-only rule. |
| PageNumber | Integer | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | E16671B7-DEA6- 48E0-8E9C- 41913DAD44DD | The ID of the request. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeIpv6EgressOnlyRules &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456cdvf**** &Common request parameters
```

Sample responses `XML` format

```xml
<DescribeIpv6EgressOnlyRulesResponse>
   <Ipv6EgressOnlyRules>
      <Ipv6EgressOnlyRule>
         <Name></Name>
         <Status>Available</Status>
         <Description></Description>
         <InstanceId>ipv6-hp3b5a8t12ihycdvf****</InstanceId>
         <Ipv6EgressOnlyRuleId>ipv6py-hp3w98rmlbqp0cdvf****</Ipv6EgressOnlyRuleId>
         <InstanceType>Ipv6Address</InstanceType>
      </Ipv6EgressOnlyRule>
   </Ipv6EgressOnlyRules>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>D1FFB517-D1A7-49BA-9169-C7E7194A9B55</RequestId>
</DescribeIpv6EgressOnlyRulesResponse>
```

`JSON` format `{`

```json
 "Ipv6EgressOnlyRules":{
  "Ipv6EgressOnlyRule":[
```

`{`

```json
    "Name":"",
    "Status":"Available",
    "Description":"",
    "Ipv6EgressOnlyRuleId":"ipv6py-hp3w98rmlbqp0cdvf****",
    "InstanceId":"ipv6-hp3b5a8t12ihycdvf****",
    "InstanceType":"Ipv6Address"
```

`]` `},`

```json
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"D1FFB517-D1A7-49BA-9169-C7E7194A9B55"
```

### 5.9 DeleteIpv6EgressOnlyRule

You can call this operation to delete an egress-only rule. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Egress OnlyRule | The operation that you want to perform. Set the value to Delet eIpv6EgressOnlyRule. |

| Developer Guide·IPv6 | Gateway |   |   | IPv6 Gatewa |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Ipv6EgressOnlyRul eId | String | Yes | ipv6py- hp3w98rmlbqp0v fbg**** | The ID of the egress-only rule that you want to delete. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteIpv6EgressOnlyRule &RegionId=cn-huhehaote &Ipv6EgressOnlyRuleId=ipv6py-hp3w98rmlbqp0vfbg**** &Common request parameters
```

Sample responses `XML` format

```xml
<DeleteIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</DeleteIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
 "RequestId":"4E40EAF1-783D-4C05-948D-DA0426C398C1"
```

### 5.10 AllocateIpv6InternetBandwidth

You can call this operation to purchase public network bandwidth for an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateIpv6Inter netBandwidth | The operation that you want to perform. Set the value to Allocat eIpv6Int ernet Bandwidt h. |
| Bandwidth | Integer | Yes | 2 | The public network bandwidth of the IPv6 address. |
| Ipv6AddressId | String | Yes | ipv6- 123456cdvf**** | The instance ID of the IPv6 address. |
| Ipv6GatewayId | String | Yes | ipv5gw- 123456cdvf**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetBandwi dthId | String | 2 | The purchased public network bandwidth. |
| Ipv6AddressId | String | ipv6- hp352ungkzckndcvf **** | The instance ID of the IPv6 address. |
| RequestId | String | 6972A26E-99B1- 4367-9890- FBDEBB0F5E7D | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?AllocateIpv6InternetBandwidth &Ipv6AddressId=ipv6-123456cdvf**** &Ipv6GatewayId=ipv6gw-123456cdvf**** &RegionId=cn-huhehaote &<Common request parameters>
```

Sample responses `XML` format

```xml
<AllocateIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
   <InternetBandwidthId>2</InternetBandwidthId>
   <Ipv6AddressId>ipv6-hp352ungkzckncdvf****</Ipv6AddressId>
</AllocateIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "Ipv6AddressId":"ipv6-hp352ungkzckncdvf****",
 "RequestId":"6972A26E-99B1-4367-9890-FBDEBB0F5E7D",
 "InternetBandwidthId":2
```

### 5.11 ModifyIpv6InternetBandwidth

You can call this operation to modifiy the public network bandwidth of an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Interne tBandwidth | The operation that you want to perform. Set the value to Modif yIpv6Int ernet Bandwidt h. |
| Bandwidth | Long | Yes | 4 | The public network bandwidth of the IPv6 address. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Ipv6AddressId | String | No | ipv6- 1233456cdvf**** | The instance ID of the IPv6 address. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyIpv6InternetBandwidth &Bandwidth=3 &Ipv6AddressId=ipv6-hp351bytt9inrcdvf**** &RegionId=cn-huhehaote &Common request parameters
```

Sample responses `XML` format

```xml
<ModifyIpv6InternetBandwidthResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "RequestId":"D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

### 5.12 DeleteIpv6InternetBandwidth

You can call this operation to disable public access to an IPv6 address and set its public network bandwidth to zero. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Interne tBandwidth | The operation that you want to perform. Set the value to Delet eIpv6Int ernet Bandwidt h. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway to which the IPv6 address belongs. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6- 123456xxxxxxxx | The ID of the IPv6 address. |
| Ipv6InternetBand widthId | String | No | 2 | The public network bandwidth of the IPv6 address. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E07E0FE6-5C21- 405F-AF82- 7613AA81EF92 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteIpv6InternetBandwidth &RegionId=cn-huhehaote &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
</DeleteIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "RequestId":"E07E0FE6-5C21-405F-AF82-7613AA81EF92"
```

### 5.13 DescribeIpv6Addresses

Queries one or more IPv6 addresses. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Addr esses | The operation that you want to perform. Set the value to DescribeIpv6Addresses. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| AssociatedInstan ceId | String | No | i-123456nhmj**** | The ID of the instance associated with the IPv6 address. |
| AssociatedInstan ceType | String | No | EcsInstance | The type of the instance associated with the IPv6 address. Set the value to EcsInst ance (default): an ECS instance in a VPC |
| Ipv6Address | String | No | 2408:xxxx:180:17 01:94c7:bc38:3b fa:d2c | The IPv6 address that you want to query. |
| Ipv6AddressId | String | No | ipv6gw- hp33of4uz4k4knh mj**** | The instance ID of the IPv6 address. You can enter up to 20 instance IDs at a time. Separate instance IDs with commas (,). |
| Ipv6InternetBand widthId | String | No | 1 | The Internet bandwidth of the IPv6 address. |
| Name | String | No | test | The name of the IPv6 address. |
| NetworkType | String | No | Public | The communication type of the IPv6 address. Valid values: Privat e: communication within the private network Public: communication over the Internet |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| VSwitchId | String | No | vsw- 123456nhmj**** | The ID of the VSwitch to which the IPv6 address belongs. |
| VpcId | String | No | vpc- 123456nhmj**** | The ID of the VPC to which the IPv6 address belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Addresses |   |   | The details of IPv6 addresses. |
| AllocationTime | String | 2018-12- 20T14:56:09Z | The time when the IPv6 address was created. |
| AssociatedInsta nceId | String | i- hp325kt6307nhmj*** * | The ID of the instance associated with the IPv6 address. |
| AssociatedInsta nceType | String | EcsInstance | The type of the instance associated with the IPv6 address. |
| Ipv6Address | String | 2408:xxxx:0:2900:2 901:3c61:9ff0:xxxx | The IPv6 address. |
| Ipv6AddressId | String | ipv6- hp32vv2klzw4nhmj* *** | The instance ID of the IPv6 address. |
| Ipv6AddressNa me | String | test | The instance name of the IPv6 address. |
| Ipv6GatewayId | String | ipv6gw- hp38x2x0fz7nhmj*** * | The ID of the IPv6 gateway to which the IPv6 address belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6InternetBan dwidth |   |   | The information about the Internet bandwidth of the IPv6 address. |
| Bandwidth | Integer | 2 | The exclusive Internet bandwidth of the IPv6 address. Unit: Mbit/s. |
| BusinessStatus | String | Normal | The status of the exclusive bandwidth of the IPv6 address. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| Ipv6InternetBan dwidthId | String | ipv6bw- hp3b35oq1fj5nhmj** ** | The ID of the Internet bandwidth. |
| NetworkType | String | Public | The communication type of the IPv6 address. Valid values: Privat e: communication within the private network Public: communication over the Internet |
| Status | String | Available | The status of the IPv6 address. Valid values: Pending: The IPv6 address is being configured. Available: The IPv6 address is available. |
| VSwitchId | String | vsw- hp3123456nhmj**** | The ID of the VSwitch to which the IPv6 address belongs. |
| VpcId | String | vpc-123456nhmj**** | The ID of the VPC to which the IPv6 address belongs. |
| PageNumber | Integer | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Developer Guide·IPv | 6 Gateway |   | IPv6 Gatewa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AA4486A8-B6AE- 469E-AB09- 820EF8ECFA2B | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeIpv6Addresses &RegionId=cn-huhehaote &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6Addresses>
   <PageNumber>1</PageNumber>
   <TotalCount>2</TotalCount>
   <Ipv6Addresses>
      <Ipv6Address>
         <Ipv6AddressId>ipv6-hp32vv2klzw4ynhmj****</Ipv6AddressId>
         <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
         <AllocationTime>2019-01-07T05:16:23Z</AllocationTime>
         <Ipv6InternetBandwidth>
            <BusinessStatus></BusinessStatus>
            <Ipv6InternetBandwidthId></Ipv6InternetBandwidthId>
            <Bandwidth>0</Bandwidth>
         </Ipv6InternetBandwidth>
         <VSwitchId>vsw-hp3lyltb1dosjnhmj****</VSwitchId>
         <VpcId>vpc-hp34hflqqsjhnhmj****</VpcId>
         <Ipv6GatewayId></Ipv6GatewayId>
         <Status>Available</Status>
         <NetworkType>Private</NetworkType>
         <Ipv6Address>2408:xxxx:0:2900:2901:3c61:9ff0:8fdc</Ipv6Address>
         <Ipv6AddressName></Ipv6AddressName>
         <AssociatedInstanceId>i-hp325kt6307wnhmj****</AssociatedInstanceId>
         <RealBandwidth>0</RealBandwidth>
      </Ipv6Address>
      <Ipv6Address>
         <Ipv6AddressId>ipv6-hp331xt3oqafdnhmj****</Ipv6AddressId>
         <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
         <AllocationTime>2018-11-30T07:39:31Z</AllocationTime>
         <Ipv6InternetBandwidth>
            <BusinessStatus></BusinessStatus>
            <Ipv6InternetBandwidthId></Ipv6InternetBandwidthId>
            <Bandwidth>0</Bandwidth>
         </Ipv6InternetBandwidth>
         <VSwitchId>vsw-hp3ju1q8dtgfgnhmj****</VSwitchId>
         <VpcId>vpc-hp3kzilwd9yflxxxxxxxx</VpcId>
         <Ipv6GatewayId>ipv6gw-hp33p10bdbt77nhmj****</Ipv6GatewayId>
         <Status>Available</Status>
         <NetworkType>Private</NetworkType>
         <Ipv6Address>2408:xxxx:c0:200:35b:cd32:c460:6aa3</Ipv6Address>
         <Ipv6AddressName>abc</Ipv6AddressName>
         <AssociatedInstanceId>i-hp37gpsnhjn4nhmj****</AssociatedInstanceId>
         <RealBandwidth>0</RealBandwidth>
      </Ipv6Address>
   </Ipv6Addresses>
   <PageSize>10</PageSize>
   <RequestId>AA4486A8-B6AE-469E-AB09-820EF8ECFA2B</RequestId>
</DescribeIpv6Addresses>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "TotalCount":2,
 "Ipv6Addresses":{
  "Ipv6Address":[
```

`{`

```json
    "Ipv6AddressId":"ipv6-hp32vv2klzw4ynhmj****",
    "AssociatedInstanceType":"EcsInstance",
    "AllocationTime":"2019-01-07T05:16:23Z",
    "Ipv6InternetBandwidth":{
     "BusinessStatus":"",
     "Ipv6InternetBandwidthId":"",
     "Bandwidth":0
```

`},`

```json
    "VSwitchId":"vsw-hp3lyltb1dosjnhmj****",
    "VpcId":"vpc-hp34hflqqsjh3nhmj****",
    "Ipv6GatewayId":"",
    "Status":"Available",
    "NetworkType":"Private",
    "Ipv6Address":"2408:xxxx:0:2900:2901:3c61:9ff0:8fdc",
    "Ipv6AddressName":"",
    "AssociatedInstanceId":"i-hp325kt6307wnhmj****",
    "RealBandwidth":0
```

`},` `{`

```json
    "Ipv6AddressId":"ipv6-hp331xt3oqafdnhmj****",
    "AssociatedInstanceType":"EcsInstance",
    "AllocationTime":"2018-11-30T07:39:31Z",
    "Ipv6InternetBandwidth":{
     "BusinessStatus":"",
     "Ipv6InternetBandwidthId":"",
     "Bandwidth":0
```

`},`

```json
    "VSwitchId":"vsw-hp3ju1q8dtgfgnhmj****",
    "VpcId":"vpc-hp3kzilwd9yflnhmj****",
    "Ipv6GatewayId":"ipv6gw-hp33p10bdbt77nhmj****",
    "Status":"Available",
    "NetworkType":"Private",
    "Ipv6Address":"2408:xxxx:c0:200:35b:cd32:c460:6aa3",
    "Ipv6AddressName":"abc",
    "AssociatedInstanceId":"i-hp37gpsnhjn4nhmj****",
    "RealBandwidth":0
```

`]` `},`

```json
 "PageSize":10,
 "RequestId":"AA4486A8-B6AE-469E-AB09-820EF8ECFA2B"
```

### 5.14 ModifyIpv6AddressAttribute

You can call this operation to modify the name and description of an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Addre ssAttribute | The operation that you want to perform. Set the value to Modif yIpv6AddressAt t ribut e. |
| Ipv6AddressId | String | Yes | ipv6- hp32vv2klzw4yer df**** | The ID of the IPv6 address. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| Description | String | No | test | The description of the IPv6 address. The description must be 2 to 256 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with _ a letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | test | The name of the IPv6 address. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=ModifyIpv6AddressAttribute &Ipv6AddressId=ipv6-hp32vv2klzw4yerdf**** &RegionId=cn-huhehaote &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifyIpv6AddressAttributeResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6AddressAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId":"D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

using Asapi

## 6 Make SDK calls by using Asapi

### 6.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize operations and audit and manage their calls. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, avoiding inconsistent operations caused by different call methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a unified manner and customize development. ASAPI supports access of most cloud services deployed in Apsara Stack and passthrough or encapsulation of different backend APIs. This way, operations can be called with the same method. ASAPI allows you to use SDKs and API Portal to call APIs registered in ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. using Asapi

### 6.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 6.3 View the information about API operations

operations You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon. using Asapi
4. View and remember the service name, API operation name, and API version.

### 6.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), using Asapi dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
of the Apsara ASAPI Management platform. using Asapi

### 6.5 Obtain the core package for ASAPI

ASAPI Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 6.6 Obtain an AccessKey pair

An AccessKey pair is composed of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the AccessKey message, view the AccessKey pair of the organization.
using Asapi Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

### 6.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

### 6.8 SDK for Java

This topic describes how to obtain and use the Apsara Stack SDK for Java. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use the Apsara Stack SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of Asapi. For more information about how to obtain the endpoint of Asapi, see Obtain the endpoint of Asapi. using Asapi The Apsara Stack SDK for Java supports JDK 1.6 and later. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use the Apsara Stack SDK for Java You can call API operations on Asapi by using GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests using Asapi

```java
public class DescribeIpv6Gateways {
    public static void main(String[] args) {
        // Obtain the endpoint of Asapi.
        String endpoint = "http://xxx/asapi/v3";
    // Set request parameters.
    Map<String, String> parameters = new HashMap<String, String>();
    // Set parameters for the product.
    parameters.put("Product", "vpc");            // The product name must be the same as
the name displayed in the corresponding API directory.
    parameters.put("Action", "DescribeIpv6Gateways");           // The API operation, whi
ch is case-sensitive and must be the same as that on the API directory.
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

### 6.9 SDK for Node.js

This topic describes how to obtain and use the Apsara Stack SDK for Node.js. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use the Apsara Stack SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of Asapi. For more information about how to obtain the endpoint of Asapi, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information, see Query the region ID. Add dependencies
1. Install the Apsara Stack SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, you must configure mocha.opts as follows:
using Asapi

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use the Apsara Stack SDK for Node.js The following example shows how to use the Apsara Stack SDK for Node.js:
1. Create a client instance. To create a client instance, you must set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. as shown in the following example:

```
local: {
    regionId: 'obtained region ID',
    API_GATEWAY: 'obtained endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and set its parameters.
3. Initiate the request and handle any responses or exceptions.

```
// Specify the Asapi endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'DescribeIpv6Gateways',
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

6.10. (Optional) Use POP SDK to call Asapi If an application used POP SDK to call cloud services, you must switch the gateway to Asapi. Procedure
1. Switch the gateway to Asapi and add common parameters required by the API operation to the
using Asapi request header.
2. Add the Product Name field to the request header.
Code samples The following example calls the IPv6 Gateway API.

```java
try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessK
eySecret);
    // Set the Asapi gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "vpc", "<Asapi gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
    DescribeIpv6GatewaysRequest request = new DescribeIpv6GatewaysRequest();
    request.setSysRegionId(regionId); // Or setRegionId(regionId)
    // Set common parameters based on the information about the current user.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    DescribeIpv6GatewaysResponse result = (DescribeIpv6GatewaysResponse) acsClient.getAcsRe
sponse(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```
