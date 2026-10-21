---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Virtual Private Cloud Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 303
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Virtual Private Cloud Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Virtual%20Private%20Cloud%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Virtual Private Cloud Developer Guide 20220928

## Table of Contents

- 1 API reference
  - 1.1 List of API operations by function
  - 1.2 Call VPC APIs
    - 1.2.1 Request syntax
    - 1.2.2 API authorization
    - 1.2.3 Signature method
  - 1.3 RAM authentication
  - 1.4 Common parameters
  - 1.5 VPC
    - 1.5.1 CreateVpc
    - 1.5.2 DeleteVpc
    - 1.5.3 DescribeVpcs
    - 1.5.4 ModifyVpcAttribute
    - 1.5.5 DescribeVpcAttribute
  - 1.6 VRouter
    - 1.6.1 DescribeVRouters
    - 1.6.2 ModifyVRouterAttribute
  - 1.7 VSwitch
    - 1.7.1 CreateVSwitch
    - 1.7.2 DeleteVSwitch
    - 1.7.3 ModifyVSwitchAttribute
    - 1.7.4 DescribeVSwitches
    - 1.7.5 DescribeVSwitchAttributes
  - 1.8 Routing table
    - 1.8.1 CreateRouteEntry
    - 1.8.2 DeleteRouteEntry
    - 1.8.3 DescribeRouteTables
  - 1.9 Elastic IP Address (EIP)
    - 1.9.1 AllocateEipAddress
    - 1.9.2 AllocateEipAddressPro
    - 1.9.3 AssociateEipAddress
    - 1.9.4 UnassociateEipAddress
    - 1.9.5 ModifyEipAddressAttribute
    - 1.9.6 ReleaseEipAddress
    - 1.9.7 DescribeEipAddresses
    - 1.9.8 DescribeEipMonitorData
    - 1.9.9 MoveResourceGroup
    - 1.9.10 DescribeHighDefinitionMonitorLogAttribute
  - 1.10 Router interface
    - 1.10.1 ConnectRouterInterface
    - 1.10.2 DeactivateRouterInterface
    - 1.10.3 ModifyRouterInterfaceSpec
    - 1.10.4 DeleteRouterInterface
    - 1.10.5 DescribeRouterInterfaces
    - 1.10.6 ActivateRouterInterface
    - 1.10.7 ModifyRouterInterfaceAttribute
    - 1.10.8 CreateRouterInterface
  - 1.11 Physical connection
    - 1.11.1 CreatePhysicalConnection
    - 1.11.2 CancelPhysicalConnection
    - 1.11.3 DeletePhysicalConnection
    - 1.11.4 ModifyPhysicalConnectionAttribute
    - 1.11.5 DescribePhysicalConnections
    - 1.11.6 TerminatePhysicalConnection
    - 1.11.7 EnablePhysicalConnection
  - 1.12 Virtual border router
    - 1.12.1 CreateVirtualBorderRouter
    - 1.12.2 DeleteVirtualBorderRouter
    - 1.12.3 DescribeVirtualBorderRouters
    - 1.12.4 DescribeVirtualBorderRoutersForPhysicalConnection
    - 1.12.5 ModifyVirtualBorderRouterAttribute
    - 1.12.6 TerminateVirtualBorderRouter
    - 1.12.7 RecoverVirtualBorderRouter
  - 1.13 NAT Gateway
    - 1.13.1 CreateNatGateway
    - 1.13.2 DeleteNatGateway
    - 1.13.3 ModifyNatGatewaySpec
    - 1.13.4 ModifyNatGatewayAttribute
    - 1.13.5 DescribeNatGateways
    - 1.13.6 CreateBandwidthPackage
    - 1.13.7 ModifyBandwidthPackageSpec
    - 1.13.8 DescribeBandwidthPackages
    - 1.13.9 ModifyBandwidthPackageAttribute
    - 1.13.10 DeleteBandwidthPackage
    - 1.13.11 AddBandwidthPackageIps
    - 1.13.12 RemoveBandwidthPackageIps
    - 1.13.13 CreateForwardEntry
    - 1.13.14 DeleteForwardEntry
    - 1.13.15 ModifyForwardEntry
    - 1.13.16 DescribeForwardTableEntries
    - 1.13.17 CreateSnatEntry
    - 1.13.18 DeleteSnatEntry
    - 1.13.19 ModifySnatEntry
    - 1.13.20 DescribeSnatTableEntries
  - 1.14 VPN Gateway
    - 1.14.1 CreateVpnGateway
    - 1.14.2 DescribeVpnGateways
    - 1.14.3 DescribeVpnGateway
    - 1.14.4 DeleteVpnGateway
    - 1.14.5 CreateCustomerGateway
    - 1.14.6 DescribeCustomerGateways
    - 1.14.7 DescribeCustomerGateway
    - 1.14.8 DeleteCustomerGateway
    - 1.14.9 ModifyCustomerGatewayAttribute
    - 1.14.10 DescribeVpnConnection
    - 1.14.11 DeleteVpnConnection
    - 1.14.12 DownloadVpnConnectionConfig
    - 1.14.13 CreateSslVpnServer
    - 1.14.14 DescribeSslVpnServers
    - 1.14.15 DeleteSslVpnServer
    - 1.14.16 ModifySslVpnServer
    - 1.14.17 DeleteSslVpnClientCert
    - 1.14.18 ModifySslVpnClientCert
    - 1.14.19 ModifyVpnGatewayAttribute
    - 1.14.20 CreateVpnConnection
    - 1.14.21 DescribeVpnConnections
    - 1.14.22 ModifyVpnConnectionAttribute
    - 1.14.23 CreateSslVpnClientCert
    - 1.14.24 DescribeSslVpnClientCerts
    - 1.14.25 DeleteVpnPbrRouteEntry
    - 1.14.26 DeleteVpnRouteEntry
    - 1.14.27 CreateVpnPbrRouteEntry
    - 1.14.28 DescribeVpnRouteEntries
    - 1.14.29 ModifyVpnRouteEntryWeight
    - 1.14.30 PublishVpnRouteEntry
    - 1.14.31 DescribeVpnPbrRouteEntries
    - 1.14.32 ModifyVpnPbrRouteEntryWeight
    - 1.14.33 CreateVpnRouteEntry
    - 1.14.34 DescribeVpnSslServerLogs
    - 1.14.35 DescribeSslVpnClientCert
  - 1.15 IPv6 Gateway
    - 1.15.1 CreateIpv6Gateway
    - 1.15.2 DeleteIpv6Gateway
    - 1.15.3 ModifyIpv6GatewaySpec
    - 1.15.4 DescribeIpv6EgressOnlyRules
    - 1.15.5 CreateIpv6EgressOnlyRule
    - 1.15.6 DeleteIpv6EgressOnlyRule
    - 1.15.7 DeleteIpv6InternetBandwidth
    - 1.15.8 DescribeIpv6GatewayAttribute
    - 1.15.9 DescribeIpv6Addresses
    - 1.15.10 AllocateIpv6InternetBandwidth
    - 1.15.11 ModifyIpv6InternetBandwidth
    - 1.15.12 ModifyIpv6GatewayAttribute
    - 1.15.13 ModifyIpv6AddressAttribute
    - 1.15.14 DescribeIpv6Gateways
  - 1.16 High-Availability Virtual IP
    - 1.16.1 CreateHaVip
    - 1.16.2 ModifyHaVipAttribute
    - 1.16.3 DeleteHaVip
    - 1.16.4 AssociateHaVip
    - 1.16.5 UnassociateHaVip
    - 1.16.6 DescribeHaVips
  - 1.17 DescribeRegions
  - 1.18 DescribeZones
  - 1.19 DescribeAccessPoints
- 2 Call VPC SDK by using ASAPI
  - 2.1 Overview
  - 2.2 Log on to the API Tool console
  - 2.3 View the information about API operations
  - 2.4 Obtain the endpoint of ASAPI
  - 2.5 Obtain the core package for ASAPI
  - 2.6 Obtain an AccessKey pair
  - 2.7 Query the region ID
  - 2.8 SDK for Java
  - 2.9 SDK for Node.js
  - 2.10. (Optional) Use POP SDK to call ASAPI API operations

## 1 API reference

### 1.1 List of API operations by function

This topic describes API operations available for use in Virtual Private Cloud (VPC). VPCs

| API | Description |
|---|---|
| CreateVpc | Creates a VPC. |
| DeleteVpc | Deletes a VPC. |
| DescribeVpcs | Queries one or more VPCs. |
| ModifyVpcAttribute | Modifies the name and description of a VPC. |

VSwitches

| API | Description |
|---|---|
| CreateVSwitch | Creates a VSwitch. |
| DeleteVSwitch | Deletes a VSwitch. |
| ModifyVSwitchAttribute | Modifies the name and description of a VSwitch. |
| DescribeVSwitches | Queries one or more VSwitches. |

VRouters

| API | Description |
|---|---|
| ModifyVRouterAttribute | Modifies the name and description of a VRouter. |
| DescribeVRouters | Queries VRouters in a specified region. |
| CreateRouteEntry | Creates a custom route entry in the route table of a VRouter or Virtual Border Router (VBR). |
| DeleteRouteEntry | Deletes a route entry from the route table of a VRouter or VBR. |
| DescribeRouteTables | Queries route entries in a route table. |

EIPs

| API | Description |
|---|---|
| AllocateEipAddress | Applies for an elastic IP address (EIP) |

|   | Developer Guide·API reference | Virtual Private Clou | d |
|---|---|---|---|

| API | Description |
|---|---|
| AllocateEipAddressPro | Applies for a specified EIP. |
| AssociateEipAddress | Associates an EIP with an instance in the same region. |
| UnassociateEipAddress | Disassociates an EIP from an instance. |
| ModifyEipAddressAttribute | Modifies the name, description, and peak bandwidth of an EIP. |
| ReleaseEipAddress | Releases a specified EIP. |
| DescribeEipAddresses | Queries one or more EIPs. |

Router interfaces

| API | Description |
|---|---|
| CreateRouterInterface | Creates a router interface. |
| ConnectRouterInterface | Initiates a connection from the initiator router interface to the acceptor router interface. |
| DeactivateRouterInterface | Deactivates a router interface. |
| ModifyRouterInterfaceSpec | Modifies the specification of a router interface. |
| DeleteRouterInterface | Deletes a router interface. |
| DescribeRouterInterfaces | Queries router interfaces in a specified region. |
| ActivateRouterInterface | Activates a router interface that is in the Inactive state. |
| ModifyRouterInterfaceAttribute | Modifies the configuration of a router interface. |

Express Connect circuits

| API | Description |
|---|---|
| CreatePhysicalConnection | Creates an Express Connect circuit. |
| CancelPhysicalConnection | Cancels the connection over an Express Connect circuit before it is enabled. After you perform this operation, the status of the Express Connect circuit changes to Canceled. |
| DeletePhysicalConnection | Deletes an Express Connect circuit. |
| ModifyPhysicalConnectionAttribute | Modifies the configuration of an Express Connect circuit. |
| DescribePhysicalConnections | Queries Express Connect circuits in a specified region. |

| API | Description |
|---|---|
| TerminatePhysicalConnection | Terminates the connection over an Express Connect circuit after it is enabled. |
| EnablePhysicalConnection | Enables an Express Connect circuit that is in the Confirmed state. After you perform this operation, the status of the Express Connect circuit changes to Enabled. |

VBRs

| API | Description |
|---|---|
| CreateVirtualBorderRouter | Creates a VBR. |
| DeleteVirtualBorderRouter | Deletes a VBR. |
| DescribeVirtualBorderRouters | Queries one or more VBRs. |
| DescribeVirtualBorderRoutersForPhysicalConnection | Queries the VBRs created for an Express Connect circuit, including VBRs that belong to the owner of the Express Connect circuit and those belong to other accounts. |
| ModifyVirtualBorderRouterAttribute | Modifies the configuration of a VBR. |
| TerminateVirtualBorderRouter | Terminates the connection over a VBR. |
| RecoverVirtualBorderRouter | Recovers a terminated VBR. |

NAT gateways

| API | Description |
|---|---|
| CreateNatGateway | Creates a NAT gateway. |
| DeleteNatGateway | Deletes a NAT gateway. |
| ModifyNatGatewaySpec | Modifies the specification of a NAT gateway. |
| ModifyNatGatewayAttribute | Modifies the configuration of a NAT gateway. |
| DescribeNatGateways | Queries one or more NAT gateways. |
| CreateBandwidthPackage | Creates a NAT bandwidth plan. |
| ModifyBandwidthPackageSpec | Modifies the bandwidth of a NAT bandwidth plan. |
| DescribeBandwidthPackages | Queries detailed information of a NAT bandwidth plan. |
| ModifyBandwidthPackageAttribute | Modifies the name and description of a NAT bandwidth plan. |
| DeleteBandwidthPackage | Deletes a NAT bandwidth plan. |

| Developer Guide·API reference | Virtual Private Clou |
|---|---|

| API | Description |
|---|---|
| AddBandwidthPackageIps | Adds public IP addresses to a NAT bandwidth plan. |
| RemoveBandwidthPackageIps | Removes public IP addresses from a NAT bandwidth plan. |
| CreateForwardEntry | Adds a destination network address translation (DNAT) entry to a specified DNAT table. |
| DeleteForwardEntry | Deletes a DNAT entry. |
| ModifyForwardEntry | Modifies a DNAT entry. |
| DescribeForwardTableEntries | Queries DNAT entries in a specified DNAT table. |
| CreateSnatEntry | Adds a source network address translation (SNAT) entry to a specified SNAT table. |
| DeleteSnatEntry | Deletes an SNAT entry. |
| ModifySnatEntry | Modifies the value of SnatIp (public IP address) in an SNAT entry. |
| DescribeSnatTableEntries | Queries SNAT entries in a specified SNAT table. |

IPv6 gateways

| API | Description |
|---|---|
| CreateIpv6Gateway | Creates an IPv6 gateway. |
| DeleteIpv6Gateway | Deletes an IPv6 gateway. |
| ModifyIpv6GatewaySpec | Modifies the specification of an IPv6 gateway. |
| DescribeIpv6EgressOnlyRules | Queries detailed information of egress-only rules. |
| CreateIpv6EgressOnlyRule | Creates an egress-only rule for an IPv6 address. |
| DeleteIpv6EgressOnlyRule | Deletes an egress-only rule. |
| DeleteIpv6InternetBandwidth | Deletes an IPv6 Internet bandwidth plan. |
| DescribeIpv6GatewayAttribute | Queries detailed information of an IPV6 gateway. |
| DescribeIpv6Addresses | Queries IPv6 addresses. |
| AllocateIpv6InternetBandwidth | Purchases an Internet bandwidth plan for an IPv6 address. |
| ModifyIpv6InternetBandwidth | Modifies the Internet bandwidth plan of an IPv6 address. |
| ModifyIpv6GatewayAttribute | Modifies the information of an IPv6 gateway. |

| irtual Private Cloud | Developer Guide·API referenc |
|---|---|

| API | Description |
|---|---|
| ModifyIpv6AddressAttribute | Modifies the name and description of an IPv6 address. |
| DescribeIpv6Gateways | Queries one or more IPv6 gateways. |

VPN gateways

| API | Description |
|---|---|
| CreateVpnGateway | Creates a VPN gateway. |
| DescribeVpnGateways | Queries one or more VPN gateways. |
| ModifyVpnGatewayAttribute | Modifies the name and description of a VPN gateway. |
| DeleteVpnGateway | Deletes a VPN gateway. |
| CreateCustomerGateway | Creates a customer gateway. |
| DescribeCustomerGateways | Queries one or more customer gateways. |
| DescribeCustomerGateway | Queries detailed information of a customer gateway. |
| DeleteCustomerGateway | Deletes a customer gateway. |
| ModifyCustomerGatewayAttribute | Modifies the name and description of a customer gateway. |
| CreateVpnConnection | Creates an IPsec-VPN connection. |
| DescribeVpnConnections | Queries IPsec-VPN connections in a specified region. |
| DescribeVpnConnection | Queries detailed information of an IPsec-VPN connection. |
| ModifyVpnConnectionAttribute | Modifies the configuration of an IPsec-VPN connection. |
| DeleteVpnConnection | Deletes an IPsec-VPN connection. |
| DownloadVpnConnectionConfig | Obtains the configuration information of an IPsec-VPN connection. |
| CreateSslVpnServer | Creates an SSL-VPN server. |
| DescribeSslVpnServers | Queries one or more SSL-VPN servers. |
| DeleteSslVpnServer | Deletes an SSL-VPN server. |
| ModifySslVpnServer | Modifies the configuration of an SSL-VPN server. |
| CreateSslVpnClientCert | Creates an SSL-VPN client certificate. |
| DescribeSslVpnClientCerts | Queries one or more SSL-VPN client certificates. |
| DeleteSslVpnClientCert | Deletes an SSL-VPN client certificate. |

| Developer Guide·API reference | Virtual Private Clou |
|---|---|
| API | Description |
| ModifySslVpnClientCert | Modifies the name of an SSL-VPN client certificate. |
| DescribeVpnGateway | Queries detailed information of a VPN gateway. |
| DeleteVpnPbrRouteEntry | Deletes a policy-based route entry of a VPN gateway. |
| DeleteVpnRouteEntry | Deletes a destination-based route entry of a VPN gateway. |
| CreateVpnPbrRouteEntry | Creates a policy-based route entry for a VPN gateway. |
| DescribeVpnRouteEntries | Queries detailed information of destination-based route entries of a VPN gateway. |
| ModifyVpnRouteEntryWeight | Modifies the weight of a destination-based route entry of a VPN gateway. |
| PublishVpnRouteEntry | Advertises a route entry of a VPN gateway to the route table of the associated VPC. |
| DescribeVpnPbrRouteEntries | Queries detailed information of policy-based route entries of a VPN gateway. |
| ModifyVpnPbrRouteEntryWeight | Modifies the weight of a policy-based route entry of a VPN gateway. |
| CreateVpnRouteEntry | Creates a destination-based route entry for a VPN gateway. |
| DescribeVpnSslServerLogs | Queries the logs of an SSL-VPN server. |
| DescribeSslVpnClientCert | Queries detailed information of an SSL-VPN client certificate. |

HAVIPs

| API | Description |
|---|---|
| CreateHaVip | Creates a high-availability virtual IP address (HAVIP). |
| DescribeHaVips | Queries HAVIPs in a specified region. |
| UnassociateHaVip | Disassociates an HAVIP from an ECS instance deployed in a VPC. |
| AssociateHaVip | Associates an HAVIP with an ECS instance of the VPC network. |
| ModifyHaVipAttribute | Modifies the description of an HAVIP. |
| DeleteHaVip | Deletes an HAVIP. |

### 1.2 Call VPC APIs

#### 1.2.1 Request syntax

To send a Virtual Private Cloud (VPC) API request, you must send an HTTP GET request to the VPC endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. Requests and responses are encoded in UTF-8. VPC API operations use the RPC protocol. You can call VPC API operations by sending HTTP GET requests. The request syntax is as follows:

```
http://Endpoint/?Action=xx&Parameters
```

In the request, Endpoint: The endpoint of the VPC API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Stack Operations console. For more information, see Obtain the endpoint of Asapi. Action: the name of the operation being performed. For example, to query created VPC instances, you must set the Action parameter to DescribeVpcs. Version: the version of the API that you want to use. The current VPC API version is 2016-04-28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters are used for all VPC API calls regardless of the operation. For more information, see Common parameters. The following example demonstrates how to call the DescribeVpcs operation. Not e The examples in this topic have been formatted for ease of reading.

```
https://vpc.example.com/?Action=DescribeVpcs &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 1.2.2 API authorization

To ensure the security of your account, we recommend that you call VPC APIs as a RAM user. Before you can use a RAM account to call a VPC API, you must create a RAM account and assign corresponding permissions to it. For more information about VPC resources and APIs you can assign permissions on, see RAM authentication.

#### 1.2.3 Signature method

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. VPC implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. To call an RPC API operation, you must add the signature to the API request in the following format: https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeVpcs as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` . The original request URL is as follows:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

To calculate the signature, perform the following operations:
1. Use the request parameters to create a query string for signature.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC-SHA1 &SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2 016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string you want to sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature to the request parameters:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 1.3 RAM authentication

Before calling a VPC API using a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used as the unique identifier of the resource to authorize. VPC resources The following table lists the VPC resources that can be authorized and their corresponding ARN formats.

| Resource type | ARN format |
|---|---|
| Virtual Private Cloud (VPC) | acs:vpc:$regionid:$accountid:vpc/$vpcid |
|   | acs:vpc:$regionid:$accountid:vpc/* |
|   | acs:vpc:*:$accountid:vpc/* |
| VRouter | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
|   | acs:vpc:$regionid:$accountid:vrouter/* |
|   | acs:vpc:*:$accountid:vrouter/* |
| VSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
|   | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:*:$accountid:vswitch/* |
| Routing table | acs:vpc:$regionid:$accountid:routetable/$routetableid |
|   | acs:vpc:$regionid:$accountid:routetable/* |
|   | acs:vpc:*:$accountid:routetable/* |
| Elastic IP Address (EIP) | acs:vpc:$regionid:$accountid:eip/$allocationid |
|   | acs:vpc:$regionid:$accountid:eip/* |
|   | acs:vpc:*:$accountid:eip/* |
| NAT Gateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|   | acs:vpc:$regionid:$accountid:natgateway/* |
|   | acs:vpc*:$accountid:vpc/* |
| NAT Gateway service plan | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
|   | aacs:vpc:*:$accountid:vpc/* |
| Forwarding table | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
|   | acs:vpc:$regionid:$accountid:forwardtable/* |
| Document Version: 202 | 20928 1 |

| Developer Guide·API refe |   |
|---|---|
|   | rence Virtual Private Clou |
| Resource type | ARN format |
|   | acs:vpc:*:$accountid:vpc/* |
| SNAT table | acs:vpc:$regionid:$accountid:snattable/$snattableid |
|   | acs:vpc:$regionid:$accountid:snattable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| General resource | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accoutid`/`vrouterid are IDs of the specific resources, `*` represents all resources. VPC API operations The following table lists the API operations that can be authorized and their corresponding ARN formats.

| Operation | ARN format |
|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |
| vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVRouters | acs:vpc:$regionid:$accountid:vrouter/* |
|   | The VRouter ID is specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
|   | The VRouter ID is not specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/*" |
| vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
| vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |
|   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
| vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:CreateRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |
| vpc:DeleteRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |

| irtual Private Cloud | Developer Guide·API referenc |
|---|---|

| Operation | ARN format |   |   |
|---|---|---|---|
| vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |   |   |
|   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrout erid" |   |   |
|   |   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrout |   |
|   | erid" |   |   |
| vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:AssociateEipAddres | acs:vpc:$regionid:$accountid:eip/* |   |   |
|   | Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
| vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |   |   |
| vpc:UnassociateEipAddress | Bind an ECS instance acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
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
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp ackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp |   |
| vpc:DescribeBandwidthPackages | ackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp ackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp |   |
| vpc:ModifyBandwidthPackageSpec | ackageid |   |   |

|   | Developer Guide·API reference | Virtual Private Clou | d |
|---|---|---|---|

| Operation | ARN format |   |   |
|---|---|---|---|
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp ackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp |   |
| vpc:ModifyBandwidthPackageAttribute | ackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp ackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp |   |
| vpc:AddBandwidthPackageIps | ackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp ackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp |   |
| vpc:RemoveBandwidthPackageIps | ackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp ackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthp |   |
| vpc:DeleteBandwidthPackage | ackageid |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:CreateForwardEntry |   |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:DeleteForwardEntry |   |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:ModifyForwardEntry |   |   |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |   |
|   |   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:DescribeForwardTableEntries |   |   |   |
| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |   |   |
| vpc:ModifySnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| vpc:DescribeSnatTableEntries | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |
| vpc:DeleteSnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |   |   |

### 1.4 Common parameters

Common request parameters Common request parameters are request parameters that you must use when you call each API. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | String | Yes | The API version in the format of YYYY-MM-DD . Valid value: 2016-04-28 |
| AccessKeyId | String | Yes | The AccessKey ID that you use to call an API. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Name | Type | Required | Description |   |   |
|---|---|---|---|---|---|
| Signature | String | Yes | The signature result string. |   |   |
| SignatureMetho d | String | Yes | The algorithm used to create the request signature. Valid value: HMAC-SHA1 |   |   |
| Timestamp | String | Yes | The timestamp of the request. The timestamp uses UTC and it complies with the ISO 8601 standard. Its format is YYYY-MM- DDThh:mm:ssZ . For example, 20:00:00 on January 10, 2013 in China Standard Time (UTC +8) is written as 2013-01-10T12:00:00Z. |   |   |
|   |   |   |   | YYYY-MM- |   |
| SignatureVersio n | String | Yes | The version of the signature algorithm. Valid value: 1.0 |   |   |
| SignatureNonce | String | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |   |   |

| s | DDThh:mm:ssZ |
|---|---|

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Common response parameters API responses use a unified format. 2xx HTTP status codes indicate a successful invocation. 4xx or 5xx HTTP status codes indicate a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time you send a request to call an API, the system returns a unique identifier RequestId, regardless of whether the invocation is successful or not.

```xml
<? xml version="1.0" encoding="utf-8"? >
      <!—Result root node-->
      <API name+Response>
      <!—Returned request tag-->
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
      <!—Returned results-->
      </API name+Response>
```

```json
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
      /*Returned results*/
```

### 1.5 VPC

#### 1.5.1 CreateVpc

Creates a virtual private cloud (VPC). When you call this operation, follow these rules: You must specify the IP address range of the VPC in the form of a Classless Inter-domain Routing (CIDR) block. You can use a standard CIDR block or a subset of a standard CIDR block as the IP address range of the VPC. The standard CIDR blocks include 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. The subnet mask must be 8 to 28 bits in length. The default CIDR block is 172.16.0.0/12. After you create a VPC, you cannot modify its CIDR block. Each VPC can contain a maximum of 15,000 instances. After you create a VPC, a VRouter and a route table are automatically created for the VPC. You can add a maximum of three client-side CIDR blocks to a VPC. If one client-side CIDR block is a subset of another, the one with the shorter subnet mask takes effect. For example, if you specify 10.0.0.0/8 and 10.1.0.0/16 as the client-side CIDR blocks for a VPC, only 10.0.0.0/8 takes effect.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpc | The operation that you want to perform. Set the value to CreateVpc. |
| RegionId | String | Yes | cn- hangzhou | The region ID of the VPC. You can call the DescribeRegions operation to query the most recent region list. |
| CidrBlock | String | No | 172.16.0.0/ 12 | The CIDR block of the VPC. Set the value to one of the following CIDR blocks or their subsets: 10.0.0.0/8 172.16.0.0/12 (default) 192.168.0.0/16 |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| VpcName | String | No | vpc1 | The name of the VPC. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | This is my first Vpc. | The description of the VPC. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | sha223ndd 2333 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| UserCidr | String | No | 189.16.0.0/ 12 | The client-side CIDR block. Separate multiple CIDR blocks with commas (,). You can specify a maximum of three CIDR blocks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |
| VpcId | String | vpc- bp15zckdt37pq72zv** ** | The ID of the VPC. |
| VRouterId | String | vrt- bp1lhl0taikrteen8**** | The ID of the automatically created VRouter. |
| RouteTableId | String | vtb- bp145q7glnuzdv**** | The ID of the automatically created route table. |

Sample request s

```
https://vpc.example.com/?Action=CreateVpc &RegionId=cn-hangzhou &CidrBlock=172.16.0.0/12 &Common request parameters
```

```json
<? xml version="1.0" encoding="UTF-8"? >
 <CreateVpcResponse>
            <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
            <RouteTableId>vtb-bp145q7glnuzdv****</RouteTableId>
            <VRouterId>vrt-bp1lhl0taikrteen8****</VRouterId>
            <VpcId>vpc-bp15zckdt37pq72zv****</VpcId>
</CreateVpcResponse>
     "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
     "RouteTableId": "vtb-bp145q7glnuzdv****",
     "VRouterId": "vrt-bp1lhl0taikrteen8****",
     "VpcId": "vpc-bp15zckdt37pq72zv****"
```

#### 1.5.2 DeleteVpc

Deletes a VPC. When you call this operation, take note of the following: Before you delete a VPC, make sure that you have released or removed all resources in the VPC, such as VSwitches, instances, and router interfaces. You can only delete VPCs in the Available state.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpc | The operation that you want to perform. Set the value to DeleteVpc. |
| VpcId | String | Yes | vpc- bp1m7v25emi1 h5mtc**** | The ID of the VPC that you want to delete. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeleteVpc &VpcId=vpc-bp1m7v25emi1h5mtc**** <? xml version="1.0" encoding="UTF-8"? > <DeleteVpcResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
 </DeleteVpcResponse>
   "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.5.3 DescribeVpcs

Queries created VPCs.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcs | The operation that you want to perform. Set the value to DescribeVpcs. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPC. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | No | vpc- 257gq64**** | The IDs of the VPCs that you want to query. You can specify up to 20 VPC IDs. Separate the IDs with commas (,). |
| IsDefault | Boolea n | No | false | Specifies whether to query the default VPC in the specified region. Default value: true. Valid values: true: All VPCs in the specified region are queried. false: The default VPC is not queried. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C6532AA8-D0F7-497F- A8EE-094126D441F5 | The ID of the request. |
| TotalCount | String | 2 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| Vpcs | List | - | Details about the VPC. For more information, see the Vpcs list. |

Vpcs list

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcId | String | vpc- bp1qpo0kug3a20qqe* *** | The ID of the VPC. |
| RegionId | String | cn-hangzhou | The region ID of the VPC. |
| Status | String | Available | The status of the VPC. Valid values: Pending: The VPC is being configured. Available: The VPC is available. |
| VpcName | String | vpc1 | The name of the VPC. |
| VSwitchIds | String | { "VSwitchId": [] } | The list of VSwitches in the VPC. |
| CidrBlock | String | 10.0.0.0/24 | The CIDR block of the VPC. |
| VRouterId | String | vrt- bp1jcg5cmxjbl9xgc**** | The ID of the VRouter that belongs to the VPC. |
| Description | String | This is my VPC | The description of the VPC. |
| CreationTime | String | 2018-04- 18T15:02:37Z | The time when the VPC was created. |
| IsDefault | Boolean | false | Indicates whether the VPC is the default VPC in the region. |
| UserCidrs | String | 10.0.0.0/8 | The list of client-side CIDR blocks. |

Sample request s

```xml
https://vpc.example.com/?Action=DescribeVpcs &RegionId=cn-hangzhou &CidrBlock=10.10.0.0/24 <<? xml version="1.0" encoding="UTF-8" ? > <DescribeVpcsResponse>
    <PageNumber>1</PageNumber>
    <Vpcs>
        <Vpc>
            <VpcName>vpc1</VpcName>
            <Description></Description>
            <IsDefault>false</IsDefault>
            <ResourceGroupId>rg-acfmxazb4a2d4****</ResourceGroupId>
            <UserCidrs></UserCidrs>
            <NatGatewayIds></NatGatewayIds>
            <RouterTableIds>
                <RouterTableIds>vtb-bp145q7glnuzda2d4****</RouterTableIds>
            </RouterTableIds>
            <VpcId>vpc-bp15zckdt37pqa2d4****</VpcId>
            <VRouterId>vrt-bp1lhl0taikrta2d4****</VRouterId>
            <CreationTime>2018-04-18T15:02:37Z</CreationTime>
            <Status>Available</Status>
            <CidrBlock>10.0.0.0/24</CidrBlock>
            <VSwitchIds></VSwitchIds>
            <RegionId>cn-hangzhou</RegionId>
        </Vpc>
    </Vpcs>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>9B941224-B647-4644-A746-641906D6B954</RequestId>
</DescribeVpcsResponse>
```

```json
    "PageNumber": 1,
    "Vpcs": {
        "Vpc": [
                "VpcName": "vpc1",
                "Description": "",
                "IsDefault": false,
                "ResourceGroupId": "rg-acfmxazba2d4****",
                "UserCidrs": {
                    "UserCidr": [ ]
```

`},`

```json
                "NatGatewayIds": {
                    "NatGatewayIds": [ ]
```

`},`

```json
                "RouterTableIds": {
                    "RouterTableIds": [
                        "vtb-bp145q7glnuzda2d4****"
```

`]` `},`

```json
                "VpcId": "vpc-bp15zckdt37pqa2d4****",
                "VRouterId": "vrt-bp1lhl0taikra2d4****",
                "CreationTime": "2018-04-18T15:02:37Z",
                "Status": "Available",
                "CidrBlock": "10.0.0.0/24",
                "VSwitchIds": {
                    "VSwitchId": [ ]
```

`},`

```json
                "RegionId": "cn-hangzhou"
```

`]` `},`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "9B941224-B647-4644-A746-641906D6B954"
```

#### 1.5.4 ModifyVpcAttribute

Modifies the name and description of a VPC.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpcAttribute | The operation that you want to perform. Set the value to ModifyVpcAttribute. |
| VpcId | String | Yes | vpc- bp1qtbach57ywecf* *** | The ID of the VPC. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| VpcName | String | No | Vpc-1 | The name of the VPC. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | This is my VPC | The description of the VPC. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyVpcAttribute &VpcId=vpc-bp1qtbach57ywecf**** &VpcName=Vpc02 <? xml version="1.0" encoding="UTF-8"? > <ModifyVpcAttributeResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVpcAttributeResponse>
     "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.5.5 DescribeVpcAttribute

Queries the configurations of a VPC.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcAttribut e | The operation that you want to perform. Set the value to DescribeVpcAttribute. |
| VpcId | String | Yes | vpc- bp18sth14qii3pnv** ** | The ID of the VPC that you want to query. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPC. |
| IsDefault | Boolea n | No | false | Specifies whether the VPC is the default VPC. Valid values: false: The VPC is not the default VPC. true: The VPC is the default VPC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7486AE4A-129D-43DB- A714-2432C074BA04 | The ID of the request. |
| VpcName | String | doctest2 | The name of the VPC. |
| Description | String | vpc1 | The description of the VPC. |
| IsDefault | Boolean | false | Indicates whether the VPC is the default VPC. |
| VRouterId | String | vrt- bp1jso6ng1at0ajsc**** | The ID of the VRouter that belongs to the VPC. |
| VpcId | String | vpc- bp18sth14qii3pnvo**** | The ID of the VPC. |
| CidrBlock | String | 192.168.0.0/16 | The CIDR block of the VPC. |
| VSwitchIds | List | {"VSwitchId": [ "vsw- bp14cagpfysr29feg*** *" ]} | The list of VSwitches in the VPC. |
| Status | String | Available | The status of the VPC. |
| CreationTime | String | 2018-10- 16T07:31:09Z | The time when the VPC was created. |
| CloudResources | List | - | The list of resources in the VPC. For more information, see the CloudResources list. |

CloudResources list

| Paramete r | Type | Example | Description |
|---|---|---|---|
| Resource Count | Integer | 1 | The number of resources in the VPC. |
| Resource Type | String | VSwitch | The type of resources in the VPC. |

Sample request s

```
https://vpc.example.com/?Action=DescribeVpcAttribute &VpcId=vpc-bp13cwaie5zzb23s**** &RegionId=cn-hangzhou &CommonParameters
```

```xml
<? xml version="1.0" encoding="utf-8"? > </DescribeVpcAttributeResponse>
    <VpcName>k8s_vpc</VpcName>
    <Description></Description>
    <IsDefault>false</IsDefault>
    <VRouterId>vrt-bp19a5yibawcb23s****
</VRouterId>
    <VpcId>vpc-bp13cwaie5zzbb23s****
</VpcId>
    <CreationTime>2018-04-20T03:02:33Z</CreationTime>
    <CidrBlock>192.168.0.0/16</CidrBlock>
    <Status>Available</Status>
    <VSwitchIds>
        <VSwitchId>vsw-bp1oisthjafqqb23s****
</VSwitchId>
    </VSwitchIds>
    <RequestId>3FEECC52-51EC-4F0E-B2D4-DA181D50F5B6</RequestId>
    <RegionId>cn-hangzhou</RegionId>
    <CloudResources>
        <CloudResourceSetType>
            <ResourceType>NatGateway</ResourceType>
            <ResourceCount>1</ResourceCount>
        </CloudResourceSetType>
        <CloudResourceSetType>
            <ResourceType>VSwitch</ResourceType>
            <ResourceCount>1</ResourceCount>
        </CloudResourceSetType>
        <CloudResourceSetType>
            <ResourceType>VRouter</ResourceType>
            <ResourceCount>1</ResourceCount>
        </CloudResourceSetType>
        <CloudResourceSetType>
            <ResourceType>RouteTable</ResourceType>
            <ResourceCount>1</ResourceCount>
        </CloudResourceSetType>
    </CloudResources>
</DescribeVpcAttributeResponse>
```

```json
    "VpcName": "k8s_vpc",
    "Description": "",
    "IsDefault": false,
    "VRouterId": "vrt-bp19a5yibawcb23s****
```

`",`

```json
    "VpcId": "vpc-bp13cwaie5zzbb23s****
```

`",`

```json
    "CreationTime": "2018-04-20T03:02:33Z",
    "CidrBlock": "192.168.0.0/16",
    "Status": "Available",
    "VSwitchIds": {
        "VSwitchId": [
            "vsw-bp1oisthjafqqb23s****
```

`"` `]` `},`

```json
    "RequestId": "3FEECC52-51EC-4F0E-B2D4-DA181D50F5B6",
    "RegionId": "cn-hangzhou",
    "CloudResources": {
        "CloudResourceSetType": [
                "ResourceType": "NatGateway",
                "ResourceCount": 1
```

`},`

```json
                "ResourceType": "VSwitch",
                "ResourceCount": 1
```

`},`

```json
                "ResourceType": "VRouter",
                "ResourceCount": 1
```

`},`

```json
                "ResourceType": "RouteTable",
                "ResourceCount": 1
```

`]`

### 1.6 VRouter

#### 1.6.1 DescribeVRouters

Queries VRouters in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVRouters | The operation that you want to perform. Set the value to DescribeVRouters. |
| RegionId | String | No | cn-hangzhou | The region ID of the VPC. You can call the DescribeRegions operation to query the most recent region list. |
| VRouterId | String | No | vrt- bp1lhl0taikrteen**** | The ID of the VRouter. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| VRouters | JSON string | - | Details about the VRouter. |
| VRouters elements |   |   |   |
| VRouterId | String | vrt- rj98khsezfqpjrxmv**** | The ID of the VRouter. |
| RegionId | String | us-west-1 | The region ID of the VPC. |
| VpcId | String | vpc- rj905wotv6y030t1**** | The ID of the VPC to which the VRouter belongs. |
| RouteTableIds | String | { "RouteTableId": [ "vtb- rj9ybe3y0u41mmjsp*** *"] } | The ID of the route table for the VRouter. |
| VRouterName | String | doctest | The name of the VRouter. |

| irtual Private Cloud |   |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Description | String | My VRouter | The description of the VRouter. |
| CreationTime | String | 2018-03- 22T07:46:20Z | The time when the VRouter was created. |

Sample request s

```xml
https://vpc.example.com/?Action=DescribeVRouters &RegionId=us-west-1 <? xml version="1.0" encoding="UTF-8" ? > <DescribeVRoutersResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>1</TotalCount>
    <VRouters>
        <VRouter>
            <VRouterName>doctest</VRouterName>
            <RouteTableIds>
                <RouteTableId>vtb-rj9ybe3y0u41mdc3s****</RouteTableId>
            </RouteTableIds>
            <CreationTime>2018-03-22T07:46:20Z</CreationTime>
            <Description></Description>
            <RegionId>us-west-1</RegionId>
            <VRouterId>vrt-rj98khsezfqpjrxmv****</VRouterId>
            <VpcId>vpc-rj905wotv6y030t1****</VpcId>
        </VRouter>
    </VRouters>
    <PageSize>10</PageSize>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DescribeVRoutersResponse>
```

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "VRouters": {
        "VRouter": [
                "VRouterName": "doctest",
                "RouteTableIds": {
                    "RouteTableId": [
                        "vtb-rj9ybe3y0u41mdc3s****"
```

`]` `},`

```json
                "CreationTime": "2018-03-22T07:46:20Z",
                "Description": "",
                "RegionId": "us-west-1",
                "VRouterId": "vrt-rj98khsezfqpjrxmv****",
                "VpcId": "vpc-rj905wotv6y030t1****"
```

`]` `},`

```json
    "PageSize": 10,
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.6.2 ModifyVRouterAttribute

Modifies the name and description of a VRouter.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVRouterAttri bute | The operation that you want to perform. Set the value to Modif yVRout erAt t ribut e. |
| VRouterId | String | Yes | vrt- bp1lhl0taikrteen8*** * | The ID of the VRouter. |
| VRouterName | String | No | VRouter-1 | The name of the VRouter. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | My VRouter | The description of the VRouter. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyVRouterAttribute &VRouterId=vrt-bp1lhl0taikrteen8**** &VRouterName=VRouter-1 <? xml version="1.0" encoding="UTF-8"? > <ModifyVRouterAttributeResponse>
   <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVRouterAttributeResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
    "RouteTableId": "vtb-bp145q7glnuzdxxxxxxxx",
    "VRouterId": "vrt-bp1lhl0taikrtxxxxxxxx",
     "VpcId": "vpc-bp15zckdt37pqxxxxxxxx"
```

### 1.7 VSwitch

#### 1.7.1 CreateVSwitch

Creates a VSwitch. When you call this operation, take note of the following: A maximum of 24 VSwitches can be created in a VPC. The first one and last three IP addresses of each VSwitch CIDR block are reserved. For example, if the CIDR block of a VSwitch is 192.168.1.0/24, IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The number of instances under a VSwitch cannot exceed the remaining capacity of the VPC. The remaining capacity is the difference between 15,000 and the current number of instances. Each instance can belong to only one VSwitch. VSwitches do not support broadcasting or multicasting. After you create a VSwitch, you cannot modify its CIDR block.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVSwitch | The operation that you want to perform. Set the value to CreateVSwitch. |
| ZoneId | String | Yes | cn-hangzhou-b | The ID of the zone to which the VSwitch belongs. You can call the DescribeZones operation to query the most recent zone list. |
| CidrBlock | String | Yes | 172.16.0.0/24 | The CIDR block of the VSwitch. Take note of the following: The subnet mask for the VSwitch must be 16 to 29 bits in length. The CIDR block of the VSwitch must be within the range of the CIDR block of the VPC to which the VSwitch belongs. The CIDR block of the VSwitch cannot be the same as the destination CIDR block of a route entry in the VPC but can be a subset of it. If the CIDR block of the VSwitch is the same as that of the VPC, only the current VSwitch can be created for the VPC. |
| VpcId | String | Yes | vpc-257fsegq6n**** | The ID of the VPC to which the VSwitch belongs. |
| VSwitchName | String | No | VSwitch-1 | The name of the VSwitch. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | This is my vswitch | The description of the VSwitch. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | dhueeuxxxxxxdde | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 861E6630-AEC0-4B2D- B214-6CB5E44B7F04 | The ID of the request. |
| VSwitchId | String | vsw-25nsdf2aue4g**** | The ID of the VSwitch. |

Sample request s

```json
https://vpc.example.com/?Action=CreateVSwitch &CidrBlock=172.16.1.0/24 &VpcId=vpc-257fsegq6n**** &ZoneId=cn-hangzhou-b <? xml version="1.0" encoding="UTF-8"? > <CreateVSwitchResponse>
    <RequestId>861E6630-AEC0-4B2D-B214-6CB5E44B7F04</RequestId>
    <VSwitchId>vsw-25nsdf2aue4g****
</VSwitchId> </CreateVSwitchResponse>
    "RequestId": "861E6630-AEC0-4B2D-B214-6CB5E44B7F04",
    "VSwitchId": "vsw-25nsdf2aue4g****
```

`"`

#### 1.7.2 DeleteVSwitch

Deletes a VSwitch. When you call this operation, take note of the following: Before you delete a VSwitch, make sure that you have released or removed all resources in the VPC, such as instances and router interfaces. You can only delete VSwitches in the Available state. You cannot delete a VSwitch from a VPC in which a VSwitch or route entry is being created or deleted.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVSwitch | The operation that you want to perform. Set the value to DeleteVSwitch. |
| VSwitchId | String | Yes | vsw-asdfjlna**** | The ID of the VSwitch to delete. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeleteVSwitch &VSwitchId=vsw-asdfjlna**** <? xml version="1.0" encoding="UTF-8"? > <DeleteVSwitchResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVSwitchResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.7.3 ModifyVSwitchAttribute

Modifies the name and description of a VSwitch.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVSwitchAttri bute | The operation that you want to perform. Set the value to ModifyVSwitchAttribute. |

| irtual Private Clou | d |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | Yes | vsw-25naue4gz**** | The ID of the VSwitch. |
| VSwitchName | String | No | VSwitch-1 | The name of the VSwitch. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | This is my vswitch | The description of the VSwitch. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyVSwitchAttribute &VSwitchId=vsw-25naue4gz**** &VSwitchName=VS02 <? xml version="1.0" encoding="UTF-8"? > <ModifyVSwitchAttributeResponse>
       <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVSwitchAttributeResponse>
  "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.7.4 DescribeVSwitches

Queries created VSwitches.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVSwitches | The operation that you want to perform. Set the value to DescribeVSwitches. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPC to which the VSwitch belongs. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | No | vpc-25eq58pl**** | The ID of the VPC. |
| ZoneId | String | No | cn-hangzhou-d | The ID of the zone to which the VSwitch belongs. You can call the DescribeZones operation to query the most recent zone list. |
| VSwitchId | String | No | vsw-23dsf3**** | The ID of the VSwitch. |
| IsDefault | Boolea n | No | true | Specifies whether to query the default VSwitches in the specified region. Default value: true. Valid values: true: All VSwitches in the specified region, including the default VSwitches, are queried. false: The default VSwitches are not queried. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9A572171-4E27-40D1- BD36-D26C9E71E29E | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |

| irtual Private Cloud |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | String | 10 | The number of entries returned per page. |
| VSwitches | JSON string |   | Details about the VSwitch. |
| VSwitches elements |   |   |   |
| VpcId | String | vpc-257gq64**** | The ID of the VPC to which the VSwitch belongs. |
| VSwitchId | String | vsw-25b7pv1**** | The ID of the VSwitch. |
| Status | String | Available | The status of the VSwitch. Valid values: Pending: The VSwitch is being configured. Available: The VSwitch is available. |
| CidrBlock | String | 172.16.0.0/24 | The CIDR block of the VSwitch. |
| ZoneId | String | cn-hangzhou-d | The ID of the zone to which the VSwitch belongs. |
| AvailableIpAddre ssCount | Integer | 246 | The number of available IP addresses in the VSwitch. |
| VSwitchName | String | VSwitch-1 | The name of the VSwitch. |
| Description | String | VSwitchDescription | The description of the VSwitch. |
| CreationTime | String | 2018-01- 18T12:43:57Z | The time when the VSwitch was created. |
| IsDefault | Boolean | true | Indicates whether the VSwitch is the default VSwitch in the zone. |

Sample request s

```
https://vpc.example.com/?Action=DescribeVSwitches &RegionId=cn-hangzhou
```

```json
<? xml version="1.0" encoding="UTF-8"? > <DescribeVSwitchesResponse>
    <RequestId>9A572171-4E27-40D1-BD36-D26C9E71E29E</RequestId>
    <VSwitches>
        <VSwitch>
            <VSwitchId>vsw-25b7pv1****</VSwitchId>
            <Status>Available</Status>
            <CidrBlock>172.16.1.0/24</CidrBlock>
            <ZoneId>cn-hangzhou-d</ZoneId>
            <AvailableIpAddressCount>246</AvailableIpAddressCount>
            <VpcId>vpc-257gq64****</VpcId>
            <Description>VSwitchDescription</Description>
            <VSwitchName>VSwitch-1</VSwitchName>
            <CreationTime>2018-01-18T12:43:57Z</CreationTime>
        </VSwitch>
    </VSwitches>
</DescribeVSwitchesResponse>
    "PageNumber": 1,
    "PageSize": 10,
    "RequestId": "9A572171-4E27-40D1-BD36-D26C9E71E29E",
    "TotalCount": 1,
    "VSwitches": {
        "VSwitch": [
                "AvailableIpAddressCount": 246,
                "CidrBlock": "172.16.1.0/24",
                "CreationTime": "2018-01-18T12:43:57Z",
                "Description": "VSwitchDescription",
                "Status": "Available",
                "VSwitchId": "vsw-25b7pv1****",
                "VSwitchName": "VSwitch-1",
                "VpcId": "vpc-257gq64****",
                "ZoneId": "cn-hangzhou-d"
```

`]`

#### 1.7.5 DescribeVSwitchAttributes

Queries the configurations of a VSwitch.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVSwitchAttr ibutes | The operation that you want to perform. Set the value to DescribeVSwitchAttributes. |

| irtual Private Clou | d |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | Yes | vsw-25naue4g**** | The ID of the VSwitch. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7B48B4B9-1EAD-469F- B488-594DAB4B6A1A | The ID of the request. |
| RouteTable | List |   | The route table of the VSwitch. For more information, see the RouteTable list. |
| Description | String | abc | The description of the VSwitch. |
| IsDefault | Boolean | false | Indicates whether the VSwitch is the default VSwitch. |
| ZoneId | String | cn-beijing-a | The ID of the zone to which the VSwitch belongs. |
| AvailableIpAddre ssCount | Integer | 12 | The number of available IP addresses. |
| VSwitchId | String | vsw-25b7pv15t**** | The ID of the VSwitch. |
| VpcId | String | vpc-257gq642n**** | The ID of the VPC to which the VSwitch belongs. |
| CidrBlock | String | 192.168.0.1/24 | The CIDR block of the VSwitch. |
| Status | String | Pending | The status of the VSwitch. |
| VSwitchName | String | test | The name of the VSwitch. |
| CreationTime | String | 2017-08- 22T10:40:25Z | The time when the VSwitch was created. |
| CloudResources | String | i- m5eimwfzk9nzhie3**** | The cloud resources under the VSwitch. |

RouteTable list

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouteTableId | String | vtb-bp145q7glnuzdv**** | The ID of the route table associated with the VSwitch. |
| RouteTableType | String | System | The type of the route table. |

Sample request s

```json
https://vpc.example.com/?Action=DescribeVSwitchAttributes &VSwitchId=vsw-25naue4g**** <? xml version="1.0" encoding="utf-8"? > </DescribeVSwitchAttributesResponse>
    <RouteTable>
        <RouteTableId>vtb-bp145q7glnuzdv****</RouteTableId>
        <RouteTableType>System</RouteTableType>
    </RouteTable>
    <Description>abc</Description>
    <IsDefault>false</IsDefault>
    <AvailableIpAddressCount>65532</AvailableIpAddressCount>
    <ZoneId>cn-hangzhou-e</ZoneId>
    <VSwitchId>vsw-25b7pv15t****</VSwitchId>
    <VpcId>vpc-257gq642n****</VpcId>
    <CreationTime>2018-05-11T02:45:46Z</CreationTime>
    <CidrBlock>192.168.0.0/16</CidrBlock>
    <Status>Available</Status>
    <RequestId>55BAAD8E-F1FA-4B46-BF6B-DF1E51555F52</RequestId>
    <VSwitchName>HBase_verification</VSwitchName>
    <CloudResources></CloudResources>
</DescribeVSwitchAttributesResponse>
    "RouteTable": {
        "RouteTableId": "vtb-bp145q7glnuzdv****",
        "RouteTableType": "System"
```

`},`

```json
    "Description": "abc",
    "IsDefault": false,
    "AvailableIpAddressCount": 65532,
    "ZoneId": "cn-hangzhou-e",
    "VSwitchId": "vsw-25b7pv15t****",
    "VpcId": "vpc-257gq642n****",
    "CreationTime": "2018-05-11T02:45:46Z",
    "CidrBlock": "192.168.0.0/16",
    "Status": "Available",
    "RequestId": "55BAAD8E-F1FA-4B46-BF6B-DF1E51555F52",
    "VSwitchName": "HBase_verification",
    "CloudResources": {
        "CloudResourceSetType": []
```

### 1.8 Routing table

#### 1.8.1 CreateRouteEntry

You can call this operation to create a custom route entry in the routing table of a VRouter or VBR. When you call this operation to create a custom route entry in the routing table of a VRouter, take note of the following items: A routing table can contain a maximum of 48 custom route entries. The destination CIDR block (DestinationCidrBlock) of a custom route entry and the CIDR block of a VSwitch in the VPC cannot be the same or be a subset of each other. The destination CIDR block (DestinationCidrBlock) of a custom route entry cannot be 100.64.0.0/10 or a subset of it. The destination CIDR blocks (DestinationCidrBlock) of route entries in the same routing table cannot be the same. If the specified destination CIDR block (DestinationCidrBlock) is an IP address, the 32-bit subnet mask is used. Multiple custom route entries can be destined for the same next hop (NextHopId). The next hop (NextHopId) of a custom route entry must belong to the same VPC as the routing table. ECMP route entries can be configured by specifying the NextHopList parameter. If you create a non-ECMP route entry, you must specify DestinationCidrBlock, NextHopType, and NextHopId, and you must not specify NextHopList. If you create an ECMP route entry, you must specify DestinationCidrBlock and NextHopList, and you cannot specify NextHopType and NextHopId. When you call this operation to create a custom route entry in the routing table of a VBR, take note of the following: A routing table can contain a maximum of 48 custom route entries. The NextHopList parameter is not supported. The destination CIDR block (DestinationCidrBlock) of a custom route entry cannot be 100.64.0.0/10 or a subset of it. The destination CIDR blocks (DestinationCidrBlock) of route entries in the same routing table cannot be the same. If the specified destination CIDR block (DestinationCidrBlock) is an IP address, the 32-bit subnet mask is used. Multiple custom route entries can be destined for the same next hop (NextHopId). The next hop (NextHopId) of a custom route entry must be a router interface associated with the VBR. You can create route entries only when the VBR is in the Active state, and the physical connection corresponding to the VBR is in the Enabled state and is not locked. You can create only non-ECMP route entries. To create such an entry, you must specify DestinationCidrBlock, NextHopType, and NextHopId and cannot specify NextHopList.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouteEntry | The operation that you want to perform. Set the value to CreateRouteEntry. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzd**** | The ID of the routing table. |
| DestinationCidr Block | String | Yes | 192.168.0.1/24 | The destination CIDR block of the custom route entry. Take note of the following: The destination CIDR block of a route entry cannot be 100.64.0.0/10 or a subset of it. The destination CIDR blocks of route entries in the same routing table cannot be the same. If the specified destination CIDR block is an IP address, the 32-bit subnet mask is used. |
| NextHopType | String | No | RouterInterface | The type of the next hop. Default value: Instance. Valid values: Instance: The next hop is an ECS instance. RouterInterface: The next hop is a router interface. Not e If you create a non-ECMP route entry, you must specify this parameter. |
| NextHopId | String | No | ri- 2zeo3xzyf38r4**** | The ID of the next-hop instance of the route entry. The next-hop instance must be in the VPC or VBR to which the routing table belongs. Not e If you create a non-ECMP route entry, you must specify this parameter. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to guarantee the idempotency of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| NextHopList | List | No |   | The list of next hops. Take note of the following: ECMP route entries can be created only in the routing table of a VRouter. Two to four next hops can be specified. The next hops must be VRouter interfaces that are destined for VBRs. Not e If you create an ECMP route entry, you must specify this parameter. |
| NextHopList elements Not e If you create an ECMP route entry, you must specify this parameter. |   |   |   |   |
| NextHopType | String | No | RouterInterface | The type of the next hop. Default value: Instance. Valid values: Instance: The next hop is an ECS instance. RouterInterface: The next hop is a router interface. |
| NextHopId | String | No | ri- 2zeo3xzyf38r4**** | The ID of the next-hop instance. |
| Enabled | Integer | No | 1 | Specifies whether the next hop is available. 1: available 0: unavailable |
| Weight | Integer | No | 100 | The route weight of the next hop. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D0 06- F706- 4D23- 88ED- E11ED28 DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=CreateRouteEntry &RouteTableId=vtb-bp145q7glnuzd**** &DestinationCidrBlock=0.0.0.0/0 &NextHopId=ri-2zeo3xzyf38r4**** <?xml version="1.0" encoding="UTF-8"?> <CreateRouteEntryResponse>
    <RequestId>12D086F6-8F31-4658-84C1-006DED011A85</RequestId>
</CreateRouteEntryResponse>
    "RequestId": "12D086F6-8F31-4658-84C1-006DED011A85"
```

#### 1.8.2 DeleteRouteEntry

You can call this operation to delete a route entry from the routing table of a VRouter or VBR. When you call this operation, take note of the following: You can only delete route entries in the Available state. If a VSwitch or route entry is being created or deleted in a VPC, you cannot delete route entries from that VPC.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouteEntry | The operation that you want to perform. Set the value to DeleteRouteEntry. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzd**** | The ID of the routing table to which the route entry belongs. |
| DestinationCidr Block | String | Yes | 0.0.0.0/0 | The destination CIDR block of the route entry. |
| NextHopId | String | No | ri- 2zeo3xzyf38r4urzd* *** | The ID of the next-hop instance of the route entry. If you delete a non-ECMP route entry, you must specify this parameter. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| NextHopList | String | No |   | The list of next hops in the route entry. If you delete an ECMP route entry, you must specify this parameter. |

NextHopList list

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| NextHopType | String | No | RouterInterface | The type of the next hop. Valid values: Instance: The next hop is an ECS instance. RouterInterface: The next hop is a router interface. |
| NextHopId | String | No | ri- 2zeo3xzyf38r43cd** ** | The ID of the next-hop instance. |
| Enabled | Integer | No | 1 | Specifies whether the next hop is available. 1: available 0: unavailable |
| Weight | Integer | No | 10 | The route weight of the next hop. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=DeleteRouteEntry &RouterTableId=vtb-bp145q7glnuzd**** &DestinationCidrBlock=192.168.1.0/24 &NextHopId=ri-2zeo3xzyf38r4urzd****
```

```json
<?xml version="1.0" encoding="UTF-8"?> <DeleteRouteEntryResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteRouteEntryResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.8.3 DescribeRouteTables

Queries the route entries of a route table.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouteTable s | The operation that you want to perform. Set the value to DescribeRouteTables. |
| RouterType | String | No | VRouter | The type of the router to which the route table belongs. Valid values: VRouter VBR |
| RouterId | String | No | vrt- uf64cqu16yawny76 2**** | The ID of the VRouter or VBR to which the route table belongs. |
| VRouterId | String | No | vrt- uf64cqu16yawny76 2**** | The ID of the VRouter to which the route table belongs. When this parameter is specified, the value of the RouterType parameter is automatically set to VRouter. |
| RouteTableId | String | No | vtb- uf6b6iqrk9n3bpq6e ayg0 | The ID of the route table. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC668356-BCB4-42FD- 9BC3-FA2B2E04B634 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RouteTables | List |   | Details about the route table. For more information, see the RouteTables list. |

RouteTables list

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouterType | String | VRouter | The type of the router to which the route table belongs. Valid values: VRouter VBR |
| RouterId | String | vrt- uf64cqu16yawny762** ** | The ID of the VRouter or VBR to which the route table belongs. |
| VRouterId | String | vrt- bp1lhl0taikrteen8**** | The ID of the VRouter. |
| RouteTableId | String | vtb- bp145q7glnuzdvzu2** ** | The ID of the route table. |
| RouteTableType | String | System | The type of the route table. |
| CreationTime | String | 2017-08- 22T10:40:25Z | The time when the route table was created. |
| RouteEntrys | List |   | Details about route entries. For more information, see the RouteEntrys list. |

RouteEntrys list

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | Custom | The type of the route entry. Valid value: Custom: custom route entry |
| RouteTableId | String | vtb- bp145q7glnuzdvzu2** ** | The ID of the route table to which the route entry belongs. |

| Developer Guide·API | reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| DestinationCidrBl ock | String | 192.168.0.1/24 | The destination CIDR block of the route entry. |
| NextHopType | String | RouterInterface | The type of the next hop. |
| InstanceId | String | ri- 2zeo3xzyf38r4urzd**** | The ID of the next-hop instance. |
| Status | String | Pending | The status of the route entry. Valid values: Pending: The route entry is being configured. Available: The route entry is available. Modifying: The route entry is being modified. |
| NextHops | List |   | The list of next hops of ECMP routes. For more information, see the NextHops list. |

NextHops list

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextHopType | String | RouterIn terface | The type of the next hop. Default value: Instance. Valid values: Instance: ECS instance RouterInterface: router interface |
| NextHopId | String | ri- 2zeo3xz yf38r4ur zdpvqw | The ID of the next-hop instance. |
| Enabled | Integer | 1 | Indicates whether the next hop is available. Valid values: 1: available 0: unavailable |
| Weight | Integer | 100 | The route weight of the next hop. |

Sample request s

```
https://vpc.example.com/?Action=DescribeRouteTables &RouteTableId=vtb-bp1krxxzp0c29fmon****
```

```xml
<? xml version="1.0" encoding="UTF-8"? > <DescribeRouteTablesResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
    <RouteTables>
        <RouteTable>
            <CreationTime>2017-08-22T10:40:25Z</CreationTime>
            <RouteEntrys>
                <RouteEntry>
                    <NextHops></NextHops>
                    <Status>Available</Status>
                    <Type>System</Type>
                    <InstanceId></InstanceId>
                    <NextHopType>service</NextHopType>
                    <RouteTableId>vtb-2zevpmy9th8cdc34****</RouteTableId>
                    <DestinationCidrBlock>100.64.0.0/10</DestinationCidrBlock>
                </RouteEntry>
            </RouteEntrys>
            <RouteTableId>vtb-2zevpmy9th8cvf43****</RouteTableId>
            <RouteTableType>System</RouteTableType>
            <VRouterId>vrt-2zefso23vmu6vf35****</VRouterId>
        </RouteTable>
    </RouteTables>
</DescribeRouteTablesResponse>
```

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "DC668356-BCB4-42FD-9BC3-FA2B2E04B634",
    "RouteTables": {
        "RouteTable": [
                "CreationTime": "2017-08-22T10:40:25Z",
                "RouteEntrys": {
                    "RouteEntry": [
                            "NextHops": {
                                "NextHop": [ ]
```

`},`

```json
                            "Status": "Available",
                            "Type": "System",
                            "InstanceId": "",
                            "NextHopType": "service",
                            "RouteTableId": "vtb-2zevpmy9th8cdc34****",
                            "DestinationCidrBlock": "100.64.0.0/10"
```

`]` `},`

```json
                "RouteTableId": "vtb-2zevpmy9th8cvf43****",
                "RouteTableType": "System",
                "VRouterId": "vrt-2zefso23vmu6vf35****"
```

`]`

### 1.9 Elastic IP Address (EIP)

#### 1.9.1 AllocateEipAddress

Applies for an EIP. After you call this operation, an EIP in the Available state in a specified region is randomly allocated. EIPs support only the following transport layer protocols: ICMP, TCP, and UDP.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddress | The operation that you want to perform. Set the value to AllocateEipAddress. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| Bandwidth | String | No | 5 | The peak bandwidth of the EIP. Unit: Mbit/s. Default value: 5. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| EipAddress | String | 123.xx.xx.206 | The EIP that was allocated. |
| AllocationId | String | eip-25877c70gddh**** | The ID of the allocated EIP. |

Sample request s

```xml
https://vpc.example.com/?Action=AllocateEipAddress &RegionId=cn-beijing <? xml version="1.0" encoding="UTF-8" ? > <AllocateEipAddressResponse>
        <AllocationId>eip-25877c70gddh****</AllocationId>
        <EipAddress>123.xx.xx.206</EipAddress>
        <RequestId>B6B9F518-60F8-4D81-9242-1207B356754D</RequestId>
</AllocateEipAddressResponse>
```

```json
    "AllocationId": "eip-25877c70gddh****",
     "EipAddress": "123.xx.xx.206",
     "RequestId": "B6B9F518-60F8-4D81-9242-1207B356754D"
```

#### 1.9.2 AllocateEipAddressPro

Applies for a specified EIP. After you call this operation, a specified EIP in the Available state in a specified region is allocated. EIPs support only the following transport layer protocols: ICMP, TCP, and UDP.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddress Pro | The operation that you want to perform. Set the value to AllocateEipAddressPro. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| Bandwidth | String | No | 5 | The peak bandwidth of the EIP. Unit: Mbit/s. Default value: 5. |
| IpAddress | String | No | 12.xx.xx.23 | The EIP that you want to apply. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| EipAddress | String | 123.xx.xx.206 | The EIP that was allocated. |
| AllocationId | String | eip-25877c70gddh**** | The ID of the allocated EIP. |

Sample request s

```json
https://vpc.example.com/?Action=AllocateEipAddress &RegionId=cn-beijing <? xml version="1.0" encoding="UTF-8" ? > <AllocateEipAddressResponse>
        <AllocationId>eip-25877c70gddh****</AllocationId>
        <EipAddress>123.xx.xx.206</EipAddress>
        <RequestId>B6B9F518-60F8-4D81-9242-1207B356754D</RequestId>
</AllocateEipAddressResponse>
    "AllocationId": "eip-25877c70gddh****",
     "EipAddress": "123.xx.xx.206",
     "RequestId": "B6B9F518-60F8-4D81-9242-1207B356754D"
```

#### 1.9.3 AssociateEipAddress

You can call this operation to associate an Elastic IP address with an instance in the same region. When you call this operation, take note of the following: You can only associate Elastic IP addresses in the Available state. Each Elastic IP address can only be associated with one instance.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateEipAddres s | The operation that you want to perform. Set the value to AssociateEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7ujd342* *** | The ID of the Elastic IP address. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| InstanceType | String | No | EcsInstance | The type of the instance with which you want to associate the Elastic IP address. Valid values: SlbInstance: an SLB instance. EcsInstance (default): an ECS instance in a VPC. Nat: a NAT gateway. NetworkInterface: a secondary ENI. |
| InstanceId | String | Yes | i- 2zebb08phyczdw32 **** | The ID of the instance with which you want to associate the Elastic IP address. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C0FD0EED-F90D-4479- 803D-DD62335357E5 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=AssociateEipAddress &AllocationId=eip-2zeerraiwb7ujd342**** &InstanceId=i-2zebb08phyczdw32**** <?xml version="1.0" encoding="UTF-8"?> <AssociateEipAddressResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</AssociateEipAddressResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.9.4 UnassociateEipAddress

You can call this operation to disassociate an Elastic IP address from an instance.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateEipAddr ess | The operation that you want to perform. Set the value to UnassociateEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0d** ** | The ID of the Elastic IP address. |
| InstanceType | String | No | EcsInstance | The type of the instance from which you want to disassociate the Elastic IP address. Valid values: SlbInstance: an SLB instance. EcsInstance (default): an ECS instance in a VPC. Nat: a NAT gateway. NetworkInterface: a secondary ENI. |
| InstanceId | String | Yes | i-12345678 | The ID of the instance from which you want to disassociate the Elastic IP address. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 220F3179-5238-47F0-A0CA- 1272AA2BC41F | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=UnassociateEipAddress &AllocationId=eip-2zeerraiwb7uj6i0d**** &InstanceId=i-12345678 <?xml version="1.0" encoding="UTF-8"?> <UnassociateEipAddressResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</UnassociateEipAddressResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.9.5 ModifyEipAddressAttribute

Modifies the name, description, and peak bandwidth of an EIP.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyEipAddressAt tribute | The operation that you want to perform. Set the value to ModifyEipAddressAttribute. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0d** ** | The ID of the EIP. |
| Bandwidth | String | No | 5 | The peak bandwidth of the EIP. Unit: Mbit/s. |
| Name | String | No | eip1 | The name of the EIP. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | eip111 | The description of the EIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=ModifyEipAddressAttribute &AllocationId=eip-2zeerraiwb7uj6i0d**** &Name=eip1
```

```json
<? xml version="1.0" encoding="UTF-8"? > <ModifyEipAddressAttributeResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyEipAddressAttributeResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.9.6 ReleaseEipAddress

Releases an EIP. You can only release EIPs in the Available state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseEipAddress | The operation that you want to perform. Set the value to ReleaseEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0d** ** | The ID of the EIP. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 748C38F6-9A3D-482E- 83FB-DB6C39C68AEA | The ID of the request. |

Sample request s

```xml
https://vpc.example.com/?Action=ReleaseEipAddress &AllocationId=eip-2zeerraiwb7uj6i0d**** <? xml version="1.0" encoding="UTF-8"? > <ReleaseEipAddressResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ReleaseEipAddressResponse>
```

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.9.7 DescribeEipAddresses

You can call this operation to query the Elastic IP addresses created in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEipAddress es | The operation that you want to perform. Set the value to DescribeEipAddresses. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the Elastic IP address. You can call the DescribeRegions operation to query the most recent region list. |
| Status | String | No | Available | The status of the Elastic IP address. Valid values: Associating: The Elastic IP address is being associated with an instance. Unassociating: The Elastic IP address is being disassociated from an instance. InUse: The Elastic IP address is associated with an instance. Available: The Elastic IP address is available. |
| AllocationId | String | No | eip- 2zeerraiwb7ujdefr** ** | The ID of the Elastic IP address. |
| AssociatedInst anceType | String | No | EcsInstance | The type of the instance with which you want to associate the Elastic IP address. Valid values: SlbInstance: an SLB instance. EcsInstance (default): an ECS instance in a VPC. Nat: a NAT gateway. NetworkInterface: a secondary ENI. |
| AssociatedInst anceId | String | No | i- 2zebb08phycz12w* *** | The ID of the instance with which you want to associate the Elastic IP address. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| irtual Private Clou | d |   |   | Developer Guide·API referenc |
|---|---|---|---|---|
| Parameter | Type | Requi red | Example | Description |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| EipAddresses | List |   | Details about the queried Elastic IP addresses. For more information, see the EipAddresses list. |

EipAddresses list

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionId | String | cn-hangzhou | The region ID of the Elastic IP address. |
| IpAddress | String | 101.xx.xx.36 | The Elastic IP address. |
| AllocationId | String | eip- 2zeerraiwb7ujc32a**** | The ID of the Elastic IP address. |
| Status | String | Associating | The status of the Elastic IP address. Valid values: Associating: The Elastic IP address is being associated with an instance. Unassociating: The Elastic IP address is being disassociated from an instance. InUse: The Elastic IP address is associated with an instance. Available: The Elastic IP address is available. |
| InstanceType | String | EcsInstance | The type of the instance with which the Elastic IP address is associated. |
| InstanceId | String | i- 2zebb08phyc3d2a**** | The ID of the instance with which the Elastic IP address is associated. |
| Bandwidth | String | 5 | The peak bandwidth of the Elastic IP address. Unit: Mbit/s. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetChargeTy pe | String | PayByBandwidth | The billing method of the Elastic IP address. |
| AllocationTime | String | 2019-04- 23T01:37:38Z | The time when the Elastic IP address was created. |
| OperationLocks | String | financial | The reason why the Elastic IP address was locked. Valid values: financial: The Elastic IP address was locked due to overdue payments. security: The Elastic IP address was locked for security reasons. |

Sample request s

```
https://vpc.example.com/?Action=DescribeEipAddresses &RegionId=cn-hangzhou-1
```

```xml
<?xml version="1.0" encoding="UTF-8"?> <DescribeEipAddressesResponse>
    <RequestId>7EEF2D6B-D207-4197-AE37-01279C888757</RequestId>
    <PageNumber>1</PageNumber>
    <EipAddresses>
        <EipAddress>
            <ChargeType>PostPaid</ChargeType>
            <AllocationTime>2018-01-15T11:17:30Z</AllocationTime>
            <ResourceGroupId>rg-acfmxazb42sa****</ResourceGroupId>
            <InstanceId></InstanceId>
            <Description></Description>
            <IpAddress>59.xx.xx.11</IpAddress>
            <AllocationId>eip-2zeerraiwb7ujc32a****</AllocationId>
            <InternetChargeType>PayByTraffic</InternetChargeType>
            <InstanceType></InstanceType>
            <Name></Name>
            <Status>Available</Status>
            <BandwidthPackageId></BandwidthPackageId>
            <InstanceRegionId></InstanceRegionId>
            <BandwidthPackageType></BandwidthPackageType>
            <RegionId>cn-beijing</RegionId>
            <OperationLocks></OperationLocks>
            <ExpiredTime></ExpiredTime>
            <AvailableRegions>
                <AvailableRegion>cn-hangzhou</AvailableRegion>
            </AvailableRegions>
                        <Bandwidth>1</Bandwidth>
        </EipAddress>
    </EipAddresses>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
</DescribeEipAddressesResponse>
```

```json
  "DescribeEipAddressesResponse": {
    "RequestId": "7EEF2D6B-D207-4197-AE37-01279C888757",
    "PageNumber": "1",
    "EipAddresses": {
      "EipAddress": {
        "ChargeType": "PostPaid",
        "AllocationTime": "2018-01-15T11:17:30Z",
        "ResourceGroupId": "rg-acfmxazb42sa****",
        "IpAddress": "59.xx.xx.11",
        "AllocationId": "eip-2zeerraiwb7ujc32a****",
        "InternetChargeType": "PayByTraffic",
        "Status": "Available",
        "RegionId": "cn-beijing",
        "AvailableRegions": {
                    "AvailableRegion": "cn-hangzhou"
```

`},`

```json
        "Bandwidth": "1"
```

`},`

```json
    "TotalCount": "1",
    "PageSize": "10"
```

#### 1.9.8 DescribeEipMonitorData

Queries the monitoring data of an elastic IP address (EIP). You can query monitoring data within the last 30 days and specify up to 400 data points in each request.

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | DescribeEipMonito rData | The operation that you want to perform. Set the value to DescribeEipMonit orDat a |   |   |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6idc fv**** | The ID of the EIP. |   |   |
| EndTime | String | Yes | 2020-01- 05T03:05:10Z | The end of the time range to query. The time must be in UTC. Specify the time in the ISO 8601 standard in YYYY- MM-DDThh:mm:ssZ format. For example, 2013-01-10T12:00:00Z specifies 20:00:00 (UTC+8) on January 10, 2013. |   |   |
|   |   |   |   |   | YYYY- |   |

|   | MM-DDThh:mm:ssZ |
|---|---|

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| StartTime | String | Yes | 2020-01- 05T01:05:05Z | The beginning of the time range to query. The time must be in UTC. Specify the time in the ISO 8601 standard in YYYY- MM-DDThh:mm:ssZ format. For example, 2013-01-10T12:00:00Z specifies 20:00:00 (UTC+8) on January 10, 2013. |   |   |
|   |   |   |   |   | YYYY- |   |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |   |   |
| Period | Integer | No | 60 | The duration of each monitoring data entry. Unit: seconds. Valid values: 60 (default), 300, 900, and 3600. If the value of (EndT ime - St art T ime)/Period is greater than 200, a maximum of 200 monitoring data entries are returned at a time. If the value of (EndT ime - St art T ime)/Period is less than or equal to 200, only the monitoring data collected between the start time and end time is returned. |   |   |

|   | MM-DDThh:mm:ssZ |
|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipMonitorDatas | Array of EipMonitorData |   | The detailed information about the monitoring data of the EIP. |
| EipMonitorData |   |   |   |
| EipBandwidth | Integer | 10 | The average bandwidth value. This value is equal to EipFlow/Period. Unit: Byte/s. The default value of Period is 60. Unit: seconds. |
| EipFlow | Integer | 465 | The sum of inbound and outbound traffic. |
| EipPackets | Integer | 3434 | The number of packets. |
| EipRX | Integer | 122 | The inbound traffic. Unit: bytes. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |
| EipTX | Integer | 343 | The outbound traffic. Unit: bytes. |
| TimeStamp | String | 2020-01- 21T09:50:23Z | The time when the monitoring information was queried. Specify the time in the ISO8601 standard. Example: 2020-01- 21T09:50:23Z . |
| RequestId | String | C8B26B44-0189- 443E-9816- D951F59623A9 | The ID of the request. |

|   | 21T09:50:23Z |
|---|---|

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEipMonitorData &AllocationId=eip-2zeerraiwb7uj6idcfv**** &EndTime=2020-01-05T03:05:10Z &StartTime=2020-01-05T01:05:05Z
```

Sample success responses

```json
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
    "RequestId": "C8B26B44-0189-443E-9816-D951F59623A9",
    "EipMonitorDatas": {
        "EipPackets": 3434,
        "EipBandwidth": 10,
        "EipFlow": 465,
        "EipTX": 343,
        "TimeStamp": "2020-01-21T09:50:23Z",
        "EipRX": 122
```

Error codes

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 404 | InvalidIpInstanceId.No tFound | The specified Eip InstanceId does not exist in our records. | The error message returned because the specified EIP does not exist. |
| 404 | InvalidInstanceId.NotF ound | The InstanceId provided does not exist in our records. | The error message returned because the specified Elastic Compute Service (ECS) instance does not exist in the virtual private cloud (VPC). |
| 400 | InvalidStartTime.Malf ormed | The specified parameter "StartTime" is not valid. | The error message returned because the value of the StartTime parameter is invalid. |
| 400 | InvalidEndTime.Malfo rmed | The specified parameter "EndTime" is not valid. | The error message returned because the value of the EndTime parameter is invalid. |
| 400 | InvalidPeriod.ValueNo tSupported | The specified parameter "Period" is not valid. | The error message returned because the value of the Period parameter is invalid. |
| 400 | InvalidStartTime.Too Early | The specified parameter "StartTime" is too early. | The error message returned because the value of the StartTime parameter is invalid. |
| 400 | InvalidAllocationId.No tFound | Specified allocation id is not found. | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | OperationDenied.Too ManyDataQueried | Specified operation is denied as too many data to return. | The error message returned because the number of data entries to be returned has reached the upper limit. |
| 404 | Forbidden.RegionNot Found | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

#### 1.9.9 MoveResourceGroup

Moves a resource to a different resource group.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | MoveResourceGro up | The operation that you want to perform. Set the value to MoveResourceGroup. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| NewResourceGrou pId | String | Yes | rg- acfm3peow3k**** | The ID of the resource group to which the cloud resource is to be moved. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the cloud resource. You can call the DescribeRegions operation to query the most recent region list. |
| ResourceId | String | Yes | vpc- hp31psbg8ec3023 s6**** | The ID of the cloud resource that you want to move. |
| ResourceType | String | Yes | vpc | The type of the resource. Valid values: vpc: a virtual private cloud (VPC) eip: an elastic IP address (EIP) bandwidt hpackage: an EIP bandwidth plan |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F84A05B3-7275- 4C8B-8AEE- 9088C639C271 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=MoveResourceGroup &NewResourceGroupId=rg-acfm3peow3k**** &RegionId=cn-qingdao-env66-d01 &ResourceId=vpc-hp31psbg8ec3023s6**** &ResourceType=vpc
```

Sample success responses

```xml
<MoveResourceGroupResponse>
  <RequestId>F84A05B3-7275-4C8B-8AEE-9088C639C271</RequestId>
</MoveResourceGroupResponse>
```

```json
    "RequestId": "F84A05B3-7275-4C8B-8AEE-9088C639C271"
```

Error codes

| HttpCode | Error codes | Error message | Description |
|---|---|---|---|
| 400 | InvalidResourceGroupI d | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |

#### 1.9.10 DescribeHighDefinitionMonitorLogAttribute

Queries configurations about the fine-grained monitoring feature of an elastic IP address (EIP).

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHighDefini tionMonitorLogAtt ribute | The operation that you want to perform. Set the value to DescribeHighDef init ionMonit orLogAt t ribut e. |
| InstanceId | String | Yes | eip- wz9fi6qboho9fwg x7**** | The ID of the instance whose fine- grained monitoring configurations you want to query. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the EIP. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceType | String | No | EIP | The type of the instance. Set the value to EIP. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | eip- wz9fi6qboho9fwgx7 **** | The ID of the instance whose fine-grained monitoring configurations you want to query. |
| InstanceType | String | EIP | The type of the instance. Only EIP is returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogProject | String | hdmonitor-cn- qingdao- 1658206966225390 | The name of the project of Log Service. |
| LogStore | String | hdmonitor | The name of the Logstore of Log Service. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |
| Success | String | true | Indicates whether the operation is performed. Valid values: t rue: yes f alse: no |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHighDefinitionMonitorLogAttribute &InstanceId=eip-wz9fi6qboho9fwgx7**** &RegionId=cn-qingdao-env66-d01
```

Sample success responses

```json
<DescribeHighDefinitionMonitorLogAttributeResponse>
  <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
  <LogStore>hdmonitor</LogStore>
  <InstanceId>eip-wz9fi6qboho9fwgx7****</InstanceId>
  <InstanceType>EIP</InstanceType>
  <LogProject>hdmonitor-cn-qingdao-1658206966225390</LogProject>
  <Success>true</Success>
</DescribeHighDefinitionMonitorLogAttributeResponse>
    "RequestId": "54B48E3D-DF70-471B-AA93-08E683A1B457",
    "LogStore": "hdmonitor",
    "InstanceId": "eip-wz9fi6qboho9fwgx7****",
    "InstanceType": "EIP",
    "LogProject": "hdmonitor-cn-qingdao-1658206966225390",
    "Success": true
```

### 1.10 Router interface

#### 1.10.1 ConnectRouterInterface

Initiates a connection from the initiator router interface to the acceptor. After you call this operation, the router interface enters the Connecting state. When the connection is established, it enters the Active state. When you call this operation, take note of the following: Only an initiator router interface in the Idle state can initiate a connection. You can interconnect only a single pair of router interfaces between two routers. You cannot initiate a connection if your account contains a router interface with overdue payments.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConnectRouterInterf ace | The operation that you want to perform. Set the value to ConnectRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri-2ze7fbuohm**** | The ID of the initiator router interface. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=ConnectRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2ze7fbuohm****
```

```json
<? xml version="1.0" encoding="UTF-8"? > <ConnectRouterInterfaceResponse>
     <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
</ConnectRouterInterfaceResponse>
   "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907"
```

#### 1.10.2 DeactivateRouterInterface

Deactivates a router interface. After you call this operation, the router interface enters the Deactivating state. When the router interface is deactivated, it enters the Inactive state. Not e You cannot deactivate a router interface that has overdue payments.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeactivateRouterInt erface | The operation that you want to perform. Set the value to DeactivateRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri- 2zeo3xzyf38r4urz** ** | The ID of the router interface. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | BE7EB53A-99AB-4DA8- AEDE-75FA90D046A6 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeactivateRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** <? xml version="1.0" encoding="UTF-8"? > <DeactivateRouterInterfaceResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeactivateRouterInterfaceResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.10.3 ModifyRouterInterfaceSpec

Modifies the specifications of a router interface. After you call this operation, the router interface enters the Activating state. When the router interface is activated, it enters the Active state. Not e You cannot modify the specifications of a router interface that has overdue payments.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouterInterfa ceSpec | The operation that you want to perform. Set the value to ModifyRouterInterfaceSpec. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri- 2zeo3xzyf38r4urzd* *** | The ID of the router interface. |
| Spec | String | Yes | Large | The specifications of the router interface. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| Spec | String | Small.1 | The specifications of the router interface. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyRouterInterfaceSpec &RegionId=cn-hangzhou &Spec=Middle.2 &RouterInterfaceId=ri-2zeo3xzyf38r4urzd**** <? xml version="1.0" encoding="UTF-8"? > <ModifyRouterInterfaceSpecResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
     <Spec>Middle.2</Spec>
</ModifyRouterInterfaceSpecResponse>
     "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
     "Spec":"Middle.2"
```

#### 1.10.4 DeleteRouterInterface

Deletes a router interface. When you call this operation, take note of the following: You can only delete a router interface that is in the Idle or Inactive state. Before you delete a router interface, you must delete all custom route entries destined for the router interface.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouterInterfa ce | The operation that you want to perform. Set the value to DeleteRouterInterface. |
| RegionId | String | Yes | cn-shanghai | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri- 2zeo3xzyf38r4urz** ** | The ID of the router interface. |
| ClientToken | String | No | qwefcc1212333333 4f | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=DeleteRouterInterface &RegionId=cn-shanghai &RouterInterfaceId=ri-2zeo3xzyf38r4urz****
```

```json
<? xml version="1.0" encoding="UTF-8"? > <DeleteRouterInterfaceResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteRouterInterfaceResponse>
   "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.10.5 DescribeRouterInterfaces

Queries router interfaces in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouterInter faces | The operation that you want to perform. Set the value to DescribeRouterInterfaces. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interfaces that you want to query. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Filter.n.Key | String | No | Filter.1.status | Filter condition n. You can specify a maximum of five filter conditions. Valid values of n: 1 to 5. You can specify multiple values for each filter condition. The values are associated by the OR operator. If a router interface matches at least one of the values, it meets the filter condition. Multiple filter conditions are associated by the AND operator. A router interface is returned only if it meets all the filter conditions. The following filter conditions are available: RouterInterfaceId: the ID of the router interface. RouterId: the ID of the VRouter or VBR associated with the router interface. RouterType: the type of the router associated with the router interface. Valid values: VRouter and VBR. RouterInterfaceOwnerId: the account ID of the router interface. OppositeInterfaceId: the ID of the peer router interface. OppositeRouterType: the type of the router associated with the peer router interface. Valid values: VRouter and VBR. OppositeRouterId: the ID of the VRouter or VBR associated with the peer router interface. OppositeInterfaceOwnerId: the account ID of the peer router interface. Status: the status of the router interface. Name: the name of the router interface. |
| Filter.n.Value.m | String | No | Filter.1.Active | Value m of filter condition n. Valid values of m: 1 to 5. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C7F6FCBD-F9CC-4501- 8EF3-CDC9577CAE45 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| RouterInterfaceS et | List |   | Details about the router interface. For more information, see the RouterInterfaceType list. |

RouterInterfaceType list

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouterType | String | VRouter | The type of the router to which the route table belongs. Valid values: VRouter VBR |
| RouterInterfaceId | String | ri- 2zenfgfpyu3v93koa*** * | The ID of the router interface. |
| RouterId | String | vrt- bp1d3bxtdv68tfd7g*** * | The ID of the router to which the route table belongs. |
| Spec | String | Large | The specifications of the router interface. |
| Role | String | InitiatingSide | Indicates whether the router interface is the connection initiator or connection acceptor. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the router interface was created. |
| OppositeInterfac eOwnerId | String | 123157908552**** | The account ID of the owner of the peer router interface. |
| OppositeRouterT ype | String | VRouter | The type of the router associated with the peer router interface. |
| OppositeRouterId | String | vrt- bp1d3bxtdv68tfd7g*** * | The ID of the router associated with the peer router interface. |
| OppositeInterfac eId | String | ri- bp12dxgw8gmoma1h* *** | The ID of the peer router interface. |
| VpcInstanceId | String | vpc- 2ze3tq4uxhysg717x*** * | The ID of the local VPC for the peering connection. |

| irtual Private Cloud |   |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Status | String | active | The status of the router interface. |

Sample request s

```
https://vpc.example.com/?Action=DescribeRouterInterfaces &RegionId=cn-beijing
```

```xml
<? xml version="1.0" encoding="UTF-8" ? > <DescribeRouterInterfacesResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>FC2B35C9-15C5-4972-94B7-F529A1620AE0</RequestId>
    <RouterInterfaceSet>
        <RouterInterfaceType>
            <ChargeType>AfterPay</ChargeType>
            <OppositeInterfaceBusinessStatus>Normal</OppositeInterfaceBusinessStatus>
            <RouterInterfaceId>ri-2zepoga55p33dxxxxxxxx</RouterInterfaceId>
            <OppositeInterfaceStatus>Active</OppositeInterfaceStatus>
            <Spec>Small.1</Spec>
            <OppositeInterfaceOwnerId>12315790xxxxxxxx</OppositeInterfaceOwnerId>
            <OppositeInterfaceSpec>Negative</OppositeInterfaceSpec>
            <CreationTime>2018-04-19T07:35:00Z</CreationTime>
            <RouterType>VRouter</RouterType>
            <Status>Active</Status>
            <OppositeRouterType>VRouter</OppositeRouterType>
            <OppositeRouterId>vrt-m5ey5a8d65bmxxxxxxxx</OppositeRouterId>
            <OppositeInterfaceId>ri-m5eo6ht5pu2fxxxxxxxxx</OppositeInterfaceId>
            <VpcInstanceId>vpc-2zeugdd0wut2rhxxxxxxxx</VpcInstanceId>
            <RouterId>vrt-2zefso23vmu6xxxxxxxxx</RouterId>
            <ConnectedTime>2018-04-19T07:35:07Z</ConnectedTime>
            <OppositeRegionId>cn-qingdao</OppositeRegionId>
            <BusinessStatus>Normal</BusinessStatus>
            <Role>InitiatingSide</Role>
            <OppositeVpcInstanceId>vpc-m5ep989i7ocrtnxxxxxxxx</OppositeVpcInstanceId>
            <EndTime>2999-09-08T16:00:00Z</EndTime>
        </RouterInterfaceType>
        <RouterInterfaceType>
            <ChargeType>Prepaid</ChargeType>
            <OppositeInterfaceBusinessStatus>Normal</OppositeInterfaceBusinessStatus>
            <RouterInterfaceId>ri-2zegbp7nhj0mxxxxxxxx</RouterInterfaceId>
            <OppositeInterfaceStatus>Deleted</OppositeInterfaceStatus>
            <Spec>Small.1</Spec>
            <OppositeInterfaceOwnerId>1231579085529123</OppositeInterfaceOwnerId>
            <OppositeInterfaceSpec>Negative</OppositeInterfaceSpec>
            <CreationTime>2017-12-27T06:31:30Z</CreationTime>
            <RouterType>VRouter</RouterType>
            <Status>Inactive</Status>
            <OppositeRouterType>VRouter</OppositeRouterType>
            <OppositeRouterId>vrt-bp1d3bxtdv68txxxxxxxx</OppositeRouterId>
            <OppositeInterfaceId>ri-bp12dxgw8gmoxxxxxxxx</OppositeInterfaceId>
            <VpcInstanceId>vpc-2ze3tq4uxhysg7xxxxxxxx</VpcInstanceId>
            <RouterId>vrt-2zeazning6tbzkxxxxxxxx</RouterId>
            <ConnectedTime>2017-12-27T06:31:36Z</ConnectedTime>
            <OppositeRegionId>cn-hangzhou</OppositeRegionId>
            <BusinessStatus>Normal</BusinessStatus>
            <Role>InitiatingSide</Role>
            <OppositeVpcInstanceId>vpc-bp15k6sx6fhdzxxxxxxxx</OppositeVpcInstanceId>
            <EndTime>2018-07-27T16:00:00Z</EndTime>
        </RouterInterfaceType>
    </RouterInterfaceSet>
</DescribeRouterInterfacesResponse>
```

```json
    "PageNumber": 1,
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "FC2B35C9-15C5-4972-94B7-F529A1620AE0",
    "RouterInterfaceSet": {
        "RouterInterfaceType": [
                "ChargeType": "AfterPay",
                "OppositeInterfaceBusinessStatus": "Normal",
                "RouterInterfaceId": "ri-2zepoga55p33djxxxxxxxx",
                "OppositeInterfaceStatus": "Active",
                "Spec": "Small.1",
                "OppositeInterfaceOwnerId": "123157908xxxxxxxx",
                "OppositeInterfaceSpec": "Negative",
                "CreationTime": "2018-04-19T07:35:00Z",
                "RouterType": "VRouter",
                "Status": "Active",
                "OppositeRouterType": "VRouter",
                "OppositeRouterId": "vrt-m5ey5a8d65bmauxxxxxxxx",
                "OppositeInterfaceId": "ri-m5eo6ht5pu2fxxxxxxxxx",
                "VpcInstanceId": "vpc-2zeugdd0wut2rhxxxxxxxx",
                "RouterId": "vrt-2zefso23vmu6xi3xxxxxxxx",
                "ConnectedTime": "2018-04-19T07:35:07Z",
                "OppositeRegionId": "cn-qingdao",
                "BusinessStatus": "Normal",
                "Role": "InitiatingSide",
                "OppositeVpcInstanceId": "vpc-m5ep989i7ocrxxxxxxxx",
                "EndTime": "2999-09-08T16:00:00Z"
```

`},`

```json
                "ChargeType": "Prepaid",
                "OppositeInterfaceBusinessStatus": "Normal",
                "RouterInterfaceId": "ri-2zegbp7nhj0mnxxxxxxxx",
                "OppositeInterfaceStatus": "Deleted",
                "Spec": "Small.1",
                "OppositeInterfaceOwnerId": "1231579085xxxxxxxx",
                "OppositeInterfaceSpec": "Negative",
                "CreationTime": "2017-12-27T06:31:30Z",
                "RouterType": "VRouter",
                "Status": "Inactive",
                "OppositeRouterType": "VRouter",
                "OppositeRouterId": "vrt-bp1d3bxtdv68xxxxxxxx",
                "OppositeInterfaceId": "ri-bp12dxgw8gmomxxxxxxxx",
                "VpcInstanceId": "vpc-2ze3tq4uxhysgxxxxxxxx",
                "RouterId": "vrt-2zeazning6tbzkxxxxxxxx",
                "ConnectedTime": "2017-12-27T06:31:36Z",
                "OppositeRegionId": "cn-hangzhou",
                "BusinessStatus": "Normal",
                "Role": "InitiatingSide",
                "OppositeVpcInstanceId": "vpc-bp15k6sx6fhdzxxxxxxxx",
                "EndTime": "2018-07-27T16:00:00Z"
```

`]`

#### 1.10.6 ActivateRouterInterface

Activates a router interface that is in the Inactive state. After you call this operation, the router interface enters the Activating state. When the router interface is activated, it enters the Active state. Not e You cannot activate a router interface that has overdue payments.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ActivateRouterInterf ace | The operation that you want to perform. Set the value to ActivateRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri- 2zeo3xzyf38r4urz** ** | The ID of the router interface. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=ActivateRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2zeo3xzyf38r4urz****
```

```json
<? xml version="1.0" encoding="UTF-8"? > <ActivateRouterInterfaceResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
 </ActivateRouterInterfaceResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.10.7 ModifyRouterInterfaceAttribute

Modifies the configurations of a router interface.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouterInterfa ceAttribute | The operation that you want to perform. Set the value to ModifyRouterInterfaceAttribute. |
| RegionId | String | Yes | cn-shanghai | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri- 2zeo3xzyf38r4urz** ** | The ID of the router interface. |
| DeleteHealthCh eckIp | Boolea n | No | true | Specifies whether to delete the IP address for health checks configured on the router interface. Value values: true: The IP address for health checks is deleted. false (default): The IP address for health checks is not deleted. |
| OppositeRoute rId | String | No | vrt- bp1jcg5cmxjbl9xgc* *** | The ID of the router associated with the peer router interface. |
| OppositeInterf aceId | String | No | ri- 2zeo3xzyf38r4urz** ** | The ID of the peer router interface. |
| OppositeInterf aceOwnerId | String | No | 102561542445**** | The ID of the owner of the peer router interface. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| HealthCheckSo urceIp | String | No | 116.62.222.XX | The source IP address that is used to perform health checks on the physical connection. It must be an unused IP address in the local VPC. Not e You can specify this parameter in the scenario of physical connection access. |
| HealthCheckTar getIp | String | No | 116.62.222.XX | The destination IP address that is used to perform health checks on the physical connection. Not e This parameter is required when the HealthCheckSourceIp parameter is specified. |
| Name | String | No | TEST | The name of the router interface. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | aabbcc | The description of the router interface. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=ModifyRouterInterfaceAttribute &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &RegionId=cn-shanghai
```

```json
<? xml version="1.0" encoding="UTF-8"? > <ModifyRouterInterfaceAttributeResponse>
    <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</ModifyRouterInterfaceAttributeResponse>
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

#### 1.10.8 CreateRouterInterface

Creates a router interface. When you call this operation, take note of the following: You can only create one pair of interconnected router interfaces between two routers. You can create a maximum of five router interfaces for a router. If your account contains any router interface that has overdue payments, you cannot create new router interfaces. The destination CIDR blocks (DestinationCidrBlock) of route entries in the same route table cannot be the same. The router interface created for a VBR must act as the connection initiator. You can create a router interface for a VBR only when it is in the Active state. Not e Router interfaces created by calling the operation are billed on a daily basis.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouterInterfa ce | The operation that you want to perform. Set the value to CreateRouterInterface. |
| RegionId | String | Yes | cn-shanghai | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterType | String | Yes | VRouter | The type of the router associated with the router interface. Valid values: VRouter VBR |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| AccessPointId | String | No | ap-cn-shanghaiSZ- **** | The ID of the access point to which the VBR belongs. You can call the DescribeAccessPoints operation to query the most recent access point list. Not e You must specify this parameter in the scenario of physical connection access. |
| RouterId | String | Yes | vrt- o6w678x9md98wp8 93**** | The ID of the router associated with the router interface. |
| Role | String | Yes | InitiatingSide | The role of the router interface. Valid values: InitiatingSide: connection initiator AcceptingSide: connection acceptor |
| Spec | String | Yes | Large.1 | The specifications of the router interface. The available specifications and the corresponding bandwidths are as follows: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1000 Mbit/s Large.2: 2000 Mbit/s Large.5: 5000 Mbit/s Xlarge.1: 10000 Mbit/s |
| OppositeRegio nId | String | Yes | cn-hangzhou | The region ID of the connection acceptor. |
| OppositeAcces sPointId | String | No | ap-cn-shanghaiSZ- **** | The ID of the access point of the peer router interface. Not e This parameter must be specified when the peer router interface is on a VBR. The value cannot be modified after the router interface is created. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| OppositeRoute rType | String | No | VRouter | The type of the router associated with the peer router interface. Valid values: VRouter VBR |
| OppositeRoute rId | String | No | vrt- bp1lhl0taikrteen8*** * | The ID of the router associated with the peer router interface. |
| OppositeInterf aceId | String | No | ri- 2zeo3xzyf38r4urzd* *** | The ID of the peer router interface. |
| OppositeInterf aceOwnerId | String | No | 1251452541**** | The ID of the owner of the peer router interface. |
| HealthCheckSo urceIp | String | No | 116.62.222.XX | The source IP address that is used to perform health checks on the physical connection. It must be an unused IP address in the local VPC. Not e You can specify this parameter in the scenario of physical connection access. |
| HealthCheckTar getIp | String | No | 116.62.222.XX | The destination IP address that is used to perform health checks on the physical connection. Not e This parameter is required when the HealthCheckSourceIp parameter is specified. |
| Name | String | No | abc | The name of the router interface. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the router interface. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | sjffha123334 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |
| RouterInterfaceId | String | ri-2ze7fbuohm**** | The ID of the router interface. |

Sample request s

```json
https://vpc.example.com/?Action=CreateRouterInterface &RegionId=cn-beijing &Role=InitiatingSide &OppositeRegionId=cn-beijing &Spec=Mini.5 &RouterType=VRouter &RouterId=vrt-o6w678x9md98wp893**** &OppositeRouterId=vrt-bp1lhl0taikrteen8**** <? xml version="1.0" encoding="UTF-8"? > <CreateRouterInterfaceResponse>
    <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
    <RouterInterfaceId>ri-2ze7fbuohm****</RouterInterfaceId>
</CreateRouterInterfaceResponse>
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
    "RouterInterfaceId": "ri-2ze7fbuohm****"
```

### 1.11 Physical connection

#### 1.11.1 CreatePhysicalConnection

Creates a physical connection. After you create a physical connection, it enters the Initial state, and you can contact the carrier to begin construction. When you call this operation, take note of the following: If the number of physical connections that are not in the Enabled state exceeds five, you cannot create a physical connection. If your account contains a physical connection that has overdue payments, you cannot create a physical connection.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalConn ection | The operation that you want to perform. Set the value to CreatePhysicalConnection. |
| RegionId | String | Yes | cn-shanghai | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |
| AccessPointId | String | Yes | AccessPointId=ap- cn-beijing-ft-A | The ID of the access point that is associated with the physical connection. You can call the DescribeAccessPoints operation to query the most recent access point list. |
| CircuitCode | String | No | longtel001 | The circuit code provided by the carrier for the physical connection. |
| LineOperator | String | Yes | CT | The carrier that provides the line. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other carriers in China Equinix: Equinix Other: other carriers outside China |
| PeerLocation | String | Yes | Zhejiang province -- - vfjdbg 21e _ | The geographical location of the on-premises data center. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Bandwidth | String | No | 10 | The bandwidth of the physical connection. Unit: Mbit/s. Valid values: 2 to 10240. Default value: 100. |
| PortType | String | No | 1000Base-T | The access port type of the physical connection. Valid values: 100Base-T: 100M electrical port 1000Base-T (default): GE electrical port 1000Base-LX: GE single-mode optical port (10 km) 10GBase-T: 10GE electrical port 10GBase-LR: 10GE single-mode optical port (10 km) |
| RedundantPhys icalConnectionI d | String | No | pc-119mfjzm7**** | The ID of the redundant physical connection. The redundant physical connection must be in the Allocated, Confirmed, or Enabled state. |
| Name | String | No | test | The name of the physical connection. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the physical connection. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | dgfdg12344ff | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | pc- bp1qrb3044eqixog0*** * | The ID of the request. |

| irtual Private Cloud |   |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nId | String | 8A6A5EC5-6F6C-4906- 9689-56ACE58A13E0 | The ID of the VPC. |

Sample request s

```json
https://vpc.example.com/?Action=CreatePhysicalConnection &RegionId=cn-beijing &AccessPointId=ap-cn-beijing-ft-A &LineOperator=CT &PeerLocation=XXX <? xml version="1.0" encoding="UTF-8"? >
 <CreatePhysicalConnectionResponse>
     <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0"</RequestId>
     <PhysicalConnectionId>pc-bp1qrb3044eqixog0****</PhysicalConnectionId>
</CreatePhysicalConnectionResponse>
    "PhysicalConnectionId": "pc-bp1qrb3044eqixog0****",
    "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0"
```

#### 1.11.2 CancelPhysicalConnection

Cancels a physical connection that is not enabled. After you have canceled the physical connection, it enters the Canceled state. You can only cancel a physical connection that is in the Initial, Approved, Allocated, or Confirmed state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelPhysicalConn ection | The operation that you want to perform. Set the value to CancelPhysicalConnection. |
| RegionId | String | Yes | cn-shanghai | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |

| Developer Guide·A | PI referen | ce |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| PhysicalConnec tionId | String | Yes | pc-119mfjzm7**** | The ID of the physical connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=CancelPhysicalConnection &PhysicalConnectionId=pc-119mfjzm7**** &RegionId=cn-beijing <? xml version="1.0" encoding="UTF-8"? > <CancelPhysicalConnectionResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</CancelPhysicalConnectionResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.11.3 DeletePhysicalConnection

Deletes a physical connection. You can only delete a physical connection that is in the Rejected, Canceled, AllocationFailed, or Terminated state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePhysicalConn ection | The operation that you want to perform. Set the value to DeletePhysicalConnection. |

| V | irtual Private Clou | d |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |
| PhysicalConnec tionId | String | Yes | pc-119mfjzm7**** | The ID of the physical connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2B3670CD-670E-4540- 8C13-6DE929AEDD3B | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeletePhysicalConnection &PhysicalConnectionId=pc-119mfjzm7**** &RegionId=cn-beijing <? xml version="1.0" encoding="UTF-8"? > <DeletePhysicalConnectionResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeletePhysicalConnectionResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.11.4 ModifyPhysicalConnectionAttribute

Modifies the configurations of a physical connection. When you call this operation, take note of the following: You can modify the specifications of a physical connection or the ID of its redundant physical connection only when the physical connection is in the Initial or Rejected state. You cannot modify the configurations of a physical connection that is in the Canceled, Allocating, AllocationFailed, or Terminated state. After you modify the configurations of a physical connection in the Rejected state, the physical connection enters the Initial state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyPhysicalConn ectionAttribute | The operation that you want to perform. Set the value to ModifyPhysicalConnectionAttribute. |
| RegionId | String | Yes | cn-shanghai | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |
| PhysicalConnec tionId | String | Yes | pc-119mfjzm7**** | The ID of the physical connection. |
| LineOperator | String | No | CT | The carrier that provides the line. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other carriers in China Equinix: Equinix Other: other carriers outside China |
| CircuitCode | String | No | longtel001 | The circuit code provided by the carrier for the physical connection. |
| PeerLocation | String | No | Zhejiang province -- - vfjdbg 21e _ | The geographical location of the on-premises data center. |
| Bandwidth | String | No | 10 | The bandwidth of the physical connection. Unit: Mbit/s. Valid values: 2 to 10240. Default value: 100. |
| PortType | String | No | 100Base-T | The access port type of the physical connection. Valid values: 100Base-T: 100M electrical port 1000Base-T (default): GE electrical port 1000Base-LX: GE single-mode optical port (10 km) 10GBase-T: 10GE electrical port 10GBase-LR: 10GE single-mode optical port (10 km) |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RedundantPhys icalConnectionI d | String | No | pc-119mfjzm7**** | The ID of the redundant physical connection. The redundant physical connection must be in the Allocated, Confirmed, or Enabled state. |
| Name | String | No | test | The name of the physical connection. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the physical connection. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | efefe566754h | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 013EE132-A109-4247- 91B0-099A8FF49AD7 | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=ModifyPhysicalConnectionAttribute &PhysicalConnectionId=pc-2zeoaxkq3x**** &RegionId=cn-beijing &Name=test3
```

```json
<? xml version="1.0" encoding="UTF-8"? > <ModifyPhysicalConnectionAttributeResponse>
    <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0"</RequestId>
</ModifyPhysicalConnectionAttributeResponse>
      "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0"
```

#### 1.11.5 DescribePhysicalConnections

You can call this operation to query physical connections in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePhysicalCon nections | The operation that you want to perform. Set the value to DescribePhysicalConnections. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the physical connections. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Filter.n.Key | String | No | Filter.1.PhysicalConn ectionId | Filter condition n. You can specify a maximum of five filter conditions. Valid values of n: 1 to 5. You can specify multiple values for each filter condition. The logic relationship among multiple values is OR. If a physical connection matches at least one of the values, it meets the filter condition. Multiple filter conditions are associated by the AND operator. A physical connection is returned only when it meets all the filter conditions. The following filter conditions are available: PhysicalConnectionId: the ID of the physical connection. AccessPointId: the ID of the access point. Type: the type of the physical connection. Default value: VPC. LineOperator: the carrier that provides the physical connection. Status: the status of the physical connection. Spec: the specifications of the physical connection. Name: the name of the physical connection. |
| Filter.n.Value.m | String | No | Filter.1.pc- bp1qrb3044eqixog0 **** | Value m of filter condition n. Valid values of m: 1 to 5. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EEC8EAB1-F299-4F5C- 8E54-0A3129164C27 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |

| Developer Guide·API | reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nSet | List |   | The details about physical connections. For more information, see the PhysicalConnectionSet list. |

PhysicalConnectionSet list

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nId | String | pc- bp1qrb3044eqixog0*** * | The ID of the physical connection. |
| AccessPointId | String | ap-cn-beijing-dx-A | The ID of the access point that is associated with the physical connection. |
| Status | String | Initial | The status of the physical connection. Valid values: Initial: application in progress Approved: approved Allocating: resource allocation in progress Allocated: under construction Confirmed: waiting for user confirmation Enabled: enabled Rejected: rejected Canceled: canceled Allocation Failed: resource allocation failed Terminated: terminated |
| BusinessStatus | String | Normal | The payment status of the physical connection. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| CreationTime | String | 2017-12- 13T02:28:42Z | The time when the physical connection was created. |
| EnabledTime | String | 2017-12- 13T02:28:42Z | The time when the physical connection was enabled. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LineOperator | String | CT | The carrier that provides the physical connection. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other carriers in China Equinix: Equinix Other: other carriers outside China |
| Spec | String | Large | The specifications of the physical connection. |
| PeerLocation | String | Zhejiang province --- vfjdbg 21e _ | The geographical location of the on-premises data center. |
| PortType | String | 100Base-T | The ingress port type of the physical connection. Valid values: 100Base-T: 100M copper port 1000Base-T (default): GE electrical port 1000Base-LX: GE single-mode fiber port (10 km) 10GBase-T: 10GE electrical port 10GBase-LR: 10GE single-mode optical port (10 km) |
| RedundantPhysic alConnectionId | String | pc- bp1qrb3044eqixog0*** * | The ID of the redundant physical connection. |
| Name | String | aaa | The name of the physical connection. |
| Description | String | abcabc | The description of the physical connection. |
| ADLocation | String | Room Ax-x Bxx, building xx, xxx Avenue, Nanshan District, Shenzhen city, Guangdong province | The location of the physical access device. |
| PortNumber | String | 80 | The port number of the physical access device. |
| CircuitCode | String | longtel001 | The circuit code provided by the carrier for the physical connection. |
| Bandwidth | String | 10 | The bandwidth of the physical connection. |

Sample request s

```xml
https://vpc.example.com/?Action=DescribePhysicalConnections &RegionId=cn-beijing <?xml version="1.0" encoding="UTF-8"?> <DescribePhysicalConnectionsResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>7C07B0AF-4FC0-4BB2-9667-F75812824BCD</RequestId>
    <PhysicalConnectionSet>
        <PhysicalConnectionType>
            <Type>VPC</Type>
            <PhysicalConnectionId>pc-2zeoaxkq3jot5pxxxxxxxx</PhysicalConnectionId>
            <PeerLocation>XXX-XX District--XXX Road </PeerLocation>
            <CreationTime>2017-12-13T02:28:42Z</CreationTime>
            <Name>TEST</Name>
            <Status>Enabled</Status>
            <AdLocation>XXX--XX-XXX Datacenter XX Network Cabinet XXU</AdLocation>
            <EnabledTime>2017-12-18T04:01:30Z</EnabledTime>
            <BusinessStatus>Normal</BusinessStatus>
            <LineOperator>CT</LineOperator>
            <PortNumber>1/1/4</PortNumber>
            <AccessPointId>ap-cn-beijing-xx-x</AccessPointId>
            <PortType>100Base-T</PortType>
            <Bandwidth>2</Bandwidth>
        </PhysicalConnectionType>
    </PhysicalConnectionSet>
</DescribePhysicalConnectionsResponse>
```

```json
  "PageNumber": 1,
  "TotalCount": 1,
  "PageSize": 10,
  "RequestId": "7C07B0AF-4FC0-4BB2-9667-F75812824BCD",
  "PhysicalConnectionSet": {
    "PhysicalConnectionType": [
        "Type": "VPC",
        "PhysicalConnectionId": "pc-2zeoaxkq3jot5xxxxxxxx",
        "PeerLocation": "XXX-XX District--XXX Road",
        "CreationTime": "2017-12-13T02:28:42Z",
        "Name": "TEST",
        "Status": "Enabled",
        "AdLocation": "XXX--XX-XXX Datacenter XX Network Cabinet XXU",
        "EnabledTime": "2017-12-18T04:01:30Z",
        "BusinessStatus": "Normal",
        "LineOperator": "CT",
        "PortNumber": "1/1/4",
        "AccessPointId": "ap-cn-beijing-xx-x",
        "PortType": "100Base-T",
        "Bandwidth": 2
```

`]`

#### 1.11.6 TerminatePhysicalConnection

You can call this operation to terminate an enabled leased line. After you call this operation, the physical connection enters the Terminating state. When the physical connection is terminated, it enters the Terminated state. When you call this operation, make sure that the following requirements are met: You can only terminate a physical connection in the Enabled state. Before you terminate a physical connection, you must delete the VBRs associated with it.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminatePhysicalC onnection | The operation that you want to perform. Set the value to TerminatePhysicalConnection. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| PhysicalConnec tionId | String | Yes | pc-2zeoaxkq3x**** | The ID of the physical connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=TerminatePhysicalConnection &PhysicalConnectionId=pc-2zeoaxkq3x**** &RegionId=cn-beijing <?xml version="1.0" encoding="UTF-8"?> <TerminatePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</TerminatePhysicalConnectionResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.11.7 EnablePhysicalConnection

Enables a physical connection that is in the Confirmed state. After you enable the physical connection, it enters the Enabled state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnablePhysicalConn ection | The operation that you want to perform. Set the value to EnablePhysicalConnection. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |
| PhysicalConnec tionId | String | Yes | pc-2zeoaxkq3x**** | The ID of the physical connection. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20365164-5b0d-460a- 83c2-2189972b3349 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=EnablePhysicalConnection &PhysicalConnectionId=pc-2zeoaxkq3x**** &RegionId=cn-beijing <? xml version="1.0" encoding="UTF-8"? > <EnablePhysicalConnectionResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</EnablePhysicalConnectionResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

### 1.12 Virtual border router

#### 1.12.1 CreateVirtualBorderRouter

Creates a VBR. You can create two VBRs for each physical connection. One belongs to the current account and the other belongs to a different account. If you create a VBR for the current account, the VBR is in the Enabled state after the operation is called. If you create a VBR for another account, the VBR is in the Unconfirmed state after the operation is called.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVirtualBorder Router | The operation that you want to perform. Set the value to CreateVirtualBorderRouter. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |
| PhysicalConnec tionId | String | Yes | pc- 2zeoaxkq3jotcd34** ** | The ID of the physical connection. |
| VbrOwnerId | String | No | 1256321452**** | The account ID of the VBR owner. The default value is the ID of the current account, which is the owner of the physical connection. |
| VlanId | String | Yes | 10 | The VLAN ID of the VBR. Valid values: 1 to 2999. Not e Only the owner of the physical connection can specify this parameter. The VLAN IDs of two VBRs of the same physical connection must be different. |
| CircuitCode | String | Yes | longtel001 | The circuit code provided by the carrier for the physical connection. Not e Only the owner of the physical connection can specify this parameter. |
| LocalGatewayI p | String | Yes | 116.62.222.XX | The IP address configured on the Apsara Stack VPC side for interconnecting the VPC with your on-premises data center. |

| V | irtual Private Clou | d |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| PeerGatewayIp s | String | Yes | 116.62.222.XX | The IP address configured on your side for interconnecting your on-premises data center with Apsara Stack VPC. |
| PeeringSubnet Mask | String | No | 255.255.255.252 | The subnet mask for the IP address configured on the Apsara Stack VPC side and the IP address configured on your side. The two IP addresses must belong to the same subnet. |
| Name | String | No | test | The name of the VBR. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| VbrId | String | vbr- bp1jcg5cmxjbl9xgc**** | The ID of the VBR. |

Sample request s

```json
https://vpc.example.com/?Action=CreateVirtualBorderRouter &PhysicalConnectionId=pc-2zeoaxkq3jotcd34**** &RegionId=cn-hangzhou &VlanId=10 <? xml version="1.0" encoding="UTF-8"? > <CreateRouterInterfaceResponse>
        <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
        <VbrId>vbr-bp1jcg5cmxjbl9xgc****</VbrId>
</CreateRouterInterfaceResponse>
     "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
     "VbrId": "vbr-bp1jcg5cmxjbl9xgc****"
```

#### 1.12.2 DeleteVirtualBorderRouter

Deletes a VBR. When you call this operation, take note of the following: Before you delete a VBR, you must delete all router interfaces on the VBR. You can only delete a VBR that is in the Unconfirmed, Enabled, or Terminated state. The owner of a physical connection can delete a VBR under another account only when the VBR is in the Unconfirmed state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVirtualBorder Router | The operation that you want to perform. Set the value to DeleteVirtualBorderRouter. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp12mw1f8k3jgygk 9**** | The ID of the VBR. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeleteVirtualBorderRouter &VbrId=vbr-bp12mw1f8k3jgygk9**** <? xml version="1.0" encoding="UTF-8"? > <DeleteVirtualBorderRouterResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVirtualBorderRouterResponse>
   "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.12.3 DescribeVirtualBorderRouters

Queries created VBRs.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBord erRouters | The operation that you want to perform. Set the value to DescribeVirtualBorderRouters. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Filter.n.Key | String | No | Filter.1.PhysicalConn ectionId | Filter condition n. You can specify a maximum of five filter conditions. Valid values of n: 1 to 5. You can specify multiple values for each filter condition. The values are associated by the OR operator. If a VBR matches at least one of the values, it meets the filter condition. Multiple filter conditions are associated by the AND operator. A VBR is returned only if it meets all the filter conditions. The following filter conditions are available: PhysicalConnectionId: the ID of the physical connection. VbrId: the ID of the VBR. Status: the status of the VBR. AccessPointId: the ID of the access point that is associated with the physical connection. Name: the name of the VBR. |
| Filter.n.Value.m | String | No | Filter.1.pc- 119mfjzm7az12**** | Value m of filter condition n. Valid values of m: 1 to 5. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DE77A7F3-3B74-41C0- A5BC-CAFD188C28B6 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| VirtualBorderRout erSet | List |   | The list of VBRs. For more information, see the VirtualBorderRouterSet list. |

VirtualBorderRouterSet list

| Parameter | Type | Example | Description |
|---|---|---|---|
| VbrId | String | vbr-kojok19xsc12**** | The ID of the VBR. |
| VbrOwnerUid | String | 12356311**** | The account ID of the VBR owner. When the VBR owner and the physical connection owner are the same, this parameter is empty. |
| CreationTime | Integer | 2017-06-08T12:20:55 | The time when the VBR was created. |
| ActivationTime | String | 2017-06-08T12:20:55 | The first time when the VBR was activated. |
| TerminationTime | String | 2017-08-08T12:20:55 | The last time when the VBR was terminated. |
| RecoveryTime | String | 2017-06-08T12:20:55 | The last time when the VBR was recovered from the Terminated state to the Active state. |
| Status | String | active | The status of the VBR. |
| VlanId | String | 10 | The VLAN ID of the VBR. |
| CircuitCode | String | longtel001 | The circuit code provided by the carrier for the physical connection. |
| RouteTableId | String | rtb-bp1nsxcdfv34d**** | The ID of the route table of the VBR. |
| VlanInterfaceId | String | ri- 2zeum6rgu0586gjro*** * | The ID of the router interface of the VBR. |
| LocalGatewayIp | String | 116.62.xx.xx | The IP address configured on the Apsara Stack VPC side for interconnecting the VPC with your on-premises data center. |
| PeerGatewayIp | String | 116.62.xx.xx | The IP address configured on your side for interconnecting your on-premises data center with Apsara Stack VPC. |
| PeeringSubnetMa sk | String | 255.0.0.0 | The subnet mask for the IP address configured on the Apsara Stack VPC side and the IP address configured on your side. |
| Name | String | test | The name of the VBR. |
| Description | String | abcabc | The description of the VBR. |
| PhysicalConnectio nId | String | pc-119mfjzm7cdx2**** | The ID of the physical connection to which the VBR connects. |
| AccessPointId | String | ap-cn-kojok1xxxxxxxx | The ID of the access point that is associated with the physical connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Initial | The status of the physical connection. Valid values: Initial: application in progress Approved: approved Allocating: resource allocation in progress Allocated: under construction Confirmed: waiting for user confirmation Enabled: enabled Rejected: rejected Canceled: canceled Allocation Failed: resource allocation failed Terminated: terminated |
| BusinessStatus | String | Normal | The payment status of the physical connection. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |

Sample request s

```
https://vpc.example.com/?Action=DescribeVirtualBorderRouters &RegionId=cn-beijing
```

```xml
<? xml version="1.0" encoding="UTF-8"? > <DescribeVirtualBorderRoutersResponse>
    <RequestId>AE65530E-8436-4FB1-8217-DCD35712AC89</RequestId>
    <PageNumber>1</PageNumber>
    <VirtualBorderRouterSet>
        <VirtualBorderRouterType>
            <LocalGatewayIp>116.62.xx.xx</LocalGatewayIp>
            <PeerGatewayIp>116.62.xx.xx</PeerGatewayIp>
            <Description></Description>
            <PhysicalConnectionOwnerUid>12356311****</PhysicalConnectionOwnerUid>
            <VlanId>10</VlanId>
            <RecoveryTime></RecoveryTime>
            <PhysicalConnectionStatus>Enabled</PhysicalConnectionStatus>
            <PhysicalConnectionId>pc-119mfjzm7cdx2****</PhysicalConnectionId>
            <RouteTableId>rtb-bp1nsxcdfv34d****</RouteTableId>
            <PeeringSubnetMask>255.0.0.0</PeeringSubnetMask>
            <TerminationTime></TerminationTime>
            <Name></Name>
            <CreationTime>2018-03-06T11:16:34Z</CreationTime>
            <ActivationTime>2018-03-06T11:16:34Z</ActivationTime>
            <CircuitCode></CircuitCode>
            <Status>active</Status>
            <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessStatus>
            <VlanInterfaceId>ri-2zeum6rgu0586gjro****</VlanInterfaceId>
            <AccessPointId>ap-cn-beijing-dx-A</AccessPointId>
            <VbrId>vbr-2zecmmvg5gvu8i4te****</VbrId>
        </VirtualBorderRouterType>
    </VirtualBorderRouterSet>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
</DescribeVirtualBorderRoutersResponse>
```

```json
  "PageNumber": 1,
  "VirtualBorderRouterSet": {
    "VirtualBorderRouterType": [
        "LocalGatewayIp": "116.62.xx.xx",
        "PeerGatewayIp": "116.62.xx.xx",
        "Description": "",
        "PhysicalConnectionOwnerUid": "12356311****",
        "VlanId": 10,
        "RecoveryTime": "",
        "PhysicalConnectionStatus": "Enabled",
        "PhysicalConnectionId": "pc-119mfjzm7cdx2****",
        "RouteTableId": "rtb-bp1nsxcdfv34d****",
        "PeeringSubnetMask": "255.0.0.0",
        "TerminationTime": "",
        "Name": "",
        "CreationTime": "2018-03-06T11:16:34Z",
        "ActivationTime": "2018-03-06T11:16:34Z",
        "CircuitCode": "",
        "Status": "active",
        "PhysicalConnectionBusinessStatus": "Normal",
        "VlanInterfaceId": "ri-2zeum6rgu0586gjro****",
        "AccessPointId": "ap-cn-beijing-dx-A",
        "VbrId": "vbr-2zecmmvg5gvu8i4te****"
  "TotalCount": 1,
  "PageSize": 10,
  "RequestId": "98B24329-ADC9-4725-A5F8-6C1B282DA17D"
```

#### 1.12.4 DescribeVirtualBorderRoutersForPhysicalConnection

Queries the VBRs connected to a specified physical connection, including VBRs that belong to the physical connection owner and other accounts.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBord erRoutersForPhysica lConnection | The operation that you want to perform. Set the value to DescribeVirtualBorderRoutersForPhysicalConnecti on. |
| RegionId | String | Yes | cn-beijing | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| PhysicalConnec tionId | String | No | pc- bp1qrb3044eqixog0 f**** | The ID of the physical connection. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7C5AE8B3-A2D8-428D- A2FF-93A225C0821E | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| VirtualBorderRout erForPhysicalCon nectionSet | List |   | The list of VBRs. For more information, see the VirtualBorderRouterForPhysicalConnectionSet list. |

VirtualBorderRouterForPhysicalConnectionSet list

| Parameter | Type | Example | Description |
|---|---|---|---|
| VbrId | String | vbr- bp16ksp61j7e0tkn**** | The ID of the VBR. |
| VbrOwnerUid | String | 12363253**** | The account ID of the VBR owner. When the VBR owner and the physical connection owner are the same, this parameter is empty. |
| CreationTime | Integer | 2017-06-08T12:20:55 | The time when the VBR was created. |
| ActivationTime | String | 2017-06-08T12:20:55 | The first time when the VBR was activated. |
| TerminationTime | String | 2017-06-08T12:20:55 | The last time when the VBR was terminated. |
| RecoveryTime | String | 2017-06-08T12:20:55 | The last time when the VBR was recovered from the Terminated state to the Active state. |
| VlanId | String | 10 | The VLAN ID of the VBR. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CircuitCode | String | longtel001 | The circuit code provided by the carrier for the physical connection. |

Sample request s

```xml
https://vpc.example.com/?Action=DescribeVirtualBorderRoutersForPhysicalConnection &RegionId=cn-beijing &PhysicalConnectionId=pc-bp1qrb3044eqixog0f**** <? xml version="1.0" encoding="UTF-8"? > <DescribeVirtualBorderRoutersForPhysicalConnectionResponse>
    <RequestId>03E8CB87-5876-4034-BBB2-6E0851281C37</RequestId>
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <PageSize>10</PageSize>
    <VirtualBorderRouterForPhysicalConnectionSet>
        <VirtualBorderRouterForPhysicalConnectionType>
            <ActivationTime>2018-03-06T11:16:34Z</ActivationTime>
            <CreationTime>2018-03-06T11:16:34Z</CreationTime>
            <CircuitCode></CircuitCode>
            <VlanId>10</VlanId>
            <RecoveryTime></RecoveryTime>
            <VbrOwnerUxxx231579085529123
            </VbrOwnerUid>
            <TerminationTime></TerminationTime>
            <VbrId>Vbr-2zecmmvg5gvu8ibgcd****</VbrId>
        </VirtualBorderRouterForPhysicalConnectionType>
        <VirtualBorderRouterForPhysicalConnectionType>
            <ActivationTime>2018-01-04T13:34:18Z</ActivationTime>
            <CreationTime>2018-01-04T13:34:18Z</CreationTime>
            <CircuitCode></CircuitCode>
            <VlanId>100</VlanId>
            <RecoveryTime></RecoveryTime>
            <VxxxbrOwnerUid>12315790xxxxxxxx
            </VbrOwnerUid>
            <TerminationTime></TerminationTime>
            <VbrId>vbr-2zee2e2cwetx4k0xswe****</VbrId>
        </VirtualBorderRouterForPhysicalConnectionType>
 </DescribeVirtualBorderRoutersForPhysicalConnectionResponse>
```

```json
    "PageNumber": 1,
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "03E8CB87-5876-4034-BBB2-6E0851281C37",
    "VirtualBorderRouterForPhysicalConnectionSet": {
        "VirtualBorderRouterForPhysicalConnectionType": [
                "ActivationTime": "2018-03-06T11:16:34Z",
                "CreationTime": "2018-03-06T11:16:34Z",
                "CircuitCode": "",
                "VlanId": 10,
                "RecoveryTime": "",
                "VbrOwnerUid": "1231579085xxxxxx529123",
                "TerminationTime": "",
                "VbrId": "Vbr-2zecmmvg5gvu8ibgcd****"
```

`},`

```json
                "ActivationTime": "2018-01-04T13:34:18Z",
                "CreationTime": "2018-01-04T13:34:18Z",
                "CircuitCode": "",
                "VlanId": 100,
                "RecoveryTime": "",
                "VbrOwnerUid": "12315xxxxxxxx",
                "TerminationTime": "",
                "VbrId": "vbr-2zee2e2cwetx4k0xswe****"
```

`]`

#### 1.12.5 ModifyVirtualBorderRouterAttribute

Modifies the configurations of a VBR.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVirtualBorder RouterAttribute | The operation that you want to perform. Set the value to ModifyVirtualBorderRouterAttribute. |
| RegionId | String | Yes | cn-shanghai | The region ID of the physical connection. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- 2zee2e2cwetxcdfv* *** | The ID of the VBR. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| VlanId | String | Yes | 10 | The VLAN ID of the VBR. Valid values: 1 to 2999. Not e Only the owner of the physical connection can specify this parameter. The VLAN IDs of two VBRs of the same physical connection must be different. |
| CircuitCode | String | Yes | longtel001 | The circuit code provided by the carrier for the physical connection. Not e Only the owner of the physical connection can specify this parameter. |
| LocalGatewayI p | String | Yes | 116.62.xx.xx | The IP address configured on the Apsara Stack VPC side for interconnecting the VPC with your on-premises data center. |
| PeerGatewayIp s | String | Yes | 116.62.xx.xx | The IP address configured on your side for interconnecting your on-premises data center with Apsara Stack VPC. |
| PeeringSubnet Mask | String | No | 255.255.255.0 | The subnet mask for the IP address configured on the Apsara Stack VPC side and the IP address configured on your side. The two IP addresses must belong to the same subnet. |
| Name | String | No | test | The name of the VBR. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyVirtualBorderRouterAttribute &VbrId=vbr-2zee2e2cwetxcdfv**** &Name=test <? xml version="1.0" encoding="UTF-8"? > <ModifyVirtualBorderRouterAttributeResponse>
    <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</ModifyVirtualBorderRouterAttributeResponse>
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

#### 1.12.6 TerminateVirtualBorderRouter

You can call this operation to terminate a VBR. After the operation is called, the VBR changes from the Enabled state to the Terminating state. After the VBR is terminated, it enters the Terminated state. When you call this operation, take note of the following: Only the owner of the leased line to which the VBR connects can call this operation. If the VBR has been in the Terminated state for seven days or longer, its VLAN ID can be allocated to other VBRs.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminateVirtualBor derRouter | The operation that you want to perform. Set the value to TerminateVirtualBorderRouter. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |

| Developer Guide·A | PI referen | ce |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Requi red | Example | Description |
| VbrId | String | Yes | vbr- bp15zckdt37pq72** ** | The ID of the VBR. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=TerminateVirtualBorderRouter &VbrId=vbr-bp15zckdt37pq72**** <?xml version="1.0" encoding="UTF-8"?> <TerminateVirtualBorderRouterResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</TerminateVirtualBorderRouterResponse>
   "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.12.7 RecoverVirtualBorderRouter

Recovers a terminated VBR. After the operation is called, the VBR changes from the Terminated state to the Recovering state. When the VBR recovers, it enters the Enabled state. When you call this operation, take note of the following: Only the owner of the physical connection to which the VBR connects can call this operation. The physical connection to which the VBR connects must be in the Enabled state. If the VBR has been in the Terminated state for seven days or longer, its VLAN ID can be allocated to other VBRs. In this case, the recovery fails.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RecoverVirtualBorde rRouter | The operation that you want to perform. Set the value to RecoverVirtualBorderRouter. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp1lhl0taikrte**** | The ID of the VBR. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=RecoverVirtualBorderRouter &VbrId=vbr-bp1lhl0taikrte**** <? xml version="1.0" encoding="UTF-8"? > <RecoverVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</RecoverVirtualBorderRouterResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

### 1.13 NAT Gateway

#### 1.13.1 CreateNatGateway

You can call this operation to create a NAT gateway. When you call this operation, take note of the following: You are not allowed to create a NAT gateway and a user-created SNAT gateway in the same VPC network if the SNAT gateway is deployed on an Elastic Compute Service (ECS) instance. After you create a NAT gateway, a route entry is automatically added to the routing table of the VPC. The destination CIDR block is 0.0.0.0/0 and the next hop is the NAT gateway. The route entry ensures that traffic is routed to the NAT gateway. If the route table of the VPC already contains an entry with a destination CIDR block of 0.0.0.0/0, delete this entry. Otherwise, you cannot create a NAT gateway. You can specify the type of a NAT gateway as needed. The type of a NAT gateway determines its SNAT performance, including the maximum number of connections and the number of new connections per second, but it does not affect the data throughput. The following table describes the correlations between NAT gateway types and SNAT performance metrics.

| Type | Maximum connections | New connections per second |
|---|---|---|
| Small | 10,000 | 1,000 |
| Medium | 50,000 | 5,000 |
| Large | 200,000 | 10,000 |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNatGateway | The operation that you want to perform. Set the value to CreateNatGateway. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1di7uewzmtvfuq 8**** | The ID of the VPC. |
| Spec | String | No | Large | The type of the NAT gateway. Valid values: Small (default) Middle Large |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| BandwidthPack age.n.IpCount | String | No | 2 | The number of public IP addresses in NAT bandwidth package n. Valid values: 1 to 50. n indicates the sequence number of the bandwidth package. Valid values: 1 to 4. Not e You can specify this parameter only if the NAT bandwidth package was purchased before November 3, 2017. If your account does not have a NAT bandwidth package purchased before November 3, 2017, bind an Elastic IP address. |
| BandwidthPack age.n.Bandwidt h | String | No | 5 | The bandwidth of NAT bandwidth package n. Unit: Mbit/s. Valid values: 5 to 5000. Not e You can specify this parameter only if the NAT bandwidth package was purchased before November 3, 2017. If your account does not have a NAT bandwidth package purchased before November 3, 2017, bind an Elastic IP address. |
| BandwidthPack age.n.Zone | String | No | cn-hangzhou-b | The zone to which NAT bandwidth package n belongs. If you do not specify this parameter, the bandwidth package is randomly allocated to a zone. Connectivity is not affected if the IP addresses of the NAT bandwidth package and the ECS instance belong to different zones. If the IP addresses belong to the same zone, the latency can be shortened. Not e You can specify this parameter only if the NAT bandwidth package was purchased before November 3, 2017. If your account does not have a NAT bandwidth package purchased before November 3, 2017, bind an Elastic IP address. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Name | String | No | fortest | The name of the NAT gateway. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | shefffxxddjehfh123 | The description of the NAT gateway. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | abcabc | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2315DEB7-5E92-423A- 91F7-4C1EC9AD97C3 | The ID of the request. |
| NatGatewayId | String | ngw-112za33e4**** | The ID of the NAT gateway. |
| SnatTableIds | List | stb-SnatTableIds**** | The SNAT table of the NAT gateway. |
| ForwardTableIds | List | ftb-11tc6xgmv**** | The DNAT table of the NAT gateway. |
| BandwidthPackag eIds | String | bwp-11odxu2k7**** | The NAT bandwidth package of the NAT gateway. |

Sample request s

```
https://vpc.example.com/?Action=CreateNatGateway &VpcId=vpc-bp1di7uewzmtvfuq8**** &Name=MyNatGW &BandwidthPackage.1.IpCount=5 &RegionId=cn-shanghai &BandwidthPackage.1.Bandwidth=150 &BandwidthPackage.1.Zone=cn-shanghai-a
```

```xml
<?xml version="1.0" encoding="UTF-8" ?> <CreateNatGatewayResponse>
    <BandwidthPackageIds></BandwidthPackageIds>
    <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
    <SnatTableIds>
        <SnatTableId>stb-SnatTableIds****</SnatTableId>
    </SnatTableIds>
    <ForwardTableIds>
        <ForwardTableId>ftb-11tc6xgmv****</ForwardTableId>
    </ForwardTableIds>
    <NatGatewayId>ngw-112za33e4****</NatGatewayId>
</CreateNatGatewayResponse>
```

JSON f format

```json
    "BandwidthPackageIds": {
        "BandwidthPackageId": [ ]
```

`},`

```json
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF",
    "SnatTableIds": {
        "SnatTableId": [
            "stb-SnatTableIds****"
```

`]` `},`

```json
    "ForwardTableIds": {
        "ForwardTableId": [
            "ftb-11tc6xgmv****"
```

`]` `},`

```json
    "NatGatewayId": "ngw-112za33e4****"
```

#### 1.13.2 DeleteNatGateway

Deletes a specified NAT gateway.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNatGateway | The operation that you want to perform. Set the value to DeleteNatGateway. |
| RegionId | String | Yes | cn-beijing | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5770 **** | The ID of the NAT gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeleteNatGateway &RegionId=cn-beijing &NatGatewayId=ngw-bp1uewa15k4iy5770**** <? xml version="1.0" encoding="UTF-8"? > <DeleteNatGatewayResponse>
     <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteNatGatewayResponse>
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.13.3 ModifyNatGatewaySpec

Modifies the type of a NAT gateway. A NAT gateway is billed based on the type of the highest specifications that have been used on the current day. You can specify the type of a NAT gateway as needed. The type of a NAT gateway determines its SNAT performance, including the maximum number of connections and the number of new connections per second, but it does not affect the data throughput. The following table lists the mapping between NAT gateway types and SNAT performance metrics.

| Type | Maximum connections | New connections per second |
|---|---|---|
| Small | 10,000 | 1,000 |

| irtual Private Cloud |   | Developer Guide·API referenc |
|---|---|---|

| Type | Maximum connections | New connections per second |
|---|---|---|
| Middle | 50,000 | 5,000 |
| Large | 200,000 | 10,000 |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatewayS pec | The operation that you want to perform. Set the value to ModifyNatGatewaySpec. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5770 **** | The ID of the NAT gateway. |
| Spec | String | No | Small | The type of the NAT gateway. Valid values: Small (default) Middle Large |
| ClientToken | String | No | SHA234js121223xxx xx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DBD4E4A2-786E-4BD2- 8EB6-107FFC2B5B7D | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyNatGatewaySpec &NatGatewayId=ngw-bp1uewa15k4iy5770**** &Spec=Large <? xml version="1.0" encoding="UTF-8" ? > <ModifyNatGatewaySpecResponse>
    <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifyNatGatewaySpecResponse>
    "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

#### 1.13.4 ModifyNatGatewayAttribute

Modifies the configurations of a NAT gateway.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGateway Attribute | The operation that you want to perform. Set the value to ModifyNatGatewayAttribute. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| NatGatewayId | String | Yes | ngw- xxoo123zas23**** | The ID of the NAT gateway. |
| Name | String | No | nat123 | The name of the NAT gateway. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the NAT gateway. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AB5F62CF-2B60-4458- A756-42C9DFE108D1 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyNatGatewayAttribute &NatGatewayId=ngw-xxoo123zas23**** &Spec=Large <? xml version="1.0" encoding="UTF-8" ? > <ModifyNatGatewayAttributeResponse>
    <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifyNatGatewayAttributeResponse>
    "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

#### 1.13.5 DescribeNatGateways

Queries created NAT gateways.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNatGatewa ys | The operation that you want to perform. Set the value to DescribeNatGateways. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iy5770 **** | The ID of the NAT gateway. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| VpcId | String | No | vpc- bp15zckdt37pq72z* *** | The ID of the VPC. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| NatGateways | List |   | Details about NAT gateways. For more information, see the NatGateway list. |

NatGateway list

| Parameter | Type | Example | Description |
|---|---|---|---|
| NatGatewayId | String | ngw- bp1047e2d4z7kf2ki*** * | The ID of the NAT gateway. |
| RegionId | String | cn-hangzhou | The region ID of the NAT gateway. |
| Description | Integer | abcabc | The description of the NAT gateway. |
| Spec | String | Small | The type of the NAT gateway. |
| Status | String | Available | The status of the NAT gateway. Valid values: Initiating: The NAT gateway is being initialized. Available: The NAT gateway is available. Pending: The NAT gateway is being configured. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardTableIds | List | ftb- uf6gj3mhsg94qsqst*** * | DNAT tables. |
| BandwidthPackag eId | String | bwp-s6lmotmkk**** | The ID of the service plan bound to the NAT gateway. |
| SnatTableId | String | stb- uf6dalcdu0krz423p**** | The ID of the SNAT table for the NAT gateway. |
| BusinessStatus | String | Normal | The payment status of the NAT gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the NAT gateway was created. |

Sample request s

```
https://vpc.example.com/?Action=DescribeNatGateways &RegionId=cn-beijing
```

```xml
<? xml version="1.0" encoding="UTF-8"? > <DescribeNatGatewaysResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>1207C80C-7CAB-4874-A9A0-D19EC9F35490</RequestId>
    <NatGateways>
        <NatGateway>
            <Description></Description>
            <Spec>Small</Spec>
            <IpLists>
                <IpList>
                    <IpAddress>118.xx.xx.181</IpAddress>
                    <AllocationId>eip-bp1xyg5ipmh3nxxxxxxxx</AllocationId>
                    <UsingStatus>UsedBySnatTable</UsingStatus>
                </IpList>
                <IpList>
                    <IpAddress>47.xx.xx.34</IpAddress>
                    <AllocationId>eip-bp19eue77u20cfxxxxxxxx</AllocationId>
                    <UsingStatus>UsedByForwardTable</UsingStatus>
                </IpList>
            </IpLists>
            <ForwardTableIds>
                <ForwardTableId>ftb-bp15o9aylj19vxxxxxxxx</ForwardTableId>
            </ForwardTableIds>
            <VpcId>vpc-bp15k6sx6fhdz2xxxxxxxx</VpcId>
            <NatGatewayId>ngw-bp1047e2d4z7kxxxxxxxx</NatGatewayId>
            <CreationTime>2018-01-10T09:48:29Z</CreationTime>
            <BandwidthPackageIds></BandwidthPackageIds>
            <Name></Name>
            <Status>Available</Status>
            <BusinessStatus>Normal</BusinessStatus>
            <RegionId>cn-hangzhou</RegionId>
            <SnatTableIds>
                <SnatTableId>stb-bp1tyr0o48w6wxxxxxxxx</SnatTableId>
            </SnatTableIds>
            <InstanceChargeType>PostPaid</InstanceChargeType>
        </NatGateway>
    </NatGateways>
</DescribeNatGatewaysResponse>
```

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "1207C80C-7CAB-4874-A9A0-D19EC9F35490",
    "NatGateways": {
        "NatGateway": [
                "Description": "",
                "Spec": "Small",
                "IpLists": {
                    "IpList": [
                            "IpAddress": "118.xx.xx.181",
                            "AllocationId": "eip-bp1xyg5ipmh3nlxxxxxxxx",
                            "UsingStatus": "UsedBySnatTable"
```

`},`

```json
                            "IpAddress": "47.xx.xx.34",
                            "AllocationId": "eip-bp19eue77u20cxxxxxxxx",
                            "UsingStatus": "UsedByForwardTable"
```

`]` `},`

```json
                "ForwardTableIds": {
                    "ForwardTableId": [
                        "ftb-bp15o9aylj19vxxxxxxxx"
```

`]` `},`

```json
                "VpcId": "vpc-bp15k6sx6fhdzxxxxxxxx",
                "NatGatewayId": "ngw-bp1047e2d4z7xxxxxxxx",
                "CreationTime": "2018-01-10T09:48:29Z",
                "BandwidthPackageIds": {
                    "BandwidthPackageId": [ ]
```

`},`

```json
                "Name": "",
                "Status": "Available",
                "BusinessStatus": "Normal",
                "RegionId": "cn-hangzhou",
                "SnatTableIds": {
                    "SnatTableId": [
                        "stb-bp1tyr0o48w6wyxxxxxxxx"
```

`]` `},`

```json
                "InstanceChargeType": "PostPaid"
```

`]`

#### 1.13.6 CreateBandwidthPackage

Creates a NAT service plan. Descriptions A NAT service plan consists of bandwidth resources and one or more public IP addresses. You can associate up to four NAT service plans with a NAT gateway. A NAT service plan includes: Bandwidth resources A group of public IP addresses

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBandwidthP ackage | The operation that you want to perform. Set the value to Creat eBandwidt hPackage. |
| Bandwidth | Integer | Yes | 5 | The bandwidth of the NAT service plan. Valid values: 5 to 1000. Unit: Mbit/s. |
| IpCount | Integer | Yes | 2 | The number of public IP addresses in the NAT service plan. Valid values: 1 t o 50. |
| NatGatewayId | String | Yes | ngw- 7mwb327j1**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | Name | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter. It cannot start with http:// or https:// . |
| Description | String | No | Description | The description of the NAT service plan. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ISP | String | No | BGP | Only BGP is supported. |
| Zone | String | No | cn-qingdao- env17- amtest11001-a | The zone to which the NAT service plan belongs. If you do not set this parameter, the service plan is randomly allocated to a zone. Not e Connectivity is not affected when the IP addresses provided by the NAT service plan and the backend Elastic Compute Service (ECS) instances belong to different zones. However, when the IP addresses and ECS instances belong to the same zone, latency can be reduced. |
| InternetChargeTyp e | String | No | PayByBandwidth | The metering method of the NAT service plan. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h: pay-by-bandwidth |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPacka geId | String | bwp-s6lmotmkk**** | The ID of the NAT service plan. |
| RequestId | String | 54ED4074-3F89-4F11- B166-837DD3E20FE3 | The ID of the request. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateBandwidthPackage &Bandwidth=5 &IpCount=2 &NatGatewayId=ngw-7mwb327j1**** &RegionId=cn-qingdao-env17-d01
```

Sample success responses

```json
<CreateBandwidthPackageResponse>
  <RequestId>54ED4074-3F89-4F11-B166-837DD3E20FE3</RequestId>
  <BandwidthPackageId>bwp-s6lmotmkk****</BandwidthPackageId>
</CreateBandwidthPackageResponse>
    "RequestId": "54ED4074-3F89-4F11-B166-837DD3E20FE3",
    "BandwidthPackageId": "bwp-s6lmotmkk****"
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFo und | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidVpcId.NotFoun d | Specified value of VpcId is not found in our record. | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidZoneId.NotFou nd | Specified value of ZoneId is not exists. | The error message returned because the specified zone does not exist. |
| 404 | InvalidZoneId.NotFou nd | Can not find ZoneId for allocated ip. | The error message returned because the zone of the specified IP address is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Band widthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Request a quota increase on the Quota Management page. |
| 400 | QuotaExceeded.Band widthPackageCountO nNatGateway | BandwidthPackage count limit on one NatGateway exceeded. | The error message returned because the number of NAT service plans has reached the upper limit. You can associate up to four NAT service plans with a NAT gateway. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. Enter the name in the valid format. |
| 400 | InvalidParameter.Des cription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | InvalidParameter.Ban dwidthPackage.n.ISP. ValueNotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified Internet service provider (ISP) of the bandwidth resources is invalid. |
| 400 | ZONE NO AVAILABLE _ _ _ IP | The Zone have no available ip. | The error message returned because no IP address is available in the zone. |

#### 1.13.7 ModifyBandwidthPackageSpec

Modifies the bandwidth of a NAT service plan.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidthPa ckageSpec | The operation that you want to perform. Set the value to ModifyBandwidthPackageSpec. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPack ageId | String | Yes | bwp- s6lmotmkkasdc**** | The ID of the NAT service plan. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 5 | The bandwidth specified in the NAT service plan. Valid values: 5 to 1000. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifyBandwidthPackageSpec &BandwidthPackageId=bwp-s6lmotmkkasdc**** &RegionId=cn-shanghai &Bandwidth=200 &IpCount=1 <? xml version="1.0" encoding="UTF-8" ? > <ModifyBandwidthPackageSpecResponse>
      <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifyBandwidthPackageSpecResponse>
     "RequestId": "54ED4074-3F89-4F11-B166-837DD3E20FE3"
```

#### 1.13.8 DescribeBandwidthPackages

Queries NAT service plans in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBandwidthP ackages | The operation that you want to perform. Set the value to DescribeBandwidthPackages. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iydfre **** | The ID of the NAT gateway. |
| BandwidthPack ageId | String | No | bwp- bp1xea10o8qxwdfs **** | The ID of the NAT service plan. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| BandwidthPackag es | List |   | Details about NAT service plans. For more information, see the BandwidthPackage list. |

BandwidthPackage list

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPackag eId | String | bwp-xxoo123sfwr**** | The ID of the NAT service plan. |
| RegionId | String | cn-hangzhou | The region ID of the NAT service plan. |
| Description | Integer | abcabc | The description of the NAT service plan. |

| Developer Guide·API | reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | abc | The name of the NAT service plan. |
| ZoneId | String | cn-shanghai-a | The ID of the zone to which the NAT service plan belongs. |
| NatGatewayId | String | ngw-xxoo123ggtf**** | The ID of the NAT gateway. |
| Bandwidth | String | 5 | The bandwidth of the NAT service plan. Unit: Mbit/s. |
| InternetChargeTy pe | String | PayByBandwidth | The billing method of the NAT service plan. Set the value to PayByBandwidth. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the NAT service plan was created. |
| ISP | String | BGP | The carrier type of the NAT service plan. Set the value to BGP. |
| PublicIpAddresse s | List |   | The public IP address list of the NAT service plan. For more information, see the PublicIpAddresse list. |

PublicIpAddresse list

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationId | String | nateip- bp1jb1uijvm9o**** | The ID of the public IP address. |
| IpAddress | String | 118.xx.xx.33 | The public IP address. |

Sample request s

```
https://vpc.example.com/?Action=DescribeBandwidthPackages &RegionId=cn-beijing
```

```xml
<? xml version="1.0" encoding="UTF-8" ? > <DescribeBandwidthPackagesResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>1</TotalCount>
    <BandwidthPackages>
        <BandwidthPackage>
            <Description></Description>
            <IpCount>2</IpCount>
            <ISP>BGP</ISP>
            <ZoneId>cn-hangzhou-b</ZoneId>
            <InternetChargeType>PayByTraffic</InternetChargeType>
            <NatGatewayId>ngw-xxoo123ggtf****</NatGatewayId>
            <Name></Name>
            <CreationTime>2018-03-06T07:33:51Z</CreationTime>
            <Status>Available</Status>
            <BandwidthPackageId>bwp-xxoo123sfwr****</BandwidthPackageId>
            <BusinessStatus>Normal</BusinessStatus>
            <RegionId>cn-hangzhou</RegionId>
            <InstanceChargeType>PostPaid</InstanceChargeType>
            <PublicIpAddresses>
                <PublicIpAddresse>
                    <IpAddress>118.xx.xx.33</IpAddress>
                    <AllocationId>nateip-bp1jb1uijvm9o****</AllocationId>
                    <UsingStatus>Idle</UsingStatus>
                </PublicIpAddresse>
                <PublicIpAddresse>
                    <IpAddress>118.xx.xx.31</IpAddress>
                    <AllocationId>nateip-bp1dt4hpe8847****</AllocationId>
                    <UsingStatus>UsedBySnatTable</UsingStatus>
                </PublicIpAddresse>
            </PublicIpAddresses>
            <Bandwidth>5</Bandwidth>
        </BandwidthPackage>
    </BandwidthPackages>
    <PageSize>10</PageSize>
</DescribeBandwidthPackagesResponse>
```

```json
  "PageNumber": 1,
  "TotalCount": 1,
  "BandwidthPackages": {
    "BandwidthPackage": [
        "Description": "",
        "IpCount": "2",
        "ISP": "BGP",
        "ZoneId": "cn-hangzhou-b",
        "InternetChargeType": "PayByTraffic",
        "NatGatewayId": "ngw-xxoo123ggtf****",
        "Name": "",
        "CreationTime": "2018-03-06T07:33:51Z",
        "Status": "Available",
        "BandwidthPackageId": "bwp-xxoo123sfwr****",
        "BusinessStatus": "Normal",
        "RegionId": "cn-hangzhou",
        "InstanceChargeType": "PostPaid",
        "PublicIpAddresses": {
          "PublicIpAddresse": [
              "IpAddress": "118.xx.xx.33",
              "AllocationId": "nateip-bp1jb1uijvm9o****",
              "UsingStatus": "Idle"
```

`},`

```json
              "IpAddress": "118.xx.xx.33",
              "AllocationId": "nateip-bp1dt4hpe8847****",
              "UsingStatus": "UsedBySnatTable"
```

`]` `},`

```json
        "Bandwidth": "5"
```

`]` `},`

```json
  "PageSize": 10,
  "RequestId": "8909013D-4A64-41A6-93E6-E3FD08A3EAFE"
```

#### 1.13.9 ModifyBandwidthPackageAttribute

Modifies the name and description of a NAT service plan.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidthPa ckageAttribute | The operation that you want to perform. Set the value to ModifyBandwidthPackageAttribute. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPack ageId | String | Yes | bwp- s6lmotmkkzaw3**** | The ID of the NAT service plan. |
| Name | String | No | abc | The name of the NAT service plan. The name must be 2 to 128 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start _ with a letter but cannot start with http:// or https:// . |
| Description | String | No | abcabc | The description of the NAT service plan. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DFDDD35D-3F29-4E15- AA28-53F5341F9599 | The ID of the request. |

Sample request s

```xml
https://vpc.example.com?Action=ModifyBandwidthPackageAttribute &BandwidthPackageId=bwp-s6lmotmkkzaw3**** &Name=modified &RegionId=cn-shanghai <? xml version="1.0" encoding="UTF-8" ? > <ModifyBandwidthPackageAttributeResponse>
    <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifyBandwidthPackageAttributeResponse>
```

```json
    "RequestId": "54ED4074-3F89-4F11-B166-837DD3E20FE3"
```

#### 1.13.10 DeleteBandwidthPackage

Deletes a NAT service plan.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBandwidthPa ckage | The operation that you want to perform. Set the value to DeleteBandwidthPackage. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPack ageId | String | Yes | bwp- bp1arsrmca9kp1q2s **** | The ID of the NAT service plan. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7D275A59-1EB0-4775- 8A20-2A47055EAC5C | The ID of the request. |

Sample request s

```xml
https://vpc.example.com/?Action=DeleteBandwidthPackage &BandwidthPackageId=bwp-bp1arsrmca9kp1q2s**** &amp;RegionId=cn-hangzhou <? xml version="1.0" encoding="UTF-8"? > <DeleteBandwidthPackageResponse>
    <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBandwidthPackageResponse>
```

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.13.11 AddBandwidthPackageIps

Adds public IP addresses to a NAT service plan.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBandwidthPack ageIps | The operation that you want to perform. Set the value to AddBandwidthPackageIps. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPack ageId | String | Yes | bwp- s6lmotmkkaq12**** | The ID of the NAT service plan. |
| IpCount | String | No | 5 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EC0B5C51-7F40-44D6- A642-1DE764B547EC | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=AddBandwidthPackageIps &BandwidthPackageId=bwp-s6lmotmkkaq12**** &RegionId=cn-hangzhou &IpCount=6
```

```json
<? xml version="1.0" encoding="UTF-8" ? > <AddBandwidthPackageIpsResponse>
    <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</AddBandwidthPackageIpsResponse>
   "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

#### 1.13.12 RemoveBandwidthPackageIps

Removes public IP addresses from a NAT service plan. When you call this operation, take note of the following: You cannot remove all public IP addresses from a NAT service plan. You cannot remove an IP address that is not included in the specified NAT service plan. You cannot remove an IP address that is listed in the DNAT table or the SNAT table.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveBandwidthP ackageIps | The operation that you want to perform. Set the value to RemoveBandwidthPackageIps. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPack ageId | String | Yes | bwp- s6lmotmkkza1w**** | The ID of the NAT bandwidth package. |
| RemovedIpAdd resses.n | String | No | nateip- 1110a2l1ad2**** | The ID of public IP address n to be removed. n must start from 1 and cannot exceed 20. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7D275A59-1EB0-4775- 8A20-2A47055EAC5C | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=RemoveBandwidthPackageIps &RemovedIpAddresses.1=nateip-1110a2l1ad2**** &BandwidthPackageId=bwp-s6lmotmkkza1w**** &amp;RegionId=cn-hangzhou <? xml version="1.0" encoding="UTF-8" ? > <RemoveBandwidthPackageIpsResponse>
       <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</RemoveBandwidthPackageIpsResponse>
     "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

#### 1.13.13 CreateForwardEntry

Adds a DNAT entry to a DNAT table. Each DNAT entry consists of five elements: ExternalIp, ExternalPort, Protocol, InternalIp, and InternalPort. After you add a DNAT entry, the NAT gateway forwards packets of the specified protocol received from [ExternalIp: ExternalPort] to [InternalIp: InternalPort] and sends responses back over the same route. When you call this operation, take note of the following: A NAT gateway and a user-created SNAT gateway (using an ECS instance as the SNAT gateway) cannot coexist in a VPC. After you have created a NAT gateway, a route entry is automatically added to the route table of the VPC. The destination CIDR block is 0.0.0.0/0 and the next hop is the NAT gateway. The route entry ensures that traffic is routed to the NAT gateway. If the route table of the VPC already contains an entry with a destination CIDR block of 0.0.0.0/0, delete this entry. Otherwise, you cannot create a NAT gateway.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateForwardEntry | The operation that you want to perform. Set the value to CreateForwardEntry. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardTableI d | String | Yes | ftb- bp1mbjubq34hlcqp a**** | The ID of the DNAT table. |
| ExternalIp | String | Yes | 139.xx.xx.107 | The public IP address. |
| IpProtocol | String | Yes | Any | The protocol type. Valid values: TCP: The NAT gateway forwards TCP packets. UDP: The NAT gateway forwards UDP packets. Any: The NAT gateway forwards packets of any protocol. |
| ExternalPort | String | No | Any | The public port. Valid values: 1 to 65535. |
| InternalIp | String | Yes | 192.xx.xx.1 | The destination private IP address. |
| InternalPort | String | No | Any | The destination private port. Valid values: 1 to 65535. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A4AEE536-A97A-40EB- 9EBE-53A6948A6928 | The ID of the request. |
| ForwardEntryId | String | fwd- 119smw5tkza12**** | The ID of the DNAT entry. |

Sample request s

```
https://vpc.example.com/?Action=CreateForwardEntry &ExternalIp=139.xx.xx.107 &RegionId=cn-shanghai &ExternalPort=Any &InternalIp=192.xx.xx.1 &ForwardTableId=ftb-bp1mbjubq34hlcqpa**** &IpProtocol=Any &InternalPort=Any
```

```json
<? xml version="1.0" encoding="UTF-8" ? > <CreateForwardEntryResponse>
        <ForwardEntryId>fwd-119smw5tkza12****</ForwardEntryId>
        <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</CreateForwardEntryResponse>
       "ForwardEntryId": "fwd-119smw5tkza12****",
       "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

#### 1.13.14 DeleteForwardEntry

Deletes a DNAT entry from a specified DNAT table.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteForwardEntry | The operation that you want to perform. Set the value to DeleteForwardEntry. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway to which the DNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardTableI d | String | Yes | ftb- 8vbx8xu2lqj9qb334* *** | The ID of the DNAT table. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0gy **** | The ID of the DNAT entry. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeleteForwardEntry &ForwardEntryId=fwd-8vbn3bc8roygjp0gy**** &RegionId=cn-shanghai &ForwardTableId=ftb-8vbx8xu2lqj9qb334**** <? xml version="1.0" encoding="UTF-8" ? > <DeleteForwardEntryResponse>
     <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</DeleteForwardEntryResponse>
     "RequestId": "69B31D6E-9F34-4A5A-8DBC-230A3918E828"
```

#### 1.13.15 ModifyForwardEntry

Modifies a DNAT entry in a specified DNAT table. You cannot modify a DNAT entry if any DNAT entry in the DNAT table is in the Pending or Modifying state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyForwardEntry | The operation that you want to perform. Set the value to ModifyForwardEntry. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway to which the DNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardTableI d | String | Yes | ftb- 8vbx8xu2lqj9qb334* *** | The ID of the DNAT table. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0gy **** | The ID of the DNAT entry. |
| ExternalIp | String | No | 139.xx.xx.107 | The public IP address. |

| irtual Private Clou | d |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| IpProtocol | String | No | Any | The protocol type. Valid values: TCP: The NAT gateway forwards TCP packets. UDP: The NAT gateway forwards UDP packets. Any: The NAT gateway forwards packets of any protocol. |
| ExternalPort | String | No | Any | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 192.xx.xx.1 | The destination private IP address. |
| InternalPort | String | No | Any | The destination private port. Valid values: 1 to 65535. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 24CC85DC-7700-4F09- 9624-99E988C7DD03 | The ID of the request. |
| ForwardEntryId | String | fwd-119smw5zx12**** | The ID of the DNAT entry. |

Sample request s

```xml
https://vpc.example.com/?Action=CreateForwardEntry &ExternalIp=139.xx.xx.107 &RegionId=cn-shanghai &ExternalPort=Any &InternalIp=192.xx.xx.1 &ForwardTableId=ftb-8vbx8xu2lqj9qb334**** &IpProtocol=Any &InternalPort=Any <? xml version="1.0" encoding="UTF-8" ? > <CreateForwardEntryResponse>
        <ForwardEntryId>fwd-119smw5zx12****</ForwardEntryId>
        <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</CreateForwardEntryResponse>
```

```json
    "ForwardEntryId": "fwd-119smw5zx12****",
    "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

#### 1.13.16 DescribeForwardTableEntries

You can call this operation to query DNAT entries in a specified DNAT table.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeForwardTa bleEntries | The operation that you want to perform. Set the value to DescribeForwardTableEntries. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway to which the DNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardTableI d | String | No | ftb- bp1mbjubq34hlcqp a**** | The ID of the DNAT table. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A6C4A8B1-7561-4509- 949C-20DEB40D71E6 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| ForwardTableEnt ries | List |   | Details about DNAT entries. For more information, see the ForwardTableEntry list. |

ForwardTableEntry list

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardTableId | String | ftb-11tc6xgmv**** | The ID of the DNAT table to which the DNAT entry belongs. |
| ForwardEntryId | String | fwd-119smw5tk**** | The ID of the DNAT entry. |
| ExternalIp | String | 139.xxx.xx.79 | The public IP address. |
| ExternalPort | String | 80 | The public port. |
| IpProtocol | String | tcp | The protocol type. |
| InternalIp | String | 192.168.1.1 | The private IP address. |
| InternalPort | String | any | The private port. |
| Status | String | Available | The status of the DNAT entry. Valid values: Pending: The DNAT entry is being configured. Available: The DNAT entry is available. Modifying: The DNAT entry is being modified. |

Sample request s

```
https://vpc.example.com/?&Action=DescribeForwardTableEntries &RegionId=cn-shanghai &ForwardTableId=ftb-bp1mbjubq34hlcqpa****
```

```json
<?xml version="1.0" encoding="UTF-8" ?> <DescribeForwardTableEntriesResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>1</TotalCount>
    <PageSize>10</PageSize>
    <RequestId>74F2BAD8-AF35-4C57-81F1-5E33BFB0F5F2</RequestId>
    <ForwardTableEntries>
        <ForwardTableEntry>
            <Status>Available</Status>
            <IpProtocol>any</IpProtocol>
            <ForwardEntryId>fwd-bp18jpb1tlm55xxxxxxxx</ForwardEntryId>
            <ExternalIp>47.xx.xx.33</ExternalIp>
            <ForwardTableId>ftb-bp15o9aylj19vfxxxxxxxx</ForwardTableId>
            <ExternalPort>any</ExternalPort>
            <InternalPort>any</InternalPort>
            <InternalIp>192.168.xx.xx</InternalIp>
        </ForwardTableEntry>
    </ForwardTableEntries>
</DescribeForwardTableEntriesResponse>
    "PageNumber": 1,
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "74F2BAD8-AF35-4C57-81F1-5E33BFB0F5F2",
    "ForwardTableEntries": {
        "ForwardTableEntry": [
                "Status": "Available",
                "IpProtocol": "any",
                "ForwardEntryId": "fwd-bp18jpb1tlm55xxxxxxxx",
                "ExternalIp": "47.xx.xx.33",
                "ForwardTableId": "ftb-bp15o9aylj19vxxxxxxxx",
                "ExternalPort": "any",
                "InternalPort": "any",
                "InternalIp": "192.168.xx.xx"
```

`]`

#### 1.13.17 CreateSnatEntry

Adds a SNAT entry to a specified SNAT table. Each SNAT entry consists of two elements: SourceVSwitchId (VSwitch ID) and SnatIp (public IP address). After you have added a SNAT entry, the ECS instances in the VSwitch can access the Internet through the public IP address. When you call this operation, take note of the following: The VSwitch must belong to the same VPC as the NAT gateway. Each VSwitch can be specified in only one SNAT entry. A public IP address cannot be used by a DNAT entry and a SNAT entry at the same time.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSnatEntry | The operation that you want to perform. Set the value to CreateSnatEntry. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway to which the SNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- bp190wu8io1vgev** ** | The ID of the SNAT table. |
| SourceVSwitchI d | String | Yes | vsw- bp1nhx2s9ui5o**** | The ID of the VSwitch. |
| SourceCIDR | String | Yes | 10.1.1.0/24 | The CIDR block of the VSwitch, such as 10.1.1.0/24. Not e You cannot specify this parameter and SourceVSwitchId at the same time. |
| SnatIp | String | No | 139.xx.xx.40 | The public IP address. If multiple IP addresses are specified, separate them with commas (,), such as 47.XX.XX.98,47.XX.XX.99,47.XX.XX.241. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2315DEB7-5E92-423A- 91F7-4C1EC9AD97C3 | The ID of the request. |
| SnatEntryId | String | snat-kmd6nv8fy**** | The ID of the SNAT entry. |

Sample request s

```json
https://vpc.example.com/?Action=CreateSnatEntry &RegionId=cn-shanghai &SnatTableId=stb-bp190wu8io1vgev**** &SnatIp=139.xx.xx.40 &SourceVSwitchId=vsw-bp1nhx2s9ui5o**** <? xml version="1.0" encoding="UTF-8" ? > <CreateSnatEntryResponse>
     <SnatEntryId>snat-kmd6nv8fy****</SnatEntryId>
     <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
 </CreateSnatEntryResponse>
  "RequestId": "69B31D6E-9F34-4A5A-8DBC-230A3918E828",
  "SnatEntryId": "snat-kmd6nv8fy****"
```

#### 1.13.18 DeleteSnatEntry

Deletes a SNAT entry from a specified SNAT table.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSnatEntry | The operation that you want to perform. Set the value to DeleteSnatEntry. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway to which the SNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- bp190wu8io1vgev8 0**** | The ID of the SNAT table. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0plqcg **** | The ID of the SNAT entry. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 47B80B6A-759A-479C- A565-76D04BDA29F3 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=DeleteSnatEntry &SnatEntryId=snat-bp1vcgcf8tm0plqcg**** &RegionId=cn-shanghai &SnatTableId=stb-bp190wu8io1vgev80**** <? xml version="1.0" encoding="UTF-8" ? > <DeleteSnatEntryResponse>
    <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</DeleteSnatEntryResponse>
    "RequestId": "69B31D6E-9F34-4A5A-8DBC-230A3918E828"
```

#### 1.13.19 ModifySnatEntry

Modifies the value of SnatIp (public IP address) in a specified SNAT entry.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySnatEntry | The operation that you want to perform. Set the value to ModifySnatEntry. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT gateway to which the SNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table. |
| SnatEntryId | String | Yes | snat- bs5bezbmxsw2**** | The ID of the SNAT entry. |

| Developer Guide·A | PI referen | ce |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Requi red | Example | Description |
| SnatIp | String | No | 139.xx.xx.107 | The public IP address. If multiple IP addresses are specified, separate them with commas (,), such as 47.XX.XX.98,47.XX.XX.99,47.XX.XX.241. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2315DEB7-5E92-423A- 91F7-4C1EC9AD97C3 | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=ModifySnatEntry &SnatEntryId=snat-bs5bezbmxsw2**** &RegionId=cn-shanghai &SnatTableId=stb-8vbczigrhop8x5u3t**** &SnatIp=139.xx.xx.107 <? xml version="1.0" encoding="UTF-8" ? > <ModifySnatEntryResponse>
      <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</ModifySnatEntryResponse>
     "RequestId": "69B31D6E-9F34-4A5A-8DBC-230A3918E828"
```

#### 1.13.20 DescribeSnatTableEntries

Queries SNAT entries in a specified SNAT table.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSnatTableE ntries | The operation that you want to perform. Set the value to DescribeSnatTableEntries. |

| irtual Private Clou | d |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the NAT gateway to which the SNAT table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6D7E89B1-1C5B-412B- 8585-4908E222EED5 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| SnatTableEntries | List |   | Details about SNAT entries. For more information, see the SnatTableEntries list. |

SnatTableEntries list

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatTableId | String | stb-gz3r3odaw**** | The ID of the SNAT table to which the SNAT entry belongs. |
| SnatEntryId | String | snat-kmd6nv8fy**** | The ID of the SNAT entry. |
| SourceVSwitchId | String | vsw-3xazxs12ws**** | The ID of the VSwitch that accesses the Internet by using the SNAT function. |
| SourceCIDR | String | 192.168.1.0/24 | The source CIDR block of the SNAT entry. |

| Developer Guide·API | reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatIp | String | 116.xx.xx.28 | The public IP address of the SNAT entry. |
| Status | String | Available | The status of the SNAT entry. Valid values: Pending: The SNAT entry is being configured. Available: The SNAT entry is available. Modifying: The SNAT entry is being modified. |

Sample request s

```xml
https://vpc.example.com/?Action=DescribeSnatTableEntries &RegionId=cn-shanghai &SnatTableId=stb-8vbczigrhop8x5u3t**** <? xml version="1.0" encoding="UTF-8" ? > <DescribeSnatTableEntriesResponse>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <RequestId>6D7E89B1-1C5B-412B-8585-4908E222EED5</RequestId>
    <SnatTableEntries>
        <SnatTableEntry>
            <SnatEntryId>snat-kmd6nv8xxxxxxxx</SnatEntryId>
            <SnatIp>139.xx.xx.40</SnatIp>
            <SnatTableId>stb-gz3r3odxxxxxxxx</SnatTableId>
            <SourceCIDR>192.168.1.0/24</SourceCIDR>
            <SourceVSwitchId>vsw-yrv0xxxxx</SourceVSwitchId>
            <Status>Available</Status>
        </SnatTableEntry>
        <SnatTableEntry>
            <SnatEntryId>snat-bs5bezbxxxxxxxx</SnatEntryId>
            <SnatIp>139.xxx.xx.40</SnatIp>
            <SnatTableId>stb-gz3r3oxxxxxxxx</SnatTableId>
            <SourceCIDR>192.168.3.0/24</SourceCIDR>
            <SourceVSwitchId>vsw-3xbxxxxx</SourceVSwitchId>
            <Status>Available</Status>
        </SnatTableEntry>
    </SnatTableEntries>
    <TotalCount>2</TotalCount>
</DescribeSnatTableEntriesResponse>
```

```json
  "PageNumber": 1,
  "PageSize": 10,
  "RequestId": "6D7E89B1-1C5B-412B-8585-4908E222EED5",
  "SnatTableEntries": {
    "SnatTableEntry": [
        "SnatEntryId": "snat-kmd6nvxxxxxxxx",
        "SnatIp": "139.xx.xx.40",
        "SnatTableId": "stb-gz3r3odxxxxxxxx",
        "SourceCIDR": "192.168.1.0/24",
        "SourceVSwitchId": "vsw-yrv0xxxxx",
        "Status": "Available"
```

`},`

```json
        "SnatEntryId": "snat-bs5bezbxxxxxxxx",
        "SnatIp": "139.xx.xx.40",
        "SnatTableId": "stb-gz3r3odxxxxxxxx",
        "SourceCIDR": "192.168.3.0/24",
        "SourceVSwitchId": "vsw-3xbxxxxx",
        "Status": "Available"
```

`]` `},`

```json
  "TotalCount": 2
```

### 1.14 VPN Gateway

#### 1.14.1 CreateVpnGateway

You can call this operation to create a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnGatewa y | The operation that you want to perform. Set the value to Creat eVpnGat eway. |
| Bandwidth | Integer | Yes | 5 | The network bandwidth of the VPN gateway. Unit: Mbit/s. Valid values: 5, 10, 20, 50, and 100. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1ub1yt9cvakoel j**** | The ID of the VPC to which the VPN gateway belongs. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| EnableIpsec | Boolean | No | true | Specifies whether to enable the IPsec- VPN feature. Valid values: t rue (default): Enable the IPsec-VPN feature. f alse: Disable the IPsec-VPN feature. |
| EnableSsl | Boolean | No | true | Specifies whether to enable the SSL-VPN feature. Valid values: t rue: Enable the SSL-VPN feature. f alse (default): Disable the SSL-VPN feature. |
| Name | String | No | MYVPN | The name of the VPN gateway. The default value is the ID of the VPN gateway. The name can be 2 to 128 characters in length. It can contain letters, digits, underscores ( ), and hyphens (-). The _ name must start with a letter or Chinese character and cannot start with http:// or https:// . |
| SslConnections | Integer | No | 2 | The maximum number of clients that can be connected simultaneously. Valid values: 5, 10, and 20, |
| VSwitchId | String | No | vsw- bp1j5miw2bae9s2 vt**** | The ID of the VSwitch to which the VPN gateway belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | myVpn | The name of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |

Sample requests

```json
http(s)://vpc.example.com/? Action=CreateVpnGateway &Bandwidth=5 &RegionId=cn-hangzhou &VpcId=vpc-bp1ub1yt9cvakoelj**** <CreateVpnGatewayResponse>
      <Name>myVpn</Name>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
</CreateVpnGatewayResponse>
 "CreateVpnGatewayResponse":{
  "Name":"myVpn",
  "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****",
  "RequestId":"54B48E3D-DF70-471B-AA93-08E683A1B457"
```

#### 1.14.2 DescribeVpnGateways

You can call this operation to query one or more VPN gateways.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGate ways | The operation that you want to perform. Set this value to DescribeVpnGat eways. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Status | String | No | init | The status of the VPN gateway. Valid values: init provisioning act ive updat ing delet ing |
| VpcId | String | No | vpc- bp1ub1yt9cvakoel j**** | The ID of the VPC to which the VPN gateway belongs. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGateways |   |   | Details of the VPN gateways. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj*** * | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv** ** | The ID of the VSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.62.69.xxx | The public IP address of the VPN gateway. |
| CreateTime | Long | 1515383700000 | The time when the VPN gateway was created. |
| EndTime | Long | 1518105600000 | The time when the VPN gateway expires. |
| Spec | String | 5M | The maximum bandwidth supported by the VPN gateway. |
| Name | String | test | The name of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| BusinessStatus | String | Normal | The status of the VPN gateway. |
| IpsecVpn | String | enable | Indicates whether the IPsec-VPN feature is enabled. |
| SslMaxConnectio ns | Long | 5 | The maximum number of concurrent SSL-VPN connections. |
| SslVpn | String | enable | Indicates whether the SSL-VPN feature is enabled. |
| Tag | String | 1 | The tag. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries on the current page. |
| RequestId | String | DF11D6F6-E35A- 41C3-9B20- 6FC8A901FE65 | The ID of the request. |

Sample requests

```
https://vpc.example.com/?Action=DescribeVpnGateways &RegionId=cn-hangzhou
```

```json
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
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "VpnGateways":{
  "VpnGateway":[
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

`]` `},`

```json
 "RequestId":"B2CD1315-CA2B-47B1-9DA5-8F1D69C48E82"
```

#### 1.14.3 DescribeVpnGateway

Queries detailed information of a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGate way | The operation that you want to perform. Set the value to DescribeVpnGat eway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj*** * | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv** ** | The ID of the VSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.62.222.XX | The public IP address of the VPN gateway. |
| CreateTime | Long | 1495382400000 | The time when the VPN gateway was created. |
| EndTime | Long | 1495382400000 | The time when the VPN gateway expires. |
| Spec | String | 5 | The specification of the VPN gateway. |
| Name | String | vpngatewayname | The name of the VPN gateway. |
| Description | String | vpngatewaydescripti on | The description of the VPN gateway. |
| Status | String | init | The status of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpsecVpn | String | enable | Indicates whether IPsec-VPN is enabled for the VPN gateway. |
| RequestId | String | DE77A7F3-3B74- 41C0-A5BC- CAFD188C28B6 | The ID of the request. |
| SslMaxConnectio ns | Long | 5 | The maximum number of concurrent SSL-VPN connections. |
| SslVpn | String | enable | Indicates whether SSL-VPN is enabled for the VPN gateway. |
| Tag | String | tag1 | The tag associated with the VPN gateway. |

Sample requests

```
https://vpc.example.comm/?Action=DescribeVpnGateway &RegionId=cn-shanghai &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj****
```

Sample success responses

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

#### 1.14.4 DeleteVpnGateway

You can call this operation to delete a VPN gateway. Not e You cannot delete a VPN gateway associated with an IPsec connection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnGatewa y | The operation that you want to perform. Set the value to Delet eVpnGat eway. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | >0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=DeleteVpnGateway &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** <DeleteNatGatewayResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteNatGatewayResponse>
 "RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

#### 1.14.5 CreateCustomerGateway

You can call this operation to create a customer gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateCustomerGa teway | The operation that you want to perform. Set the value to Creat eCust omerGat eway. |
| IpAddress | String | Yes | 116.62.222.xxx | The IP address of the customer gateway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | Gateway | The description of the customer gateway. The description must be 2 to 256 characters in length. It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | Gateway | The name of the customer gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGatew ayId | String | cgw- bp1aw0a5nfff03xp1* *** | The ID of the customer gateway. |
| IpAddress | String | 100.1.1.XX | The IP address of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| CreateTime | Long | 1493363486000 | The time when the customer gateway was created. |
| RequestId | String | cgw- bp1aw0a5nfff03xp1* *** | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=CreateCustomerGateway &IpAddress=116.62.222.xxx &RegionId=cn-shanghai <CreateCustomerGatewayResponse>
      <CustomerGatewayId>cgw-bp1aw0a5nfff03xp****</CustomerGatewayId>
      <RequestId>185E81B1-3916-4667-B48F-C52409B33F2B</RequestId>
      <CreateTime>1493363486000</CreateTime>
      <IpAddress>100.1.1.XX</IpAddress>
</CreateCustomerGatewayResponse>
 "CustomerGatewayId":"cgw-bp1jrawp82av6bws9****",
 "RequestId":"D32B3C26-6C6C-4988-93E9-D2A6444CE6AE",
 "CreateTime":1493363599000,
 "IpAddress":"100.1.1.XX"
```

#### 1.14.6 DescribeCustomerGateways

You can call this operation to query one or more customer gateways.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustomer Gateways | The operation that you want to perform. Set the value to DescribeCust omerGat eways. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| CustomerGatewayI d | String | No | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the customer gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |

| V | irtual Private Cloud |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGatew ays |   |   | The description of the customer gateway. |
| CustomerGatew ayId | String | cgw- bp1pvpl9r9adju6l5*** * | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.196.32.xxx | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The time when the customer gateway was created. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```
https://vpc.example.com/?Action=DescribeCustomerGateways &RegionId=cn-shanghai
```

```json
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
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29",
 "CustomerGateways":{
  "CustomerGateway":[
    "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
    "Name":"test",
    "CreateTime":1492747187000,
    "IpAddress":"139.196.32.xxx"
```

`]`

#### 1.14.7 DescribeCustomerGateway

You can call this operation to query the details of a specified customer gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustomer Gateway | The operation that you want to perform. Set the value to DescribeCust omerGat eway. |
| CustomerGatewayI d | String | Yes | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGatew ayId | String | cgw- bp1pvpl9r9adju6l5*** * | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.196.32.xxx | The IP address of the customer gateway. |
| RequestId | String | 99506ECB-218F- 45A5-AE8E- 79518451F615 | The ID of the request. |
| CreateTime | Long | 1492747187000 | The time when the customer gateway was created. |

Sample requests

```xml
https://vpc.example.com/?Action=DescribeCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-shanghai <DescribeCustomerGatewayResponse>
      <Name>test</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <CreateTime>1492747187000</CreateTime>
      <RequestId>99506ECB-218F-45A5-AE8E-79518451F615</RequestId>
      <IpAddress>139.196.32.xxx</IpAddress>
</DescribeCustomerGatewayResponse>
```

```json
 "Name":"test",
 "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
 "CreateTime":1492747187000,
 "RequestId":"A0457BC9-6C0F-4437-AB9D-FB2EABC1D6A2",
 "IpAddress":"139.196.32.xxx"
```

#### 1.14.8 DeleteCustomerGateway

You can call this operation to delete a customer gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCustomerGa teway | The operation that you want to perform. Set the value to Delet eCust omerGat eway. |
| CustomerGatewayI d | String | Yes | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=DeleteCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-shanghai <DeleteCustomerGatewayResesponse>
  <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteCustomerGatewayResesponse>
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

#### 1.14.9 ModifyCustomerGatewayAttribute

You can call this operation to modify the name and description of a customer gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyCustomerG atewayAttribute | The operation that you want to perform. Set the value to Modif yCust omerGat ewayAt t ribut e. |
| CustomerGatewayI d | String | Yes | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-shanghai | The region ID of the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | test | The description of the customer gateway. The description must be 2 to 256 characters in length. It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | test | The name of the customer gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGatew ayId | String | cgw- bp1pvpl9r9adju6l5*** * | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.196.32.xxx | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The time when the customer gateway was created. |
| RequestId | String | E61293C8-AF07-4E87- A272-542680038F93 | The ID of the request. |

Sample requests

```
https://vpc.example.com/?Action=ModifyCustomerGatewayAttribute &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-shanghai &Name=test
```

```json
<ModifyCustomerGatewayAttributeResponse>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RequestId>E61293C8-AF07-4E87-A272-542680038F93</RequestId>
      <CreateTime>1492747187000</CreateTime>
      <IpAddress>139.196.32.xxx</IpAddress>
</ModifyCustomerGatewayAttributeResponse>
 "CustomerGatewayId":"cgw-bp1pvpl9r9adju6l5****",
 "CreateTime":1492747187000,
 "RequestId":"8AA5CE21-2E6A-4530-BDF5-F055849476E6",
 "IpAddress":"139.196.32.xxx"
```

#### 1.14.10 DescribeVpnConnection

You can call this operation to query the details of an IPsec-VPN connection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConne ction | The operation that you want to perform. Set the value to DescribeVpnConnect ion. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nc k**** | The ID of the IPsec-VPN connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp1bbi27hojx80nck** ** | The ID of the IPsec-VPN connection. |
| CustomerGatew ayId | String | cgw- bp1mvj4g9kogwwcxk **** | The ID of the customer gateway. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |
| Name | String | ipsec1 | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the on-premises data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |
| Status | String | ike sa not establish _ _ _ ed | The status of the connection. Valid values: ike sa not est ablished indicates that _ _ _ phase one negotiations failed. ike sa est ablished indicates that phase _ _ one negotiations were successful. ipsec sa not est ablished indicates that _ _ _ phase two negotiations failed. ipsec sa est ablished indicates that phase _ _ two negotiations were successful. |
| EffectImmediate ly | Boolean | true | Indicates whether the IPsec-VPN connection takes effect immediately. Valid values: t rue: Reconnection is triggered when the configuration is changed. f alse: Reconnection is triggered when network traffic is detected. Reconnection may cause intermittent disconnection. |
| IkeConfig |   |   | The configurations for phase one negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IkeMode | String | main | The IKE mode. Both main and aggressive modes are supported. The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.62.69.xxx | The ID of the server end. By default, it is the IP address of the VPN gateway. Both FQDN and IP formats are supported. |
| Psk | String | pgw6dy7d1i8in7x5 | The pre-shared key. |
| RemoteId | String | 139.196.32.xxx | The peer ID. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The configurations for phase two negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | F2310D45-BCF6-4E2E- 9082-B4503844BA4C | The ID of the request. |
| VcoHealthCheck |   |   | The health check information. |
| Dip | String | 10.0.0.xx | The destination IP address specified for health checks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Enable | String | true | Indicates whether health checks are enabled. Valid values: f alse: Indicates that health checks are disabled. t rue: Indicates that health checks are enabled. |
| Interval | Integer | 3 | The time interval of health check retries. Unit: Second. |
| Retry | Integer | 3 | The maximum number of attempts for resending health check probes. |
| Sip | String | 192.168.1.xx | The source IP address specified for health checks. |
| Status | String | failed | The status of the health check. Valid values: |

Sample requests

```
https://vpc.example.com/?Action=DescribeVpnConnection &RegionId=cn-hangzhou &VpnConnectionId=vco-bp1bbi27hojx80nck****
```

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

```json
 "PageNumber":1,
 "VpnConnections":{
  "VpnConnection":[
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

`]` `},`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"7D598A10-26EF-44F2-9F47-E417842F3CEA"
```

#### 1.14.11 DeleteVpnConnection

You can call this operation to delete an IPsec-VPN connection. After the IPsec-VPN connection is deleted, the connection between the VPC and the on-premises data center is closed.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnConnect ion | The operation that you want to perform. Set the value to Delet eVpnConnect ion. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nc k**** | The ID of the IPsec-VPN connection. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Sample requests

```xml
https://vpc.example.com/?Action=DeleteVpnConnection &RegionId=cn-hangzhou &VpnConnectionId=vco-bp1bbi27hojx80nck**** <DeleteVpnConnectionResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteVpnConnectionResponse>
```

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

#### 1.14.12 DownloadVpnConnectionConfig

You can call this operation to obtain the configuration information of an IPsec-VPN connection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DownloadVpnCon nectionConfig | The operation that you want to perform. Set the value to DownloadVpnConnect ionConf ig. |
| RegionId | String | Yes | cn-shanghai | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nc k**** | The name of the IPsec-VPN connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0C68048B-0F70- 40DA-B8AE- 1B79B5CF62E3 | The ID of the request. |
| VpnConnectionC onfig |   |   | The configuration of the IPsec-VPN connection. |
| IkeConfig |   |   | The IKE configurations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IkeMode | String | main | The IKE mode. Both main and aggressive modes are supported. The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.62.69.xx | The ID of the server end. By default, it is the IP address of the VPN gateway. Both FQDN and IP formats are supported. |
| Psk | String | pgw6dy7d1i8i**** | The pre-shared key. |
| RemoteId | String | 139.196.32.xx | The peer ID. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The IPsec configurations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| Local | String | 139.196.32.xx | The ID of the IPsec VPN gateway. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the VPC. |
| Remote | String | 116.62.69.xx | The ID of the customer gateway. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the on-premises data center. |

Sample requests

```xml
https://vpc.example.com/?Action=DownloadVpnConnectionConfig &RegionId=cn-shanghai &VpnConnectionId=vco-bp1bbi27hojx80nck**** <DownloadVpnConnectionConfigResponse>
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

#### 1.14.13 CreateSslVpnServer

You can call this operation to create an SSL server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnServe r | The operation that you want to perform. Set the value to Creat eSslVpnServer. |
| ClientIpPool | String | Yes | 192.168.1.0/24 | The CIDR block from which IP addresses are allocated to the virtual network interface of the client. It is not the CIDR block of the client. When the client accesses the server end through an SSL-VPN connection, the VPN gateway selects an IP address from the specified CIDR block and assigns it to the client. This CIDR block must not conflict with LocalSubnet . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LocalSubnet | String | Yes | 10.0.0.0/8 | The CIDR block to be accessed by the client through the SSL-VPN connection. You can set the value to the CIDR block of a VPC network, a VSwitch, an on- premises data center connected to the VPC through a leased line, or an Alibaba Cloud service, such as an ApsaraDB for RDS instance or OSS instance. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1hgim8by0kc9n ga**** | The ID of the VPN gateway. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm used by the SSL server. Valid values: AES-128-CBC (def ault ), AES-192- CBC, AES-256-CBC, and none |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to guarantee the idempotency of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | sslvpnname | The name of the SSL server. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Port | Integer | No | 1194 | The port used by the SSL server. Default value: 1194. The following ports are not supported: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500 |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Proto | String | No | UDP | The protocol used by the SSL server. Valid values: UDP (def ault ) and T CP |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the SSL server. |
| RequestId | String | E98A9651-7098- 40C7-8F85- C818D1EBBA85 | The ID of the request. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v*** * | The ID of the SSL server. |

Sample requests

```json
http(s)://vpc.example.com/? Action=CreateSslVpnServer &ClientIpPool=192.168.1.0/24 &LocalSubnet=10.0.0.0/8 &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1hgim8by0kc9nga**** <CreateSslVpnServerResponse>
  <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId>
  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
  <Name>test</Name>
</CreateSslVpnServerResponse>
 "Name":"test",
 "RequestId":"E98A9651-7098-40C7-8F85-C818D1EBBA85",
 "SslVpnServerId":"vss-bp18q7hzj6largv4v****"
```

#### 1.14.14 DescribeSslVpnServers

You can call this operation to query one or more SSL servers.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnSer vers | The operation that you want to perform. Set the value to DescribeSslVpnServers. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | test | The name of the SSL server. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| SslVpnServerId | String | No | vss- bp15j3du13gq1dg ey**** | The ID of the SSL server. |
| VpnGatewayId | String | No | vpn- bp1on0xae9d771g gi**** | The ID of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 085CA5EA-1E76- 43A8-981B- E0208DECA0CB | The ID of the request. |
| SslVpnServers |   |   | Details of the SSL server. |
| Cipher | String | AES-128-CBC | The encryption algorithm used. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ClientIpPool | String | 10.10.1.0/24 | The IP address pool of the client. |
| Compress | Boolean | false | Indicates whether the communication is compressed. |
| Connections | Integer | 0 | The total number of active connections. |
| CreateTime | Long | 1544668844000 | The time when the SSL server was created. |
| InternetIp | String | 47.96.167.xxx | The public IP address. |
| LocalSubnet | String | 192.168.0.0/24 | The CIDR block of the local client. |
| MaxConnections | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL server. |
| Port | Integer | 1194 | The port used by the SSL server. |
| Proto | String | UDP | The protocol used by the SSL server. |
| RegionId | String | cn-hangzhou | The region ID of the SSL server. |
| SslVpnServerId | String | vss- bp15j3du13gq1dgey* *** | The ID of the SSL server. |
| VpnGatewayId | String | vpn- bp1on0xae9d771ggi* *** | The ID of the VPN gateway. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Sample requests

```
https://vpc.example.com/?Action=DescribeSslVpnServers &RegionId=cn-hangzhou
```

```json
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

`},`

```json
 "PageSize":"10",
 "RequestId":"DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

#### 1.14.15 DeleteSslVpnServer

You can call this operation to delete an SSL server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnServe r | The operation that you want to perform. Set the value to Delet eSslVpnServer. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv4 v**** | The ID of the SSL server. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Sample requests

```
https://vpc.example.com/?Action=DeleteSslVpnServer &RegionId=cn-hangzhou &SslVpnServerId=vss-bp18q7hzj6largv4v****
```

```json
<DeleteSslVpnServerResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnServerResponse>
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

#### 1.14.16 ModifySslVpnServer

You can call this operation to modify the configuration of an SSL server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnServ er | The operation that you want to perform. Set the value to Modif ySslVpnServer. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway associated with the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv4 v**** | The ID of the SSL server. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm used by the SSL server. Valid values: AES-128-CBC (def ault ), AES-192-CBC, AES-256- CBC, and none |
| ClientIpPool | String | No | 10.30.30.0/2 | The IP address pool of the client. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Compress | Boolean | No | false | Specifies whether to compress the communication. Valid values: t rue (def ault ) and f alse |
| LocalSubnet | String | No | 10.20.20.0/24 | The CIDR block of the local client. |
| Name | String | No | test | The name of the SSL server. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter but cannot start with http:// or https:// . |
| Port | Integer | No | 1194 | The port used by the SSL server. Default value: 1194. The following ports cannot be used: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500 |
| Proto | String | No | UDP | The protocol used by the SSL server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cipher | String | AES-128-CBC | Indicates the encryption algorithm used. |
| ClientIpPool | String | 10.30.30.0/24 | The IP address pool of the client. |
| Compress | Boolean | false | Indicates whether the communication is compressed. |
| Connections | Integer | 0 | The total number of current connections. |
| CreateTime | Long | 1492753580000 | The time when the SSL server was created. |
| InternetIp | String | 47.98.xx.xx | The public IP address of the VPN gateway. |
| LocalSubnet | String | 10.20.20.0/24 | The CIDR block of the local client. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MaxConnections | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL server. |
| Port | Integer | 1194 | The port of the SSL server. |
| Proto | String | UDP | The protocol used by the SSL server. |
| RegionId | String | cn-hangzhou | The region ID of the SSL server. |
| RequestId | String | DF11D6F6-E35A- 41C3-9B20- 6FC8A901FE65 | The ID of the request. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v*** * | The ID of the SSL server. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |

Sample requests

```
https://vpc.example.com/?Action=ModifySslVpnServer &RegionId=cn-hangzhou &SslVpnServerId=vss-bp18q7hzj6largv4****
```

```json
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

`},`

```json
 "PageSize":"10",
 "RequestId":"DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

#### 1.14.17 DeleteSslVpnClientCert

You can call this operation to delete an SSL client certificate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnClien tCert | The operation that you want to perform. Set the value to Delet eSslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificate. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertId | String | Yes | vsc- bp1n8wcf134yl0o sr**** | The ID of the SSL client certificate. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |

Sample requests

```xml
https://vpc.example.com/?Action=DeleteSslVpnClientCert &RegionId=cn-hangzhou &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr**** <DeleteSslVpnClientCertResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnClientCertResponse>
```

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

#### 1.14.18 ModifySslVpnClientCert

You can call this operation to modify the name of an SSL client certificate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnClien tCert | The operation that you want to perform. Set the value to Modif ySslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificate. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertId | String | Yes | vsc- bp1n8wcf134yl0o src**** | The ID of the SSL client certificate. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | cert2 | The name of the SSL client certificate. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | cert2 | The name of the client certificate. |
| RequestId | String | 606998F0-B94D-48FE- 8316-ACA81BB230DA | The ID of the request. |
| SslVpnClientCert Id | String | vsc- bp1n8wcf134yl0osr** ** | The ID of the SSL client certificate. |

Sample requests

```json
https://vpc.example.com/?Action=ModifySslVpnClientCert &RegionId=cn-hangzhou &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr**** &Name=cert2 <ModifySslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <Name>cert2</Name>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</ModifySslVpnClientCertResponse>
 "Name":"cert2",
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA",
 "SslVpnClientCertId":"vsc-bp1n8wcf134yl0osr****"
```

#### 1.14.19 ModifyVpnGatewayAttribute

You can call this operation to modify the name and description of a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnGatewa yAttribute | The operation that you want to perform. Set the value to Modif yVpnGat ewayAt t ribut e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm2 ogj**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | VPN Gateway | The description of the VPN gateway. The description must be 2 to 256 characters in length. It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | myvpn | The name of the VPN gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoel*** * | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv** ** | The ID of the VSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.62.69.xxx | The public IP address of the VPN gateway. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492753580000 | The time when the VPN gateway was created. |
| EndTime | Long | 1495382400000 | The time when the VPN gateway expires. |
| Spec | String | 5M | The specification of the VPN gateway. |
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| IntranetIp | String | 172.16.104.xxx | The private IP address of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |

Sample requests

```xml
https://vpc.example.com/?Action=ModifyVpnGatewayAttribute &RegionId=cn-shanghai &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** <ModifyVpnGatewayAttributeResponse>
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

#### 1.14.20 CreateVpnConnection

You can call this operation to create an IPsec-VPN connection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnConnect ion | The operation that you want to perform. Set the value to Creat eVpnConnect ion. |
| CustomerGatewayI d | String | Yes | vpn- bp1q8bgx4xnk**** | The ID of the customer gateway. |
| LocalSubnet | String | Yes | 1.1.1.0/24,1.1.2.0/ 24 | The CIDR block of the VPC to be connected with the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| RegionId | String | Yes | cn-shanghai | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| RemoteSubnet | String | Yes | 1.1.1.0/24,1.1.2.0/ 24 | The CIDR block of the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm** ** | The ID of the VPN gateway. |
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically configure routes. Valid values: t rue (default): Routes are automatically configured. f alse: Routes are not automatically configured. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| EffectImmediately | Boolean | No | false | Specifies whether to delete a successfully negotiated IPsec-VPN tunnel and initiate a negotiation again. Valid values: t rue: Negotiate immediately after the configuration is completed. f alse (default): Negotiate when inbound traffic is detected. |
| HealthCheckConfig | String | No | ['enable':'true','di p':'192.168.1.2','si p':'192.168.2.2','in terval':'3','retry':' 3'] | The health check configurations: Healt hCheckConf ig.enable: Specifies whether to enable health checks. Valid values: t rue \| f alse (default) Healt hCheckConf ig.dip: The destination IP address configured for health checks. Healt hCheckConf ig.sip: The source IP address configured for health checks. Healt hCheckConf ig.int erval: The interval between health check retries. Unit: seconds. Healt hCheckConf ig.ret ry: The maximum number of health check retries. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | ['IkeVersion':'ikev1 ','IkeMode':'main'] | The configurations of phase one negotiations. IkeConf ig.Psk: The pre-shared key used for authentication between the IPsec-VPN gateway and the customer gateway. The value is generated randomly by default. It can contain up to 100 characters. You can also specify a pre-shared key. IkeConf ig.IkeVersion: The version of the IKE protocol. Valid values: ikev1 \| ikev2. Default value: ikev1. IkeConf ig.IkeMode: The negotiation mode of IKE V1. Valid values: main \| aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm of phase one negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm of phase one negotiations. Valid values: md5 \| sha1. Default value: md5. IkeConf ig.IkePf s: The Diffie-Hellman key exchange algorithm used by phase one negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IkeConf ig.IkeLif et ime: The SA lifetime resulting from phase one negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: The identification of the VPN gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the VPN gateway. IkeConf ig.Remot eId: The identification of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | ['IpsecAuthAlg':'m d5','IpsecEncAlg':' aes'] | The configurations of phase two negotiations. IpsecConf ig.IpsecEncAlg: The encryption algorithm of phase two negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm of phase two negotiations. Valid values: md5 \| sha1. Default value: md5. IpsecConf ig. IpsecPf s: The Diffie- Hellman group for perfect forward secrecy (PFS). The Diffie-Hellman key exchange algorithm used by phase two negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IpsecConf ig. IpsecLif et ime: The SA lifetime value resulting from phase two negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp15oes1py4i6**** | The ID of the IPsec-VPN connection. |
| CreateTime | Long | 1544666102000 | The time when the IPsec-VPN connection was created. |
| Name | String | test | The name of the IPsec-VPN connection. |
| RequestId | String | 082AD562-B8DB- 4BB2-861F- DA1FCA01FD76 | The ID of the request. |

Sample requests

```json
http(s)://vpc.example.com/? Action=CreateVpnConnection &CustomerGatewayId=vpn-bp1q8bgx4xnk**** &LocalSubnet=1.1.1.0/24,1.1.2.0/24 &RegionId=cn-shanghai &RemoteSubnet=1.1.1.0/24,1.1.2.0/24 &VpnGatewayId=vpn-bp1q8bgx4xnkm**** <CreateVpnConnectionResponse>
      <VpnConnectionId>vco-bp1bbi27hojx8****</VpnConnectionId>
      <CreateTime>1493363928000</CreateTime>
</CreateVpnConnectionResponse>
 "VpnConnectionId":"vco-bp15oes1py4i6****",
 "CreateTime":1544666102000
```

#### 1.14.21 DescribeVpnConnections

Queries one or more IPsec-VPN connections.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConne ctions | The operation that you want to perform. Set the value to DescribeVpnConnect ions. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| CustomerGatewayI d | String | No | cgw- bp1mvj4g9kogw** ** | The ID of the customer gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10 |
| VpnConnectionId | String | No | vco- bp15oes1py4i6*** * | The ID of the IPsec-VPN connection. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkx*** * | The ID of the VPN gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnections |   |   | The details of the IPsec-VPN connections. |
| IkeConfig |   |   | The configurations of phase-one negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Both SHA-1 and MD5 are supported. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. Both the main mode and aggressive mode are supported. The main mode features high security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The Diffie-Hellman (DH) group. Valid values: group1 \| group2 \| group5 \| group14 \| group24 |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.xx.xx.64 | The local ID of the VPN gateway. The default value is the IP address of the VPN gateway. Both fully qualified domain name (FQDN) and IP address formats are supported. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Psk | String | pgw6dy7dxxxxxxxx | The pre-shared key. |
| RemoteId | String | 139.xx.xx.167 | The ID of the peer. By default, it is the IP address of the customer gateway. Both FQDN and IP formats are supported. |
| IpsecConfig |   |   | The configurations of phase two negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Both SHA-1 and MD5 are supported. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| VpnConnectionI d | String | vco- bp10lz7aejumd**** | The ID of the IPsec-VPN connection. |
| CustomerGatew ayId | String | vpn- bp1q8bgx4xnk**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm**** | The ID of the VPN gateway. |
| Name | String | name | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the on-premises data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | ipsec sa established _ _ | The status of the connection. Valid values: ike sa not est ablished: Phase one _ _ _ negotiations failed. ike sa est ablished: Phase one _ _ negotiations were successful. ipsec sa not est ablished: Phase two _ _ _ negotiations failed. ipsec sa est ablished: Phase two _ _ negotiations were successful. |
| EffectImmediate ly | Boolean | true | Indicates whether the connection takes effect immediately. t rue: A reconnection is triggered when the configuration is changed. f alse: A reconnection is triggered when network traffic is detected. Reconnections may cause transient disconnections. |
| VcoHealthCheck |   |   | Details of health checks. |
| Dip | String | 8.xx.xx.8 | The destination IP address configured for health checks. |
| Interval | Integer | 2 | The interval between two consecutive health checks. Unit: seconds. |
| Sip | String | 192.xx.xx.66 | The source IP address configured for health checks. |
| TotalCount | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The number of the page returned. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 54A4B3D0-DF4D- 4C54-B8DC- 5DC8DD49C939 | The ID of the request. |

Sample requests

```
https://vpc.example.com/?Action=DescribeVpnConnections &RegionId=cn-hangzhou
```

Sample success responses

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

```json
 "PageNumber":1,
 "VpnConnections":{
  "VpnConnection":[
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

`]` `},`

```json
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939"
```

#### 1.14.22 ModifyVpnConnectionAttribute

You can call this operation to modify the configuration of an IPsec-VPN connection.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnConnec tionAttribute | The operation that you want to perform. Set the value to Modif yVpnConnect ionAt t ribut e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80nc k**** | The ID of the IPsec-VPN connection. |
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically publish routes. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| EffectImmediately | Boolean | No | false | Specifies whether to delete a successfully negotiated IPsec-VPN tunnel and initiate a negotiation again. Valid values: t rue: Negotiate immediately after the configuration is completed. f alse (default): Negotiate when inbound traffic is detected. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | ikev1, ikev2 | The configurations of phase one negotiations. IkeConf ig.Psk: The pre-shared key used for authentication between the IPsec-VPN gateway and the customer gateway. By default, the parameter value is generated randomly. You can also specify a pre-shared key. It can contain up to 100 characters. IkeConf ig.IkeVersion: The version of the IKE protocol. Valid values: ikev1 \| ikev2. Default value: ikev1. IkeConf ig.IkeMode: The negotiation mode of IKE V1. Valid values: main \| aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm of phase one negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm of phase one negotiations. Valid values: md5 \| sha1. Default value: sha. IkeConfig.IkePfs: The Diffie-Hellman key exchange algorithm used by phase one negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IkeConf ig.IkeLif et ime: The SA lifetime resulting from phase one negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: The identification of the VPN gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the VPN gateway. IkeConf ig.Remot eId: The identification of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | sha1 | The configurations of phase two negotiation. IpsecConf ig.IpsecEncAlg: The encryption algorithm of phase two negotiations. Valid values: aes \| aes192 \| aes256 \| des \| 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm of phase two negotiations. Valid values: md5 \| sha1. Default value: sha1. IpsecConf ig. IpsecPf s: The Diffie- Hellman group for perfect forward secrecy (PFS). The Diffie-Hellman key exchange algorithm used by phase two negotiations. Valid values: group1 \| group2 \| group5 \| group14 \| group24. Default value: group2. IpsecConf ig. IpsecLif et ime: The SA lifetime value resulting from phase two negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. |
| LocalSubnet | String | No | 1.1.1.0/24,1.1.2.0/ 24 | The CIDR block of the VPC to be connected with the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| RemoteSubnet | String | No | 1.1.1.0/24,1.1.2.0/ 24 | The CIDR block of the on-premises data center. This parameter is used for phase two negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp1bbi27hojx80nck** ** | The ID of the IPsec-VPN connection. |
| CustomerGatew ayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2ogj **** | The ID of the VPN gateway. |
| Name | String | test | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 1.1.1.0/24,1.1.2.0/24 | The CIDR block of the on-premises data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |
| Description | String | description | The description of the IPsec-VPN connection. |
| EffectImmediate ly | Boolean | false | Indicates whether the IPsec-VPN connection takes effect immediately. |
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
| VcoHealthCheck |   |   | The health check configurations. |
| Dip | String | 1.1.1.xx | The destination IP address configured for health checks. |
| Enable | String | true | Indicates whether health checks are enabled. t rue: Health checks are enabled. f alse: Health checks are disabled. |
| Interval | Integer | 3 | The time interval between two consecutive health check retries. Unit: seconds. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Retry | Integer | 1 | The number of attempts for resending health check probes. |
| Sip | String | 2.2.2.xx | The source IP address configured for health checks. |

Sample requests

```xml
https://vpc.example.com/?Action=ModifyVpnConnectionAttribute &RegionId=cn-shanghai &VpnConnectionId=vco-bp1bbi27hojx80nck**** <ModifyVpnConnectionAttributeResponse>
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

#### 1.14.23 CreateSslVpnClientCert

You can call this operation to create an SSL client certificate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnClien tCert | The operation that you want to perform. Set the value to Creat eSslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- m5et0q3iy1qex32 8w**** | The ID of the SSL server. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | SslVpnClientCert1 | The name of the client certificate. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | SslVpnClientCert | The name of the client certificate. |
| RequestId | String | 079874CD-AEC1- 43E6-AC03- ADD96B6E4907 | The ID of the request. |
| SslVpnClientCert Id | String | vsc- m5euof6s5jy8vs5kd** ** | The ID of the client certificate. |

Sample requests

```xml
https://vpc.example.com/?Action=CreateSslVpnClientCert &RegionId=cn-hangzhou &SslVpnServerId=vss-m5et0q3iy1qex328w**** <CreateSslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</CreateSslVpnClientCertResponse>
```

```json
 "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA",
 "SslVpnClientCertId":"vsc-bp1n8wcf134yl0osr****"
```

#### 1.14.24 DescribeSslVpnClientCerts

You can call this operation to query one or more SSL client certificates.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnClie ntCerts | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert s. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificates to be queried. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | cert1 | The name of the SSL client certificate. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| SslVpnClientCertId | String | No | vsc- bp1n8wcf134yl0o sr**** | The name of the SSL client certificate. |
| SslVpnServerId | String | No | vss- bp18q7hzj6largv4 v**** | The ID of the SSL server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| SslVpnClientCert Keys | Array |   | The details of the queried SSL client certificates. |
| SslVpnClientCert Key |   |   | The details of the queried SSL client certificate. |
| CreateTime | Long | 1492747187000 | The time when the SSL client certificate was created. |
| EndTime | Long | 1494966335000 | The time when the SSL client certificate expires. |
| Name | String | cert1 | The name of the SSL client certificate. |
| RegionId | String | cn-hangzhou | The region ID of the SSL client certificate. |
| SslVpnClientCert Id | String | vsc- bp1n8wcf134yl0osr** ** | The ID of the SSL client certificate. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v*** * | The ID of the SSL server. |
| Status | String | normal | The status of the client certificate. expiring-soon: The certificate will expire in one week. normal: The certificate is in a normal state. expired: The certificate has expired. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Sample requests

```
http(s)://vpc.example.com/? Action=DescribeSslVpnClientCerts &RegionId=cn-hangzhou
```

```json
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

`},`

```json
  "PageSize":"10",
  "RequestId":"DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

#### 1.14.25 DeleteVpnPbrRouteEntry

You can call this operation to delete a VPN policy-based route.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnPbrRout eEntry | The operation that you want to perform. Set the value to Delet eVpnPbrRout eEnt ry.. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN policy-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0 \| 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. Set the value to Ipsec (IPsec tunneling protocol). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```json
http(s)://vpc.example.com/? Action=DeleteVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 <DeleteVpnPbrRouteEntryResponse>
      <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnPbrRouteEntryResponse>
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

#### 1.14.26 DeleteVpnRouteEntry

You can call this operation to delete a destination-based route for a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnRouteEn try | The operation that you want to perform. Set the value to Delet eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based route. You can call the DescribeRegions operation to query the most recent region list. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```
http(s)://vpc.example.com/? Action=DeleteVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0
```

```json
<DeleteVpnRouteEntryResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnRouteEntryResponse>
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

#### 1.14.27 CreateVpnPbrRouteEntry

You can call this operation to create a policy-based route for a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnPbrRout eEntry | The operation that you want to perform. Set the value to Creat eVpnPbrRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to publish the policy- based route to the route table of the associated VPC network. t rue: Publish the policy-based route to the route table of the associated VPC network. f alse: Do not publish the policy- based route to the route table of the associated VPC network. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the VPN policy-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | vpnroute1 | The description of the policy-based route. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The time when the policy-based route was created. |
| Description | String | vpnroute1 | The description of the policy-based route. |
| NextHop | String | vco- bp15oes1py4i66rmd* *** | The next hop of the policy-based route. |
| OverlayMode | String | Ipsec | The tunneling protocol. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | 192.168.1.0/24 | The source CIDR block of the policy-based route. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| State | String | normal | The status of the policy-based route. Valid values: published: published normal: not published |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9 **** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0 and 100. |

Sample requests

```xml
http(s)://vpc.example.com/? Action=CreateVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 <CreateVpnPbrRouteEntryResponse>
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

#### 1.14.28 DescribeVpnRouteEntries

You can call this operation to query one or more destination-based routes of a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnRoute Entries | The operation that you want to perform. Set the value to DescribeVpnRout eEnt ries. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based routes. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 10 | The current page number. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |
| TotalCount | Integer | 10 | The total number of entries returned. |
| VpnRouteEntries |   |   | The detailed information about the destination-based routes. |
| CreateTime | Long | 1492747187000 | The time when the destination-based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd* *** | The next hop of the destination-based route. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination- based route. |
| State | String | published | The status of the destination-based route. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9 **** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

Sample requests

```
http(s)://vpc.example.com/? Action=DescribeVpnRouteEntries &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1a3kqjiiq9legfx****
```

```json
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
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "VpnRouteEntries":{
  "VpnRouteEntry":[
    "RouteDest":"10.0.0.0/24",
    "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
    "Weight":100,
    "State":"normal",
    "NextHop":"vco-bp1tui07ob10fmuro****",
    "CreateTime":1563874074000
```

`]` `},`

```json
 "RequestId":"BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5"
```

#### 1.14.29 ModifyVpnRouteEntryWeight

You can call this operation to modify the weight of a destination-based route of a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnRouteE ntryWeight | The operation that you want to perform. Set the value to Modif yVpnRout eEnt ryWeight . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NewWeight | Integer | Yes | 100 | The new weight of the destination- based route after you perform this operation. Valid values: 0 and 100. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The previous weight of the destination- based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```json
http(s)://vpc.example.com/? Action=ModifyVpnRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 <ModifyVpnRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnRouteEntryWeightResponse>
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

#### 1.14.30 PublishVpnRouteEntry

You can call this operation to publish a route of a VPN gateway to the routing table of the associated VPC network.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PublishVpnRouteE ntry | The operation that you want to perform. Set the value to PublishVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to publish the route to the routing table of the associated VPC network. t rue: Publish the route to the routing table of the associated VPC network. f alse: Do not publish the route to the routing table of the associated VPC network. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the route. |
| RouteType | String | Yes | pbr | The type of the route. Valid values: pbr: policy-based route dbr: destination-based route |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```
http(s)://vpc.example.com/? Action=PublishVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteType=PBR &VpnGatewayId=vpn-bp1a3kqjiiq9legfx****
```

```json
<PublishVpnRouteEntryResponse>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</PublishVpnRouteEntryResponse>
 "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

#### 1.14.31 DescribeVpnPbrRouteEntries

You can call this operation to query one or more policy-based routes of a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnPbrRo uteEntries | The operation that you want to perform. Set the value to DescribeVpnPbrRout eEnt ries. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the policy-based routes. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |
| VpnPbrRouteEnt ries |   |   | The detailed information about the policy- based routes. |
| CreateTime | Long | 1492747187000 | The time when the policy-based route entry was created. |
| NextHop | String | vco- bp15oes1py4i66rmd* *** | The next hop of the policy-based route. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | 192.168.0.0/24 | The source CIDR block of the policy-based route. |
| State | String | published | The status of the policy-based route. Valid values: published: published normal: not published |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9 **** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0 and 100. |

Sample requests

```
http(s)://vpc.example.com/? Action=DescribeVpnPbrRouteEntries &RegionId=cn-hangzhou &VpnGatewayId=vpn-bp1a3kqjiiq9legfx****
```

```json
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
 "PageNumber":1,
 "TotalCount":1,
 "PageSize":10,
 "RequestId":"E5D94DC7-AEC7-4E73-A203-61B04D1F1160",
 "VpnPbrRouteEntries":{
  "VpnPbrRouteEntry":[
    "RouteDest":"10.0.0.0/32",
    "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
    "Weight":100,
    "State":"published",
    "RouteSource":"11.0.0.0/32",
    "NextHop":"vco-bp1tui07ob10fmuro****",
    "CreateTime":1563881012000
```

`]`

#### 1.14.32 ModifyVpnPbrRouteEntryWeight

You can call this operation to modify the weight of a policy-based route of a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnPbrRout eEntryWeight | The operation that you want to perform. Set the value to Modif yVpnPbrRout eEnt ryWeight . |

| irtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NewWeight | Integer | Yes | 100 | The new weight of the policy-based route after you perform this operation. Valid values: 0 and 100. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the policy-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The original weight of the policy-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. Set the value to Ipsec (IPsec tunneling protocol). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```json
http(s)://vpc.example.com/? Action=ModifyVpnPbrRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=100 <ModifyVpnPbrRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnPbrRouteEntryWeightResponse>
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

#### 1.14.33 CreateVpnRouteEntry

You can call this operation to create a destination-based route for a VPN gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnRouteEn try | The operation that you want to perform. Set the value to Creat eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to publish the destination-based route to the routing table of the associated VPC network. t rue: Publish the destination-based route to the routing table of the associated VPC network. f alse: Do not publish the destination- based route to the routing table of the associated VPC network. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the destination-based route. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx* *** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The tunneling protocol. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The time when the destination-based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd* *** | The next hop of the destination-based route. |
| OverlayMode | String | Ipsec | The tunneling protocol. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination- based route. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| State | String | published | The status of the destination-based route. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m9 **** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

Sample requests

```json
http(s)://vpc.example.com/? Action=CreateVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-hangzhou &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 <CreateVpnRouteEntryResponse>
   <RouteDest>10.0.0.0/24</RouteDest>
   <VpnInstanceId>vpn-bp1cmw7jh1nfe43m9****</VpnInstanceId>
   <OverlayMode>Ipsec</OverlayMode>
   <State>published</State>
   <Weight>100</Weight>
   <CreateTime>1563873294331</CreateTime>
   <NextHop>vco-bp1tui07ob10fmuro****</NextHop>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</CreateVpnRouteEntryResponse>
 "RouteDest":"10.0.0.0/24",
 "VpnInstanceId":"vpn-bp1cmw7jh1nfe43m9****",
 "OverlayMode":"Ipsec",
 "Weight":100,
 "State":"published",
 "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78",
 "NextHop":"vco-bp1tui07ob10fmuro****",
 "CreateTime":1563873294331
```

#### 1.14.34 DescribeVpnSslServerLogs

You can call this operation to query the logs of an SSL server.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnSslSer verLogs | The operation that you want to perform. Set the value to DescribeVpnSslServerLogs. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL server. You can call the DescribeRegions operation to query the most recent region list. |
| VpnSslServerId | String | Yes | vss- bp155e9yclsg1xg q4**** | The name of the SSL server. |
| From | Integer | No | 2018020201 | The start time of the logs to be queried. |
| MinutePeriod | Integer | No | 10 | The recording cycle of the logs. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| To | Integer | No | 2018020206 | The end time of the logs to be queried. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of log entries. |
| Data |   | test | An array of log entries. Each item in the array indicates a log entry. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsCompleted | Boolean | true | Indicates whether the log is accurate. Valid values: t rue: accurate f alse: inaccurate |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Sample requests

```json
http(s)://vpc.example.com/? Action=DescribeVpnSslServerLogs &RegionId=cn-hangzhou &VpnSslServerId=vss-bp155e9yclsg1xgq4**** <DescribeVpnSslServerLogsResponse>
   <Data></Data>
   <PageNumber>1</PageNumber>
   <Count>0</Count>
   <PageSize>10</PageSize>
   <IsCompleted>true</IsCompleted>
   <RequestId>26641E42-66C7-4942-9FEC-F99213914F8F</RequestId>
</DescribeVpnSslServerLogsResponse>
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

#### 1.14.35 DescribeSslVpnClientCert

You can call this operation to query an SSL client certificate.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnClie ntCert | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert . |
| RegionId | String | Yes | cn-hangzhou | The region ID of the SSL client certificate to be queried. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertId | String | Yes | vsc- bp17r58rjf5r1gjyr* *** | The ID of the SSL client certificate to be queried. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RegionId | String | cn-hangzhou | The region ID of the SSL client certificate. |
| SslVpnClientCert Id | String | vsc- bp13k5mp4tg8v3z9b **** | The ID of the SSL client certificate. |
| Name | String | abc | The name of the SSL client certificate. |
| SslVpnServerId | String | vss- bp155e9yclsg1xgq4* *** | The ID of the SSL server. |
| CaCert | String | The CA certificate | The CA certificate used to sign the client certificate. |
| ClientCert | String | The SSL-VPN client certificate | The SSL client certificate. |
| ClientKey | String | The key of the SSL- VPN client | The key of the SSL client. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ClientConfig | String | The configuration of the SSL-VPN client | The configuration of the SSL client. |
| CreateTime | Long | 1552550980000 | The time when the SSL client certificate was created. |
| EndTime | Long | 1647158980000 | The time when the SSL client certificate expires. |
| Status | String | normal | The status of the client certificate. expiring-soon: The certificate will expire in one week. normal: The certificate is normal. expired: The certificate has expired. |

Sample requests

```
http(s)://vpc.example.com/? Action=DescribeSslVpnClientCert &RegionId=cn-hangzhou &SslVpnClientCertId=vsc-bp17r58rjf5r1gjyr****
```

`JSON` &nbsp;format

```json
    "Name": "df",
    "Status": "normal",
    "ClientConfig": "****",
    "ClientCert": "****",
    "CreateTime": 1552550980000,
    "RegionId": "cn-hangzhou",
    "RequestId": "49D54005-6E0E-4132-B305-F3A24DEDDDC9",
    "EndTime": 1647158980000,
    "SslVpnClientCertId": "vsc-bp13k5mp4tg8v3z9b****",
    "ClientKey": "****",
    "CaCert": "****",
    "SslVpnServerId": "vss-bp155e9yclsg1xgq4****"
```

```xml
<DescribeSslVpnServersResponse>
      <Name>df</Name>
      <Status>normal</Status>
      <ClientConfig>****</ClientConfig>
      <ClientCert>****</ClientCert>
      <CreateTime>1552550980000</CreateTime>
      <RegionId>cn-hangzhou</RegionId>
      <RequestId>49D54005-6E0E-4132-B305-F3A24DEDDDC9</RequestId>
      <EndTime>1647158980000</EndTime>
      <SslVpnClientCertId>vsc-bp13k5mp4tg8v3z9b****</SslVpnClientCertId>
      <ClientKey>****</ClientKey>
      <CaCert>****</CaCert>
      <SslVpnServerId>vss-bp155e9yclsg1xgq4****</SslVpnServerId>
</DescribeSslVpnServersResponse>
```

### 1.15 IPv6 Gateway

#### 1.15.1 CreateIpv6Gateway

You can call this operation to create an IPv6 gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Gatewa y | The operation that you want to perform. Set the value to Creat eIpv6Gat eway. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- 123456defrde**** | The ID of the VPC for which you want to create the IPv6 gateway. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | ipv6gatewayforVP C1 | The description of the IPv6 gateway. The description must be 2 to 256 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a _ letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | ipv6GW | The name of the IPv6 gateway. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |
| Spec | String | No | Small | The specification of the IPv6 gateway. Valid values: Small (default): free edition Medium: enterprise edition Large: enhanced enterprise edition |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6GatewayId | String | ipv6gw- hp3y0l3ln89j8bgnh*** * | The ID of the IPv6 gateway. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC | The ID of the request. |

Sample requests

```
https://vpc.example.com/?Action=CreateIpv6Gateway &RegionId=cn-huhehaote &VpcId=vpc-hp3x04of74a6aqsw**** &Common request parameters
```

```json
<CreateIpv6GatewayResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
      <Ipv6GatewayId>vipv6gw-hp3y0l3ln89j8qsw****</Ipv6GatewayId>
</CreateIpv6GatewayResponse>
 "RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
 "Ipv6GatewayId":"ipv6gw-hp3y0l3ln89j8qsw****"
```

#### 1.15.2 DeleteIpv6Gateway

You can call this operation to delete an IPv6 gateway. API description Before you can delete an IPv6 gateway of the enterprise or enhanced enterprise type, you must delete the egress-only rules of the IPv6 gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Gatewa y | The operation that you want to perform. Set the value to Delet eIpv6Gat eway. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3y0l3ln89j8bgn h**** | The ID of the IPv6 gateway instance that you want to delete. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9A8AABE-A84B- 4AF2-A68A- 8E2EA190E7AE | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=DeleteIpv6Gateway &Ipv6GatewayId=ipv6gw-hp3y0l3ln89j8bgnh**** &RegionId=cn-huhehaote <DeleteIpv6GatewayResponse>
      <RequestId>E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE</RequestId>
</DeleteIpv6GatewayResponse>
 "RequestId":"E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE"
```

#### 1.15.3 ModifyIpv6GatewaySpec

You can call this operation to modify the specification of an IPv6 gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gatewa ySpec | The operation that you want to perform. Set the value to Modif yIpv6Gat ewaySpec. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456nhmj**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Spec | String | Yes | Middle | The new specification you want to set for the IPv6 gateway. Valid values: Small (default): free edition Middle: enterprise edition Large: enhanced enterprise edition |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=ModifyIpv6GatewaySpec &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456cdvf**** &Spec=Middle &Common request parameters <ModifyIpv6GatewaySpecResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewaySpecResponse>
 "RequestId":"9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

#### 1.15.4 DescribeIpv6EgressOnlyRules

You can call this operation to query the egress-only rules that match specific conditions.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Egres sOnlyRules | The operation that you want to perform. Set the value to DescribeIpv6EgressOnlyRules. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456cdvf**** | The ID of the IPv6 gateway with which the egress-only rules are configured. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| InstanceId | String | No | i-123456cdvf**** | The ID of the instance that is associated with the IPv6 address configured with the egress-only rules. |
| InstanceType | String | No | Ipv6Address | The type of the instance that is configured with the egress-only rules. Set the value to: Ipv6Address: IPv6 address |
| Ipv6EgressOnlyRul eId | String | No | ipv6gwpy- 123456cdvf**** | The ID of the egress-only rule that you want to query. |
| Name | String | No | rulename | The name of the egress-only rule. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressOnlyR ules |   |   | The details of the egress-only rules. |
| Description | String | ruledescription | The description of the egress-only rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | i-123456cdvf**** | The ID of the instance that is configured with the egress-only rule. |
| InstanceType | String | Ipv6Address | The type of the instance that is configured with the egress-only rule. |
| Ipv6EgressOnlyR uleId | String | ipv6gwpy- 123456cdvf**** | The ID of the egress-only rule. |
| Name | String | rulename | The name of the egress-only rule. |
| Status | String | Available | The status of the egress-only rule. |
| PageNumber | Integer | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | E16671B7-DEA6- 48E0-8E9C- 41913DAD44DD | The ID of the request. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Sample requests

```
https://vpc.example.com/?Action=DescribeIpv6EgressOnlyRules &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456cdvf**** &Common request parameters
```

```json
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
 "Ipv6EgressOnlyRules":{
  "Ipv6EgressOnlyRule":[
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

#### 1.15.5 CreateIpv6EgressOnlyRule

You can call this operation to create and configure an egress-only rule with an IPv6 address.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6EgressO nlyRule | The operation that you want to perform. Set the value to Creat eIpv6EgressOnlyRule. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceId | String | Yes | ipv6- hp3nxjkfxn5pnhgl 5**** | The ID of the IPv6 address with which the egress-only rule will be configured. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3c2paq0ywauas za**** | The ID of the IPv6 gateway to which the specified IPv6 address belongs. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | ruledescription | The description of the egress-only rule. The description must be 2 to 256 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a _ letter or Chinese character and cannot start with http:// or https:// . |
| InstanceType | String | No | IPv6Address | The type of the instance that will be configured with the egress-only rule. Set the value to: Ipv6Address (Default): IPv6 address |
| Name | String | No | rulename | The name of the egress-only rule. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressRuleId | String | ipv6py- hp3w98rmlbqp01245 **** | The ID of the egress-only rule. |
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=CreateIpv6EgressOnlyRule &RegionId=cn-huhehaote &InstanceId=ipv6-hp3nxjkfxn5pnhgl5**** &Ipv6GatewayId=ipv6gw-hp3c2paq0ywauasza**** &Common request parameters <CreateIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
   <Ipv6EgressRuleId>ipv6py-hp3w98rmlbqp01245****</Ipv6EgressRuleId>
</CreateIpv6EgressOnlyRuleResponse>
 "RequestId":"9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75",
 "Ipv6EgressRuleId":"ipv6py-hp3w98rmlbqp01245****"
```

#### 1.15.6 DeleteIpv6EgressOnlyRule

You can call this operation to delete an egress-only rule.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6EgressO nlyRule | The operation that you want to perform. Set the value to Delet eIpv6EgressOnlyRule. |
| Ipv6EgressOnlyRul eId | String | Yes | ipv6py- hp3w98rmlbqp0vf bg**** | The ID of the egress-only rule that you want to delete. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=DeleteIpv6EgressOnlyRule &RegionId=cn-huhehaote &Ipv6EgressOnlyRuleId=ipv6py-hp3w98rmlbqp0vfbg**** &Common request parameters <DeleteIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</DeleteIpv6EgressOnlyRuleResponse>
 "RequestId":"4E40EAF1-783D-4C05-948D-DA0426C398C1"
```

#### 1.15.7 DeleteIpv6InternetBandwidth

You can call this operation to disable public access to an IPv6 address and set its public network bandwidth to zero.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Internet Bandwidth | The operation that you want to perform. Set the value to Delet eIpv6Int ernet Bandwidt h. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway to which the IPv6 address belongs. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6- 123456xxxxxxxx | The ID of the IPv6 address. |
| Ipv6InternetBandw idthId | String | No | 2 | The public network bandwidth of the IPv6 address. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E07E0FE6-5C21-405F- AF82-7613AA81EF92 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=DeleteIpv6InternetBandwidth &RegionId=cn-huhehaote <DeleteIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
</DeleteIpv6InternetBandwidthResponse>
 "RequestId":"E07E0FE6-5C21-405F-AF82-7613AA81EF92"
```

#### 1.15.8 DescribeIpv6GatewayAttribute

You can call this operation to query the details of an IPV6 gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gate wayAttribute | The operation that you want to perform. Set the value to DescribeIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456vfbg**** | The ID of the IPv6 gateway to query. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments Securit yLocked: locked due to security reasons |
| CreationTime | String | 2018-12- 05T09:21:35Z | The time when the IPv6 gateway was created. |
| Description | String | test | The description of the IPv6 gateway. |
| ExpiredTime | String | 2018-12- 05T09:21:35Z | The time when the IPv6 gateway expires. |
| Ipv6GatewayId | String | ipv6gw- 123456xxxxxxxx | The instance ID of the IPv6 gateway. |
| Name | String | test | The name of the IPv6 gateway. |
| RegionId | String | cn-huhehaote | The region ID of the IPv6 gateway. |
| RequestId | String | ipv6gw- hp33p10bdbt77vfbg* *** | The ID of the request. |
| Spec | String | Medium | The specification of the IPv6 gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Available | The status of the IPv6 gateway. |
| VpcId | String | vpc-123456vfbg**** | The ID of the VPC instance to which the IPv6 gateway belongs. |

Sample requests

```json
https://vpc.example.com/?Action=DescribeIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-hp33p10bdbt77vfbg**** &RegionId=cn-huhehaote &Common request parameters <DescribeIpv6GatewayAttributeResponse>
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

#### 1.15.9 DescribeIpv6Addresses

Queries one or more IPv6 addresses.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Addre sses | The operation that you want to perform. Set the value to DescribeIpv6Addresses. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| AssociatedInstanc eId | String | No | i-123456nhmj**** | The ID of the instance associated with the IPv6 address. |
| AssociatedInstanc eType | String | No | EcsInstance | The type of the instance associated with the IPv6 address. Set the value to EcsInst ance (default): an ECS instance in a VPC |
| Ipv6Address | String | No | 2408:xxxx:180:17 01:94c7:bc38:3bf a:d2c | The IPv6 address that you want to query. |
| Ipv6AddressId | String | No | ipv6gw- hp33of4uz4k4knh mj**** | The instance ID of the IPv6 address. You can enter up to 20 instance IDs at a time. Separate instance IDs with commas (,). |
| Ipv6InternetBandw idthId | String | No | 1 | The Internet bandwidth of the IPv6 address. |
| Name | String | No | test | The name of the IPv6 address. |
| NetworkType | String | No | Public | The communication type of the IPv6 address. Valid values: Privat e: communication within the private network Public: communication over the Internet |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| VSwitchId | String | No | vsw- 123456nhmj**** | The ID of the VSwitch to which the IPv6 address belongs. |
| VpcId | String | No | vpc- 123456nhmj**** | The ID of the VPC to which the IPv6 address belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Addresses |   |   | The details of IPv6 addresses. |
| AllocationTime | String | 2018-12- 20T14:56:09Z | The time when the IPv6 address was created. |
| AssociatedInsta nceId | String | i- hp325kt6307nhmj**** | The ID of the instance associated with the IPv6 address. |
| AssociatedInsta nceType | String | EcsInstance | The type of the instance associated with the IPv6 address. |
| Ipv6Address | String | 2408:xxxx:0:2900:29 01:3c61:9ff0:xxxx | The IPv6 address. |
| Ipv6AddressId | String | ipv6- hp32vv2klzw4nhmj*** * | The instance ID of the IPv6 address. |
| Ipv6AddressNa me | String | test | The instance name of the IPv6 address. |
| Ipv6GatewayId | String | ipv6gw- hp38x2x0fz7nhmj**** | The ID of the IPv6 gateway to which the IPv6 address belongs. |
| Ipv6InternetBan dwidth |   |   | The information about the Internet bandwidth of the IPv6 address. |
| Bandwidth | Integer | 2 | The exclusive Internet bandwidth of the IPv6 address. Unit: Mbit/s. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the exclusive bandwidth of the IPv6 address. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| Ipv6InternetBan dwidthId | String | ipv6bw- hp3b35oq1fj5nhmj*** * | The ID of the Internet bandwidth. |
| NetworkType | String | Public | The communication type of the IPv6 address. Valid values: Privat e: communication within the private network Public: communication over the Internet |
| Status | String | Available | The status of the IPv6 address. Valid values: Pending: The IPv6 address is being configured. Available: The IPv6 address is available. |
| VSwitchId | String | vsw- hp3123456nhmj**** | The ID of the VSwitch to which the IPv6 address belongs. |
| VpcId | String | vpc-123456nhmj**** | The ID of the VPC to which the IPv6 address belongs. |
| PageNumber | Integer | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | AA4486A8-B6AE- 469E-AB09- 820EF8ECFA2B | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Sample requests

```
https://vpc.example.com/?Action=DescribeIpv6Addresses &RegionId=cn-huhehaote
```

Sample success responses

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

```json
 "PageNumber":1,
 "TotalCount":2,
 "Ipv6Addresses":{
  "Ipv6Address":[
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

`},`

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

#### 1.15.10 AllocateIpv6InternetBandwidth

You can call this operation to purchase public network bandwidth for an IPv6 address.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateIpv6Intern etBandwidth | The operation that you want to perform. Set the value to Allocat eIpv6Int ernet Bandwidt h. |
| Bandwidth | Integer | Yes | 2 | The public network bandwidth of the IPv6 address. |
| Ipv6AddressId | String | Yes | ipv6- 123456cdvf**** | The instance ID of the IPv6 address. |
| Ipv6GatewayId | String | Yes | ipv5gw- 123456cdvf**** | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetBandwid thId | String | 2 | The purchased public network bandwidth. |
| Ipv6AddressId | String | ipv6- hp352ungkzckndcvf** ** | The instance ID of the IPv6 address. |
| RequestId | String | 6972A26E-99B1- 4367-9890- FBDEBB0F5E7D | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?AllocateIpv6InternetBandwidth &Ipv6AddressId=ipv6-123456cdvf**** &Ipv6GatewayId=ipv6gw-123456cdvf**** &RegionId=cn-huhehaote <AllocateIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
   <InternetBandwidthId>2</InternetBandwidthId>
   <Ipv6AddressId>ipv6-hp352ungkzckncdvf****</Ipv6AddressId>
</AllocateIpv6InternetBandwidthResponse>
 "Ipv6AddressId":"ipv6-hp352ungkzckncdvf****",
 "RequestId":"6972A26E-99B1-4367-9890-FBDEBB0F5E7D",
 "InternetBandwidthId":2
```

#### 1.15.11 ModifyIpv6InternetBandwidth

You can call this operation to modifiy the public network bandwidth of an IPv6 address.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Internet Bandwidth | The operation that you want to perform. Set the value to Modif yIpv6Int ernet Bandwidt h. |
| Bandwidth | Long | Yes | 4 | The public network bandwidth of the IPv6 address. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Ipv6AddressId | String | No | ipv6- 1233456cdvf**** | The instance ID of the IPv6 address. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=ModifyIpv6InternetBandwidth &Bandwidth=3 &Ipv6AddressId=ipv6-hp351bytt9inrcdvf**** &RegionId=cn-huhehaote &Common request parameters <ModifyIpv6InternetBandwidthResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6InternetBandwidthResponse>
 "RequestId":"D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

#### 1.15.12 ModifyIpv6GatewayAttribute

You can call this operation to modify the name and description of an IPv6 gateway.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gatewa yAttribute | The operation that you want to perform. Set the value to Modif yIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp39kh1ya51yzp2l u**** | The ID of the IPv6 gateway to be modified. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Description | String | No | ipv6description | The description of the IPv6 gateway. |
| Name | String | No | ipv6name | The name of the IPv6 gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB-49E8- A2DC-CC114C67AF75 | The ID of the request. |

Sample requests

```json
https://vpc.example.com/?Action=ModifyIpv6GatewayAttribute &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-hp39kh1ya51yzp2lu**** &Common request parameters <ModifyIpv6GatewayAttributeResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewayAttributeResponse>
 "RequestId":"9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

#### 1.15.13 ModifyIpv6AddressAttribute

You can call this operation to modify the name and description of an IPv6 address.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Addres sAttribute | The operation that you want to perform. Set the value to Modif yIpv6AddressAt t ribut e. |
| Ipv6AddressId | String | Yes | ipv6- hp32vv2klzw4yerd f**** | The ID of the IPv6 address. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 address. You can call the DescribeRegions operation to query the most recent region list. |
| Description | String | No | test | The description of the IPv6 address. The description must be 2 to 256 characters in length. It can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a _ letter or Chinese character and cannot start with http:// or https:// . |
| Name | String | No | test | The name of the IPv6 address. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens _ (-). It must start with a letter or Chinese character and cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

Sample requests

```
http(s)://vpc.example.com/? Action=ModifyIpv6AddressAttribute &Ipv6AddressId=ipv6-hp32vv2klzw4yerdf**** &RegionId=cn-huhehaote
```

```json
<ModifyIpv6AddressAttributeResponse>
   <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6AddressAttributeResponse>
 "RequestId":"D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

#### 1.15.14 DescribeIpv6Gateways

You can call this operation to query one or more IPv6 gateways.

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gate ways | The operation that you want to perform. Set the value to DescribeIpv6Gat eways. |
| RegionId | String | Yes | cn-huhehaote | The region ID of the IPv6 gateway. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6GatewayId | String | No | ipv6gw- 123456xscd**** | The ID of the IPv6 gateway. |
| Name | String | No | ipv6GW | The name of the IPv6 gateway. |
| PageNumber | Integer | No | 1 | The number of the returned page. |
| PageSize | Integer | No | 10 | The number of entries returned per page. |
| VpcId | String | No | vpc- 123456xscd**** | The ID of the VPC to which the IPv6 gateway belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Gateways |   |   | The details of the IPv6 gateways |
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal: normal FinancialLocked: locked due to overdue payments |
| CreationTime | String | 2018-12- 20T14:51:23Z | The time when the IPv6 gateway was created. |
| Description | String | descriptionforIPv6GW | The description of the IPv6 gateway. |
| ExpiredTime | String | 2018-12- 20T14:51:23Z | The time when the IPv6 gateway expires. |
| InstanceChargeT ype | String | PostPaid | The billing method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw- hp3rwmtmfhgisxscd* *** | The ID of the IPv6 gateway. |
| Name | String | name | The name of the IPv6 gateway. |
| RegionId | String | cn-huhehaote | The region ID of the IPv6 gateway. |
| Spec | String | Small | The specification of the IPv6 gateway. |
| Status | String | Available | The running status of the IPv6 gateway. |
| VpcId | String | vpc-123456xscd**** | The ID of the VPC to which the IPv6 gateway belongs. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 19 | The number of entries returned per page. |
| RequestId | String | E3A06196-3E7C- 490D-8F39- CB4B5A0CE8AD | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Sample requests

```xml
https://vpc.example.com/?Action=DescribeIpv6Gateways &RegionId=cn-huhehaote &Common request parameters <DescribeIpv6GatewaysResponse>
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

```json
 "Ipv6Gateways":{
  "Ipv6Gateway":[
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

`},`

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

### 1.16 High-Availability Virtual IP

#### 1.16.1 CreateHaVip

Creates a high-availability virtual IP address (HAVIP).

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateHaVip | The operation that you want to perform. Set the value to CreateHaVip. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| VSwitchId | String | Yes | vsw- asdfjlnaue4g**** | The ID of the VSwitch to which the HAVIP belongs. |
| IpAddress | String | No | 192.xx.xx.10 | The IP address of the HAVIP. If this parameter is not specified, an idle IP address of the specified VSwitch is allocated to the HAVIP. |
| Description | String | No | abcabc | The description of the HAVIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |
| HaVipId | String | havip- 2zeo05qre24nhrqpy*** * | The ID of the HAVIP. |

Sample request s

```xml
https://vpc.example.com/?Action=CreateHaVip &VSwitchId=vsw-asdfjlnaue4g**** &RegionId=cn-hangzhou &Common request parameters <CreateHaVipResponse>
    <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
    <HaVipId>havip-2zeo05qre24nhrqpy****</HaVipId>
</CreateHaVipResponse>
```

```json
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF",
    "HaVipId": "havip-2zeo05qre24nhrqpy****"
```

#### 1.16.2 ModifyHaVipAttribute

Modifies the description of a high-availability virtual IP address (HAVIP).

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyHaVipAttribut e | The operation that you want to perform. Set the value to ModifyHaVipAttribute. |
| RegionId | String | Yes | cn-shanghai | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqp* *** | The ID of the HAVIP. |
| Description | String | No | abcabc | The new description of the HAVIP. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Sample request s

```xml
https://vpc.example.com/?Action=ModifyHaVipAttribute &HaVipId=havip-2zeo05qre24nhrqp**** &RegionId=cn-shanghai &Common request parameters <ModifyHaVipAttributeResponse>
    <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</ModifyHaVipAttributeResponse>
```

```json
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

#### 1.16.3 DeleteHaVip

Deletes a high-availability virtual IP address (HAVIP). When you call this operation, follow these rules: You can only delete an HAVIP that is in the Available state. Make sure that there is no route destined to the HAVIP that you want to delete. Make sure that the HAVIP you want to delete is not associated with any elastic IP address (EIP).

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteHaVip | The operation that you want to perform. Set the value to DeleteHaVip. |
| RegionId | String | Yes | cn-shanghai | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqpy **** | The ID of the HAVIP to be deleted. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988B | The ID of the request. |

Sample request s

```
https://vpc.example.com/?Action=DeleteHaVip &HaVipId=havip-2zeo05qre24nhrqpy**** &RegionId=cn-shanghai &Common request parameters
```

```json
<DeleteHaVipResponse>
    <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</DeleteHaVipResponse>
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

#### 1.16.4 AssociateHaVip

Associates a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). When you call this operation, follow these rules: The HAVIP takes effect immediately after it is associated with an ECS instance in a VPC. You do not need to restart the ECS instance. However, you must configure the HAVIP on the network interface controller (NIC) of the ECS instance. The HAVIP and the ECS instance must belong to the same VSwitch. You can associate an HAVIP with a maximum of two ECS instances. The ECS instance must either be in the Running or Stopped state. The HAVIP must either be in the Available or InUse state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateHaVip | The operation that you want to perform. Set the value to AssociateHaVip. |
| RegionId | String | Yes | cn-shanghai | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqpy **** | The ID of the HAVIP. |
| InstanceId | String | Yes | i- faf344422ffsfad**** | The ID of the ECS instance that you want to associate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=AssociateHaVip &HaVipId=havip-2zeo05qre24nhrqpy**** &RegionId=cn-shanghai &InstanceId=i-faf344422ffsfad**** &Common request parameters <AssociateHaVipResponse>
    <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</AssociateHaVipResponse>
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

#### 1.16.5 UnassociateHaVip

Dissociates a high-availability virtual IP address (HAVIP) from an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). When you call this operation, follow these rules: The ECS instance must either be in the Running or Stopped state. The HAVIP must either be in the Available or InUse state.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateHaVip | The operation that you want to perform. Set the value to UnassociateHaVip. |
| RegionId | String | Yes | cn-shanghai | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |

| Developer Guide·A | PI referen | ce |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| HaVipId | String | Yes | havip- 2zeo05qre24nhrqpy **** | The ID of the HAVIP. |
| InstanceId | String | Yes | i- faf344422ffsfad**** | The ID of the ECS instance that you want to dissociate. |
| Force | String | No | True | Specifies whether to force a dissociation. Valid values: True and False. Default value: False Not e If you set this parameter to False, you cannot disassociate an HAVIP from a primary ECS instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7-4277- B117-69243F3988BF | The ID of the request. |

Sample request s

```json
https://vpc.example.com/?Action=UnassociateHaVip &HaVipId=havip-2zeo05qre24nhrqpy**** &RegionId=cn-shanghai &InstanceId=i-faf344422ffsfad**** &Common request parameters <UnassociateHaVipResponse>
    <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</UnassociateHaVipResponse>
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

#### 1.16.6 DescribeHaVips

Queries high-availability virtual IP address (HAVIPs) in a specified region.

| Param eter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHaVips | The operation that you want to perform. Set the value to DescribeHaVips. |
| Regio nId | String | Yes | cn-hangzhou | The ID of the region where you want to query HAVIPs. You can call the DescribeRegions operation to query the most recent region list. |
| Filter. n.Key | String | Yes | Filter.1.HaVipId | Specifies filter condition n. You can specify a maximum of five filter conditions. Valid values of n: 1, 2, 3, 4, and 5. You can specify multiple values for each filter condition. Specified values have logical OR relations, which means that even if an HAVIP matches only one value of a filter condition, it still meets this condition. Filter conditions are connected with AND operators, in which case all the filter conditions must be met for an HAVIP to be included in the result. The following filter conditions are available: VpcId: the ID of the virtual private cloud (VPC). VSwitchId: the ID of the VSwitch Status: the status of the HAVIP HaVipId: the ID of the HAVIP HaVipAddress: the IP address of the HAVIP |
| Filter. n.Valu e.m | String | Yes | Filter.1.havip- bp149uyvut73dplq2q* *** | Specifies value m of filter condition n. Valid values of m: 1, 2, 3, 4, and 5. |
| PageN umber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSi ze | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10 |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 33E480C5-B46F-4CA5- B6FD-D77C746E86AB | The ID of the request. |
| TotalCount | String | 1 | The total number of entries. |

| Developer Guide·API | reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The number of the page returned. |
| PageSize | String | 10 | The number of entries returned per page. |
| HaVipItemType | List |   | Details about a returned HAVIP. For more information, see the HaVipItemType table. |

HaVipItemType

| Parameter | Type | Example | Description |
|---|---|---|---|
| HaVipId | String | havip- bp149uyvut73dpld**** | The ID of the HAVIP. |
| RegionId | String | cn-hangzhou | The region ID of the HAVIP. |
| VpcId | String | vpc- bp1kcm36tevkpms97o **** | The ID of the VPC to which the HAVIP belongs. |
| VSwitchId | String | vsw- bp1pkt1fba8e824ezs* *** | The ID of the VSwitch to which the HAVIP belongs. |
| IpAddress | String | 192.168.35.xx | The private IP address of the HAVIP. |
| Status | String | Available | The status of the HAVIP. |
| AssociatedInstan ces | String | i- bp145q7glnuzdvzu21* *** | The Elastic Compute Service (ECS) instances that are associated with the HAVIP. |
| MasterInstanceId | String | i-bp145q7glnuzdvz**** | The ID of the primary instance that is associated with the HAVIP. |
| AssociatedEipAd dresses | String | 121.23.36.xx | The list of elastic IP addresses (EIPs) that are associated with the HAVIP. |
| Description | String | abcabc | The description of the HAVIP. |
| CreationTime | String | 2018-07- 03T14:25:26Z | The time when the HAVIP was created. |

Sample request s

```
https://vpc.example.com/?Action=DescribeHaVips &RegionId=cn-hangzhou &Filter=HaVipId.havip-bp149uyvut73dplq2q**** &Common request parameters
```

```json
<DescribeHaVipsResponse> <PageNumber>1</PageNumber> <TotalCount>1</TotalCount> <HaVips>
    <HaVip>
    <Status>Available</Status>
    <Description></Description>
    <MasterInstanceId></MasterInstanceId>
    <AssociatedInstances></AssociatedInstances>
    <AssociatedEipAddresses></AssociatedEipAddresses>
    <CreateTime>2018-07-03T14:25:26Z</CreateTime>
    <RegionId>cn-hangzhou</RegionId>
    <IpAddress>192.xx.xx.27</IpAddress>
    <HaVipId>havip-bp149uyvut73ddefr****</HaVipId>
    <VSwitchId>vsw-bp1pkt1fba8e8defr****</VSwitchId>
    <VpcId>vpc-bp1kcm36tevkpdefr****</VpcId>
    </HaVip>
</HaVips> <PageSize>10</PageSize> <RequestId>33E480C5-B46F-4CA5-B6FD-D77C746E86AB</RequestId> </DescribeHaVipsResponse>
    "PageNumber": 1,
    "TotalCount": 1,
    "HaVips": {
        "HaVip": [
                "Status": "Available",
                "Description": "",
                "MasterInstanceId": "",
                "AssociatedInstances": {
                    "associatedInstance": [ ]
```

`},`

```json
                "AssociatedEipAddresses": {
                    "associatedEipAddresse": [ ]
```

`},`

```json
                "CreateTime": "2018-07-03T14:25:26Z",
                "RegionId": "cn-hangzhou",
                "IpAddress": "192.xx.xx.27",
                "HaVipId": "havip-bp149uyvut73ddefr****",
                "VSwitchId": "vsw-bp1pkt1fba8e82defr****",
                "VpcId": "vpc-bp1kcm36tevkpmdefr****"
```

`]` `},`

```json
    "PageSize": 10,
    "RequestId": "33E480C5-B46F-4CA5-B6FD-D77C746E86AB"
```

### 1.17 DescribeRegions

Queries available regions.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 611CB80 C-B6A9- 43DB- 9E38- 0B0AC3 D9B58F | The ID of the request. |
| Regions | List |   | The list of available regions. |
| RegionId | String | cn- qingdao | The region ID. |

Sample request s

```xml
https://vpc.example.com/?Action=DescribeRegions <? xml version="1.0" encoding="utf-8"? > <DescribeRegionsResponse>
  <RequestId>611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F</RequestId>
  <Regions>
    <Region>
      <RegionId>cn-hangzhou</RegionId>
    </Region>
    <Region>
      <RegionId>cn-qingdao</RegionId>
    </Region>
  </Regions>
</DescribeRegionsResponse>
```

```json
    "RequestId": "611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F",
    "Regions": {
        "Region": [
                "RegionId": "cn-hangzhou "
```

`},`

```json
                "RegionId": "cn-qingdao"
```

`]`

### 1.18 DescribeZones

Queries zones in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-hangzhou | The region ID. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6FEA0CF3-D3B9-43E5- A304-D217037876A8 | The ID of the request. |
| Zones | List |   | The list of zones. |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| LocalName | String | Hangzhou Zone B | The name of the zone. |

Sample request s

```
https://vpc.example.com/?Action=DescribeZones &amp;RegionId=cn-hangzhou
```

```xml
<? xml version="1.0" encoding="UTF-8" ? > <DescribeZonesResponse> <RequestId>6FEA0CF3-D3B9-43E5-A304-D217037876A8</RequestId>
 <Zones>
  <Zone>
   <ZoneId>cn-hangzhou-b</ZoneId>
   <LocalName>Hangzhou Zone B</LocalName>
  </Zone>
  <Zone>
   <ZoneId>cn-hangzhou-d</ZoneId>
   <LocalName>Hangzhou Zone D</LocalName>
  </Zone>
  <Zone>
   <ZoneId>cn-hangzhou-e</ZoneId>
   <LocalName>Hangzhou Zone E</LocalName>
  </Zone>
  <Zone>
   <ZoneId>cn-hangzhou-f</ZoneId>
   <LocalName>Hangzhou Zone F</LocalName>
  </Zone>
  <Zone>
   <ZoneId>cn-hangzhou-g</ZoneId>
   <LocalName>Hangzhou Zone G</LocalName>
  </Zone>
  <Zone>
   <ZoneId>cn-hangzhou-h</ZoneId>
   <LocalName>Hangzhou Zone H</LocalName>
  </Zone>
 </Zones>
<DescribeZonesResponse>
```

```json
 "RequestId":"6FEA0CF3-D3B9-43E5-A304-D217037876A8",
 "Zones":{
  "Zone":[
    "ZoneId":"cn-hangzhou-b",
    "LocalName":"Hangzhou Zone B"
```

`},`

```json
    "ZoneId":"cn-hangzhou-d",
    "LocalName":"Hangzhou Zone D"
```

`},`

```json
    "ZoneId":"cn-hangzhou-e",
    "LocalName":"Hangzhou Zone E"
```

`},`

```json
    "ZoneId":"cn-hangzhou-f",
    "LocalName":"Hangzhou Zone F"
```

`},`

```json
    "ZoneId":"cn-hangzhou-g",
    "LocalName":"Hangzhou Zone G"
```

`},`

```json
    "ZoneId":"cn-hangzhou-h",
    "LocalName":"Hangzhou Zone H"
```

`]`

### 1.19 DescribeAccessPoints

Queries the access points of physical connections in a specified region.

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessPoint s | The operation that you want to perform. Set the value to DescribeAccessPoints. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the access points that you want to query. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Developer Guide·A | PI referen | ce |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Requi red | Example | Description |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3E85D803-C7CF-4BCD- 9CFE-6DBA1DFFA027 | The ID of the request. |
| TotalCount | String | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | String | 10 | The number of entries returned per page. |
| AccessPointSet | List |   | Access point information. For more information, see the AccessPointSet list. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessPointI d | String | ap-cn-beijing-ft-A | The ID of the access point. |
| AttachedReg ionNo | String | cn-beijing | The region ID of the access point. |
| Description | String | ap1 | The description of the access point. |
| HostOperato r | String | CNIX | The carrier of the access point. |
| Location | String | aplocation | The location of the access point. |
| Name | String | Beijing-Fengtai-A | The name of the access point. |
| Status | String | recommended | The status of the access point. |
| Type | String | VPC | The network type of the physical connection. |

Sample request s

```
https://vpc.example.com/?Action=DescribeAccessPoints &RegionId=cn-beijing
```

```json
    "AccessPointSet": {
        "AccessPointType": [
                "Name": "Beijing-Fengtai-A",
                "Status": "recommended",
                "Description": "cn-beijing-ft-cxp32",
                "Type": "VPC",
                "Location": "",
                "HostOperator": "CNIX",
                "AttachedRegionNo": "cn-beijing",
                "AccessPointId": "ap-cn-beijing-ft-A"
"PageNumber": 1, "TotalCount": 1, "PageSize": 10, "RequestId": "3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027" <? xml version="1.0" encoding="UTF-8" ? > </DescribeAccessPointsResponse>
      <AccessPointSet>
            <AccessPointType>
            <Name>Beijing-Fengtai-A</Name>
            <Status>recommended</Status>
            <Description>cn-beijing-ft-cxp32</Description>
            <Type>VPC</Type>
            <Location></Location>
            <HostOperator>xxx</HostOperator>
            <AttachedRegionNo>cn-beijing</AttachedRegionNo>
            <AccessPointId>ap-cn-beijing-ft-A</AccessPointId>
            </AccessPointType>
       </AccessPointSet>
       <PageNumber>1</PageNumber>
       <TotalCount>1</TotalCount>
       <PageSize>10</PageSize>
<RequestId>3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027</RequestId> </DescribeAccessPointsResponse>
```

ng ASAPI

## 2 Call VPC SDK by using ASAPI

### 2.1 Overview

This topic describes the architecture and features of Apsara Stack API (ASAPI). ASAPI is a platform that integrates all features and is the only portal to connect to Apsara Stack. ASAPI can categorize operations and audit and manage their calls. It can also assemble and customize existing operations and adapt to your operations. Each cloud service can call ASAPI for required data and features, avoiding inconsistent operations caused by different call methods and separate encapsulation. This can ensure the operation program integrity and improve development efficiency and code portability. ASAPI allows you to manage and call operations in a unified manner and customize development. ASAPI supports access of most cloud services deployed in Apsara Stack and passthrough or encapsulation of different backend APIs. This way, operations can be called with the same method. ASAPI allows you to use SDKs and API Portal to call APIs registered in ASAPI, customize SDKs, and manage versions of Apsara Stack, services, and APIs.

### 2.2 Log on to the API Tool console

ng ASAPI You can log on to the API Tool console through the Apsara Stack Cloud Management (ASCM) console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the Enter
key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

### 2.3 View the information about API operations

operations You must obtain a service name, API operation name, and API version. All the information is required when you use SDKs. Procedure
1. Log on to the API Tool console.
2. In the left-side navigation pane, click API f old.
3. On the API Direct ory page, select the target service from the drop-down list, enter the API operation
name in the search box, and then click the search icon. ng ASAPI
4. View and remember the service name, API operation name, and API version.

### 2.4 Obtain the endpoint of ASAPI

You can obtain the endpoint of Apsara Stack API (ASAPI) in the Apsara Stack Operations (ASO) console. Procedure
1. In the address bar, enter the URL region-id.aso.intranet-domain-id.com and press the Enter key.
Not e You can select a language from the drop-down list in the upper-right corner of the page.
2. Enter your username and password.
Not e Obtain the username and password for logging on to the ASO console from the deployment personnel or an administrator. When you log on to the ASO console for the first time, you must change the password of your username as prompted. To enhance security, a password must meet the following requirements: It must contain uppercase and lowercase letters. It must contain digits. It must contain special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). ng ASAPI It must be 10 to 20 characters in length.
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
9. In the Det ails dialog box, view the value of asapi.gat eway.endpoint . The value is the logon URL of
the Apsara ASAPI Management platform. ng ASAPI

### 2.5 Obtain the core package for ASAPI

Apsara Stack uses Apsara Stack API (ASAPI) as a unified portal for all Apsara Stack products that are connected to ASAPI. ASAPI also provides SDKs to call product APIs. For more information about how to obtain the core package for ASAPI, see Apsara Stack documentation.

### 2.6 Obtain an AccessKey pair

An AccessKey pair is composed of an AccessKey ID and an AccessKey secret. The AccessKey pair is used to implement symmetric encryption to verify the identity of the requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites Only operation administrators and level-1 organization administrators can obtain the AccessKey pair of an organization. Obtain the AccessKey of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the
icon on the right of the organization to be added.
5. Select AccessKey.
6. In the AccessKey message, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations: ng ASAPI
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey pair.
Not e The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

### 2.7 Query the region ID

You must specify the region ID when you call Apsara Stack SDK for Node.js. You must query the region ID in the Apsara Stack Cloud Management (ASCM) console. Procedure
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, you can view the region ID.

### 2.8 SDK for Java

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Java. Preparation You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use VPC SDK for Java. For more information about how to obtain and view your AccessKey pair in the ASCM console, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. The version of VPC SDK for Java is JDK 1.6 or later. Add the dependency Add the dependency to pom.xml: ng ASAPI

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>asapi</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/aliyun-java-sdk-asapi.jar</systemPath>
</dependency>
```

Use SDK for Java You can call ASAPI API operations by sending GET and POST requests. GET requests

```
 ASClient client = new ASClient();
// Form 1 String result = client.doGet(endpoint, parameters); // Form 2 String result = client.doRequest(endpoint, parameters);
```

POST requests

```java
public class DescribeVpcs {
    public static void main(String[] args) {
        // Set the endpoint of ASAPI.
        String endpoint = "http://xxx/asapi/v3";
    // Set request parameters.
    Map<String, String> parameters = new HashMap<String, String>();
    // Set product parameters.
    parameters.put("Product", "vpc");            //The product name, which must be the same a
s that displayed on the APIs page.
    parameters.put("Action", "DescribeVpcs");          // The API operation, which is case-se
nsitive and must be the same as that on the APIs page.
    parameters.put("Version", "2016-04-28");      // The API version.
    // Set authorization parameters.
    parameters.put("AccessKeyId", "<your-access-key-id>");          // The AccessKey ID of th
e authorized account.
    parameters.put("AccessKeySecret", "<your-access-key-secret>");  // The AccessKey secret o
f the authorized account.
    // Set service parameters.
    parameters.put("username", "<your-username>");                  // The username used to l
og on to the ASCM console.
    parameters.put("password", "<your-password>");                  // The password used to l
og on to the ASCM console.
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("RegionId", "cn-hangzhou-env12-d01");
    parameters.put("json", jsonObject.toJSONString());
    // Create an ASClient instance for initiating requests.
    ASClient client = new ASClient();
    // Add the request header.
    client.addHeader("x-acs-resourceGroupId", "112233");
    // Initiate the request and obtain the response.
    String result = client.doPost(endpoint, parameters);
```

ng ASAPI

### 2.9 SDK for Node.js

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Node.js. Preparation You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use VPC SDK for Node.js. For more information, see Obtain an AccessKey pair. You have obtained the endpoint of Apsara Stack API (ASAPI). For more information about how to obtain the endpoint of ASAPI, see Obtain the endpoint of Asapi. You have obtained the region ID. For more information about how to query the region ID, see Query the region ID. Add the dependency
1. Install SDK for Node.js.

```
 tnpm install --save @ali/asapi-nodejs-sdk
```

2. If mocha.opts depends on Egg.js, configure mocha.opts as follows:

```
--recursive --colors --timeout 60000 --reporter mochawesome --require co-mocha --require egg-ts-helper/register --require espower-typescript/guess --require intelli-espower-loader
```

Use SDK for Node.js The following example shows the three main steps of calling SDK for Node.js:
1. Create an ASClient instance. When you create an ASClient instance, set the region ID, endpoint,
AccessKey ID, and AccessKey secret in the config.ts file. Example:

```
local: {
    regionId: 'obtained region ID',
    API_GATEWAY: 'obtained endpoint',
    accessKeyId: 'your AccessKey ID',
    accessKeySecret: 'your AccessKey secret',
```

`},`
2. Create an API request and configure the parameters.
3. Initiate the request and handle the responses or exceptions.
ng ASAPI

```
// Set the endpoint of ASAPI. const API_GATEWAY = "http://xxxx/asapi/v3" // Create an RPC client. const asapiClient = ctx.service.sdk.rpcClient; // Set request parameters. let params = {
    Action: 'DescribeVpcs',
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

2.10. (Optional) Use POP SDK to call ASAPI API operations If an application used POP SDK to call Virtual Private Cloud (VPC), you must switch the gateway to Apsara Stack API (ASAPI). Procedure
1. Switch the gateway to ASAPI and add common parameters required by the API operation to the
request header.
2. Add the Product Name field to the request header.
The following code provides an example on how to use POP SDK to call VPC OpenAPI.

```java
try {
    DefaultProfile clientProfile = DefaultProfile.getProfile(regionId, accessKeyId, accessKeySe
cret);
    // Set the ASAPI gateway. Format: server.asapi.${intranet-domain}.
    clientProfile.addEndpoint(region, region, "vpc", "<ASAPI gateway>");
    DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
    DescribeVpcsRequest request = new DescribeVpcsRequest();
    request.setSysRegionId(regionId); // Or setRegionId(regionId)
    // Set common parameters based on the information about the current user.
    request.putHeaderParameter("x-acs-organizationid", "<Department ID>");
    request.putHeaderParameter("x-acs-resourcegroupid", "<Resource group ID>");
    DescribeVpcsResponse result = (DescribeVpcsResponse) acsClient.getAcsResponse(request);
    System.out.println(result);
} catch (Exception e) {
    e.printStackTrace();
```
