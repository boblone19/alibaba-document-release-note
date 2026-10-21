---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Virtual Private Cloud Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 488
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Virtual Private Cloud Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Virtual%20Private%20Cloud%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Virtual Private Cloud Developer Guide 20220928

## Table of Contents

- 1 Call VPC SDK by using ASAPI
  - 1.1 ASAPI Developer Guide
    - 1.1.1 ASAPI overview
    - 1.1.2 Preparations
      - 1.1.2.1 Log on to the API Tool console
      - 1.1.2.2 View information about API operations
      - 1.1.2.3 Generate an endpoint for the ASAPI
      - 1.1.2.4 Obtain Apsara Stack SDKs
      - 1.1.2.5 Obtain an AccessKey pair
      - 1.1.2.6 Query a region ID
    - 1.1.3 Common parameters
    - 1.1.4 SDK description
      - 1.1.4.1 Use Apsara Stack SDK for Java to call API operations
      - 1.1.4.2 Use Apsara Stack SDK for Python to call API operations
      - 1.1.4.3 Use Apsara Stack SDK for Node.js to call API operations
      - 1.1.4.4 SDK for POP
        - 1.1.4.4.1 SDK for Java
        - 1.1.4.4.2 SDK for Go
        - 1.1.4.4.3 SDK for Python
    - 1.1.5 HTTP requests
      - 1.1.5.1 Overview
      - 1.1.5.2 Request syntax
      - 1.1.5.3 Request signatures
      - 1.1.5.4 Response
- 2 API reference
  - 2.1 API reference
    - 2.1.1 List of operations by function
    - 2.1.2 Call VPC APIs
      - 2.1.2.1 Request syntax
      - 2.1.2.2 API authorization
      - 2.1.2.3 Request signatures
    - 2.1.3 RAM authentication
    - 2.1.4 Common parameters
    - 2.1.5 VPC
      - 2.1.5.1 CreateVpc
      - 2.1.5.2 DeleteVpc
      - 2.1.5.3 ModifyVpcAttribute
      - 2.1.5.4 DescribeVpcAttribute
      - 2.1.5.5 AssociateVpcCidrBlock
      - 2.1.5.6 UnassociateVpcCidrBlock
    - 2.1.6 vSwitch
      - 2.1.6.1 CreateVSwitch
      - 2.1.6.2 DeleteVSwitch
      - 2.1.6.3 ModifyVSwitchAttribute
      - 2.1.6.4 DescribeVSwitchAttributes
    - 2.1.7 vRouter
      - 2.1.7.1 ModifyVRouterAttribute
      - 2.1.7.2 DescribeVRouters
    - 2.1.8 Route table
      - 2.1.8.1 CreateRouteTable
      - 2.1.8.2 CreateRouteEntry
      - 2.1.8.3 DeleteRouteEntry
      - 2.1.8.4 DescribeRouteEntryList
      - 2.1.8.5 ModifyRouteEntry
      - 2.1.8.6 AssociateRouteTable
      - 2.1.8.7 DeleteRouteTable
      - 2.1.8.8 DescribeRouteTableList
      - 2.1.8.9 UnassociateRouteTable
    - 2.1.9 Region
      - 2.1.9.1 DescribeRegions
      - 2.1.9.2 DescribeZones
    - 2.1.10 Tag
      - 2.1.10.1 TagResources
      - 2.1.10.2 ListTagResources
      - 2.1.10.3 UnTagResources
    - 2.1.11 BGP
      - 2.1.11.1 DescribeBgpGroups
      - 2.1.11.2 ModifyBgpGroupAttribute
      - 2.1.11.3 DeleteBgpGroup
      - 2.1.11.4 DescribeBgpPeers
      - 2.1.11.5 DeleteBgpPeer
      - 2.1.11.6 AddBgpNetwork
      - 2.1.11.7 DeleteBgpNetwork
      - 2.1.11.8 DescribeBgpNetworks
    - 2.1.12 VBR
      - 2.1.12.1 CreateVirtualBorderRouter
      - 2.1.12.2 DeleteVirtualBorderRouter
      - 2.1.12.3 DescribeVirtualBorderRouters
      - 2.1.12.4 TerminateVirtualBorderRouter
      - 2.1.12.5 RecoverVirtualBorderRouter
      - 2.1.12.6 UnassociatePhysicalConnectionFromVirtualBorderRouter
    - 2.1.13 Physical connections
      - 2.1.13.1 CancelPhysicalConnection
      - 2.1.13.2 DescribePhysicalConnections
      - 2.1.13.3 ModifyPhysicalConnectionAttribute
      - 2.1.13.4 TerminatePhysicalConnection
      - 2.1.13.5 EnablePhysicalConnection
      - 2.1.13.6 DeletePhysicalConnection
      - 2.1.13.7 CreatePhysicalConnectionOccupancyOrder
      - 2.1.13.8 ApplyPhysicalConnectionLOA
      - 2.1.13.9 CreatePhysicalConnectionSetupOrder
      - 2.1.13.10 CompletePhysicalConnectionLOA
      - 2.1.13.11 DescribePhysicalConnectionLOA
    - 2.1.14 VPN gateways
      - 2.1.14.1 VPN gateway
        - 2.1.14.1.1 CreateVpnGateway
        - 2.1.14.1.2 DescribeVpnGateways
        - 2.1.14.1.3 DescribeVpnGateway
        - 2.1.14.1.4 DeleteVpnGateway
        - 2.1.14.1.5 ModifyVpnGatewayAttribute
      - 2.1.14.2 Customer gateway
        - 2.1.14.2.1 CreateCustomerGateway
        - 2.1.14.2.2 DescribeCustomerGateways
        - 2.1.14.2.3 DescribeCustomerGateway
        - 2.1.14.2.4 DeleteCustomerGateway
        - 2.1.14.2.5 ModifyCustomerGatewayAttribute
      - 2.1.14.3 Routes for VPN gateways
        - 2.1.14.3.1 DeleteVpnPbrRouteEntry
        - 2.1.14.3.2 DeleteVpnRouteEntry
        - 2.1.14.3.3 DescribeVpnRouteEntries
        - 2.1.14.3.4 ModifyVpnRouteEntryWeight
        - 2.1.14.3.5 CreateVpnRouteEntry
        - 2.1.14.3.6 ModifyVpnPbrRouteEntryWeight
        - 2.1.14.3.7 DescribeVpnPbrRouteEntries
        - 2.1.14.3.8 PublishVpnRouteEntry
        - 2.1.14.3.9 CreateVpnPbrRouteEntry
      - 2.1.14.4 IPsec-VPN
        - 2.1.14.4.1 DescribeVpnConnection
        - 2.1.14.4.2 DeleteVpnConnection
        - 2.1.14.4.3 DownloadVpnConnectionConfig
        - 2.1.14.4.4 CreateVpnConnection
        - 2.1.14.4.5 DescribeVpnConnections
        - 2.1.14.4.6 ModifyVpnConnectionAttribute
      - 2.1.14.5 SSL-VPN
        - 2.1.14.5.1 CreateSslVpnServer
        - 2.1.14.5.2 DeleteSslVpnServer
        - 2.1.14.5.3 ModifySslVpnServer
        - 2.1.14.5.4 DeleteSslVpnClientCert
        - 2.1.14.5.5 ModifySslVpnClientCert
        - 2.1.14.5.6 CreateSslVpnClientCert
        - 2.1.14.5.7 DescribeSslVpnClientCerts
        - 2.1.14.5.8 DescribeSslVpnClientCert
        - 2.1.14.5.9 DescribeSslVpnServers
        - 2.1.14.5.10 DescribeVpnSslServerLogs
    - 2.1.15 NAT gateways
      - 2.1.15.1 ModifyNatGatewayAttribute
      - 2.1.15.2 ModifyNatGatewaySpec
      - 2.1.15.3 DeleteNatGateway
      - 2.1.15.4 CreateForwardEntry
      - 2.1.15.5 DescribeForwardTableEntries
      - 2.1.15.6 ModifyForwardEntry
      - 2.1.15.7 DeleteForwardEntry
      - 2.1.15.8 CreateSnatEntry
      - 2.1.15.9 DescribeSnatTableEntries
      - 2.1.15.10 ModifySnatEntry
      - 2.1.15.11 DeleteSnatEntry
      - 2.1.15.12 ModifyBandwidthPackageSpec
      - 2.1.15.13 DeleteBandwidthPackage
      - 2.1.15.14 CreateBandwidthPackage
      - 2.1.15.15 DescribeBandwidthPackages
      - 2.1.15.16 ModifyBandwidthPackageAttribute
      - 2.1.15.17 AddBandwidthPackageIps
    - 2.1.16 Elastic IP addresses
      - 2.1.16.1 AllocateEipAddress
      - 2.1.16.2 AllocateEipAddressPro
      - 2.1.16.3 AssociateEipAddress
      - 2.1.16.4 ModifyEipAddressAttribute
      - 2.1.16.5 UnassociateEipAddress
      - 2.1.16.6 ReleaseEipAddress
      - 2.1.16.7 DescribeEipGatewayInfo
    - 2.1.17 HAVIPs
      - 2.1.17.1 CreateHaVip
      - 2.1.17.2 DescribeHaVips
      - 2.1.17.3 ModifyHaVipAttribute
      - 2.1.17.4 AssociateHaVip
      - 2.1.17.5 UnassociateHaVip
      - 2.1.17.6 DeleteHaVip
    - 2.1.18 ACLs
      - 2.1.18.1 CreateNetworkAcl
      - 2.1.18.2 AssociateNetworkAcl
      - 2.1.18.3 ModifyNetworkAclAttributes
      - 2.1.18.4 UpdateNetworkAclEntries
      - 2.1.18.5 UnassociateNetworkAcl
      - 2.1.18.6 CopyNetworkAclEntries
      - 2.1.18.7 DeleteNetworkAcl
      - 2.1.18.8 DescribeNetworkAcls
      - 2.1.18.9 DescribeNetworkAclAttributes
    - 2.1.19 IPv6 gateways
      - 2.1.19.1 CreateIpv6Gateway
      - 2.1.19.2 DeleteIpv6Gateway
      - 2.1.19.3 DescribeIpv6Gateways
      - 2.1.19.4 ModifyIpv6GatewaySpec
      - 2.1.19.5 DescribeIpv6EgressOnlyRules
      - 2.1.19.6 CreateIpv6EgressOnlyRule
      - 2.1.19.7 DeleteIpv6EgressOnlyRule
      - 2.1.19.8 DeleteIpv6InternetBandwidth
      - 2.1.19.9 DescribeIpv6GatewayAttribute
      - 2.1.19.10 DescribeIpv6Addresses
      - 2.1.19.11 ModifyIpv6InternetBandwidth
      - 2.1.19.12 AllocateIpv6InternetBandwidth
      - 2.1.19.13 ModifyIpv6AddressAttribute
      - 2.1.19.14 ModifyIpv6GatewayAttribute

ng ASAPI

## 1 Call VPC SDK by using ASAPI

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, ng ASAPI specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. ng ASAPI Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click Log On.
4. In the top navigation bar, choose Product s > Ot hers > API T ool.

##### 1.1.2.2 View information about API operations

This topic describes how to view information about API operations. Before you use SDKs, obtain service names, API operation names, and API operation versions. Context The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails. Procedure
1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click API Direct ory.
3. On the API Direct ory page, select the desired service from the drop-down list, enter a keyword of
an API operation name in the search box, and then click the search icon.
4. Then, you can view the service name, API operation name, and API operation version.

##### 1.1.2.3 Generate an endpoint for the ASAPI

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). ng ASAPI Method 1: Use Registration Vars of Services to generate an endpoint
1. Log on to Apsara Infrastructure Management Framework.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
2. In the left-side navigation pane, click Report s.
3. On the All Report s page, search for `Registration Vars of Services` and click the report name.
4. On the Regist rat ion Vars of Services page, click the
icon next to Service and search for `asapi` .
5. Find the asapi service, right-click in the Service Regist rat ion column, and then select Show More
from the shortcut menu. In the Det ails dialog box, obtain the value of asapi.public.endpoint .
6. Generate an endpoint for the ASAPI based on the following format:

```
https://<asapi.public.endpoint>/asapi/v3
```

Method 2: Use cluster resources to generate an endpoint
1. Log on to Apsara Infrastructure Management Framework.
ng ASAPI i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
2. Go to the cluster operations page.
i. In the left-side navigation pane, choose Operations > Cluster Operations. ii. In the Clust er search box, enter `ascm` . iii. Find the cluster that you want to manage and click Operat ions in the Act ions column.
3. Obtain the value of the domain parameter.
i. Click the Cluster Resources tab. ii. In the Name field, search for `asapi_dns_public` . iii. Click Det ails in the Applicat ion Paramet er column. In the Applicat ion Paramet er message, obtain the value of the domain parameter.
4. Generate an endpoint for the ASAPI based on the following format:

```
https://<domain>/asapi/v3
```

Method 3: Concatenate strings to generate an endpoint You can also concatenate strings to generate an endpoint based on the following format:

```
https://public.asapi.<region>.<internet-domain>/asapi/v3
```

Not e
1. Replace <region> with your actual region ID. For information about how to query a region ID,
see Query a region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain the
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: ng ASAPI

```
https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3
```

##### 1.1.2.4 Obtain Apsara Stack SDKs

The Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use the ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls. For more information about how to obtain Apsara Stack SDKs, see Apsara Stack documentation.

##### 1.1.2.5 Obtain an AccessKey pair

An AccessKey pair that consists of an AccessKey ID and an AccessKey secret is used to implement symmetric encryption. This helps you verify the identity of a requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. This topic describes how to obtain an AccessKey pair. Prerequisites An account of the operations administrator or the level-1 organization administrator is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair. Context If you need to make API calls to the Apsara Uni-manager Management Console or other Apsara Stack services, we recommend that you use the AccessKey pair of a personal account. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, for example, cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance to which you make API calls. If you need to make API calls to an Elastic Compute Service (ECS) instance, obtain the ID of the ECS instance on the Instances page. |

ng ASAPI

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

Obtain the AccessKey pair of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, obtain the AccessKey pair.
Not e The AccessKey pair that consists of an AccessKey ID and an AccessKey secret is the credential for you to have full permissions on Apsara Stack resources. Keep your AccessKey pair confidential. Obtain the AccessKey pair of an account that has permissions on an organization To obtain the AccessKey pair of an account that has permissions on an organization, perform the following operations:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations navigation tree, click the name of the organization that you want to manage.
5. On the right side of the page, click Obt ain AccessKey Pair.
6. In the message that appears, obtain the AccessKey pair of the account that has permissions on the
organization. Not e The system automatically allocates an AccessKey pair to the account that has permissions on the level-1 organization. The same AccessKey pair is used by the accounts that have permissions on the subordinate organizations.

##### 1.1.2.6 Query a region ID

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure ng ASAPI
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click User
Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section, view the region ID.

#### 1.1.3 Common parameters

Common request parameters must be included in all API requests. Sample common parameters The following table describes the common parameters that are used when you call API operations supported by the Apsara Stack API (ASAPI).

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. For more information, see View information about API operations. |
| Product | String | Yes | The name of the service. |
| Version | String | Yes | The version of the API operation. For more information, see View information about API operations. |
| RegionId | String | Yes | The ID of the region. For more information, see Query a region ID. |
| AccessKeyId | String | Yes | The AccessKey ID used to connect to the service. For more information, see Obtain an AccessKey pair. |

ng ASAPI

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

ng ASAPI Not e

```
The Signature , SignatureMethod , SignatureVersion , SignatureNonce , Timestamp ,
```

and `Format` parameters are encapsulated into Apsara Stack SDK. You do not need to configure these parameters.

#### 1.1.4 SDK description

##### 1.1.4.1 Use Apsara Stack SDK for Java to call API operations

operations This topic describes how to obtain and use Apsara Stack SDK for Java to call API operations. Prerequisites An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of the Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for the ASAPI. Apsara Stack SDK for Java 1.8 or later is installed. Background information The help center of Apsara Stack provides Maven dependencies and JAR files for Apsara Stack SDK for Java. You can write code to use Apsara Stack SDK for Java to call API operations. In this example, the Windows 10 64-bit OS and IntelliJ IDEA are used. Procedure
1. Use one of the following methods to configure Maven in IntelliJ IDEA. Maven is a tool used for
project management. Use Maven that is integrated in IntelliJ IDEA. Download Maven based on the OS that you are using from the official website and configure Maven. For more information, see Download Maven.
2. Obtain the Maven dependencies for Apsara Stack SDK for Java from the official website. For more
information about how to obtain the dependencies, see Obtain the core package for ASAPI.
3. Use one of the following methods to create a Maven project:
Method 1: Create a Maven project in IntelliJ IDEA. ng ASAPI Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure. ng ASAPI
5. Add the dependencies of Apsara Stack SDK for Java to the pom.xml file in the project directory.

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>asapi</artifactId>
        <version>1.0.6-RELEASE</version>
        <scope>system</scope>
        <systemPath>${project.basedir}/libs/asapi-1.0.6-RELEASE.jar</systemPath>
    </dependency>
  <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>alicrypto-java-aliyun</artifactId>
    <version>1.0.4</version>
    <systemPath>${project.basedir}/libs/alicrypto-java-aliyun-1.0.4.jar</systemPath>
  </dependency>
  <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>gmsse</artifactId>
    <version>1.1.0</version>
    <systemPath>${project.basedir}/libs/gmsse-1.1.0.jar</systemPath>
  </dependency>
</dependencies>
```

Not e Replace `1.0.6-RELEASE` with the actual version of Apsara Stack SDK for Java.
6. On the right side of IntelliJ IDEA, view information in the Maven section.
ng ASAPI If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations: ng ASAPI

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers ng ASAPI

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query the region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-inst anceid | The ID of the instance to which you make API calls. |

##### 1.1.4.2 Use Apsara Stack SDK for Python to call API operations

operations This topic describes how to use Apsara Stack SDK for Python to call API operations provided by the Apsara Stack API (ASAPI). Preparations An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of the ASAPI is obtained. For more information, see Generate an endpoint for the ASAPI. Install Apsara Stack SDK for Python
1. Download the required version of Apsara Stack SDK for Python. For more information, see Obtain
Apsara Stack SDKs.
2. Upload the compressed file of Apsara Stack SDK for Python to the host from which you want to
send API requests and extract the file. Then, run the following code in the directory of the extracted files to install Apsara Stack SDK for Python:

```bash
# Install Apsara Stack SDK for Python 2.x.
pip install aliyun-python2-sdk-asapi-2.4.7.tar.gz
# Install Apsara Stack SDK for Python 3.x.
pip3 install aliyun-python3-sdk-asapi-2.4.7.tar.gz
```

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI. ng ASAPI

```python
   # 1. Import dependencies.
   from aliyunsdkasapi.ASClient import ASClient
   from aliyunsdkasapi.AsapiRequest import AsapiRequest
   if __name__ == '__main__':
    # 2. Create a request. The Product parameter specifies the name of the service. The Ver
sion parameter specifies the version of the API operation. The Action parameter specifies t he operation that you want to perform. The asapi-endpoint parameter specifies the endpoint of the ASAPI.
    req = AsapiRequest("<Product>", "<Version>", "<Action>", "<asapi-endpoint>")
    # 3. Configure operation-specific parameters.
    req.add_body_params("<key>", "<value>")
    # 4. Configure request headers.
    req.add_header("x-acs-resourcegroupid", "<your-resourcegroupid>");
    req.add_header("x-acs-organizationid", "<your-organizationid>");
    req.add_header("x-acs-regionid", "<your-regionid>");
    req.add_header("x-acs-instanceid", "<your-instanceid>");
    # 5. Configure a request method.
    req.set_method("POST")
    # 6. Configure initialization parameters for an ASClient object. The parameter values v
ary based on your environment. The timeout parameter specifies the time-out period for a re quest. The cert_file parameter specifies the certificate. The verify parameter specifies wh ether to verify the certificate.
    as_client = ASClient("<accesskeyid>", "<accesskeysecret>", "<regionid>",timeout=1000,
            cert_file=None,
            verify=False)
    # Configure the identifier of the requester. This parameter is required and used only f
or identification. You can set this parameter to a random value.
    as_client.setSdkSource("<The identifier of the requester>")
    response = as_client.do_request(req)
    print(response)
```

Request headers

| Paramet er | Descript ion |
|---|---|
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query a region ID. |
| x-acs-instanceid | The ID of the instance to which you make API calls. |

ng ASAPI Configure a proxy Perform the following steps to configure a proxy:
1. Import OS dependencies.

```java
import os
```

2. Configure one or more proxies.

```bash
# Before you make an API call, configure one or more proxies.
os.environ['http_proxy'] = "http://x.x.x.x:xxxx" os.environ['https_proxy'] = "https://x.x.x.x:xxxx"
```

##### 1.1.4.3 Use Apsara Stack SDK for Node.js to call API operations

operations This topic describes how to obtain and use Apsara Stack SDK for Node.js to call API operations. Preparations An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information about how to obtain an AccessKey pair in the Apsara Uni-manager Management Console, see Obtain an AccessKey pair. The endpoint of the Apsara Stack API (ASAPI) is obtained. For more information, see Generate an endpoint for the ASAPI. A region ID is obtained. For more information about how to obtain a region ID, see Query the region ID. Add dependencies Run the following command to install Apsara Stack SDK for Node.js:

```
tnpm install --save @ali/asapi-nodejs-sdk
```

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls: ng ASAPI

```
// 1. Import the dependencies of Apsara Stack SDK for Node.js. const Controller = require('egg').Controller; const ASAPIClient = require('@ali/asapi-nodejs-sdk'); // 2. Configure the parameters. const cnofig = {
    API_GATEWAY: '<The endpoint of the ASAPI>',
    regionId: '<The ID of the region in which the Apsara Stack service is deployed>',
    accessKeyId: '<The AccessKey ID of your Apsara Stack tenant account>',
    accessKeySecret: '<The AccessKey secret of your Apsara Stack tenant account>'
```

};

```json
// 3. Initialize a client for API calls. const AsapiClient = new ASAPIClient(cnofig, this.ctx); // 4. Configure request parameters. const params = {
    "Action": "<The name of the API operation>",
    "Product": "<The name of the service that provides the API operation>",
    "Version": "<The version of the API operation>",
    "regionId": '<The ID of the region in which the Apsara Stack service is deployed>',
      "<The name of the operation-specific parameter required by the API operation>": "<The
value of the operation-specific parameter>"
```

`}`

```
// 5. Configure request headers. AsapiClient.addHeader('x-acs-caller-sdk-source', '<The identifier of the requester>') AsapiClient.addHeader('x-acs-roleid', '<The ID of the role>') AsapiClient.addHeader('x-acs-userid', '<The ID of the user>') AsapiClient.addHeader('x-acs-organizationid', '<your-organizationid>') AsapiClient.addHeadert("x-acs-regionid", "<your-regionid>"); AsapiClient.addHeader("x-acs-resourcegroupid", "<your-resourcegroupid>"); AsapiClient.addHeader("x-acs-instanceid", "<your-instanceid>"); // 6. Make an API call and obtain the response. try {
  const res = await AsapiClient.doRequest(cnofig.API_GATEWAY, params, {
    method: 'POST', // The request method.
    formatParams: false, // Specifies whether to format parameters and capitalize the first
letter of each parameter.
    enableProxy: true, // Specifies whether to configure a proxy.
    proxy: 'http://x.x.x.x:xxxx',
    timeout: 10000, // The time-out period.
  // ca: , // The certificate issued by a certificate authority (CA). For more information,
visit https://nodejs.org/api/https.html#https_https_request_options_callback.
```

`})`

```
  console.log(res)
} catch (e) {
  console.log(e)
```

`}` Disable certificate validation The following sample code shows how to disable certificate validation:

```
Configure the environment variable. NODE_TLS_REJECT_UNAUTHORIZED=0
```

ng ASAPI Request headers

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Query the region ID. |
| x-acs-organizat ionid | The ID of the organization in the Apsara Uni- manager Management Console. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. |
| x-acs-inst anceid | The ID of the instance to which you make API calls. |
| x-acs-caller-sdk-source | The custom name of the requester or the system. This parameter is used to identify the source of the API request. |
| x-acs-roleid | The ID of the role. |
| x-acs-userid | The ID of the user. |

##### 1.1.4.4 SDK for POP

###### 1.1.4.4.1 SDK for Java

Before you use Apsara Stack API (ASAPI) SDK for POP for Java to access ASAPI, you must know the remote procedure call (RPC) and resource-oriented architecture (ROA) styles that are supported for API calls. ASAPI is compatible with both styles. Their difference lies in the ASAPI endpoints that are used for API calls. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. SSL certificate validation is ignored for requests over HTTPS. Background information ASAPI supports only the HTTPS request protocol. Difference between two styles When you use the RPC or ROA style to make API calls, take note that the two styles use different ASAPI endpoints.

```bash
# ASAPI endpoint for the RPC style:
public.asapi.<global:region>.<global:internet-domain>/asapi/v3
# ASAPI endpoint for the ROA style:
public.asapi.<global:region>.<global:internet-domain>/asapi/v3/roa
```

ng ASAPI Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
package com.aliyuns.client.pop.ecs; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.ecs.model.v20140526.DescribeInstancesRequest; import com.aliyuncs.ecs.model.v20140526.DescribeInstancesResponse; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import java.util.List; public class DescribeInstancesTest {
    public static void main(String[] args) {
        // Specify the endpoint of ASAPI.
        String endpoint = "public.asapi.<global:region>.<global:internet-domain>/asapi/v3";
        // Specify the region where the ECS service resides.
        String region = "<global:region>";
        // Specify the name of the service that you want to access.
        String product = "ECS";
        // Specify your AccessKey pair.
        String ak = "<accessKeyId>";
        String sk = "<accessKeySecret>";
        try {
            DefaultProfile clientProfile = DefaultProfile.getProfile(region, ak, sk);
            // Ignore SSL certificate validation.
            HttpClientConfig clientConfig = HttpClientConfig.getDefault();
            clientConfig.setIgnoreSSLCerts(true);
            // Set the connection timeout period.
            clientConfig.setConnectionTimeoutMillis(3000L);
            // Set the read timeout period.
            clientConfig.setReadTimeoutMillis(10000L);
            clientProfile.setHttpClientConfig(clientConfig);
            // Create a connection.
            DefaultAcsClient acsClient = new DefaultAcsClient(clientProfile);
            // Create a request.
            DescribeInstancesRequest request = new DescribeInstancesRequest();
            // Specify the endpoint of ASAPI.
            request.setSysEndpoint(endpoint);
            // Specify the name of the service that you want to access and the region where
the service resides.
            request.setSysLocationProduct(product);
            request.setSysRegionId(region);
            // Set the request protocol to HTTPS.
            request.setSysProtocol(ProtocolType.HTTPS);
            DescribeInstancesResponse result =  acsClient.getAcsResponse(request);
            List<DescribeInstancesResponse.Instance> instances = result.getInstances();
            for (DescribeInstancesResponse.Instance instance: instances) {
```

ng ASAPI

```java
                System.out.println(instance.getInstanceId());
                System.out.println(instance.getInstanceName());
```

`}`

```
        } catch (Exception e) {
            e.printStackTrace();
```

`}` `}` `}` The following sample code provides an example on how to use the ROA style to make an API call. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016- 06-07. Sample code:

```java
package com.aliyuns.client.pop.cr; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceListTest {
    public static void main(String[] args) {
        // Specify the endpoint of ASAPI.
        String endpoint = "public.asapi.<global:region>.<global:internet-domain>/asapi/v3/r
oa";
        // Specify the region where the Container Registry service resides.
        String region = "<global:region>";
        // Specify the name of the service that you want to access.
        String product = "cr";
        // Specify your AccessKey pair.
        String ak = "<accessKeyId>";
        String sk = "<accessKeySecret>";
        DefaultProfile profile = DefaultProfile.getProfile(region, ak, sk);
        // Ignore SSL certificate validation.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        // Set the connection timeout period.
        clientConfig.setConnectionTimeoutMillis(3000L);
        // Set the read timeout period.
        clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        // Create a connection for the client.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create a request.
```

ng ASAPI

```java
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTPS);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of ASAPI.
        request.setSysDomain(endpoint);
        // Specify the version of the API.
        request.setSysVersion("2016-06-07");
        // Specify the pattern of the uniform resource identifier (URI).
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where the
service resides.
        request.setSysLocationProduct(product);
        request.putHeadParameter("Content-Type", "application/json");
        String requestBody = "" +
                "{}";
        request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
```

`}` `}` `}` Not ice If you send a request over HTTPS, you must enable the request to ignore SSL certificate validation.

###### 1.1.4.4.2 SDK for Go

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. ng ASAPI Sample code:

```java
package main import (
 "fmt"
 "time"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses"
```

`)`

```
func getSdkConfig() *sdk.Config {
 return sdk.NewConfig().
  WithTimeout(time.Duration(30) * time.Second).
  WithEnableAsync(true).
  WithGoRoutinePoolSize(100).
  WithMaxTaskQueueSize(10000).
  WithDebug(false).
  WithScheme("HTTP")
```

`}`

```
func main(){
 ak := "<The AccessKey ID of your Apsara Stack tenant account.>"
 sk := "<The AccessKey secret of your Apsara Stack tenant account.>"
 regionId := "<The region where the ECS service resides.>"
 endpoint := "<The endpoint of ASAPI.>" // No network protocol.
 request := requests.NewCommonRequest()
  request.SetReadTimeout(10 * time.Second) // Set the read timeout period of the request to
10 seconds.
  request.SetConnectTimeout(5 * time.Second)  // Set the connection timeout period of the r
equest to 5 seconds.
 request.Method = requests.GET
 request.Domain = endpoint         // Location Service will not be enabled if the host is s
pecified. For example, the service with a certification type-bearer token must be specified
```

`.`

```
 request.Version = "2014-05-26"            // Specify the version of the API.
 request.Scheme = "https"                // Specify the request protocol. Default value: ht
tp.
 request.ApiName = "DescribeInstances"
 request.QueryParams["Product"] = "Ecs"  // Specify the name of the service that you want t
o access.
 request.TransToAcsRequest()
 client, err := sdk.NewClientWithOptions(regionId,getSdkConfig(),credentials.NewAccessKeyCr
edential(ak,sk))
 // If relevant parameters are not set for the request, the client settings are used.
  //client.SetReadTimeout(10 * time.Second)              // Set the read timeout period of
the client to 10 seconds.
 //client.SetConnectTimeout(5 * time.Second)            // Set the connection timeout perio
d of the client to 5 seconds.
  resp := responses.BaseResponse{}
  err = client.DoAction(request, &resp)
```

`if` !

```
il{
```

ng ASAPI

```
    if err != nil {
        panic(err)
```

`}`

```
 fmt.Print(endpoint)
```

`}` Configure proxies You can configure proxies in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY and HTTPS_PROXY environment variables, or set the NO_PROXY environment variable. Sample code:

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment variabl
```

`e.`

```
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment vari
able.
```

`}` Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are conf igured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

###### 1.1.4.4.3 SDK for Python

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. ng ASAPI Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

```java
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest import os
# Create an AcsClient instance.
client = AcsClient(
   "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>",
   timeout=1000,  # Set the timeout period.
    verify=False, # Ignore certificate validation. or verify='<The location where the certi
ficate is stored.>'
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def hello_ecs_instance():
    # Create a request and set the parameters.
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    params = {"PageNumber":"1", "Product":"Ecs","Version": "2014-05-26","Action": "Describe
Instances"};
    request.set_body_params(params)
    # The endpoint that contains no network protocol is in the following format: ASAPI doma
in name/asapi/v3.
    request.set_endpoint('<The endpoint of ASAPI.>')
    # Set the following parameter if the endpoint contains no network protocol:
    request.set_protocol_type("https")
    request.set_PageSize(10)
    # Initiate the API request and obtain the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
```

Configure proxies ng ASAPI Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

#### 1.1.5 HTTP requests

##### 1.1.5.1 Overview

This topic describes how to make API requests and is intended for users who use API URLs to initiate HTTP GET requests. If you are using an SDK to initiate requests, you can skip this topic. The request URL consists of different parameters and has a fixed syntax. The URL contains common request parameters, your signature, and operation-specific parameters. Sample request URLs are provided for each API operation. These URLs are not encoded to make them easy to read. Before you make a request, you must encode the request URL. After the authentication process is complete based on your signature, the results are returned to you. Response parameters are returned if the call is successful, whereas an error message is returned if the call fails. You can troubleshoot issues based on the error message.

##### 1.1.5.2 Request syntax

The Apsara Stack API (ASAPI) allows you to call API operations by sending HTTP GET requests based on URLs. Each URL must include request parameters. This topic describes the syntax of HTTP GET requests and provides the endpoint of the ASAPI. Sample request GetOrganizationList is used in the following unencoded URL request:

```
https://public.asapi.aliyuns.com/asapi/v3?Action=GetOrganizationList&Product=ascm&Version=2 019-05-10&Id=<Organization ID>&<Common parameters>
```

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. ng ASAPI Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. ng ASAPI Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException
```

`{`

```
    return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").rep
lace("*", "%2A").replace("%7E", "~") : null;
```

`}`
3. Use equal signs ( `=` ) to connect the encoded request parameters and their values.
4. Use ampersands ( `&` ) to connect the encoded request parameters. These parameters must be
arranged in the same order as those in Step 1. Then, a canonicalized query string that follows the request structure is obtained. For more information, see Request structure. Step 2: Create a string-to-sign
1. Create a `string-to-sign` . You can also use `percentEncode` to encode the canonicalized query
string created in Step 1 based on the following rules:

```
StringToSign=
    HTTPMethod + "&" + //HTTPMethod: the HTTP method that is used to send a request, su
ch as GET.
    percentEncode("/") + "&" + //percentEncode("/"): Encode the forward slash (/) in UT
F-8 as %2F.
    percentEncode(CanonicalizedQueryString) // Encode the canonicalized query string cr
eated in Step 1.
```

2. Calculate the RFC 2104-compliant HMAC-SHA1 or HMAC-256 value of `StringToSign` . In the
following example, Java Base64 is used:

```
String signature = Base64.getEncoder().encodeToString(signData);
```

ng ASAPI Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
3. Encode the `Signature` parameter based on RFC 3986 and add it to the canonicalized query
string. Example 1: Concat enat e paramet ers `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid and `AccessKeySecret` is set to testsecret. Perform the following operations:
1. Construct a canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

2. Create a `string-to-sign` .

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DGetOrganizationList%26Format%3DJSON%26Id%3D1%26 Product%3Dascm%26RegionId%3Dcn-region-test%26SignatureMethod%3DHMAC-SHA1%26SignatureNon ce%3D43967c6e-e3ad-44fa-b06b-fcf3db5f39d2%26SignatureVersion%3D1.0%26Timestamp%3D2020-0 9-15T08%253A50%253A40Z%26Version%3D2019-05-10
```

3. Calculate the signature.
Calculate the signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is set to testsecret. The calculated signature is `OLeaidS1JvxuMvnyHOwuJ+uX5qY=` . Java Base64 is used in the following sample code:

```
 String signature = Base64.getEncoder().encodeToString(signData);  Encode
```

`Signature=hvqv9Ll5RE6kQ4YsQXFAf9VuRIY=` based on RFC 3986 and add it to the canonicalized query string.

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language ng ASAPI `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
1. Predefine an encoding method.

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException {
        return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").r
eplace("*", "%2A").replace("%7E", "~") : null;
```

`}`
2. Predefine the time format for the `Timestamp` parameter. Specify the `Timestamp` parameter in
the ISO 8601 format. The time must be in UTC+0.

```java
private static final String ISO8601_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"; private static String formatIso8601Date(Date date) {
    SimpleDateFormat df = new SimpleDateFormat(ISO8601_DATE_FORMAT);
    df.setTimeZone(new SimpleTimeZone(0, "GMT"));
    return df.format(date);
```

`}`
3. Create a request string.
ng ASAPI

```
final String HTTP_METHOD = "GET"; Map parameters = new HashMap(); // Specify request parameters. parameters.put("Product", "ascm"); parameters.put("Action", "GetOrganizationList"); parameters.put("Version", "2019-05-10"); parameters.put("AccessKeyId", "testid"); parameters.put("RegionId", "cn-region-test"); parameters.put("Timestamp", formatIso8601Date(new Date())); parameters.put("SignatureMethod", "HMAC-SHA1"); parameters.put("SignatureVersion", "1.0"); parameters.put("SignatureNonce", UUID.randomUUID().toString()); parameters.put("Format", "JSON"); parameters.put("Id", "1"); // Arrange request parameters. String[] sortedKeys = parameters.keySet().toArray(new String[]{}); Arrays.sort(sortedKeys); final String SEPARATOR = "&"; // Create a string-to-sign. StringBuilder stringToSign = new StringBuilder(); stringToSign.append(HTTP_METHOD).append(SEPARATOR); stringToSign.append(percentEncode("/")).append(SEPARATOR); StringBuilder canonicalizedQueryString = new StringBuilder(); for(String key : sortedKeys) {
    // Encode the key and the value.
    canonicalizedQueryString.append("&")
    .append(percentEncode(key)).append("=")
    .append(percentEncode(parameters.get(key)));
```

`}`

```
//Encode the canonicalized query string. stringToSign.append(percentEncode( canonicalizedQueryString.toString().substring(1)));
```

4. The signature. The key value used for calculation is `testsecret&` because `AccessKeySecret` is
set to testsecret. The calculated signature is OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D .

```
// The following sample code shows how to calculate the signature: final String ALGORITHM = "HmacSHA1"; final String ENCODING = "UTF-8"; key = "testsecret&"; Mac mac = Mac.getInstance(ALGORITHM); mac.init(new SecretKeySpec(key.getBytes(ENCODING), ALGORITHM)); byte[] signData = mac.doFinal(stringToSign.getBytes(ENCODING)); String signature = Base64.getEncoder().encodeToString(signData);
```

Encode the Signature parameter based on RFC 3986 and add it to the canonicalized query string. The following URL is obtained:

```
https://public.asapi.aliyuns.com/asapi/v3/?AccessKeyId=testid&Action=GetOrganizationLis t&Format=JSON&Id=1&Product=ascm&RegionId=cn-region-test&SignatureMethod=HMAC-SHA1&Signa tureNonce=43967c6e-e3ad-44fa-b06b-fcf3db5f39d2&SignatureVersion=1.0&Timestamp=2020-09-1 5T08%3A50%3A40Z&Version=2019-05-10
```

ng ASAPI
5. Use browsers or tools such as cURL and Wget to initiate an HTTP request.

##### 1.1.5.4 Response

Responses are returned only in the JSON format. If a return code is greater than or equal to 200 and less than 300, a success response is returned. Otherwise, an error response is returned. Sample success response If a request is successful, the request ID and operation-specific parameter values are returned. For more information, see the developer guide of the corresponding Apsara Stack service. `{`

```json
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": true,
    "RequestId": "xxxxxxxxxx",
    "Regions": { // The regions returned after you call the DescribeRegions operation.
        "Region": [
```

`{`

```json
                "RegionId": "",
                "RegionEndpoint": "",
                "LocalName": ""
```

`}` `]` `}` `}` Sample error response If a request fails, the following information is returned. For more information, see the developer guide of the corresponding Apsara Stack service. `{`

```json
    "code": "asapi.server.api.notfound",// The error code.
    "eagleEyeTraceId": "xxx-xxx-xxx-xxx", // The trace ID provided by EagleEye.
    "asapiSuccess": false, // Indicates whether the request is successful.
    "hostId": "xxxx", // The ID of the host.
    "message": "Failed to ....", // The message returned.
    "asapiErrorMessage": "Failed to ....", // The error message provided by the ASAPI.
    "asapiErrorCode": "asapi.server.api.notfound" // The error code provided by the ASAPI.
```

`}`

## 2 API reference

### 2.1 API reference

#### 2.1.1 List of operations by function

The following tables list the API operations available for use in Virtual Private Cloud (VPC). VPC API

| API | Description |
|---|---|
| CreateVpc | Creates a VPC. |
| DeleteVpc | Deletes a VPC. |
| ModifyVpcAttribute | Modifies the name and description of a VPC. |
| DescribeVpcs | Queries VPCs. |
| AssociateVpcCidrBlock | Adds a secondary IPv4 CIDR block to a VPC. |
| UnassociateVpcCidrBlock | Deletes a secondary IPv4 CIDR block from a VPC. |

vSwitch API

| API | Description |
|---|---|
| CreateVSwitch | Creates a vSwitch. |
| DeleteVSwitch | Deletes a vSwitch. |
| ModifyVSwitchAttribute | Modifies the name and description of a vSwitch. |
| DescribeVSwitches | Queries vSwitches. |

vRouter API

| API | Description |
|---|---|
| ModifyVRouterAttribute | Modifies the name and description of a vRouter. |
| DescribeVRouters | Queries vRouters in a specified region. |

Route table API

| API | Description |
|---|---|
| CreateRouteTable | Creates a custom route table. |

| eveloper Guide·API reference | Virtual Private Clou |
|---|---|

| API | Description |
|---|---|
| CreateRouteEntry | Creates a custom route entry in the vRouter or virtual border router (VBR) of a VPC. |
| DeleteRouteEntry | Deletes a custom route entry. |
| DescribeRouteEntryList | Queries route entries. |
| ModifyRouteEntry | Modifies the name and description of a custom route entry. |
| AssociateRouteTable | Associates a custom route table with a vSwitch in the same VPC. |
| DeleteRouteTable | Deletes a custom route table. |
| DescribeRouteTableList | Queries route tables. |
| UnassociateRouteTable | Disassociates a route table from a vSwitch. |

Region API

| API | Description |
|---|---|
| DescribeRegions | Queries available regions. |
| DescribeZones | Queries zones in a specified region. |

Tag API

| API | Description |
|---|---|
| TagResources | Creates and adds tags to a specified resource. |
| ListTagResources | Queries tags that are added to instances. |
| UnTagResources | Removes tags from a specified resource. |

BGP API

| API | Description |
|---|---|
| DescribeBgpGroups | Queries Border Gateway Protocol (BGP) groups in a specified region. |
| ModifyBgpGroupAttribute | Modifies configurations of BGP groups. |
| DeleteBgpGroup | Deletes a specified BGP group. |
| DescribeBgpPeers | Queries BGP peers in a specified region. |

| irtual Private Cloud | Developer Guide·API referenc |
|---|---|

| API | Description |
|---|---|
| DeleteBgpPeer | Deletes a specified BGP peer. |
| AddBgpNetwork | Advertises BGP networks. |
| DeleteBgpNetwork | Deletes advertised BGP networks. |
| DescribeBgpNetworks | Queries advertised BGP networks. |

VBR API

| API | Description |
|---|---|
| CreateVirtualBorderRouter | Creates a VBR. |
| DeleteVirtualBorderRouter | Deletes a VBR. |
| DescribeVirtualBorderRouters | Queries VBRs. |
| TerminateVirtualBorderRouter | Disables a VBR. |
| RecoverVirtualBorderRouter | Enables a disabled VBR. |
| UnassociatePhysicalConnectionFromVirtualBorderRo uter | Disassociate a VBR from an Express Connect circuit. |

Express Connect API

| API | Description |
|---|---|
| CancelPhysicalConnection | Cancels an Express Connect circuit before it is enabled. After you perform this operation, the Express Connect circuit enters the Canceled state. |
| DescribePhysicalConnections | Queries Express Connect circuits in a specified region. |
| ModifyPhysicalConnectionAttribute | Modifies the configuration of an Express Connect circuit. |
| TerminatePhysicalConnection | Disables an Express Connect circuit after it is enabled. |
| EnablePhysicalConnection | Enables an Express Connect circuit that is in the Confirmed state. After you perform this operation, the Express Connect circuit enters the Enabled state. |
| DeletePhysicalConnection | Deletes an Express Connect circuit. |
| CreatePhysicalConnectionOccupancyOrder | Creates an order for resource occupation. |
| ApplyPhysicalConnectionLOA | Applies for a letter of authorization (LOA). |

| eveloper Guide·API reference | Virtual Private Clou |
|---|---|

| API | Description |
|---|---|
| CreatePhysicalConnectionSetupOrder | Creates an order for initial installation. |
| CompletePhysicalConnectionLOA | Completes construction. |
| DescribePhysicalConnectionLOA | Queries LOA information about an Express Connect. |

VPN Gateway API

| API | Description |
|---|---|
| CreateVpnGateway | Creates a VPN gateway. |
| DescribeVpnGateways | Queries VPN gateways. |
| DescribeVpnGateway | Queries detailed information about a specified VPN gateway. |
| DeleteVpnGateway | Deletes a specified VPN gateway. |
| ModifyVpnGatewayAttribute | Modifies the name and description of a VPN gateway. |
| CreateCustomerGateway | Creates a customer gateway. |
| DescribeCustomerGateways | Queries customer gateways. |
| DescribeCustomerGateway | Queries details about a customer gateway. |
| DeleteCustomerGateway | Deletes a specified customer gateway. |
| ModifyCustomerGatewayAttribute | Modifies the name and description of a customer gateway. |
| DeleteVpnPbrRouteEntry | Deletes a policy-based route entry of a VPN gateway. |
| DeleteVpnRouteEntry | Deletes a destination-based route entry of a VPN gateway. |
| DescribeVpnRouteEntries | Queries destination-based route entries of a VPN gateway. |
| ModifyVpnRouteEntryWeight | Modifies the weight of a destination-based route entry of a VPN gateway. |
| CreateVpnRouteEntry | Creates a destination-based route entry for a VPN gateway. |
| ModifyVpnPbrRouteEntryWeight | Modifies the weight of a policy-based route entry of a VPN gateway. |

| API | Description |
|---|---|
| DescribeVpnPbrRouteEntries | Queries policy-based route entries of a VPN gateway. |
| PublishVpnRouteEntry | Advertises a route entry of a VPN gateway to a VPC. |
| CreateVpnPbrRouteEntry | Creates a policy-based route entry for a VPN gateway. |
| DescribeVpnConnection | Queries details about an IPsec-VPN connection. |
| DeleteVpnConnection | Deletes a specified IPsec-VPN connection. |
| DownloadVpnConnectionConfig | Queries configuration information about an IPsec- VPN connections. |
| CreateVpnConnection | Creates an IPsec-VPN connection. |
| DescribeVpnConnections | Queries IPsec-VPN connections in a specified region. |
| ModifyVpnConnectionAttribute | Modifies the configuration of an IPsec-VPN connection. |
| CreateSslVpnServer | Creates an SSL-VPN server. |
| DeleteSslVpnServer | Deletes an SSL-VPN server. |
| ModifySslVpnServer | Modifies the configuration of an SSL-VPN server. |
| DeleteSslVpnClientCert | Deletes an SSL-VPN client certificate. |
| ModifySslVpnClientCert | Modifies the name of an SSL-VPN client certificate. |
| CreateSslVpnClientCert | Creates an SSL-VPN client certificate. |
| DescribeSslVpnClientCerts | Queries SSL-VPN client certificates. |
| DescribeSslVpnClientCert | Queries details about an SSL-VPN client certificate. |
| DescribeSslVpnServers | Queries SSL-VPN servers. |
| DescribeVpnSslServerLogs | Queries the logs of an SSL-VPN server. |

NAT Gateway API

| API | Description |
|---|---|
| ModifyNatGatewayAttribute | Modifies the configuration of a NAT gateway. |
| ModifyNatGatewaySpec | Resizes a NAT gateway. |
| DeleteNatGateway | Deletes a specified NAT gateway. |

| D | eveloper Guide·API reference | Virtual Private Clou | d |
|---|---|---|---|

| API | Description |
|---|---|
| CreateForwardEntry | Adds DNAT entries to a DNAT table. |
| DescribeForwardTableEntries | Queries DNAT entries in a specified DNAT table. |
| ModifyForwardEntry | Modifies a specified DNAT entry. |
| DeleteForwardEntry | Deletes a specified DNAT entry. |
| CreateSnatEntry | Adds SNAT entries to an SNAT table. |
| DescribeSnatTableEntries | Queries SNAT entries. |
| ModifySnatEntry | Modifies a specified SNAT entry. |
| DeleteSnatEntry | Deletes a specified SNAT entry. |
| ModifyBandwidthPackageSpec | Modifies the bandwidth of a NAT service plan. |
| DeleteBandwidthPackage | Deletes a specified NAT service plan. |
| CreateBandwidthPackage | Creates a NAT service plan. |
| DescribeBandwidthPackages | Queries NAT service plans in a specified region. |
| ModifyBandwidthPackageAttribute | Modifies the name and description of a specified NAT service plan. |
| AddBandwidthPackageIps | Adds public IP addresses to a NAT service plan. |

EIP API

| API | Description |
|---|---|
| AllocateEipAddress | Applies for an elastic IP address (EIP). |
| AllocateEipAddressPro | Applies for a specified EIP. |
| AssociateEipAddress | Associates an EIP with a cloud service in the same region. |
| ModifyEipAddressAttribute | Modifies the name, description, and maximum bandwidth of an EIP. |
| UnassociateEipAddress | Disassociates an EIP from a cloud resource. |
| ReleaseEipAddress | Releases a specified EIP. |
| DescribeEipGatewayInfo | Queries information about the subnet mask and gateway of an EIP. |

HAVIP API

| API | Description |
|---|---|
| CreateHaVip | Creates a high-availability virtual IP address (HAVIP). |
| DescribeHaVips | Queries HAVIPs in a specified region. |
| ModifyHaVipAttribute | Modifies the description of an HAVIP. |
| AssociateHaVip | Associates an HAVIP with an Elastic Compute Service (ECS) instance. |
| UnassociateHaVip | Disassociates an HAVIP from an ECS instance. |
| DeleteHaVip | Deletes an HAVIP. |

Network ACL API

| API | Description |
|---|---|
| CreateNetworkAcl | Creates a network access control list (ACL). |
| AssociateNetworkAcl | Associates a network ACL with a vSwitch. |
| ModifyNetworkAclAttributes | Modifies the attributes of a network ACL. |
| UpdateNetworkAclEntries | Updates rules of a network ACL. |
| UnassociateNetworkAcl | Disassociates a network ACL from a vSwitch. |
| CopyNetworkAclEntries | Copies rules of a network ACL. |
| DeleteNetworkAcl | Deletes a network ACL. |
| DescribeNetworkAcls | Queries network ACLs. |
| DescribeNetworkAclAttributes | Queries details about a network ACL. |

IPv6 Gateway API

| API | Description |
|---|---|
| CreateIpv6Gateway | Creates an IPv6 gateway. |
| DeleteIpv6Gateway | Deletes an IPv6 gateway. |
| DescribeIpv6Gateways | Queries IPv6 gateways. |
| ModifyIpv6GatewaySpec | Modifies the specification of an IPv6 gateway. |
| DescribeIpv6EgressOnlyRules | Queries egress-only rules. |
| CreateIpv6EgressOnlyRule | Adds an egress-only rule to an IPv6 address. |

|   | Developer Guide·API reference | Virtual Private Clou | d |
|---|---|---|---|

| API | Description |
|---|---|
| DeleteIpv6EgressOnlyRule | Deletes an egress-only rule. |
| DeleteIpv6InternetBandwidth | Deletes an IPv6 Internet bandwidth plan. |
| DescribeIpv6GatewayAttribute | Queries detailed information about an IPV6 gateway. |
| DescribeIpv6Addresses | Queries IPv6 addresses. |
| ModifyIpv6InternetBandwidth | Modifies the Internet bandwidth plan of an IPv6 address. |
| AllocateIpv6InternetBandwidth | Purchases an Internet bandwidth plan for an IPv6 address. |
| ModifyIpv6AddressAttribute | Modifies the name and description of an IPv6 address. |
| ModifyIpv6GatewayAttribute | Modifies the information about an IPv6 gateway. |

#### 2.1.2 Call VPC APIs

##### 2.1.2.1 Request syntax

To call a Virtual Private Cloud (VPC) API operation, you must send an HTTP GET request to the endpoint of the VPC API. You must add the request parameters that correspond to the API operation being called. After you call the API, the system returns a response. The request and response are encoded in UTF-8. VPC API operations use the RPC protocol. You can call VPC API operations by sending HTTP GET requests. The following example shows the syntax of a VPC API request:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the API. The endpoint of the VPC API is `vpc.`example`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Uni-manager Operations Console. For more information, see Generate the ASAPI endpoint. Action: the operation that you want to perform. For example, to query VPCs, you must set the Action parameter to DescribeVpcs. Version: the version of the API that you want to call. The current VPC API version is 2016-04-28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common request parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information about common parameters, see Common parameters. The following example describes how to call the DescribeVpcs operation. Not e The example in this topic is formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeVpcs &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

##### 2.1.2.2 API authorization

To ensure the security of your account, we recommend that you call VPC APIs as a RAM user. Before you can use a RAM account to call a VPC API, you must create a RAM account and assign corresponding permissions to it. For more information about VPC resources and APIs you can assign permissions on, see RAM authentication.

##### 2.1.2.3 Request signatures

You must sign all API requests to ensure security. Virtual Private Cloud (VPC) uses the request signature to verify the identity of the API caller. VPC implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Alibaba Cloud accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to an RPC API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
```

SHA1`&Signature=`xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeVpcs as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` . The original request URL is formatted as the following example:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Create a string-to-sign by using the request parameters:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC- SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeS tamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter:

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

#### 2.1.3 RAM authentication

Before calling a VPC API using a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used as the unique identifier of the resource to authorize. VPC resources The following table lists the VPC resources that can be authorized and their corresponding ARN formats.

| Resource type | ARN format |
|---|---|
| Virtual Private Cloud (VPC) | acs:vpc:$regionid:$accountid:vpc/$vpcid |
|   | acs:vpc:$regionid:$accountid:vpc/* |
| 2 | > Document Version: 2022092 |

| irtual Private Cloud |   |
|---|---|
|   | Developer Guide·API referenc |
| Resource type | ARN format |
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
|   | acs:vpc:*:$accountid:vpc/* |
| SNAT table | acs:vpc:$regionid:$accountid:snattable/$snattableid |
|   | acs:vpc:$regionid:$accountid:snattable/* |
|   | acs:vpc:*:$accountid:vpc/* |
|   | acs:vpc:$regionid:$accountid:* |
| Document Version: 202 | 20928 5 |

| eveloper Guide·API refe | rence Virtual Private Clou |
|---|---|
| GReesnoeurarcl ere tsyopuerce | ARN format |
|   | acs:vpc:*:$accountid:* |

$regionid`/`accoutid`/`vrouterid are IDs of the specific resources, `*` represents all resources. VPC API operations The following table lists the API operations that can be authorized and their corresponding ARN formats.

| Operation | ARN format |   |   |
|---|---|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |   |   |
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

| irtual Private Cloud | Developer Guide·API referenc |
|---|---|

| Operation | ARN format |   |   |
|---|---|---|---|
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

| eveloper Guide·API reference | Virtual Private Clou |
|---|---|

| Operation | ARN format |   |   |
|---|---|---|---|
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:AddBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:RemoveBandwidthPackageIps | thpackageid |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid thpackageid |   |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwid |   |
| vpc:DeleteBandwidthPackage | thpackageid |   |   |
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

#### 2.1.4 Common parameters

Common request parameters Common request parameters are request parameters that you must use when you call each API. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | Strin g | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | Strin g | Yes | The API version in the format of YYYY-MM-DD . Valid value: 2016-04-28 |
| AccessKeyId | Strin g | Yes | The AccessKey ID that you use to call an API. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Name | Type | Required | Description |   |   |
|---|---|---|---|---|---|
| Signature | Strin g | Yes | The signature result string. |   |   |
| SignatureMeth od | Strin g | Yes | The algorithm used to create the request signature. Valid value: HMAC-SHA1 |   |   |
| Timestamp | Strin g | Yes | The timestamp of the request. The timestamp uses UTC and it complies with the ISO 8601 standard. Its format is YYYY-MM- DDThh:mm:ssZ . For example, 20:00:00 on January 10, 2013 in China Standard Time (UTC +8) is written as 2013-01-10T12:00:00Z. |   |   |
|   |   |   |   | YYYY-MM- |   |
| SignatureVersi on | Strin g | Yes | The version of the signature algorithm. Valid value: 1.0 |   |   |
| SignatureNonc e | Strin g | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |   |   |

| es | DDThh:mm:ssZ |
|---|---|

```
http://vpc.example.com/?Action=DescribeVpcs &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Common response parameters API responses use a unified format. 2xx HTTP status codes indicate a successful invocation. 4xx or 5xx HTTP status codes indicate a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time you send a request to call an API, the system returns a unique identifier RequestId, regardless of whether the invocation is successful or not. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
      <!—Result root node-->
      <API name+Response>
      <!—Returned request tag-->
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
      <!—Returned results-->
      </API name+Response>
```

JSON format `{`

```json
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
      /*Returned results*/
```

`}`

#### 2.1.5 VPC

##### 2.1.5.1 CreateVpc

Deletes a virtual private cloud (VPC). Descriptions When you call this operation, take note of the following rules: You can specify only one CIDR block for a VPC. The CIDR block must be 172.16.0.0/16, 192.168.0.0/16, or their subnets, and the subnet mask must be 8 to 24 bits in length. The default CIDR block is 192.168.0.0/16. After you create a VPC, you cannot modify its CIDR block. In each VPC, cloud services can use a maximum of 60,000 private IP addresses. You cannot increase the quota. After you create a VPC, a vRouter and a route table are automatically created. At most three customer-side CIDR blocks can be added to a VPC. If a user CIDR block includes another user CIDR block, the one with the shorter subnet mask takes effect. For example, if 192.168.0.0/16 and 192.168.0.0/24 are specified, only 192.168.0.0/16 takes effect. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpc | The operation that you want to perform. Set the value to Creat eVpc. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the VPC belongs. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CidrBlock | String | No | 172.16.0.0/16 | The CIDR block of the VPC. You can use one of the following CIDR blocks or their subnets as the CIDR block of your VPC: 172.16.0.0/16. 192.168.0.0/16 (default). |
| Ipv6CidrBlock | String | No | 1007:XXXX:0:40: :/56 | The IPv6 CIDR block of the VPC. |
| EnableIpv6 | Boolean | No | false | Specifies whether to enable the IPv6 CIDR block. Valid values: f alse (default): disables the IPv6 CIDR block. t rue: enables the IPv6 CIDR block. |
| VpcName | String | No | abc | The name of the VPC. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| Description | String | No | This is my first Vpc. | The description of the VPC. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| ResourceGroupId | String | No | rg- acfmxazb4ph6aiy **** | The ID of the resource group. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| DryRun | Boolean | No | false | Specifies whether to precheck this request. Valid values: t rue: sends a check request without creating a VPC. The system checks the required parameters, request format and service limits. An error message is returned if the request fails the precheck. If the request passes the precheck, the DryRunOp eration error code is returned. f alse: sends the request. This is the default value. If the request passes the precheck, a 2XX HTTP status code is returned and the a VPC is created. |   |   |
|   |   |   |   |   | DryRunOp |   |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |   |   |
| UserCidr | String | No | 189.XX.XX.0/12 | The user CIDR block. Separate multiple CIDR blocks with commas (,). At most three CIDR blocks are supported. |   |   |

|   | eration |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcId | String | vpc- bp15zckdt37pq72zv **** | The ID of the created VPC. |
| VRouterId | String | vrt- bp1lhl0taikrteen8*** * | The ID of the vRouter that is automatically created by the system after the VPC is created. |
| RouteTableId | String | vtb- bp145q7glnuzdv**** | The ID of the route table that is automatically created by the system after the VPC is created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |
| ResourceGroupI d | String | rg- acfmxazb4ph6aiy*** * | The ID of the resource group to which the EIP belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpc &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpcResponse>
      <ResourceGroupId>rg-acfmxazb4ph****</ResourceGroupId>
      <RequestId>8B2F5262-6B57-43F2-97C4-971425462DFE</RequestId>
      <RouteTableId>vtb-bp1krxxzp0c2****</RouteTableId>
      <VRouterId>vrt-bp1jcg5cmxjbl9xgc****</VRouterId>
      <VpcId>vpc-bp1qpo0kug3a20qqe****</VpcId>
</CreateVpcResponse>
```

`JSON` format `{`

```json
    "CreateVpcResponse": {
        "ResourceGroupId": "rg-acfmxazb4ph****",
        "RequestId": "8B2F5262-6B57-43F2-97C4-971425462DFE",
        "RouteTableId": "vtb-bp1krxxzp0c2****",
        "VRouterId": "vrt-bp1jcg5cmxjbl9xgc****",
        "VpcId": "vpc-bp1qpo0kug3a20qqe****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Specified CIDR block is not valid | The error message returned because the specified CIDR block is invalid. |
| 400 | ResourceNotAvailabl e | Resource you requested is not available in this region or zone. | The error message returned because you cannot create a vSwitch in the current region or zone. |
| 400 | InvalidVpcName.Mal formed | Specified VPC name is not valid. | The error message returned because the format of the VPC name is invalid. Enter a valid VPC name and try again. |
| 400 | InvalidVpcDiscription .Malformed | Specified VPC description is not valid. | The error message returned because the format of the VPC description is invalid. |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the permissions and try again. |
| 400 | QuotaExceeded.Vpc | VPC quota exceeded. | The error message returned because the number of VPCs that belong to the Apsara Stack tenant account has reached the upper limit. You can submit a ticket to request a quota increase. |
| 400 | ResourceNotAvailabl e.Vpc | Resource you requested is not available in this region or zone. | The error message returned because the resource you requested is not available in this region or zone. |
| 400 | InvalidParameter | Specified UserCidr invalid format. | The error message returned because the format of the user CIDR block is invalid. |
| 400 | InvalidParameter | Specified UserCidr Subnet mask is not valid . | The error message returned because the subnet mask of the user CIDR block is invalid. |
| 400 | InvalidUserCidr.Quot a | Specified UserCidr number is greater than 3. | The error message returned because the UserCidr value has reached the upper limit. |
| 400 | InvalidUserCidr.Malfo rmed | Specified UserCidr overlapping in of 100.64.0.0/10. | The error message returned because the UserCidr value overlaps with 100.64.0.0/10. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID is invalid. |
| 400 | OperationUnsupport ed.ResourceGroupId | ResourceGroup is not supported in this region. | The error message returned because the resource group feature is not enabled. |

##### 2.1.5.2 DeleteVpc

Deletes a virtual private cloud (VPC). Descriptions When you call this operation, take note of the following limits: Before you delete a VPC, make sure that you have released or removed all resources deployed in the VPC, such as vSwitches, instances, and high-availability virtual IP addresses (HAVIPs). You can delete only a VPC that is in the Available state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpc | The operation that you want to perform. Set the value to Delet eVpc. |
| VpcId | String | Yes | vpc- bp1m7v25emi1h5 mtc**** | The ID of the VPC that you want to delete. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the VPC is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpc &VpcId=vpc-bp1m7v25emi1h5mtc**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpcResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVpcResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | OperationDenied | The operation is not supported in this status. | The error message returned because the state of the VPC is invalid and the operation cannot be performed. |
| 403 | OperationDenied | The snapshot creation for the specified disk is not finished yet. | The error message returned because the snapshot of the specified disk is being created. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |
| 400 | DependencyViolatio n.RouteEntry | Specified object has dependent resources | The error message returned because custom route entries exist in the VPC and the VPC cannot be deleted. |
| 400 | DependencyViolatio n.Instance | Specified object has dependent resources | The error message returned because the VPC is associated with a resource. |
| 400 | DependencyViolatio n.VSwitch | Specified object has dependent resources | The error message returned because vSwitches exist in the VPC and the VPC cannot be deleted. Delete the vSwitches and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | DependencyViolatio n.SecurityGroup | Specified object has dependent resources | The error message returned because security groups exist in the VPC and the VPC cannot be deleted. Delete the security groups and try again. |
| 404 | InvalidVpcId.NotFou nd | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |
| 400 | DependencyViolatio n.RouteInterface | Specified object has dependent route interface . | The error message returned because the vSwitch is associated with a router interface and cannot be deleted. |
| 400 | DependencyViolatio n.Tunnel | Specified object has dependent tunnel. | The error message returned because the VPC is associated with a tunnel. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | DependencyViolatio n.NatGateway | Specified object has dependent resources NatGateway. | The error message returned because NAT gateways exist in the VPC and the VPC cannot be deleted. Delete the NAT gateways and try again. |
| 400 | DependencyViolatio n.RouterInterface | Specified object has dependent resources RouterInterface. | The error message returned because the VPC is associated with a router interface. |
| 400 | DependencyViolatio n.SecurityGroup | Specified object has dependent resources SecurityGroup. | The error message returned because security groups exist in the VPC and the VPC cannot be deleted. Delete the security groups and try again. |
| 400 | Forbidden.VpcNotFo und | Specified VPC can not found. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | Forbbiden | Active custom route in vpc. | The error message returned because you must add a custom route entry to the VPC. |
| 400 | DependencyViolatio n.DhcpOptionsSet | The VPC cannot be deleted when it is associated with dhcpOptionsSet. | The error message returned because DHCP options sets exist in the VPC and the VPC cannot be deleted. Delete the DHCP options sets and try again. |

##### 2.1.5.3 ModifyVpcAttribute

Modifies the name and description of a virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpcAttribu te | The operation that you want to perform. Set the value to Modif yVpcAt t ribut e. |
| VpcId | String | Yes | vpc- bp1qtbach57ywe cf**** | The ID of the VPC that you want to modify. |
| Description | String | No | This is my VPC. | The description of the VPC. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| VpcName | String | No | Vpc-1 | The new name of the VPC. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| CidrBlock | String | No | 192.XX.XX.0/24 | The IPv4 CIDR block of the VPC. The CIDR block can be 172.16.0.0/16, 192.168.0.0/16, and one of their subnets. The subnet mask must be 8 to 24 bits in length. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the VPC is deployed. You can call the DescribeRegions operation to the most recent region list. |
| EnableIPv6 | Boolean | No | true | Specifies whether to enable IPv6 CIDR blocks. Valid values: t rue: enables IPv6 CIDR blocks. f alse: disables IPv6 CIDR blocks. |

| irtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |

| Ipv6CidrBlock | String | No | 1007:XXXX:0:40: :/61 | Specifies whether to enable IPv6 CIDR blocks. Valid values: t rue: enables IPv6 CIDR blocks. f alse: disables IPv6 CIDR blocks. |
|---|---|---|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpcAttribute &VpcId=vpc-bp1qtbach57ywecf**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpcAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVpcAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyVpcAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVpcId.NotFou nd | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |
| 400 | InvalidVpcName.Mal formed | Specified VPC name is not valid. | The error message returned because the format of the VPC name is invalid. Enter a valid VPC name and try again. |
| 400 | InvalidVpcDiscription .Malformed | Specified VPC description is not valid. | The error message returned because the format of the VPC description is invalid. |
| 400 | InvalidParameter | Specified UserCidr invalid format. | The error message returned because the format of the user CIDR block is invalid. |
| 400 | InvalidParameter | Specified UserCidr Subnet mask is not valid . | The error message returned because the subnet mask of the user CIDR block is invalid. |
| 400 | InvalidUserCidr.Quot a | Specified UserCidr number is greater than 3. | The error message returned because the UserCidr value has reached the upper limit. |
| 400 | InvalidUserCidr.Malfo rmed | Specified UserCidr overlapping in of 100.64.0.0/10. | The error message returned because the UserCidr value overlaps with 100.64.0.0/10. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |
| 400 | InvalidCidrBlock.Malf ormed | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |

##### 2.1.5.4 DescribeVpcAttribute

Queries detailed information about a virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpcAttri bute | The operation that you want to perform. Set the value to DescribeVpcAt t ribut e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the VPC is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp18sth14qii3pnv **** | The ID of the VPC that you want to query. |
| DryRun | Boolean | No | false | Specifies whether to precheck the request. t rue: prechecks the API request. Resources are not queried. The system checks whether your AccessKey pair is valid, whether the RAM user is authorized, and whether required parameters are set. If the request fails the precheck, the corresponding error message is returned. If the request passes the precheck, the DryRunOperation error code is returned. f alse: sends the request. This is the default value. If the request passes the precheck, a 2XX HTTP status code is returned and the resource is queried. |
| IsDefault | Boolean | No | false | Specifies whether the VPC is the default one. Valid values: f alse: no t rue (default): yes |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssociatedCens | Array of AssociatedCen |   | The list of Cloud Enterprise Network (CEN) instances that are associated with the VPC. If the VPC is not associated with a CEN instance, no value is returned. |
| AssociatedCen |   |   |   |

| eveloper Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CenId | String | cen- 7qthudw0ll6jmc**** | The ID of the CEN instance that is associated with the VPC. |
| CenOwnerId | Long | 111111111111 | The ID of the Apsara Stack tenant account to which the CEN instance belongs. |
| CenStatus | String | Attached | The state of the associated CEN instance. At t ached is returned only when the VPC is associated with a CEN instance. |
| CidrBlock | String | 192.168.0.0/16 | The IPv4 CIDR block of the VPC. |
| ClassicLinkEnabl ed | Boolean | false | Indicates whether the ClassicLink feature is enabled. Valid values: t rue: enabled f alse: disabled |
| CloudResources | Array of CloudResource SetType |   | The list of resources deployed in the VPC. |
| CloudResource SetType |   |   |   |
| ResourceCount | Integer | 1 | The number of resources deployed in the VPC. |
| ResourceType | String | VSwitch | The type of resources deployed in the VPC. Valid values: VSwit ch: vSwitches VRout er: vRouters Rout eT able: route tables |
| CreationTime | String | 2018-10- 16T07:31:09Z | The time when the VPC was created. |
| Description | String | VPC | The description of the VPC. |
| DhcpOptionsSe tId | String | dopt- o6w0df4epg9zo8isy **** | The ID of the DHCP options set. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DhcpOptionsSe tStatus | String | Available | The state of the DHCP options set. Valid values: Available: The DHCP options set is available for use. InUse: The DHCP options set is being used. Delet ed:The DHCP options set is deleted. Pending: The DHCP options set is being configured. |
| Ipv6CidrBlock | String | 2408:XXXX:0:a600: :/56 | The IPv6 CIDR block of the VPC. |
| IsDefault | Boolean | false | Indicates whether the VPC is the default one. Valid values: t rue: The VPC is the default one. f alse: The VPC is not the default one. |
| OwnerId | Long | 3253532535 | The ID of the owner. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the VPC is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| RequestId | String | 7486AE4A-129D- 43DB-A714- 2432C074BA04 | The ID of the request. |
| ResourceGroupI d | String | rg- acfmxazbvgb4ph*** * | The ID of the resource group to which the EIPs belong. |
| SecondaryCidrB locks | List | 192.168.20.0/24 | The IPv4 CIDR block of the VPC. |
| Status | String | Available | The state of the VPC. Valid values: Available: The VPC is available. Pending: The VPC is being configured. |
| UserCidrs | List | 172.16.0.1/24 | The user CIDR block. Separate multiple CIDR blocks with commas (,). You can specify at most three CIDR blocks. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| VRouterId | String | vrt- bp1jso6ng1at0ajsc** ** | The ID of the vRouter that belongs to the VPC. |
| VSwitchIds | List | vsw- bp1nhbnpv2blyz8dl **** | The list of vSwitches deployed in the VPC. |
| VpcId | String | vpc- bp18sth14qii3pnvo* *** | The ID of the VPC. |
| VpcName | String | doctest2 | The name of the VPC. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpcAttribute &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-bp18sth14qii3pnv**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpcAttributeResponse>
      <VpcName>doctest2</VpcName>
      <Description></Description>
      <IsDefault>false</IsDefault>
      <ResourceGroupId>rg-acfmxazb4ph****</ResourceGroupId>
      <UserCidrs></UserCidrs>
      <ClassicLinkEnabled>false</ClassicLinkEnabled>
      <AssociatedCens>
            <AssociatedCen>
                  <CenStatus>Attached</CenStatus>
                  <CenOwnerId>12315790855****</CenOwnerId>
                  <CenId>cen-7qthudw0ll6jmc****</CenId>
            </AssociatedCen>
      </AssociatedCens>
      <VRouterId>vrt-bp1jso6ng1at0ajs****</VRouterId>
      <VpcId>vpc-bp18sth14qii3pnvo****</VpcId>
      <CreationTime>2018-10-16T07:31:09Z</CreationTime>
      <CidrBlock>192.168.0.0/16</CidrBlock>
      <Status>Available</Status>
      <VSwitchIds>
            <VSwitchId>vsw-bp14cagpfysr29fe****</VSwitchId>
      </VSwitchIds>
      <RequestId>7486AE4A-129D-43DB-A714-2432C074BA04</RequestId>
      <RegionId>cn-hangzhou</RegionId>
      <CloudResources>
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

`JSON` format `{`

```json
    "DescribeVpcAttributeResponse": {
        "VpcName": "doctest2",
        "Description": "",
        "IsDefault": false,
        "ResourceGroupId": "rg-acfmxazb4ph****",
        "UserCidrs": "",
        "ClassicLinkEnabled": false,
        "AssociatedCens": {
            "AssociatedCen": {
                "CenStatus": "Attached",
                "CenOwnerId": "12315790855****",
                "CenId": "cen-7qthudw0ll6jmc****"
```

`}` `},`

```json
        "VRouterId": "vrt-bp1jso6ng1at0ajs****",
        "VpcId": "vpc-bp18sth14qii3pnvo****",
        "CreationTime": "2018-10-16T07:31:09Z",
        "CidrBlock": "192.168.0.0/16",
        "Status": "Available",
        "VSwitchIds": {
            "VSwitchId": "vsw-bp14cagpfysr29fe****"
```

`},`

```json
        "RequestId": "7486AE4A-129D-43DB-A714-2432C074BA04",
        "RegionId": "cn-hangzhou",
        "CloudResources": {
            "CloudResourceSetType": [
```

`{`

```json
                    "ResourceType": "VSwitch",
                    "ResourceCount": 1
```

`},` `{`

```json
                    "ResourceType": "VRouter",
                    "ResourceCount": 1
```

`},` `{`

```json
                    "ResourceType": "RouteTable",
                    "ResourceCount": 1
```

`}` `]` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |
| 404 | InvalidVpcId.NotFou nd | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

##### 2.1.5.5 AssociateVpcCidrBlock

Adds a secondary IPv4 CIDR block to a virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateVpcCidr Block | The operation that you want to perform. Set the value to Associat eVpcCidrBlock. |
| RegionId | String | Yes | ch-qingdao- env17-d01 | The ID of the region where the VPC is deployed. You can call the DescribeRegions operation to the most recent region list. |
| VpcId | String | Yes | vpc- o6wrloqsdqc9io3 mg**** | The ID of the VPC to which you want to add a secondary IPv4 CIDR block. |
| SecondaryCidrBlo ck | String | No | 192.168.0.0/16 | The secondary IPv4 CIDR block. You can specify one of the following standard IPv4 CIDR blocks or their subnets as the secondary IPv4 CIDR block: 192.168.0.0/16, 172.16.0.0/12, and 10.0.0.0/8. To use a public CIDR block as the secondary IPv4 CIDR block, submit a ticket. When you add a secondary IPv4 CIDR block, take note of the following rules: The CIDR block cannot start with 0. The subnet mask must be 8 to 24 bits in length. The secondary CIDR block cannot overlap with the primary CIDR block or an existing secondary CIDR block. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C1221A1F-2ACD- 4592-8F27- 474E02883159 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateVpcCidrBlock &RegionId=ch-qingdao-env17-d01 &VpcId=vpc-o6wrloqsdqc9io3mg**** &<Common request parameters>
```

Sample success response `XML` format

```xml
<AssociateVpcCidrBlockResponse>
         <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
</AssociateVpcCidrBlockResponse>
```

`JSON` format `{`

```json
 "RequestId":"C1221A1F-2ACD-4592-8F27-474E02883159"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock.Malf ormed | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the permissions and try again. |
| 400 | MissingParam.Secon daryCidrBlockOrIpv6 CidrBlock | Either SecondaryCidrBlock or Ipv6CidrBlock must be specified. | The error message returned because the secondary IPv4 CIDR block or the IPv6 CIDR block is not set. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingParam.VpcId | You must specify VpcId. | The error message returned because VpcId is not set. |

##### 2.1.5.6 UnassociateVpcCidrBlock

Deletes a secondary IPv4 CIDR block from a virtual private cloud (VPC). Descriptions Before you delete a secondary IPv4 CIDR block from a VPC, delete the vSwitch which is created with the IPv4 CIDR block. For more information, see `DeleteVSwitch` . Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateVpcCi drBlock | The operation that you want to perform. Set the value to Unassociat eVpcCidrBlock. |
| RegionId | String | Yes | ch-qingdao- env17-d01 | The ID of the region to which the secondary IPv4 CIDR block to be deleted belongs. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- o6wrloqsdqc9io3 mg**** | The ID of the VPC from which you want to delete a secondary IPv4 CIDR block. |
| SecondaryCidrBlo ck | String | No | 192.XX.XX.0/16 | The secondary IPv4 CIDR block. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C1221A1F-2ACD- 4592-8F27- 474E02883159 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateVpcCidrBlock &RegionId=ch-qingdao-env17-d01 &VpcId=vpc-o6wrloqsdqc9io3mg**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateVpcCidrBlockResponse>
         <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
</UnassociateVpcCidrBlockResponse>
```

`JSON` format `{`

```json
 "RequestId":"C1221A1F-2ACD-4592-8F27-474E02883159"
```

`}`

#### 2.1.6 vSwitch

##### 2.1.6.1 CreateVSwitch

Creates a vSwitch. Descriptions When you call this operation, take note of the following limits: You can create at most 24 vSwitches in a virtual private cloud (VPC). The first IP address and last three IP addresses of each vSwitch CIDR block are reserved. For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved. The number of instances in a vSwitch cannot exceed the remaining capacity of the VPC. The remaining capacity is the difference between 15,000 and the current number of instances. Each instance can belong to only one vSwitch. vSwitches do not support multicasting or broadcasting. After you create a vSwitch, you cannot modify its CIDR block. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVSwitch | The operation that you want to perform. Set the value to Creat eVSwit ch. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CidrBlock | String | Yes | 172.XX.XX.0/24 | The CIDR block of the vSwitch. Take note of the following limits: The subnet mask must be 16 to 29 bits in length. The CIDR block of the vSwitch must fall within the range of the CIDR block of the VPC to which the vSwitch belongs. The CIDR block of a vSwitch cannot be the same as the destination CIDR block in a route entry of the VPC. However, it can be a subset of the destination CIDR block. |
| VpcId | String | Yes | vpc- 257gqcdfvx6n**** | The ID of the VPC where you want to create the vSwitch. |
| ZoneId | String | Yes | cn-qingdao-env- amtest11001-a | The ID of the zone where you want to create the vSwitch. You can call the DescribeZones operation to query the most recent zone list. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to create the vSwitch. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6CidrBlock | Integer | No | 12 | The last eight bits of the IPv6 CIDR block of the vSwitch. Valid values: 0 to 255. |
| Description | String | No | This is my vswitch. | The description of the vSwitch. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| VSwitchName | String | No | VSwitch-1 | The name of the vSwitch. The name must be 2 to 128 characters in length and must start with a letter. The description cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters. It must be 1 to 64 characters in length. |
| IsCgw | Boolean | No | true | Specifies whether the gateway is a customer gateway. Valid values: t rue: yes f alse: no |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VSwitchId | String | vsw- 25navfgbue4g**** | The ID of the vSwitch. |
| RequestId | String | 861E6630-AEC0- 4B2D-B214- 6CB5E44B7F04 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVSwitch &CidrBlock=172.XX.XX.0/24 &VpcId=vpc-257gqcdfvx6n**** &ZoneId=cn-qingdao-env-amtest11001-a &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVSwitchResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
      <VSwitchId>vsw-25naue4cdvf****</VSwitchId>
</CreateVSwitchResponse>
```

`JSON` format `{`

```json
    "CreateVSwitchResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
        "VSwitchId": "vsw-25naue4cdvf****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidZoneId.NotFo und | Specified zone does not exist. | The error message returned because the ID of the zone is invalid. |
| 404 | InvalidVpcId.NotFou nd | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |
| 400 | InvalidVSwitchName. Malformed | Specified virtual switch name is not valid. | The error message returned because the format of the vSwitch name is invalid. |
| 400 | InvalidVSwitchDiscrip tion.Malformed | Specified virtual switch description is not valid. | The error message returned because the description of the vSwitch is invalid. |
| 400 | ResourceNotAvailabl e | Resource you requested is not available in this region or zone. | The error message returned because you cannot create a vSwitch in the current region or zone. |
| 400 | InvalidParameter | Specified CIDR block is not valid in VPC. | The error message returned because the vSwitch CIDR block does not fall within the VPC CIDR block. |
| 400 | InvalidCidrBlock.Over lapped | Specified CIDR block overlapped with other subnets. | The error message returned because the vSwitch CIDR block overlaps with another vSwitch CIDR block or the destination CIDR block of a custom route entry. Make sure that the vSwitch CIDR block does not overlap with another vSwitch CIDR block or the destination CIDR block of a route entry. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock.Over lapped | Specified CIDR block overlapped with other entry. | The error message returned because the vSwitch CIDR block overlaps with another vSwitch CIDR block or the destination CIDR block of a custom route entry. Make sure that the vSwitch CIDR block does not overlap with another vSwitch CIDR block or the destination CIDR block of a route entry. |
| 400 | QuotaExceeded.VSw itch | Virtual switch quota exceeded. | The error message returned because the number of vSwitches has reached the quota. Reduce the number of vSwitches and try again later. |
| 400 | IncorrectRouteEntryS tatus | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectVSwitchSta tus | Some virtual switch is modifying within the same VPC. | The error message returned because multiple vSwitches are in the Modifying state in the same VPC. Try again later. |
| 400 | InvalidCirdrBlock.Mas kLength | Specified CIDR block is not valid . | The error message returned because the format of the CIDR block is invalid. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |
| 400 | InvalidCidrBlock.Malf ormed | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 400 | IncorrectVSwitchSta tus | VSwitch Creation simultaneously is not supported. | The error message returned because the system failed to create the vSwitch and one or more vSwitches that belong to the VPC are in the Creating state. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.VpcNotFo und | Specified VPC can not found. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |

##### 2.1.6.2 DeleteVSwitch

Deletes a vSwitch. Descriptions When you call this operation, take note of the following limits: Before you delete a vSwitch, delete all the resources that are deployed in the vSwitch first, including Elastic Compute Service (ECS) instances, Server Load Balancer (SLB) instances, and ApsaraDB RDS instances. If Source Network Address Translation (SNAT) entries and high-availability virtual IP addresses (HAVIPs) are configured in the vSwitch, delete them before you delete the vSwitch. You can delete only vSwitches that are in the Available state. You cannot delete a vSwitch from a virtual private cloud (VPC) where a vSwitch or a route entry is being created or deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVSwitch | The operation that you want to perform. Set the value to Delet eVSwit ch. |
| VSwitchId | String | Yes | vsw- asdfjcdvflna**** | The ID of the vSwitch that you want to delete. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the vSwitch is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://vpc.aliyuncs.com/?Action=DeleteVSwitch &VSwitchId=vsw-asdfjcdvflna**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVSwitchResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVSwitchResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectVSwitchSta tus | The current virtual switch status does not support this operation. | The error message returned because the vSwitch is in the Pending state and cannot be deleted. |
| 400 | DependencyViolatio n | Specified object has dependent resources. | The error message returned because resources deployed in the vSwitch are not deleted and the vSwitch cannot be deleted. Delete the resources deployed in the VPC first before you delete the VPC. |
| 400 | DependencyViolatio n | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectRouteEntryS tatus | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | DependencyViolatio n.HaVip | VSwitch cannot be deleted when there are some HaVip dependent with it. | The error message returned because the vSwitch is associated with an HAVIP and the vSwitch cannot be deleted. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because the required parameters values are missing. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidVSwitchId.Not Found | VSwitch not exist. | The error message returned because the specified vSwitch does not exist. Check whether you specify a valid vSwitch. |
| 404 | IncorrectStatus | Vswtich status not stable. | The error message returned because the vSwitch is in the Pending or Modifying state. Try again later. |

##### 2.1.6.3 ModifyVSwitchAttribute

Modifies the name and description of a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVSwitchAt tribute | The operation that you want to perform. Set the value to Modif yVSwit chAt t ribut e. |
| VSwitchId | String | Yes | vsw- 25nacdfvue4**** | The ID of the vSwitch. |
| VSwitchName | String | No | VSwitch-1 | The new name for the vSwitch. The name must be 2 to 128 characters in length, and can contain, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter The name cannot start with http:// or https:// . |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the vSwitch is deployed. You can call the DescribeRegions operation to the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | This is my vswitch. | The description of the vSwitch. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Ipv6CidrBlock | Integer | No | 10 | The last eight bits of the IPv6 CIDR block of the vSwitch. Valid values: 0 to 255. You can set this parameter only when the VPC to which the vSwitch belongs has the IPv6 feature enabled. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVSwitchAttribute &VSwitchId=vsw-25nacdfvue4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVSwitchAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVSwitchAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVSwitchId.Not Found | The specified virtual switch does not exists. | The error message returned because the specified vSwitch does not exist. Check whether the specified ID is valid. |
| 400 | InvalidVSwitchName. Malformed | Specified virtual switch name is not valid. | The error message returned because the format of the specified vSwitch name is invalid. Check whether the specified name is valid. |
| 400 | InvalidVSwitchDiscrip tion.Malformed | Specified virtual switch description is not valid. | The error message returned because the format of the specified vSwitch description is invalid. Check whether the specified description is valid. |
| 400 | InvalidVSwitchDiscrip tion.Malformed | Specified virtual switch description is not valid. | The error message returned because the specified description of the vSwitch is invalid. |

##### 2.1.6.4 DescribeVSwitchAttributes

Queries detailed information about a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVSwitchA ttributes | The operation that you want to perform. Set the value to DescribeVSwit chAt t ribut es. |
| VSwitchId | String | Yes | vsw- 25naue4g**** | The ID of the vSwitch that you want to query. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the vSwitch is deployed. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| DryRun | Boolean | No | false | Specifies whether to precheck this request. Valid values: t rue: prechecks the API request. Resources are not queried. The system checks whether your AccessKey pair is valid, whether the RAM user is authorized, and whether required parameters are set. If the request fails the precheck, an error message is returned. If the request passes the precheck, the DryRunOp eration error code is returned. f alse: sends the request. This is the default value. If the request passes the precheck, a 2XX HTTP status code is returned and the resource is queried. |   |   |
|   |   |   |   |   | DryRunOp |   |

|   | eration |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AvailableIpAddr essCount | Long | 12 | The number of available IP addresses. |
| CidrBlock | String | 192.168.0.1/24 | The IPv4 CIDR block of the vSwitch. |
| CloudResources | Array of CloudResource SetType |   | The list of resources deployed in the VPC. |
| CloudResource SetType |   |   |   |
| ResourceCount | Integer | 1 | The number of resources deployed in the VPC. |
| ResourceType | String | VSwitch | The types of resources deployed in the VPC. Valid values: VSwit ch: vSwitches VRout er: vRouters Rout eT able: route tables |
| CreationTime | String | 2017-08- 22T10:40:25Z | The time when the vSwitch was created. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | abc | The description of the vSwitch. |
| Ipv6CidrBlock | String | 2408:XXXX:0:2900: :/64 | The IPv6 CIDR block of the vSwitch. |
| IsCgw | Boolean | false | Indicates whether the gateway is a customer gateway. Valid values: t rue: yes f alse (default): no |
| IsDefault | Boolean | false | Indicates whether the vSwitch is the default vSwitch. Valid values: t rue: yes f alse (default): no |
| NetworkAclId | String | nacl- 2zesich96aa37rl29** ** | The ID of the network ACL that is associated with the vSwitch. |
| OwnerId | Long | 12345678 | The ID of the Alibaba Cloud account to which the vSwitch belongs. |
| RequestId | String | 7B48B4B9-1EAD- 469F-B488- 594DAB4B6A1A | The ID of the request. |
| ResourceGroupI d | String | rg- acfmxazb4pbgfh*** * | The ID of the resource group. |
| RouteTable | Struct |   | The information about the route table that is associated with the vSwitch. |
| RouteTableId | String | vtb- bp145q7glnuzdv**** | The ID of the route table that is associated with the vSwitch. |
| RouteTableTyp e | String | System | The type of the route table. Syst em : a system route table Cust om: a custom route table |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Pending | The state of the vSwitch. Valid values: Pending: The vSwitch is being configured. Available: The vSwitch is available. |
| VSwitchId | String | vsw- 25b7pcdfvv15t**** | The ID of the vSwitch. |
| VSwitchName | String | test | The name of the vSwitch. |
| VpcId | String | vpc- 257gqcfv642n**** | The ID of the VPC to which the vSwitch belongs. |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | The ID of the zone to which the vSwitch belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVSwitchAttributes &VSwitchId=vsw-25naue4g**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVSwitchAttributesResponse>
  <IsDefault>false</IsDefault>
  <Status>Pending</Status>
  <Description>abc</Description>
  <NetworkAclId>nacl-2zesich96aa37rl29****</NetworkAclId>
  <ResourceGroupId>rg-acfmxazb4pbgfh****</ResourceGroupId>
  <ZoneId>cn-qingdao-env17-amtest11001-a</ZoneId>
  <RequestId>7B48B4B9-1EAD-469F-B488-594DAB4B6A1A</RequestId>
  <AvailableIpAddressCount>12</AvailableIpAddressCount>
  <VSwitchId>vsw-25b7pcdfvv15t****</VSwitchId>
  <CidrBlock>192.168.0.1/24</CidrBlock>
  <RouteTable>
        <RouteTableId>vtb-bp145q7glnuzdv****</RouteTableId>
        <RouteTableType>System</RouteTableType>
  </RouteTable>
  <IsCgw>false</IsCgw>
  <OwnerId>12345678</OwnerId>
  <VpcId>vpc-257gqcfv642n****</VpcId>
  <CreationTime>2017-08-22T10:40:25Z</CreationTime>
  <VSwitchName>test</VSwitchName>
  <Ipv6CidrBlock>2408:XXXX:0:2900::/64</Ipv6CidrBlock>
  <CloudResources>
        <ResourceCount>1</ResourceCount>
        <ResourceType>VSwitch</ResourceType>
  </CloudResources>
</DescribeVSwitchAttributesResponse>
```

`JSON` format `{`

```json
    "IsDefault": false,
    "Status": "Pending",
    "Description": "abc",
    "NetworkAclId": "nacl-2zesich96aa37rl29****",
    "ResourceGroupId": "rg-acfmxazb4pbgfh****",
    "ZoneId": "cn-qingdao-env17-amtest11001-a",
    "RequestId": "7B48B4B9-1EAD-469F-B488-594DAB4B6A1A",
    "AvailableIpAddressCount": 12,
    "VSwitchId": "vsw-25b7pcdfvv15t****",
    "CidrBlock": "192.168.0.1/24",
    "RouteTable": {
        "RouteTableId": "vtb-bp145q7glnuzdv****",
        "RouteTableType": "System"
```

`},`

```json
    "IsCgw": false,
    "OwnerId": 12345678,
    "VpcId": "vpc-257gqcfv642n****",
    "CreationTime": "2017-08-22T10:40:25Z",
    "VSwitchName": "test",
    "Ipv6CidrBlock": "2408:XXXX:0:2900::/64",
    "CloudResources": {
        "ResourceCount": 1,
        "ResourceType": "VSwitch"
```

`}` `}`

#### 2.1.7 vRouter

##### 2.1.7.1 ModifyVRouterAttribute

Modifies the name and description of a vRouter. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVRouterAt tribute | The operation that you want to perform. Set the value to Modif yVRout erAt t ribut e. |
| VRouterId | String | Yes | vrt- bp1lhl0taikrteen8 **** | The ID of the vRouter. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the vRouter is deployed. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VRouterName | String | No | VRouter-1 | The name of the vRouter to be modified. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | My VRouter | The description of the vRouter to be modified. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=ModifyVRouterAttribute &VRouterId=vrt-bp1lhl0taikrteen8**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVRouterAttributeResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyVRouterAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyVRouterAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVRouterId.Not Found | Specified virtual router does not exist. | The error message returned because the specified vRouter does not exist. Check whether the specified vRouter is valid. |
| 400 | InvalidVRouterName. Malformed | Specified virtual router name is not valid. | The error message returned because the name format of the specified vRouter is invalid. |
| 400 | InvalidVRouterDiscrip tion.Malformed | Specified virtual router description is not valid. | The error message returned because the description format of the specified vRouter is invalid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |

##### 2.1.7.2 DescribeVRouters

Queries vRouters in a region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVRouters | The operation that you want to perform. Set the value to DescribeVRout ers. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to query vRouters. You can call the DescribeRegions operation to query the most recent region list. |
| VRouterId | String | No | vrt- bp1lhl0taikrteen* *** | The ID of the vRouter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VRouters | Array of VRouter |   | Details about the vRouter. |
| VRouter |   |   |   |
| CreationTime | String | 2018-03- 22T07:46:20Z | The time when the vRouter was created. |
| Description | String | abc | The description of the vRouter. |
| RegionId | String | cn-hangzhou | The region to which the vRouter belongs. |
| RouteTableIds | List | { "RouteTableId": [ "vtb- rj9ybe3y0u41mmjsp ****"] } | The ID of the route table in the vRouter. |
| VRouterId | String | vrt- rj98khsezfqpjrxmv** ** | The ID of the vRouter. |
| VRouterName | String | doctest | The name of the vRouter. |
| VpcId | String | vpc- rj905wotv6y030t1*** * | The ID of the virtual private cloud (VPC) to which the vRouter belongs. |
| TotalCount | Integer | 1 | The total number of entries to return. |
| PageNumber | Integer | 1 | The number of the page to return. |
| PageSize | Integer | 10 | The number of entries to return on each page. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVRouters &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVRoutersResponse>
    <PageNumber>1</PageNumber>
    <TotalCount>2</TotalCount>
    <VRouters>
        <VRouter>
            <VRouterName></VRouterName>
            <RouteTableIds>
                <RouteTableId>vtb-bp1krxxzp0c29fmo****</RouteTableId>
            </RouteTableIds>
            <CreationTime>2018-12-06T06:11:55Z</CreationTime>
            <Description></Description>
            <RegionId>cn-hangzhou</RegionId>
            <VRouterId>vrt-bp1jcg5cmxjbl9xgc****</VRouterId>
            <VpcId>vpc-bp1qpo0kug3a20qqe****</VpcId>
        </VRouter>
        <VRouter>
            <VRouterName></VRouterName>
            <RouteTableIds>
                <RouteTableId>vtb-bp1blq1oh0ybfnpm****</RouteTableId>
            </RouteTableIds>
            <CreationTime>2018-11-08T08:54:03Z</CreationTime>
            <Description></Description>
            <RegionId>cn-hangzhou</RegionId>
            <VRouterId>vrt-bp149ve7yeyvio4nc****</VRouterId>
            <VpcId>vpc-bp1aevy8sofi8mh1q****</VpcId>
        </VRouter>
    </VRouters>
    <PageSize>10</PageSize>
    <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</DescribeVRoutersResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "VRouters": {
        "VRouter": [
```

`{`

```json
                "VRouterName": "",
                "RouteTableIds": {
                    "RouteTableId": [
                        "vtb-rj9ybe3y0u41mmjsp****"
```

`]` `},`

```json
                "CreationTime": "2018-03-22T07:46:20Z",
                "Description": "",
                "RegionId": "us-west-1",
                "VRouterId": "vrt-rj98khsezfqpjrxmv****",
                "VpcId": "vpc-rj905wotv6y030t1z****"
```

`}` `]` `},`

```json
    "PageSize": 10,
    "RequestId": "CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

`}`

#### 2.1.8 Route table

##### 2.1.8.1 CreateRouteTable

Creates a custom route table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouteTabl e | The operation that you want to perform. Set the value to Creat eRout eT able. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the virtual private cloud (VPC) to which the custom route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1qpo0kug3a20 qqe**** | The ID of the VPC to which the custom route table belongs. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouteTableName | String | No | myRouteTable | The name of the route table. The name must be 2 to 128 characters in length and must start with a letter. The name can contain digits, periods (.), underscores ( ), and hyphens (-). It _ cannot start with http:// or https:// . |
| Description | String | No | abc | The description of the route table. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 62172DD5-6BAC- 45DF-8D44- E11ED28DCAC0 | The ID of the instance. |
| RouteTableId | String | vtb- bp145q7glnuzdvzu2 **** | The ID of the route table. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateRouteTable &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-bp1qpo0kug3a20qqe**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouteTableResponse>
      <RequestId>62172DD5-6BAC-45DF-8D44-E11ED28DCAC0</RequestId>
      <RouteTableId>vtb-bp145q7glnuzdvzu2****</RouteTableId>
</CreateRouteTableResponse>
```

`JSON` format `{`

```json
    "RequestId": "62172DD5-6BAC-45DF-8D44-E11ED28DCAC0",
    "RouteTableId": "vtb-bp145q7glnuzdvzu2****"
```

`}` Error codes

| HttpCode | Error code | Error message | Required |
|---|---|---|---|
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 404 | InvalidVpcId.NotFou nd | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

##### 2.1.8.2 CreateRouteEntry

Adds a custom route entry to the route table of a vRouter or a virtual border router (VBR) in a virtual private cloud (VPC). Descriptions When you call t his operat ion, t ake not e of t he f ollowing limit s: The number of custom route entries in a route table cannot exceed 48. The destination CIDR block of a custom route entry cannot be the same as or overlap with the CIDR block of a VPC vSwitch. The destination CIDR block of a custom route entry cannot be 100.64.0.0/10 or a subset of 100.64.0.0/10. The destination CIDR blocks of route entries in the same route table must be unique. If the specified destination CIDR block is an IP address, a 32-bit subnet mask is used. Multiple custom route entries can point to the same next hop. The next hop of a custom route entry and the route table must belong to the same VPC. You can configure equal-cost multi-path (ECMP) route entries by setting the NextHopList parameter. When you add non-ECMP route entries, you must set DestinationCidrBlock, NextHopType, and NextHopId. NextHopList is not supported. When you add ECMP route entries, you must set DestinationCidrBlock and NextHopList. NextHopType and NextHopId are not supported. When you call t his operat ion, t ake not e of t he f ollowing limit s: The number of custom route entries in a route table cannot exceed 48. The NextHopList parameter is not supported. The destination CIDR block of a custom route entry cannot be 100.64.0.0/10 or a subset of 100.64.0.0/10. The destination CIDR blocks of route entries in the same route table must be unique. If the specified destination CIDR block is an IP address, a 32-bit subnet mask is used. Multiple route entries can point to the same next hop. The next hop of a custom route entry must be a vRouter interface associated with the VBR. You can add route entries only when the VBR is in the Active state, and the physical connection associated with the VBR is enabled and unlocked. You can add only non-ECMP route entries. To create such an entry, you must set DestinationCidrBlock, NextHopType, and NextHopId. NextHopList is not supported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouteEntry | The operation that you want to perform. Set the value to Creat eRout eEnt ry. |
| DestinationCidrBl ock | String | Yes | 192.168.0.0/24 | The destination CIDR block of the custom route entry. Both IPv4 and IPv6 CIDR blocks are supported. Make sure that the destination CIDR block meets the following requirements: The destination CIDR block is not 100.64.0.0/10 or a subset of 100.64.0.0/10. The destination CIDR block of the custom route entry is different from the destination CIDR blocks of other route entries in the same route table. If the specified destination CIDR block is an IPv4 address, a 32-bit subnet mask is used. If the specified destination CIDR block is an IPv6 address, a 128-bit subnet mask is used. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzd** ** | The ID of the route table to which you want to add a custom route entry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| NextHopId | String | No | ri- 2zeo3xzyf38r4*** * | The ID of the next hop. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |
| RouteEntryName | String | No | test | The name of the custom route entry that you want to add. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter. |
| Description | String | No | abc | The description of the router entry. |
| NextHopType | String | No | RouterInterface | The type of next hop. Valid values: Inst ance: The next hop is an ECS instance. This is the default value. HaVip: The next hop is a high- availability virtual IP address (HAVIP). Rout erInt erf ace: The next hop is a router interface. Net workInt erf ace: The next hop is an elastic network interface (ENI). VpnGat eway: The next hop is a VPN gateway. IPv6Gat eway: The next hop is an IPv6 gateway. |
| NextHopList.N.Ne xtHopType | String | No | RouterInterface | The next hop type of the equal-cost multi-path routing (ECMP) route. Set the value to Rout erInt erf ace. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHopList.N.Ne xtHopId | String | No | ri- 2zeo3xzyf3cd8r4 **** | The ID of the next hop of the ECMP route. |
| NextHopList.N.W eight | Integer | No | 10 | The route weight of the next hop of the ECMP route. Valid values: 0 to 100. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateRouteEntry &DestinationCidrBlock=192.168.0.0/24 &RouteTableId=vtb-bp145q7glnuzd**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouteEntryResponse> <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId> <CreateRouteEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidInstanId.NotF ound | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the instance ID is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 400 | InvalidCidrBlock.Malf ormed | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 404 | InvalidNextHopId.No tFound | Specified next hop does not exist. | The error message returned because the specified next hop does not exist. |
| 404 | InvalidRouteTableId. NotFound | Specified route table does not exist. | The error message returned because the specified route table does not exist. |
| 400 | InvalidCIDRBlock.Dup licate | Specified CIDR block is already exists. | The error message returned because the specified CIDR block already exists in the route table. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |
| 400 | IncorrectInstanceSta tus | Current instance status does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |
| 400 | QuotaExceeded | Route entry quota exceeded in this route table. | The error message returned because the number of route entries in the route table has reached the upper limit. |
| 400 | IncorrectRouteEntryS tatus | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCidrBlock | Specified CIDR block is not valid. | The error message returned because: 1.The error message returned because you are unauthorized to use the 10.0.0.0/8 CIDR block. 2.The error message returned because the destination CIDR block cannot be a subset of the CIDR blocks of the vSwitches in the VPC. 3.The error message returned because the CIDR block cannot be 100.64.0.0/10. |
| 400 | InvalidNextHopType | Specified parameter "NextHopType" is not valid | The error message returned because the specified next hop type is invalid. |
| 400 | InvalidNextHop.NotF ound | Specified next hop does not exist. | The error message returned because the IP address of the specified next hop does not exist. |
| 400 | InvalidVRouter.NotF ound | vRouter not exists. | The error message returned because the specified vRouter does not exist. Check whether the specified vRouter is valid. |
| 400 | InvalidVPC.NotFound | vpc not exists. | The error message returned because the specified VPC does not exist. Check whether the configuration of the VPC is valid. |
| 400 | InvalidNexthopType AndList.BothNull | both nexthopType and nextHopList are null. | The error message returned because the NextHopType and NextHopList parameters are not specified. |
| 400 | InvalidNexthopType AndList.BothNotNull | both nexthopType and nextHopList are not null. | The error message returned because you cannot leave both the NextHopType and the NextHopList parameters empty. |
| 400 | InvalidRouterInterfac e | invalid router interface. | The error message returned because the specified router interface does not exist. |
| 400 | InvalidOppositeRout erType | nexthop list cannot only contain router interface whose opposite router interface is on vbr. | The error message returned because the specified next hop is invalid. The peer router of the router interface that you specify as the next hop must be a VBR. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidNexthopListSi ze | nexthop size is illegal. Must be between 2 and 4. | The error message returned because you must specify two to four router interfaces as next hops. |
| 400 | InvalidEntryRuleQuot a.NotFound | Route entry quota rule not exists. | The error message returned because the number of route entries that you create has reached the upper limit. |
| 400 | Forbidden.CheckEntr yRuleQuota | Route entry quota rule check error. | The error message returned because an error occurs when the system checks the quota of route entries. |
| 400 | InvalidVBRStatus | invalid virtual border router status. | The error message returned because the VBR is in a state that does not support the operation. |
| 400 | InvalidPhysicalConne ctionBusinessStatus | invalid physical connection business status. | The error message returned because the Express Connect circuit is in a state that does not support the operation. |
| 404 | InvalidHaVipId.NotFo und | The specified HaVip does not exist in the specified VPC. | The error message returned because the specified HAVIP does not exist in the VPC. |
| 400 | IncorrectHaVipStatu s | This operation is denied because satus of the specified HaVip is neither Available nor InUse. | The error message returned because you cannot perform the operation when the specified HAVIP is in the Available or InUse state. |
| 400 | CountLimitExceed.Ha VipRouteEntry | There can be 5 route entry to HaVip at most in one route table. | The error message returned because the number of route entries that point to the HAVIP reaches the upper limit. |
| 400 | InvalidRouteEntry.Du plicate | The route entry already exist. | The error message returned because the specified route entry already exists. |
| 403 | IncorrectInstanceSta tus | The current status of the resource does not support this operation. | The error message returned because the specified resource is in a state that does not support the operation. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectRouteEntryS tatus | Specified routeEntry status error. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectRouteEntryS tatus | VBR has NotStable route entry. | The error message returned because one or more route entries in the current virtual border router (VBR) are in the Pending or Modifying state. |
| 400 | InvalidParam | The Ecmp routerEntry with router interfaces local vgw vip not match. | The error message returned because the route entry does not match the gateway IP address of the router interface. |
| 400 | INVALID WEIGHT PA _ _ RAM | Specified value of weight invalid | The error message returned because the specified weight is invalid. |
| 400 | FORBIDDEN USE VPC _ _ AS INTERNET GATE _ _ _ WAY | The Specified CIDR must be in vpc CIDR. | The error message returned because the specified CIDR block must be a subset of the VPC CIDR block. |
| 400 | INVALID VPC ID _ _ | The Specified VpcId not match. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidRouteEntrySiz e | The Specified routerEntry size not legal. | The error message returned because you must specify two to four router interfaces as next hops if you want to configure ECMP routing. |
| 400 | InvalidRouteEntry | Specified routeEntry not exist. | The error message returned because the specified route entry does not exist. |

##### 2.1.8.3 DeleteRouteEntry

Deletes a custom route entry from a route table. Descriptions When you call this operation, take note of the following rules: You can delete only a custom route entry that is in the Available state. You cannot delete a custom route entry from a VPC where a vSwitch or a route entry is being created or deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouteEntry | The operation that you want to perform. Set the value to Delet eRout eEnt ry. |
| DestinationCidrBl ock | String | Yes | 10.0.0.0/16 | The destination CIDR block of the route entry. IPv4 and IPv6 CIDR blocks are supported. |
| RouteTableId | String | Yes | vtb- hp37isva36oj7839 j**** | The ID of the route table to which the route entry belongs. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the route table to which the route entry belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteEntryId | String | No | rte- bp1mnnr2al0nao mn**** | The ID of the route entry that you want to delete. |
| NextHopId | String | No | ngw- bp1vpo4l2vd7zef 8o**** | The ID of the next hop. |
| NextHopList.N.Ne xtHopType | String | No | RouterInterface | The next hop type of the equal-cost multi-path routing (ECMP) route. Set the value to Rout erInt erf ace. |
| NextHopList.N.Ne xtHopId | String | No | ri- 2zeo3xzyf38r43c d**** | The ID of the next hop of the ECMP route. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRouteEntry &DestinationCidrBlock=10.0.0.0/16 &RouteTableId=vtb-hp37isva36oj7839j**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteRouteEntryResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteRouteEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingParameter | Either nexthopId or nextHopList should be specified | The error message returned because nexthopId or nextHopList is not set. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 400 | IncorrcetRouteEntryS tatus | Some route entry status blocked this operation. | The error message returned because one or more route entries in the route table are in the Pending or Modifying state. |
| 400 | InvalidCidrBlock.Malf ormed | Specified CIDR block is not valid. | The error message returned because the format of the specified CIDR block is invalid. |
| 404 | InvalidRouteTableId. NotFound | Specified route table does not exist. | The error message returned because the specified route table does not exist. |
| 400 | OperationDenied | Specified operation is denied as route entry type is system. | The error message returned because the specified route entry is a system route entry. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidRouteEntry.No tFound | Route entry not exists. | The error message returned because the specified route entry does not exist. Check whether the specified route entry is valid. |
| 400 | InvalidVRouter.NotF ound | vRouter not exists. | The error message returned because the specified vRouter does not exist. Check whether the specified vRouter is valid. |
| 400 | IncorrectRouteEntryS tatus | Some route entry status blocked this operation. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | IncorrectRouteEntryS tatus | VBR has NotStable route entry. | The error message returned because one or more route entries in the current virtual border router (VBR) are in the Pending or Modifying state. |
| 404 | InvalidVpcId.NotFou nd | Specified value of VpcId is not found in our record. | The error message returned because the specified VPC does not exist. Check whether the specified VPC is valid. |
| 400 | IncorrectRouteEntryS tatus | Specified routeEntry status error. | The error message returned because one or more route entries in the current route table are in the Pending or Modifying state. |
| 400 | Forbbiden | Specified RouteEntry cannot allowed delete by openApi. | The error message returned because you cannot call this operation to delete the specified route entry. |
| 400 | InvalidNextHop | Specified nexthop and nexthop list cannot both null. | The error message returned because the next hop type and next hop list cannot be empty at the same time. |
| 400 | InvalidRouteEntry | Specified routeEntry not exist. | The error message returned because the specified route entry does not exist. |
| 400 | IncorrectVpcStatus | Current VPC status does not support this operation. | The error message returned because the state of the VPC does not support this operation. |

##### 2.1.8.4 DescribeRouteEntryList

Queries information about route entries in a route table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouteEnt ryList | The operation that you want to perform. Set the value to DescribeRout eEnt ryList . |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the route table to which the route entries belong. You can call the DescribeRegions operation to query the most recent region list. |
| RouteTableId | String | Yes | vtb- bp1r9pvl4xen8s9j u**** | The ID of the route table that you want to query. |
| RouteEntryId | String | No | rte- bp1mnnr2al0nao mnp**** | The ID of the route entry that you want to query. |
| DestinationCidrBl ock | String | No | 192.168.2.0/24 | The destination CIDR block of the route entry. IPv4 and IPv6 CIDR blocks are supported. Not e Only Apsara Stack China Site supports IPv6 CIDR blocks. |
| RouteEntryName | String | No | abc | The name of the route entry. |
| IpVersion | String | No | IPv4 | The IP version. Valid values: IPv4: IPv4 IPv6: IPv6 Not e Only Apsara Stack China Site supports IPv6. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouteEntryType | String | No | System | The type of the route entry. Valid values: Cust om: a custom route entry Syst em : a system route entry |
| NextHopId | String | No | vpn- bp10zyaph5cc8b 7c7**** | The ID of the next hop. |
| NextHopType | String | No | Instance | The type of the next hop. Valid values: Inst ance: an Elastic Compute Service (ECS) instance HaVip: a high-availability virtual IP address (HAVIP) VpnGat eway: a VPN gateway Nat Gat eway: a NAT gateway Net workInt erf ace: a secondary elastic network interface (ENI) Rout erInt erf ace: a router interface IPv6Gat eway: an IPv6 gateway Not e Only Apsara Stack China Site supports IPv6 gateways as next hops. |
| MaxResult | Integer | No | 50 | The number of entries to return on each page. Valid values: 20 to 100. Default value: 50. |
| NextToken | String | No | caeba0bbb2be03 f84eb48b699f0a4 **** | The token used to start the next query. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f8 4eb48b699f0a4883 | The token used to start the next query. |
| RequestId | String | 14A07460-EBE7- 47CA-9757- 12CC4761D47A | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouteEntrys | Array of RouteEntry |   | The information about the route entry. |
| RouteEntry |   |   |   |
| Description | String | RouteEntryDescripti on | The description of the vRouter. |
| DestinationCidr Block | String | 10.0.0.0/24 | The destination CIDR block of the route entry. |
| IpVersion | String | IPv4 | The IP version. Valid values: IPv4 : IPv4 IPv6: IPv6 |
| NextHops | Array of NextHop |   | The information about the next hop. |
| NextHop |   |   |   |
| Enabled | Integer | 0 | Indicates whether the route entry is available. Valid values: 0: unavailable 1: available |
| NextHopId | String | vpn- bp10zyaph5cc8b7c7 **** | The ID of the next hop. |
| NextHopRegion Id | String | cn-qingdao-env17- d01 | The ID of the region where the next hop is deployed. |
| NextHopRelate dInfo | Struct |   | The information about the next hop. |
| InstanceId | String | vpc- bp1t36rn9l53iwbsf* *** | The ID of the instance associated with the next hop. |
| InstanceType | String | VPC | The type of the instance associated with the next hop. Valid values: VPC: a virtual private cloud (VPC) VBR: a virtual border router (VBR) |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionId | String | ch-qingdao-env17- d01 | The ID of the region where the next hop is deployed. |
| NextHopType | String | Instance | The type of the next hop. Valid values: Inst ance: an ECS instance HaVip: an HAVIP VpnGat eway: a VPN gateway Nat Gat eway: a NAT gateway Net workInt erf ace: a secondary ENI Rout erInt erf ace: a router interface IPv6Gat eway: an IPv6 gateway Not e Only Alibaba Cloud China Site supports IPv6 gateways as next hops. |
| Weight | Integer | 100 | The weight of the route entry. |
| RouteEntryId | String | rte- bp1mnnr2al0naomn p**** | The ID of the route entry. |
| RouteEntryNam e | String | aaa | The name of the route entry. |
| RouteTableId | String | vtb- bp15w5q90d2rk3bw w**** | The ID of the route table. |
| Status | String | Available | The state of the route entry. Valid values: Pending: being configured Available: available Modif ying: being modified |
| Type | String | Custom | The type of the route entry. Valid values: Cust om: a custom route entry Syst em : a system route entry |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRouteEntryList &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp1r9pvl4xen8s9ju**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRouteEntryListResponse>
  <NextToken>caeba0bbb2be03f84eb48b699f0a4883</NextToken>
  <RequestId>14A07460-EBE7-47CA-9757-12CC4761D47A    </RequestId>
  <RouteEntrys>
        <Status>Available</Status>
        <RouteEntryId>rte-bp1mnnr2al0naomnp****</RouteEntryId>
        <Type>Custom</Type>
        <Description>RouteEntryDescription</Description>
        <RouteTableId>vtb-bp15w5q90d2rk3bww****</RouteTableId>
        <IpVersion>IPv4</IpVersion>
        <RouteEntryName>aaa</RouteEntryName>
        <DestinationCidrBlock>10.0.0.0/24</DestinationCidrBlock>
        <NextHops>
              <NextHopRegionId>cn-qingdao-env17-d01</NextHopRegionId>
              <NextHopType>Instance</NextHopType>
              <NextHopId>vpn-bp10zyaph5cc8b7c7****</NextHopId>
              <Enabled>0</Enabled>
              <Weight>100</Weight>
              <NextHopRelatedInfo>
                    <InstanceId>vpc-bp1t36rn9l53iwbsf****</InstanceId>
                    <RegionId>ch-qingdao-env17-d01</RegionId>
                    <InstanceType>VPC</InstanceType>
              </NextHopRelatedInfo>
        </NextHops>
  </RouteEntrys>
</DescribeRouteEntryListResponse>
```

`JSON` format `{`

```json
    "NextToken": "caeba0bbb2be03f84eb48b699f0a4883",
    "RequestId": "14A07460-EBE7-47CA-9757-12CC4761D47A",
    "RouteEntrys": {
        "Status": "Available",
        "RouteEntryId": "rte-bp1mnnr2al0naomnp****",
        "Type": "Custom",
        "Description": "RouteEntryDescription",
        "RouteTableId": "vtb-bp15w5q90d2rk3bww****",
        "IpVersion": "IPv4",
        "RouteEntryName": "aaa",
        "DestinationCidrBlock": "10.0.0.0/24",
        "NextHops": {
            "NextHopRegionId": "cn-qingdao-env17-d01",
            "NextHopType": "Instance",
            "NextHopId": "vpn-bp10zyaph5cc8b7c7****",
            "Enabled": 0,
            "Weight": 100,
            "NextHopRelatedInfo": {
                "InstanceId": "vpc-bp1t36rn9l53iwbsf****",
                "RegionId": "ch-qingdao-env17-d01",
                "InstanceType": "VPC"
```

`}` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Required |
|---|---|---|---|
| 400 | OperationFailed.Que ryCenEntry | Operation is denied because getting CEN route entry has failed. | The error message returned because the system cannot obtain the Cloud Enterprise Network (CEN) routes. |

##### 2.1.8.5 ModifyRouteEntry

Modifies the name and description of a custom route entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouteEntry | The operation that you want to perform. Set the value to Modif yRout eEnt ry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the route entry belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteEntryId | String | Yes | rte- acfvgfsghfdd**** | The ID of the custom route entry. |
| RouteEntryName | String | No | EntryName | The name of the route entry. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with http:// or https:// . |
| Description | String | No | EntryDescription | The description of the route entry. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |

|   | http:// |
|---|---|
| https:// |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 861E6630-AEC0- 4B2D-B214- 6CB5E44B7F04 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRouteEntry &RegionId=cn-qingdao-env17-d01 &RouteEntryId=rte-acfvgfsghfdd**** &<Common request parameters>
```

Sample success response `XML` format

```xml
<ModifyRouteEntryResponse>
    <RequestId>861E6630-AEC0-4B2D-B214-6CB5E44B7F04</RequestId>
</ModifyRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId": "861E6630-AEC0-4B2D-B214-6CB5E44B7F04"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the permissions and try again. |
| 400 | InvalidRouteEntryId. NotFound | The specified routeEntry does not exist. | The error message returned because the specified route entry does not exist. |

##### 2.1.8.6 AssociateRouteTable

Associates a custom route table with a vSwitch in the same virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateRouteT able | The operation that you want to perform. Set the value to Associat eRout eT able. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the VPC to which the route table belongs. You can call the DescribeRegions operation to the most recent region list. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzdv zu2**** | The ID of the route table. |
| VSwitchId | String | Yes | vsw- 25ncdvfaue4**** | The ID of the vSwitch. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC668356-BCB4- 42FD-9BC3- FA2B2E04B634 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateRouteTable &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp145q7glnuzdvzu2**** &VSwitchId=vsw-25ncdvfaue4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateRouteTableResponse>
  <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
</AssociateRouteTableResponse>
```

`JSON` format

```json
{"RequestId":"DC668356-BCB4-42FD-9BC3-FA2B2E04B634"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRouteTableId. NotFound | Specified route table does not exist. | The error message returned because the specified route table does not exist. |

##### 2.1.8.7 DeleteRouteTable

Deletes a custom route table. Descriptions Before you delete a custom route table, disassociate the vSwitch that is associated with the custom route table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouteTabl e | The operation that you want to perform. Set the value to Delet eRout eT able. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the virtual private cloud (VPC) to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzdv zu2**** | The ID of the route table to be deleted. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DC668356-BCB4- 42FD-9BC3- FA2B2E04B634 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRouteTable &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp145q7glnuzdvzu2**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteRouteTableResponse>
      <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
</DeleteRouteTableResponse>
```

`JSON` format `{`

```json
  "RequestId": "DC668356-BCB4-42FD-9BC3-FA2B2E04B634"
```

`}` Error codes

| HttpCode | Error code | Error message | Required |
|---|---|---|---|
| 400 | IncorrectVSwitchSta tus | The current virtual switch status does not support this operation. | The error message returned because the vSwitch is in the Pending state and cannot be deleted. |

##### 2.1.8.8 DescribeRouteTableList

Queries the list of route tables. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouteTa bleList | The operation that you want to perform. Set the value to DescribeExport erRuleList . |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the virtual private cloud (VPC) to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouterType | String | No | VBR | The ID of the vRouter to which the route table belongs. Set the value to: VRout er (default): a vRouter VBR: a virtual border router (VBR) |
| RouterId | String | No | vrt- bp1lhl0taikrteen8 **** | The ID of the vRouter to which the route table belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpcId | String | No | vpc- bp15zckdt37pq7 2**** | The ID of the vRouter to which the route table belongs. After you set this parameter, Rout erT ype is automatically set to VRout er. |
| RouteTableId | String | No | vtb- bp145q7glnuzdv zu2**** | The ID of the route table that you want to query. |
| RouteTableName | String | No | doctest | The name of the route table that you want to query. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| ResourceGroupId | String | No | rg- acfmxazb4ph**** | The ID of the resource group to which the route table to be queried belongs. |
| Tag.N.Key | String | No | Key1 | The key of the tag. |
| Tag.N.Value | String | No | Value1 | The value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The response code. Not e The HTTP status code 200 indicates that the call was successful. |
| Message | String | The Request is not authorization. | The returned message. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | DC668356-BCB4- 42FD-9BC3- FA2B2E04B634 | The ID of the instance. |
| RouterTableList | Array of RouterTableList Type |   | The list of route tables. |
| RouterTableList Type |   |   |   |
| CreationTime | String | 2017-08- 22T10:40:25Z | The time when the route table was created. |
| Description | String | This is Route Table. | The description of the route table. |
| OwnerId | Long | 12345678 | The ID of the Apsara Stack tenant account to which the route table belongs. |
| ResourceGroupI d | String | rg-acfmxazb4ph**** | The ID of the resource group to which the route table belongs. |
| RouteTableId | String | vtb- bp145q7glnuzdvzu2 **** | The ID of the route table. |
| RouteTableNa me | String | doctest | The name of the route table. |
| RouteTableTyp e | String | System | The type of the route table. Cust om: a custom route table Syst em : a system route table |
| RouterId | String | vrt- bp1lhl0taikrteen8*** * | The ID of the router to which the route table belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouterType | String | VBR | The type of the router to which the route table belongs. Valid values: VRout er: a vRouter VBR: a virtual border router (VBR) |
| Status | String | Available | The state of the route table. Pending: The route table is being configured. Available: The route table is available. |
| Tags | Array of Tag |   | The tag of the route table. |
| Tag |   |   |   |
| Key | String | type | The key of the tag that is added to the route table. |
| Value | String | ingress | The value of the tag that is added to the route table. |
| VSwitchIds | List | vsw- bp12mw1f8k3jgygk 9**** | The list of vSwitches deployed in the VPC. |
| VpcId | String | vpc- bp15zckdt37pq72** ** | The ID of the VPC to which the route table belongs. |
| Success | Boolean | true | Indicates whether the call is successful. Valid values: t rue: The call is successful. f alse: The call fails. |
| TotalCount | Integer | 1 | The number of entries to return. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRouteTableList &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRouteTableListResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <Message>The Request is not authorization.</Message>
  <RequestId>DC668356-BCB4-42FD-9BC3-FA2B2E04B634</RequestId>
  <PageNumber>1</PageNumber>
  <RouterTableList>
        <Status>Available</Status>
        <Description>This is Route Table.</Description>
        <RouteTableId>vtb-bp145q7glnuzdvzu2****</RouteTableId>
        <OwnerId>12345678</OwnerId>
        <ResourceGroupId>rg-acfmxazb4ph****</ResourceGroupId>
        <VpcId>vpc-bp15zckdt37pq72****</VpcId>
        <RouterType>VBR</RouterType>
        <CreationTime>2017-08-22T10:40:25Z</CreationTime>
        <RouterId>vrt-bp1lhl0taikrteen8****</RouterId>
        <RouteTableType>System</RouteTableType>
        <RouteTableName>doctest</RouteTableName>
        <Tags>
              <Value>ingress</Value>
              <Key>type</Key>
        </Tags>
        <VSwitchIds>vsw-bp12mw1f8k3jgygk9****</VSwitchIds>
  </RouterTableList>
  <Code>200</Code>
  <Success>true</Success>
</DescribeRouteTableListResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "Message": "The Request is not authorization.",
    "RequestId": "DC668356-BCB4-42FD-9BC3-FA2B2E04B634",
    "PageNumber": 1,
    "RouterTableList": {
        "Status": "Available",
        "Description": "This is Route Table.",
        "RouteTableId": "vtb-bp145q7glnuzdvzu2****",
        "OwnerId": 12345678,
        "ResourceGroupId": "rg-acfmxazb4ph****",
        "VpcId": "vpc-bp15zckdt37pq72****",
        "RouterType": "VBR",
        "CreationTime": "2017-08-22T10:40:25Z",
        "RouterId": "vrt-bp1lhl0taikrteen8****",
        "RouteTableType": "System",
        "RouteTableName": "doctest",
        "Tags": {
            "Value": "ingress",
            "Key": "type"
```

`},`

```json
        "VSwitchIds": "vsw-bp12mw1f8k3jgygk9****"
```

`},`

```json
    "Code": 200,
    "Success": true
```

`}` Error codes

| HttpCode | Error code | Error message | Description. |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are not authorized to perform this operation on the specified resource. You can apply for the permissions and try again. |

##### 2.1.8.9 UnassociateRouteTable

Disassociates a route table from a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateRout eTable | The operation that you want to perform. Set the value to Unassociat eRout eT able. |

|   | Developer Guide·API r | eference |   |   | Virtual Private Clou | d |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the virtual private cloud (VPC) to which the route table belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouteTableId | String | Yes | vtb- bp145q7glnuzdv zu2**** | The ID of the route table. |
| VSwitchId | String | Yes | vsw- 25naucfvfbgte4** ** | The ID of the vSwitch from which you want to disassociate the route table. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 62172DD5-6BAC- 45DF-8D44- 62172DD5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateRouteTable &RegionId=cn-qingdao-env17-d01 &RouteTableId=vtb-bp145q7glnuzdvzu2**** &VSwitchId=vsw-25naucfvfbgte4**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateRouteTableResponse>
      <RequestId>62172DD5-6BAC-45DF-8D44-62172DD5</RequestId>
</UnassociateRouteTableResponse>
```

`JSON` format `{`

```json
  "RequestId": "62172DD5-6BAC-45DF-8D44-62172DD5"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRouteTableId. NotFound | Specified route table does not exist. | The error message returned because the specified route table does not exist. |

#### 2.1.9 Region

##### 2.1.9.1 DescribeRegions

Queries the most recent region list. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |
| ProductType | String | No | ECS | The type of the cloud service. |
| AcceptLanguage | String | No | zh-CN | The language of the response. Valid values: zh-CN: Chinese. This is the default value. en-US: English |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | The list of regions. |
| Region |   |   |   |
| LocalName | String | China (Qingdao) | The name of the region. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RegionEndpoint | String | vpc.aliyuncs.com | The endpoint of the region. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region. |
| RequestId | String | 611CB80C-B6A9- 43DB-9E38- 0B0AC3D9B58F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRegionsResponse>
  <RequestId>611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F</RequestId>
  <Regions>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <RegionEndpoint>vpc.aliyuncs.com</RegionEndpoint>
        <LocalName>China (Qingdao)</LocalName>
  </Regions>
</DescribeRegionsResponse>
```

`JSON` format `{`

```json
    "RequestId": "611CB80C-B6A9-43DB-9E38-0B0AC3D9B58F",
    "Regions": {
        "RegionId": "cn-qingdao-env17-d01",
        "RegionEndpoint": "vpc.aliyuncs.com",
        "LocalName": "China (Qingdao)"
```

`}` `}`

##### 2.1.9.2 DescribeZones

Queries zones in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where zones are queried. You can call the DescribeRegions operation to the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array of Zone |   | The zones that are returned. |
| Zone |   |   |   |
| LocalName | String | Hangzhou Zone | The name of the zone. |
| ZoneId | String | cn-cn-qingdao- env17- amtest11001-a | The ID of the zone. |
| RequestId | String | 6FEA0CF3-D3B9- 43E5-A304- D217037876A8 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeZones &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeZonesResponse>
  <RequestId>6FEA0CF3-D3B9-43E5-A304-D217037876A8</RequestId>
  <Zones>
        <ZoneId>cn-cn-qingdao-env17-amtest11001-a</ZoneId>
        <LocalName>Hangzhou Zone B</LocalName>
  </Zones>
</DescribeZonesResponse>
```

`JSON` format `{`

```json
    "RequestId": "6FEA0CF3-D3B9-43E5-A304-D217037876A8",
    "Zones": {
        "ZoneId": "cn-cn-qingdao-env17-amtest11001-a",
        "LocalName": "Hangzhou Zone B"
```

`}` `}`

#### 2.1.10 Tag

##### 2.1.10.1 TagResources

Creates tags and adds the tags to resources at a time. Descriptions Tags are used to classify instances. Each tag consists of a key and a value. To use tags, make sure that the following requirements are met: The keys of tags that are added to the same instance must be unique. You cannot create tags without adding them to instances. All tags must be added to instances. Tag information is not shared across regions. Virtual private clouds (VPCs), route tables, vSwitches, and elastic IP addresses (EIPs) that belong to the same Apsara Stack tenant account and in the same region share tag information with each other. For example, if you have added a tag to a VPC, the tag is available to vSwitches, route tables, and EIPs that belong to the same account and in the same region where the VPC is created. You can select this tag from the editing page without the need to enter the tag again. You can modify the key and value of a tag or remove a tag from an instance. After you delete an instance, all tags that are added to the instance are deleted. You can add up to 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TagResources | The operation that you want to perform. Set the value to T agResources. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the resource belongs. |

| irtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ResourceId.N | RepeatLi st | Yes | vpc- bp16qjewdsunr4 1m1**** | The ID of the resource. Valid values of N: 1 to 20. |
| ResourceType | String | Yes | VPC | The type of the resource. Valid values: VPC: a VPC VSWIT CH: a vSwitch ROUT ET ABLE: a route table EIP: an elastic IP address (EIP) |
| Tag.N.Key | String | No | FinanceDept | The key of the tag that is added to the resource. Valid values of N: 1 to 20. This parameter value cannot be an empty string. The key can be up to 64 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter but cannot start with aliyun or acs: . It cannot contain http:// or https:// . |
| Tag.N.Value | String | No | FinanceJoshua | The value of tag N that is added to the resource. Valid values of N: 1 to 20. The key can be an empty string. The tag value must be up to 128 characters in length, and start with a letter. It can contain digits, periods (.), underscores ( ), and hyphens (-). It cannot start _ with aliyun or acs: . It cannot contain http:// or https:// . |

| acs: |   |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C46FF5A8-C5F0- 4024-8262- B16B639225A0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=TagResources &RegionId=cn-qingdao-env17-d01 &ResourceId.1=vpc-bp16qjewdsunr41m1**** &ResourceType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TagResourcesResponse>
      <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
</TagResourcesResponse>
```

`JSON` format `{`

```json
 "RequestId":"C46FF5A8-C5F0-4024-8262-B16B639225A0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To obtain the required permissions, submit a ticket. |

##### 2.1.10.2 ListTagResources

Queries tags that are added to one or more instances. Descriptions Set ResourceId.N or T ag.N t hat consist s of T ag.N.Key and T ag.N.Value in the request to specify the object to be queried. T ag.N is a resource tag that consists of a key-value pair. If you set only T ag.N.Key, all tag values that are associated with the specified key are returned. If you set only T ag.N.Value, an error message is returned. If you set T ag.N and ResourceId.N to filter tags, ResourceId.N must match all specified key-value pairs. If you specify multiple key-value pairs, resources that contain these key-value pairs are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListTagResources | The operation that you want to perform. Set the value to List T agResources. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the resource belongs. |
| ResourceType | String | Yes | VPC | The type of the resource. Valid values: VPC: a VPC VSWIT CH: a vSwitch ROUT ET ABLE: a route table EIP: an elastic IP address (EIP) |
| ResourceId.N | RepeatLi st | No | vpc- bp16qjewdsunr4 1m1**** | The ID of the resource. Valid values of N: 1 to 20. |
| Tag.N.Key | String | No | FinanceDept | The key of the tag that is added to the resource. Valid values of N: 1 to 20. It cannot be an empty string. The key can be up to 64 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter but cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tag.N.Value | String | No | FinanceJoshua | The value of tag N that is added to the resource. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value must be up to 128 characters in length, and start with a letter or Chinese character. It can contain digits, periods (.), underscores ( ), and hyphens (-) and cannot start _ with aliyun or acs: . It cannot contain http:// or https:// . |
| NextToken | String | No | caeba0bbb2be03 f84eb48b699f0a* *** | The query token. Set this parameter to the NextToken value that is returned in the last API call. If no subsequent request is sent, you do not need to set this parameter. |
| MaxResults | Integer | No | 10 | The maximum number of entries to return. |

| acs: |   |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | caeba0bbb2be03f8 4eb48b699f0**** | The token that is required for the next query. If the Next T oken parameter is empty, no subsequent request will be sent. |
| RequestId | String | DE65F6B7-7566- 4802-9007- 96F2494AC512 | The ID of the request. |
| TagResources | Array of TagResource |   | The resources to which the tags are added. |
| TagResource |   |   |   |
| ResourcId | String | vpc- bp16qjewdsunr41m 1**** | The ID of the resource. |
| ResourceId | String | 2zebd226fxed6h4i** ** | The ID of the resource. |
| ResourceType | String | VPC | The type of the resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TagKey | String | FinanceDept | The key of the tag. |
| TagValue | String | FinanceJoshua | The value of the tag. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ListTagResources &RegionId=cn-qingdao-env17-d01 &ResourceType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ListTagResourcesResponse>
  <NextToken>caeba0bbb2be03f84eb48b699f0****</NextToken>
  <RequestId>DE65F6B7-7566-4802-9007-96F2494AC512</RequestId>
  <TagResources>
        <ResourceId>2zebd226fxed6h4i****</ResourceId>
        <TagKey>FinanceDept</TagKey>
        <ResourceType>VPC</ResourceType>
        <ResourcId>vpc-bp16qjewdsunr41m1****</ResourcId>
        <TagValue>FinanceJoshua</TagValue>
  </TagResources>
</ListTagResourcesResponse>
```

`JSON` format `{`

```json
    "NextToken": "caeba0bbb2be03f84eb48b699f0****",
    "RequestId": "DE65F6B7-7566-4802-9007-96F2494AC512",
    "TagResources": {
        "ResourceId": "2zebd226fxed6h4i****",
        "TagKey": "FinanceDept",
        "ResourceType": "VPC",
        "ResourcId": "vpc-bp16qjewdsunr41m1****",
        "TagValue": "FinanceJoshua"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To obtain the required permissions, submit a ticket. |

##### 2.1.10.3 UnTagResources

Removes tags from specified resources. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnTagResources | The operation that you want to perform. Set the value to Unt agResources. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the resource belongs. |
| ResourceId.N | RepeatLi st | Support ed | vpc- bp16qjewdsunr4 1m1**** | The ID of the resource. Valid values of N: 1 to 20. |
| ResourceType | String | Yes | VPC | The type of the resource. Valid values: VPC: a virtual private cloud (VPC) VSWIT CH: a vSwitch ROUT ET ABLE: a route table EIP: an elastic IP address (EIP) |
| TagKey.N | RepeatLi st | No | FinanceDept | The key of the tag that you want to remove. Valid values of N: 1 to 20. The key can be an empty string. The key can be up to 64 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter but cannot start with aliyun or acs: . It cannot contain http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| All | Boolean | No | false | Specifies whether to remove all tags from the resource. This parameter takes effect only when the T agKey.N parameter is not set in the request. Valid values: t rue: removes all tags from the resource. f alse(default): does not remove tags. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C46FF5A8-C5F0- 4024-8262- B16B639225A0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnTagResources &RegionId=cn-qingdao-env17-d01 &ResourceId.1=vpc-bp16qjewdsunr41m1**** &ResourceType=VPC &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UntagResourcesResponse>
      <RequestId>C46FF5A8-C5F0-4024-8262-B16B639225A0</RequestId>
</UntagResourcesResponse>
```

`JSON` format `{`

```json
 "RequestId":"C46FF5A8-C5F0-4024-8262-B16B639225A0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To obtain the required permissions, submit a ticket. |

#### 2.1.11 BGP

##### 2.1.11.1 DescribeBgpGroups

Queries Border Gateway Protocol (BGP) groups in a region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpGrou ps | The operation that you want to perform. Set the value to DescribeBgpGroups. |
| RegionId | String | Yes | cn-shanghai | The region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | No | vrt- kojok19x3j0q6kx | The ID of the virtual border router (VBR) that is associated with the BGP group. |
| BgpGroupId | String | No | bgpg- wz9f62v4fbg2gx xxxxxxx | The ID of the BGP group. |
| IsDefault | Boolean | No | false | Specifies whether the specified BGP group is the default one. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 10 | The total number of entries. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| BgpGroups | Array of BgpGroup |   | The detailed information about the BGP group. |
| BgpGroup |   |   |   |
| AuthKey | String | ! PWZ2wsq | The key used by the BGP group. |
| BgpGroupId | String | bgp- wz977wcrmb69axxx xxxxx | The ID of the BGP group. |
| Description | String | The description of the BGP group. | The description of the BGP group |
| Hold | String | 30 | The hold time of the BGP connection. If no message is received within the hold time, the BGP peer is considered disconnected. |
| IpVersion | String | IPv4 |   |
| IsFake | String | true | Whether the autonomous system (AS) number is valid. |
| Keepalive | String | 10 | The keepalive time. |
| LocalAsn | String | 45104 | The local AS number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | The name of the BGP group | The name of the BGP group. |
| PeerAsn | String | 1111 | The AS number of the BGP peer. |
| RegionId | String | cn-shanghai | The ID of the region to which the BGP group belongs. For more information about region IDs, see Regions and zones. |
| RouteLimit | String | 99 | Routing limits. |
| RouterId | String | vrt- bp1lhl0taikrteen**** * | The ID of the VBR. |
| Status | String | active | The status of the BGP peer. |
| RequestId | String | 1D0971B2-A35A- 42C1-A44C- E91360C36C0B | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeBgpGroups &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpGroupsResponse>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>09E2C0FD-37FF-4737-80DF-517AC36D43DB</RequestId>
   <BgpGroups>
      <BgpGroup>
         <BgpGroupId>bgpg-2zev8h2wo4******</BgpGroupId>
         <LocalAsn>45104</LocalAsn>
         <Hold>30</Hold>
         <Description></Description>
         <AuthKey></AuthKey>
         <IsFake>true</IsFake>
         <PeerAsn>234</PeerAsn>
         <Keepalive>10</Keepalive>
         <RouteLimit>99</RouteLimit>
         <Name>Group1</Name>
         <Status>Pending</Status>
         <RouterId>vbr-2zecmmvg5gvu8i4******</RouterId>
         <RegionId>cn-beijing</RegionId>
      </BgpGroup>
   </BgpGroups>
</DescribeBgpGroupsResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "09E2C0FD-37FF-4737-80DF-517AC36D43DB",
    "BgpGroups": {
        "BgpGroup": [
```

`{`

```json
                "BgpGroupId": "bgpg-2zev8h2wo******",
                "LocalAsn": 45104,
                "Hold": 30,
                "Description": "",
                "AuthKey": "",
                "IsFake": true,
                "PeerAsn": 234,
                "Keepalive": 10,
                "RouteLimit": 99,
                "Name": "Group1",
                "Status": "Pending",
                "RouterId": "vbr-2zecmmvg5gvu8i4*****",
                "RegionId": "cn-beijing"
```

`}` `]` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because unknown errors occur. |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

##### 2.1.11.2 ModifyBgpGroupAttribute

Modifies the configuration of a Border Gateway Protocol (BGP) group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBgpGroup Attribute | The operation that you want to perform. Set the value to Modif yBgpGroupAt t ribut e. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg2g** ****** | The ID of the BGP group. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the BGP group is deployed. You can call the DescribeRegions operation to query region IDs. |
| Name | String | No | test | The name of the BGP group. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| Description | String | No | BGP | The description of the BGP group. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LocalAsn | Long | No | 23 | The autonomous system (AS) number of the device on the cloud side. |
| PeerAsn | Long | No | 1111 | The AS number of the local device. |
| AuthKey | String | No | ! PWZ2wsq | The authentication key of the BGP group. |
| IsFakeAsn | Boolean | No | true | A router that runs BGP typically belongs to only one AS. In some cases, for example, the AS needs to be migrated or is merged with another AS, a new AS number replaces of the original one. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001******* | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C3C6D7C-A1CE- 4FD8-BC57- DC493A55F76F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyBgpGroupAttribute &BgpGroupId=bgpg-wz9f62v4fbg2g******** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBgpGroupAttributeResponse>
      <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
</ModifyBgpGroupAttributeResponse>
```

`JSON` format `{`

```json
  "RequestId": "C1221A1F-2ACD-4592-8F27-474E02883159"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has exceeded the upper limit. |
| 400 | QuotaExceeded.Bgp Network | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR ID is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Mal formed | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidBgpDiscription .Malformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.M alformed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malfo rmed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFo und | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.Alread yExists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.Cannot Operate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

##### 2.1.11.3 DeleteBgpGroup

Deletes a Border Gateway Protocol (BGP) group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpGroup | The operation that you want to perform. Set the value to Delet eBgpGroup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg2gx xxxxxxx | The ID of the BGP group. |
| RegionId | String | Yes | cn-shanghai | The region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 97E2E97F-968C- 48AF-A310- AC4D068854DB | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteBgpGroup &BgpGroupId=bgpg-wz9f62v4fbg2gxxxxxxxx &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpGroupResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBgpGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The Network Quality Analyzer (NQA) number has exceeded the quota of the VBR. |
| 400 | QuotaExceeded.Bgp Network | bgp network count per vbr quota exceed. | The number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified vRouter does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Mal formed | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription .Malformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.M alformed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidPeerAsn.Malfo rmed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNu ll | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFo und | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.Alread yExists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.Cannot Operate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

##### 2.1.11.4 DescribeBgpPeers

Queries BGP peers in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpPeers | The operation that you want to perform. Set the value to DescribeBgpPeers. |
| RegionId | String | Yes | cn-shanghai | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouterId | String | No | vbr- 2zecmmvg5gvu8i 4te**** | The ID of the router. |
| BgpPeerId | String | No | bgp- 2ze3un0ft1jd1xd* **** | The ID of the BGP peer. |
| BgpGroupId | String | No | bgpg- 2zev8h2wo414sf h****** | The ID of the BGP group. |
| IsDefault | Boolean | No | false | Specifies whether the BGP group is the default one. t rue: yes f alse: no |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpPeers | Array of BgpPeer |   | The detailed information about the BGP peer. |
| BgpPeer |   |   |   |
| Name | String | test | The name of the BGP peer. |
| PeerIpAddress | String | 116.62.**. ** | The IP address of the BGP peer. |
| AuthKey | String | ! PWZ2wsq****** | The authentication key of the BGP group. |
| RouterId | String | vbr- 2zecmmvg5gvu8i4t e****w | The ID of the router. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | active | The state of the BGP peer. Valid values: Pending: pending. Available: available. Modif ying: being modified. Delet ing: being deleted. Delet ed: deleted. |
| BfdMultiHop | Integer | 3 |   |
| BgpGroupId | String | bgp- wz977wcrmb69***** ** | The ID of the BGP group. |
| BgpPeerId | String | bgp- wz977wcrmb69agd b****** | The ID of the BGP peer. |
| BgpStatus | String | deleted | The state of the BGP connection. Valid values: creat ing: being created. working: being used. modif ying: being modified. delet ing: being deleted. Delet ed: deleted. |
| Description | String | xxxxxxxxx | The description of the BGP group. |
| EnableBfd | Boolean | true | Indicates whether the Bidirectional Forwarding Detection (BFD) protocol is enabled. |
| Hold | String | 30 | The hold time of the BGP connection. |
| IpVersion | String | IPv4 |   |
| IsFake | String | true | Indicates whether a fake autonomous system (AS) number is used. |
| Keepalive | String | 10 | The hold time of the BGP connection. |
| LocalAsn | String | 45104 | The local AS number. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PeerAsn | String | active | The AS number of the BGP peer. |
| RegionId | String | cn-shanghai | The ID of the region to which the BGP group belongs. |
| RouteLimit | String | 99 | Routing limits. |
| TotalCount | Integer | 10 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| RequestId | String | DE77A7F3-3B74- 41C0-A5BC- CAFD188C28B6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeBgpPeers &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpPeersResponse>
  <TotalCount>10</TotalCount>
  <BgpPeers>
        <Status>active</Status>
        <Description>xxxxxxxxx</Description>
        <IpVersion>IPv4</IpVersion>
        <PeerIpAddress>116.62. **. **</PeerIpAddress>
        <Keepalive>10</Keepalive>
        <RouterId>vbr-2zecmmvg5gvu8i4te****w</RouterId>
        <PeerAsn>active</PeerAsn>
        <Name>test</Name>
        <BgpPeerId>bgp-wz977wcrmb69agdb******</BgpPeerId>
        <LocalAsn>45104</LocalAsn>
        <BfdMultiHop>3</BfdMultiHop>
        <EnableBfd>true</EnableBfd>
        <BgpStatus>deleted</BgpStatus>
        <IsFake>true</IsFake>
        <AuthKey>! PWZ2wsq******</AuthKey>
        <RouteLimit>99</RouteLimit>
        <RegionId>cn-shanghai</RegionId>
        <Hold>30</Hold>
        <BgpGroupId>bgp-wz977wcrmb69*******</BgpGroupId>
  </BgpPeers>
  <PageSize>2</PageSize>
  <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId>
  <PageNumber>1</PageNumber>
</DescribeBgpPeersResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "BgpPeers": {
        "Status": "active",
        "Description": "xxxxxxxxx",
        "IpVersion": "IPv4",
        "PeerIpAddress": "116.62. **. **",
        "Keepalive": 10,
        "RouterId": "vbr-2zecmmvg5gvu8i4te****w",
        "PeerAsn": "active",
        "Name": "test",
        "BgpPeerId": "bgp-wz977wcrmb69agdb******",
        "LocalAsn": 45104,
        "BfdMultiHop": 3,
        "EnableBfd": true,
        "BgpStatus": "deleted",
        "IsFake": true,
        "AuthKey": "! PWZ2wsq******",
        "RouteLimit": 99,
        "RegionId": "cn-shanghai",
        "Hold": 30,
        "BgpGroupId": "bgp-wz977wcrmb69*******"
```

`},`

```json
    "PageSize": 2,
    "RequestId": "DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6",
    "PageNumber": 1
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because unknown errors occur. |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

##### 2.1.11.5 DeleteBgpPeer

Deletes a specific Border Gateway Protocol (BGP) peer. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpPeer | The operation that you want to perform. Set the value to Delet eBgpPeer. |
| BgpPeerId | String | Yes | bgp- wz977wcrmb69a ******** | The ID of the BGP peer. |
| RegionId | String | Yes | cn-shanghai | The region to which the BGP group belongs. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001xxxxxxxx | The client token that is used to ensure the idempotence of the request. The value of this parameter is generated by a client. The value must be unique among different requests and must be 1 to 64 ASCII characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AEBB1EB6-3C15- 4A35-B4CE- 03485200C143 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteBgpPeer &BgpPeerId=bgp-wz977wcrmb69a******** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpPeerResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBgpPeerResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | Specified value of "regionId" is not supported. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The Network Quality Analyzer (NQA) number exceeds the virtual border router (VBR) quota. |
| 400 | QuotaExceeded.Bgp Network | bgp network count per vbr quota exceed. | The number of BGP networks in the VBR has reached the quota. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Mal formed | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription .Malformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.M alformed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |

| eveloper Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |
| 400 | InvalidPeerAsn.Malfo rmed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNu ll | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFo und | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.Alread yExists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.Cannot Operate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

##### 2.1.11.6 AddBgpNetwork

Advertises a Border Gateway Protocol (BGP) network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBgpNetwork | The operation that you want to perform. Set the value to AddBgpNet work. |
| DstCidrBlock | String | Yes | 10.10.**. **/32 | The CIDR block of the virtual private cloud (VPC) or vSwitch that you want to connect to a data center. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The ID of the region where the virtual border router (VBR) is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | Yes | vrt- 2zeo3xzyf38r4u** **** | The ID of the vRouter associated with the router interface. |
| VpcId | String | No | vpc- bp1qpo0kug3a2* **** | The ID of the VPC. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9C7FA9D6-72E0- 48A9-A9C3- 2DA8569CD5EB | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=AddBgpNetwork &DstCidrBlock=10.10. **. **/32 &RegionId=cn-shanghai &RouterId=vrt-2zeo3xzyf38r4u****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBgpNetworkResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</AddBgpNetworkResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the quota. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number exceeds the VBR quota. |
| 400 | QuotaExceeded.Bgp Network | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the quota. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified vRouter does not exist. Check whether the ID of the VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Mal formed | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription .Malformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidBgpAuthkey.M alformed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malfo rmed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNu ll | parameter must not null. | The error message returned because a required parameter is not set. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFo und | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.Alread yExists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.Cannot Operate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the quota. |

##### 2.1.11.7 DeleteBgpNetwork

Deletes an advertised Border Gateway Protocol (BGP) network. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpNetwo rk | The operation that you want to perform. Set the value to Delet eBgpNet work. |
| DstCidrBlock | String | Yes | 10.110.192.12/32 | The CIDR block of the virtual private cloud (VPC) or vSwitch that you want to connect to a data center. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the BGP group is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | Yes | vrt- bp1lhl0taikrteen8 0oxx | The ID of the virtual border router (VBR). |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 22F4C006-D3BB- 4F96-9FF9- 4C8335276D70 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteBgpNetwork &DstCidrBlock=10.110.192.12/32 &RegionId=cn-hangzhou &RouterId=vrt-bp1lhl0taikrteen80oxx &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpNetworkResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteBgpNetworkResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | Specified value of "regionId" is not supported. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has exceeded the upper limit. |
| 400 | QuotaExceeded.Bgp Network | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR ID is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Mal formed | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |

| eveloper Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidBgpDiscription .Malformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.M alformed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malfo rmed | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNu ll | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the instance does not exist. |
| 400 | InvalidParams.NotFo und | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.Alread yExists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.Cannot Operate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |

##### 2.1.11.8 DescribeBgpNetworks

Queries advertised Border Gateway Protocol (BGP) networks. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpNetw orks | The operation that you want to perform. Set the value to DescribeBgpNet works. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the BGP group is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | No | vrt- 2zeazning6tb**** **** | The ID of the vRouter to which the route table belongs. |
| PageNumber | Integer | No | 2 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpNetworks | Array of BgpNetwork |   | BGP networks. |
| BgpNetwork |   |   |   |
| DstCidrBlock | String | 10.1.**. **/24 | The advertised BGP network. |
| RouterId | String | vrt- bp1el837xkkak****** ** | The ID of the vRouter. |
| Status | String | Enabled | The state of the advertised BGP network. |
| VpcId | String | vpc- bp1qpo0kug3a****** ** | The ID of the virtual private cloud (VPC). |
| PageNumber | Integer | 2 | The page number of the returned page. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 12 | The number of entries returned per page. |
| RequestId | String | 6F513A15-669F- 419D-B511- 08A85292059B | The ID of the request. |
| TotalCount | Integer | 2 | The total number of advertised BGP networks. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeBgpNetworks &RegionId=cn-hangzhou &RouterId=vrt-2zeazning6tb******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpNetworksResponse>
      <BgpNetworks>
            <BgpNetwork>
                  <DstCidrBlock>192.168. **. **/24</DstCidrBlock>
                  <VpcId></VpcId>
            </BgpNetwork>
      </BgpNetworks>
      <RequestId>6F513A15-669F-419D-B511-08A85292059B</RequestId>
      <PageSize>10</PageSize>
      <TotalCount>1</TotalCount>
</DescribeBgpNetworksResponse>
```

`JSON` format `{`

```json
  "BgpNetworks": {
    "BgpNetwork": [
```

`{`

```json
        "DstCidrBlock": "192.168. **. **/24",
        "VpcId": ""
```

`}` `]` `},`

```json
  "RequestId": "6F513A15-669F-419D-B511-08A85292059B",
  "PageSize": 10,
  "TotalCount": 1
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because unknown errors have occurred. |
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

#### 2.1.12 VBR

##### 2.1.12.1 CreateVirtualBorderRouter

Creates a virtual border router (VBR). If you create a VBR for the current Apsara Stack tenant account, the state of the VBR becomes Enabledafter it is created. If you create a VBR for another Apsara Stack tenant account, the state of the VBR becomes Unconf irmed after it is created. The Unconfirmed state indicates that the other Apsara Stack tenant account must confirm the operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVirtualBord erRouter | The operation that you want to perform. Set the value to Creat eVirt ualBorderRout er. |
| PhysicalConnectio nId | String | Yes | pc-xxxxxxxxx | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VlanId | Integer | Yes | 10 | The VLAN ID of the VBR. Valid values: 1 t o 2999. Not e Only the owner of the physical connection can set this parameter. The VLAN IDs of two VBRs of the same physical connection must be different. |
| VbrOwnerId | Long | No | 10 | The ID of the Apsara Stack tenant account that owns the VBR. The default value is the ID of the current Apsara Stack tenant account, which is the owner of the physical connection. |
| CircuitCode | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) of the physical connection. Not e Only the owner of the physical connection can set this parameter. |
| LocalGatewayIp | String | No | 116.62.222.XX | The IP address of the local VBR on the Apsara Stack side. |
| PeerGatewayIp | String | No | 116.62.222.XX | The IP address of the VBR peer. This parameter can be set only in the following scenario: The owner of the physical connection is creating a VBR for the current Apsara Stack tenant account. |
| PeeringSubnetMa sk | String | No | 255.255.255.252 | The subnet mask of the IP address on the Apsara Stack side and the IP address on the client side. The two IP addresses must belong to the same subnet. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | The description of the VBR | The description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Name | String | No | test | The name of the VBR. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VbrId | String | vbr- bp1jcg5cmxjbl9xgc* *** | The ID of the VBR. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreateVirtualBorderRouter &PhysicalConnectionId=pc-xxxxxxxxx &RegionId=cn-shanghai &VlanId=10 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouterInterfaceResponse>
      <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
      <VbrId>vbr-2zecmmvg5gvu8i4t****</VbrId>
</CreateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "CreateRouterInterfaceResponse": {
        "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB",
        "VbrId": "vbr-2zecmmvg5gvu8i4te****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidPhysicalConne ctionId.NotFound | The specified PhysicalConnectionId is not found. | The error message returned because the ID of the physical connection does not exist. |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | The error message returned because PhysicalConnectionId is not set. |
| 400 | InvalidPhysicalConne ctionId.NotEnabled | The specified PhysicalConnectionId is not in Enabled state. | The error message returned because the state of the physical connection is invalid. Check the physical connection and try again. |
| 404 | InvalidVbrOwnerId.N otFound | The specified VbrOwnerId is not valid. | The error message returned because VbrOwnerId is set to an invalid value. |
| 400 | InvalidVlanId.Malfor med | The specified VlanId is not valid. | The error message returned because VlanId is set to an invalid value. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidCircuitCode.M alformed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because LocalGatewayIp is not set. |
| 400 | InvalidLocalGatewayI p.Malformed | The specified LocalGatewayIp is not valid. | The error message returned because the IP address of the local gateway is invalid. |
| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because PeerGatewayIp is not set. |
| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | The error message returned because PeeringSubnetMask is not set. |
| 400 | InvalidPeeringSubnet Mask.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.LocalGate wayIpNotAllowedBy Caller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |
| 403 | Forbidden.PeerGate wayIpNotAllowedBy Caller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSu bnetMaskNotAllowe dByCaller | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.NameNot AllowedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.Descriptio nNotAllowedByCalle r | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidName.Malfor med | The specified ? Name? is not valid. | The error message returned because the format of the name is invalid. |

| eveloper Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDescription.M alformed | The specifid ? Description? is not valid. | The error message returned because the specified resource description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | QuotaExceeded.vbrP erpConn | Virtual boarder router per PhysicalConnection quota exceed. | The error message returned because the number of VBRs of the current physical connection has reached the upper limit. Reduce the number of VBRs and try again. |
| 400 | QuotaExceeded.free vbr | Free virtual boarder router quota exceed. | The error message returned because the VBR quota is exhausted. |
| 400 | InvalidIp.NotSameSu bnet | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |
| 404 | CROSS BID.FORBIDDE _ N | Create VBR across bid is illegal | The error message returned because you are not allowed to create a VBR for a user of another site. |

##### 2.1.12.2 DeleteVirtualBorderRouter

Deletes a virtual border router (VBR). When you call this operation, take note of the following rules: Before you delete a VBR, you must delete all router interfaces on the VBR. You can delete only a VBR that is in the Unconfirmed, Enabled, or Terminated state. If the owner of a physical connection wants to delete a VBR that belongs to another Apsara Stack tenant account, the VBR must be in the Unconfirmed state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVirtualBord erRouter | The operation that you want to perform. Set the value to Delet eVirt ualBorderRout er. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The ID of the region where the VBR is deployed. You can call the DescribeRegions operation to query region IDs. |
| VbrId | String | Yes | vbr- bp12mw1f8k3jgy gk9**** | The ID of the VBR. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8BF7D24-F3EB- 4E23-9208- B77C6EB78E75 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeleteVirtualBorderRouter &RegionId=cn-shanghai &VbrId=vbr-bp12mw1f8k3jgygk9**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFoun d | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified vRouter does not exist. Check whether the ID of the VBR is valid. |
| 400 | InvalidOperation.Rou terInterfaceNotDelet ed | The specified VirutalBorderRouter still has routerInterface. | The error message returned because the VBR is associated with router interfaces. |
| 400 | InvalidOperation.Op erationNotAllowedIn State | The specified VirutalBorderRouter is in invalid state. | The error message returned because the state of the VBR is invalid. Check the state of the VBR. |
| 403 | Forbidden.Operation NotAllowedByUser | The caller is not allowed to delete the specified VirtualBorderRouter. | The error message returned because you are not allowed to delete the VBR. |
| 403 | Forbidden.MultiVlan Ri | Multiple vlan router interfaces are found. | The error message returned because multiple VLAN router interfaces exist. |
| 403 | Forbidden.NoRiFoun d | No vlan router interfaces are found. | The error message returned because no VLAN router interface is available. |
| 400 | InvalidStatus.NotAll owed | The virtual border has been associated by physicalConnection. | The error message returned because the VBR is associated with a physical connection. |

##### 2.1.12.3 DescribeVirtualBorderRouters

Queries virtual border routers (VBRs) that you have created. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBo rderRouters | The operation that you want to perform. Set the value toDescribeVirt ualBorderRout ers. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the VBR is deployed. You can call the DescribeRegions operation to query region IDs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1 |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| Filter.N.Key | String | No | 1 | The key of filter condition N. Valid values of N:1 t o 5. Valid values of filter conditions: PhysicalConnect ionId: Filter by physical connection ID. VbrId: Filter by VBR ID. St at us: Filter by VBR status. Name: Filter by VBR name. AccessPoint Id: Filter by access point ID. t ype: Filter by physical connection type. |
| Filter.N.Value.N | RepeatLi st | No | 1 | The value of filter condition N. Valid values of N:1 t o 5. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VirtualBorderRo uterSet | Array of VirtualBorderRo uterType |   | The information about the queried VBR. |
| VirtualBorderRo uterType |   |   |   |
| AccessPointId | String | ap-cn- kojok1xxxxxxxx | The ID of the access point that is associated with the physical connection. |
| ActivationTime | String | 2017-06- 08T12:20:55 | The first time when the VBR was activated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssociatedCens | Array of AssociatedCen |   | Cloud Enterprise Network (CEN). |
| AssociatedCen |   |   |   |
| CenId | String | cen-kojok19xxxxxxxx | The ID of the CEN instance. |
| CenOwnerId | Long | 1086496381294461 | The user ID (UID) of the Apsara Stack tenant account to which the CEN instance belongs. |
| CenStatus | String | Attached | The status of the CEN instance. |
| AssociatedPhys icalConnections | Array of AssociatedPhys icalConnection |   | The associated physical connection. |
| AssociatedPhys icalConnection |   |   |   |
| CircuitCode | String | 12 | The circuit code of the Internet service provider (ISP) that corresponds to the router interface of the VBR. |
| EnableIpv6 | Boolean | false |   |
| LocalGatewayIp | String | 116.62.xx.xx | The IP address of the on-premises router interface of the VBR. |
| LocalIpv6Gatew ayIp | String | 2408:****:cc:400::* |   |
| PeerGatewayIp | String | 116.62.xx.xx | The IP address of the peer router interface of the VBR. |
| PeerIpv6Gatew ayIp | String | 2408:****:cc:400::* |   |
| PeeringIpv6Sub netMask | String | 2408:****:cc:400::/* |   |
| PeeringSubnet Mask | String | 255.255.255.252 | The subnet mask of the connection between the on-premises router interface and the peer router interface of the VBR. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnec tionBusinessSta tus | String | Normal | The business status of the physical connection. |
| PhysicalConnec tionId | String | pc- 119mfjzm7xxxxxxxx | The ID of the physical connection. |
| PhysicalConnec tionOwnerUid | String | qfrgrgs | The UID of the Apsara Stack tenant account to which the physical connection belongs. |
| PhysicalConnec tionStatus | String | Normal | The status of the physical connection. |
| Status | String | Active |   |
| VlanId | String | 0 | The VLAN ID of the VBR. |
| VlanInterfaceId | String | ri- kojok19x3j0q6kxxxxx xxxx | The ID of the router interface of the VBR. This ID can be used as the next hop of a route entry of the VBR. |
| CircuitCode | String | longtel001 | The circuit code provided by the ISP for the physical connection. |
| CreationTime | String | 2017-06- 08T12:20:55 | The time when the VBR was created. |
| Description | String | VBR | The description of the VBR. |
| DetectMultiplier | Long | 3 | The multiple of the detection time. This value indicates the maximum number of dropped packets that is allowed by the receiver when the sender transmits packets. This value can be used to check whether the connection functions as expected. Valid values:3 t o 10. |
| EccId | String | ecc-h********* |   |
| EnableIpv6 | Boolean | false |   |
| LocalGatewayIp | String | 116.62.**. ** | The IP address configured on the Apsara Stack side. |

| eveloper Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| LocalIpv6Gatew ayIp | String | 2408:****:cc:400::* |   |
| MinRxInterval | Long | 100 | The time interval to receive Bidirectional Forwarding Detection (BFD) packets. Valid values: 200 to 1000. Unit: milliseconds. |
| MinTxInterval | Long | 100 | The time interval to send BFD packets. Valid values: 200 to 1000. Unit: milliseconds. |
| Name | String | test | The name of the VBR. |
| PConnVbrExpire Time | String | 2017-06- 08T12:20:55 | The time when the VBR expires. |
| PeerGatewayIp | String | 116.62.**. ** | The IP address configured on the user side. |
| PeerIpv6Gatew ayIp | String | 2408:****:cc:400::* |   |
| PeeringIpv6Sub netMask | String | 2408:****:cc:400::/* |   |
| PeeringSubnet Mask | String | 255.255.255.252 | The subnet mask of the connection between the Apsara Stack-side IP address and the user-side IP address. |
| PhysicalConnec tionBusinessSta tus | String | Normal | The service status of the physical connection. |
| PhysicalConnec tionId | String | pc- 119mfjzm7x****** | The ID of the physical connection to which the VBR connects. |
| PhysicalConnec tionOwnerUid | String | usdgbh123f****** | The UID of the Apsara Stack tenant account to which the physical connection belongs. |
| PhysicalConnec tionStatus | String | Normal | The status of the physical connection. |
| RecoveryTime | String | 2017-06- 08T12:20:55 | The last time when the VBR was recovered from the Terminated state to the Active state. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RouteTableId | String | rtb- bp1nxxxxxxxx******* | The ID of the route table of the VBR. |
| Status | String | active | The status of the physical connection. Valid values: Init ial: Application is being reviewed. Approved: Application is approved. Allocat ing: Resources are being allocated. Allocat ed: The leased line is under construction. Conf irmed: waiting for user confirmation. Enabled: The physical connection is enabled. Reject ed: The application is rejected. Canceled: The application is canceled. Allocat ion Failed: The system failed to allocate resources. T erminat ed: The physical connection is terminated. |
| TerminationTim e | String | 2017-06- 08T12:20:55 | The last time when the VBR was terminated. |
| Type | String | ecc | The type of the physical connection. |
| VbrId | String | vbr-kojok19xx****** | The ID of the VBR. |
| VlanId | Integer | 10 | The VLAN ID of the VBR. |
| VlanInterfaceId | String | ri- 2zeo3xzyf38r4xx**** *** | The ID of the router interface of the VBR. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DE77A7F3-3B74- 41C0-A5BC- CAFD188C28B6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribeVirtualBorderRouters &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVirtualBorderRoutersResponse>
          <RequestId>AE65530E-8436-4FB1-8217-DCD35712AC89</RequestId>
          <PageNumber>1</PageNumber>
          <VirtualBorderRouterSet>
                <VirtualBorderRouterType>
                      <LocalGatewayIp>10.1.xx.xx</LocalGatewayIp>
                      <PeerGatewayIp>10.2.xx.xx</PeerGatewayIp>
                      <PhysicalConnectionOwnerUid>123157908XXXXXXXX</PhysicalConnectionOwne
rUid>
                      <VlanId>10</VlanId>
                      <PhysicalConnectionStatus>Enabled</PhysicalConnectionStatus>
                      <PhysicalConnectionId>pc-2zeoaxkq3jotxxxxxxxx</PhysicalConnectionId>
                      <RouteTableId>vtb-2ze9hmd6yofwvxxxxxxxx</RouteTableId>
                      <PeeringSubnetMask>255.0.0.0</PeeringSubnetMask>
                      <CreationTime>2018-03-06T11:16:34Z</CreationTime>
                      <ActivationTime>2018-03-06T11:16:34Z</ActivationTime>
                      <Status>active</Status>
                      <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessS
tatus>
                      <VlanInterfaceId>ri-2zeum6rgu0586xxxxxxxx</VlanInterfaceId>
                      <AccessPointId>ap-cn-beijing-dx-A</AccessPointId>
                      <VbrId>vbr-2zecmmvg5gxxxxxxxx</VbrId>
                </VirtualBorderRouterType>
          </VirtualBorderRouterSet>
          <TotalCount>1</TotalCount>
          <PageSize>10</PageSize>
</DescribeVirtualBorderRoutersResponse>
```

`JSON` format `{`

```json
    "DescribeVirtualBorderRoutersResponse": {
        "RequestId": "AE65530E-8436-4FB1-8217-DCD35712AC89",
        "PageNumber": "1",
        "VirtualBorderRouterSet": {
            "VirtualBorderRouterType": {
                "LocalGatewayIp": "10.1.xx.xx",
                "PeerGatewayIp": "10.2.xx.xx",
                "PhysicalConnectionOwnerUid": "123157908XXXXXXXX",
                "VlanId": "10",
                "PhysicalConnectionStatus": "Enabled",
                "PhysicalConnectionId": "pc-2zeoaxkq3jotxxxxxxxx",
                "RouteTableId": "vtb-2ze9hmd6yofwvxxxxxxxx",
                "PeeringSubnetMask": "255.0.0.0",
                "CreationTime": "2018-03-06T11:16:34Z",
                "ActivationTime": "2018-03-06T11:16:34Z",
                "Status": "active",
                "PhysicalConnectionBusinessStatus": "Normal",
                "VlanInterfaceId": "ri-2zeum6rgu0586xxxxxxxx",
                "AccessPointId": "ap-cn-beijing-dx-A",
                "VbrId": "vbr-2zecmmvg5gxxxxxxxx"
```

`}` `},`

```json
        "TotalCount": "1",
        "PageSize": "10"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.Valu eNotSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

##### 2.1.12.4 TerminateVirtualBorderRouter

Disables a virtual border router (VBR). After you call this operation, the state of the VBR changes from Enabled to T erminat ing. After the VBR is disabled, its state changes to T erminat ed. Not e Only the owner of the physical connection to which the VBR connects can call this operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminateVirtual BorderRouter | The operation that you want to perform. Set the value to T erminat eVirt ualBorderRout er. |
| RegionId | String | Yes | cn-shanghai | The region where the VBR is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp15zckdt37pq7 2**** | The ID of the VBR that you want to disable. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-00**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=TerminateVirtualBorderRouter &RegionId=cn-shanghai &VbrId=vbr-bp15zckdt37pq72**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TerminateVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</TerminateVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFoun d | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the specified VBR ID is valid. |
| 400 | InvalidOperation.Op erationNotAllowedIn State | The specified VirutalBorderRouter is in invalid state. | The error message returned because the state of the specified VBR is invalid. Check the state of the VBR. |
| 403 | Forbidden.Operation TerminateNotAllow edByUser | The caller is not allowed to terminate the specified VirtualBorderRouter. | The error message returned because you are not authorized to disable the specified VBR. |

##### 2.1.12.5 RecoverVirtualBorderRouter

Enables a disabled VBR. After you call the operation, the state of the VBR changes from T erminat ed to Recovering. When the VBR is enabled, its state changes to Enabled. When you call this operation, take note of the following items: Only the owner of the physical connection can call this operation. The physical connection to which the VBR belongs must be in the Enabled state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RecoverVirtualBor derRouter | The operation that you want to perform. Set the value to RecoverVirt ualBorderRout er. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-shanghai | The ID of the region where the VBR is deployed. You can call the DescribeRegions operation to query region IDs. |
| VbrId | String | Yes | vbr- bp1lhl0taikrte**** | The ID of the VBR. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=RecoverVirtualBorderRouter &RegionId=cn-shanghai &VbrId=vbr-bp1lhl0taikrte**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RecoverVirtualBorderRouterResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</RecoverVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFoun d | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidOperation.Op erationNotAllowedIn State | The specified VirutalBorderRouter is in invalid state | The error message returned because the status of the VBR interface is invalid. |
| 400 | OperationFailed.Vlan IdAlreadyInUse | The specifed vlanId has been used. | The error message returned because the VLAN interface is being used. |
| 403 | Forbidden.Operation RecoverNotAllowed ByUser | The caller is not allowed to recover the specified VirtualBorderRouter. | The error message returned because you do not have the permissions to recover the VBR. |

##### 2.1.12.6 UnassociatePhysicalConnectionFromVirtualBorderRouter

Disassociates a virtual border router (VBR) from a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociatePhysi calConnectionFro mVirtualBorderRo uter | The operation that you want to perform. Set the value toUnassociat ePhysicalConnect ionF romVirt ualBorderRout er. |
| PhysicalConnectio nId | String | Yes | pc- bp1qrb3044eqixo g**** | The ID of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VbrId | String | Yes | vbr- bp16ksp61j7e0tk n***** | The VLAN ID of the VBR. Valid values: 1 to 2999. Not e Only the owner of the physical connection can set this parameter. The VLAN IDs of two VBRs of the same physical connection must be different. |
| ClientToken | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) of the physical connection. Not e Only the owner of the physical connection can set this parameter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969- 40BF-8542- EBB34FD358AB | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=UnassociatePhysicalConnectionFromVirtualBorderRouter &PhysicalConnectionId=pc-bp1qrb3044eqixog**** &RegionId=cn-hangzhou &VbrId=vbr-bp16ksp61j7e0tkn***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociatePhysicalConnectionFromVirtualBorderRouterResponse>
      <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
    </UnassociatePhysicalConnectionFromVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFoun d | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 404 | InvalidVbrId.NotFoun d | The specified VirutalBorderRouter or PhysicalConnection does not exist in our records. | The error message returned because the VBR or physical connection does not exist. |
| 400 | PARAMETER MUST N _ _ OT NULL _ | The specified physical connection id or vbrId must not be null. | The error message returned because the VbrId and PhysicalConnectionId parameters are not set. |
| 400 | PHYSICAL NOT ASS _ _ OCIATE TO VBR _ _ | The specified PhysicalConnection have not associate to the vbr. | The error message returned because no VBR is created for the physical connection. |
| 400 | ROUTER INTERFACE _ _ REFERED BY ROUTEE _ _ NTRY | The specified VlanInterface has been used by routeEntry. | The error message returned because the VLAN interface is being used by a route entry. |
| 400 | InvalidStatus.NotAll owed | Invalid virtual border router status. | The error message returned because the status of the VBR is invalid. |
| 400 | PHYSICAL NOT ALLO _ _ W ASSOCIATE VBR _ _ | The specified operation not allow. | The error message returned because the physical connection is associated with a VBR and the operation cannot be performed. |

#### 2.1.13 Physical connections

##### 2.1.13.1 CancelPhysicalConnection

Cancels a physical connection before it is enabled. After you cancel a physical connection, its state becomes Canceled. You can cancel only a physical connection that is in the Initial, Approved, Allocated, or Confirmed state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelPhysicalCo nnection | The operation that you want to perform. Set the value to CancelPhysicalConnect ion. |
| PhysicalConnectio nId | String | Yes | pc-119mfjzm7 | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CancelPhysicalConnection &PhysicalConnectionId=pc-119mfjzm7 &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelPhysicalConnectionResponse>
   <RequestId>BE36E95A-F83E-4127-A29E-F2F35D4C999A</RequestId>
    </CancelPhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "BE36E95A-F83E-4127-A29E-F2F35D4C999A"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConne ctionId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified physical connection does not exist. |
| 400 | Forbidden.NotAllow edInState | The request does not allow in this state. | The error message returned because the state is invalid and the operation cannot be performed. |

##### 2.1.13.2 DescribePhysicalConnections

Queries physical connections in a region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePhysicalC onnections | The operation that you want to perform. Set the value to DescribePhysicalConnect ions . |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Filter.N.Key | String | No | 1 | The filter condition. Valid values of N: 1, 2, 3, 4, and 5. The following filter conditions are supported: PhysicalConnect ionId: the ID of the physical connection. AccessPoint Id: the ID of the access point. T ype: the type of the physical connection. LineOperat or: the Internet service provider (ISP) of the physical connection. Spec: the specifications of the physical connection. St at us: the status of the physical connection. Name: the name of the physical connection. The logical operator between multiple values in a filter condition is OR. In this case, the filter condition is met if one of the values is met. The logical operator between filter conditions is AND. In this case, the result is returned only when all conditions are met. |
| Filter.N.Value.N | RepeatLi st | No | 1 | The value of the filter condition. Valid values of N: 1 t o 5. |
| IncludeReservatio nData | Boolean | No | false | Specifies whether to return the orders that have not taken effect. Valid values: t rue and f alse. t rue: returns the orders that have not taken effect. f alse: does not return the orders that have not taken effect. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 23243242rggy**** | A unique token generated by the client to ensure the idempotency of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnec tionSet | Array of PhysicalConnec tionType |   | The description of the physical connection. |
| PhysicalConnec tionType |   |   |   |
| AccessPointId | String | eip- 2zeerraiwb7uj6i0**** *** | The ID of the access point. |
| AdLocation | String | Room Ax-x Bxx, building xx, xxx Avenue, Nanshan District, Shenzhen, Guangdong | The geographical location of the access device. |
| Bandwidth | Long | 10 | The bandwidth of the physical connection. |
| BusinessStatus | String | Normal | The payment state of the physical connection. Valid values: Normal: The physical connection is functioning as expected. FinancialLocked: The physical connection is locked due to overdue payments. Securit yLocked: The physical connection is locked due to security reasons. |
| ChargeType | String | Prepaid | The billing method. Valid values: Prepaid: subscription. |
| CircuitCode | String | longtel001 | The circuit code provided by the ISP. |

| eveloper Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreationTime | String | 2017-06- 08T12:20:55 | The time when the physical connection was created. |
| Description | String | The physical connection | The description of the physical connection. |
| EnabledTime | String | 2017-06- 08T12:20:55 | The time when the physical connection was created. |
| EndTime | String | 2019-02- 25T11:01:04Z | The time when the physical connection expires. |
| HasReservation Data | String | true | Indicates whether you have subscription messages. Valid values: t rue and f alse. t rue : yes. f alse: no. |
| LineOperator | String | CT | The ISP of the physical connection. Valid values: CT: China Telecom. CU: China Unicom. CM: China Mobile. CO: other ISPs in China. Equinix: Equinix. Other: Other ISPs outside China. |
| LoaStatus | String | Available | The status of the LOA. |
| Name | String | name | The name of the physical connection. |
| PeerLocation | String | Building XX, XX Avenue, XX District, Hangzhou, Zhejiang | The geographical location of the data center. |
| PhysicalConnec tionId | String | pc-119mfjzm***** | The ID of the physical connection. |
| PortNumber | String | 80 | The port number of the access device. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PortType | String | 1000Base-T | The port type of the physical connection. Valid values: 100Base-T : 100M copper port. 1000Base-T (default): GE electrical port. 1000Base-LX: GE single-mode fiber port (10 kilometers). 10GBase-T : 10GE electrical port. 10GBase-LR: 10GE single-mode optical port (10 kilometers). |
| RedundantPhysi calConnectionId | String | pc-119mfjzm******* | The ID of the backup physical connection. |
| ReservationActi veTime | String | 2019-02- 25T11:01:04Z | The time when the renewal takes effect. |
| ReservationInte rnetChargeTyp e | String | PayByBandwidth | The renewal type. |
| ReservationOrd erType | String | RENEW | The type of the renewal order. |
| Spec | String | Large | The specifications of the physical connection. |
| Status | String | Initial | The state of the physical connection. Valid values: Init ial: application in progress. Approved: approved. Allocat ing: resource allocation in progress. Allocat ed: under construction. Conf irmed: waiting for user confirmation. Enabled: enabled. Reject ed: rejected. Canceled: canceled. Allocat ion Failed: resource allocation failed. T erminat ed: terminated. |
| Type | String | VPC | The type of the physical connection. Default value: VPC. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 10 | The total number of entries returned. |
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | EEC8EAB1-F299- 4F5C-8E54- 0A3129164C27 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribePhysicalConnections &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePhysicalConnectionsResponse>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
   <PageSize>10</PageSize>
   <RequestId>7C07B0AF-4FC0-4BB2-9667-F75812824BCD</RequestId>
   <PhysicalConnectionSet>
      <PhysicalConnectionType>
         <Type>VPC</Type>
         <PhysicalConnectionId>pc-2zeoaxkq3jot5p71qcnuy</PhysicalConnectionId>
         <PeerLocation>XXX-XX District--XXX Road </PeerLocation>
         <CreationTime>2017-12-13T02:28:42Z</CreationTime>
         <Name>TEST</Name>
         <Status>Enabled</Status>
         <AdLocation>XXX--XX-XXX Datacenter XX Server Rack XXU</AdLocation>
         <EnabledTime>2017-12-18T04:01:30Z</EnabledTime>
         <BusinessStatus>Normal</BusinessStatus>
         <LineOperator>CT</LineOperator>
         <PortNumber>1/1/4</PortNumber>
         <AccessPointId>ap-cn-beijing-dx-A</AccessPointId>
         <PortType>100Base-T</PortType>
         <Bandwidth>2</Bandwidth>
      </PhysicalConnectionType>
   </PhysicalConnectionSet>
</DescribePhysicalConnectionsResponse>
```

`JSON` format `{`

```json
  "PageNumber": 1,
  "TotalCount": 1,
  "PageSize": 10,
  "RequestId": "7C07B0AF-4FC0-4BB2-9667-F75812824BCD",
  "PhysicalConnectionSet": {
    "PhysicalConnectionType": [
```

`{`

```json
        "Type": "VPC",
        "PhysicalConnectionId": "pc-2zeoaxkq3jot5p71qcnuy",
        "PeerLocation": "XXX-XX District--XXX Road",
        "CreationTime": "2017-12-13T02:28:42Z",
        "Name": "TEST",
        "Status": "Enabled",
        "AdLocation": "XXX--XX-XXX Datacenter XX Server Rack XXU",
        "EnabledTime": "2017-12-18T04:01:30Z",
        "BusinessStatus": "Normal",
        "LineOperator": "CT",
        "PortNumber": "1/1/4",
        "AccessPointId": "ap-cn-beijing-dx-A",
        "PortType": "100Base-T",
        "Bandwidth": 2
```

`}` `]` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.Valu eNotSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

##### 2.1.13.3 ModifyPhysicalConnectionAttribute

Modifies the configuration of a physical connection. When you call this operation, take note of the following limits: You can only modify the configuration of a physical connection that is in the Init ial, Enabled, or Reject ed state. You cannot modify the configurations of a physical connection that is in the Canceled, Allocat ing, Allocat ionFailed, or T erminat ed state. After you modify the configurations of a physical connection that is in the Reject ed state, its state becomes Init ial. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyPhysicalCo nnectionAttribute | The operation that you want to perform. Set the value to Modif yPhysicalConnect ionAt t ribut e. |
| PhysicalConnectio nId | String | Yes | pc- 119mfjzm****** | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| LineOperator | String | No | CT | The Internet service provider (ISP). Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in China Equinix: Equinix Other: other ISPs outside China |
| bandwidth | Integer | No | 5 | The bandwidth of the physical connection. Unit: Mbit/s. Valid values: 2 to 10240. |
| PeerLocation | String | No | Building XX, XX Avenue, XX District, Hangzhou, Zhejiang | The geographical location of the data center. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PortType | String | No | 1000Base-LX | The port type of the physical connection. Default value: 1000Base-T. Valid values: 100Base-T: a copper port that supports 100 Mbit/s. 1000Base-T: a copper port that supports 1,000 Mbit/s. 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s (10 kilometers). 10GBase-T: a copper port that supports 10,000 Mbit/s. 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s (10 kilometers). |
| RedundantPhysic alConnectionId | String | No | pc-119mfjzm7 | The ID of the standby physical connection. The standby physical connection must be in the Allocat ed, Conf irmed, or Enabled state. |
| Description | String | No | The description of the physical connection | The description of the physical connection. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Name | String | No | The name of the physical connection | The name of the physical connection. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). The name cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | efefe566754h | The client token that is used to guarantee the idempotency of the request. You can use the client to generate a token, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| CircuitCode | String | No | longtel001 | The circuit code provided by the ISP for the physical connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 013EE132-A109- 4247-91B0- 099A8FF49AD7 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyPhysicalConnectionAttribute &PhysicalConnectionId=pc-119mfjzm****** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyPhysicalConnectionAttributeResponse>
      <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0</RequestId>
</ModifyPhysicalConnectionAttributeResponse>
```

`JSON` format `{`

```json
  "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConne ctionId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the physical connection does not exist. |
| 400 | InvalidLineOperator. Malformd | The LineOperator provided was invalid. | The error message returned because the value of the LineOperator parameter is invalid. |
| 400 | InvalidPeerLocation. Malformd | The PeerLocation provided was invalid. | The error message returned because the value of the PeerLocation parameter is invalid. |
| 400 | InvalidPortType.Malf ormd | The PortType provided was invalid. | The error message returned because the type of the port is invalid. |
| 400 | InvalidDescription.M alformed | The specifid ? Description? is not valid. | The error message returned because the format of the resource description is invalid. The value must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | InvalidName.Malfor med | The specified ? Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidStatus | invalid physical connection status. | The error message returned because the state of the specified physical connection is invalid. |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | The error message returned because the maximum bandwidth of the physical connection is invalid. |
| 400 | InvalidRedundantPhy sicalConnection | redundant physical connection doesn't belong to current user. | The error message returned because the backup connection does not belong to your Apsara Stack tenant account. |
| 400 | InvalidRedundantPhy sicalConnectionStat us | invalid redundant physical connection status. | The error message returned because the state of the backup physical connection is invalid. |
| 400 | InvalidCircuitCode.M alformed | circuitCode is illegal. | The error message returned because the value of the CircuitCode parameter is invalid. |

##### 2.1.13.4 TerminatePhysicalConnection

Terminates a physical connection after it is enabled. After you call this operation, the state of the physical connection becomes Terminating. After the physical connection is terminated, its state becomes Terminated. When you call this operation, take note of the following limits: You can only terminate a physical connection in the Enabled state. Before you terminate a physical connection, you must delete the virtual border routers (VBRs) that are associated with it. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminatePhysica lConnection | The operation that you want to perform. Set the value to T erminat ePhysicalConnect ion. |
| PhysicalConnectio nId | String | Yes | pc-119mfjzm**** | The ID of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=TerminatePhysicalConnection &PhysicalConnectionId=pc-119mfjzm**** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TerminatePhysicalConnectionResponse>
    <RequestId>513E0A50-4F2D-4CBE-BF35-40559DF65D79</RequestId>
</TerminatePhysicalConnectionResponse>
```

`JSON` format `{`

```json
  "RequestId": "513E0A50-4F2D-4CBE-BF35-40559DF65D79"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConne ctionId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the physical connection does not exist. |
| 400 | Forbidden.NotAllow edInState | The request does not allow in this state. | The error message returned because the state is invalid. |

##### 2.1.13.5 EnablePhysicalConnection

Enables a physical connection that is in the Confirmed state. After you enable the physical connection, its state becomes Enabled. When you call this operation, take note of the following limits: You can enable only a physical connection that is in the Conf irmed state. After a physical connection is enabled, its state becomes Enabled. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnablePhysicalCo nnection | The operation that you want to perform. Set the value to EnablePhysicalConnect ion. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PhysicalConnectio nId | String | Yes | pc-119mfjz**** | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to guarantee the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | API-20365164-5b0d- 460a-83c2- 2189972b3349 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=EnablePhysicalConnection &PhysicalConnectionId=pc-119mfjz**** &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnablePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</EnablePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConne ctionId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified physical connection does not exist. |
| 400 | Forbidden.NotAllow edInState | The request does not allow in this state. | The error message returned because the state is invalid and the operation cannot be performed. |

##### 2.1.13.6 DeletePhysicalConnection

Deletes a physical connection. Not e You can delete only physical connections that are in the following states:Reject ed,Canceled,Allocat ionFailed, andT erminat ed. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePhysicalCo nnection | The operation that you want to perform. Set the value to Delet ePhysicalConnect ion. |
| PhysicalConnectio nId | String | Yes | pc- 119mfjzm7******* ** | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2B3670CD-670E- 4540-8C13- 6DE929AEDD3B | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DeletePhysicalConnection &PhysicalConnectionId=pc-119mfjzm7********* &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeletePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeletePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConne ctionId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified physical connection does not exist. |
| 400 | Forbidden.NotAllow edInState | The request does not allow in this state. | The error message returned because the state is invalid and the operation cannot be performed. |
| 400 | InvalidPhysicalConne ctionId.NotMatched | instance id not matched. | The error message returned because the instance ID does not match. |
| 400 | Forbidden.VBRExists | physical connection owner's vbr still exists. | The error message returned because the virtual border router (VBR) of the physical connection still exists. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.VBRExists | vbr owner's vbr still exists. | The error message returned because the VBR still exists. |
| 400 | Forbidden.Associate ToVBR | The physical connection still associate to VBR. | The error message returned because the physical connection is already associated with a VBR. |

##### 2.1.13.7 CreatePhysicalConnectionOccupancyOrder

Creates an order for resource occupation of one or more physical connections. Not e You can perform this operation only for a physical connection that is in the Complet e state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalCo nnectionOccupan cyOrder | The operation that you want to perform. Set the value to Creat ePhysicalConnect ionOccupan cyOrder. |
| PhysicalConnectio nId | String | Yes | pc- bp1hp0wr072f6** **** | The ID of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The region where the physical connection is deployed. |
| Period | Integer | No | 1 | The subscription duration. |
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the physical connection. Valid values: PrePaid: subscription. If you select this billing method, make sure that your Apsara Stack tenant account supports balance payment or credit payment. Post Paid: pay-as-you-go. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | true | Specifies whether automatic payment is enabled. Valid values: t rue: enables automatic payment. This is the default value. Make sure that you have sufficient balance in your account. Otherwise, your order becomes invalid and must be canceled. f alse: An order is generated but no payment is made. |
| PricingCycle | String | No | Month | The unit of the subscription cycle. Year: by year. Mont h: by month. |
| ClientToken | String | No | CBCE910E-D396- 4944-8764- B4047838B2D1 | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B9300FE-11E2- 4E3B-949C- BED3B44DD26D | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreatePhysicalConnectionOccupancyOrder &PhysicalConnectionId=pc-bp1hp0wr072f6****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionOccupancyOrder>
    <RequestId>9B9300FE-11E2-4E3B-949C-BED3B44DD26D</RequestId>
</CreatePhysicalConnectionOccupancyOrder>
```

`JSON` format `{`

```json
 "RequestId": "9B9300FE-11E2-4E3B-949C-BED3B44DD26D"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConne ctionId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the physical connection does not exist. |
| 400 | Forbidden.NotAllow edInState | The request does not allow in this state. | The error message returned because the state is invalid. |

##### 2.1.13.8 ApplyPhysicalConnectionLOA

Requests a letter of authorization (LOA) for a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ApplyPhysicalCon nectionLOA | The operation that you want to perform. Set the value toApplyPhysicalConnect ionLOA. |
| CompanyName | String | Yes | company | The name of the customer company that requires the physical connection. |
| ConstructionTime | String | Yes | 2019-02- 28T16:00:00.000 Z | The time when construction started. |
| InstanceId | String | Yes | pc- bp1qrb3044eqixx xxxxxx | The ID of the physical connection. |
| LineType | String | Yes | SDH | The type of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. |
| Si | String | Yes | Alibaba | The construction company. |

| eveloper Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | A47BD386-7FDE- 4xxx4-8D22- C62xxxxxxxx | Client authentication. |
| Bandwidth | Integer | No | 3 | The bandwidth of the physical connection. |
| PeerLocation | String | No | Hangzhou | The geographical location where the physical connection is deployed. |
| PMInfo.N.PMNam e | String | No | Tom | The name of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMCont actInfo | String | No | 1320000**** | The contact information about the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMCertif icateType | String | No | IDCard | The identity type of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMCertif icateNo | String | No | 3210xxxxxxxxxxxx xx | The identity number of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMGend er | String | No | Male | The gender of the construction personnel. N is a natural number. Replace N with a value when you call this operation. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A47BD386-7FDE- 42C4-8D22- C6223D18AA1C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ApplyPhysicalConnectionLOA &CompanyName=company &ConstructionTime=2019-02-28T16:00:00.000Z &InstanceId=pc-bp1qrb3044eqixxxxxxxx &LineType=SDH &RegionId=cn-hangzhou &Si=Alibaba &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ApplyPhysicalConnectionLOAResponse>
      <RequestId>A47BD386-7FDE-42C4-8D22-C6223D18AA1C</RequestId>
    </ApplyPhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "RequestId":"A47BD386-7FDE-42C4-8D22-C6223D18AA1C"
```

`}`

##### 2.1.13.9 CreatePhysicalConnectionSetupOrder

Creates an order for initial installation of a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalCo nnectionSetupOr der | The operation that you want to perform. Set the value toCreat ePhysicalConnect ionSet upO rder. |
| AccessPointId | String | Yes | ap-cn-beijing-ft- A | The ID of the access point. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LineOperator | String | Yes | CT | The Internet service provider (ISP). Valid values: CT: China Telecom. CU: China Unicom. CM: China Mobile. CO: other ISPs in China. Equinix: Equinix. Other: other ISPs outside China. |
| RegionId | String | Yes | cn-shanghai | The region where the physical connection is deployed. |
| PortType | String | No | 100Base-T | The port type of the physical connection. Default value: 1000Base-T. Valid values: 100Base-T : a copper port that supports 100 Mbit/s. 1000Base-T : a copper port that supports 1,000 Mbit/s. 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s (10 kilometers). 10GBase-T : a copper port that supports 10,000 Mbit/s. 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s (10 kilometers). |
| RedundantPhysic alConnectionId | String | No | pc- bp10zsv5ntp***** *** | The ID of the standby physical connection. The standby physical connection must be in the Allocat ed, Conf irmed, or Enabled state. |
| AutoPay | Boolean | No | true | Indicates whether automatic payment is enabled. Valid values:t rueandf alse. |
| ClientToken | String | No | 318BB676-0A2B- 43A0-9AD8- F1D34E93750F | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 202844382740728 | The ID of the order. |
| PhysicalConnec tionId | String | pc- 2zegmc02v7ss4***** * | The ID of the physical connection. |
| RequestId | String | F7A6301A-64BA- 41EC-8284- 8F4838C15D1F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CreatePhysicalConnectionSetupOrder &AccessPointId=ap-cn-beijing-ft-A &LineOperator=CT &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionSetupOrderResponse>
     <OrderId>205226815210296</OrderId>
     <RequestId>76CCB7F1-C141-4BD1-8106-63987D12BEF4</RequestId>
     <PhysicalConnectionId>pc-2zegmc02v7ss4pin******</PhysicalConnectionId>
</CreatePhysicalConnectionSetupOrderResponse>
```

`JSON` format `{`

```json
    "OrderId": 205226815210296,
    "RequestId": "76CCB7F1-C141-4BD1-8106-63987D12BEF4",
    "PhysicalConnectionId": "pc-2zegmc02v7ss4******"
```

`}`

##### 2.1.13.10 CompletePhysicalConnectionLOA

Generates a report for an installed physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CompletePhysical ConnectionLOA | The operation that you want to perform. Set the value to Complet ePhysicalConnect ionLOA. |
| InstanceId | String | Yes | pc- bp10tvlhnwkwxx xxxxxxxx | The ID of the physical connection. |
| LineCode | String | Yes | aaa111 | The circuit code provided by the Internet service provider (ISP). |
| LineLabel | String | Yes | bbb222 | The label of the cable in the data center. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the physical connection is deployed. |
| ClientToken | String | No | F8983C74-E068- 4509-B442- 89xxxxxC8F43B | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8983C74-E068- 4509-B442- 89BD82C8F43B | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=CompletePhysicalConnectionLOA &InstanceId=pc-bp10tvlhnwkwxxxxxxxxxx &LineCode=aaa111 &LineLabel=bbb222 &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CompletePhysicalConnectionLOAResponse>
      <code>200</code>
   <message>successful</message>
   <requestId>5FA3B04E-AEA0-4F89-BF0D-3FD71ED69BF7</requestId>
   <success>true</success>
    </CompletePhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "code":"200",
    "message":"successful",
    "requestId":"5FA3B04E-AEA0-4F89-BF0D-3FD71ED69BF7",
    "success":true
```

`}`

##### 2.1.13.11 DescribePhysicalConnectionLOA

Queries letter of authorization (LOA) information about a physical connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePhysicalC onnectionLOA | The operation that you want to perform. Set the value toDescribePhysicalConnect ionLOA. |
| InstanceId | String | Yes | pc- bp1ca4wca27ex* ***** | The ID of the physical connection. |
| RegionId | String | Yes | cn-hangzhou | The region where the physical connection is deployed. |
| ClientToken | String | No | 318BB676-0A2B- 43A0-9AD8- F1D34E93750F | The client token that is used for authentication. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnec tionLOAType | Struct |   | The LOA information about the physical connection. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CompanyLocali zedName | String | company | The name of the construction company. |
| CompanyName | String | AppCompany**** | The name of the organization that requires the physical connection. |
| ConstructionTi me | String | 2019-02- 26T08:00:00Z | The time when construction started. |
| InstanceId | String | pc- bp1ca4wca27****** | The ID of the physical connection. |
| LineCode | String | lincode**** | The line code of the Internet service provider (ISP). |
| LineLabel | String | linetest**** | The label of the cable in the data center. |
| LineType | String | MSTP | The type of the physical connection. Valid values: MST P Ot her. SDH. MPLSVPN. FIBRE. |
| LoaUrl | String | http://****** | The download URL of the LOA file. |
| PMInfo | Array of PMInfo |   | The information about construction personnel. |
| PMInfo |   |   |   |
| PMCertificateN o | String | engineer**** | The identity number of the construction personnel. |
| PMCertificateTy pe | String | Other | The type of the identity number. Valid values: IDCard: the national identification number. Other: other identity numbers. Passport: the passport number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PMContactInfo | String | 18910010****** | The phone number of the construction personnel. |
| PMGender | String | Male | The gender of the construction personnel. |
| PMName | String | name | The name of the construction personnel. |
| SI | String | ctcu | The construction company. |
| Status | String | Available | The state of the physical connection. |
| RequestId | String | 318BB676-0A2B- 43A0-9AD8- F1D34E93750F | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=DescribePhysicalConnectionLOA &InstanceId=pc-bp1ca4wca27e****** &RegionId=cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePhysicalConnectionLOAResponse>
      <code>200</code>
      <data>
            <companyName>test1234</companyName>
            <constructionTime>2019-02-26T08:00:00Z</constructionTime>
            <instanceId>pc-bp1ca4wca27ert****</instanceId>
            <lineType>MSTP</lineType>
            <loaUrl>http://********</loaUrl>
            <pmInfo>
                  <nextPMIndex>1</nextPMIndex>
                  <pmCertificateNo>12345**</pmCertificateNo>
                  <pmCertificateType>Other</pmCertificateType>
                  <pmContactInfo>189100100**0</pmContactInfo>
                  <pmGender>Male</pmGender>
                  <pmName>test</pmName>
            </pmInfo>
            <si>ctcu</si>
            <status>Available</status>
      </data>
      <message>successful</message>
      <requestId>318BB676-0A2B-43A0-9AD8-F1D34E93750F</requestId>
      <success>true</success>
    </DescribePhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "code": "200",
    "data": {
        "companyName": "test1234",
        "constructionTime": "2019-02-26T08:00:00Z",
        "instanceId": "pc-bp1ca4wca27erts****",
        "lineType": "MSTP",
        "loaUrl":"http://*******",
        "pmInfo": [
```

`{`

```json
                "nextPMIndex": 1,
                "pmCertificateNo": "1234567",
                "pmCertificateType": "Other",
                "pmContactInfo": "18910010***",
                "pmGender": "Male",
                "pmName": "test"
```

`}` `],`

```json
        "si": "ctcu",
        "status": "Available"
```

`},`

```json
    "message": "successful",
    "requestId": "318BB676-0A2B-43A0-9AD8-F1D34E93750F",
    "success": true
```

`}`

#### 2.1.14 VPN gateways

##### 2.1.14.1 VPN gateway

###### 2.1.14.1.1 CreateVpnGateway

Creates a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnGatew ay | The operation that you want to perform. Set the value to: Creat eVpnGat eway. |
| Bandwidth | Integer | Yes | 5 | The public bandwidth of the VPN gateway. Unit: Mbit/s. Valid values: 5, 10, 20, 50, and 100. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where you want to create the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | Yes | vpc- bp1ub1yt9cvakoe lj**** | The ID of the virtual private cloud (VPC) where the VPN gateway is deployed. |
| EnableIpsec | Boolean | No | true | Specifies whether to enable the IPsec- VPN feature. Valid values: t rue: enables the IPsec-VPN feature. f alse: disables the IPsec-VPN feature. This is the default value. |
| EnableSsl | Boolean | No | true | Specifies whether to enable the SSL- VPN feature. Valid values: t rue: enables the SSL-VPN feature. f alse: disables the SSL-VPN feature. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | MYVPN | The name of the VPN gateway. The default value is the ID of the VPN gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter, and cannot start with http:// or https:// . |
| SslConnections | Integer | No | 5 | The maximum number of concurrent connections. Valid values: 5, 10, and 20. |
| VSwitchId | String | No | vsw- bp1j5miw2bae9s 2vt**** | The ID of the vSwitch to which the VPN gateway belongs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | myVpn | The name of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |

Examples Sample requests

```
http(s)://vpc.example.com/?Action=CreateVpnGateway &Bandwidth=5 &RegionId=cn-qingdao-env66d01 &VpcId=vpc-bp1ub1yt9cvakoelj**** &
```

Sample success responses `XML` format

```xml
<CreateVpnGatewayResponse>
      <Name>myVpn</Name>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
</CreateVpnGatewayResponse>
```

`JSON` format

```json
{ "CreateVpnGatewayResponse":{ "Name":"myVpn", "VpnGatewayId":"vpn-bp1q8bgx4xnkm2ogj****", "RequestId":"54B48E3D-DF70-471B-AA93-08E683A1B457" } }
```

###### 2.1.14.1.2 DescribeVpnGateways

Queries one or more VPN gateways. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGate ways | The operation that you want to perform. Set the value to DescribeVpnGat eways. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpcId | String | No | vpc- bp1ub1yt9cvakoe lj**** | The ID of the virtual private cloud (VPC) to which the VPN gateway belongs. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |
| Status | String | No | init | The status of the VPN gateway. Valid values: init : The VPN gateway is being initialized. provisioning: The VPN gateway is being prepared. act ive: The VPN gateway is running as expected. updat ing: The VPN gateway is being updated. Delet ing: The VPN gateway is being deleted. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BusinessStatus | String | No | Normal | The payment status of the VPN gateway. Valid values: Normal: The VPN gateway is running as expected. FinancialLocked: The VPN gateway is locked due to overdue payments. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGateways | Array of VpnGateway |   | Detailed information about the VPN gateways. |
| VpnGateway |   |   |   |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj** ** | The ID of the VPC to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv* *** | The ID of the vSwitch to which the VPN gateway is attached. |
| InternetIp | String | 116.XX.XX.69 | The public IP address of the VPN gateway. |
| CreateTime | Long | 1515383700000 | The timestamp generated when the VPN gateway was created. |
| EndTime | Long | 1518105600000 | The timestamp to be generated when the VPN gateway expires. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Spec | String | 5 Mbps | The maximum bandwidth of the VPN gateway. Unit: Mbit/s. |
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| BusinessStatus | String | Normal | The payment status of the VPN gateway. |
| ChargeType | String | Prepay | The billing type. Valid value: Post payByFlow. |
| IpsecVpn | String | enable | Indicates whether the IPsec-VPN feature is enabled. enable: IPsec-VPN is enabled. disable : IPsec-VPN is disabled. |
| SslMaxConnecti ons | Long | 5 | The maximum number of concurrent SSL- VPN connections. |
| SslVpn | String | enable | Indicates whether the SSL-VPN feature is enabled. enable: SSL-VPN is enabled. disable : SSL-VPN is disabled. |
| Tag | String | 1 | The tag of the VPN gateway. |
| TotalCount | Integer | 1 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned on the current page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | DF11D6F6-E35A- 41C3-9B20- 6FC8A901FE65 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnGateways &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

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
                  <InternetIp>116.XX.XX.69</InternetIp>
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
    "PageNumber": 1,
    "TotalCount": 1,
    "VpnGateways": {
        "VpnGateway": [
```

`{`

```json
                "Status": "active",
                "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
                "BusinessStatus": "Normal",
                "Spec": "5M",
                "CreateTime": 1492753580000,
                "InternetIp": "116.XX.XX.69",
                "EndTime": 1495382400000,
                "VSwitchId": "vsw-bp1y9ovl1cu9ou4tv****",
                "VpcId": "vpc-bp1ub1yt9cvakoelj****"
```

`}` `]` `},`

```json
    "PageSize": 10,
    "RequestId": "B2CD1315-CA2B-47B1-9DA5-8F1D69C48E82"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.1.3 DescribeVpnGateway

Queries the details of a specified VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnGate way | The operation that you want to perform. Set the value to DescribeVpnGat eway. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoelj** ** | The ID of the VPC for which the VPN gateway is created. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv* *** | The ID of the vSwitch to which the VPN gateway is attached. |
| InternetIp | String | 116.XX.XX.222 | The public IP address of the VPN gateway. |
| CreateTime | Long | 1495382400000 | The timestamp generated when the VPN gateway was created. |
| EndTime | Long | 1495382400000 | The timestamp to be generated when the VPN gateway expires. |
| Spec | String | 5 M | The maximum bandwidth of the VPN gateway. Unit: Mbit/s. |
| Name | String | vpngatewayname | The name of the VPN gateway. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | vpngatewaydescript ion | The description of the VPN gateway. |
| Status | String | init | The status of the VPN gateway. init : The VPN gateway is being initialized. provisioning : The VPN gateway is being prepared. act ive: The VPN gateway is running as expected. updat ing: The VPN gateway is being updated. Delet ing: The VPN gateway is being deleted. |
| BusinessStatus | String | Normal | The payment status of the VPN gateway. Normal: The VPN gateway is running as expected. FinancialLocked: The VPN gateway is locked due to overdue payments. |
| ChargeType | String | PostpayByFlow | The billing method of the VPN gateway. Valid value: Post payByFlow. |
| IpsecVpn | String | enable | Indicates whether the IPsec-VPN feature is enabled. enable: IPsec-VPN is enabled. disable : IPsec-VPN is disabled. |
| RequestId | String | E98A9651-7098- 40C7-8F85- C818D1EBBA85 | The ID of the request. |
| SslMaxConnecti ons | Long | 5 | The maximum number of concurrent SSL- VPN connections. |
| SslVpn | String | enable | Indicates whether the SSL-VPN feature is enabled. enable: SSL-VPN is enabled. disable : SSL-VPN is disabled. |
| Tag | String | tag1 | The tag of the VPN gateway. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnGateway &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnGatewayResponse>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <Spec>5M</Spec>
      <BusinessStatus>Normal</BusinessStatus>
      <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId>
      <CreateTime>1492753580000</CreateTime>
      <InternetIp>116.XX.XX.222</InternetIp>
      <EndTime>1495382400000</EndTime>
      <VSwitchId>vsw-bp1y9ovl1cu9ou4tv****</VSwitchId>
      <VpcId>vpc-bp1ub1yt9cvakoelj****</VpcId>
</DescribeVpnGatewayResponse>
```

`JSON` format `{`

```json
    "Status": "active",
    "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
    "BusinessStatus": "Normal",
    "Spec": "5M",
    "CreateTime": 1492753580000,
    "RequestId": "E98A9651-7098-40C7-8F85-C818D1EBBA85",
    "InternetIp": "116.XX.XX.222",
    "EndTime": 1495382400000,
    "VSwitchId": "vsw-bp1y9ovl1cu9ou4tv****",
    "VpcId": "vpc-bp1ub1yt9cvakoelj****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

###### 2.1.14.1.4 DeleteVpnGateway

Deletes a specified VPN gateway. Not e You cannot delete a VPN gateway that is associated with an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnGatew ay | The operation that you want to perform. Set the value to Delet eVpnGat eway. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnGateway &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNatGatewayResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeleteNatGatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 403 | ForbiddenRelease | Forbidden to release a prepaid instance within validity period | The error message returned because you cannot release a subscription VPN gateway within the subscription duration. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Config uring | The specified VPN gateway is being configured. | The error message returned because the VPN gateway is being configured. |

###### 2.1.14.1.5 ModifyVpnGatewayAttribute

Modifies the name and description of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnGatew ayAttribute | The operation that you want to perform. Set the value to Modif yVpnGat ewayAt t ribut e. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | vpngateway | The description of the VPN gateway. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Name | String | No | myvpn | The name of the VPN gateway. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| VpcId | String | vpc- bp1ub1yt9cvakoel** ** | The ID of the virtual private cloud (VPC) to which the VPN gateway belongs. |
| VSwitchId | String | vsw- bp1y9ovl1cu9ou4tv* *** | The ID of the vSwitch to which the VPN gateway belongs. |
| InternetIp | String | 116.XX.XX.69 | The public IP address of the VPN gateway. |
| CreateTime | Long | 1492753580000 | The timestamp generated when the VPN gateway was created. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | Long | 1495382400000 | The timestamp to be generated when the VPN gateway expires. |
| Spec | String | 5 Mbps | The specification of the VPN gateway. |
| Name | String | test | The name of the VPN gateway. |
| Description | String | test | The description of the VPN gateway. |
| Status | String | active | The status of the VPN gateway. |
| IntranetIp | String | 172.XX.XX.104 | The private IP address of the VPN gateway. |
| RequestId | String | 54B48E3D-DF70- 471B-AA93- 08E683A1B457 | The ID of the request. |

Examples Sample requests

```
https://vpc.example.com/?Action=ModifyVpnGatewayAttribute &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1q8bgx4xnkm2ogj****
```

`&<`公共请求参数`>` Sample success responses `XML` format

```xml
<ModifyVpnGatewayAttributeResponse>
      <Name>aaa</Name>
      <Status>active</Status>
      <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
      <Spec>5M</Spec>
      <CreateTime>1492753580000</CreateTime>
      <IntranetIp>172.XX.XX.104</IntranetIp>
      <RequestId>54B48E3D-DF70-471B-AA93-08E683A1B457</RequestId>
      <InternetIp>116.XX.XX.69</InternetIp>
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
 "RequestId":"BA56EAF8-E3A9-4BE6-8511-8F03512153E2",
 "IntranetIp":"172.XX.XX.104",
 "CreateTime":1492753580000,
 "InternetIp":"116.XX.XX.69",
 "EndTime":1495382400000,
 "VSwitchId":"vsw-bp1y9ovl1cu9ou4tv****",
 "VpcId":"vpc-bp1ub1yt9cvakoelj****"
```

`}`

##### 2.1.14.2 Customer gateway

###### 2.1.14.2.1 CreateCustomerGateway

Creates a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateCustomerG ateway | The operation that you want to perform. Set the value to Creat eCust omerGat eway. |
| IpAddress | String | Yes | 116.XX.XX.222 | The IP address of the customer gateway. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where you want to create the customer gateway. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | Gateway | The name of the customer gateway. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. However, the name cannot start with http:// or https:// . |
| Description | String | No | Gateway | The description of the customer gateway. The description must be 2 to 256 characters in length, and contain digits, hyphens (-), underscores ( ), full width _ periods (。), full width commas (，), and full width colons (：). The description cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate wayId | String | cgw- bp1aw0a5nfff03xp1 **** | The ID of the customer gateway. |
| IpAddress | String | 100.XX.XX.1 | The IP address of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| CreateTime | Long | 1493363486000 | The timestamp generated when the customer gateway was created. |
| RequestId | String | cgw- bp1aw0a5nfff03xp1 pcqc | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateCustomerGateway &IpAddress=116.XX.XX.222 &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateCustomerGatewayResponse>
      <CustomerGatewayId>cgw-bp1aw0a5nfff03xp****</CustomerGatewayId>
      <RequestId>185E81B1-3916-4667-B48F-C52409B33F2B</RequestId>
      <CreateTime>1493363486000</CreateTime>
      <IpAddress>100.XX.XX.1</IpAddress>
</CreateCustomerGatewayResponse>
```

`JSON` format `{`

```json
    "CustomerGatewayId": "cgw-bp1jrawp82av6bws9****",
    "CreateTime": 1493363599000,
    "RequestId": "D32B3C26-6C6C-4988-93E9-D2A6444CE6AE",
    "IpAddress": "100.XX.XX.1"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | InvalidIpAddress.Alre adyExist | Specified IpAddress is already exist. | The error message returned because the specified IP address already exists. The IP addresses must be unique in the same region. |
| 400 | InvalidIpAddress.Wr ongFormat | Specified IpAddress is invalid. | The error message returned because the specified IP address is invalid. |

| V | irtual Private | Cloud |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |
| 400 | InvalidDescription | The description is not valid | The error message returned because the description format of the specified parameter is invalid. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |

###### 2.1.14.2.2 DescribeCustomerGateways

Queries customer gateways in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustome rGateways | The operation that you want to perform. Set the value to DescribeCust omerGat eways. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the customer gateways are created. You can call the DescribeRegions operation to query the most recent region list. |
| CustomerGatewa yId | String | No | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate ways | Array of CustomerGate way |   | Detailed information about the customer gateways. |
| CustomerGate way |   |   |   |
| CustomerGate wayId | String | cgw- bp1pvpl9r9adju6l5** ** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.XX.XX.55 | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The timestamp generated when the customer gateway was created. |
| TotalCount | Integer | 1 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomerGateways &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

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
                  <IpAddress>139.XX.XX.55</IpAddress>
            </CustomerGateway>
      </CustomerGateways>
</DescribeCustomerGatewaysResponse>
```

`JSON` format `{`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "E82612A9-CB90-4D7E-B394-1DB7F6509B29",
    "CustomerGateways": {
        "CustomerGateway": [
```

`{`

```json
                "Name": "test",
                "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
                "CreateTime": 1492747187000,
                "IpAddress": "139.XX.XX.55"
```

`}` `]` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.2.3 DescribeCustomerGateway

Queries details of a specified customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCustome rGateway | The operation that you want to perform. Set the value to DescribeCust omerGat eway. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the customer gateway is created. You can call the DescribeRegions operation to query the most recent region list. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate wayId | String | cgw- bp1pvpl9r9adju6l5** ** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.XX.XX.32 | The IP address of the customer gateway. |
| RequestId | String | 99506ECB-218F- 45A5-AE8E- 79518451F615 | The ID of the request. |
| CreateTime | Long | 1492747187000 | The timestamp generated when the customer gateway was created. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCustomerGatewayResponse>
      <Name>test</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <CreateTime>1492747187000</CreateTime>
      <RequestId>99506ECB-218F-45A5-AE8E-79518451F615</RequestId>
      <IpAddress>139.XX.XX.32</IpAddress>
</DescribeCustomerGatewayResponse>
```

`JSON` format `{`

```json
    "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
    "Name": "test",
    "RequestId": "A0457BC9-6C0F-4437-AB9D-FB2EABC1D6A2",
    "CreateTime": 1492747187000,
    "IpAddress": "139.XX.XX.32"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidCustomerGate wayInstanceId.NotF ound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |

###### 2.1.14.2.4 DeleteCustomerGateway

Deletes a specified customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCustomerG ateway | The operation that you want to perform. Set the value to Delet eCust omerGat eway. |
| CustomerGatewa yId | String | Yes | cgw- 2zllmw9lqrcdis3b d**** | The ID of the customer gateway. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the customer gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteCustomerGateway &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteCustomerGatewayResesponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteCustomerGatewayResesponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidCustomerGate wayInstanceId.NotF ound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |

###### 2.1.14.2.5 ModifyCustomerGatewayAttribute

Modifies the name and description of a customer gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyCustomerG atewayAttribute | The operation that you want to perform. Set the value to Modif yCust omerGat ewayAt t ribut e. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnkm 2ogj**** | The ID of the customer gateway. |

| eveloper Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the customer gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | test | The name of the customer gateway. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). The name must start with a letter, but cannot start with http:// or https:// . |
| Description | String | No | test | The description of the customer gateway. The description must be 2 to 256 characters in length, and can contain letters, digits, hyphens (-), underscores ( ), full width periods (。), full width _ commas (，), and full width colons (：). The description must start with a letter, but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CustomerGate wayId | String | cgw- bp1pvpl9r9adju6l5** ** | The ID of the customer gateway. |
| Name | String | test | The name of the customer gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | test | The description of the customer gateway. |
| IpAddress | String | 139.XX.XX.55 | The IP address of the customer gateway. |
| CreateTime | Long | 1492747187000 | The timestamp generated when the customer gateway was created. |
| RequestId | String | E61293C8-AF07- 4E87-A272- 542680038F93 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyCustomerGatewayAttribute &CustomerGatewayId=vpn-bp1q8bgx4xnkm2ogj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyCustomerGatewayAttributeResponse>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RequestId>E61293C8-AF07-4E87-A272-542680038F93</RequestId>
      <CreateTime>1492747187000</CreateTime>
      <IpAddress>139.XX.XX.55</IpAddress>
      <Description>modify</Description>
</ModifyCustomerGatewayAttributeResponse>
```

`JSON` format `{`

```json
    "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
    "RequestId": "8AA5CE21-2E6A-4530-BDF5-F055849476E6",
    "CreateTime": 1492747187000,
    "IpAddress": "139.XX.XX.55",
    "Description": "modify"
```

`}` Error codes

| HttpCode | Error code | Error message | Required |
|---|---|---|---|

| HttpCode | Error code | Error message | Required |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform this operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidCustomerGate wayInstanceId.NotF ound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |
| 400 | InvalidDescription | The description is not valid | The error message returned because the format of the specified description is invalid. |

##### 2.1.14.3 Routes for VPN gateways

###### 2.1.14.3.1 DeleteVpnPbrRouteEntry

Deletes a policy-based route from a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnPbrRou teEntry | The operation that you want to perform. Set the value to Delet eVpnPbrRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the policy- based route is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0: specifies a low priority for the route. 100: specifies a high priority for the route entry. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpnPbrRouteEntryResponse>
      <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnPbrRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.3.2 DeleteVpnRouteEntry

Deletes a destination-based route from a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnRouteE ntry | The operation that you want to perform. Set the value to Delet eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the destination-based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0:: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two destination- based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpnRouteEntryResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</DeleteVpnRouteEntryResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.3.3 DescribeVpnRouteEntries

Queries destination-based routes of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnRout eEntries | The operation that you want to perform. Set the value to DescribeVpnRout eEnt ries. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the destination-based routes are created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |
| TotalCount | Integer | 10 | The number of returned entries. |
| VpnRouteEntrie s | Array of VpnRouteEntry |   | The detailed information about the destination-based routes. |
| VpnRouteEntry |   |   |   |
| CreateTime | Long | 1492747187000 | The timestamp generated when the destination-based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| State | String | published | The status of the destination-based route. published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0: indicates that the priority of the route entry is low. 100: indicates that the priority of the route entry is high. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnRouteEntries &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample success responses `XML` format

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
 "PageNumber": 1,
 "TotalCount": 1,
 "VpnRouteEntries": {
  "VpnRouteEntry": [
```

`{`

```json
    "RouteDest": "10.0.0.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "State": "normal",
    "Weight": 100,
    "CreateTime": 1563874074000,
    "NextHop": "vco-bp1tui07ob10fmuro****"
```

`}` `]` `},`

```json
 "PageSize": 10,
 "RequestId": "BF3995A6-FA4F-4C74-B90F-89ECF4BFF4D5"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.3.4 ModifyVpnRouteEntryWeight

Modifies the weight of a destination-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnRouteE ntryWeight | The operation that you want to perform. Set the value to Modif yVpnRout eEnt ryWeight . |
| NewWeight | Integer | Yes | 100 | The new weight you want to set for the destination-based route. 0: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two destination- based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the destination-based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The current weight of the destination- based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpnRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpnRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnRouteEntryWeightResponse>
```

`JSON` format `{`

```json
    "RequestId": "E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.3.5 CreateVpnRouteEntry

Creates a destination-based route on a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnRouteE ntry | The operation that you want to perform. Set the value to Creat eVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the destination-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to advertise the destination-based route to the route table of the associated virtual private cloud (VPC). t rue: advertises the destination- based route to the route table of the associated VPC. f alse: does not advertise the destination-based route to the route table of the associated VPC. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the destination-based route is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |

| irtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The weight of the destination-based route. Valid values: 0: specifies a low priority for the route. 100:specifies a high priority for the route. Not e If two destination- based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | mytest | The description of the destination- based route. |
| OverlayMode | String | No | Ipsec | The overlay mode. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The timestamp generated when the destination-based route was created. |
| Description | String | mytest | The description of the destination-based route. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the destination-based route. |
| OverlayMode | String | Ipsec | The overlay mode. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the destination-based route. |
| State | String | published | The status of the destination-based route. published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the destination-based route. Valid values: 0 and 100. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

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
    "RouteDest": "10.0.0.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "OverlayMode": "Ipsec",
    "State": "published",
    "Weight": 100,
    "CreateTime": 1563873294331,
    "NextHop": "vco-bp1tui07ob10fmuro****",
    "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.3.6 ModifyVpnPbrRouteEntryWeight

Modifies the weight of a policy-based route of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnPbrRou teEntryWeight | The operation that you want to perform. Set the value to Modif yVpnPbrRout eEnt ryWeight . |
| NewWeight | Integer | Yes | 100 | The new weight you want to set for the policy-based route. 0: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the policy- based route is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| Weight | Integer | Yes | 0 | The original weight of the policy-based route. Valid values: 0 and 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| OverlayMode | String | No | Ipsec | The overlay mode. Set the value to Ipsec (IPsec tunneling). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpnPbrRouteEntryWeight &NewWeight=100 &NextHop=vco-bp15oes1py4i66rmd**** &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpnPbrRouteEntryWeightResponse>
        <RequestId>5BE01CD7-5A50-472D-AC14-CA181C5C03BE</RequestId>
</ModifyVpnPbrRouteEntryWeightResponse>
```

`JSON` format `{`

```json
 "RequestId":"E82612A9-CB90-4D7E-B394-1DB7F6509B29"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.3.7 DescribeVpnPbrRouteEntries

Queries policy-based routes of a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnPbrR outeEntries | The operation that you want to perform. Set the value to DescribeVpnPbrRout eEnt ries. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the policy- based routes are created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| TotalCount | Integer | 12 | The number of returned entries. |
| VpnPbrRouteEn tries | Array of VpnPbrRouteEn try |   | The detailed information about the policy- based routes. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnPbrRouteEn try |   |   |   |
| CreateTime | Long | 1492747187000 | The timestamp generated when the policy- based route was created. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | 192.xx.0.0/24 | The source CIDR block of the policy-based route. |
| State | String | published | The status of the policy-based route. Valid values: published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0: indicates that the priority of the route entry is low. 100: indicates that the priority of the route entry is high. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnPbrRouteEntries &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample success responses `XML` format

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
    "PageNumber": 1,
    "TotalCount": 1,
    "RequestId": "E5D94DC7-AEC7-4E73-A203-61B04D1F1160",
    "PageSize": 10,
    "VpnPbrRouteEntries": {
        "VpnPbrRouteEntry": [
```

`{`

```json
                "RouteDest": "10.0.0.0/32",
                "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
                "State": "published",
                "Weight": 100,
                "CreateTime": 1563881012000,
                "NextHop": "vco-bp1tui07ob10fmuro****",
                "RouteSource": "11.0.0.0/32"
```

`}` `]` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.3.8 PublishVpnRouteEntry

Advertises a route of a VPN gateway to the route table of the associated virtual private cloud (VPC). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | PublishVpnRoute Entry | The operation that you want to perform. Set the value to PublishVpnRout eEnt ry. |
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to advertise the route of the VPN gateway to the route table of the associated VPC. t rue: advertises the route to the route table of the associated VPC. f alse: does not advertise the route to the route table of the associated VPC. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the route of the VPN gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the route of the VPN gateway. |
| RouteType | String | Yes | pbr | The type of the route of the VPN gateway. Valid values: pbr: policy-based route. dbr: destination-based route. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=PublishVpnRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteType=pbr &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PublishVpnRouteEntryResponse>
      <RequestId>EE4C2417-9437-4333-BDEB-8493F7AA7258</RequestId>
</PublishVpnRouteEntryResponse>
```

`JSON` format `{`

```json
    "RequestId":"CB2793A8-845F-444C-8E93-76F1BBDF9C78"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.3.9 CreateVpnPbrRouteEntry

Creates a policy-based route for a VPN gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnPbrRou teEntry | The operation that you want to perform. Set the value to Creat eVpnPbrRout eEnt ry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NextHop | String | Yes | vco- bp15oes1py4i66r md**** | The next hop of the policy-based route. |
| PublishVpc | Boolean | Yes | true | Specifies whether to advertise the policy-based route to the route table of the associated virtual private cloud (VPC). Valid values: t rue: advertises the policy-based route to the route table of the associated VPC . f alse: does not advertise the policy-based route to the route table of the associated VPC. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where you want to create the policy-based route for the VPN gateway. You can call the DescribeRegions operation to query the most recent region list. |
| RouteDest | String | Yes | 10.0.0.0/24 | The destination CIDR block of the policy-based route. |
| RouteSource | String | Yes | 192.168.1.0/24 | The source CIDR block of the policy- based route. |
| VpnGatewayId | String | Yes | vpn- bp1a3kqjiiq9legfx **** | The ID of the VPN gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Weight | Integer | Yes | 0 | The weight of the policy-based route. Valid values: 0: specifies a low priority for the route entry. 100: specifies a high priority for the route entry. Not e If two policy-based route entries are configured with the same destination CIDR block, you cannot set the weights of both route entries to 100. |
| ClientToken | String | No | d7d24a21-f4ba- 4454-9173- b3828dae492b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | vpnroute1 | The description of the policy-based route. |
| OverlayMode | String | No | Ipsec | The overlay mode. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreateTime | Long | 1492747187000 | The timestamp generated when the policy- based route was created. |
| Description | String | vpnroute1 | The description of the policy-based route. |
| NextHop | String | vco- bp15oes1py4i66rmd **** | The next hop of the policy-based route. |
| OverlayMode | String | Ipsec | The overlay mode. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| RouteDest | String | 10.0.0.0/24 | The destination CIDR block of the policy- based route. |
| RouteSource | String | 192.168.1.0/24 | The source CIDR block of the policy-based route. |
| State | String | normal | The status of the policy-based route. Valid values: published: The route is advertised. normal: The route is not advertised. |
| VpnInstanceId | String | vpn- bp1cmw7jh1nfe43m 9**** | The ID of the VPN gateway. |
| Weight | Integer | 0 | The weight of the policy-based route. Valid values: 0 and 100. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpnPbrRouteEntry &NextHop=vco-bp15oes1py4i66rmd**** &PublishVpc=true &RegionId=cn-qingdao-env66-d01 &RouteDest=10.0.0.0/24 &RouteSource=192.168.1.0/24 &VpnGatewayId=vpn-bp1a3kqjiiq9legfx**** &Weight=0 &<Common request parameters>
```

Sample success responses `XML` format

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
    "RouteDest": "10.0.0.0/24",
    "RouteSource": "192.168.1.0/24",
    "VpnInstanceId": "vpn-bp1cmw7jh1nfe43m9****",
    "OverlayMode": "Ipsec",
    "State": "published",
    "Weight": 100,
    "CreateTime": 1563873294331,
    "NextHop": "vco-bp1tui07ob10fmuro****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

##### 2.1.14.4 IPsec-VPN

###### 2.1.14.4.1 DescribeVpnConnection

Queries the details of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConn ection | The operation that you want to perform. Set the value to DescribeVpnConnect ion. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the IPsec- VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |
| CustomerGate wayId | String | cgw- bp1mvj4g9kogwwcx k**** | The ID of the customer gateway. |

| eveloper Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| Name | String | ipsec1 | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0 /24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2 .0/24 | The CIDR block of the data center. |
| CreateTime | Long | 1492753817000 | The time when the IPsec-VPN connection was created. |
| Status | String | ike sa not establish _ _ _ ed | The status of the IPsec-VPN connection. Valid values: ike sa not est ablished: indicates that _ _ _ Phase 1 negotiations failed. ike sa est ablished: indicates that _ _ Phase 1 negotiations succeeded. ipsec sa not est ablished: indicates _ _ _ that Phase 2 negotiations failed. ipsec sa est ablished: indicates that _ _ Phase 2 negotiations succeeded. |
| EffectImmediat ely | Boolean | true | Indicates whether the IPsec-VPN connection immediately takes effect. Valid values: t rue: Negotiations are reinitiated when the configuration is changed. f alse: Negotiations are reinitiated when traffic is detected. When negotiations are reinitiated, transient connections may occur. |
| IkeConfig | Struct |   | The configuration of Phase 1 negotiations. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IkeMode | String | main | The IKE mode. Both main and aggressive modes are supported. The main mode provides higher security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.69 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d1i8in7x5 | The pre-shared key. |
| RemoteId | String | 139.XX.XX.32 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of Phase 2 negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | F2310D45-BCF6- 4E2E-9082- B4503844BA4C | The ID of the request. |
| VcoHealthChec k | Struct |   | The information about health checks. |
| Dip | String | 10.XX.XX.1 | The destination IP address. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Enable | String | true | Indicates whether health checks are enabled. Valid values: f alse: Health checks are disabled. t rue: Health checks are enabled. |
| Interval | Integer | 3 | The interval between two consecutive health checks. Unit: seconds. |
| Retry | Integer | 3 | The maximum number of health check retries. |
| Sip | String | 192.XX.XX.2 | The source IP address for health checks. |
| Status | String | failed | The status of the health check. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnConnection &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

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
                        <RemoteId>47.XX.XX.176</RemoteId>
                        <IkePfs>group2</IkePfs>
                        <IkeAuthAlg>sha1</IkeAuthAlg>
                        <Psk>1234567</Psk>
                        <IkeMode>aggressive</IkeMode>
                        <IkeLifetime>86400</IkeLifetime>
                        <IkeVersion>ikev1</IkeVersion>
                        <LocalId>116.XX.XX.119</LocalId>
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
    "PageNumber": 1,
    "VpnConnections": {
        "VpnConnection": [
```

`{`

```json
                "Name": "c2",
                "CustomerGatewayId": "cgw-bp1wl8dtz3auwlavw****",
                "Status": "ike_sa_not_established",
                "RemoteSubnet": "192.168.0.0/16",
                "IpsecConfig": {
                    "IpsecLifetime": 86400,
                    "IpsecAuthAlg": "md5",
                    "IpsecPfs": "group2",
                    "IpsecEncAlg": "aes"
```

`},`

```json
                "EffectImmediately": false,
                "VpnGatewayId": "vpn-bp1yfrjxn4d5t63t****",
                "CreateTime": 1519391420000,
                "VpnConnectionId": "vco-bp1w3m1p23iftycv****",
                "LocalSubnet": "172.16.0.0/12",
                "IkeConfig": {
                    "IkeEncAlg": "aes",
                    "RemoteId": "47.XX.XX.176",
                    "IkePfs": "group2",
                    "IkeAuthAlg": "sha1",
                    "Psk": "1234567",
                    "IkeMode": "aggressive",
                    "IkeLifetime": 86400,
                    "IkeVersion": "ikev1",
                    "LocalId": "116.XX.XX.119"
```

`}` `}` `]` `},`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "7D598A10-26EF-44F2-9F47-E417842F3CEA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectio nInstanceId.NotFoun d | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. Check whether the ID of the IPsec-VPN connection is valid. |

###### 2.1.14.4.2 DeleteVpnConnection

Deletes a specified IPsec-VPN connection. Not e After an IPsec-VPN connection between a virtual private cloud (VPC) and a data center is deleted, the communication between the VPC and data center is interrupted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVpnConnec tion | The operation that you want to perform. Set the value to Delet eVpnConnect ion. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the IPsec- VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVpnConnection &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVpnConnectionResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteVpnConnectionResponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectio nInstanceId.NotFoun d | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. Check whether the ID of the IPsec-VPN connection is valid. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |

###### 2.1.14.4.3 DownloadVpnConnectionConfig

Queries the configuration of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DownloadVpnCo nnectionConfig | The operation that you want to perform. Set the value to DownloadVpnConnect ionConf ig. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the IPsec- VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0C68048B-0F70- 40DA-B8AE- 1B79B5CF62E3 | The ID of the request. |
| VpnConnection Config | Struct |   | The configuration of the IPsec-VPN connection. |
| IkeConfig | Struct |   | The IKE configuration. |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Valid values: sha1 and md5. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. Unit: seconds. |
| IkeMode | String | main | The IKE mode. Valid values: main and aggressive. The main mode offers higher security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.69 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d1i8i**** | The pre-shared key. |
| RemoteId | String | 139.XX.XX.32 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of the IPsec-VPN connection. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. Valid values: sha1 and md5. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. Unit: seconds. |
| IpsecPfs | String | group2 | The DH group. |
| Local | String | 139.XX.XX.32 | The ID of the VPN gateway. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0 /24 | The CIDR block of the VPC. |
| Remote | String | 116.XX.XX.69 | The ID of the customer gateway. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2 .0/24 | The CIDR block of the data center. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DownloadVpnConnectionConfig &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DownloadVpnConnectionConfigResponse>
      <RequestId>0C68048B-0F70-40DA-B8AE-1B79B5CF62E3</RequestId>
      <VpnConnectionConfig>
            <RemoteSubnet>10.10.1.0/24,10.10.2.0/24</RemoteSubnet>
            <Local>139.XX.XX.32</Local>
            <IpsecConfig>
                  <IpsecLifetime>86400</IpsecLifetime>
                  <IpsecAuthAlg>sha1</IpsecAuthAlg>
                  <IpsecPfs>group2</IpsecPfs>
                  <IpsecEncAlg>aes</IpsecEncAlg>
            </IpsecConfig>
            <Remote>116.XX.XX.69x</Remote>
            <LocalSubnet>172.16.2.0/24</LocalSubnet>
            <IkeConfig>
                  <IkeEncAlg>aes</IkeEncAlg>
                  <IkePfs>group2</IkePfs>
                  <RemoteId>116.XX.XX.69</RemoteId>
                  <IkeAuthAlg>sha1</IkeAuthAlg>
                  <Psk>pgw6dy7d1i8i****</Psk>
                  <IkeMode>main</IkeMode>
                  <IkeLifetime>86400</IkeLifetime>
                  <IkeVersion>ikev1</IkeVersion>
                  <LocalId>139.XX.XX.32</LocalId>
            </IkeConfig>
      </VpnConnectionConfig>
</DownloadVpnConnectionConfigResponse>
```

`JSON` format `{`

```json
    "RequestId": "0C68048B-0F70-40DA-B8AE-1B79B5CF62E3",
    "VpnConnectionConfig": {
        "RemoteSubnet": "10.10.1.0/24,10.10.2.0/24",
        "Local": "139.XX.XX.32",
        "IpsecConfig": {
            "IpsecLifetime": 86400,
            "IpsecAuthAlg": "sha1",
            "IpsecPfs": "group2",
            "IpsecEncAlg": "aes"
```

`},`

```json
        "Remote": "116.XX.XX.69",
        "LocalSubnet": "172.16.2.0/24",
        "IkeConfig": {
            "IkeEncAlg": "aes",
            "IkePfs": "group2",
            "RemoteId": "116.XX.XX.69",
            "IkeAuthAlg": "sha1",
            "Psk": "pgw6dy7d1i8i****",
            "IkeMode": "main",
            "IkeLifetime": 86400,
            "IkeVersion": "ikev1",
            "LocalId": "139.XX.XX.32"
```

`}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectio nInstanceId.NotFoun d | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. Check whether the ID of the IPsec-VPN connection is valid. |

###### 2.1.14.4.4 CreateVpnConnection

Creates an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVpnConnec tion | The operation that you want to perform. Set the value to Creat eVpnConnect ion. |
| CustomerGatewa yId | String | Yes | vpn- bp1q8bgx4xnk*** * | The ID of the customer gateway. |
| LocalSubnet | String | Yes | 10.1.1.0/24,10.1. 2.0/24 | The CIDR block of the virtual private cloud (VPC) that is used to connect with the data center. This CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the IPsec-VPN connection. You can call the DescribeRegions operation to query the most recent region list. |
| RemoteSubnet | String | Yes | 10.10.1.0/24,10.1 0.2.0/24 | The CIDR block of the data center. The peer CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |
| VpnGatewayId | String | Yes | vpn- bp1q8bgx4xnkm* *** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter and cannot start with http:// or https:// . |
| EffectImmediatel y | Boolean | No | false | Specifies whether to delete the current IPsec tunnel and reinitiate negotiations. Valid values: t rue: initiates negotiations after the configuration is completed. f alse: initiates negotiations when inbound traffic is detected. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | {"IkeVersion":"ike v1","IkeMode":"m ain","IkeEncAlg":" aes","IkeAuthAlg" :"sha1","IkePfs":" group2","IkeLifeti me":86400} | The configuration of Phase 1 negotiations: IkeConf ig.Psk: the pre-shared key that is used to authenticate the VPN gateway and the customer gateway. By default, a random value is generated. You can also specify a pre-shared key. The description cannot exceed 100 characters in length. IkeConf ig.IkeVersion: The version of the IKE protocol. Valid values: ikev1 and ikev2. Default value: ikev1. IkeConf ig.IkeMode: the negotiation mode of IKE V1. Valid values: main and aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm used in Phase 1 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm used in Phase 1 negotiations. Valid values: md5 and sha1. Default value: md5. IkeConf ig.IkePf s: The Diffie- Hellman key exchange algorithm used in Phase 1 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IkeConf ig.IkeLif et ime: the SA lifetime as a result of Phase 1 negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: the identifier of the VPN gateway. This parameter can contain up to 100 characters. The default value is the public IP address of the VPN gateway. IkeConf ig.Remot eId: the identifier of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | {"IpsecEncAlg":"a es","IpsecAuthAlg ":"sha1","IpsecPf s":"group2","Ipse cLifetime":86400} | The configuration of Phase 2 negotiations: IpsecConf ig.IpsecEncAlg: The encryption algorithm used in Phase 2 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm used in Phase 2 negotiations. Valid values: md5 and sha1. Default value: md5. IpsecConf ig. IpsecPf s: the Diffie- Hellman group for perfect forward secrecy (PFS). If you set this parameter, the system forwards packets of all protocols. The Diffie- Hellman key exchange algorithm used in Phase 2 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IpsecConf ig. IpsecLif et ime: the SA lifetime as a result of Phase 2 negotiations. Valid values: 0 t o 86400. Unit: seconds. Default value: 86400. |
| HealthCheckConfi g | String | No | {"enable":"true"," dip":"192.168.xx. 2","sip":"192.168. xx.2","interval":"3 ","retry":"3"} | The health check configuration: Healt hCheckConf ig.enable: specifies whether to enable health checks. Valid values: t rue and f alse. Default value: false. Healt hCheckConf ig.dip: the destination IP address configured for health checks. Healt hCheckConf ig.sip: the source IP address configured for health checks. Healt hCheckConf ig.int erval: the time interval of health check retries. Unit: seconds. Healt hCheckConf ig.ret ry: the maximum number of health check retries. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically configure routes. Valid values: t rue: enables automatic configuration. f alse: disables automatic configuration. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp15oes1py4i6**** | The ID of the IPsec-VPN connection. |
| CreateTime | Long | 1544666102000 | The timestamp generated when the IPsec- VPN connection was created. |
| Name | String | test | The name of the IPsec-VPN connection. |
| RequestId | String | 082AD562-B8DB- 4BB2-861F- DA1FCA01FD76 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVpnConnection &CustomerGatewayId=vpn-bp1q8bgx4xnk**** &LocalSubnet=10.1.1.0/24,10.1.2.0/24 &RegionId=cn-qingdao-env66-d01 &RemoteSubnet=10.10.1.0/24,10.10.2.0/24 &VpnGatewayId=vpn-bp1q8bgx4xnkm**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVpnConnectionResponse>
      <VpnConnectionId>vco-bp1bbi27hojx8****</VpnConnectionId>
      <CreateTime>1493363928000</CreateTime>
</CreateVpnConnectionResponse>
```

`JSON` format `{`

```json
    "CreateTime": 1544666102000,
    "VpnConnectionId": "vco-bp15oes1py4i6****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 404 | InvalidCustomerGate wayInstanceId.NotF ound | The specified customer gateway instance id does not exist. | The error message returned because the specified instance ID does not exist. |
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | InvalidVpnConnectio n.AlreadyExists | Vpn connection already exists. | The error message returned because the IPsec-VPN connection already exists. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.4.5 DescribeVpnConnections

Queries one or more IPsec-VPN connections. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnConn ections | The operation that you want to perform. Set the value to DescribeVpnConnect ions. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the IPsec- VPN connections are created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | No | vpn- bp1q8bgx4xnkx** ** | The ID of the VPN gateway. |
| CustomerGatewa yId | String | No | cgw- bp1mvj4g9kogw* *** | The ID of the customer gateway. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| VpnConnectionId | String | No | vco- bp15oes1py4i6** ** | The ID of the IPsec-VPN connection. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnection s | Array of VpnConnection |   | The detailed information about the IPsec- VPN connections. |
| VpnConnection |   |   |   |
| IkeConfig | Struct |   | The configuration of Phase 1 negotiations. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. Valid values: sha1 and MD5. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. Unit: seconds. |
| IkeMode | String | main | The IKE mode. Valid values: main and aggressive . The main mode offers higher security. If NAT traversal is enabled, we recommend that you select the aggressive mode. |
| IkePfs | String | group2 | The DH group. Valid values: group1, group2, group5, group14, and group24. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.64 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d**** | The pre-shared key. |
| RemoteId | String | 139.XX.XX.167 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of Phase 2 negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm.Valid values: sha1 and md5. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpsecPfs | String | group2 | The DH group. |
| VpnConnectionI d | String | vco- bp10lz7aejumd**** | The ID of the IPsec-VPN connection. |
| CustomerGate wayId | String | cgw- bp1mvj4g9kogw**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm**** | The ID of the VPN gateway. |
| Name | String | name | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0 /24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2 .0/24 | The CIDR block of the data center. |
| CreateTime | Long | 1492753817000 | The timestamp generated when the IPsec- VPN connection was created. |
| Status | String | ipsec sa establishe _ _ d | The status of the IPsec-VPN connection. Valid values: ike sa not est ablished: indicates that _ _ _ Phase 1 negotiations failed. ike sa est ablished: indicates that _ _ Phase 1 negotiations succeeded. ipsec sa not est ablished: indicates _ _ _ that Phase 2 negotiations failed. ipsec sa est ablished: indicates that _ _ Phase 2 negotiations succeeded. |
| EffectImmediat ely | Boolean | true | Indicates whether IPsec-VPN negotiations are initiated immediately. Valid values: t rue: Negotiations are reinitiated when the configuration is changed. f alse: Negotiations are reinitiated when traffic is detected. When negotiations are reinitiated, transient connections may occur. |
| VcoHealthChec k | Struct |   | The configuration of health checks. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Dip | String | 8.XX.XX.8 | The destination IP address. |
| Enable | String | true | Indicates whether health checks are enabled. Valid values: t rue: Health checks are enabled. f alse: Health checks are disabled. |
| Interval | Integer | 2 | The interval between two consecutive health checks. Unit: seconds. |
| Retry | Integer | 1 | The maximum number of health check retries. |
| Sip | String | 192.XX.XX.66 | The source IP address that is used for health checks. |
| Status | String | failed | The status of the health check. Valid values: f ailed: The health check failed. success: The health check was successful. |
| TotalCount | Integer | 10 | The number of entries. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| RequestId | String | 54A4B3D0-DF4D- 4C54-B8DC- 5DC8DD49C939 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnConnections &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVpnConnections>
   <PageNumber>1</PageNumber>
   <VpnConnections>
      <VpnConnection>
         <Name>VPN connection test</Name>
         <CustomerGatewayId>cgw-bp1pvpl9r9adjxxxxxxxx</CustomerGatewayId>
         <RemoteSubnet>172.16.2.0/24</RemoteSubnet>
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
         <LocalSubnet>10.1.1.0/24,10.1.2.0/24</LocalSubnet>
         <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.XX.XX.167</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.XX.XX.64</LocalId>
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
    "PageNumber": 1,
    "VpnConnections": {
        "VpnConnection": [
```

`{`

```json
                "Name": "vpn connection test",
                "CustomerGatewayId": "cgw-bp1pvpl9r9adjxxxxxxxx",
                "RemoteSubnet": "172.16.2.0/24",
                "IpsecConfig": {
                    "IpsecLifetime": 86400,
                    "IpsecAuthAlg": "sha1",
                    "IpsecPfs": "group2",
                    "IpsecEncAlg": "aes"
```

`},`

```json
                "EffectImmediately": true,
                "VpnGatewayId": "vpn-bp1q8bgx4xnkmxxxxxxxx",
                "CreateTime": 1492753817000,
                "VpnConnectionId": "vco-bp10lz7aejumdxxxxxxxx",
                "status": "ipsec_sa_established",
                "LocalSubnet": "10.1.1.0/24,10.1.2.0/24",
                "IkeConfig": {
                    "IkeEncAlg": "aes",
                    "RemoteId": "139.XX.XX.167",
                    "IkePfs": "group2",
                    "IkeAuthAlg": "sha1",
                    "Psk": "pgw6dy****",
                    "IkeMode": "main",
                    "IkeLifetime": 86400,
                    "IkeVersion": "ikev1",
                    "LocalId": "116.XX.XX.64"
```

`}` `}` `]` `},`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "54A4B3D0-DF4D-4C54-B8DC-5DC8DD49C939"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.4.6 ModifyVpnConnectionAttribute

Modifies the configuration of an IPsec-VPN connection. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVpnConne ctionAttribute | The operation that you want to perform. Set the value to Modif yVpnConnect ionAt t ribut e. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the IPsec- VPN connection is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnConnectionId | String | Yes | vco- bp1bbi27hojx80n ck**** | The ID of the IPsec-VPN connection. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | IPsec | The name of the IPsec-VPN connection. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. However, the name cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LocalSubnet | String | No | 10.1.1.0/24,10.1. 2.0/24 | The CIDR block of the virtual private cloud (VPC) that is used to connect with the data center. This CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.1.0/24,192.168.2.0/24. |
| RemoteSubnet | String | No | 10.10.1.0/24,10.1 0.2.0/24 | The CIDR block of the data center. This CIDR block is used in Phase 2 negotiations. Separate multiple CIDR blocks with commas (,). Example: 192.168.3.0/24,192.168.4.0/24. |
| EffectImmediatel y | Boolean | No | false | Specifies whether to delete the current IPsec tunnel and reinitiate negotiations. Valid values: t rue: initiates negotiations after the configuration is completed. f alse: initiates negotiations when inbound traffic is detected. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IkeConfig | String | No | {"IkeVersion":"ike v1","IkeMode":"m ain","IkeEncAlg":" aes","IkeAuthAlg" :"sha1","IkePfs":" group2","IkeLifeti me":86400} | The configuration of Phase 1 negotiations: IkeConf ig.Psk: the pre-shared key that is used to authenticate the VPN gateway and the customer gateway. You can specify a key or use the default key that is randomly generated by the system. The key must be 1 to 100 characters in length. IkeConf ig.IkeVersion: the version of the IKE protocol. Valid values: ikev1 and ikev2. Default value: ikev1. IkeConf ig.IkeMode: the negotiation mode of IKE V1. Valid values: main and aggressive. Default value: main. IkeConf ig.IkeEncAlg: The encryption algorithm of Phase 1 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IkeConf ig.IkeAut hAlg: The authentication algorithm of Phase 1 negotiations. Valid values: md5 and sha1. Default value: sha1. IkeConfig.IkePfs: The Diffie-Hellman key exchange algorithm of Phase 1 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IkeConf ig.IkeLif et ime: the SA lifetime as a result of Phase 1 negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. IkeConf ig.LocalIdIPsec: the identifier of the VPN gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the VPN gateway. IkeConf ig.Remot eId: the identifier of the customer gateway. This parameter can contain up to 100 characters. By default, it is the public IP address of the customer gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IpsecConfig | String | No | {"IpsecEncAlg":"a es","IpsecAuthAlg ":"sha1","IpsecPf s":"group2","Ipse cLifetime":86400} | The configuration of Phase 2 negotiations: IpsecConf ig.IpsecEncAlg: The encryption algorithm of Phase 2 negotiations. Valid values: aes, aes192, aes256, des, and 3des. Default value: aes. IpsecConf ig. IpsecAut hAlg: The authentication algorithm of Phase 2 negotiations. Valid values: md5 and sha1. Default value: sha1. IpsecConf ig. IpsecPf s: the Diffie- Hellman group for perfect forward secrecy (PFS). If you set this parameter, the system forwards packets of all protocols. The Diffie- Hellman key exchange algorithm of Phase 2 negotiations. Valid values: group1, group2, group5, group14, and group24. Default value: group2. IpsecConf ig. IpsecLif et ime: the SA lifetime as a result of Phase 2 negotiations. Valid values: 0 to 86400. Unit: seconds. Default value: 86400. |
| HealthCheckConfi g | String | No | {"enable":"true"," dip":"192.168.xx. 2","sip":"192.168. xx.2","interval":"3 ","retry":"3"} | The health check configuration: Healt hCheckConf ig.enable: specifies whether to enable health checks. Valid values: t rue and f alse. Default value: false. Healt hCheckConf ig.dip: the destination IP address configured for the health check. Healt hCheckConf ig.sip: the source IP address configured for the health check. Healt hCheckConf ig.int erval: the time interval of health check retries. Unit: seconds. Healt hCheckConf ig.ret ry: the maximum number of health check retries. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoConfigRoute | Boolean | No | true | Specifies whether to automatically advertise routes. Valid values: t rue: enables automatic advertising. f alse: disables automatic advertising. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpnConnectionI d | String | vco- bp1bbi27hojx80nck* *** | The ID of the IPsec-VPN connection. |
| CustomerGate wayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the customer gateway. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |
| Name | String | test | The name of the IPsec-VPN connection. |
| LocalSubnet | String | 10.1.1.0/24,10.1.2.0 /24 | The CIDR block of the VPC. |
| RemoteSubnet | String | 10.10.1.0/24,10.10.2 .0/24 | The CIDR block of the data center. |
| CreateTime | Long | 1492753817000 | The timestamp generated when the IPsec- VPN connection was created. |
| Description | String | description | The description of the IPsec-VPN connection. |
| EffectImmediat ely | Boolean | false | Indicates whether IPsec-VPN negotiations are initiated immediately. Valid values: t rue: initiates negotiations after the configuration is completed. f alse: initiates negotiations when inbound traffic is detected. |
| IkeConfig | Struct |   | The configuration of Phase 1 negotiations. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IkeAuthAlg | String | sha1 | The IKE authentication algorithm. |
| IkeEncAlg | String | aes | The IKE encryption algorithm. |
| IkeLifetime | Long | 86400 | The IKE lifetime. |
| IkeMode | String | main | The IKE mode. |
| IkePfs | String | group2 | The DH group. |
| IkeVersion | String | ikev1 | The IKE version. |
| LocalId | String | 116.XX.XX.64 | The local ID. The default value is the IP address of the VPN gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. |
| Psk | String | pgw6dy7d1i8i**** | The pre-shared key. |
| RemoteId | String | 139.XX.XX.167 | The peer ID. The default value is the IP address of the customer gateway. Both FQDNs and IP addresses are supported. |
| IpsecConfig | Struct |   | The configuration of Phase 2 negotiations. |
| IpsecAuthAlg | String | sha1 | The IPsec authentication algorithm. |
| IpsecEncAlg | String | aes | The IPsec encryption algorithm. |
| IpsecLifetime | Long | 86400 | The IPsec lifetime. |
| IpsecPfs | String | group2 | The DH group. |
| RequestId | String | 7DB79D0C-5F27- 4AB5-995B- 79BE55102F90 | The ID of the request. |
| VcoHealthChec k | Struct |   | The health check configuration. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Dip | String | 1.XX.XX.1 | The destination IP address. |
| Enable | String | true | Indicates whether health checks are enabled. Valid values: t rue: Health checks are enabled. f alse: Health checks are disabled. |
| Interval | Integer | 3 | The interval between two consecutive health checks. Unit: seconds. |
| Retry | Integer | 1 | The maximum number of health check retries. |
| Sip | String | 2.XX.XX.2 | The source IP address. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVpnConnectionAttribute &RegionId=cn-qingdao-env66-d01 &VpnConnectionId=vco-bp1bbi27hojx80nck**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVpnConnectionAttributeResponse>
      <Name>vpn</Name>
      <CustomerGatewayId>cgw-bp1pvpl9r9adju6l5****</CustomerGatewayId>
      <RemoteSubnet>172.16.2.0/24</RemoteSubnet>
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
      <LocalSubnet>10.1.1.0/24,10.1.2.0/24</LocalSubnet>
      <IkeConfig>
            <IkeEncAlg>aes</IkeEncAlg>
            <RemoteId>139.XX.XX.32</RemoteId>
            <IkePfs>group2</IkePfs>
            <IkeAuthAlg>sha1</IkeAuthAlg>
            <Psk>pgw6dy7d1i8i****</Psk>
            <IkeMode>main</IkeMode>
            <IkeLifetime>86400</IkeLifetime>
            <IkeVersion>ikev1</IkeVersion>
            <LocalId>116.XX.XX.69</LocalId>
      </IkeConfig>
</ModifyVpnConnectionAttributeResponse>
```

`JSON` format `{`

```json
    "Name": "vpn",
    "CustomerGatewayId": "cgw-bp1pvpl9r9adju6l5****",
    "RemoteSubnet": "172.16.2.0/24",
    "IpsecConfig": {
        "IpsecLifetime": 86400,
        "IpsecAuthAlg": "sha1",
        "IpsecPfs": "group2",
        "IpsecEncAlg": "aes"
```

`},`

```json
    "EffectImmediately": false,
    "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
    "CreateTime": 1492753817000,
    "VpnConnectionId": "vco-bp10lz7aejumd2vxo****",
    "RequestId": "7DB79D0C-5F27-4AB5-995B-79BE55102F90",
    "LocalSubnet": "10.1.1.0/24,10.1.2.0/24",
    "IkeConfig": {
        "IkeEncAlg": "aes",
        "RemoteId": "139.XX.XX.32",
        "IkePfs": "group2",
        "IkeAuthAlg": "sha1",
        "Psk": "pgw6dy7d1i8i****",
        "IkeMode": "main",
        "IkeLifetime": 86400,
        "IkeVersion": "ikev1",
        "LocalId": "116.XX.XX.69"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 404 | InvalidVpnConnectio nInstanceId.NotFoun d | The specified vpn connection instance id does not exist. | The error message returned because the specified IPsec-VPN connection does not exist. You can check whether the configuration of the connection is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |

##### 2.1.14.5 SSL-VPN

###### 2.1.14.5.1 CreateSslVpnServer

Creates an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnServ er | The operation that you want to perform. Set the value to Creat eSslVpnServer. |
| ClientIpPool | String | Yes | 192.168.1.0/24 | The CIDR block that is allocated to the virtual network interface of the client. It is not the CIDR block where the client resides. When the client accesses the server through an SSL-VPN connection, the VPN gateway selects an IP address from the specified CIDR block and assigns it to the client. This CIDR block must not conflict with the value of LocalSubnet . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LocalSubnet | String | Yes | 10.0.0.0/8 | The CIDR block to be accessed by the client through the SSL-VPN connection. You can set the value to the CIDR block of a VPC, a vSwitch, a data center that is connected to the VPC through an Express Connect circuit, or an Alibaba Cloud service, such as ApsaraDB RDS or OSS. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnGatewayId | String | Yes | vpn- bp1hgim8by0kc9 nga**** | The ID of the VPN gateway. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | sslvpnname | The name of the SSL-VPN server. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, but cannot start with http:// or https:// . |
| Proto | String | No | UDP | The protocol that is used by the SSL- VPN server. Valid values: T CP: TCP. UDP : UDP. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cipher | String | No | AES-128-CBC | The encryption algorithm that is used in the SSL-VPN connection. Valid values: AES-128-CBC: the AES-128-CBC algorithm. This is the default value. AES-192-CBC: the AES-192-CBC algorithm. AES-256-CBC: the AES-256-CBC algorithm. none: If the parameter is set to this value, no encryption algorithm is used. |
| Port | Integer | No | 1194 | The port that is used by the SSL-VPN server. Default value: 1194. The following ports cannot be used: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. |
| Compress | Boolean | No | false | Specifies whether to enable data compression. Valid values: t rue: enables data compression. f alse: disables data compression. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | test | The name of the SSL-VPN server. |
| RequestId | String | E98A9651-7098- 40C7-8F85- C818D1EBBA85 | The ID of the request. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v* *** | The ID of the SSL-VPN server. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSslVpnServer &ClientIpPool=192.168.1.0/24 &LocalSubnet=10.0.0.0/8 &RegionId=cn-qingdao-env66-d01 &VpnGatewayId=vpn-bp1hgim8by0kc9nga**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateSslVpnServerResponse>
      <RequestId>E98A9651-7098-40C7-8F85-C818D1EBBA85</RequestId>
      <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
      <Name>test</Name>
</CreateSslVpnServerResponse>
```

`JSON` format `{`

```json
    "RequestId": "E98A9651-7098-40C7-8F85-C818D1EBBA85",
    "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
    "Name": "test"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 400 | InvalidName | The name is not valid | The error message returned because the format of the specified name is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVpnGatewayIn stanceId.NotFound | The specified vpn gateway instance id does not exist. | The error message returned because the specified VPN gateway does not exist. Check whether the configuration of the VPN gateway is valid. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.5.2 DeleteSslVpnServer

Deletes an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnServ er | The operation that you want to perform. Set the value to Delet eSslVpnServer. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the SSL-VPN server is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv 4v**** | The ID of the SSL-VPN server. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSslVpnServer &RegionId=cn-qingdao-env66-d01 &SslVpnServerId=vss-bp18q7hzj6largv4v**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSslVpnServerResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnServerResponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.5.3 ModifySslVpnServer

Modifies the configuration of an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnServ er | The operation that you want to perform. Set the value to Modif ySslVpnServer. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- bp18q7hzj6largv 4v**** | The ID of the SSL-VPN server. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | test | The name of the SSL-VPN server. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, and cannot start with http:// or https:// . |
| ClientIpPool | String | No | 10.30.30.0/24 | The client IP address pool. |
| LocalSubnet | String | No | 10.20.20.0/24 | The CIDR block of the VPC. |
| Proto | String | No | UDP | The protocol that is used by the SSL- VPN server. Valid values: T CP: TCP UDP: UDP. This is the default value. |
| Cipher | String | No | AES-128-CBC | The encryption algorithm that is used in the SSL-VPN connection. Valid values: AES-128-CBC: the AES-128-CBC algorithm. This is the default value. AES-192-CBC: the AES-192-CBC algorithm. AES-256-CBC: the AES-256-CBC algorithm. none: If the parameter is set to this value, no encryption algorithm is used. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Port | Integer | No | 1194 | The port that is used by the SSL-VPN server. Default value: 1194. The following ports cannot be used: 22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, and 4500. |
| Compress | Boolean | No | false | Specifies whether to enable data compression. Valid values: t rue: enables data compression. f alse: disables data compression. This is the default value. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cipher | String | AES-128-CBC | The encryption algorithm. |
| ClientIpPool | String | 10.30.30.0/24 | The client IP address pool. |
| Compress | Boolean | false | Indicates whether data compression is enabled. |
| Connections | Integer | 0 | The total number of current connections. |
| CreateTime | Long | 1492753580000 | The time when the SSL-VPN server was created. |
| InternetIp | String | 47.XX.XX.98 | The public IP address. |
| LocalSubnet | String | 10.20.20.0/24 | The CIDR block of the VPC. |
| MaxConnection s | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL-VPN server. |
| Port | Integer | 1194 | The port that is used by the SSL-VPN server. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Proto | String | UDP | The protocol that is used by the SSL-VPN server. |
| RegionId | String | cn-qingdao-env66- d01 | The region ID of the SSL-VPN server. |
| RequestId | String | DF11D6F6-E35A- 41C3-9B20- 6FC8A901FE65 | The ID of the request. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v* *** | The ID of the SSL-VPN server. |
| VpnGatewayId | String | vpn- bp1q8bgx4xnkm2og j**** | The ID of the VPN gateway. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySslVpnServer &RegionId=cn-qingdao-env66-d01 &SslVpnServerId=vss-bp18q7hzj6largv4v**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySslVpnServerResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-qingdao-env66-d01</RegionId>
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
                  <InternetIp>47.XX.XX.98</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</ModifySslVpnServerResponse>
```

`JSON` format `{`

```json
    "PageNumber": "1",
    "TotalCount": "1",
    "PageSize": "10",
    "SslVpnServers": {
        "SslVpnServer": {
            "RegionId": "cn-qingdao-env66-d01",
            "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
            "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
            "Name": "test",
            "CLientIpPool": "10.30.30.0/24",
            "LocalSubnet": "10.20.20.0/24",
            "Proto": "UDP",
            "Port": "1194",
            "Cipher": "AES-128-CBC",
            "Compress": "true",
            "CreateTime": "1492753580000",
            "Connections": "0",
            "MaxConnections": "5",
            "InternetIp": "47.XX.XX.98"
```

`}` `},`

```json
    "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |

###### 2.1.14.5.4 DeleteSslVpnClientCert

Deletes an SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSslVpnClie ntCert | The operation that you want to perform. Set the value to Delet eSslVpnClient Cert . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the SSL-VPN client certificate is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertI d | String | Yes | vsc- bp1n8wcf134yl0 osr**** | The ID of the SSL-VPN client certificate. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp1n8wcf134yl0osr**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSslVpnClientCertResponse>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</DeleteSslVpnClientCertResponse>
```

`JSON` format `{`

```json
  "RequestId":"606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |

###### 2.1.14.5.5 ModifySslVpnClientCert

Modifies the name of an SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySslVpnClie ntCert | The operation that you want to perform. Set the value to Modif ySslVpnClient Cert . |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the SSL-VPN client certificate is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SslVpnClientCertI d | String | Yes | vsc- bp1n8wcf134yl0 osrc**** | The ID of the SSL-VPN client certificate. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | cert2 | The name of the SSL-VPN client certificate. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. However, the name cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | cert2 | The name of the SSL-VPN client certificate. |
| RequestId | String | 606998F0-B94D- 48FE-8316- ACA81BB230DA | The ID of the request. |
| SslVpnClientCer tId | String | vsc- bp1n8wcf134yl0osr* *** | The ID of the SSL-VPN client certificate. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp1n8wcf134yl0osrc**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifySslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <Name>cert2</Name>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</ModifySslVpnClientCertResponse>
```

`JSON` format `{`

```json
    "SslVpnClientCertId": "vsc-bp1n8wcf134yl0osr****",
    "Name": "cert2",
    "RequestId": "606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |

###### 2.1.14.5.6 CreateSslVpnClientCert

Creates an SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSslVpnClie ntCert | The operation that you want to perform. Set the value to Creat eSslVpnClient Cert . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the VPN gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | Yes | vss- m5et0q3iy1qex32 8w**** | The ID of the SSL-VPN server. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |
| Name | String | No | SslVpnClientCert1 | The name of the SSL-VPN client certificate. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, and cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Name | String | SslVpnClientCert | The name of the SSL-VPN client certificate. |
| RequestId | String | 079874CD-AEC1- 43E6-AC03- ADD96B6E4907 | The ID of the request. |
| SslVpnClientCer tId | String | vsc- m5euof6s5jy8vs5kd* *** | The ID of the SSL-VPN client certificate. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnServerId=vss-m5et0q3iy1qex328w**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateSslVpnClientCertResponse>
      <SslVpnClientCertId>vsc-bp1n8wcf134yl0osr****</SslVpnClientCertId>
      <RequestId>606998F0-B94D-48FE-8316-ACA81BB230DA</RequestId>
</CreateSslVpnClientCertResponse>
```

`JSON` format `{`

```json
    "SslVpnClientCertId": "vsc-bp1n8wcf134yl0osr****",
    "RequestId": "606998F0-B94D-48FE-8316-ACA81BB230DA"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |
| 400 | Resource.QuotaFull | The quota of resource is full | The error message returned because the resource quota is reached. |
| 400 | VpnGateway.Config uring | The specified service is configuring. | The error message returned because the operation is not allowed when the specified service is being configured. Try again later. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | VpnGateway.Financi alLocked | The specified service is financial locked. | The error message returned because the service is suspended due to overdue payments. Top up your account first. |
| 400 | InvalidName | The name is not valid | The error message returned because the specified name is in an invalid format. |

###### 2.1.14.5.7 DescribeSslVpnClientCerts

Queries one or more SSL-VPN client certificates. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnCli entCerts | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert s. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The region ID of the SSL-VPN client certificates to be queried. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | No | vss- bp18q7hzj6largv 4v**** | The ID of the SSL-VPN server. |
| SslVpnClientCertI d | String | No | vsc- bp1n8wcf134yl0 osr**** | The ID of the SSL-VPN client certificate. |
| Name | String | No | cert1 | The name of the SSL-VPN client certificate. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |
| SslVpnClientCer tKeys | Array of SslVpnClientCer tKey |   | The detailed information about the queried SSL client certificates. |
| SslVpnClientCer tKey |   |   |   |
| CreateTime | Long | 1492747187000 | The timestamp generated when the SSL client certificate was created. |
| EndTime | Long | 1494966335000 | The time to be generated when the SSL client certificate expires. |
| Name | String | cert1 | The name of the SSL-VPN client certificate. |
| RegionId | String | cn-qingdao-env66- d01 | The region ID of the SSL-VPN client certificate. |
| SslVpnClientCer tId | String | vsc- bp1n8wcf134yl0osr* *** | The ID of the SSL-VPN client certificate. |
| SslVpnServerId | String | vss- bp18q7hzj6largv4v* *** | The ID of the SSL-VPN server. |
| Status | String | normal | The status of the SSL-VPN client certificate. Valid values: expiring-soon: The SSL-VPN client certificate expires in one week. normal: The certificate is normal. expired: The certificate has expired. |
| TotalCount | Integer | 1 | The number of returned entries. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSslVpnClientCerts &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-qingdao-env66-d01</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.10.20.0/24</CLientIpPool>
                  <LocalSubnet>10.10.10.0/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.XX.XX.98</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
    "DescribeSslVpnServersResponse": {
        "PageNumber": "1",
        "TotalCount": "1",
        "PageSize": "10",
        "SslVpnServers": {
            "SslVpnServer": {
                "RegionId": "cn-qingdao-env66-d01",
                "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
                "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
                "Name": "test",
                "CLientIpPool": "10.10.20.0/24",
                "LocalSubnet": "10.10.10.0/24",
                "Proto": "UDP",
                "Port": "1194",
                "Cipher": "AES-128-CBC",
                "Compress": "true",
                "CreateTime": "1492753580000",
                "Connections": "0",
                "MaxConnections": "5",
                "InternetIp": "47.XX.XX.98"
```

`}` `},`

```json
        "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.5.8 DescribeSslVpnClientCert

Queries a specified SSL-VPN client certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnCli entCert | The operation that you want to perform. Set the value to DescribeSslVpnClient Cert . |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the SSL-VPN client certificate that you want to query is created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnClientCertI d | String | Yes | vsc- bp17r58rjf5r1gjyr **** | The ID of the SSL-VPN client certificate that you want to query. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CaCert | String | The CA certificate | The CA certificate. |
| ClientCert | String | The SSL-VPN client certificate | The SSL-VPN client certificate. |
| ClientConfig | String | The configuration of the client | The configuration of the client. |
| ClientKey | String | The key of the client | The key of the client. |
| CreateTime | Long | 1552550980000 | The timestamp generated when the SSL-VPN client certificate was created. |
| EndTime | Long | 1647158980000 | The timestamp to be generated when the SSL-VPN client certificate expires. |
| Name | String | abc | The name of the SSL-VPN client certificate. |
| RegionId | String | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN client certificate is created. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SslVpnClientCer tId | String | vsc- bp13k5mp4tg8v3z9 b**** | The ID of the SSL-VPN client certificate. |
| SslVpnServerId | String | vss- bp155e9yclsg1xgq4 **** | The ID of the SSL-VPN server. |
| Status | String | normal | The status of the SSL-VPN client certificate. Valid values: expiring-soon: The SSL-VPN client certificate expires in one week. normal: The certificate is normal. expired: The certificate has expired. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSslVpnClientCert &RegionId=cn-qingdao-env66-d01 &SslVpnClientCertId=vsc-bp17r58rjf5r1gjyr**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <Name>df</Name>
      <Status>normal</Status>
      <ClientConfig>****</ClientConfig>
      <ClientCert>****</ClientCert>
      <CreateTime>1552550980000</CreateTime>
      <RegionId>cn-qingdao-env66-d01</RegionId>
      <RequestId>49D54005-6E0E-4132-B305-F3A24DEDDDC9</RequestId>
      <EndTime>1647158980000</EndTime>
      <SslVpnClientCertId>vsc-bp13k5mp4tg8v3z9b****</SslVpnClientCertId>
      <ClientKey>****</ClientKey>
      <CaCert>****</CaCert>
      <SslVpnServerId>vss-bp155e9yclsg1xgq4****</SslVpnServerId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
 "Name": "df",
 "Status": "normal",
 "ClientConfig": "****",
 "ClientCert": "****",
 "CreateTime": 1552550980000,
 "RegionId": "cn-qingdao-env66-d01",
 "RequestId": "49D54005-6E0E-4132-B305-F3A24DEDDDC9",
 "EndTime": 1647158980000,
 "SslVpnClientCertId": "vsc-bp13k5mp4tg8v3z9b****",
 "ClientKey": "****",
 "CaCert": "****",
 "SslVpnServerId": "vss-bp155e9yclsg1xgq4****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.5.9 DescribeSslVpnServers

Queries one or more SSL-VPN servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSslVpnSe rvers | The operation that you want to perform. Set the value to DescribeSslVpnServers. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the SSL-VPN servers are created. You can call the DescribeRegions operation to query the most recent region list. |
| SslVpnServerId | String | No | vss- bp15j3du13gq1d gey**** | The ID of the SSL-VPN server. |
| VpnGatewayId | String | No | vpn- bp1on0xae9d771 ggi**** | The ID of the VPN gateway. |
| Name | String | No | test | The name of the SSL-VPN server. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned on each page. |
| RequestId | String | 085CA5EA-1E76- 43A8-981B- E0208DECA0CB | The ID of the request. |
| SslVpnServers | Array of SslVpnServer |   | The detailed information about the SSL-VPN servers. |
| SslVpnServer |   |   |   |
| Cipher | String | AES-128-CBC | The encryption algorithm. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ClientIpPool | String | 10.10.1.0/24 | The client IP address pool. |
| Compress | Boolean | false | Indicates whether the transmitted data is compressed. |
| Connections | Integer | 0 | The total number of current connections. |
| CreateTime | Long | 1544668844000 | The timestamp generated when the SSL-VPN server was created. |
| InternetIp | String | 47.XX.XX.167 | The public IP address. |
| LocalSubnet | String | 192.168.0.0/24 | The CIDR block of the client. |
| MaxConnection s | Integer | 5 | The maximum number of connections. |
| Name | String | test | The name of the SSL-VPN server. |
| Port | Integer | 1194 | The port that is used by the SSL-VPN server. |
| Proto | String | UDP | The protocol that is used by the SSL-VPN server. |
| RegionId | String | cn-qingdao-env66- d01 | The ID of the region where the SSL-VPN server is created. |
| SslVpnServerId | String | vss- bp15j3du13gq1dgey **** | The ID of the SSL-VPN server. |
| VpnGatewayId | String | vpn- bp1on0xae9d771ggi **** | The ID of the VPN gateway. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSslVpnServers &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeSslVpnServersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>10</PageSize>
      <SslVpnServers>
            <SslVpnServer>
                  <RegionId>cn-qingdao-env66-d01</RegionId>
                  <SslVpnServerId>vss-bp18q7hzj6largv4v****</SslVpnServerId>
                  <VpnGatewayId>vpn-bp1q8bgx4xnkm2ogj****</VpnGatewayId>
                  <Name>test</Name>
                  <CLientIpPool>10.10.10.0/24</CLientIpPool>
                  <LocalSubnet>10.10.20.0/24</LocalSubnet>
                  <Proto>UDP</Proto>
                  <Port>1194</Port>
                  <Cipher>AES-128-CBC</Cipher>
                  <Compress>true</Compress>
                  <CreateTime>1492753580000</CreateTime>
                  <Connections>0</Connections>
                  <MaxConnections>5</MaxConnections>
                  <InternetIp>47.XX.XX.167</InternetIp>
            </SslVpnServer>
      </SslVpnServers>
      <RequestId>DF11D6F6-E35A-41C3-9B20-6FC8A901FE65</RequestId>
</DescribeSslVpnServersResponse>
```

`JSON` format `{`

```json
    "PageNumber": "1",
    "TotalCount": "1",
    "PageSize": "10",
    "SslVpnServers": {
        "SslVpnServer": {
            "RegionId": "cn-qingdao-env66-d01",
            "SslVpnServerId": "vss-bp18q7hzj6largv4v****",
            "VpnGatewayId": "vpn-bp1q8bgx4xnkm2ogj****",
            "Name": "test",
            "CLientIpPool": "10.10.10.0/24",
            "LocalSubnet": "10.10.20.0/24",
            "Proto": "UDP",
            "Port": "1194",
            "Cipher": "AES-128-CBC",
            "Compress": "true",
            "CreateTime": "1492753580000",
            "Connections": "0",
            "MaxConnections": "5",
            "InternetIp": "47.XX.XX.167"
```

`}` `},`

```json
    "RequestId": "DF11D6F6-E35A-41C3-9B20-6FC8A901FE65"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

###### 2.1.14.5.10 DescribeVpnSslServerLogs

Queries the logs of an SSL-VPN server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVpnSslSe rverLogs | The operation that you want to perform. Set the value to DescribeVpnSslServerLogs. |
| RegionId | String | Yes | cn-qingdao- env66-d01 | The ID of the region where the SSL-VPN server is created. You can call the DescribeRegions operation to query the most recent region list. |
| VpnSslServerId | String | Yes | vss- bp155e9yclsg1xg q4**** | The name of the SSL-VPN server. |
| From | Integer | No | 2018020201 | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. If the From parameter is set, you must set the T o or Minut ePeriod parameter. |
| To | Integer | No | 2018020206 | The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. If the From parameter is set, you must set the T o or Minut ePeriod parameter. |
| MinutePeriod | Integer | No | 10 | The cycle of the logs. If the From and T o parameters are not set, you must set the Minut ePeriod parameter. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of log entries. |
| Data | List | test | An array of log entries. Each item in the array indicates a log entry. |
| IsCompleted | Boolean | true | Indicates whether the log data is accurate. Valid values: t rue: accurate f alse: inaccurate |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 5BE01CD7-5A50- 472D-AC14- CA181C5C03BE | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVpnSslServerLogs &RegionId=cn-qingdao-env66-d01 &VpnSslServerId=vss-bp155e9yclsg1xgq4**** &<Common request parameters>
```

Sample success responses `XML` format

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
 "Data": {
  "Logs": []
```

`},`

```json
 "PageNumber": 1,
 "Count": 0,
 "PageSize": 10,
 "IsCompleted": true,
 "RequestId": "26641E42-66C7-4942-9FEC-F99213914F8F"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden.SubUser | User not authorized to operate on the specified resource as your account is created by another user. | The error message returned because you are unauthorized to perform this operation on the specified resource. You can apply for the required permissions and try again. |
| 403 | Forbidden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. To acquire the required permissions, submit a ticket. |

#### 2.1.15 NAT gateways

##### 2.1.15.1 ModifyNatGatewayAttribute

Modifies the name and description of a NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatew ayAttribute | The operation that you want to perform. Set the value to Modif yNat Gat ewayAt t ribut e. |
| NatGatewayId | String | Yes | ngw- 2ze0dcn4mq31qx 2jc**** | The ID of the NAT gateway that you want to modify. |

| irtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | nat123 | The name of the NAT gateway that you want to modify. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. The name cannot start with http:// or https:// . Not e You must specify at least one of the following parameters: Name and Descript ion. |
| Description | String | No | fortest | The description of the NAT gateway. The description must be 2 to 256 characters in length, and must start with a letter. It cannot start with http:// or https:// . Not e You must specify at least one of the following parameters: Name and Descript ion. |

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

`JSON` format

```json
{"RequestId":"AB5F62CF-2B60-4458-A756-42C9DFE108D1"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |

##### 2.1.15.2 ModifyNatGatewaySpec

Resizes a NAT gateway. NAT gateways are available in different sizes. The size of a NAT gateway determines the Source Network Address Translation (SNAT) performance of the gateway, such as the maximum number of connections and the number of new connections per second. However, the data throughput is not affected. The following table describes the correlations between different sizes of NAT gateways and SNAT performance metrics.

| Size | Maximum connection | Number of new connections per second |
|---|---|---|
| Small | 10,000 | 1,000 |
| Medium | 50,000 | 5,000 |
| Large | 200,000 | 10,000 |

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatew aySpec | The operation that you want to perform. Set the value to Modif yNat Gat ewaySpec. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5 770**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. |
| Spec | String | Yes | Small | The size of the NAT gateway. Valid values: Small: a small-sized NAT gateway Middle: a middle-sized NAT gateway Large: a large-sized NAT gateway |
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: t rue: enables automatic payment. f alse: disables automatic payment. This is the default value. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | SHA234js121223* *** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters, and cannot exceed 64 characters in length. |

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
    "RequestId":"DBD4E4A2-786E-4BD2-8EB6-107FFC2B5B7D"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | NATGW MODIFY SPE _ _ C SAME _ | The specified Spec is same with now. | The error message returned because the specified gateway size is the same as the current one. |
| 400 | InvalidParameter.Sp ec.ValueNotSupport ed | The specified Spec is not valid. | The error message returned because the specified gateway size is invalid. |

##### 2.1.15.3 DeleteNatGateway

Deletes a specified NAT gateway. Not e Before you delete a NAT gateway, you must disassociate NAT service plans from the NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNatGatewa y | The operation that you want to perform. Set the value to Delet eNat Gat eway. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5 770**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT gateway. Valid values: t rue: forcibly deletes the NAT gateway. f alse: does not forcibly delete the NAT gateway. |

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
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | DependencyViolatio n.BandwidthPackage s | There are BandwidthPackages on specified NatGateway not deleted. | The error message returned because one or more NAT service plans are associated with the NAT gateway. Disassociate all NAT service plans from the NAT gateway and try again. |

##### 2.1.15.4 CreateForwardEntry

Adds a DNAT entry to a DNAT table. Each DNAT entry consists of the following parameters: ExternalIp, ExternalPort, Protocol, InternalIp, and InternalPort. After you add a DNAT entry, the NAT gateway forwards packets of the specified protocol from [ExternalIp: ExternalPort] to [InternalIp: InternalPort] and sends responses back over the same route. When you call this operation, take note of the following limits: The combinations of ExternalIp, ExternalPort, and Protocol used in DNAT entries must be unique. Requests cannot be distributed to more than one Elastic Compute Service (ECS) instance if these requests are originated from the same source IP address, received on the same port, and use the same protocol. The combinations of Protocol, InternalIp, and InternalPort used in DNAT entries must be unique. If one or more DNAT entries in the DNAT table are in the Pending or Modifying state, you cannot add DNAT entries to the DNAT table. The public IP address (ExternalIp) in the DNAT entry, which is used to access the Internet, must meet the following requirements: If you have purchased a NAT service plan before November 3, 2017, the ExternalIp must be a public IP address in the NAT service plan. If you have not purchased a NAT service plan before November 3, 2017, the ExternalIp must be an elastic IP address (EIP) associated with the NAT service plan. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. The private IP address (InternalIp) in the DNAT entry must meet the following requirements: The private IP address must belong to the CIDR block of the virtual private cloud (VPC) where the NAT gateway is deployed. The DNAT entry takes effect only when the private IP address is allocated to an ECS instance and the ECS instance is not assigned an EIP. If the private IP address is allocated to a resource other than an ECS instance, such as a high-availability virtual IP addresses (HAVIPs), Server Load Balancer (SLB) instance, or RDS instance, the DNAT entry does not take effect. Consequently, inbound traffic cannot be forwarded to the private IP address. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. You can add up to 100 DNAT entries to a DNAT table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateForwardEn try | The operation that you want to perform. Set the value to Creat eForwardEnt ry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ExternalIp | String | Yes | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | Yes | 8080 | The public port. Valid values: 1 t o 65535. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlc qpa**** | The ID of the DNAT table. |
| InternalIp | String | Yes | 192.XX.XX.1 | The destination private IP address. |
| InternalPort | String | Yes | 80 | The destination private port. Valid values: 1 t o 65535. |
| IpProtocol | String | Yes | TCP | The protocol that is used by the ports. Valid values: T CP: forwards TCP packets. UDP: forwards UDP packets. Any: forwards packets of all protocols. |
| RegionId | String | Yes | cn-qingdao- env17-d0 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. |
| PortBreak | Boolean | No | false | Specifies whether to remove limits on the port range. Valid values: t rue: removes limits on the port range. f alse (default): sets limits on the port range. Not e When an SNAT entry and a DNAT entry use the same public IP address, and you want to specify a port number greater than 1024, set Port Break to t rue. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardEntryId | String | fwd- 119smw5tkasdf**** | The ID of the DNAT entry. |
| RequestId | String | A4AEE536-A97A- 40EB-9EBE- 53A6948A6928 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateForwardEntry &ExternalIp=116.XX.XX.28 &ExternalPort=8080 &ForwardTableId=ftb-bp1mbjubq34hlcqpa**** &InternalIp=192.XX.XX.1 &InternalPort=80 &IpProtocol=TCP &RegionId=cn-qingdao-env17-d0 &<Common request parameters>
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
    "CreateForwardEntryResponse": {
        "RequestId": "A4AEE536-A97A-40EB-9EBE-53A6948A6928",
        "ForwardEntryId": "fwd-119smw5tkasdf****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidExternalIp.Mal formed | The specified ExternalIp is not a valid IP address. | The error message returned because the specified IP address is invalid. |
| 400 | InvalidInternalIp.Malf ormed | The specified InternalIp is not a valid IP address. | The error message returned because the specified private IP address is invalid. |
| 400 | InvalidExternalPort.M alformed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |
| 400 | InvalidInternalPort.M alformed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.Destnatio nIpOutOfVpcCIDR | The specified Internal Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.Valu eNotSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 404 | InvalidExternalIp.Not Found | Specified External Ip address does not found on the VRouter | The error message returned because the specified public IP address does not exist. |
| 400 | Forbidden.ExternalIp .UsedInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified public IP address is already used by an SNAT entry. Select a different IP address or delete the SNAT entry. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create forwarding rules. |
| 400 | Forbidden.InternalIp OutOfVpcCIDR | The specified Internal Ip is Out of VPC CIDR. | The error message returned because the private IP address does not fall within the CIDR block of the VPC. |
| 400 | Invalid.natgwNotExis t | The specified natgateway not exist. | The error message returned because the specified NAT gateway does not exist. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidIp.NotInNatg w | The specified Ip not belong to natgateway. | The error message returned because the specified IP address is not associated with the NAT gateway. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because one or more required parameters are not set. Check whether you have set all required parameters. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |

##### 2.1.15.5 DescribeForwardTableEntries

Queries DNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeForward TableEntries | The operation that you want to perform. Set the value to DescribeForwardT ableEnt ries. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlc qpa**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryId | String | No | fwd- 8vbn3bc8roygjp0 gy**** | The ID of the DNAT entry that is automatically assigned. |
| ExternalIp | String | No | 116.XX.XX.28 | The public IP address of the NAT gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ExternalPort | String | No | 8080 | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 192.XX.XX.1 | The destination private IP address. |
| InternalPort | String | No | 80 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: forwards TCP packets. UDP: forwards UDP packets. Any: forwards packets of all protocols. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardTableE ntries | Array of ForwardTableE ntry |   | The details of the DNAT entries. |
| ForwardTableE ntry |   |   |   |
| ExternalIp | String | 116.XXX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | 80 | The public port. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ForwardEntryId | String | fwd-119smw5tk**** | The ID of the DNAT entry. |
| ForwardEntryN ame | String | ForwardEntry-1 | The name of the DNAT entry. |
| ForwardTableId | String | ftb-11tc6xgmv**** | The ID of the DNAT table to which the DNAT entry belongs. |
| InternalIp | String | 192.XX.XX.1 | The private IP address. |
| InternalPort | String | 25 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | TCP | The protocol type. |
| Status | String | Available | The state of the DNAT entry. |
| TotalCount | Integer | 5 | The total number of entries returned. |
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
        <ExternalIp>116.XXX.XX.28</ExternalIp>
        <ForwardEntryId>fwd-119smw5tk****</ForwardEntryId>
        <IpProtocol>TCP</IpProtocol>
        <InternalPort>25</InternalPort>
        <ForwardEntryName>ForwardEntry-1</ForwardEntryName>
        <InternalIp>192.XX.XX.1</InternalIp>
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
        "ExternalIp": "116.XXX.XX.28",
        "ForwardEntryId": "fwd-119smw5tk****",
        "IpProtocol": "TCP",
        "InternalPort": 25,
        "ForwardEntryName": "ForwardEntry-1",
        "InternalIp": "192.XX.XX.1",
        "ForwardTableId": "ftb-11tc6xgmv****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. One or more DNAT entries in the DNAT table are in the Pending or Modifying state. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidForwardTableI d.NotFound | Specified forwardTableId does not exist | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |

##### 2.1.15.6 ModifyForwardEntry

Modifies a DNAT entry. Not e You cannot modify DNAT entries if one or more DNAT entries in the DNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyForwardEn try | The operation that you want to perform. The operation that you want to perform. Set the value to Modif yForwardEnt ry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0 gy3xk7 | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb3 34h0ow | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ExternalIp | String | No | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | No | 80 | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 10.XX.XX.78 | The destination private IP address. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InternalPort | String | No | 80 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: forwards Transmission Control Protocol (TCP) packets. UDP: forwards User Datagram Protocol (UDP) packets. Any: forwards packets of all protocols. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The description must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 24CC85DC-7700- 4F09-9624- 99E988C7DD03 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=ModifyForwardEntry &ForwardEntryId=fwd-8vbn3bc8roygjp0gy3xk7 &ForwardTableId=ftb-8vbx8xu2lqj9qb334h0ow &RegionId= cn-hangzhou &<Common request parameters>
```

Sample success responses `XML` format

```xml
</ModifyForwardEntryResponse> <RequestId>24CC85DC-7700-4F09-9624-99E988C7DD03</RequestId> </ModifyForwardEntryResponse>
```

`JSON` format `{`

```json
    "RequestId": "24CC85DC-7700-4F09-9624-99E988C7DD03"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | InvalidExternalIp.Mal formed | The specified ExternalIp is not a valid IP address. | The error message returned because the specified IP address is invalid. |
| 400 | InvalidInternalIp.Malf ormed | The specified InternalIp is not a valid IP address. | The error message returned because the specified private IP address is invalid. |
| 400 | InvalidExternalPort.M alformed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |
| 400 | InvalidInternalPort.M alformed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |
| 400 | Forbidden.Destnatio nIpOutOfVpcCIDR | The specified Destination Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.Valu eNotSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because the operation cannot be performed. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 400 | QuotaExceeded | Forward entry quota exceeded in this route table. | The error message returned because one route table cannot contain more than 48 custom routes to a route table. You can submit a ticket to increase the quota. |
| 404 | InvalidForwardEntryI d.NotFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidExternalIp.Not Found | Specified External Ip address does not found on the VRouter | The error message returned because the specified public IP address does not exist. |
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 400 | Forbidden.ExternalIp .UsedInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified public IP address is already used by an SNAT entry. Select a different IP address or delete the SNAT entry. |
| 400 | Forbidden.Already.B ounded | The specified instance already bounded | The error message returned because the specified instance is already associated with another DNAT entry. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the format of the specified name is invalid. |

##### 2.1.15.7 DeleteForwardEntry

Deletes a DNAT entry. Not e You cannot delete DNAT entries if one or more DNAT entries in the DNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteForwardEn try | The operation that you want to perform. Set the value to Delet eForwardEnt ry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0 g**** | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb3 34**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

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

`JSON` format

```json
{"RequestId":"0ED8D006-F706-4D23-88ED-E11ED28DCAC0"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardEntryI d.NotFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 400 | IncorretForwardEntr yStatus | The Specified forwardEntry is not exist | The error message returned because the specified DNAT entry does not exist. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because one or more required parameters are not set. Check whether you have set all required parameters. |

##### 2.1.15.8 CreateSnatEntry

Adds an SNAT entry to an SNAT table. When you call this operation, take note of the following limits: The vSwitch and the Elastic Compute Service (ECS) instance specified in the SNAT entry must belong to the virtual private cloud (VPC) where the NAT gateway is deployed. Each vSwitch or ECS instance can be specified in only one SNAT entry. If a high-availability virtual IP address (HAVIP) exists in the vSwitch, you cannot create SNAT entries. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSnatEntry | The operation that you want to perform. Set the value to Creat eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatIp | String | Yes | 47.XX.XX.98 | The public IP addresses. Separate multiple IP addresses with commas (,). |
| SnatTableId | String | Yes | stb- bp190wu8io1vge v**** | The ID of the SNAT table. |
| SourceVSwitchId | String | No | vsw- bp1nhx2s9ui5o*** * | The ID of the vSwitch that requires to access the Internet. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceCIDR | String | No | 10.1.1.0/24 | The CIDR block of the vSwitch or the IP address of the ECS instance. vSwitch granularity: specifies the CIDR block of the vSwitch, for example, 192.168.1.0/24. When an ECS instance of a vSwitch requires to access the Internet, the NAT gateway provides the SNAT service for the ECS instance. If you specify only one public IP address in the Snat Ip parameter, the ECS instance uses the specified public IP address to access the Internet. If you specify multiple public IP addresses in the Snat Ip parameter, the ECS instance randomly selects a public IP address from Snat Ip to access the Internet. ECS granularity: specifies the IP address of the ECS instance, for example, 192.168.1.0/32. When the ECS instance requires to access the Internet, the NAT gateway provides the SNAT service for the ECS instance. If you specify only one public IP address in the Snat Ip parameter, the ECS instance uses the specified public IP address to access the Internet. If you specify multiple public IP addresses in the Snat Ip parameter, the ECS instance randomly selects a public IP address from Snat Ip to access the Internet. This parameter and the SourceVSwt ichId parameter cannot be set at the same time. If the SourceVSwit chId parameter is set, you cannot set the SourceCIDR parameter. If the SourceCIDR parameter is set, you cannot set the SourceVSwit chId parameter. |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length, and must start with a letter. It cannot start with http:// or https:// . |

|   | http:// |
|---|---|
| https:// |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatEntryId | String | snat-kmd6nv8fy**** | The ID of the SNAT entry. |
| RequestId | String | 2315DEB7-5E92- 423A-91F7- 4C1EC9AD97C3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateSnatEntry &RegionId=cn-qingdao-env17-d01 &SnatIp=47.XX.XX.98 &SnatTableId=stb-bp190wu8io1vgev**** &<Common request parameters>
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
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 400 | Forbidden.SourceVS witchId.IncludeHaVip | There is some HaVips under specified VSwitch | The error message returned because the specified vSwitch is associated with HAVIPs. |
| 400 | InvalidSnatIp.Malfor med | The specified SnatIp is not a valid IP address. | The error message returned because the specified public IP address is invalid. |
| 400 | SNAT IP POOL COU _ _ _ NT TOO MANY _ _ | The Snat pool ip too many. | The error message returned because the number of IP addresses in the SNAT IP address pool has reached the upper limit. |
| 400 | Forbidden.SnatEntry CountLimited | SNAT entry in the specified SNAT table reach it?s limit. | The error message returned because the number of SNAT entries has reached the upper limit. |
| 400 | NOT ALLOW USE SO _ _ _ URCECIDR | The User not in nat scope unlimited white list. _ _ Cannot use SourceCidr param. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. |
| 404 | InvalidVSwitchId.Not Found | The specified virtual switch does not exists. | The error message returned because the specified vSwitch does not exist. Check whether the specified ID is valid. |
| 400 | INVALID PARAMETER _ | The parameter invalid. | The error message returned because the specified parameter is invalid. |
| 400 | Forbidden.SourceVS witchId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already created for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFou nd | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified public IP address is not found on the NAT gateway. |

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.IpUsedInF orwardTable | The specified SnatIp already used in forward table | The error message returned because the specified public IP address is already used by a DNAT entry. Select another public IP address or delete the DNAT entry. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create forwarding rules. |
| 400 | OperationUnsupport ed.CidrConflict | The specified CIDR block conflicts with an existing SNAT entry. | The error message returned because the specified CIDR block conflicts with those in existing SNAT entries. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |

##### 2.1.15.9 DescribeSnatTableEntries

Queries SNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSnatTabl eEntries | The operation that you want to perform. Set the value to DescribeSnat T ableEnt ries. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u 3t**** | The ID of the SNAT table. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SnatEntryId | String | No | snat- 8vbae8uqh7rjpk7 d2**** | The ID of the SNAT entry. |
| SourceVSwitchId | String | No | vsw-3xb**** | The ID of the vSwitch that can access the Internet through SNAT. |
| SourceCIDR | String | No | 116.XX.XX.0/28 | The source CIDR block of the SNAT entry. |
| SnatIp | String | No | 116.XX.XX.28 | The public IP address in the SNAT entry. |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The name must be 2 to 128 characters in length, and start with a letter. The name cannot start with http:// or https:// . |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatTableEntrie s | Array of SnatTableEntry |   | The detailed information about the SNAT entries. |
| SnatTableEntry |   |   |   |
| SnatEntryId | String | snat- 8vbae8uqh7rjpk7d2* *** | The ID of the SNAT entry. |
| SnatEntryName | String | SnatEntry-1 | The name of the SNAT entry. |
| SnatIp | String | 116.XX.XX.28 | The public IP address in the SNAT entry. |

|   | Developer Guide·AP | I reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnatTableId | String | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table to which the SNAT entry belongs. |
| SourceCIDR | String | 116.XX.XX.0/28 | The source CIDR block of the SNAT entry. |
| SourceVSwitchI d | String | vsw-3xb**** | The ID of the vSwitch that can access the Internet through SNAT. |
| Status | String | Pending | The state of the SNAT entry. |
| TotalCount | Integer | 1 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned on each page. |
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
        <SourceCIDR>116.XX.XX.0/28</SourceCIDR>
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
        "SourceCIDR": "116.XX.XX.0/28",
        "SnatEntryId": "snat-8vbae8uqh7rjpk7d2****",
        "SnatIp": "116.XX.XX.28",
        "SnatTableId": "stb-8vbczigrhop8x5u3t****"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |

##### 2.1.15.10 ModifySnatEntry

Modifies a specified SNAT entry. Not e You cannot modify SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySnatEntry | The operation that you want to perform. Set the value to Modif ySnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d0 | The ID of the region where the NAT gateway is deployed. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0pl qcg**** | The ID of the SNAT entry. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u 3t**** | The ID of the SNAT table to which the SNAT entry belongs. |
| SnatIp | String | Yes | 47.XX.XX.98 | The public IP address in the SNAT entry. If multiple IP addresses are specified, separate them with commas (,). |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The description must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Only ASCII characters are allowed. It can contain up to 64 ASCII characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2315DEB7-5E92- 423A-91F7- 4C1EC9AD97C3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifySnatEntry &RegionId=cn-qingdao-env17-d0 &SnatEntryId=snat-bp1vcgcf8tm0plqcg**** &SnatTableId=stb-8vbczigrhop8x5u3t**** &SnatIp=47.XX.XX.98 &<Common request parameters>
```

Successful response examples `XML` format

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
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 400 | InvalidSnatIp.Malfor med | The specified SnatIp is not a valid IP address. | The error message returned because the specified public IP address is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidSnatEntryId.N otFound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 400 | Forbidden.SourceVS witchId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already configured for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFou nd | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified public IP address does not exist in the NAT gateway. |
| 400 | Forbidden.IpUsedInF orwardTable | The specified SnatIp already used in forward table | The error message returned because the specified public IP address is already used by a DNAT entry. Select another IP address or delete the DNAT rule that uses the public IP address. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. |

##### 2.1.15.11 DeleteSnatEntry

Deletes a specified SNAT entry. Not e You cannot delete SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSnatEntry | The operation that you want to perform. Set the value to Delet eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0pl qc**** | The ID of the SNAT entry. |
| SnatTableId | String | Yes | stb- bp190wu8io1vge v80**** | The ID of the SNAT table. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 42665544**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 47B80B6A-759A- 479C-A565- 76D04BDA29F3 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSnatEntry &RegionId=cn-qingdao-env17-d01 &SnatEntryId=snat-bp1vcgcf8tm0plqc**** &SnatTableId=stb-bp190wu8io1vgev80**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteSnatEntryResponse>
  <RequestId>47B80B6A-759A-479C-A565-76D04BDA29F3</RequestId>
</DeleteSnatEntryResponse>
```

`JSON` format

```json
{"RequestId":"47B80B6A-759A-479C-A565-76D04BDA29F3"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretSnatEntrySta tus | Some Snat entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more SNAT entries in the SNAT table are in the Pending or Modifying state. |
| 404 | InvalidSnatEntryId.N otFound | Specified Snat entry ID does not exist | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 404 | InvalidSnatEntryId.N otFound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |

##### 2.1.15.12 ModifyBandwidthPackageSpec

Modifies the bandwidth value of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidth PackageSpec | The operation that you want to perform. Set the value to Modif yBandwidt hPackageSpec. |
| Bandwidth | String | Yes | 5 | The maximum bandwidth of the NAT service plan. Valid values: 5 to 1000. |
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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

| Developer Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |
| 404 | BandwidthPackage.F inancialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

##### 2.1.15.13 DeleteBandwidthPackage

Deletes a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBandwidth Package | The operation to perform. Set the value to paybytraffic. Delet eBandwidt hPackage |
| BandwidthPackag eId | String | Yes | bwp- bp1arsrmca9kp** ** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions interface to obtain the region ID. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT service plan. f alse (default): does not forcibly delete the bandwidth plan. t rue : forcibly deletes the bandwidth plan. |

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
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | DependencyViolatio n.ForwardEntry | The specified BandwidthPackageId has dependent resource. | The error message returned because the NAT service plan contains SNAT or DNAT entries. Delete them and try again. |
| 400 | DependencyViolatio n.SnatEntry | The specified BandwidthPackageId has dependent resource. | The error message returned because the NAT service plan contains SNAT or DNAT entries. Delete them and try again. |

##### 2.1.15.14 CreateBandwidthPackage

Creates a NAT service plan. A NAT service plan consists of bandwidth resources and one or more public IP addresses. You can associate up to four NAT service plans with a NAT gateway. A NAT service plan includes: Bandwidth resources One or more public IP addresses Not e This operation can be performed by only Apsara Stack accounts that have purchased NAT service plans before November 3, 2017. If you have not purchased a NAT service plan before November 3, 2017, you can apply for public IP addresses by associating elastic IP addresses (EIPs). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBandwidth Package | The operation that you want to perform. Set the value to Creat eBandwidt hPackage. |
| Bandwidth | Integer | Yes | 5 | The maximum bandwidth of the NAT service plan. Valid values: 5 to 1000. Unit: Mbit/s. |
| IpCount | Integer | Yes | 2 | The number of public IP addresses in the NAT service plan. Valid values: 1 t o 50. |
| NatGatewayId | String | Yes | ngw- 7mwb327j1**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | The name of the NAT service plan. | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. The name cannot start with http:// or https:// . |
| Description | String | No | The description of the NAT service plan. | The description of the NAT service plan. The name must be 2 to 256 characters in length, and start with a letter. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| ISP | String | No | BGP | Only BGP is supported. |
| Zone | String | No | cn-qingdao- env17- amtest11001-a | The zone to which the NAT service plan belongs. If you do not set this parameter, the service plan is randomly allocated to a zone. Not e Connectivity is not affected when the IP addresses provided by the NAT service plan and the backend Elastic Compute Service (ECS) instances belong to different zones. However, when the IP addresses and ECS instances belong to the same zone, latency can be reduced. |
| InternetChargeTy pe | String | No | PayByBandwidth | The metering method of the NAT service plan. Valid values: PayByT raf f ic: pay-by-data-transfer |

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
| 404 | InvalidVpcId.NotFou nd | Specified value of VpcId is not found in our record. | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | MissingParameter | Miss mandatory parameter. | The error message returned because one or more required parameters are not set. Check whether you have set all the required parameters before you call this operation. |
| 404 | InvalidZoneId.NotFo und | Specified value of ZoneId is not exists. | The error message returned because the specified zone does not exist. |
| 404 | InvalidZoneId.NotFo und | Can not find ZoneId for allocated ip. | The error message returned because the zone of the specified IP address is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Ban dwidthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Submit a ticket to increase the quota. |
| 400 | QuotaExceeded.Ban dwidthPackageCoun tOnNatGateway | BandwidthPackage count limit on one NatGateway exceeded. | The error message returned because the number of NAT service plans has reached the upper limit. You can associate up to four NAT service plans with a NAT gateway. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | InvalidParameter.Ba ndwidthPackage.n.IS P.ValueNotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified Internet service provider (ISP) of the EIP bandwidth plan is invalid. |
| 400 | ZONE NO AVAILABLE _ _ IP _ | The Zone have no available ip. | The error message returned because no IP address is available in the zone. |

##### 2.1.15.15 DescribeBandwidthPackages

Queries NAT service plans in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBandwid thPackages | The operation that you want to perform. Set the value to DescribeBandwidt hPackages. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BandwidthPackag eId | String | No | bwp- bp1xea10o8qxw dfs**** | The ID of the NAT service plan. |
| NatGatewayId | String | No | ngw- bp1uewa15k4iydf re**** | The ID of the NAT gateway. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BandwidthPack ages | Array of BandwidthPack age |   | The detailed description of the NAT service plan. |
| BandwidthPack age |   |   |   |
| Bandwidth | String | 5 | The bandwidth value of the NAT service plan. Valid values: 5 to 5000. Unit: Mbit/s. |
| BandwidthPack ageId | String | bwp- xxoo123sfwr**** | The ID of the NAT service plan. |
| BusinessStatus | String | Normal | The state of the NAT service plan. Valid values: Normal: The NAT service plan working as expected. FinancialLocked: The NAT service plan is locked due to overdue payments. Securit yLocked: The NAT service plan is locked due to security reasons. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| CreationTime | String | 2017-06- 08T12:20:55 | The time when the NAT service plan was created. The time follows the ISO 8601 standard in YYYY-MM-DDThh:mmZ format. It must be in UTC. |
| Description | String | test123 | The description of the NAT service plan. The description must be 2 to 256 characters in length. The description is displayed in the console. This parameter is empty by default. It cannot start with http:// or https:// . |
| ISP | String | BGP | Only BGP is supported. |
| InstanceCharge Type | String | PostPaid | The billing method of the NAT service plan. Only Post Paid (pay-as-you-go) is supported. |
| InternetCharge Type | String | PayByBandwidth | The metering method of the NAT service plan. PayByT raf f ic: pay-by-data-transfer |
| IpCount | String | 1 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. |
| Name | String | abc | The name of the NAT service plan. |
| NatGatewayId | String | ngw- xxoo123ggtf**** | The ID of the NAT gateway. |
| PublicIpAddress es | Array of PublicIpAddress e |   | The IP address in the NAT service plan. |
| PublicIpAddress e |   |   |   |
| AllocationId | String | eip- 2zeerraiwb7ujdeds* *** | The ID that is allocated. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApAccessEnabl ed | Boolean | true |   |
| IpAddress | String | 116.XX.XX.28 | The IP address. |
| UsingStatus | String | Available | The state of the NAT service plan. |
| RegionId | String | cn-qingdao-env17- d01 | The region ID of the NAT service plan. |
| Status | String | Available | The state of the bandwidth plan. |
| ZoneId | String | cn-qingdao-env17- amtest11001-a | The ID of the zone to which the NAT service plan belongs. |
| TotalCount | Integer | 10 | The number of entries returned. |
| PageNumber | Integer | 10 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF" | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBandwidthPackages &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBandwidthPackagesResponse>
  <TotalCount>10</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF"</RequestId>
  <PageNumber>10</PageNumber>
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
        <CreationTime>2017-06-08T12:20:55</CreationTime>
        <BandwidthPackageId>bwp-xxoo123sfwr****</BandwidthPackageId>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <NatGatewayId> ngw-xxoo123ggtf****</NatGatewayId>
        <PublicIpAddresses>
              <UsingStatus>Available</UsingStatus>
              <ApAccessEnabled>true</ApAccessEnabled>
              <AllocationId>eip-2zeerraiwb7ujdeds****</AllocationId>
              <IpAddress>116.XX.XX.28</IpAddress>
        </PublicIpAddresses>
  </BandwidthPackages>
</DescribeBandwidthPackagesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF\"",
    "PageNumber": 10,
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
        "CreationTime": "2017-06-08T12:20:55",
        "BandwidthPackageId": "bwp-xxoo123sfwr****",
        "RegionId": "cn-qingdao-env17-d01",
        "NatGatewayId": "ngw-xxoo123ggtf****",
        "PublicIpAddresses": {
            "UsingStatus": "Available",
            "ApAccessEnabled": true,
            "AllocationId": "eip-2zeerraiwb7ujdeds****",
            "IpAddress": "116.XX.XX.28"
```

`}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.15.16 ModifyBandwidthPackageAttribute

Modifies the name and description of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidth PackageAttribute | The operation that you want to perform. Valid values: Modif yBandwidt hPackageAt t ribut e . |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions interface to obtain the region ID. |   |   |
| Name | String | No | NATABC | The name of the NAT bandwidth plan. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). But not with http:// or https:// The beginning. |   |   |
| Description | String | No | This is NAT. | The description of the NAT bandwidth plan. The name must be 2 to 256 characters in length. It must start with a letter, but cannot start with http:// or https:// The beginning. |   |   |

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
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |

##### 2.1.15.17 AddBandwidthPackageIps

Adds one or more public IP addresses to a NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBandwidthPa ckageIps | The operation that you want to perform. Valid values: AddBandwidt hPackageIps . |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT bandwidth plan resides. You can call DescribeRegions interface to obtain the region ID. |
| IpCount | String | Yes | 2 | The number of public IP addresses in the NAT bandwidth plan. Valid values: 1 ~ 50 . |
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |

| V | irtual Private Cloud |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e0**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EC0B5C51-7F40- 44D6-A642- 1DE764B547EC | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddBandwidthPackageIps &RegionId=cn-qingdao-env17-d01 &IpCount=2 &BandwidthPackageId=bwp-s6lmotmkk**** &<Public request parameters>
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

| D | eveloper Guid | e·API reference |   | Virtual Private Clou | d |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidIpCount.Value NotSupported | The specified value of IpCount not supported. | The error message returned because the value of the IpCount parameter is invalid. |
| 400 | QuotaExceeded.Ban dwidthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Submit a ticket to increase the quota. |
| 404 | BandwidthPackage.F inancialLocked | The specified BandwidthPackage has been Financail Lock. | The error message returned because the specified NAT service plan is locked due to overdue payments. |

#### 2.1.16 Elastic IP addresses

##### 2.1.16.1 AllocateEipAddress

Applies for an elastic IP address (EIP). After you call this operation, the system randomly allocates an EIP that is in the Available state in the specified region. EIPs support only the ICMP, TCP, and UDP transport layer protocols. The IGMP and SCTP protocols are not supported. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateEipAddre ss | The operation that you want to perform. Set the value to Allocat eEipAddress. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to apply for an EIP. You can call the DescribeRegions operation to query region IDs. |
| Bandwidth | String | No | 1 | The bandwidth limit of the EIP. Valid values: 1 to 200. Unit: Mbit/s. Default value: 1. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Period | Integer | No | 1 | The subscription duration of the EIP. When PricingCycle is set to Mont h, Period can be set from 1 t o 9. When PricingCycle is set to Year, Period can be set from 1 t o 3. This parameter is required when Inst anceChargeT ype is set to PrePaid. When Inst anceChargeT ype is set to Post Paid, ignore this parameter. Not e This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |
| ISP | String | No | BGP | The line type. Default value: BGP. If your account is in the single-path BGP whitelist, you can set the parameter to ChinaT elecom, ChinaUnicom, or ChinaMobile. This parameter is required if your workloads are deployed in the China East 1 Finance region. In this case, set the value to BGP FinanceCloud. _ |
| ActivityId | Long | No | 111111 | The promotion code. You can leave this parameter empty. |
| Netmode | String | No | public | The type of network. Set the value to public (Internet). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: f alse: disables automatic payment. After an order is generated, you must go to the order center to complete the payment. t rue: enables automatic payment. After an order is generated, the system automatically deducts fees from your account balance to pay for the order. This parameter is required when Inst anceChargeT ype is set to PrePaid. When Inst anceChargeT ype is set to Post Paid, this parameter is not required. Not e This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |
| PricingCycle | String | No | Month | The billing cycle of the subscription EIP. Valid values: Mont h: billed on a monthly basis. This is the default value. Year: billed on an annual basis. This parameter is required when Inst anceChargeT ype is set to PrePaid. When Inst anceChargeT ype is set to Post Paid, this parameter is not required. Not e This parameter is unavailable for EIPs that are purchased on the Alibaba Cloud International site. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the EIP. Valid values: PrePaid: subscription. Post Paid: pay-as-you-go. This is the default value. When Inst anceChargeT ype is set to PrePaid, you must set Int ernet ChargeT ype to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, you can set Int ernet ChargeT ype to PayByBandwidt h or PayByT raf f ic. Not e If you want to purchase an EIP from the Alibaba Cloud International site, you must set this parameter to Post Paid (pay-as-you-go). |
| InternetChargeTy pe | String | No | PayByTraffic | The metering method of the EIP. Valid values: PayByBandwidt h: pay-by-bandwidth. This is the default value. PayByT raf f ic: pay-by-data-transfer. When Inst anceChargeT ype is set to PrePaid, Int ernet ChargeT ype must be set to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, Int ernet ChargeT ype can be set to PayByBandwidt h or PayByT raf f ic. |
| ResourceGroupId | String | No | rg- acfmxazffggds** ** | The ID of the enterprise resource group. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipAddress | String | 10.XX.XX.78 | The allocated EIP. |
| AllocationId | String | eip- 25877c70gddh**** | The ID of the EIP. |
| OrderId | Long | 10 | The order number. This parameter is returned only when Inst anceChargeT ype is set to PrePaid. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| ResourceGroupI d | String | rg- acfmxazfdgdg**** | The ID of the enterprise resource group. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AllocateEipAddress &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateEipAddressrResponse>
  <ResourceGroupId>rg-acfmxazfdgdg****</ResourceGroupId>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <AllocationId>eip-25877c70gddh****</AllocationId>
  <EipAddress>10.XX.XX.78</EipAddress>
  <OrderId>10</OrderId>
</AllocateEipAddressrResponse>
```

`JSON` format `{`

```json
    "AllocateEipAddressrResponse": {
        "ResourceGroupId": "rg-acfmxazfdgdg****",
        "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
        "AllocationId": "eip-25877c70gddh****",
        "EipAddress": "10.XX.XX.78",
        "OrderId": 10
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | InvalidParameter | Specified value of "InternetChargeType" is not valid | The error message returned because InternetChargeType is set to an invalid value. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth limit is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the EIP. |
| 400 | InvalidRegion.NotSu pport | The specified region does not support. | The error message returned because the specified region does not support this operation. |

| eveloper Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|
| HttpCode | Error code | Error message | Description |

| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |
|---|---|---|---|
| 409 | OperationConflict | Request was denied due to conflict with a previos request. | The error message returned because a request conflict occurs. Try again later or submit a ticket to report the problem. |

##### 2.1.16.2 AllocateEipAddressPro

Applies for a specified elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to apply for a specified EIP. You can call the DescribeRegions operation to query region IDs. |
| IpAddress | String | No | 12.XX.XX.23 | The IP address of the specified EIP. Specify IpAddress or Inst anceId. If you leave both parameters empty, the system randomly allocates an EIP to your account. |
| InstanceId | String | No | eip- 25877c70gddh*** * | The ID of the specified EIP. Specify IpAddress or Inst anceId. If you leave both parameters empty, the system randomly allocates an EIP to your account. |
| Bandwidth | String | No | 5 | The bandwidth limit of the specified EIP. Unit: Mbit/s. Default value: 1. Unit: Mbit/s. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Period | Integer | No | 1 | The subscription duration of the specified EIP. When PricingCycle is set to Mont h, Period can be set from 1 t o 9. When PricingCycle is set to Year, Period can be set from 1 to 3. When Inst anceChargeT ype is set to PrePaid, this parameter is required. When Inst anceChargeT ype is set to Post Paid, ignore this parameter. |
| ISP | String | No | BGP | The line type. Default value: BGP. If your account is in the single-path BGP whitelist, you can set the parameter to ChinaT elecom, ChinaUnicom, or ChinaMobile. This parameter is required if your workloads are deployed in the China East 1 Finance region. In this case, set the value to BGP FinanceCloud. _ |
| Netmode | String | No | public | The type of network. Set the value to public (Internet). Default value: public (Internet). |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values: f alse: disables automatic payment. After an order is generated, you must go to the order center to complete the payment. t rue: enables automatic payment. After an order is generated, the system automatically deducts fees from your account balance to pay for the order. When Inst anceChargeT ype is set to PrePaid, this parameter is required. When Inst anceChargeT ype is set to Post Paid, ignore this parameter. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceChargeTy pe | String | No | PostPaid | The billing method of the specified EIP. Valid values: PrePaid: subscription. Post Paid: pay-as-you-go. This is the default value. When Inst anceChargeT ype is set to PrePaid, Int ernet ChargeT ype must be set to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, Int ernet ChargeT ype can be set to PayByBandwidt h or PayByT raf f ic. |
| InternetChargeTy pe | String | No | PayByBandwidth | The metering method of the specified EIP. Valid values: PayByBandwidt h (default): pay-by- bandwidth PayByT raf f ic: pay-by-data-transfer. When Inst anceChargeT ype is set to PrePaid, Int ernet ChargeT ype must be set to PayByBandwidt h. When Inst anceChargeT ype is set to Post Paid, Int ernet ChargeT ype can be set to PayByBandwidt h or PayByT raf f ic. |
| ResourceGroupId | String | No | rg- resourcegroup*** * | The ID of the resource group to which the EIP belongs. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. Client T oken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AllocationId | String | eip- 25877c70gddh**** | The ID of the specified EIP. |

| V | irtual Private Clou | d |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| EipAddress | String | 12.XX.XX.23 | The IP address of the specified EIP. |
| OrderId | Long | 20190000 | The ID of the order. |
| RequestId | String | 4EC47282-1B74- 4534-BD0E- 403F3EE64CAF | The ID of the request. |
| ResourceGroupI d | String | rg- resourcegroup**** | The ID of the resource group to which the EIP belongs. |

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
  <EipAddress>12.XX.XX.23</EipAddress>
  <OrderId>20190000</OrderId>
</AllocateEipAddressProResponse>
```

`JSON` format `{`

```json
    "ResourceGroupId": "rg-resourcegroup****",
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "AllocationId": "eip-25877c70gddh****",
    "EipAddress": "12.XX.XX.23",
    "OrderId": 20190000
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | InvalidParameter | Specified value of "InternetChargeType" is not valid | The error message returned because InternetChargeType is set to an invalid value. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not valid. | The error message returned because the specified bandwidth limit is invalid. |
| 400 | InsufficientBalance | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 400 | QuotaExceeded.Eip | Elastic IP address quota exceeded. | The error message returned because the number of EIPs reaches the quota. You can submit a ticket to request a quota increase. We recommend that you use NAT gateways. |
| 400 | ReserveIpFail | Reserve eip failed. | The error message returned because the system failed to reserve the specified EIP. |
| 400 | InvalidRegion.NotSu pport | The specified region does not support. | The error message returned because the specified region does not support this operation. |
| 400 | InvalidResourceGrou pId | The specified ResourceGroupId does not exist. | The error message returned because the specified resource group ID does not exist. |

##### 2.1.16.3 AssociateEipAddress

Associates an elastic IP address (EIP) with an instance in the same region. When you call the operation, take note of the following items: You can associate an EIP with an Elastic Compute Service (ECS) instance, a Server Load Balancer (SLB) instance, a secondary elastic network interface (ENI), or a NAT gateway that is deployed in a virtual private cloud (VPC). The EIP and the instance with which you want to associate the EIP must belong to the same region. To associate an EIP with a NAT gateway, make sure that no NAT service plan that was purchased before November 3, 2017 exists in your account. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateEipAddr ess | The operation that you want to perform. Valid values: Associat eEipAddress . |
| AllocationId | String | Yes | eip- 2zeerraiwb7ujsxd c**** | The ID of the EIP that you want to associate with an instance. |
| InstanceId | String | Yes | i- 2zebb08phyczza we**** | The ID of the instance with which you want to associate the EIP. NAT gateways, SLB instances, ECS instances, secondary ENIs, and high- availability virtual IP addresses (HAVIPs) are supported. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. |
| InstanceType | String | No | EcsInstance | The type of instance with which you want to associate the EIP. Valid values: Nat : NAT Gateway. SlbInst ance : SLB SLB. EcsInst ance : ECS instances. Net workInt erf ace : auxiliary Elastic Network Interface. HaVip : High-availability virtual IP addresses. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| InstanceRegionId | String | No | cn-hangzhou | The ID of the region where the instance to be associated with the EIP is deployed. Not e This parameter is required only when the EIP is associated with a shared- bandwidth Global Accelerator (GA) instance. |   |   |
| PrivateIpAddress | String | No | 192.1.XX.XX | An IP address that belongs to the CIDR block of a vSwitch. If you do not set this parameter, the system allocates a private IP address based on the VPC ID and vSwitch ID. |   |   |
| Mode | String | No | NAT | The binding mode. Valid values: NAT : NAT mode (normal mode). MULT I BINDED : The multi-EIP _ network interface controller visible mode. BINDED : The visible mode of the EIP network interface controller. Only Inst anceT ype Configure as Net workInt erf ace this parameter is required. |   |   |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001sdfg | Guaranteed request idempotence. You can use the client to generate the value, but you must ensure that it is unique among different requests. ClientToken Only ASCII characters are supported and cannot exceed 64 characters in length. |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C0FD0EED-F90D- 4479-803D- DD62335357E5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateEipAddress &AllocationId=eip-2zeerraiwb7ujsxdc**** &InstanceId=i-2zebb08phyczzawe**** &<Public request parameters>
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

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAssociation.D uplicated | Specified instance already is associated. | The error message returned because an EIP or a GA instance is already associated with the specified instance. You must disassociate the EIP or GA instance from the specified instance before you can perform the operation. |
| 400 | OperationDenied | Specified instance is not in VPC. | The error message returned because the specified instance does not exist in the VPC. |
| 400 | InvalidParameter.Mis match | Specified elastic IP address and ECS instance are not in the same region. | The error message returned because the specified EIP and ECS instance do not belong to the same region. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation | The error message returned because the state of the EIP does not support the operation. |
| 404 | InvalidInstanId.NotF ound | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the ID is valid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectInstanceSta tus | Current instance status does not support this operation. | The error message returned because this operation cannot be performed while the instance is in the current state. |
| 400 | InvalidInstanceType. ValueNotSupported | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStatu s | HaVip can be operated by this action only when it's status is Available or InUse. | The error message returned because the state of the HAVIP does not support the operation. You can perform the operation only when the HAVIP is in the Available or InUse state. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the specified value of the parameter is invalid. |
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because the operation is not supported by EIPs in the default VPC. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatus | The eip binding status invalid. | The error message returned because the EIP is in an invalid state. |
| 400 | BIND INSTANCE HAV _ _ E PORTMAP OR BIN _ _ _ D EIP _ | The instance may have portMap or already bind eip. | The error message returned because a port forwarding rule is configured for the ECS instance. Delete the port forwarding rule and try again. |
| 400 | BIND INSTANCE OWE _ _ NER ERROR _ | Cannot operate the eip. | The error message returned because you are unauthorized to manage the specified EIP. |
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParams.NotFo und | instance not found | The error message returned because the specified instance does not exist. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 503 | ServiceUnavailable | The request has failed due to a temporary failure of the server. | The error message returned because the request failed due to a temporary malfunction of the server. |

##### 2.1.16.4 ModifyEipAddressAttribute

Modifies the name, description, and bandwidth limit of a specified elastic IP address (EIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyEipAddress Attribute | The operation that you want to perform. Set the value to Modif yEipAddressAt t ribut e. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0 d**** | The ID of the EIP that you want to modify. |
| Bandwidth | String | No | 100 | The bandwidth limit of the EIP. Valid values: 1 to 200. Unit: Mbit/s. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. |
| Name | String | No | Test123 | The name of the EIP. The name must be 2 to 128 characters in length, and can contain, digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. The name cannot start with http:// or https:// . |
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
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</ModifyEipAddressAttributeResponse>
```

`JSON` format `{`

```json
    "ModifyEipAddressAttributeResponse": {
        "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InsufficientBalance.Ei p | Your account does not have enough balance. | The error message returned because the balance in your account is insufficient. Top up your account and try again. |
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | Specified value of "Bandwidth" is not supported. | The error message returned because the specified bandwidth limit is invalid. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |

| irtual Private | Cloud |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found.. | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | InvalidParameter | The parameter is invalid. | The error message returned because the parameter is set to an invalid value. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |

##### 2.1.16.5 UnassociateEipAddress

Disassociates an elastic IP address (EIP) from an instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateEipAd dress | The operation that you want to perform. Set the value to Unassociat eEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0 d**** | The ID of the EIP that you want to disassociate. |
| InstanceId | String | Yes | i- hp3akk9irtd69jad **** | The ID of the instance from which you want to disassociate the EIP. |
| Force | Boolean | No | false | Specifies whether to disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. Valid values: f alse (default): does not disassociate the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. t rue: disassociates the EIP from a NAT gateway if a DNAT or SNAT entry is added to the NAT gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. |
| InstanceType | String | No | EcsInstance | The type of instance from which you want to disassociate the EIP. Valid values: EcsInst ance (default): an Elastic Compute Service (ECS) instance that is deployed in a virtual private cloud (VPC) SlbInst ance: a Server Load Balancer (SLB) instance that is deployed in a VPC Net workInt erf ace: a secondary elastic network interface (ENI) that is deployed in a VPC Nat : a NAT gateway HaVip a high-availability virtual IP address (HAVIP) |
| PrivateIpAddress | String | No | 192.XX.XX.2 | The private IP address of the ECS instance or the secondary ENI from which you want to disassociate the EIP. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44-001*** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. |

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
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |
| 400 | InvalidInstanceId.Not Found | Specified instance does not exist. | The error message returned because the specified instance does not exist. Check whether the specified instance is valid. |
| 400 | IncorrectInstanceSta tus | The current status of instance does not support this operation. | The error message returned because the state of the instance does not support the operation. |
| 400 | InvalidInstanceType. ValueNotSupported | The specified value of InstanceType is not supported. | The error message returned because InstanceType is set to an invalid value. |
| 400 | IncorrectHaVipStatu s | This operation is denied because satus of the specified HaVip is neither Available nor InUse. | The error message returned because you cannot perform the operation when the specified HAVIP is in the Available or InUse state. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationDenied | Eip of default vpc not allow this operation | The error message returned because EIPs in the default VPC do not support the operation. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | InvalidParameter | The specified parameter is not valid. | The error message returned because the parameter is set to an invalid value. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | InvalidBindingStatus | The eip binding status invalid. | The error message returned because the binding mode of the EIP is invalid. |

##### 2.1.16.6 ReleaseEipAddress

Releases a specified elastic IP address (EIP). Before you release an EIP, make sure that the EIP meets the following requirements: You can release only EIPs that are in the Available state. You can release only EIPs that are billed on a pay-as-you-go basis. You cannot release subscription EIPs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ReleaseEipAddres s | The operation that you want to perform. Set the value to ReleaseEipAddress. |
| AllocationId | String | Yes | eip- 2zeerraiwb7uj6i0 d**** | The ID of the EIP that you want to release. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the EIP belongs. You can call the DescribeRegions operation to query region IDs. |

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
| 404 | InvalidAllocationId.N otFound | Specified allocation ID is not found | The error message returned because the specified EIP does not exist. Check whether the value of the parameter is valid. |
| 400 | IncorrectEipStatus | Current elastic IP status does not support this operation. | The error message returned because the state of the EIP does not support this operation. |

| eveloper Guid | e·API reference |   | Virtual Private Clou |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | Forbidden.RegionNo tFound | Specified region is not found during access authentication. | The error message returned because the specified region does not exist. Check whether the specified region ID is valid. |
| 400 | Forbidden.ChargeTy peIsPrepaid | It's forbidden to release a prepaid EIP | The error message returned because you cannot release subscription EIPs. |
| 400 | Forbbiden | The eip instance owener error | The error message returned because you are unauthorized to perform the operation on the EIP. |
| 400 | TaskConflict.Associa teGlobalAcceleratio nInstance | Operate too frequent. | The error message returned because the number of requests that you send exceeds the upper limit. |

##### 2.1.16.7 DescribeEipGatewayInfo

Queries information about the gateway and subnet mask of an elastic IP address (EIP). You can query only EIPs that are associated with secondary elastic network interfaces (ENIs) in multi-EIP to ENI mode. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEipGatew ayInfo | The operation that you want to perform. Set the value to DescribeEipGat ewayInf o. |
| InstanceId | String | Yes | eni- bp1d66qjxb3qoin 3**** | The ID of the secondary ENI that is associated with the EIP. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region to which the EIP that you want to query belongs. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Code | String | 200 | The status code of the operation. |
| EipInfos | Array of EipInfo |   | Detailed information about the EIP. |
| EipInfo |   |   |   |
| Ip | String | 47.XX.XX.236 | The IP address of the EIP. |
| IpGw | String | 47.XX.XX.1 | The IP address of the gateway that is associated with the EIP. |
| IpMask | String | 255.255.255.0 | The subnet mask of the EIP. |
| Message | String | successful | The result of the operation. |
| RequestId | String | C0FD0EED-F90D- 4479-803D- DD62335357E5 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEipGatewayInfo &InstanceId=eni-bp1d66qjxb3qoin3**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeEipGatewayInfoResponse>
  <Message>successful</Message>
  <RequestId>C0FD0EED-F90D-4479-803D-DD62335357E5    </RequestId>
  <Code>200</Code>
  <EipInfos>
        <IpMask>255.255.255.0</IpMask>
        <IpGw>47.XX.XX.1</IpGw>
        <Ip>47.XX.XX.236</Ip>
  </EipInfos>
</DescribeEipGatewayInfoResponse>
```

`JSON` format `{`

```json
    "Message": "successful",
    "RequestId": "C0FD0EED-F90D-4479-803D-DD62335357E5",
    "Code": 200,
    "EipInfos": {
        "IpMask": "255.255.255.0",
        "IpGw": "47.XX.XX.1",
        "Ip": "47.XX.XX.236"
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 403 | Forbbiden | User not authorized to operate on the specified resource. | The error message returned because you are unauthorized to perform the operation on the specified resource. Apply for permissions and try again. |

#### 2.1.17 HAVIPs

##### 2.1.17.1 CreateHaVip

Creates a high-availability virtual IP address (HAVIP). Descriptions When you call this operation, take note of the following rules: You can create a maximum of five HAVIPs for a virtual private cloud (VPC). Before you delete a VPC, you must delete the HAVIPs that you have created for it. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateHaVip | The operation that you want to perform. Set the value to Creat eHaVip. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to create an HAVIP. You can call the DescribeRegions operation to the most recent region list. |
| VSwitchId | String | Yes | vsw-asdfjlnau**** | The ID of the vSwitch to which the HAVIP belongs. |
| Name | String | No | test | The name of the HAVIP. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001s**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| IpAddress | String | No | 192.XX.XX.10 | The IP address of the HAVIP. If this parameter is not set, an idle IP address of the specified vSwitch is randomly allocated to the HAVIP. |
| Description | String | No | This is my HaVip. | The description of the HAVIP. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HaVipId | String | havip- 2zeo05qre24nhrqp* *** | The ID of the HAVIP. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IpAddress | String | 192.XX.XX.10 | The IP address of the HAVIP. |
| RequestId | String | C44F62BE-9CE7- 4277-B117- 69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateHaVip &RegionId=cn-qingdao-env17-d01 &VSwitchId=vsw-asdfjlnau**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
  <IpAddress>192.XX.XX.10</IpAddress>
  <HaVipId>havip-2zeo05qre24nhrqp****</HaVipId>
</CreateHaVipResponse>
```

`JSON` format `{`

```json
    "RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF",
    "IpAddress": "192.XX.XX.10",
    "HaVipId": "havip-2zeo05qre24nhrqp****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | Specified value of "regionId" is not supported. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 404 | InvalidVSwitchId.Not Found | The specified VSwitch does not exist in the specified region. | The error message returned because the specified vSwitch does not exist in the specified region. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidDescription.M alformed | The specified Description is wrongly formed. | The error message returned because the format of the specified description is invalid. The description must be 2 to 256 characters in length. It cannot start with http:// or https://. |
| 403 | CountLimitExceed.Ha VipInVpc | Specified Vpc exceeds the quota of max number of ha-vip count. | The error message returned because the number of HAVIPs in the VPC has reached the upper limit. |
| 403 | QuotaExceeded.HaVi p | Living HaVip quota exceeded. | The error message returned because the number of active HAVIPs has reached the upper limit. |
| 400 | InvalidIPAddress.Out OfRange | The specified IPAddress is out of VSwitch CIDR. | The error message returned because the specified IP address does not fall within the CIDR block of the vSwitch. |
| 400 | InvalidIPAddress.Not Available | The specified IPAddress is not available because it is a system reserved IPAddress. | The error message returned because the specified IP address is reserved by the system and cannot be used. |
| 400 | InvalidIPAddress.Alre adyUsed | The specified IPAddress is already used by other resource. | The error message returned because the specified IP address is already used by another resource. |

##### 2.1.17.2 DescribeHaVips

Queries high-availability virtual IP addresses (HAVIPs) in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHaVips | The operation that you want to perform. Set the value to DescribeHaVips. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to create an HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| Filter.N.Key | String | No | HaVipId.havip- bp149uyvut73dpl du**** | Specifies filter conditions. You can specify at most five filter conditions. Valid values of n: 1 t o 5. You can specify multiple values for each filter condition. The logical operator among multiple values is OR. If one value is matched, the filter condition is met. The logical operator among multiple filter conditions is AND, in which case all the filter conditions must be met for an HAVIP to be included in the result. The following filter conditions are available: VpcId: the ID of the virtual private cloud (VPC). VSwit chId: the ID of the vSwitch. St at us: the status of the HAVIP. HaVipId: the ID of the HAVIP. HaVipAddress: the IP address of the HAVIP. |
| Filter.N.Value.N | RepeatLi st | No | 1 | Specifies the value of the filter condition. Valid values of N: 1 t o 5. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| HaVips | Array of HaVip |   | The details about the HAVIP. |
| HaVip |   |   |   |
| AssociatedEipA ddresses | List | 121.XX.XX.1 | The list of elastic IP addresses (EIPs) that are associated with the HAVIP. |
| AssociatedInsta nceType | String | EcsInstance | The type of the instance that is associated with the HAVIP. |
| AssociatedInsta nces | List | i- bp145q7glnuzdvzu2 1**** | The Elastic Compute Service (ECS) instances that are associated with the HAVIP. |
| ChargeType | String | none | The parameter is invalid. No value is returned. |
| CreateTime | String | 2018-07- 03T14:25:26Z | The time when the HAVIP was created. |
| Description | String | My HaVip | The description of the HAVIP. |
| HaVipId | String | havip- bp149uyvut73dpld** ** | The ID of the HAVIP. |
| IpAddress | String | 192.XX.XX.27 | The private IP address of the HAVIP. |
| MasterInstanceI d | String | i- bp145q7glnuzdvz** ** | The ID of the instance that has obtained the private IP address of the HAVIP. |
| Name | String | test | The name of the HAVIP. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the HAVIP is deployed. |
| Status | String | Available | The status of the HAVIP. |
| VSwitchId | String | vsw- bp1pkt1fba8e824ez **** | The ID of the vSwitch to which the HAVIP belongs. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| VpcId | String | vpc- bp1kcm36tevkpms9 **** | The ID of the VPC to which the HAVIP belongs. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 33E480C5-B46F- 4CA5-B6FD- D77C746E86AB | The ID of the request. |
| TotalCount | Integer | 1 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHaVips &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHaVipsResponse>
  <TotalCount>1</TotalCount>
  <HaVips>
        <Status>Available</Status>
        <Description>My HaVip</Description>
        <VpcId>vpc-bp1kcm36tevkpms9****</VpcId>
        <MasterInstanceId>i-bp145q7glnuzdvz****</MasterInstanceId>
        <ChargeType>none</ChargeType>
        <CreateTime>2018-07-03T14:25:26Z</CreateTime>
        <VSwitchId>vsw-bp1pkt1fba8e824ez****</VSwitchId>
        <IpAddress>192.XX.XX.27</IpAddress>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <HaVipId>havip-bp149uyvut73dpld****</HaVipId>
        <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
        <Name>test</Name>
        <AssociatedInstances>i-bp145q7glnuzdvzu21****</AssociatedInstances>
        <AssociatedEipAddresses>121.XX.XX.1</AssociatedEipAddresses>
  </HaVips>
  <PageSize>10</PageSize>
  <RequestId>33E480C5-B46F-4CA5-B6FD-D77C746E86AB</RequestId>
  <PageNumber>1</PageNumber>
</DescribeHaVipsResponse>
```

`JSON` format `{`

```json
    "DescribeHaVipsResponse": {
        "TotalCount": 1,
        "HaVips": {
            "Status": "Available",
            "Description": "My HaVip",
            "VpcId": "vpc-bp1kcm36tevkpms9****",
            "MasterInstanceId": "i-bp145q7glnuzdvz****",
            "ChargeType": "none",
            "CreateTime": "2018-07-03T14:25:26Z",
            "VSwitchId": "vsw-bp1pkt1fba8e824ez****",
            "IpAddress": "192.XX.XX.27",
            "RegionId": "cn-qingdao-env17-d01",
            "HaVipId": "havip-bp149uyvut73dpld****",
            "AssociatedInstanceType": "EcsInstance",
            "Name": "test",
            "AssociatedInstances": "i-bp145q7glnuzdvzu21****",
            "AssociatedEipAddresses": "121.XX.XX.1"
```

`},`

```json
        "PageSize": 10,
        "RequestId": "33E480C5-B46F-4CA5-B6FD-D77C746E86AB",
        "PageNumber": 1
```

`}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.Valu eNotSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

##### 2.1.17.3 ModifyHaVipAttribute

Modifies the description of a high-availability virtual IP address (HAVIP). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyHaVipAttri bute | The operation that you want to perform. Set the value to: Modif yHaVipAt t ribut e. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrq p**** | The ID of the HAVIP that you want to modify. |

| Developer Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the HAVIP belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e0**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| Description | String | No | This is my HaVip. | The description of the HAVIP. |
| Name | String | No | test | The name of the HAVIP. The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7- 4277-B117- 69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyHaVipAttribute &HaVipId=havip-2zeo05qre24nhrqp**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyHaVipAttributeResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</ModifyHaVipAttributeResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFo und | The specified HaVip does not exist in the specified region. | The error message returned because the HAVIP does not exist in the specified region. Specify another region ID and try again. |
| 400 | IncorrectStatus | HaVip can be deleted only when it's status is Available or InUse. | The error message returned because the HAVIP is unavailable and failed to be deleted. |
| 400 | InvalidDescription.M alformed | The specified Description is wrongly formed. | The error message returned because the format of the specified description is invalid. The description must be 2 to 256 characters in length. It cannot start with http:// or https://. |

##### 2.1.17.4 AssociateHaVip

Associates a high-availability virtual IP address (HAVIP) with an Elastic Compute Service (ECS) instance. Descriptions When you call this operation, take note of the following limits: The HAVIP takes effect immediately after it is associated with an ECS instance in a VPC. You do not need to restart the ECS instance. However, you must associate the HAVIP with the elastic network interface (ENI) of the ECS instance. The HAVIP and ECS instance must belong to the same vSwitch. You can associate an HAVIP with at most two ECS instances. The ECS instance must be in the Running or Stopped state. The HAVIP must be in the Available or InUse state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateHaVip | The operation that you want to perform. Set the value to Associat eHaVip. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrq pyf*** | The ID of the HAVIP. |
| InstanceId | String | Yes | i- faf344422ffsfa** ** | The ID of the ECS instance that you want to associate. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the HAVIP belongs. You can call the DescribeRegions to query the most recent region list. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| InstanceType | String | No | ecs.g6.large | The instance type. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7- 4277-B117- 69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateHaVip &HaVipId=havip-2zeo05qre24nhrqpyf*** &InstanceId=i-faf344422ffsfa**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</AssociateHaVipResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFo und | The specified HaVip does not exist in the specified region. | The error message returned because the specified HAVIP does not exist in the specified region. Check the region. |
| 404 | InvalidInstanceId.Not Found | The specified Instance does not exist in the specified region. | The error message returned because the instance does not exist in the specified region. |
| 400 | IncorrectHaVipStatu s | HaVip can be operated by this action only when it's status is Available or InUse. | The error message returned because this operation can be performed only when the HAVIP is in the Available or InUse state. |
| 400 | CountLimitExceed.Ha VipOnInstance | The amount of HaVip associated with the specified Instance reach its limits. | The error message returned because the number of HAVIPs has reached the upper limit. |
| 400 | CountLimitExceeded. HaVipOnECSInstance | The amount of Instance associated with the specified HaVip reach its limits. | The error message returned because the number of HAVIPs has reached the upper limit. |
| 400 | InvalidNetworkInterf aceId.NotFound | The network interface is not found. | The error message returned because the specified ENI does not exist. |

##### 2.1.17.5 UnassociateHaVip

Disassociates a high-availability virtual IP address (HAVIP) from an Elastic Compute Service (ECS) instance in a virtual private cloud (VPC). Descriptions When you call this operation, take note of the following limits: The ECS instance must be in the Running or Stopped state. The HAVIP must be in the Available or InUse state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateHaVip | The operation that you want to perform. Set the value to Unassociat eHaVip. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrq pyf**** | The ID of the HAVIP. |
| InstanceId | String | Yes | i- faf344422ffsfa** ** | The ID of the ECS instance that you want to disassociate. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |
| InstanceType | String | No | ecs.g5.large | The type of the ECS instance. |
| Force | String | No | True | Specifies whether to forcibly disassociate the HAVIP from the ECS instance. Valid values: T rue and False (default). Not e If you set this parameter to False, you cannot disassociate the HAVIP from a primary ECS instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7- 4277-B117- 69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateHaVip &HaVipId=havip-2zeo05qre24nhrqpyf**** &InstanceId=i-faf344422ffsfa**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociateHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</UnassociateHaVipResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFo und | The specified HaVip does not exist in the specified region. | The error message returned because the specified HAVIP does not exist in the specified region. Check whether the region is correct. |
| 404 | InvalidInstanceId.Not Found | The specified Instance does not exist in the specified region. | The error message returned because the instance does not exist in the specified region. |
| 400 | IncorrectHaVipStatu s | HaVip can be operated by this action only when it's status is InUse. | The error message returned because the operation can be performed only when the HAVIP is in the InUse state. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectInstanceSta tus | ECS instance can be operated by this action only when it's status is Running or Stopped. | The error message returned because the operation can be performed only when the ECS instance is in the Running or Stopped state. |
| 400 | ResourceNotAssocia ted | The HaVip and ECS instance are not associated. | The error message returned because the HAVIP is not associated with the ECS instance. |
| 400 | Forbidden.Unassocia teMaster | Unassociating a master instance is not allowed unless the parameter Force is True. | The error message returned because the Force parameter is set to False. |
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 400 | InvalidNetworkInterf aceId.NotFound | The network interface is not found. | The error message returned because the specified elastic network interface (ENI) does not exist. |

##### 2.1.17.6 DeleteHaVip

Deletes a high-availability virtual IP address (HAVIP). When you call this operation, take note of the following rules: You can delete only HAVIPs that are in the Available state. Make sure that no routes are destined for the HAVIP that you want to delete. Make sure that no elastic IP addresses (EIPs) are associated with the HAVIP that you want to delete. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteHaVip | The operation that you want to perform. Set the value to Delet eHaVip. |
| HaVipId | String | Yes | havip- 2zeo05qre24nhrq pyf**** | The ID of the HAVIP that you want to delete. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where you want to create an HAVIP. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | C44F62BE-9CE7- 4277-B117- 69243F3988BF | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteHaVip &HaVipId=havip-2zeo05qre24nhrqpyf**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteHaVipResponse>
  <RequestId>C44F62BE-9CE7-4277-B117-69243F3988BF</RequestId>
</DeleteHaVipResponse>
```

`JSON` format `{`

```json
"RequestId": "C44F62BE-9CE7-4277-B117-69243F3988BF"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidHaVipId.NotFo und | The specified HaVip does not exist in the specified region. | The error message returned because the specified HAVIP does not exist in the specified region. Check the region. |
| 400 | IncorrectStatus | HaVip can be deleted only when it is status is Available. | The error message returned because the HAVIP cannot be deleted. The error message returned because the HAVIP is not in the Available state. |
| 400 | DependencyViolatio n.HaVipReferedByRo uteEntry | HaVip cannot be deleted when it is refered by a route table entry as next hop. | The error message returned because the HAVIP functions as the next hop of a route entry and cannot be deleted. You must delete the route entry before you can delete the HAVIP. |
| 400 | DependencyViolatio n.HaVipAssociatedW ithEIP | HaVip cannot be deleted when it is associated with EIP. | The error message returned because the HAVIP is associated with an elastic IP address (EIP) and cannot be deleted. |

#### 2.1.18 ACLs

##### 2.1.18.1 CreateNetworkAcl

Creates a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNetworkAc l | The operation that you want to perform. Set the value to Creat eNet workAcl. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to the most recent region list. |
| VpcId | String | Yes | vpc- dsfd34356vdf**** | The ID of the virtual private cloud (VPC) to which you want to apply the network ACL. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NetworkAclName | String | No | acl-1 | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter and cannot start with http:// or https:// . |
| Description | String | No | This is my NetworkAcl. | The description of the network ACL. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

|   | http:// |
|---|---|
| https:// |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclAttr ibute | Struct |   | The attributes of the network ACL. |
| CreationTime | String | 2019-04-25 11:33:27 | The time when the network ACL was created. |
| Description | String | This is my NetworkAcl. | The description of the network ACL. |
| EgressAclEntrie s | Array of EgressAclEntry |   | The outbound rules. |
| EgressAclEntry |   |   |   |
| Description | String | This is EgressAclEntries. | The description of the outbound rule. |
| DestinationCidrI p | String | 10.0.0.0/24 | The destination CIDR block. |

| eveloper Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|
| Parameter | Type | Example | Description |

| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule. syst em: a system rule. |
|---|---|---|---|
| NetworkAclEntr yId | String | nae- a2d447uw4tillxsdc** ** | The ID of the outbound rule. |
| NetworkAclEntr yName | String | acl-2 | The name of the outbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The destination ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp gre t cp udp all: all protocols supported |
| IngressAclEntrie s | Array of IngressAclEntry |   | The inbound rules. |
| IngressAclEntry |   |   |   |
| Description | String | This is IngressAclEntries. | The description of the inbound rule. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule. syst em: a system rule. |
| NetworkAclEntr yId | String | nae- a2dk86arlydmexscd **** | The ID of the inbound rule. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclEntr yName | String | acl-3 | The name of the inbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The source ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp gre t cp udp all: all protocols supported |
| SourceCidrIp | String | 10.0.0.0/24 | The source CIDR block. |
| NetworkAclId | String | nacl- a2do9e413e0spdefr **** | The description of the network ACL. |
| NetworkAclNa me | String | acl-1 | The name of the network ACL. |
| RegionId | String | cn-qingdao-env17- d01 | The region where the network ACL is deployed. |
| Resources | Array of Resource |   | The resources that are associated with the network ACL. |
| Resource |   |   |   |
| ResourceId | String | vsw- bp1de348lntdwgthy **** | The ID of the associated resource. |
| ResourceType | String | VSwitch | The type of the associated resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | BINDED | The state of the associated resource. Valid values: BINDED: The resource is associated with the network ACL. BINDING: The resource is being associated with the network ACL. UNBINDING: The resource is disassociated from the network ACL. |
| Status | String | Modifying | The state of the network ACL. Valid values: Available: The network ACL is available for use. Modif ying: The network ACL is being configured. |
| VpcId | String | vpc- a2d33rfpl72k5xsscd **** | The ID of the VPC to which the network ACL applies. |
| NetworkAclId | String | nacl- a2do9e413e0spzasx **** | The description of the network ACL. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateNetworkAcl &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-dsfd34356vdf**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateNetworkAclResponse>
  <NetworkAclId>nacl-a2do9e413e0spzasx****</NetworkAclId>
  <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
  <NetworkAclAttribute>
        <Status>Modifying</Status>
        <Description>This is my NetworkAcl.</Description>
        <VpcId>vpc-a2d33rfpl72k5xsscd****</VpcId>
        <NetworkAclId>nacl-a2do9e413e0spdefr****</NetworkAclId>
        <CreationTime>2019-04-25 11:33:27</CreationTime>
        <NetworkAclName>acl-1 </NetworkAclName>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <IngressAclEntries>
              <Policy>accept</Policy>
              <Description>This is IngressAclEntries. </Description>
              <EntryType>custom</EntryType>
              <Port>-1/-1 </Port>
              <SourceCidrIp>10.0.0.0/24 </SourceCidrIp>
              <NetworkAclEntryName>acl-3 </NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2dk86arlydmexscd****</NetworkAclEntryId>
        </IngressAclEntries>
        <EgressAclEntries>
              <Policy>accept</Policy>
              <Description>This is EgressAclEntries.</Description>
              <EntryType>custom</EntryType>
              <DestinationCidrIp>10.0.0.0/24</DestinationCidrIp>
              <Port>-1/-1 </Port>
              <NetworkAclEntryName>acl-2</NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2d447uw4tillxsdc****</NetworkAclEntryId>
        </EgressAclEntries>
        <Resources>
              <Status>BINDED</Status>
              <ResourceId>vsw-bp1de348lntdwgthy****</ResourceId>
              <ResourceType>VSwitch</ResourceType>
        </Resources>
  </NetworkAclAttribute>
</CreateNetworkAclResponse>
```

`JSON` format `{`

```json
    "NetworkAclId": "nacl-a2do9e413e0spzasx****",
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
    "NetworkAclAttribute": {
        "Status": "Modifying",
        "Description": "This is my NetworkAcl.",
        "VpcId": "vpc-a2d33rfpl72k5xsscd****",
        "NetworkAclId": "nacl-a2do9e413e0spdefr****",
        "CreationTime": "2019-04-25 11:33:27",
        "NetworkAclName": "acl-1",
        "RegionId": "cn-qingdao-env17-d01",
        "IngressAclEntries": {
            "Policy": "accept",
            "Description": "This is IngressAclEntries.",
            "EntryType": "custom",
            "Port": "-1/-1",
            "SourceCidrIp": "10.0.0.0/24",
            "NetworkAclEntryName": "acl-3",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2dk86arlydmexscd****"
```

`},`

```json
        "EgressAclEntries": {
            "Policy": "accept",
            "Description": "This is EgressAclEntries.",
            "EntryType": "custom",
            "DestinationCidrIp": "10.0.0.0/24",
            "Port": "-1/-1",
            "NetworkAclEntryName": "acl-2",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2d447uw4tillxsdc****"
```

`},`

```json
        "Resources": {
            "Status": "BINDED",
            "ResourceId": "vsw-bp1de348lntdwgthy****",
            "ResourceType": "VSwitch"
```

`}` `}` `}`

##### 2.1.18.2 AssociateNetworkAcl

Associates a network access control list (ACL) with a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociateNetwor kAcl | The operation that you want to perform. Set the value to Associat eNet workAcl. |

| V | irtual Private Cloud |   |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| NetworkAclId | String | Yes | nacl- a2do9e413e0spx scd**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| Resource.N.Resou rceType | String | No | VSwitch | The type of the resource with which you want to associate the network ACL. Set the value to VSwit ch. |
| Resource.N.Resou rceId | String | No | vsw- bp1de348lntdwb gnh**** | The ID of the resource with which you want to associate the network ACL. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4CF20CC7-D1FC- 425B-A15B- DF7C8E2131A7 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AssociateNetworkAcl &NetworkAclId=nacl-a2do9e413e0spxscd**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociateNetworkAclResponse>
     <RequestId>4CF20CC7-D1FC-425B-A15B-DF7C8E2131A7</RequestId>
</AssociateNetworkAclResponse>
```

`JSON` format `{`

```json
    "RequestId":"4CF20CC7-D1FC-425B-A15B-DF7C8E2131A7"
```

`}`

##### 2.1.18.3 ModifyNetworkAclAttributes

Modifies the attributes of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNetworkAc lAttributes | The operation that you want to perform. Set the value to Modif yNet workAclAt t ribut es. |
| NetworkAclId | String | Yes | acl- bp1lhl0taik**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region where to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| NetworkAclName | String | No | acl-1 | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter and cannot start with http:// or https:// . |
| Description | String | No | This is my NetworkAcl. | The description of the network ACL. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |

|   | http:// |
|---|---|
| https:// |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It must be 1 to 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8F76C3E4-B39F- 465D-B8B3- 50BAF03CA833 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyNetworkAclAttributes &NetworkAclId=acl-bp1lhl0taik**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success response `XML` format

```xml
<ModifyNetworkAclAttributesResponse>
     <RequestId>8F76C3E4-B39F-465D-B8B3-50BAF03CA833</RequestId>
</ModifyNetworkAclAttributesResponse>
```

`JSON` format `{`

```json
    "RequestId": "8F76C3E4-B39F-465D-B8B3-50BAF03CA833"
```

`}`

##### 2.1.18.4 UpdateNetworkAclEntries

Updates the rules of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UpdateNetworkA clEntries | The operation that you want to perform. Set the value to Updat eNet workAclEnt ries. |
| NetworkAclId | String | Yes | nacl- bp1lhl0taikrzxsc* *** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| IngressAclEntries. N.NetworkAclEntr yName | String | No | acl-3 | The name of the inbound rule. |
| IngressAclEntries. N.NetworkAclEntr yId | String | No | nae- 2zepn32de59j8m 4**** | The ID of the inbound rule. |
| IngressAclEntries. N.Policy | String | No | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| IngressAclEntries. N.Protocol | String | No | all | The transport layer protocols. Valid values: icmp: Internet Control Message Protocol (ICMP) gre: Generic Routing Encapsulation (GRE) t cp: TCP udp: UDP all: All protocols are supported. |
| IngressAclEntries. N.SourceCidrIp | String | No | 10.0.0.0/24 | The source CIDR block. |
| IngressAclEntries. N.Port | String | No | -1/-1 | The source ports. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| IngressAclEntries. N.EntryType | String | No | custom | The type of the rule. Valid values: cust om (default): a custom rule. syst em: a system rule. |
| IngressAclEntries. N.Description | String | No | This is IngressAclEntries. | The description of the inbound rule. |
| EgressAclEntries. N.NetworkAclEntr yName | String | No | acl-2 | The name of the outbound rule. |
| EgressAclEntries. N.NetworkAclEntr yId | String | No | nae- 2zecs97e0brcge4 6**** | The ID of the outbound rule. |
| EgressAclEntries. N.Policy | String | No | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| EgressAclEntries. N.Protocol | String | No | all | The transport layer protocols. Valid values: icmp: ICMP gre: GRE t cp: TCP udp: UDP all: All protocols are supported. |
| EgressAclEntries. N.DestinationCidrI p | String | No | 10.0.0.0/24 | The destination CIDR block. |
| EgressAclEntries. N.Port | String | No | -1/-1 | The destination ports. |
| EgressAclEntries. N.EntryType | String | No | custom | The type of the rule. Valid values: cust om (default): a custom rule syst em: a system rule |
| EgressAclEntries. N.Description | String | No | This is EgressAclEntries. | The description of the outbound rule. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UpdateIngressAcl Entries | Boolean | No | false | Specifies whether to update the inbound rule. Valid rules: t rue: updates the inbound rule. f alse (default): does not update the inbound rule. |
| UpdateEgressAclE ntries | Boolean | No | false | Specifies whether to update the outbound rule. Valid rules: t rue: updates the outbound rule. f alse (default): does not update the outbound rule. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe637760 | The client token that is used to guarantee the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1170A5A0-E760- 4331-9133- A7D38D973215 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UpdateNetworkAclEntries &NetworkAclId=nacl-bp1lhl0taikrzxsc**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UpdateNetworkAclEntriesResponse>
     <RequestId>1170A5A0-E760-4331-9133-A7D38D973215</RequestId>
</UpdateNetworkAclEntriesResponse>
```

`JSON` format `{`

```json
    "RequestId": "1170A5A0-E760-4331-9133-A7D38D973215"
```

`}`

##### 2.1.18.5 UnassociateNetworkAcl

Disassociates a network access control list (ACL) from a vSwitch. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociateNetw orkAcl | The operation that you want to perform. Set the value to Unassociat eNet workAcl. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0sp** ** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the network ACL is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Resource.N.Resou rceType | String | No | VSwitch | The type of the resource associated with the network ACL. |
| Resource.N.Resou rceId | String | No | vsw- bp1de348lntdw** ** | The ID of the associated resource. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AD024BAA-2D91- 48FD-810B- 8FB7489B6EE6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UnassociateNetworkAcl &NetworkAclId=nacl-a2do9e413e0sp**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success response `XML` format

```xml
<UnassociateNetworkAclResponse>
     <RequestId>AD024BAA-2D91-48FD-810B-8FB7489B6EE6</RequestId>
</UnassociateNetworkAclResponse>
```

`JSON` format `{`

```json
    "RequestId": "AD024BAA-2D91-48FD-810B-8FB7489B6EE6"
```

`}`

##### 2.1.18.6 CopyNetworkAclEntries

Copies rules of a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CopyNetworkAclE ntries | The operation that you want to perform. Set the value to CopyNet workAclEnt ries. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0sp** ** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| SourceNetworkAc lId | String | Yes | nacl- ghuo9ehg3e0sp* *** | The ID of the network ACL whose rules you want to copy. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6608E72F-F276- 440F-ABEF- 419971CEC4D1 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CopyNetworkAclEntries &NetworkAclId=nacl-a2do9e413e0sp**** &RegionId=cn-qingdao-env17-d01 &SourceNetworkAclId=nacl-ghuo9ehg3e0sp**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CopyNetworkAclEntriesResponse>
     <RequestId>6608E72F-F276-440F-ABEF-419971CEC4D1</RequestId>
</CopyNetworkAclEntriesResponse>
```

`JSON` format `{`

```json
    "RequestId": "6608E72F-F276-440F-ABEF-419971CEC4D1"
```

`}`

##### 2.1.18.7 DeleteNetworkAcl

Deletes a network access control list (ACL). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNetworkAc l | The operation that you want to perform. Set the value to Delet eNet workAcl. |
| NetworkAclId | String | Yes | nacl- bp1q8bgx4xnkm* *** | The ID of the network ACL. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 34F1206D-04B0- 4A05-9D8A- 80521E288BD1 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNetworkAcl &NetworkAclId=nacl-bp1q8bgx4xnkm**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteNetworkAclResponse>
     <RequestId>34F1206D-04B0-4A05-9D8A-80521E288BD1</RequestId>
</DeleteNetworkAclResponse>
```

`JSON` format `{`

```json
    "RequestId": "34F1206D-04B0-4A05-9D8A-80521E288BD1"
```

`}`

##### 2.1.18.8 DescribeNetworkAcls

Queries network ACLs. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNetwork Acls | The operation that you want to perform. Set the value to DescribeNet workAcls. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region where the network ACL is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| NetworkAclId | String | No | nacl- bp1lhl0taikrbgnh **** | The description of the network ACL. |
| NetworkAclName | String | No | acl-1 | The name of the network ACL. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). _ The name must start with a letter and cannot start with http:// or https:// . |
| VpcId | String | No | vpc-1234**** | The ID of the VPC to which the network ACL applies. |
| ResourceType | String | No | VSwitch | The type of the associated instance. Set the value to VSwit ch. This parameter is valid only when ResourceType and ResourceId are both set. |
| ResourceId | String | No | vsw- bp1de348lntdwn hbg**** | The ID of the associated instance. This parameter is valid only when ResourceType and ResourceId are both set. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe63**** | The token used to ensure idempotence. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAcls | Array of NetworkAcl |   | The details about the network ACL. |
| NetworkAcl |   |   |   |
| CreationTime | String | 2019-04-25 11:44:17 | The time when the network ACL was created. |
| Description | String | This is my NetworkAcl. | The description of the network ACL. |
| EgressAclEntrie s | Array of EgressAclEntry |   | The outbound rules. |
| EgressAclEntry |   |   |   |
| Description | String | This is EgressAclEntries. | The description of the outbound rule. |
| DestinationCidrI p | String | 10.0.0.0/24 | The destination CIDR block. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclEntr yId | String | nae- a2d447uw4tillfvgb** ** | The ID of the outbound rule. |
| NetworkAclEntr yName | String | acl-2 | The name of the outbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The destination ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp: Internet Control Message Protocol (ICMP) gre: Generic Routing Encapsulation (GRE) t cp: TCP udp: UDP all: All protocols are supported. |
| IngressAclEntrie s | Array of IngressAclEntry |   | Information about inbound rules. |
| IngressAclEntry |   |   |   |
| Description | String | This is IngressAclEntries. | The description of the inbound rule. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |
| NetworkAclEntr yId | String | nae- a2dk86arlydmezasw **** | The ID of the inbound rule. |
| NetworkAclEntr yName | String | acl-3 | The name of the inbound rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The source ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp: ICMP gre: GRE t cp: TCP udp: UDP all: All protocols are supported. |
| SourceCidrIp | String | 10.0.0.0/24 | The source CIDR block. |
| NetworkAclId | String | nacl- a2do9e413e0spxscd **** | The ID of the network ACL. |
| NetworkAclNa me | String | acl-8 | The name of the network ACL. |
| OwnerId | Long | 12345678 | The ID of the Apsara Stack tenant account to which the network ACL belongs. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region to which the network ACL belongs. |
| Resources | Array of Resource |   | The resources that are associated with the network ACL. |
| Resource |   |   |   |
| ResourceId | String | vsw- bp1de348lntdwcdf* *** | The ID of the resource with which you want to associate the network ACL. |
| ResourceType | String | VSwitch | The type of the associated resource. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | BINDED | The status of the associated resource. Valid values: BINDED: The resource is associated with the network ACL. BINDING: The resource is being associated with the network ACL. UNBINDING: The resource is disassociated from the network ACL. |
| Status | String | Available | The status of the network ACL. Valid values: Available: The network ACL is available for use. Modif ying: The network ACL is being configured. |
| VpcId | String | vpc- a2d33rfpl72k5defr** ** | The ID of the associated VPC. |
| PageNumber | String | 1 | The page number of the returned page. |
| PageSize | String | 10 | The number of entries on the current page. |
| RequestId | String | F7DDDC17-FA06- 4AC2-8F35- 59D2470FCFC1 | The ID of the request. |
| TotalCount | String | 2 | The total number of entries returned. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNetworkAcls &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeNetworkAclsResponse>
  <TotalCount>2</TotalCount>
  <NetworkAcls>
        <Status>Available</Status>
        <Description>This is my NetworkAcl.</Description>
        <OwnerId>12345678</OwnerId>
        <VpcId>vpc-a2d33rfpl72k5defr****</VpcId>
        <NetworkAclId>nacl-a2do9e413e0spxscd****</NetworkAclId>
        <CreationTime>2019-04-25 11:44:17</CreationTime>
        <NetworkAclName>acl-8</NetworkAclName>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <IngressAclEntries>
              <Policy>accept</Policy>
              <Description>This is IngressAclEntries. </Description>
              <EntryType>custom</EntryType>
              <Port>-1/-1 </Port>
              <SourceCidrIp>10.0.0.0/24 </SourceCidrIp>
              <NetworkAclEntryName>acl-3 </NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2dk86arlydmezasw****</NetworkAclEntryId>
        </IngressAclEntries>
        <EgressAclEntries>
              <Policy>accept</Policy>
              <Description>This is EgressAclEntries. </Description>
              <EntryType>custom</EntryType>
              <DestinationCidrIp>10.0.0.0/24 </DestinationCidrIp>
              <Port>-1/-1 </Port>
              <NetworkAclEntryName>acl-2 </NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2d447uw4tillfvgb****</NetworkAclEntryId>
        </EgressAclEntries>
        <Resources>
              <Status>BINDED</Status>
              <ResourceId>vsw-bp1de348lntdwcdf****</ResourceId>
              <ResourceType>VSwitch</ResourceType>
        </Resources>
  </NetworkAcls>
  <PageSize>10</PageSize>
  <RequestId>F7DDDC17-FA06-4AC2-8F35-59D2470FCFC1</RequestId>
  <PageNumber>1</PageNumber>
</DescribeNetworkAclsResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "NetworkAcls": {
        "Status": "Available",
        "Description": "This is my NetworkAcl.",
        "OwnerId": 12345678,
        "VpcId": "vpc-a2d33rfpl72k5defr****",
        "NetworkAclId": "nacl-a2do9e413e0spxscd****",
        "CreationTime": "2019-04-25 11:44:17",
        "NetworkAclName": "acl-8",
        "RegionId": "cn-qingdao-env17-d01",
        "IngressAclEntries": {
            "Policy": "accept",
            "Description": "This is IngressAclEntries.",
            "EntryType": "custom",
            "Port": "-1/-1",
            "SourceCidrIp": "10.0.0.0/24",
            "NetworkAclEntryName": "acl-3",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2dk86arlydmezasw****"
```

`},`

```json
        "EgressAclEntries": {
            "Policy": "accept",
            "Description": "This is EgressAclEntries.",
            "EntryType": "custom",
            "DestinationCidrIp": "10.0.0.0/24",
            "Port": "-1/-1",
            "NetworkAclEntryName": "acl-2",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2d447uw4tillfvgb****"
```

`},`

```json
        "Resources": {
            "Status": "BINDED",
            "ResourceId": "vsw-bp1de348lntdwcdf****",
            "ResourceType": "VSwitch"
```

`}` `},`

```json
    "PageSize": 10,
    "RequestId": "F7DDDC17-FA06-4AC2-8F35-59D2470FCFC1",
    "PageNumber": 1
```

`}`

##### 2.1.18.9 DescribeNetworkAclAttributes

Queries details about a network ACL. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNetwork AclAttributes | The operation that you want to perform. Set the value to DescribeNet workAclAt t ribut es. |
| NetworkAclId | String | Yes | nacl- a2do9e413e0spz asx**** | The ID of the network ACL. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the network ACL belongs. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 0c593ea1-3bea- 11e9-b96b- 88e9fe**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters. It cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclAttr ibute | Struct |   | The details about the network ACL. |
| CreationTime | String | 2019-04-25 11:33:27 | The time when the network ACL was created. |
| Description | String | This is my NetworkAcl. | The description of the network ACL. |
| EgressAclEntrie s | Array of EgressAclEntry |   | The information about outbound rules of the network ACL. |
| EgressAclEntry |   |   |   |
| Description | String | This is EgressAclEntries. | The description of the outbound rule. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DestinationCidrI p | String | 10.0.0.0/24 | The destination CIDR block. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |
| NetworkAclEntr yId | String | nae- a2d447uw4tillxdcv** ** | The ID of the outbound rule. |
| NetworkAclEntr yName | String | acl-2 | The name of the outbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The range of destination ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp: Internet Control Message Protocol (ICMP) gre: Generic Routing Encapsulation (GRE) t cp: TCP udp: UDP all: all protocols supported |
| IngressAclEntrie s | Array of IngressAclEntry |   | The information about inbound rules of the network ACL. |
| IngressAclEntry |   |   |   |
| Description | String | This is IngressAclEntries. | The description of the inbound rule. |
| EntryType | String | custom | The type of the rule. Valid values: cust om: a custom rule syst em: a system rule |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkAclEntr yId | String | nae- a2dk86arlydmevfbg **** | The ID of the inbound rule. |
| NetworkAclEntr yName | String | acl-3 | The name of the inbound rule. |
| Policy | String | accept | The action to be performed on network traffic that matches the rule. Valid values: accept : allows the network traffic. drop: blocks the network traffic. |
| Port | String | -1/-1 | The range of source ports. |
| Protocol | String | all | The transport layer protocols. Valid values: icmp: ICMP gre: GRE t cp: TCP udp: UDP all: All protocols are supported. |
| SourceCidrIp | String | 10.0.0.0/24 | The CIDR block of the source address. |
| NetworkAclId | String | nacl- a2do9e413e0spnhm j**** | The ID of the network ACL. |
| NetworkAclNa me | String | acl-1 | Enter a name for the network ACL. |
| OwnerId | Long | 12345678 | The ID of the Alibaba Cloud account to which the network ACL belongs. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region to which the network ACL belongs. |
| Resources | Array of Resource |   | The resources that are associated with the network ACL. |
| Resource |   |   |   |
| ResourceId | String | vsw- bp1de348lntdwxscd **** | The ID of the associated resource. |

| irtual Private Clou | d |   | Developer Guide·API referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| ResourceType | String | VSwitch | The type of the associated resource. |
| Status | String | BINDED | The state of the associated resource. Valid values: BINDED: The resource is associated with the network ACL. BINDING: The resource is being associated with the network ACL. UNBINDING: The resource is disassociated from the network ACL. |
| Status | String | Available | The state of the associated resource. Valid values: Available: The network ACL is available for use. Modif ying: The network ACL is being configured. |
| VpcId | String | vpc- a2d33rfpl72k5defr** ** | The ID of the VPC to which the network ACL applies. |
| RequestId | String | F5905F9C-0161- 4E72-9CB1- 1F3F3CF6268A | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeNetworkAclAttributes &NetworkAclId=nacl-a2do9e413e0spzasx**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeNetworkAclAttributesResponse>
  <RequestId>F5905F9C-0161-4E72-9CB1-1F3F3CF6268A</RequestId>
  <NetworkAclAttribute>
        <Status>Available</Status>
        <Description>This is my NetworkAcl.</Description>
        <OwnerId>12345678</OwnerId>
        <VpcId>vpc-a2d33rfpl72k5defr****</VpcId>
        <NetworkAclId>nacl-a2do9e413e0spnhmj****</NetworkAclId>
        <CreationTime>2019-04-25 11:33:27</CreationTime>
        <NetworkAclName>acl-1</NetworkAclName>
        <RegionId>cn-qingdao-env17-d01</RegionId>
        <IngressAclEntries>
              <Policy>accept</Policy>
              <Description>This is IngressAclEntries.</Description>
              <EntryType>custom</EntryType>
              <Port>-1/-1</Port>
              <SourceCidrIp>10.0.0.0/24</SourceCidrIp>
              <NetworkAclEntryName>acl-3</NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2dk86arlydmevfbg****</NetworkAclEntryId>
        </IngressAclEntries>
        <EgressAclEntries>
              <Policy>accept</Policy>
              <Description>This is EgressAclEntries.</Description>
              <EntryType>custom</EntryType>
              <DestinationCidrIp>10.0.0.0/24</DestinationCidrIp>
              <Port>-1/-1</Port>
              <NetworkAclEntryName>acl-2</NetworkAclEntryName>
              <Protocol>all</Protocol>
              <NetworkAclEntryId>nae-a2d447uw4tillxdcv****</NetworkAclEntryId>
        </EgressAclEntries>
        <Resources>
              <Status>BINDED</Status>
              <ResourceId>vsw-bp1de348lntdwxscd****</ResourceId>
              <ResourceType>VSwitch</ResourceType>
        </Resources>
  </NetworkAclAttribute>
</DescribeNetworkAclAttributesResponse>
```

`JSON` format `{`

```json
    "RequestId": "F5905F9C-0161-4E72-9CB1-1F3F3CF6268A",
    "NetworkAclAttribute": {
        "Status": "Available",
        "Description": "This is my NetworkAcl.",
        "OwnerId": 12345678,
        "VpcId": "vpc-a2d33rfpl72k5defr****",
        "NetworkAclId": "nacl-a2do9e413e0spnhmj****",
        "CreationTime": "2019-04-25 11:33:27",
        "NetworkAclName": "acl-1",
        "RegionId": "cn-qingdao-env17-d01",
        "IngressAclEntries": {
            "Policy": "accept",
            "Description": "This is IngressAclEntries.",
            "EntryType": "custom",
            "Port": "-1/-1",
            "SourceCidrIp": "10.0.0.0/24",
            "NetworkAclEntryName": "acl-3",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2dk86arlydmevfbg****"
```

`},`

```json
        "EgressAclEntries": {
            "Policy": "accept",
            "Description": "This is EgressAclEntries.",
            "EntryType": "custom",
            "DestinationCidrIp": "10.0.0.0/24",
            "Port": "-1/-1",
            "NetworkAclEntryName": "acl-2",
            "Protocol": "all",
            "NetworkAclEntryId": "nae-a2d447uw4tillxdcv****"
```

`},`

```json
        "Resources": {
            "Status": "BINDED",
            "ResourceId": "vsw-bp1de348lntdwxscd****",
            "ResourceType": "VSwitch"
```

`}` `}` `}`

#### 2.1.19 IPv6 gateways

##### 2.1.19.1 CreateIpv6Gateway

You can call this operation to create an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Gatew ay | The operation that you want to perform. Valid values: Creat eIpv6Gat eway . |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the IPv6 gateway. You can call DescribeRegions interface to obtain the region ID. |   |   |
| VpcId | String | Yes | vpc- 123sedrfswd23** ** | The ID of the virtual private cloud (VPC) for which you want to create the IPv6 gateway. |   |   |
| Spec | String | No | Small | The specification that you want to set for the IPv6 gateway. Valid values: Small (Default value): Free edition. Medium : Enterprise Edition. Large : Enterprise enhanced edition. IPv6 gateways of different specifications have different forwarding capabilities. For more information, see the IPv6 Gateway Specifications . |   |   |
|   |   |   |   |   | IPv6 Gateway |   |
| Name | String | No | ipv6GW | The name of the IPv6 gateway. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, but cannot start with http:// or https:// The beginning. |   |   |
| Description | String | No | ipv6gatewayforV PC1 | The description of the IPv6 gateway. The name must be 2 to 256 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, but cannot start with http:// or https:// The beginning. |   |   |

|   | Specifications |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. The value of this parameter is generated by a client. The value must be unique among different requests and must be 1 to 64 ASCII characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6GatewayId | String | ipv6gw- hp3y0l3ln89j8cdvf** ** | The ID of the IPv6 gateway. |
| RequestId | String | 0ED8D006-F706- 4D23-88ED- E11ED28DCAC | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateIpv6Gateway &RegionId=cn-qingdao-env17-d01 &VpcId=vpc-123sedrfswd23**** &<Public request parameters>
```

Sample success responses `XML` format

```xml
<CreateIpv6GatewayResponse>
        <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
        <Ipv6GatewayId>ipv6gw-hp3y0l3ln89j8cdvf****</Ipv6GatewayId>
</CreateIpv6GatewayResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0",
    "Ipv6GatewayId": "ipv6gw-hp3y0l3ln89j8cdvf****"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidVpcId.NotFou nd | Specified VPC does not exist. | The error message returned because the specified VPC does not exist. |

##### 2.1.19.2 DeleteIpv6Gateway

Deletes an IPv6 gateway. Before you delete an IPv6 gateway of the Enterprise Edition and Enterprise Enhanced Edition, you must delete the outbound-only rule. For more information, see the DeleteIpv6EgressOnlyRule . Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Gatew ay | The operation that you want to perform. Valid values: Delet eIpv6Gat eway . |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3y0l3ln89j8xxx xxxxx | The ID of the IPv6 gateway that you want to delete. |
| RegionId | String | Yes | cn-huhehaote | The ID of the region to which the IPv6 gateway belongs. You can call DescribeRegions interface to obtain the region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E9A8AABE-A84B- 4AF2-A68A- 8E2EA190E7AE | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteIpv6Gateway &Ipv6 GatewayId=ipv6gw-hp3y0l3ln89j8xxxxxxxx &RegionId=cn-huhehaote &<Public request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6GatewayResponse>
  <RequestId>E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE</RequestId>
</DeleteIpv6GatewayResponse>
```

`JSON` format `{`

```json
   "RequestId": "E9A8AABE-A84B-4AF2-A68A-8E2EA190E7AE"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |

##### 2.1.19.3 DescribeIpv6Gateways

Queries IPv6 gateways that you have created. Request parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gate ways | The operation that you want to perform. Valid values: DescribeIpv6Gat eWays . |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region to which the IPv6 gateway belongs. You can call DescribeRegions interface to obtain the region ID. |   |   |
| Ipv6GatewayId | String | No | ipv6gw- 123456**** | The ID of the IPv6 gateway. |   |   |
| VpcId | String | No | vpc-123456**** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |   |   |
| Name | String | No | ipv6GW**** | The name of the IPv6 gateway. |   |   |

| eveloper Guide·API r | eference |   |   | Virtual Private Clou |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to query. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Gateways | Array of Ipv6Gateway |   | The details about the IPv6 gateways. |
| Ipv6Gateway |   |   |   |
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal : normal. FinancialLocked : The overdue payment is locked. |
| CreationTime | String | 2018-12- 20T14:51:23Z | The time when the IPv6 gateway was created. |
| Description | String | descriptionforIPv6G W | The description of the IPv6 gateway. |
| ExpiredTime | String | 2018-12- 20T14:51:23Z | The time when the IPv6 gateway expires. |
| InstanceCharge Type | String | PostPaid | The metering method of the IPv6 gateway. |
| Ipv6GatewayId | String | ipv6gw- hp3rwmtmfhgis**** | The ID of the IPv6 gateway. |
| Name | String | name | The name of the IPv6 gateway. |
| RegionId | String | cn-qingdao-env17- d01 | The region ID of the IPv6 gateway to which the IPv6 address belongs. |
| Spec | String | Small | The specification of the IPv6 gateway. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Available | The status of the IPv6 gateway. |
| VpcId | String | vpc-123456**** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |
| PageNumber | Integer | 1 | The number of the page to query. |
| PageSize | Integer | 19 | The number of entries returned per page. |
| RequestId | String | E3A06196-3E7C- 490D-8F39- CB4B5A0CE8AD | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DescribeIpv6Gateways &RegionId=cn-huhehaote &Common request parameter
```

Sample success responses `XML` format

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
                  <VpcId>vpc-hp3ag7ydchedxxxxxxxxx</VpcId>
                  <Ipv6GatewayId>ipv6gw-hp33of4uz4k4kxxxxxxxx</Ipv6GatewayId>
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
                  <VpcId>vpc-hp3kzilwd9yflxxxxxxxx</VpcId>
                  <Ipv6GatewayId>ipv6gw-hp33p10bdbt77xxxxxxxx</Ipv6GatewayId>
            </Ipv6Gateway>
      </Ipv6Gateways>
      <TotalCount>2</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>E3A06196-3E7C-490D-8F39-CB4B5A0CE8AD</RequestId>
</DescribeIpv6GatewaysResponse>
```

`JSON` format

```json
     { "DescribeIpv6GatewaysResponse": { "TotalCount": 2, "PageSize": 19, "RequestId": "E3A
06196-3E7C-490D-8F39-CB4B5A0CE8AD", "PageNumber": 1, "Ipv6Gateways": { "Status": "Available ", "Description": "descriptionforIPv6GW", "VpcId": "vpc-123456****", "InstanceChargeType": "PostPaid", "ExpiredTime": "2018-12-20T14:51:23Z", "CreationTime": "2018-12-20T14:51:23Z", "Ipv6GatewayId": "ipv6gw-hp3rwmtmfhgis****", "RegionId": "cn-qingdao-env17-d01", "Spec": "S mall", "BusinessStatus": "Normal", "Name": "name" } } }
```

##### 2.1.19.4 ModifyIpv6GatewaySpec

Changes the specification of an IPv6 gateway. Different specifications have different forwarding capabilities and bandwidths. For more information,

```
see IPv6 Gateway Specifications .
```

Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gatew aySpec | The operation that you want to perform. Valid values: Modif yIpv6Gat ewaySpec . |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456**** | The ID of the IPv6 gateway with which the egress-only rules are configured. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the IPv6 gateway. You can call DescribeRegions interface to obtain the region ID. |
| Spec | String | Yes | Middle | The new specification that you want to set for the IPv6 gateway. Valid values: Small (Default value): Free edition. Middle : Enterprise Edition. Large : Enterprise enhanced edition. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. The value of this parameter is generated by a client. The value must be unique among different requests and must be 1 to 64 ASCII characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=ModifyIpv6GatewaySpec &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456xxxxxxxx &Spec=Middle &Common request parameter
```

Sample success responses `XML` format

```xml
<ModifyIpv6GatewaySpecResponse>
      <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewaySpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.19.5 DescribeIpv6EgressOnlyRules

You can call this operation to query the egress-only rules that match specific conditions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Egre ssOnlyRules | The operation that you want to perform. Valid values: DescribeIpv6EgressOnlyRules . |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456******** | The ID of the IPv6 gateway with which the egress-only rules are configured. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the IPv6 gateway. You can call DescribeRegions interface to obtain the region ID. |
| Ipv6EgressOnlyRul eId | String | No | ipv6gwpy- 123456******** | The ID of the egress-only rule that you want to query. |
| Name | String | No | rulename | The name of the egress-only rule. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InstanceType | String | No | Ipv6Address | The type of the instance to which you want to apply the egress-only rule. Set the value to: Ipv6Address : an IPv6 address. |
| InstanceId | String | No | i-123456******** | The ID of the instance that is associated with the IPv6 address to which the egress-only rule is applied. |
| PageNumber | Integer | No | 1 | The page number of the list. Default value: 1 . |
| PageSize | Integer | No | 10 | The number of rows per page in a paged query. The maximum value is 50 , the default value is 10 . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressOnly Rules | Array of Ipv6EgressOnly Rule |   | The details about the egress-only rule. |
| Ipv6EgressOnly Rule |   |   |   |
| Description | String | ruledescription | The description of the egress-only rule. |
| InstanceId | String | i-123456******** | The ID of the instance to which the egress- only rule is applied. |
| InstanceType | String | Ipv6Address | The type of the instance to which the egress-only rule is applied. |
| Ipv6EgressOnly RuleId | String | ipv6gwpy- 123456******** | The ID of the egress-only rule. |
| Name | String | rulename | The name of the egress-only rule. |
| Status | String | Available | The status of the egress-only rule. |

| Developer Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the list. Default value: 1 . |
| PageSize | Integer | 10 | The number of rows per page in a paged query. The maximum value is 50 , the default value is 10 . |
| RequestId | String | E16671B7-DEA6- 48E0-8E9C- 41913DAD44DD | The ID of the request. |
| TotalCount | Integer | 1 | The number of returned entries. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DescribeIpv6EgressOnlyRules &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456xxxxxxxx &Common request parameter
```

Sample success responses `XML` format

```xml
<DescribeIpv6EgressOnlyRulesResponse>
      <Ipv6EgressOnlyRules>
            <Ipv6EgressOnlyRule>
                  <Name></Name>
                  <Status>Available</Status>
                  <Description></Description>
                  <InstanceId>ipv6-hp3b5a8t12ihyxxxxxxxx</InstanceId>
                  <Ipv6EgressOnlyRuleId>ipv6py-hp3w98rmlbqp0xxxxxxxx</Ipv6EgressOnlyRuleId>
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
    "Ipv6EgressOnlyRules": {
        "Ipv6EgressOnlyRule": [
```

`{`

```json
                "Name": "",
                "Status": "Available",
                "Description": "",
                "InstanceId": "ipv6-hp3b5a8t12ihyxxxxxxxx",
                "Ipv6EgressOnlyRuleId": "ipv6py-hp3w98rmlbqp0xxxxxxxx",
                "InstanceType": "Ipv6Address"
```

`}` `]` `},`

```json
    "PageNumber": 1,
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "D1FFB517-D1A7-49BA-9169-C7E7194A9B55"
```

`}`

##### 2.1.19.6 CreateIpv6EgressOnlyRule

Creates an egress-only rule for an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateIpv6Egress OnlyRule | The operation that you want to perform. Valid values: Creat eIpv6EgressOnlyRule . |
| InstanceId | String | Yes | ipv6- hp3nxjkfxn5pnhgl 5**** | The ID of the IPv6 address with which the egress-only rule will be configured. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp3c2paq0ywaua sza**** | The ID of the IPv6 gateway to which the specified IPv6 address belongs. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the IPv6 gateway. You can call DescribeRegions interface to obtain the region ID. |
| InstanceType | String | No | IPv6Address | The type of the instance that will be configured with the egress-only rule. Set the value to: Ipv6Address (Default),IPv6 address. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Name | String | No | rulename | The name of the egress-only rule. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, but cannot start with http:// or https:// The beginning. |
| Description | String | No | ruledescription | The description of the egress-only rule. The name must be 2 to 256 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter, but cannot start with http:// or https:// The beginning. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. The value of this parameter is generated by a client. The value must be unique among different requests and must be 1 to 64 ASCII characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6EgressRuleI d | String | ipv6py- hp3w98rmlbqp0124 5**** | The ID of the egress-only rule. |
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=CreateIpv6EgressOnlyRule &RegionId=cn-huhehaote &InstanceId=ipv6-hp3nxjkfxn5pnhgl5**** &Ipv6GatewayId=ipv6gw-hp3c2paq0ywauasza**** &Common request parameter
```

Sample success responses `XML` format

```xml
<CreateIpv6EgressOnlyRuleResponse>
      <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
      <Ipv6EgressRuleId>ipv6py-hp3w98rmlbqp01245****</Ipv6EgressRuleId>
</CreateIpv6EgressOnlyRuleResponse>
```

`JSON` format

```json
     { "CreateIpv6EgressOnlyRuleResponse": { "Ipv6EgressRuleId": "ipv6py-hp3w98rmlbqp01245*
***", "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75" } }
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.19.7 DeleteIpv6EgressOnlyRule

Deletes an egress-only rule. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Egress OnlyRule | The operation that you want to perform. Set the value to Delet eIpv6EgressOnlyRule. |
| Ipv6EgressOnlyRul eId | String | Yes | ipv6py- hp3w98rmlbqp0x xxxxxxx | The ID of the egress-only rule that you want to delete. |
| RegionId | String | Yes | cn-huhehaote | The ID of the IPv6 gateway. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteIpv6EgressOnlyRule &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-123456 &Ipv6EgressOnlyRuleId=ipv6py-hp3w98rmlbqp0xxxxxxxx &Common request parameter
```

Sample success responses `XML` format

```xml
<DeleteIpv6EgressOnlyRuleResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</DeleteIpv6EgressOnlyRuleResponse>
```

`JSON` format `{`

```json
 "RequestId": "4E40EAF1-783D-4C05-948D-DA0426C398C1"
```

`}`

##### 2.1.19.8 DeleteIpv6InternetBandwidth

Sets the Internet bandwidth value of an IPv6 address to zero. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteIpv6Interne tBandwidth | The operation that you want to perform. Set the value to Delet eIpv6Int ernet Bandwidt h. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-huhehaote | The ID of the region where the IPv6 gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Ipv6AddressId | String | No | ipv6- 123456xxxxxxxx | The ID of the IPv6 address. |
| Ipv6InternetBand widthId | String | No | 2 | The Internet bandwidth value of the IPv6 address. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | E07E0FE6-5C21- 405F-AF82- 7613AA81EF92 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DeleteIpv6InternetBandwidth &RegionId=cn-huhehaote &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
</DeleteIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
 "RequestId": "E07E0FE6-5C21-405F-AF82-7613AA81EF92"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

##### 2.1.19.9 DescribeIpv6GatewayAttribute

You can call this operation to query the details of an IPV6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Gate wayAttribute | The operation that you want to perform. Valid values: DescribeIpv6Gat ewayAt t ribut e . |
| Ipv6GatewayId | String | Yes | ipv6gw- 123456******** | The ID of the IPv6 gateway to query. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the IPv6 gateway. You can call DescribeRegions interface to obtain the region ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BusinessStatus | String | Normal | The status of the IPv6 gateway. Valid values: Normal : normal. FinacialLocked : The overdue payment is locked. Securit yLocked : Security locked. |
| CreationTime | String | 2018-12- 05T09:21:35Z | The time when the IPv6 gateway was created. |
| Description | String | test | The description of the IPv6 gateway. |
| ExpiredTime | String | 2018-12- 05T09:21:35Z | The time when the IPv6 gateway expires. |
| InstanceCharge Type | String | PostPaid | The metering method of the IPv6 gateway. |

| V | irtual Private Clou | d |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6GatewayId | String | ipv6gw- 123456******** | The ID of the IPv6 gateway. |
| Name | String | test | The name of the IPv6 gateway. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the IPv6 gateway is deployed. |
| RequestId | String | ipv6gw- hp33p10bdbt77***** *** | The ID of the request. |
| Spec | String | Medium | The specification of the IPv6 gateway. |
| Status | String | Available | The status of the IPv6 gateway. |
| VpcId | String | vpc-123456******** | The ID of the virtual private cloud (VPC) to which the IPv6 gateway belongs. |

Examples Sample requests

```
https://vpc.cn-huhehaote.aliyuncs.com/?Action=DescribeIpv6GatewayAttribute &Ipv6GatewayId=ipv6gw-hp33p10bdbt77xxxxxxxx &RegionId=cn-huhehaote &Common request parameter
```

Sample success responses `XML` format

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
      <InstanceChargeType>PostPaid</InstanceChargeType>
      <ExpiredTime></ExpiredTime>
      <VpcId>vpc-hp3kzilwd9yflxxxxxxxx</VpcId>
      <Ipv6GatewayId>ipv6gw-hp33p10bdbt77xxxxxxxx</Ipv6GatewayId>
</DescribeIpv6GatewayAttributeResponse>
```

`JSON` format

```json
     { "DescribeIpv6GatewayAttributeResponse": { "Status": "Available", "Description": "tes
t", "RequestId": "ipv6gw-hp33p10bdbt77********", "InstanceChargeType": "PostPaid", "Ipv6Gat ewayId": "ipv6gw-123456********", "BusinessStatus": "Normal", "Name": "test", "VpcId": "vpc -123456********", "ExpiredTime": "2018-12-05T09:21:35Z", "CreationTime": "2018-12-05T09:21: 35Z", "RegionId": "cn-qingdao-env17-d01", "Spec": "Medium" } }
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.19.10 DescribeIpv6Addresses

You can call this operation to query one or more IPv6 addresses. Request parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | DescribeIpv6Addr esses | The operation that you want to perform. Valid values: DescribeIpv6Addresses . |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the IPv6 address resides. You can call DescribeRegions interface to obtain the region ID. |   |   |
| Ipv6AddressId | String | No | ipv6gw- hp33of4uz4k4k** ****** | The ID of the IPv6 address. You can enter up to 20 instance IDs for each call, separated by commas (,). |   |   |
| Ipv6Address | String | No | 2408:xxxx:180:17 01:94c7:bc38:3b fa:d2c | The IPv6 address that you want to query. |   |   |
| Name | String | No | test | The name of the IPv6 address. |   |   |
| AssociatedInstan ceId | String | No | i-123456******** | The ID of the instance that is assigned the IPv6 address. |   |   |

| irtual Private Cloud |   |   |   | Developer Guide·API referenc |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AssociatedInstan ceType | String | No | EcsInstance | The type of the instance that is assigned the IPv6 address. Valid value: EcsInst ance (Default):VPC-type ECS. |
| NetworkType | String | No | Public | The type of connection supported by the IPv6 address. Valid values: Privat e : the private network communication type. Public : the Internet communication type. |
| VpcId | String | No | vpc- 123456******** | The ID of the VPC to which the IPv6 address belongs. |
| VSwitchId | String | No | vsw- 123456******** | The ID of the vSwitch to which the IPv6 address belongs. |
| Ipv6InternetBand widthId | String | No | 1 | The Internet bandwidth of the IPv6 address. |
| PageNumber | Integer | No | 1 | The page number of the list. Default value: 1 . |
| PageSize | Integer | No | 10 | The number of rows per page in a paged query. The maximum value is 50 , the default value is 10 . |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ipv6Addresses | Array of Ipv6Address |   | The details about the IPv6 addresses. |
| Ipv6Address |   |   |   |
| AllocationTime | String | 2018-12- 20T14:56:09Z | The time when the IPv6 address was created. |
| AssociatedInsta nceId | String | i- hp325kt6307888**** **** | The ID of the instance that is assigned the IPv6 address. |

| eveloper Guide·AP | I reference |   | Virtual Private Clou |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AssociatedInsta nceType | String | EcsInstance | The type of the instance associated with the IPv6 address. |
| Ipv6Address | String | 2408:xxxx:0:2900:2 901:3c61:9ff0:xxxx | The IPv6 address. |
| Ipv6AddressId | String | ipv6- hp32vv2klzw4******* * | The ID of the IPv6 address. |
| Ipv6AddressNa me | String | test | The name of the IPv6 address. |
| Ipv6GatewayId | String | ipv6gw- hp38x2x0fz7******** | The ID of the IPv6 gateway to which the IPv6 address belongs. |
| Ipv6InternetBan dwidth | Struct |   | The information about the Internet bandwidth of the IPv6 address. |
| Bandwidth | Integer | 2 | The exclusive Internet bandwidth of the IPv6 address. Unit: Mbit/s. |
| BusinessStatus | String | Normal | The status of the exclusive bandwidth of the IPv6 address. Valid values: Normal : normal. FinacialLocked : The overdue payment is locked. Securit yLocked : Security locked. |
| InstanceCharge Type | String | PostPaid | The billing method of the IPv6 gateway. Valid values: Post Paid : Pay-as-you-go. |
| InternetCharge Type | String | PayByTraffic | The metering method of the IPv6 gateway. Valid values: PayByT raf f ic : pay-by-data-transfer. PayByBandwidt h : pay-by-bandwidth. |
| Ipv6InternetBan dwidthId | String | ipv6bw- hp3b35oq1fj50kbvm xxx | The ID of the Internet bandwidth. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkType | String | Public | The type of connection supported by the IPv6 address. Valid values: Privat e : the private network communication type. Public : the Internet communication type. |
| RealBandwidth | Integer | 2 | The peak bandwidth value of the IPv6 address. Valid value: If the EIP Bandwidth Plan is added, then RealBandwidt h The value of is the peak EIP Bandwidth Plan. If not joined, then RealBandwidt h is the Internet bandwidth of IPv6 itself. If the IPv6 address is not added to the EIP Bandwidth Plan and no public bandwidth is purchased, RealBandwidt h and Bandwidt h The values of are all zero. |
| Status | String | Available | The status of the IPv6 address. Valid values: Pending : is being configured. Available : available. |
| VSwitchId | String | vsw- hp3123456******** | The ID of the vSwitch to which the IPv6 address belongs. |
| VpcId | String | vpc-123456******** | The ID of the VPC to which the IPv6 address belongs. |
| PageNumber | Integer | 1 | The page number of the list. Default value: 1 . |
| PageSize | Integer | 10 | The number of rows per page in a paged query. The maximum value is 50 , the default value is 10 . |
| RequestId | String | AA4486A8-B6AE- 469E-AB09- 820EF8ECFA2B | The ID of the request. |
| TotalCount | Integer | 2 | The number of returned entries. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=DescribeIpv6Addresses &RegionId=cn-huhehaote &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeIpv6AddressesResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>2</TotalCount>
      <Ipv6Addresses>
            <Ipv6Address>
                  <Ipv6AddressId>ipv6-hp32vv2klzw4yxxxxxxxx</Ipv6AddressId>
                  <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
                  <AllocationTime>2019-01-07T05:16:23Z</AllocationTime>
                  <Ipv6InternetBandwidth>
                        <BusinessStatus></BusinessStatus>
                        <Ipv6InternetBandwidthId></Ipv6InternetBandwidthId>
                        <InternetChargeType></InternetChargeType>
                        <Bandwidth>0</Bandwidth>
                  </Ipv6InternetBandwidth>
                  <VSwitchId>vsw-hp3lyltb1dosjxxxxxxxx</VSwitchId>
                  <VpcId>vpc-hp34hflqqsjh3xxxxxxxx</VpcId>
                  <Ipv6GatewayId></Ipv6GatewayId>
                  <Status>Available</Status>
                  <NetworkType>Private</NetworkType>
                  <Ipv6Address>2408:xxxx:0:2900:2901:3c61:9ff0:8fdc</Ipv6Address>
                  <Ipv6AddressName></Ipv6AddressName>
                  <AssociatedInstanceId>i-hp325kt6307wxxxxxxxx</AssociatedInstanceId>
                  <RealBandwidth>0</RealBandwidth>
            </Ipv6Address>
            <Ipv6Address>
                  <Ipv6AddressId>ipv6-hp331xt3oqafdxxxxxxxx</Ipv6AddressId>
                  <AssociatedInstanceType>EcsInstance</AssociatedInstanceType>
                  <AllocationTime>2018-11-30T07:39:31Z</AllocationTime>
                  <Ipv6InternetBandwidth>
                        <BusinessStatus></BusinessStatus>
                        <Ipv6InternetBandwidthId></Ipv6InternetBandwidthId>
                        <InternetChargeType></InternetChargeType>
                        <Bandwidth>0</Bandwidth>
                  </Ipv6InternetBandwidth>
                  <VSwitchId>vsw-hp3ju1q8dtgfgxxxxxxxx</VSwitchId>
                  <VpcId>vpc-hp3kzilwd9yflxxxxxxxx</VpcId>
                  <Ipv6GatewayId>ipv6gw-hp33p10bdbt77xxxxxxxx</Ipv6GatewayId>
                  <Status>Available</Status>
                  <NetworkType>Private</NetworkType>
                  <Ipv6Address>2408:xxxx:c0:200:35b:cd32:c460:6aa3</Ipv6Address>
                  <Ipv6AddressName>abc</Ipv6AddressName>
                  <AssociatedInstanceId>i-hp37gpsnhjn4xxxxxxxx</AssociatedInstanceId>
                  <RealBandwidth>0</RealBandwidth>
            </Ipv6Address>
      </Ipv6Addresses>
      <PageSize>10</PageSize>
      <RequestId>AA4486A8-B6AE-469E-AB09-820EF8ECFA2B</RequestId>
</DescribeIpv6AddressesResponse>
```

`JSON` format

```json
     { "DescribeIpv6AddressesResponse": { "TotalCount": 2, "PageSize": 10, "RequestId": "AA
4486A8-B6AE-469E-AB09-820EF8ECFA2B", "PageNumber": 1, "Ipv6Addresses": { "AllocationTime": "2018-12-20T14:56:09Z", "Status": "Available", "AssociatedInstanceId": "i-hp325kt6307888***
*****", "VpcId": "vpc-123456********", "NetworkType": "Public", "VSwitchId": "vsw-hp3123456
********", "Ipv6AddressId": "ipv6-hp32vv2klzw4********", "Ipv6GatewayId": "ipv6gw-hp38x2x0f
z7********", "RealBandwidth": 2, "AssociatedInstanceType": "EcsInstance", "Ipv6Address": "2 408:xxxx:0:2900:2901:3c61:9ff0:xxxx", "Ipv6AddressName": "test", "Ipv6InternetBandwidth": { "InstanceChargeType": "PostPaid", "Bandwidth": 2, "Ipv6InternetBandwidthId": "ipv6bw-hp3b35 oq1fj50kbvmxxx", "BusinessStatus": "Normal", "InternetChargeType": "PayByTraffic" } } } }
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.19.11 ModifyIpv6InternetBandwidth

You can call this operation to modifiy the public network bandwidth of an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Interne tBandwidth | The operation that you want to perform. Valid values: Modif yIpv6Int ernet Bandwidt h . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Long | Yes | 4 | The public bandwidth of the IPv6 address. Unit: Mbit /s. Valid values: 1~5000 . When Int ernet ChargeT ype For PayByBandwidt h , the public bandwidth of the IPv6 address is 1 to 5000. When Int ernet ChargeT ype For PayByT raf f ic , the public bandwidth range of IPv6 addresses is also restricted by the IPv6 gateway specifications. Small (Default free edition). The public bandwidth ranges from 1 to 500. Medium (Enterprise Edition). The Internet bandwidth ranges from 1 to 1000. Large (Enterprise Enhanced Edition). The Internet bandwidth ranges from 1 to 2000. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the IPv6 gateway. You can call DescribeRegions interface to obtain the region ID. |
| Ipv6AddressId | String | No | ipv5- 1233456******** | The ID of the IPv6 address. |
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

Examples Sample requests

```
https://vpc.cn-huhehaote.aliyuncs.com/?Action=ModifyIpv6InternetBandwidth &Bandwidth=3 &Ipv6AddressId=ipv6-hp351bytt9inrxxxxxxxx &RegionId=cn-huhehaote &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6InternetBandwidthResponse>
      <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
    "RequestId": "D560AF68-4CE8-4A5C-B3FE-469F558094D0"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.19.12 AllocateIpv6InternetBandwidth

Purchases Internet bandwidth resources for an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AllocateIpv6Inter netBandwidth | The operation that you want to perform. Set the value to Allocat eIpv6Int ernet Bandwidt h. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 2 | The amount of Internet bandwidth resources of the IPv6 address, in Mbit/s. Valid values: 1 t o 5000. If Int ernet ChargeT ype is set to PayByBandwidt h, the Internet bandwidth of the IPv6 address is from 1 to 5,000 Mbit/s. If Int ernet ChargeT ype is set to PayByT raf f ic, the amount of Internet bandwidth resources of the IPv6 address is limited by the specification of the IPv6 gateway. Small (default) specifies the Free edition and the Internet bandwidth is from 1 to 500 Mbit/s. Medium specifies the Medium edition and the Internet bandwidth is from 1 to 1,000 Mbit/s. Large specifies the Large edition and the Internet bandwidth is from 1 to 2,000 Mbit/s. |
| Ipv6AddressId | String | Yes | ipv6- 123456xxxxxxxx | The ID of the IPv6 address. |
| Ipv6GatewayId | String | Yes | ipv5gw- 123456xxxxxxxx | The ID of the IPv6 gateway. |
| RegionId | String | Yes | cn-huhehaote | The ID of the region where the IPv6 gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| InternetChargeTy pe | String | No | PayByTraffic | The metering method of the Internet bandwidth resources of the IPv6 gateway. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h (default): pay- by-bandwidth |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ClientToken | String | No | 123456 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| InternetBandwi dthId | String | 2 | The amount of Internet bandwidth resources purchased for the IPv6 gateway. |
| Ipv6AddressId | String | ipv6- hp352ungkzcknxxxx xxxx | The ID of the IPv6 address. |
| RequestId | String | 6972A26E-99B1- 4367-9890- FBDEBB0F5E7D | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?AllocateIpv6InternetBandwidth &Ipv6AddressId=ipv6-123456xxxxxxxx &Ipv6GatewayId=ipv6gw-123456xxxxxxxx &RegionId=cn-huhehaote &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AllocateIpv6InternetBandwidthResponse>
   <RequestId>6972A26E-99B1-4367-9890-FBDEBB0F5E7D</RequestId>
   <InternetBandwidthId>2</InternetBandwidthId>
   <Ipv6AddressId>ipv6-hp352ungkzcknxxxxxxxx</Ipv6AddressId>
</AllocateIpv6InternetBandwidthResponse>
```

`JSON` format `{`

```json
    "RequestId": "6972A26E-99B1-4367-9890-FBDEBB0F5E7D",
    "InternetBandwidthId": 2,
    "Ipv6AddressId": "ipv6-hp352ungkzcknxxxxxxxx"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |

##### 2.1.19.13 ModifyIpv6AddressAttribute

You can call this operation to modify the name and description of an IPv6 address. Request parameters

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Addre ssAttribute | The operation that you want to perform. Valid values: Modif yIpv6AddressAt t ribut e . |   |   |
| Ipv6AddressId | String | Yes | ipv6- hp32vv2klzw4yer df**** | The ID of the IPv6 address. |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the IPv6 address resides. You can call DescribeRegions Obtain the region ID. |   |   |
| Name | String | No | test | The name of the IPv6 address. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character. But not with http:// or https:// The beginning. |   |   |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Description | String | No | test | The description of the IPv6 address. The name must be 2 to 256 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter or Chinese character. But not with http:// or https:// The beginning. |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D560AF68-4CE8- 4A5C-B3FE- 469F558094D0 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/? Action=ModifyIpv6AddressAttribute &Ipv6AddressId=ipv6-hp32vv2klzw4yerdf**** &RegionId=cn-huhehaote &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyIpv6AddressAttributeResponse>
      <RequestId>D560AF68-4CE8-4A5C-B3FE-469F558094D0</RequestId>
</ModifyIpv6AddressAttributeResponse>
```

`JSON` format

```json
     { "ModifyIpv6AddressAttributeResponse": { "RequestId": "D560AF68-4CE8-4A5C-B3FE-469F55
8094D0" } }
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

##### 2.1.19.14 ModifyIpv6GatewayAttribute

Modifies the name and description of an IPv6 gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyIpv6Gatew ayAttribute | The operation that you want to perform. Set the value to Modif yIpv6Gat ewayAt t ribut e. |
| Ipv6GatewayId | String | Yes | ipv6gw- hp39kh1ya51yzp 2lu**** | The ID of the IPv6 gateway that you want to modify. |
| RegionId | String | Yes | cn-huhehaote | The ID of the region where the IPv6 gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | ipv6name | The name of the IPv6 gateway. |
| Description | String | No | ipv6description | The description of the IPv6 gateway. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DFEDBEE-E5AB- 49E8-A2DC- CC114C67AF75 | The ID of the request. |

Examples Sample requests

```
https://vpc.aliyuncs.com/?Action=ModifyIpv6GatewayAttribute &RegionId=cn-huhehaote &Ipv6GatewayId=ipv6gw-hp39kh1ya51yzp2lu**** &Common request parameter
```

Sample success responses `XML` format

```xml
<ModifyIpv6GatewayAttributeResponse>
   <RequestId>9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75</RequestId>
</ModifyIpv6GatewayAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId": "9DFEDBEE-E5AB-49E8-A2DC-CC114C67AF75"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
