---
title: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Server Load Balancer Developer Guide 20220928"
product_version: "V3.14.0"
doc_version: "20220928"
pdf_pages: 244
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.14.0 Server Load Balancer Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/v3.14.0/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.14.0%20Server%20Load%20Balancer%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.14.0 Server Load Balancer Developer Guide 20220928

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
- 2 API Reference
  - 2.1 Make API requests
  - 2.2 RAM authentication
  - 2.3 Common parameters
  - 2.4 SLB instance
    - 2.4.1 CreateLoadBalancer
    - 2.4.2 DeleteLoadBalancer
    - 2.4.3 ModifyLoadBalancerInstanceSpec
    - 2.4.4 ModifyLoadBalancerInternetSpec
    - 2.4.5 SetLoadBalancerName
    - 2.4.6 SetLoadBalancerStatus
    - 2.4.7 DescribeLoadBalancerAttribute
    - 2.4.8 DescribeLoadBalancers
    - 2.4.9 DescribeRegions
    - 2.4.10 DescribeZones
  - 2.5 Listeners
    - 2.5.1 TCP listeners
      - 2.5.1.1 CreateLoadBalancerTCPListener
      - 2.5.1.2 SetLoadBalancerTCPListenerAttribute
      - 2.5.1.3 DescribeLoadBalancerTCPListenerAttribute
    - 2.5.2 UDP listeners
      - 2.5.2.1 CreateLoadBalancerUDPListener
      - 2.5.2.2 SetLoadBalancerUDPListenerAttribute
      - 2.5.2.3 DescribeLoadBalancerUDPListenerAttribute
    - 2.5.3 HTTP listeners
      - 2.5.3.1 CreateLoadBalancerHTTPListener
      - 2.5.3.2 SetLoadBalancerHTTPListenerAttribute
      - 2.5.3.3 DescribeLoadBalancerHTTPListenerAttribute
    - 2.5.4 HTTPS listeners
      - 2.5.4.1 CreateLoadBalancerHTTPSListener
      - 2.5.4.2 SetLoadBalancerHTTPSListenerAttribute
      - 2.5.4.3 DescribeLoadBalancerHTTPSListenerAttribute
      - 2.5.4.4 DescribeHealthStatus
    - 2.5.5 Access control
      - 2.5.5.1 SetListenerAccessControlStatus
      - 2.5.5.2 DescribeListenerAccessControlAttribute
      - 2.5.5.3 AddListenerWhiteListItem
      - 2.5.5.4 RemoveListenerWhiteListItem
    - 2.5.6 DeleteLoadBalancerListener
    - 2.5.7 StopLoadBalancerListener
    - 2.5.8 StartLoadBalancerListener
  - 2.6 Server certificates
    - 2.6.1 UploadServerCertificate
    - 2.6.2 DeleteServerCertificate
    - 2.6.3 DescribeServerCertificates
    - 2.6.4 SetServerCertificateName
    - 2.6.5 UploadCACertificate
    - 2.6.6 DeleteCACertificate
    - 2.6.7 DescribeCACertificates
    - 2.6.8 SetCACertificateName
  - 2.7 Backend servers
    - 2.7.1 AddBackendServers
    - 2.7.2 RemoveBackendServers
    - 2.7.3 SetBackendServers
  - 2.8 vServer groups
    - 2.8.1 CreateVServerGroup
    - 2.8.2 SetVServerGroupAttribute
    - 2.8.3 AddVServerGroupBackendServers
    - 2.8.4 RemoveVServerGroupBackendServers
    - 2.8.5 ModifyVServerGroupBackendServers
    - 2.8.6 DeleteVServerGroup
    - 2.8.7 DescribeVServerGroups
    - 2.8.8 DescribeVServerGroupAttribute
  - 2.9 Primary/secondary server groups
    - 2.9.1 CreateMasterSlaveServerGroup
    - 2.9.2 DeleteMasterSlaveServerGroup
    - 2.9.3 DescribeMasterSlaveServerGroups
    - 2.9.4 DescribeMasterSlaveServerGroupAttribute
  - 2.10 Tags
    - 2.10.1 AddTags
    - 2.10.2 DescribeTags
    - 2.10.3 RemoveTags
  - 2.11 Error codes

using ASAPI

## 1 Make SDK calls by using ASAPI

### 1.1 ASAPI Developer Guide

#### 1.1.1 ASAPI overview

This topic describes the architecture and features of the Apsara Stack API (ASAPI). The ASAPI is a unified ingress gateway for Apsara Stack services and a main component of the Apsara Uni-manager Management Console. The ASAPI provides a unified method for you to manage and make API calls. You can use Apsara Stack SDK to centrally make API calls to Apsara Stack services, including Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). The ASAPI allows you to make API calls to manage and maintain Apsara Stack services. Make API calls to implement enterprise-grade management. For example, you can manage organizations, users, roles, resource sets, and logon policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage operations. For example, you can manage quotas, usage statistics, using ASAPI specifications, and password policies. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to manage resources. For example, you can create, delete, query, or modify cloud resources. These operations are provided by Apsara Stack services. If you call an API operation to create an ECS instance or a VPC, the API operation is provided by ECS or VPC. Make API calls to query monitoring metrics of Apsara Stack services. These operations are provided by the Apsara Uni-manager Management Console. Make API calls to perform O&M. For example, you can manage monitoring and alerting, inventories, tasks, and physical servers. These operations are provided by the Apsara Uni-manager Operations Console. For more information, see the developer guide of the corresponding Apsara Stack service. For information about API operations used to manage organization users, see Apsara Uni-manager Management Console Developer Guide. For information about the API operation used to create an ECS instance, see ECS Developer Guide. Not e If the "Use Apsara Stack SDK to make API calls" section is included in the developer guide of an Apsara Stack service, the ASAPI is supported by the Apsara Stack service. In this case, you can make API calls based on the developer guide.

#### 1.1.2 Preparations

##### 1.1.2.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console. Prerequisites Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment staff. We recommend that you use Google Chrome. Procedure
1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press the
Enter key.
2. Enter your username and password.
Obtain the username and password that you use to log on to the Apsara Uni-manager Management Console from the operations administrator. using ASAPI Not e The first time that you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Uppercase or lowercase letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
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

This topic describes three methods used to generate an endpoint for the Apsara Stack API (ASAPI). using ASAPI Method 1: Use Registration Vars of Services to generate an endpoint
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
using ASAPI i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click O&M. iii. In the left-side navigation pane, choose Product Management > Product s. iv. In the Apsara Stack O&M section, click Apsara Inf rast ruct ure Management Framework.
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
root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internetdomain parameter instead of the intranet-domain parameter. If the region value is `cn-****-****-d01` and the int ernet -domain value is `inter.****.****.com` , the following endpoint can be generated: using ASAPI

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

using ASAPI

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

When you use Apsara Stack SDK for Node.js to make API calls, specify a region ID. You can obtain a region ID in the Apsara Uni-manager Management Console. Procedure using ASAPI
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

using ASAPI

| Paramet er | T ype | Required | Descript ion |
|---|---|---|---|
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |
| SignatureMethod | String | Yes | The encryption method of the signature string. Valid values: HMAC- SHA1 and HMAC- SHA256. |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Valid values: 1.0 and 2.0. |
| SignatureNonce | String | Yes | A unique, random number used to prevent replay attacks. You must use different numbers for different requests. |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy- MM-ddTHH:mm:ssZ format. The time must be in UTC. Sample value: 2018-01- 01T12:00:00Z. |
| Format | String | Yes | The format in which to return the response. Set the value to JSON. |

using ASAPI Not e

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
Method 1: Create a Maven project in IntelliJ IDEA. using ASAPI Method 2: Convert an existing project to a Maven project. a. Right-click the project that you want to convert and select Add Framework Support .... b. Select Maven and click OK.
4. Create a folder named libs in the root directory of the project. Then, add the JAR file of Apsara
Stack SDK for Java to the libs folder, as shown in the following figure. using ASAPI
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
using ASAPI If the information in the following figure appears, the dependencies are added. Use Apsara Stack SDK for Java You can use the GET or POST method to call API operations provided by the ASAPI. The following sample code shows how to call API operations: using ASAPI

```java
// 1. Create a connection to an ASClient object. ASClient client = new ASClient(); // 2. Configure the identifier of the requester. This parameter is required and used only f or identification. You can set this parameter to a random value. client.setSdkSource("<The identifier of the requester>"); Map<String, Object> parameters = new HashMap<String, Object>(); // 3. Configure the parameters for authorization. The parameter values vary based on your e nvironment. // The AccessKey ID of your Apsara Stack tenant account. parameters.put("AccessKeyId","<AccessKey ID>"); // The AccessKey secret of your Apsara Stack tenant account. parameters.put("AccessKeySecret", "<AccessKey Secret>"); // The ID of the region. parameters.put("RegionId", "<your RegionID>"); // 4. Configure parameters for an API call. In this example, the Product, Action, and Versi on parameters are configured. parameters.put("Product", "<The name of the service>"); parameters.put("Action", "<The name of the API operation>"); parameters.put("Version", "<The version of the API operation>"); // 5. Configure operation-specific parameters. parameters.put("<The name of the operation-specific parameter>", "<The value of the operati on-specific parameter>"); // 6. Configure request headers and the encryption method for the signature string. Valid v alues of the SignatureMethod parameter: HMAC-SHA1 and HMAC-SHA256. By default, HMAC-SHA256 is used. Map<String, String> headers = new HashMap<String, String>(); //headers.put("SignatureMethod", "HMAC-SHA1"); headers.put("x-acs-regionid", "<your-regionid>"); headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); headers.put("x-acs-organizationid", "<your-organizationid>"); headers.put("x-acs-instanceid", "<your-instanceid>"); // 7. Make an API call. We recommend that you use the doPost() method. // Configure the time-out period for a connection. //client.setConnectTimeout(10000); // Configure the time-out period for a request. // client.setSocketTimeout(10000); String result = client.doPost(endpoint, headers, parameters); System.out.println(result);
```

Configure a proxy If you need to use a proxy to make API calls, use the following sample code to configure the proxy:

```
Cloud cloud = new Cloud(); // Configure the IP address of the proxy. cloud.setConfig("proxy_host", "<IP>"); // Configure the port used by the proxy. cloud.setConfig("proxy_port", "<Port>"); // 1. Create a connection to an ASClient object. ASClient client = new ASClient(cloud);
```

Request headers using ASAPI

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

Not e Replace `2.4.7` with the actual version of Apsara Stack SDK for Python. Sample requests You can use the GET or POST method to call API operations provided by the ASAPI. using ASAPI

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

using ASAPI Configure a proxy Perform the following steps to configure a proxy:
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

Use Apsara Stack SDK for Node.js The following sample code shows how to use Apsara Stack SDK for Node.js to make API calls: using ASAPI

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

using ASAPI Request headers

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

using ASAPI Call examples The following sample code provides an example on how to use the RPC style to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

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

using ASAPI

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

using ASAPI

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Go. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. using ASAPI Sample code:

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

using ASAPI

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

This topic describes how to use Apsara Stack API (ASAPI) SDK for POP for Python. Prerequisites An Alibaba Cloud SDK package is downloaded for the service that you want to access. The required dependencies are installed. Background information Only the remote procedure call (RPC) style is supported for API calls. using ASAPI Call examples The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05- 26. Sample code:

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

Configure proxies using ASAPI Set the HTTP_PROXY and HTTPS_PROXY environment variables. Sample code:

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

`https` : the protocol used to transmit the request. `public.asapi.aliyuns.com/asapi/v3` : the endpoint of the ASAPI. `Action=GetOrganizationList Product=ascm Version=2019-05-10` : the API operation to call. `Id` : the ID of the organization. `<Common parameters>` : the common parameters specified in the system. using ASAPI Protocol The ASAPI supports only HTTPS. Endpoint For more information about how to obtain an endpoint, see Generate an endpoint for the ASAPI. To specify an API operation, use the `Action, Product, and Version` parameters. For example, set `Action` to GetOrganizationList, Product to ascm, and Version to 2019-05-10. You must also specify other operation-specific parameters and common parameters. For more information, see Common parameters.

##### 1.1.5.3 Request signatures

This topic describes how to sign HTTP API requests. ASAPI uses the request signature to verify the identity of the request sender. ASAPI implements symmetric encryption by using an AccessKey pair to verify the identity of the request sender. Not e An AccessKey pair consists of an AccessKey ID and an AccessKey secret, which are issued to each user or organization in the Apsara Uni-manager Management Console. The AccessKey ID is used to verify identities of users, and the AccessKey secret is used to encrypt and verify signature strings. You must keep your AccessKey secret confidential. ASAPI provides SDKs for Node.js, Python, and Java to facilitate complex signature calculation. For more information, see Obtain the core package for ASAPI. Step 1: Create a canonicalized query string
1. Arrange the request parameters in alphabetical order, including all common and operation-specific
parameters except the `Signature` parameter. Not e If you use the GET method to send a request,these parameters are connected by ampersands (&) and included in the request URL. The first request parameter follows a question mark (?).
2. Encode the request parameters and their values in UTF-8 based on RFC 3986. The following rules
apply in the encoding process: Letters, digits, and special characters such as hyphens ( `-` ), underscores ( `_` ), and periods ( `.` ) do not need to be encoded. using ASAPI Other characters must be percent encoded in the %XY format. `XY` represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks ( `"` ) are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20 . Do not encode spaces as plus signs ( `+` ). This encoding method is similar to but different from the `application/x-www-form-urlencoded` MIME encoding algorithm. If you use `java.net.URLEncoder` from the Java standard library, use `percentEncode` to encode request parameters and their values. In the encoded query string, replace the plus signs ( `+` ) with %20 , asterisks ( `*` ) with %2A , and %7E with tildes ( ~ ). This way, you can obtain an encoded string that matches the preceding encoding rules.

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

using ASAPI Not e When you calculate the signature, the key value specified by RFC 2104 is your `AccessKey secret` plus an ampersand (&), which has an ASCII value of 38. For more information, see Obtain an AccessKey pair.
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

You can use browsers or tools such as cURL and Wget to initiate an HTTP request for calling the `DescribeRegions` operation to query the Alibaba Cloud region list. Example 2: Use t he st andard library of t he programming language using ASAPI `GetOrganizationList` is used in this example to query regions. For example, `AccessKeyID` is set to testid, `AccessKeySecret` is set to testsecret, and all request parameters are stored in a Java `Map<String, String>` object.
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
using ASAPI

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

using ASAPI
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

## 2 API Reference

### 2.1 Make API requests

To call a Server Load Balancer (SLB) API operation, you must send an HTTP GET request to the endpoint of the SLB API. You must add the request parameters that correspond to the API operation being called. After you call the API operation, the system returns a response. The request and response are encoded in UTF-8. Request syntax SLB API operations use the RPC protocol. You can call SLB API operations by sending HTTP GET requests. The request syntax is:

```
http://Endpoint/?Action=xx&Parameters
```

where: Endpoint: the endpoint of the SLB API is `slb.example.com` . Not e `example.com` is a custom domain name. To obtain the domain name, contact an administrator. For more information, see Generate the Apsara Stack API (ASAPI) endpoint. Action: the name of the operation being performed. For example, to query SLB instances, you must set the Action parameter to DescribeLoadBalancers. Version: is the version of the API that you want to use. The current SLB API version is 2014-05-15. Parameters: the request parameters for the operation. Separate multiple parameters with ampersands (&). Request parameters include both common parameters and operation-specific parameters. Common parameters include the API version and authentication information. For more information, see Common parameters. The following example demonstrates how to call the DescribeLoadBalancers operation in SLB. Not e The sample requests are formatted to improve readability.

```
https://slb.example.com/?Action=DescribeLoadBalancers &Format=xml &Version=2014-05-15 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &TimeStamp=2016-02-23T12:46:24Z ...
```

API authorization To ensure the security of your account, we recommend that you call APIs as a Resource Access Management (RAM) user. To call the SLB API as a RAM user, you must create and add a permission policy to the RAM user. For more information about the resources and operations that can be authorized to a RAM user, see RAM authentication. Request signatures You must sign all API requests to ensure security. Apsara Stack uses the request signature to verify the identity of the API caller. SLB implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Apsara Stack tenant accounts and RAM users. An AccessKey pair is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information, see Obtain an AccessKey pair. You must add the signature to the SLB API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
```

SHA1`&Signature=`xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf Take the DescribeLoadBalancers operation as an example. If the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the pre-signed request URL is:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-26 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a query string for the signature.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeLoadBalancers&Format%3DXML&SignatureMetho d%3DHMAC-SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D 1.0&TimeStamp%3D2016-02-23T12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the hash-based message authentication code (HMAC) value of the string-to-sign.
Append an ampersand (&) to the AccessKey secret as the key for calculating the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YG****E=
```

3. Add the signature to the request parameters:

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2014-05-15 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 2.2 RAM authentication

Before calling an SLB API as a RAM user, you must use an Alibaba Cloud account to create an authorization policy to assign permissions to the RAM user. In the authorization policy, you must use an Alibaba Cloud Resource Name (ARN) as the unique identifier of the resource. Available SLB resources The following table describes the ARN format for different types of SLB resources.

| Resource type | ARN format |
|---|---|
| LoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/$loadbalancerid |
|   | acs:slb:$regionid:$accountid:loadbalancer/* |
|   | acs:slb:*:$accountid:loadbalancer/* |
|   | acs:slb:*:*:loadbalancer/* |
| Certificate | acs:slb:$regionid:$accountid:certificate/$servercertificateId |
|   | acs:slb:$regionid:$accountid:certificate/* |

$regionid/accoutid/servercertificateId is the resource ID. `*` indicates the corresponding resources. SLB APIs The following table lists the APIs that can be authorized and their corresponding ARN formats.

| API | ARN format |   |   |
|---|---|---|---|
| CreateLoadBalancer | acs:slb:$regionid:$accountid:loadbalancer/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ModifyLoadBalancerInternetSpec | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteLoadBalancer | rid |   |   |

| API | ARN format |   |   |
|---|---|---|---|
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerStatus | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerName | rid |   |   |
| DescribeLoadBalancers | acs:slb:$regionid:$accountid:loadbalancer/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeLoadBalancerAttribute | rid |   |   |
| DescribeRegions | acs:slb:*:$accountid:* |   |   |
| UploadServerCertificate | acs:slb:%s:%s:certificate/* |   |   |
| DeleteServerCertificate | acs:slb:%s:%s:certificate/% |   |   |
| DescribeServerCertificate | acs:slb:%s:%s:certificate/% |   |   |
| SetServerCertificateName | acs:slb:%s:%s:certificate/% |   |   |
| DescribeServerCertificates | acs:slb:%s:%s:certificate/* |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerHTTPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerHTTPSListener | rid |   |   |
|   | acs:slb:%s:%s:certificate/% |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerTCPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateLoadBalancerUDPListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteLoadBalancerListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| StartLoadBalancerListener | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| StopLoadBalancerListener | rid |   |   |
| SetLoadBalancerHTTPListenerAttribut | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| e | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
|   | rid |   |   |
| SetLoadBalancerHTTPSListenerAttrib |   |   |   |
| 3 |   |   |   |

| erver Load Balancer | Developer Guide·API Referenc |   |   |
|---|---|---|---|
| SetLoadBalancerHTTPSListenerAttrib |   |   |   |
| uAtPeI | ARN format |   |   |
|   | acs:slb:%s:%s:certificate/% |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerTCPListenerAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetLoadBalancerUDPListenerAttribute | rid |   |   |
| DescribeLoadBalancerHTTPListenerAt | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| tribute | rid |   |   |
| DescribeLoadBalancerHTTPSListenerA | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ttribute | rid |   |   |
| DescribeLoadBalancerTCPListenerAttr | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ibute | rid |   |   |
| DescribeLoadBalancerUDPListenerAttr | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ibute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| AddBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| RemoveBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeHealthStatus | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| CreateVServerGroup | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| SetVServerGroupAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DeleteVServerGroup | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeVServerGroups | rid |   |   |

| eveloper Guide·API Reference | Server Load Balance |
|---|---|

| API | ARN format |   |   |
|---|---|---|---|
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| DescribeVServerGroupAttribute | rid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| AddVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| RemoveVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |
|   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance rid |   |   |
|   |   | acs:slb:$regionid:$accountid:loadbalancer/$loadbalance |   |
| ModifyVServerGroupBackendServers | rid |   |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |   |

### 2.3 Common parameters

Common request parameters Common request parameters are request parameters that you must use when you call any API. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The format of the response. Valid values: JSON (default) \| XML |
| Version | String | Yes | The API version in the format of YYYY-MM-DD . Valid values: 2014-05-15 |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access a service. |
| Signature | String | Yes | The signature result string. |
| SignatureMethod | String | Yes | The algorithm used to create the request signature. Valid values: HMAC-SHA1 |

| Name | Type | Required | Description |
|---|---|---|---|
| Timestamp | String | Yes | The request timestamp. The timestamp uses UTC and it complies with the ISO 8601 standard. The timestamp format is YYYY-MM-DDThh:mm:ssZ . For example, 20:00:00 on January 1st, 2013 in China Standard Time (UTC +8) would be written as 2013-01- 10T12:00:00Z. |
| SignatureVersion | String | Yes | The signature algorithm version. Valid value: 1.0 |
| SignatureNonce | String | Yes | A unique random number that is used to prevent network replay attacks. You must use different random numbers for different requests. |

```
http://slb.example.com/?Action=DescribeLoadBalancers &TimeStamp=2014-05-19T10%3A33%3A56Z &Format=xml &AccessKeyId=testid &Action=DescribeLoadBalancerAttribute &SignatureMethod=Hmac-SHA1 &LoadBalancerId=loadBalancerID &SignatureNonce=NwDAxvLU6tFE0DVb &Version=2014-05-15 &SignatureVersion=1.0 &Signature=Signature
```

Common response parameters API responses use a unified format. The 2xx HTTP status code indicates a successful invocation. The 4xx or 5xx HTTP status code indicates a failed invocation. The responses can be returned in JSON or XML format. The XML format is used by default. You can specify the format when calling an API. Each time a request is sent to call an API, the system returns a unique identifier RequestId, regardless of whether the invocation is successful. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
    <!—Result root node-->
    <API name+Response>
        <!—Returned request tag-->
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
        <!—Returned result-->
    </API name+Response>
```

JSON format `{`

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /*Returned result*/
```

`}`

### 2.4 SLB instance

#### 2.4.1 CreateLoadBalancer

Creates a Server Load Balancer (SLB) instance. Before you call this operation, take note of the following items: Before you create an SLB instance, call the DescribeAvailableResource operation to query the resources available for purchase in the zone where you want to create the SLB instance. You are charged for the SLB instances that you create. For more information, see Create an SLB instance. If you do not set LoadBalancerSpec, a shared-resource SLB instance is created. We recommend that you set the LoadBalancerSpec parameter to specify the specification of the SLB instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cer | The operation that you want to perform. Set the value to Creat eLoadBalancer. |
| RegionId | String | Yes | cn-east- hangzhou-01 | The ID of the region where you want to create the SLB instance. You can call the DescribeRegions operation to query region IDs. |
| AddressType | String | No | internet | The network type of the SLB instance. Valid values: int ernet and int ranet . int ernet : After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. int ranet : After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| InternetChargeTy pe | String | No | paybytraffic | The billing method of the Internet- facing SLB instance. Set the value to paybytraffic. |
| Bandwidth | Integer | No | 10 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit for each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. For more information, see Bandwidth of a shared-resource SLB instance. |
| ClientToken | String | No | 5A2CFF0E-5718- 45B5-9D4D- 70B3FF3898 | This parameter is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LoadBalancerNa me | String | No | abc | The name of the SLB instance. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. If this parameter is not set, the system automatically creates a name for the SLB instance. |
| VpcId | String | No | vpc- bp1aevy8sofi8mh 1***** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| VSwitchId | String | No | vsw- bp12mw1f8k3jgy ***** | The ID of the vSwitch to which the internal-facing SLB instance belongs. The vSwitch must be deployed in a VPC. To create an internal-facing SLB instance that is deployed in a VPC, you must set this parameter. If this parameter is set, the value of the AddessT ype parameter is set to int ranet by default. |
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. You can call the DescribeZone operation to query information about the primary and secondary zones in a region. |
| access key id _ _ | String | No | 111 | The AccessKey ID. |
| Tags | String | No | test | The tags that you want to add to the SLB instance. |
| EnableVpcVipFlo w | String | No | 1 | The flow log. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerSpe c | String | No | slb.s2.small | Apsara Stack provides two types of SLB instance: shared-resource SLB instances and high-performance SLB instances. You can create high-performance SLB instances of different specifications. Valid values: slb.s1.small slb.s2.small slb.s3.small slb.s2.medium For more information about the specifications of high-performance SLB instances, see High-performance SLB instances. |
| AddressIPVersion | String | No | ipv4 | The IP version that is used by the SLB instance. Valid values: ipv4 and ipv6. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-hddhfjg******* | The ID of the SLB instance. |
| Address | String | 42.250.**.** | The IP address that is allocated to the SLB instance. |
| VpcId | String | vpc-25dvzy9***** | The ID of the VPC to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecr*** | The ID of the vSwitch to which the SLB instance belongs. |
| LoadBalancerN ame | String | abc | The name of the SLB instance. |
| AddressIPVersi on | String | ipv4 | The IP version that is used by the SLB instance. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkType | String | classic | The type of network where the SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancer &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerResponse>
    <NetworkType>vpc</NetworkType>
      <LoadBalancerName>abc</LoadBalancerName>
      <Address>192.168.0.**</Address>
      <ResourceGroupId>rg-acfmxazb***</ResourceGroupId>
      <RequestId>AB197CF0-D9E9-4475-A89D-35DBCCF13BBE</RequestId>
      <AddressIPVersion>ipv4</AddressIPVersion>
      <LoadBalancerId>lb-bp1b6c719dfa0***</LoadBalancerId>
      <VSwitchId>vsw-bp12mw1f8k3jgygk9****</VSwitchId>
      <VpcId>vpc-bp1aevy8sofi8mh1q***</VpcId>
</CreateLoadBalancerResponse>
```

`JSON` format

```json
{"LoadBalancerName":"abc", "VpcId":"vpc-25dvzy9*****", "Address":"42.250.**.**", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "NetworkType":"classic", "AddressIPVersion":"ipv4", "VSwitchId":"vsw-255ecr***", "LoadBalancerId":"lb-hddhfjg*******"}
```

#### 2.4.2 DeleteLoadBalancer

Deletes a pay-as-you-go Server Load Balancer (SLB) instance. Not e After you delete an SLB instance, the listeners configured for the SLB instance and the tags added to the SLB instance are deleted. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalan cer | The operation that you want to perform. Set the value to Delet eLoadBalancer. |
| LoadBalancerId | String | Yes | lb- bp1h66tp5uat8** ** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

If the SLB instance that you want to delete has deletion protection enabled, the system reports an error in the following formats: JSON format `{`

```json
 "RequestId": "7B7AB375-1EA6-4A18-9D1C-F258F2D57638",
 "HostId": "slb.aliyuncs.com",
 "Code": "OperationDenied.DeleteProtectionIsOn",
 "Message": "The loadbalancer can't be deleted due to DeleteProtection is enabled."
```

`}` XML format

```xml
   <?xml version="1.0" encoding="UTF-8" ?>
        <DeleteLoadBabalancerResponse>
 <RequestId>7B7AB375-1EA6-4A18-9D1C-F258F2D57638</RequestId>
 <HostId>slb.aliyuncs.com</HostId>
 <Code>OperationDenied.DeleteProtectionIsOn</Code>
 <Message>The loadbalancer can't be deleted due to DeleteProtection is enabled.</Message>
       </DeleteLoadBabalancerResponse>
```

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancer &LoadBalancerId=lb-bp1h66tp5uat8******** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteLoadBabalancerResponse>
   <RequestId>E3F602B8-A162-4683-A7EC-49364E597259</RequestId>
</DeleteLoadBabalancerResponse>
```

`JSON` format `{`

```json
    "RequestId": "0D9B7343-AC1F-498C-A18A-78FE14A7C3A3"
```

`}`

#### 2.4.3 ModifyLoadBalancerInstanceSpec

Modifies the specification of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalan cerInstanceSpec | The operation that you want to perform. Set the value to Modif yLoadBalancerInst anceSpec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719df**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerSpe c | String | Yes | slb.s1.small | The specification of the SLB instance. Valid values: slb.s1.small slb.s2.small slb.s2.medium slb.s3.small slb.s3.medium slb.s3.large The supported specifications vary by region. For more information, see Instance types . Not e When you change a shared-resource SLB instance to a high-performance SLB instance, your service may be temporarily interrupted for 10 to 30 seconds. Therefore, we recommend that you modify the specification during off-peak hours. In addition, you can use Alibaba Cloud DNS (DNS) to schedule your workloads to another SLB instance before you modify the specification. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInstanceSpec &LoadBalancerId=lb-bp1b6c719df**** &LoadBalancerSpec=slb.s2.small &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyLoadBalancerInstanceSpecResponse>
     <RequestId>D456A34A-6E40-4379-8DAF-9175760FE215</RequestId>
  </ModifyLoadBalancerInstanceSpecResponse>
```

`JSON` format `{`

```json
    "ModifyLoadBalancerInstanceSpecResponse": {
        "RequestId": "D456A34A-6E40-4379-8DAF-9175760FE215"
```

`}` `}`

#### 2.4.4 ModifyLoadBalancerInternetSpec

Modifies the billing method of an Internet-facing Server Load Balancer (SLB) instance. You can modify the billing method of an Internet-facing SLB instance in the following ways: Change the bandwidth limit of a pay-by-bandwidth SLB instance. The new bandwidth limit immediately takes effect. Change the billing method of an SLB instance from pay-by-data-transfer to pay-by-bandwidth. The new billing method takes effect at 00:00 the following day. Change the billing method of an SLB instance from pay-by-bandwidth to pay-by-data-transfer. The new billing method takes effect at 00:00 the following day. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLoadBalan cerInternetSpec | The operation that you want to perform. Set the value to Modif yLoadBalancerInt ernet Spec. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | 10 | The bandwidth limit of the Internet- facing SLB instance that is billed on a pay-by-bandwidth basis. Unit: Mbit/s. Valid values: 1 t o 5000. The bandwidth limit varies based on the region where the SLB instance is created. Not e You do not need to set this parameter for pay-by- data-transfer SLB instances. In this case, the value of Int ernet ChargeT ype is paybyt raf f ic. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyLoadBalancerInternetSpec &LoadBalancerId=lb-bp1b6c719dfa08ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyLoadBalancerInternetSpecResponse>
      <RequestId>E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED</RequestId>
</ModifyLoadBalancerInternetSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "E4DD2D80-8DC0-4A2E-BFBA-BE983A31AFED"
```

`}`

#### 2.4.5 SetLoadBalancerName

Modifies the name of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer Name | The operation that you want to perform. Set the value to Set LoadBalancerName. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 e**** | The ID of the SLB instance. |
| LoadBalancerNa me | String | Yes | lb-instance-test | The name of the SLB instance. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerName &LoadBalancerId=lb-bp1b6c719dfa08e**** &LoadBalancerName=abc1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerStatusResponse>
   <RequestId>3C7F675E-9F82-4806-BA47-FF57E3ACC850</RequestId>
</SetLoadBalancerStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "3C7F675E-9F82-4806-BA47-FF57E3ACC850"
```

`}`

#### 2.4.6 SetLoadBalancerStatus

Sets the state of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer Status | The operation that you want to perform. Set the value to Set LoadBalancerSt at us. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 e**** | The ID of the SLB instance. |
| LoadBalancerStat us | String | Yes | active | The state of the SLB instance. Valid values: act ive and inact ive. act ive (default) When an SLB instance is in the Active state, listeners of the SLB instance can forward inbound traffic based on forwarding rules. inact ive When an SLB instance is in the inact ive state, listeners of the SLB instance do not forward inbound traffic. Not e If all listeners of an SLB instance are deleted, the SLB instance automatically switches to the inact ive state. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerStatus &LoadBalancerId=lb-bp1b6c719dfa08e****** &LoadBalancerStatus=active &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerStatusResponse>
     <RequestId>E6DDFE22-F019-4F34-B8DD-FD14973450A6</RequestId>
  </SetLoadBalancerStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "E6DDFE22-F019-4F34-B8DD-FD14973450A6"
```

`}`

#### 2.4.7 DescribeLoadBalancerAttribute

Queries detailed information about a specified Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerAt t ribut e. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb-dhhd**** | The ID of the SLB instance. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the SLB instance is deployed. |
| RegionIdAlias | String | cn-qingdao-env17- d01 | The alias of the region where the SLB instance is deployed. |
| LoadBalancerN ame | String | abc | The name of the SLB instance. |
| LoadBalancerSt atus | String | active | The state of the SLB instance. Valid values: inact ive: The SLB instance is stopped. SLB instances in the inactive state do not forward traffic. act ive: The SLB instance runs as expected. Newly created SLB instances are in the act ive state by default. locked: The SLB instance is locked. SLB instances may be locked due to overdue payments or other reasons. |
| Address | String | 42.XX.XX.6 | The IP address that the SLB instance uses to provide services. |
| AddressType | String | internet | The type of IP address that the SLB instance uses to provide services. |
| NetworkType | String | vpc | The type of network where the SLB instance is deployed. |

| eveloper Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | Description |
| VpcId | String | vpc-25dvzy9f8**** | The ID of the virtual private cloud (VPC) where the internal-facing SLB instance is deployed. |
| Bandwidth | Integer | 5 | The bandwidth limit of the Internet-facing SLB instance that is billed on a pay-by- bandwidth basis. |
| CreateTime | String | 2017-08- 31T02:49:05Z | The time when the SLB instance was created. |
| ListenerPorts | List | 80 | The list of frontend ports that are used by the SLB instance. |
| ListenerPortsAn dProtocol | Array of ListenerPortAn dProtocol |   | The list of frontend ports and protocols that are used by the SLB instance. |
| ListenerPortAn dProtocol |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtoco l | String | https | The frontend protocol that is used by the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers that are added to the SLB instance. |
| BackendServer |   |   |   |
| ServerId | String | i-djghr2**** | The ID of the backend server. |
| Weight | Integer | 90 | The weight of the backend server. |
| ServerIp | String | 192.168.0.1 | The IP address of the backend server. |
| Type | String | ecs | The type of the backend server. |
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AutoReleaseTi me | Long | 1513947075 | The timestamp that indicates when the SLB instance was released. |
| CreateTimeSta mp | Long | 1504147745000 | The timestamp that indicates when the SLB instance was created. |
| EndTime | String | 2999-09- 08T16:00:00Z | The time when the SLB instance was suspended. |
| EndTimeStamp | Long | 32493801600000 | The timestamp that indicates when the SLB instance was suspended. |
| InternetCharge Type | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Valid values: paybybandwidt h and paybyt raf f ic. paybybandwidt h: pay-by-bandwidth paybyt raf f ic (default): pay-by-data- transfer |
| ListenerPortsAn dProtocal | Array of ListenerPortAn dProtocal |   | The port and protocol of the listener. |
| ListenerPortAn dProtocal |   |   |   |
| ListenerPort | Integer | 443 | The frontend port that is used by the SLB instance. |
| ListenerProtoca l | String | http | The frontend protocol that is used by the SLB instance. |
| LoadBalancerS pec | String | slb.s2.small | The specification of the SLB instance. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. |
| VSwitchId | String | vsw-255ecrwq5**** | The ID of the vSwitch to which the internal- facing SLB instance belongs. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerAttribute &LoadBalancerId=lb-bp1b6c719dfa08ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerAttributeResponse>
      <CreateTimeStamp>1541679713000</CreateTimeStamp>
   <RegionIdAlias>cn-hangzhou</RegionIdAlias>
   <BackendServers>
      <BackendServer>
         <ServerId>i-bp1c3zrr37ablp8ujo7v</ServerId>
         <Weight>100</Weight>
         <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
   <HasReservedInfo>false</HasReservedInfo>
   <ListenerPorts></ListenerPorts>
   <InternetChargeType>paybytraffic</InternetChargeType>
   <VSwitchId>vsw-bp12mw1f8k3*********</VSwitchId>
   <VpcId>vpc-bp1aevy8sofi8mh*****</VpcId>
   <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
   <LoadBalancerSpec>slb.s2.small</LoadBalancerSpec>
   <NetworkType>vpc</NetworkType>
   <ListenerPortsAndProtocol></ListenerPortsAndProtocol>
   <PayType>PayOnDemand</PayType>
   <Bandwidth>5120</Bandwidth>
   <LoadBalancerName>abc1</LoadBalancerName>
   <ResourceGroupId>rg-acfmxazb4p*****</ResourceGroupId>
   <AddressIPVersion>ipv4</AddressIPVersion>
   <LoadBalancerId>lb-bp1b6c719dfa08e*****</LoadBalancerId>
   <EndTimeStamp>32493801600000</EndTimeStamp>
   <MasterZoneId>cn-hangzhou-b</MasterZoneId>
   <ListenerPortsAndProtocal></ListenerPortsAndProtocal>
   <Address>192.168.0.1</Address>
   <RegionId>cn-hangzhou</RegionId>
   <RequestId>35D745B3-1567-4855-9EF1-F5CED3C1670C</RequestId>
   <CreateTime>2018-11-08T12:21:53Z</CreateTime>
   <AddressType>intranet</AddressType>
   <EndTime>2999-09-08T16:00:00Z</EndTime>
   <LoadBalancerStatus>active</LoadBalancerStatus>
</DescribeLoadBalancerAttributeResponse>
```

`JSON` format `{`

```json
    "CreateTimeStamp": 1541679713000,
    "RegionIdAlias": "cn-hangzhou",
    "BackendServers": {
        "BackendServer": [
```

`{`

```json
                "ServerId": "i-bp1c3zrr37ab*****",
                "Weight": 100,
                "Type": "ecs"
```

`}` `]` `},`

```json
    "HasReservedInfo": "false",
    "ListenerPorts": {
        "ListenerPort": [ ]
```

`},`

```json
    "InternetChargeType": "paybytraffic",
    "VSwitchId": "vsw-bp12mw1f8k******",
    "VpcId": "vpc-bp1aevy8sofi8mh******",
    "SlaveZoneId": "cn-hangzhou-d",
    "LoadBalancerSpec": "slb.s2.small",
    "NetworkType": "vpc",
    "ListenerPortsAndProtocol": {
        "ListenerPortAndProtocol": [ ]
```

`},`

```json
    "PayType": "PayOnDemand",
    "Bandwidth": 5120,
    "LoadBalancerName": "abc1",
    "ResourceGroupId": "rg-acfmxazb*****",
    "AddressIPVersion": "ipv4",
    "LoadBalancerId": "lb-bp1b6c719dfa08*****",
    "EndTimeStamp": 32493801600000,
    "MasterZoneId": "cn-hangzhou-b",
    "ListenerPortsAndProtocal": {
        "ListenerPortAndProtocal": [ ]
```

`},`

```json
    "Address": "192.168.0.1",
    "RegionId": "cn-hangzhou",
    "RequestId": "35D745B3-1567-4855-9EF1-F5CED3C1670C",
    "CreateTime": "2018-11-08T12:21:53Z",
    "AddressType": "intranet",
    "EndTime": "2999-09-08T16:00:00Z",
    "LoadBalancerStatus": "active"
```

`}`

#### 2.4.8 DescribeLoadBalancers

Queries Server Load Balancer (SLB) instances. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncers | The operation that you want to perform. Set the value to DescribeLoadBalancers. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. You can query the region ID from the Regions and zones list or by calling the DescribeRegions operation. |
| ServerId | String | No | vm-23**** | The ID of the backend server that is added to the SLB instance. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa*** * | The ID of the SLB instance. You can specify at most 10 IDs in each request. Separate multiple IDs with commas (,). |
| LoadBalancerNa me | String | No | abc1 | The name of the SLB instance. You can specify at most 10 names in each request. Separate multiple names with commas (,). |
| ServerIntranetAd dress | String | No | 10.XX.XX.6 | The private IP address of the backend server that is added to the SLB instance. You can specify multiple IP addresses to query SLB instances. Separate multiple IP addresses with commas (,). |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| AddressType | String | No | intranet | The type of network where the SLB instance is deployed. Valid values: int ranet and int ernet . int ernet : After an Internet-facing SLB instance is created, the system allocates a public IP address to the SLB instance. Then, the SLB instance can forward requests from the Internet. int ranet : After an internal-facing SLB instance is created, the system allocates a private IP address to the SLB instance. Then, the SLB instance can forward only internal requests. |
| InternetChargeTy pe | String | No | paybybandwidth | The billing method of the Internet- facing SLB instance. Valid values: paybybandwidt h and paybyt raf f ic. paybybandwidt h: pay-by- bandwidth paybyt raf f ic: pay-by-data- transfer. Not e If you do not specify this parameter, the billing method of the SLB instance remains unchanged. |
| VpcId | String | No | vpc- bp1aevy8sof**** | The ID of the virtual private cloud (VPC) to which the SLB instance belongs. |
| VSwitchId | String | No | vsw- bp12mw1f8k3*** * | The ID of the vSwitch to which the SLB instance belongs. |
| NetworkType | String | No | vpc | The type of network where the internal-facing SLB instance is deployed. Valid values: vpc and classic. vpc: a VPC classic: a classic network |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Address | String | No | 192.168.0.1 | The IP address that the SLB instance uses to provide services. |
| MasterZoneId | String | No | cn-hangzhou-b | The ID of the primary zone to which the SLB instance belongs. |
| SlaveZoneId | String | No | cn-hangzhou-d | The ID of the secondary zone to which the SLB instance belongs. Multiple zones are not supported for users whose workloads are deployed on Alibaba Finance Cloud. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The list of tags that are added to the SLB instances. The tags must be key- value pairs in a JSON dictionary. You can specify at most 10 tags in each request. |
| PayType | String | No | PayOnDemand | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. PayOnDemand: pay-as-you-go PrePay: subscription |
| AddressIPVersion | String | No | ipv4 | The IP version. Valid values: ipv4 and ipv6. Not e You can create high- performance IPv6 SLB instances only in the following zones: Hangzhou Zone E and Hangzhou Zone F in the China (Hangzhou) region, Beijing Zone F and Beijing Zone G in the China (Beijing) region, Nantong Zone D and Nantong Zone E in the China (Nantong) region, Zhangjiakou Zone A and Zhangjiakou Zone B in the China (Zhangjiakou) region, and Shenzhen Zone D and Shenzhen Zone E in the China (Shenzhen) region. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancers | Array of LoadBalancer |   | The list of SLB instances. |
| LoadBalancer |   |   |   |
| LoadBalancerId | String | lb-hjfng**** | The ID of the SLB instance. |
| LoadBalancerN ame | String | def | The name of the SLB instance. |
| LoadBalancerSt atus | String | active | The state of the SLB instance. Valid values: inact ive: Listeners do not forward requests. act ive: Newly created SLB instances are in the active state by default. locked: The SLB instance is locked. |
| Address | String | 100.XX.XX.28 | The IP address of the SLB instance. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the SLB instance is deployed. |
| RegionIdAlias | String | cn-qingdao-env17- d01 | The name of the region where the SLB instance is deployed. |
| AddressType | String | intranet | The type of network where the SLB instance is deployed. |
| VSwitchId | String | vsw-255ecr**** | The ID of the vSwitch to which the internal- facing SLB instance belongs. |
| VpcId | String | vpc-25dvzy9f8**** | The ID of the VPC to which the internal- facing SLB instance belongs. |
| NetworkType | String | vpc | The type of network where the internal- facing SLB instance is deployed. Valid values: vpc: a VPC classic: a classic network |
| CreateTime | String | 2017-08- 31T02:49:05Z | The time when the SLB instance was created. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterZoneId | String | cn-hangzhou-b | The ID of the primary zone where the SLB instance is deployed. |
| SlaveZoneId | String | cn-hangzhou-d | The ID of the secondary zone where the SLB instance is deployed. |
| AddressIPVersi on | String | ipv4 | The IP version. Valid values: ipv4 and ipv6. |
| CreateTimeSta mp | Long | 1504147745000 | The timestamp generated when the SLB instance was created. |
| InternetCharge Type | String | paybybandwidth | The billing method of the Internet-facing SLB instance. Set the value to paybytraffic. paybyt raf f ic (default): pay-by-data- transfer Not e If the value of the PayType parameter is set to PrePay, only pay-by- bandwidth is supported. |
| PayType | String | PrePay | The billing method of the SLB instance. Valid values: PayOnDemand and PrePay. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancers &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancersResponse>
      <PageNumber>1</PageNumber>
      <TotalCount>1</TotalCount>
      <PageSize>50</PageSize>
      <LoadBalancers>
            <LoadBalancer>
                  <CreateTimeStamp>1541679713000</CreateTimeStamp>
                  <LoadBalancerName>abc1</LoadBalancerName>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxaz*******y</ResourceGroupId>
                  <AddressIPVersion>ipv4</AddressIPVersion>
                  <LoadBalancerId>lb-bp1b6c********fuca5</LoadBalancerId>
                  <VSwitchId>vsw-bp12mw1f********bmlj</VSwitchId>
                  <InternetChargeType>4</InternetChargeType>
                  <VpcId>vpc-bp1aevy8*********5cm</VpcId>
                  <SlaveZoneId>cn-hangzhou-d</SlaveZoneId>
                  <NetworkType>vpc</NetworkType>
                  <MasterZoneId>cn-hangzhou-b</MasterZoneId>
                  <CreateTime>2018-11-08T20:21Z</CreateTime>
                  <Address>192.168.0.**</Address>
                  <RegionId>cn-hangzhou</RegionId>
                  <AddressType>intranet</AddressType>
                  <PayType>PayOnDemand</PayType>
                  <LoadBalancerStatus>active</LoadBalancerStatus>
            </LoadBalancer>
      </LoadBalancers>
      <RequestId>1C7445CB-C21C-4C19-9A3C-65C3190D1944</RequestId>
</DescribeLoadBalancersResponse>
```

`JSON` format `{`

```json
    "DescribeLoadBalancersResponse": {
        "PageNumber": 1,
        "TotalCount": 1,
        "PageSize": 50,
        "LoadBalancers": {
            "LoadBalancer": {
                "CreateTimeStamp": 1541679713000,
                "LoadBalancerName": "abc1",
                "RegionIdAlias": "cn-hangzhou",
                "ResourceGroupId": "rg-acfmxaz*******y",
                "AddressIPVersion": "ipv4",
                "LoadBalancerId": "lb-bp1b6c********fuca5",
                "VSwitchId": "vsw-bp12mw1f********bmlj",
                "InternetChargeType": 4,
                "VpcId": "vpc-bp1aevy8*********5cm",
                "SlaveZoneId": "cn-hangzhou-d",
                "NetworkType": "vpc",
                "MasterZoneId": "cn-hangzhou-b",
                "CreateTime": "2018-11-08T20:21Z",
                "Address": "192.168.0.**",
                "RegionId": "cn-hangzhou",
                "AddressType": "intranet",
                "PayType": "PayOnDemand",
                "LoadBalancerStatus": "active"
```

`}` `},`

```json
        "RequestId": "1C7445CB-C21C-4C19-9A3C-65C3190D1944"
```

`}` `}`

#### 2.4.9 DescribeRegions

Queries regions. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Regions | Array of Region |   | The list of regions. |

|   | Developer Guide·AP | I Reference |   | Server Load Balance | r |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Region |   |   |   |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region. |
| LocalName | String | China (Qingdao) | The name of the region. |
| RequestId | String | 1651FBB6-4FBF- 49FF-A9F5- DF5D696C7EC6 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRegions &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6</RequestId> <Regions>
    <Region>
        <RegionId>cn-beijing</RegionId>
        <LocalName>China (Beijing)</LocalName>
    </Region>
</Regions>
```

`JSON` format `{`

```json
    "RequestId": "1651FBB6-4FBF-49FF-A9F5-DF5D696C7EC6",
    "Regions": {
        "Region": {
            "RegionId": "cn-beijing",
            "LocalName": "China (Beijing)"
```

`}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Acquire the permissions and try again. |

#### 2.4.10 DescribeZones

Queries zones in a specified region. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array of Zone |   | The list of zones. |
| Zone |   |   |   |
| ZoneId | String | cn-hangzhou-b | The ID of the zone. |
| LocalName | String | Hangzhou Zone | The name of the zone. |
| SlaveZones | Array of SlaveZone |   | The list of secondary zones. |
| SlaveZone |   |   |   |
| ZoneId | String | cn-hangzhou-g | The ID of the secondary zone. |
| LocalName | String | Hangzhou Zone G | The name of the secondary zone. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A48D35FF-440A- 4BC0-A4A2- A9BF69B7E43A | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeZones &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeZonesResponse>
  <RequestId>3FF183FF-F4AA-40E8-8B5D-90788C6799C2</RequestId>
   <Zones>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
               <LocalName>Hangzhou Zone D</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <LocalName>Hangzhou Zone B</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
               <LocalName>Hangzhou Zone E</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-d</ZoneId>
         <LocalName>Hangzhou Zone D</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-f</ZoneId>
               <LocalName>Hangzhou Zone F</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-d</ZoneId>
               <LocalName>Hangzhou Zone D</LocalName>
```

`g` `/`

```xml
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <LocalName>Hangzhou Zone E</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-e</ZoneId>
               <LocalName>Hangzhou Zone E</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <LocalName>Hangzhou Zone F</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-h</ZoneId>
               <LocalName>Hangzhou Zone H</LocalName>
            </SlaveZone>
            <SlaveZone>
               <ZoneId>cn-hangzhou-b</ZoneId>
               <LocalName>Hangzhou Zone B</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-g</ZoneId>
         <LocalName>Hangzhou Zone G</LocalName>
      </Zone>
      <Zone>
         <SlaveZones>
            <SlaveZone>
               <ZoneId>cn-hangzhou-g</ZoneId>
               <LocalName>Hangzhou Zone G</LocalName>
            </SlaveZone>
         </SlaveZones>
         <ZoneId>cn-hangzhou-h</ZoneId>
         <LocalName>Hangzhou Zone H</LocalName>
      </Zone>
   </Zones>
</DescribeZonesResponse>
```

`JSON` format `{`

```json
    "DescribeZonesResponse": {
        "RequestId": "3FF183FF-F4AA-40E8-8B5D-90788C6799C2",
        "Zones": {
            "Zone": [
```

`{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{` `"Z`

```
Id"
```

`"` `h` `h` `"`

```json
                                "ZoneId": "cn-hangzhou-g",
                                "LocalName": "Hangzhou Zone G"
```

`},` `{`

```json
                                "ZoneId": "cn-hangzhou-d",
                                "LocalName": "Hangzhou Zone D"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-b",
                    "LocalName": "Hangzhou Zone B"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
                            "LocalName": "Hangzhou Zone E"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-d",
                    "LocalName": "Hangzhou Zone D"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{`

```json
                                "ZoneId": "cn-hangzhou-f",
                                "LocalName": "Hangzhou Zone F"
```

`},` `{`

```json
                                "ZoneId": "cn-hangzhou-d",
                                "LocalName": "Hangzhou Zone D"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-e",
                    "LocalName": "Hangzhou Zone E"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-e",
                            "LocalName": "Hangzhou Zone E"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-f",
                    "LocalName": "Hangzhou Zone F"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": [
```

`{`

```json
                                "ZoneId": "cn-hangzhou-h",
                                "LocalName": "Hangzhou Zone H"
```

`}` `},` `{`

```json
                                "ZoneId": "cn-hangzhou-b",
                                "LocalName": "Hangzhou Zone B"
```

`}` `]` `},`

```json
                    "ZoneId": "cn-hangzhou-g",
                    "LocalName": "Hangzhou Zone G"
```

`},` `{`

```json
                    "SlaveZones": {
                        "SlaveZone": {
                            "ZoneId": "cn-hangzhou-g",
                            "LocalName": "Hangzhou Zone G"
```

`}` `},`

```json
                    "ZoneId": "cn-hangzhou-h",
                    "LocalName": "Hangzhou Zone H"
```

`}` `]` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | Illegal parameter, query.namespace is not auth. | The error message returned because you are unauthorized to perform the operation. Request the permissions and try again. |

### 2.5 Listeners

#### 2.5.1 TCP listeners

##### 2.5.1.1 CreateLoadBalancerTCPListener

Creates a TCP listener. Not e Newly created listeners are in the Stopped state. After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerTCPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerT CPList ener. |
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit of each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. Not e Only high- performance SLB instances support the sch and tch consistent hashing algorithms. |
| PersistenceTimeo ut | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 t o 3600. Unit: seconds. Default value: 0. By default, session persistence is disabled. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. |
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period of a health check response. Valid values: 1 t o 300. Unit: seconds. Default value: 5. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 t o 65535. If you do not set this parameter, the port of the backend server is used for health checks. |
| healthCheckInterv al | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.),and hyphens (-). |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter to enable HTTP health checks for the TCP listener. If this parameter is not set, TCP health checks are performed. |
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. Default _ _ value: http 2xx. _ |
| HealthCheckType | String | No | tcp | The type of health checks. Valid values: t cp and ht t p. Default value: tcp. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterSlaveServe rGroupId | String | No | rsp-0bfucw**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| EstablishedTimeo ut | Integer | No | 500 | The timeout period of a connection. Valid values: 10 t o 900. Unit: seconds. |
| Description | String | No | CreateListeners. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain Chinese _ characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerTCPListener &Bandwidth=-1 &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerTCPListenerResponse>
     <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</CreateLoadBalancerTCPListenerResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.VServerGroupId AndMasterSlaveServ erGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the VServerGroupId parameter or the MasterSlaveServerGroupId parameter does not match. |

##### 2.5.1.2 SetLoadBalancerTCPListenerAttribute

Modifes the configurations of a TCP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer TCPListenerAttrib ute | The operation that you want to perform. Set the value to Set LoadBalancerT CPList enerAt t rib ut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | 43 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1 and 1 t o 5120. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 t o 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify the bandwidth limit of each listener. The sum of bandwidth limit values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. Not e Only high- performance SLB instances support the sch and tch consistent hashing algorithms. |
| PersistenceTimeo ut | Integer | No | 0 | The timeout period of session persistence. Valid values: 0 to 3600. Unit: seconds. Default value: 0. If you set the value to 0, session persistence is disabled. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 to 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 to 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the health check fails. Valid values: 1 to 300. Unit: seconds. Not e If the value of the Healt hCheckConnect T imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the HCT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. If this parameter is not set, the port specified in BackendServerPort is used for health checks. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. $ ip: The private IP address of the _ backend server. If you do not set this parameter or set the parameter to $ ip, the SLB _ instance uses the private IP address of each backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). You can set this parameter when the TCP listener requires HTTP health checks. If you do not set this parameter, TCP health checks are performed. ) |
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ |
| HealthCheckType | String | No | tcp | The type of health checks. Valid values: t cp and ht t p. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SynProxy | String | No | enable | Specifies whether to enable SynProxy to protect backend servers against attacks. We recommend that you use the default value for this parameter. Valid values: enable and disable. |
| MaxConnection | Integer | No | 20 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| VServerGroupId | String | No | rsp-cige6j5**** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-cige**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| MasterSlaveServe rGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and of f . You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| EstablishedTimeo ut | Integer | No | 500 | The timeout period of connections. Valid values: 10 to 900. Unit: seconds. |
| Description | String | No | test | The description of the TCP listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerTCPListenerAttributeResponse>
     <RequestId>59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1</RequestId>
</SetLoadBalancerTCPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "59B41B53-BC4B-481A-9D8D-2A0D20B3FCD1"
```

`}`

##### 2.5.1.3 DescribeLoadBalancerTCPListenerAttribute

Queries the configurations of a TCP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerTCPListenerA ttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerT CPList enerA t t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| eveloper Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y**** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. Not e When the SLB instance uses a vServer group, this parameter is not displayed. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet- facing SLB instance, this value is set to -1. This indicates that the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, a bandwidth limit is set for each listener. The sum of bandwidth limit values that are set for all listeners of an SLB instance does not exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: indicates that the listener runs as expected. st opped: indicates that the listener is stopped. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| SynProxy | String | enable | Indicates whether SynProxy is enabled. SynProxy is a feature that protects SLB from attacks. We recommend that you use the default value for this parameter. Valid values: Enable: SynProxy is enabled. Disable: SynProxy is disabled. |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| PersistenceTim eout | Integer | 0 | Indicates whether session persistence is enabled. If the value is set to 0, it indicates that session persistence is disabled. |
| HealthCheckTy pe | String | tcp | The health check method that is used by the TCP listener. Valid values: t cp and ht t p. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. |

|   | Parameter | Type |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | HealthCheckInt erval | Integer |   | 5 | The interval between two consecutive health checks. Unit: seconds. |   |   |
|   | HealthCheckDo main | String |   | www.domain.com | The domain name that is used for health checks. |   |   |
|   | HealthCheckURI | String |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), |   |   |
|   |   |   |   |   |   | hyphens (-), forward slashes (/), |   |
|   |   |   | ing | /test/index.html | periods (.),%?number signs (#), and |   |   |
|   |   |   |   |   | ampersands (&) |   |   |
|   | HealthCheckHtt pCode | String |   | http 2xx _ | The HTTP status code that indicates a successful health check. Valid values: ht t p 2xx, ht t p 3xx, ht t p 4xx, and _ _ _ ht t p 5xx. Default value: http 2xx. _ _ |   |   |
|   | VServerGroupId | String |   | rsp-cige6******8 | The ID of the associated vServer group. |   |   |
|   | Description | String |   | Description. | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain _ Chinese characters. |   |   |
|   | EstablishedTim eout | Integer |   | 500 | The timeout period of connections. Valid values: 10 t o 900. Unit: seconds. |   |   |
|   | HealthCheckCo nnectTimeout | Integer |   | 100 | The timeout period of a health check response. |   |   |
|   | MasterSlaveSer verGroupId | String |   | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |   |   |
|   | MaxConnection | Integer |   | 10 | The maximum number of connections. |   |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerTCPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerTCPListenerAttributeResponse>
     <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
   <PersistenceTimeout>0</PersistenceTimeout>
   <HealthCheckType>tcp</HealthCheckType>
   <HealthyThreshold>3</HealthyThreshold>
   <Scheduler>wrr</Scheduler>
   <UnhealthyThreshold>3</UnhealthyThreshold>
   <Bandwidth>-1</Bandwidth>
   <Description>tcp_80</Description>
   <AclStatus>off</AclStatus>
   <HealthCheckURI>/</HealthCheckURI>
   <HealthCheck>on</HealthCheck>
   <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout>
   <ListenerPort>80</ListenerPort>
   <Status>running</Status>
   <EstablishedTimeout>900</EstablishedTimeout>
   <HealthCheckDomain></HealthCheckDomain>
   <HealthCheckInterval>2</HealthCheckInterval>
   <RequestId>9A113A8C-BB8F-475E-9533-7819ECA2FFC1</RequestId>
   <BackendServerPort>80</BackendServerPort>
    </DescribeLoadBalancerTCPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "PersistenceTimeout": 0,
    "HealthCheckType": "tcp",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "UnhealthyThreshold": 3,
    "Bandwidth": -1,
    "Description": "tcp_80",
    "AclStatus": "off",
    "HealthCheckURI": "/",
    "HealthCheck": "on",
    "HealthCheckConnectTimeout": 5,
    "ListenerPort": 80,
    "Status": "running",
    "EstablishedTimeout": 900,
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "RequestId": "9A113A8C-BB8F-475E-9533-7819ECA2FFC1",
    "BackendServerPort": 80
```

`}`

#### 2.5.2 UDP listeners

##### 2.5.2.1 CreateLoadBalancerUDPListener

Creates a UDP listener. Not e You cannot view the source IP addresses of network traffic if you create UDP listeners for a Server Load Balancer (SLB) instance that is deployed in a classic network. In addition, newly created listeners are in the st opped state. After a listener is created, you must call the StartLoadBalancerListener operation to enable the listener. This way, the listener can forward network traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerUDPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerUDPList ener. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | 34 | The bandwidth limit of the listener. Unit: Mbit/s. Set the value to -1.For a pay-by-data- transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1ygod3yctvg1 y7**** | The ID of the SLB instance. |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. qch: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Not e Only high- performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 t o 300. Unit: seconds. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 t o 65535. If you do not specify this parameter, the backend port is used to send health check probes. |
| healthCheckInterv al | Integer | No | 3 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. |
| healthCheckReq | String | No | hello | Specifies the request string for UDP listener health checks. The request string must be 1 to 500 characters in length, and can contain only letters and digits. |
| healthCheckExp | String | No | ok | Specifies the response string for UDP listener health checks. The response string must be 1 to 500 characters in length, and can contain only letters and digits. |
| VServerGroupId | String | No | rsp-cige6j****8 | The ID of the vServer group. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| MasterSlaveServe rGroupId | String | No | rsp-0bfucwu**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| Description | String | No | test | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain Chinese _ characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerUDPListener &Bandwidth=34 &ListenerPort=80 &LoadBalancerId=lb-bp1ygod3yctvg1y7****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerUDPListenerResponse>
      <RequestId>06F00FBB-3D9E-4CCE-9D43-1A6946A75456</RequestId>
</CreateLoadBalancerUDPListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "06F00FBB-3D9E-4CCE-9D43-1A6946A75456"
```

`}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | Abs.VServerGroupId AndMasterSlaveServ erGroupId.MissMatch | The parameters VServerGroupId or MasterSlaveServerGroupId miss match. | The error message returned because the VServerGroupId parameter or the MasterSlaveServerGroupId parameter does not match. |

##### 2.5.2.2 SetLoadBalancerUDPListenerAttribute

Modifies the configurations of a UDP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer UDPListenerAttrib ute | The operation that you want to perform. Set the value to Set LoadBalancerUDPList enerAt t rib ut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb4 3ecu4sf-c**** | The ID of the SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | No | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: 1 t o 5120 and -1. -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 t o 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify a value as the bandwidth limit for each listener. The sum of maximum bandwidth values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. For more information, see Bandwidth limit of a shared- resource SLB instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. sch: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server. t ch: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server. qch: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server. Not e Only high- performance SLB instances support the sch, tch, and qch consistent hashing algorithms. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 to 10. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 to 10. |
| HealthCheckConn ectTimeout | Integer | No | 100 | The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 to 300. Not e If the value of the Healt hCheckConnect T imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCheckConnect T imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is regarded as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 80 | The port that is used for health checks. Valid values: 1 to 65535. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |
| healthCheckReq | String | No | hello | The request string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| healthCheckExp | String | No | ok | The response string for UDP listener health checks. The string must be 1 to 500 characters in length and can contain only letters and digits. |
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . Not e You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| VServerGroupId | String | No | rsp-cige6**** | The ID of the vServer group. |
| MasterSlaveServe rGroupId | String | No | rsp-0bfuc**** | The ID of the primary/secondary server group. Not e You cannot specify both VServerGroupId and MasterSlaveServerGroupId. |
| MasterSlaveServe rGroup | String | No | on | Specifies whether to use a primary/secondary server group. Valid values: on and of f . You cannot set both VserverGroup and Mast erSlaveServerGroup to on. |
| Description | String | No | test | The description of the listener. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43ecu4sf-c**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerUDPListenerAttributeResponse>
     <RequestId>A0F0643E-D653-4F6F-A67F-205B2A92BE18</RequestId>
</SetLoadBalancerUDPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "A0F0643E-D653-4F6F-A67F-205B2A92BE18"
```

`}`

##### 2.5.2.3 DescribeLoadBalancerUDPListenerAttribute

Queries the configurations of a UDP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerUDPListenerA ttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerUDPList ener At t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| LoadBalancerId | String | Yes | lb- bp1rtfnodmywb4 3e**** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 53 | The backend port that is used by the SLB instance. Not e If the listener is associated with a vServer group, this parameter is not returned. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet- facing SLB instance, this value is set to -1. This indicates that the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, each listener has a bandwidth limit. The sum of bandwidth limit values that are set for all listeners of an SLB instance does not exceed the bandwidth limit of the SLB instance. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: indicates that the listener runs as expected. st opped: indicates that the listener is stopped. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckCo nnectTimeout | Integer | 100 | The timeout period for a health check response. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Unit: seconds. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group that is associated with the listener. |
| Description | String | AccessControlDescri ption. | The description of access control. |
| HealthCheckExp | String | ok | The response string for UDP listener health checks. |

| S | erver Load Balanc | er |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckRe q | String | hello | The request string for UDP listener health checks. |
| MasterSlaveSer verGroupId | String | rsp-0bfucw**** | The ID of the primary/secondary server group that is associated with the listener. |
| MaxConnection | Integer | 10 | The maximum number of connections. |
| PersistenceTim eout | Integer | 0 | The timeout period of session persistence. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerUDPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1rtfnodmywb43e**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerUDPListenerAttributeResponse>
    <AclStatus>off</AclStatus>
    <HealthCheck>on</HealthCheck>
    <HealthCheckConnectTimeout>5</HealthCheckConnectTimeout>
    <PersistenceTimeout>0</PersistenceTimeout>
    <ListenerPort>80</ListenerPort>
    <Status>stopped</Status>
    <Scheduler>wrr</Scheduler>
    <HealthyThreshold>3</HealthyThreshold>
    <HealthCheckInterval>2</HealthCheckInterval>
    <RequestId>9C103591-2533-432B-9E6B-6DB098C0E65C</RequestId>
    <UnhealthyThreshold>3</UnhealthyThreshold>
    <BackendServerPort>34</BackendServerPort>
    <Bandwidth>67</Bandwidth>
</DescribeLoadBalancerUDPListenerAttributeResponse>
```

`JSON` format `{`

```json
 "AclStatus":"off",
 "HealthCheck":"on",
 "HealthCheckConnectTimeout":5,
 "PersistenceTimeout":0,
 "ListenerPort":80,
 "Status":"stopped",
 "Scheduler":"wrr",
 "HealthyThreshold":3,
 "HealthCheckInterval":2,
 "RequestId":"9C103591-2533-432B-9E6B-6DB098C0E65C",
 "UnhealthyThreshold":3,
 "BackendServerPort":34,
 "Bandwidth":67
```

`}`

#### 2.5.3 HTTP listeners

##### 2.5.3.1 CreateLoadBalancerHTTPListener

Creates an HTTP listener. Not e Newly created listeners are in the st opped state. After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerHTTPListener | The operation that you want to perform. Set the value to Creat eLoadBalancerHT T PList ener. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: If you set the value to -1, the bandwidth of the listener is unlimited. 1 t o 5120: If you set a value from 1 to 5120, the value that you specify equals the bandwidth limit of the listener. The sum of bandwidth limit values that you specify for all listeners of the Server Load Balancer (SLB) instance cannot exceed the bandwidth limit of the SLB instance. Not e This parameter applies only to mainland China. |
| HealthCheck | String | Yes | on | Specifies whether to enable health checks. Valid values: on and of f . |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1c9vixxjh92q83 tw**** | The ID of the SLB instance. |
| StickySession | String | Yes | off | Specifies whether to enable session persistence. Valid values: on and of f . |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. Not e If the VServerGroupId parameter is not set, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |

| X- |   |
|---|---|

|   | Forwarded-For |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will forward the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

|   | Parameter | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes |   |
|   |   |   |   |   |   |   | hyphens (-), forward slashes |
|   |   |   |   |   |   | (/), periods (.),%?number signs |   |
|   |   |   |   |   |   | (#), and ampersands (&) |   |
|   | HealthCheckURI | String | No |   | /test/index.html |   |   |
|   | HealthyThreshold | Integer | No |   | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 t o 300. Unit: seconds. Not e If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is invalid and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckConn ectPort | Integer | No | 80 | The backend port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Default value: ht t p 2xx. _ Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . Default value: off. |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . Default value: off. |

|   | IP |
|---|---|

|   | ID |
|---|---|

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
|   |   |   |   |   | X- |   |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Default value: on. Valid values: on and of f . Default value: off. |   |   |
| IdleTimeout | Integer | No | 3 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |   |   |
| RequestTimeout | Integer | No | 6 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
| ListenerForward | String | No | off | Specifies whether to enable HTTP-to- HTTPS redirection. Valid values: on and of f . |   |   |
| ForwardPort | Integer | No | 443 | The listening port that is used to redirect HTTP requests to HTTPS. |   |   |

|   | Forwarded-Proto |
|---|---|

|   | 504 |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | ListenerDescriptio n | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain Chinese _ characters. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPListener &HealthCheck=off &ListenerPort=80 &LoadBalancerId=lb-bp1c9vixxjh92q83tw***** &StickySession=off &BackendServerPort=80 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerHTTPListenerResponse>
   <RequestId>1FF504CB-BFFF-4508-A51A-58A416604FC8</RequestId>
</CreateLoadBalancerHTTPListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "1FF504CB-BFFF-4508-A51A-58A416604FC8"
```

`}`

##### 2.5.3.2 SetLoadBalancerHTTPListenerAttribute

Modifies the configurations of an HTTP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer HTTPListenerAttri bute | The operation that you want to perform. Set the value to Set LoadBalancerHT T PList enerAt t ri but e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a h**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: For a pay-by-data-transfer Internet-facing SLB instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and of f . |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites a cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will forward the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 to 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and of f . |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is specified or the HealthCheckDomain parameter is not specified, the SLB instance uses the private IP address of the backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 to 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 to 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the health check fails. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 to 300. Unit: seconds. Not e If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is invalid and the value of the Healt hCheckInt erval parameter is used as the timeout period. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 to 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| MaxConnection | Integer | No | 10 | The maximum number of connections. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the server group. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . |

|   | IP |
|---|---|

|   | ID |
|---|---|

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . |   |   |
|   |   |   |   |   | X- |   |
| Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and of f . |   |   |
| IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |   |   |
| RequestTimeout | Integer | No | 3 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If no response is received from the backend server within the specified timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
| Description | String | No | test | The description of the listener. |   |   |

|   | Forwarded-Proto |
|---|---|

|   | 504 |
|---|---|

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1qjwo61pqz3ah**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerHTTPListenerAttributeResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPListenerAttributeResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### 2.5.3.3 DescribeLoadBalancerHTTPListenerAttribute

Queries the configurations of an HTTP listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerHTTPListener Attribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHT T PList ene rAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5**** | The ID of the SLB instance. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1: If the value is set to -1, this indicates that the bandwidth of the listener is unlimited. 1 t o 5120: If a value from 1 to 5120 is set, the specified value indicates the bandwidth limit of the listener. The sum of bandwidth limit values that are specified for all listeners of the SLB instance must not exceed the bandwidth limit of the SLB instance. Not e This parameter applies only to mainland China. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. running: The listener runs as expected. st opped: The listener is stopped. |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is added to obtain the real IP address of the client. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr: Backend servers that have higher weights receive more requests than backend servers that have lower weights. This is the default value. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and of f . Default value: off. |
| StickySessionTy pe | String | insert | The method that is used to handle a cookie. Valid values: insert and server. insert : inserts a cookie into the response. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user- defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Not e If the St ickySession parameter is set to on, this parameter is required. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Cookie | String | B490B5EBF6F3CD402 E515D22BCDA1598 | The cookie that is configured on the backend server. The value is 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($). |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthCheckDo main | String | www.domain.com | The domain name that is used for health checks. |
| HealthCheckURI | String | /test/index.html | The URL that is used for health checks. The URL is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). ) |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckTi meout | Integer | 3 | The timeout period of a health check response. Valid values: 1 to 300. Unit: seconds. |
| HealthCheckInt erval | Integer | 5 | The interval between two consecutive health checks. Valid values: 1 to 50. Unit: seconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckHtt pCode | String | http 2xx _ | The HTTP status code that indicates a successful health check. Multiple HTTP status codes are separated by commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. Default value: _ _ http 2xx. _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| VServerGroupId | String | rsp-cige6j**** | The ID of the associated vServer group. |
| Gzip | String | on | Indicates whether gzip compression is enabled to compress specific types of files. Valid values: on and of f . |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. |
| Description | String | test | The description of the HTTP listener. The description is 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| ForwardPort | Integer | 80 | The listening port that is used to redirect HTTP requests to HTTPS. Not e If the value of the List enerForward parameter is set to of f , this parameter is not displayed. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| IdleTimeout | Integer | 2 | The timeout period of an idle connection. Valid values: 1 t o 60. Unit: seconds. Default value: 15. If no request is received within the specified timeout period, SLB closes the connection. SLB starts a new connection when it receives a new connection request. |
| ListenerForwar d | String | on | Indicates whether HTTP-to-HTTPS redirection is enabled. Valid values: on: enabled of f : disabled |
| MaxConnection | Integer | 10 | The maximum number of connections. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeou t | Integer | 34 | The timeout period of a request. Valid values: 1 t o 180. Unit: seconds. Default value: 60. If no response is received from the backend server within the timeout period, SLB returns an HTTP 504 error to the client. |
| SecurityStatus | String | on | The security status. Valid values: on and of f . |
| XForwardedFor SLBID _ | String | on | Indicates whether the SLB-ID header is added to obtain the ID of the SLB instance. |
| XForwardedFor SLBIP _ | String | on | Indicates whether the SLB-IP header is added to obtain the real IP address of the client. |
| XForwardedFor proto _ | String | on | Indicates whether the X-Forwarded- Proto header is added to obtain the listener protocol of the SLB instance. |

|   | Proto |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5********* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerHTTPListenerAttributeResponse>
    <ForwardPort>443</ForwardPort>
    <ListenerPort>80</ListenerPort>
    <Status>stopped</Status>
    <RequestId>99439CEF-192C-4B01-A45A-2D5BD5BCDA62</RequestId>
    <ListenerForward>on</ListenerForward>
</DescribeLoadBalancerHTTPListenerAttributeResponse>
```

`JSON` format `{`

```json
    "ForwardPort": 443,
    "ListenerPort": 80,
    "Status": "stopped",
    "RequestId": "99439CEF-192C-4B01-A45A-2D5BD5BCDA62",
    "ListenerForward": "on"
```

`}`

#### 2.5.4 HTTPS listeners

##### 2.5.4.1 CreateLoadBalancerHTTPSListener

Creates an HTTPS listener. Not e Newly created listeners are in the Stopped state. After a listener is created, you can call the `StartLoadBalancerListener` operation to enable the listener to forward traffic. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLoadBalan cerHTTPSListener | The operation that you want to perform. Set the value to Creat eLoadBalancerHT T PSList ener. |

| Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|
| Bandwidth | Integer | Yes | -1 | The bandwidth limit of the listener. Unit: Mbit/s. Valid values: -1 and 1 t o 5120. -1: For a pay-by-data-transfer Internet-facing Server Load Balancer (SLB) instance, you can set the value to -1. If you set the value to -1, the bandwidth is unlimited. 1 to 5120: For a pay-by-bandwidth Internet-facing SLB instance, you can specify a value as the bandwidth limit for each listener. The sum of maximum bandwidth values that you set for all listeners cannot exceed the bandwidth limit of the SLB instance. |   |   |
| HealthCheck | String | Yes | on | Specifies whether to enable health checks. Valid values: on and of f . |   |   |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |   |   |
| LoadBalancerId | String | Yes | lb- bp1o94dp5i6earr **** | The ID of the SLB instance. |   |   |
| StickySession | String | Yes | on | Specifies whether to enable session persistence. Valid values: on and of f . |   |   |
| BackendServerPor t | Integer | No | 80 | The backend port that is used by the SLB instance. Valid values: 1 t o 65535. If the VServerGroupId parameter is not set, this parameter is required. |   |   |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Set the value to on. |   |   |
|   |   |   |   |   | X- |   |

|   | Forwarded-For |
|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. If you set the StickySession parameter to on, you must specify this parameter. Valid values: insert and server. insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server. server:rewrites a cookie. When the SLB instance detects a user-defined cookie, it rewrites the original cookie with the user-defined cookie. The next request from the client contains the user-defined cookie, and the listener distributes the request to the recorded backend server. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie to be configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If you do not set this parameter or set the parameter to $ ip, the SLB instance uses the _ private IP address of each backend server as the domain name for health checks. domain: The domain name must be 1 to 80 characters in length and can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter |   | Type | Required |   | Example | Description |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | The URL that is used for health checks. The value must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward |   |   |
|   |   |   |   |   |   |   | hyphens (-), forward |   |
|   |   |   |   |   |   | slashes (/), periods (.),%? |   |   |
|   |   |   |   |   |   | number signs (#), and ampersands |   |   |
|   |   |   |   |   |   | (&) |   |   |
| HealthCheckURI |   | String | No |   | /test/index.html |   |   |   |
| HealthyThreshold |   | Integer | No |   | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |
| UnhealthyThresh old |   | Integer | No |   | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy. (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |   |   |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the health check fails. This parameter takes effect only when the Healt hCheck parameter is set to on. Valid values: 1 t o 300. Unit: seconds. If the value of the Healt hCHeckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCHeckT imeout parameter is invalid and the value of the Healt hCheckInt erval parameter is used as the timeout period. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50 . Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckHttpC ode | String | No | http 2xx _ | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Default value: ht t p 2xx. _ Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificateI d | String | No | idkp-123-cn-test- **** | The ID of the server certificate. |
| VServerGroupId | String | No | rsp- cige6j5e7p**** | The ID of the vServer group. |
| CACertificateId | String | No | 139a00604ad-cn- east-hangzh**** | The ID of the CA certificate. Two-factor authentication: upload a CA certificate and a server certificate. Single-factor authentication: upload only a server certificate. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . Default value: off. |

|   | IP |
|---|---|

|   | Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
|   | XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . Default value: off. |   |   |
|   |   |   |   |   |   | X- |   |
|   | Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and of f . Default value: off. |   |   |
|   | IdleTimeout | Integer | No | 12 | The timeout period of an idle connection. Valid values: 1 t o 60. Default value: 15. Unit: seconds. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |   |   |
|   | RequestTimeout | Integer | No | 23 | The timeout period of a request. Valid values: 1 t o 180. Default value: 60. Unit: seconds. If no response is received from the backend server during the timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
|   |   |   |   |   | You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes TLS protocol versions and cipher suites available for HTTPS. The following security policies are supported. For more information about the differences, see Differences in TLS security policies. |   |   |

|   | ID |
|---|---|

|   | Forwarded-Proto |
|---|---|

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | t ls cipher policy 1 0: Descri_ption _ _ _ Supported TLS versions: TLSv1.0, |
| TLSCipherPolicy | String | No | tls cipher policy _ _ _ 1 1 _ | TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA- AES256-SHA. |
| Document Version: | 20220928 |   |   | 14 |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Description | String | No | CreateListeners | The description of the listener. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateLoadBalancerHTTPSListener &Bandwidth=-1 &HealthCheck=on &ListenerPort=80 &LoadBalancerId=lb-bp1o94dp5i6earr***** &StickySession=on &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateLoadBalancerHTTPSListenerResponse>
   <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</CreateLoadBalancerHTTPSListenerResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### 2.5.4.2 SetLoadBalancerHTTPSListenerAttribute

Modifies the configurations of an HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetLoadBalancer HTTPSListenerAtt ribute | The operation that you want to perform. Set the value to Set LoadBalancerHT T PSList enerAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb-sjhfdji**** | The ID of the SLB instance. |
| Bandwidth | Integer | No | -1 | Specify the bandwidth limit of the listener. Valid values: 1 t o 5120 and -1. -1: If you set the value to -1, the bandwidth is unlimited. 1 t o 5120: If you set a value from 1 to 5120, the value that you specify equals the bandwidth limit of the listener. The sum of bandwidth limit values that you specify for all listeners of the SLB instance cannot exceed the bandwidth limit of the SLB instance. |
| XForwardedFor | String | No | on | Specifies whether to use the X- Forwarded-For header to obtain the real IP address of the client. Valid values: on and of f . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Scheduler | String | No | wrr | The scheduling algorithm. Valid values: wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | No | on | Specifies whether to enable session persistence. Valid values: on and of f . |
| StickySessionTyp e | String | No | insert | The method that is used to handle a cookie. Valid values: insert : inserts a cookie. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| CookieTimeout | Integer | No | 500 | The timeout period of a cookie. Valid values: 1 t o 86400. Unit: seconds. Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to insert , this parameter is required. |
| Cookie | String | No | B490B5EBF6F3CD4 02E515D22BCDA1 598 | The cookie that is configured on the backend server. The value must be 1 to 200 characters in length, and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($). Not e If you set the St ickySession parameter to on and the St ickySessionT ype parameter to server, this parameter is required. |
| HealthCheck | String | No | on | Specifies whether to enable health checks. Valid values: on and of f . |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckDom ain | String | No | 172.XX.XX.6 | The domain name that is used for health checks. Valid values: $ ip: The private IP address of the _ backend server. If the $ ip _ parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks. domain: The domain name must be 1 to 80 characters in length, and can contain only letters, digits, periods (.),and hyphens (-). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckURI | String | No | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must not be a single forward slash (/). However, it must start with a forward slash (/). Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthyThreshold | Integer | No | 4 | The number of health checks that an unhealthy backend server must consecutively pass before it can be declared healthy (from f ail to success). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| UnhealthyThresh old | Integer | No | 4 | The number of health checks that a healthy backend server must consecutively fail before it can be declared unhealthy (from success to f ail). Valid values: 2 t o 10. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckTime out | Integer | No | 3 | The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Valid values: 1 t o 300. Unit: seconds. Not e If the value of the Healt hCheckT imeout parameter is smaller than that of the Healt hCheckInt erval parameter, the value of the Healt hCheckT imeout parameter is ignored and the value of the Healt hCheckInt erval parameter is used as the timeout period. This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckInterv al | Integer | No | 5 | The interval between two consecutive health checks. Valid values: 1 t o 50. Unit: seconds. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| HealthCheckConn ectPort | Integer | No | 8080 | The port that is used for health checks. Valid values: 1 t o 65535. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| HealthCheckHttpC ode | String | No | http 2xx,http 3x _ _ x | The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: ht t p 2xx, ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificateI d | String | No | idkp-123-cn- te**** | The ID of the server certificate. |
| CACertificateId | String | No | 139a00604ad-cn- east-**** | The ID of the CA certificate. If both the CA certificate and the server certificate are uploaded, two- factor authentication is used. If you upload only the server certificate, single-factor authentication is used. |
| VServerGroup | String | No | on | Specifies whether to use a vServer group. Valid values: on and of f . |
| VServerGroupId | String | No | rsp-cige6j**** | The ID of the vServer group. |
| Tags | String | No | loadbalancerhttp s**** | The tags. |
| XForwardedFor S _ LBIP | String | No | on | Specifies whether to use the SLB- IP header to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor S _ LBID | String | No | on | Specifies whether to use the SLB- ID header to obtain the ID of the SLB instance. Valid values: on and of f . |

|   | IP |
|---|---|

|   | ID |
|---|---|

|   | Parameter | Type | Required | Example | Description |   |   |
|---|---|---|---|---|---|---|---|
|   | XForwardedFor p _ roto | String | No | on | Specifies whether to use the X- Forwarded-Proto header to obtain the listener protocol of the SLB instance. Valid values: on and of f . |   |   |
|   |   |   |   |   |   | X- |   |
|   | Gzip | String | No | on | Specifies whether to enable gzip compression to compress specific types of files. Valid values: on and of f . |   |   |
|   | IdleTimeout | Integer | No | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 t o 60. Default value: 15. If no request is received during the specified timeout period, the SLB instance closes the connection. When another request is received, the SLB instance establishes a new connection. |   |   |
|   | RequestTimeout | Integer | No | 223 | The timeout period of a request. Unit: seconds. Valid values: 1 t o 180. Default value: 60. If no response is received from the backend server during the specified timeout period, SLB sends an HTTP 504 error code to the client. |   |   |
|   |   |   |   |   | You can specify the TLSCipherPolicy parameter only for a high-performance SLB instance. Each security policy includes TLS protocol versions and cipher suites that are available for HTTPS. You can select a security policy based on your requirements. The following security policies are supported: t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. |   |   |

|   | Forwarded-Proto |
|---|---|

|   | Parameter | Type | Required |   | Example | Supported cipher suites: ECDHE- Description RSA-AES128-GCM-SHA256, ECDHE- |   |   |
|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, |   |   |
|   | TLSCipherPolicy | String | No |   | tls cipher policy _ _ _ 1 2 _ | ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- RSA-AES256-GCM-SHA384, ECDHE- RSA-AES128-SHA256, ECDHE-RSA- AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE- RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE- RSA-AES128-GCM-SHA256, ECDHE- |   |   |
|   | Description | String | No |   | ListenerDescriptio n | RSA-AES256-GCM-SHA384, ECDHE- The dReSsAc-rAipEtSio1n2 8o-fS tHhAe2 l5is6t,e EnCeDrH. TE-hReSA- description must be 2 to 256 AES256-SHA384, ECDHE-RSA- charaAcEteSr1s2 i8n- SleHnAg,t ahn. dIt EcCaDnH cEo-nRtSaAin- only characters in the following string: AES256-SHA. ^([^\x00-\xff]\|[\w.,;/@-]) {2,256}$ . |   |   |
|   |   |   |   |   |   |   | ^([^\x00-\xff]\|[\w.,;/@-]) |   |
|   |   |   |   |   |   | {2,256}$ |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-sjhfdji**************** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetLoadBalancerHTTPSListenerAttributeResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetLoadBalancerHTTPSListenerAttributeResponse>
```

`JSON` format `{`

```json
 "RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}`

##### 2.5.4.3 DescribeLoadBalancerHTTPSListenerAttribute

Queries the configurations of an HTTPS listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLoadBala ncerHTTPSListene rAttribute | The operation that you want to perform. Set the value to DescribeLoadBalancerHT T PSList en erAt t ribut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| erver Load Balancer |   |   |   | Developer Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |
| LoadBalancerId | String | Yes | lb- bp1mxu5r8lau*** * | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| BackendServerP ort | Integer | 80 | The backend port that is used by the SLB instance. |
| Bandwidth | Integer | -1 | The bandwidth limit of the listener. |
| Status | String | stopped | The state of the listener. Valid values: running and st opped. |
| XForwardedFor | String | on | Indicates whether the X-Forwarded-For header is used to obtain the real IP address of the client. Valid values: on and of f . |
| Scheduler | String | wrr | The scheduling algorithm. Valid values: wrr, wlc, and rr. wrr (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights. wlc: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests. rr: Requests are distributed to backend servers in sequence. |
| StickySession | String | on | Indicates whether session persistence is enabled. Valid values: on and of f . |

| Parameter | Type | Example | Description |
|---|---|---|---|
| StickySessionTy pe | String | insert | The method that is used to handle a cookie. If you set the StickySession parameter to on, this parameter is required. Valid values: insert and server. insert : inserts a cookie into the response. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will forward this request to the recorded backend server. server: rewrites the original cookie. When SLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user- defined cookie, and the listener will distribute the request to the recorded backend server. Not e If you set the St ickySession parameter to on, this parameter is required. |
| CookieTimeout | Integer | 500 | The timeout period of a cookie. |
| Cookie | String | B490B5EBF6F3CD402 E515D22BCDA1598 | The cookie configured on the backend server. |
| HealthCheck | String | on | Indicates whether health checks are enabled. Valid values: on and of f . |
| HealthCheckDo main | String | www.test.com | The domain name that is used for health checks. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| HealthCheckURI | String | /test/index.html | The URL that is used for health checks. The URL must be 1 to 80 characters in length and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL must start with a forward slash (/) but cannot contain only a forward slash (/). |
| HealthyThresho ld | Integer | 4 | The healthy threshold. |
| UnhealthyThres hold | Integer | 4 | The unhealthy threshold. |
| HealthCheckTi meout | Integer | 3 | The timeout period of a health check response. Unit: seconds. |
| HealthCheckInt erval | Integer | 5 | The time interval between two consecutive health checks. Unit: seconds. Valid values: 1 t o 50. |
| HealthCheckHtt pCode | String | http 2xx _ | The HTTP status code that indicates a successful health check. Multiple status codes are separated with commas (,). Valid values: ht t p 2xx (default), ht t p 3xx, _ _ ht t p 4xx, and ht t p 5xx. _ _ |
| HealthCheckCo nnectPort | Integer | 8080 | The port that is used for health checks. Not e This parameter takes effect only when the Healt hCheck parameter is set to on. |
| ServerCertificat eId | String | idkp-123-cn-test- **** | The ID of the server certificate. |
| CACertificateId | String | idkp-234-cn-test- **** | The ID of the CA certificate. |
| VServerGroupId | String | rsp-cige6j5e**** | The ID of the associated vServer group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Gzip | String | on | Indicates whether gzip compression is enabled. Valid values: on and of f . |
| Description | String | ListenerDescription | The description of the listener. The description must be 2 to 256 characters in length. It can contain only Chinese characters and characters in the following string: /^([^\x00-\xff]\|[\w.,;/@-]){2,256}$/. |
| IdleTimeout | Integer | 23 | The timeout period of an idle connection. Unit: seconds. Valid values: 1 to 60. Default value: 15. If no request is received during the specified timeout period, SLB closes the connection. When another request is received, SLB establishes a new connection. |
| MaxConnection | Integer | 10 |   |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |
| RequestTimeou t | Integer | 43 | The timeout period of a request. Unit: seconds. Valid values: 1 to 180. Default value: 60. If the backend server does not respond within the specified timeout period, SLB returns the HTTP 504 error code to the client. |
| SecurityStatus | String | on | The security status. Valid values: on and of f . |
|   |   |   | The security policy. You can specify the TLSCipherPolicy parameter only for a high- performance SLB instance. Each security policy includes different TLS protocol versions and cipher suites for HTTPS. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | The following security policies are Description supported. For more information about the |
| TLSCipherPolicy | String | tls cipher policy 1 _ _ _ _ 0 | differences, see Differences in TLS security policies. You can specify a security policy based on your requirements. Valid values: t ls cipher policy 1 0: _ _ _ _ Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 1: _ _ _ _ Supported TLS versions: TLSv1.1 and TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 2 _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM- SHA256, AES256-GCM-SHA384, AES128- SHA256, AES256-SHA256, ECDHE-RSA- AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3- SHA. t ls cipher policy 1 2 st rict _ _ _ _ _ Supported TLS version: TLSv1.2. Supported cipher suites: ECDHE-RSA- AES128-GCM-SHA256, ECDHE-RSA-AES256- GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA- AES128-SHA, and ECDHE-RSA-AES256-SHA. |

| Parameter | Type | Example | Description Indicates whether the SLB-ID header is |
|---|---|---|---|
| XForwardedFor SLBID _ | String | on | used to obtain the ID of the SLB instance. Valid values: on and of f . |
| XForwardedFor SLBIP _ | String | on | Indicates whether the SLB-IP header is used to obtain the real IP address of the client. Valid values: on and of f . |
| XForwardedFor proto _ | String | on | Indicates whether the X-Forwarded- Proto header is used to obtain the listener protocol of the SLB instance. Valid values: on and of f . |

|   | Proto |
|---|---|

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLoadBalancerHTTPSListenerAttribute &ListenerPort=80 &LoadBalancerId=lb-bp1mxu5r8lau******* &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeLoadBalancerHTTPSListenerAttributeResponse>
   <RequestId>11F52428-64ED-40F7-98C2-DBB6D0BB0AD7</RequestId>
      <HealthCheckHttpCode>http_2xx,http_3xx</HealthCheckHttpCode>
      <HealthCheckTimeout>5</HealthCheckTimeout>
      <ServerCertificateId>1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746</ServerCertifi
cateId>
      <XForwardedFor_SLBID>off</XForwardedFor_SLBID>
      <Gzip>on</Gzip>
      <HealthyThreshold>3</HealthyThreshold>
      <Scheduler>wrr</Scheduler>
      <StickySession>off</StickySession>
      <UnhealthyThreshold>3</UnhealthyThreshold>
      <XForwardedFor_SLBIP>off</XForwardedFor_SLBIP>
      <XForwardedFor_proto>off</XForwardedFor_proto>
      <Bandwidth>-1</Bandwidth>
      <HealthCheckURI>/</HealthCheckURI>
      <VServerGroupId>rsp-0xiju72x******</VServerGroupId>
      <HealthCheck>on</HealthCheck>
      <ListenerPort>443</ListenerPort>
      <Status>running</Status>
      <XForwardedFor>on</XForwardedFor>
      <HealthCheckDomain></HealthCheckDomain>
      <HealthCheckInterval>2</HealthCheckInterval>
      <BackendServerPort>443</BackendServerPort>
</DescribeLoadBalancerHTTPSListenerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "11F52428-64ED-40F7-98C2-DBB6D0BB0AD7",
    "HealthCheckHttpCode": "http_2xx,http_3xx",
    "HealthCheckTimeout": 5,
    "ServerCertificateId": "1231579xxxxxxxx_15dbf6ff26f_1991415478_2054196746",
    "XForwardedFor_SLBID": "off",
    "Gzip": "on",
    "HealthyThreshold": 3,
    "Scheduler": "wrr",
    "StickySession": "off",
    "UnhealthyThreshold": 3,
    "XForwardedFor_SLBIP": "off",
    "XForwardedFor_proto": "off",
    "Bandwidth": -1,
    "HealthCheckURI": "/",
    "VServerGroupId": "rsp-0xiju72x******",
    "HealthCheck": "on",
    "ListenerPort": 443,
    "Status": "running",
    "XForwardedFor": "on",
    "HealthCheckDomain": "",
    "HealthCheckInterval": 2,
    "BackendServerPort": 443
```

`}`

##### 2.5.4.4 DescribeHealthStatus

Queries the health status of backend servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHealthSt atus | The operation that you want to perform. Set the value to DescribeHealt hSt at us. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a h**** | The ID of the Server Load Balancer (SLB) instance. |
| ListenerPort | Integer | No | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. Not e If you do not specify this parameter, the health status of all ports is returned. |
| RegionId | String | Yes | cn-hangzhou | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i- bp1h5u3fv54ytf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerHealthSt atus | String | abnormal | The health status of the backend server: normal: The backend server is healthy. abnormal: The backend server is unhealthy. unavailable: The health check is not completed. |
| ListenerPort | Integer | 80 | The frontend port that is used by the SLB instance. |
| port | Integer | 80 |   |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeHealthStatus &LoadBalancerId=lb-bp1qjwo61pqz3ah**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeHealthStatusResponse>
  <RequestId>E69BA4CE-2B55-45EC-94CA-E47B16759459</RequestId>
  <BackendServers>
        <BackendServer>
              <ListenerPort>80</ListenerPort>
              <ServerId>i-bp1h5u3fv54ytf0******</ServerId>
              <Port>80</Port>
              <ServerIp>192.168.0.**</ServerIp>
              <ServerHealthStatus>abnormal</ServerHealthStatus>
              <Protocol>http</Protocol>
        </BackendServer>
        <BackendServer>
              <ListenerPort>8080</ListenerPort>
              <ServerId>i-bp1h5u3fv54ytf0******</ServerId>
              <Port>80</Port>
              <ServerIp>192.168.0.**</ServerIp>
              <ServerHealthStatus>abnormal</ServerHealthStatus>
              <Protocol>tcp</Protocol>
        </BackendServer>
  </BackendServers>
</DescribeHealthStatusResponse>
```

`JSON` format `{`

```json
    "RequestId": "E69BA4CE-2B55-45EC-94CA-E47B16759459",
    "BackendServers": {
        "BackendServer": [
```

`{`

```json
                "ListenerPort": 80,
                "ServerId": "i-bp1h5u3fv54ytf*****",
                "Port": 80,
                "ServerIp": "192.168.**.**",
                "ServerHealthStatus": "abnormal",
                "Protocol": "http"
```

`},` `{`

```json
                "ListenerPort": 8080,
                "ServerId": "i-bp1h5u3fv54ytf0******",
                "Port": 80,
                "ServerIp": "192.168.**.**",
                "ServerHealthStatus": "abnormal",
                "Protocol": "tcp"
```

`}` `]` `}` `}`

#### 2.5.5 Access control

##### 2.5.5.1 SetListenerAccessControlStatus

Enables or disables the whitelist of a specified listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetListenerAcces sControlStatus | The operation that you want to perform. Set the value to Set List enerAccessCont rolSt at us. |
| AccessControlSta tus | String | Yes | open white list _ _ | Specifies whether to enable the whitelist. Valid values: open whit e list : enables the _ _ whitelist. close: disables the whitelist. Not e After the whitelist is enabled, if no IP address is added to the whitelist, the Server Load Balancer (SLB) instance does not distribute network traffic. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetListenerAccessControlStatus &AccessControlStatus=open_white_list &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetListenerAccessControlStatusResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</SetListenerAccessControlStatusResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

##### 2.5.5.2 DescribeListenerAccessControlAttribute

Queries the whitelist configurations of a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeListenerA ccessControlAttri bute | The operation that you want to perform. Set the value to DescribeList enerAccessCont rolAt t r ibut e. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| LoadBalancerId | String | Yes | lb- 8vb86hxixo8****** *6jaz | The ID of the SLB instance. |
| Tags | String | No | listeneraccesscon trolslb**** | The tags. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessControlS tatus | String | open white list _ _ | Indicates whether the whitelist is enabled. Valid values: open whit e list : the whitelist is _ _ enabled. close: the whitelist is disabled. |
| SourceItems | String | 192.168.0.1 | The IP addresses or CIDR blocks that are added to the whitelist. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeListenerAccessControlAttribute &ListenerPort=80 &LoadBalancerId=lb-8vb86hxixo8*******6jaz &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeListenerAccessControlAttributeResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
   <AccessControlStatus>open_white_list</AccessControlStatus>
   <SourceItems>192.168.0.1</SourceItems>
</DescribeListenerAccessControlAttributeResponse>
```

`JSON` format

```json
{"AccessControlStatus":"open_white_list", "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710", "SourceItems":"192.168.0.1"}
```

##### 2.5.5.3 AddListenerWhiteListItem

Adds IP addresses to the whitelist of a listener. Request parameters

| Parameter | Type |   | Required | Example | Description |   |
|---|---|---|---|---|---|---|
| Action | String |   | Yes | AddListenerWhite ListItem | The operation that you want to perform. Set the value to AddList enerWhit eList It em. |   |
| ListenerPort | Integer |   | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |   |
| LoadBalancerId | String |   | Yes | 139a00604ad-cn- east-hangzhou- 01 | The ID of the SLB instance. |   |
| SourceItems | String |   | Yes | 1.XX.XX.1,1.XX.X X.0/21 | The IP addresses or CIDR blocks that you want to add to the whitelist. This parameter takes effect only when AccessCont rolSt at us of the listener is set to open whit e list . _ _ Separate multiple IP addresses or CIDR blocks with commas (,). You cannot enter 0.0.0.0 or 0.0.0.0/0. You can call the SetListenerAccessControlStatus operation to set the value of the AccessCont rolSt at us parameter to close. This indicates that access control is disabled. |   |
|   |   |   |   |   |   | SetListenerAccessControlStatus |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=139a00604ad-cn-east-hangzhou-01 &SourceItems=1.XX.XX.1,XX.XX.1.0/21 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddListenerWhiteListItemResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</AddListenerWhiteListItemResponse>
```

`JSON` format `{`

```json
    "AddListenerWhiteListItemResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` `}`

##### 2.5.5.4 RemoveListenerWhiteListItem

Removes IP addresses from the whitelist of a listener. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveListenerW hiteListItem | The operation that you want to perform. Set the value to RemoveList enerWhit eList It em. |
| ListenerPort | Integer | Yes | 80 | The listener port. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the Server Load Balancer (SLB) instance. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| SourceItems | String | Yes | 192.168.0.1/24 | The IP addresses or CIDR blocks to be removed. Separate multiple IP addresses or CIDR blocks with commas (,). Not e If all IP addresses are removed from the whitelist, the listener does not forward requests. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveListenerWhiteListItem &ListenerPort=80 &LoadBalancerId=lb-bp1b6c719dfa08ex**** &SourceItems=192.168.0.1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveListenerWhiteListItemResponse>
    <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</RemoveListenerWhiteListItemResponse>
```

`JSON` format

```json
{"RequestId":" CEF72CEB-54B6-4AE8-B225-F876FF7BA984"}
```

#### 2.5.6 DeleteLoadBalancerListener

Deletes a listener. Not e You can delete only listeners that are in the st opped or running state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLoadBalan cerListener | The operation that you want to perform. Set the value to Delet eLoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the Server Load Balancer (SLB) instance. Valid values: 1 t o 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5xm** ** | The ID of the SLB instance. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xm**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteLoadBalancerListenerResponse>
     <RequestId>791D8B68-AE0F-4174-AF54-088C8B3C5D54</RequestId>
  </DeleteLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "791D8B68-AE0F-4174-AF54-088C8B3C5D54"
```

`}`

#### 2.5.7 StopLoadBalancerListener

Disables a listener. When you call this operation, take note of the following items: If the operation is successful, the listener switches to the Stopped state. You cannot perform the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state. Not e After a listener is disabled, it stops forwarding requests to the associated backend servers. This may cause service interruptions. Proceed with caution. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StopLoadBalance rListener | The operation that you want to perform. Set the value to St opLoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5xmgl **** | The ID of the SLB instance. |
| Tags | String | No | null | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=StopLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5xmgl**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StopLoadBalancerListenerResponse>
     <RequestId>21D2B318-650E-4B0B-A3B5-693D462247B3</RequestId>
  </StopLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "21D2B318-650E-4B0B-A3B5-693D462247B3"
```

`}`

#### 2.5.8 StartLoadBalancerListener

Enables a listener. When you call this operation, take note of the following items: You can call the operation only when the listener is in the Stopped state. If the operation is successful, the state of the listener changes to Starting. You cannot call the operation when the Server Load Balancer (SLB) instance to which the listener belongs is in the Locked state. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartLoadBalance rListener | The operation that you want to perform. Set the value to St art LoadBalancerList ener. |
| ListenerPort | Integer | Yes | 80 | The frontend port that is used by the SLB instance. Valid values: 1 to 65535. |
| LoadBalancerId | String | Yes | lb- bp13jaf5qli5**** | The ID of the SLB instance. |
| Tags | String | No | {"tagKey":"Key1", "tagValue":"Valu e1"} | The key and value of the tag. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=StartLoadBalancerListener &ListenerPort=80 &LoadBalancerId=lb-bp13jaf5qli5**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<StartLoadBalancerListenerResponse>
     <RequestId>CC000321-00F2-49B8-9BCA-60D822414960</RequestId>
  </StartLoadBalancerListenerResponse>
```

`JSON` format `{`

```json
    "RequestId": "CC000321-00F2-49B8-9BCA-60D822414960"
```

`}`

### 2.6 Server certificates

#### 2.6.1 UploadServerCertificate

Uploads a server certificate. You can upload only one server certificate and its private key in each request. The request is successful only when the server certificate and its private key are both uploaded. If the server certificate or its private key is not uploaded, the request fails. After a server certificate and its private key are uploaded, the fingerprints of all server certificates that belong to your account are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadServerCert ificate | The operation that you want to perform. Set the value to UploadServerCert if icat e. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the server certificate is created. You can call the DescribeRegions operation to query region IDs. |
| AliCloudCertificat eId | String | No | 730912673****** _ 15d97e7709a 71 _ 445759hr 7892*** _ *** | The ID of the server certificate that is provided by Apsara Stack SSL Certificates Service. This parameter is required if you use a server certificate that is provided by Apsara Stack SSL Certificates Service. |
| AliCloudCertificat eName | String | No | testcertkey | The name of the server certificate that is provided by Apsara Stack SSL Certificates Service. |
| ServerCertificate | String | No | test | The public key certificate that you want to upload. Not e This parameter is required if you use a server certificate that is provided by a third party. |
| PrivateKey | String | No | wmsa**** | The private key that you want to upload. Not e This parameter is required if you use a server certificate that provided by a third party. |
| ServerCertificateN ame | String | No | mycert01 | The name of the server certificate that you want to upload. The name must be 1 to 80 characters in length and can contain digits, periods (.), underscores ( ), and _ hyphens (-). It must start with a letter. |
| Tags | String | No | ServerCertificate* *** | The tag that you want to add to the server certificate. |

| eveloper Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| StandardType | String | No | ServerCertificate | The type of the server certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerCertificat eId | String | xxxxidkp-123-cn- test**** | The ID of the server certificate. |
| ServerCertificat eName | String | mycert01 | The name of the server certificate. |
| Fingerprint | String | 01:DF:AB:** | The fingerprint of the server certificate. |
| AliCloudCertific ateId | String | 730912xxxxx 15d97 _ e7709a 71445759hr _ 7**** _ | The ID of the server certificate if the server certificate is provided by Apsara Stack SSL Certificates Service. |
| AliCloudCertific ateName | String | testcert**** | The name of the server certificate if the server certificate is provided by Apsara Stack SSL Certificates Service. |
| IsAliCloudCertifi cate | Integer | 0 | Indicates whether the server certificate is provided by Apsara Stack SSL Certificates Service. Valid values: 0: The server certificate is provided by a third-party CA. 1: The server certificate is provided by Apsara Stack SSL Certificates Service. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the server certificate is created. |
| RegionIdAlias | String | hangzhou | The name of the region where the server certificate is created. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UploadServerCertificate &RegionId=cn-east-hangzhou-01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UploadServerCertificateResponse>
      <RegionIdAlias>cn-east-hangzhou-01</RegionIdAlias>
      <Fingerprint>01:DF:AB:**</Fingerprint>
      <AliCloudCertificateName>testcert***</AliCloudCertificateName>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <IsAliCloudCertificate>0</IsAliCloudCertificate>
      <ServerCertificateId>xxxxidkp-123-cn-test******</ServerCertificateId>
      <ServerCertificateName>mycert01</ServerCertificateName>
      <RegionId>cn-hangzhou</RegionId>
      <AliCloudCertificateId>730912xxxxx_15d97e7709a_71445759hr_7*******</AliCloudCertifica
teId> </UploadServerCertificateResponse>
```

`JSON` format `{`

```json
    "UploadServerCertificateResponse": {
        "RegionIdAlias": "cn-east-hangzhou-01",
        "Fingerprint": "01:DF:AB:**",
        "AliCloudCertificateName": "testcert***",
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "IsAliCloudCertificate": 0,
        "ServerCertificateId": "xxxxidkp-123-cn-test******",
        "ServerCertificateName": "mycert01",
        "RegionId": "cn-hangzhou",
        "AliCloudCertificateId": "730912xxxxx_15d97e7709a_71445759hr_7*******"
```

`}` `}`

#### 2.6.2 DeleteServerCertificate

Deletes a server certificate. Not e You cannot delete a server certificate that is in use. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteServerCerti ficate | The operation that you want to perform. Set the value to Delet eServerCert if icat e. |
| ServerCertificateI d | String | Yes | 123157**** 166f8 _ 204689 1714763 _ 408 7099**** _ | The ID of the server certificate. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteServerCertificate &ServerCertificateId=123157****_166f8204689_1714763408_7099**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteServerCertificateResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</DeleteServerCertificateResponse>
```

`JSON` format `{`

```json
    "DeleteServerCertificateResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` `}`

#### 2.6.3 DescribeServerCertificates

Queries server certificates in a specified region. Not e For security reasons, only fingerprints and names of the server certificates are returned. The content of the server certificates and private keys is not returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeServerCer tificates | The operation that you want to perform. Set the value to DescribeServerCert if icat es. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateI d | String | No | 12315790xxxxxxx 166f8204689 17 _ _ 14763408 709*** _ ** | The ID of the server certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerCertificat es | Array of ServerCertificat e |   | The list of server certificates. |
| ServerCertificat e |   |   |   |
| ServerCertificat eId | String | 123157xxxxxxxx 166 _ f8204689 17147634 _ 08 709981430-cn- _ east-hangz****** | The ID of the server certificate. |
| ServerCertificat eName | String | slb | The name of the server certificate. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the server certificate is created. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|
| Parameter | Type | Example | Description |
| Fingerprint | String | 68:08:1a:f8:2c:97:6 9:a3:a1:e6:16:41:4 b:ca:4f:5d:ee:a5:ef :0d | The fingerprint of the server certificate. |
| AliCloudCertific ateId | String | 7309xxxxxxxx 15d97 _ e7709a 71445759hr _ 78928***** _ | The ID of the server certificate from Apsara Stack SSL Certificates Service. |
| AliCloudCertific ateName | String | testcertkey | The name of the server certificate from Apsara Stack SSL Certificates Service. |
| IsAliCloudCertifi cate | Integer | 0 | Indicates whether the server certificate is from Apsara Stack SSL Certificates Service. Valid values: 1: yes 0: no |
| RegionIdAlias | String | cn-qingdao-env17- d01 | The name of the region where the SLB instance is deployed. |
| StandardType | String | ServerCertificate | The type of the server certificate. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeServerCertificates &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeServerCertificatesResponse>
      <RequestId>9FFF450B-CC09-4FFB-900F-E347EB7AA2CC</RequestId>
      <ServerCertificates>
            <ServerCertificate>
                  <CreateTimeStamp>1541761156000</CreateTimeStamp>
                  <CommonName>*.example1.com</CommonName>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:ef:0d<
/Fingerprint>
                  <ServerCertificateId>1231579xxxxxx_166f8204689_1714763408_709981430</Serv
erCertificateId>
                  <ExpireTimeStamp>1558161264000</ExpireTimeStamp>
                  <AliCloudCertificateId>1501739</AliCloudCertificateId>
                  <ExpireTime>2019-05-18T06:34:24Z</ExpireTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <CreateTime>2018-11-09T10:59:16Z</CreateTime>
                  <ServerCertificateName>*.example1.com</ServerCertificateName>
                  <IsAliCloudCertificate>1</IsAliCloudCertificate>
                  <AliCloudCertificateName>slb</AliCloudCertificateName>
            </ServerCertificate>
            <ServerCertificate>
                  <CreateTimeStamp>1481623069000</CreateTimeStamp>
                  <RegionIdAlias>cn-hangzhou</RegionIdAlias>
                  <ResourceGroupId>rg-acfmxazb4ph6aiy</ResourceGroupId>
                  <Fingerprint>cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:84:8d<
/Fingerprint>
                  <ServerCertificateId>1231579085xxxx_158f79de306</ServerCertificateId>
                  <ExpireTimeStamp>1732169065000</ExpireTimeStamp>
                  <AliCloudCertificateId>0</AliCloudCertificateId>
                  <ExpireTime>2024-11-21T06:04:25Z</ExpireTime>
                  <RegionId>cn-hangzhou</RegionId>
                  <CreateTime>2016-12-13T09:57:49Z</CreateTime>
                  <ServerCertificateName>test_certificate</ServerCertificateName>
                  <IsAliCloudCertificate>0</IsAliCloudCertificate>
                  <AliCloudCertificateName></AliCloudCertificateName>
            </ServerCertificate>
      </ServerCertificates>
</DescribeServerCertificatesResponse>
```

`JSON` format `{`

```json
    "DescribeServerCertificatesResponse": {
        "RequestId": "9FFF450B-CC09-4FFB-900F-E347EB7AA2CC",
        "ServerCertificates": {
            "ServerCertificate": [
```

`{`

```json
                    "CreateTimeStamp": 1541761156000,
                    "CommonName": "*.example1.com",
                    "RegionIdAlias": "cn-hangzhou",
                    "ResourceGroupId": "rg-acfmxazb4ph6aiy",
                    "Fingerprint": "68:08:1a:f8:2c:97:69:a3:a1:e6:16:41:4b:ca:4f:5d:ee:a5:e
f:0d",
                    "ServerCertificateId": "1231579xxxxxx_166f8204689_1714763408_709981430"
```

`,`

```json
                    "ExpireTimeStamp": 1558161264000,
                    "AliCloudCertificateId": 1501739,
                    "ExpireTime": "2019-05-18T06:34:24Z",
                    "RegionId": "cn-hangzhou",
                    "CreateTime": "2018-11-09T10:59:16Z",
                    "ServerCertificateName": "*.example1.com",
                    "IsAliCloudCertificate": 1,
                    "AliCloudCertificateName": "slb"
```

`},` `{`

```json
                    "CreateTimeStamp": 1481623069000,
                    "RegionIdAlias": "cn-hangzhou",
                    "ResourceGroupId": "rg-acfmxazb4ph6aiy",
                    "Fingerprint": "cd:90:1b:7b:49:4d:1d:90:f6:01:de:9a:81:7d:31:a7:38:1d:8
4:8d",
                    "ServerCertificateId": "1231579085xxxx_158f79de306",
                    "ExpireTimeStamp": 1732169065000,
                    "AliCloudCertificateId": 0,
                    "ExpireTime": "2024-11-21T06:04:25Z",
                    "RegionId": "cn-hangzhou",
                    "CreateTime": "2016-12-13T09:57:49Z",
                    "ServerCertificateName": "test_certificate",
                    "IsAliCloudCertificate": 0,
                    "AliCloudCertificateName": ""
```

`}` `]` `}` `}` `}`

#### 2.6.4 SetServerCertificateName

Sets the name of a server certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetServerCertifica teName | The operation that you want to perform. Set the value to Set ServerCert if icat eName. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| ServerCertificateI d | String | Yes | 139a****-cn- qingdao-env17- d01 | The ID of the server certificate. |
| ServerCertificateN ame | String | Yes | slb- servercertificate- cn-east- hangzhou**** | The name of the server certificate. The name must be 1 to 80 characters in length and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FE7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetServerCertificateName &RegionId=cn-east-hangzhou-01 &ServerCertificateId=139a****-cn-east-hangzhou-01 &ServerCertificateName=slb-servercertificate-cn-east-hangzhou**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetServerCertificateNameResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId>
</SetServerCertificateNameResponse>
```

`JSON` format `{`

```json
    "SetServerCertificateNameResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984"
```

`}` `}`

#### 2.6.5 UploadCACertificate

Uploads a CA certificate. You can upload only one CA certificate in each call. After a CA certificate is uploaded, the ID, name, and fingerprint of the certificate are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UploadCACertific ate | The operation that you want to perform. Set the value to UploadCACert if icat e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| CACertificate | String | Yes | test | The content of the CA certificate that you want to upload. |
| CACertificateNam e | String | No | mycacert01 | The name of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificateId | String | 139a00604ad-cn- east-hangzh**** | The ID of the CA certificate. |
| CACertificateNa me | String | mycacert01 | The name of the CA certificate. |
| Fingerprint | String | 02:DF:AB:ED | The fingerprint of the CA certificate. |

| S | erver Load Balanc | er |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=UploadCACertificate &RegionId=cn-qingdao-env17-d01 &CACertificate=test &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UploadCACertificateResponse>
      <Fingerprint>02:DF:AB:ED</Fingerprint>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <CACertificateId>139a00604ad-cn-east-hangzh*****</CACertificateId>
      <CACertificateName>mycacert01</CACertificateName>
</UploadCACertificateResponse>
```

`JSON` format `{`

```json
    "UploadCACertificateResponse": {
        "Fingerprint": "02:DF:AB:ED",
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "CACertificateId": "139a00604ad-cn-east-hangzh*****",
        "CACertificateName": "mycacert01"
```

`}` `}`

#### 2.6.6 DeleteCACertificate

Deletes a CA certificate. Not e You cannot delete a CA certificate that is in use. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteCACertifica te | The operation that you want to perform. Set the value to Delet eCACert if icat e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 123157908**** 1 _ 5c73d77203 - _ 986300114 - _ 2110544**** | The ID of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FF7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteCACertificate &RegionId=cn-east-hangzhou-01 &CACertificateId=123157908****_15c73d77203_-986300114_-211054**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteCACertificateResponse>
      <RequestId>CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984</RequestId>
</DeleteCACertificateResponse>
```

`JSON` format `{`

```json
    "DeleteCACertificateResponse": {
        "RequestId": "CEFxxxxx72CEB-54B6-4AE8-B225-F876FF7BA984"
```

`}` `}`

#### 2.6.7 DescribeCACertificates

Queries CA certificates. Not e For security reasons, only fingerprints and names of the CA certificates are returned, the content of the CA certificates is not returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCACertifi cates | The operation that you want to perform. Set the value to DescribeCACert if icat es. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the CA certificate is created. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | No | 139a006****-cn- qingdao-env17- d01 | The ID of the CA certificate. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| CACertificates | Array of CACertificate |   | Information about the CA certificate. |
| CACertificate |   |   |   |
| CACertificateId | String | 139a006****-cn- qingdao-env17-d01 | The ID of the CA certificate. |
| CACertificateNa me | String | test | The name of the CA certificate. |
| RegionId | String | cn-qingdao-env17- d01 | The ID of the region where the CA certificate is created. |
| Fingerprint | String | AC:BE:FD | The fingerprint of the CA certificate. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCACertificates &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCACertificateResponse>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <CACertificates>
            <CACertificateName>test</CACertificateName>
            <Fingerprint>AC:BE:FD</Fingerprint>
            <RegionId>cn-east-hangzhou-01</RegionId>
            <CACertificateId>139a006****-cn-east-hangzhou-02</CACertificateId>
      </CACertificates>
</DescribeCACertificateResponse>
```

`JSON` format `{`

```json
    "DescribeCACertificateResponse": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "CACertificates": {
            "CACertificateName": "test",
            "Fingerprint": "AC:BE:FD",
            "RegionId": "cn-east-hangzhou-01",
            "CACertificateId": "139a006****-cn-east-hangzhou-02"
```

`}` `}` `}`

#### 2.6.8 SetCACertificateName

Sets the name of a CA certificate. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetCACertificateN ame | The operation that you want to perform. Set the value to Set CACert if icat eName. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. You can call the DescribeRegions operation to query region IDs. |
| CACertificateId | String | Yes | 139a0****-cn- qingdao-env17- d01 | The ID of the CA certificate. |
| CACertificateNam e | String | Yes | mycacert02 | The name of the CA certificate. The name must be 1 to 80 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). It _ must start with a letter. |
| access key id _ _ | String | No | acc- hp34s2h0xx1ht4n wo**** | The AccessKey ID. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | CEF72CEB-54B6- 4AE8-B225- F876FE7BA984 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetCACertificateName &RegionId=cn-qingdao-env17-d01 &CACertificateId=139a0****-cn-qingdao-env17-d01 &CACertificateName=mycacert02 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetCACertificateNameResponse>
      <RequestId>CEF72CEB-54B6-4AE8-B225-F876FE7BA984</RequestId>
</SetCACertificateNameResponse>
```

`JSON` format `{`

```json
    "SetCACertificateNameResponse": {
        "RequestId": "CEF72CEB-54B6-4AE8-B225-F876FE7BA984"
```

`}` `}`

### 2.7 Backend servers

#### 2.7.1 AddBackendServers

Adds backend servers. Not e If multiple identical Elastic Compute Service (ECS) instances are specified in a request, only the first ECS instance is added. The other ECS instances are ignored. If the backend server that you add is the same as one of the existing backend servers that are already associated with the listener, an error message is returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBackendServe rs | The operation that you want to perform. Set the value to AddBackendServers. |
| LoadBalancerId | String | Yes | lb- 2ze7o5h52g02kk zz**** | The ID of the Server Load Balancer (SLB) instance. |
|   |   |   |   | The list of backend servers that you want to add to the SLB instance. The following parameters are used to specify the backend servers: ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. You can specify the ID of an ECS instance or an elastic network interface (ENI). If ServerId is set to the ID of an ENI, the T ype parameter is required. Weight : The weight of the backend |

|   | Parameter |   | Type |   | Required |   | Example |   | server. Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | Valid values: 0 t o 100. |   |   |   |
|   | BackendServers |   | String |   | Yes |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", |   | Default value: 100. Not e If the weight is set to 0, no requests are forwarded to the backend server. Descript ion: Optional. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also contain _ Chinese characters. T ype: Specify the type of backend server. Valid values: ecs (default): an ECS instance. eni: an ENI. ServerIp: Specify the IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   | "Port":"80","Desc |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   | ription":"test- |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   | 113" }] |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |
|   | Document Version: |   | 20220928 |   |   |   |   |   | 18 |   |   |   |

| Parameter | Type | Required | Example |   | Description Not e Only backend servers |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | that are in the Running state can be added to an SLB instance. You can add at most 20 backend |   |
| Response parameters |   |   |   |   | servers in each call. |   |

| Parameter | Type | Example | You can specify ENIs as backend Descriptisoenrvers only for high-performance |
|---|---|---|---|
| LoadBalancerId | String | lb- 2ze7o5h52g02kkzz* *** | SLB instances. The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-2zej4lxhjoq1icu**** | The ID of the ECS instance or ENI. |
| Weight | String | 100 | The weight of the backend server. Valid values: 0 t o 100. Default value: 100. If the value is set to 0, the SLB instance does not forward requests to the backend server. |
| Description | String | BackendServer | The description of the backend server. |
| RequestId | String | 34B82C81-F13B- 4EEB-99F6- A048C67CC830 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddBackendServers &LoadBalancerId=lb-2ze7o5h52g02kkzz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBackendServersResponse>
    <BackendServers>
        <BackendServer>
            <ServerId>i-2zej4lxhjoq1icu*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
        <BackendServer>
            <ServerId>i-2ze1u9ywulp5pbv*****</ServerId>
            <Weight>100</Weight>
            <Type>ecs</Type>
        </BackendServer>
    </BackendServers>
    <RequestId>34B82C81-F13B-4EEB-99F6-A048C67CC830</RequestId>
    <LoadBalancerId>lb-2ze7o5h52g02kkzz*****</LoadBalancerId>
</AddBackendServersResponse>
```

`JSON` format `{`

```json
    "AddBackendServersResponse": {
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "i-2zej4lxhjoq1icu*****",
                    "Weight": 100,
                    "Type": "ecs"
```

`},` `{`

```json
                    "ServerId": "i-2ze1u9ywulp5pbv*****",
                    "Weight": 100,
                    "Type": "ecs"
```

`}` `]` `},`

```json
        "RequestId": "34B82C81-F13B-4EEB-99F6-A048C67CC830",
        "LoadBalancerId": "lb-2ze7o5h52g02kkzz*****"
```

`}` `}`

#### 2.7.2 RemoveBackendServers

Removes backend servers. Not e If the backend server that you want to remove does not belong to the specified Server Load Balancer (SLB) instance, the request fails. However, the system does not report an error. Request parameters

| Parameter |   | Type | Required |   | Example | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| Action |   | String | Yes |   | RemoveBackendS ervers | The operation that you want to perform. Set the value to RemoveBackendServers. |   |   |   |
| BackendServers |   | String | Yes |   | [{"ServerId":"i- 2zej4lxhjoq****", "Type": "ecs","Weight":"1 00"}] | The backend servers to be removed. Valid values: ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. T ype: Specify the type of the backend server. Valid values: ecs: an Elastic Compute Service (ECS) instance. This is the default value. eni: an elastic network interface (ENI). Not e You can remove up to 20 backend servers in each call. Examples: ECS: [{"ServerId":"i- 2zej 4lx |   |   |   |
|   |   |   |   |   |   |   | [{"ServerId":"i- 2zej 4lx |   |   |
|   |   |   |   |   |   | hjoq ***", "Type": "ecs","Weig |   |   |   |
|   |   |   |   |   |   | ht":"100"}] |   |   |   |
|   |   |   |   |   |   | ENI: | [{"ServerId":"eni- 2ze 1s |   |   |
|   |   |   |   |   |   | dp 5***","Type": "eni","Weight |   |   |   |
|   |   |   |   |   |   | ":"100"}] |   |   |   |
| LoadBalancerId |   | String | Yes |   | lb- bp1qjwo61pqz3a hl**** | The ID of the SLB instance. |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| LoadBalancerId | String | lb- bp1vjkb671z53**** | The ID of the SLB instance. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |

| erver Load Balanc | er |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackendServer |   |   |   |
| ServerId | String | i-jjgjgjgggd**** | The ID of the backend server. |
| Weight | Integer | 100 | The weight of the backend server. Valid values: 0 t o 100. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveBackendServers &BackendServers=[{"ServerId":"i-2zej4lxhjoq****", "Type": "ecs","Weight":"100"}] &LoadBalancerId=lb-bp1qjwo61pqz3ahl**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveBackendServersResponse>
  <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
  <LoadBalancerId>lb-bp1vjkb671z53cy******</LoadBalancerId>
  <BackendServers>
        <BackendServer>
              <ServerId>i-jjgjgjg*****</ServerId>
              <Weight>100</Weight>
        </BackendServer>
        <BackendServer>
              <ServerId>i-jjgjgituitu****</ServerId>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
</RemoveBackendServersResponse>
```

`JSON` format `{`

```json
    "RemoveBackendServers": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "LoadBalancerId": "lb-bp1vjkb671z53cy******",
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "i-jjgjgjg*****",
                    "Weight": 100
```

`},` `{`

```json
                    "ServerId": "i-jjgjgituitu****",
                    "Weight": 100
```

`}` `]` `}` `}` `}`

#### 2.7.3 SetBackendServers

Sets the weights of backend servers. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetBackendServer s | The operation that you want to perform. Set the value to Set BackendServers. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a **** | The ID of the Server Load Balancer (SLB) instance. |
|   |   |   |   | The list of backend servers that you want to add to the SLB instance. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. |

|   | Parameter |   | Type |   | Required |   | Example |   | Weight : Required. Specify the Description weight of the backend server. This |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   | parameter must be of the INTEGER type. Valid values: 0 to 100. |   |   |   |
|   | BackendServers |   | String |   | Yes |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Desc ription":"test- 112" }] |   | Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: Specify the IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |

| Parameter |   | Type | Required |   | Example |   |   | Description Not e The backend servers |   |
|---|---|---|---|---|---|---|---|---|---|
| Response parameters |   |   |   |   |   |   |   | that you add to an SLB instance must be in the Running state. You can add at most 20 backend |   |
| Parameter | Type |   |   | Example |   | Descri |   | ptsioenrvers to an SLB instance in each call. In addition, you can specify |   |
| LoadBalancerId | String |   |   | lb- bp1qjwo61pqz3a*** * |   | ENIs as backend servers only for The ID ohf igthhe- pSeLrBf oinrsmtaannccee. SLB instances. |   | ENIs as backend servers only for ohf igthhe- pSeLrBf oinrsmtaannccee. SLB instances. |   |
| BackendServers | Array of BackendServer |   |   |   |   | The list of backend servers. |   |   |   |
| BackendServer |   |   |   |   |   |   |   |   |   |
| ServerId | String |   |   | eni-hg231**** |   | The ID of the ECS instance. |   |   |   |
| Weight | String |   |   | 100 |   | The weight of the backend server. |   |   |   |
| Description | String |   |   | BackendServer |   | The description of the backend server. |   |   |   |
| Type | String |   |   | ecs |   | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |   |   |   |
| RequestId | String |   |   | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 |   | The ID of the request. |   |   |   |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetBackendServers &LoadBalancerId=lb-bp1qjwo61pqz3a**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetBackendServersResponse>
      <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
      <LoadBalancerId>lb-dhf13*******</LoadBalancerId>
      <BackendServers>
            <BackendServer>
                  <ServerId>eni-hg231**</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
            <BackendServer>
                  <ServerId>eni-hfhf***</ServerId>
                  <Weight>100</Weight>
                              <Type>eni</Type>
            </BackendServer>
      </BackendServers>
</SetBackendServersResponse>
```

`JSON` format `{`

```json
    "SetBackendServersResponse": {
        "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
        "LoadBalancerId": "lb-dhf13*******",
        "BackendServers": {
            "BackendServer": [
```

`{`

```json
                    "ServerId": "eni-hg231**",
                    "Weight": 100,
                    "Type": "eni"
```

`},` `{`

```json
                    "ServerId": "eni-hfhf***",
                    "Weight": 100,
                    "Type": "eni"
```

`}` `]` `}` `}` `}`

### 2.8 vServer groups

#### 2.8.1 CreateVServerGroup

Creates a vServer group and adds backend servers to the vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVServerGro up | The operation that you want to perform. Set the value to Creat eVServerGroup. |
| LoadBalancerId | String | Yes | lb- bp1qjwo61pqz3a hl**** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |
| VServerGroupNa me | String | No | Group1 | The name of the vServer group. The name must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
|   |   |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- | The list of backend servers to be added. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements in a list for each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. |

|   |   |   |   |   |   |   | pt o : test |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | BPaacrakmenedtSeerrvers |   | STtyrpineg |   | NReoquired |   | 112" }, { Example "ServerId": "eni- |   | T ype: Required. Specify the type of Description the backend server. This parameter |   |   |   |
|   |   |   |   |   |   |   | xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" }] |   | must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-2**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| Description | String | vServerGroup | The description of the vServer group. |
| ServerType | String | ECS |   |
| Type | String | Type | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateVServerGroup &LoadBalancerId=lb-bp1qjwo61pqz3ahl**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateVServerGroupResponse>
  <VServerGroupId>rsp-bp1i4c******</VServerGroupId>
  <RequestId>3EBBDBAE-8E8B-438F-A109-95C2FDB2C333</RequestId>
  <BackendServers>
        <BackendServer>
              <Type>ecs</Type>
              <ServerId>i-bp1ds2yjlk66********</ServerId>
              <Description>test-11244</Description>
              <Port>80</Port>
              <Weight>100</Weight>
        </BackendServer>
  </BackendServers>
</CreateVServerGroupResponse>
```

`JSON` format `{`

```json
  "VServerGroupId": "rsp-bp1i4c3******",
  "RequestId": "3EBBDBAE-8E8B-438F-A109-95C2FDB2C333",
  "BackendServers": {
    "BackendServer": [
```

`{`

```json
        "Type": "ecs",
        "ServerId": "i-bp1ds2yjlk666******",
        "Description": "test-11244",
        "Port": 80,
        "Weight": 100
```

`}` `]` `}` `}`

#### 2.8.2 SetVServerGroupAttribute

Modifies the configurations of a vServer group. You can call the operation to modify only configurations such as the weight and port of a backend server. If you want to modify backend servers in a specified vServer group, call the `ModifyVServerGroupBack` `endServers` operation. If you want to add backend servers, call the `AddVServerGroupBackendServers` operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetVServerGroup Attribute | The operation that you want to perform. Set the value to Set VServerGroupAt t ribut e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupNa me | String | No | vserver-group- test | The name of the vServer group. |
|   |   |   |   | The backend servers in the vServer group. |

|   | eveloper Guide·API |   | Reference |   |   |   |   |   | Server Load Balance |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   | Type |   | Required |   | Example |   | You can add up to 20 backend servers Description in each call. |   |   |   |
|   | BackendServers |   | String |   | No |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Desc ription":"test- 113" }] |   | ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 to 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 to 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |

|   |   |   |   | 6.**.**", "Port":"80","Descrip Description |   |
|---|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |   |
|   |   |   |   | tion":"test-113" }] |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupN ame | String | Group1 | The name of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | i-bp1ek6yd7jvkx**** | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescrip tion. | The description of the vServer group. |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=SetVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<SetVServerGroupAttributeResponse>
  <BackendServers>
        <BackendServer>
              <ServerId>i-bp1ek6yd7jvkx*****</ServerId>
              <Port>80</Port>
              <Weight>100</Weight>
              <Type>ecs</Type>
        </BackendServer>
  </BackendServers>
  <RequestId>A4FDF333-F904-4540-88FC-ED6F87AEFFCB</RequestId>
  <VServerGroupId>rsp-bp1d2e3*****</VServerGroupId>
  <VServerGroupName>test1</VServerGroupName>
</SetVServerGroupAttributeResponse>
```

`JSON` format `{`

```json
    "SetVServerGroupAttributeResponse": {
        "BackendServers": {
            "BackendServer": {
                "ServerId": "i-bp1ek6yd7jvkx*****",
                "Port": 80,
                "Weight": 100,
                "Type": "ecs"
```

`}` `},`

```json
        "RequestId": "A4FDF333-F904-4540-88FC-ED6F87AEFFCB",
        "VServerGroupId": "rsp-bp1d2e3*****",
        "VServerGroupName": "test1"
```

`}` `}`

#### 2.8.3 AddVServerGroupBackendServers

Adds backend servers to a specified vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddVServerGroup BackendServers | The operation that you want to perform. Set the value to AddVServerGroupBackendServers. |
|   |   |   |   | The list of backend servers that you want to add to the vServer group. You can specify up to 20 backend servers in each request. |

|   | erver Load Balancer |   |   |   |   |   |   |   | Developer Guide·API Referenc |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   | Type |   | Required |   | Example |   | The following parameters are used to Description specify the backend servers: |   |   |   |
|   | BackendServers |   | String |   | Yes |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6*", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Desc ription":"test- 113" }] |   | ServerId: The ID of the backend server. You can specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). Port : Required. The port that is used by the backend server. Valid values: 1 t o 65535. Weight : The weight of the backend server. Valid values: 0 t o 100. Default value: 100. If the value is set to 0, no requests are forwarded to the backend server. T ype: The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. ServerIp: The IP address of the ECS instance or ENI. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |

|   |   |   |   | tion":"test-113" }] |   |   |
|---|---|---|---|---|---|---|
| Parameter | Type | Required | Example | Description |   |   |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |   |   |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-231 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | test | The description of the vServer group. |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weigh t": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }
```

`]`

```
&RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddVServerGroupBackendServersResponse>
  <VServerGroupId>rsp-cige6j******</VServerGroupId>
  <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
  <BackendServers>
        <Type>ecs</Type>
        <Description>test</Description>
        <ServerId>vm-231</ServerId>
        <Weight>100</Weight>
        <Port>70</Port>
  </BackendServers>
</AddVServerGroupBackendServersResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6j******", "RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C", "BackendServers":[
    {"Type":"ecs","Description":"test","ServerId":"vm-231","Weight":"100","Port":"70"}
```

`]` `}`

#### 2.8.4 RemoveVServerGroupBackendServers

Removes a backend server from a specified vServer group. Not e If one or more backend servers specified by BackendServers do not exist in the vServer group, the backend servers are ignored and no error message is returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveVServerGr oupBackendServe rs | The operation that you want to perform. Set the value to RemoveVServerGroupBackendServ ers. |
| BackendServers | String | Yes | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Desc ription":"test- 113" }] | The list of backend servers that you want to remove from the vServer group. You can specify at most 20 backend servers for a vServer group in each call. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI). This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. ServerIp: Specify the IP address of the ECS instance or ENI. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-230 | The ID of the ECS instance or ENI. |
| Port | Integer | 80 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveVServerGroupBackendServers &BackendServers=[{ "ServerId": "eni-xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Description":"test-112" },{ "ServerId": "eni-xxxxxxxxx", "Weigh t": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80","Description":"test-113" }
```

`]`

```
&RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveVServerGroupBackendServersResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
   <VServerGroupId>rsp-cige6******</VServerGroupId>
   <BackendServers>
      <BackendServer>
         <ServerId>vm-231</ServerId>
         <Port>70</Port>
         <Weight>100</Weight>
                              <Type>ecs</Type>
      </BackendServer>
   </BackendServers>
</RemoveVServerGroupBackendServersResponse>
```

`JSON` format `{`

```json
  "RemoveVServerGroupBackendServersResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "VServerGroupId": "rsp-cige6******",
    "BackendServers": {
      "BackendServer": {
        "ServerId": "vm-231",
        "Port": "70",
        "Weight": "100",
        "Type": "ecs"
```

`}` `}` `}` `}`

#### 2.8.5 ModifyVServerGroupBackendServers

Replaces backend servers in a specified vServer group. You can call this operation to replace the backend servers in a specified vServer group. To modify the configurations of the backend servers, such as their weights, you can call the `SetVServerGroupAttribute` operation. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVServerGro upBackendServer s | The operation that you want to perform. Set the value to Modif yVServerGroupBackendServer s. |

| Parameter |   | Type | Required |   | Example | Description |   |
|---|---|---|---|---|---|---|---|
| RegionId |   | String | Yes |   | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |   |
| VServerGroupId |   | String | Yes |   | rsp-cige6j**** | The ID of the vServer group. |   |
| OldBackendServer s |   | String | No |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Desc ription":"test- 112" }] | The list of backend servers to be replaced. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. Specify the description of the backend server. This parameter must be of the STRING type. The description must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It can also _ contain Chinese characters. T ype: Specify the type of backend server. This parameter must be of the STRING type. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an ENI ServerIp: Specify the IP address of the ECS instance or ENI Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |
|   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |
|   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |
|   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |
|   |   |   |   |   |   | n":"test-112" }] |   |

|   | Parameter |   | Type |   | Required |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | red | Example |   | Description xxxx", "Weight": "100", "Type" | tion |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |
|   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |
|   |   |   |   |   |   |   |   |   | The list of backend servers to be added. You can specify at most 20 backend servers for a vServer group in each call. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each request. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. |   |   |
|   | NewBackendServ ers |   | String |   | No |   | [{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "192.XX.XX.6", "Port":"80","Desc ription":"test- 112" },{ "ServerId": "eni- xxxxxxxxx", "Weight": "100", "Type": "eni", "ServerIp": "172.XX.XX.6", "Port":"80" "Desc |   | This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter must be of the STRING type. It can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). It _ can also contain Chinese characters. T ype: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an ENI ServerIp: the IP address of the ECS |   |   |

|   |   |   |   |   |   |   | Port : 80 , Desc |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Parameter |   | Type |   | Required |   | rEixpatmionp"le:"test- 113" }] |   | instance or ENI Description |   |   |   |
|   |   |   |   |   |   |   |   |   | Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |
|   |   |   |   |   |   |   |   |   | "ecs", "Port":"80","Descriptio |   |   |   |
|   |   |   |   |   |   |   |   |   | n":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |
|   |   |   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |
|   |   |   |   |   |   |   |   |   | : "eni", "ServerIp": "192.168. |   |   |   |
|   |   |   |   |   |   |   |   |   | **.**", "Port":"80","Descripti |   |   |   |
|   |   |   |   |   |   |   |   |   | on":"test-112" }] |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | [{ |
|   |   |   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |   |   |
|   |   |   |   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |   |   |
|   |   |   |   |   |   |   |   |   | Port":"80","Description":"test |   |   |   |
|   |   |   |   |   |   |   |   |   | -112" },{ "ServerId": "eni-xxx |   |   |   |
|   |   |   |   |   |   |   |   |   | xxxxxx", "Weight": "100", "Typ |   |   |   |
|   |   |   |   |   |   |   |   |   | e": "eni", "ServerIp": "172.16 |   |   |   |
|   |   |   |   |   |   |   |   |   | 6.**.**", "Port":"80","Descrip |   |   |   |
|   |   |   |   |   |   |   |   |   | tion":"test-113" }] |   |   |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6j**** | The ID of the vServer group. |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-236 | The ID of the ECS instance or ENI. |
| Port | Integer | 70 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVServerGroupBackendServers &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVServerGroupBackendServersResponse>
      <VServerGroupId>rsp-cige6j******</VServerGroupId>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
      <BackendServers>
            <ServerId>vm-236</ServerId>
            <Weight>100</Weight>
            <Port>70</Port>
      </BackendServers>
</ModifyVServerGroupBackendServersResponse>
```

`JSON` format `{`

```json
    "ModifyVServerGroupBackendServersResponse": {
        "VServerGroupId": "rsp-cige6j******",
        "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
        "BackendServers": {
            "ServerId": "vm-236",
            "Weight": 100,
            "Port": 70
```

`}` `}` `}`

#### 2.8.6 DeleteVServerGroup

Deletes a vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVServerGro up | The operation that you want to perform. Set the value to Delet eVServerGroup. |

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6j**** | The ID of the vServer group. Not e You cannot delete a vServer group that is in use. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVServerGroup &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6j**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVServerGroupResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteVServerGroupResponse>
```

`JSON` format `{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

`}`

#### 2.8.7 DescribeVServerGroups

Queries the vServer groups of a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerG roups | The operation that you want to perform. Set the value to DescribeVServerGroups. |
| LoadBalancerId | String | Yes | lb- bp1o94dp5i6ea** ** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroups | Array of VServerGroup |   | The list of backend servers. |
| VServerGroup |   |   |   |
| VServerGroupId | String | rsp-bp1oygn**** | The ID of the vServer group. |
| VServerGroupN ame | String | k8s/31065/nginx- ingress-lb/kube- system/clust****" | The name of the vServer group. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVServerGroups &LoadBalancerId=lb-bp1o94dp5i6ea**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVServerGroupsResponse>
  <VServerGroups>
        <VServerGroup>
              <VServerGroupId>rsp-bp1oygn******</VServerGroupId>
              <VServerGroupName>k8s/31065/nginx-ingress-lb/kube-system/clust****</VServerGr
oupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1i6sn******</VServerGroupId>
              <VServerGroupName>k8s/31605/nginx-ingress-lb/kube-system/clusterid</VServerGr
oupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
        <VServerGroup>
              <VServerGroupId>rsp-bp1f85n******</VServerGroupId>
              <VServerGroupName>VSG1</VServerGroupName>
              <AssociatedObjects>
                    <Listeners>
            </Listeners>
                    <Rules>
            </Rules>
              </AssociatedObjects>
        </VServerGroup>
  </VServerGroups>
  <RequestId>31ADDBCD-275F-4C37-B0A3-5DFC8564E686</RequestId>
</DescribeVServerGroupsResponse>
```

`JSON` format `{`

```json
 "VServerGroups": {
  "VServerGroup": [
```

`{`

```json
    "VServerGroupId": "rsp-bp1oygn******",
    "VServerGroupName": "k8s/31065/nginx-ingress-lb/kube-system/clust****",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `},` `{`

```json
    "VServerGroupId": "rsp-bp1i6sn******",
    "VServerGroupName": "k8s/31605/nginx-ingress-lb/kube-system/clusterid",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `},` `{`

```json
    "VServerGroupId": "rsp-bp1f85n******",
    "VServerGroupName": "VSG1",
    "AssociatedObjects": {
     "Listeners": {
      "Listener": []
```

`},`

```json
     "Rules": {
      "Rule": []
```

`}` `}` `}` `]` `},`

```json
 "RequestId": "31ADDBCD-275F-4C37-B0A3-5DFC8564E686"
```

`}`

#### 2.8.8 DescribeVServerGroupAttribute

Queries detailed information about a vServer group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVServerG roupAttribute | The operation that you want to perform. Set the value to DescribeVServerGroupAt t ribut e. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| VServerGroupId | String | Yes | rsp-cige6**** | The ID of the vServer group. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| VServerGroupId | String | rsp-cige6**** | The ID of the vServer group. |
| VServerGroupN ame | String | Group1 | The name of the vServer group. The name is 1 to 80 characters in length, and can contain Chinese characters, letters, digits, hyphens (- ), forward slashes (/), periods (.),and underscores ( ). _ |
| BackendServers | Array of BackendServer |   | The list of backend servers. |
| BackendServer |   |   |   |
| ServerId | String | vm-233 | The ID of the Elastic Compute Service (ECS) instance. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| Description | String | vServerGroupDescrip tion. | The description of the vServer group. |
| ServerType | String | ecs |   |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an Elastic Compute Service (ECS) instance eni: an elastic network interface (ENI) |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVServerGroupAttribute &RegionId=cn-qingdao-env17-d01 &VServerGroupId=rsp-cige6**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVServerGroupAttributeResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
   <VServerGroupId>rsp-cige6******</VServerGroupId>
   <VServerGroupName>Group1</VServerGroupName>
   <BackendServers>
      <BackendServer>
         <ServerId>vm-232</ServerId>
         <Port>80</Port>
         <Weight>100</Weight>
      </BackendServer>
      <BackendServer>
         <ServerId>vm-233</ServerId>
         <Port>90</Port>
         <Weight>100</Weight>
      </BackendServer>
   </BackendServers>
</DescribeVServerGroupAttributeResponse>
```

`JSON` format

```json
{"VServerGroupId":"rsp-cige6*****","RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C","VSer verGroupName":"Group1","BackendServers":[{"ServerType":"ecs","Type":"ecs","ServerId":"vm-23 3","Description":"vServerGroupDescription.","VpcId":"vpc-**","Port":"90","ServerIp":"192.16 8.*.*","Weight":"100"}]}
```

### 2.9 Primary/secondary server groups

#### 2.9.1 CreateMasterSlaveServerGroup

Creates a primary/secondary server group. A primary/secondary server group contains only two Elastic Compute Service (ECS) instances. One of the ECS instances serves as the primary server. The other ECS instance serves as the secondary server. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMasterSlav eServerGroup | The operation that you want to perform. Set the value to Creat eMast erSlaveServerGroup. |
| LoadBalancerId | String | Yes | lb- bp1hv944r69al4j* *** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |
| MasterSlaveServe rGroupName | String | No | sg- atstuj3rtopty**** | The name of the primary/secondary server group. |
|   |   |   |   | The list of backend servers in the primary/secondary server group. The value of this parameter must be a STRING list in the JSON format. You can specify at most 20 elements for this parameter in each call. ServerId: Required. Specify the ID of the backend server. This parameter must be of the STRING type. Port : Required. Specify the port that is used by the backend server. This parameter must be of the INTEGER type. Valid values: 1 t o 65535. Weight : Required. Specify the weight of the backend server. This parameter must be of the INTEGER type. Valid values: 0 t o 100. Descript ion: Optional. The description of the backend server. This parameter must be of the |

| Parameter |   | Type | Required |   | Example |   | STRING type. The description must Description be 1 to 80 characters in length and |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). The _ description can contain Chinese characters. ServerT ype: Specify the type of the backend server. This parameter must be of the STRING type. Valid values: |   |   |   |   |
| MasterSlaveBacke ndServers |   | String | No |   | [{ "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Serv erType":"Master" ,"Description":"te st-112" }, { "ServerId": "i- xxxxxxxxx", "Weight": "100", "Type": "ecs", "Port":"80","Serv erType":"Slave"," Description":"tes t-112" }] |   | Mast er: primary server Slave: secondary server T ype: The type of the backend server. This parameter must be of the STRING type. Valid values: ecs (default): an ECS instance eni: an elastic network interface (ENI) ServerIp: the IP address of the ECS instance or ENI. A primary/secondary server group can contain at most two backend servers. If you do not set this parameter, an empty primary/secondary server group is created. Examples: ECS: [{ "ServerId": "i-xxxxxxx |   |   |   |   |
|   |   |   |   |   |   |   |   | [{ "ServerId": "i-xxxxxxx |   |   |   |
|   |   |   |   |   |   |   | xx", "Weight": "100", "Type": |   |   |   |   |
|   |   |   |   |   |   |   | "ecs", "Port":"80","ServerType |   |   |   |   |
|   |   |   |   |   |   |   | ":"Master","Description":"test |   |   |   |   |
|   |   |   |   |   |   |   | -112" }, { "ServerId": "i-xxxx |   |   |   |   |
|   |   |   |   |   |   |   | xxxxx", "Weight": "100", "Type |   |   |   |   |
|   |   |   |   |   |   |   | ": "ecs", "Port":"80","ServerT |   |   |   |   |
|   |   |   |   |   |   |   | ype":"Slave","Description":"te |   |   |   |   |
|   |   |   |   |   |   |   | st-112" }] |   |   |   |   |
|   |   |   |   |   |   |   | ENI: | [{ "ServerId": "eni-xxxxx |   |   |   |
|   |   |   |   |   |   |   | xxxx", "Weight": "100", "Type" |   |   |   |   |
|   |   |   |   |   |   |   | : "eni", "Port":"80","ServerTy |   |   |   |   |
|   |   |   |   |   |   |   | pe":"Master","Description":"te |   |   |   |   |
|   |   |   |   |   |   |   | st-112" }, { "ServerId": "eni- |   |   |   |   |
|   |   |   |   |   |   |   | xxxxxxxxx", "Weight": "100", " |   |   |   |   |
|   |   |   |   |   |   |   | Type": "eni", "ServerIp": "192 |   |   |   |   |
|   |   |   |   |   |   |   | .168.**.**", "Port":"80","Serv |   |   |   |   |
|   |   |   |   |   |   |   | erType":"Slave","Description": |   |   |   |   |
|   |   |   |   |   |   |   | "test-112" }] |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | [{ |   |
|   |   |   |   |   |   |   | "ServerId": "eni-xxxxxxxxx", " |   |   |   |   |

|   |   |   |   |   |   | Weight": "100", "Type": "eni", |   |
|---|---|---|---|---|---|---|---|
|   | Parameter | Type |   | Required | Example | Description |   |
|   |   |   |   |   |   | "ServerIp": "192.168.**.**", " |   |
|   |   |   |   |   |   | Port":"80","ServerType":"Maste |   |
|   |   |   |   |   |   | r","Description":"test-112" }, |   |
|   |   |   |   |   |   | { "ServerId": "eni-xxxxxxxxx", |   |
|   |   |   |   |   |   | "Weight": "100", "Type": "eni" |   |
|   |   |   |   |   |   | ,"ServerIp": "192.168.**.**", |   |
|   |   |   |   |   |   | "Port":"80","ServerType":"Slav |   |
|   |   |   |   |   |   | e","Description":"test-112" }] |   |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupId | String | rsp-cige6j**** | The ID of the primary/secondary server group. |
| MasterSlaveBac kendServers | Array of MasterSlaveBac kendServer |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveBac kendServer |   |   |   |
| ServerId | String | vm-2h**** | The ID of the ECS instance or ENI that is added. |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |
| ServerType | String | Slave | Indicates whether the backend server is a primary or secondary server. Valid values: Mast er and Slave. Default value: Master. |
| Description | String | Primary/SecondaryS erverGroupDescripti on. | The description of the primary/secondary server group. The description is 1 to 80 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores ( ). _ |
| Type | String | ecs | The type of backend server. Valid values: ecs (default): an ECS instance eni: an ENI |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=CreateMasterSlaveServerGroup &LoadBalancerId=lb-bp1hv944r69al4j**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateMasterSlaveServerGroupResponse>
      <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
      <MasterSlaveServerGroupId>rsp-cige******</MasterSlaveServerGroupId>
      <MasterSlaveBackendServers>
            <MasterSlaveBackendServers>
                  <ServerId>vm-gtgt***</ServerId>
                  <Port>80</Port>
                  <Weight>100</Weight>
                  <ServerType>Master</ServerType>
            </MasterSlaveBackendServers>
            <MasterSlaveBackendServers>
                  <ServerId>vm-tygtyg****</ServerId>
                  <Port>90</Port>
                  <Weight>100</Weight>
                  <ServerType>Slave</ServerType>
            </MasterSlaveBackendServers>
      </MasterSlaveBackendServers>
</CreateMasterSlaveServerGroupResponse>
```

`JSON` format `{`

```json
    "CreateMasterSlaveServerGroupResponse": {
        "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
        "MasterSlaveServerGroupId": "rsp-cige******",
        "MasterSlaveBackendServers": {
            "MasterSlaveBackendServers": [
```

`{`

```json
                    "ServerId": "vm-gtgt***",
                    "Port": 80,
                    "Weight": 100,
                    "ServerType": "Master"
```

`},` `{`

```json
                    "ServerId": "vm-tygtyg****",
                    "Port": 90,
                    "Weight": 100,
                    "ServerType": "Slave"
```

`}` `]` `}` `}` `}` Error codes

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | BACKEND SERVERS N _ _ UM MUST BE TWO _ _ _ | Backend servers num must be 2. | The error message returned because two backend servers must be specified. |
| 400 | BACKEND SERVERS H _ _ AVE SAME PORT AN _ _ _ D SERVERID _ | Backend servers have same port and serverId. | The error message returned because a backend server with the same port and ID is already specified in the server group. |
| 400 | BACKEND SERVERS C _ _ AN ONLY CONTAIN _ _ _ ONE MASTER AND O _ _ _ NE SLAVE _ | Backend servers can only contain one master and one slave. | The error message returned because a primary/secondary server group can contain only one primary server and one secondary server. |
| 400 | BACKEND SERVER ID _ _ CAN NOT EMPTY _ _ _ | Backend server id can not empty. | The error message returned because the ID of the backend server is not specified. |
| 400 | INVALID SERVER TYP _ _ E | Invalid server type. | The error message returned because the specified type of backend server is invalid. |
| 400 | BACKEND SERVER PO _ _ RT CAN NOT EMPTY _ _ _ | Backend server port can not empty. | The error message returned because the port of the backend server is not specified. |

| Developer Guid | e·API Reference |   | Server Load Balance |
|---|---|---|---|

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | RealServerPortNotSu pport | Real server port not support. | The error message returned because the specified port of the backend server is invalid. |

#### 2.9.2 DeleteMasterSlaveServerGroup

Deletes a specified primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMasterSlav eServerGroup | The operation that you want to perform. Set the value to Delet eMast erSlaveServerGroup. |
| MasterSlaveServe rGroupId | String | Yes | rsp-cige6**** | The ID of the primary/secondary server group. Not e You cannot delete a primary/secondary server group that is in use. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DeleteMasterSlaveServerGroup &MasterSlaveServerGroupId=rsp-cige6**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteMasterSlaveServerGroupResponse>
   <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
</DeleteMasterSlaveServerGroupResponse>
```

`JSON` format `{`

```json
"RequestId":"9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C"
```

`}`

#### 2.9.3 DescribeMasterSlaveServerGroups

Queries backend servers in a primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSl aveServerGroups | The operation that you want to perform. Set the value to DescribeMast erSlaveServerGroups. |
| LoadBalancerId | String | Yes | lb- bp14zi0n66zpg6 o**** | The ID of the Server Load Balancer (SLB) instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroups | Array of MasterSlaveSer verGroup |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveSer verGroup |   |   |   |
| MasterSlaveSer verGroupId | String | rsp-0bfuc**** | The ID of the primary/secondary server group. |

| Developer Guide·AP | I Reference |   | Server Load Balance |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupName | String | Group3 | The name of the primary/secondary server group. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroups &LoadBalancerId=lb-bp14zi0n66zpg6o**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMasterSlaveServerGroupsResponse>
      <RequestId>2631BB5E-B576-4925-BDED-07A66D23E5DE</RequestId>
      <MasterSlaveServerGroups>
     <MasterSlaveServerGroup>
        <MasterSlaveServerGroupId>rsp-bp1ro3mw******</MasterSlaveServerGroupId>
        <MasterSlaveServerGroupName>test</MasterSlaveServerGroupName>
     </MasterSlaveServerGroup>
      </MasterSlaveServerGroups>
</DescribeMasterSlaveServerGroupsResponse>
```

`JSON` format `{`

```json
    "RequestId": "265989FE-136B-4D6A-B549-FD40E7",
    "MasterSlaveServerGroups": {
        "MasterSlaveServerGroup": [
```

`{`

```json
                "MasterSlaveServerGroupId": "rsp-bp1nly******",
                "MasterSlaveServerGroupName": "primary/secondary1",
                "AssociatedObjects": {
                    "Listeners": {
                        "Listener": [ ]
```

`}` `}` `}` `]` `}` `}`

#### 2.9.4 DescribeMasterSlaveServerGroupAttribute

Queries detailed information about a primary/secondary server group. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMasterSl aveServerGroupA ttribute | The operation that you want to perform. Set the value to DescribeMast erSlaveServerGroupA t t ribut e. |
| MasterSlaveServe rGroupId | String | Yes | rsp-cige6j**** | The ID of the primary/secondary server group. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is created. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| MasterSlaveSer verGroupId | String | rsp-cige6**** | The ID of the primary/secondary server group. |
| MasterSlaveSer verGroupName | String | Group1 | The name of the primary/secondary server group. |
| MasterSlaveBac kendServers | Array of MasterSlaveBac kendServer |   | The list of backend servers in the primary/secondary server group. |
| MasterSlaveBac kendServer |   |   |   |
| ServerId | String | vm-hrf**** | The ID of the Elastic Compute Service (ECS) instance or elastic network interface (ENI). |
| Port | Integer | 90 | The port that is used by the backend server. |
| Weight | Integer | 100 | The weight of the backend server. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ServerType | String | Slave | The type of backend server. Valid values: Mast er and Slave. Default value: Master. |
| Description | String | Primary/SecondaryS erverGroupDescripti on. | The description of the primary/secondary server group. |
| Type | String | ecs | The type of backend server. Valid values: ecs: an ECS instance. This is the default value. eni: an ENI. |
| RequestId | String | 9DEC9C28-AB05- 4DDF-9A78- 6B08EC9CE18C | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeMasterSlaveServerGroupAttribute &MasterSlaveServerGroupId=rsp-cige6j**** &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeMasterSlaveServerGroupAttributeResponse>
    <RequestId>9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C</RequestId>
    <MasterSlaveServerGroupId>rsp-cige6******</MasterSlaveServerGroupId>
    <MasterSlaveBackendServers>
          <MasterSlaveBackendServers>
                <ServerId>vm-sshssh****</ServerId>
                <Port>80</Port>
                <Weight>100</Weight>
                <ServerType>Master</ServerType>
          </MasterSlaveBackendServers>
          <MasterSlaveBackendServers>
                <ServerId>vm-ffff*****</ServerId>
                <Port>90</Port>
                <Weight>100</Weight>
                <ServerType>Slave</ServerType>
          </MasterSlaveBackendServers>
    </MasterSlaveBackendServers>
</DescribeMasterSlaveServerGroupAttributeResponse>
```

`JSON` format `{`

```json
  "DescribeMasterSlaveServerGroupAttributeResponse": {
    "RequestId": "9DEC9C28-AB05-4DDF-9A78-6B08EC9CE18C",
    "MasterSlaveServerGroupId": "rsp-cige6******",
    "MasterSlaveBackendServers": {
      "MasterSlaveBackendServers": [
```

`{`

```json
          "ServerId": "vm-sshssh****",
          "Port": "80",
          "Weight": "100",
          "ServerType": "Master"
```

`},` `{`

```json
          "ServerId": "vm-ffff*****",
          "Port": "90",
          "Weight": "100",
          "ServerType": "Slave"
```

`}` `]` `}` `}` `}`

### 2.10 Tags

#### 2.10.1 AddTags

Adds tags to a Server Load Balancer (SLB) instance. When you call this operation, take note of the following items: You can add at most 10 tags to an SLB instance. You can specify at most five tags in each request. All tags and keys added to an SLB instance must be unique. If you add a tag that has the same key as an existing tag but with a different value, the new tag overwrites the existing tag. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddTags | The operation that you want to perform. Set the value to AddT ags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |

| Developer Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |
| Tags | String | Yes | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags to be added. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=AddTags &LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</AddTagsResponse>
```

`JSON` format `{`

```json
  "RequestId":"365F4154-92F6-4AE4-92F8-7FF34B540710"
```

`}`

#### 2.10.2 DescribeTags

Queries a list of tags. When you call this operation, take note of the following items: You can query tags by instance ID, tag key, and tag value. If the operation is successful, the system returns all tags that match the specified conditions. If the logical relationship among the specified conditions is `AND` , only tags that match all of the specified conditions are returned. If the Tagkey parameter is specified and the Tagvalue parameter is not specified, all tags that contain the specified tag key are returned. If you have specified the Tagvalue parameter in a request, you must also specify the Tagkey parameter in this request. If you specify both the Tagkey and Tagvalue parameters, tags with the specified key-value pair are returned. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTags | The operation that you want to perform. Set the value to DescribeT ags. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the Server Load Balancer (SLB) instance is deployed. |
| LoadBalancerId | String | No | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| Tags | String | No | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags to be queried. |
| DistinctKey | Boolean | No | false | Specifies whether the tag is DistinctKey. Valid values: t rue and f alse. |
| PageSize | Integer | No | 50 | The number of entries to return on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | No | 1 | The number of the page to return. Minimum value: 1. Default value: 1. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| TagSets | Array of TagSet |   | The list of tags. |
| TagSet |   |   |   |
| TagKey | String | test | The key of the tag. |
| TagValue | String | api | The value of the tag. |
| InstanceCount | Integer | 10 | The number of instances to which the tag is added. |
| PageSize | Integer | 50 | The number of entries returned on each page. Default value: 50. Maximum value: 100. |
| PageNumber | Integer | 1 | The number of the returned page. Minimum value: 1. Default value: 1. |
| TotalCount | Integer | 1 | The total number of instances that are returned after the tags are matched against the specified conditions. |
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTags &RegionId=cn-qingdao-env17-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
    <TagSets>
            <TagSet>
                  <TagKey>test</TagKey>
                  <TagValue>api</TagValue>
            </TagSet>
      </TagSets>
   <PageSize>50</PageSize>
   <PageNumber>1</PageNumber>
   <TotalCount>1</TotalCount>
</DescribeTagsResponse>
```

`JSON` format `{`

```json
    "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710",
    "TagSets": {
        "TagSet": [
```

`{`

```json
                "TagKey": "test",
                "TagValue": "api"
```

`}` `],`

```json
        "PageNumber": 1,
        "PageSize": 50,
        "TotalCount": 1
```

`}` `}`

#### 2.10.3 RemoveTags

Removes tags from a Server Load Balancer (SLB) instance. Request parameters

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveTags | The operation that you want to perform. Set the value to RemoveT ags. |
| LoadBalancerId | String | Yes | lb- bp1b6c719dfa08 ex**** | The ID of the SLB instance. |
| RegionId | String | Yes | cn-qingdao- env17-d01 | The ID of the region where the SLB instance is deployed. |

| Developer Guide·API | Reference |   |   | Server Load Balance |
|---|---|---|---|---|

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Tags | String | Yes | [{"TagKey":"Key1" ,"TagValue":"Val ue1"}, {"TagKey":"Key2", "TagValue":"Valu e2"}] | The list of tags that you want to remove. |

Response parameters

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 365F4154-92F6- 4AE4-92F8- 7FF34B540710 | The ID of the request. |

Examples Sample requests

```
http(s)://[Endpoint]/?Action=RemoveTags &LoadBalancerId=lb-bp1b6c719dfa08ex**** &RegionId=cn-qingdao-env17-d01 &Tags=[{"TagKey":"Key1","TagValue":"Value1"},{"TagKey":"Key2","TagValue":"Value2"}] &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RemoveTagsResponse>
   <RequestId>365F4154-92F6-4AE4-92F8-7FF34B540710</RequestId>
</RemoveTagsResponse>
```

`JSON` format

```json
{ "RequestId": "365F4154-92F6-4AE4-92F8-7FF34B540710" }
```

### 2.11 Error codes

|   | Error code |   |   |   | Error message |   |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|
|   | CertificateAndPriv |   |   |   | Certificate and |   |   |   | The error message returned because the certificate is used by other resources. |
|   |   |   |   |   |   | Certificate and |   |   | The |
|   |   | CertificateAndPriv |   |   |   | Certificate |   |   |   |
|   |   |   | ficateAndPriv |   | PrivateKey I |   |   |   |   |
|   |   |   |   |   |   |   |   | 40 |   |
|   | ateKeyIsRefered |   | sRefered |   |   |   |   |   |   |
|   |   |   |   |   | Refered. |   |   |   |   |

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code |   | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | CertificateNotMatc |   |   |   |   |   |   |   |   |   |   |   | Certificate and |   |   |   |   |   |   | The error message returned because the certificate and the private key do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Certificate and |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | CertificateNotMatc |   |   |   |   |   |   |   |   |   |   |   | Certifi |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ficateNotMatc |   |   |   |   |   |   | key does |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |   |
|   |   |   |   |   |   | hPrivateKey |   |   |   |   | eKey |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health- |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No health- |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ch |   |   | ecked Listener |   |   |   | The error message returne |   |
|   |   |   |   |   |   |   | CheckedListenerNot |   |   |   |   |   | enerNot |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | to |   |   |   |   | 404 |   | health c |   |
|   |   |   |   |   |   | Found |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | authorized to |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the |   |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified |   |   |   |   |   |   | you are unauthorized to per |   |
|   |   |   |   |   |   |   | Forbbiden.SubUser |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 403 |   | you are unauthori |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource as your |   |   |   |   |   |   | operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | account is |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | created by |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | another user. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   | The error message returned because you are unauthorized to perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | User not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | authorized to |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   | Forbidden |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operate on the |   |   |   |   | 403 |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | resource. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   | IncorrectListenerA |   |   |   |   |   |   |   |   |   |   |   | Current |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Current |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   | IncorrectList |   |   |   |   |   |   |   | enerA |   |   | listener access |   |   |   |   |   |   | The error message returned be |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the access control configuratio |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the access c |   |
|   |   |   |   |   |   |   | ccessControlStatusSt |   |   |   |   |   |   |   |   |   |   | co |   | ntrol status |   |   | 500 |   | the listener i |   |
|   |   |   |   |   |   | atus |   |   |   |   |   |   |   |   |   |   |   | does not support |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   | The error message returned because an internal error occurred. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing has |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message re |   |
|   |   |   |   |   |   |   | InternalError |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failed due to |   |   |   |   | 400 |   | an in |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backend service |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exception. |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processing has |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InternalInvokeErro |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | failed due to |   |   |   |   |   |   | The error message re |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 500 |   |   |   |
|   |   |   |   |   |   | r |   |   |   |   |   |   |   |   |   |   |   | some unknown |   |   |   |   |   |   | an int |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | error, exception |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or failure. |   |   |   |   |   |   |   |   |

|   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancer |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance's |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | addresstype is |   |   |   |   | the network types of the Elastic |   |
|   |   |   |   |   | InvalidBackendServ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | private, so it |   |   |   | 400 | Compute Service (ECS) instances |   |
|   |   |   |   | ers.Inconsistent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | forbidden to add |   |   |   |   | that of the S |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ecs vpc |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | backendservers |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | for now. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | All |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | BackendServers on |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned because you cannot specify both ECS |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | you cannot specify both ECS |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | one Specified |   |   |   |   | instances in a classic network and |   |
|   |   |   |   |   |   |   | InvalidBackendServ |   |   |   |   |   |   |   |   |   |   |   |   | instances in a classi |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | LoadBalancer h |   |   | ave | 400 | ECS instances in a vi |   |
|   |   |   |   | ers.Inconsistent |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | to be in the same |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc or all |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | classic |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   |   | The error message returned because you are unauthorized to perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | identity was not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   | InvalidIdentity | InvalidIdentity |   |   |   |   | entity |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | allowed |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | operated. |   |   |   |   |   |   |
|   |   |   |   | InvalidLoadBalance |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The error message returned because the specified SLB instance is invalid. |   |
|   |   |   |   |   | InvalidLoadBalance |   |   |   |   |   |   |   |   |   |   | LoadBala | ncerId |   | 404 |   |   |
|   |   |   |   | rId.NotF |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ound |   |   |   |   |   |   | does not exist. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the specified certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | format is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | error. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the certificate is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The |   |
|   |   |   |   |   | InvalidParameter |   |   |   | Parameter |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id is empty. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the ID of the server certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id is not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | support. |   |   |   |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the certificate and the private key are not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ServerCertificate |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | or Key is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | empty. |   |   |   |   |   |   |

|   |   |   |   |   | Error code |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified private key is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter key |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   | InvalidParameter | InvalidParameter | Parameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | format is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | error. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned because the specified region does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   | Specified |   | T |   |
|   |   |   |   |   |   | InvalidPara |   | meter |   | region does not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Port is not Integer. |   | 400 | The error message returned because the specified port is invalid. Valid values: 1 to 65535. |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   | 400 | The error message returned because the specified port is invalid. Valid values: 1 to 65535. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   | Invalid | Parameter |   |   | port is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified bandwidth limit is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | Th |   |
|   |   |   |   |   |   | Invalid | Parameter |   |   | bandwidth is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned because a specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | Specified |   | The |   |
|   |   |   |   |   |   | InvalidPara |   | meter |   | parameter Check |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of HealthCheckHttpCode is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | HealthCheckHttpCo |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | de is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth is not |   |   | the specified value of Band |   |
|   |   |   |   |   | InvalidParameter | InvalidParameter |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | valid, out of the |   |   | exceeds |   |
|   |   |   |   |   |   |   |   |   |   | instance total |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of Bandwidth is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error me |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | bandwidth is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |
|   |   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified health check configuration is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   | The specified |   | The error messa |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | HealthCheck is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |

|   | Port is not | 40 |
|---|---|---|
| Integer. |   |   |

|   |   |   |   | Error code |   |   |   |   | Error message |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error mess |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | SourceItem is not |   |   |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified protocol type is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | T |
|   |   |   |   |   | Invalid | Parameter |   |   | protocol is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 40 |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | RS Pool is empty. |   | 400 | The error message returned because no backend server is available. |
|   |   |   |   | InvalidParameter |   |   |   |   | RS Pool doesn't exist. |   | 400 | The error message returned because no backend server is available. |
|   |   |   |   | InvalidParameter |   |   |   |   | Illegal user ID. |   | 400 | The error message returned because the user ID is invalid. |
|   |   |   |   | InvalidParameter |   |   |   |   | User ID is null |   | 400 | The error message returned because the user ID is not specified. |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified type of SLB instance is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error m |
|   |   |   |   |   | Invalid | Parameter |   |   | parameter lb type _ |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of Mode is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error |
|   |   |   |   |   | Invalid | Parameter |   |   | parameter mode is |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | not valid.. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of AccessControlStatus is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   |   |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   | The erro |
|   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | AccessControlStat |   | 400 |   |
|   |   |   |   |   |   |   |   |   | us is not |   |   |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of SourceItem is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error messa |
|   |   |   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | SourceItems is |   |   |   |
|   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | The specified |   |   | The error message returned because the specified value of BackendServers is invalid. |
|   |   |   |   |   |   |   |   |   |   | The specified |   | The error message |
|   |   |   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   |   |   | 404 | th |
|   |   |   |   |   | InvalidParameter | Parameter |   |   |   |   | 404 |   |
|   |   |   |   |   |   |   |   |   | BackendServers is |   |   |   |
|   |   |   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   |   | InvalidParameter |   |   |   |   | Specified |   |   | The error message returned because a specified parameter is invalid. |
|   |   |   |   |   |   |   |   |   |   | Specified |   |   |
|   |   |   |   |   | InvalidPara |   | meter |   | parameter is not |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   |   |   | valid. |   |   |   |

|   | RS Pool is |
|---|---|
| empty. |   |

|   | RS Pool doesn't | 400 |
|---|---|---|
| exist. |   |   |

|   | Illegal user |
|---|---|
| ID. |   |

|   | User ID is |
|---|---|
| null |   |

|   |   |   | Error code |   |   |   | Error message |   | HTTP status code | Description |
|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of Domain is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error m |
|   |   |   |   | Invalid | Parameter |   | parameter Domain |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of URI is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The err |
|   |   |   |   | Invalid | Parameter |   | parameter URI is |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of Scheduler is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error me |
|   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | Scheduler is not |   |   |   |
|   |   |   |   |   |   |   | valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of ListenerStatus is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message |
|   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   | 400 | th |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ListenerStatus is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of PersistenceTimeout is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message return |
|   |   |   |   |   |   |   | parameter |   |   | The err |
|   |   |   |   |   |   |   |   |   | 400 | the spe |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | PersistenceTimeou |   |   |   |
|   |   |   |   |   |   |   | t is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of ConnectPort is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error messa |
|   |   |   |   |   |   |   | parameter |   |   |   |
|   |   |   |   |   |   |   |   |   | 400 |   |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ConnectPort is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of ConnectTimeout is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error messag |
|   |   |   |   |   |   |   | parameter |   |   | T |
|   |   |   |   |   |   |   |   |   | 400 | t |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | ConnectTimeou is |   |   |   |
|   |   |   |   |   |   |   | not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of StickySessionType is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message retu |
|   |   |   |   |   |   |   | parameter |   |   | The e |
|   |   |   |   |   |   |   |   |   | 400 | the s |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | StickySessionType |   |   |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of HealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message ret |
|   |   |   |   |   |   |   | parameter |   |   | The |
|   |   |   |   |   |   |   |   |   | 400 | the |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | HealthyThreshold |   |   |   |
|   |   |   |   |   |   |   | is not valid. |   |   |   |
|   |   |   | InvalidParameter |   |   |   | The specified |   |   | The error message returned because the specified value of UnhealthyThreshold is invalid. |
|   |   |   |   |   |   |   |   | The specified |   | The error message return |
|   |   |   |   |   |   |   | parameter |   |   | The err |
|   |   |   |   |   |   |   |   |   | 400 | the spe |
|   |   |   |   | InvalidParameter | Parameter |   |   |   | 400 |   |
|   |   |   |   |   |   |   | UnhealthyThreshol |   |   |   |
|   |   |   |   |   |   |   | d is not valid. |   |   |   |

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   | Error message |   |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of Interval is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error m |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 40 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Interval is not |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of XForwardedFor is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error messag |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | t |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | XForwardedFor is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of IsPublicAddress is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message r |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |   | Th |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 | the |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   | Parameter |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | IsPublicAddress |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidRegionId.No tFound |   |   |   |   |   |   |   |   | Specified region does not exist. |   |   |   |   | 404 | The error message returned because the specified region is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   | The error message returned because the ID of the backend server is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | serv |   |   |   | er ID is not |   | The error messag |   |
|   |   |   |   |   |   |   |   |   |   |   | rverId.Ma |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vali |   |   |   | d, flush | 400 |   |   |
|   |   |   |   |   |   | lformed |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | control ip chain |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | fail. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidServerId.No |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified backend server is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InvalidServerId.No |   |   |   |   |   |   |   |   | Th |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | ServerId.No |   |   |   |   | ser |   |   |   |   |   |   |   |
|   |   |   |   |   |   | tFound |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | found. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | InvalidWeight.Malf |   |   |   |   |   |   |   |   | A specified |   |   |   |   | 400 | The error message returned because the specified value of weight is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | A specified |   |   |   |   |   |   |
|   |   |   |   |   |   |   | InvalidWeight.Malf |   |   |   |   |   |   |   |   | A |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | ight.Malf |   |   |   | we |   |   |   |   |   |   |   |
|   |   |   |   |   |   | ormed |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | IpNotAvailable |   |   |   |   |   |   |   |   | The specified |   |   |   |   |   | The error message returned because the specified value of Address is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error m |   |
|   |   |   |   |   |   |   | IpNotAv |   |   | ailable |   |   |   |   | parameter Address |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | is not valid. |   |   |   |   |   |   |   |
|   |   |   |   |   |   | ListenerAlreadyExi |   |   |   |   |   |   |   |   | There is |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | There is |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | already a |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | Lis | tenerAlreadyExi |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener bound to |   |   |   |   | The error message retur |   |
|   |   |   |   |   |   | sts |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the port on the |   |   |   |   |   | the |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | specified load |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | balancer. |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to |   |   |   |   |   | The error message returned because the specified listener is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | No Listener to |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the specified |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 404 | The |   |
|   |   |   |   |   |   | ListenerNotFound | ListenerNotFound |   |   | rNotFound |   |   |   |   |   |   |   |   |   | 404 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port of the Load |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Balancer. |   |   |   |   |   |   |   |

| InvalidRegionId.No | Spe |
|---|---|

|   |   |   |   | Error code |   |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter Cookie |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned b |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   |   | the Cookie parameter is not |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   | 400 | the Cook |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | specified |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | BackendServerPort |   |   | The error message returned because |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   | 400 | the BackendServerPort param |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | not speci |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | LoadBalancerId |   |   | The error message returned because |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | that is mandatory |   | 400 | the LoadBalancerId paramete |   |
|   |   |   |   |   |   |   |   |   |   | for processing |   |   | specified |   |
|   |   |   |   |   |   |   |   |   |   | this request is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | not supplied. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | RegionId that is |   |   | The error message returned because |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | mandatory for |   | 400 | the RegionId param |   |
|   |   |   |   |   |   |   |   |   |   | processing this |   |   | spec |   |
|   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | supplied. |   |   |   |   |
|   |   |   |   | MissingParameter |   |   |   |   |   | The combination |   |   | The error message returned because a required parameter is not specified. |   |
|   |   |   |   |   |   |   |   |   |   |   | The combination |   |   |   |
|   |   |   |   |   |   |   |   |   |   | of some |   |   |   |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameters |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   | violates the |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | spec. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | The input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | The input |   |   |   |
|   |   |   |   |   |   |   |   |   |   | parameter |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | OwnerId,OwnerAcco |   |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned beca |   |
|   |   |   |   |   |   |   |   |   |   | unt that is |   |   | OwnerAccount and OwnerId are n |   |
|   |   |   |   |   | MissingParameter |   |   |   |   |   |   | 403 | OwnerAccount and |   |
|   |   |   |   |   |   |   |   |   |   | mandatory for |   |   | specified. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | spec |   |
|   |   |   |   |   |   |   |   |   |   | processing this |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | request is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | supplied. |   |   |   |   |
|   |   |   |   | PrivateKeyEncrypti on |   |   |   |   |   | Key has Encrypted . |   | 400 | The error message returned because the private key is encrypted. |   |

| PrivateKeyEncrypti |   |   | Key has | 4 |
|---|---|---|---|---|

|   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   |   | Error message |   |   |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | ProcessingSameRequ |   |   |   |   |   |   |   |   |   |   |   |   | The same |   |   |   |   | The error message returned because the same request is being processed. Try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The same |   |   |   | The error message ret |   |
|   |   |   |   |   |   |   |   | ProcessingSa |   |   |   |   |   |   |   | meRequ |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | request is being |   |   | 400 | the same |   |
|   |   |   |   |   |   | est |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | processed. Please |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | try later. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServerCertificateI |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   | The error message returned because the specified certificate is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Specified |   |   |   |   |   |
|   |   |   |   |   |   |   |   | ServerCerti |   |   |   |   |   |   | ficateI |   |   |   | ServerCe |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | rtificate | 404 |   |   |
|   |   |   |   |   |   | d.NotFound |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Id does not |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exist. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The request has |   |   |   |   | The error message returned because the service is unavailable. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The request has |   |   |   |   |   |
|   |   |   |   |   |   |   |   | Servic |   |   |   | eUnavailable |   |   |   |   |   |   | failed due to a |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 | The error mes |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | temporary failure |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | of the server. |   |   |   |   |   |   |
|   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because the specified name already exists. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The error mes |   |
|   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   | loadbalancer name |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has been used. |   |   |   |   |   |   |
|   |   |   |   |   |   | TcpNotSupportForHy |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   | The error message returned because you cannot create TCP listeners. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Hybrid type |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loa |   | dbalancer |   |   | The error m |   |
|   |   |   |   |   |   |   |   | TcpNotSupportForHy |   |   |   |   |   | ortForHy |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doe |   |   |   | 400 |   |   |
|   |   |   |   |   |   | bridLb | bridLb |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | TCP type |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listener. |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number of input |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message returned |   |
|   |   |   |   |   |   |   |   | TooManyBackendServ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | real servers |   |   | 400 | you canno |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | ers |   |   |   |   |   |   |   |   |   |   |   |   | exceeds max |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported number: |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 20. |   |   |   |   |   |   |
|   |   |   |   |   |   | TooManyBackendServ |   |   |   |   |   |   |   |   |   |   |   |   | The backend |   |   |   |   | The error message returned because the number of backend servers exceeds the limit. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The backend |   |   |   | The error messag |   |
|   |   |   |   |   |   |   |   | TooManyBac |   |   |   |   |   | kendServ |   |   |   |   |   |   |   |   |   | T |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | server parameter |   |   | 400 | th |   |
|   |   |   |   |   |   | ers |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 4 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | has too many |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | entries. |   |   |   |   |   |   |
|   |   |   |   |   |   | UnsupportedOperati on |   |   |   |   |   |   |   |   |   |   |   |   | The |   |   |   |   | The error message returned because the specified type of SLB instance does not support the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The |   |   |   | The error mes |   |
|   |   |   |   |   |   |   |   | UnsupportedOperat |   |   |   |   |   |   |   |   | i |   |   |   |   |   |   | The erro |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Loadbalancer |   |   | 400 | the spe |   |
|   |   |   |   |   |   | on |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doesn't support |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this function. |   |   |   |   |   |   |
|   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   | The error message returned because you cannot perform the operation. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   | The |   |
|   |   |   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   | rtedOperati |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   | on |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | supported. |   |   |   |   |   |   |

|   |   |   |   |   |   |   | Error code |   |   |   |   |   |   |   |   |   |   |   |   | Error message |   | HTTP status code | Description |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | port has been |   |   |   |   |
|   |   |   |   |   |   |   |   |   | UnsupportedOperati |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | assigned one type |   |   | The error message returned because |   |
|   |   |   |   |   |   |   | ononfixedprotocalpor |   |   |   |   |   |   |   |   |   |   |   |   | of protocal, and |   | 400 | the protocol of the specified |   |
|   |   |   |   |   |   |   | t |   |   |   |   |   |   |   |   |   |   |   |   | this protocal |   |   | does not s |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | doesn't support |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | this operation. |   |   |   |   |
|   |   |   |   |   |   |   | UnsupportedParamet |   |   |   |   |   |   |   |   |   |   |   |   | The input |   |   | The error message returned because a specified parameter is invalid. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The input |   | The e |   |
|   |   |   |   |   |   |   |   |   | UnsupportedParamet |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Paramet |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   | er |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | unsupported. |   |   |   |   |
|   |   |   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   |   |   |   |   |   |   |   | The vip |   |   | The error message returned because the protocol type of the listener and the protocol type of the backend server do not match. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The vip |   | The err |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | protocol is not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   | VipNotMatchRspool |   |   |   |   |   |   | pool |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | match with |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Rspool. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   | The error message returned because you cannot add more than 50 listeners in each call. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The total |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number of input |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error message return |   |
|   |   |   |   |   |   |   |   |   | VipTooManyListener |   |   |   |   |   | istener |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | listeners exceeds |   | 400 | you can |   |
|   |   |   |   |   |   |   | s |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | max supported |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | number: 50. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified resource does not exist. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | The |   |
|   |   |   |   |   |   |   |   |   | Invalid |   |   |   |   | Parameter |   |   |   |   |   | resource does not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | exist. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified instance is being configured. Try again later. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | loadbalancer is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The error me |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   | Unavailable |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | configuring, |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | please retry |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | later. |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Obtain Ip Fail, |   | The error message returned because |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | please make sure |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the system fails to obtai |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   | ceUnavailable |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | the ECS exists |   | 503 | addr |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | and the status is |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | running. |   |   |   |   |
|   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified region does not support VPCs. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   | Th |   |
|   |   |   |   |   |   |   |   |   | ServiceUnavailable |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   | Unavailable |   |   |   |   |   | region not |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 503 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | support VPC. |   |   |   |   |
|   |   |   |   |   |   |   | InvalidParameter |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   | The error message returned because the specified VPC is deleted. |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | The specified |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | vpc cloud |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 400 |   |   |
|   |   |   |   |   |   |   |   |   | InvalidParameter |   |   |   |   | Parameter |   |   |   |   |   |   |   | 4 |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | instance has |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | deleted. |   |   |   |   |
