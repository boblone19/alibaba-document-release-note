---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for Redis Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 104
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for Redis Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E6%95%B0%E6%8D%AE%E5%BA%93/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20ApsaraDB%20for%20Redis%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 ApsaraDB for Redis Developer Guide 20220928

## Table of Contents

- 1 Call Apsara Stack SDK by using ASAPI
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
  - 2.1 API overview
  - 2.2 Request structures
  - 2.3 Common parameters
  - 2.4 Responses
  - 2.5 Request signatures
  - 2.6 RAM-based authorization
    - 2.6.1 Grant resource permissions to a RAM user
    - 2.6.2 Authorized resource types in RAM
    - 2.6.3 Operation permissions granted to a RAM user
    - 2.6.4 API authentication rules
  - 2.7 Manage the lifecycle
    - 2.7.1 CreateInstance
    - 2.7.2 DeleteInstance
    - 2.7.3 ModifyInstanceSpec
  - 2.8 Manage instances
    - 2.8.1 DescribeInstanceAttribute
    - 2.8.2 DescribeInstances
    - 2.8.3 DescribeRegions
    - 2.8.4 DescribeSecurityIps
    - 2.8.5 FlushInstance
    - 2.8.6 ModifyInstanceAttribute
    - 2.8.7 ModifyInstanceMaintainTime
    - 2.8.8 ModifyInstanceNetExpireTime
    - 2.8.9 ModifySecurityIps
    - 2.8.10 SwitchNetwork
  - 2.9 Backup and recovery
    - 2.9.1 CreateBackup
    - 2.9.2 ModifyBackupPolicy
    - 2.9.3 DescribeBackupPolicy
    - 2.9.4 DescribeBackups
    - 2.9.5 RestoreInstance
  - 2.10 Manage monitoring
    - 2.10.1 DescribeMonitorItems
    - 2.10.2 DescribeHistoryMonitorValues
  - 2.11 Manage parameters
    - 2.11.1 DescribeInstanceConfig
    - 2.11.2 ModifyInstanceConfig
  - 2.12 Appendixes
    - 2.12.1 Instance specifications
    - 2.12.2 Error codes
    - 2.12.3 Instance configurations

SDK by using ASAPI

## 1 Call Apsara Stack SDK by using ASAPI

using ASAPI

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the SDK by using ASAPI Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. SDK by using ASAPI Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). SDK by using ASAPI Method 1: Use Registration Vars of Services to generate an endpoint
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
SDK by using ASAPI i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: SDK by using ASAPI

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

SDK by using ASAPI

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

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure SDK by using ASAPI
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

SDK by using ASAPI

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

SDK by using ASAPI Not e

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
Method 1: Create a Maven project in IntelliJ IDEA. SDK by using ASAPI Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure. SDK by using ASAPI
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
SDK by using ASAPI If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations: SDK by using ASAPI

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers SDK by using ASAPI

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI. SDK by using ASAPI

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

SDK by using ASAPI Configure a proxy Perform the following steps to configure a proxy:
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

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls: SDK by using ASAPI

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

SDK by using ASAPI Request headers

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

SDK by using ASAPI Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

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

SDK by using ASAPI

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

SDK by using ASAPI

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. SDK by using ASAPI Sample code:

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

SDK by using ASAPI

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. SDK by using ASAPI Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

Configure proxies SDK by using ASAPI Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. SDK by using ASAPI Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. SDK by using ASAPI Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

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

SDK by using ASAPI Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language SDK by using ASAPI `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
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
SDK by using ASAPI

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

SDK by using ASAPI
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

### 2.1 API overview

Instance lifecycle management API operations

| Operation | Description |
|---|---|
| CreateInstance | Creates an instance. |
| DeleteInstance | Releases an instance. |
| ModifyInstanceSpec | Changes the specifications of a specified instance. |

Instance management API operations

| Operation | Description |
|---|---|
| DescribeInstanceAttribute | Queries detailed information about instances. |
| DescribeInstances | Queries basic information about instances. |
| DescribeRegions | Queries available regions. |
| DescribeSecurityIps | Queries the IP whitelist that allows connections to a specified instance from specified IP addresses or CIDR blocks. |
| FlushInstance | Clears an instance. |
| ModifyInstanceAttribute | Sets the attribute for a specified instance. |
| ModifyInstanceMaintainTime | Changes maintenance time for a specified instance. |
| ModifySecurityIps | Changes the whitelist for a specified instance. |
| ModifyInstanceNetExpireTime | Changes the period for retaining a domain name of a specified classic network. |
| SwitchNetwork | Changes the type of a network. |

Backup and recovery API operations

| Operation | Description |
|---|---|
| CreateBackup | Creates a backup. |
| ModifyBackupPolicy | Changes a backup policy. |
| DescribeBackupPolicy | Queries backup policies. |

|   | Developer Guide·API reference | ApsaraDB for Redi | s |
|---|---|---|---|

| Operation | Description |
|---|---|
| DescribeBackups | Queries available backups. |
| RestoreInstance | Restore a specified instance based on a specified backup set. |

Monitoring management API operations

| Operation | Description |
|---|---|
| DescribeMonitorItems | Queries available monitoring metrics. |
| DescribeHistoryMonitorValues | Queries historical monitoring data. |

Parameter management API operations

| Operation | Description |
|---|---|
| DescribeInstanceConfig | Queries parameters of a specified instance. |
| ModifyInstanceConfig | Changes parameters of a specified instance. |

### 2.2 Request structures

Endpoint The endpoint of the KVStore for Redis API is `r-kvstore.`example.com. For more information about how to obtain an endpoint, see Generate the endpoint of ASAPI. Not e example.com is a domain name that is customized for a project. You can obtain the domain name from the administrator. Protocols You can send requests over HTTP or HTTPS. To enhance data security, we recommend that you send API requests by using HTTPS. Methods You can send requests by using the HTTP GET method. This method requires that you specify request parameters in the request URL. Request parameters You must specify the Action parameter for each request. For example, you can specify CreateInstance. You must also specify common request parameters and specific request parameters that are required by each operation. Encoding Requests and responses are both encoded in UTF-8.

### 2.3 Common parameters

Common request parameters must be included in all API requests. Common request parameters Common request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| Format | String | Yes | The type of the returned value. Valid values: JSON and XML. Default value: XML |
| Version | String | Yes | The version of the API. Specify the version in the YYYY- MM-DD format. The current version is 2015-01-01. |
| AccessKeyId | String | Yes | The AccessKey ID provided by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For example, you can set the parameter to 2016-01-01T12:00:00Z. This specifies 20:00:00, January 1, 2016, UTC+08:00. |
| SignatureVersio n | String | Yes | The version of the signature algorithm. The current version is 1.0. |
| SignatureNonce | String | Yes | The unique random number that is used to prevent replay attacks. You must use different random numbers for different requests. |

```
https:// r-kvstore.example.com/ ? Format=json &Version=2015-01-01 &Signature=Pc5xxxxxxxxxxxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2016-01-01T12:00:00Z
```

Common response parameters Each time you call an API operation, the system returns a globally unique ID (RequestId). This is regardless of whether the request is successful.

```xml
<? xml version="1.0" encoding="utf-8"? > <!-The root of the response--> <Operation name+Response> <!—The returned request tag--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The returned result--> </Operation name+Response>
```

### 2.4 Responses

After you call an API operation, KVStore for Redis returns data in the same format. In the response, an HTTP status code in the `2xx` format indicates that the call is successful. An HTTP status code in the `4xx` or `5xx` format indicates that the call failed. The system returns responses for successful calls in XML or JSON format. You can specify the response format in request parameters. The system uses the XML format by default. Not e The response examples in this topic have been formatted with line breaks or indents to provide a clear view. The responses in your actual running environments are not properly formatted as these examples. Sample success response The response in XML format includes a message that indicates whether the call is successful and the specific service data. An example is as follows:

```xml
<? xml version="1.0" encoding="utf-8"? > <!—The root node of the response--> <Operation name+Response> <!—The request ID returned--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The result data returned--> </Operation name+Response>
```

JSON format `{`

```json
"RequestId": "4C4fdsf38-3910-447D-87AD-AC078932216", /* The result data returned */
```

`}` Sample error response When an error occurs during an API call, no result data is returned. You can locate the cause of the error by referencing the attached list of error codes. If an error occurs when you call an operation over HTTP, an HTTP status code in the `4xx` or `5xx` format is returned. The returned message body includes the specific error code and error message. The message body also contains a globally unique request ID called RequestId and a target site ID called HostId. If you cannot locate the cause, request Apsara Stack customer service, and provide the HostId and RequestId for troubleshooting.

```xml
<? xml version="1.0" encoding="UTF-8"? > <Error> <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId> <HostId> r-kvstore.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error>
```

JSON format `{`

```json
"RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF", "HostId": " r-kvstore.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

### 2.5 Request signatures

KVStore for Redis authenticates each access request. You need to include a signature when you submit an HTTP or HTTPS request. KVStore for Redis authenticates the request sender identity by using symmetric encryption based on an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. An AccessKey ID and an AccessKey secret are issued to you by Alibaba Cloud. You can apply for and manage them on the Alibaba Cloud website. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to obtain the AccessKey pair, see Obtain an AccessKey pair. Sign a request Perform the following steps to sign an API request:
1. Create a canonicalized query string by using request parameters.
i. To construct a canonicalized query string, sort all request parameters by name in alphabetic order. These parameters include common request parameters and customized API request parameters. However, this does not include the Signature parameter. Not e When you use the GET method to submit requests, you specify these parameters in the request URI that follow the question mark (?) and are connected with the ampersand (&). ii. Encode the name and value of each request parameter. Perform URL encoding on the names and values by using the UTF-8 character set. The following section shows the URL encoding rules: Uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Encode other characters in the %XY format, where `XY` specifies the ASCII code of the characters in the hexadecimal format. For example, double quotation marks (") are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA format. Spaces must be encoded as %20 . Do not encode spaces as plus signs (+).

| Not e Libraries that support URL encoding, such as java.net.URLEncoder, follow the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x-www-form-u rlencoded . If this encoding method is used, replace the plus signs (+) in the encoded strings with %20 , the asterisks (*) with %2A , and %7E with a tilde (~) to conform to the encoding rules. |   |   |
|---|---|---|
|   | application/x-www-form-u |   |

| rlencoded |   |
|---|---|
|   | %20 |

iii. Connect the encoded parameter name and value with an equal sign (=). iv. Sort the key-value pairs connected by equal signs (=) in alphabetical order and separate them with ampersands (&).
2. Create a string-to-sign from the encoded canonicalized query string that is obtained in the
preceding step based on the following rules:

```
 StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

In this example, `HTTPMethod` specifies the HTTP method that is used to submit the request, such as GET. `percentEncode("/")` is the value ( %2F ) as the result of encoding the slash sign (/) based on the URL encoding rule described in Step 1.b. `percentEncode(CanonicalizedQueryString)` is the string that results from encoding the canonicalized query string described in Step 1 based on the URL encoding rules described in Step 1.b.
3. As defined in RFC 2104, use the preceding signature string to calculate the signature into an HMAC
value. Not e The key that is used for calculating the signature is your AccessKey secret followed by an ampersand (&) (ASCII:38). The SHA1 algorithm is used for the calculation.
4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.
Not e When you submit the signature string to the KVStore for Redis instance as the final request parameter value, perform URL encoding on this parameter based on RFC 3986 rules. This is the same method that is used to process other parameters. Example DescribeDrdsInstances is used in this example. The following section shows the canonicalized query string:

```
http://r-kvstore.example.com/?Timestamp=2013-06-01T10:33:56Z&Format=XML&AccessKeyId=testid& Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDAxvLU 6tFE0DVb&Version=2015-01-01&SignatureVersion=1.0
```

The following section shows the calculated StringToSign:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeInstances&Format%3DXML&RegionId%3Dregion1&Sig natureMethod%3DHMAC-SHA1&SignatureNonce%3DNwDAxvLU6tFE0DVb&SignatureVersion%3D1.0&Timestamp %3D2013-06-01T10%253A33%253A56Z&Version%3D2015-01-01
```

| In this example, if the AccessKey ID is testid used for HMAC calculation is testsecret& . T BIxxxxxxxxxxxxxxxxxxxxxx= . | testid |
|---|---|
| BIxxxxxxxxxxxxxxxxxxxxxx= |   |

In this example, if the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the key The following section shows the signed request URL that includes the Signature parameter:

```
http://r-kvstore.example.com/?Timestamp=2013-06-01T10%3A33%3A56Z&Format=XML&AccessKeyId=tes tid&Action=DescribeInstances&SignatureMethod=HMAC-SHA1&RegionId=region1&SignatureNonce=NwDA xvLU6tFE0DVb&SignatureVersion=1.0&Version=2015-01-01&Signature=BIPOMlxxxxxxxxxxxxxxxxxxu8LX BeZtLQkJTw6iFvw1E%3D
```

### 2.6 RAM-based authorization

#### 2.6.1 Grant resource permissions to a RAM user

The instances that you create by using your Alibaba Cloud account are the resources owned by the account. An account has the full operation permissions on the resources under this account by default. Alibaba Cloud Resource Access Management (RAM) allows you to grant the access and management permissions on resources under a cloud account to RAM users. Not e Ignore this topic if you do not use Resource Access Management (RAM).

#### 2.6.2 Authorized resource types in RAM

KVStore for Redis only supports RAM authorization for Redis instances. The following table lists the description of resources when you use RAM to authorize access permissions to these resources.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:kvstore:$regionid:$accountid:instance/$instanc eid acs:kvstore:$regionid:$accountid:instance/ acs:kvstore:::instance/ |

All $regionids must be the ID of a region or an asterisk ( `*` ). All $instanceids must be the ID of an instance or an asterisk ( `*` ). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk ( `*` ).

#### 2.6.3 Operation permissions granted to a RAM user

user You are authorized to call the following API operations to manage the specified resource as a Resource Access Management (RAM) user: RenewInstance RenewMultiInstance TransformToPrePaid

#### 2.6.4 API authentication rules

When you use API operations to access resources as a Resource Access Management (RAM) user, the system queries the RAM service and checks whether the RAM user is granted the required permissions. Each API operation determines the resources for permission check according to the involved resources and the semantics of the API operation. The following table lists the authentication rules corresponding to different API operations. Authentication rules

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DeleteInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceSpec | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RenewInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RenewMultiInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| TransformToPrePaid | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| FlushInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstances | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceMaintainTime | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifySecurityIps | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| SwitchNetwork | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceNetExpireTime | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| CreateBackup | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$instanc eid |

| eveloper Guide·API reference | ApsaraDB for Redi |
|---|---|
| Operation | Authentication rule |
| DescribeBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeBackups | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| RestoreInstance | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeHistoryMonitorValues | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| DescribeInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$instanc eid |
| ModifyInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$instanc eid |

### 2.7 Manage the lifecycle

#### 2.7.1 CreateInstance

You can call this operation to create an instance. For more information, see Instance specifications. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateInstance. |

| Parameter | Type |   |   | Required |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| InstanceName | String |   |   | No |   | The name of the instance. The name must be 2 to 128 characters in length and must start with a letter. The name cannot contain special characters or spaces. Special characters include @ / : = ” < > { } [ ] |   |   |   |   |
| Password | String |   |   | No |   | The password of the instance. The password must be a string of 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. Not e Special characters are not supported, such as ! < > ( ) [ |   |   |   |   |
|   |   |   |   |   |   |   | Not e Special characters are not supported, such as ! < > ( ) [ |   |   |   |
|   |   |   |   |   |   |   |   | ! < > ( ) [ |   |   |
|   |   |   |   |   |   |   | ] { } , ` ~ . - |   |   |   |
|   |   |   |   |   |   |   | @ # $ % ^ & * _ |   |   |   |
| InstanceClass | String |   |   | Yes |   | The type of the requested KVStore for Redis instance. For more information, see Instance specifications. |   |   |   |   |
| RegionId | String |   |   | Yes |   | The region ID of the instance. You can query available data regions by calling the DescribeRegions operation. |   |   |   |   |
| ZoneId | String |   |   | No |   | The zone ID of the instance. You can call DescribeRegions to view available zones. |   |   |   |   |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ChargeType | String | No | The billing method of the instance. Valid values: PrePaid and PostPaid. Default value: PostPaid. |
| Period | Long | No | The billing period of the instance. If you set the ChargeType parameter to PrePaid, you must also specify the Period parameter. Unit: month. Valid values: 1-9, 12, 24, and 36. |
| Token | String | No | The client token that is used to ensure the idempotence of requests. The value of this parameter is generated by the client and must be unique among different requests. The value is case-sensitive and can be up to 64 ASCII characters in length. For more information, see How to ensure idempotence. |
| NetworkType | String | No | The type of the network. Default value: Classic. Valid values: Classic VPC |
| VpcId | String | No | The ID of the VPC to which the instance belongs. |
| VSwitchId | String | No | The ID of the VSwitch. |
| PrivateIp | String | No | The private IP address of the instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SrcDBInstanceId | String | No | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the instance that generates the backup set. |
| BackupId | String | No | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the generated backup set. You can call DescribeBackups to query the value of BackupId. |
| InstanceType | String | No | The category of the instance. Valid values: Redis and Memcache. Default value: Redis. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| InstanceId | String | The ID of the instance, which is globally unique. |
| InstanceName | String | The name of the instance. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields as needed in the future. Sample requests

```
https://r-kvstore.example.com ? <Common request parameters> &Action=CreateInstance &RegionId=cn-hangzhou &Password=Qa123456 &InstanceClass= redis.master.small.default
```

Sample responses `{`

```json
"InstanceId":"73xxxxxxxxxxx", "InstanceName":"73xxxxxxxxxxx"
```

`}`

#### 2.7.2 DeleteInstance

You can call this operation to delete a specified instance. This instance that you want to release must be in the following status: The instance is in the running state. The instance is not locked. Not e You cannot delete a subscription instance until the instance expires. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DeleteInstance. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DeleteInstance &InstanceId=657xxxxxxxxxxxxx
```

Sample response `{`

```json
"RequestId" : "C2225574-1D93-4F8A-B1D5-39FCBAA40660"
```

`}`

#### 2.7.3 ModifyInstanceSpec

You can call this operation to change the specifications of a specified instance. For more information about instance specifications, see Instance types. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceSpec. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| InstanceClass | String | Yes | The type of the specified instance. For more information, see Instance types. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common request parameters> | - | For more information, see Common parameters. |

| Developer Guide·API reference |   | ApsaraDB for Redi |
|---|---|---|

| Parameter | Type | Description |
|---|---|---|
| OrderId | String | The ID of the order that you have placed. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=ModifyInstanceSpec &InstanceId=736538d0a6894665 &InstanceClass= redis.master.mid.default
```

Sample response `{`

```json
"OrderId" : "201294900260011" "RequestId" : "283746AF-82B3-4BFF-88CC-BF34CDE2732"
```

`}`

### 2.8 Manage instances

#### 2.8.1 DescribeInstanceAttribute

You can call this operation to query details of a specified instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common requests. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeInstanceAttribu te. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| Instances | List | The array that contains the DBInstanceAttribute values. |

DBInstanceAttribute parameters

| Parameter | Type | Description |
|---|---|---|
| InstanceId | String | The globally unique ID of the instance that was queried. |
| InstanceName | String | The name of the instance that was queried. |
| Capacity | Long | The capacity that you have requested for the instance that was queried, in MB. |
| InstanceClass | String | The type of the instance that was queried. |
| Bandwidth | Long | The bandwidth limit of the instance that was queried, in Mbit/s. |
| Connections | Long | The maximum number of connections to the instance that was queried. |
| ConnectionDomain | String | The domain name of the instance that was queried. This domain name only supports connections over an internal network. |
| Port | Int | The port of the instance that was queried. |
| RegionId | String | The region where the instance that was queried was located. For more information, see DescribeRegions. |
| ZoneId | String | The ID of the zone under the RegionId of the instance that was queried. For more information, see DescribeRegions. |

| Parameter | Type | Description |   |   |
|---|---|---|---|---|
| InstanceStatus | String | The status of the instance that was queried. Possible values: Normal: the instance that was queried was normal. Creating: the instance that was queried was being created. Changing: the instance that was queried was being changed. Inactive: the instance that was queried was disabled. |   |   |
| ChargeType | String | The billing method of the instance that was queried. Possible values: PrePaid and PostPaid. |   |   |
| CreateTime | String | The time when the instance that was queried was created. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
|   |   |   | YYYY-MM- |   |
| EndTime | String | The time when the subscription instance that was queried was about to expire. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
| NetworkType | String | The type of the network where the instance that was queried was located. Possible values: CLASSIC or VPC. |   |   |
| VpcId | String | The ID of the VPC where the instance that was queried was located. |   |   |
| VSwitchId | String | The ID of the VSwitch for the instance that was queried. |   |   |
| PrivateIpAddress | String | The private IP address of the instance that was queried. |   |   |

|   | DDThh:mm:ssZ |
|---|---|

| Parameter | Type | Description |
|---|---|---|
| MaintainStartTime | String | The time when maintenance can be started. |
| MaintainEndTime | String | The time when maintenance can be ended. |
| SecurityIPList | String | The IP whitelist for the instance that was queried. |
| AvailabilityValue | String | The availability metrics of the current month for the instance that was queried. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields as needed in the future. In this case, do not rely on the returned fields that this topic has not described when you call this operation. Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeInstanceAttribute &InstanceId=7xxxxxxxxxxx
```

Sample response `{` `{`

```json
    "Instances" : {
        " DBInstanceAttribute " : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d004211.m.cnhzalicm10pub001.r-kvstore.exampl
e.com.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "dexxxxxxxxxx",
                "InstanceName" : "xxxxxx",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "QPS" : 4500,
                "RegionId" : "cn-qingdao",
                 "ChargType":"PostPaid",
                  "NetworkType":"ClASSSIC"
                "MaintainStartTime": "02:00Z",
                 "MaintainEndTime": "06:00Z",
                 "SecurityIPList":"192.168.0.1",
                  "AvailabilityValue":"100%"
```

`}]` `}`

```json
"RequestId" : "283746AF-82B3-4BFF-88CC-BF34CDE2732"
```

`}`

#### 2.8.2 DescribeInstances

You can call this operation to query one or more instances under a specified account. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | - | See Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeInstances. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceIds | String | No | The globally unique ID of the target instance. This parameter is required when you specify an instance ID. To query multiple instances, separate the identifiers of these instances with commas (,). If the parameter value is left blank, the system queries all instances under the specified account by default. |
| InstanceStatus | String | No | The instance status of the specified instance: Valid values: Normal: the specified instance is normal. Creating: the specified instance is being created. Changing: the specified instance is being changed. Inactive: the specified instance is disabled. |
| ChargeType | String | No | The billing method of the specified instance. Valid values: PrePaid: the subscription billing method. PostPaid: the pay-as- you-go billing method. |
| RegionId | String | Yes | You can call the DescribeRegions operation to query the RegionId value. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceType | String | No | The type of the engine for the specified instance. Valid values: Memcache: specifies an instance of Memcache type. Redis: specifies an instance of Redis type. |
| PageNumber | Integer | No | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |
| NetworkType | String | No | The type of the network where the specified instance is located. Valid values: CLASSIC: specifies an instance in a classic network. VPC: specifies an instance in a VPC. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| Instances | List | The array that contains the instances that were queried. |
| TotalCount | Integer | The total number of instances that were queried. |
| PageNumber | Integer | The number of the page returned. |
| PageSize | Integer | The number of entries returned on each page. |

Instance parameters

| Parameter | Type | Description |
|---|---|---|
| InstanceId | String | The globally unique ID of the instance that was queried. |
| InstanceName | String | The name of the instance that was queried. |
| Capacity | Long | The capacity that you have requested for the instance that was queried, in MB. |
| InstanceClass | String | The type of the instance that was queried. |
| Bandwidth | Long | The bandwidth limit of the instance that was queried, in Mbit/s. |
| Connections | Long | The maximum number of connections to the instance that was queried. |
| ConnectionDomain | String | The domain name of the instance that was queried. This domain name only supports connections over an internal network. |
| Port | Int | The port of the instance that was queried. |
| UserName | String | The username of the instance that was queried. |
| RegionId | String | The region where the instance that was queried was located. |
| ZoneId | String | The ID of the zone under the RegionId of the instance that was queried. |

| Parameter | Type | Description |   |   |
|---|---|---|---|---|
| InstanceStatus | String | The status of the instance that was queried. Possible values: Normal: the instance that was queried was normal. Creating: the instance that was queried was being created. Changing: the instance that was queried was being changed. Inactive: the instance that was queried was disabled. Transforming: the instance that was queried was being transformed. BackupRecovering: the instance that was queried was being backed up and restored. MinorVersionUpgrading: the minor version of the instance that was queried was being upgraded. |   |   |
| ChargeType | String | The billing method of the instance that was queried. Possible values: PrePaid and PostPaid. |   |   |
| CreateTime | String | The time when the instance that was queried was created. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
|   |   |   | YYYY-MM- |   |
| EndTime | String | The time when the subscription instance that was queried was about to expire. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC time format. |   |   |
| NetworkType | String | The type of the network where the instance that was queried was located. Possible values: CLASSIC or VPC. |   |   |

|   | DDThh:mm:ssZ |
|---|---|

| Parameter | Type | Description |
|---|---|---|
| VpcId | String | The ID of the VPC where the instance that was queried was located. |
| VSwitchId | String | The ID of the VSwitch for the instance that was queried. |
| PrivateIpAddr | String | The private IP address of the instance that was queried. |

Not e Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config for the operation. Alibaba Cloud will delete these fields as needed in the future. In this case, do not rely on the returned fields that this topic has not described when you call this operation. Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeInstances &PageNumber=1 &PageSize=10 &InstanceId=dexxxxxxxxxx1
```

Sample response `{`

```json
    "Instances" : {
        "Instance" : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d004211.m.cnhzalicm10pub001.r-kvstore.exampl
e.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "dexxxxxxxxxx1",
                "InstanceName" : "xxxxxx",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "RegionId" : "cn-qingdao",
                "UserName" : "xxxxxxxxxx"
                "NetworkType":"CLASSSIC"
"ChargeType":" PostPaid"
```

`}` `]` `},`

```json
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
    "RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
```

`}`

#### 2.8.3 DescribeRegions

You can call this operation to query regions where you can create instances. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeRegions. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| RegionIds | List | The RegionIds parameter is a list. Every element in this list consists of the RegionId and ZoneIds. ZoneIds is a string, and multiple ZoneId values are separated with commas (,). |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeRegions
```

Sample response `{`

```json
    "RequestId":"535A88D3-5408-4B29-AFD4-07319D97EBC4",
    "RegionIds":
```

`{` `{`

```json
                "ZoneIds":"cn-qingdao-b",
                "RegionId":"cn-qingdao",
```

`},` `{`

```json
                "ZoneIds":"cn-shenzhen-a",
                "RegionId":"cn-shenzhen",
```

`},` `{`

```json
                "ZoneIds":"cn-hangzhou-d,cn-hangzhou-b",
                "RegionId":"cn-hangzhou"
```

`},` `{`

```json
                "ZoneIds":"cn-beijing-a",
                "RegionId":"cn-beijing"
```

`}` `}` `}`

#### 2.8.4 DescribeSecurityIps

You can call this operation to query the list of IP addresses or CIDR blocks that you can use to connect to an instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeSecurityIps. |
| InstanceId | String | Yes | The name of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| SecurityIpGroups | List | The list of whitelisted IP addresses or CIDR blocks for the instance that was queried. |

SecurityIpGroups parameters SecurityIpGroups parameters

| Parameter | Type | Description |
|---|---|---|
| SecurityIpGroupName | String | The name of the IP whitelist that was queried. |

| Parameter | Type | Description |   |
|---|---|---|---|
| SecurityIpList | String | The list of whitelisted IP addresses or CIDR blocks that were queried. A maximum of 1,000 IP addresses or CIDR blocks are displayed. IP addresses or CIDR blocks are separated with commas (,), such as 0.0.0.0/0,10.23.12.24 (IPv4 addresses) or 10.23.12.24/24 (Classless Inter-Domain Routing or CIDR notation). In the CIDR notation, 10.23.12.24 represents the IPv4 address 10.23.12.24. Its subnet mask is 255.255.255.0. The slash (/) and the following number 24 represent 24 leading 1 bits in the subnet mask and its associated routing prefix. The length of the routing prefix ranges from 1 to 32. |   |

Sample request

```
https://r-kvstore.example.com/ ? <Common request parameters> &Action= DescribeSecurityIps &InstanceId=6xxxxxxxxxxxxxx
```

Sample response `{`

```
" SecurityIpGroups " : { " SecurityIpGroup" : [{ " SecurityIpGroupName" : "ipsecuritytest" , " SecurityIpList " : "10.xx.xx. 24"
```

`}` `]` `},`

```json
"RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
```

`}`

#### 2.8.5 FlushInstance

You can call this operation to clear data stored on an instance. The cleared data cannot be restored. This is an asynchronous operation. After you call this operation, the system returns the result immediately. The system clears data in the background. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | - | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to FlushInstance. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= FlushInstance &InstanceId=65xxxxxxxx
```

Sample response `{`

```json
"RequestId" : "96893674-E50C-495D-AB0E-2F12C1E0FD45"
```

`}`

#### 2.8.6 ModifyInstanceAttribute

You can call this operation to modify attributes of an instance, such as the name or the password of the instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | - | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceAttribute . |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| InstanceName | String | No | The instance name that you want to change to. The name must be a string of 2 to 128 characters in length and must start with an uppercase or lowercase letter or Chinese character. Special characters, such as at signs (@), slashes (/), colons (:), equal signs (=), quotation marks ("), angle brackets (<>), braces ({}), brackets ([]), and spaces, are not supported. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| NewPassword | String | No | The password of the specified instance. The password must be a string of 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and numbers. Not e Special characters, such as exclamation points (!), angle brackets (<>), parentheses (()), brackets ([]), braces ({}), commas (,), backticks (`), tildes (~), periods (.), hyphens (-), underscores ( ), at _ signs (@), number signs (#), dollar signs ($), percent signs (%), carets (^), ampersands (&), and asterisks (*), are not supported. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyInstanceAttribute &InstanceId=65xxxxxxxxxx &NewPassword=Qa12345678 &InstanceName=TestInstance
```

Sample response `{`

```json
"RequestId" : "E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59"
```

`}`

#### 2.8.7 ModifyInstanceMaintainTime

You can call this operation to modify maintenance time for an instance. Alibaba Cloud may perform routine maintenance for the instance during the specified maintenance time. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceMaintain Time. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| MaintainStartTime | String | Yes | The start time of the maintenance to be performed. |
| MaintainEndTime | String | Yes | The end time of the maintenance to be performed. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=ModifyInstanceMaintainTime &InstanceId=65xxxxxxxxx & MaintainStartTime=02:00Z & MaintainEndTime=06:00Z
```

Sample response `{`

```json
"RequestId" : "A099747A-0826-499D-9422-381C07337F73"
```

`}`

#### 2.8.8 ModifyInstanceNetExpireTime

You can call this operation to prolong the maximum period where the IP address in a classic network is retained if you switch an instance from the classic network to a Virtual Private Cloud (VPC) and retain the IP address in the classic network. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceNetExpir eTime. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| ConnectionString | String | Yes | The domain name of the specified classic network. |
| ClassicExpiredDays | String | Yes | The maximum number of days where the IP address in a specified classic network is retained. Valid values: 14, 30, 60, and 120. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyInstanceNetExpireTime &ConectionString= fdafas32323ed.redis.rds.aliyuncs.com &InstanceId=fdxxxxxxxxxx & ClassicExpiredDays=120
```

Sample response `{`

```json
"RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E46ACF"
```

`}`

#### 2.8.9 ModifySecurityIps

You can call this operation to set the IP whitelist for an instance, so that only authorized ECS IP addresses or CIDR blocks can be used to connect to the instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifySecurityIps. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| SecurityIps | String | Yes | The list of whitelisted IP addresses or CIDR blocks that you want to modify. |
| SecurityIpGroupName | String | Yes | The name of the specified whitelist group. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifySecurityIps &InstanceId=65xxxxxxxxxxx &SecurityIps=1.x.x. 1,2.x.x. 2 &SecurityIpGroupName=testgroup
```

Sample response `{`

```json
"RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E46ACF"
```

`}`

#### 2.8.10 SwitchNetwork

You can call this operation to switch the network type of an instance. You can switch an instance from a classic network to a Virtual Private Cloud (VPC). Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to SwitchNetwork. |
| InstanceId | String | Yes | The globally unique ID of the specified instance. |
| TargetNetworkType | String | Yes | The type of the network that you want to switch to. VPC Classic You can only switch from a classic network to a VPC. In this case, set this parameter to VPC. |
| VpcId | String | No | The ID of the VPC that you want to switch to. |
| VSwitchId | String | No | The ID of the VSwitch ID for the VPC that you want to switch to. This parameter is required if you have set VpcId. |
| RetainClassic | String | No | Specifies whether to retain the IP address in the classic network. Valid values: True: the classic network IP address is retained. False: the classic network IP address is not retained. Default value: False. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| ClassicExpiredDays | String | No | The maximum number of days where the IP address in the classic network are retained. Unit: days. Valid values: 14, 30, 60, and 120. This parameter is required if you have set RetainClassic to True. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= SwitchNetwork &InstanceId=fdaxxxxxxxxxx & TargetNetworkType=VPC &VpcId=fadsfa &VSwitchId=131ed &RetainClassic=True &ClassicExpiredDays=30
```

Sample response `{`

```json
"RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E46ACF"
```

`}`

### 2.9 Backup and recovery

#### 2.9.1 CreateBackup

You can call this operation to create a backup. This is an asynchronous operation. After you call this operation, the system returns the result immediately. The system creates the backup in the background. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to CreateBackup. |
| InstanceId | String | Yes | The ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= CreateBackup &InstanceId= de5d8xxxxxxxxxx
```

Sample response `{`

```json
"RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7"
```

`}`

#### 2.9.2 ModifyBackupPolicy

You can call this operation to modify a backup policy. Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set the value to ModifyBackupPolicy. |
| InstanceId | String | Yes | The ID of the instance to which the backup file belongs. |
| PreferredBackupTime | String | Yes | The period of time to execute backup. Specify the time in the HH:mmZ-HH:mmZ format. |
| PreferredBackupPeriod | String | Yes | The period of data backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample requests

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyBackupPolicy &InstanceId= de5xxxxxxxxxx &PreferredBackupTime=00:00Z-04:00Z &PreferredBackupPeriod= Saturday
```

Sample responses `{`

```json
"RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7”
```

`}`

#### 2.9.3 DescribeBackupPolicy

You can call this operation to query a backup policy that you have specified. You can query the backup details of an instance, such as the backup cycle and backup time. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeBackupPolicy. |
| InstanceId | String | Yes | The ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| BackupRetentionPeriod | String | The maximum number of days where backups of the specified instance were retained. |
| PreferredBackupTime | String | The time of the backup for the specified instance in the HH:mmZ-HH:mm Z format. |

| Parameter | Type | Description |
|---|---|---|
| PreferredBackupPeriod | String | The backup cycle for the specified instance. Possible values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| PreferredNextBackupTime | String | The time of the next backup for the specified instance. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeBackupPolicy &InstanceId= de5d8xxxxxxxxxxxxxx
```

Sample response `{`

```json
"BackupRetentionPeriod":"7" "PreferredBackupTime":"06:00Z-07:00Z" "PreferredNextBackupTime":"2017-10-19T06:16Z" "PreferredBackupPeriod":"Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday" "RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7"
```

`}`

#### 2.9.4 DescribeBackups

You can call this operation to query the details of a backup file, such as the backup start time, file size, backup mode, and download address. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set the value to DescribeBackups. |
| InstanceId | String | Yes | The ID of the instance to which the backup file belongs. |
| BackupId | String | No | The ID of the backup set. |
| PageSize | String | Yes | The number of entries to return on each page. Valid values: 30, 50, and 100. |
| PageNumber | String | Yes | The number of the page to return. Valid values: any non-zero positive integer. |
| StartTime | String | Yes | The beginning of the time range to query. |
| End time. | String | Yes | The end of the time range to query. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| Backups | List | An array consisting of Backup data. |
| PageNumber | Integer | The number of the returned page. |
| TotalCount | Integer | The total number of backups. |
| PageSize | Integer | The number of entries returned on each page. |

Backup parameter structure Backup parameter structure

| Parameter | Type | Description |
|---|---|---|
| BackupId | String | The ID of the backup set. |
| BackupDBNames | String | The name of the database that is backed up. |
| BackupStatus | String | The status of the backup set. Success Failed |
| BackupStartTime | String | The beginning of the time range where the data was backed up. |
| BackupEndTime | String | The end of the time range where the data was backed up. |
| BackupType | String | The type of the backup. Valid values: FullBackup IncrementalBackup |
| BackupMode | String | The mode of the backup. Valid values: Automated Manual |
| BackupMethod | String | The method of the backup. Valid values: Logical Physical |
| BackupDownloadURL | String | The download URL of the backup file. |
| BackupSize | String | The size of the backup set. |

Sample requests

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeBackups &InstanceId= de5xxxxxxxxxxxxx &PageNumber=1 &PageSize=10 &InstanceId=de5xxxxxxxxxxxxx
```

Sample responses `{` `{`

```json
    " Backups " : {
        "Backup " : [{
           “BackupId":"111111111"，
           "BackupDBNames":"all"，
          "BackupStatus":"Success",
         "BackupType":"FullBackup",
"BackupStartTime":"2017-10-18T10:34:52Z"， "BackupEndTime":"2017-10-18T10:36:06Z"， "BackupMode":"Manual"， "BackupMethod":"Physical"， "BackupDownloadURL":"https://rdsxxx-st-v2.oss-cn-shenzhen.example.com/custins11111111/xxxxx xxxx_data_20171018183408.rdb"， "BackupSize":"1024"
```

`}` `]` `},`

```json
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
"RequestId" : "5C97648D-C85F-4D58-A71F-7111111111117"
```

`}`

#### 2.9.5 RestoreInstance

You can call this operation to restore data to a primary instance based on a backup set. Not e Calling this operation will cause overwriting data on the specified instance with backup data. Proceed with caution. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to RestoreInstance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| InstanceId | String | Yes | The ID of the specified instance. |
| BackupId | String | Yes | Backup set ID |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= RestoreInstance &InstanceId= de5dxxxxxxxxxxxx &BackupId=fdaxxxxxx
```

Sample response `{`

```json
"RequestId" : "AFA391BF-808F-4DA6-80A2-A382108A0945"
```

`}`

### 2.10 Manage monitoring

#### 2.10.1 DescribeMonitorItems

You can call this operation to query available monitoring metrics. The result is returned in the <parameter:unit> format. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |

| psaraDB for Redis |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Parameter | Type | Required | Description |
|---|---|---|---|
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeMonitorItems. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| MonitorItems | List | The list of monitoring metrics that were queried. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action=DescribeMonitorItems
```

Sample response `{`

```json
    "MonitorItems" : {
        "MonitorItem" : [{
                "MonitorKey" : "GetQ",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "Flush",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "UsedMemCache",
                "Unit" : "Bytes"
            }, {
                "MonitorKey" : "ReplaceQ",
                "Unit" : "Counts/s"
```

`}` `]` `},`

```json
    "RequestId" : "B906A893-58A3-4644-AC2D-A2C9B08706C1"
```

`}`

#### 2.10.2 DescribeHistoryMonitorValues

You can call this operation to query historical monitoring data of an instance. Request parameters Request parameters

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| <Common request parameters> | - | Yes |   | For more information, see Common parameters. |   |   |
| Action | String | Yes |   | The operation that you want to perform. Set this parameter to DescribeHistoryMonitorV alues. |   |   |
| InstanceId | String | Yes |   | The ID of the specified instance. |   |   |
| StartTime | String | Yes |   | The beginning of the time range where the historical monitoring data is queried. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC time format. |   |   |
|   |   |   |   |   | YYYY- |   |
|   |   |   |   | MM-DDThh:mm:ssZ |   |   |
| EndTime | String | Yes |   | The end of the time range where the historical monitoring data is queried. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC time format. The value of EndTime must be greater than or equal to that of StartTime. |   |   |
|   |   |   |   |   | YYYY- |   |
|   |   |   |   | MM-DDThh:mm:ssZ |   |   |
| IntervalForHistory | String | Yes |   | The interval for collecting monitoring data. Monitoring samples were collected every N minutes. Valid values: 01m, 05m, 15m, and 60m. |   |   |

| Parameter | Type | Required | Description |
|---|---|---|---|
| MonitorKeys | String | No | The key of the specified metric. You can call the DescribeMonitorItems operation to query the value of this parameter. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |
| MonitorHistory | String | The monitoring data returned in the JSON format. For more information, see DescribeMonitorItems. Not e To improve the data transmission efficiency, only metrics whose values are not 0 have been returned. All metrics that are not displayed have been set to the default value 0. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeHistoryMonitorValues &InstanceId= de5xxxxxxxxxxxx &EndTime=2014-11-27T12%3A02%3A00Z &StartTime=2014-11-27T12%3A00%3A00Z &IntervalForHistory=01m
```

Sample response `{`

```json
"MonitorHistory" : "{"2014-11-27T12:00:00Z":{"IsConnectControl":false,"IsFlowControl":false,"ItemCount":1,"Quo taConnection":500,"QuotaFlow":15360,"QuotaMemCache":1073741824,"QuotaQps":9000,"UsedMemCach e":14}, "2014-11-27T12:01:00Z":{"IsConnectControl":false,"IsFlowControl":false,"ItemCount":1,"Quota Connection":500,"QuotaFlow":15360,"QuotaMemCache":1073741824,"QuotaQps":9000,"UsedMemCache" :14}, "2014-11-27T12:02:00Z":{"IsConnectControl":false,"IsFlowControl":false,"ItemCount":1,"Quota Connection":500,"QuotaFlow":15360,"QuotaMemCache":1073741824,"QuotaQps":9000,"UsedMemCache" :14} }", "RequestId" : "5C97648D-C85F-4D58-A71F-7B6750856BF7"
```

`}`

### 2.11 Manage parameters

#### 2.11.1 DescribeInstanceConfig

You can call this operation to query parameters of an instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to DescribeInstanceConfig. |
| InstanceId | String | Yes | The ID of the specified instance. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

| Parameter | Type | Description |
|---|---|---|
| Config | String | The parameters of the specified instance that was queried. For more information, see Instance configurations. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= DescribeInstanceConfig &InstanceId= de5dxxxxxxxxxxxx
```

Sample response `{`

```json
"Config":"{"EvictionPolicy":"volatile-lru","hash-max-ziplist-entries":512, "hash-max-ziplist-value":64,"list-max-ziplist-entries":512, "list-max-ziplist-value":64,"set-max-intset-entries":512, "zset-max-ziplist-entries":128,"zset-max-ziplist-value":64}, "RequestId":"59A58517-F8FF-44E5-B90F-F386DB3E4AB8"
```

`}`

#### 2.11.2 ModifyInstanceConfig

You can call this operation to modify a parameter of an instance. Request parameters Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| <Common request parameters> | - | Yes | For more information, see Common parameters. |
| Action | String | Yes | The operation that you want to perform. Set this parameter to ModifyInstanceConfig. |
| InstanceId | String | Yes | The ID of the specified instance. |

| Parameter | Type | Required | Description |
|---|---|---|---|
| Config | String | Yes | The parameter of the specified instance that you want to modify. The value of this parameter must be in the JSON string format. For more information, see Instance configurations. |

Response parameters Response parameters

| Parameter | Type | Description |
|---|---|---|
| <Common response parameters> | - | For more information, see Common parameters. |

Sample request

```
https://r-kvstore.example.com ? <Common request parameters> &Action= ModifyInstanceConfig &InstanceId= de5xxxxxxxxxxxx &Config={"hash-max-ziplist-entries":"512"}
```

Sample response `{`

```json
"RequestId":"59A58517-F8FF-44E5-B90F-F386DB3E4AB8"
```

`}`

### 2.12 Appendixes

#### 2.12.1 Instance specifications

KVStore for Redis provides instances of Community Edition and performance-enhanced instances of Enhanced Edition. These instance types support the standard architecture and the cluster architecture. This topic describes the specifications of different instance types, such as the memory capacity, maximum number of connections, and maximum bandwidth value. Calculation rules for bandwidth values If network resources are sufficient, bandwidth is unlimited. However, if network resources are insufficient, the bandwidth is limited. The upper limit of the total bandwidth for a read/write splitting instance is 2,048 MB/s. After the upper limit is reached, the bandwidth cannot be increased even if you add more shards or nodes. The bandwidth value applies to the upstream and downstream bandwidths. For example, if the bandwidth of an instance is 10 MB/s, the upstream and downstream bandwidths of the instance are both 10 MB/s. The bandwidth in the preceding table is the internal bandwidth of the ApsaraDB for Redis instance. The Internet bandwidth is determined by the internal bandwidth and is limited by the bandwidth of the connection between the instance and a client. We recommend that you use an internal network to maximize the performance of the instance. Performance-enhanced instances of KVStore for Redis Enhanced Edition (Tair) Standard master-replica instances

| Specification | Specification code | Number of I/O threads | Number of connectio ns per second | Maximum number of concurren t connectio ns | Total maximum bandwidt h value (MB/s) |
|---|---|---|---|---|---|
| 1 GB master- replica performance- enhanced instance | redis.amber.master.small.mul tithread | 6 | 10000 | 30000 | 96 |
| 2 GB master- replica performance- enhanced instance | redis.amber.master.mid.multit hread | 6 | 10000 | 30000 | 96 |
| 4 GB master- replica performance- enhanced instance | redis.amber.master.stand.mul tithread | 6 | 10000 | 30000 | 96 |
| 8 GB master- replica performance- enhanced instance | redis.amber.master.large.mult ithread | 6 | 10000 | 30000 | 96 |
| 16 GB master- replica performance- enhanced instance | redis.amber.master.2xlarge.m ultithread | 6 | 10000 | 30000 | 96 |
| 32 GB master- replica performance- enhanced instance | redis.amber.master.4xlarge.m ultithread | 6 | 10000 | 30000 | 96 |

| Specification | Specification code | Number of I/O threads | Number of connectio ns per second | Maximum number of concurren t connectio ns | Total maximum bandwidt h value (MB/s) |
|---|---|---|---|---|---|
| 64 GB master- replica performance- enhanced instance | redis.amber.master.8xlarge.m ultithread | 6 | 10000 | 30000 | 96 |

Cluster instances

| Specification | Specification code | Num ber of I/O thre ads | Num ber of shar ds | Num ber of prox y serv ers | Num ber of con nect ions per seco nd | Maxi mu m num ber of conc urre nt con nect ions | Maxi mu m ban dwi dth valu e per shar d | Tot al maxi mu m ban dwi dth valu e (MB/ s) |
|---|---|---|---|---|---|---|---|---|
| 2 GB cluster performance- enhanced instance (2 shards) | redis.amber.logic.shar ding.1g.2db.0rodb.6p roxy.multithread | 6 | 2 | 4 | 500 00 | 600 00 | 96 | 192 |
| 4 GB cluster performance- enhanced instance (2 shards) | redis.amber.logic.shar ding.2g.2db.0rodb.6p roxy.multithread | 6 | 2 | 4 | 500 00 | 500 00 | 96 | 192 |
| 8 GB cluster performance- enhanced instance (4 shards) | redis.amber.logic.shar ding.2g.4db.0rodb.12 proxy.multithread | 6 | 4 | 4 | 500 00 | 120 000 | 96 | 384 |
| 16 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.shar ding.2g.8db.0rodb.24 proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 32 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.shar ding.4g.8db.0rodb.24 proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |

| Specification | Specification code | Num ber of I/O thre ads | Num ber of shar ds | Num ber of prox y serv ers | Num ber of con nect ions per seco nd | Maxi mu m num ber of conc urre nt con nect ions | Maxi mu m ban dwi dth valu e per shar d | Tot al maxi mu m ban dwi dth valu e (MB/ s) |
|---|---|---|---|---|---|---|---|---|
| 64 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.shar ding.8g.8db.0rodb.24 proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 32 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.shar ding.2g.16db.0rodb.4 8proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 64 GB cluster performance- enhanced (16 shards) | redis.amber.logic.shar ding.4g.16db.0rodb.4 8proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 128 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.shar ding.8g.16db.0rodb.4 8proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 256 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.shar ding.16g.16db.0rodb. 48proxy.multithread | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 512 GB cluster performance- enhanced instance (32 shards) | redis.amber.logic.shar ding.16g.32db.0rodb. 96proxy.multithread | 6 | 32 | 32 | 500 00 | 500 000 | 96 | 204 8 |
| 1,024 GB cluster performance- enhanced instance (64 shards) | redis.amber.logic.shar ding.16g.64db.0rodb. 192proxy.multithread | 6 | 64 | 64 | 500 00 | 500 000 | 96 | 204 8 |
| 2,048 GB cluster performance- enhanced instance (128 shards) | redis.amber.logic.shar ding.16g.128db.0rodb .384proxy.multithread | 6 | 128 | 128 | 500 00 | 500 000 | 96 | 204 8 |

| Specification | Specification code | Num ber of I/O thre ads | Num ber of shar ds | Num ber of prox y serv ers | Num ber of con nect ions per seco nd | Maxi mu m num ber of conc urre nt con nect ions | Maxi mu m ban dwi dth valu e per shar d | Tot al maxi mu m ban dwi dth valu e (MB/ s) |
|---|---|---|---|---|---|---|---|---|
| 4,096 GB cluster performance- enhanced instance (256 shards) | redis.amber.logic.shar ding.16g.256db.0rodb .768proxy.multithread | 6 | 256 | 256 | 500 00 | 500 000 | 96 | 204 8 |
| 8,192 GB cluster performance- enhanced instance (256 shards) | redis.amber.logic.shar ding.32g.256db.0rodb .768proxy.multithread | 6 | 256 | 256 | 500 00 | 500 000 | 96 | 204 8 |

Community Edition instances Standard master-replica instances

| Specification | Service code | Maximum number of connections | Maximum bandwidth value (MB/s) | CPU |
|---|---|---|---|---|
| 1GB master- replica instance | redis.master.small.default | 20000 | 48 | 1 core |
| 2 GB master- replica instance | redis.master.mid.default | 20000 | 48 | 1 core |
| 4 GB master- replica instance | redis.master.stand.default | 20000 | 48 | 1 core |
| 8 GB master- replica instance | redis.master.large.default | 20000 | 48 | 1 core |
| 16 GB master- replica instance | redis.master.2xlarge.defaul t | 20000 | 48 | 1 core |
| 32 GB master- replica instance | redis.master.4xlarge.defaul t | 20000 | 48 | 1 core |
| 64 GB master- replica instance | redis.master.8xlarge.defaul t | 20000 | 96 | 1 core |

Cluster instances

| Specification | Service code | Num ber of shard s | Maximu m number of connecti ons | Maximu m bandwid th value (MB/s) | CPU |
|---|---|---|---|---|---|
| 16 GB cluster instance | redis.logic.sharding.2g.8db.0rodb.8prox y.default | 8 | 80000 | 768 | 8 cores |
| 32 GB cluster instance | redis.logic.sharding.4g.8db.0rodb.8prox y.default | 8 | 80000 | 768 | 8 cores |
| 64 GB cluster instance | redis.logic.sharding.8g.8db.0rodb.8prox y.default | 8 | 80000 | 768 | 8 cores |
| 128 GB cluster instance | redis.logic.sharding.8g.16db.0rodb.16pr oxy.default | 16 | 160000 | 1536 | 16 cores |
| 256 GB cluster instance | redis.logic.sharding.16g.16db.0rodb.16 proxy.default | 16 | 160000 | 1536 | 16 cores |
| 512 GB cluster instance | redis.logic.sharding.16g.32db.0rodb.32 proxy.default | 32 | 320000 | 2048 | 32 cores |
| 1 TB cluster instance | redis.logic.sharding.16g.64db.0rodb.64 proxy.default | 64 | 500000 | 2048 | 64 cores |
| 2 TB cluster instance | redis.logic.sharding.16g.128db.0rodb.12 8proxy.default | 128 | 500000 | 2048 | 128 cores |
| 4 TB cluster instance | redis.logic.sharding.16g.256db.0rodb.25 6proxy.default | 256 | 500000 | 2048 | 256 cores |

#### 2.12.2 Error codes

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because RAM users are not authorized to call the API operation. | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| The error message returned because the operation is unavailable for RAM users. | Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |
| The error message returned because an exception or error occurs on the server. | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |

| eveloper Guide·API refere | nce |   | ApsaraDB for Redi |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the instance status that you specified does not exist. | InvalidStatus.NotFound | The Status provided does not exist in our records. | 404 |
| The error message returned because the specified value of the parameter is invalid. | InvalidParameter | The specified parameter InstanceName is not valid. | 400 |
| The error message returned because you are not authorized to call the administrator- specific API operations. | Forbbiden.NotAdminUse r | User not authorized to operate on the specified API as you are not the | 403 |
| The error message returned because the parameter is missing. | MissingParameter | Specified parameter is missing. | 400 |
| The error message returned because neither InstanceName nor NewPassword is specified. | MissingParameter | InstanceName/NewPass word at least one is mandatory for this action. | 400 |
| The error message returned because OwnerId is not specified for this operation. | MissingParameter | The input parameter OwnerId, OwnerAccount that is mandatory for processing this request | 403 |
| The error message returned because the specified Token parameter is invalid. | InvalidToken.Malformed | The Specified parameter "Token" is not valid. | 400 |
| The error message returned because the specified InstanceName parameter is invalid. | InvalidInstanceName.Ma lformed | The Specified parameter "InstanceName" is not valid. | 400 |
| The error message returned because the specified Password parameter is invalid. | InvalidPassword.Malfor med | The Specified parameter "Password" is not valid." | 400 |
| The error message returned because the specified Instances parameter is invalid. | InvalidInstances.Malfor med | The Specified parameter "Instances" is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified StartTime parameter is invalid. | InvalidStartTime.Malfor med | The Specified parameter "StartTime" is not valid. | 400 |
| The error message returned because the specified EndTime parameter is invalid. | InvalidEndTime.Malform ed | The Specified parameter "EndTime" is not valid. | 400 |
| The error message returned because the specified InstanceIds parameter is invalid. | InvalidInstanceIds.Malfo rmed | The Specified parameter "InstanceIds" is not valid. | 400 |
| The error message returned because your balance is insufficient to perform the current operation. | InsufficientBalance | Your account does not have enough balance. | 400 |
| The error message returned because your account fails to pass the real-name authentication. | RealNameAuthenticatio nError | Your account has not passed the real-name authentication yet. | 403 |
| The error message returned because your instance quota has been exhausted. | QuotaExcee | Living afterpay instances quota exceeded. | 400 |
| The error message returned because the capacity configuration is invalid. | InvalidCapacity.NotFoun d | The Capacity provided does not exist in our records. | 400 |
| The error message returned because the ClientToken parameter used for this request has already been used for a different request. | IdempotentParameterMi smatch | Request uses a client token in a previous request but is not identical to that request. | 400 |
| The error message returned because the inventory of instances in the specified zone is insufficient. | QuotaNotEnough | Quota not enough in this zone. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because you are not authorized to call the order-class API operations. | Forbbiden.SubUser | The specified action is not available for you. | 403 |
| The error message returned because the Apsara Stack risk control system denies this access request. | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| The error message returned because the specified region does not exist. | InvalidRegion.NotFound | The RegionId or ZoneId provided does not exist in our records. | 404 |
| The error message returned because the specified ZoneId parameter is invalid. | InvalidZoneId.NotFound | The ZoneId provided is invalid. | 400 |
| The error message returned because the ID of the instance does not exist. | InvalidInstanceId.NotFou nd | The InstanceId provided does not exist in our records. | 404 |
| The error message returned because the password is incorrect. | IncorrectPassword | The Password provided is not correct. | 400 |
| The error message returned because the service is unavailable. | ServiceNotSupported | The specified service is not supported. | 400 |
| The error message returned because a renewal and configuration change order has not taken effect. | HasRenewChangeOrder | This instance has a renewChange order. | 400 |
| The error message returned because an internal error occured. | InternalError | The request processing has failed due to some unknown error. | 500 |
| The error message returned because the specified backup time is invalid. | InvalidPreferredBackupT ime | Specified preferred backup time is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified backup type is invalid. | InvalidBackupType.Form at | Specified backup type is not valid. | 400 |
| The error message returned because the specified backup method is invalid. | InvalidBackupMethod.Fo rmat | Specified backup method is not valid. | 400 |
| The error message returned because the backup task already exists. | BackupJobExists | A backup job already exists in the specified DB instance. | 400 |
| The error message returned because the maximum number of daily backup operations has been reached. | BackupTimesExceeded | Exceeding the daily backup times of this DB instance. | 400 |
| The error message returned because no parameters are specified. | ParameterLeastAssociat e | Must input at least one optional parameter. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidBackupRetentionP eriod.Malformed | Specified backup retention period is not valid. | 400 |
| The error message returned because the specified next backup time is invalid. | InvalidPreferredBackupT ime.Format | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidPreferredBackupP eriod.Malformed | Specified backup period is not valid. | 400 |
| The error message returned because the operation is not supported by the current instance type. | IncorrectDBInstanceTyp e | Current DB instance type does not support this operation | 400 |
| The error message returned because the specified key is invalid. | InvalidKey.Malformed | Specified key is not valid. | 400 |

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the nonce signature is used and cannot be used again. | SignatureNonceUsed | Specified signature nonce was used already. | 400 |
| The error message returned because no virtual IP address can be assigned. | AllocateVpcIp.NotEnoug h | Ip resource is not enough | 400 |
| The error message returned because instances of the specified type cannot be created in the zone. | Zone.NotSupport | Specified zone does not support creating with instance class. | 400 |
| The error message returned because the code for the instance type is invalid. | MissingClassCode | Capacity or InstanceClass is mandatory for this action. | 400 |
| The error message returned because the specified instance type is not supported. | InvalidDBInstanceClass.N otFound | Specified DB instance class is not found. | 404 |
| The error message returned because the instance is locked. | IncorrectDBInstanceLock Mode | Current DB instance lock mode does not support this operation. | 400 |
| The error message returned because the ID of the backup set does not exist. | InvalidBackupSetID.NotF ound | Specified backup set ID does not exist. | 400 |
| The error message returned because the operation is not supported while the instance is in the current state. | IncorrectDBInstanceStat e | Current DB instance state does not support this operation. | 400 |
| The error message returned when the available resource capacity in the specified instance is insufficient. | InsufficientResourceCap acity | There is insufficient capacity available for the requested instance. | 400 |
| The error message returned because the specified end time is invalid. | InvalidEndTime.Format | Specified end time is not valid. | 400 |

| psaraDB for Redis |   | De | veloper Guide·API referenc |
|---|---|---|---|

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because the specified duration for reserving a classic IP address is invalid. | InvalidClassicExpiredDay s.Format | The specified classicExpiredDays format is not valid. | 400 |
| The error message returned because the operation is not supported while the backup set is in the current state. | IncorrectBackupSetStat e | Current backup set state does not support operations. | 400 |
| The error message returned when the specified whitelist is not correct in format. | InvalidSecurityIPList.For mat | Specified security IP list format is not valid. | 400 |

#### 2.12.3 Instance configurations

KVStore for Redis instance configurations

| Parameter | Description | Value |
|---|---|---|
| maxmemory-policy | The eviction policy that a KVStore for Redis instance uses to evict data when the memory exceeds the threshold. KVStore for Redis supports six data eviction policies. | VolatileLRU: only evicts original data that has Time To Live (TTL) configured based on the Least Recently Used (LRU) algorithm. VolatileTTL: only evicts data that has TTL configured based on the TTL values in ascending order. AllKeysLRU: evicts original data based on the LRU algorithm. VolatileRandom: only evicts original data that has TTL configured randomly. AllKeysRandom: evicts original data randomly. NoEviction: evicts no data, but returns an error message when you write new data to the instance. |

| Parameter | Description | Value |
|---|---|---|
| hash-max-ziplist-entries | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 512. |
| hash-max-ziplist-value | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 64. |
| list-max-ziplist-entries | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 512. |

| Parameter | Description | Value |
|---|---|---|
| list-max-ziplist-value | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist-value. | Default value: 64. |
| set-max-intset-entries | A set object uses intset encoding only if: the number of entries is smaller than or equal to the value of set-max-intset-entries and all entries are decimal integers. | Default value: 512. |
| zset-max-ziplist-entries | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 128. |

| Parameter | Description | Value |
|---|---|---|
| zset-max-ziplist-value | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 64. |
| notify-keyspace-events | The keyspace notifications allow clients to subscribe to channels or modes to receive events where Redis datasets were modified in some way. | K: the keyspace notifications. All notifications are prefixed with \ keyspace\@ \ . __ _ _ E: the keyevent notifications. All notifications are prefixed with keyevent@ . __ __ g: the notifications about general commands that are non-type specific, such as DEL, EXPIRE, and RENAME. $: the string command notifications. l: the list command notifications. s: the set command notifications. h: the hash command notifications. z: the sorted set command notifications. x: the expiration events. The system sends an expiration event after the system deletes an expired key. e: the eviction events. The system sends an eviction event after the system evicts a key according to the maxmemory policy. A: the alias for g$lshzxe. |
