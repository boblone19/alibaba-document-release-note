---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 NAT Gateway Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 96
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 NAT Gateway Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20NAT%20Gateway%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 NAT Gateway Developer Guide 20220928

## Table of Contents

- 1 Make SDK calls by using ASAPI
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
  - 2.1 List of operations by function
  - 2.2 Make API requests
    - 2.2.1 Request syntax
    - 2.2.2 API authorization
    - 2.2.3 Request signatures
  - 2.3 RAM authentication
  - 2.4 Common parameters
  - 2.5 NAT gateways
    - 2.5.1 ModifyNatGatewayAttribute
    - 2.5.2 ModifyNatGatewaySpec
    - 2.5.3 DeleteNatGateway
  - 2.6 DNAT tables
    - 2.6.1 CreateForwardEntry
    - 2.6.2 DeleteForwardEntry
    - 2.6.3 ModifyForwardEntry
    - 2.6.4 DescribeForwardTableEntries
  - 2.7 SNAT tables
    - 2.7.1 CreateSnatEntry
    - 2.7.2 DeleteSnatEntry
    - 2.7.3 ModifySnatEntry
    - 2.7.4 DescribeSnatTableEntries
  - 2.8 NAT bandwidth packages
    - 2.8.1 CreateBandwidthPackage
    - 2.8.2 ModifyBandwidthPackageSpec
    - 2.8.3 ConvertBandwidthPackage
    - 2.8.4 DescribeBandwidthPackages
    - 2.8.5 ModifyBandwidthPackageAttribute
    - 2.8.6 DeleteBandwidthPackage
    - 2.8.7 RemoveBandwidthPackageIps

## 1 Make SDK calls by using ASAPI

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). Method 1: Use Registration Vars of Services to generate an endpoint
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
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated:

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

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure
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

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

Not e

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
Method 1: Create a Maven project in IntelliJ IDEA. Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure.
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
If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations:

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI.

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

Configure a proxy Perform the following steps to configure a proxy:
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

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls:

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

Request headers

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

Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

Configure proxies Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. Parameter To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

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

Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
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

### 2.1 List of operations by function

The following table lists API operations available for use in NAT Gateway.

| API | Description |
|---|---|
| ModifyNatGatewayAttribute | Modifies the name and description of a NAT gateway. |
| ModifyNatGatewaySpec | Resizes a NAT gateway. |
| DeleteNatGateway | Deletes a specified NAT gateway. |
| CreateForwardEntry | Adds DNAT entries to a DNAT table. |
| DeleteForwardEntry | Deletes a specified DNAT entry. |
| ModifyForwardEntry | Modifies a specified DNAT entry. |
| DescribeForwardTableEntries | Queries DNAT entries in a specified DNAT table. |
| CreateSnatEntry | Adds SNAT entries to an SNAT table. |
| DeleteSnatEntry | Deletes a specified SNAT entry from an SNAT table. |
| ModifySnatEntry | Modifies the value of SnatIp (public IP address) in a specified SNAT entry. |
| DescribeSnatTableEntries | Queries SNAT entries in a specified SNAT table. |
| CreateBandwidthPackage | Creates a NAT service plan. |
| ModifyBandwidthPackageSpec | Modifies the bandwidth value of a NAT service plan. |
| ConvertBandwidthPackage | Converts a NAT service plan to an EIP bandwidth plan. |
| DescribeBandwidthPackages | Queries NAT service plans in a specified region. |
| ModifyBandwidthPackageAttribute | Modifies the name and description of a specified NAT service plan. |
| DeleteBandwidthPackage | Deletes a NAT service plan. |
| RemoveBandwidthPackageIps | Removes a public IP address from a NAT service plan. |

### 2.2 Make API requests

#### 2.2.1 Request syntax

To send a NAT Gateway API request, you must send an HTTP GET request to the NAT Gateway endpoint. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8. NAT Gateway API operations use the RPC protocol. You can call NAT Gateway API operations by sending HTTP GET requests. The following example shows the syntax of a NAT Gateway API request:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the NAT Gateway API. The endpoint of the NAT Gateway API is `vpc.`exa mple`.com` . Not e `example.com` is a custom domain name. You can obtain the endpoint in the Apsara Uni-manager Operations Console. For more information, see Generate the ASAPI endpoint. Action: the name of the operation that you want to perform. For example, to query NAT gateways, you must set the Action parameter to DescribeNatGateways. Version: the version of the API that you want to call. The current NAT Gateway API version is 2016-04 -28. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information about common parameters, see Common parameters. The following example demonstrates how to call the DescribeNatGateways operation to query NAT gateways: Not e The sample requests are formatted to improve readability.

```
https://vpc.example.com/?Action=DescribeNatGateways &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 2.2.2 API authorization

To ensure the security of your account, we recommend that you call NAT Gateway API operations as a RAM user. To call NAT Gateway API operations as a RAM user, you must create and attach authorization policies to the RAM user. For more information about the NAT Gateway resources and API operations that allow the authorization, see RAM authentication.

#### 2.2.3 Request signatures

You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. NAT Gateway implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to an RPC API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
```

SHA1`&Signature=`xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take DescribeNatGateways as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the following code shows the original request URL:

```
http://vpc.example.com/?Action=DescribeNatGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Create a string-to-sign by using the request parameters:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeNatGateways&Format%3DXML&SignatureMethod% 3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1. 0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string-to-sign.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request as the Signature parameter:

```
http://vpc.example.com/?Action=DescribeNatGateways &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 2.3 RAM authentication

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

### 2.4 Common parameters

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

### 2.5 NAT gateways

#### 2.5.1 ModifyNatGatewayAttribute

Modifies the name and description of a NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNatGatew ayAttribute | The operation that you want to perform. Set the value to Modif yNat Gat ewayAt t ribut e. |
| NatGatewayId | String | Yes | ngw- 2ze0dcn4mq31qx 2jc**** | The ID of the NAT gateway that you want to modify. |
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

#### 2.5.2 ModifyNatGatewaySpec

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

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: t rue: enables automatic payment. f alse: disables automatic payment. This is the default value. |
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
| 404 | InvalidNatGatewayId .NotFound | The specified NatGatewayId does not exist in our records. | The error message returned because the specified NAT gateway ID does not exist. Check whether the NAT gateway ID is valid. |
| 400 | NATGW MODIFY SPE _ _ C SAME _ | The specified Spec is same with now. | The error message returned because the specified gateway size is the same as the current one. |
| 400 | InvalidParameter.Sp ec.ValueNotSupport ed | The specified Spec is not valid. | The error message returned because the specified gateway size is invalid. |

#### 2.5.3 DeleteNatGateway

Deletes a specified NAT gateway. Not e Before you delete a NAT gateway, you must disassociate NAT service plans from the NAT gateway. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNatGatewa y | The operation that you want to perform. Set the value to Delet eNat Gat eway. |
| NatGatewayId | String | Yes | ngw- bp1uewa15k4iy5 770**** | The ID of the NAT gateway. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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

### 2.6 DNAT tables

#### 2.6.1 CreateForwardEntry

Adds a DNAT entry to a DNAT table. Description Each DNAT entry consists of the following parameters: ExternalIp, ExternalPort, Protocol, InternalIp, and InternalPort. After you add a DNAT entry, the NAT gateway forwards packets of the specified protocol from [ExternalIp: ExternalPort] to [InternalIp: InternalPort] and sends responses back over the same route. When you call this operation, take note of the following limits: The combinations of ExternalIp, ExternalPort, and Protocol used in DNAT entries must be unique. Requests cannot be distributed to more than one Elastic Compute Service (ECS) instance if these requests are originated from the same source IP address, received on the same port, and use the same protocol. The combinations of Protocol, InternalIp, and InternalPort used in DNAT entries must be unique. If one or more DNAT entries in the DNAT table are in the Pending or Modifying state, you cannot add DNAT entries to the DNAT table. The public IP address (ExternalIp) in the DNAT entry, which is used to access the Internet, must meet the following requirements: If you have purchased a NAT service plan before November 3, 2017, the ExternalIp must be a public IP address in the NAT service plan. If you have not purchased a NAT service plan before November 3, 2017, the ExternalIp must be an elastic IP address (EIP) associated with the NAT service plan. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. The private IP address (InternalIp) in the DNAT entry must meet the following requirements: The private IP address must belong to the CIDR block of the virtual private cloud (VPC) where the NAT gateway is deployed. The DNAT entry takes effect only when the private IP address is allocated to an ECS instance and the ECS instance is not assigned an EIP. If the private IP address is allocated to a resource other than an ECS instance, such as a high-availability virtual IP addresses (HAVIPs), Server Load Balancer (SLB) instance, or RDS instance, the DNAT entry does not take effect. Consequently, inbound traffic cannot be forwarded to the private IP address. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. You can add up to 100 DNAT entries to a DNAT table. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateForwardEn try | The operation that you want to perform. Set the value to Creat eForwardEnt ry. |
| ExternalIp | String | Yes | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | Yes | 8080 | The public port. Valid values: 1 t o 65535. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlc qpa**** | The ID of the DNAT table. |
| InternalIp | String | Yes | 192.XX.XX.1 | The destination private IP address. |
| InternalPort | String | Yes | 80 | The destination private port. Valid values: 1 t o 65535. |
| IpProtocol | String | Yes | TCP | The protocol that is used by the ports. Valid values: T CP: forwards TCP packets. UDP: forwards UDP packets. Any: forwards packets of all protocols. |
| RegionId | String | Yes | cn-qingdao- env17-d0 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The name must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |
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

| eveloper Guid | e·API reference |   | NAT Gatewa |
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

#### 2.6.2 DeleteForwardEntry

Deletes a DNAT entry. Not e You cannot delete DNAT entries if one or more DNAT entries in the DNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteForwardEn try | The operation that you want to perform. Set the value to Delet eForwardEnt ry. |
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0 g**** | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb3 34**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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

|   | NAT Gateway |   |   | Developer Guide·API referenc | e |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 404 | InvalidForwardEntryI d.NotFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 400 | IncorretForwardEntr yStatus | The Specified forwardEntry is not exist | The error message returned because the specified DNAT entry does not exist. |
| 400 | MissingParameter | Missing mandatory parameter | The error message returned because one or more required parameters are not set. Check whether you have set all required parameters. |

#### 2.6.3 ModifyForwardEntry

Modifies a DNAT entry. Not e You cannot modify DNAT entries if one or more DNAT entries in the DNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyForwardEn try | The operation that you want to perform. The operation that you want to perform. Set the value to Modif yForwardEnt ry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ForwardEntryId | String | Yes | fwd- 8vbn3bc8roygjp0 gy3xk7 | The ID of the DNAT entry. |
| ForwardTableId | String | Yes | ftb- 8vbx8xu2lqj9qb3 34h0ow | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ExternalIp | String | No | 116.XX.XX.28 | The public IP address of the NAT gateway. |
| ExternalPort | String | No | 80 | The public port. Valid values: 1 to 65535. |
| InternalIp | String | No | 10.XX.XX.78 | The destination private IP address. |
| InternalPort | String | No | 80 | The destination private port. Valid values: 1 to 65535. |
| IpProtocol | String | No | TCP | The protocol type. Valid values: T CP: forwards Transmission Control Protocol (TCP) packets. UDP: forwards User Datagram Protocol (UDP) packets. Any: forwards packets of all protocols. |
| ForwardEntryNam e | String | No | ForwardEntry-1 | The name of the DNAT entry. The description must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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

| D | eveloper Guid | e·API reference |   | NAT Gatewa | y |
|---|---|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidExternalIp.Mal formed | The specified ExternalIp is not a valid IP address. | The error message returned because the specified IP address is invalid. |
| 400 | InvalidInternalIp.Malf ormed | The specified InternalIp is not a valid IP address. | The error message returned because the specified private IP address is invalid. |
| 400 | InvalidExternalPort.M alformed | The specified ExternalPort is not a valid port. | The error message returned because the specified public port is invalid. |
| 400 | InvalidInternalPort.M alformed | The specified InternalPort is not a valid port. | The error message returned because the specified private port is invalid. |
| 400 | Forbidden.Destnatio nIpOutOfVpcCIDR | The specified Destination Ip is Out of VPC CIDR. | The error message returned because the specified private IP address does not fall within the CIDR block of the VPC. Enter a private IP address that falls within the CIDR block of the VPC. |
| 400 | InvalidProtocal.Valu eNotSupported | The specified IpProtocol does not support. | The error message returned because the specified protocol is not supported. |
| 400 | IncorretForwardEntr yStatus | Some Forward entry status blocked this operation.. | The error message returned because the operation cannot be performed. The error message returned because one or more DNAT entries in the DNAT table are in the Pending or Modifying state. |
| 400 | QuotaExceeded | Forward entry quota exceeded in this route table. | The error message returned because one route table cannot contain more than 48 custom routes to a route table. You can submit a ticket to increase the quota. |
| 404 | InvalidForwardEntryI d.NotFound | Specified forward entry ID does not exist | The error message returned because the specified DNAT entry does not exist. |
| 404 | InvalidExternalIp.Not Found | Specified External Ip address does not found on the VRouter | The error message returned because the specified public IP address does not exist. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidForwardTableI d.NotFound | Specified forward table does not exist. | The error message returned because the specified DNAT table does not exist. Check the parameter value and try again. |
| 400 | Forbidden.ExternalIp .UsedInSnatTable | The specified ExternalIp is already used in SnatTable | The error message returned because the specified public IP address is already used by an SNAT entry. Select a different IP address or delete the SNAT entry. |
| 400 | Forbidden.Already.B ounded | The specified instance already bounded | The error message returned because the specified instance is already associated with another DNAT entry. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the format of the specified name is invalid. |

#### 2.6.4 DescribeForwardTableEntries

Queries DNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeForward TableEntries | The operation that you want to perform. Set the value to DescribeForwardT ableEnt ries. |
| ForwardTableId | String | Yes | ftb- bp1mbjubq34hlc qpa**** | The ID of the DNAT table. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ForwardEntryId | String | No | fwd- 8vbn3bc8roygjp0 gy**** | The ID of the DNAT entry that is automatically assigned. |
| ExternalIp | String | No | 116.XX.XX.28 | The public IP address of the NAT gateway. |

| eveloper Guide·API r | eference |   |   | NAT Gatewa |
|---|---|---|---|---|

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

| NAT Gateway |   |   | Developer Guide·API referenc |
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

### 2.7 SNAT tables

#### 2.7.1 CreateSnatEntry

Adds an SNAT entry to an SNAT table. Description When you call this operation, take note of the following limits: The vSwitch and the Elastic Compute Service (ECS) instance specified in the SNAT entry must belong to the virtual private cloud (VPC) where the NAT gateway is deployed. Each vSwitch or ECS instance can be specified in only one SNAT entry. If a high-availability virtual IP address (HAVIP) exists in the vSwitch, you cannot create SNAT entries. You cannot specify the same EIP in both a DNAT entry and an SNAT entry. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateSnatEntry | The operation that you want to perform. Set the value to Creat eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatIp | String | Yes | 47.XX.XX.98 | The public IP addresses. Separate multiple IP addresses with commas (,). |
| SnatTableId | String | Yes | stb- bp190wu8io1vge v**** | The ID of the SNAT table. |
| SourceVSwitchId | String | No | vsw- bp1nhx2s9ui5o*** * | The ID of the vSwitch that requires to access the Internet. |

| Developer Guide·API r | eference |   |   | NAT Gatewa |
|---|---|---|---|---|

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

| NAT Gateway |   |   | Developer Guide·API referenc |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.IpUsedInF orwardTable | The specified SnatIp already used in forward table | The error message returned because the specified public IP address is already used by a DNAT entry. Select another public IP address or delete the DNAT entry. |
| 400 | Forbindden | The specified Instance already bind eip | The error message returned because the ECS instance is associated with an EIP. Disassociate the EIP from the ECS instance before you create forwarding rules. |
| 400 | OperationUnsupport ed.CidrConflict | The specified CIDR block conflicts with an existing SNAT entry. | The error message returned because the specified CIDR block conflicts with those in existing SNAT entries. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |

#### 2.7.2 DeleteSnatEntry

Deletes a specified SNAT entry. Not e You cannot delete SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteSnatEntry | The operation that you want to perform. Set the value to Delet eSnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0pl qc**** | The ID of the SNAT entry. |

| Developer Guide·API r | eference |   |   | NAT Gatewa |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
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

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotF ound | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 400 | IncorretSnatEntrySta tus | Some Snat entry status blocked this operation.. | The error message returned because you are not authorized to perform the specified operation. The error message returned because one or more SNAT entries in the SNAT table are in the Pending or Modifying state. |
| 404 | InvalidSnatEntryId.N otFound | Specified Snat entry ID does not exist | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 404 | InvalidSnatTableId.N otFound | Specified SNAT table does not exist. | The error message returned because the specified SNAT table does not exist. Check whether the ID of the SNAT table is valid. |
| 404 | InvalidSnatEntryId.N otFound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |

#### 2.7.3 ModifySnatEntry

Modifies a specified SNAT entry. Not e You cannot modify SNAT entries if one or more SNAT entries in the SNAT table are in the Pending or Modif ying state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySnatEntry | The operation that you want to perform. Set the value to Modif ySnat Ent ry. |
| RegionId | String | Yes | cn-qingdao- env17-d0 | The ID of the region where the NAT gateway is deployed. |

| Developer Guide·API r | eference |   |   | NAT Gatewa |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SnatEntryId | String | Yes | snat- bp1vcgcf8tm0pl qcg**** | The ID of the SNAT entry. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u 3t**** | The ID of the SNAT table to which the SNAT entry belongs. |
| SnatIp | String | Yes | 47.XX.XX.98 | The public IP address in the SNAT entry. If multiple IP addresses are specified, separate them with commas (,). |
| SnatEntryName | String | No | SnatEntry-1 | The name of the SNAT entry. The description must be 2 to 128 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. Only ASCII characters are allowed. It can contain up to 64 ASCII characters. |

Response parameters

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
| 404 | InvalidSnatEntryId.N otFound | Specified SNAT entry does not exist. | The error message returned because the specified SNAT entry does not exist. Check whether the SNAT entry is valid. |
| 400 | Forbidden.SourceVS witchId.Duplicated | The specified SourceCIDRis duplicated. | The error message returned because an SNAT entry is already configured for the specified vSwitch. |
| 404 | InvalidSnatIp.NotFou nd | Specified SnatIp does not found on the NAT Gateway | The error message returned because the specified public IP address does not exist in the NAT gateway. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Forbidden.IpUsedInF orwardTable | The specified SnatIp already used in forward table | The error message returned because the specified public IP address is already used by a DNAT entry. Select another IP address or delete the DNAT rule that uses the public IP address. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name format is invalid. |

#### 2.7.4 DescribeSnatTableEntries

Queries SNAT entries. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSnatTabl eEntries | The operation that you want to perform. Set the value to DescribeSnat T ableEnt ries. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| SnatTableId | String | Yes | stb- 8vbczigrhop8x5u 3t**** | The ID of the SNAT table. |
| SnatEntryId | String | No | snat- 8vbae8uqh7rjpk7 d2**** | The ID of the SNAT entry. |
| SourceVSwitchId | String | No | vsw-3xb**** | The ID of the vSwitch that can access the Internet through SNAT. |
| SourceCIDR | String | No | 116.XX.XX.0/28 | The source CIDR block of the SNAT entry. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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
| SnatTableId | String | stb- 8vbczigrhop8x5u3t* *** | The ID of the SNAT table to which the SNAT entry belongs. |
| SourceCIDR | String | 116.XX.XX.0/28 | The source CIDR block of the SNAT entry. |
| SourceVSwitchI d | String | vsw-3xb**** | The ID of the vSwitch that can access the Internet through SNAT. |

| Parameter | Type | Example | Description |
|---|---|---|---|
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

### 2.8 NAT bandwidth packages

#### 2.8.1 CreateBandwidthPackage

Creates a NAT service plan. Description A NAT service plan consists of bandwidth resources and one or more public IP addresses. You can associate up to four NAT service plans with a NAT gateway. A NAT service plan includes: Bandwidth resources One or more public IP addresses Not e This operation can be performed by only Apsara Stack accounts that have purchased NAT service plans before November 3, 2017. If you have not purchased a NAT service plan before November 3, 2017, you can apply for public IP addresses by associating elastic IP addresses (EIPs). Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBandwidth Package | The operation that you want to perform. Set the value to Creat eBandwidt hPackage. |
| Bandwidth | Integer | Yes | 5 | The maximum bandwidth of the NAT service plan. Valid values: 5 to 1000. Unit: Mbit/s. |
| IpCount | Integer | Yes | 2 | The number of public IP addresses in the NAT service plan. Valid values: 1 t o 50. |
| NatGatewayId | String | Yes | ngw- 7mwb327j1**** | The ID of the NAT gateway. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | The name of the NAT service plan. | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. The name cannot start with http:// or https:// . |
| Description | String | No | The description of the NAT service plan. | The description of the NAT service plan. The name must be 2 to 256 characters in length, and start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 001**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate a token, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| ISP | String | No | BGP | Only BGP is supported. |
| Zone | String | No | cn-qingdao- env17- amtest11001-a | The zone to which the NAT service plan belongs. If you do not set this parameter, the service plan is randomly allocated to a zone. Not e Connectivity is not affected when the IP addresses provided by the NAT service plan and the backend Elastic Compute Service (ECS) instances belong to different zones. However, when the IP addresses and ECS instances belong to the same zone, latency can be reduced. |
| InternetChargeTy pe | String | No | PayByBandwidth | The metering method of the NAT service plan. Valid values: PayByT raf f ic: pay-by-data-transfer PayByBandwidt h：按带宽计费。 |

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
| 400 | QuotaExceeded.Ban dwidthPackageIps | The specified ipCount exceeded quota. | The error message returned because the number of IP addresses has reached the upper limit. Submit a ticket to increase the quota. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Ban dwidthPackageCoun tOnNatGateway | BandwidthPackage count limit on one NatGateway exceeded. | The error message returned because the number of NAT service plans has reached the upper limit. You can associate up to four NAT service plans with a NAT gateway. |
| 400 | InvalidParameter.Na me.Malformed | The specified Name is not valid. | The error message returned because the specified name is invalid. |
| 400 | InvalidParameter.De scription.Malformed | The specified Description is not valid. | The error message returned because the specified description is invalid. |
| 400 | InvalidParameter.Ba ndwidthPackage.n.IS P.ValueNotSupport | The specified ISP of BandwidthPackage is not valid. | The error message returned because the specified Internet service provider (ISP) of the EIP bandwidth plan is invalid. |
| 400 | ZONE NO AVAILABLE _ _ IP _ | The Zone have no available ip. | The error message returned because no IP address is available in the zone. |

#### 2.8.2 ModifyBandwidthPackageSpec

Modifies the bandwidth value of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidth PackageSpec | The operation that you want to perform. Set the value to Modif yBandwidt hPackageSpec. |
| Bandwidth | String | Yes | 5 | The maximum bandwidth of the NAT service plan. Valid values: 5 to 1000. |
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

#### 2.8.3 ConvertBandwidthPackage

Converts a NAT service plan to an EIP bandwidth plan. Before you convert a NAT service plan to an EIP bandwidth plan, take note of the following limits: You are not charged for the conversion. When you convert a NAT service plan to an EIP bandwidth plan, you can continue to use the SNAT and DNAT features of the NAT gateway, and your workloads are not affected. However, we recommend that you convert your NAT service plan during off-peak hours. After the NAT service plan is converted to an EIP bandwidth plan, the public IP addresses in the NAT service plan are converted to elastic IP addresses (EIPs). The maximum bandwidth and billing method of the EIP bandwidth plan are the same as those of the NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConvertBandwidt hPackage | The operation that you want to perform. Set the value to Creat eBandwidt hPackage. |
| BandwidthPackag eId | String | Yes | bwp- bp1xea10o8qxw4 f**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is created. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ConvertInstanc eId | String | cbwp- s6lmotmkkf567b**** | The ID of the EIP bandwidth plan. |
| RequestId | String | 0C2EE7A8-74D4- 4081-8236- CEBDE3BBCF50 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ConvertBandwidthPackage &BandwidthPackageId=bwp-bp1xea10o8qxw4f**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ConvertBandwidthPackageResponse>
   <RequestId>0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50</RequestId>
   <ConvertInstanceId>cbwp-s6lmotmkkf567b****</ConvertInstanceId>
</ConvertBandwidthPackageResponse>
```

`JSON` format `{`

```json
    "ConvertBandwidthPackageResponse": {
        "RequestId": "0C2EE7A8-74D4-4081-8236-CEBDE3BBCF50",
        "ConvertInstanceId": "cbwp-s6lmotmkkf567b****"
```

`}` `}`

#### 2.8.4 DescribeBandwidthPackages

Queries NAT service plans in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBandwid thPackages | The operation that you want to perform. Set the value to DescribeBandwidt hPackages. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPackag eId | String | No | bwp- bp1xea10o8qxw dfs**** | The ID of the NAT service plan. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
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
| CreationTime | String | 2017-06- 08T12:20:55 | The time when the NAT service plan was created. The time follows the ISO 8601 standard in YYYY-MM-DDThh:mmZ format. It must be in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | test123 | The description of the NAT service plan. The description must be 2 to 256 characters in length. The description is displayed in the console. This parameter is empty by default. It cannot start with http:// or https:// . |
| ISP | String | BGP | Only BGP is supported. |
| InstanceCharge Type | String | PostPaid | The billing method of the NAT service plan. Only Post Paid (pay-as-you-go) is supported. |
| InternetCharge Type | String | PayByBandwidth | The metering method of the NAT service plan. PayByT raf f ic: pay-by-data-transfer PayByBandwidt h：按带宽计费。 |
| IpCount | String | 1 | The number of public IP addresses in the NAT service plan. Valid values: 1 to 50. |
| Name | String | abc | The name of the NAT service plan. |
| NatGatewayId | String | ngw- xxoo123ggtf**** | The ID of the NAT gateway. |
| PublicIpAddress es | Array of PublicIpAddress e |   | The IP address in the NAT service plan. |
| PublicIpAddress e |   |   |   |
| AllocationId | String | eip- 2zeerraiwb7ujdeds* *** | The ID that is allocated. |
| ApAccessEnabl ed | Boolean | true |   |
| IpAddress | String | 116.XX.XX.28 | The IP address. |

| Parameter | Type | Example | Description |
|---|---|---|---|
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

#### 2.8.5 ModifyBandwidthPackageAttribute

Modifies the name and description of a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBandwidth PackageAttribute | The operation that you want to perform. Set the value to Modif yBandwidt hPackageAt t ribut e . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| BandwidthPackag eId | String | Yes | bwp- s6lmotmkk**** | The ID of the NAT service plan. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | NATABC | The name of the NAT service plan. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). The name cannot start with http:// or https:// . |
| Description | String | No | This is NAT. | The description of the NAT service plan. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |

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

#### 2.8.6 DeleteBandwidthPackage

Deletes a specified NAT service plan. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBandwidth Package | The operation that you want to perform. Set the value to Delet eBandwidt hPackage. |
| BandwidthPackag eId | String | Yes | bwp- bp1arsrmca9kp** ** | The ID of the NAT service plan. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the NAT gateway is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Force | Boolean | No | false | Specifies whether to forcibly delete the NAT service plan. f alse(default): no t rue: yes |

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

#### 2.8.7 RemoveBandwidthPackageIps

Removes public IP addresses from a NAT service plan. Description When you call this operation, take note of the following: You cannot remove all public IP addresses from a NAT service plan. You cannot remove an IP address that is not included in the specified NAT service plan. You cannot remove an IP address that is listed in the DNAT table or the SNAT table. Request parameters

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveBandwidth PackageIps | The operation that you want to perform. Set the value to RemoveBandwidthPackageIps. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the NAT service plan. You can call the DescribeRegions operation to query the most recent region list. |
| BandwidthPac kageId | String | Yes | bwp- s6lmotmkkza1w*** * | The ID of the NAT bandwidth package. |
| RemovedIpAd dresses.n | String | No | nateip- 1110a2l1ad2**** | The ID of public IP address n to be removed. n must start from 1 and cannot exceed 20. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7D275A59-1EB0- 4775-8A20- 2A47055EAC5C | The ID of the request. |

Examples Sample request s

```
https://vpc.example.com/?Action=RemoveBandwidthPackageIps &RemovedIpAddresses.1=nateip-1110a2l1ad2**** &BandwidthPackageId=bwp-s6lmotmkkza1w**** &amp;RegionId=cn-hangzhou &<Common request parameters>
```

Sample responses XML format

```xml
<? xml version="1.0" encoding="UTF-8" ? > <RemoveBandwidthPackageIpsResponse>
       <RequestId>2315DEB7-5E92-423A-91F7-4C1EC9AD97C3</RequestId>
</RemoveBandwidthPackageIpsResponse>
```

JSON format `{`

```json
     "RequestId": "2315DEB7-5E92-423A-91F7-4C1EC9AD97C3"
```

`}`
