---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 VPN Gateway Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 121
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 VPN Gateway Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20VPN%20Gateway%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 VPN Gateway Developer Guide 20220928

## Table of Contents

- 1 List of operations by function
- 2 Make API requests
  - 2.1 Request syntax
  - 2.2 API authorization
  - 2.3 API signature
- 3 RAM authentication
- 4 Common parameters
- 5 VPN Gateway
  - 5.1 CreateVpnGateway
  - 5.2 ModifyVpnGatewayAttribute
  - 5.3 DescribeVpnGateways
  - 5.4 DescribeVpnGateway
  - 5.5 DeleteVpnGateway
- 6 Customer gateway
  - 6.1 CreateCustomerGateway
  - 6.2 ModifyCustomerGatewayAttribute
  - 6.3 DescribeCustomerGateways
  - 6.4 DescribeCustomerGateway
  - 6.5 DeleteCustomerGateway
- 7 VPN Gateway routes
  - 7.1 CreateVpnRouteEntry
  - 7.2 CreateVpnPbrRouteEntry
  - 7.3 PublishVpnRouteEntry
  - 7.4 DescribeVpnRouteEntries
  - 7.5 DescribeVpnPbrRouteEntries
  - 7.6 ModifyVpnRouteEntryWeight
  - 7.7 ModifyVpnPbrRouteEntryWeight
  - 7.8 DeleteVpnRouteEntry
  - 7.9 DeleteVpnPbrRouteEntry
- 8 IPsec-VPN
  - 8.1 CreateVpnConnection
  - 8.2 ModifyVpnConnectionAttribute
  - 8.3 DescribeVpnConnections
  - 8.4 DescribeVpnConnection
  - 8.5 DownloadVpnConnectionConfig
  - 8.6 DeleteVpnConnection
- 9 SSL-VPN
  - 9.1 CreateSslVpnServer
  - 9.2 ModifySslVpnServer
  - 9.3 DescribeSslVpnServers
  - 9.4 DeleteSslVpnServer
  - 9.5 CreateSslVpnClientCert
  - 9.6 ModifySslVpnClientCert
  - 9.7 DescribeSslVpnClientCerts
  - 9.8 DescribeVpnSslServerLogs
  - 9.9 DeleteSslVpnClientCert
- 10 Call VPC SDK by using ASAPI
  - 10.1 Overview
  - 10.2 Log on to the API Tool console
  - 10.3 View the information about API operations
  - 10.4 Obtain the endpoint of ASAPI
  - 10.5 Obtain the core package for ASAPI
  - 10.6 Obtain an AccessKey pair
  - 10.7 Query the region ID
  - 10.8 SDK for Java
  - 10.9 SDK for Node.js
  - 10.10 Use SDK for POP through ASAPI (optional)

by function

## 1 List of operations by function

The following tables list the API operations that are available for use in VPN Gateway.

| API | Description |
|---|---|
| CreateVpnGateway | Creates a VPN gateway. |
| ModifyVpnGatewayAttribute | Modifies the name and description of a VPN gateway. |
| DescribeVpnGateways | Queries one or more VPN gateways. |
| DescribeVpnGateway | Queries details about a VPN gateway. |
| DeleteVpnGateway | Delete a VPN gateway |

Customer Gateway

| API | Description |
|---|---|
| CreateCustomerGateway | Creates a customer gateway. |
| ModifyCustomerGatewayAttribute | Modifies the name and description of a customer gateway. |
| DescribeCustomerGateways | Queries one or more customer gateways. |
| DescribeCustomerGateway | Queries details about a customer gateway. |
| DeleteCustomerGateway | Deletes a customer gateway. |

Configures routes for a VPN gateway

| API | Description |
|---|---|
| CreateVpnRouteEntry | Creates a destination-based route entry for a VPN gateway. |
| CreateVpnPbrRouteEntry | Creates a policy-based route entry for a VPN gateway. |
| PublishVpnRouteEntry | Publishes a route entry of a VPN gateway to the route table of the associated VPC network. |
| DescribeVpnRouteEntries | Queries destination-based route entries of a VPN gateway. |
| DescribeVpnPbrRouteEntries | Queries policy-based route entries of a VPN gateway. |

| eveloper Guide·List of operations y function | VPN Gatewa |
|---|---|

| API | Description |
|---|---|
| ModifyVpnRouteEntryWeight | Modifies the weight of a destination-based route entry for a VPN gateway. |
| ModifyVpnPbrRouteEntryWeight | Modifies the weight of a policy-based route entry for a VPN gateway. |
| DeleteVpnRouteEntry | Deletes a destination-based route entry of a VPN gateway. |
| DeleteVpnPbrRouteEntry | Deletes a policy-based route entry of a VPN gateway. |

IPsec-VPN

| API | Description |
|---|---|
| CreateVpnConnection | Creates an IPsec-VPN connection. |
| ModifyVpnConnectionAttribute | Modifies the configuration of an IPsec-VPN connection. |
| DescribeVpnConnections | Queries IPsec-VPN connections. |
| DescribeVpnConnection | Queries details about an IPsec-VPN connection. |
| DownloadVpnConnectionConfig | Modifies the configuration of an IPsec-VPN connection. |
| DeleteVpnConnection | Deletes an IPsec-VPN connection. |

SSL-VPN

| API | Description |
|---|---|
| CreateSslVpnServer | Creates an SSL-VPN server. |
| ModifySslVpnServer | Modifies the configuration of an SSL-VPN server. |
| DescribeSslVpnServers | Queries SSL-VPN servers. |
| DeleteSslVpnServer | Deletes an SSL-VPN server. |
| CreateSslVpnClientCert | Creates an SSL-VPN client certificate. |
| ModifySslVpnClientCert | Modifies the name of an SSL-VPN client certificate. |
| DescribeSslVpnClientCerts | Queries SSL-VPN client certificates. |
| DescribeVpnSslServerLogs | Queries the logs of an SSL server. |
| DeleteSslVpnClientCert | Deletes an SSL-VPN client certificate. |

## 2 Make API requests

### 2.1 Request syntax

You can send HTTP GET requests to call the VPN Gateway API. Before you send a request, specify the request parameters for the specific operation. A response is returned for each request. Requests and responses are encoded by using UTF-8. The VPN Gateway API is in the remote procedure call (RPC) style. You can call the VPN Gateway API by sending an HTTP GET request. The following is the request syntax:

```
http://Endpoint/?Action=xx&Parameters
```

Where Endpoint: The endpoint of the VPN Gateway API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can view the endpoint in the Apsara Stack Operations console. For more information, see Obtain the endpoint of Asapi. Action: the operation that you want to perform. For example, you can call DescribeVpnGateways to query a VPN gateway. Version: the version of the API that you want to call. The current version of the VPN Gateway API is 2 016-04-28. Parameters: the request parameters. The parameters must be separated with ampersands (&). Request parameters include both common request parameters and API operation-specific parameters. Common request parameters include information such as the API version number and authentication information. For more information, see Common parameters. The following example shows how to call DescribeVpnGateways to query a VPN gateway. Not e The following code has been formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeVpnGateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

### 2.2 API authorization

To ensure the security of your account, we recommend that you call API operations as a Resource Access Management (RAM) user. Before you call the VPN Gateway API as a RAM user, you must create a RAM user and grant the RAM user the required permissions. For more information about VPN resources and API operations that you can authorize a RAM user to use, see RAM authentication.

### 2.3 API signature

SSL Certificates Service authenticates each API request. Before sending a request by using HTTP or HTTPS, you must add signature information to the request. You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. VPN Gateway implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Alibaba Cloud accounts and RAM users that is similar to a pair of username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. To call an RPC API operation, you must add the signature to the API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

For example, you want to call the DescribeVpcs operation. The AccessKey ID is `testid` and the AccessKey secret is `testsecret` . The following code block shows the URL of the request before the request is signed

```
http://vpc.example.com/?Action=DescribeVpnGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

To calculate the signature, perform the following operations:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpnGateways&Format%3DXML&SignatureMethod% 3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1. 0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2016-04-28
```

2. Calculate the HMAC value of the string-to-sign.
Append an ampersand (&) to the end of the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request:

```
http://vpc.example.com/?Action=DescribeVpnGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

n

## 3 RAM authentication

Before you call the VPN Gateway API as a RAM user, you must use an Apsara Stack tenant account to create a permission policy to assign permissions to the RAM user. In the permission policy, you must use an Alibaba Cloud Resource Name (ARN) to specify the resource that you want this RAM user to access. Resources types of VPN Gateway that can be authorized The following table lists the VPN Gateway resources that can be authorized and the ARNs of these resources.

| Resource type | ARN |
|---|---|
| VPN gateway | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
|   | acs:vpc:$regionid:$accountid:vpngateway/* |
|   | acs:vpc:*:$accountid:vpngateway/* |
| Customer gateway | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
|   | acs:vpc:$regionid:$accountid:customergateway/* |
|   | acs:vpc:*:$accountid:customergateway/* |
| IPsec-VPN connection | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
|   | acs:vpc:$regionid:$accountid:vpnconnection/* |
|   | acs:vpc:*:$accountid:vpnconnection/* |
| SSL-VPN server | acs:vpc:$regionid:$accountid:sslvpnserver/$sslvpnserverid |
|   | acs:vpc:$regionid:$accountid:sslvpnserver/* |
|   | acs:vpc:*:$accountid:sslvpnserver/* |
| SSL-VPN client certificate | acs:vpc:$regionid:$accountid:sslvpnclientcert/$sslvpnclientcertid |
|   | acs:vpc:$regionid:$accountid:sslvpnclientcert/* |
|   | acs:vpc:*:$accountid:sslvpnclientcert/* |
| General-purpose resource | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accoutid`/`vrouterid are the IDs of specific resources. `*` represents all resources. VPN Gateway API operations that can be authorized The following table lists the VPN Gateway API operations that can be authorized and the ARNs of these API operations. n

| API | ARN |
|---|---|
| ModifyVpnGatewayAttri bute | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
| DescribeVpnGateways | acs:vpc:$regionid:$accountid:vpngateway/* |
| DescribeVpnGateway | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
| DeleteVpnGateway | acs:vpc:$regionid:$accountid:vpngateway/$vpngatewayid |
| CreateCustomerGatewa y | acs:vpc:$regionid:$accountid:customergateway/* |
| DeleteCustomerGatewa y | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
| DescribeCustomerGate way | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
| DescribeCustomerGate ways | acs:vpc:$regionid:$accountid:customergateway/* |
| ModifyCustomerGatewa yAttribute | acs:vpc:$regionid:$accountid:customergateway/$customergatewayid |
| CreateVpnConnection | acs:vpc:$regionid:$accountid:vpnconnection/* |
| DeleteVpnConnection | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
| DescribeVpnConnection | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
| DescribeVpnConnection s | acs:vpc:$regionid:$accountid:vpnconnection/* |
| ModifyVpnConnectionAt tribute | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |
| DownloadVpnConnectio nConfig | acs:vpc:$regionid:$accountid:vpnconnection/$vpnconnectionid |

ers

## 4 Common parameters

Common request parameters Common request parameters are required by all API operations. Common request parameters

| Parameter | Type | Requir ed | Description |
|---|---|---|---|
| Format | String | No | The format in which the response is returned. Valid values: JSON and XML. Default value: JSON. |
| Version | String | Yes | The version number of the API, which is in the YYYY-MM-DD format. Valid values: 2016-04-28. |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud |
| Signature | String | Yes | The signature string in the API request. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Valid value: HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2013-01-10T12:00:00Z indicates 20:00:00 on January 10, 2013 (UTC+8). |
| SignatureVersio n | String | Yes | The version of the signature encryption algorithm. Valid value: 1.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different random numbers for different requests. |

Common response parameters API responses use the HTTP response format where a 2XX status code indicates a successful call and a 4XX or 5XX status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is JSON. Every response returns a unique RequestId regardless of whether the call is successful. XML format ers

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

## 5 VPN Gateway

### 5.1 CreateVpnGateway

You can call this operation to create a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnGatew ay | The operation that you want to perform. Set the value to Creat eVpnGat eway. |
| Bandwidth | Integer | Yes | 5 | The network bandwidth of the VPN gateway. Unit: Mbit/s. Valid values: 5, 10, 20, 50, and 100. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1ub1yt9cvakoe lj**** | The ID of the VPC to which the VPN gateway belongs. |
| EnableIpsec | Boolean | No | true | Specifies whether to enable the IPsec- VPN feature. Valid values: t rue (default): Enable the IPsec-VPN feature. f alse: Disable the IPsec-VPN feature. |
| EnableSsl | Boolean | No | true | Specifies whether to enable the SSL- VPN feature. Valid values: t rue: Enable the SSL-VPN feature. f alse (default): Disable the SSL-VPN feature. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | MYVPN | The name of the VPN gateway. The default value is the ID of the VPN gateway. The name can be 2 to 128 characters in length. It can contain letters, digits, underscores ( ), and hyphens (-). The _ name must start with a letter or Chinese character and cannot start with http:// or https:// . |
| SslConnections | Integer | No | 2 | The maximum number of clients that can be connected simultaneously. Valid values: 5, 10, and 20, |
| VSwitchId | String | No | vsw- bp1j5miw2bae9s 2vt**** | The ID of the VSwitch to which the VPN gateway belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | myVpn | The name of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=CreateVpnGateway &Bandwidth=5 &RegionId=cn-hangzhou &VpcId=vpc-bp1ub1yt9cvakoelj**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateVpnGatewayResponse>
      <Name>myVpn</Name>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
</CreateVpnGatewayResponse>
```

`JSON` format `{`

```json
 "CreateVpnGatewayResponse":{
  "Name":"myVpn",
  "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
  "RequestId":"54B48E3D-DF70-471B-AA93-08E683A1B457"
```

`}` `}`

### 5.2 ModifyVpnGatewayAttribute

You can call this operation to modify the name and description of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnGatew ayAttribute | The operation that you want to perform. Set the value to Modif yVpnGat ewayAt t ribut e. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | VPN Gateway | The description of the VPN gateway. The description must be 2 to 256 characters in length. It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | myvpn | The name of the VPN gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoel** ** | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv* *** | The ID of the VSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.62.69.xxx | The public IP address of the VPN gateway. |
| CreateTime | Long | 1492753580000 | The time when the VPN gateway was created. |
| EndTime | Long | 1495382400000 | The time when the VPN gateway expires. |
| Spec | String | 5M | The specification of the VPN gateway. |
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |

| Developer Guide·VP | N Gateway |   | VPN Gatewa |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Status | String | active | The status of the VPN gateway. |
| IntranetIp | String | 172.16.104.xxx | The private IP address of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyVpnGatewayAttribute &RegionId=cn-shanghai &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifyVpnGatewayAttributeResponse>
      <Name>aaa</Name>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <BusinessStatus>Normal</BusinessStatus>
      <Spec>5M</Spec>
      <CreateTime>1492753580000</CreateTime>
      <IntranetIp>172.16.104.xxx</IntranetIp>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
      <InternetIp>116.62.69.xxx</InternetIp>
      <EndTime>1495382400000</EndTime>
      <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
      <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
</ModifyVpnGatewayAttributeResponse>
```

`JSON` format `{`

```json
 "Name":"aaa",
 "Status":"active",
 "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
 "Spec":"5M",
 "BusinessStatus":"Normal",
 "RequestId":"BA56EAF8-E3A9-4BE6-8511-8F03512153E2",
 "IntranetIp":"172.16.104.xxx",
 "CreateTime":1492753580000,
 "InternetIp":"116.62.69.xxx",
 "EndTime":1495382400000,
 "VSwitchId":"vsw-bp1y9ovl1cu9ou4tv****",
 "VpcId":"vpc-bp1ub1yt9cvakoelj****"
```

`}`

### 5.3 DescribeVpnGateways

You can call this operation to query one or more VPN gateways. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGate ways | The operation that you want to perform. Set this value to DescribeVpnGat eways. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status | String | No | init | The status of the VPN gateway. Valid values: init provisioning act ive updat ing delet ing |
| VpcId | String | No | vpc- bp1ub1yt9cvakoe lj**** | The ID of the VPC to which the VPN gateway belongs. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGateways |   |   | Details of the VPN gateways. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj** ** | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv* *** | The ID of the VSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.62.69.xxx | The public IP address of the VPN gateway. |
| CreateTime | Long | 1515383700000 | The time when the VPN gateway was created. |
| EndTime | Long | 1518105600000 | The time when the VPN gateway expires. |
| Spec | String | 5M | The maximum bandwidth supported by the VPN gateway. |

| PN Gateway |   |   | Developer Guide·VPN Gatewa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| BusinessStatus | String | Normal | The status of the VPN gateway. |
| IpsecVpn | String | enable | Indicates whether the IPsec-VPN feature is enabled. |
| SslMaxConnecti ons | Long | 5 | The maximum number of concurrent SSL- VPN connections. |
| SslVpn | String | enable | Indicates whether the SSL-VPN feature is enabled. |
| Tag | String | 1 | The tag. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries on the current page. |
| RequestId | String | DF11D6F6-E35A- 41C3-9B20- 6FC8A901FE65 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeVpnGateways &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeVpnGatewaysResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <VpnGateways>
            <VpnGateway>
                  <Status>active</Status>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <BusinessStatus>Normal</BusinessStatus>
                  <Spec>5M</Spec>
                  <CreateTime>1492753580000</CreateTime>
                  <InternetIp>116.62.69.xxx</InternetIp>
                  <EndTime>1495382400000</EndTime>
                  <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
                  <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
            </VpnGateway>
      </VpnGateways>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeVpnGatewaysResponse>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "VpnGateways":{
  "VpnGateway":[
```

`{`

```json
    "Status":"active",
    "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
    "Spec":"5M",
    "BusinessStatus":"Normal",
    "CreateTime":1492753580000,
    "InternetIp":"116.62.69.xxx",
    "EndTime":1495382400000,
    "VSwitchId":"vsw-bp1y9ovl1cu9ou4tv****",
    "VpcId":"vpc-bp1ub1yt9cvakoelj****"
```

`}` `]` `},`

```json
 "RequestId":"B2CD1315-CA2B-47B1-9DA5-8F1D69C48E82"
```

`}`

### 5.4 DescribeVpnGateway

Queries detailed information of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGate way | The operation that you want to perform. Set the value to DescribeVpnGat eway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj** ** | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv* *** | The ID of the VSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.62.222.XX | The public IP address of the VPN gateway. |
| CreateTime | Long | 1495382400000 | The time when the VPN gateway was created. |
| EndTime | Long | 1495382400000 | The time when the VPN gateway expires. |
| Spec | String | 5 | The specification of the VPN gateway. |
| Name | String | vpngatewayname | The name of the VPN gateway. |
| Description | String | vpngatewaydescript ion | The description of the VPN gateway. |

| Developer Guide·VP | N Gateway |   | VPN Gatewa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | init | The status of the VPN gateway. |
| IpsecVpn | String | enable | Indicates whether IPsec-VPN is enabled for the VPN gateway. |
| RequestId | String | DE77A7F3-3B74- 41C0-A5BC- CAFD188C28B6 | The ID of the request. |
| SslMaxConnecti ons | Long | 5 | The maximum number of concurrent SSL- VPN connections. |
| SslVpn | String | enable | Indicates whether SSL-VPN is enabled for the VPN gateway. |
| Tag | String | tag1 | The tag associated with the VPN gateway. |

Examples Sample requests

```
https://vpc.example.comm/?Action=DescribeVpnGateway &RegionId=cn-shanghai &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnGatewayResponse>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <Spec>5M</Spec>
      <BusinessStatus>Normal</BusinessStatus>
      <RequestId>98C99F30-A3D2-42E1-AC75-0C882FBE92F7</RequestId>
      <CreateTime>1492753580000</CreateTime>
      <InternetIp>116.62.69.xx</InternetIp>
      <EndTime>1495382400000</EndTime>
      <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
      <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
</DescribeVpnGatewayResponse>
```

`JSON` format `{`

```json
 "Status":"active",
 "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
 "Spec":"5M",
 "BusinessStatus":"Normal",
 "RequestId":"E98A9651-7098-40C7-8F85-C818D1EBBA85",
 "CreateTime":1492753580000,
 "InternetIp":"116.62.69.XX",
 "EndTime":1495382400000,
 "VSwitchId":"vsw-bp1y9ovl1cu9ou4tv****",
 "VpcId":"vpc-bp1ub1yt9cvakoelj****"
```

`}`

### 5.5 DeleteVpnGateway

You can call this operation to delete a VPN gateway. Not e You cannot delete a VPN gateway associated with an IPsec connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnGatew ay | The operation that you want to perform. Set the value to Delet eVpnGat eway. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | >0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteVpnGateway &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteNatGatewayResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteNatGatewayResponse>
```

`JSON` format `{`

```json
 "RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` y

## 6 Customer gateway

### 6.1 CreateCustomerGateway

You can call this operation to create a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateCustomerG ateway | The operation that you want to perform. Set the value to Creat eCust omerGat eway. |
| IpAddress | String | Yes | 116.62.222.xxx | The IP address of the customer gateway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | Gateway | The description of the customer gateway. The description must be 2 to 256 characters in length. It must start with a letter or Chinese character and cannot start with http:// or https:// . |

y

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | Gateway | The name of the customer gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate wayId | String | cgw- bp1aw0a5nfff03xp1 **** | The ID of the customer gateway. |
| IpAddress | String | 100.1.1.XX | The IP address of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| CreateTime | Long | 1493363486000 | The time when the customer gateway was created. |
| RequestId | String | cgw- bp1aw0a5nfff03xp1 **** | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=CreateCustomerGateway &IpAddress=116.62.222.xxx &RegionId=cn-shanghai &<Common request parameters>
```

Sample responses `XML` format y

```xml
<CreateCustomerGatewayResponse>
      <CustomerGatewayId>cgw-bp1aw0a5nfff03xp****</CustomerGatewayId>
      <RequestId>185E81B1-3916-4667-B48F-C52409B33F2B</RequestId>
      <CreateTime>1493363486000</CreateTime>
      <IpAddress>100.1.1.XX</IpAddress>
</CreateCustomerGatewayResponse>
```

`JSON` format `{`

```json
 "CustomerGatewayId":"cgw-bp1jrawp82av6bws9****",
 "RequestId":"D32B3C26-6C6C-4988-93E9-D2A6444CE6AE",
 "CreateTime":1493363599000,
 "IpAddress":"100.1.1.XX"
```

`}`

### 6.2 ModifyCustomerGatewayAttribute

You can call this operation to modify the name and description of a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyCustomerG atewayAttribute | The operation that you want to perform. Set the value to Modif yCust omerGat ewayAt t ribut e. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

y

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | test | The description of the customer gateway. The description must be 2 to 256 characters in length. It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | test | The name of the customer gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate wayId | String | cgw- bp1pvpl9r9adju6l5** ** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.196.32.xxx | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The time when the customer gateway was created. |
| RequestId | String | E61293C8-AF07- 4E87-A272- 542680038F93 | The ID of the request. |

Examples Sample requests y

```
https://vpc.example.com/?Action=ModifyCustomerGatewayAttribute &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-shanghai &Name=test &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifyCustomerGatewayAttributeResponse>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RequestId>E61293C8-AF07-4E87-A272-542680038F93</RequestId>
      <CreateTime>1492747187000</CreateTime>
      <IpAddress>139.196.32.xxx</IpAddress>
</ModifyCustomerGatewayAttributeResponse>
```

`JSON` format `{`

```json
 "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
 "CreateTime":1492747187000,
 "RequestId":"8AA5CE21-2E6A-4530-BDF5-F055849476E6",
 "IpAddress":"139.196.32.xxx"
```

`}`

### 6.3 DescribeCustomerGateways

You can call this operation to query one or more customer gateways. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustome rGateways | The operation that you want to perform. Set the value to DescribeCust omerGat eways. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| CustomerGatewa yId | String | No | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |

| D y | eveloper Guide·Cust | omer gatew | a |   | VPN Gatewa | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate ways |   |   | The description of the customer gateway. |
| CustomerGate wayId | String | cgw- bp1pvpl9r9adju6l5** ** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.196.32.xxx | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The time when the customer gateway was created. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests y

```
https://vpc.example.com/?Action=DescribeCustomerGateways &RegionId=cn-shanghai &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeCustomerGatewaysResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
      <CustomerGateways>
            <CustomerGateway>
                  <Name>test</Name>
                  <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
                  <CreateTime>1492747187000</CreateTime>
                  <IpAddress>139.196.32.xxx</IpAddress>
            </CustomerGateway>
      </CustomerGateways>
</DescribeCustomerGatewaysResponse>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29",
 "CustomerGateways":{
  "CustomerGateway":[
```

`{`

```json
    "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
    "Name":"test",
    "CreateTime":1492747187000,
    "IpAddress":"139.196.32.xxx"
```

`}` `]` `}` `}`

### 6.4 DescribeCustomerGateway

You can call this operation to query the details of a specified customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

y

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustome rGateway | The operation that you want to perform. Set the value to DescribeCust omerGat eway. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate wayId | String | cgw- bp1pvpl9r9adju6l5** ** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.196.32.xxx | The IP address of the customer gateway. |
| RequestId | String | 99506ECB-218F- 45A5-AE8E- 79518451F615 | The ID of the request. |
| CreateTime | Long | 1492747187000 | The time when the customer gateway was created. |

Examples Sample requests y

```
https://vpc.example.com/?Action=DescribeCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-shanghai &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeCustomerGatewayResponse>
      <Name>test</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <CreateTime>1492747187000</CreateTime>
      <RequestId>99506ECB-218F-45A5-AE8E-79518451F615</RequestId>
      <IpAddress>139.196.32.xxx</IpAddress>
</DescribeCustomerGatewayResponse>
```

`JSON` format `{`

```json
 "Name":"test",
 "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
 "CreateTime":1492747187000,
 "RequestId":"A0457BC9-6C0F-4437-AB9D-FB2EABC1D6A2",
 "IpAddress":"139.196.32.xxx"
```

`}`

### 6.5 DeleteCustomerGateway

You can call this operation to delete a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCustomerG ateway | The operation that you want to perform. Set the value to Delet eCust omerGat eway. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |

y

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-shanghai &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteCustomerGatewayResesponse>
  <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteCustomerGatewayResesponse>
```

`JSON` format `{`

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` es

## 7 VPN Gateway routes

### 7.1 CreateVpnRouteEntry

You can call this operation to create a destination-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnRouteE ntry | The operation that you want to perform. Set the value to Creat eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to publish the destination-based route to the routing table of the associated VPC network. t rue: Publish the destination-based route to the routing table of the associated VPC network. f alse: Do not publish the destination-based route to the routing table of the associated VPC network. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

| D e | eveloper Guide·VPN s | Gateway ro | ut |   | VPN Gatewa | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The time when the destination-based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| OverlayMode | String | Ipsec | The tunneling protocol. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| State | String | published | The status of the destination-based route. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

Examples Sample requests es

```
http(s)://vpc.example.com/? Action=CreateVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateVpnRouteEntryResponse>
   <RouteDest>10.0.0.0/24</RouteDest>
   <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
   <OverlayMode>Ipsec</OverlayMode>
   <State>published</State>
   <Weight>100</Weight>
   <CreateTime>1563873294331</CreateTime>
   <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</CreateVpnRouteEntryResponse>
```

`JSON` format `{`

```json
 "RouteDest":"10.0.0.0/24",
 "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
 "OverlayMode":"Ipsec",
 "Weight":100,
 "State":"published",
 "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78",
 "NextHop":"vco-bp1tui07ob10fmuro****",
 "CreateTime":1563873294331
```

`}`

### 7.2 CreateVpnPbrRouteEntry

You can call this operation to create a policy-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnPbrRou teEntry | The operation that you want to perform. Set the value to Creat eVpnPbrRout eEnt ry. |

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to publish the policy-based route to the route table of the associated VPC network. t rue: Publish the policy-based route to the route table of the associated VPC network. f alse: Do not publish the policy- based route to the route table of the associated VPC network. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN policy-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | vpnroute1 | The description of the policy-based route. |

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The time when the policy-based route was created. |
| Description | String | vpnroute1 | The description of the policy-based route. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| OverlayMode | String | Ipsec | The tunneling protocol. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | 192.168.1.0/24 | The source CIDR block of the policy-based route. |
| State | String | normal | The status of the policy-based route. Valid values: published: published normal: not published |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0 and 100. |

Examples Sample requests es

```
http(s)://vpc.example.com/? Action=CreateVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateVpnPbrRouteEntryResponse>
   <RouteDest>10.0.0.0/24</RouteDest>
   <RouteSource>192.168.1.0/24</RouteSource>
   <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
   <OverlayMode>Ipsec</OverlayMode>
   <State>published</State>
   <Weight>100</Weight>
   <CreateTime>1563873294331</CreateTime>
   <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
</CreateVpnPbrRouteEntryResponse>
```

`JSON` format `{`

```json
 "RouteDest":"10.0.0.0/24",
 "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
 "OverlayMode":"Ipsec",
 "Weight":100,
 "State":"published",
 "NextHop":"vco-bp1tui07ob10fmuro****",
 "CreateTime":1563873294331,
 "RouteSource":"192.168.1.0/24"
```

`}`

### 7.3 PublishVpnRouteEntry

You can call this operation to publish a route of a VPN gateway to the routing table of the associated VPC network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PublishVpnRoute Entry | The operation that you want to perform. Set the value to PublishVpnRout eEnt ry. |

| PN Gateway |   |   |   | Developer Guide·VPN Gateway rou e |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to publish the route to the routing table of the associated VPC network. t rue: Publish the route to the routing table of the associated VPC network. f alse: Do not publish the route to the routing table of the associated VPC network. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the route. |
| RouteType | String | Yes | pbr | The type of the route. Valid values: pbr: policy-based route dbr: destination-based route |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

es Examples Sample requests

```
http(s)://vpc.example.com/? Action=PublishVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteType=PBR &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<PublishVpnRouteEntryResponse>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</PublishVpnRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

`}`

### 7.4 DescribeVpnRouteEntries

You can call this operation to query one or more destination-based routes of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnRout eEntries | The operation that you want to perform. Set the value to DescribeVpnRout eEnt ries. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based routes. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 10 | The current page number. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |
| TotalCount | Integer | 10 | The total number of entries returned. |
| VpnRouteEntrie s |   |   | The detailed information about the destination-based routes. |
| CreateTime | Long | 1492747187000 | The time when the destination-based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| State | String | published | The status of the destination-based route. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

es Examples Sample requests

```
http(s)://vpc.example.com/? Action=DescribeVpnRouteEntries &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeVpnRouteEntriesResponse>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <VpnRouteEntries>
      <VpnRouteEntry>
         <RouteDest>10.0.0.0/24</RouteDest>
         <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
         <State>normal</State>
         <Weight>100</Weight>
         <CreateTime>1563874074000</CreateTime>
         <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
      </VpnRouteEntry>
   </VpnRouteEntries>
   <PageSize>10</PageSize>
   <RequestId>BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5</RequestId>
</DescribeVpnRouteEntriesResponse>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "VpnRouteEntries":{
  "VpnRouteEntry":[
```

`{`

```json
    "RouteDest":"10.0.0.0/24",
    "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
    "Weight":100,
    "State":"normal",
    "NextHop":"vco-bp1tui07ob10fmuro****",
    "CreateTime":1563874074000
```

`}` `]` `},`

```json
 "RequestId":"BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5"
```

`}` es

### 7.5 DescribeVpnPbrRouteEntries

You can call this operation to query one or more policy-based routes of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnPbrR outeEntries | The operation that you want to perform. Set the value to DescribeVpnPbrRout eEnt ries. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the policy-based routes. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |
| VpnPbrRouteEn tries |   |   | The detailed information about the policy- based routes. |

| Developer Guide·VP | N Gateway rout |   | VPN Gatewa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The time when the policy-based route entry was created. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | 192.168.0.0/24 | The source CIDR block of the policy-based route. |
| State | String | published | The status of the policy-based route. Valid values: published: published normal: not published |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0 and 100. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=DescribeVpnPbrRouteEntries &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample responses `XML` format es

```xml
<DescribeVpnPbrRouteEntriesResponse>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <RequestId>E5D94DC7-AEC7-4E73-A203-61B04D1F1160</RequestId>
   <PageSize>10</PageSize>
   <VpnPbrRouteEntries>
      <VpnPbrRouteEntry>
         <RouteDest>10.0.0.0/32</RouteDest>
         <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
         <State>published</State>
         <Weight>100</Weight>
         <CreateTime>1563881012000</CreateTime>
         <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
         <RouteSource>11.0.0.0/32</RouteSource>
      </VpnPbrRouteEntry>
   </VpnPbrRouteEntries>
</DescribeVpnPbrRouteEntriesResponse>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"E5D94DC7-AEC7-4E73-A203-61B04D1F1160",
 "VpnPbrRouteEntries":{
  "VpnPbrRouteEntry":[
```

`{`

```json
    "RouteDest":"10.0.0.0/32",
    "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
    "Weight":100,
    "State":"published",
    "RouteSource":"11.0.0.0/32",
    "NextHop":"vco-bp1tui07ob10fmuro****",
    "CreateTime":1563881012000
```

`}` `]` `}` `}`

### 7.6 ModifyVpnRouteEntryWeight

You can call this operation to modify the weight of a destination-based route of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnRouteE ntryWeight | The operation that you want to perform. Set the value to Modif yVpnRout eEnt ryWeight . |
| NewWeight | Integer | Yes | 100 | The new weight of the destination- based route after you perform this operation. Valid values: 0 and 100. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The previous weight of the destination-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

es

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=ModifyVpnRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifyVpnRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnRouteEntryWeightResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}`

### 7.7 ModifyVpnPbrRouteEntryWeight

You can call this operation to modify the weight of a policy-based route of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnPbrRou teEntryWeight | The operation that you want to perform. Set the value to Modif yVpnPbrRout eEnt ryWeight . |
| NewWeight | Integer | Yes | 100 | The new weight of the policy-based route after you perform this operation. Valid values: 0 and 100. |

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the policy-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The original weight of the policy-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. Set the value to Ipsec (IPsec tunneling protocol). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests es

```
http(s)://vpc.example.com/? Action=ModifyVpnPbrRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=100 &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifyVpnPbrRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnPbrRouteEntryWeightResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}`

### 7.8 DeleteVpnRouteEntry

You can call this operation to delete a destination-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnRouteE ntry | The operation that you want to perform. Set the value to Delet eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |

| Developer Guide·VPN | Gateway ro | ut |   | VPN Gatewa |
|---|---|---|---|---|

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=DeleteVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteVpnRouteEntryResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnRouteEntryResponse>
```

`JSON` format es `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}`

### 7.9 DeleteVpnPbrRouteEntry

You can call this operation to delete a VPN policy-based route. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnPbrRou teEntry | The operation that you want to perform. Set the value to Delet eVpnPbrRout eEnt ry.. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN policy-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0 \| 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

es

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| OverlayMode | String | No | Ipsec | The tunneling protocol. Set the value to Ipsec (IPsec tunneling protocol). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=DeleteVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteVpnPbrRouteEntryResponse>
      <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnPbrRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}`

## 8 IPsec-VPN

### 8.1 CreateVpnConnection

You can call this operation to create an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnConnec tion | The operation that you want to perform. Set the value to Creat eVpnConnect ion. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnk*** * | The ID of the customer gateway. |
| LocalSubnet | String | Yes | 1.1.1.0/24,1.1.2.0 /24 | The CIDR block of the VPC to be connected with the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| RegionId | String | Yes | cn-shanghai | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| RemoteSubnet | String | Yes | 1.1.1.0/24,1.1.2.0 /24 | The CIDR block of the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm* *** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically configure routes. Valid values: t rue (default): Routes are automatically configured. f alse: Routes are not automatically configured. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| EffectImmediatel y | Boolean | No | false | Specifies whether to delete a successfully negotiated IPsec-VPN tunnel and initiate a negotiation again. Valid values: t rue: Negotiate immediately after the configuration is completed. f alse (default): Negotiate when inbound traffic is detected. |
| HealthCheckConfi g | String | No | ['enable':'true','di p':'192.168.1.2','s ip':'192.168.2.2','i nterval':'3','retry' :'3'] | The health check configurations: Healt hCheckConf ig.enable: Specifies whether to enable health checks. Valid values: t rue \| f alse (default) Healt hCheckConf ig.dip: The destination IP address configured for health checks. Healt hCheckConf ig.sip: The source IP address configured for health checks. Healt hCheckConf ig.int erval: The interval between health check retries. Unit: seconds. Healt hCheckConf ig.ret ry: The maximum number of health check retries. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | ['IkeVersion':'ikev 1','IkeMode':'mai n'] | The configurations of phase one negotiations. IkeConf ig.Psk: The pre-shared key used for authentication between the IPsec-VPN gateway and the customer gateway. The value is generated randomly by default. It can contain up to 100 characters. You can also specify a pre-shared key. IkeConf ig.IkeVersion: The version of the IKE protocol. Valid values: ikev1 \| ikev2. Default value: ikev1. IkeConf ig.IkeMode: The negotiation mode of IKE V1. Valid values: main \| aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm of phase one negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm of phase one negotiations. Valid values: md5 \| sha1. Default value: md5. IkeConf ig.IkePf s: The Diffie- Hellman key exchange algorithm used by phase one negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IkeConf ig.IkeLif et ime: The SA lifetime resulting from phase one negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: The identification of the VPN gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the VPN gateway. IkeConf ig.Remot eId: The identification of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | ['IpsecAuthAlg':' md5','IpsecEncAl g':'aes'] | The configurations of phase two negotiations. IpsecConf ig.IpsecEncAlg: The encryption algorithm of phase two negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm of phase two negotiations. Valid values: md5 \| sha1. Default value: md5. IpsecConf ig. IpsecPf s: The Diffie- Hellman group for perfect forward secrecy (PFS). The Diffie-Hellman key exchange algorithm used by phase two negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IpsecConf ig. IpsecLif et ime: The SA lifetime value resulting from phase two negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp15oes1py4i6**** | The ID of the IPsec-VPN connection. |
| CreateTime | Long | 1544666102000 | The time when the IPsec-VPN connection was created. |
| Name | String | test | The name of the IPsec-VPN connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 082AD562-B8DB- 4BB2-861F- DA1FCA01FD76 | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=CreateVpnConnection &CustomerGatewayId=vpn-bp1q8bgx4xnk**** &LocalSubnet=1.1.1.0/24,1.1.2.0/24 &RegionId=cn-shanghai &RemoteSubnet=1.1.1.0/24,1.1.2.0/24 &VpnGatewayId=vpn-bp1q8bgx4xnkm**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateVpnConnectionResponse>
      <VpnConnectionId>vco-bp1bbi27hojx8****</VpnConnectionId>
      <CreateTime>1493363928000</CreateTime>
</CreateVpnConnectionResponse>
```

`JSON` format `{`

```json
 "VpnConnectionId":"vco-bp15oes1py4i6****",
 "CreateTime":1544666102000
```

`}`

### 8.2 ModifyVpnConnectionAttribute

You can call this operation to modify the configuration of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnConne ctionAttribute | The operation that you want to perform. Set the value to Modif yVpnConnect ionAt t ribut e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically publish routes. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| EffectImmediatel y | Boolean | No | false | Specifies whether to delete a successfully negotiated IPsec-VPN tunnel and initiate a negotiation again. Valid values: t rue: Negotiate immediately after the configuration is completed. f alse (default): Negotiate when inbound traffic is detected. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | ikev1, ikev2 | The configurations of phase one negotiations. IkeConf ig.Psk: The pre-shared key used for authentication between the IPsec-VPN gateway and the customer gateway. By default, the parameter value is generated randomly. You can also specify a pre-shared key. It can contain up to 100 characters. IkeConf ig.IkeVersion: The version of the IKE protocol. Valid values: ikev1 \| ikev2. Default value: ikev1. IkeConf ig.IkeMode: The negotiation mode of IKE V1. Valid values: main \| aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm of phase one negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm of phase one negotiations. Valid values: md5 \| sha1. Default value: sha. IkeConfig.IkePfs: The Diffie-Hellman key exchange algorithm used by phase one negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IkeConf ig.IkeLif et ime: The SA lifetime resulting from phase one negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: The identification of the VPN gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the VPN gateway. IkeConf ig.Remot eId: The identification of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description The configurations of phase two |
|---|---|---|---|---|
| IpsecConfig | String | No | sha1 | negotiation. IpsecConf ig.IpsecEncAlg: The encryption algorithm of phase two negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm of phase two negotiations. Valid values: md5 \| sha1. Default value: sha1. IpsecConf ig. IpsecPf s: The Diffie- Hellman group for perfect forward secrecy (PFS). The Diffie-Hellman key exchange algorithm used by phase two negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IpsecConf ig. IpsecLif et ime: The SA lifetime value resulting from phase two negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. |
| LocalSubnet | String | No | 1.1.1.0/24,1.1.2.0 /24 | The CIDR block of the VPC to be connected with the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ |
|   |   |   |   | hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| RemoteSubnet | String | No | 1.1.1.0/24,1.1.2.0 /24 | The CIDR block of the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |
| CustomerGate wayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| Name | String | test | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the VPC. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the on-premises data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |
| Description | String | description | The description of the IPsec-VPN connection. |
| EffectImmediat ely | Boolean | false | Indicates whether the IPsec-VPN connection takes effect immediately. |
| IkeConfig |   |   | The configurations of phase one negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. Valid values: main and aggressive.The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IkePfs | String | group2 | The DH group. Valid values: group1, group2, group5, group14, and group24. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.62.69.64 | The local ID. By default, it is the IP address of the VPN gateway. Both FQDN and IP formats are supported. |
| Psk | String | pgw6dy7d1i8in7x5 | The pre-shared key. |
| RemoteId | String | 139.196.32.167 | The peer ID. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The configurations of phase two negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | 7DB79D0C-5F27- 4AB5-995B- 79BE55102F90 | The ID of the request. |
| VcoHealthChec k |   |   | The health check configurations. |
| Dip | String | 1.1.1.xx | The destination IP address configured for health checks. |
| Enable | String | true | Indicates whether health checks are enabled. t rue: Health checks are enabled. f alse: Health checks are disabled. |

| PN Gateway |   |   | Developer Guide·IPsec-VP |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Interval | Integer | 3 | The time interval between two consecutive health check retries. Unit: seconds. |
| Retry | Integer | 1 | The number of attempts for resending health check probes. |
| Sip | String | 2.2.2.xx | The source IP address configured for health checks. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyVpnConnectionAttribute &RegionId=cn-shanghai &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifyVpnConnectionAttributeResponse>
      <Name>VPN connection tsst</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RemoteSubnet>2.2.2.0/24</RemoteSubnet>
      <IpsecConfig>
            <IpsecLifetime>86400</IpsecLifetime>
            <IpsecAuthAlg>sha1</IpsecAuthAlg>
            <IpsecPfs>group2</IpsecPfs>
            <IpsecEncAlg>aes</IpsecEncAlg>
      </IpsecConfig>
      <EffectImmediately>false</EffectImmediately>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <CreateTime>1492753817000</CreateTime>
      <VpnConnectionId>vco-bp10lz7aejumd2vxo****</VpnConnectionId>
      <RequestId>57070A3D-38F2-40A6-A1C9-DB14542EF54D</RequestId>
      <LocalSubnet>1.1.1.0/24,1.1.2.0/24</LocalSubnet>
      <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.196.32.xx</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy7d1i8i****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.62.69.xx</LocalId>
      </IkeConfig>
</ModifyVpnConnectionAttributeResponse>
```

`JSON` format `{`

```json
 "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
 "Name":"VPN connection test",
 "RemoteSubnet":"2.2.2.0/24",
 "IpsecConfig":{
  "IpsecLifetime":86400,
  "IpsecAuthAlg":"sha1",
  "IpsecPfs":"group2",
  "IpsecEncAlg":"aes"
```

`},`

```json
 "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
 "EffectImmediately":false,
 "RequestId":"7DB79D0C-5F27-4AB5-995B-79BE55102F90",
 "VpnConnectionId":"vco-bp10lz7aejumd2vxo****",
 "CreateTime":1492753817000,
 "LocalSubnet":"1.1.1.0/24,1.1.2.0/24",
 "IkeConfig":{
  "IkeEncAlg":"aes",
  "IkePfs":"group2",
  "RemoteId":"139.196.32.xx",
  "IkeAuthAlg":"sha1",
  "Psk":"pgw6dy7d1i8i****",
  "IkeMode":"main",
  "IkeLifetime":86400,
  "IkeVersion":"ikev1",
  "LocalId":"116.62.69.xx"
```

`}` `}`

### 8.3 DescribeVpnConnections

Queries one or more IPsec-VPN connections. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConn ections | The operation that you want to perform. Set the value to DescribeVpnConnect ions. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CustomerGatewa yId | String | No | cgw- bp1mvj4g9kogw* *** | The ID of the customer gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10 |
| VpnConnectionId | String | No | vco- bp15oes1py4i6** ** | The ID of the IPsec-VPN connection. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkx** ** | The ID of the VPN gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnection s |   |   | The details of the IPsec-VPN connections. |
| IkeConfig |   |   | The configurations of phase-one negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. Both the main mode and aggressive mode are supported. The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IkePfs | String | group2 | The Diffie-Hellman (DH) group. Valid values: group1 \| group2 \| group5 \| group14 \| group24 |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.xx.xx.64 | The local ID of the VPN gateway. The default value is the IP address of the VPN gateway. Both fully qualified domain name (FQDN) and IP address formats are supported. |
| Psk | String | pgw6dy7dxxxxxxxx | The pre-shared key. |
| RemoteId | String | 139.xx.xx.167 | The ID of the peer. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The configurations of phase two negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| VpnConnectionI d | String | vco- bp10lz7aejumd**** | The ID of the IPsec-VPN connection. |
| CustomerGate wayId | String | vpn- bp1q8bgx4xnk**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm**** | The ID of the VPN gateway. |
| Name | String | name | The name of the IPsec-VPN connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the VPC. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the on-premises data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |
| Status | String | ipsec sa establishe _ _ d | The status of the connection. Valid values: ike sa not est ablished: Phase one _ _ _ negotiations failed. ike sa est ablished: Phase one _ _ negotiations were successful. ipsec sa not est ablished: Phase two _ _ _ negotiations failed. ipsec sa est ablished: Phase two _ _ negotiations were successful. |
| EffectImmediat ely | Boolean | true | Indicates whether the connection takes effect immediately. t rue: A reconnection is triggered when the configuration is changed. f alse: A reconnection is triggered when network traffic is detected. Reconnections may cause transient disconnections. |
| VcoHealthChec k |   |   | Details of health checks. |
| Dip | String | 8.xx.xx.8 | The destination IP address configured for health checks. |
| Interval | Integer | 2 | The interval between two consecutive health checks. Unit: seconds. |
| Sip | String | 192.xx.xx.66 | The source IP address configured for health checks. |
| TotalCount | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The number of the page returned. |

| PN Gateway |   |   | Developer Guide·IPsec-VP |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 54A4B3D0-DF4D- 4C54-B8DC- 5DC8DD49C939 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeVpnConnections &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnConnections>
   <PageNumber>1</PageNumber>
   <VpnConnections>
      <VpnConnection>
         <Name>VPN connection test</Name>
         <CustomerGatewayId>cgw-bp1pvpl9r9adjxxxxxxxx</CustomerGatewayId>
         <RemoteSubnet>2.2.2.0/24</RemoteSubnet>
         <IpsecConfig>
            <IpsecLifetime>86400</IpsecLifetime>
            <IpsecAuthAlg>sha1</IpsecAuthAlg>
            <IpsecPfs>group2</IpsecPfs>
            <IpsecEncAlg>aes</IpsecEncAlg>
         </IpsecConfig>
         <EffectImmediately>true</EffectImmediately>
         <VpnGatewayId>vpn-bp1q8bgx4xnkmxxxxxxxx</VpnGatewayId>
         <CreateTime>1492753817000</CreateTime>
         <VpnConnectionId>vco-bp10lz7aejumdxxxxxxxx</VpnConnectionId>
         <status>ipsec_sa_established</status>
         <LocalSubnet>1.1.1.0/24,1.1.2.0/24</LocalSubnet>
         <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.xx.xx.167</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dyxxxxxxxx</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.xx.xx.64</LocalId>
         </IkeConfig>
      </VpnConnection>
   </VpnConnections>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939</RequestId>
</DescribeVpnConnections>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "VpnConnections":{
  "VpnConnection":[
```

`{`

```json
    "CustomerGatewayId":"cgw-bp1pvpl9r9adjxxxxxxxx",
    "Name": "VPN connection test",
    "RemoteSubnet":"2.2.2.0/24",
    "IpsecConfig":{
     "IpsecLifetime":86400,
     "IpsecAuthAlg":"sha1",
     "IpsecPfs":"group2",
     "IpsecEncAlg":"aes"
```

`},`

```json
    "VpnGatewayId":"vpn-bp1q8bgx4xnkmxxxxxxxx",
    "EffectImmediately":true,
    "status":"ipsec_sa_established",
    "VpnConnectionId":"vco-bp10lz7aejumdxxxxxxxx",
    "CreateTime":1492753817000,
    "LocalSubnet":"1.1.1.0/24,1.1.2.0/24",
    "IkeConfig":{
     "IkeEncAlg":"aes",
     "IkePfs":"group2",
     "RemoteId":"139.xx.xx.167",
     "IkeAuthAlg":"sha1",
     "Psk":"pgw6dyxxxxxxxx",
     "IkeMode":"main",
     "IkeLifetime":86400,
     "IkeVersion":"ikev1",
     "LocalId":"116.xx.xx.64"
```

`}` `}` `]` `},`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939"
```

`}`

### 8.4 DescribeVpnConnection

You can call this operation to query the details of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConn ection | The operation that you want to perform. Set the value to DescribeVpnConnect ion. |

| D | eveloper Guide·IPse | c-VPN |   |   | VPN Gatewa | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |
| CustomerGate wayId | String | cgw- bp1mvj4g9kogwwcx k**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| Name | String | ipsec1 | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the VPC. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the on-premises data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | ike sa not establish _ _ _ ed | The status of the connection. Valid values: ike sa not est ablished indicates that _ _ _ phase one negotiations failed. ike sa est ablished indicates that phase _ _ one negotiations were successful. ipsec sa not est ablished indicates _ _ _ that phase two negotiations failed. ipsec sa est ablished indicates that _ _ phase two negotiations were successful. |
| EffectImmediat ely | Boolean | true | Indicates whether the IPsec-VPN connection takes effect immediately. Valid values: t rue: Reconnection is triggered when the configuration is changed. f alse: Reconnection is triggered when network traffic is detected. Reconnection may cause intermittent disconnection. |
| IkeConfig |   |   | The configurations for phase one negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. Both main and aggressive modes are supported. The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.62.69.xxx | The ID of the server end. By default, it is the IP address of the VPN gateway. Both FQDN and IP formats are supported. |

| eveloper Guide·IPs | ec-VPN |   | VPN Gatewa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Psk | String | pgw6dy7d1i8in7x5 | The pre-shared key. |
| RemoteId | String | 139.196.32.xxx | The peer ID. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The configurations for phase two negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | F2310D45-BCF6- 4E2E-9082- B4503844BA4C | The ID of the request. |
| VcoHealthChec k |   |   | The health check information. |
| Dip | String | 10.0.0.xx | The destination IP address specified for health checks. |
| Enable | String | true | Indicates whether health checks are enabled. Valid values: f alse: Indicates that health checks are disabled. t rue: Indicates that health checks are enabled. |
| Interval | Integer | 3 | The time interval of health check retries. Unit: Second. |
| Retry | Integer | 3 | The maximum number of attempts for resending health check probes. |

| PN Gateway |   |   | Developer Guide·IPsec-VP |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Sip | String | 192.168.1.xx | The source IP address specified for health checks. |
| Status | String | failed | The status of the health check. Valid values: |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeVpnConnection &RegionId=cn-hangzhou &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeVpnConnectionResponse>
      <PageNumber>1</PageNumber>
      <VpnConnections>
            <VpnConnection>
                  <Name>c2</Name>
                  <CustomerGatewayId>cgw-bp1wl8dtz3auwlav****</CustomerGatewayId>
                  <Status>ike_sa_not_established</Status>
                  <RemoteSubnet>192.168.0.0/16</RemoteSubnet>
                  <IpsecConfig>
                        <IpsecLifetime>86400</IpsecLifetime>
                        <IpsecAuthAlg>md5</IpsecAuthAlg>
                        <IpsecPfs>group2</IpsecPfs>
                        <IpsecEncAlg>aes</IpsecEncAlg>
                  </IpsecConfig>
                  <EffectImmediately>false</EffectImmediately>
                  <VpnGatewayId>vpn-bp1yfrjxn4d5t63tb****</VpnGatewayId>
                  <CreateTime>1519391420000</CreateTime>
                  <VpnConnectionId>vco-bp1w3m1p23iftycvs****</VpnConnectionId>
                  <LocalSubnet>172.16.0.0/12</LocalSubnet>
                  <IkeConfig>
                        <IkeEncAlg>aes</IkeEncAlg>
                        <RemoteId>47.97.176.xxx</RemoteId>
                        <IkePfs>group2</IkePfs>
                        <IkeAuthAlg>sha1</IkeAuthAlg>
                        <Psk>1234567</Psk>
                        <IkeMode>aggressive</IkeMode>
                        <IkeLifetime>86400</IkeLifetime>
                        <IkeVersion>ikev1</IkeVersion>
                        <LocalId>116.62.119.xxx</LocalId>
                  </IkeConfig>
            </VpnConnection>
      </VpnConnections>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>7D598A10-26EF-44F2-9F47-E417842F3CEA</RequestId>
</DescribeVpnConnectionResponse>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "VpnConnections":{
  "VpnConnection":[
```

`{`

```json
    "CustomerGatewayId":"cgw-bp1wl8dtz3auwlavw****",
    "Name":"c2",
    "Status":"ike_sa_not_established",
    "RemoteSubnet":"192.168.0.0/16",
    "IpsecConfig":{
     "IpsecLifetime":86400,
     "IpsecAuthAlg":"md5",
     "IpsecPfs":"group2",
     "IpsecEncAlg":"aes"
```

`},`

```json
    "VpnGatewayId":"vpn-bp1yfrjxn4d5t63t****",
    "EffectImmediately":false,
    "VpnConnectionId":"vco-bp1w3m1p23iftycv****",
    "CreateTime":1519391420000,
    "LocalSubnet":"172.16.0.0/12",
    "IkeConfig":{
     "IkeEncAlg":"aes",
     "IkePfs":"group2",
     "RemoteId":"47.97.176.xxx",
     "IkeAuthAlg":"sha1",
     "Psk":"1234567",
     "IkeMode":"aggressive",
     "IkeLifetime":86400,
     "IkeVersion":"ikev1",
     "LocalId":"116.62.119.xxx"
```

`}` `}` `]` `},`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"7D598A10-26EF-44F2-9F47-E417842F3CEA"
```

`}`

### 8.5 DownloadVpnConnectionConfig

You can call this operation to obtain the configuration information of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DownloadVpnCo nnectionConfig | The operation that you want to perform. Set the value to DownloadVpnConnect ionConf ig. |

| D | eveloper Guide·IPse | c-VPN |   |   | VPN Gatewa | y |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The name of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0C68048B-0F70- 40DA-B8AE- 1B79B5CF62E3 | The ID of the request. |
| VpnConnection Config |   |   | The configuration of the IPsec-VPN connection. |
| IkeConfig |   |   | The IKE configurations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. Both main and aggressive modes are supported. The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LocalId | String | 116.62.69.xx | The ID of the server end. By default, it is the IP address of the VPN gateway. Both FQDN and IP formats are supported. |
| Psk | String | pgw6dy7d1i8i**** | The pre-shared key. |
| RemoteId | String | 139.196.32.xx | The peer ID. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The IPsec configurations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| Local | String | 139.196.32.xx | The ID of the IPsec VPN gateway. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the VPC. |
| Remote | String | 116.62.69.xx | The ID of the customer gateway. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/2 4 | The CIDR block of the on-premises data center. |

Examples Sample requests

```
https://vpc.example.com/?Action=DownloadVpnConnectionConfig &RegionId=cn-shanghai &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DownloadVpnConnectionConfigResponse>
      <RequestId>6F4A035F-7060-45D7-B9BD-719372782AF6</RequestId>
      <VpnConnectionConfig>
            <RemoteSubnet>1.1.1.0/24,1.1.2.0/24</RemoteSubnet>
            <Local>139.196.32.xx</Local>
            <IpsecConfig>
                  <IpsecLifetime>86400</IpsecLifetime>
                  <IpsecAuthAlg>sha1</IpsecAuthAlg>
                  <IpsecPfs>group2</IpsecPfs>
                  <IpsecEncAlg>aes</IpsecEncAlg>
            </IpsecConfig>
            <Remote>116.62.69.xx</Remote>
            <LocalSubnet>2.2.2.0/24</LocalSubnet>
            <IkeConfig>
                  <IkeEncAlg>aes</IkeEncAlg>
                  <IkePfs>group2</IkePfs>
                  <RemoteId>116.62.69.xx</RemoteId>
                  <IkeAuthAlg>sha1</IkeAuthAlg>
                  <Psk>pgw6dy7d1i8i****</Psk>
                  <IkeMode>main</IkeMode>
                  <IkeLifetime>86400</IkeLifetime>
                  <IkeVersion>ikev1</IkeVersion>
                  <LocalId>139.196.32.xx</LocalId>
            </IkeConfig>
      </VpnConnectionConfig>
</DownloadVpnConnectionConfigResponse>
```

`JSON` format `{`

```json
 "RequestId":"0C68048B-0F70-40DA-B8AE-1B79B5CF62E3",
 "VpnConnectionConfig":{
  "RemoteSubnet":"1.1.1.0/24,1.1.2.0/24",
  "IpsecConfig":{
   "IpsecLifetime":86400,
   "IpsecAuthAlg":"sha1",
   "IpsecPfs":"group2",
   "IpsecEncAlg":"aes"
```

`},`

```json
  "Local":"139.196.32.xx",
  "Remote":"116.62.69.64",
  "LocalSubnet":"2.2.2.0/24",
  "IkeConfig":{
   "IkeEncAlg":"aes",
   "RemoteId":"116.62.69.xx",
   "IkePfs":"group2",
   "IkeAuthAlg":"sha1",
   "Psk":"pgw6dy7d1i8i****",
   "IkeMode":"main",
   "IkeLifetime":86400,
   "IkeVersion":"ikev1",
   "LocalId":"139.196.32.xx"
```

`}` `}` `}`

### 8.6 DeleteVpnConnection

You can call this operation to delete an IPsec-VPN connection. After the IPsec-VPN connection is deleted, the connection between the VPC and the on-premises data center is closed. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnConnec tion | The operation that you want to perform. Set the value to Delet eVpnConnect ion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteVpnConnection &RegionId=cn-hangzhou &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteVpnConnectionResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteVpnConnectionResponse>
```

`JSON` format `{`

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}`

## 9 SSL-VPN

### 9.1 CreateSslVpnServer

You can call this operation to create an SSL server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnServ er | The operation that you want to perform. Set the value to Creat eSslVpnServer. |
| ClientIpPool | String | Yes | 192.168.1.0/24 | The CIDR block from which IP addresses are allocated to the virtual network interface of the client. It is not the CIDR block of the client. When the client accesses the server end through an SSL-VPN connection, the VPN gateway selects an IP address from the specified CIDR block and assigns it to the client. This CIDR block must not conflict with LocalSubnet . |
| LocalSubnet | String | Yes | 10.0.0.0/8 | The CIDR block to be accessed by the client through the SSL-VPN connection. You can set the value to the CIDR block of a VPC network, a VSwitch, an on- premises data center connected to the VPC through a leased line, or an Alibaba Cloud service, such as an ApsaraDB for RDS instance or OSS instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1hgim8by0kc9 nga**** | The ID of the VPN gateway. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm used by the SSL server. Valid values: AES-128-CBC (def ault ), AES-192- CBC, AES-256-CBC, and none |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to guarantee the idempotency of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | sslvpnname | The name of the SSL server. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Port | Integer | No | 1194 | The port used by the SSL server. Default value: 1194. The following ports are not supported: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500 |
| Proto | String | No | UDP | The protocol used by the SSL server. Valid values: UDP (def ault ) and T CP |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the SSL server. |
| RequestId | String | E98A9651-7098- 40C7-8F85- C818D1EBBA85 | The ID of the request. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v* *** | The ID of the SSL server. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=CreateSslVpnServer &ClientIpPool=192.168.1.0/24 &LocalSubnet=10.0.0.0/8 &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1hgim8by0kc9nga**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateSslVpnServerResponse>
  <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId>
  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
  <Name>test</Name>
</CreateSslVpnServerResponse>
```

`JSON` format `{`

```json
 "Name":"test",
 "RequestId":"E98A9651-7098-40C7-8F85-C818D1EBBA85",
 "SslVpnServerId":"vss-bp18q7hzj6largv4v****"
```

`}`

### 9.2 ModifySslVpnServer

You can call this operation to modify the configuration of an SSL server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnServ er | The operation that you want to perform. Set the value to Modif ySslVpnServer. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway associated with the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv 4v**** | The ID of the SSL server. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm used by the SSL server. Valid values: AES-128-CBC (def ault ), AES-192-CBC, AES-256- CBC, and none |
| ClientIpPool | String | No | 10.30.30.0/2 | The IP address pool of the client. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Compress | Boolean | No | false | Specifies whether to compress the communication. Valid values: t rue (def ault ) and f alse |
| LocalSubnet | String | No | 10.20.20.0/24 | The CIDR block of the local client. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | test | The name of the SSL server. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |
| Port | Integer | No | 1194 | The port used by the SSL server. Default value: 1194. The following ports cannot be used: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500 |
| Proto | String | No | UDP | The protocol used by the SSL server. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cipher | String | AES-128-CBC | Indicates the encryption algorithm used. |
| ClientIpPool | String | 10.30.30.0/24 | The IP address pool of the client. |
| Compress | Boolean | false | Indicates whether the communication is compressed. |
| Connections | Integer | 0 | The total number of current connections. |
| CreateTime | Long | 1492753580000 | The time when the SSL server was created. |
| InternetIp | String | 47.98.xx.xx | The public IP address of the VPN gateway. |
| LocalSubnet | String | 10.20.20.0/24 | The CIDR block of the local client. |
| MaxConnection s | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL server. |

| PN Gateway |   |   | Developer Guide·SSL-VP |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Port | Integer | 1194 | The port of the SSL server. |
| Proto | String | UDP | The protocol used by the SSL server. |
| RegionId | String | cn-hangzhou | The region ID of the SSL server. |
| RequestId | String | DF11D6F6-E35A- 41C3-9B20- 6FC8A901FE65 | The ID of the request. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v* *** | The ID of the SSL server. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifySslVpnServer &RegionId=cn-hangzhou &SslVpnServerId=vss-bp18q7hzj6largv4**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifySslVpnServerResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-hanghzou</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.30.30.0/24</CLientIpPool>
                  <LocalSubnet>10.20.20.0/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.98.xx.xx</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</ModifySslVpnServerResponse>
```

`JSON` format `{`

```json
 "PageNumber":"1",
 "TotalCount":"1",
 "SslVpnServers":{
  "SslVpnServer":{
   "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
   "CLientIpPool":"10.30.30.0/24",
   "Proto":"UDP",
   "Cipher":"AES-128-CBC",
   "InternetIp":"47.98.xx.xx",
   "SslVpnServerId":"vss-bp18q7hzj6largv4v****",
   "Name":"test",
   "Port":"1194",
   "MaxConnections":"5",
   "RegionId":"cn-hanghzou",
   "CreateTime":"1492753580000",
   "Compress":"true",
   "LocalSubnet":"10.20.20.0/24",
   "Connections":"0"
```

`}` `},`

```json
 "PageSize":"10",
 "RequestId":"DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

`}`

### 9.3 DescribeSslVpnServers

You can call this operation to query one or more SSL servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnSe rvers | The operation that you want to perform. Set the value to DescribeSslVpnServers. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | test | The name of the SSL server. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| SslVpnServerId | String | No | vss- bp15j3du13gq1d gey**** | The ID of the SSL server. |
| VpnGatewayId | String | No | vpn- bp1on0xae9d771 ggi**** | The ID of the VPN gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 085CA5EA-1E76- 43A8-981B- E0208DECA0CB | The ID of the request. |
| SslVpnServers |   |   | Details of the SSL server. |
| Cipher | String | AES-128-CBC | The encryption algorithm used. |
| ClientIpPool | String | 10.10.1.0/24 | The IP address pool of the client. |
| Compress | Boolean | false | Indicates whether the communication is compressed. |
| Connections | Integer | 0 | The total number of active connections. |
| CreateTime | Long | 1544668844000 | The time when the SSL server was created. |
| InternetIp | String | 47.96.167.xxx | The public IP address. |
| LocalSubnet | String | 192.168.0.0/24 | The CIDR block of the local client. |
| MaxConnection s | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL server. |
| Port | Integer | 1194 | The port used by the SSL server. |
| Proto | String | UDP | The protocol used by the SSL server. |
| RegionId | String | cn-hangzhou | The region ID of the SSL server. |
| SslVpnServerId | String | vss- bp15j3du13gq1dgey **** | The ID of the SSL server. |
| VpnGatewayId | String | vpn- bp1on0xae9d771ggi **** | The ID of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
https://vpc.example.com/?Action=DescribeSslVpnServers &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-hanghzou</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.10.10.20/24</CLientIpPool>
                  <LocalSubnet>10.10.10.10/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.98.xx.xx</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
 "PageNumber":"1",
 "TotalCount":"1",
 "SslVpnServers":{
  "SslVpnServer":{
   "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
   "CLientIpPool":"10.10.10.20/24",
   "Proto":"UDP",
   "Cipher":"AES-128-CBC",
   "InternetIp":"47.98.xx.xx",
   "SslVpnServerId":"vss-bp18q7hzj6largv4v****",
   "Name":"test",
   "Port":"1194",
   "MaxConnections":"5",
   "RegionId":"cn-hanghzou",
   "CreateTime":"1492753580000",
   "Compress":"true",
   "LocalSubnet":"10.10.10.10/24",
   "Connections":"0"
```

`}` `},`

```json
 "PageSize":"10",
 "RequestId":"DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

`}`

### 9.4 DeleteSslVpnServer

You can call this operation to delete an SSL server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnServ er | The operation that you want to perform. Set the value to Delet eSslVpnServer. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv 4v**** | The ID of the SSL server. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteSslVpnServer &RegionId=cn-hangzhou &SslVpnServerId=vss-bp18q7hzj6largv4v**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteSslVpnServerResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnServerResponse>
```

`JSON` format `{`

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}`

### 9.5 CreateSslVpnClientCert

You can call this operation to create an SSL client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnClie ntCert | The operation that you want to perform. Set the value to Creat eSslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- m5et0q3iy1qex32 8w**** | The ID of the SSL server. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | SslVpnClientCert1 | The name of the client certificate. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | SslVpnClientCert | The name of the client certificate. |
| RequestId | String | 079874CD-AEC1- 43E6-AC03- ADD96B6E4907 | The ID of the request. |
| SslVpnClientCer tId | String | vsc- m5euof6s5jy8vs5kd* *** | The ID of the client certificate. |

Examples Sample requests

```
https://vpc.example.com/?Action=CreateSslVpnClientCert &RegionId=cn-hangzhou &SslVpnServerId=vss-m5et0q3iy1qex328w**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<CreateSslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</CreateSslVpnClientCertResponse>
```

`JSON` format `{`

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA",
 "SslVpnClientCertId":"vsc-bp1n8wcf134yl0osr****"
```

`}`

### 9.6 ModifySslVpnClientCert

You can call this operation to modify the name of an SSL client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnClie ntCert | The operation that you want to perform. Set the value to Modif ySslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificate. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertI d | String | Yes | vsc- bp1n8wcf134yl0 osrc**** | The ID of the SSL client certificate. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | cert2 | The name of the SSL client certificate. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | cert2 | The name of the client certificate. |
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |
| SslVpnClientCer tId | String | vsc- bp1n8wcf134yl0osr* *** | The ID of the SSL client certificate. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifySslVpnClientCert &RegionId=cn-hangzhou &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr**** &Name=cert2 &<Common request parameters>
```

Sample responses `XML` format

```xml
<ModifySslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <Name>cert2</Name>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</ModifySslVpnClientCertResponse>
```

`JSON` format `{`

```json
 "Name":"cert2",
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA",
 "SslVpnClientCertId":"vsc-bp1n8wcf134yl0osr****"
```

`}`

### 9.7 DescribeSslVpnClientCerts

You can call this operation to query one or more SSL client certificates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnCli entCerts | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert s. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificates to be queried. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | cert1 | The name of the SSL client certificate. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| SslVpnClientCertI d | String | No | vsc- bp1n8wcf134yl0 osr**** | The name of the SSL client certificate. |

| eveloper Guide·SSL- | VPN |   |   | VPN Gatewa |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SslVpnServerId | String | No | vss- bp18q7hzj6largv 4v**** | The ID of the SSL server. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| SslVpnClientCer tKeys | Array |   | The details of the queried SSL client certificates. |
| SslVpnClientCer tKey |   |   | The details of the queried SSL client certificate. |
| CreateTime | Long | 1492747187000 | The time when the SSL client certificate was created. |
| EndTime | Long | 1494966335000 | The time when the SSL client certificate expires. |
| Name | String | cert1 | The name of the SSL client certificate. |
| RegionId | String | cn-hangzhou | The region ID of the SSL client certificate. |
| SslVpnClientCer tId | String | vsc- bp1n8wcf134yl0osr* *** | The ID of the SSL client certificate. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v* *** | The ID of the SSL server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | normal | The status of the client certificate. expiring-soon: The certificate will expire in one week. normal: The certificate is in a normal state. expired: The certificate has expired. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=DescribeSslVpnClientCerts &RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-hanghzou</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.10.10.20/24</CLientIpPool>
                  <LocalSubnet>10.10.10.10/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.98.xx.xx</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
 "DescribeSslVpnServersResponse":{
  "PageNumber":"1",
  "TotalCount":"1",
  "SslVpnServers":{
   "SslVpnServer":{
    "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
    "CLientIpPool":"10.10.10.20/24",
    "Proto":"UDP",
    "Cipher":"AES-128-CBC",
    "InternetIp":"47.98.xx.xx",
    "SslVpnServerId":"vss-bp18q7hzj6largv4v****",
    "Name":"test",
    "Port":"1194",
    "MaxConnections":"5",
    "RegionId":"cn-hanghzou",
    "CreateTime":"1492753580000",
    "Compress":"true",
    "LocalSubnet":"10.10.10.10/24",
    "Connections":"0"
```

`}` `},`

```json
  "PageSize":"10",
  "RequestId":"DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

`}` `}`

### 9.8 DescribeVpnSslServerLogs

You can call this operation to query the logs of an SSL server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnSslSe rverLogs | The operation that you want to perform. Set the value to DescribeVpnSslServerLogs. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| VpnSslServerId | String | Yes | vss- bp155e9yclsg1xg q4**** | The name of the SSL server. |
| From | Integer | No | 2018020201 | The start time of the logs to be queried. |

| PN Gateway |   |   |   | Developer Guide·SSL-VP |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MinutePeriod | Integer | No | 10 | The recording cycle of the logs. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| To | Integer | No | 2018020206 | The end time of the logs to be queried. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of log entries. |
| Data |   | test | An array of log entries. Each item in the array indicates a log entry. |
| IsCompleted | Boolean | true | Indicates whether the log is accurate. Valid values: t rue: accurate f alse: inaccurate |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.example.com/? Action=DescribeVpnSslServerLogs &RegionId=cn-hangzhou &VpnSslServerId=vss-bp155e9yclsg1xgq4**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DescribeVpnSslServerLogsResponse>
   <Data></Data>
   <PageNumber>1</PageNumber>
   <Count>0</Count>
   <PageSize>10</PageSize>
   <IsCompleted>true</IsCompleted>
   <RequestId>26641E42-66C7-4942-9FEC-F99213914F8F</RequestId>
</DescribeVpnSslServerLogsResponse>
```

`JSON` format `{`

```json
 "PageNumber":1,
 "Data":{
  "Logs":[]
```

`},`

```json
 "Count":0,
 "IsCompleted":true,
 "PageSize":10,
 "RequestId":"26641E42-66C7-4942-9FEC-F99213914F8F"
```

`}`

### 9.9 DeleteSslVpnClientCert

You can call this operation to delete an SSL client certificate. Request Parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnClie ntCert | The operation that you want to perform. Set the value to Delet eSslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificate. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertI d | String | Yes | vsc- bp1n8wcf134yl0 osr**** | The ID of the SSL client certificate. |

| PN Gateway |   |   |   | Developer Guide·SSL-VP |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=DeleteSslVpnClientCert &RegionId=cn-hangzhou &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr**** &<Common request parameters>
```

Sample responses `XML` format

```xml
<DeleteSslVpnClientCertResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnClientCertResponse>
```

`JSON` format `{`

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` ng ASAPI

## 10 Call VPC SDK by using ASAPI

### 10.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize operations and audit and manage their calls. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, avoiding inconsistent operations caused by different call methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a unified manner and customize development. ASAPI supports access of most cloud services deployed in Apsara Stack and passthrough or encapsulation of different backend APIs. This way, operations can be called with the same method. ASAPI allows you to use SDKs and API Portal to call APIs registered in ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs. ng ASAPI

### 10.2 Log on to the API Tool console

You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 10.3 View the information about API operations

operations You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API
operation name in the search box, and then click the search icon. ng ASAPI
4. View and remember the service name, API operation name, and API version.

### 10.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), ng ASAPI dollar signs ($), and percent signs (%). It must be 10 to 20 characters in length.
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
of the Apsara ASAPI Management platform. ng ASAPI

### 10.5 Obtain the core package for ASAPI

ASAPI Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 10.6 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain the AccessKey pair of an organization. Prerequisites Only operations administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the Apsara Stack Cloud Management (ASCM) console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the message that appears, view the AccessKey pair of the organization.
ng ASAPI Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. They allow you to access Apsara Stack resources with full permissions for your account. You must keep them confidential.

### 10.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

### 10.8 SDK for Java

This topic describes how to obtain and use Apsara Stack SDK for Java. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Apsara Stack SDK for Java. For more information about how to obtain and view your AccessKey pair in the Apsara Stack Cloud Management (ASCM) console, see Obtain an AccessKey pair. You have obtained the endpoint of ASAPI. For more information about how to obtain the endpoint of Apsara Stack API (ASAPI), see Obtain the endpoint of Asapi. ng ASAPI Apsara Stack SDK for Java supports JDK 1.6 and later. Add dependencies Add dependencies to pom.xml:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Work with Apsara Stack SDK for Java You can call API operations on ASAPI by sending GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Format 1 String result = client.doGet(endpoint, parameters); // Format 2 String result = client.doRequest(endpoint, parameters);
```

POST requests ng ASAPI

```java
public class DescribeVpnGateways {
    public static void main(String[] args) {
        // Obtain the endpoint of ASAPI.
        String endpoint = "http://xxx/asapi/v3";
    // Set request parameters.
    Map<String, String> parameters = new HashMap<String, String>();
    // Set service parameters.
    parameters.put("Product", "ascm");            // The service name must be the same as
the name displayed in the corresponding API directory.
    parameters.put("Action", "DescribeVpnGateways"); // The API operation that you want t
o perform. It must be the same as that in the API directory.
    parameters.put("Version", "2016-04-28");      // The API version.
    // Set authorization-related parameters.
    parameters.put("AccessKeyId", "<your-access-key-id>");          // The AccessKey ID o
f the authorized account.
    parameters.put("AccessKeySecret", "<your-access-key-secret>");  // The AccessKey secr
et of the authorized account.
    // Set connection parameters.
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

### 10.9 SDK for Node.js

This topic describes how to obtain and use Apsara Stack SDK for Node.js. Prerequisites You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Apsara Stack SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add dependencies
1. Install Apsara Stack SDK for Node.js

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on eggjs, you must add the following content to mocha.opts:
ng ASAPI

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Work with Apsara Stack SDK for Node.js The following example shows the three steps to call Apsara Stack SDK for Node.js:
1. Create an ASClient instance. When you create an ASClient instance, set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'the region ID',
    API_GATEWAY: 'the endpoint of ASAPI'.
    accessKeyId: 'the AccessKey ID'.
    accessKeySecret: 'the AccessKey secret'.
```

`},`
2. Create an API request and configure the parameters.
3. Initiate the request and handle any responses or exceptions.

```
// Specify the ASAPI endpoint. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'DescribeVpnGateways',
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

### 10.10 Use SDK for POP through ASAPI (optional)

(optional) If an application used Apsara Stack SDK for POP to call cloud services, you must switch the gateway to ASAPI by performing the following steps: Procedure ng ASAPI
1. Switch the gateway to ASAPI and add common parameters required by the API operation to the
request header, so the API operation can be called in a transparent manner.
2. Add the Product Name field to the request header.
Sample code The following code provides an example on how to use Apsara Stack SDK for POP to call VPN Gateway API operations.

```java
try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessK
eySecret);
    // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "ecs", "<Asapi gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
    DescribeVpnGatewaysRequest request = new DescribeVpnGatewaysRequest();
    request.setSysRegionId(regionId); // Or setRegionId(regionId)
    // Set common parameters based on the information about the current user account.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    DescribeVpnGatewaysResponse result = (DescribeVpnGatewaysResponse) acsClient.getAcsResp
onse(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```

`}`
